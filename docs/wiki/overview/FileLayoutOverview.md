---
title: FileLayoutOverview
original: https://code.google.com/p/unfinnigan/wiki/FileLayoutOverview
updated: 2012-05-26 16:12:49
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

## Typical file layout

![](../images/structure-overview.png)

> [image source (svg)](../images/structure-overview.svg)

This diagram summarises the recent file layouts (versions 57 and up, and maybe some earlier ones as well, which I have not seen).

Most of the differences between file versions are concentrated at the stream record level. The overall structure remains the same.

Also, because I have not seen more than one file version recorded by a single instrument, it is possible that the differences are more related to the capabilities of instruments and recording modes selected in the software.

### Addressing data streams in the modern layouts

It looks like there is no way to reach the interesting data in these files without completely parsing the [FileHeader](../structures/FileHeader.md), [SeqRow](../structures/SeqRow.md) and [ASInfo](../structures/ASInfo.md) structures. [FileHeader](../structures/FileHeader.md) and [ASInfo](../structures/ASInfo.md) could be skipped because they are fixed-size structures (1356 and 28 bytes, respectively), but [SeqRow](../structures/SeqRow.md) is a variable-size structure, whose length can only be determined by reading it all.

After that, [RawFileInfo](../structures/RawFileInfo.md) can be read, which contains the first two pointers into the data. It points to [ScanData](../structures/ScanData.md) and to [RunHeader](../structures/RunHeader.md), which in turn contains pointers to all data streams in the file.

Note that in the earlier file formats, [RawFileInfo](../structures/RawFileInfo.md) was preceded by [RunHeader](../structures/RunHeader.md), so it did not contain the pointer to it (besause [RunHeader](../structures/RunHeader.md) could be reached at a static offset). Also, in the earlier formats, [RunHeader](../structures/RunHeader.md) did not contain stream pointers outside its [SampleInfo](../structures/SampleInfo.md) component (it contains two now).

To read the [InstrumentLog](../structures/InstrumentLog.md) stream, it is necessary to consume every object up to the start of of the log header, because there is no direct reference to the header itself anywhere in the index structures. The only [InstrumentLog](../structures/InstrumentLog.md) reference points to the first [InstrumentLogRecord](../structures/InstrumentLogRecord.md).

### Instrument method data

One of the key differences between the modern layouts and the earlier file formats the embedded [MethodFile](../structures/MethodFile.md) based on the Microsoft Compound Binary File Format (OLE2). It stores a hierarchy of objects representing the method data for various instruments (pumps, detectors, &c.) used during the scan. In the earlier formats, these objects were more haphazardly arranged among the data streams.
