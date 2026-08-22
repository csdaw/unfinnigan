---
title: RawFileInfo
original: https://code.google.com/p/unfinnigan/wiki/RawFileInfo
updated: 2010-03-13 17:24:04
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

This variable-size structure consists of [RawFileInfoPreamble](RawFileInfoPreamble.md) followed by six text strings. The first five strings contain the headings for the user-defined labels stored in [SeqRow](SeqRow.md). The sixth string is probably used to store the name of the sample.

The older versions of [RawFileInfoPreamble](RawFileInfoPreamble.md) contained an unpacked rpresentation of the file creation date in the UTC time zone.

The modern versions of the preamble also contain the pointer to [ScanData](ScanData.md) and the pointer to [RunHeader](RunHeader.md), which in turn stores pointers to all other data streams in the file.

There are other data elements in the modern preamble, whose meaning is unkonwn.

## Structure

| offset | size | type | key | examples |
| --- | --- | --- | --- | --- |
| 0 | 804 | [RawFileInfoPreamble](RawFileInfoPreamble.md) | `preamble` | ... |
| 804 | 12 | [PascalStringWin32](PascalStringWin32.md) | `label heading[1]` | `Date` |
| 816 | 12 | [PascalStringWin32](PascalStringWin32.md) | `label heading[2]` | `Trap` |
| 828 | 16 | [PascalStringWin32](PascalStringWin32.md) | `label heading[3]` | `Column` |
| 844 | 24 | [PascalStringWin32](PascalStringWin32.md) | `label heading[4]` | `Mob. Phase` |
| 868 | 14 | [PascalStringWin32](PascalStringWin32.md) | `label heading[5]` | `Phone` |
| 882 | 20 | [PascalStringWin32](PascalStringWin32.md) | `unknown text` | `R0182002` |

## The unknowns

The last text tag appears to contain the sample name, but I have not received a confirmation yet, and the Thermo tools do not display it.

Other examples of `unknown text`:

```
PCMANN75
DB23HPD1
LTQ-FT-105
```
