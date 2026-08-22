---
title: UnfinniganIndex
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganIndex
updated: 2011-06-20 03:39:09
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-index

## SYNOPSIS

```
uf-index [options] <file>
```

### OPTIONS

***-help*** print a brief help message and exit.

***-a`[`ll`]`*** process all index entries, ignoring the range specified in [RunHeader](../structures/RunHeader.md)

***-n`[`umber`]` `<n>`*** extract the index entry number ***n***

***-range `<`from`>` .. `<`to`>`*** extract all entries with numbers between <`from`> and <`to`>

***-d`[`ump`]`*** dump all data in each entry

***-s`[`ize`]`*** print object size (requires: ***-d***)

***-h`[`tml`]`*** format as html

***-w`[`iki`]`*** format as a wiki table

***-r`[`elative`]`*** show relative addersess in the dump (requires: ***-d***)

***-f`[`ormat`]` <`type: bin|hex|ms`>*** format the unknown long using the binary or hexadecimal encoding, or attempt to extract the MS power. The MS power interpretation is probably incorrect and only seems to work by co-incidence.

***`<`file`>`*** input file

## DESCRIPTION

**uf-index** can be used to examine the [scan index stream](../structures/ScanIndexStream.md) in a Finnigan raw file. Scan index is a set of auxiliary structures ([ScanIndexEntry](../structures/ScanIndexEntry.md)) containing pointers to [ScanDataPacket](../structures/ScanDataPacket.md) structures and their sizes.

Without options, **uf-index** lists all entries in tabular format, one row per entry.

The only unknown element in the [ScanEvent](../structures/ScanEvent.md) structure can be interpreted in a number of ways; to aid in its interpretation, the ***-format*** option allows it to be printed in different formats when the structure is rendered in the tabular form. The default format is decimal.

## SEE ALSO

[ScanIndexStream](../structures/ScanIndexStream.md) (structure)

[ScanIndexEntry](../structures/ScanIndexEntry.md) (structure)

[RunHeader](../structures/RunHeader.md) (primary index structure)

[ScanDataPacket](../structures/ScanDataPacket.md) (main data structure)

[Finnigan::ScanIndexEntry](../decoder-api/FinniganScanIndexEntry.md) (decoder object)

### EXAMPLES

- `uf-index sample.raw`

> (prints all index entries in the file in the tabular form)

- `uf-index -range 1 .. 5 sample.raw`

> (prints the first five records)

- `uf-index -range 1 .. 5 -format bin sample.raw`

> (shows individual bits in the unknown 'scan type' word)

- `uf-index -rdsn 5 sample.raw`

> (dumps the fifth index entry with relative addresses and shows its size)
