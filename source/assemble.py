# -*- coding: utf-8 -*-
import base64, pathlib, urllib.parse, re
import processo

B = pathlib.Path('/home/claude/lumiar/build')
UP = pathlib.Path('/mnt/user-data/uploads/Novo Site Lumiar/Design System')

WA_NUM = '553537218751'

def wa(msg):
    return 'https://wa.me/%s?text=%s' % (WA_NUM, urllib.parse.quote(msg))

# ─────────── Logos ───────────
logo_raw = (UP / 'Logo' / 'Lumiar-Logo-Yellow.svg').read_text(encoding='utf-8')
logo_body = logo_raw.split('>', 1)[1] if logo_raw.startswith('<?xml') else logo_raw
m = re.search(r'<svg.*?</svg>', logo_raw, re.S)
logo_svg_full = m.group(0)
# limpa e aplica classes
logo_inline = re.sub(r'<svg[^>]*?viewBox="([^"]+)"[^>]*>',
                     r'<svg viewBox="\1" class="h-[26px] w-auto sm:h-[28px]" role="img" aria-label="Lumiar" xmlns="http://www.w3.org/2000/svg">',
                     logo_svg_full, count=1, flags=re.S)
logo_inline = logo_inline.replace('<style type="text/css">\n\t.st0{fill:#FFC132;}\n</style>', '<style>.st0{fill:#FFC132}</style>')

sym_raw = (UP / 'Symbol' / 'Lumiar-Symbol-Yellow.svg').read_text(encoding='utf-8')
sym_svg = re.search(r'<svg.*?</svg>', sym_raw, re.S).group(0)
favicon = 'data:image/svg+xml;base64,' + base64.b64encode(sym_svg.encode('utf-8')).decode()

# rodapé usa a versão branca
sym_white = re.search(r'<svg.*?</svg>', (UP / 'Symbol' / 'Lumiar-Symbol-White.svg').read_text(encoding='utf-8'), re.S).group(0)
logo_white_raw = (UP / 'Logo' / 'Lumiar-Logo-White.svg').read_text(encoding='utf-8')
logo_white = re.search(r'<svg.*?</svg>', logo_white_raw, re.S).group(0)
logo_white = re.sub(r'<svg[^>]*?viewBox="([^"]+)"[^>]*>',
                    r'<svg viewBox="\1" class="h-[34px] w-auto" role="img" aria-label="Lumiar" xmlns="http://www.w3.org/2000/svg">',
                    logo_white, count=1, flags=re.S)

# ─────────── Ícones ───────────
WA_PATH = ('<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164'
           '-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606'
           '.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207'
           '-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074'
           '.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413'
           '.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214'
           '-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884a9.82 9.82 0 0 1 6.988 2.896'
           '9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892'
           'c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893'
           'A11.821 11.821 0 0 0 20.885 3.4"/>')

def wa_icon(cls):
    return '<svg class="%s" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">%s</svg>' % (cls, WA_PATH)

ICON_WA = wa_icon('h-[19px] w-[19px]')
ICON_WA_SM = wa_icon('h-4 w-4')
ICON_WA_DARK = wa_icon('h-[19px] w-[19px]')

# ─────────── Selos ───────────
def selo(txt):
    return ('<span class="flex items-center gap-2.5 text-[13px] font-bold uppercase tracking-[0.16em] text-navy-800/45">'
            '<svg class="h-3.5 w-3.5 text-sun-600" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
            '<path d="m12 2 2.6 6.6L21.5 9l-5.2 4.4 1.7 6.9L12 16.6 6 20.3l1.7-6.9L2.5 9l6.9-.4z"/></svg>%s</span>') % txt

SELOS = ''.join(selo(t) for t in [
    'UNESCO', 'Stanford University', 'Microsoft', 'Top 12 mundial em inovação',
    'Autorizada SEE-MG · Res. 107/2019', 'Poços de Caldas desde 2018'])

