#!/usr/bin/env python3
"""
render_cv.py — Converte um curriculo.md adaptado em HTML + PDF no padrão ATS.

Estilo espelha CV-Andre-Rajo-Backend-Senior-{BR,ES}-ATS.pdf:
- Preto/branco (sem cores)
- Helvetica/Arial, 10pt
- Section headers MAIÚSCULOS com linha horizontal
- Sem caixas, sem colunas, sem ícones
- Layout simples, focado em palavra-chave, parseável por ATS

Uso:
    python3 render_cv.py path/to/curriculo.md
    # gera curriculo.html e curriculo.pdf no mesmo diretório
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from weasyprint import HTML


# ---------- markdown -> html ----------

def md_inline(text: str) -> str:
    """Converte inline markdown: **bold**, *italic*, [link](url), `code`."""
    text = re.sub(r"\\\*", "\x00", text)  # protege *
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    text = text.replace("\x00", "*")
    return text


def md_to_html(md: str) -> str:
    """Converte markdown de currículo em HTML semântico simples."""
    lines = md.splitlines()
    html_parts: list[str] = []

    in_ul = False
    in_table = False
    in_header = True
    header_buffer: list[str] = []

    def close_ul():
        nonlocal in_ul
        if in_ul:
            html_parts.append("</ul>")
            in_ul = False

    def close_table():
        nonlocal in_table
        if in_table:
            html_parts.append("</tbody></table>")
            in_table = False

    def flush_header():
        """Renderiza o bloco do topo (nome, subtítulo, contato, resumo)."""
        nonlocal in_header
        if not header_buffer:
            return
        # Espera: # Nome / **Subtitle** / contato linha 1 / contato linha 2 / --- / resumo (1+ paras)
        idx = 0
        # nome
        if idx < len(header_buffer) and header_buffer[idx].startswith("# "):
            html_parts.append(f'<h1>{md_inline(header_buffer[idx][2:].strip())}</h1>')
            idx += 1
        # subtitle (em **...** ou linha qualquer não vazia até linha de contato)
        if idx < len(header_buffer):
            sub = header_buffer[idx].strip()
            if sub.startswith("**") and sub.endswith("**"):
                html_parts.append(f'<div class="subtitle">{md_inline(sub.strip("*"))}</div>')
                idx += 1
            elif sub:
                # subtitle não-bold
                html_parts.append(f'<div class="subtitle">{md_inline(sub)}</div>')
                idx += 1
        # linhas de contato (até encontrar separador ---)
        contact_lines: list[str] = []
        while idx < len(header_buffer):
            line = header_buffer[idx].strip()
            if line.startswith("---"):
                idx += 1
                break
            if line:
                contact_lines.append(md_inline(line))
            idx += 1
        for cl in contact_lines:
            html_parts.append(f'<div class="contact">{cl}</div>')
        # resumo: tudo até o fim do header
        summary_paras: list[str] = []
        buf: list[str] = []
        while idx < len(header_buffer):
            line = header_buffer[idx]
            if line.strip() == "":
                if buf:
                    summary_paras.append(" ".join(buf))
                    buf = []
            else:
                buf.append(line.strip())
            idx += 1
        if buf:
            summary_paras.append(" ".join(buf))
        for p in summary_paras:
            html_parts.append(f'<p class="summary">{md_inline(p)}</p>')
        header_buffer.clear()
        in_header = False

    # primeiro: separar header (até o primeiro ##) do resto
    body_start = len(lines)
    for i, line in enumerate(lines):
        if line.startswith("## "):
            body_start = i
            break
    header_buffer.extend(lines[:body_start])
    flush_header()

    # processar o resto
    i = body_start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # section header
        if line.startswith("## "):
            close_ul()
            close_table()
            html_parts.append(f'<h2>{md_inline(line[3:].strip())}</h2>')
            i += 1
            continue

        # job header (### Cargo · Empresa — período)
        if line.startswith("### "):
            close_ul()
            close_table()
            html_parts.append(f'<h3>{md_inline(line[4:].strip())}</h3>')
            i += 1
            continue

        # italic single-line descrição (job-desc)
        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            close_ul()
            close_table()
            text = stripped.strip("*").strip()
            html_parts.append(f'<p class="job-desc">{md_inline(text)}</p>')
            i += 1
            continue

        # tabela markdown (linha começa com | e próxima é separator |---)
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-\|:]+\|\s*$", lines[i + 1].strip()):
            close_ul()
            close_table()
            # parse header
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            html_parts.append('<table class="kv"><thead><tr>')
            for c in header_cells:
                html_parts.append(f"<th>{md_inline(c)}</th>")
            html_parts.append("</tr></thead><tbody>")
            in_table = True
            i += 2  # pula header + separator
            while i < len(lines) and lines[i].strip().startswith("|"):
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                html_parts.append("<tr>")
                for c in row_cells:
                    html_parts.append(f"<td>{md_inline(c)}</td>")
                html_parts.append("</tr>")
                i += 1
            continue

        # bullet list item
        if stripped.startswith("- "):
            if not in_ul:
                close_table()
                html_parts.append("<ul>")
                in_ul = True
            item = stripped[2:]
            # Pode ter sub-bullets indentados (com 2 espaços) — junta como continuação
            sub: list[str] = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.startswith("  - "):
                    sub.append(nxt.strip()[2:])
                    j += 1
                else:
                    break
            if sub:
                html_parts.append(f'<li>{md_inline(item)}<ul>')
                for s in sub:
                    html_parts.append(f"<li>{md_inline(s)}</li>")
                html_parts.append("</ul></li>")
                i = j
            else:
                html_parts.append(f"<li>{md_inline(item)}</li>")
                i += 1
            continue

        # stack: linha começando com "Stack:"
        if stripped.startswith("Stack:"):
            close_ul()
            close_table()
            html_parts.append(f'<p class="stack"><em>{md_inline(stripped)}</em></p>')
            i += 1
            continue

        # separador horizontal --- (ignora silenciosamente)
        if stripped.startswith("---"):
            close_ul()
            close_table()
            i += 1
            continue

        # parágrafo regular (skills section: **Linguagens:** ...)
        if stripped and not stripped.startswith("#"):
            close_ul()
            close_table()
            html_parts.append(f"<p>{md_inline(stripped)}</p>")
            i += 1
            continue

        # linha em branco ou desconhecida
        i += 1

    close_ul()
    close_table()

    return "\n".join(html_parts)


# ---------- CSS ATS ----------

CSS = r"""
@page {
  size: A4;
  margin: 14mm 14mm 12mm 14mm;
}
* { box-sizing: border-box; }
body {
  font-family: "Helvetica", "Arial", sans-serif;
  font-size: 10pt;
  line-height: 1.35;
  color: #000;
  margin: 0;
}
h1 {
  font-size: 19pt;
  font-weight: 700;
  margin: 0 0 2px 0;
}
.subtitle {
  font-size: 11pt;
  margin-bottom: 4px;
}
.contact {
  font-size: 9.5pt;
  margin: 0;
}
.summary {
  margin: 8px 0 0 0;
  text-align: justify;
}
h2 {
  font-size: 11pt;
  font-weight: 700;
  text-transform: uppercase;
  border-bottom: 1px solid #000;
  padding-bottom: 2px;
  margin: 14px 0 6px 0;
  letter-spacing: 0.3px;
}
h3 {
  font-size: 10.5pt;
  font-weight: 700;
  margin: 8px 0 2px 0;
}
.job-desc {
  font-style: italic;
  margin: 0 0 3px 0;
  font-size: 10pt;
}
ul {
  margin: 2px 0 4px 0;
  padding-left: 18px;
}
li {
  margin-bottom: 3px;
  text-align: justify;
}
li ul {
  margin: 2px 0 0 0;
  padding-left: 18px;
}
.stack {
  margin: 3px 0 4px 0;
  font-size: 10pt;
}
p {
  margin: 2px 0;
}
strong { font-weight: 700; }
em { font-style: italic; }
a { color: #000; text-decoration: none; }
table.kv {
  width: 100%;
  border-collapse: collapse;
  margin: 4px 0;
  font-size: 9.5pt;
}
table.kv th, table.kv td {
  border: 1px solid #000;
  padding: 4px 6px;
  text-align: left;
  vertical-align: top;
}
table.kv th {
  font-weight: 700;
  background: #fff;
}
"""


def build_html(body_html: str, title: str = "Currículo") -> str:
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{body_html}
</body>
</html>
"""


def render(md_path: Path) -> tuple[Path, Path]:
    md = md_path.read_text(encoding="utf-8")
    body = md_to_html(md)
    # extrai nome da pasta para o title
    title = md_path.parent.name
    html = build_html(body, title=title)
    html_path = md_path.with_suffix(".html")
    pdf_path = md_path.with_suffix(".pdf")
    html_path.write_text(html, encoding="utf-8")
    HTML(string=html, base_url=str(md_path.parent)).write_pdf(str(pdf_path))
    return html_path, pdf_path


def main() -> int:
    if len(sys.argv) < 2:
        print("uso: render_cv.py path/to/curriculo.md [outro.md ...]", file=sys.stderr)
        return 1
    rc = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        if not p.exists():
            print(f"[skip] {p}: não existe", file=sys.stderr)
            rc = 1
            continue
        try:
            html_path, pdf_path = render(p)
            print(f"[ok]   {p} -> {pdf_path.name}")
        except Exception as e:
            print(f"[fail] {p}: {e}", file=sys.stderr)
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
