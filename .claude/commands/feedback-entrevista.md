---
description: Analisa a transcrição de uma entrevista técnica (entrevistador + dev) e dá feedback crítico sobre desempenho, comunicação e lacunas
---

# /feedback-entrevista — Feedback de entrevista por transcrição

Recebe a transcrição de uma entrevista técnica e devolve um diagnóstico crítico e honesto:
o que foi bem, o que foi fraco, o que o entrevistador provavelmente anotou, e o que mudar
na próxima.

## Inputs aceitos
- Transcrição colada diretamente no chat (texto livre, pode ser bagunçado)
- Arquivo de transcrição (qualquer formato — o sistema lê e normaliza)
- Transcrição gerada por ferramenta de reunião (Google Meet, Zoom, Teams — cole o texto)
- Contexto extra opcional: "era entrevista técnica de NestJS pra startup de fintech", "o entrevistador parecia sênior"

## Fluxo

### 1. Leia o contexto obrigatoriamente
- `_contexto/perfil.md` — stack do usuário, pontos fortes declarados, seniority
- Se o usuário informar a empresa/vaga, leia também a `vaga.md` da candidatura correspondente

### 2. Normalize a transcrição
Identifique os falantes e normalize pra formato legível:
```
[Entrevistador]: ...
[Dev]: ...
```
Se os nomes não estiverem claros, infira pelo contexto (quem faz perguntas = entrevistador).
Se não for possível inferir, pergunte uma linha antes de continuar.

### 3. Analise em 5 dimensões

**A — Domínio técnico**
- As respostas estavam corretas? Completas? Imprecisas?
- Onde você foi além do esperado (ponto positivo real)
- Onde respondeu superficialmente quando o nível da vaga pedia profundidade
- Onde errou conceitualmente — corrija com a resposta esperada por um sênior

**B — Comunicação e clareza**
- As respostas foram diretas ou enroladas?
- Usou jargão sem explicar? Ou explicou demais o óbvio?
- Teve momento de "não sei" bem gerenciado (honestidade técnica) ou mal gerenciado (travar/inventar)?
- Pausas longas, respostas muito curtas, ou falas que provavelmente confundiram o entrevistador

**C — Sinal que passou ao entrevistador**
- O que o entrevistador provavelmente anotou de positivo
- O que provavelmente gerou dúvida ou bandeira vermelha
- Se houve pergunta de fit cultural ou soft skill, como foi a resposta

**D — Gestão de perguntas difíceis**
- Como você lidou com o que não sabia: admitiu, chutou, ou desviou?
- Fez perguntas inteligentes ao entrevistador? (ausência de perguntas também é sinal)
- Aproveitou momentos pra ancorar provas reais do perfil?

**E — Energia e presença**
- O tom foi seguro, ansioso, defensivo, ou excessivamente informal?
- Houve momento de virada (começou travado e ganhou ritmo, ou vice-versa)?
- Alguma resposta que soa bem no papel mas provavelmente não funcionou ao vivo?

### 4. Veredicto final

Dê um veredicto direto — sem rodeios:

```
Veredicto: [PASSOU / RISCO DE REJEIÇÃO / PROVAVELMENTE RECUSADO]
Motivo em 1 linha: ...
```

Não especule se não tiver base na transcrição. Se não der pra saber, diga isso.

### 5. Os 3 ajustes mais importantes pra próxima entrevista

Priorize por impacto. Não liste 10 coisas. Liste 3, com instrução concreta:

```
1. [O que mudar]: [Como mudar em termos práticos]
2. ...
3. ...
```

### 6. Salve o relatório

Salve em `vagas/candidaturas/[pasta-da-vaga]/feedback-entrevista-[YYYY-MM-DD].md`
(se a vaga não for identificada, salve em `vagas/feedbacks/feedback-[YYYY-MM-DD].md`).

Estrutura do arquivo:
```md
# Feedback de entrevista — [Empresa ou "sem vaga identificada"] | [Data]

## Transcrição normalizada
[transcrição formatada]

## Análise por dimensão
### A — Domínio técnico
...
### B — Comunicação e clareza
...
### C — Sinal ao entrevistador
...
### D — Gestão de perguntas difíceis
...
### E — Energia e presença
...

## Veredicto
...

## 3 ajustes pra próxima
1. ...
2. ...
3. ...
```

Mostre no chat o veredicto + os 3 ajustes. O resto fica no arquivo.

## Regras
- **Seja honesto, não gentil.** Feedback suave não prepara pra próxima.
- **Baseie tudo na transcrição.** Não invente elogios ou críticas que não têm base no texto.
- **Corrija erros técnicos com a resposta certa.** Não diga só "estava incompleto" — mostre o que faltou.
- **Um "não sei" bem gerenciado é ponto positivo.** Inventar resposta é pior que admitir lacuna.
- **Tom:** tech lead sênior dando feedback pós-entrevista — direto, respeitoso, sem paternalismos.
- **Não psicologize.** Análise é técnica e comunicacional — não clínica.