# ─────────── Ciclos ───────────
CICLOS = [
    dict(id='i3', ativo=True, tag='2 a 5 anos · Infantil', cor='leaf',
         titulo='Educação Infantil',
         foco='Acolhimento, adaptação e turma reduzida',
         texto='A entrada na escola é um momento delicado — e aqui ela é conduzida no ritmo da criança. Cada família recebe um plano de adaptação individual, e o mesmo tutor acompanha o grupo o ano inteiro, criando o vínculo que dá segurança para explorar.',
         itens=['Plano de adaptação individual, feito com a família',
                'Brincar como linguagem central de aprendizagem',
                'Rotina ao ar livre na área verde, todos os dias',
                'Registro diário do dia da criança no Mosaico Digital'],
         slot='Foto real · roda de crianças na área externa'),
    dict(id='f1', ativo=False, tag='6 a 10 anos · 1º ao 5º ano', cor='sun',
         titulo='Fundamental 1',
         foco='Alfabetização, descoberta e projetos',
         texto='A fase em que ler e escrever deixa de ser tarefa e vira ferramenta. Os projetos partem de perguntas dos próprios estudantes e atravessam matemática, ciências, arte e linguagem — com acompanhamento individual de leitura e escrita.',
         itens=['Acompanhamento individual de leitura e escrita',
                'Projetos investigativos com produto final apresentado',
                'Oficinas com mestres especialistas (Português, Matemática)',
                'Multietariedade: aprender com e ensinar aos colegas'],
         slot='Foto real · projeto em grupo na sala'),
    dict(id='f2', ativo=False, tag='11 a 14 anos · 6º ao 9º ano', cor='navy',
         titulo='Fundamental 2',
         foco='Mentoria, protagonismo e saúde mental',
         texto='É a fase em que a maioria das escolas perde o adolescente para a turma de 40 alunos. Aqui, cada estudante tem um tutor que conhece seu momento, seus projetos e suas dificuldades — e uma assembleia (A Roda) onde sua voz tem peso real nas decisões da escola.',
         itens=['Tutoria individual com conversas periódicas de percurso',
                'A Roda: assembleia com voz e voto do estudante',
                'Projetos autorais com apresentação pública',
                'Preparação sólida para o Ensino Médio, sem massacre de apostila'],
         slot='Foto real · adolescente apresentando projeto'),
    dict(id='em', ativo=False, tag='15 a 17 anos · Ensino Médio', cor='sun',
         titulo='Ensino Médio',
         foco='Orientação de futuro e projetos reais',
         texto='Currículo em Mosaico articulado às exigências do ENEM e dos vestibulares, com itinerários construídos a partir do projeto de vida de cada estudante. Aprender fazendo — com entregas que valem para o portfólio e para a vida.',
         itens=['Itinerários formativos alinhados ao projeto de vida',
                'Preparação para ENEM e vestibulares integrada aos projetos',
                'Mentoria de carreira e experiências fora da escola',
                'Avaliação integrada e contínua, sem surpresa no fim do ano'],
         slot='Foto real · estudante do Médio em projeto'),
]

CORES = {
    'leaf': dict(chip='bg-leaf-500/12 text-leaf-600', dot='text-leaf-500'),
    'sun':  dict(chip='bg-sun-600/10 text-sun-700',   dot='text-sun-600'),
    'navy': dict(chip='bg-navy-800/8 text-navy-700',  dot='text-navy-700'),
}

def painel(c):
    cor = CORES[c['cor']]
    itens = ''.join(
        '<li class="flex items-start gap-3"><svg class="mt-1 h-[18px] w-[18px] shrink-0 %s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg><span class="text-[15.5px] leading-snug text-graphite/80">%s</span></li>' % (cor['dot'], i)
        for i in c['itens'])
    hidden = '' if c['ativo'] else ' hidden'
    return f'''<div role="tabpanel" id="painel-{c['id']}" aria-labelledby="aba-{c['id']}" class="grid gap-8 rounded-card border border-navy-800/10 bg-white p-6 sm:p-9 lg:grid-cols-[1fr_0.8fr] lg:items-center{hidden}" data-panel="{c['id']}">
  <div>
    <span class="pill {cor['chip']}">{c['tag']}</span>
    <h3 class="mt-4 text-[26px] font-extrabold leading-tight text-navy-800 sm:text-[32px]">{c['titulo']}</h3>
    <p class="mt-2 text-[15px] font-bold uppercase tracking-[0.1em] text-sun-600">{c['foco']}</p>
    <p class="mt-5 max-w-2xl text-[16px] leading-relaxed text-graphite/75">{c['texto']}</p>
    <ul class="mt-7 grid gap-3.5 sm:grid-cols-2">{itens}</ul>
    <div class="mt-8 flex flex-col gap-3 sm:flex-row">
      <a href="{wa('Olá! Tenho interesse no ciclo ' + c['titulo'] + ' na Escola Lumiar Poços de Caldas. Podem me passar as vagas e valores?')}" target="_blank" rel="noopener" class="btn-primary" data-track="cta-ciclo-{c['id']}">{ICON_WA_SM} Ver vagas em {c['titulo']}</a>
      <a href="#visita" class="btn-outline-navy">Agendar visita</a>
    </div>
  </div>
  <div class="photo-slot aspect-[4/5] rounded-card ring-1 ring-navy-800/10" data-slot="{c['slot']}">
    <!-- SUBSTITUIR: <img src="assets/fotos/{c['id']}.jpg" alt="{c['slot']}" class="h-full w-full object-cover"> -->
  </div>
</div>'''

