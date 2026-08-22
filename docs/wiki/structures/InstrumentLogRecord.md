---
title: InstrumentLogRecord
original: https://code.google.com/p/unfinnigan/wiki/InstrumentLogRecord
updated: 2011-03-31 03:21:30
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Description

The instrument log records contain more than a hundred parameters, including operational data on the pumps, power supplies, ion optics and injectors -- everything that may be useful in the auditing of the instrument's performance.

Each record is timestamped with the current retention time of the sample (a 32-bit floating point number).

The content of the record (besides the timestamp) is designed to be decoded with the [GenericDataHeader](GenericDataHeader.md).

## Structure

### Size: fixed, varies with the file version
