---
title: FinniganGenericDataHeader
original: https://code.google.com/p/unfinnigan/wiki/FinniganGenericDataHeader
updated: 2011-04-11 03:04:31
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::GenericDataHeader`

[source]

## SYNOPSIS

```
use Finnigan;

my $h = Finnigan::GenericDataHeader->decode(\*INPUT);
say $h->n;
say $h->dump;
```

## Description

[GenericDataHeader](../structures/GenericDataHeader.md) drives the decoding of a [GenericRecord](../structures/GenericRecord.md). It stores a list of [GenericDataDescriptor](../structures/GenericDataDescriptor.md) objects, each describing a field in the record.

## Methods

- **decode($stream)**
> The constructor method

- **n**
> Get the number of fields in each record

- **fields**
> Get the list of [Finnigan::GenericDataDescriptor](FinniganGenericDataDescriptor.md) objects. Each descriptor object corresponds to a field in the [GenericRecord](../structures/GenericRecord.md) structure to be decoded with this header.

- **labels**
> Get the list of descriptor labels in the order they occur in the header

- **field_templates**
> Get the list of unpack templates for the entire record in the form that can be passed to [Finnigan::Decoder](FinniganDecoder.md).

- **ordered_field_templates**
> Get the list of unpack templates whose keys are tagged with ordinal numbers to disambiguate possible duplicate keys and to preserve the order of fields. This is necessary for decoding the [InstrumentLogRecord](../structures/InstrumentLogRecord.md) structures.

## See Also

[GenericData](../structures/GenericData.md) (the explanation of the term)

[GenericRecord](../structures/GenericRecord.md) (structure)

[GenericDataDescriptor](../structures/GenericDataDescriptor.md) (structure)

[Finnigan::GenericDataDescriptor](FinniganGenericDataDescriptor.md) (decoder object)
