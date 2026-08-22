---
title: FinniganPacketHeader
original: https://code.google.com/p/unfinnigan/wiki/FinniganPacketHeader
updated: 2011-04-04 06:51:53
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::PacketHeader`

[source]

## SYNOPSIS

```
use Finnigan;

my $ph = Finnigan::PacketHeader->decode(\*INPUT);
say $ph->layout;
say $ph->profile_size;
```

## Description

Calling this decoder is a pre-requisite to reading any scan data. It reads the data packet layout indicator and the sizes of the data streams included in the packet.

## Methods

- **decode($stream)**
> The constructor method

- **layout**
> Get the layout indicator. Two values have been sighted so far: 0 and 128

- **profile_size**
> Get the profile size in 4-byte words

- **peak_list_size**
> Get the peak list size in 4-byte words

- **low_mz**

> Get the low end of the *M/z* range

- **high_mz**

> Get the high end of the *M/z* range

## See Also

[PacketHeader](../structures/PacketHeader.md) (structure)

[ScanDataPacket](../structures/ScanDataPacket.md) (structure)
