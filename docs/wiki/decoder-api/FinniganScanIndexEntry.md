---
title: FinniganScanIndexEntry
original: https://code.google.com/p/unfinnigan/wiki/FinniganScanIndexEntry
updated: 2011-04-04 05:10:07
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::ScanIndexEntry`

[source]

## SYNOPSIS

```
use Finnigan;

my $entry = Finnigan::ScanIndexEntry->decode(\*INPUT);
say $entry->offset; # returns an offset from the start of scan data stream 
say $entry->data_size;
$entry->dump;
```

## Description

This decoder reads [ScanIndexEntry](../structures/ScanIndexEntry.md), the static (fixed-size) structure containing the pointer to a scan, the scan's data size and some auxiliary information about the scan.

Scan index elements seem to form a linked list. Each [ScanIndexEntry](../structures/ScanIndexEntry.md) contains the index of the next entry.

Although in all observed instances the scans were sequential and their indices could be ignored, it may not always be the case.

## Methods

- **decode($stream)**
> The constructor method

- **offset**
> Get the address of the corresponding [ScanDataPacket](../structures/ScanDataPacket.md) relative to the start of the data stream

- **index**
> Get this element's index (*a valid assumption if the scan data indices start at 0, otherwise this is the previous element's index*)

- **next**
> Get the next element's index(*a valid assumption if the scan data indices start at 0, otherwise this is the current element's index*)

- **scan_event**
> Get the index of this element's [ScanEventTemplate](../structures/ScanEventTemplate.md) in the current scan segment

- **scan_segment**
> Get the index of this element's scan segment in [Scan Event Hierarchy](../structures/ScanEventHierarchy.md)

- **data_size**
> Get the size of the [ScanDataPacket](../structures/ScanDataPacket.md) this index element is pointing to

- **start_time**
> Get the current scan's start time

- **total_current**
> Get the scan's total current (a rough indicator of how many ions were scanned)

- **base_intensity**
> Get the intensity of the most abundant ion

- **base_mz**
> Get the *M/z* value of the most abundant ion

- **low_mz**
> Get the low end of the scan range

- **high_mz**
> Get the high end of the scan range

- **unknown**
> Get the only unknown UInt32 stored in the index entry. Its value (or some bits in it) seem to correspond to the type of scan, but its interpretation is uncertain.

**Note**: The "current/next" theory of the two ordinal numbers in this structure may be totally wrong. It may just be that one of these numbers is the 0-base index (0 .. *n* -1), and the other is 1-based: (1 .. *n*). It is suspicious that in the last entry in every stream, the "next" value is not null, it simply *n*.

## See Also

[ScanDataPacket](../structures/ScanDataPacket.md) (structure)

[ScanEventHierarchy](../structures/ScanEventHierarchy.md) (structure)
