---
description: Aplica para uma vaga — detecta o canal (form/gmail/dm), adapta o CV, escreve a mensagem do canal e salva o pacote pronto pra enviar
---

# /aplicar — Candidatura completa em 1 comando

Comando único pra encurtar tempo por candidatura (meta: 20/dia).
Recebe uma vaga, detecta o canal de envio, gera o pacote completo (CV adaptado + mensagem do canal) e salva tudo organizado.

## Inputs aceitos
- Print da vaga (qualquer plataforma: LinkedIn, Indeed, Vagas.com, Gupy, etc.)
- Texto/descrição colado
- Link da vaga
- Qualquer combinação dos acima
- Contexto extra opcional ("vi indicação no DM", "essa eu quero muito", etc.)

## Fluxo

1. **Leia o contexto OBRIGATORIAMENTE:**
   - `_contexto/curriculo-base.md` (PT) OU `_contexto/curriculo-base-es.md` (ES)
     — esta é a **fonte canônica** da estrutura e dos elementos do CV. O CV
     adaptado tem que ser fiel a este arquivo (mesmas seções, mesma ordem das
     empresas, mesma forma de listar projetos como bullets, **mesmo cabeçalho
     — cidade, telefone, contato**).
   - `_contexto/perfil.md` (provas, stack, faixa de preço, disponibilidade,
     **localizações e telefones por idioma — PT/BR vs ES/AR**)
   - `_contexto/icp.md` (verificar fit antes de adaptar)
   - `_contexto/voz.md` (tom da mensagem do canal)
   - Os `_contexto/curriculo-base*.pdf` são a referência visual ATS — não edite,
     o gerador os reproduz a partir do `.md`.

   > **IMPORTANTE — modelos por idioma têm dados diferentes.** O modelo PT
   > (`curriculo-base.md`) carrega cidade/telefone BR; o modelo ES
   > (`curriculo-base-es.md`) carrega cidade/telefone AR. NUNCA misture: se a
   > vaga é em ES, use ES inteiro (cabeçalho AR + telefone AR). Se você precisar
   > de um dado que não está no modelo do idioma escolhido (ex.: CNPJ pra
   > mensagem em ES), busque no `perfil.md`.

2. **Pegue a data de hoje** (formato `YYYY-MM-DD`, ex.: `2026-05-26`). Toda
   candidatura nasce dentro da pasta do dia em que foi criada. Use a data do
   sistema; se a data não estiver disponível, pergunte ao usuário em 1 linha.

3. **Dedup:** cheque `vagas/_index.md` (crie se não existir) por match de
   `[empresa-normalizada] + [cargo-normalizado]` em **qualquer dia**.
   - Se duplicado, mostre a entrada anterior (data, canal, status) e pergunte:
     **manter / atualizar / cancelar**.

4. **Detecte o canal** pelo conteúdo da vaga:
   - Menciona "enviar para [...]@gmail.com" / qualquer email → **canal=gmail**
   - Link/botão "Candidatar-se" externo / formulário → **canal=form**
   - "Envie DM" / "Mande mensagem no LinkedIn" → **canal=dm-linkedin**
   - Número WhatsApp / "WhatsApp" → **canal=dm-whatsapp**
   - "Apply on company website" / link direto → **canal=form**
   - Sem sinal claro com confiança >80% → **pergunte 1 linha objetiva**.

5. **Extraia palavras-chave** da vaga: stack obrigatória, stack desejada, anos
   de exp, seniority, idiomas, modelo de contratação, faixa salarial (se tiver).

6. **Verifique fit com ICP:** se a vaga claramente foge do ICP (ex.: júnior,
   CLT exclusivo quando ele quer PJ, stack totalmente diferente), avise antes
   de gerar — pergunte se quer prosseguir mesmo assim.

