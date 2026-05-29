# dog-crazy-os

> Seu co-piloto de carreira no Claude Code. Candidaturas, prospecção, prep de entrevista e conteúdo — tudo em comandos.

Procurar emprego virou um segundo trabalho. Você adapta currículo, faz cadastro infinito, estuda empresa, treina resposta — e muitas vezes recebe em troca o silêncio.

O **dog-crazy-os** automatiza a parte mecânica pra você focar no que importa: se apresentar bem e tomar decisões certas.

---

## O que ele faz

| Comando | O que faz |
|---|---|
| `/install` | Configura o sistema: preenche seu perfil, ICP e voz |
| `/aplicar` | Candidatura completa: adapta CV, escreve mensagem do canal (email/DM/form), salva tudo organizado |
| `/prospectar` | Encontra empresas-alvo e escreve abordagens PJ/freela personalizadas |
| `/curriculo` | Adapta seu CV base às palavras-chave de uma vaga específica |
| `/conteudo` | Gera posts LinkedIn e Instagram na sua voz |
| `/conversa` | Analisa print de conversa (LinkedIn, WhatsApp) e diz o próximo passo |
| `/entrevista` | Prep de entrevista técnica: perguntas em escada do básico ao framework, com feedback por resposta |
| `/feedback-entrevista` | Analisa transcrição de entrevista e dá diagnóstico crítico + 3 ajustes pra próxima |
| `/check` | Check de energia antes de começar o dia — calibra o que faz sentido fazer hoje |

---

## Pré-requisitos

1. **Claude Code** — extensão do VS Code ou CLI ([claude.ai/code](https://claude.ai/code))
2. **Assinatura Claude Pro** (a partir de US$20/mês) — o plano gratuito não dá acesso ao Claude Code
3. **Python 3** — para o gerador de PDF do currículo (`render_cv.py`)
4. **wkhtmltopdf** — para renderizar o PDF ([download](https://wkhtmltopdf.org/downloads.html))

---

## Instalação

```bash
# 1. Clone o repo
git clone https://github.com/seu-usuario/dog-crazy-os.git
cd dog-crazy-os

# 2. Abra no VS Code
code .

# 3. No Claude Code, rode o install
/install
```

O `/install` vai te entrevistar e preencher os arquivos em `_contexto/` — que ficam no `.gitignore` (seus dados não vão pro repo).

---

## Estrutura

```
dog-crazy-os/
├── .claude/
│   ├── commands/          # Comandos do sistema
│   ├── skills/            # Skills de prospecção e agente principal
│   └── scripts/           # Gerador de PDF ATS
├── _contexto/             # Seu perfil (gerado pelo /install, no .gitignore)
│   ├── *.md.template      # Templates para novos usuários
├── vagas/                 # Candidaturas organizadas por data
├── prospeccao/            # Leads e abordagens enviadas
├── conteudo/              # Posts gerados
├── conversas/             # Análises de conversa
└── marca/                 # Assets de marca pessoal
```

---

## Como funciona o fluxo

```
1. /install       → preenche perfil, ICP e voz
2. /prospectar    → encontra empresas-alvo e escreve abordagens
3. /aplicar       → candidatura completa para cada vaga
4. /check         → calibra o dia antes de começar
5. /entrevista    → quando uma vaga avança para entrevista técnica
6. /feedback-entrevista → depois da entrevista, com a transcrição
```

---

## Contribuindo

PRs são bem-vindos. O que mais ajuda:
- Novos templates de mensagem (outros idiomas, outros setores)
- Melhorias no gerador de PDF
- Novos comandos (`/negociar`, `/follow-up`, `/pipeline`)
- Traduções do COMECE-AQUI.md

Antes de abrir PR, rode `/install` num contexto limpo e teste o fluxo completo.

---

## Licença

MIT — use, adapte e distribua livremente.
