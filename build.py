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

When the directory also holds the gradient-flow conditions (conditions.html and
phi4_gradient.json, written by the same generator), it publishes them as well:

  conditions.html     the conditions page, with the same doctype and charset and a
                      header line giving its provenance and a link to the export.
  phi4_gradient.json  the conditions, with a map from structure id to atlas name.

    python build.py <directory containing graph_atlas.html>
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = 'https://github.com/andstergiou/phi4-graph-atlas'
JSON_NAME = 'phi4_atlas.json'
GRAD_NAME = 'phi4_gradient.json'

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
    'anomalous dimension, per structure, at 1 to 7 loops, with the antisymmetric '
    'upsilon of the gradient-flow vector field at 5 to 7 loops.  Every value is in '
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
    'On is the O(n) value of a single term of the orbit, so a structure '
    'contributes coefficient*orbit*On/3^V, V its number of vertices at O(n); gamma_phi_On is that '
    'contribution for a propagator structure, both orientations included.  '
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
    'orientations; those that carry upsilon are oriented as in its calculation, '
    'and their graph strings use the vertex numbers of its marked pole tables.  '
    'Every structure carries aut, the order of its automorphism '
    'group with the external legs held fixed and parallel lines included '
    '(the symmetry factor is 1/aut), and prim, true for a primitive graph: '
    '1PI with no UV subdivergence, so its counterterm is a single 1/epsilon '
    'pole.  For a propagator a subgraph whose contraction leaves a scaleless '
    'graph does not count, so the lowest-order propagator structure is '
    'primitive and no other is.  '
    'upsilon is given for the 163 asymmetric 1PI propagator structures at five to '
    'seven loops.  It is the coefficient of the structure in the antisymmetric '
    'upsilon_ij of the gradient-flow vector field, B_ijkl = beta_ijkl - '
    '(upsilon_im lambda_mjkl + perms), which is the S of arXiv:2402.17817: '
    'upsilon_ij = upsilon (G_ji - G_ij) + ..., with G_ij the tensor of the '
    'structure and leg i (the first entry of ext) on the end that the calculation '
    'calls i.  upsilon is in the f-alphabet and upsilon_z in zeta notation '
    '(z3 = zeta(3), z4 = zeta(4), ...).  upsilon_poles holds the marked pole '
    'tables.  index is m in upsilon^(L)_m, the s^(L)_m of arXiv:2402.17817.  '
    'labels maps the registry vertices to the vertex numbers of the table: 1 is '
    'the end of leg j and the largest number the end of leg i.  Each row '
    '[a, v, z^[orders[0]], ..., z^[1]] gives, in zeta notation, the counterterm '
    'Z_av = sum_r z^[r]_av / epsilon^r of the graph with momentum entering at '
    'the end a and leaving at the marked vertex v.  upsilon is half the sum over '
    'v of z^[1]_1v - z^[1]_tv, with t the end of leg i.')

# The page's record of upsilon -> the keys of the export.
UPSILON = {'value': 'upsilon', 'value_z': 'upsilon_z'}
UPSILON_POLES = ('index', 'labels', 'orders', 'rows')
UPSILON_CREDIT = ('The full calculation of upsilon (the S of W. H. Pannell and A. Stergiou, '
                  'Phys. Lett. B 853 (2024) 138701, arXiv:2402.17817) at five to seven loops, '
                  'with its marked pole tables, was performed by Claude Fable 5.1 and GPT-6 Astra.')


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
                'Structures and their beta and gamma coefficients extracted from '
                'HyperlogProcedures and recomputed by tensorial minimal subtraction '
                'with Claude Fable 5.1.  All values are in minimal subtraction (MS-bar).',
            'upsilon_calculation': UPSILON_CREDIT,
            'licence': 'CC BY 4.0',
        },
        'loops': sorted(by_loop),
        'counts': {
            'structures': len(data),
            'four_point': sum(1 for e in data if e['kind'] == '4'),
            'two_point': sum(1 for e in data if e['kind'] == '2'),
            'by_loop': {str(k): by_loop[k] for k in sorted(by_loop)},
            'upsilon': sum(1 for e in data if 'ups' in e),
        },
        'structures': [{k: e[k] for k in META if k in e} for e in data],
    }
    for src, name in list(FOUR_POINT.items()) + list(TWO_POINT.items()):
        doc[name] = {str(e['id']): e[src] for e in data if src in e}
    for src, name in UPSILON.items():
        doc[name] = {str(e['id']): e['ups'][src] for e in data if 'ups' in e}
    doc['upsilon_poles'] = {str(e['id']): {k: e['ups'][k] for k in UPSILON_POLES}
                            for e in data if 'ups' in e}
    with open(out, 'w') as fh:
        json.dump(doc, fh, indent=1)
    return doc


