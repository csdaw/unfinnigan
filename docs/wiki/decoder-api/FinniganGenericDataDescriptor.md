---
title: FinniganGenericDataDescriptor
original: https://code.google.com/p/unfinnigan/wiki/FinniganGenericDataDescriptor
updated: 2011-04-04 08:47:05
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::GenericDataDescriptor`

[source]

## SYNOPSIS

```
use Finnigan;

my $d = Finnigan::GenericDataDescriptor->decode(\*INPUT);
say d->type;
say d->label;
```

## Description

[GenericDataDescriptor](../structures/GenericDataDescriptor.md) stores information on the type, size and name of a data element in a [GenericRecord](../structures/GenericRecord.md).

## Methods

- **decode($stream)**
> The constructor method

- **type**
> Get the element type (see Known data types)

- **length**
> Get the size of the element represented by this descriptor

- **label**
> Get the element's label. It is the same label that Thermo uses in their GUI, such as Xcalibur.

- **definition**
> Returns an appropriate decoder template based on descriptor type

- **stringify**
> Make a short string representation of the descriptor

## See Also

[GenericData](../structures/GenericData.md) (the explanation of the term)

[GenericRecord](../structures/GenericRecord.md) (structure)

[GenericDataHeader](../structures/GenericDataHeader.md) ([GenericDataDescriptor](../structures/GenericDataDescriptor.md)'s parent structure)

[Finnigan::GenericDataHeader](FinniganGenericDataHeader.md) (decoder object)
