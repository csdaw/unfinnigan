---
title: UnfinniganSeqRow
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganSeqRow
updated: 2011-03-22 05:14:15
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-seqrow

## SYNOPSIS

```
uf-seqrow [options] file
```

## OPTIONS

***--help*** Print a brief help message and exit.

***--man*** Print the manual page and exit.

***--dump*** Prints a table listing all header fields with their seek addresses, sizes, acess keys and values.

***--html*** Dump as html table.

***--wiki*** Dump as a wiki table.

***--size*** Show structure size in bytes.

***--injection*** Dump the contents of [InjectionData](../structures/InjectionData.md), instead of the parent object.

***--relative*** Show relative addresses of all itmes. The default is to show the absolute seek address.

## DESCRIPTION

`uf-seqrow` will display the contents of the [SeqRow](../structures/SeqRow.md) (Sequence Table Row) structure or its component, [InjectionData](../structures/InjectionData.md).

It will return an error message if its input is not a Finnigan raw file.

By default, it will dump the [SeqRow](../structures/SeqRow.md) object in a tabular format.

## EXAMPLES

```
uf-seqrow sample.raw
```

> (dumps the entire [SeqRow](../structures/SeqRow.md) structure with absolute addresses)

```
uf-seqrow -sri sample.raw
```

> (dumps the [InjectionData](../structures/InjectionData.md) substructure with relative addresses and prints its size)

## SEE ALSO

[SeqRow](../structures/SeqRow.md)
