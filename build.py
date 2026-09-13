#!/usr/bin/env python3
r"""Copy the generated phi^4 atlas into this repo and inject the credit line.

The atlas itself is built in the research repo with

    python schnetz/extracted/graph_viewer.py 7      -> graph_atlas.html

This script copies that file to index.html (so the site root is the atlas)
prepends a doctype and a UTF-8 charset declaration (the generator emits neither,
so the page is mojibake unless the server announces UTF-8), and appends one line to
the header naming the data's provenance.  Nothing else is touched.

    python build.py [path/to/research/repo/schnetz/extracted_results]
"""

import os
import sys

SRC_DEFAULT = os.path.expanduser(
    '~/Gits/Papers/Gradient Properties of Perturbative Multiscalar RG Flows '
    'to Six Loops/schnetz/extracted_results')
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = 'https://github.com/andstergiou/phi4-graph-atlas'

CREDIT = (
    '<div class="prov">Graph ordering and the seven-loop input data follow '
    "O. Schnetz's <a href=\"https://github.com/oliverschnetz/HyperlogProcedures\">"
    'HyperlogProcedures</a> 0.8; every coefficient shown here is recomputed by '
    'tensorial minimal subtraction. Provenance, citation and licence (CC BY 4.0): '
    f'<a href="{REPO}">github.com/andstergiou/phi4-graph-atlas</a>.</div>')

CSS = ('.conv{font-size:12px;color:var(--muted);margin:2px 0 8px;max-width:110ch;line-height:1.45}\n'
       '.prov{flex-basis:100%;font-size:12px;color:var(--muted);margin:0 0 6px;max-width:110ch;line-height:1.45}\n'
       '.prov a{color:var(--accent-ink)}\n')

CONV_RULE = '.conv{font-size:12px;color:var(--muted);margin:2px 0 8px;max-width:110ch;line-height:1.45}\n'

# The generated file starts straight at <title>: no doctype and no charset, so it
# renders as mojibake wherever the server does not announce UTF-8 (a file:// open,
# or any host that serves text/html bare).  Give it a real head.
HEAD = ('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n')


def inject(html):
    """Put the credit block just after the conventions block, and its styling
    just after the existing .conv rule."""
    if 'class="prov"' in html:
        raise SystemExit('credit block already present')
    i = html.index('<div class="conv">')
    j = html.index('</div>', i) + len('</div>')
    html = html[:j] + '\n  ' + CREDIT + html[j:]
    if CONV_RULE not in html:
        raise SystemExit('the .conv style rule changed; update build.py')
    html = html.replace(CONV_RULE, CSS, 1)
    if html.lstrip().startswith('<!doctype'):
        raise SystemExit('the generated file now has its own doctype; update build.py')
    return HEAD + html


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else SRC_DEFAULT
    path = os.path.join(src, 'graph_atlas.html')
    if not os.path.exists(path):
        raise SystemExit(f'missing {path} — regenerate it with graph_viewer.py 7')
    with open(path) as fh:
        html = inject(fh.read())
    out = os.path.join(HERE, 'index.html')
    with open(out, 'w') as fh:
        fh.write(html)
    print(f'graph_atlas.html -> index.html  ({len(html) / 1048576:.1f} MB)')


if __name__ == '__main__':
    main()
