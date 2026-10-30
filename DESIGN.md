---
name: Ícaro Gavioli
description: O marco geodésico, com o sol, a estrela e as asas. Concreto claro de dia, céu do Sul à noite.
colors:
  chao-dia: "#ebedea"
  chao-noite: "#0c1322"
  placa-dia: "#f7f8f6"
  placa-noite: "#141d31"
  tinta-dia: "#1b1f1d"
  tinta-noite: "#e9edf4"
  tinta-suave-dia: "#4a524d"
  tinta-suave-noite: "#a9b3c6"
  bronze-dia: "#b0602a"
  bronze-noite: "#bd6b32"
  bronze-texto-dia: "#84431a"
  bronze-texto-noite: "#e3a06a"
  patina-dia: "#f4e4d1"
  patina-noite: "#fbeee0"
  rio-dia: "#1f5299"
  rio-noite: "#8fb6f2"
  sobre-rio-dia: "#ffffff"
  sobre-rio-noite: "#0c1322"
  terra-roxa-dia: "#7a2b1d"
  terra-roxa-noite: "#ef8a72"
  grade-dia: "#cdd2ce"
  grade-noite: "#24304a"
  curva-dia: "rgb(176 96 42 / 0.38)"
  estrela-noite: "#fbeee0"
  ceu-do-sul: "#0f1a33"
  friso-escurecedor: "#000000"
typography:
  display:
    fontFamily: "Archivo, Verdana, sans-serif"
    fontSize: "clamp(2.75rem, 5.2vw, 4.5rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 125"
  display-celular:
    fontFamily: "Archivo, Verdana, sans-serif"
    fontSize: "clamp(1.75rem, 6.6vw + 0.5rem, 2.75rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 125"
  titulo-1:
    fontFamily: "Archivo, Verdana, sans-serif"
    fontSize: "clamp(2rem, 3.4vw, 2.5rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 125"
  titulo-2:
    fontFamily: "Archivo, Verdana, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 112"
  titulo-fechamento:
    fontFamily: "Archivo, Verdana, sans-serif"
    fontSize: "clamp(2.25rem, 4.4vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 125"
  destaque:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 400
    lineHeight: 1.5
  apoio:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 400
    lineHeight: 1.6
  corpo-medio:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  rotulo-minimo:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 700
    lineHeight: 1.4
  corpo:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.6
  corpo-pequeno:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
  rotulo:
    fontFamily: "Atkinson Hyperlegible Next, Verdana, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 700
    lineHeight: 1.3
  coordenada:
    fontFamily: "Atkinson Hyperlegible Mono, ui-monospace, monospace"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.4
    fontFeature: "'tnum' 1"
rounded:
  raio-sm: "6px"
  raio-lg: "16px"
  disco: "50%"
spacing:
  espaco-2: "8px"
  espaco-4: "16px"
  espaco-8: "32px"
  espaco-16: "64px"
components:
  botao-principal:
    backgroundColor: "{colors.rio-dia}"
    textColor: "{colors.sobre-rio-dia}"
    typography: "{typography.rotulo}"
    rounded: "{rounded.raio-sm}"
    padding: "16px 32px"
    height: "48px"
  botao-principal-noite:
    backgroundColor: "{colors.rio-noite}"
    textColor: "{colors.sobre-rio-noite}"
    typography: "{typography.rotulo}"
    rounded: "{rounded.raio-sm}"
    padding: "16px 32px"
    height: "48px"
  botao-secundario:
    backgroundColor: "transparent"
    textColor: "{colors.tinta-dia}"
    typography: "{typography.rotulo}"
    rounded: "{rounded.raio-sm}"
    padding: "14px 32px"
    height: "48px"
  botao-secundario-hover:
    textColor: "{colors.rio-dia}"
  seletor-tema:
    backgroundColor: "transparent"
    textColor: "{colors.tinta-dia}"
    typography: "{typography.rotulo}"
    rounded: "{rounded.raio-sm}"
    padding: "0 16px"
    height: "44px"
  tag:
    backgroundColor: "transparent"
    textColor: "{colors.tinta-dia}"
    typography: "{typography.corpo-pequeno}"
    rounded: "{rounded.raio-sm}"
    padding: "4px 10px"
  monografia:
    backgroundColor: "{colors.placa-dia}"
    textColor: "{colors.tinta-dia}"
    rounded: "{rounded.raio-lg}"
    padding: "32px"
  menu-celular:
    backgroundColor: "{colors.placa-dia}"
    textColor: "{colors.tinta-dia}"
    padding: "16px 32px 32px"
