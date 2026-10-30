# Ícaro Silva

Identidade visual do Ícaro Silva, versão 1.0, aprovada pelo Ícaro. Este documento é a fonte da verdade para o site de apresentação e para qualquer material da marca: cores, fontes, logo, tom de voz e regras de código. Quando algo aqui entrar em conflito com o código existente, vale este documento.

## A ideia central: o sol e a asa

No mito, Ícaro voa com asas de cera feitas pelo pai, Dédalo, o grande inventor, e cai quando chega perto demais do sol. Esta marca vira a história do avesso: sol e asa deixam de ser inimigos e passam a formar uma só figura. A asa não é de cera, é de engrenagens e latão. A ciência (Dédalo) é o que torna o voo possível, e o sol deixa de ser ameaça para virar a outra metade de quem voa.

Isso sustenta três ideias do Ícaro:

- **Inovação com responsabilidade.** Voar alto, mas com engenharia, dados e segurança por trás.
- **Inclusão como ponto de partida.** O voo só vale se leva todo mundo junto. Daí a assinatura: *Voar alto, levando todo mundo junto.*
- **Mostrar as cicatrizes.** As marcas de cera derretida não se escondem. O Ícaro quer falar das falhas que o mundo tech prefere esconder (exclusão, vieses, insegurança) e isso faz parte da marca, não é um ruído nela.

Universos de referência: mitologia grega, astronomia, steampunk (latão, rebites, engrenagens) e a origem latina do Ícaro, representada pelo vermelho carmesim.

## Para quem fala

Pequenas e médias empresas que podem virar clientes, e outros desenvolvedores. O objetivo do site é conquistar clientes e mostrar a trajetória do Ícaro como tecnologista interessado em ciências sociais. No futuro, a marca deve sustentar uma empresa própria e uma presença em redes sociais.

## Personalidade e voz

A marca é **inclusiva, criativa e inovadora**. Ela nunca deve soar **acadêmica, complicada ou monocromática**.

Como isso aparece no texto:

- Profissional sem formalidade em excesso. Fale com "você", em frases curtas.
- Explique termos técnicos na primeira vez ou troque por palavras simples. "Sites que qualquer pessoa consegue usar" em vez de "conformidade WCAG 2.2 AA".
- Mostre abertura: termine seções com um convite concreto ("Me conte sobre o seu projeto"), não com slogans.
- Botões dizem exatamente o que fazem: "Enviar mensagem", "Ver projeto", "Falar no WhatsApp".
- Nada de "apaixonado por tecnologia", "soluções inovadoras" ou "transformação digital" sem um exemplo real ao lado.

Exemplos:

| Em vez de | Escreva |
| --- | --- |
| Desenvolvedor Full Stack apaixonado por inovação | Crio sites e apps que funcionam para todo mundo, inclusive quem quase sempre fica de fora. |
| Entre em contato | Tem um projeto em mente? Me conte. |
| Em breve | Estou organizando meus projetos. Enquanto isso, veja meu GitHub. |

## Logo

A logo oficial foi criada pelo Ícaro. À esquerda, meio sol em traço fino. Uma linha vertical divide a figura. À direita, uma asa mecânica: engrenagens, rebites e articulações, e penas angulares em contorno com veios. O sol (o mito, a astronomia) e a asa (a engenharia de Dédalo) são as duas metades de uma mesma figura.

Cores da logo, todas da paleta:

| Parte | Dia | Noite |
| --- | --- | --- |
| Raios, anel do sol e linha divisória | `sol-traco` #b07808 | `sol` #f4b942 |
| Contornos das penas e da mecânica | `tinta` #0f1a3d | `tinta` #edf1fb |
| Peças de latão claro (polias, alavancas) | `sol` #e3a21a | `sol` #f4b942 |
| Engrenagens e veios das penas | `latao` #7e5d2b | `latao` #c9a46a |

O carmesim fica de fora da logo de propósito, para continuar sendo um acento raro.

Arquivos:

- `logo-icaro-silva-dia.svg` e `logo-icaro-silva-noite.svg`: a logo completa em vetor, fundo transparente. Troque entre as duas junto com o tema.
- `favicon-icaro-silva-dia.svg` e `favicon-icaro-silva-noite.svg`: a versão reduzida, desenhada pelo Ícaro, em quadro quadrado. Para favicon, aba do navegador e qualquer uso abaixo de 120px.

O favicon mantém o sol em traço e a mesma linha divisória, mas a asa tem penas preenchidas e menos peças mecânicas, para ser lida de longe. Cores do favicon:

