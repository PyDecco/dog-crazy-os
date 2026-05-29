# COMECE AQUI — Instalação no VS Code (passo a passo)

Guia para rodar o dog-crazy-os dentro do VS Code. Leva ~15 min. Não precisa
saber programar.

---

## O que você precisa antes
1. **VS Code instalado.** Se não tiver: https://code.visualstudio.com (versão
   1.98 ou mais nova — qualquer download atual já serve).
2. **Assinatura paga do Claude** (Pro, a partir de US$20/mês). O plano grátis
   NÃO dá acesso ao Claude Code. Assine em https://claude.ai.
3. **Este sistema** — a pasta `dog-crazy-os` clonada ou descompactada num lugar
   fácil (ex: Área de Trabalho).
4. **Python 3 + wkhtmltopdf** — para gerar o PDF do currículo.
   - Python: https://python.org/downloads
   - wkhtmltopdf: https://wkhtmltopdf.org/downloads.html

> Bom saber: a extensão do VS Code já vem com o Claude Code embutido. Você NÃO
> precisa instalar nada por terminal separadamente.

---

## Passo 1 — Instalar a extensão Claude Code
1. Abra o VS Code.
2. Aperte `Ctrl + Shift + X` (Windows/Linux) ou `Cmd + Shift + X` (Mac). Isso
   abre a aba de Extensões.
3. Na busca, digite **Claude Code**.
4. Na extensão da **Anthropic**, clique em **Install**.
5. Se ela não aparecer depois de instalar, abra a paleta de comandos
   (`Ctrl/Cmd + Shift + P`), digite **Developer: Reload Window** e Enter.

## Passo 2 — Abrir a pasta do sistema
1. No VS Code: menu **File → Open Folder** (Arquivo → Abrir Pasta).
2. Selecione a pasta `dog-crazy-os` que você clonou ou descompactou.
3. Se aparecer um aviso perguntando se você confia na pasta, clique em
   **"Yes, I trust the authors"** (Sim, confio) — é o seu próprio sistema.

## Passo 3 — Entrar na sua conta
1. Procure o ícone do Claude Code (uma estrelinha / "Spark"). Ele fica no canto
   superior direito do editor (precisa ter um arquivo aberto) OU na barra lateral
   esquerda, OU no rodapé como **✱ Claude Code**.
2. Clique nele para abrir o painel do Claude.
3. Na primeira vez aparece uma tela de login. Clique em **Sign in** e autorize
   no navegador, com a conta da sua assinatura.

> Dica: abra qualquer arquivo (ex: clique em `README.md` na lista à esquerda)
> para o ícone da estrelinha aparecer no canto superior direito.

## Passo 4 — Configurar o sistema

### Jeito garantido (terminal integrado do VS Code)
1. Abra o terminal integrado: `Ctrl + '` (crase, ao lado do número 1) no
   Windows/Linux, ou `Cmd + '` no Mac. Também dá pelo menu **Terminal → New
   Terminal**.
2. Vai abrir uma faixa na parte de baixo. Digite e Enter:
   ```
   claude
   ```
3. Quando o Claude iniciar ali, digite:
   ```
   /install
   ```
   Ele vai te entrevistar (nome, área, o que você vende, preços, stack...) e
   preencher seu contexto em `_contexto/`. Esses arquivos ficam no `.gitignore`
   — seus dados não saem da sua máquina.

### Jeito alternativo (painel gráfico)
No painel do Claude, digite `/` e veja se `install` aparece na lista. Se aparecer,
pode usar por ali. Se não aparecer, use o terminal integrado acima.

---

## DEPOIS DE INSTALAR — seus comandos

| Comando | O que faz |
|---|---|
| `/prospectar` | Acha empresas-alvo e escreve abordagens PJ/freela. **Comece por aqui.** |
| `/aplicar` | Candidatura completa: adapta CV, escreve mensagem, salva tudo |
| `/curriculo` | Adapta seu currículo às palavras-chave de uma vaga |
| `/conteudo` | Gera posts para LinkedIn e Instagram na sua voz |
| `/conversa` | Cole o print de uma conversa → indica o próximo passo |
| `/entrevista` | Prep de entrevista técnica com perguntas em escada |
| `/feedback-entrevista` | Analisa transcrição de entrevista e dá diagnóstico |
| `/check` | Check de energia antes de começar o dia |

Logo após o `/install`, rode:
```
/prospectar
```

---

## Se algo travar
- **Estrelinha não aparece:** abra um arquivo qualquer; ela só surge com um
  arquivo aberto. Ou use **✱ Claude Code** no rodapé.
- **"Please run /login":** sua sessão caiu — clique em Sign in de novo. Confirme
  que sua assinatura está ativa em claude.ai.
- **Comando /install não aparece no menu:** use o terminal integrado (Passo 4,
  jeito garantido). É normal — o painel mostra só um subconjunto.
- **PDF não gera:** confirme que Python 3 e wkhtmltopdf estão instalados e no PATH.
- **Extensão não instala:** confira a versão do VS Code (Help → About, precisa
  ser 1.98+).
- **Ajuda oficial:** https://code.claude.com/docs/en/vs-code
