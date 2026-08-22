---
title: UnfinniganScanParameters
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganScanParameters
updated: 2011-04-02 11:39:53
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-params

## SYNOPSIS

```
uf-params [options] <file>
```

### OPTIONS

***-help*** Print a brief help message and exit.

***-d`[`ump`]`*** dump the requested feature showing file seek addresses

***-a`[`ist`]`*** detailed dump of all field descriptors (requires: ***-d***)

***-s`[`ize`]`*** print record size (requires: ***-d***)

***-n`[`umber`]` `<n>`*** extract the log entry number ***n***

***-h`[`tml`]`*** format as html

***-w`[`iki`]`*** format as a wiki table

***-r`[`elative`]`*** show relative addersess in the dump (requires: ***-d***)

***`<`file`>`*** input file

## DESCRIPTION

**uf-params** can be used to examine the [ScanParameters](../structures/ScanParameters.md) records in a Finnigan raw file. These records contain a miscellany of data pertaining to a single scan: ion injection time, retention time, charge state and *M/z* of the precursor ion, *M/z* conversion coefficients, and other data.

## SEE ALSO

[ScanParameters](../structures/ScanParameters.md) (structure)

[Finnigan::ScanParameters](../decoder-api/FinniganScanParameters.md) (decoder object)

### EXAMPLES

- `uf-params sample.raw`

> (lists all [ScanParameters](../structures/ScanParameters.md) records in the tabular form: <record number, label, value>)

- `uf-params -n 5 sample.raw`

> (prints the parameters record for the fifth scan)

- `uf-params -dswr -n 5 sample.raw`

> (dumps the fifth [ScanParameters](../structures/ScanParameters.md) record in wiki format with total size and relative addresses)

- `uf-params -header sample.raw`

> (prints the contents of the stream header in the tabular form: <type, length, label>)

- `uf-params -header -dw sample.raw`

> (dumps the header in the compact wiki format, with a stringified
> [GenericDataDescriptor](../structures/GenericDataDescriptor.md) list)

- `uf-params -header -daw sample.raw`

> (dumps the header in the extended wiki format, showing the
> location of echa [GenericDataDescriptor](../structures/GenericDataDescriptor.md)'s element)
