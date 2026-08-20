# Como rebuildar

Pré-requisitos: Node.js e Python 3.

```bash
npm install
npx tailwindcss -c tailwind.config.js -i input.css -o out.css --minify
python3 assemble.py
python3 inline.py
```

O resultado final (`index.html`, autocontido) é gerado na pasta pai deste diretório.

Arquivos:
- `src.html` — esqueleto da página com placeholders
- `assemble.py` — monta todo o conteúdo (copy, ciclos, footer, schema, etc.) e substitui os placeholders
- `processo.py` / `processo_dados.py` — a seção interativa "Como funciona na prática"
- `ilustracoes.py` — as 7 ilustrações SVG originais das etapas do processo
- `input.css` / `tailwind.config.js` — design system (cores, tipografia, animações)
- `inline.py` — embute CSS e fontes no HTML final
- `fonts/` — fontes Malva convertidas para WOFF2 (com fonts.css já com base64)
