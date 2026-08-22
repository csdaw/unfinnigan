---
title: ScanDataPacket
original: https://code.google.com/p/unfinnigan/wiki/ScanDataPacket
updated: 2011-03-31 16:43:49
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Purpose

This structure contains the data stream acquired during a single scan and/or its processed forms and ancillary data. The data can be raw time-domain signals, frequency spectra or converted *M/z* spectra.

Some data necessary for conversion (such as transform coefficients) reside in a separate stream (see [ScanEvent](ScanEvent.md)).

## Structure (variable size)

| size | quantity | substructure | function |
| --- | --- | --- | --- |
| *40* | 0 or 1 | [PacketHeader](PacketHeader.md) | Stores the layout indicator and sizes of the data streams acquired during one scan or derived from it |
| *2·n+1* | 0 or 1 | [PeakList](PeakList.md) | A list of peak centroids calculated from the profile data |
| *n* | 0 or 1 | *n* ⨯ PeakDescriptor | A list of peak descriptors (*index*, *flags*, *charge*) |
| *n + 1* | 0 or 1 | UnknownStream | A list of floating-point numbers sometimes truncated (or rounded) to the nearest integer |
| *3 ⨯ 9* | 0 or 1 | *9* ⨯ UnknownTriplet | Each triplet starts with an *M/z* value followed by two floating-point numbers |

Either the profile or the peak list may be absent. The profile may contain various types of data: time-domain signal, frequency-domain signal, or converted *M/z* spectrum.
