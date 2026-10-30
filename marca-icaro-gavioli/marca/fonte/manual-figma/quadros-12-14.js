// Manual da marca no Figma: quadros 12 (usos incorretos), 13 (aplicações) e 14 (encerramento).
// Arquivo "Logo - Ícaro Gavioli" (fileKey wG5rdqJ8DhLEiy5Wb9C7Y8), página "Manual da marca" (9:2).
// Ficou pendente porque o plano Starter da Figma atingiu o limite de chamadas do MCP.
// Para terminar: rodar este código com a ferramenta use_figma nesse arquivo, uma única vez.
// Os IDs abaixo são do arquivo como estava em 29/10/2026 (componentes da logo 9:112 a 9:125,
// cabeçalho 10:2, rodapé 10:5, biblioteca 9:111, quadros 10:19, 10:20 e 10:21).

const page = await figma.getNodeByIdAsync("9:2");
await figma.setCurrentPageAsync(page);
const rgb = h => ({ r: parseInt(h.slice(1,3),16)/255, g: parseInt(h.slice(3,5),16)/255, b: parseInt(h.slice(5,7),16)/255 });
const solid = h => [{ type: "SOLID", color: rgb(h) }];
await Promise.all([
  figma.loadFontAsync({ family: "Archivo" }),
  figma.loadFontAsync({ family: "Atkinson Hyperlegible Next", style: "Regular" }),
  figma.loadFontAsync({ family: "Atkinson Hyperlegible Next", style: "Bold" }),
  figma.loadFontAsync({ family: "Atkinson Hyperlegible Mono", style: "Regular" }),
]);
const DISPLAY = { family: "Archivo", style: "ExtraBold", variationSettings: { wdth: 125, wght: 800 } };
const TEXTO = { family: "Atkinson Hyperlegible Next", style: "Regular" };
const TEXTO_B = { family: "Atkinson Hyperlegible Next", style: "Bold" };
const MONO = { family: "Atkinson Hyperlegible Mono", style: "Regular" };
function txt(str, fonte, tam, cor, larg, lh) {
  const t = figma.createText();
  t.fontName = fonte; t.fontSize = tam; t.characters = str; t.fills = solid(cor);
  if (lh) t.lineHeight = { unit: "PERCENT", value: lh };
  if (fonte === DISPLAY) t.letterSpacing = { unit: "PERCENT", value: -2 };
  if (larg) { t.resize(larg, t.height); t.textAutoResize = "HEIGHT"; }
  return t;
}
function por(no, pai, x, y) { pai.appendChild(no); no.x = x; no.y = y; return no; }
function caber(inst, w, h) { inst.rescale(Math.min(w / inst.width, h / inst.height)); return inst; }
const P = {};
for (const [k, id] of Object.entries({ hDia: "9:112", simbNoite: "9:120", simbBranco: "9:121", fav: "9:124", cab: "10:2", rod: "10:5", lib: "9:111" })) P[k] = await figma.getNodeByIdAsync(id);
const ids = [];
function cabecalho(q, titulo, intro) { const c = P.cab.createInstance(); c.setProperties({ "Título#10:0": titulo, "Introdução#10:1": intro }); por(c, q, 120, 120); ids.push(c.id); }
function rodape(q, pag) { const r = P.rod.createInstance(); r.setProperties({ "Página#10:2": pag + " / 14" }); por(r, q, 120, 1000); ids.push(r.id); }
const [q12, q13, q14] = await Promise.all(["10:19", "10:20", "10:21"].map(id => figma.getNodeByIdAsync(id)));

// marca de uso incorreto, como componente
const xSvg = figma.createNodeFromSvg('<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="20" r="19" fill="#1b1f1d"/><path d="M13.5 13.5 L26.5 26.5 M26.5 13.5 L13.5 26.5" stroke="#f7f8f6" stroke-width="3.4" stroke-linecap="round"/></svg>');
const incorreto = figma.createComponentFromNode(xSvg);
incorreto.name = "Manual/Uso incorreto"; incorreto.description = "Marca os exemplos de uso incorreto da logo.";
P.lib.appendChild(incorreto); ids.push(incorreto.id);

