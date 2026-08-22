---
title: FinniganSampleInfo
original: https://code.google.com/p/unfinnigan/wiki/FinniganSampleInfo
updated: 2011-04-04 05:40:00
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::SampleInfo`

[source]

## SYNOPSIS

```
use Finnigan;

my $rh = Finnigan::RunHeader->decode(\*INPUT, $version);
my $si = $rh->sample_info; # calls Finnigan::SampleInfo->decode
say $si->first_scan;
say $si->last_scan;
say $si->tot_ion_current;
my $scan_index_addr = $si->scan_index_addr;
. . .
```

## Description

This decoder reads [SampleInfo](../structures/SampleInfo.md), a static (fixed-size) binary preamble to [RunHeader](../structures/RunHeader.md) containing data stream lengths and addresses, as well as some unidentified data. Four out of six data streams in the file have their addresses stored in [SampleInfo](../structures/SampleInfo.md). The other two, ScanHeader and [ScanEvent](../structures/ScanEvent.md) streams, are addressed through [RunHeader](../structures/RunHeader.md).

The [SampleInfo](../structures/SampleInfo.md) structure also a few numeric values describing the run (the fact that vaguely justifies its name).

## Methods

- **decode($stream)**
> The constructor method

- **first_scan**
> Get the first scan number

- **last_scan**
> Get the last scan number

- **inst_log_length**
> Get the number of instrument log records

- **max_ion_current**
> Get the pointer to the stream of ScanPrarameters structures

- **low_mz**
> Get the low end of the *M/z* range

- **high_mz**
> Get the high end of the *M/z* range

- **start_time**
> Get the start time (retention time in seconds)

- **end_time**
> Get the end time (retention time in seconds)

- **scan_index_addr**
> Get the address of the [ScanIndex](../structures/ScanIndex.md) stream

- **data_addr**
> Get the address of the [ScanDataPacket](../structures/ScanDataPacket.md) stream

- **inst_log_addr**
> Get the address of the instrument log records (of [GenericRecord](../structures/GenericRecord.md) type)

- **error_log_addr**
> Get the address of the [Error](../structures/Error.md) stream

## See Also

[RunHeader](../structures/RunHeader.md) (parent structure)

[ScanDataPacket](../structures/ScanDataPacket.md) (structure)

[ScanIndex](../structures/ScanIndex.md) (structure)

[ScanEvent](../structures/ScanEvent.md) (structure)

[ScanParameters](../structures/ScanParameters.md) (structure)

[Error](../structures/Error.md) (structure)
