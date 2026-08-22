---
title: FinniganASInfoPreamble
original: https://code.google.com/p/unfinnigan/wiki/FinniganASInfoPreamble
updated: 2012-05-26 16:17:10
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::ASInfoPreamble`

[source]

## SYNOPSIS

```
use Finnigan;

my $object = Finnigan::ASInfoPreamble->decode(\*INPUT);
$object->dump;
```

## Description

[ASInfoPreamble](../structures/ASInfoPreamble.md) is a fixed-length structure with some unknown data about the autosampler. It is a component of [ASInfo](../structures/ASInfo.md), which consists of this numeric descriptor and and a text string following it.

## Methods

- **decode($stream)**
> The constructor method

## See also

[ASInfo](../structures/ASInfo.md) (structure)
