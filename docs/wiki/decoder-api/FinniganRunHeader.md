---
title: FinniganRunHeader
original: https://code.google.com/p/unfinnigan/wiki/FinniganRunHeader
updated: 2011-04-04 05:45:02
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::RunHeader`

[source]

## SYNOPSIS

```
use Finnigan;

my $rh = Finnigan::RunHeader->decode(\*INPUT, $version);
my $first_scan_number = $rh->first_scan;
my $last_scan_number = $rh->last_scan;
my $scan_index_addr = $rh->sample_info->scan_index_addr;
```

## Description

Decodes [RunHeader](../structures/RunHeader.md), the static (fixed-size) structure containing data stream lengths and addresses, as well as some unidentified data. Every data stream in the file has its address stored in [RunHeader](../structures/RunHeader.md) or in its historical antecedent [SampleInfo](../structures/SampleInfo.md), which it now includes.

## Methods

- **decode($stream, $version)**
> The constructor method

- **sample_info**
> Get the [Finnigan::SampleInfo](FinniganSampleInfo.md) object

- **self_addr**
> Get own address

- **trailer_addr**
> Get the "trailer" address -- the pointer to the stream of [ScanEvent](../structures/ScanEvent.md) structures

- **params_addr**
> Get the pointer to the stream of ScanPrarameters structures

- **ntrailer**
> Get the length of the [ScanEvent](../structures/ScanEvent.md) stream

- **nparams**
> Get the length of the [ScanParameters](../structures/ScanParameters.md) stream

- **nsegs**
> Get the number of scan segments

## See Also

[RunHeader](../structures/RunHeader.md) (structure)

[ScanEvent](../structures/ScanEvent.md) (structure)

[ScanParameters](../structures/ScanParameters.md) (structure)

[Finnigan::SampleInfo](FinniganSampleInfo.md) (decoder object)