CICLOS_PANELS = '\n'.join(painel(c) for c in CICLOS)

# ─────────── Depoimentos ───────────
DEPS = [
    dict(txt='Meu filho voltou a querer ir para a escola. Isso, para mim, já pagaria tudo. Ele chega em casa contando o que descobriu, não reclamando de prova.',
         nome='Depoimento de família', papel='Mãe · Fundamental 2', ini='F1'),
    dict(txt='A adaptação da minha filha no Infantil foi conduzida com um cuidado que eu nunca tinha visto. A tutora conhecia ela de verdade em duas semanas.',
         nome='Depoimento de família', papel='Pai · Educação Infantil', ini='F2'),
    dict(txt='O espaço verde faz uma diferença enorme. Eles passam boa parte do dia ao ar livre, e a gente sente isso no humor e no sono das crianças.',
         nome='Depoimento de família', papel='Mãe · Fundamental 1', ini='F3'),
]

def dep(d, i):
    return f'''<figure class="reveal card flex h-full flex-col p-7 hover:-translate-y-1 hover:shadow-lift" style="transition-delay:{i*0.08:.2f}s">
  <svg class="h-7 w-7 text-lumiar" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.6 4.8C5.5 6.4 3 9.9 3 14.4c0 3.1 1.9 5 4.4 5 2.3 0 4-1.7 4-4 0-2.2-1.5-3.8-3.6-3.8-.4 0-.9.1-1 .1.4-2 2.3-4.2 4.5-5.3zm10.2 0c-4.1 1.6-6.6 5.1-6.6 9.6 0 3.1 1.9 5 4.4 5 2.3 0 4-1.7 4-4 0-2.2-1.5-3.8-3.6-3.8-.4 0-.9.1-1 .1.4-2 2.3-4.2 4.5-5.3z"/></svg>
  <blockquote class="mt-5 flex-1 text-[16px] leading-relaxed text-graphite/80">“{d['txt']}”</blockquote>
  <figcaption class="mt-6 flex items-center gap-3.5 border-t border-navy-800/8 pt-5">
    <span class="grid h-11 w-11 shrink-0 place-items-center rounded-full bg-navy-800/8 text-[13px] font-black text-navy-700">{d['ini']}</span>
    <span>
      <span class="block text-[14.5px] font-extrabold text-navy-800">{d['nome']}</span>
      <span class="block text-[13px] text-graphite/55">{d['papel']}</span>
    </span>
  </figcaption>
</figure>'''

DEPOIMENTOS = ('<!-- SUBSTITUIR: trocar por depoimentos reais e autorizados de famílias da unidade -->\n'
               '<div class="mt-12 grid gap-5 md:grid-cols-3">' + ''.join(dep(d, i) for i, d in enumerate(DEPS)) + '</div>')

# ─────────── Objeções ───────────
OBJ = [
    ('“Ele vai ficar defasado em relação à turma nova.”',
     'O percurso na Lumiar é individual e registrado no Mosaico Digital. Nas primeiras semanas o tutor mapeia exatamente onde seu filho está e monta o plano a partir dali — não a partir do calendário da turma.'),
    ('“Vai custar a fazer amigos no meio do ano.”',
     'Turmas multietárias e pequenas. Na prática, um estudante novo é notado e acolhido no primeiro dia — não some no meio de 35 colegas.'),
    ('“E se ele não se adaptar?”',
     'Por isso existe o Dia de Experiência: seu filho passa um dia real de aula antes de qualquer decisão. Você e ele decidem depois de viver a escola, não depois de ler um folheto.'),
    ('“A escola atual não devolve a matrícula.”',
     'Entendemos o aperto. Por isso a Condição de Transição Suave isenta a taxa de rematrícula aqui e permite parcelar o restante do semestre.'),
]

def obj(q, a, i):
    return f'''<details class="group overflow-hidden rounded-card bg-white/8 ring-1 ring-inset ring-white/12 transition hover:bg-white/12"{' open' if i == 0 else ''}>
  <summary class="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 text-[16px] font-bold text-white marker:hidden">
    <span>{q}</span>
    <svg class="h-5 w-5 shrink-0 text-lumiar transition-transform duration-300 group-open:rotate-45" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
  </summary>
  <p class="px-6 pb-6 text-[15.5px] leading-relaxed text-white/70">{a}</p>
</details>'''

