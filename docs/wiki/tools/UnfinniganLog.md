---
title: UnfinniganLog
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganLog
updated: 2011-04-02 11:44:09
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-log

## SYNOPSIS

```
uf-log [options] <file>
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

**uf-log** can be used to examine the instrument log stream in a Finnigan raw file. The instrument log records typically contain more than a hundred parameters, including operational data on the pumps, power supplies, ion optics and injectors -- everything that may be useful in the auditing of the instrument's performance.

Each record is timestamped with the current retention time of the sample.

## SEE ALSO

[InstrumentLog](../structures/InstrumentLog.md) (structure)

[Finnigan::InstrumentLogRecord](../decoder-api/FinniganInstrumentLogRecord.md) (decoder object)

### EXAMPLES

- `uf-log sample.raw`

> (lists all log records in the tabular form: <record number, time, label, value>)

- `uf-log -n 5 sample.raw`

> (prints the fifth log record)

- `uf-log -dswr -n 5 sample.raw`

> (dumps the fifth log record in wiki format with total size and relative addresses)

- `uf-log -header sample.raw`

> (prints the contents of the stream header in the tabular form: <type, length, label>)

- `uf-log -header -dw sample.raw`

> (dumps the header in the compact wiki format, with a stringified
> [GenericDataDescriptor](../structures/GenericDataDescriptor.md) list)

- `uf-log -header -daw sample.raw`

> (dumps the header in the extended wiki format, showing the
> location of echa [GenericDataDescriptor](../structures/GenericDataDescriptor.md)'s element)
