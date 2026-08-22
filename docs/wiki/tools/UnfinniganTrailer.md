---
title: UnfinniganTrailer
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganTrailer
updated: 2011-07-26 04:42:56
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-trailer

## SYNOPSIS

```
uf-trailer [options] <file>
```

### OPTIONS

***-help*** print a brief help message and exit.

***-a`[`ll`]`*** process all scan event entries, ignoring the range specified in [RunHeader](../structures/RunHeader.md)

***-n`[`umber`]` `<n>`*** extract [ScanEvent](../structures/ScanEvent.md) number ***n***

***-range `<`from`>` .. `<`to`>`*** extract [ScanEvent](../structures/ScanEvent.md) objects with numbers between <`from`> and <`to`>

***-d`[`ump`]`*** dump all data in each [ScanEvent](../structures/ScanEvent.md)

***-h`[`tml`]`*** format as html

***-w`[`iki`]`*** format as a wiki table

***-r`[`elative`]`*** show relative addersess in the dump (requires: ***-d***)

***-p`[`reamble`]`*** include the translated listing of [ScanEventPreamble](../structures/ScanEventPreamble.md)

***`<`file`>`*** input file

## DESCRIPTION

**uf-trailer** can be used to list or dump the [ScanEvent](../structures/ScanEvent.md) records in a Finnigan raw file. These records are stored in a stream Thermo calls a "trailer", which occurs near the end of the file. Now, the "trailer" containing scan event descriptions is not the only stream trailing the data; apparently, new ones were added as the format evolved, but the name stuck. The code in Thermo libraries refers to this stream as "TrailerScanEvent".

## SEE ALSO

ScanEventsStream (structure)

[ScanEvent](../structures/ScanEvent.md) (structure)

[RunHeader](../structures/RunHeader.md) (primary index structure)

[Finnigan::ScanEvent](../decoder-api/FinniganScanEvent.md) (decoder object)

### EXAMPLES

- `uf-trailer sample.raw`

> (lists all scan events in the file using Thermo's short-hand notation known as "filter line")

- `uf-index -range 1..5 sample.raw`

> (lists the first five records)

- `uf-index -range 1..5 -format bin sample.raw`

> (shows individual bits in the unknown 'scan type' word)

- `uf-index -drn 5 sample.raw`

> (dumps the fifth [ScanEvent](../structures/ScanEvent.md) with relative addresses)
