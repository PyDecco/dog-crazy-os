# dog-crazy-os

Sistema para vender sua mão de obra (PJ, freela pontual, projetos) e construir
autoridade no LinkedIn e Instagram — usando Claude Code como co-piloto.

## Como o Claude deve operar aqui
- SEMPRE leia `_contexto/` (perfil.md, icp.md, voz.md) antes de qualquer tarefa.
- Se `_contexto/perfil.md` não existir, oriente o usuário a rodar `/install` antes de qualquer outro comando.
- Use os comandos em `.claude/commands/` e as skills em `.claude/skills/`.
- Salve saídas nas pastas certas: `prospeccao/`, `vagas/`, `conteudo/`, `conversas/`.
- Nunca invente resultados, experiência ou clientes. Credibilidade é o ativo do usuário.

## Comandos
- `/install` — configura o sistema: entrevista o usuário e preenche o contexto (`_contexto/`)
- `/aplicar` — candidatura completa em 1 comando: detecta canal (gmail/form/dm), adapta CV, escreve mensagem do canal, salva pacote pronto
- `/prospectar` — encontra empresas e escreve abordagens PJ/freela
- `/curriculo` — só adapta o CV às palavras-chave (subset do `/aplicar`, mantido pra uso isolado)
- `/conteudo` — gera posts para LinkedIn e Instagram
- `/conversa` — analisa print de conversa e indica o próximo passo
- `/entrevista` — prep de entrevista técnica de uma vaga ativa: perguntas em escada (básico→framework), sessão interativa com feedback por resposta, relatório final de lacunas
- `/feedback-entrevista` — analisa transcrição de entrevista (entrevistador + dev) e devolve diagnóstico crítico: domínio técnico, comunicação, sinal ao entrevistador, veredicto e 3 ajustes pra próxima
- `/check` — check de energia antes de começar o dia: calibra o que faz sentido fazer hoje com base em como você está

## Primeira vez? Rode `/install`.