OBJECOES = '\n'.join(obj(q, a, i) for i, (q, a) in enumerate(OBJ))

# ─────────── Formulário ───────────
FORMULARIO = f'''<form id="form-visita" novalidate class="space-y-5">
  <div>
    <label for="f-nome" class="mb-2 block text-[13.5px] font-bold text-navy-800">Seu nome <span class="text-sun-600">*</span></label>
    <input id="f-nome" name="nome" type="text" required autocomplete="name" placeholder="Como podemos te chamar?"
      class="w-full rounded-2xl border-2 border-navy-800/10 bg-cream-50 px-4 py-3.5 text-[15.5px] text-graphite outline-none transition placeholder:text-graphite/35 focus:border-sun-600 focus:bg-white">
  </div>

  <div class="grid gap-5 sm:grid-cols-2">
    <div>
      <label for="f-tel" class="mb-2 block text-[13.5px] font-bold text-navy-800">WhatsApp <span class="text-sun-600">*</span></label>
      <input id="f-tel" name="telefone" type="tel" required inputmode="tel" autocomplete="tel" placeholder="(35) 99999-0000" maxlength="16"
        class="w-full rounded-2xl border-2 border-navy-800/10 bg-cream-50 px-4 py-3.5 text-[15.5px] text-graphite outline-none transition placeholder:text-graphite/35 focus:border-sun-600 focus:bg-white">
    </div>
    <div>
      <label for="f-email" class="mb-2 block text-[13.5px] font-bold text-navy-800">E-mail</label>
      <input id="f-email" name="email" type="email" autocomplete="email" placeholder="seu@email.com"
        class="w-full rounded-2xl border-2 border-navy-800/10 bg-cream-50 px-4 py-3.5 text-[15.5px] text-graphite outline-none transition placeholder:text-graphite/35 focus:border-sun-600 focus:bg-white">
    </div>
  </div>

  <div class="grid gap-5 sm:grid-cols-2">
    <div>
      <label for="f-idade" class="mb-2 block text-[13.5px] font-bold text-navy-800">Idade do seu filho(a)</label>
      <input id="f-idade" name="idade" type="number" min="1" max="18" inputmode="numeric" placeholder="Ex.: 7"
        class="w-full rounded-2xl border-2 border-navy-800/10 bg-cream-50 px-4 py-3.5 text-[15.5px] text-graphite outline-none transition placeholder:text-graphite/35 focus:border-sun-600 focus:bg-white">
    </div>
    <div>
      <label for="f-serie" class="mb-2 block text-[13.5px] font-bold text-navy-800">Série de interesse <span class="text-sun-600">*</span></label>
      <select id="f-serie" name="serie" required
        class="w-full appearance-none rounded-2xl border-2 border-navy-800/10 bg-cream-50 bg-[length:18px] bg-[right_1rem_center] bg-no-repeat px-4 py-3.5 text-[15.5px] text-graphite outline-none transition focus:border-sun-600 focus:bg-white"
        style="background-image:url(&quot;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232C3E50' stroke-width='2.5' stroke-linecap='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E&quot;)">
        <option value="">Selecione…</option>
        <option>Educação Infantil (I3 a I5)</option>
        <option>Fundamental 1 (1º ao 5º ano)</option>
        <option>Fundamental 2 (6º ao 9º ano)</option>
        <option>Ensino Médio</option>
        <option>Lumiar Teen Hub (contraturno)</option>
        <option>Colônia LumiFérias</option>
      </select>
    </div>
  </div>

  <div>
    <label for="f-msg" class="mb-2 block text-[13.5px] font-bold text-navy-800">Algo que devemos saber? <span class="font-medium text-graphite/45">(opcional)</span></label>
    <textarea id="f-msg" name="mensagem" rows="3" placeholder="Ex.: gostaria de visitar numa terça de manhã."
      class="w-full resize-none rounded-2xl border-2 border-navy-800/10 bg-cream-50 px-4 py-3.5 text-[15.5px] text-graphite outline-none transition placeholder:text-graphite/35 focus:border-sun-600 focus:bg-white"></textarea>
  </div>

  <p id="form-erro" class="hidden rounded-2xl bg-sun-600/10 px-4 py-3 text-[14px] font-bold text-sun-700" role="alert"></p>

  <button type="submit" class="btn-primary w-full !py-4 !text-base" data-track="cta-form">
    {ICON_WA} Enviar e falar no WhatsApp
  </button>

  <p class="text-center text-[12.5px] leading-relaxed text-graphite/50">
    Ao enviar, abrimos o WhatsApp com seus dados preenchidos. Não compartilhamos suas informações com terceiros.
  </p>
</form>'''

