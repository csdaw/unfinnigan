---
title: FinniganScan
original: https://code.google.com/p/unfinnigan/wiki/FinniganScan
updated: 2011-04-04 11:46:04
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::Scan`

[source]

## SYNOPSIS

```
use Finnigan;

my $scan = Finnigan::Scan->decode(\*INPUT);
say $scan->header->profile_size;
say $scan->header->peak_list_size;

my $profile = $scan->profile;
$profile->set_converter( $converter ); # from ScanEvent
my $bins = $profile->bins;
say $bins->[0]->[0]; # M/z of the first profile bin
say $bins->[0]->[1]; # abundance

my $c = $scan->centroids
say $c->count;
say $c->list->[0]->[0]; # the first centroid M/z
say $c->list->[0]->[1]; # abundance
```

## Description

This decoder reads the entire [ScanDataPacket](../structures/ScanDataPacket.md), discarding the location and type meta-data. It is a more efficient alternative to the full-featured combination decoders using the [Finnigan::Profile](FinniganProfile.md), [Finnigan::Peaks](FinniganPeaks.md) and [Finnigan::Peak](FinniganPeak.md) modules.

## Methods

- **decode**
> The constructor method

- **header**
> Get the [Finnigan::PacketHeader](FinniganPacketHeader.md) object. It is the only full-featured decoder object used in this module; since it occurs only once in each scan, there is no significant performance loss.

- **profile**
> Get the [Finingan::Scan::Profile](FinniganScanProfile.md) object containing the profile, if it exists

- **centroids**
> Get the [Finnigan::Scan::CentroidList](FinniganScanCentroidList.md) object containing the peak centroid list, if it exists

## See Also

[ScanDataPacket](../structures/ScanDataPacket.md) (structure)

[PacketHeader](../structures/PacketHeader.md) (structure)

[Profile](../structures/Profile.md) (structure)

[PeakList](../structures/PeakList.md) (structure)

[Finnigan::PacketHeader](FinniganPacketHeader.md) (decoder object)

[Finnigan::Scan::Profile](FinniganScanProfile.md) (lightweight decoder object)

[Finnigan::Scan::CentroidList](FinniganScanCentroidList.md) (lightweight decoder object)
