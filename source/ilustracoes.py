# -*- coding: utf-8 -*-
"""Ilustrações SVG originais para as 7 etapas do processo de projetos.

Linguagem visual comum: fundo creme arredondado, blobs suaves na cor da fase,
formas chapadas na paleta da marca e faíscas em amarelo Lumiar.
"""

PELE = ['#F3C9A4', '#D9A277', '#B0764B', '#8A5731', '#F7D9BC']
CABELO = ['#2C2116', '#5B3A21', '#1A1310', '#7A4B22', '#3D2B1F']
ROUPA = ['#E67E22', '#27AE60', '#4F63F1', '#FFC132', '#24395C', '#E84393']

FASE_COR = {
    'leaf': ('#27AE60', '#2ECC71'),
    'sun': ('#E67E22', '#FFC132'),
    'navy': ('#4F63F1', '#FFC132'),
}


# ─────────────────────────── primitivas ───────────────────────────

def _fundo(cor1, cor2):
    return (f'<rect width="480" height="360" rx="26" fill="#FFFCF6"/>'
            f'<circle cx="418" cy="54" r="96" fill="{cor1}" opacity="0.10"/>'
            f'<circle cx="52" cy="322" r="78" fill="{cor2}" opacity="0.12"/>')


def faisca(x, y, r, cor='#FFC132', op='1'):
    k = r * 0.26
    return (f'<path d="M{x} {y - r}Q{x + k} {y - k} {x + r} {y}Q{x + k} {y + k} {x} {y + r}'
            f'Q{x - k} {y + k} {x - r} {y}Q{x - k} {y - k} {x} {y - r}Z" fill="{cor}" opacity="{op}"/>')


def crianca(cx, cy, s=1.0, i=0, roupa=None, cabelo_estilo=0, olhando='frente'):
    """cy = centro da cabeça. Ombros e tronco abaixo."""
    pele = PELE[i % len(PELE)]
    cab = CABELO[i % len(CABELO)]
    rou = roupa or ROUPA[i % len(ROUPA)]

    if cabelo_estilo == 1:      # coque
        cabelos = (f'<circle cx="0" cy="-21" r="7" fill="{cab}"/>'
                   f'<path d="M-19 -1a19 19 0 0 1 38 0z" fill="{cab}"/>')
    elif cabelo_estilo == 2:    # maria-chiquinha
        cabelos = (f'<circle cx="-21" cy="-2" r="7.5" fill="{cab}"/>'
                   f'<circle cx="21" cy="-2" r="7.5" fill="{cab}"/>'
                   f'<path d="M-19 -1a19 19 0 0 1 38 0z" fill="{cab}"/>')
    elif cabelo_estilo == 3:    # cabelo comprido
        cabelos = (f'<path d="M-20 -1a20 20 0 0 1 40 0v16q0 5-5 5h-2V6H-13v14h-2q-5 0-5-5z" fill="{cab}"/>')
    else:                       # curto com franja
        cabelos = (f'<path d="M-19 -1a19 19 0 0 1 38 0q-4-8-12-8-6 3-14 2-8-1-12 6z" fill="{cab}"/>')

    dx = {'frente': 0, 'esq': -2.5, 'dir': 2.5}[olhando]

    return (f'<g transform="translate({cx},{cy}) scale({s})">'
            f'<path d="M-27 48c0-15 12-27 27-27s27 12 27 27v4a4 4 0 0 1-4 4h-46a4 4 0 0 1-4-4z" fill="{rou}"/>'
            f'<circle cx="0" cy="0" r="19.5" fill="{pele}"/>'
            f'{cabelos}'
            f'<circle cx="{-6.5 + dx}" cy="3" r="2.4" fill="#2C3E50"/>'
            f'<circle cx="{6.5 + dx}" cy="3" r="2.4" fill="#2C3E50"/>'
            f'<path d="M{-4.5 + dx} 10q4.5 4.5 9 0" stroke="#2C3E50" stroke-width="2.1" fill="none" stroke-linecap="round"/>'
            f'</g>')