// 12 Usos incorretos
cabecalho(q12, "Usos incorretos", "A logo só funciona inteira, na proporção e nas cores certas. Estes são os erros mais comuns.");
const erros = [
  ["Não gire", n => { n.rotation = 14; }],
  ["Não distorça", n => { const d = n.detachInstance(); for (const c of d.findAll(x => "constraints" in x)) c.constraints = { horizontal: "SCALE", vertical: "SCALE" }; d.resize(d.width * 1.25, d.height * 0.62); return d; }],
  ["Não mude as cores", n => { for (const c of n.findAll(x => "fills" in x)) { if (c.fills.length) c.fills = solid("#6a2fa0"); if ("strokes" in c && c.strokes.length) c.strokes = solid("#2e8b57"); } }],
  ["Não aplique sombra nem contorno", n => { n.effects = [{ type: "DROP_SHADOW", color: { r: 0, g: 0, b: 0, a: 0.45 }, offset: { x: 6, y: 8 }, radius: 10, spread: 0, visible: true, blendMode: "NORMAL" }]; }],
  ["Respeite a área de proteção", null],
  ["Não use a versão Dia no escuro", null],
];
erros.forEach(([rot, mexe], i) => {
  const x = 120 + (i % 3) * 570, y = 390 + Math.floor(i / 3) * 300;
  const placa = figma.createFrame(); placa.name = "Erro · " + rot; placa.resize(540, 220); placa.cornerRadius = 16; placa.clipsContent = true;
  placa.fills = solid(i === 5 ? "#0c1322" : "#f7f8f6");
  let logo = caber(P.hDia.createInstance(), 360, 90);
  placa.appendChild(logo); logo.x = (540 - logo.width) / 2; logo.y = (220 - logo.height) / 2;
  if (mexe) { const r = mexe(logo); if (r) { logo = r; logo.x = (540 - logo.width) / 2; logo.y = (220 - logo.height) / 2; } }
  if (i === 4) {
    const apertado = txt("Sites, dados e segurança", TEXTO_B, 22, "#1b1f1d");
    placa.appendChild(apertado); apertado.x = logo.x + 40; apertado.y = logo.y + logo.height - 6;
  }
  const marca = incorreto.createInstance(); placa.appendChild(marca); marca.x = 540 - 56; marca.y = 16;
  if (i === 5) { // no fundo escuro, o X inverte para continuar visível
    for (const c of marca.findAll(n => "fills" in n && n.fills.length)) c.fills = solid("#f7f8f6");
    for (const c of marca.findAll(n => "strokes" in n && n.strokes.length)) c.strokes = solid("#1b1f1d");
  }
  por(placa, q12, x, y); ids.push(placa.id);
  const legenda = txt(rot, TEXTO_B, 24, "#1b1f1d", 540); por(legenda, q12, x, y + 234); ids.push(legenda.id);
});
rodape(q12, "12");

