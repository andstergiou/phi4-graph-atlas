# φ⁴ Graph Atlas

An interactive atlas of the tensor structures of the multiscalar φ⁴ beta function
β<sub>ijkl</sub> and the anomalous dimension γ<sub>φ</sub>, through seven loops.

**→ [andstergiou.github.io/phi4-graph-atlas](https://andstergiou.github.io/phi4-graph-atlas/)**

## What is in it

6117 structures: 5812 four-point structures and 305 two-point structures, by loop
order 1, 4, 11, 41, 176, 875 and 5009 at L = 1…7. Each one is drawn as a Feynman
graph and comes with

- its label in the project's tables and its number in Schnetz's ordering
  (V = 1PI vertex structures, D = leg-dressed, S = propagator structures),
- the tensor contraction and the O(n) value,
- the β and counterterm (Z) coefficients, and γ where it contributes,
- the stabiliser and orbit size of the graph's symmetry,
- a TikZ export of the drawing exactly as it appears on screen.

The graph drawings are editable: drag a vertex to place it (it stays pinned), drag a
handle to curve a line, and the layout you arrive at is kept in the browser per
structure. The filter box takes structure numbers (`V6.12`, `D5.3`, `S2.1`), graph
ids (`#431`) and coefficient names (`b_{6,12}`, `f_7`). Individual structures are
addressable: `…/#L7-789`.

Conventions are stated in the page header: d = 4 − ε, λ₀ = μ^ε(λ + Z-poles), the loop
factor 1/(16π²) absorbed into λ, so the one-loop β is λ<sub>ijmn</sub>λ<sub>mnkl</sub> +
2 permutations with coefficient 1 and γ<sub>φ</sub> = (1/12) λ<sub>iklm</sub>λ<sub>jklm</sub>
at two loops.

## Provenance and citation

The graph ordering and the seven-loop input data come from Oliver Schnetz's Maple
package [HyperlogProcedures](https://github.com/oliverschnetz/HyperlogProcedures),
version 0.8, and the seven-loop calculation it implements. The coefficients displayed
here are not copied from the package: they are recomputed structure by structure by
tensorial minimal subtraction, in an independent Python implementation, and checked
against the published O(n)-symmetric results.

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
python build.py                              # -> index.html, with the credit line added
```

[`build.py`](build.py) is the whole of the difference between the generated file and
what is served: it adds one line to the header pointing at this repository. The page
is otherwise self-contained — all data is inlined as JSON — and loads only
[d3](https://d3js.org/) 7.9.0 from cdnjs (ISC licence) and two families from Google
Fonts.

It is about 5.4 MB uncompressed, 0.8 MB over the wire.

## Licence

[CC BY 4.0](LICENSE) — reuse freely with attribution.

Andreas Stergiou
