# φ⁴ Graph Atlas

An interactive atlas of the tensor structures of the multiscalar φ⁴ beta function
β<sub>ijkl</sub> and the anomalous dimension γ<sub>φ</sub>, through seven loops, in
minimal subtraction (MS-bar).

**→ [andstergiou.github.io/phi4-graph-atlas](https://andstergiou.github.io/phi4-graph-atlas/)**

Its cubic companion is the [φ³ Graph Atlas](https://andstergiou.github.io/phi3-graph-atlas/).

## What is in it

6117 structures: 5812 four-point structures and 305 two-point structures, by loop
order 1, 4, 11, 41, 176, 875 and 5009 at L = 1…7. Each one is drawn as a Feynman
graph and comes with

- its number in Schnetz's enumeration
  (V = 1PI vertex structures, D = leg-dressed, S = propagator structures),
- the tensor contraction and the O(n) value,
- the β and counterterm (Z) coefficients, and γ where it contributes,
- the stabiliser and orbit size of the graph's symmetry,
- a TikZ export of the drawing exactly as it appears on screen.

**Non-factorisable only** hides the one-vertex-reducible structures: those whose
internal graph has a cut vertex, so the tensor factorises through a single vertex.
That leaves 4051 of the 6117 — 1, 2, 7, 23, 107, 552, 3359 at L = 1…7. Every
leg-dressed structure (all 1230) and every propagator chain (all 29) is of this kind,
and the 807 undressed ones all have vanishing β under minimal subtraction: the single
structure with β = 0 that survives the filter is V5.60, the accidental zero at five
loops. It is the same test as `is_1vr` in the project's `PredictSevenLoopEpsilon.py`.

The graph drawings are editable: drag a vertex to place it (it stays pinned), drag a
handle to curve a line, and the layout you arrive at is kept in the browser per
structure. The filter box takes structure numbers (`V6.12`, `D5.3`, `S2.1`), graph
ids (`#431`) and coefficient names (`b_{6,12}`, `f_7`). Individual structures are
addressable: `…/#L7-789`.

Conventions are stated in the page header: d = 4 − ε, λ₀ = μ^ε(λ + Z-poles), the loop
factor 1/(16π²) absorbed into λ, so the one-loop β is λ<sub>ijmn</sub>λ<sub>mnkl</sub> +
2 permutations with coefficient 1 and γ<sub>φ</sub> = (1/12) λ<sub>iklm</sub>λ<sub>jklm</sub>
at two loops.

## The data

The whole set is in [`phi4_atlas.json`](phi4_atlas.json) — 8.7 MB, 0.8 MB gzipped —
served next to the page, so it can be fetched directly:

```
curl -O https://andstergiou.github.io/phi4-graph-atlas/phi4_atlas.json
```

It follows the shape of the project's `renorm_L*.json` files, with all loop orders in
one document:

| key | contents |
| --- | --- |
| `note`, `source` | conventions, provenance, licence |
| `loops`, `counts` | 1…7, and the structure counts per loop order |
| `structures` | one record each: `id`, `L`, `kind`, `num`, `edges`, `ext`, `stab`, `orbit`, `On`, `tensor`, `graph`, `onepi`, `vr`, `comp` |
| `beta`, `beta_z`, `Z_lambda` | four-point expressions, keyed by structure id |
| `Zphi_minus_half`, `gamma_phi`, `gamma_phi_On` | two-point expressions, keyed by structure id |

Expressions are sympy-readable strings in `n` and `epsilon`; `id` is unique across
loop orders and is the registry number the atlas displays. `vr` is the
one-vertex-reducible flag the "non-factorisable only" filter uses, so the same cut can
be made on the data: `[s for s in d['structures'] if not s['vr']]`. The L = 7 entries agree
with `renorm_L7.json` expression for expression.

```python
import json, sympy
d = json.load(open('phi4_atlas.json'))
v71 = next(s for s in d['structures'] if s['num'] == 'V7.1')
print(d['beta'][str(v71['id'])])            # f_3/960 - 197/2048 - pi**4/14400
print(sympy.sympify(d['gamma_phi_On']['4583']))
```

## Transcendentals: the f-alphabet

Every value in the atlas is in **minimal subtraction (MS-bar)**. The coefficients are
written in Schnetz's f-alphabet in Lyndon polynomial normal form; `beta_z` carries the
same numbers in the zeta notation instead. Powers of π appear directly in both.

The f-words that occur through seven loops map to multiple zeta values exactly as
follows (this is `F_TO_Z` in the project's `renorm.py`, solved from Schnetz's own
period files, which carry both forms):

| symbol | value | first appears |
| --- | --- | --- |
| `f_3`, `f_5`, `f_7`, `f_9`, `f_11` | ζ(3), ζ(5), ζ(7), ζ(9), ζ(11) | 3, 4, 5, 6, 7 loops |
| `f_3_5` | ζ(3)ζ(5) + ζ(5,3)/5 | 6 loops |
| `f_3_7` | ζ(3)ζ(7) + (3/14)ζ(5)² + ζ(7,3)/14 | 7 loops |
| `f_3_3_5` | ζ(3)²ζ(5)/2 + ζ(3)ζ(5,3)/5 − ζ(5,3,3)/5 + π⁶ζ(5)/1890 − π⁴ζ(7)/150 − (3/2)π²ζ(9) | 7 loops |

In the zeta notation of `beta_z`: `z3`…`z11` are ζ(3)…ζ(11), and the irreducible
multiple zeta values get their own symbols — `z3z5` = ζ(5,3), `z3z7` = ζ(7,3),
`z533` = ζ(5,3,3). `P711` is Period[7,11], the seven-loop period that is not an MZV.

Only Lyndon words appear as generators, so a word like `f_3_3` is never written: the
shuffle algebra is the polynomial algebra on the Lyndon words, and the reductions are

    f_3_3 = f_3²/2        f_3_3_3 = f_3³/6      f_5_5 = f_5²/2
    f_5_3 = f_3 f_5 − f_3_5 = −ζ(5,3)/5         f_3_5_3 = f_3 f_3_5 − 2 f_3_3_5

Squares therefore show up as ordinary monomials (`f_3**2`), not as words.

Two more symbols appear at seven loops only. The level-6 letters `f6_2_3_3_3`,
`f6_2_9`, `f6_4_7`, `f6_6_5` and `f6_8_3` occur solely in the combination that equals
a rational multiple of Period[7,11]; `beta_z` collapses them to `P711`. And `sqrt(3)`
and `I` occur in exactly one structure, V7.2855, in its β and Z_λ.

The weights behave as they should: the heaviest f-word in β at L loops is weight
2L − 3 — 3, 5, 7, 9, 11 at L = 3…7.


## Provenance and citation

The graph ordering and the seven-loop input data come from Oliver Schnetz's Maple
package [HyperlogProcedures](https://github.com/oliverschnetz/HyperlogProcedures),
version 0.8, and the seven-loop calculation it implements. The coefficients displayed
here are not copied from the package: they are recomputed structure by structure by
tensorial minimal subtraction, in an independent Python implementation, and checked
against the published O(n)-symmetric results.

The structures and coefficients were extracted from HyperlogProcedures and recomputed
with **Claude Fable 5.1**.

If you use this atlas, please cite Schnetz's work alongside it:

- O. Schnetz, *Seven loops φ⁴*, [arXiv:2212.03663](https://arxiv.org/abs/2212.03663).
- O. Schnetz, *HyperlogProcedures*, version 0.8 (2025),
  <https://github.com/oliverschnetz/HyperlogProcedures>.

No HyperlogProcedures code is redistributed here. The package is offered under
GPL-3.0 on its repository (the 0.8 distribution itself ships no licence text); the
graph topologies shown in this atlas are re-encoded from its graph list, and the
numbers beside them are this project's own computation.

## How the page is built

The atlas is generated in the research repository, then copied here:

```
python schnetz/extracted/graph_viewer.py 7   # -> schnetz/extracted_results/graph_atlas.html
python build.py                              # -> index.html + phi4_atlas.json
```

[`build.py`](build.py) is the whole of the difference between the generated file and
what is served: it adds a doctype and a UTF-8 charset, one header line giving the
provenance, a download link, and it writes the JSON export out of the page's own
inlined data. The page
is otherwise self-contained — all data is inlined as JSON — and loads only
[d3](https://d3js.org/) 7.9.0 from cdnjs (ISC licence) and two families from Google
Fonts.

It is about 5.4 MB uncompressed, 0.8 MB over the wire.

## Licence

[CC BY 4.0](LICENSE) — reuse freely with attribution.

Andreas Stergiou