def balao(x, y, w, h, fill, conteudo, rabo='baixo', stroke='none', op='1'):
    """x,y = canto superior esquerdo."""
    cx, cy = x + w / 2, y + h / 2
    if rabo == 'baixo':
        r = f'<path d="M{cx - 7} {y + h}h14l-7 11z" fill="{fill}" opacity="{op}"/>'
    elif rabo == 'cima':
        r = f'<path d="M{cx - 7} {y}h14l-7 -11z" fill="{fill}" opacity="{op}"/>'
    else:
        r = ''
    borda = f' stroke="{stroke}" stroke-width="2.5"' if stroke != 'none' else ''
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(w, h) * 0.34:.0f}" '
            f'fill="{fill}" opacity="{op}"{borda}/>{r}'
            f'<g transform="translate({cx},{cy})">{conteudo}</g></g>')


# ─────────────────────────── glifos ───────────────────────────

def g_foguete(cor='#E67E22', cor2='#FFFFFF', s=1.0):
    return (f'<g transform="scale({s})">'
            f'<path d="M0-15c4.4 0 8 6.4 8 13.5 0 4.4-1.2 7.4-2.6 9.2h-10.8C-6.8 5.9-8 2.9-8-1.5-8-8.6-4.4-15 0-15z" fill="{cor}"/>'
            f'<path d="M-8-1c-4 1.6-6.6 5-6.6 9.2L-8 6zM8-1c4 1.6 6.6 5 6.6 9.2L8 6z" fill="{cor}" opacity="0.62"/>'
            f'<circle cx="0" cy="-4" r="3.6" fill="{cor2}"/>'
            f'<path d="M-3.4 9.4h6.8l-3.4 7z" fill="#FFC132"/></g>')


def g_nota(cor='#4F63F1'):
    return (f'<g><path d="M-3 6V-9l11-3v14" stroke="{cor}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="-6.5" cy="6.5" r="4" fill="{cor}"/><circle cx="8.5" cy="3.5" r="4" fill="{cor}"/></g>')


def g_bola(cor='#27AE60'):
    return (f'<g><circle cx="0" cy="0" r="10" fill="{cor}"/>'
            f'<path d="M0-6l5 3.6-2 6h-6l-2-6z" fill="#FFFCF6"/></g>')


def g_folha(cor='#27AE60'):
    return (f'<path d="M8-9c1.6 9-2 16-9.6 17.2-4 .6-7-1.4-7.6-4.6C-9.8-.6-3.2-6.6 8-9z" fill="{cor}"/>'
            f'<path d="M6-7C-1-2-6 3-8 9" stroke="#FFFCF6" stroke-width="1.8" fill="none" stroke-linecap="round"/>')


def g_livro(cor='#E67E22'):
    return (f'<g><path d="M-10-8h8a3 3 0 0 1 3 3v14a3 3 0 0 0-3-3h-8z" fill="{cor}"/>'
            f'<path d="M10-8h-8a3 3 0 0 0-3 3v14a3 3 0 0 1 3-3h8z" fill="{cor}" opacity="0.6"/></g>')


def g_mat(cor='#4F63F1'):
    return (f'<g stroke="{cor}" stroke-width="2.6" stroke-linecap="round" fill="none">'
            f'<path d="M-9-6h7M-5.5-9.5v7M2-7h8M2 4h8M2 8h8"/>'
            f'<path d="M-9 4.5l7 7M-2 4.5l-7 7"/></g>')


def g_frasco(cor='#27AE60'):
    return (f'<g><path d="M-3-9v6l-6 10a3 3 0 0 0 2.6 4.6h12.8A3 3 0 0 0 9 7L3-3v-6z" fill="{cor}" opacity="0.75"/>'
            f'<path d="M-5-9h10" stroke="{cor}" stroke-width="2.8" stroke-linecap="round"/>'
            f'<circle cx="-1" cy="6" r="1.8" fill="#FFFCF6"/><circle cx="3" cy="9" r="1.3" fill="#FFFCF6"/></g>')


def g_globo(cor='#E67E22'):
    return (f'<g stroke="{cor}" stroke-width="2.4" fill="none"><circle cx="0" cy="0" r="9.5"/>'
            f'<path d="M-9.5 0h19M0-9.5c4 4.6 4 14.4 0 19M0-9.5c-4 4.6-4 14.4 0 19"/></g>')


