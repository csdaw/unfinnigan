---
title: ScanEventTemplate
original: https://code.google.com/p/unfinnigan/wiki/ScanEventTemplate
updated: 2011-07-28 11:56:00
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Purpose

This is a template structure that apparently forms the core of each [ScanEvent](ScanEvent.md) structure corresponding to an individual scan. It is an elment of MSScanEvent hirerachy (that's the name used by Thermo), which models the grouping of scan events into segments.

The [ScanEvent](ScanEvent.md) structure in each dependent scan starts with `ScanEventTemplate`, and it augments it with information about precursor ions (where applicable), conversion coefficients, and some other data.

## Structure

### Size: 116 bytes

| offset | size | type | key | value | remark |
| --- | --- | --- | --- | --- | --- |
| 0 | 80 | [ScanEventPreamble](ScanEventPreamble.md) | `preamble` | `FTMS + p ESI d SIM ms` |  |
| 80 | 4 | UInt32 | `unknown long[1]` | `0` | *suspected controllerType == Controller_MS* |
| 84 | 4 | UInt32 | `unknown long[2]` | `1` | *suspected controllerNumber* |
| 88 | 16 | [FractionCollector](FractionCollector.md) | `fraction collector` | `[50.00-150.00]` |  |
| 104 | 4 | UInt32 | `unknown long[3]` | `0` |  |
| 108 | 4 | UInt32 | `unknown long[4]` | `0` |  |
| 112 | 4 | UInt32 | `unknown long[5]` | `0` |  |

## The unknowns

None of the unknown data varies from sample to sample in the data files I have examined, so it is fair to say that this structure defines the scan type (with all the relevant data stored in [ScanEventPreamble](ScanEventPreamble.md)) and the scan range (in [FractionCollector](FractionCollector.md))

## See also

[Scan event hierarchy](ScanEventHierarchy.md)

[ScanEvent](ScanEvent.md) (structure)

[ScanEventPreamble](ScanEventPreamble.md) (structure)

[FractionCollector](FractionCollector.md) (structure)

[Finnigan::ScanEventTemplate](../decoder-api/FinniganScanEventTemplate.md) (the decoder object for this structure)