---

# Design System: Ícaro Gavioli

> A fonte da verdade da identidade é o livro da marca, `marca-icaro-gavioli/marca/README.md`, com `tokens.css` e `tokens.json` na mesma pasta. Este arquivo registra como essa marca ficou no site construído (`index.html`, `css/style.css`, `css/tokens.css`, `js/script.js`). Os tokens de `css/tokens.css` são uma cópia literal dos da marca: mude lá primeiro e copie para cá. Em 28/10/2026 o livro foi atualizado para refletir as decisões do site, e os dois estão alinhados. Se voltarem a divergir, vale o livro: corrija o site ou atualize o livro, nunca deixe a diferença em silêncio.

## Overview

**Creative North Star: "O Marco Geodésico"**

O Ícaro é um disco de bronze chumbado no concreto, com a posição medida pelas estrelas, que qualquer pessoa pode usar como referência. A página é uma carta topográfica de um ponto só: de dia, o chão (concreto claro, curvas de nível em sépia, grade de coordenadas fina); à noite, o céu do Sul (as curvas somem e aparecem as estrelas que posicionaram o marco). O seletor de tema troca a planta inteira, não só as cores.

A densidade é calma e editorial: seções largas separadas por divisas finas, colunas de texto curtas, muito chão em volta. O vocabulário visual vem do levantamento topográfico e não de interface genérica: legenda de carta em vez de cartões de serviço, poligonal em vez de linha do tempo, monografia de marco em vez de lista de recursos, coordenadas medidas em vez de enfeite técnico. Nada flutua; tudo está apoiado no chão.

O site recusa o portfólio de dev padrão: nome gigante com foto ao lado, três cartões de serviço, fundo escuro com gradiente. O livro da marca recusa também gradientes azul-roxo, cartões com emoji, fundo creme com acento terracota e brilhos de "IA".

**Key Characteristics:**
- Dois temas com cenas diferentes: Dia é o chão (curvas e grade), Noite é o céu (estrelas).
- Paleta de papéis fixos: concreto, bronze, azul de rio e terra roxa.
- Archivo expandida a 125% nos títulos, Atkinson Hyperlegible Next no texto, Atkinson Hyperlegible Mono só em dados medidos.
- Plano: profundidade só por tom (placa sobre chão) e por linhas de grade, nunca por sombra.
- Cantos de placa estampada (6px); o círculo pertence só ao disco do marco.
- Uma única animação automática: o terreno sendo medido ao abrir.

## Colors

Uma paleta completa de papéis fixos, tirada de um marco no chão e de uma carta do IBGE; cada token tem um valor por tema, trocado por `data-theme` no `<html>` (ou por `prefers-color-scheme` quando não há escolha salva).

### Primary
- **Azul de Hidrografia** (`--rio`): a única cor de ação. Botão principal, links no texto, item de menu atual, anel de foco, seleção de texto. Mais escuro no Dia, mais claro na Noite.
- **Sobre o Rio** (`--sobre-rio`): rótulo do botão principal e do atalho "Pular para o conteúdo"; branco no Dia, o próprio céu na Noite.

### Secondary
- **Bronze do Disco** (`--bronze`): preenchimento do disco do marco no herói e do selo no Contato. Nunca texto pequeno.
- **Bronze de Gravação** (`--bronze-texto`): bronze legível. Coordenadas, rótulos da grade, símbolos da legenda de serviços, a linha e os vértices da poligonal, bordas das tags, números da monografia, barra de rolagem.
- **Pátina** (`--patina`): o que é gravado sobre o bronze (o símbolo no disco e o texto do aro). Só em gravação grande.

### Tertiary
- **Terra Roxa** (`--terra-roxa`): acento raro. No site aparece em dois lugares só: a tag "Em andamento" da poligonal e a cor de hover dos links. Não é cor de erro.

