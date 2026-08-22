---
title: FinniganError
original: https://code.google.com/p/unfinnigan/wiki/FinniganError
updated: 2011-04-04 08:30:06
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::Error`

[source]

## SYNOPSIS

```
use Finnigan;

my $entry = Finnigan::Error->decode(\*INPUT);
say $entry->time;
say $entry->message;
```

## Description

[Error](../structures/Error.md) is a is a varibale-length structure containing timestamped error messages.

## Methods

- **decode($stream)**
> The constructor method

- **time**
> Get the entry's timestamp (retention time)

- **message**
> Get the text message
