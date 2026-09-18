# -*- coding: utf-8 -*-
"""Seção 'Como funciona na prática' — stepper interativo com ilustrações."""

from processo_dados import FASES, CORES_FASE, ETAPAS, CHECK
import ilustracoes as il

# índice da fase (0,1,2) de cada etapa, pela cor
FASE_IDX = {'leaf': 0, 'sun': 1, 'navy': 2}
ETAPAS_POR_FASE = [[i + 1 for i, e in enumerate(ETAPAS) if FASE_IDX[e['fase']] == f] for f in range(3)]


# ─────────────────────────── botões de fase ───────────────────────────

def _botao_fase(i, nome, faixa, cor, desc):
    c = CORES_FASE[cor]
    ativa = i == 0
    return f'''<button type="button" data-fase="{i}" aria-pressed="{'true' if ativa else 'false'}"
  class="fase-btn group relative overflow-hidden rounded-card border-2 border-navy-800/10 bg-white p-5 text-left transition-all duration-300 hover:-translate-y-0.5 hover:border-navy-800/25{' is-on' if ativa else ''}">
  <span class="flex items-center gap-3">
    <span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl {c['suave']} text-[15px] font-black {c['txt']}">{i + 1}</span>
    <span class="min-w-0">
      <span class="block text-[17px] font-extrabold leading-none text-navy-800">{nome}</span>
      <span class="mt-1.5 block text-[11.5px] font-bold uppercase tracking-[0.1em] {c['txt']}">{faixa}</span>
    </span>
    <svg class="fase-seta ml-auto h-5 w-5 shrink-0 {c['txt']}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
  </span>
  <span class="mt-3.5 block text-[13.5px] leading-relaxed text-graphite/65">{desc}</span>
  <span class="absolute inset-x-0 bottom-0 h-[3px] bg-navy-800/8" aria-hidden="true">
    <span class="fase-barra block h-full w-0 {c['no']} transition-[width] duration-500 ease-out"></span>
  </span>
</button>'''


# ─────────────────────────── painel de uma etapa ───────────────────────────

def _pills_bncc(pills, c):
    linhas = ''.join(
        f'''<li class="flex items-center gap-2.5 rounded-xl bg-white px-3 py-2 ring-1 ring-inset ring-navy-800/10">
  <span class="text-[12.5px] font-extrabold text-navy-800">{t}</span>
  <span class="text-[12px] text-graphite/55">{d}</span>
</li>''' for t, d in pills)
    return f'''<div class="mt-3 rounded-2xl {c['suave']} p-3">
  <p class="text-[11px] font-extrabold uppercase tracking-[0.14em] {c['txt']}">Habilidades mapeadas no Mosaico</p>
  <ul class="mt-2 flex flex-wrap gap-2">{linhas}</ul>
</div>'''


def _painel(n, e):
    """n = 1..7"""
    c = CORES_FASE[e['fase']]
    nome_fase = FASES[FASE_IDX[e['fase']]][1]
    itens = ''.join(
        f'<li class="flex gap-2.5">{CHECK % c["txt"]}<span class="text-[15px] leading-snug text-graphite/75">{it}</span></li>'
        for it in e['itens'])
    pills = _pills_bncc(e['pills'], c) if e.get('pills') else ''

    return f'''<article id="etapa-{n}" role="tabpanel" aria-labelledby="ponto-{n}" data-etapa="{n}" class="etapa{' is-on' if n == 1 else ''}">
  <div class="flex flex-wrap items-center gap-2.5">
    <span class="pill {c['chip']}">Etapa {n:02d} de 07</span>
    <span class="text-[12px] font-bold uppercase tracking-[0.1em] text-graphite/40">{nome_fase} · {e['dur']}</span>
  </div>

  <p class="eyebrow mt-3">{e['etiqueta']}</p>
  <h3 class="mt-2 text-[23px] font-extrabold leading-snug text-navy-800 sm:text-[28px]">{e['titulo']}</h3>
  <p class="mt-2.5 text-[15.5px] leading-relaxed text-graphite/70">{e['texto']}</p>

  <ul class="etapa-itens mt-4 space-y-2">{itens}</ul>
  {pills}

  <aside class="caso relative mt-4 overflow-hidden rounded-card bg-navy-800 p-5 text-white">
    <div class="absolute inset-0 grid-paper opacity-60" aria-hidden="true"></div>
    <div class="pointer-events-none absolute -right-10 -top-10 h-32 w-32 rounded-full bg-lumiar/20 blur-2xl" aria-hidden="true"></div>
    <div class="relative">
      <div class="flex items-center gap-2.5">
        <svg class="h-4 w-4 shrink-0 text-lumiar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>
        <p class="text-[11.5px] font-extrabold uppercase tracking-[0.14em] text-lumiar">Na prática · {e['caso_tit']}</p>
      </div>
      <p class="mt-3.5 text-[15px] leading-relaxed text-white/80">{e['caso']}</p>
    </div>
  </aside>
</article>'''