### Neutral
- **Concreto / Céu do Sul** (`--chao`): fundo da página. Concreto claro de dia, azul-noite profundo à noite. Também é o fundo do topo fixo (a 94%, com leve transparência).
- **Placa** (`--placa`): o que fica sobre o chão: a ficha da monografia, o menu aberto no celular, o fundo da foto enquanto carrega.
- **Tinta** (`--tinta`): texto principal, bordas de 2px dos botões secundários e controles, filetes de 2px que abrem a legenda e os canais de contato.
- **Tinta Suave** (`--tinta-suave`): texto de apoio, introduções de seção, instituições, rótulos da régua de coordenadas, direitos no rodapé.
- **Grade** (`--grade`): grade de coordenadas do terreno, divisas entre seções, linhas entre itens. Nunca borda de controle.
- **Curva** (`--curva`): curvas de nível, bronze translúcido. Só existe de dia; à noite vale `transparent`.
- **Estrela** (`--estrela`): pontos do céu. Só existe à noite; de dia vale `transparent`.
- **Cruzeiro** (`--ceu-do-sul`): fixo nos dois temas, reservado ao centro do símbolo Cruzeiro do livro da marca. O site não o usa hoje.

### Named Rules
**A Regra do Rio.** O `--rio` é a única cor de ação. Se algo é azul, dá para clicar; se dá para clicar, o estado de foco é azul.

**A Regra da Terra Roxa.** No máximo um elemento em `--terra-roxa` por tela, e nunca para sinalizar erro.

**A Regra do Bronze que Escreve.** `--bronze` preenche (o disco, o selo); `--bronze-texto` escreve e traça (coordenadas, vértices, legenda). Texto pequeno nunca vai em `--bronze`.

## Typography

**Display Font:** Archivo, eixo de largura em 125% (com Verdana, sans-serif)
**Body Font:** Atkinson Hyperlegible Next (com Verdana, sans-serif)
**Label/Mono Font:** Atkinson Hyperlegible Mono (com ui-monospace, monospace)

**Character:** Letra estampada em placa de metal nos títulos, contra uma fonte de texto desenhada pelo Braille Institute para baixa visão. A mono não é enfeite técnico: só aparece onde há um número medido.

As três famílias vêm do Google Fonts num único link, com `preconnect` para `fonts.googleapis.com` e `fonts.gstatic.com`. A largura da Archivo vem do token `--display-largura` (125%) via `font-stretch`.

### Hierarchy
- **Display** (800, `clamp(2.75rem, 5.2vw, 4.5rem)`, entrelinha 1, -0.03em, `text-wrap: balance`, até 14ch): só o título do herói, uma vez por página. No celular (até 640px) passa para `clamp(1.75rem, 6.6vw + 0.5rem, 2.75rem)`, cerca de 34px numa tela de 390px, para o título caber em três linhas e o botão principal aparecer na primeira tela; a parte em rem faz o título crescer com a fonte do sistema.
- **Título 1** (800, `clamp(2rem, 3.4vw, 2.5rem)`, 1.1, -0.02em, até 22ch): título de cada seção. O título do Contato é a única variação, maior (`clamp(2.25rem, 4.4vw, 3.5rem)`, até 18ch), porque é o convite final.
- **Título 2** (700, 1.625rem, 1.25, -0.01em, largura 112%): serviço na legenda, curso na poligonal, título da monografia, assinatura no rodapé.
- **Corpo** (400, 1.125rem, 1.6): parágrafos, até 58–62ch nas colunas de texto (nunca acima de 70 caracteres). A frase de apoio do herói sobe para 1.25rem e o destaque do Sobre para 1.375rem/1.5.
- **Corpo pequeno** (400, 0.9375rem, 1.5): tags, direitos no rodapé.
- **Rótulo** (700, 0.9375rem, 1.3): botões, seletor de tema, botão de menu, termos (`dt`) da monografia e dos canais. Sempre em caixa normal.
- **Coordenada** (mono 400, 0.9375rem, 1.4, algarismos tabulares, em `--bronze-texto`): coordenadas, anos da poligonal, rótulos da grade do terreno. Na régua do herói sobe para 1rem.

### Named Rules
**A Regra da Caixa Normal.** Nenhum texto em maiúsculas, nem o aro gravado do marco, nem rótulos, nem botões.

