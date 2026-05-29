---
description: Prepara para entrevista técnica de uma vaga que avançou no processo — gera perguntas do básico ao framework, simula sessão e dá feedback por resposta
---

# /entrevista — Prep de entrevista técnica

Comando pra preparar o usuário para entrevistas técnicas de vagas que avançaram no processo.
Lê a vaga cadastrada, identifica a stack exigida e gera uma sessão de perguntas em escada —
do conceito mais básico até o framework/padrão específico pedido na vaga.

## Inputs aceitos
- Caminho da pasta da candidatura (ex.: `vagas/candidaturas/2026-05-28/empresa-cargo/`)
- Nome da empresa ou cargo (o sistema localiza a pasta)
- Texto/link da vaga colado diretamente
- Nenhum input → lista as vagas com status `entrevista` no `_index.md` e pede escolha

## Fluxo

### 1. Leia o contexto obrigatoriamente
- `_contexto/perfil.md` — stack do usuário, pontos fortes e gaps
- A `vaga.md` da candidatura escolhida — stack exigida, stack desejada, seniority, empresa
- A `curriculo.md` gerada pra essa vaga — o que o usuário afirmou saber nela

### 2. Extraia o mapa de tópicos da vaga

Para **cada hard skill** listada na vaga (obrigatória e desejada), monte uma árvore de perguntas em 5 níveis:

```
[hard skill da vaga]
  └── L1 — Conceito fundacional: o que é, por que existe, qual problema resolve
       └── L2 — Como funciona internamente: modelo de execução, paradigma, trade-offs
            └── L3 — Padrões e boas práticas: arquitetura, SOLID, convenções do ecossistema
                 └── L4 — Uso avançado da ferramenta: APIs internas, configurações não óbvias, edge cases
                      └── L5 — Problema real: como você resolveria X nessa stack em produção
```

Exemplos de como a árvore se aplica a diferentes skills:

| Hard skill | L1 | L3 | L5 |
|---|---|---|---|
| NestJS | O que é Node, event loop | Módulos, DI, Guards | Como isolar módulo de pagamento |
| PostgreSQL | O que é um RDBMS, ACID | Índices, query plan, transactions | Como resolver N+1 no Prisma |
| RabbitMQ | O que é mensageria, por que usar | Exchange types, dead letter queue | Como garantir entrega exactly-once |
| Terraform | O que é IaC, por que declarativo | State, módulos, workspaces | Como gerenciar multi-env sem duplicar código |
| Docker | O que é containerização, diff de VM | Layers, multi-stage build | Como otimizar imagem de produção Node |
| Redis | O que é cache, quando não usar | TTL, eviction policies, pub/sub | Como invalidar cache em evento de domínio |
| TypeScript | O que é tipagem estática | Generics, utility types, strict mode | Como tipar um repositório genérico com Prisma |

Gere a árvore completa antes de começar a sessão. Priorize as skills **obrigatórias** da vaga — skills desejadas entram só se sobrar tempo ou você pedir.

### 3. Apresente o plano da sessão
Mostre avocê:
- Quais tópicos serão cobertos e em que ordem
- Estimativa de tempo (ex.: "~25 min, 4 blocos de perguntas")
- Pergunte: **"Quer começar agora ou pular algum bloco?"**

### 4. Conduza a sessão em modo entrevistador

Execute bloco a bloco. Para cada bloco:

1. **Faça a pergunta** — uma de cada vez, espere a resposta
2. **Após a resposta**, dê feedback imediato:
   - ✅ O que estava certo e por quê
   - ⚠️ O que estava incompleto (sem julgar, completar a lacuna)
   - ❌ O que estava errado — corrija com a resposta esperada por um sênior
   - 💡 O que um recrutador sênior espera ouvir além disso
3. **Pergunte:** "Pronto para a próxima?" — não avance sem confirmação

#### Como formular perguntas por nível

Para cada skill, gere perguntas seguindo os 5 níveis da árvore do passo 2.
A formulação muda conforme a natureza da skill:

- **Ferramentas/frameworks** (NestJS, Prisma, Docker): pergunte como funciona internamente antes de perguntar como usar
- **Bancos de dados**: sempre inclua uma pergunta de problema real com a ORM/driver da vaga
- **Arquitetura/padrões** (SOLID, DDD, Clean): peça exemplo de código ou decisão real — não aceite definição de livro
- **Cloud** (AWS, Azure): ancore em serviço específico que a vaga mencionar, não em conceito genérico
- **Estruturas de dados/algoritmos** (se a vaga pedir ou for produto de alto tráfego): problema concreto com complexidade justificada

Adapte o vocabulário da pergunta à stack da vaga: se a vaga usa Prisma, pergunte N+1 no Prisma — não no TypeORM.

### 5. Relatório final da sessão

Ao final (ou quando você pedir `fim`), gere um relatório salvo em
`vagas/candidaturas/[pasta-da-vaga]/entrevista-prep.md`:

```md
# Prep de entrevista — [Empresa] | [Cargo]
Data: [YYYY-MM-DD]

## Resultado por bloco
| Bloco | Acertou | Parcial | Errou |
|-------|---------|---------|-------|
| Fundação Node | X | X | X |
...

## Pontos fortes identificados
- ...

## Lacunas pra revisar antes da entrevista
- [tópico]: [o que estudar em 10 min]

## Frases que soaram bem
> "..."

## Frases pra evitar
- ...
```

Mostre o resumo no chat (3–5 bullets do que reforçar antes da entrevista real).

## Regras
- **Uma pergunta por vez.** Nunca despeje 5 perguntas de uma vez.
- **Espere a resposta antes de dar feedback.** Não antecipe.
- **Adapte a dificuldade em tempo real:** se você está respondendo bem, aprofunde; se está travando, volte um nível sem humilhar.
- **Nunca invente lacunas** que não existam no CV ou na vaga — o prep é sobre o que foi afirmado, não sobre o que seria ideal.
- **Tom:** direto, técnico, sem paternalismos — como um tech lead sênior que respeita o entrevistado.
- **Se a vaga pedir EN**, conduza a sessão em inglês — use o nível de inglês declarado no `perfil.md`; se for intermediário, prefira frases mais curtas e diretas.
