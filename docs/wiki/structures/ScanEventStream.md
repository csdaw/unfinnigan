---
title: ScanEventStream
original: https://code.google.com/p/unfinnigan/wiki/ScanEventStream
updated: 2011-04-03 06:59:29
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Description

The stream contains fixed-size [ScanEvent](ScanEvent.md) structures loaded with the detailed information about scan type ([ScanEventPreamble](ScanEventPreamble.md)) and containing conversion coefficients for profile-type scans. The steam begins with the record counter, although it seems to be redundant, given that there are exactly the same number of [ScanEvent](ScanEvent.md) structures as there are [scan data packets](ScanDataPacket.md).

Thermo calls this stream a "trailer", apparently because it was added to the end of the file at one time in the history of the format. It no longer is that, as there are a couple more streams trailing it today.

## Structure

| Number of scan events (UInt32) |
| --- |
| [ScanEvent](ScanEvent.md) 1 |
| . . . |
| [ScanEvent](ScanEvent.md) *n* |

The pointer to the stream is contained in Run Header.

## See Also

[ScanEvent](ScanEvent.md) (structure)

[ScanEventPreamble](ScanEventPreamble.md) (structure)

[Scan Event Hierarchy](ScanEventHierarchy.md) (structure)

[ScanEventTemplate](ScanEventTemplate.md) (structure)

[RunHeader](RunHeader.md) (index structure)
