---
title: FinniganScanProfile
original: https://code.google.com/p/unfinnigan/wiki/FinniganScanProfile
updated: 2011-04-04 11:34:26
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::Scan::Profile`

[source]

## SYNOPSIS

```
use Finnigan;

my $scan = Finnigan::Scan->decode(\*INPUT);
my $profile = $scan->profile;
$profile->set_converter( $converter ); # from ScanEvent
my $bins = $profile->bins;
my ($mz, $abundance) = @{$bins->[0]} # data in the first bin
```

## Description

`Finningan::Scan::Profile` is a lightweight decoder for the [Profile](../structures/Profile.md) structure. It does not save the location and type information for the elements it decodes, nor does it provide element-level accessor methods. That makes it fast, at the cost of a slight reduction in convenience of access to the data.

It does not do file reads either, decoding part of the stream of profile chunks it receives as a constructor argument from the caller. Its full-featured equivalent, [Finnigan::Profile](FinniganProfile.md), does a file read for every data element down to a single integer of floating-point number, which makes it very slow.

`Finnigan::Scan::Profile` is good for use in production-level programs that need extensive debugging. In a situation that calls for detailed exploration (*e.g.*, a new file format), better use [Finnigan::Peaks](FinniganPeaks.md), which has an equivalent interface.

Every scan done in the *profile mode* has a profile, which is either a time-domain signal or a frequency spectrum accumulated in histogram-like bins.

A profile can be either raw or filtered. Filtered profiles are sparse; they consist of separate data chunks. Each chunk consists of a contiguous range of bins containing the above-threshold signal. The bins whose values fall below a cerain threshold are simply discarded, leaving gaps in the profile -- the reason for the [ProfileChunk](../structures/ProfileChunk.md) structure to exist.

One special case is raw profile, which preserves all data. Since there are no gaps in a raw profile, it is represented by a single chunk covering the entire range of bins, so the same container structure is suitable for complete profiles, as well as for sparse ones.

The bins store the signal intensity, and the bin co-ordinates are typically the frequencies of Fourier-transformed signal. Since the bins are equally spaced in the frequency domain, only the first bin frequency is stored in each profile header. The bin width is common for all bins and it is also stored in the same header. With these data, it is possible to calculate the bin values based on the bin indices.

The programs reading these data must convert the frequencies into the M/z values using the conversion function specific to the type of analyser used to acquire the signal. The calibrated coefficients for this convesion function are stored in the [ScanEvent](../structures/ScanEvent.md) structure (one instance of this structure exists for every scan).

The **bins** method of **Finnigan::Scan::Profile** returns the converted bins, optionally filling the gaps with zeroes.

## Methods

- **new($buffer, $layout)**
> The constructor method

- **nchunks**
> Get the number of chunks in the profile

- **set_converter($func_ref)**
> Set the converter function (*f* → *M/z*)

- **set_inverse_converter($func_ref)**
> Set the inverse converter function (*M/z* → *f*)

- **bins**
> Get the reference to an array of bin values. Each array element contains an (*M/z*, abundance) pair. This method calls the converter set by the **set_converter** method.

- **find_peak_intensity($query_mz)**
> Get the nearest peak in the profile for a given query value. The search will fail if nothing is found within 0.025 kHz of the target value (the parameter set internally as `$max_dist`). This method supports the search for precursor intensity in **uf-mzxml**.

## See Also

[Profile](../structures/Profile.md) (structure)

[ProfileChunk](../structures/ProfileChunk.md) (structure)

[Finnigan::Scan::ProfileChunk](FinniganScanProfileChunk.md) (lightweight decoder)

[Finnigan::PacketHeader](FinniganPacketHeader.md) (decoder object)

[Finnigan::Profile](FinniganProfile.md) (full-featured decoder)

[Finnigan::Scan](FinniganScan.md) (lightweight decoder)

[ScanEvent](../structures/ScanEvent.md) (structure containing conversion coefficients)

[Finnigan::ScanEvent](FinniganScanEvent.md) (decoder object)
