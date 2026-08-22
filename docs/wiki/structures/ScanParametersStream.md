---
title: ScanParametersStream
original: https://code.google.com/p/unfinnigan/wiki/ScanParametersStream
updated: 2011-04-02 15:57:11
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Purpose

I do not fully understand the purpose of this structure, but based on the labels it contains, it seems to have been intended for human consumption. It does not seem to contain any data that wouldn't be stored somewhere else in the file.

One possible exception is the **Charge State** attribute that I needed to fill the precursor data while writing out the XML for the MS2 scans in [UnfinniganMzXML](../tools/UnfinniganMzXML.md).

The content of [ScanParameters](ScanParameters.md) records is designed to be decoded with the [GenericDataHeader](GenericDataHeader.md) mechanism.

## Structure

| [GenericDataHeader](GenericDataHeader.md) (loaded with `ScanParmeters` descriptors) |
| --- |
| . . . |
| *a few intervening data structures and streams* |
| . . . |
| [ScanParameters](ScanParameters.md) record 1 |
| . . . |
| [ScanParameters](ScanParameters.md) record *n* |

Each [ScanParameters](ScanParameters.md) record corresponds to a [ScanDataPacket](ScanDataPacket.md), so there is no need for a separate object counter. The seek address of the first [ScanParameters](ScanParameters.md) record is contained in [RunHeader](RunHeader.md), but the stream's header (a [GenericDataHeader](GenericDataHeader.md)) can only be reached by starting from the [ErrorLog](ErrorLog.md) (the nearest object with a known seek address) and reading through it, then reading through. [Scan Event Hierarchy](ScanEventHierarchy.md).