# ─────────────────────────── pontos de progresso ───────────────────────────

def _ponto(n, e):
    c = CORES_FASE[e['fase']]
    ativo = n == 1
    estado = 'w-8 opacity-100' if ativo else 'w-2.5 opacity-30 hover:opacity-60'
    return f'''<button type="button" role="tab" id="ponto-{n}" aria-controls="etapa-{n}"
  aria-selected="{'true' if ativo else 'false'}" tabindex="{'0' if ativo else '-1'}" data-ponto="{n}"
  class="ponto h-2.5 rounded-pill transition-all duration-300 {c['no']} {estado}">
  <span class="sr-only">Etapa {n}: {e['etiqueta']}</span>
</button>'''


# ─────────────────────────── a seção ───────────────────────────

def secao():
    fases = ''.join(_botao_fase(i, nome, faixa, cor, desc)
                    for i, (_slug, nome, faixa, cor, desc) in enumerate(FASES))
    ilos = ''.join(
        f'<figure data-ilo="{n}" class="ilo absolute inset-4 sm:inset-6{" is-on" if n == 1 else ""}">{il.para(n)}</figure>'
        for n in range(1, 8))
    paineis = ''.join(_painel(n, e) for n, e in enumerate(ETAPAS, start=1))
    pontos = ''.join(_ponto(n, e) for n, e in enumerate(ETAPAS, start=1))

    return f'''<!-- ══════════════════════════ COMO FUNCIONA NA PRÁTICA ══════════════════════════ -->
<section id="projetos" class="relative overflow-hidden bg-white py-20 sm:py-28">
  <div class="pointer-events-none absolute -left-32 top-1/3 h-[420px] w-[420px] rounded-full bg-leaf-500/5 blur-3xl" aria-hidden="true"></div>
  <div class="pointer-events-none absolute -right-32 top-2/3 h-[420px] w-[420px] rounded-full bg-sun-600/5 blur-3xl" aria-hidden="true"></div>

  <div class="wrap relative">
    <div class="reveal max-w-3xl">
      <p class="eyebrow">Como funciona na prática</p>
      <h2 class="h-section mt-3 text-balance">“Mas se é tudo por projeto, como meu filho aprende o conteúdo?”</h2>
      <p class="lead mt-5">É a pergunta que mais ouvimos nas visitas — e ela merece uma resposta concreta. Clique nas três fases abaixo e percorra o caminho inteiro, do primeiro “o que você quer descobrir?” até a avaliação do trimestre. Em cada etapa, o percurso real de um estudante que queria ser astronauta.</p>
    </div>

    <!-- Fases clicáveis -->
    <div class="reveal mt-10 grid gap-3.5 sm:grid-cols-3">{fases}</div>

    <!-- Palco -->
    <div class="reveal mt-6 overflow-hidden rounded-card border border-navy-800/10 bg-cream-50 shadow-soft" data-palco data-dir="next">
      <div class="grid lg:h-[68vh] lg:max-h-[620px] lg:min-h-[440px] lg:grid-cols-[0.94fr_1.06fr]">

        <!-- Ilustração (altura fixa, proporcional à tela, no desktop) -->
        <div class="border-b border-navy-800/8 bg-cream-100 lg:h-full lg:border-b-0 lg:border-r">
          <div class="relative h-[268px] sm:h-[340px] lg:h-full">
            {ilos}
          </div>
        </div>

        <!-- Conteúdo (rola internamente se não couber na altura fixa) -->
        <div class="relative overflow-y-auto bg-white p-5 sm:p-7 lg:h-full lg:p-8">{paineis}</div>
      </div>

      <!-- Controles -->
      <div class="flex flex-col-reverse gap-4 border-t border-navy-800/10 bg-white px-4 py-4 sm:flex-row sm:items-center sm:justify-between sm:gap-3 sm:px-7">
        <div class="flex items-center gap-3">
        <button type="button" data-prev
          class="btn shrink-0 border-2 border-navy-800/12 bg-white !px-4 !py-3 text-navy-800 transition hover:border-navy-800/35 disabled:pointer-events-none disabled:opacity-30 sm:!py-2.5 sm:!px-5">
          <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>
          <span class="hidden sm:inline">Anterior</span><span class="sr-only sm:hidden">Etapa anterior</span>
        </button>
        <button type="button" data-next class="btn-primary flex-1 !py-3 sm:hidden">
          <span data-next-txt-m>Próxima etapa</span>
          <svg data-icone-seta-m class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          <svg data-icone-volta-m class="hidden h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg>
        </button>
        </div>

        <ol role="tablist" aria-label="Etapas do processo" class="flex flex-1 items-center justify-center gap-2">{pontos}</ol>

        <button type="button" data-next class="btn-primary hidden shrink-0 !px-4 !py-2.5 sm:inline-flex sm:!px-6">
          <span data-next-txt>Próxima etapa</span>
          <svg data-icone-seta class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          <svg data-icone-volta class="hidden h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg>
        </button>
      </div>
    </div>

  </div>
</section>
'''


