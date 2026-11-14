# φ⁴ Graph Atlas

An interactive atlas of the tensor structures of the multiscalar φ⁴ beta function
β<sub>ijkl</sub>, the anomalous dimension (γ<sub>φ</sub>)<sub>ij</sub> and the antisymmetric υ<sub>ij</sub> of the
gradient-flow vector field, through seven loops, in minimal subtraction (MS-bar).

**→ [andstergiou.github.io/phi4-graph-atlas](https://andstergiou.github.io/phi4-graph-atlas/)**

**→ [The gradient-flow conditions](https://andstergiou.github.io/phi4-graph-atlas/conditions.html)** through seven loops, on a second page.

Its cubic companion is the [φ³ Graph Atlas](https://andstergiou.github.io/phi3-graph-atlas/).

## What is in it

6117 structures: 5812 four-point structures and 305 two-point structures, by loop
order 1, 4, 11, 41, 176, 875 and 5009 at L = 1…7. Each one is drawn as a Feynman
graph and comes with

- its number in Schnetz's enumeration
  (V = 1PI vertex structures, D = leg-dressed, S = propagator structures),
- the tensor contraction and the O(N) value,
- the β and counterterm (Z) coefficients, and γ and υ where they contribute,
- the symmetry factor S = 1/|Aut|, and |stab| and orbit, which say how the tensor behaves
  under permuting its external indices,
- whether the graph is primitive,
- for the 163 asymmetric 1PI propagator structures at five to seven loops, which carry υ, its marked pole tables,
- for every β and υ coefficient, the gradient-flow conditions it enters,
- a TikZ export of the drawing exactly as it appears on screen.

**Non-factorisable only** hides the structures whose tensor really splits into lower
ones: an undressed structure whose internal graph has a cut vertex, a propagator chain,
and every leg-dressed structure except a pure wave-function renormalisation — a
tree-level vertex with one irreducible self-energy on one leg. A vertex correction
dressed on a leg, or self-energies on more than one leg, count as products and are
hidden. That leaves 4490 of the 6117 — 1, 3, 8, 27, 122, 621, 3708 at L = 1…7.

The cut is purely topological, but it lands on the physics: the vertex structures it
keeps are exactly the 4213 with non-vanishing β under minimal subtraction, plus V5.60 —
the accidental zero at five loops, a structure with no cut vertex whose β happens to
vanish. In particular the 439 leg-dressed structures that survive are precisely the
dressed structures with β ≠ 0, and the 807 undressed structures with a cut vertex all
have β = 0.

**Primitive only** keeps the primitive graphs: 1PI with no UV subdivergence, so the
counterterm is a single 1/ε pole. There are 61 — 60 vertex structures (1, 0, 1, 1, 3, 10,
44 at L = 1…7) and the sunset S2.1. For a propagator, a subgraph whose contraction leaves a
scaleless graph does not count; that is what keeps the sunset, and every propagator
structure from three loops on has a subdivergence that does count. The flag was checked
against Schnetz's table of φ⁴ periods (the file `Periods` in HyperlogProcedures). Each of
the 45 vertex graphs obtained by deleting a vertex of a completed primitive graph listed
there (L ≤ 7) is flagged, with β = 2(−1)<sup>L+1</sup>·S·P.
The other 15 are product graphs, whose completion has a three-vertex cut: β is the same
multiple of a product of periods (f₃², f₃f₅, f₅², f₃f₇, f₃³), and the table leaves these
graphs out. Every primitive has a single-pole counterterm, and among the 1PI structures
nothing else does. The one structure with a single pole that is not primitive is D2.3, the
tree vertex with the sunset on one leg: it is not 1PI, and its only divergence is the
primitive self-energy it carries (Z<sub>λ</sub> = 1/(24ε), β = 1/12 = γ<sub>φ</sub> of S2.1).

Every structure shows its **symmetry factor** S = 1/|Aut|, on its list row and in the
details pane. Automorphisms are counted with the external legs held fixed and parallel
lines included, so S = 1/2 for V1.1 and 1/6 for S2.1. Letting the legs move multiplies
|Aut| by exactly |stab|. Both counts were checked against an independent networkx count
on all 6117 structures.

**|stab| and orbit** describe how a structure's tensor behaves under permuting its
external indices. |stab| is the number of permutations of i j k l that leave the tensor
unchanged, which are exactly the leg permutations realised by an automorphism of the graph;
orbit = 24/|stab| is the number of distinct tensors the permutations produce. β and
Z<sub>λ</sub> both multiply the sum of those orbit terms, so β<sub>L</sub> = L times the 1/ε
residue of Z<sub>λ</sub>. V1.1, λ<sub>ijmn</sub>λ<sub>mnkl</sub> + 2 permutations, has
|stab| = 8, orbit = 3 and Z<sub>λ</sub> = 1/ε, giving β = 1. V6.11 and V6.36, two
decompletions of the same product graph with orbits 6 and 4, both have
Z<sub>λ</sub> = −40 f₃f₅/ε and β = −240 f₃f₅.

Propagators follow the same rule: exchanging i and j either leaves the tensor unchanged
(|stab| = 2, orbit = 1, a symmetric graph) or not (|stab| = 1, orbit = 2), and
Z<sub>φ</sub><sup>−½</sup> − 1 and γ<sub>φ</sub> multiply the sum of the orbit terms, so an
asymmetric graph's γ<sub>φ</sub> is the coefficient of G<sup>ij</sup> + G<sup>ji</sup>, and
γ<sub>φ</sub> = −L times the 1/ε residue of Z<sub>φ</sub><sup>−½</sup>. With every coefficient
normalised this way, each pure wave-function renormalisation — a tree-level vertex with
one self-energy S on one leg — has β equal to γ<sub>φ</sub> of S, for all 439 of them.

The **O(N) value** belongs to a single term of the orbit, like the tensor shown. A structure's
contribution at O(N) is therefore coefficient × orbit × O(N) value / 3<sup>V</sup>, where V is its
number of vertices (L + 1 for a vertex structure, L for a propagator) and each 1/3 comes from
λ<sub>ijkl</sub> = g(δ<sub>ij</sub>δ<sub>kl</sub> + δ<sub>ik</sub>δ<sub>jl</sub> + δ<sub>il</sub>δ<sub>jk</sub>)/3.
For V1.1 that is 1 × 3 × (N + 8)/9 = (N + 8)/3. Summed over the structures at a loop order it
gives the O(N) β and γ<sub>φ</sub> — for instance −(3N + 14)/3 and (N + 2)/36 at two loops.
`gamma_phi_On` in the export is already this contribution for each propagator structure.

**β only** and **γ only** restrict the list to the structures contributing to the beta
function or to the anomalous dimension; **all** puts them back. The page opens on the
one-loop beta structure, V1.1.

Every anomalous-dimension structure is marked **symmetric** or **asymmetric**, according to
whether its graph is unchanged under exchanging the two external legs. Under **γ only** a
second row branches from it, arrows fanning out to all · symmetric · asymmetric; it opens on
all each time γ only is chosen. Of the 305 propagator structures 117 are symmetric and 188 asymmetric; asymmetric
ones first appear at five loops (5 of 12), and at seven loops they outnumber the symmetric
160 to 70. The registry is unoriented, so an asymmetric graph appears once and stands for
both orientations. The 163 that carry υ are oriented as in its calculation (see below).

Every expression in the details pane can be copied as LaTeX: hover it and a **TeX**
button appears, putting the formula on the clipboard in standard syntax
(`\frac`, `\varepsilon`, `\zeta_{5,3}`, `\lambda_{ikab}`, `f^{(6)}_{2,9}`), ready to
paste into a paper.

On a phone the page becomes a single scrolling column — the list, then the graph, then its
details — with the conventions and sources behind a toggle. Tapping a structure brings its
graph into view, and the TeX buttons stay visible since there is no hover.

The graph drawings are editable: drag a vertex to place it (it stays pinned), drag a
handle to curve a line, and the layout you arrive at is kept in the browser per
structure. The filter box takes structure numbers (`V6.12`, `D5.3`, `S2.1`), graph
ids (`#431`) and coefficient names (`f_7`). It also finds υ<sup>(7)</sup><sub>105</sub> by `Y7.105`, its name in the gradient conditions, or by `u7_105`, and all the structures with υ by `upsilon`. Individual structures are
addressable: `…/#L7-789`.

Conventions are stated in the page header: d = 4 − ε, λ₀ = μ^ε(λ + Z-poles), the loop
factor 1/(16π²) absorbed into λ, so the one-loop β is λ<sub>ijmn</sub>λ<sub>mnkl</sub> +
2 permutations with coefficient 1 and (γ<sub>φ</sub>)<sub>ij</sub> = (1/12) λ<sub>iklm</sub>λ<sub>jklm</sub>
at two loops.

## The antisymmetric υ

The 163 asymmetric 1PI propagator structures at five, six and seven loops (4, 19 and 140) also carry υ<sup>(L)</sup><sub>m</sub>. This is their coefficient in the antisymmetric υ<sub>ij</sub> of the gradient-flow vector field B<sub>ijkl</sub> = β<sub>ijkl</sub> − (υ<sub>im</sub>λ<sub>mjkl</sub> + permutations). The 25 asymmetric chains carry none, so **γ only** → **asymmetric** with **non-factorisable only** lists exactly these 163.

The atlas writes υ for the quantity that [arXiv:2402.17817](https://arxiv.org/abs/2402.17817) calls S, because S already names the symmetry factor and the propagator structures here. Its υ<sup>(L)</sup><sub>m</sub> is the s<sup>(L)</sup><sub>m</sub> of that paper, with the same numbering, normalisation and sign.

A structure enters as υ<sub>ij</sub> = υ<sup>(L)</sup><sub>m</sub> (G<sub>ji</sub> − G<sub>ij</sub>) + …, with G<sub>ij</sub> the tensor shown. The sign depends on which end carries i. These 163 structures are therefore oriented as in the calculation of υ, with leg i on the end that it calls i. For 94 of them this exchanges i and j relative to earlier versions of the atlas. Their tensors change, but γ<sub>φ</sub> does not, since it multiplies G<sup>ij</sup> + G<sup>ji</sup>.

The details pane gives υ<sup>(L)</sup><sub>m</sub> in the f-alphabet and in zeta notation. Below the drawing a panel shows the **marked pole tables**. Each row is a marked graph: momentum p enters at an end a and leaves at an internal vertex v, the marked vertex. Its counterterm in minimal subtraction is Z<sub>a,v</sub> = Σ<sub>r</sub> z<sup>[r]</sup><sub>a,v</sub>/ε<sup>r</sup>. Hovering a row rings the vertex a on the drawing and marks the vertex v, and clicking the row keeps the mark.

The vertices are numbered as in the tables of the calculation, in the drawing and in the graph string alike. Vertex 1 is the end of leg j and the largest number is the end of leg i; at five and six loops the number 3 is not used. The coefficient follows from the simple poles as υ = ½ Σ<sub>v</sub>(z<sup>[1]</sup><sub>1,v</sub> − z<sup>[1]</sup><sub>t,v</sub>), with t the end of leg i. These structures open on the drawing that accompanies the tables, with leg i on the left and leg j on the right. **Copy as LaTeX** gives a table as a `tabular`, and the TikZ export includes a mark that is kept. The panel can be hidden, and the page remembers the choice.

## The gradient-flow conditions

The [conditions page](https://andstergiou.github.io/phi4-graph-atlas/conditions.html) lists the conditions for the RG flow to be gradient, T<sub>IJ</sub>B<sup>J</sup> = ∂<sub>I</sub>A, through seven loops. B is the vector field above, β corrected by υ. There are 2058 conditions, in d = 4 and in d = 4 − ε.

Each condition is a polynomial set to zero, in the form of the six-loop analysis of [arXiv:2402.17817](https://arxiv.org/abs/2402.17817). A structure name such as V7.2 or D2.3 stands for the β coefficient of that structure, normalised as everywhere in the atlas. A name such as Y7.105 stands for the υ coefficient υ<sup>(7)</sup><sub>105</sub>. The one-loop coefficient of V1.1 is 1 and is not written. A condition can mix loop orders. G4.2, for instance, reads

    V4.13 + 2 V4.21 − 2 V2.2·V3.6 + 2 D2.3·V3.7 − 2 D2.3·V3.8 = 0

The conditions are derived order by order in the covariant form of the gradient equation. At each loop order only the metric and potential coefficients of that order are solved for. The lower ones enter as the particular solutions with their free coefficients set to zero. A different choice, tested at six and seven loops, gives the same conditions.

Each condition is reduced modulo the lower-loop conditions times monomials, so it carries no multiple of a lower one. The reduction also replaces a coefficient that leads a lower-loop condition wherever it would appear in a product. That is why V4.13 occurs only in G4.2.

The three ansätze for T<sub>IJ</sub> are nested:

| ansatz | T<sub>IJ</sub> |
| --- | --- |
| any T<sub>IJ</sub> | arbitrary: a potential A merely exists |
| quasi-gradient | G<sub>IJ</sub> + ∂<sub>[I</sub>w<sub>J]</sub>, with G<sub>IJ</sub> symmetric |
| gradient | a symmetric metric G<sub>IJ</sub> |

Each ansatz needs every condition of the ones above it, and d = 4 − ε needs every condition of d = 4. Gradient flow in d = 4 − ε therefore needs all of them. The number of conditions each ansatz needs:

| loops | d = 4: any T<sub>IJ</sub> | quasi-gradient | gradient | d = 4 − ε: any T<sub>IJ</sub> | quasi-gradient | gradient |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| 5 | 28 | 33 | 37 | 32 | 37 | 41 |
| 6 | 144 | 193 | 225 | 176 | 230 | 266 |
| 7 | 899 | 1290 | 1481 | 1075 | 1520 | 1747 |

Each condition is marked with the weakest ansatz that already needs it, and with whether only d = 4 − ε needs it. At four loops all four conditions are needed already for any T<sub>IJ</sub>. Going from any T<sub>IJ</sub> to the quasi-gradient form adds 0, 5, 49 and 391 conditions at four to seven loops, and going on to a symmetric metric adds 0, 4, 32 and 191. The page can show either all the conditions an ansatz needs or only those new at its level.

Through six loops the conditions agree with those of arXiv:2402.17817, up to multiples of lower-loop conditions. In d = 4 − ε there are 41 at six loops rather than the 32 published, and the 32 lie among them. At seven loops d = 4 − ε adds 266, 230 and 176 conditions for the gradient, quasi-gradient and general metrics. These are the d = 4 counts at six, five and four loops added up.

Every condition holds for the MS-bar β and υ of the atlas. Without υ they fail from six loops on: β alone is not gradient. Six conditions at seven loops contain no seven-loop coefficient, G7.895 to G7.899 and G7.1290. Four of them constrain υ<sup>(5)</sup> and υ<sup>(6)</sup>, and two relate β coefficients up to six loops. All six hold in MS-bar.

The page filters the conditions by loop order, by the ansatz and dimension that need them, and by coefficient or condition id (`V7.2`, `D2.3`, `Y7.105`, `G7.123`). Each coefficient in a condition links to its structure in the atlas. **Copy as LaTeX** writes the β coefficient of V7.2 as `\beta_{\mathrm{V}7.2}` and Y7.105 as `\upsilon_{\mathrm{Y}7.105}`. In the atlas, the details pane of every coefficient gives how many conditions it enters, how many of them each ansatz needs, which ones it leads, and a link to them.

## The data

The whole set is in [`phi4_atlas.json`](phi4_atlas.json) — 9.4 MB, 0.9 MB gzipped —
served next to the page, so it can be fetched directly:

```
curl -O https://andstergiou.github.io/phi4-graph-atlas/phi4_atlas.json
```

It holds all loop orders in one document:

| key | contents |
| --- | --- |
| `note`, `source` | conventions, provenance, licence |
| `loops`, `counts` | 1…7, and the structure counts per loop order |
| `structures` | one record each: `id`, `L`, `kind`, `num`, `edges`, `ext`, `stab`, `orbit`, `aut`, `prim`, `On`, `tensor`, `graph`, `onepi`, `vr`, `fac`, `sym`, `comp` |
| `beta`, `beta_z`, `Z_lambda` | four-point expressions, keyed by structure id |
| `Zphi_minus_half`, `gamma_phi`, `gamma_phi_On` | two-point expressions, keyed by structure id (`gamma_phi_On`: both orientations at O(N)) |
| `upsilon`, `upsilon_z`, `upsilon_poles` | υ<sup>(L)</sup><sub>m</sub> in the f-alphabet and in zeta notation, and its marked pole tables, keyed by structure id |

Each entry of `upsilon_poles` has `index` (the m of υ<sup>(L)</sup><sub>m</sub>), `labels` (registry vertex → number in the table), `orders` (the pole orders, highest first) and `rows`. A row `[a, v, z^[orders[0]], …, z^[1]]` holds the coefficients of Z<sub>a,v</sub> in zeta notation.

Expressions are sympy-readable strings in `n` (the N of O(N)) and `epsilon`; `id` is unique across
loop orders and is the registry number the atlas displays. Two reducibility flags travel with each
structure: `vr` is the raw topology (the internal graph has a cut vertex), and `fac` is
what the "non-factorisable only" filter hides, so the same cut can be made on the data:
`[s for s in d['structures'] if not s['fac']]`. Propagator structures
also carry `sym`, true when the graph is symmetric under exchanging its two external legs. `vr` and `fac` differ exactly on the leg-dressed
structures, as described above. Every structure carries `aut`, the |Aut| above (its
symmetry factor is `1/aut`), and `prim`, the primitive flag.

The conditions are in [`phi4_gradient.json`](phi4_gradient.json), 7.1 MB, 1.8 MB gzipped:

| key | contents |
| --- | --- |
| `note`, `source` | conventions, provenance, licence |
| `counts` | per loop order, the number of conditions each ansatz needs in `d=4` and in `d=4-eps` |
| `first_needed` | per loop order, the number new at each level |
| `names` | structure id → atlas name (`Y7.105` is υ<sup>(7)</sup><sub>105</sub>) |
| `conditions` | one record each: `id`, `L`, `first_needed_by` (the weakest ansatz that needs it: `general` for any T<sub>IJ</sub>, `quasi-gradient` or `gradient`), `eps_only` (true when only d = 4 − ε needs it) and `terms` |

A term is `[coefficient, [ids]]`, with the coefficient a rational number as a string. A four-point id stands for the β coefficient of that structure and a two-point id for its υ coefficient.

```python
import json, sympy
d = json.load(open('phi4_atlas.json'))
v71 = next(s for s in d['structures'] if s['num'] == 'V7.1')
print(d['beta'][str(v71['id'])])            # f_3/960 - 197/2048 - pi**4/14400
print(sympy.sympify(d['gamma_phi_On']['4583']))
s53 = next(s for s in d['structures'] if s['num'] == 'S5.3')
print(d['upsilon'][str(s53['id'])])         # 259/4608, which is upsilon^(5)_2
g = json.load(open('phi4_gradient.json'))
c = next(c for c in g['conditions'] if c['id'] == 'G4.2')
print([(q, [g['names'][str(f)] for f in fs]) for q, fs in c['terms']])
# [('1', ['V4.13']), ('2', ['V4.21']), ('-2', ['V2.2', 'V3.6']), ...]
```

## Transcendentals: the f-alphabet

Every value in the atlas is in **minimal subtraction (MS-bar)**. The coefficients are
written in Schnetz's f-alphabet in Lyndon polynomial normal form; `beta_z` carries the
same numbers in the zeta notation instead. Powers of π appear directly in both.

The f-words that occur through seven loops map to multiple zeta values exactly as
follows (solved from Schnetz's period files, which carry both forms):

| symbol | value | first appears |
| --- | --- | --- |
| `f_3`, `f_5`, `f_7`, `f_9`, `f_11` | ζ(3), ζ(5), ζ(7), ζ(9), ζ(11) | 3, 4, 5, 6, 7 loops |
| `f_3_5` | ζ(3)ζ(5) + ζ(5,3)/5 | 6 loops |
| `f_3_7` | ζ(3)ζ(7) + (3/14)ζ(5)² + ζ(7,3)/14 | 7 loops |
| `f_3_3_5` | ζ(3)²ζ(5)/2 + ζ(3)ζ(5,3)/5 − ζ(5,3,3)/5 + π⁶ζ(5)/1890 − π⁴ζ(7)/150 − (3/2)π²ζ(9) | 7 loops |

In the zeta notation of `beta_z`: `z3`…`z11` are ζ(3)…ζ(11), and the irreducible
multiple zeta values get their own symbols — `z3z5` = ζ(5,3), `z3z7` = ζ(7,3),
`z533` = ζ(5,3,3). `P711` is Period[7,11], the seven-loop period that is not an MZV.

`upsilon_z` gives υ in the same zeta notation. The marked pole tables use it too, as the calculation of υ does. There the even zeta values appear by name: `z4` = ζ(4) = π⁴/90 and `z6` = ζ(6) = π⁶/945.

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
here were not copied from the package: they were extracted by **Claude Fable 5.1**
with an independent Python implementation of the forest formula, and checked against
Schnetz's published O(N)-symmetric results. The integrals behind β and γ were not recomputed by AI.

The full calculation of υ, with its marked pole tables, was performed by **Claude Fable 5.1** and **GPT-6 Astra**.

The gradient-flow conditions were derived and checked by **Claude Opus 5.5**, with an independent order-by-order solution of the gradient equation. Through six loops they reproduce arXiv:2402.17817.

If you use this atlas, please cite Schnetz's work alongside it, and for υ and the gradient-flow conditions the paper that defines them:

- O. Schnetz, *Seven loops φ⁴*, [arXiv:2212.03663](https://arxiv.org/abs/2212.03663).
- O. Schnetz, *HyperlogProcedures*, version 0.8 (2025),
  <https://github.com/oliverschnetz/HyperlogProcedures>.
- W. H. Pannell and A. Stergiou, *Gradient properties of perturbative multiscalar RG flows to six loops*, Phys. Lett. B 853 (2024) 138701, [arXiv:2402.17817](https://arxiv.org/abs/2402.17817).

No HyperlogProcedures code is redistributed here. The package is offered under
GPL-3.0 on its repository (the 0.8 distribution itself ships no licence text); the
graph topologies shown in this atlas are re-encoded from its graph list, and the
numbers beside them are this project's own computation.

## How the page is built

The atlas page is generated from the results of the computation;
[`build.py`](build.py) is the whole of the difference between the generated file and
what is served: it adds a doctype and a UTF-8 charset, one header line giving the
provenance, a download link, and it writes the JSON export out of the page's own
inlined data. The page
is otherwise self-contained — all data is inlined as JSON — and loads only
[d3](https://d3js.org/) 7.9.0 from cdnjs (ISC licence) and two families from Google
Fonts.

It is about 5.9 MB uncompressed, 0.9 MB over the wire.

The conditions page is built the same way, with the conditions inlined: 7.2 MB uncompressed, 1.8 MB over the wire. The atlas page fetches [`phi4_gradient.json`](phi4_gradient.json) only when it first shows a coefficient's conditions.

## Licence

[CC BY 4.0](LICENSE) — reuse freely with attribution.

Andreas Stergiou
