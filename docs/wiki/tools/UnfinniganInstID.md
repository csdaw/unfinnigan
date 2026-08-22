---
title: UnfinniganInstID
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganInstID
updated: 2011-04-02 11:49:55
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-instrument

## SYNOPSIS

```
uf-instrument [options] <file>
```

### OPTIONS

***-help*** Print a brief help message and exit.

***-d`[`ump`]`*** dump the InstID structure showing file seek addresses

***-s`[`ize`]`*** print object size (requires ***-d***)

***-h`[`tml`]`*** format as html (requires ***-d***)

***-w`[`iki`]`*** format as a wiki table (requires ***-d***)

***-r`[`elative`]`*** show relative addersess in the dump (requires ***-d***)

***`<`file`>`*** input file

## DESCRIPTION

If called without options, **uf-instrument** prints all instrument ID information on one line.

For more detailed information about all instruments involved in the acquisition of the data, use **[uf-meth](UnfinniganMethodFile.md)**, the method file tool.

## SEE ALSO

[InstID](../structures/InstID.md) (structure)

[Finnigan::InstID](../decoder-api/FinniganInstID.md) (decoder object)

**[uf-meth](UnfinniganMethodFile.md)**, the method file tool

### EXAMPLES

- `uf-instrument sample.raw`

> (prints all IDS on one line)

- `uf-log -dswr sample.raw`

> (dumps the InstID structure in wiki format with size and using relative addresses)
