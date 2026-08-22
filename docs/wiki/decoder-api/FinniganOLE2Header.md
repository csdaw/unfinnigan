---
title: FinniganOLE2Header
original: https://code.google.com/p/unfinnigan/wiki/FinniganOLE2Header
updated: 2011-03-29 13:50:53
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# Finnigan::OLE2Header

[source]

## SYNOPSIS

```
use Finnigan;
my $header = Finnigan::OLE2Header->decode(\*INPUT);
say "$header";
```

## Description

This is an auxiliary decoder used by [Finnigan::OLE2File](FinniganOLE2File.md); it is of no use on its own.

The OLE2 header is the first the first object to be decoded on the way to parsing the embedded filesystem. It contains the key parameters that determine the shape of the filesystem.

## Methods

- **decode($stream)**
> The constructor method

- **stringify**
> Get a short text description of the data, e.g.,
>
> ```
> Version 3.62; block(s) in FAT chain: 1; in mini-FAT chain: 1; in DIF chain: 0
> ```

## See Also

[Finnigan::OLE2File](FinniganOLE2File.md) (decoder object)
