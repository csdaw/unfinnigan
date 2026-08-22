---
title: FinniganScanEventTemplate
original: https://code.google.com/p/unfinnigan/wiki/FinniganScanEventTemplate
updated: 2011-07-31 08:21:54
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::ScanEventTemplate`

[source]

## SYNOPSIS

```
use Finnigan;

my $e = Finnigan::ScanEventTemplate->decode(\*INPUT, $version);
say $e->size;
say $e->dump;
say join(" ", $e->preamble->list(decode => 'yes'));
say $e->preamble->analyzer(decode => 'yes');
$e->fraction_collector->dump;
```

## Description

This is a template structure that apparently forms the core of each [ScanEvent](../structures/ScanEvent.md) structure corresponding to an individual scan. It is an elment of *MSScanEvent* hirerachy (that's the name used by Thermo), which models the grouping of scan events into segments.

## Methods

- **decode($stream, $version)**
> The constructor method

- **preamble**
> Get the [Finnigan::ScanEventPreamble](FinniganScanEventPreamble.md) object

- **controllerType**
> Get the virtual controller type for this event (a guess; data not verified)

- **controllerNumber**
> Get the virtual controller number for this event (a guess; data not verified)

- **fraction_collector**
> Get the [Finnigan::FractionCollector](FinniganFractionCollector.md) object

- **stringify**
> Make a short text representation of the object

## See Also

[ScanEventTemplate](../structures/ScanEventTemplate.md) (structure)

[ScanEvent](../structures/ScanEvent.md) (structure)

[ScanEventPreamble](../structures/ScanEventPreamble.md) (structure)

[Finnigan::ScanEventPreamble](FinniganScanEventPreamble.md) (decoder object)

[FractionCollector](../structures/FractionCollector.md) (structure)

[Finnigan::FractionCollector](FinniganFractionCollector.md) (decoder object)
