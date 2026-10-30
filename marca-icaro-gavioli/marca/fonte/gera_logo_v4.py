"""Gera a logo v4 da marca Ícaro Gavioli a partir do desenho original do Figma.

Fonte: fonte/figma-logo-v4.svg, exportado do arquivo "Logo - Ícaro Gavioli" (quadro "Plugin icon - 1").
O desenho é do Ícaro; este script não muda a forma, só:
  - troca as "borrachas" brancas do círculo por arcos de verdade (o desenho funciona em qualquer fundo);
  - aplica as cores da marca, em Dia, Noite e uma cor só;
  - cria a versão para tamanho pequeno, com traço e estrela reforçados.

Uso: python3 -I fonte/gera_logo_v4.py fonte/figma-logo-v4.svg assets/v4
"""
import math
import re
import sys
from pathlib import Path

FONTE = Path(sys.argv[1]).read_text()
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

CORES = {
    # sol e estrela em bronze, asas e nome na cor do texto, assinatura na cor de apoio
    "dia": {"sol": "#b0602a", "asa": "#1b1f1d", "apoio": "#4a524d"},
    "noite": {"sol": "#e3a06a", "asa": "#e9edf4", "apoio": "#a9b3c6"},
    "preto": {"sol": "#000000", "asa": "#000000", "apoio": "#000000"},
    "branco": {"sol": "#ffffff", "asa": "#ffffff", "apoio": "#ffffff"},
}


# ---------- leitura do SVG do Figma ----------

def elemento(id_):
    m = re.search(r'<(path|circle)\b[^>]*\bid="' + re.escape(id_) + r'"[^>]*/>', FONTE)
    if not m:
        raise KeyError(id_)
    return m.group(0)


def attr(el, nome):
    m = re.search(r'\b' + nome + r'="([^"]*)"', el)
    return m.group(1) if m else None


def caminho(id_):
    return attr(elemento(id_), "d")


def poligono(id_):
    """As borrachas do Figma só têm retas (M/L/Z)."""
    nums = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', caminho(id_))]
    return list(zip(nums[0::2], nums[1::2]))


def dentro(p, poli):
    x, y = p
    res = False
    for i in range(len(poli)):
        (x1, y1), (x2, y2) = poli[i - 1], poli[i]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            res = not res
    return res


def arcos_visiveis(cx, cy, r, borrachas, passo=0.25):
    """Trechos do círculo que as borrachas brancas não cobriam, como arcos SVG."""
    polis = [poligono(b) for b in borrachas]
    n = int(360 / passo)
    vis = []
    for i in range(n):
        a = math.radians(i * passo)
        p = (cx + r * math.cos(a), cy + r * math.sin(a))
        vis.append(not any(dentro(p, q) for q in polis))
    if all(vis):
        return f"M{cx - r} {cy}a{r} {r} 0 1 0 {2 * r} 0a{r} {r} 0 1 0 {-2 * r} 0"
    ini = vis.index(False)  # começa num ponto apagado para não cortar um trecho visível no meio
    trechos, atual = [], None
    for k in range(1, n + 1):
        i = (ini + k) % n
        if vis[i] and atual is None:
            atual = [i, i]
        elif vis[i]:
            atual[1] = i
        elif atual is not None:
            trechos.append(atual)
            atual = None
    if atual is not None:
        trechos.append(atual)
    d = []
    for a0, a1 in trechos:
        t0, t1 = math.radians(a0 * passo), math.radians(a1 * passo)
        if t1 < t0:
            t1 += 2 * math.pi
        x0, y0 = cx + r * math.cos(t0), cy + r * math.sin(t0)
        x1, y1 = cx + r * math.cos(t1), cy + r * math.sin(t1)
        grande = 1 if t1 - t0 > math.pi else 0
        d.append(f"M{x0:.3f} {y0:.3f}A{r} {r} 0 {grande} 1 {x1:.3f} {y1:.3f}")
    return "".join(d)


# ---------- peças ----------

def asas(ids, cor):
    return "".join(f'<path d="{caminho(i)}" fill="{cor}" stroke="{cor}" stroke-width="0.2"/>' for i in ids)


def estrela(id_, cor, escala=1.0, centro=None):
    d = caminho(id_)
    if escala == 1.0:
        return f'<path d="{d}" fill="{cor}"/>'
    cx, cy = centro
    return f'<path d="{d}" fill="{cor}" transform="translate({cx} {cy}) scale({escala}) translate({-cx} {-cy})"/>'


def traco(d, cor, largura=0.5):
    return f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{largura}"/>'


def texto(id_, cor):
    return f'<path d="{caminho(id_)}" fill="{cor}"/>'


def circulo_completo(id_):
    el = elemento(id_)
    return float(attr(el, "cx")), float(attr(el, "cy")), float(attr(el, "r"))


def svg(vb, corpo, rotulo):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {w:g} {h:g}" role="img" aria-label="{rotulo}">'
            f'<title>{rotulo}</title>{corpo}</svg>\n')


