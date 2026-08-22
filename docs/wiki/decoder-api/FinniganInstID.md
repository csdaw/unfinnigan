---
title: FinniganInstID
original: https://code.google.com/p/unfinnigan/wiki/FinniganInstID
updated: 2011-04-04 08:58:31
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::InstID`

[source]

## SYNOPSIS

```
use Finnigan;

my $inst = Finnigan::InstID->decode(\*INPUT);
say $inst->model;
say $inst->serial_number;
say $inst->software_version;
$inst->dump;
```

## Description

Decodes the static (fixed-size) structure containing several instrument identifiers and some unknown data.

## Methods

- **decode($stream)**
> The constructor method

- **model**
> Get the first copy of the `model` attribute (there always seem to be two of them)

- **serial_number**
> Get the instrument's serial number

- **software_version**
> Get the version of software that created the data file

- **stringify**
> Concatenate all IDs in a single line of text

## See Also

[InstID](../structures/InstID.md) (structure)