| Parte | Dia | Noite |
| --- | --- | --- |
| Raios, anel do sol e linha divisória | `sol-traco` #b07808 | `sol` #f4b942 |
| Contornos | `tinta` #0f1a3d | `tinta` #edf1fb |
| Penas e braço da asa | `sol` #e3a21a | `sol` #f4b942 |
| Engrenagens e haste de cobre | `latao` #7e5d2b | `latao` #c9a46a |

Os dois arquivos foram vetorizados a partir de imagens: os degradês viraram cores chapadas e o miolo das formas é transparente. Se um dia existirem vetores desenhados à mão, eles substituem estes.

Regras:

- Logo completa a partir de 120px de largura; abaixo disso, use o favicon. Em 32px e 48px o favicon mostra sol e asa; em 16px fica a silhueta dourada.
- No HTML, aponte o favicon para a versão Noite quando o sistema estiver em modo escuro (`<link rel="icon" media="(prefers-color-scheme: dark)">`).
- Ao lado do símbolo, o nome "Ícaro Silva" em Bricolage Grotesque, peso 800, cor `tinta`.
- Área de respiro em volta: um quarto da largura da logo.
- Não gire, não distorça, não mude as cores, não coloque sobre fotos.

## Cores

A paleta foge do monocromático de propósito: um azul meia-noite como base, o dourado do sol, o latão das engrenagens e o vermelho carmesim como acento latino.

- `ceu` é o fundo, `superficie` fica sobre ele, `tinta` é o texto.
- `meia-noite` é a cor da marca: títulos de destaque, botão principal, links e o anel de foco do teclado.
- `sol` é para preencher e ilustrar, nunca para texto no tema Dia.
- `sol-traco` é o dourado dos traços finos (os raios do sol na logo, ícones de linha), mais escuro no Dia para ficar visível sobre o fundo claro.
- `latao` aparece nos detalhes mecânicos: linha do tempo da formação, ícones, divisórias especiais.
- `carmesim` é raro: no máximo um elemento por tela (uma tag, um link em hover). Como o vermelho também costuma sinalizar erro, mensagens de erro do formulário sempre vêm com ícone e texto explicando o problema, para não se confundirem com o acento.
- Proporção sugerida por tela: 70% `ceu` e `superficie`, 20% `meia-noite` e `tinta`, 10% somando `sol`, `latao` e `carmesim`.

## Temas Dia e Noite

O site tem os dois temas, e o padrão segue a preferência do sistema da pessoa. O seletor é uma pílula com sol e lua, rotulada "Tema claro" e "Tema escuro" para leitores de tela. A escolha fica salva no navegador.

No código:

- O tema ativo fica no atributo `data-theme="dia"` ou `data-theme="noite"` do elemento `<html>`.
- Sem escolha salva, o tema segue `prefers-color-scheme`. A escolha manual fica em `localStorage` na chave `tema`, sempre dentro de `try/catch`.
- Um script pequeno no `<head>`, antes do CSS, aplica o tema salvo para a página não piscar no tema errado ao carregar.
- A logo troca entre `logo-icaro-silva-dia.svg` e `logo-icaro-silva-noite.svg` junto com o tema (dois `<img>` alternados por CSS, ou um `<picture>`).

## Tipografia

- **Bricolage Grotesque** (`display`) nos títulos: expressiva, um pouco irregular, com personalidade sem parecer acadêmica.
- **Atkinson Hyperlegible** (`texto`) no corpo: criada pelo Braille Institute para pessoas com baixa visão, com letras que não se confundem (I, l, 1; O, 0). Ela é a prova da inclusão já na escolha da fonte.
- As duas estão no Google Fonts, com acentos para português, espanhol e francês. Link: `https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600..800&display=swap`, com `preconnect` para `fonts.googleapis.com` e `fonts.gstatic.com`.
- Pilhas de fallback: `"Bricolage Grotesque", "Trebuchet MS", sans-serif` e `"Atkinson Hyperlegible", Verdana, sans-serif`.
- Escala: `display` 64px (só o herói, cai para 44px no celular), `titulo-1` 40px (32px no celular), `titulo-2` 26px, `corpo` 18px com entrelinha 1.6, `corpo-pequeno` 15px, `rotulo` 15px negrito. Use `rem` no código (base 16px) para respeitar o zoom do navegador.
- Sem textos em maiúsculas, sem sublinhar palavras soltas no meio de títulos, sem fonte monoespaçada decorativa.

## Forma e espaço

- A pílula (`raio-pilula`) é a forma de pena da marca: botões, seletor de tema, seletor de idioma.
- Cartões e blocos de cor usam `raio-lg`; campos e tags, `raio-sm`.
- Espaçamento em múltiplos de 8px (`espaco-2` a `espaco-16`). Seções bem separadas: o site respira.

## Movimento

O Ícaro não quer um site estático, mas movimento demais cansa e exclui. A regra é um momento marcante e respostas úteis:

