---
title: DecoderTOC
original: https://code.google.com/p/unfinnigan/wiki/DecoderTOC
updated: 2012-05-26 16:12:49
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# Finnigan data decoder

**Note**: *The API has changed to accommodate the new 64-bit file pointers introduced in **v.64**, as well as the 32-bit pointers used in the older versions. [The tools written with the old API must be fixed](APIChanges.md).*

## Overview

The decoder is written in [perl](http://www.perl.org/) and it consists of a hierarchy of objects recursively instantiating themselves from the binary data in the input file. The object hierarchy closely follows the [Finnigan file structure](../overview/FileStructureTOC.md). The simplest objects use the [unpack](http://perldoc.perl.org/functions/unpack.html) function to read the data according to their object templates, and the more complex objects call other objects' constructors, passing them the file pointer they have acquired from the user program. Each elementary object advances the file pointer by the size of its template.

Because the size of some objects stored in the input file cannot be known beforehand, certain data streams can only be reached by reading through all the preceding data structures. Use [this diagram](../overview/FileLayoutOverview.md) as a guide to determine which structures must be consumed on the way to a certain type of data.

## Decoder API

This document is work in progress. While it is reasonably complete and accurate, it cannot possibly cover all code and all use cases. An alternative way to learn how to use the decoder is to look at the Unfinnigan tools (uf-\*) and at the test suite Finnigan.t, which covers a substantial part of the API.

### The basic use pattern

```
  seek INPUT, $object_address, 0
  $object = Finnigan::Object->decode(\*INPUT, $args);
```

where `Object` is a symbol for any of the decoder objects listed below.

Each Finnigan object has a constructor method named **decode()**, whose first argument is a filehandle positioned at the start of the object to be decoded. Some decoders require additional arguments passed as an array reference, for example, the version number argument in [Finnigan::ScanEventPreamble](FinniganScanEventPreamble.md). A single argument can be passed as it is, while multiple arguments can be passed as an array reference.

The constructor advances the handle to the start of the next object, so seeking to the start of the object of interest is only necessary when doing partial reads; in principle, the entire file can be read by calling of object constructors in sequency. In reality, it is often more efficient to seek ahead to fetch an index structure stored near the end of the file, then go back to the data stream using the pointers in the index.

The decoded data can be obtained by calling accessor methods on the object or by de-referencing the object reference (since all Finnigan objects are blessed hash references):

```
  $x = $object->element
```

or

```
  $x = $object->{element}
```

The accessor option is nicer, as it leads to less clutter in the code and leaves the possibility for additional processing of the data by the accessor routine, but it incurs a substantial performance penalty. For this reason, hash dereference is preferred in performance-critical code (inside loops).

### dump(%args)

All Finnigan objects are descendants of Finnigan::Decoder. One of the **Finnigan::Decoder** methods they inherit is **dump()**, which provides an easy way to explore the contents of decoded objects. The **dump()** method prints out the structure of the object it is called on in a few style, with relative or absolute addressess.

For example, many object dumps used in this wiki were created thus:

```
  $object->dump(style => 'wiki', relative => 1);
```

The **style** argument can have the values of `wiki`, `html` or none (meaning plain text). The **relative** argument is a boolean indicating whether to use the absolute or relative file addresses in the output. Relative in this case means "an offset within the object", while absolute is the seek address within the data file.

### read($stream, $template_list, $arg)

This is the [Finnigan::Decoder](FinniganDecoder.md) constructor method. Some derived decoders use it internally, but it can also be used to decode trivial objects at a given location in a file without having to write a dedicated decoder.

For example, to read a 32-bit stream length, use:

```
  my $object = Finnigan::Decoder->read(\*INPUT, ['length' => ['V', 'UInt32']]);
```

The `$template_list` argument names all fields to decode (in this case, just one: `length`), the template to use for each field (in this example, `V`), and provides a human-readable symbol for the template, which can be used in a number of ways; for example, when inspecting the structures with the `dump` method.

This may seem like a kludgy way of reading four bytes, but the upshot is that the resulting `$object` will have the size, type and location information tucked into it, so it can be analysed and dumped in a way consistent with other decoded objects. The advantage becomes even more apparent when the structure is more complex than a single scalar object.

The inherited `read` method provides the core functionality of all Finnigan decoders.

If only the value of the object is sought, then this even more kludgy code can be used:

```
  my $stream_length = Finnigan::Decoder->read(\*INPUT, ['length' => ['V', 'UInt32']])->{data}->{length}->{value};
```

Doing it this way is nonetheless easier than writing several lines of code reading the data into a buffer, checking for the I/O errors and unpacking the value.

### stringify()

Another handy method defined in some of the Finnigan objects is **stringify()**. It allows a concise representation of an object to be injected anywhere Perl expects a string. For example,

```
  $scan_event = Finnigan::ScanEvent->decode( \*INPUT, $header->version);
  say "$scan_event";
```

## Submodules

All submodules have built-in documentation (POD). To read the documentation for the installed modules, use **man** or **perldoc**, as in this example:

```
man Finnigan::ScanEvent
perldoc Finnigan::ScanEvent
```

**[Finnigan](FinniganNamespace.md)** [source] -- the namespace object

**[Finnigan::AuditTag](FinniganAuditTag.md)** [source] -- [AuditTag](../structures/AuditTag.md) decoder

**[Finnigan::ASInfo](FinniganASInfo.md)** [source] -- [ASInfo](../structures/ASInfo.md) decoder

**[Finnigan::ASInfoPreamble](FinniganASInfoPreamble.md)** [source] -- [ASInfoPreamble](../structures/ASInfoPreamble.md) decoder

**[Finnigan::Decoder](FinniganDecoder.md)** [source] -- the base class for all Finnigan decoders

**[Finnigan::Error](FinniganError.md)** [source] -- decoder for [Error](../structures/Error.md), an [ErrorLog](../structures/ErrorLog.md) entry

**[Finnigan::FileHeader](FinniganFileHeader.md)** [source] -- [FileHeader](../structures/FileHeader.md) decoder

**[Finnigan::FractionCollector](FinniganFractionCollector.md)** [source] -- [FractionCollector](../structures/FractionCollector.md) decoder

**[Finnigan::GenericDataDescriptor](FinniganGenericDataDescriptor.md)** [source] -- [GenericDataDescriptor](../structures/GenericDataDescriptor.md) decoder

**[Finnigan::GenericDataHeader](FinniganGenericDataHeader.md)** [source] -- [GenericDataHeader](../structures/GenericDataHeader.md) decoder

**[Finnigan::GenericRecord](FinniganGenericRecord.md)** [source] -- [GenericRecord](../structures/GenericRecord.md) decoder

**[Finnigan::InjectionData](FinniganInjectionData.md)** [source] -- [InjectionData](../structures/InjectionData.md) decoder

**[Finnigan::InstID](FinniganInstID.md)** [source] -- [InstID](../structures/InstID.md) (instrument identifiers) decoder

**[Finnigan::InstrumentLogRecord](FinniganInstrumentLogRecord.md)** [source] -- [InstrumentLogRecord](../structures/InstrumentLogRecord.md) decoder

**[Finnigan::MethodFile](FinniganMethodFile.md)** [source] -- a decoder for [MethodFile](../structures/MethodFile.md), an OLE2 method file container

**[Finnigan::OLE2DIF](FinniganOLE2DIF.md)** [source] -- Double-Indirect FAT decoder

**[Finnigan::OLE2DirectoryEntry](FinniganOLE2DirectoryEntry.md)** [source] -- OLE2 directory entry decoder

**[Finnigan::OLE2FAT](FinniganOLE2FAT.md)** [source] -- FAT sector decoder

**[Finnigan::OLE2File](FinniganOLE2File.md)** [source] -- Microsoft OLE2 (CDF) file decoder

**[Finnigan::OLE2Header](FinniganOLE2Header.md)** [source] -- OLE2 header decoder

**[Finnigan::OLE2Property](FinniganOLE2Property.md)** [source] -- OLE2 Property (index node) decoder

**[Finnigan::PacketHeader](FinniganPacketHeader.md)** [source] -- [PacketHeader](../structures/PacketHeader.md) decoder

**[Finnigan::Peak](FinniganPeak.md)** [source] -- the decoder for a single peak in [PeakList](../structures/PeakList.md)

**[Finnigan::Peaks](FinniganPeaks.md)** [source] -- [PeakList](../structures/PeakList.md) decoder

**[Finnigan::Profile](FinniganProfile.md)** [source] -- [Profile](../structures/Profile.md) decoder

**[Finnigan::ProfileChunk](FinniganProfileChunk.md)** [source] -- [ProfileChunk](../structures/ProfileChunk.md) decoder

**[Finnigan::RawFileInfo](FinniganRawFileInfo.md)** [source] - the decoder for [RawFileInfo](../structures/RawFileInfo.md), the primary index structure

**[Finnigan::RawFileInfoPreamble](FinniganRawFileInfoPreamble.md)** [source] -- the binary data part in [RawFileInfo](../structures/RawFileInfo.md)

**[Finnigan::Reaction](FinniganReaction.md)** [source] -- the decoder for [Reaction](../structures/Reaction.md) (precursor ion data)

**[Finnigan::RunHeader](FinniganRunHeader.md)** [source] -- [RunHeader](../structures/RunHeader.md) (the primary file index) decoder

**[Finnigan::SampleInfo](FinniganSampleInfo.md)** [source] -- [SampleInfo](../structures/SampleInfo.md) (the primary file index) decoder

**[Finnigan::Scan](FinniganScan.md)** [source] -- compound and lightweight [ScanDataPacket](../structures/ScanDataPacket.md) decoder

- **[Finnigan::Scan::Profile](FinniganScanProfile.md)** [source] -- [Profile](../structures/Profile.md) decoder

- **[Finnigan::Scan::ProfileChunk](FinniganScanProfileChunk.md)** [source] -- [ProfileChunk](../structures/ProfileChunk.md) decoder

- **[Finnigan::Scan::CentroidList](FinniganScanCentroidList.md)** [source] -- [PeakList](../structures/PeakList.md) decoder

**[Finnigan::ScanEvent](FinniganScanEvent.md)** [source] -- the decoder for [ScanEvent](../structures/ScanEvent.md), the scan type descriptor

**[Finnigan::ScanEventPreamble](FinniganScanEventPreamble.md)** [source] -- the decoder for [ScanEventPreamble](../structures/ScanEventPreamble.md), the byte array component of [ScanEvent](../structures/ScanEvent.md)

**[Finnigan::ScanEventTemplate](FinniganScanEventTemplate.md)** [source] -- the decoder for [ScanEventTemplate](../structures/ScanEventTemplate.md), the prototype scan descriptor

**[Finnigan::ScanIndexEntry](FinniganScanIndexEntry.md)** [source] -- the decoder for [ScanIndexEntry](../structures/ScanIndexEntry.md), a linked list element pointing to scan data

**[Finnigan::ScanParameters](FinniganScanParameters.md)** [source] -- the decoder for [ScanParameters](../structures/ScanParameters.md), a [GenericRecord](../structures/GenericRecord.md) containing various scan meta-data

**[Finnigan::SeqRow](FinniganSeqRow.md)** [source] -- [SeqRow](../structures/SeqRow.md) (sequencer table row) decoder
