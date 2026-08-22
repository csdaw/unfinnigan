---
title: UnfinniganRunHeader
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganRunHeader
updated: 2011-04-02 10:24:03
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-runheader

## SYNOPSIS

```
 uf-runheader [options] <file>
```

## OPTIONS

***--help*** print a brief help message and exit.

***--man*** print the manual page and exit.

***--html*** format as HTML

***--wiki*** format as a wiki table

***--size*** tell object size

***--sample_info*** dump the contents of the [SampleInfo](../structures/SampleInfo.md) substructure

***--relative*** Show relative addresses of all elements. The default is to show the absolute seek address.

## DESCRIPTION

Displays the contents of the [RunHeader](../structures/RunHeader.md) structure, or its component [SampleInfo](../structures/SampleInfo.md).

If invoked with no arguments, **uf-runheader** prints a summary of the object's data on a single line.

## SEE ALSO

[RunHeader](../structures/RunHeader.md) (structure)

[SampleInfo](../structures/SampleInfo.md) (structure)

[Finnigan::RunHeader](../decoder-api/FinniganRunHeader.md) (decoder)

## EXAMPLES

`uf-runheader sample.raw`

> (prints a single line listing a few important numbres in [RunHeader](../structures/RunHeader.md))

`uf-runheader -d sample.raw`

> (dumps the entire [RunHeader](../structures/RunHeader.md) structure with absolute addresses)

`uf-header -isdrw sample.raw`

> (dumps the contents of the [SampleInfo](../structures/SampleInfo.md) structure in the wiki format with relative addresses and shows its size)
