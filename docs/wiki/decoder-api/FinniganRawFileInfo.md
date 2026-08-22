---
title: FinniganRawFileInfo
original: https://code.google.com/p/unfinnigan/wiki/FinniganRawFileInfo
updated: 2011-04-02 09:47:44
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::RawFileInfo`

[source]

## SYNOPSIS

```
use Finnigan;

my $file_info = Finnigan::RawFileInfo->decode(\*INPUT);
say $file_info->preamble->run_header_addr;
say $file_info->preamble->data_addr;
$file_info->dump;
```

## Description

This variable-size structure consists of [RawFileInfoPreamble](../structures/RawFileInfoPreamble.md) followed by six text strings. The first five strings contain the headings for the user-defined labels stored in [SeqRow](../structures/SeqRow.md). The sixth string is probably used to store the sample ID.

The older versions of [RawFileInfoPreamble](../structures/RawFileInfoPreamble.md) contained an unpacked rpresentation of the file creation date in the UTC time zone.

The modern versions of the preamble also contain the pointer to [ScanData](../structures/ScanData.md)? and the pointer to [RunHeader](../structures/RunHeader.md), which in turn stores pointers to all other data streams in the file.

There are other data elements in the modern preamble, whose meaning is unkonwn.

## Methods

- **decode**
> The constructor method

- **preamble**
> Get the [Finnigan::RawFileInfoPreamble](FinniganRawFileInfoPreamble.md) object

- **stringify**
> Make a concise string representation of the structure

## See also

[RawFileInfo](../structures/RawFileInfo.md) (structure)

[RawFileInfoPreamble](../structures/RawFileInfoPreamble.md) (structure)

[Finnigan::RawFileInfoPreamble](FinniganRawFileInfoPreamble.md) (decoder object)
