# -*- coding: utf-8 -*-
import pathlib

B = pathlib.Path('/home/claude/lumiar/build')
html = (B / 'page.html').read_text(encoding='utf-8')
css = (B / 'out.css').read_text(encoding='utf-8')
fonts = (B / 'fonts.css').read_text(encoding='utf-8')

bloco = ('<style>\n/* Malva — tipografia oficial Lumiar (Brand Guidelines v0.2.4). Fallback: Lato. */\n'
         + fonts + '\n</style>\n<style>' + css + '</style>')

html = html.replace('<link rel="stylesheet" href="out.css">', bloco)

out = B.parent / 'index.html'
out.write_text(html, encoding='utf-8')
print(out, out.stat().st_size, 'bytes')
