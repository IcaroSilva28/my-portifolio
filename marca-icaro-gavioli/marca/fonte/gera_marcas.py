"""Gera os símbolos, favicons e logos (com o nome em curvas) da marca Ícaro Silva.

A logo oficial (v3, Sol e asa) vai para assets/v3/, o Vértice (v2) para assets/v2/
e as outras opções desenhadas pelo caminho para assets/exploracoes/.
"""
import sys
from math import cos, radians, sin
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT = Path(sys.argv[1])
ASSETS = Path(sys.argv[2])

C = {
    "dia": {"tinta": "#1b1f1d", "bronze": "#b0602a", "bronze_escuro": "#84431a", "patina": "#f4e4d1", "traco": "#b0602a"},
    "noite": {"tinta": "#e9edf4", "bronze": "#bd6b32", "bronze_escuro": "#8f4d1f", "patina": "#fbeee0", "traco": "#e3a06a"},
}


def svg(view_w, view_h, body, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {view_w:g} {view_h:g}" role="img" aria-label="{label}">'
        f"<title>{label}</title>{body}</svg>\n"
    )


# ---------- símbolos (grade 100 x 100) ----------

def vertice(t, favicon=False):
    c = C[t]
    anel = "" if favicon else f'<circle cx="50" cy="50" r="41.5" fill="none" stroke="{c["bronze_escuro"]}" stroke-width="2"/>'
    sw, r = (9, 7) if favicon else (6.5, 5.5)
    return (
        f'<circle cx="50" cy="50" r="49" fill="{c["bronze"]}"/>{anel}'
        f'<path d="M50 24 L74.5 66.45 L25.5 66.45 Z" fill="none" stroke="{c["patina"]}" stroke-width="{sw}" stroke-linejoin="round"/>'
        f'<circle cx="50" cy="52.3" r="{r}" fill="{c["patina"]}"/>'
    )


def visada(t, favicon=False):
    # o í fica de pé sobre a linha do chão, e o acento é a visada que mira uma estrela
    c = C[t]
    if favicon:
        # abaixo de 120px o desenho ganha o disco de bronze para não sumir
        return (
            f'<circle cx="50" cy="50" r="49" fill="{c["bronze"]}"/>'
            f'<path d="M24 74 H76" stroke="{c["patina"]}" stroke-width="7" stroke-linecap="round"/>'
            f'<rect x="40.5" y="44" width="15" height="31" rx="2" fill="{c["patina"]}"/>'
            f'<path d="M52 36 L62.5 24.5" stroke="{c["patina"]}" stroke-width="8" stroke-linecap="round"/>'
            f'<circle cx="70.5" cy="16.5" r="6.5" fill="{c["patina"]}"/>'
        )
    return (
        f'<path d="M16 84 H84" stroke="{c["tinta"]}" stroke-width="6" stroke-linecap="round"/>'
        f'<rect x="41" y="44" width="14" height="41" rx="2" fill="{c["tinta"]}"/>'
        f'<path d="M52 35 L66 19.5" stroke="{c["traco"]}" stroke-width="7.5" stroke-linecap="round"/>'
        f'<circle cx="75.5" cy="10" r="6" fill="{c["traco"]}"/>'
    )


# Cruzeiro do Sul visto do Brasil, com Gacrux no alto. Posições pela ascensão reta e
# declinação reais, raios pela magnitude. A quinta estrela é a Intrometida (Epsilon Crucis).
ESTRELAS = [  # x, y, raio
    (50.4, 18.5, 5.2),   # Gacrux
    (71.5, 35.8, 3.8),   # Delta Crucis
    (28.7, 45.8, 5.8),   # Mimosa (Becrux)
    (63.2, 53.2, 2.6),   # Intrometida (Epsilon Crucis)
    (56.4, 81.5, 6.5),   # Acrux
]


CEU_DO_SUL = "#0f1a33"


def cruzeiro(t, favicon=False):
    # aro de bronze do marco com o céu do Sul no centro
    c = C[t]
    miolo = 36 if favicon else 39
    escala = miolo / 46
    k = 1.35 if favicon else 0.95
    pontos = "".join(
        f'<circle cx="{50 + (x - 50) * escala:.2f}" cy="{50 + (y - 50) * escala:.2f}" r="{r * k:.2f}" fill="{c["patina"]}"/>'
        for x, y, r in ESTRELAS
    )
    return (
        f'<circle cx="50" cy="50" r="49" fill="{c["bronze"]}"/>'
        f'<circle cx="50" cy="50" r="{miolo}" fill="{CEU_DO_SUL}"/>{pontos}'
    )