**A Regra do Número Medido.** A mono só aparece em coordenadas, anos e números medidos. Se não é uma medida, não é mono.

## Layout

Uma coluna central de até 1120px (`.faixa`: `max-width: calc(1120px + 2 * 32px)`, margem lateral de 32px em todas as larguras). As seções empilham com 128px de padding vertical no desktop e 80px no celular, separadas por uma divisa de 1px em `--grade`. O espaçamento segue múltiplos de 8px a partir dos tokens `espaco-2` a `espaco-16`; 40, 48, 56, 80 e 128px aparecem como múltiplos de 8 fora da escala nomeada.

- **Topo fixo** de 72px; `scroll-padding-top: 88px` para as âncoras não ficarem atrás dele.
- **Herói** ocupa a primeira tela (`min(100svh - 72px, 900px)`), com o terreno em SVG cobrindo tudo e o texto à esquerda; a régua de coordenadas fica presa ao pé da dobra.
- **Grades de duas colunas** nas seções: foto (até 340px) e texto no Sobre; título fixo (`sticky`, 20rem) e poligonal na Formação; texto e monografia (1fr / 1.15fr) em Projetos. Espaço entre colunas de 64px.
- **Legenda de serviços** em três colunas: símbolo (64px), nome (até 17rem), descrição.
- **Canais de contato** em quatro colunas.

Pontos de quebra:
- **Até 1000px:** os links viram menu; o terreno do herói sai de trás do texto e vira uma faixa acima do título (260 a 380px de altura), sem os rótulos da grade; a régua de coordenadas deixa de ser absoluta; grades de duas colunas viram uma; a legenda passa para duas colunas; canais em duas; o fragmento de terreno do Contato some.
- **Até 640px:** terreno com 160px, sem o texto do aro; o seletor de tema sai do topo e entra no menu; título do herói no clamp do celular; botões de ação ocupam a largura toda; monografia com padding de 16px e termos acima das definições; canais em uma coluna.

## Elevation & Depth

O sistema é plano. Não existe nenhum `box-shadow` no site. A profundidade vem de três coisas só: tom (`--placa` sobre `--chao`), linhas finas (`--grade` em 1px, `--tinta` em 2px para abrir listas) e o próprio terreno em SVG, que fica atrás do texto no herói. O topo fixo se separa do conteúdo por uma divisa de 1px e por um fundo `--chao` a 94%, nunca por sombra ou desfoque.

### Named Rules
**A Regra do Chão Plano.** Nada flutua. Sem sombras, sem brilhos, sem desfoque de fundo. Se algo precisa se destacar, ganha uma placa ou um filete, não uma sombra.

## Shapes

Cantos de placa estampada: botões, controles, tags e o atalho de teclado usam 6px (`raio-sm`); a foto e a monografia usam 16px (`raio-lg`). Não há pílulas. O círculo pleno (`disco`, 50%) pertence só ao emblema do marco: o disco grande do herói, cortado pela borda direita, com dois frisos concêntricos e o texto do aro centralizado entre eles (o mesmo espaço até cada friso), e o selo pequeno do Contato.

A outra forma recorrente é o vértice de triangulação: um triângulo de contorno com um ponto no centro (14px), em `--bronze-texto`, com o miolo pintado de `--chao`. Ele marca cada curso da poligonal e cada divisa entre seções.

Traços: curvas de nível com 1.4px e curvas-mestras com 2.6px; grade com 1px sem escala (`vector-effect: non-scaling-stroke`); linha da poligonal com 2px.

### Named Rules
**A Regra de Um Disco.** No máximo um disco de bronze por seção. O resto da seção se organiza em volta dele.

## Components

### Buttons
Diretos e tocáveis: dizem exatamente o que fazem ("Falar no WhatsApp", "Enviar e-mail", "Ver o código no GitHub").
- **Shape:** canto de placa (6px), altura mínima de 48px.
- **Principal:** fundo `--rio`, texto `--sobre-rio`, estilo rótulo, padding 16px por 32px.
- **Secundário:** fundo transparente, borda de 2px em `--tinta`, texto `--tinta`, padding vertical de 14px para compensar a borda.
- **Hover (só com mouse, `hover: hover` e `pointer: fine`):** o principal escurece no Dia (`--rio` 82% com `--tinta`) e clareia na Noite (`--rio` 82% com branco); o secundário fica azul no texto e na borda. 200ms, `ease`. No toque, nada fica preso aceso.
- **Pressão:** `scale(0.97)` em 160ms com `curva-saida`, só sem pedido de menos movimento.
- **Foco:** `outline: 3px solid var(--rio)` com 2px de afastamento, só em `:focus-visible`, sem transição.
- Nas ações do herói e do Contato, os dois botões ficam lado a lado com 16px entre eles; no celular, cada um ocupa a linha inteira.

