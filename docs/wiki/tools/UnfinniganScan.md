---
title: UnfinniganScan
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganScan
updated: 2011-08-06 03:57:24
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-scan

## SYNOPSIS

```
uf-scan [options] <file>
```

## OPTIONS

***-help*** Print a brief help message and exit.

***-d`[`ump`]`*** dump the scan header or the header and the profile (if the ***-profile*** option is supplied)

***-e`[`xtract`]`*** extract the entire scan data as a binary chunk

***-l`[`ist`]`*** list the called peaks

***-p`[`rofile`]`*** print the scan profile as a 2-column table

***-plot*** plot the profile (along with the called peaks, if available) required

***-v*** convert *f → M/z* `[`requires ***-profile***`]`

***-z*** fill the gaps with empty bins `[`requires ***-profile***`]`

***-n`[`umber`]` `<n>`*** select scan number ***n***

***-mz `<`low`>` .. `<`high`>`*** select a range of *M/z* values to plot `[`requires ***-plot***`]`

***`<`file`>`*** input file

## DESCRIPTION

**uf-scan** can be used to list or plot the scan data in a single scan. The ***-profile*** option instructs ***uf-scan*** to print the profile data, the ***-list*** option lists the peaks, and the ***-plot*** option writes an R script to plot the profile overlaid by peak centroids, if both kinds of data are present in the raw file, or just the profile if the centroids are not present.

Options ***-profile***, ***-list*** and ***plot*** are mutually exclusive.

To convert the raw scan data into the *M/z* values, use the ***-v*** option.

Option ***-z*** fills the gaps between the profile peaks with zeroes, to create a continuous table.

## SEE ALSO

**[uf-mzxml](UnfinniganMzXML.md)**

### EXAMPLES

- `uf-scan -p -n 1 sample.raw`

> (prints all raw profile bins in the 1st scan)

- `uf-scan -ep -n 1 sample.raw`

> (extracts the entire scan profile in the binary form)

- `uf-scan -pv -n 1 sample.raw`

> (same as above, except the bin values are converted into *M/z*)

- `uf-scan -pvz -n 1 sample.raw`

> (same as above, but in addition, all empty bins are wirtten out as well)

- `uf-scan -l -n 1 sample.raw`

> (will print the list of centroids in the 1st scan; note that **uf-scan** does not calculate the peak centroids from the profile; it only lists the existing centroids if they are present)

- `uf-scan -plot -n 1 -mz 445.0 .. 445.2 sample.raw | R --vanilla --slave > plot.eps`

> This command will call R to plot the profile in the given range of *M/z* values. If called peaks are present, they will be shown as dots on the graph.

- `uf-scan -d -p -n 18588 sample.raw | grep fudge | cut -f 5`

> See the amount of correction applied to each bin in scan 18588.