// 13 Aplicações
cabecalho(q13, "Aplicações", "A marca no dia a dia: na aba do navegador, no e-mail, no cartão e nas redes.");
const nav = figma.createFrame(); nav.name = "Aba do navegador"; nav.resize(820, 170); nav.cornerRadius = 16; nav.fills = solid("#cdd2ce");
const aba = figma.createAutoLayout("HORIZONTAL", { name: "Aba", itemSpacing: 14 }); aba.counterAxisAlignItems = "CENTER";
aba.fills = solid("#f7f8f6"); aba.paddingLeft = aba.paddingRight = 20; aba.paddingTop = aba.paddingBottom = 14; aba.topLeftRadius = aba.topRightRadius = 12;
const favAba = P.fav.createInstance(); favAba.rescale(28 / 240); aba.appendChild(favAba);
aba.appendChild(txt("Ícaro Gavioli: sistemas que funcionam para todo mundo", TEXTO, 20, "#1b1f1d"));
nav.appendChild(aba); aba.x = 24; aba.y = 24;
const barra = figma.createFrame(); barra.name = "Endereço"; barra.resize(772, 52); barra.cornerRadius = 26; barra.fills = solid("#f7f8f6");
const url = txt("icarosilva28.github.io/my-portifolio", MONO, 20, "#4a524d"); barra.appendChild(url); url.x = 24; url.y = 14;
nav.appendChild(barra); barra.x = 24; barra.y = 96;
por(nav, q13, 120, 390); ids.push(nav.id);
const email = figma.createAutoLayout("VERTICAL", { name: "Assinatura de e-mail", itemSpacing: 14 });
email.fills = solid("#f7f8f6"); email.cornerRadius = 16; email.paddingTop = email.paddingBottom = 32; email.paddingLeft = email.paddingRight = 36;
email.primaryAxisSizingMode = "AUTO"; email.counterAxisSizingMode = "FIXED"; email.resize(820, 100);
email.appendChild(txt("Abraço,", TEXTO, 22, "#4a524d"));
const logoEmail = caber(P.hDia.createInstance(), 220, 50); email.appendChild(logoEmail);
email.appendChild(txt("Sites e apps acessíveis, análise de dados e segurança digital", TEXTO, 20, "#4a524d", 748));
email.appendChild(txt("gsilva.icaro@gmail.com · WhatsApp (19) 98849-4927", MONO, 19, "#84431a", 748));
por(email, q13, 120, 600); ids.push(email.id);
const frente = figma.createFrame(); frente.name = "Cartão · frente"; frente.resize(390, 236); frente.cornerRadius = 12; frente.fills = solid("#ebedea"); frente.strokes = solid("#cdd2ce"); frente.strokeWeight = 1;
const logoCartao = caber(P.hDia.createInstance(), 250, 60); frente.appendChild(logoCartao); logoCartao.x = (390 - logoCartao.width) / 2; logoCartao.y = (236 - logoCartao.height) / 2;
por(frente, q13, 1010, 390); ids.push(frente.id);
const verso = figma.createAutoLayout("VERTICAL", { name: "Cartão · verso", itemSpacing: 8 });
verso.fills = solid("#0c1322"); verso.cornerRadius = 12; verso.paddingTop = verso.paddingBottom = 28; verso.paddingLeft = verso.paddingRight = 28;
verso.primaryAxisSizingMode = "FIXED"; verso.counterAxisSizingMode = "FIXED"; verso.resize(390, 236);
verso.appendChild(txt("Ícaro Gavioli", TEXTO_B, 22, "#e9edf4"));
verso.appendChild(txt("Sistemas que funcionam para todo mundo.", TEXTO, 16, "#a9b3c6", 334));
verso.appendChild(txt("gsilva.icaro@gmail.com\n(19) 98849-4927\n23°33′01″S 46°38′02″W", MONO, 15, "#e3a06a", 334, 150));
por(verso, q13, 1410, 390); ids.push(verso.id);
[[P.fav, "#ebedea"], [P.simbBranco, "#0c1322"]].forEach(([comp, fundo], i) => {
  const av = figma.createFrame(); av.name = "Avatar " + (i + 1); av.resize(180, 180); av.cornerRadius = 90; av.clipsContent = true; av.fills = solid(fundo);
  const inst = caber(comp.createInstance(), i === 0 ? 180 : 140, i === 0 ? 180 : 140);
  av.appendChild(inst); inst.x = (180 - inst.width) / 2; inst.y = (180 - inst.height) / 2;
  por(av, q13, 1010 + i * 220, 680); ids.push(av.id);
});
const legAv = txt("Avatares: o favicon e o símbolo em branco sobre o céu.", TEXTO, 20, "#4a524d", 380, 140); por(legAv, q13, 1460, 720); ids.push(legAv.id);
rodape(q13, "13");

// 14 Encerramento
const estrelas = [[200,180,2.5],[420,90,2],[760,140,2],[1180,100,2.5],[1520,170,2],[1760,90,3],[150,620,2],[1820,560,2],[300,860,2],[1640,880,2.5],[980,940,2],[640,980,2]];
for (const [x, y, r] of estrelas) { const e = figma.createEllipse(); e.resize(r * 2, r * 2); e.fills = solid("#fbeee0"); e.opacity = 0.8; e.name = "Estrela"; por(e, q14, x, y); ids.push(e.id); }
const simbFim = P.simbNoite.createInstance(); simbFim.rescale(0.9); por(simbFim, q14, (1920 - simbFim.width) / 2, 170); ids.push(simbFim.id);
const fim = txt("Um ponto firme, guiado pelo céu do Sul.", DISPLAY, 76, "#e9edf4", 1400, 108); fim.textAlignHorizontal = "CENTER";
por(fim, q14, 260, 520); ids.push(fim.id);
const contatos = txt("WhatsApp (19) 98849-4927  ·  gsilva.icaro@gmail.com  ·  icarosilva28.github.io/my-portifolio", MONO, 22, "#a9b3c6");
por(contatos, q14, (1920 - contatos.width) / 2, 800); ids.push(contatos.id);
const nomeFim = txt("Ícaro Gavioli", TEXTO_B, 24, "#e3a06a"); por(nomeFim, q14, (1920 - nomeFim.width) / 2, 860); ids.push(nomeFim.id);

for (const q of [q12, q13, q14]) q.placeholder = false;
return { createdNodeIds: ids, slides: [q12.id, q13.id, q14.id] };
