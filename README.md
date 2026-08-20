# Nova Homepage — Escola Lumiar Poços de Caldas

Arquivo único e autocontido: `index.html` (~250 KB, sem dependências externas de CSS/JS).
Tailwind já compilado e inlinado, fontes **Malva** embutidas em WOFF2, logos e símbolo em SVG inline.

---

## 1. Como publicar

**Vercel / Netlify (recomendado)** — arraste a pasta para o painel. Zero build, zero servidor, imune aos ataques que derrubaram a instalação WordPress atual.

**Hospedagem própria** — suba `index.html` na raiz do domínio.

> ⚠️ **Prioridade 0 antes de apontar o domínio:** o `escolalumiarpocos.com.br` está redirecionando para site de apostas (Meritbet). Publicar a home nova sem limpar a hospedagem só transfere o problema. Antes: limpar malware, trocar todas as senhas (painel, FTP, banco), revisar `.htaccess` e DNS, reemitir o SSL, e pedir revisão no Google Search Console.

---

## 2. O que trocar antes de ir ao ar

### Fotos reais (o item mais importante)

Cada área de imagem é um `div.photo-slot` com a legenda do que entra ali e um comentário `<!-- SUBSTITUIR: ... -->` logo abaixo, com o `<img>` pronto. Basta descomentar e apagar o `div`.

| Onde | Foto sugerida |
| --- | --- |
| Hero — destaque | Pátio verde da unidade, com estudantes |
| Hero — quadrado 1 | Oficina de projetos com mestre |
| Hero — quadrado 2 | Tutor(a) acompanhando um estudante |
| Ciclo Infantil | Roda de crianças na área externa |
| Ciclo Fundamental 1 | Projeto em grupo na sala |
| Ciclo Fundamental 2 | Adolescente apresentando projeto |
| Ensino Médio | Estudante do Médio em projeto |
| Teen Hub | Adolescentes em projeto de tecnologia/podcast |

Formato ideal: JPG otimizado (≤ 250 KB), tratamento quente e saturação natural, sem cara de banco de imagens.

### Seção “Como funciona na prática” (`#projetos`)

A trilha das 7 etapas usa o caso de um estudante chamado **Miguel, 9 anos, que quer ser astronauta** como exemplo concreto. É um caso ilustrativo, montado a partir do processo que você descreveu — **troque pelo percurso de um estudante real** assim que tiver um autorizado pela família. É o tipo de conteúdo que ganha muito com fotos da maquete, do relatório e da culminância.

Confira também, antes de publicar, se batem com a realidade da escola:

- a duração de cada etapa (“1 semana”, “semana 2”, “semana 2 e 3”, “trimestre inteiro”);
- as cinco disciplinas listadas como mapeadas no Mosaico na etapa 04;
- o nome exato da semana de levantamento de interesse.

### Depoimentos

Os três depoimentos são **placeholders plausíveis**, marcados com `<!-- SUBSTITUIR -->`. Troque por frases reais e autorizadas de famílias, com nome e ciclo. Não publique como está.

### Outros ajustes rápidos

- **Imagem de compartilhamento:** gere `og-lumiar-pocos.jpg` (1200×630) e suba na raiz.
- **CEP no Schema:** confirme o CEP exato (hoje está `37701-000`).
- **Horário no Schema:** confirme abertura/fechamento (hoje 07:30–17:30).
- **Links do rodapé:** `/trabalhe-conosco/` e `/perguntas-e-respostas/` apontam para as páginas antigas — reaponte quando as novas existirem.
- **Condição de Transição Suave:** o texto promete isenção da taxa de rematrícula + plano de adaptação de 4 semanas. Confirme com a direção antes de publicar.
- **Colônia LumiFérias:** faixa etária (4 a 12) e duração (2 semanas) são propostas — ajuste ao real.
- **Teen Hub:** horário 14h–17h, seg. a sex. — ajuste ao real.

---

## 3. Conversão

- **12 pontos de contato WhatsApp**, todos com mensagem pré-configurada e contexto próprio (hero, ciclo específico, Teen Hub, LumiFérias, transição, rodapé, botão flutuante).
- **Botão flutuante fixo** em todas as telas.
- **Formulário** (nome, WhatsApp com máscara, e-mail, idade, série, observação) valida no cliente e abre o WhatsApp já com todos os dados formatados — nenhum backend necessário.
- Cada CTA tem `data-track="..."` (`cta-hero-wa`, `cta-teenhub`, `cta-form`, `cta-float`…). Basta plugar GA4/Meta Pixel escutando esse atributo.

