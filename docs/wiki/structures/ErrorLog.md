---
title: ErrorLog
original: https://code.google.com/p/unfinnigan/wiki/ErrorLog
updated: 2011-04-02 15:35:20
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Description

The stream is a simple sequence of text messages timestamped with the current retention time of the sample.

## Structure

| Number of records (UInt32) |
| --- |
| Message 1 = {timestamp, [PascalStringWin32](PascalStringWin32.md)} |
| . . . |
| Message *n* = {timestamp, [PascalStringWin32](PascalStringWin32.md)} |

The pointer to the stream is contained in [SampleInfo](SampleInfo.md) (part of [RunHeader](RunHeader.md)).
