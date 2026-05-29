---
description: Adapta seu currículo-base às palavras-chave de uma vaga específica (otimizado para ATS)
---

# /curriculo — Currículo por palavra-chave

## Fluxo

1. **LEIA o currículo-base** antes de qualquer coisa:
   - `_contexto/curriculo-base.md` (PT) — se a vaga for em pt-BR
   - `_contexto/curriculo-base-es.md` (ES) — se a vaga for em espanhol
   - O `.pdf` no mesmo lugar mostra o visual final esperado (referência ATS).
   - Leia também `_contexto/perfil.md` para provas, números e contexto pessoal.

2. **Peça a vaga:** descrição/anúncio (texto, link ou print).

3. **Extraia palavras-chave** que o anúncio repete — stack, ferramentas, soft
   skills, responsabilidades. São o que o ATS procura.

4. **Reescreva o currículo mantendo IDÊNTICA a estrutura do base.** Esta é a
   regra mais importante: o output tem que ser parseável pelo
   `.claude/scripts/render_cv.py` e visualmente fiel ao PDF base.

   **Estrutura obrigatória, na ordem:**

   ```
   # Nome
   **Subtítulo (cargo · stacks-chave)**
   Linha-de-contato-1
   Linha-de-contato-2
   ---
   Parágrafo de resumo (3–5 linhas, denso)

   ## EXPERIÊNCIA PROFISSIONAL
   ### Cargo · Empresa (regime) — período
   *Descrição-do-papel em italic, uma linha.*
   - **Projeto/Cliente** — descrição com palavras-chave em **bold**.
   - **Projeto/Cliente** — ...
   Stack: tech1, tech2, tech3...

   (repete por empresa, ORDEM CRONOLÓGICA REVERSA — mais recente primeiro)

   ## HABILIDADES TÉCNICAS
   **Categoria:** item1, item2, item3
   **Categoria:** ...

   ## FORMAÇÃO
   - **Curso** — Instituição · ano

   ## IDIOMAS & CERTIFICAÇÕES
   - Idioma1 (nível) · Idioma2 (nível) · ...
   - Certificação (se houver)

   ## INFORMAÇÕES ADICIONAIS
   - **CNPJ:** 63.162.149/0001-97
   - **Razão social:** RAJO TECH — Consultoria em Tecnologia da Informação
   ```

   (Em ES: `## INFORMACIÓN ADICIONAL` com `Razón social` em vez de `Razão social`.)

   **NÃO crie seções fora dessa lista** (sem "Stack técnica" antes da
   experiência, sem "Provas alinhadas à vaga", sem tabelas de match — esse tipo
   de seção quebra o ATS e o renderer).

   **NÃO transforme projetos em jobs separados.** Cada empresa é UM `### `;
   projetos da mesma empresa são bullets dentro dela.

   **Manter ordem cronológica reversa** (RajoTech → Sensedia → 4all → Sistema
   Campeão). Pode-se reordenar projetos DENTRO de uma empresa pra destacar o
   mais relevante, mas a ordem das empresas é fixa.

5. **Salve** o `curriculo.md` em
   `vagas/curriculos-gerados/[YYYY-MM-DD]/[empresa-cargo]/`, onde `YYYY-MM-DD`
   é a data de hoje (use a data do sistema; se indisponível, pergunte em 1 linha).

6. **Gere o PDF ATS** rodando (do diretório raiz do projeto):
   `python3 .claude/scripts/render_cv.py vagas/curriculos-gerados/[YYYY-MM-DD]/[pasta]/curriculo.md`
   (produz `curriculo.html` + `curriculo.pdf` no padrão ATS preto/branco).

7. **Verifique o PDF gerado** com `pdfinfo` — espera-se 1–2 páginas. Se passar
   de 2, encurte projetos antigos. Se a estrutura saiu errada, **NÃO mexa no
   script** — corrija o `curriculo.md` pra bater com o formato.

8. **Aponte o gap:** liste o que a vaga pede e a pessoa não tem, para ela
   decidir se vale candidatar ou onde se desenvolver.

## Regras

- **NUNCA invente** experiência, diploma ou competência. Espelhar vocabulário
  da vaga é honesto; mentir queima reputação.
- **Estrutura é sagrada** — copie do base, não invente seções.
- **Cronologia é sagrada** — empresas em ordem reversa, sempre.
- Se a vaga for em ES, use `curriculo-base-es.md` como referência e escreva em ES.