# ---------- sol e asa (a v1 redesenhada no mundo do marco) ----------

def polar(cx, cy, r, graus):
    a = radians(graus)
    return cx + r * cos(a), cy - r * sin(a)


def pena(p, phi, ini, fim, larg, bico=10):
    """Pena angular: sai de p na direção phi, com a ponta cortada em bisel no bordo de ataque."""
    dx, dy = cos(radians(phi)), -sin(radians(phi))
    nx, ny = -dy * larg / 2, dx * larg / 2
    bx, by = p[0] + dx * ini, p[1] + dy * ini
    tx, ty = p[0] + dx * fim, p[1] + dy * fim
    mx, my = p[0] + dx * (fim - bico), p[1] + dy * (fim - bico)
    pts = [(bx - nx, by - ny), (tx - nx, ty - ny), (mx + nx, my + ny), (bx + nx, by + ny)]
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + " Z"


def contorno_engrenagem(cx, cy, r_corpo, r_dente, dentes, meia_base, meia_topo, de, ate):
    """Contorno de engrenagem entre os ângulos de e ate (sentido anti-horário), dentes nos ângulos dados."""
    pts = [polar(cx, cy, r_corpo, de)]
    for a in dentes:
        pts += [polar(cx, cy, r_corpo, a - meia_base), polar(cx, cy, r_dente, a - meia_topo),
                polar(cx, cy, r_dente, a + meia_topo), polar(cx, cy, r_corpo, a + meia_base)]
    pts.append(polar(cx, cy, r_corpo, ate))
    return pts


def caminho(pts, fechar=True):
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + (" Z" if fechar else "")


def furo(cx, cy, r):
    return f"M{cx - r:.2f} {cy:.2f} a{r} {r} 0 1 0 {2 * r} 0 a{r} {r} 0 1 0 {-2 * r} 0 Z"


def engrenagem_solar(t, favicon=False):
    # o sol é meia engrenagem: os dentes são os raios. A asa é de penas chapadas com rebites.
    c = C[t]
    if favicon:
        dentes = [108, 144, 180, 216, 252]
        meia = caminho(contorno_engrenagem(46, 50, 15, 23, dentes, 11, 8, 90, 270))
        penas = "".join(f'<path d="{pena((50, 54), f, 2, l, 12, 9)}"/>' for f, l in [(40, 40), (10, 42), (-20, 34)])
        return (
            f'<circle cx="50" cy="50" r="49" fill="{c["bronze"]}"/>'
            f'<path fill="{c["patina"]}" fill-rule="evenodd" d="{meia} M46 45 A5 5 0 0 0 46 55 Z"/>'
            f'<g fill="{c["patina"]}">{penas}</g>'
        )
    dentes = [105, 135, 165, 195, 225, 255]
    meia = caminho(contorno_engrenagem(54, 50, 22, 31, dentes, 9, 7, 90, 270))
    angulos = [(50, 62), (28, 66), (6, 62), (-16, 54), (-38, 42)]
    penas = "".join(f'<path d="{pena((57, 54), f, 3, l, 11)}"/>' for f, l in angulos)
    rebites = "".join(
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.2"/>' for x, y in (polar(57, 54, 16, f) for f, _ in angulos)
    )
    return (
        f'<path d="M54 6 V94" stroke="{c["traco"]}" stroke-width="3" stroke-linecap="round"/>'
        f'<path fill="{c["bronze"]}" fill-rule="evenodd" d="{meia} M54 43 A7 7 0 0 0 54 57 Z"/>'
        f'<g fill="{c["tinta"]}">{penas}</g><g fill="{c["bronze"]}">{rebites}</g>'
    )


