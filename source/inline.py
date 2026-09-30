# -*- coding: utf-8 -*-
import pathlib

B = pathlib.Path('/home/claude/lumiar/build')
html = (B / 'page.html').read_text(encoding='utf-8')
css = (B / 'out.css').read_text(encoding='utf-8')

# As fontes Malva (@font-face) já vêm compiladas dentro de out.css a partir de
# input.css, referenciando os arquivos .woff2 em assets/fonts/ — NÃO inlinar
# como base64 aqui. Base64 infla o HTML e bloqueia a 1ª renderização no Safari iOS.
bloco = '<style>' + css + '</style>'

html = html.replace('<link rel="stylesheet" href="out.css">', bloco)

out = B.parent / 'index.html'
out.write_text(html, encoding='utf-8')
print(out, out.stat().st_size, 'bytes')