def g_paleta(cor='#E84393'):
    return (f'<g><path d="M0-10c6 0 10 4.4 10 9.4 0 4-3 5.6-5.4 6.4-1.8.6-2.6 1.6-2.6 2.8 0 1.6-1.4 2.4-3 2.4C-6 11-10 6.4-10-.2-10-5.4-6-10 0-10z" fill="{cor}" opacity="0.85"/>'
            f'<circle cx="-4.5" cy="-3.5" r="2" fill="#FFFCF6"/><circle cx="1.5" cy="-5.5" r="2" fill="#FFFCF6"/>'
            f'<circle cx="5" cy="-.5" r="2" fill="#FFFCF6"/></g>')


def g_microfone(cor='#E67E22'):
    return (f'<g><rect x="-4.5" y="-12" width="9" height="15" rx="4.5" fill="{cor}"/>'
            f'<path d="M-8 -1a8 8 0 0 0 16 0" stroke="{cor}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
            f'<path d="M0 7v5M-4 12h8" stroke="{cor}" stroke-width="2.6" stroke-linecap="round"/></g>')


def g_conversa(cor='#4F63F1'):
    return (f'<g><path d="M-11-9h15a3 3 0 0 1 3 3v7a3 3 0 0 1-3 3h-8l-5 4v-4h-2a3 3 0 0 1-3-3v-7a3 3 0 0 1 3-3z" fill="{cor}"/>'
            f'<path d="M8-3h4a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-1v3l-4-3" fill="{cor}" opacity="0.5"/></g>')