def sol_e_asa(t, favicon=False):
    # a composição da v1 em traço único: meio sol, linha divisória e asa articulada numa engrenagem
    c = C[t]
    if favicon:
        raios = "".join(
            f'<path d="M{polar(44, 50, 23, a)[0]:.2f} {polar(44, 50, 23, a)[1]:.2f} L{polar(44, 50, 31, a)[0]:.2f} {polar(44, 50, 31, a)[1]:.2f}"/>'
            for a in (135, 180, 225)
        )
        meia = caminho(contorno_engrenagem(44, 50, 11, 17, [-60, -20, 20, 60], 13, 9, -90, 90))
        penas = "".join(
            f'<path d="{pena(polar(44, 50, 20, ab), f, 0, l, 9, 7)}"/>'
            for ab, f, l in [(45, 24, 26), (5, 4, 32), (-35, -18, 24)]
        )
        return (
            f'<circle cx="50" cy="50" r="49" fill="{c["bronze"]}"/>'
            f'<g fill="none" stroke="{c["patina"]}" stroke-width="7" stroke-linecap="round">'
            f'<path d="M44 34 A16 16 0 0 0 44 66"/>{raios}</g>'
            f'<path fill="{c["patina"]}" fill-rule="evenodd" d="{meia} M44 46 A4 4 0 0 1 44 54 Z"/>'
            f'<g fill="{c["patina"]}">{penas}</g>'
        )
    raios = []
    for i, a in enumerate([126, 153, 180, 207, 234]):
        (x1, y1), (x2, y2) = polar(56, 50, 25, a), polar(56, 50, 38 if i % 2 == 0 else 32, a)
        raios.append(f'<path d="M{x1:.2f} {y1:.2f} L{x2:.2f} {y2:.2f}"/>')
    # como na v1: a engrenagem é cortada ao meio pela linha, espelhando o meio sol,
    # e as penas nascem do aro dela
    centro = (56, 50)
    meia = caminho(contorno_engrenagem(*centro, 19, 25.5, [-75, -50, -25, 0, 25, 50, 75], 7, 5, -90, 90))
    vaos = janelas(*centro, 7.5, 14, [(-80, -36), (-24, 24), (36, 80)])
    penas, veios = [], []
    for angulo_base, direcao, comprimento in PENAS_SOL_E_ASA:
        base = polar(*centro, 30, angulo_base)
        penas.append(f'<path d="{pena(base, direcao, 0, comprimento, 8, 8)}"/>')
        (x1, y1), (x2, y2) = polar(*base, 4, direcao), polar(*base, comprimento - 10, direcao)
        veios.append(f'<path d="M{x1:.2f} {y1:.2f} L{x2:.2f} {y2:.2f}"/>')
    return (
        f'<g fill="none" stroke="{c["traco"]}" stroke-width="3.5" stroke-linecap="round">'
        f'<path d="M56 6 V94" stroke-width="3"/><path d="M56 32 A18 18 0 0 0 56 68"/>{"".join(raios)}</g>'
        f'<g fill="none" stroke="{c["tinta"]}" stroke-width="2.6" stroke-linejoin="round">{"".join(penas)}</g>'
        f'<g fill="none" stroke="{c["traco"]}" stroke-width="1.8" stroke-linecap="round">{"".join(veios)}</g>'
        f'<path fill="{c["bronze"]}" fill-rule="evenodd" d="{meia}{vaos}"/>'
    )


# (ângulo da base no aro da engrenagem, direção da pena, comprimento)
PENAS_SOL_E_ASA = [(40, 40, 40), (16, 26, 53), (-8, 12, 57), (-32, -2, 50), (-56, -16, 40)]


def janelas(cx, cy, r_in, r_out, faixas):
    """Vãos em forma de setor de anel, para a engrenagem ter cara de roda como na v1."""
    d = ""
    for a1, a2 in faixas:
        (x1, y1), (x2, y2) = polar(cx, cy, r_out, a1), polar(cx, cy, r_out, a2)
        (x3, y3), (x4, y4) = polar(cx, cy, r_in, a2), polar(cx, cy, r_in, a1)
        d += (f" M{x1:.2f} {y1:.2f} A{r_out} {r_out} 0 0 0 {x2:.2f} {y2:.2f}"
              f" L{x3:.2f} {y3:.2f} A{r_in} {r_in} 0 0 1 {x4:.2f} {y4:.2f} Z")
    return d


def vertice_alado(t, favicon=False):
    # o vértice no centro, raios do sol à esquerda e uma asa de três penas rebitadas à direita
    if favicon:
        return vertice(t, favicon=True)
    c = C[t]
    p = (62, 54)
    angulos = [(38, 74), (16, 82), (-6, 72)]
    penas = "".join(f'<path d="{pena(p, f, 0, l, 14, 12)}"/>' for f, l in angulos)
    rebites = "".join(
        f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.4"/>' for x, y in (polar(*p, 47, f) for f, _ in angulos)
    )
    raios = []
    for i, a in enumerate([135, 157.5, 180, 202.5, 225]):
        (x1, y1), (x2, y2) = polar(*p, 45, a), polar(*p, 54 if i % 2 == 0 else 50, a)
        raios.append(f'<path d="M{x1:.2f} {y1:.2f} L{x2:.2f} {y2:.2f}"/>')
    k = 40 / 49
    return (
        f'<g fill="{c["tinta"]}">{penas}</g><g fill="{c["bronze"]}">{rebites}</g>'
        f'<g stroke="{c["traco"]}" stroke-width="3.5" stroke-linecap="round">{"".join(raios)}</g>'
        f'<g transform="translate({p[0] - 50 * k:.2f} {p[1] - 50 * k:.2f}) scale({k:.4f})">{vertice(t)}</g>'
    )


