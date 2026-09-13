#!/usr/bin/env python3
r"""Build the published phi^4 atlas: index.html and the JSON export.

The atlas page is generated elsewhere, as graph_atlas.html.  This script turns that
file into what the site serves:

  index.html       the generated page, plus a doctype and a UTF-8 charset (the
                   generator emits neither, so the page is mojibake unless the
                   server announces UTF-8) and one header line giving the data's
                   provenance and a link to the export.
  phi4_atlas.json  the full data set: a structures list and expressions keyed
                   by structure id, for every loop order at once.

    python build.py <directory containing graph_atlas.html>
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = 'https://github.com/andstergiou/phi4-graph-atlas'
JSON_NAME = 'phi4_atlas.json'

HEAD = ('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n')

CONV_RULE = '.conv{font-size:12px;color:var(--muted);margin:2px 0 8px;max-width:110ch;line-height:1.45}\n'

CSS = (CONV_RULE +
       '.prov{flex-basis:100%;font-size:12px;color:var(--muted);margin:0 0 6px;max-width:110ch;line-height:1.45}\n'
       '.prov a{color:var(--accent-ink)}\n'
       '.dl{font:500 13px var(--sans);padding:5px 11px;border:1px solid var(--line);border-radius:4px;'
       'background:transparent;color:var(--ink);text-decoration:none;white-space:nowrap}\n'
       '.dl:hover{border-color:var(--accent);color:var(--accent-ink)}\n')

TABS = '<div class="tabs" id="tabs" role="tablist"></div>'

# Page field -> key of the expression map in the export.
FOUR_POINT = {'beta': 'beta', 'beta_z': 'beta_z', 'Z': 'Z_lambda'}
TWO_POINT = {'u': 'Zphi_minus_half', 'gamma': 'gamma_phi', 'gammaOn': 'gamma_phi_On'}
META = ('id', 'L', 'kind', 'num', 'seq', 'edges', 'ext', 'stab',
        'orbit', 'aut', 'prim', 'On', 'tensor', 'graph', 'onepi', 'vr', 'fac', 'sym',
        'comp')

NOTE = (
    'Tensorial MS renormalisation of the multiscalar phi^4 beta function and '
    'anomalous dimension, per structure, at 1 to 7 loops.  Every value is in '
    'minimal subtraction (MS-bar).  beta, Z_lambda, '
    'gamma_phi and Zphi_minus_half are all in the O-normalisation: coefficients '
    'of the structure summed over its distinct external labellings, so '
    'beta_L = L times the 1/epsilon residue of Z_lambda and gamma_phi = -L '
    'times that of Zphi_minus_half.  stab is the number of permutations of '
    'the external indices that leave a structure\'s tensor unchanged and orbit '
    'the number of distinct labellings: orbit = 24/stab for a vertex structure, '
    'and for a propagator stab = 2, orbit = 1 if it is symmetric under '
    'exchanging its legs, else stab = 1, orbit = 2.  (These coefficients are '
    'orbit times smaller than those of the average over all permutations.)  '
    'gamma_phi_On is a propagator structure\'s whole contribution at O(n), both '
    'orientations included.  '
    'Transcendentals: Schnetz f-alphabet in Lyndon polynomial normal form '
    '(f_3 = zeta(3), f_5, ..., f_3_5 = zeta(3)zeta(5) + zeta(5,3)/5, then f_3_7, '
    'f_3_3_5, ...; f6_... level-6 letters), sqrt(3) and I as in the data; beta_z '
    'is beta in the zeta notation: z3z5 = zeta(5,3), z3z7 = zeta(7,3), '
    'z533 = zeta(5,3,3), P711 = Period[7,11].  Expressions are sympy-readable '
    'strings in n (the number of scalars) and epsilon.  Four-point structures '
    'carry beta, beta_z and Z_lambda; two-point structures carry '
    'Zphi_minus_half, gamma_phi and gamma_phi_On.  The maps are keyed by the '
    'structure id, which is unique across all loop orders and matches the '
    'registry number shown in the atlas.  Two reducibility flags: vr is the raw '
    'topology -- the internal graph has a cut vertex -- while fac is what the '
    'atlas hides under "non-factorisable only": a structure whose tensor really '
    'splits into lower ones.  They differ on the leg-dressed structures, where a '
    'dressing always makes a cut vertex: fac keeps only a pure wave-function '
    'renormalisation -- a tree-level vertex with one irreducible self-energy '
    'on one leg -- and counts a vertex correction dressed on a leg, or '
    'dressings on more than one leg, as factorisable.  The pure wave-function '
    'renormalisations are exactly the dressed structures with non-vanishing '
    'beta.  Propagator structures also carry sym: whether the graph is '
    'symmetric under exchanging its two external legs.  The registry is '
    'unoriented, so an asymmetric graph appears once and stands for both '
    'orientations.  Every structure carries aut, the order of its automorphism '
    'group with the external legs held fixed and parallel lines included '
    '(the symmetry factor is 1/aut), and prim, true for a primitive graph: '
    '1PI with no UV subdivergence, so its counterterm is a single 1/epsilon '
    'pole.  For a propagator a subgraph whose contraction leaves a scaleless '
    'graph does not count, so the lowest-order propagator structure is '
    'primitive and no other is.')


def extract_data(html):
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S)
    if not m:
        raise SystemExit('no inlined data block found; update build.py')
    return json.loads(m.group(1))


def export(data, out):
    """Write the full set as one JSON document."""
    by_loop = {}
    for e in data:
        by_loop[e['L']] = by_loop.get(e['L'], 0) + 1
    doc = {
        'note': NOTE,
        'source': {
            'atlas': 'https://andstergiou.github.io/phi4-graph-atlas/',
            'repository': REPO,
            'graph_ordering_and_input_data':
                "O. Schnetz, HyperlogProcedures 0.8, "
                "https://github.com/oliverschnetz/HyperlogProcedures; "
                "seven-loop calculation: arXiv:2212.03663",
            'extraction':
                'Structures and coefficients extracted from HyperlogProcedures and '
                'recomputed by tensorial minimal subtraction with Claude Fable 5.1.  '
                'All values are in minimal subtraction (MS-bar).',
            'licence': 'CC BY 4.0',
        },
        'loops': sorted(by_loop),
        'counts': {
            'structures': len(data),
            'four_point': sum(1 for e in data if e['kind'] == '4'),
            'two_point': sum(1 for e in data if e['kind'] == '2'),
            'by_loop': {str(k): by_loop[k] for k in sorted(by_loop)},
        },
        'structures': [{k: e[k] for k in META if k in e} for e in data],
    }
    for src, name in list(FOUR_POINT.items()) + list(TWO_POINT.items()):
        doc[name] = {str(e['id']): e[src] for e in data if src in e}
    with open(out, 'w') as fh:
        json.dump(doc, fh, indent=1)
    return doc


def credit(n_structures, mb):
    return (
        '<div class="prov">Graph ordering and the seven-loop input data follow '
        "O. Schnetz's <a href=\"https://github.com/oliverschnetz/HyperlogProcedures\">"
        'HyperlogProcedures</a> 0.8; the structures and every coefficient shown here '
        'were extracted and recomputed by tensorial minimal subtraction (MS-bar) with '
        f'Claude Fable 5.1. The full set of {n_structures} structures is available as '
        f'<a href="{JSON_NAME}" download>{JSON_NAME}</a> ({mb:.1f} MB). Provenance, '
        f'citation and licence (CC BY 4.0): <a href="{REPO}">'
        'github.com/andstergiou/phi4-graph-atlas</a>.</div>')


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: python build.py <directory containing graph_atlas.html>')
    src = sys.argv[1]
    path = os.path.join(src, 'graph_atlas.html')
    if not os.path.exists(path):
        raise SystemExit(f'missing {path}')
    with open(path) as fh:
        html = fh.read()

    data = extract_data(html)
    json_path = os.path.join(HERE, JSON_NAME)
    export(data, json_path)
    mb = os.path.getsize(json_path) / 1048576
    print(f'{JSON_NAME}  ({len(data)} structures, {mb:.1f} MB)')

    if 'class="prov"' in html or 'class="dl"' in html:
        raise SystemExit('credit block already present')
    if html.lstrip().startswith('<!doctype'):
        raise SystemExit('the generated file now has its own doctype; update build.py')
    if CONV_RULE not in html or TABS not in html:
        raise SystemExit('the generated markup changed; update build.py')

    i = html.index('<div class="conv">')
    j = html.index('</div>', i) + len('</div>')
    html = html[:j] + '\n  ' + credit(len(data), mb) + html[j:]
    html = html.replace(
        TABS, TABS + f'\n  <a class="dl" href="{JSON_NAME}" download>Download JSON</a>', 1)
    html = HEAD + html.replace(CONV_RULE, CSS, 1)

    out = os.path.join(HERE, 'index.html')
    with open(out, 'w') as fh:
        fh.write(html)
    print(f'index.html    ({len(html) / 1048576:.1f} MB)')


if __name__ == '__main__':
    main()
