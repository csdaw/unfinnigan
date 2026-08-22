---
title: FinniganFileHeader
original: https://code.google.com/p/unfinnigan/wiki/FinniganFileHeader
updated: 2011-04-04 08:31:36
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::FileHeader`

[source]

## SYNOPSIS

```
use Finnigan;

my $header = Finnigan::FileHeader->decode(\*INPUT);
say "$header";
```

## Description

`Finnigan::FileHeader` decodes the fixed-length [FileHeader](../structures/FileHeader.md) structure at the start of a Finnigan file containing the file version number.

## Methods

- **decode($stream)**
> The constructor method

- **version**
> Get the file version

- **audit_start**
> Get the start [AuditTag](FinniganAuditTag.md) object

- **audit_end**
> Get the end [AuditTag](FinniganAuditTag.md) object

- **tag**
> Get the header tag

- **stringify**
> Create a short string representation of the header data

## See Also

[FileHeader](../structures/FileHeader.md) (structure)