# ─────────── Footer ───────────
MAPS = 'https://www.google.com/maps/search/?api=1&query=Escola%20Lumiar%20Po%C3%A7os%20de%20Caldas%2C%20Rua%20Comendador%20Jo%C3%A3o%20Afonso%20Junqueira%2C%20201'
MAPS_EMBED = 'https://maps.google.com/maps?q=Rua%20Comendador%20Jo%C3%A3o%20Afonso%20Junqueira%2C%20201%2C%20Jardim%20dos%20Estados%2C%20Po%C3%A7os%20de%20Caldas%20-%20MG&t=&z=16&ie=UTF8&iwloc=&output=embed'

FOOTER = f'''<footer id="escola" class="relative overflow-hidden bg-navy-950 pt-16 text-white sm:pt-20">
  <div class="absolute inset-0 grid-paper opacity-60" aria-hidden="true"></div>

  <div class="wrap relative">
    <div class="grid gap-12 lg:grid-cols-[1.15fr_1fr_1.1fr]">

      <div>
        {logo_white}
        <p class="mt-5 max-w-sm text-[15px] leading-relaxed text-white/60">
          Educação Infantil, Ensino Fundamental I e II e Ensino Médio em Poços de Caldas desde 2018. Metodologia Lumiar, turmas reduzidas e uma vasta área verde no Jardim dos Estados.
        </p>
        <div class="mt-6 flex gap-2.5">
          <a href="https://www.instagram.com/lumiarpocos/" target="_blank" rel="noopener" aria-label="Instagram da Escola Lumiar Poços" class="grid h-11 w-11 place-items-center rounded-xl bg-white/8 text-white/80 transition hover:bg-lumiar hover:text-navy-900">
            <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.05 1.8.25 2.2.42.6.22 1 .48 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c0 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2 0-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c0-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2m0 2.1c-3.1 0-3.5 0-4.7.07-1.1.05-1.7.24-2.1.4-.5.2-.9.44-1.3.83-.4.4-.6.8-.8 1.3-.2.4-.4 1-.4 2.1-.1 1.2-.1 1.6-.1 4.7s0 3.5.1 4.7c0 1.1.2 1.7.4 2.1.2.5.4.9.8 1.3.4.4.8.6 1.3.8.4.2 1 .4 2.1.4 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1.1 0 1.7-.2 2.1-.4.5-.2.9-.4 1.3-.8.4-.4.6-.8.8-1.3.2-.4.4-1 .4-2.1.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c0-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.3-.4-.4-.8-.6-1.3-.8-.4-.2-1-.4-2.1-.4-1.2-.1-1.6-.1-4.7-.1m0 3.5a4.2 4.2 0 1 1 0 8.4 4.2 4.2 0 0 1 0-8.4m0 6.9a2.7 2.7 0 1 0 0-5.4 2.7 2.7 0 0 0 0 5.4m5.4-7.1a1 1 0 1 1-2 0 1 1 0 0 1 2 0"/></svg>
          </a>
          <a href="https://www.facebook.com/lumiarpocos/" target="_blank" rel="noopener" aria-label="Facebook da Escola Lumiar Poços" class="grid h-11 w-11 place-items-center rounded-xl bg-white/8 text-white/80 transition hover:bg-lumiar hover:text-navy-900">
            <svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12"/></svg>
          </a>
          <a href="{wa('Olá! Vim pelo site da Escola Lumiar Poços de Caldas e gostaria de mais informações.')}" target="_blank" rel="noopener" aria-label="WhatsApp da Escola Lumiar Poços" class="grid h-11 w-11 place-items-center rounded-xl bg-white/8 text-white/80 transition hover:bg-lumiar hover:text-navy-900">
            {wa_icon('h-5 w-5')}
          </a>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-8">
        <div>
          <p class="text-[12px] font-extrabold uppercase tracking-[0.16em] text-lumiar">Navegar</p>
          <ul class="mt-5 space-y-3 text-[15px] text-white/65">
            <li><a href="#metodologia" class="transition hover:text-white">Metodologia</a></li>
            <li><a href="#ciclos" class="transition hover:text-white">Nossos ciclos</a></li>
            <li><a href="#teenhub" class="transition hover:text-white">Lumiar Teen Hub</a></li>
            <li><a href="#lumiferias" class="transition hover:text-white">LumiFérias</a></li>
            <li><a href="#familias" class="transition hover:text-white">Famílias Lumiar</a></li>
          </ul>
        </div>
        <div>
          <p class="text-[12px] font-extrabold uppercase tracking-[0.16em] text-lumiar">Institucional</p>
          <ul class="mt-5 space-y-3 text-[15px] text-white/65">
            <li><a href="#visita" class="transition hover:text-white">Matrículas</a></li>
            <li><a href="#visita" class="transition hover:text-white">Agendar visita</a></li>
            <li><a href="/trabalhe-conosco/" class="transition hover:text-white">Trabalhe conosco</a></li>
            <li><a href="/perguntas-e-respostas/" class="transition hover:text-white">Perguntas frequentes</a></li>
            <li><a href="#visita" class="transition hover:text-white">Contato</a></li>
          </ul>
        </div>
      </div>

      <div>
        <p class="text-[12px] font-extrabold uppercase tracking-[0.16em] text-lumiar">Onde estamos</p>
        <address class="mt-5 not-italic text-[15px] leading-relaxed text-white/65">
          Rua Comendador João Afonso Junqueira, 201<br>
          Jardim dos Estados · Poços de Caldas — MG<br>
          <a href="tel:+553537218751" class="mt-2 inline-block font-bold text-white transition hover:text-lumiar">(35) 3721-8751</a>
        </address>
        <div class="mt-5 overflow-hidden rounded-2xl ring-1 ring-white/12">
          <iframe title="Mapa da Escola Lumiar Poços de Caldas" src="{MAPS_EMBED}" width="100%" height="170" style="border:0;filter:grayscale(.25) contrast(1.05)" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <a href="{MAPS}" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-[14px] font-bold text-lumiar hover:underline">
          Ver rota no Google Maps
          <svg class="h-3.5 w-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>
        </a>
      </div>
    </div>

    <div class="mt-14 flex flex-col gap-4 border-t border-white/10 py-8 text-[13px] text-white/45 sm:flex-row sm:items-center sm:justify-between">
      <p>© <span data-ano>2026</span> Escola Lumiar Poços de Caldas LTDA · CNPJ 31.189.993/0001-15</p>
      <p>Autorizada pela SEE-MG · Resolução nº 107/2019 · Portaria nº 179/2019</p>
    </div>
  </div>
</footer>'''

