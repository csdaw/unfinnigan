---
title: UnfinniganScanLight
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganScanLight
updated: 2011-07-28 04:35:12
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-scan-light

## SYNOPSIS

```
uf-scan-light [options] <file>
```

## OPTIONS

***-help*** Print a brief help message and exit.

***-l`[`ist`]`*** list the called peaks (centroids)

***-p`[`rofile`]`*** print the scan profile as a 2-column table

***-b`[`ookends`]` `<n>`*** add ***n*** empty bins on both sides of each profile peak

***-n`[`umber`]` `<n>`*** select scan number ***n***

***`<`file`>`*** input file

## DESCRIPTION

**uf-scan-light** can be used to list the scan data for a single scan. Unlike [uf-scan](UnfinniganScan.md), it is based on a lightweight version of scan data decoder, [Finnigan::Scan](../decoder-api/FinniganScan.md), which does not preserve the location and type data of decoded elements and therefore cannot generate detailed data dumps. But there is one thing **uf-scan-light** does that [uf-scan](UnfinniganScan.md) does not: it mimics the manner in which Thermo-derived tools assign bin values in profile mode and it can insert stretches of empty bins on both sides of each profile peak, in the same way as they do it. Setting the value of the ***-bookends*** option to **4** results in the same output as that of readw or msconvert.

Also, **uf-scan-light** does not output the raw profiles. It automatically converts frequency values to *M/z*.

The ***-profile*** option instructs **uf-scan-light** to print the profile data. The ***-list*** option lists the peaks.

Options ***-profile***, ***-list*** and ***plot*** are mutually exclusive.

Option ***-bookends*** adds the specified number of empty bins to each side of a profile chunk. If the gap is smaller than 2x the number of bookend bins, it is completely zeroed out.

## SEE ALSO

**[Finnigan::PacketHeader](../decoder-api/FinniganPacketHeader.md)**

**[Finnigan::Scan](../decoder-api/FinniganScan.md)**

**[uf-scan](UnfinniganScan.md)**

**[uf-mzxml](UnfinniganMzXML.md)**

**[uf-mzml](UnfinniganMzML.md)**

### EXAMPLES

- `uf-scan-light -p -n 1 sample.raw`

> (prints converted profile bins in the 1st scan)

- `uf-scan-light -p -n 1 -b 4 sample.raw`

> (prints converted profile bins in the 1st scan, adding fourd-bin 'bookends' to make the output look like Thermo's)

- `uf-scan-light -l -n 1 sample.raw`

> (will print the list of centroids in the 1st scan; note that **uf-scan-light** does not calculate the peak centroids from the profile; it only lists the existing centroids if they are present)
