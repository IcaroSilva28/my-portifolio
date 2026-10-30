# Manual da marca no Figma: especificações dos quadros 12, 13 e 14

Referência visual: o canvas "Manual da marca · quadros 12 a 14" no Claude Design (https://claude.ai/artifact/2DqonEMcZzRgtVkpaBgPX2).

Destino: arquivo "Logo - Ícaro Gavioli", página "Manual da marca", nos quadros vazios 12, 13 e 14 (1920×1080). Primeiro, tire o efeito de "carregando": selecione o quadro e desmarque o placeholder, ou apague o quadro e crie outro do mesmo tamanho no mesmo lugar.

Todas as medidas estão em px e são relativas ao canto superior esquerdo do quadro (x, y).

## O que já existe no Figma e deve ser reutilizado

- **Manual/Cabeçalho**: título e introdução. Sempre em x 120, y 120.
- **Manual/Rodapé**: a linha de baixo, com a página. Sempre em x 120, y 1000, com a propriedade Página preenchida ("12 / 14", "13 / 14").
- **Logo v4/...**: as peças da logo, no quadro "Logo v4 · componentes". Use instâncias e redimensione proporcionalmente (tecla K, ferramenta Escala).

## Cores e fontes

| Uso | Valor |
| --- | --- |
| Fundo claro | #ebedea |
| Placas e cartões | #f7f8f6 |
| Texto | #1b1f1d |
| Texto de apoio | #4a524d |
| Dados (mono) | #84431a |
| Linhas | #cdd2ce |
| Fundo escuro (céu) | #0c1322 |
| Texto no escuro | #e9edf4 |
| Apoio no escuro | #a9b3c6 |
| Dados no escuro | #e3a06a |
| Estrelas | #fbeee0, 80% de opacidade |

- **Títulos:** Archivo ExtraBold. Em Type settings › Variable, Width 125, letter spacing -2%.
- **Texto:** Atkinson Hyperlegible Next, Regular ou Bold.
- **Dados:** Atkinson Hyperlegible Mono, Regular.

## Quadro 12: Usos incorretos

Fundo #ebedea.

- **Cabeçalho:**
  - Título: "Usos incorretos".
  - Introdução: "A logo só funciona inteira, na proporção e nas cores certas. Estes são os erros mais comuns."
- **Seis placas** de 540×220, cantos de 16, fundo #f7f8f6 (a sexta em #0c1322).
  - Colunas em x 120, 690 e 1260; linhas em y 390 e 690.
  - Em cada placa, uma instância de **Logo v4/Horizontal/Dia** com 360 de largura (cerca de 70 de altura), centralizada.
  - **Marca de erro**, no canto superior direito, em x 484, y 16 dentro da placa: círculo de 40 em #1b1f1d com um X em #f7f8f6 (traço de 3,4, pontas arredondadas). Na sexta placa, cores invertidas: círculo #f7f8f6 e X #1b1f1d.
  - **Legenda** 14px abaixo de cada placa (y 624 e 924): Atkinson Bold 24, #1b1f1d.

| Placa | Legenda | O que fazer com a logo |
| --- | --- | --- |
| 1 | Não gire | Girar 14°. |
| 2 | Não distorça | Desanexar a instância (Detach), pôr as camadas internas em Scale e redimensionar para 450×43. |
| 3 | Não mude as cores | Preenchimentos em #6a2fa0 e traços em #2e8b57. |
| 4 | Não aplique sombra nem contorno | Drop shadow: X 6, Y 8, blur 10, spread 0, preto a 45%. |
| 5 | Respeite a área de proteção | Texto "Sites, dados e segurança" (Atkinson Bold 22, #1b1f1d) encostado na logo: a 40px da borda esquerda dela e 6px acima da base, sobrepondo. |
| 6 | Não use a versão Dia no escuro | Mesma logo Dia, sem mudança, sobre o fundo #0c1322. |

- **Rodapé:** Página "12 / 14".

## Quadro 13: Aplicações

Fundo #ebedea.

- **Cabeçalho:**
  - Título: "Aplicações".
  - Introdução: "A marca no dia a dia: na aba do navegador, no e-mail, no cartão e nas redes."
- **Aba do navegador:** retângulo de 820×170 em x 120, y 390, cantos de 16, fundo #cdd2ce.
  - Aba (auto layout horizontal, espaçamento 14, padding 14 × 20, fundo #f7f8f6, cantos superiores de 12) em x 24, y 24 dentro do retângulo. Dentro dela:
    - **Logo v4/Favicon/Dia** em 28×28;
    - o texto "Ícaro Gavioli: sistemas que funcionam para todo mundo" em Atkinson Regular 20.
  - Barra de endereço de 772×52 em x 24, y 96, cantos de 26, fundo #f7f8f6, com "icarosilva28.github.io/my-portifolio" em Mono 20, #4a524d, a 24 da esquerda.
- **Assinatura de e-mail:** auto layout vertical em x 120, y 600, 820 de largura, padding 32 × 36, espaçamento 14, fundo #f7f8f6, cantos de 16. De cima para baixo:
  - "Abraço," em Atkinson Regular 22, #4a524d;
  - **Logo v4/Horizontal/Dia** com 220 de largura;
  - "Sites e apps acessíveis, análise de dados e segurança digital" em Regular 20, #4a524d;
  - "gsilva.icaro@gmail.com · WhatsApp (19) 98849-4927" em Mono 19, #84431a.
- **Cartão, frente:** 390×236 em x 1010, y 390, cantos de 12, fundo #ebedea, borda de 1 em #cdd2ce, com **Logo v4/Horizontal/Dia** de 250 de largura no centro.
- **Cartão, verso:** 390×236 em x 1410, y 390, cantos de 12, fundo #0c1322. Auto layout vertical, padding 28, espaçamento 8:
  - "Ícaro Gavioli" em Bold 22, #e9edf4;
  - "Sistemas que funcionam para todo mundo." em Regular 16, #a9b3c6;
  - três linhas em Mono 15, #e3a06a, entrelinha 150%: "gsilva.icaro@gmail.com", "(19) 98849-4927" e "23°33′01″S 46°38′02″W".
- **Avatares:** dois círculos de 180, com o conteúdo recortado.
  - Primeiro em x 1010, y 680: fundo #ebedea, **Logo v4/Favicon/Dia** em 180×180.
  - Segundo em x 1230, y 680: fundo #0c1322, **Logo v4/Símbolo/Branco** com 140 de largura, centralizado.
- **Legenda dos avatares:** "Avatares: o favicon e o símbolo em branco sobre o céu." em Regular 20, #4a524d, entrelinha 140%, 340 de largura, em x 1460, y 720.
- **Rodapé:** Página "13 / 14".

## Quadro 14: Encerramento

Fundo #0c1322. Não leva cabeçalho nem rodapé.

- **Estrelas:** círculos #fbeee0 com 80% de opacidade. Diâmetro e posição (x, y):
  - 5 em (200, 180); 4 em (420, 90); 4 em (760, 140); 5 em (1180, 100);
  - 4 em (1520, 170); 6 em (1760, 90); 4 em (150, 620); 4 em (1820, 560);
  - 4 em (300, 860); 5 em (1640, 880); 4 em (980, 940); 4 em (640, 980).
- **Símbolo:** **Logo v4/Símbolo/Noite** em 90% (603×283), centralizado na horizontal (x 658), y 170.
- **Assinatura:** "Um ponto firme, guiado pelo céu do Sul." em Archivo ExtraBold, Width 125, 76, #e9edf4, entrelinha 108%, letter spacing -2%. Caixa de 1400 de largura em x 260, y 520, centralizada.
- **Contatos:** "WhatsApp (19) 98849-4927  ·  gsilva.icaro@gmail.com  ·  icarosilva28.github.io/my-portifolio" em Mono 22, #a9b3c6, centralizado no quadro, y 800.
- **Nome:** "Ícaro Gavioli" em Atkinson Bold 24, #e3a06a, centralizado, y 860.