# ─────────── WhatsApp flutuante ───────────
WPP = f'''<a href="{wa('Olá! Vim pelo site e gostaria de agendar uma visita na Escola Lumiar Poços de Caldas.')}" target="_blank" rel="noopener"
   class="group fixed bottom-5 right-5 z-50 flex items-center gap-3 rounded-pill bg-[#25D366] p-4 font-bold text-white sm:py-3.5 sm:pl-4 sm:pr-5 shadow-[0_14px_34px_rgba(37,211,102,0.45)] transition-transform hover:-translate-y-1 sm:bottom-7 sm:right-7"
   aria-label="Falar no WhatsApp com a Escola Lumiar Poços de Caldas" data-track="cta-float">
  <span class="relative flex h-6 w-6 items-center justify-center">
    <span class="absolute inline-flex h-full w-full rounded-full bg-white/60 animate-pulseRing" aria-hidden="true"></span>
    {wa_icon('relative h-6 w-6')}
  </span>
  <span class="hidden text-[14.5px] leading-none sm:inline">Agendar visita</span>
</a>'''

# ─────────── Schema.org ───────────
SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "School",
  "@id": "https://www.escolalumiarpocos.com.br/#escola",
  "name": "Escola Lumiar Poços de Caldas",
  "alternateName": "Lumiar Poços",
  "description": "Escola de Educação Infantil, Ensino Fundamental I e II e Ensino Médio em Poços de Caldas (MG), com metodologia Lumiar, turmas reduzidas e ampla área verde no Jardim dos Estados.",
  "url": "https://www.escolalumiarpocos.com.br/",
  "telephone": "+55-35-3721-8751",
  "foundingDate": "2018",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Comendador João Afonso Junqueira, 201",
    "addressLocality": "Poços de Caldas",
    "addressRegion": "MG",
    "postalCode": "37701-000",
    "addressCountry": "BR"
  },
  "areaServed": { "@type": "City", "name": "Poços de Caldas" },
  "sameAs": [
    "https://www.instagram.com/lumiarpocos/",
    "https://www.facebook.com/lumiarpocos/"
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "07:30",
    "closes": "17:30"
  }],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Ciclos e programas",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Course", "name": "Educação Infantil", "description": "Acolhimento, adaptação individual e turmas reduzidas.", "provider": { "@id": "https://www.escolalumiarpocos.com.br/#escola" } } },
      { "@type": "Offer", "itemOffered": { "@type": "Course", "name": "Ensino Fundamental 1", "description": "Alfabetização, descoberta e projetos investigativos.", "provider": { "@id": "https://www.escolalumiarpocos.com.br/#escola" } } },
      { "@type": "Offer", "itemOffered": { "@type": "Course", "name": "Ensino Fundamental 2", "description": "Mentoria individual, protagonismo e projetos autorais.", "provider": { "@id": "https://www.escolalumiarpocos.com.br/#escola" } } },
      { "@type": "Offer", "itemOffered": { "@type": "Course", "name": "Ensino Médio", "description": "Itinerários formativos, projeto de vida e preparação para o ENEM.", "provider": { "@id": "https://www.escolalumiarpocos.com.br/#escola" } } },
      { "@type": "Offer", "itemOffered": { "@type": "Course", "name": "Lumiar Teen Hub", "description": "Contraturno de IA, inglês, podcast e música para 10 a 16 anos.", "provider": { "@id": "https://www.escolalumiarpocos.com.br/#escola" } } },
      { "@type": "Offer", "itemOffered": { "@type": "Course", "name": "Colônia LumiFérias", "description": "Colônia de férias em janeiro e julho para crianças de 4 a 12 anos.", "provider": { "@id": "https://www.escolalumiarpocos.com.br/#escola" } } }
    ]
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
FAQ_ITEMS
  ]
}
</script>'''

FAQ_ITEMS = ',\n'.join(
    '    { "@type": "Question", "name": %s, "acceptedAnswer": { "@type": "Answer", "text": %s } }'
    % (__import__('json').dumps(q.strip('“”"')), __import__('json').dumps(a))
    for q, a in OBJ)
SCHEMA = SCHEMA.replace('FAQ_ITEMS', FAQ_ITEMS)

# ─────────── JS ───────────
SCRIPT = '''<script>
(function () {
  'use strict';
  var WA = '%s';

  /* ── Header: fundo sólido ao rolar ── */
  var header = document.querySelector('[data-header]');
  var onScroll = function () {
    if (window.scrollY > 12) { header.classList.add('shadow-lift'); }
    else { header.classList.remove('shadow-lift'); }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Menu mobile ── */
  var toggle = document.querySelector('[data-menu-toggle]');
  var menu = document.querySelector('[data-menu]');
  toggle.addEventListener('click', function () {
    var open = menu.classList.toggle('hidden') === false;
    toggle.setAttribute('aria-expanded', String(open));
  });
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) {
      menu.classList.add('hidden');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  /* ── Abas dos ciclos ── */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[data-tab]'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('[data-panel]'));
  var ATIVA = ['bg-navy-800', 'text-white', 'shadow-soft'];
  var INATIVA = ['bg-white', 'text-navy-800/70', 'ring-1', 'ring-inset', 'ring-navy-800/12', 'hover:bg-cream-100'];

  function pinta(tab, ativa) {
    tab.classList.remove.apply(tab.classList, ativa ? INATIVA : ATIVA);
    tab.classList.add.apply(tab.classList, ativa ? ATIVA : INATIVA);
    tab.setAttribute('aria-selected', String(ativa));
    tab.setAttribute('tabindex', ativa ? '0' : '-1');
  }

  function seleciona(id) {
    tabs.forEach(function (t) { pinta(t, t.dataset.tab === id); });
    panels.forEach(function (p) { p.classList.toggle('hidden', p.dataset.panel !== id); });
  }

  tabs.forEach(function (t, i) {
    pinta(t, t.getAttribute('aria-selected') === 'true');
    t.addEventListener('click', function () { seleciona(t.dataset.tab); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      var alvo = tabs[(i + d + tabs.length) %% tabs.length];
      alvo.focus();
      seleciona(alvo.dataset.tab);
    });
  });

  /* ── Revelação ao rolar ── */
  var alvos = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8%% 0px', threshold: 0.08 });
    alvos.forEach(function (a) { io.observe(a); });
  } else {
    alvos.forEach(function (a) { a.classList.add('is-in'); });
  }

  /* ── Máscara de telefone ── */
  var tel = document.getElementById('f-tel');
  tel.addEventListener('input', function () {
    var v = tel.value.replace(/\\D/g, '').slice(0, 11);
    if (v.length > 10) v = v.replace(/(\\d{2})(\\d{5})(\\d{0,4})/, '($1) $2-$3');
    else if (v.length > 6) v = v.replace(/(\\d{2})(\\d{4})(\\d{0,4})/, '($1) $2-$3');
    else if (v.length > 2) v = v.replace(/(\\d{2})(\\d{0,5})/, '($1) $2');
    else if (v.length) v = v.replace(/(\\d{0,2})/, '($1');
    tel.value = v;
  });

  /* ── Envio do formulário → WhatsApp ── */
  var form = document.getElementById('form-visita');
  var erro = document.getElementById('form-erro');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form);
    var nome = (d.get('nome') || '').trim();
    var fone = (d.get('telefone') || '').trim();
    var serie = (d.get('serie') || '').trim();
    var faltando = [];

    if (nome.length < 2) faltando.push('seu nome');
    if (fone.replace(/\\D/g, '').length < 10) faltando.push('um WhatsApp válido');
    if (!serie) faltando.push('a série de interesse');

    if (faltando.length) {
      erro.textContent = 'Falta preencher: ' + faltando.join(', ') + '.';
      erro.classList.remove('hidden');
      return;
    }
    erro.classList.add('hidden');

    var idade = (d.get('idade') || '').trim();
    var email = (d.get('email') || '').trim();
    var msg = (d.get('mensagem') || '').trim();

    var texto = 'Olá! Quero agendar uma visita na Escola Lumiar Poços de Caldas.\\n\\n'
      + '• Nome: ' + nome + '\\n'
      + '• WhatsApp: ' + fone + '\\n'
      + (email ? '• E-mail: ' + email + '\\n' : '')
      + (idade ? '• Idade do filho(a): ' + idade + ' anos\\n' : '')
      + '• Série de interesse: ' + serie
      + (msg ? '\\n• Observação: ' + msg : '');

    /* INTEGRAÇÃO: envie também para o seu CRM/e-mail aqui, se desejar. */
    window.open(WA + '?text=' + encodeURIComponent(texto), '_blank', 'noopener');
  });

  /* ── Ano do rodapé ── */
  var ano = document.querySelector('[data-ano]');
  if (ano) ano.textContent = String(new Date().getFullYear());
})();
</script>''' % ('https://wa.me/' + WA_NUM)

# ─────────── Montagem ───────────
html = (B / 'src.html').read_text(encoding='utf-8')

subs = {
    'FAVICON_SRC': favicon,
    'LOGO_SVG': logo_inline,
    'PROCESSO_PROJETOS': processo.secao(),
    'PROCESSO_JS': processo.script(),
    'ICON_WA_DARK': ICON_WA_DARK,
    'ICON_WA_SM': ICON_WA_SM,
    'ICON_WA': ICON_WA,
    'WA_VISITA': wa('Olá! Gostaria de agendar uma visita na Escola Lumiar Poços de Caldas.'),
    'WA_EXPERIENCIA': wa('Olá! Quero agendar um Dia de Experiência para meu filho(a) na Escola Lumiar Poços de Caldas.'),
    'WA_CICLOS': wa('Olá! Gostaria de consultar as vagas disponíveis por turma na Escola Lumiar Poços de Caldas.'),
    'WA_TEENHUB': wa('Olá! Quero garantir uma vaga no Lumiar Teen Hub (contraturno). Podem me passar valores e horários?'),
    'WA_LUMIFERIAS': wa('Olá! Quero receber a programação da Colônia LumiFérias.'),
    'WA_TRANSICAO': wa('Olá! Estou pensando em trocar meu filho(a) de escola no meio do ano e quero saber mais sobre a Condição de Transição Suave da Lumiar.'),
    'WA_PROJETOS': wa('Olá! Vi no site como funcionam os projetos e gostaria de ver um projeto de perto, na escola.'),
    'GOOGLE_MAPS_URL': MAPS,
    'SELOS': SELOS,
    'CICLOS_PANELS': CICLOS_PANELS,
    'DEPOIMENTOS': DEPOIMENTOS,
    'OBJECOES': OBJECOES,
    'FORMULARIO': FORMULARIO,
    'FOOTER': FOOTER,
    'WHATSAPP_FLOAT': WPP,
    'SCHEMA_JSON': SCHEMA,
    'SCRIPT_JS': SCRIPT,
}

for k, v in subs.items():
    html = html.replace(k, v)

restantes = [k for k in subs if k in html and k not in ('ICON_WA',)]
(B / 'page.html').write_text(html, encoding='utf-8')
print('page.html', len(html), 'bytes')
print('placeholders restantes:', [p for p in re.findall(r'\b[A-Z][A-Z_]{4,}\b', html) if p not in ('DOCTYPE', 'UNESCO')][:10])
