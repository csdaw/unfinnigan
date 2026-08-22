---
title: FinniganScanEventPreamble
original: https://code.google.com/p/unfinnigan/wiki/FinniganScanEventPreamble
updated: 2011-04-04 05:21:42
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::ScanEventPreamble`

[source]

## SYNOPSIS

```
use Finnigan;

my $e = Finnigan::ScanEventPreamble->decode(\*INPUT, $version);
say join(" ", $p->list);
say join(" ", $p->list('decode'));
say p->analyzer;
say p->analyzer('decode');
```

## Description

[ScanEventPreamble](../structures/ScanEventPreamble.md) is a fixed-size (but version-dependent) structure. It is a byte array located at the head of each [ScanEvent](../structures/ScanEvent.md). It contains various boolean flags an enumerated types. For example, it's 41st byte contains the analyzer type in all versions:

```
%ANALYZER = (
  0 => "ITMS",
  1 => "TQMS",
  2 => "SQMS",
  3 => "TOFMS",
  4 => "FTMS",
  5 => "Sector",
  6 => "undefined"
);
```

The [ScanEventPreamble](../structures/ScanEventPreamble.md) decoder provides a number of accessors that interpret the enumerated and boolean values.

The meaning of some values in [ScanEventPreamble](../structures/ScanEventPreamble.md) remains unknown.

The structure seems to have grown historically: to the 41 bytes in v.57, 39 more were added in v.62, and 8 further bytes were added in v.63. That does not affect the decoder interface; those values it knows about have not changed, but the version number still has to be passed into it so it knows how many bytes to read.

## Methods

- **decode($stream, $version)**
> The constructor method

All of the following accessor methods will replace the byte value of the flag they access with a symbolic value representing that flag's meaning if given a truthy argument. The word 'decode' is a good one to use because it makes the code more readable, but any truthy value will work.

- **list(bool)**
> Returns an array containing all byte values of [ScanEventPreamble](../structures/ScanEventPreamble.md)

- **corona(bool)**
> Get the corona status (*0:off* or *1:on*).

- **detector(bool)**
> Get the detector flag (*0:valid* or *1:undefined*).

- **polarity(bool)**
> Get the polarity value (*0:negative*, *1:positive*, *2:undefined*)

- **scan_mode(bool)**
> Get the scan mode (*0:centroid*, *1:profile*, *2:undefined*)

- **ms_power(bool)**
> Get the MS power number (*0:undefined*, *1:MS1*, *2:MS2*, *3:MS3*, *4:MS4*, *5:MS5*, *6:MS6*, *7:MS7*, *8:MS8*)

- **scan_type(bool)**
> Get the scan type (*0:Full*, *1:Zoom*, *2:SIM*, *3:SRM*, *4:CRM*, *5:undefined*, *6:Q1*, *7:Q3*)

- **dependent(bool)**
> Get the dependent flag (0 for primary MS1 scans, 1 for dependent scan types)

- **ionization(bool)**
> Get the scan type (*0:EI,* 1:CI, *2:FABI,* 3:ESI, *4:APCI,* 5:NSI, *6:TSI*, *7:FDI*, *8:MALDI*, *9:GDI*, *10:undefined*)

- **wideband(bool)**
> Get the wideband flag (*0:off*, *1:on*, *2:undefined*).

- **analyzer(bool)**
> Get the scan type (*0:ITMS,* 1:TQMS, *2:SQMS,* 3:TOFMS, *4:FTMS,* 5:Sector, *6:undefined*)

- **stringify**

> Makes a short text representation of the set of flags (known as "filter line" to the users of Thermo software)

## See Also

[ScanEventTemplate](../structures/ScanEventTemplate.md) (structure)

[ScanEvent](../structures/ScanEvent.md) (structure)

[ScanEventPreamble](../structures/ScanEventPreamble.md) (structure)

[Finnigan::ScanEventTemplate](FinniganScanEventTemplate.md) (decoder object)

[Finnigan::ScanEvent](FinniganScanEvent.md) (decoder object)