### Links
Cor `--rio`, sublinhado de 1px afastado 0.22em. No hover (só com mouse) viram `--terra-roxa`.

### Navigation
- **Topo:** fixo, 72px, logo horizontal à esquerda (36px de altura, cerca de 185px de largura, versão Dia ou Noite conforme o tema), links das seções no centro-direita com 28px entre eles, controles à direita.
- **Item atual:** o link da seção visível fica `--rio` com sublinhado de 2px afastado 0.4em, marcado com `aria-current`.
- **Menu do celular (até 1000px):** botão "Menu" com ícone de três linhas que vira um X (`curva-movimento`, 200ms). O painel é uma placa sob o topo, com links empilhados de 1.125rem separados por `--grade`. Entra descendo 8px e aparecendo em 200ms, sai em 150ms. Ao abrir, o foco vai para o primeiro link; Esc fecha e devolve o foco ao botão; clicar num link fecha. Até 640px o seletor de tema mora dentro do menu.
- **Atalho "Pular para o conteúdo":** primeiro elemento da página, escondido até receber foco; aparece instantaneamente como um botão principal pequeno.

### Seletor de tema
Botão com borda de 2px em `--tinta`, 44px de altura, ícone (sol no Dia, lua na Noite) e a palavra do tema atual ("Dia" ou "Noite"). O nome acessível começa pela palavra visível: "Dia, mudar para Noite". A escolha fica em `localStorage` na chave `tema`, sempre dentro de `try/catch`, e um script no `<head>` aplica o tema salvo antes do CSS para a página não piscar. A troca usa View Transition na página inteira (400ms, `ease`), com as transições individuais suspensas durante a troca; o ícone novo entra girando de -90° e crescendo de 0.6 (250ms, `curva-saida`). A cor da barra do navegador (`theme-color`) acompanha a escolha manual.

### Tags
Corpo pequeno, borda de 1px em `--bronze-texto`, canto de 6px, padding 4px por 10px, 8px entre elas. A única variante de acento é a tag de status da poligonal ("Em andamento"), em `--terra-roxa` no texto e na borda.

### Legenda de serviços
Os serviços são a legenda de uma carta topográfica: uma lista aberta por um filete de 2px em `--tinta`, cada item separado por `--grade`, com um símbolo de legenda de 48px traçado em `--bronze-texto` (2.2px, pontas redondas), o nome em Título 2 e a descrição em corpo. Os símbolos são sinais de carta (estrada com eixo tracejado, curvas de nível, vértice com ponto), nunca ícones de interface genéricos.

### Poligonal (Formação)
A linha do tempo desenhada como levantamento: uma linha vertical de 2px em `--bronze-texto` liga os cursos, e cada curso é um vértice de 14px. Ano em coordenada mono, curso em Título 2, instituição em corpo `--tinta-suave`. Ordem do mais recente para o mais antigo, 56px entre vértices.

### Monografia (Projetos)
A ficha do marco, aplicada ao próprio site: uma placa (`--placa`, 16px de canto, 32px de padding) com título em Título 2 e uma lista de termos e definições em duas colunas (7.5rem e o resto), cada linha separada por `--grade`. Números medidos (como as razões de contraste) vão em negrito, algarismos tabulares e `--bronze-texto`.

### Régua de coordenadas
No pé da primeira tela, uma linha de 1px em `--grade` com três medidas lado a lado (48px entre elas): rótulos curtos em `--tinta-suave` e valores em coordenada mono. É a mesma coordenada que se repete no rodapé.

### Vértices de divisa
Um vértice de 14px sentado sobre a divisa inferior de cada seção, na margem esquerda da coluna, como as estações de um levantamento. Decorativo (`aria-hidden`).

