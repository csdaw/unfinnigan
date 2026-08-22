---
title: FinniganScanEvent
original: https://code.google.com/p/unfinnigan/wiki/FinniganScanEvent
updated: 2011-04-04 05:41:06
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::ScanEvent`

[source]

## SYNOPSIS

```
use Finnigan;

my $e = Finnigan::ScanEventTemplate->decode(\*INPUT, $version);
say $e->size;
say $e->dump;
say join(" ", $e->preamble->list(decode => 'yes'));
say $e->preamble->analyzer(decode => 'yes');
$e->fraction_collector->dump;
$e->reaction->dump if $e->preamble->ms_power > 1 # Reaction will not be present in MS1
```

## Description

This decoder reads the [ScanEvent](../structures/ScanEvent.md) structure corresponding to an individual scan. It consists of a [ScanEventTemplate](../structures/ScanEventTemplate.md) augmented with the list of conversion coefficients (empty for scans done in peak mode) and the list of precursor ions (empty for base-level scans).

## Methods

- **decode($stream, $version)**
> The constructor method

- **purge_unused_data**
> Delete the location, size and type data for all structure elements. Calling this method will free some memory when no introspection is needeed (the necessary measure in production-grade code)

- **np**
> Get the number of precursor ions

- **preamble**
> Get the [Finnigan::ScanEventPreamble](FinniganScanEventPreamble.md) object

- **fraction_collector**
> Get the [Finnigan::FractionCollector](FinniganFractionCollector.md) object

- **precursors**
> Get the list full list of precursor descriptors [Finnican::Reaction](FinniganReaction.md) objects

- **reaction($n)**
> Get the precursor number *n* (a [Finnigan::Reaction](FinniganReaction.md) object). In the absence of the number argument, it returns the first precursor.

- **nparam**
> Get the number of conversion coefficients

- **unknown_double**
> Get the value of the unknown first coefficient (0 in all known cases)

- **I**
> Get the value of the coefficient *I* (0 in all known cases, Orbitrap data only)

- **A**
> Get the value of the coefficient *A* (0 in all known cases)

- **B**
> Get the value of the coefficient *B* (LTQ-FT, Orbitrap)

- **C**
> Get the value of the coefficient *C* (LTQ-FT, Orbitrap)

- **D**
> Get the value of the coefficient *D* (Orbitrap only)

- **E**
> Get the value of the coefficient *E* (Orbitrap only)

- **converter**
> Returns the pointer to the function for the forward conversion *f* → *M/z*

- **inverse_converter**
> Returns the pointer to the function for the inverse conversion *M/z* → *f*

- **stringify**
> Make a short text representation of the object

## See Also

[ScanEventTemplate](../structures/ScanEventTemplate.md) (structure)

[ScanEvent](../structures/ScanEvent.md) (structure)

[ScanEventPreamble](../structures/ScanEventPreamble.md) (structure)

[Finnigan::ScanEventPreamble](FinniganScanEventPreamble.md) (decoder object)

[FractionCollector](../structures/FractionCollector.md) (structure)

[Finnigan::FractionCollector](FinniganFractionCollector.md) (decoder object)

[Reaction](../structures/Reaction.md) (structure)

[Finnigan::Reaction](FinniganReaction.md) (decoder object)
