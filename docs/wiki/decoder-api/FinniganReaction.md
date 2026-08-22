---
title: FinniganReaction
original: https://code.google.com/p/unfinnigan/wiki/FinniganReaction
updated: 2011-04-04 06:00:55
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::Reaction`

[source]

## SYNOPSIS

```
use Finnigan;

my $r = Finnigan::Reaction->decode(\*INPUT);
say $r->precursor;
say $r->enengy;
```

## Description

This object contains a couple of double-precision floating point numbers that define the precursor ion M/z and the energy of the fragmentation reaction.

There are other elements that currently remain unknown: a double (set to 1.0 in all observations) and a couple longs.

## Methods

- **decode($stream)**
> The constructor method

- **precursor**
> Get the precursor *M/z*

- **energy**
> Get the fragmentation energy

- **stringify**
> Make a short text representation of the object (found inside Therom's "filter line")

## See Also

[ScanEvent](../structures/ScanEvent.md) (containing structure)
