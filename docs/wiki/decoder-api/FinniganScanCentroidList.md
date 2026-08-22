---
title: FinniganScanCentroidList
original: https://code.google.com/p/unfinnigan/wiki/FinniganScanCentroidList
updated: 2011-04-04 03:23:20
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::Scan::CentroidList`

[source]

## SYNOPSIS

```
use Finnigan;

my $c = Finnigan::Scan::CentroidList->decode(\*INPUT);
say $c->count;
say $c->list->[0]->[0]; # M/z
say $c->list->[0]->[1]; # abundance
```

## Description

This simple and lightweight decoder for the [PeakList](../structures/PeakList.md) structure does not save the location and type information for the individual list elements, nor does it provide element-level accessor methods. That makes it fast, at the cost of a slight reduction in convenience of access to the data.

It does not do file reads either, decoding the stream of floating-point numbers it receives as a constructor argument into an array of (*M/z*, abundance) pairs. Its full-featured equivalent, [Finnigan::Peaks](FinniganPeaks.md), does a file read for each peak, which makes it very slow.

It is good for use in production-level programs. In a situation that calls for detailed exploration (*e.g.*, a new file format), better use [Finnigan::Peaks](FinniganPeaks.md), which has an equivalent interface.

## Methods

- **new**
> The constructor method

- **count**
> Get the number of peaks in the list

- **list**
> Get the reference to an array containing the pairs of (*M/z*, abundance) values of each centroided peak.

## See Also

[PeakList](../structures/PeakList.md) (structure)

[Finnigan::Peaks](FinniganPeaks.md) (full-featured decoder object)