# ─────────────────────────── comportamento ───────────────────────────

def script():
    faixas = repr(ETAPAS_POR_FASE).replace("'", '"')
    return '''<script>
(function () {
  'use strict';
  var palco = document.querySelector('[data-palco]');
  if (!palco) return;

  var FAIXAS = ''' + faixas + ''';
  var TOTAL = 7;
  var atual = 1;

  var paineis = {}, ilos = {}, pontos = {};
  palco.querySelectorAll('[data-etapa]').forEach(function (el) { paineis[el.dataset.etapa] = el; });
  palco.querySelectorAll('[data-ilo]').forEach(function (el) { ilos[el.dataset.ilo] = el; });
  palco.querySelectorAll('[data-ponto]').forEach(function (el) { pontos[el.dataset.ponto] = el; });

  var botoesFase = Array.prototype.slice.call(document.querySelectorAll('[data-fase]'));
  var btPrev = palco.querySelector('[data-prev]');
  var btsNext = Array.prototype.slice.call(palco.querySelectorAll('[data-next]'));
  var txtsNext = Array.prototype.slice.call(palco.querySelectorAll('[data-next-txt],[data-next-txt-m]'));
  var icsSeta = Array.prototype.slice.call(palco.querySelectorAll('[data-icone-seta],[data-icone-seta-m]'));
  var icsVolta = Array.prototype.slice.call(palco.querySelectorAll('[data-icone-volta],[data-icone-volta-m]'));
  var listaPontos = Object.keys(pontos).sort(function (a, b) { return a - b; })
    .map(function (k) { return pontos[k]; });

  function faseDe(n) {
    for (var f = 0; f < FAIXAS.length; f++) { if (FAIXAS[f].indexOf(n) !== -1) return f; }
    return 0;
  }

  function pintaPonto(el, ativo) {
    el.classList.toggle('w-8', ativo);
    el.classList.toggle('opacity-100', ativo);
    el.classList.toggle('w-2.5', !ativo);
    el.classList.toggle('opacity-30', !ativo);
    el.classList.toggle('hover:opacity-60', !ativo);
    el.setAttribute('aria-selected', String(ativo));
    el.setAttribute('tabindex', ativo ? '0' : '-1');
  }

  function pintaFases(n) {
    var f = faseDe(n);
    botoesFase.forEach(function (bt, i) {
      var ativa = i === f;
      bt.setAttribute('aria-pressed', String(ativa));
      bt.classList.toggle('is-on', ativa);
      var barra = bt.querySelector('.fase-barra');
      if (!barra) return;
      var faixa = FAIXAS[i], pct = 0;
      if (i < f) pct = 100;
      else if (i === f) pct = ((faixa.indexOf(n) + 1) / faixa.length) * 100;
      barra.style.width = pct + '%';
    });
  }

  function mostra(n, dir) {
    n = Math.min(TOTAL, Math.max(1, n));
    if (n === atual && palco.dataset.pronto === '1') return;
    palco.dataset.pronto = '1';
    palco.dataset.dir = dir || (n > atual ? 'next' : 'prev');

    Object.keys(paineis).forEach(function (k) {
      var on = String(n) === k;
      /* reinicia a animação de entrada */
      if (on) { paineis[k].classList.remove('is-on'); void paineis[k].offsetWidth; }
      paineis[k].classList.toggle('is-on', on);
      if (ilos[k]) ilos[k].classList.toggle('is-on', on);
      if (pontos[k]) pintaPonto(pontos[k], on);
    });

    atual = n;
    pintaFases(n);
    btPrev.disabled = n === 1;
    var fim = n === TOTAL;
    txtsNext.forEach(function (t) { t.textContent = fim ? 'Recomeçar' : 'Próxima etapa'; });
    icsSeta.forEach(function (i) { i.classList.toggle('hidden', fim); });
    icsVolta.forEach(function (i) { i.classList.toggle('hidden', !fim); });
  }

  botoesFase.forEach(function (bt, i) {
    bt.addEventListener('click', function () { mostra(FAIXAS[i][0]); });
  });
  listaPontos.forEach(function (el) {
    el.addEventListener('click', function () { mostra(parseInt(el.dataset.ponto, 10)); });
  });
  btPrev.addEventListener('click', function () { mostra(atual - 1, 'prev'); });
  btsNext.forEach(function (bt) {
    bt.addEventListener('click', function () {
      if (atual === TOTAL) { mostra(1, 'prev'); return; }
      mostra(atual + 1, 'next');
    });
  });

  listaPontos.forEach(function (el, i) {
    el.addEventListener('keydown', function (ev) {
      var d = ev.key === 'ArrowRight' ? 1 : ev.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      ev.preventDefault();
      var alvo = listaPontos[(i + d + listaPontos.length) % listaPontos.length];
      mostra(parseInt(alvo.dataset.ponto, 10), d > 0 ? 'next' : 'prev');
      alvo.focus();
    });
  });

  /* arrastar no celular */
  var x0 = null;
  palco.addEventListener('touchstart', function (ev) { x0 = ev.changedTouches[0].clientX; }, { passive: true });
  palco.addEventListener('touchend', function (ev) {
    if (x0 === null) return;
    var dx = ev.changedTouches[0].clientX - x0;
    x0 = null;
    if (Math.abs(dx) < 55) return;
    mostra(atual + (dx < 0 ? 1 : -1), dx < 0 ? 'next' : 'prev');
  }, { passive: true });

  pintaFases(1);
  btPrev.disabled = true;
})();
</script>'''