def simbolo(c, pequeno=False):
    cx, cy, r = circulo_completo("Ellipse 1")
    arco = arcos_visiveis(cx, cy, r, ["Vector 6", "Vector 7", "Vector 4", "Vector 5"])
    alas = ["Vector 1", "Vector 2", "Vector 3", "Vector 1_2", "Vector 2_2", "Vector 3_2"]
    largura, esc = (1.4, 2.6) if pequeno else (0.5, 1.0)
    return (traco(arco, c["sol"], largura) + asas(alas, c["asa"])
            + estrela("Star 1", c["sol"], esc, (cx, cy)))


def vertical(c):
    cx, cy, r = circulo_completo("Ellipse 1_2")
    arco = arcos_visiveis(cx, cy, r, ["Vector 6_2", "Vector 7_2", "Vector 4_2", "Vector 5_2"])
    alas = ["Vector 1_6", "Vector 2_6", "Vector 3_6", "Vector 1_7", "Vector 2_7", "Vector 3_7"]
    ponto = elemento("Ellipse 4")
    return (traco(arco, c["sol"]) + asas(alas, c["asa"]) + estrela("Star 1_5", c["sol"])
            + texto("ICARO", c["asa"]) + texto("GAVIOLI", c["asa"])
            + f'<circle cx="{attr(ponto, "cx")}" cy="{attr(ponto, "cy")}" r="{attr(ponto, "r")}" fill="{c["sol"]}"/>')


def horizontal(c, assinatura=False):
    if assinatura:
        alas, est, arco, nome = ["Vector 1_5", "Vector 2_5", "Vector 3_5"], "Star 1_4", "Ellipse 3_2", "ICAR_2"
    else:
        alas, est, arco, nome = ["Vector 1_4", "Vector 2_4", "Vector 3_4"], "Star 1_3", "Ellipse 3", "ICAR"
    corpo = traco(caminho(arco), c["sol"]) + asas(alas, c["asa"]) + estrela(est, c["sol"]) + texto(nome, c["asa"])
    if assinatura:
        corpo += texto("Um ponto firme, guiado pelo c&#195;&#169;u do Sul.", c["apoio"])
    return corpo


def reduzido(c, pequeno=False):
    alas = ["Vector 1_3", "Vector 2_3", "Vector 3_3"]
    largura, esc = (1.3, 2.4) if pequeno else (0.5, 1.0)
    return traco(caminho("Ellipse 2"), c["sol"], largura) + asas(alas, c["asa"]) + estrela("Star 1_2", c["sol"], esc, (90.5, 105.5))


# caixas de corte (x, y, largura, altura) no quadro de 128 do Figma, com respiro
PECAS = {
    "simbolo": ((2.5, 3, 67, 31.5), simbolo, "Ícaro Gavioli: o sol, a estrela e as asas"),
    "logo-vertical": ((56.5, 22, 67, 37.5), vertical, "Ícaro Gavioli"),
    "logo-horizontal": ((8.5, 89.2, 58.6, 11.4), horizontal, "Ícaro Gavioli"),
    "logo-horizontal-assinatura": ((8.5, 108.2, 58.6, 13.4), lambda c: horizontal(c, True), "Ícaro Gavioli: um ponto firme, guiado pelo céu do Sul."),
    "simbolo-reduzido": ((82, 97, 41, 18), reduzido, "Ícaro Gavioli: o sol com uma asa"),
}

for nome, (vb, desenha, rotulo) in PECAS.items():
    for tema, c in CORES.items():
        (OUT / f"{nome}-{tema}.svg").write_text(svg(vb, desenha(c), rotulo))

# favicon: a logo é larga demais para um quadrado de 16px, então fica o coração dela,
# o círculo com a estrela, como um disco de bronze com a estrela gravada
DISCO = {
    "dia": ("#b0602a", "#f4e4d1"),
    "noite": ("#bd6b32", "#fbeee0"),
    "preto": ("#000000", "#ffffff"),
    "branco": ("#ffffff", "#000000"),
}


def estrela_regular(cx, cy, r, pontas=8, miolo=0.382):
    """A estrela do Figma (raio interno de 38,2%), sem o achatamento da caixa do nó."""
    pts = []
    for k in range(2 * pontas):
        a = math.pi * k / pontas
        rk = r if k % 2 == 0 else r * miolo
        pts.append(f"{cx + rk * math.sin(a):.3f} {cy - rk * math.cos(a):.3f}")
    return "M" + "L".join(pts) + "Z"


def favicon(tema):
    disco, gravacao = DISCO[tema]
    # no manual, a estrela do favicon tem 58,5 de largura num disco de 98
    return (f'<circle cx="50" cy="50" r="49" fill="{disco}"/>'
            f'<path d="{estrela_regular(50, 50, 29.25)}" fill="{gravacao}"/>')


# tamanho pequeno: o traço de 0,5 e a estrela de 2 unidades somem abaixo de 64px
for tema in ("dia", "noite", "preto", "branco"):
    c = CORES[tema]
    (OUT / f"simbolo-pequeno-{tema}.svg").write_text(svg((2, 2.5, 68, 32), simbolo(c, True), "Ícaro Gavioli"))
    (OUT / f"favicon-{tema}.svg").write_text(svg((0, 0, 100, 100), favicon(tema), "Ícaro Gavioli"))

print("\n".join(sorted(p.name for p in OUT.iterdir())))