GRAD_NOTE = (
    'Gradient-flow conditions of the multiscalar phi^4 beta function in MS-bar, through seven '
    'loops, in d = 4 and d = 4 - epsilon.  Each condition is sum over terms of '
    'coefficient * product = 0.  A term is [coefficient, [ids]]: a four-point id stands for the '
    'beta coefficient of that structure (normalised as in phi4_atlas.json), a two-point id for '
    'its upsilon coefficient; names maps every id to its atlas name (u7_22 is upsilon^(7)_22).  '
    'The one-loop coefficient of V1.1 is 1 and is not written.  The conditions are derived order '
    'by order in the covariant form T_IJ B^J = d_I A of the gradient equation, solving at each '
    'loop order only for that order\'s metric and potential coefficients, with the lower ones the '
    'particular solutions whose free coefficients are set to zero.  The ansaetze are nested: '
    'gradient flow (a symmetric metric T_IJ = G_IJ) needs every condition of the quasi-gradient '
    'form T_IJ = G_IJ + d_[I w_J], which needs every condition of an arbitrary T_IJ ("general"), '
    'and d = 4 - epsilon needs every condition of d = 4, so gradient flow in d = 4 - epsilon needs '
    'all of them.  first_needed_by is the weakest ansatz that already needs a condition, and '
    'eps_only is true when only d = 4 - epsilon needs it.  counts gives, per loop order, how many '
    'conditions each ansatz needs in d = 4 and in d = 4 - epsilon; first_needed how many are new '
    'at each level.  Each condition is reduced modulo the lower-loop conditions times monomials '
    'and the weaker levels.  Every condition holds for the MS-bar beta and upsilon of '
    'phi4_atlas.json.')
GRAD_CREDIT = 'The conditions were derived and checked by Claude Opus 5.5.'


def publish_conditions(src, data):
    """conditions.html and phi4_gradient.json, when the generator wrote them."""
    page = os.path.join(src, 'conditions.html')
    grad = os.path.join(src, GRAD_NAME)
    if not (os.path.exists(page) and os.path.exists(grad)):
        return
    with open(grad) as fh:
        doc = json.load(fh)
    names = {}
    for e in data:
        names[str(e['id'])] = 'u%d_%d' % (e['L'], e['ups']['index']) if 'ups' in e else e['num']
    used = {str(f) for c in doc['conditions'] for t in c['terms'] for f in t[1]}
    out = {
        'note': GRAD_NOTE,
        'source': {'atlas': 'https://andstergiou.github.io/phi4-graph-atlas/conditions.html',
                   'repository': REPO, 'derivation': GRAD_CREDIT, 'licence': 'CC BY 4.0'},
        'counts': doc['counts'],
        'first_needed': doc['first_needed'],
        'names': {k: names[k] for k in sorted(used, key=int)},
        'conditions': doc['conditions'],
    }
    gpath = os.path.join(HERE, GRAD_NAME)
    with open(gpath, 'w') as fh:
        fh.write('{\n')
        keys = list(out)
        for i, k in enumerate(keys):
            end = ',\n' if i < len(keys) - 1 else '\n'
            if k == 'conditions':      # one condition per line
                fh.write(' "conditions": [\n' + ',\n'.join('  ' + json.dumps(c, separators=(',', ':')) for c in out[k]) + '\n ]' + end)
            else:
                fh.write(' ' + json.dumps(k) + ': ' + json.dumps(out[k], separators=(',', ':')) + end)
        fh.write('}\n')
    mb = os.path.getsize(gpath) / 1048576
    print(f'{GRAD_NAME}  ({len(doc["conditions"])} conditions, {mb:.1f} MB)')

    with open(page) as fh:
        html = fh.read()
    if html.lstrip().startswith('<!doctype') or 'class="prov"' in html:
        raise SystemExit('the generated conditions page changed; update build.py')
    i = html.index('<div class="conv">')
    j = html.index('</div>', i) + len('</div>')
    prov = ('<div class="prov">' + GRAD_CREDIT + f' The {len(doc["conditions"])} conditions are available as '
            f'<a href="{GRAD_NAME}" download>{GRAD_NAME}</a> ({mb:.1f} MB), each coefficient named by its '
            f'structure id. Provenance, citation and licence (CC BY 4.0): <a href="{REPO}">'
            'github.com/andstergiou/phi4-graph-atlas</a>.</div>')
    html = html[:j] + '\n  ' + prov + html[j:]
    html = HEAD + html.replace('</style>', CSS.replace(CONV_RULE, '') + '</style>', 1)
    with open(os.path.join(HERE, 'conditions.html'), 'w') as fh:
        fh.write(html)
    print(f'conditions.html ({len(html) / 1048576:.1f} MB)')


def credit(n_structures, mb):
    return (
        '<div class="prov">Graph ordering and the seven-loop input data follow '
        "O. Schnetz's <a href=\"https://github.com/oliverschnetz/HyperlogProcedures\">"
        'HyperlogProcedures</a> 0.8; the structures and their β and γ coefficients '
        'were extracted and recomputed by tensorial minimal subtraction (MS-bar) with '
        'Claude Fable 5.1. The full calculation of υ, the S of '
        '<a href="https://arxiv.org/abs/2402.17817">arXiv:2402.17817</a>, with its marked '
        'pole tables, was performed by Claude Fable 5.1 and GPT-6 Astra. '
        f'The full set of {n_structures} structures is available as '
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
    publish_conditions(src, data)


if __name__ == '__main__':
    main()
