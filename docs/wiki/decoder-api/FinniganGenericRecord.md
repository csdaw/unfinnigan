---
title: FinniganGenericRecord
original: https://code.google.com/p/unfinnigan/wiki/FinniganGenericRecord
updated: 2011-04-04 07:50:08
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::GenericRecord`

[source]

## SYNOPSIS

```
use Finnigan;

my $record = Finnigan::GenericRecord->decode(\*INPUT, $header->field_templates);
my $record = Finnigan::GenericRecord->decode(\*INPUT, $header->ordered_field_templates);
```

## Description

`Finnigan::GenericRecord` is a pass-through decorder that only passes the field definitions it obtains from the header ([Finnigan::GenericDataHeader](FinniganGenericDataHeader.md)) to [Finnigan::Decoder](FinniganDecoder.md).

Because Thermo's [GenericRecord](../structures/GenericRecord.md) objects are odered and may have "virtual" gaps and section titles in them, the [Finnigan::Decoder](FinniganDecoder.md)'s method of stashing the decoded data into a hash is not directly applicable. A [GenericRecord](../structures/GenericRecord.md) may have duplicate keys and the key order needs to be preserved. The **ordered_field_templates** method of [Finnigan::GenericDataHeader](FinniganGenericDataHeader.md) can be used where the order of the fields is important. It prevents key collisions by inserting ordinal numbers into the keys.

## Methods

- **decode($stream)**
> The constructor method

## See Also

[Finnigan::GenericDataHeader](FinniganGenericDataHeader.md) (decoder object)

[Finnigan::GenericDataDescriptor](FinniganGenericDataDescriptor.md) (decoder object)

[GenericRecord](../structures/GenericRecord.md) (structure)

[GenericDataHeader](../structures/GenericDataHeader.md) (structure)

[GenericDataDescriptor](../structures/GenericDataDescriptor.md) (structure)