def g_check(cor='#27AE60', s=1.0):
    return (f'<path transform="scale({s})" d="M-6 0.5l4.2 4.5L6.5-5" stroke="{cor}" stroke-width="3.2" '
            f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


def g_interrogacao(cor='#FFFCF6'):
    return (f'<g fill="{cor}"><path d="M-5.5-6.5c0-4 2.6-6.6 6-6.6 3.6 0 6 2.4 6 5.6 0 2.6-1.4 4-3.4 5.4C1-.6 0 .4 0 2.6v1h-4v-1.6c0-3 1.2-4.4 3.2-5.8C.8-4.8 1.6-5.6 1.6-7c0-1.4-1-2.2-2.4-2.2-1.6 0-2.6 1-2.6 2.7z"/>'
            f'<circle cx="-1" cy="9.5" r="2.8"/></g>')


# ─────────────────────────── as 7 cenas ───────────────────────────

def etapa1():
    """Semana de levantamento de interesse — a escuta."""
    c1, c2 = FASE_COR['leaf']
    s = [_fundo(c1, c2)]

    # chão
    s.append('<rect x="34" y="286" width="412" height="7" rx="3.5" fill="#1A2A44" opacity="0.08"/>')

    # tutora, de prancheta
    s.append(crianca(84, 214, 1.18, i=4, roupa='#24395C', cabelo_estilo=3, olhando='dir'))
    s.append('<g transform="translate(120,258) rotate(9)">'
             '<rect x="-15" y="-19" width="30" height="38" rx="4" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.2"/>'
             '<rect x="-8" y="-23" width="16" height="7" rx="3" fill="#E67E22"/>'
             '<path d="M-8-8h16M-8-1h16M-8 6h10" stroke="#1A2A44" stroke-width="2" stroke-linecap="round" opacity="0.45"/></g>')
    s.append('<text x="84" y="308" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="15" '
             'font-weight="700" fill="#24395C" opacity="0.75">Tutor</text>')

    # divisória suave
    s.append('<path d="M168 168v122" stroke="#1A2A44" stroke-width="2" stroke-dasharray="5 7" opacity="0.16"/>')

    # três crianças ouvidas
    for k, (x, i, est, olh) in enumerate([(232, 0, 0, 'frente'), (310, 1, 2, 'esq'), (388, 2, 1, 'dir')]):
        s.append(crianca(x, 226, 1.0, i=i, cabelo_estilo=est, olhando=olh))

    # balões de interesse — o do foguete em destaque
    s.append(balao(196, 92, 72, 66, '#FFC132', g_foguete('#E67E22', '#FFFCF6', 1.5)))
    s.append(balao(286, 122, 50, 48, '#FFFFFF', g_nota('#4F63F1'), stroke='#4F63F1'))
    s.append(balao(364, 116, 50, 48, '#FFFFFF', g_folha('#27AE60'), stroke='#27AE60'))

    s.append(faisca(178, 84, 9))
    s.append(faisca(280, 74, 6, '#E67E22'))
    s.append(faisca(432, 158, 7, '#27AE60'))

    return _svg(s, 'Uma tutora com prancheta escuta três crianças; acima de cada uma, um balão mostra seu interesse — foguete, música e natureza.')


def etapa2():
    """Interesse do ciclo — convergência."""
    c1, c2 = FASE_COR['leaf']
    s = [_fundo(c1, c2)]

    # balõezinhos individuais no topo
    peq = [(70, 44, g_foguete('#E67E22', '#FFFCF6', 0.9)), (176, 30, g_frasco('#27AE60')),
           (286, 34, g_mat('#4F63F1')), (390, 48, g_paleta('#E84393'))]
    for x, y, glifo in peq:
        s.append(balao(x, y, 58, 54, '#FFFFFF', glifo, rabo='', stroke='#1A2A44'))

    # setas convergindo
    for x0, y0 in [(99, 100), (205, 86), (315, 90), (419, 104)]:
        s.append(f'<path d="M{x0} {y0}Q{x0 + (240 - x0) * 0.42} {y0 + 52} {240 + (x0 - 240) * 0.11} 176" '
                 f'stroke="#1A2A44" stroke-width="2.4" stroke-dasharray="5 7" fill="none" opacity="0.3"/>')

    # a pergunta do ciclo
    s.append('<rect x="96" y="182" width="288" height="104" rx="34" fill="#27AE60"/>')
    s.append('<path d="M233 286h14l-7 13z" fill="#27AE60"/>')
    s.append('<g transform="translate(150,234)">' + g_interrogacao('#FFFCF6') + '</g>')
    s.append('<text x="182" y="222" font-family="Malva,Lato,sans-serif" font-size="17" font-weight="800" fill="#FFFCF6">Como um ser</text>')
    s.append('<text x="182" y="245" font-family="Malva,Lato,sans-serif" font-size="17" font-weight="800" fill="#FFFCF6">humano viveria</text>')
    s.append('<text x="182" y="268" font-family="Malva,Lato,sans-serif" font-size="17" font-weight="800" fill="#FFC132">fora da Terra?</text>')

    s.append(faisca(76, 150, 8))
    s.append(faisca(410, 200, 9, '#27AE60'))
    s.append(faisca(58, 250, 6, '#E67E22'))

    return _svg(s, 'Quatro balões com interesses diferentes convergem, por setas pontilhadas, para uma pergunta única do ciclo: como um ser humano viveria fora da Terra?')


def etapa3():
    """Nascem dois projetos."""
    c1, c2 = FASE_COR['sun']
    s = [_fundo(c1, c2)]

    # cartão do ciclo
    s.append('<rect x="30" y="70" width="188" height="222" rx="24" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.5" stroke-opacity="0.12"/>')
    s.append('<rect x="30" y="70" width="188" height="46" rx="24" fill="#24395C"/>')
    s.append('<rect x="30" y="98" width="188" height="18" fill="#24395C"/>')
    s.append('<text x="124" y="100" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="15" font-weight="800" fill="#FFC132">PROJETO DO CICLO</text>')
    # domo em marte
    s.append('<circle cx="124" cy="190" r="52" fill="#E67E22" opacity="0.14"/>')
    s.append('<path d="M82 208a42 42 0 0 1 84 0z" fill="#4F63F1" opacity="0.22"/>')
    s.append('<path d="M82 208a42 42 0 0 1 84 0" stroke="#4F63F1" stroke-width="2.6" fill="none"/>')
    s.append('<path d="M124 166v42M96 184q28-14 56 0" stroke="#4F63F1" stroke-width="2" fill="none" opacity="0.6"/>')
    s.append('<rect x="72" y="208" width="104" height="10" rx="5" fill="#E67E22"/>')
    for k, (x, i) in enumerate([(98, 0), (124, 2), (150, 1)]):
        s.append(crianca(x, 236, 0.52, i=i, cabelo_estilo=k, roupa=['#E67E22', '#27AE60', '#4F63F1'][k]))
    s.append('<text x="124" y="282" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="13.5" font-weight="700" fill="#24395C" opacity="0.7">Todos juntos</text>')

    # "+"
    s.append('<circle cx="240" cy="181" r="19" fill="#FFC132"/>')
    s.append('<path d="M240 171v20M230 181h20" stroke="#1A2A44" stroke-width="3.4" stroke-linecap="round"/>')

    # cartão individual
    s.append('<rect x="262" y="70" width="188" height="222" rx="24" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.5" stroke-opacity="0.12"/>')
    s.append('<rect x="262" y="70" width="188" height="46" rx="24" fill="#E67E22"/>')
    s.append('<rect x="262" y="98" width="188" height="18" fill="#E67E22"/>')
    s.append('<text x="352" y="100" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="15" font-weight="800" fill="#FFFFFF">PROJETO INDIVIDUAL</text>')
    s.append('<circle cx="356" cy="186" r="52" fill="#FFC132" opacity="0.28"/>')
    s.append('<g transform="translate(356,186)">' + g_foguete('#E67E22', '#FFFCF6', 2.5) + '</g>')
    s.append(crianca(356, 238, 0.52, i=0, cabelo_estilo=0, roupa='#FFC132'))
    s.append('<text x="356" y="282" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="13.5" font-weight="700" fill="#24395C" opacity="0.7">Só do Miguel</text>')

    s.append(faisca(400, 132, 8))
    s.append(faisca(66, 314, 7, '#E67E22'))

    return _svg(s, 'Dois cartões lado a lado: à esquerda o projeto do ciclo, com três crianças e uma base habitável; à direita o projeto individual, com um foguete e uma criança.')


def etapa4():
    """Mosaico + BNCC."""
    c1, c2 = FASE_COR['sun']
    s = [_fundo(c1, c2)]

    s.append('<rect x="28" y="34" width="424" height="292" rx="24" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.5" stroke-opacity="0.1"/>')
    s.append('<rect x="28" y="34" width="424" height="50" rx="24" fill="#1A2A44"/>')
    s.append('<rect x="28" y="60" width="424" height="24" fill="#1A2A44"/>')
    s.append('<circle cx="52" cy="59" r="5" fill="#E67E22"/><circle cx="70" cy="59" r="5" fill="#FFC132"/><circle cx="88" cy="59" r="5" fill="#27AE60"/>')
    s.append('<text x="240" y="65" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="16" font-weight="800" fill="#FFFCF6">MOSAICO · expectativas BNCC</text>')

    # grade de habilidades
    glifos = [g_frasco('#27AE60'), g_mat('#4F63F1'), g_livro('#E67E22'), g_globo('#E67E22'),
              g_paleta('#E84393'), g_folha('#27AE60'), g_nota('#4F63F1'), g_bola('#27AE60')]
    idx = 0
    vazias = {5, 9}
    for r in range(3):
        for c in range(4):
            x = 56 + c * 98
            y = 108 + r * 68
            n = r * 4 + c
            if n in vazias:
                s.append(f'<rect x="{x}" y="{y}" width="82" height="54" rx="14" fill="#FFC132" opacity="0.12"/>')
                s.append(f'<rect x="{x}" y="{y}" width="82" height="54" rx="14" fill="none" stroke="#E67E22" '
                         f'stroke-width="2.4" stroke-dasharray="6 6"/>')
                s.append(f'<path d="M{x + 41} {y + 18}v18M{x + 32} {y + 27}h18" stroke="#E67E22" stroke-width="2.8" stroke-linecap="round"/>')
            else:
                s.append(f'<rect x="{x}" y="{y}" width="82" height="54" rx="14" fill="#1A2A44" opacity="0.05"/>')
                s.append(f'<g transform="translate({x + 30},{y + 27})">{glifos[idx % len(glifos)]}</g>')
                s.append(f'<g transform="translate({x + 62},{y + 28})">{g_check("#27AE60", 0.85)}</g>')
                idx += 1

    s.append('<text x="240" y="316" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="13.5" '
             'font-weight="700" fill="#24395C" opacity="0.62">O tutor completa o que o projeto ainda não cobriu</text>')

    s.append(faisca(438, 108, 8))
    return _svg(s, 'Tela da plataforma Mosaico com uma grade de habilidades da BNCC: a maioria já marcada com um visto verde e duas ainda em aberto, aguardando o tutor.')


def etapa5():
    """Tutor convoca os mestres."""
    c1, c2 = FASE_COR['sun']
    s = [_fundo(c1, c2)]

    # órbita
    s.append('<circle cx="240" cy="180" r="118" fill="none" stroke="#1A2A44" stroke-width="2.4" stroke-dasharray="6 9" opacity="0.22"/>')
    s.append('<circle cx="240" cy="180" r="76" fill="#E67E22" opacity="0.08"/>')

    # centro: tutor + estudante
    s.append(crianca(216, 168, 0.86, i=4, roupa='#24395C', cabelo_estilo=3, olhando='dir'))
    s.append(crianca(268, 182, 0.66, i=0, roupa='#FFC132', cabelo_estilo=0, olhando='esq'))
    s.append('<rect x="176" y="246" width="128" height="30" rx="15" fill="#24395C"/>')
    s.append('<text x="240" y="266" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="14" font-weight="800" fill="#FFC132">TUTOR</text>')

    # mestres em órbita
    mestres = [(240, 62, g_mat('#4F63F1'), 'Matemática'), (358, 180, g_livro('#E67E22'), 'Português'),
               (122, 180, g_frasco('#27AE60'), 'Ciências'), (322, 285, g_globo('#E67E22'), 'Geografia'),
               (158, 285, g_paleta('#E84393'), 'Arte')]
    for x, y, glifo, nome in mestres:
        s.append(f'<circle cx="{x}" cy="{y}" r="27" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.4" stroke-opacity="0.14"/>')
        s.append(f'<g transform="translate({x},{y})">{glifo}</g>')
        s.append(f'<text x="{x}" y="{y + 44}" text-anchor="middle" font-family="Malva,Lato,sans-serif" '
                 f'font-size="12.5" font-weight="700" fill="#24395C" opacity="0.7">{nome}</text>')

    s.append(faisca(404, 88, 8))
    s.append(faisca(64, 120, 6, '#27AE60'))
    return _svg(s, 'No centro, o tutor com um estudante; em volta, cinco mestres especialistas representados por ícones de Matemática, Português, Ciências, Geografia e Arte.')


def etapa6():
    """O plano do trimestre."""
    c1, c2 = FASE_COR['navy']
    s = [_fundo(c1, c2)]

    s.append('<rect x="40" y="30" width="290" height="252" rx="22" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.5" stroke-opacity="0.12"/>')
    s.append('<rect x="40" y="30" width="290" height="44" rx="22" fill="#24395C"/>')
    s.append('<rect x="40" y="56" width="290" height="18" fill="#24395C"/>')
    s.append('<text x="185" y="59" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="14" '
             'font-weight="800" fill="#FFC132">PLANO DO PROJETO</text>')

    linhas = [('PROPÓSITO', '#E67E22', 92), ('OBJETIVO', '#FFC132', 152), ('PLANO', '#27AE60', 212)]
    for rot, cor, y in linhas:
        s.append(f'<rect x="64" y="{y}" width="{len(rot) * 8 + 18}" height="24" rx="12" fill="{cor}"/>')
        tcor = '#1A2A44' if cor == '#FFC132' else '#FFFFFF'
        s.append(f'<text x="{64 + (len(rot) * 8 + 18) / 2}" y="{y + 17}" text-anchor="middle" '
                 f'font-family="Malva,Lato,sans-serif" font-size="12" font-weight="800" fill="{tcor}">{rot}</text>')
        s.append(f'<rect x="64" y="{y + 32}" width="238" height="7" rx="3.5" fill="#1A2A44" opacity="0.12"/>')
        s.append(f'<rect x="64" y="{y + 44}" width="176" height="7" rx="3.5" fill="#1A2A44" opacity="0.08"/>')

    # calendário / trimestre
    s.append('<rect x="350" y="44" width="100" height="104" rx="16" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.4" stroke-opacity="0.12"/>')
    s.append('<rect x="350" y="44" width="100" height="32" rx="16" fill="#E67E22"/>')
    s.append('<rect x="350" y="62" width="100" height="14" fill="#E67E22"/>')
    s.append('<text x="400" y="67" text-anchor="middle" font-family="Malva,Lato,sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">TRIMESTRE</text>')
    for r in range(3):
        for c in range(4):
            marcado = (r * 4 + c) < 7
            cor = '#FFC132' if marcado else '#1A2A44'
            op = '1' if marcado else '0.10'
            s.append(f'<rect x="{362 + c * 20}" y="{88 + r * 19}" width="14" height="14" rx="4" fill="{cor}" opacity="{op}"/>')

    # linha de entregas
    s.append('<path d="M74 312h332" stroke="#1A2A44" stroke-width="3" stroke-linecap="round" opacity="0.16"/>')
    entregas = [(112, '#E67E22', 'Experimento'), (240, '#FFC132', 'Maquete'), (368, '#27AE60', 'Relatório')]
    for x, cor, nome in entregas:
        s.append(f'<circle cx="{x}" cy="312" r="13" fill="{cor}"/>')
        s.append(f'<circle cx="{x}" cy="312" r="5" fill="#FFFCF6"/>')
        s.append(f'<text x="{x}" y="341" text-anchor="middle" font-family="Malva,Lato,sans-serif" '
                 f'font-size="12.5" font-weight="700" fill="#24395C" opacity="0.72">{nome}</text>')

    s.append(faisca(432, 196, 8))
    return _svg(s, 'Um plano de projeto com três blocos — propósito, objetivo e plano — ao lado de um calendário do trimestre, e abaixo uma linha do tempo com três entregas combinadas.')


def etapa7():
    """Culminância e avaliação."""
    c1, c2 = FASE_COR['navy']
    s = [_fundo(c1, c2)]

    # palco
    s.append('<ellipse cx="240" cy="268" rx="150" ry="26" fill="#E67E22" opacity="0.13"/>')
    s.append('<rect x="120" y="252" width="240" height="20" rx="10" fill="#24395C"/>')

    # mesa com a maquete
    s.append('<rect x="288" y="208" width="9" height="46" rx="4.5" fill="#24395C" opacity="0.45"/>')
    s.append('<rect x="262" y="198" width="62" height="12" rx="6" fill="#24395C" opacity="0.7"/>')
    s.append('<g transform="translate(293,170)">' + g_foguete('#E67E22', '#FFFCF6', 1.9) + '</g>')

    # apresentador, apontando para a maquete
    s.append(crianca(180, 188, 1.05, i=0, roupa='#FFC132', cabelo_estilo=0, olhando='dir'))
    s.append('<path d="M200 214q28-2 46-16" stroke="#F3C9A4" stroke-width="7.5" fill="none" stroke-linecap="round"/>')
    s.append('<circle cx="249" cy="196" r="5.4" fill="#F3C9A4"/>')

    # plateia
    for k, x in enumerate([84, 128, 352, 396]):
        s.append(f'<circle cx="{x}" cy="292" r="15" fill="#1A2A44" opacity="{0.16 + k * 0.03:.2f}"/>')
        s.append(f'<path d="M{x - 22} 330a22 22 0 0 1 44 0z" fill="#1A2A44" opacity="{0.16 + k * 0.03:.2f}"/>')

    # os quatro olhares
    selos = [(64, 66, g_microfone('#E67E22'), 'Culminância'), (172, 44, g_check('#27AE60', 1.15), 'Mosaico'),
             (306, 44, f'<g>{faisca(0, 0, 11, "#FFC132")}</g>', 'Autoavaliação'), (414, 66, g_conversa('#4F63F1'), 'Devolutiva')]
    for x, y, glifo, nome in selos:
        s.append(f'<circle cx="{x}" cy="{y}" r="24" fill="#FFFFFF" stroke="#1A2A44" stroke-width="2.4" stroke-opacity="0.13"/>')
        s.append(f'<g transform="translate({x},{y})">{glifo}</g>')
        s.append(f'<text x="{x}" y="{y + 42}" text-anchor="middle" font-family="Malva,Lato,sans-serif" '
                 f'font-size="12" font-weight="700" fill="#24395C" opacity="0.72">{nome}</text>')

    s.append(faisca(240, 132, 9, '#E67E22'))
    s.append(faisca(64, 200, 7))
    return _svg(s, 'Uma criança apresenta no palco a maquete de um foguete para a plateia; acima, quatro selos representam a culminância, o registro no Mosaico, a autoavaliação e a devolutiva à família.')


def _svg(partes, alt):
    return (f'<svg viewBox="0 0 480 360" class="h-full w-full" role="img" aria-label="{alt}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(partes)}</svg>')


TODAS = [etapa1, etapa2, etapa3, etapa4, etapa5, etapa6, etapa7]


def para(n):
    """n = 1..7"""
    return TODAS[n - 1]()