7. **Gere o pacote** em `vagas/candidaturas/[YYYY-MM-DD]/[empresa-kebab]-[cargo-kebab]/`
   (a data é a do passo 2 — pasta do dia):

   - **`vaga.md`** — texto/link original, canal detectado, data, palavras-chave
     extraídas, score de fit com ICP.

   - **`curriculo.md`** — CV adaptado em markdown, **fiel à estrutura do modelo
     do idioma escolhido** (`curriculo-base.md` para PT, `curriculo-base-es.md`
     para ES). Regras inegociáveis:
     - **Cabeçalho copiado integralmente do modelo do idioma** — não troque
       cidade/telefone do modelo. Cada modelo já carrega os dados do país correspondente,
       conforme configurado pelo usuário em `_contexto/perfil.md`. Se a vaga é em ES,
       mesmo que seja pra empresa BR, use o modelo ES inteiro; o oposto também vale.
     - Mesmas seções, na mesma ordem do modelo de origem: cabeçalho → resumo
       → `## EXPERIÊNCIA PROFISSIONAL` (ou `EXPERIENCIA PROFESIONAL` em ES) →
       `## HABILIDADES TÉCNICAS` → `## FORMAÇÃO` → `## IDIOMAS & CERTIFICAÇÕES`.
       Se o modelo do idioma incluir `## INFORMAÇÕES ADICIONAIS` (CNPJ), copie
       essa seção; se NÃO incluir (o modelo ES não tem), também NÃO inclua. A
       regra é: **fidelidade absoluta ao modelo do idioma**, sem adicionar
       seção que ele não tem nem omitir seção que ele tem. **NÃO** invente
       seções tipo "Stack técnica" antes da experiência, "Provas alinhadas à
       vaga" ou tabelas de match — quebra o renderer e o ATS.
     - **Ordem cronológica reversa das empresas** (RajoTech → Sensedia → 4all
       → Sistema Campeão). Cada empresa é UM `### Cargo · Empresa — período`;
       projetos da mesma empresa são bullets dentro dela. Não transforme
       projetos em jobs separados.
     - Espelhe palavras-chave da vaga em **bold** dentro dos bullets, sem
       inventar nada. Reordene **projetos dentro da empresa** (não as empresas)
       pra deixar o mais relevante primeiro.
     - Use os números reais do perfil (25%, 99,9%, 40%, 100k usuários, 10k
       tx/dia). Não exagere.

   - **`curriculo.pdf`** — gere logo após salvar o `.md` rodando:
     `python3 .claude/scripts/render_cv.py vagas/candidaturas/[YYYY-MM-DD]/[pasta]/curriculo.md`
     O script produz `curriculo.html` (intermediário) + `curriculo.pdf` no padrão
     ATS preto/branco. Não crie HTML manual — o template está no script.
     Confira com `pdfinfo` que saiu 1–2 páginas. Se mais, encurte projetos
     antigos. Se a estrutura saiu errada, corrija o `curriculo.md` — não mexa
     no script.

   - **`mensagem.md`** — conteúdo do canal:
     - **gmail:** `Assunto: ...` + corpo do email (5–8 linhas, tom do perfil,
       UMA prova relevante, CTA leve) + assinatura com **telefone do idioma do
       email** (ES → +54; PT → +55) + lista de anexos (`anexar curriculo.pdf`)
     - **form:** prompt completo pro Claude for Chrome preencher campo a campo
       (ver `.claude/skills/candidaturas/chrome-prompts.md` quando existir; por
       enquanto, gere prompt direto seguindo padrão: identificação do site →
       seleção de campos → valores a preencher → ação final de submit).
     - **dm-linkedin:** mensagem 3–4 linhas, casual+técnica, gancho real da
       empresa na 1ª linha, sem corporativês.
     - **dm-whatsapp:** mensagem com quebras (várias linhas curtas), mais
       informal, gancho na 1ª.

   - **`status.md`** — `rascunho` (ao gerar), `enviado-em: [data]`, `resposta`.

