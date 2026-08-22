---
title: FractionCollector
original: https://code.google.com/p/unfinnigan/wiki/FractionCollector
updated: 2010-03-18 09:44:11
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

This object is just a container for a pair of double-precision floating point numbers that define the M/z range of ions collected during a scan. It is found in [ScanEvent](ScanEvent.md) objects.

## Structure

### Static size: 16 bytes

| offset | size | type | key | example |
| --- | --- | --- | --- | --- |
| 0 | 8 | Float64 | low mz | 400 |
| 8 | 8 | Float64 | high mz | 2000 |