- **O momento:** ao abrir o site, a logo do herói se abre a partir da linha divisória: o sol aparece para a esquerda e a asa para a direita, como uma cortina saindo do centro (`clip-path: inset(0 50% 0 50%)` animado até `inset(0)`, cerca de 700ms, curva `ease-out`). Logo depois, o nome e a assinatura surgem com um leve fade. É a única animação automática do site.
- **Respostas:** botões e links mudam de cor no hover e no foco; o seletor de tema faz o sol virar lua (rotação e troca do ícone, 300ms); cartões de projeto sobem 2px no hover. Nada além disso se mexe sozinho.
- Com "reduzir movimento" ativado no sistema (`prefers-reduced-motion: reduce`), tudo aparece já no lugar, sem animação.
- A logo é um arquivo único: não tente animar penas ou engrenagens separadamente.

## Componentes do site

Regras para os elementos de interface. Todos os valores vêm dos tokens.

- **Botão principal:** fundo `meia-noite`, texto `sobre-marca`, estilo `rotulo`, padding `espaco-4` na vertical e `espaco-8` na horizontal, `raio-pilula`. Hover: fundo um pouco mais escuro no Dia e mais claro na Noite. Altura mínima de 44px (área de toque).
- **Botão secundário:** fundo transparente, borda de 2px em `meia-noite`, texto `meia-noite`, mesma forma do principal.
- **Links no texto:** cor `meia-noite`, sublinhados. No hover, a cor vira `carmesim`.
- **Foco:** em tudo que é clicável, `outline: 3px solid var(--meia-noite); outline-offset: 2px`, visível só com `:focus-visible`.
- **Campos do formulário:** fundo `superficie`, borda de 2px em `tinta-suave`, `raio-sm`, rótulo visível acima (estilo `rotulo`), padding `espaco-4`. Foco: borda e anel em `meia-noite`. Erro: mensagem em texto abaixo do campo, com ícone, ligada ao campo por `aria-describedby`.
- **Cartões (projetos, contato):** fundo `superficie`, `raio-lg`, padding `espaco-8`, sem sombra pesada; separação por cor e espaço, não por borda grossa.
- **Tags de tecnologia:** texto `corpo-pequeno`, borda de 1px em `latao`, `raio-sm`. No máximo uma tag por cartão pode usar `carmesim` (por exemplo, "Em desenvolvimento").
- **Linha do tempo da formação:** linha vertical de 2px em `latao`, com um círculo (rebite) de 12px em `latao` em cada item. Ano em `corpo-pequeno` `tinta-suave`, curso em `titulo-2`, instituição em `corpo`. É a única lista do site que tem ordem (cronológica, da mais recente para a mais antiga).
- **Navegação:** fixa no topo, fundo `ceu` com leve transparência, logo pequena à esquerda (favicon + nome, ou a logo completa a partir de 120px), links das seções, seletor de idioma e seletor de tema à direita. No celular, os links viram um menu aberto por um botão com `aria-expanded`.
- **Seletor de tema:** botão em pílula com ícone de sol ou lua, `aria-label` "Ativar tema escuro" ou "Ativar tema claro" conforme o estado.
- **Seletor de idioma:** lista com o nome de cada idioma nele mesmo; enquanto só houver português, ele não aparece.
- **Largura do conteúdo:** texto em colunas de até 70 caracteres (cerca de 680px); seções com largura máxima de 1120px, centralizadas, com `espaco-8` de margem lateral no celular.

## Acessibilidade (inegociável)

- Contraste de texto de pelo menos 4.5:1 nos dois temas (os tokens já garantem isso quando usados como descrito).
- Foco do teclado sempre visível: anel de 3px em `meia-noite` com 2px de afastamento.
- Imagens com texto alternativo; o logo tem `aria-label`.
- Formulário com rótulos visíveis acima dos campos, mensagens de erro em texto (não só em cor).
- Site navegável só com teclado, e testado com leitor de tela.

## Idiomas

Lançamento em português. Depois, espanhol, francês e inglês, idiomas que o Ícaro fala. O seletor mostra o nome de cada idioma nele mesmo (Português, Español, Français, English), nunca bandeiras.

## Fotos

Uma ou duas fotos do Ícaro no site inteiro, com cantos `raio-lg`. Fotos reais, com luz natural; sem filtros que mudem a cor da pele.

## O que evitar

- Numeração de seções (01, 02, 03) quando o conteúdo não é uma sequência.
- Seções "Em breve" vazias. Se não há projetos ainda, mostre o processo (o app de leitura em andamento) ou o GitHub.
- Gradientes azul-roxo, cartões com emoji, fundo creme com acento terracota: são clichês de sites genéricos.
- Referências diretas a marcas e personagens de terceiros na identidade.
