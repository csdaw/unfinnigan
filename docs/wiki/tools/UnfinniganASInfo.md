---
title: UnfinniganASInfo
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganASInfo
updated: 2012-05-26 16:19:38
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-asinfo

## SYNOPSIS

```
 uf-asinfo [options] <file>
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

Prints the table listing all fields in the structure with their seek addresses, sizes, names and values.

## SEE ALSO

[ASInfo](../structures/ASInfo.md) (structure)

[ASInfoPreamble](../structures/ASInfoPreamble.md) (structure)

[Finnigan::ASInfo](../decoder-api/FinniganASInfo.md) (decoder)

## EXAMPLES

`uf-asinfo sample.raw`

> (shows the location and size of the preamble and the text following it
> with absolute addresses)

`uf-asinfo --preamble --relative sample.raw`

> (dumps the contents of the preamble with relative addresses)
