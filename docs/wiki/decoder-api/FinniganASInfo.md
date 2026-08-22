---
title: FinniganASInfo
original: https://code.google.com/p/unfinnigan/wiki/FinniganASInfo
updated: 2012-05-26 16:17:10
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::ASInfo`

[source]

## SYNOPSIS

```
use Finnigan;

my $cas_info = Finnigan::ASInfo->decode(\*INPUT);
$cas_info->dump;
```

## Description

[ASInfo](../structures/ASInfo.md) is a structure with uncertain purpose that contains a binary preamble with autosampler co-ordinates ([ASInfoPreamble](../structures/ASInfoPreamble.md)), followed by a text string. The text string is apparently a comment; in one instance where it was non-null, it contained this text:

` 384 Well Plate`

## Methods

- **decode($stream)**
> The constructor method

- **preamble**
> Get the [Finnigan::ASInfoPreamble](FinniganASInfoPreamble.md) object

## See also

[ASInfo](../structures/ASInfo.md) (structure)

[ASInfoPreamble](../structures/ASInfoPreamble.md) (structure)
