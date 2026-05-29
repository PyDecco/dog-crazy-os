---
description: Encontra empresas-alvo e escreve abordagens de prospecção PJ/freela personalizadas
---

# /prospectar — Prospecção PJ/freela

Antes de tudo, leia `_contexto/perfil.md`, `_contexto/icp.md` e `_contexto/voz.md`.
Se o ICP ou as provas de resultado estiverem vazios, peça à pessoa para rodar
`/install` ou preencher — abordagem genérica não converte.

## Fluxo
1. **Alvo:** confirme o tipo de empresa, região e dor a partir do ICP. Aceite
   ajustes pontuais ("hoje quero focar em fintechs do México").
2. **Encontrar empresas:** use busca na web para achar empresas que batem com o
   ICP (rodadas recentes, vagas abertas na área, diretórios de aceleradoras).
   Para cada uma, ache o decisor (cargo do ICP) e um gancho real e específico.
3. **Registrar:** salve/atualize a lista em `prospeccao/leads/leads.csv` com:
   empresa, contato, cargo, canal, gancho, status, ultimo_toque, proximo_passo.
4. **Escrever a abordagem:** use os modelos da skill `prospeccao` (em
   `.claude/skills/prospeccao/`). Personalize a 1ª linha com o gancho real,
   fale da dor DELES, use UMA prova do perfil, CTA leve. Salve em
   `prospeccao/enviados/`. Para mensagem final, use a ferramenta de composição
   se disponível, oferecendo variantes de abordagem.
5. **Follow-up:** lembre a pessoa de que a maioria das respostas vem do 2º/3º
   toque. Quando o lead responder, encaminhe para `/conversa`.

## Regras
- Prospecção 1:1 personalizada. Nada de lista comprada ou disparo em massa —
  queima domínio e converte mal.
- Internacional: escreva no idioma do destinatário e ajuste preço à moeda dele.
- Nunca invente resultados ou clientes.
