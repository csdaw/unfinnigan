---
title: UnfinniganRawFileInfo
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganRawFileInfo
updated: 2012-05-26 16:12:50
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-rfi

## SYNOPSIS

```
 uf-rfi [options] <file>
```

## OPTIONS

***--help*** print a brief help message and exit.

***--man*** print the manual page and exit.

***--html*** format as HTML

***--wiki*** format as a wiki table

***--size*** tell object size

***--preamble*** Dump the contents of ASInfoPreamble

***--relative*** Show relative addresses of all elements. The default is to show the absolute seek address.

## DESCRIPTION

Displays the contents of the [RawFileInfo](../structures/RawFileInfo.md) structure, or its component [RawFileInfoPreamble](../structures/RawFileInfoPreamble.md).

If invoked with no arguments, **uf-rfi** prints a summary of the object's data on a single line.

## SEE ALSO

[RawFileInfo](../structures/RawFileInfo.md) (structure)

[RawFileInfoPreamble](../structures/RawFileInfoPreamble.md) (structure)

[RunHeader](../structures/RunHeader.md) (structure)

[Finnigan::RawFileInfo](../decoder-api/FinniganRawFileInfo.md) (decoder)

## EXAMPLES

`uf-rfi sample.raw`

> (prints a single line with file creation date, followed by the data and [RunHeader](../structures/RunHeader.md) addresses)

`uf-rfi -d sample.raw`

> (dumps the file's [RawFileInfo](../structures/RawFileInfo.md) structure with absolute addresses)

`uf-rfi -dpr sample.raw`

> (dumps the contents of [RawFileInfoPreamble](../structures/RawFileInfoPreamble.md) with relative addresses)