8. **Se canal=gmail, crie o rascunho no Gmail via MCP** logo após salvar
   `mensagem.md` e gerar o PDF:
   - Tool: `mcp__claude_ai_Gmail__create_draft`
   - Parâmetros:
     - `to`: email destinatário extraído da vaga
     - `subject`: linha "Assunto:" da `mensagem.md` (sem o prefixo "Assunto: ")
     - `body`: corpo da mensagem (do "Hola/Olá" até a assinatura — **sem** a
       seção `## Anexos`)
     - `attachments` (se a integração suportar): caminho absoluto do
       `curriculo.pdf` que acabou de ser gerado.
   - **Se a tool falhar ou não suportar anexo**, NÃO interrompa o fluxo:
     - registre no chat o erro em 1 linha
     - mantenha o `mensagem.md` válido pra copy/paste manual
     - se foi só o anexo que falhou, criou rascunho só com corpo e avise pro
       usuário anexar o PDF manualmente antes de enviar.
   - Mostre no chat o ID do rascunho (`draftId`) ou o link `https://mail.google.com/mail/u/0/#drafts`
     pra o usuário abrir e revisar.

9. **Atualize `vagas/_index.md`:**
   - Incremente a linha de "Resumo por dia" para `[YYYY-MM-DD]` (cria se for o
     primeiro do dia).
   - Adicione nova linha na tabela "Detalhe":
     `[data] | [empresa] | [cargo] | [canal] | [status] | [path com data]`.

10. **Aponte o gap:** liste o que a vaga pede e a pessoa não tem. Deixe a
    decisão de candidatar-se com ela.

11. **Mostre no chat:**
   - Caminho da pasta criada
   - Resumo (1 linha) do que está em cada arquivo
   - O conteúdo de `mensagem.md` já pronto pra copiar (não espera o usuário
     abrir o arquivo)
   - Se canal=gmail: link/ID do rascunho criado no Gmail (passo 8)
   - Gap apontado

## Regras
- **NUNCA invente** experiência, diploma, cliente, anos, números. Espelhar
  vocabulário da vaga é honesto; mentir queima reputação.
- **UMA prova por mensagem** — não despeje 5 cases.
- **Soa como gente, não como LLM** — ver
  `.claude/skills/prospeccao/humanizacao.md` (mesmas regras valem aqui).
- **Tom:** direto, técnico, sem corporativês — ver `_contexto/voz.md`.
- **Idiomas:** use o nível de cada idioma declarado em `_contexto/perfil.md`. Se EN for
  intermediário, prefira frases mais curtas e diretas.
- **Se a vaga não bate com o ICP**, avise antes de gerar.
- **Se o canal não for claro**, pergunte UMA linha objetiva — não chute.
- **Coerência de país por idioma:** cada modelo de CV (`curriculo-base.md`, `curriculo-base-es.md`
  etc.) carrega os dados de contato do país correspondente, conforme configurado em `_contexto/perfil.md`.
  NUNCA edite o cabeçalho do CV gerado pra "trocar de país" no meio do fluxo — se você acha
  que deveria, é porque o modelo do idioma certo precisa ser atualizado em `_contexto/`, não na
  candidatura. Avise o usuário e pare.
- **Não mencione número fiscal local (CNPJ, CUIT, etc.) em mensagens para mercados estrangeiros.**
  Dados fiscais de outro país levantam dúvida sobre capacidade de pagamento local. Na 1ª mensagem,
  use apenas "contractor" ou equivalente no idioma. Os dados fiscais são usados no faturamento —
  isso é negociado depois. Verifique quais dados fiscais o usuário declarou em `_contexto/perfil.md`
  e quais mercados cada modelo de CV atende.
- **Rate em USD coerente com o equivalente em BRL pedido pelo usuário.**
  Quando o usuário disser "calcule USD pra X reais", pegue a cotação atual
  (`curl -s https://economia.awesomeapi.com.br/json/last/USD-BRL`), faça
  `BRL / bid = USD` e arredonde pra cima até a próxima centena. Registre no
  `status.md` a cotação usada e a data, pra rastreabilidade futura.
