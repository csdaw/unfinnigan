---
title: FinniganFractionCollector
original: https://code.google.com/p/unfinnigan/wiki/FinniganFractionCollector
updated: 2011-04-04 08:38:40
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::FractionCollector`

[source]

## SYNOPSIS

```
use Finnigan;

my $f = Finnigan::FractionCollector->decode(\*INPUT);
say "$f";
```

## Description

[FractionCollector](../structures/FractionCollector.md) object is just a container for a pair of double-precision floating point numbers that define the *M/z* range of ions collected during a scan.

## Methods

- **decode($stream)**
> The constructor method

- **low**
> Get the low *M/z*

- **high**
> Get the high *M/z*

- **stringify**
> Make a string representation of the object: "`[`low-high`]`", as in Thermo's "filter line"

## See Also

[FractionCollector](../structures/FractionCollector.md) (structure)

[ScanEvent](../structures/ScanEvent.md) (containing structure)

[Finnigan::ScanEvent](FinniganScanEvent.md) (containing object)