### Terreno do herói
SVG que cobre a primeira tela (`xMaxYMid slice`): grade de coordenadas, rótulos de latitude e longitude em mono, oito curvas de nível concêntricas ao marco (duas mestras), estrelas e o disco de bronze grande, cortado pela borda direita, com dois frisos (`--bronze` 72% com preto, o `friso-escurecedor`), o símbolo da logo v4 (o sol, a estrela e as asas) gravado em `--patina` e o aro "Ícaro Gavioli · marco zero de São Paulo ·" em Archivo 700, largura 112%. De dia as curvas aparecem e as estrelas não; à noite, o contrário, por meio dos tokens `--curva` e `--estrela`.

### Fragmento de terreno do Contato
No Contato, um pedaço de terreno à direita (até 46% da largura, 640px) com curvas de nível em volta de um selo pequeno: um disco de bronze de 68px com a estrela da logo gravada em pátina, igual ao favicon e a coordenada ao lado em mono `--bronze-texto`. Some abaixo de 1000px.

### Movimento
- **O momento:** ao abrir, as curvas do herói se desenham do marco para fora (900ms, `curva-saida`, 70ms de defasagem por curva); à noite, as estrelas acendem juntas (900ms). É a única animação automática.
- **Respostas:** pressão de 160ms; cores de hover em 200ms `ease`; menu de 200ms na entrada e 150ms na saída; ícone do menu em `curva-movimento`; troca de tema em 400ms; giro do ícone do tema em 250ms.
- **Sem animação:** foco do teclado e atalho de pular conteúdo.
- **Menos movimento:** nada se desloca, gira, cresce ou se desenha (o terreno já aparece pronto, o menu só aparece, o ícone do menu só troca de opacidade, a View Transition é pulada, a rolagem deixa de ser suave). As cores continuam mudando suavemente.

### Acessibilidade
Contraste de pelo menos 4.5:1 em todo texto nos dois temas (os tokens garantem 6.3:1 ou mais no texto de leitura); foco sempre visível em `--rio`; atalho para o conteúdo; navegável só com teclado; alvos de toque de 44px ou mais; tema e menu com nomes acessíveis e `aria-expanded`; terrenos e vértices com `aria-hidden`; foto com texto alternativo; a logo no link tem `aria-label`.

## Do's and Don'ts

### Do:
- **Do** use apenas os tokens de `css/tokens.css`, copiados de `marca-icaro-gavioli/marca/tokens.css`; um valor novo nasce no livro da marca, não no site.
- **Do** dê a cada token o seu papel nos dois temas: `--rio` para ação, `--bronze` para preencher, `--bronze-texto` para escrever, `--grade` para dividir.
- **Do** use cantos de 6px em controles e tags, 16px em placas e foto, e o círculo só no disco do marco.
- **Do** separe superfícies por tom e por filete (1px `--grade`, 2px `--tinta`), nunca por sombra.
- **Do** trate cada lista como peça de levantamento: legenda de carta, poligonal, monografia, régua de coordenadas.
- **Do** restrinja hover a `(hover: hover) and (pointer: fine)` e envolva todo deslocamento, giro ou desenho em `prefers-reduced-motion: no-preference`.
- **Do** escreva rótulos de botão que digam a ação exata, em caixa normal.

### Don't:
- **Don't** use `box-shadow`, brilho, desfoque de fundo ou gradiente em nenhuma superfície.
- **Don't** use texto em maiúsculas, nem no aro do marco.
- **Don't** use a mono como enfeite técnico; ela é só para coordenadas, anos e números medidos.
- **Don't** pinte de azul o que não é clicável, nem use `--terra-roxa` para erro ou em mais de um elemento por tela.
- **Don't** use `--grade` como borda de botão ou campo.
- **Don't** espalhe curvas de nível como papel de parede; elas ficam no herói e no fragmento do Contato.
- **Don't** use asas, sóis e engrenagens como enfeite fora da logo; o sol e a lua do seletor de tema são ícone de estado, não ornamento.
- **Don't** adicione animações automáticas além do terreno sendo medido, nem nada que apareça na rolagem.
- **Don't** use estrelas de cinco pontas, bandeiras, brilhos de "IA" (✦), cartões com emoji ou numeração de seções.
