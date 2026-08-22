---
title: UnfinniganTuneFile
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganTuneFile
updated: 2011-04-03 04:48:29
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-tune

## SYNOPSIS

```
uf-tune [options] <file>
```

### OPTIONS

***-help*** Print a brief help message and exit.

***-d`[`ump`]`*** dump the requested feature showing file seek addresses

***-a`[`ist`]`*** detailed dump of all field descriptors (requires: ***-d***)

***-s`[`ize`]`*** print object size (requires: ***-d***)

***-h`[`tml`]`*** format as html

***-w`[`iki`]`*** format as a wiki table

***-r`[`elative`]`*** show relative addersess in the dump (requires: ***-d***)

***`<`file`>`*** input file

## DESCRIPTION

**uf-tune** can be used to examine the embedded tune file, either by listing its entries (which were intended for human consumption), or by dumping the details of its encoding.

## SEE ALSO

[TuneFile](../structures/TuneFile.md) (structure)

[GenericRecord](../structures/GenericRecord.md) (structure)

[Finnigan::GenericRecord](../decoder-api/FinniganGenericRecord.md) (decoder object)

### EXAMPLES

- `uf-tune sample.raw`

> (lists the tune file in the tabular form: <label, value>)

- `uf-tune -d sample.raw`

> (dumps the tune file with absolute addresses)

- `uf-tune -header sample.raw`

> (prints the contents of the tune file header in the tabular form: <type, length, label>)

- `uf-tune -header -dw sample.raw`

> (dumps the header in the compact wiki format, with a stringified
> [GenericDataDescriptor](../structures/GenericDataDescriptor.md) list)

- `uf-tune -header -daw sample.raw`

> (dumps the header in the extended wiki format, showing the
> location of echa [GenericDataDescriptor](../structures/GenericDataDescriptor.md)'s element)