# chave: (desenho, rótulo, largura da grade; a altura é sempre 100)
SIMBOLOS = {
    "vertice": (vertice, "Ícaro Silva: vértice de um marco geodésico", 100),
    "visada": (visada, "Ícaro Silva: í plantado no chão, com o acento mirando uma estrela", 100),
    "cruzeiro": (cruzeiro, "Ícaro Silva: o Cruzeiro do Sul, com a Intrometida, num marco de bronze", 100),
    "sol-e-asa": (sol_e_asa, "Ícaro Silva: meio sol e asa presa a uma engrenagem cortada ao meio", 146),
    "engrenagem-solar": (engrenagem_solar, "Ícaro Silva: sol de engrenagem e asa de penas rebitadas", 126),
    "vertice-alado": (vertice_alado, "Ícaro Silva: o vértice com raios de sol e asa mecânica", 146),
}


# ---------- nome em curvas ----------

def nome_em_curvas(texto, tamanho, tracking_em, cor):
    font = TTFont(FONT)
    upem = font["head"].unitsPerEm
    blob = hb.Blob.from_file_path(str(FONT))
    hbfont = hb.Font(hb.Face(blob))
    buf = hb.Buffer()
    buf.add_str(texto)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": True})
    glyf = font.getGlyphSet()
    order = font.getGlyphOrder()
    escala = tamanho / upem
    x = 0.0
    caminhos = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        nome = order[info.codepoint]
        pen = SVGPathPen(glyf)
        # fonte tem y para cima; SVG tem y para baixo
        tpen = TransformPen(pen, (escala, 0, 0, -escala, x + pos.x_offset * escala, -pos.y_offset * escala))
        glyf[nome].draw(tpen)
        d = pen.getCommands()
        if d:
            caminhos.append(d)
        x += pos.x_advance * escala + tracking_em * tamanho
    largura = x - tracking_em * tamanho
    cap = font["OS/2"].sCapHeight * escala
    return f'<path fill="{cor}" d="{" ".join(caminhos)}"/>', largura, cap


def logo(chave, t):
    desenha, rotulo, largura_simbolo = SIMBOLOS[chave]
    c = C[t]
    tamanho = 50
    nome, largura, cap = nome_em_curvas("Ícaro Silva", tamanho, -0.01, c["tinta"])
    gap = 26
    baseline = 50 + cap / 2  # centro óptico do nome alinhado ao centro do símbolo
    corpo = f"<g>{desenha(t)}</g><g transform=\"translate({largura_simbolo + gap} {baseline:.2f})\">{nome}</g>"
    w = largura_simbolo + gap + largura + 2
    return svg(round(w, 1), 100, corpo, rotulo.split(":")[0])


# chave: (pasta, nome nos arquivos)
DESTINOS = {
    "sol-e-asa": ("v3", "icaro-silva"),
    "vertice": ("v2", "vertice"),
    "visada": ("exploracoes", "visada"),
    "cruzeiro": ("exploracoes", "cruzeiro"),
    "engrenagem-solar": ("exploracoes", "engrenagem-solar"),
    "vertice-alado": ("exploracoes", "vertice-alado"),
}

for chave, (desenha, rotulo, largura_simbolo) in SIMBOLOS.items():
    pasta, nome = DESTINOS[chave]
    out = ASSETS / pasta
    out.mkdir(parents=True, exist_ok=True)
    for t in ["dia", "noite"]:
        (out / f"simbolo-{nome}-{t}.svg").write_text(svg(largura_simbolo, 100, desenha(t), rotulo))
        (out / f"favicon-{nome}-{t}.svg").write_text(svg(100, 100, desenha(t, favicon=True), rotulo))
        (out / f"logo-{nome}-{t}.svg").write_text(logo(chave, t))
        print(f"{pasta}/logo-{nome}-{t}.svg")