Para enviar as leads também para CRM ou e-mail, há um ponto marcado no JS: `/* INTEGRAÇÃO: envie também para o seu CRM/e-mail aqui */`.

---

## 4. Design system aplicado

| Token | Valor | Uso |
| --- | --- | --- |
| Navy | `#1A2A44` / `#12203A` / `#0C1526` | Header, hero, Teen Hub, rodapé |
| Laranja Solar | `#E67E22` / `#F39C12` | CTAs primários, eyebrows, LumiFérias |
| Amarelo Lumiar | `#FFC132` | Logo, destaques, selos (cor oficial da marca) |
| Verde Folha | `#27AE60` / `#2ECC71` | Natureza, confirmações, Infantil |
| Off-white quente | `#FDF5E6` / `#FFFCF6` | Fundos de leitura |
| Grafite | `#2C3E50` | Texto corrido |

Tipografia **Malva** (Regular 400, Medium 500, Bold 700, ExtraBold 800, Black 900), embutida e com fallback para Lato. Border-radius de 20 px em cards, sombras difusas, badges pill.

---

## 5. Estrutura da página

Header fixo → Hero + barra de credibilidade → faixa de selos → 4 pilares + Mosaico Digital → **Como funciona na prática (trilha das 7 etapas)** → seletor de ciclos em abas → Lumiar Teen Hub → Colônia LumiFérias → depoimentos + Google → “Por que trocar de escola no meio do ano?” (acordeão de objeções) → formulário de agendamento → rodapé institucional. Botão flutuante do WhatsApp sempre visível.

### A trilha do processo de projetos (interativa)

Três fases clicáveis (Descobrir · Construir · Viver e avaliar) e um palco que mostra uma etapa por vez, com ilustração à esquerda e conteúdo à direita.

**Como a família navega**

- clica numa das três fases e cai na primeira etapa dela;
- avança com "Próxima etapa" / "Anterior", ou pula direto clicando nos pontos de progresso;
- no celular, também dá para arrastar o dedo para os lados;
- pelo teclado, as setas ← → percorrem as etapas;
- na última etapa o botão vira "Recomeçar" e volta ao início — reforçando que o ciclo se repete a cada trimestre.

A barrinha embaixo de cada card de fase mostra o quanto daquela fase já foi percorrido. As transições são direcionais (entra pela direita ao avançar, pela esquerda ao voltar) e são desligadas automaticamente para quem usa "reduzir movimento" no sistema.

**As ilustrações** são SVG originais, desenhadas na paleta da marca e embutidas no arquivo — não dependem de imagem externa, escalam sem perder nitidez e têm descrição textual para leitores de tela. Para editar, o desenho de cada etapa está em `build/ilustracoes.py` no meu ambiente; no `index.html` elas estão inline dentro de `<figure data-ilo="N">`.

1. Semana de Levantamento de Interesse
2. Interesse do Ciclo
3. Nascem dois projetos (do ciclo + individual)
4. Plataforma Mosaico + BNCC
5. O tutor convoca os Mestres
6. O plano do trimestre (propósito, objetivo, plano)
7. Culminância e avaliação integrada (apresentação, Mosaico, autoavaliação, devolutiva à família)

---

## 6. Acessibilidade e SEO

Skip link, navegação por teclado nas abas (setas ← →), `aria-selected`/`aria-controls`, foco visível, `prefers-reduced-motion` respeitado, contraste alto em todas as combinações de cor.

Meta tags completas, Open Graph, canonical e dois blocos Schema.org: `School` (com endereço, telefone, horários e catálogo de cursos) e `FAQPage` (as quatro objeções). Isso alimenta o rich result de escola local e o painel do Google Meu Negócio.

---

## 7. Próximos passos sugeridos

1. Landing pages dedicadas: **Infantil 3**, **Fundamental 2** e **Lumiar Teen Hub** (o briefing pede as três; a home já linka para cada tema).
2. Página de Metodologia expandida e página institucional “A Escola”.
3. Integração das avaliações reais do Google Meu Negócio.
4. Pixel de conversão + campanhas de tráfego pago apontando para as LPs.
