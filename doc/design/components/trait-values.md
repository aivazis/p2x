<!--
-*- markdown -*-
-*- coding: utf-8 -*-

michael a.g. aïvázis <michael.aivazis@para-sim.com>
(c) 1998-2026 all rights reserved
-->

# Trait values

How configurable classes read the values of their traits, and how component classes hold them.
The work proceeds in small steps, and each step records the decisions it made, the constraints
that shaped them, and the alternatives it set aside. Instances come after classes.

## What is

### Decisions

Where values live:

1. A value is held in a slot, which carries the value and a locator that records where the value
   was set.
2. Every trait has a slot, which holds its default; `default` reads and writes that slot. All
   kinds of traits keep their defaults the same way, so nothing that handles them needs to tell
   them apart. A default assigned to a trait records the line of the assignment, in a class body
   or anywhere else; a default given by the constructor, the preference of the kind of trait or
   an argument, records an unknown location, since no line of the user's can be named. Metadata
   is set by assignment, by convention, so the precise case is the prescribed one.
3. A class has a slot of its own for a trait only once a value is set for it after the class
   exists, which sets the class apart from the default position; a class that was never written
   owns none. The class body is all declarations: `kerf = 0.25` in the body of a derived class
   makes a plain attribute that shadows the inherited trait, as in python.
4. Only components hold values. Writes, which give a class a slot of its own, belong to `Actor`.
   Names that start with `_p2x_` belong to the framework: `Actor` hands their writes and deletes
   straight to python, without looking for a trait, since the framework writes them while the
   class is being built and its namemap may not exist yet; no trait or alias may take such a
   name. pyre 1.x does the same with `pyre_`, without the refusal.
   A protocol trait is a specification of what an implementer must provide, and its default is
   part of that specification. How protocols and components relate is examined once class state
   is settled.

Reading:

5. Reads belong to `Requirement`, so protocols and components alike read their traits. A class
   read reaches the class through the trait: python calls the trait's `__get__` with the class as
   its owner, and the trait hands the request to the class, which knows its values.
6. A read finds the nearest slot along the `__mro__`: the class's own, if it has one; otherwise
   that of the nearest ancestor that has one; otherwise the trait's own, which holds the current
   default. A later change to the default is seen by every class that was never written. For a
   protocol, the read always ends at the trait's slot. The walk stops at the class that declares
   the trait, since no class above it can hold a value for it; this keeps a redeclared trait from
   finding the values of the one it replaces, which are filed under the same name.

   Reads under an alias find nothing by that name in the class, so python hands them to
   `Requirement.__getattr__`, which resolves the alias and reads the trait. A read that fails
   with an `AttributeError`, such as a default that names something its module lacks, would pass
   for a missing attribute, so `hasattr` would deny the trait and `getattr` would hand out the
   caller's fallback; both paths report it as a `TraitReadError` instead, chained to the original.

Reading and writing:

7. Values are read and written under the trait's name or any of its aliases; aliases that are not
   python identifiers go through `getattr` and `setattr`.
8. Deleting a class's value removes its slot, and the class inherits again. Deleting a value the
   class never set is harmless, as it is for instances.
9. A trait redeclared in a derived class starts from its own default; the values set for the
   trait it replaces do not reach it.
10. A name that does not resolve to a trait, because no trait answers to it or because a plain
    attribute hides it, is read, written and deleted as python would.
11. Values are held as given. Conversion arrives with the schemata.
12. A class read of a behavior gives its default, the method it decorates, which is what python
    gives for a method. A class write of a behavior gives the class a slot like any other trait,
    and its descendants read the new method; no driver pins this down until instances are
    designed.
13. A class write records the line that made it, under the trait's name or an alias.

### Constraints

- `Requirement` and its subclasses set framework attributes, such as `_p2x_namemap`, on the class
  while it is being built. The path that turns class writes into trait values must tell those
  apart from writes of trait values; decision 4 is how it does.
- The store, the schemata and the observers are parked, but they are not far off: defaults need
  the schemata to become real values, slots carry the metadata of trait values, and observers are
  the reason for the whole design. The slot must leave room for priorities, converted values and
  observers.

The drivers in `tests/p2x.pkg/components/class_value_*.py` pin down decisions 3, 6 through 10,
and 13. The drivers `tests/p2x.pkg/configurables/class_names_*.py`, `components/class_names_write.py` and
`components/instance_names.py` check that names that are not traits behave as python defines
them, so the machinery that handles traits never disturbs the rest of a class.

### Still open

- How instances hold their values, and whether they follow the pattern of classes. The decisions
  above were made for classes alone, and some of them may not suit instances; they stay open to
  revision when instances are designed.
- How a protocol names its default implementation. pyre 1.x uses the class method
  `pyre_default`, which breaks the symmetry with the `default` of properties; its body runs late,
  so it can reach the component class without an import cycle, and the default of a facility
  invokes it. A property on the metaclass gives classes a `default` that reads and writes, and
  could hold the protocol's default in a slot inherited along the `__mro__`; but it claims the
  name, since a metaclass data descriptor wins over the class `__dict__`, and a stored value is
  eager. To be settled when facilities arrive.

## Alternatives set aside

- **Values for protocol traits.** Set aside because a protocol trait specifies what an implementer
  provides; reading it gives the default of the specification, and a protocol has no use for a
  value of its own. pyre 1.x agrees, since only the component metaclass builds an inventory. The
  default of a protocol trait may yet serve the components that implement the protocol, which is
  a question about their relationship.
- **Assignment in the class body as a value.** Reading `kerf = 0.25` in a derived class as a new
  value for the inherited trait was set aside as a source of trouble: the body would mean
  different things depending on what the ancestors declare. It shadows, as in python and pyre 1.x.
- **A default captured when the class is built.** Copying the default into each class would give
  every class a value before anyone set one, and a later change to the trait's default would
  reach none of them. Set aside in favor of the trait's slot, where every read that finds no
  class slot ends.
- **A slot for every trait in every class, from the start.** This is how pyre 1.x builds its
  inventories: the slot of an inherited trait starts as a reference to the slot of the ancestor.
  Set aside because, without observers, nothing needs a slot in a class that was never written,
  and python's resolution along the `__mro__` already gives inheritance. Observers may bring it
  back.
- **Traits without slots.** A `Slotted` class between `Trait` and the traits that need slots, as
  in pyre 1.x, would let a behavior keep its method as a plain default. Set aside because reads
  would then have to ask which kind of trait they hold, which decision 2 exists to avoid; a slot
  costs one small object and gives every default a locator. A kind of trait that needs its
  default elsewhere can override the view, and the reason is recorded here.
- **A located constructor default.** The constructor could record the line that built the trait
  by climbing a fixed number of frames. Set aside because the user's line sits at a different
  depth for each kind of trait, and deeper still for traits derived outside p2x, so a fixed level
  points into the framework.
- **Framework writes that bypass `Actor` explicitly.** Framework code could write its attributes
  with `type.__setattr__`, so they never reach the trait path. Set aside because every framework
  write would have to remember it, and nothing would stop a trait or alias from taking a
  framework name; reserving the prefix makes the rule hold for everyone.
- **A slot that holds only the value.** Set aside because the values carry metadata, starting
  with where they came from, and a bare value has nowhere to keep it.
- **Slots as observable nodes, now.** In pyre 1.x a slot is a node of the calculator: it holds a
  priority, a locator and possibly an expression over other nodes, and the slots of public
  components are registered with the nameserver. Observing is what the design is after, but it
  needs the nameserver and the store, which are parked. Revisit when they return.


<!-- end of file -->
