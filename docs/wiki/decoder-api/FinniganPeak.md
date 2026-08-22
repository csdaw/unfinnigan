---
title: FinniganPeak
original: https://code.google.com/p/unfinnigan/wiki/FinniganPeak
updated: 2011-04-04 06:39:19
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::Peak`

[source]

## SYNOPSIS

```
use Finnigan;

my $peak = Finnigan::Peak->decode(\*INPUT);
say $peak->mz;
say $peak->abundance;
say "$peak";
```

## Description

This decoder is useless in normal life. It is a full-featured decoder for the pair of floating-point numbers representing a the centroid *M/z* and intensity of a peak. The data it generates contain the seek addresses, sizes and types of both attributes. These features may be useful in the exploration of the file format and in writing new code, but not in production work.

In performance-sensitive applications, the more lightweight [Finnigan::Scan](FinniganScan.md) module should be used, which includes [Finnigan::Scan::CentroidList](FinniganScanCentroidList.md) and other related submodules. It does not store the seek addresses and object types, greatly reducing the overhead.

There is no equivalent object in [Finnigan::Scan::CentroidList](FinniganScanCentroidList.md); it simply uses a pair of scalars for the data, since the location data and decoding templates are discarded anyway, eliminating the need for an object.

## Methods

- **decode($stream)**
> The constructor method

- **mz**
> Get the *M/z* value, the first in the pair

- **abundance**
> Get the abundance value, the second in the pair

- **stringify**
> Get both attributes concatenated with a tab character. Used in the **list** method of the containing object, [Finnigan::Peaks](FinniganPeaks.md)

## See Also

[PeakList](../structures/PeakList.md) (structure)

[ScanDataPacket](../structures/ScanDataPacket.md) (structure)

[Finnigan::Scan](FinniganScan.md) (lightweight decoder object)

[Finnigan::Scan::CentroidList](FinniganScanCentroidList.md) (lightweight decoder object)
