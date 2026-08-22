---
title: Error
original: https://code.google.com/p/unfinnigan/wiki/Error
updated: 2011-03-28 06:23:07
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Purpose

Link an error message to a scan via retention time.

## Structure

### Size: variable

| offset | size | type | key | value |
| --- | --- | --- | --- | --- |
| 0 | 4 | Float32 | `time` | `39.581974029541` |
| 4 | 126 | [PascalStringWin32](PascalStringWin32.md) | `message` | `Dynamic exclusion list is full. Mass 442.78 has been dropped.` |

## Decoding in Hachoir

```
class ErrorLogRecord(FieldSet):
    endian = LITTLE_ENDIAN

    def createFields(self):
        yield Float32(self, "time", "Retention time")
        yield PascalStringWin32(self, "message", "Error Message")
```

## Decoding in Perl

```
my $fields = [
              "time"     => ['f', 'Float32'],
              "message"  =>  ['varstr', 'PascalStringWin32'],
       ];

my $entry = Finnigan::Decoder->read($stream, $fields);
```

## Decoder Object

[Finnigan::Error](../decoder-api/FinniganError.md)
