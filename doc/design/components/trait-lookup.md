<!--
-*- markdown -*-
-*- coding: utf-8 -*-

michael a.g. aïvázis <michael.aivazis@para-sim.com>
(c) 1998-2026 all rights reserved
-->

# Trait lookup

A configurable finds the trait that answers to a name, its canonical name or one of its aliases,
through `Configurable._p2x_trait(alias)`. The lookup follows python's own attribute resolution:
inherited traits are found, and a nearer binding of a name hides whatever lies further up the
`__mro__`.

## What each class keeps

- Its `__dict__`, which holds each trait it declares under the trait's canonical name.
- Its `_p2x_namemap`, built by `Requirement`, which maps every alias of the traits it declares,
  canonical names included, to the canonical name.

Classes outside the framework, such as `object` or a plain mixin, have no namemap.

## The rules

1. A trait answers to its canonical name and to every alias it declares.
2. A derived class finds the traits of its ancestors.
3. A plain attribute named after a trait or one of its aliases hides it, from that class down.
4. A trait redeclared in a derived class replaces the inherited one, aliases included; it answers
   only to the aliases its own declaration gives it.
5. Ancestors are never affected by what their descendants declare.

The drivers in `tests/p2x.pkg/configurables/class_lookup_*.py` pin each rule down.

## The invariants

`Requirement` refuses any class that would break these:

- **I1**: if an alias `a` is in the namemap of a class `M`, then its canonical name `c` is in the
  `__dict__` of `M`, and `M.__dict__[c]` is a trait declared in the body of `M` that answers to
  `a`. Aliases that collide with each other or with a plain attribute of the same body are
  refused, so the namemap never points at the wrong binding.
- **I2**: a trait lives in exactly one class `__dict__`, under exactly one name. A trait bound a
  second time, in another class or under another name in the same body, is refused.

## The walk

Let the `__mro__` of the class be `M₀, M₁, …, Mₙ`, with `Dᵢ` the `__dict__` of `Mᵢ` and `Nᵢ` its
namemap, empty when it has none. The lookup walks the levels in order, remembering the ones it has
passed, and stops at the first level `k` where `a ∈ Nₖ` or `a ∈ Dₖ`:

- if `a ∈ Nₖ`, with `c = Nₖ[a]`: the lookup fails when `c ∈ Dᵢ` for some `i < k`, and returns
  `Dₖ[c]` otherwise;
- if `a ∈ Dₖ` but not in `Nₖ`, a plain attribute holds the alias, and the lookup fails;
- if no such level exists, the lookup fails.

## Why one walk is enough

The specification asks for two resolutions: find the trait `T` that `a` names, then check that
python, resolving the canonical name `c`, finds `T` and not something nearer. Let `py(c)` be the
smallest `i` with `c ∈ Dᵢ`, the level at which python's lookup of `c` stops. The specification
succeeds exactly when `D_py(c)[c]` is `T`.

**Lemma.** `py(c) ≤ k`. By I1, `c ∈ Dₖ`, and `py(c)` is the smallest level whose `__dict__` holds
`c`.

So the second resolution never looks past level `k`, and every level it examines was already
passed by the first. There are two cases:

- `py(c) = k`: no level before `k` holds `c`, and `Dₖ[c]` is `T`; the walk returns `T`.
- `py(c) < k`: some level before `k` holds `c`, and by I2 what it holds is not `T`, since `T`
  lives only in `Dₖ`; the walk fails.

In both cases the walk agrees with the specification. Without I2 the second case breaks: a
subclass that binds `T` itself under `c` would make python find `T`, while the walk would report
it hidden. That is why `Requirement` enforces I2.


<!-- end of file -->
