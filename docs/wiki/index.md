---
title: unfinnigan wiki
original: https://code.google.com/p/unfinnigan/w/list
source: Internet Archive copy of Google Code wiki
---

# unfinnigan wiki

Documentation recovered from the Google Code project *unfinnigan* (Painless extraction of mass spectra from Thermo “raw” files), converted from Internet Archive copies of the original HTML pages.

## Start here

- [WikiHome](overview/WikiHome.md)
- [FileLayoutOverview](overview/FileLayoutOverview.md)
- [FileStructureTOC](overview/FileStructureTOC.md)
- [CommonStructures](overview/CommonStructures.md)
- [SupportedVersions](overview/SupportedVersions.md)
- [Problems](overview/Problems.md)

## File structure reference

### File-level structures

- [ASInfo](structures/ASInfo.md)
- [ASInfoPreamble](structures/ASInfoPreamble.md)
- [AuditTag](structures/AuditTag.md)
- [FileHeader](structures/FileHeader.md)
- [InjectionData](structures/InjectionData.md)
- [InstrumentMethodData](structures/InstrumentMethodData.md)
- [MethodFile](structures/MethodFile.md)
- [MethodFileStructure](structures/MethodFileStructure.md)
- [RawFileInfo](structures/RawFileInfo.md)
- [RawFileInfoPreamble](structures/RawFileInfoPreamble.md)
- [SeqRow](structures/SeqRow.md)

### Index and metadata

- [Error](structures/Error.md)
- [ErrorLog](structures/ErrorLog.md)
- [InstID](structures/InstID.md)
- [InstrumentLog](structures/InstrumentLog.md)
- [InstrumentLogRecord](structures/InstrumentLogRecord.md)
- [RunHeader](structures/RunHeader.md)
- [SampleInfo](structures/SampleInfo.md)
- [TuneFile](structures/TuneFile.md)

### Scan data streams

- [FractionCollector](structures/FractionCollector.md)
- [PacketHeader](structures/PacketHeader.md)
- [PeakData](structures/PeakData.md)
- [PeakList](structures/PeakList.md)
- [Profile](structures/Profile.md)
- [ProfileChunk](structures/ProfileChunk.md)
- [Reaction](structures/Reaction.md)
- [ScanData](structures/ScanData.md)
- [ScanDataPacket](structures/ScanDataPacket.md)
- [ScanEvent](structures/ScanEvent.md)
- [ScanEventHierarchy](structures/ScanEventHierarchy.md)
- [ScanEventPreamble](structures/ScanEventPreamble.md)
- [ScanEventStream](structures/ScanEventStream.md)
- [ScanEventTemplate](structures/ScanEventTemplate.md)
- [ScanIndex](structures/ScanIndex.md)
- [ScanIndexEntry](structures/ScanIndexEntry.md)
- [ScanIndexStream](structures/ScanIndexStream.md)
- [ScanParameters](structures/ScanParameters.md)
- [ScanParametersStream](structures/ScanParametersStream.md)

### Generic (self-describing) records

- [GenericData](structures/GenericData.md)
- [GenericDataDescriptor](structures/GenericDataDescriptor.md)
- [GenericDataHeader](structures/GenericDataHeader.md)
- [GenericRecord](structures/GenericRecord.md)
- [GenericRecordExample](structures/GenericRecordExample.md)

### Shared field types

- [PascalStringWin32](structures/PascalStringWin32.md)
- [RawBytes](structures/RawBytes.md)
- [TimestampWin64](structures/TimestampWin64.md)

## Decoder API (Perl)

- [DecoderTOC](decoder-api/DecoderTOC.md) -- start here
- [FinniganASInfo](decoder-api/FinniganASInfo.md)
- [FinniganASInfoPreamble](decoder-api/FinniganASInfoPreamble.md)
- [FinniganAuditTag](decoder-api/FinniganAuditTag.md)
- [FinniganDecoder](decoder-api/FinniganDecoder.md)
- [FinniganError](decoder-api/FinniganError.md)
- [FinniganFileHeader](decoder-api/FinniganFileHeader.md)
- [FinniganFractionCollector](decoder-api/FinniganFractionCollector.md)
- [FinniganGenericDataDescriptor](decoder-api/FinniganGenericDataDescriptor.md)
- [FinniganGenericDataHeader](decoder-api/FinniganGenericDataHeader.md)
- [FinniganGenericRecord](decoder-api/FinniganGenericRecord.md)
- [FinniganInjectionData](decoder-api/FinniganInjectionData.md)
- [FinniganInstID](decoder-api/FinniganInstID.md)
- [FinniganInstrumentLogRecord](decoder-api/FinniganInstrumentLogRecord.md)
- [FinniganMethodFile](decoder-api/FinniganMethodFile.md)
- [FinniganNamespace](decoder-api/FinniganNamespace.md)
- [FinniganOLE2DIF](decoder-api/FinniganOLE2DIF.md)
- [FinniganOLE2DirectoryEntry](decoder-api/FinniganOLE2DirectoryEntry.md)
- [FinniganOLE2FAT](decoder-api/FinniganOLE2FAT.md)
- [FinniganOLE2File](decoder-api/FinniganOLE2File.md)
- [FinniganOLE2Header](decoder-api/FinniganOLE2Header.md)
- [FinniganOLE2Property](decoder-api/FinniganOLE2Property.md)
- [FinniganPacketHeader](decoder-api/FinniganPacketHeader.md)
- [FinniganPeak](decoder-api/FinniganPeak.md)
- [FinniganPeaks](decoder-api/FinniganPeaks.md)
- [FinniganProfile](decoder-api/FinniganProfile.md)
- [FinniganProfileChunk](decoder-api/FinniganProfileChunk.md)
- [FinniganRawFileInfo](decoder-api/FinniganRawFileInfo.md)
- [FinniganRawFileInfoPreamble](decoder-api/FinniganRawFileInfoPreamble.md)
- [FinniganReaction](decoder-api/FinniganReaction.md)
- [FinniganRunHeader](decoder-api/FinniganRunHeader.md)
- [FinniganSampleInfo](decoder-api/FinniganSampleInfo.md)
- [FinniganScan](decoder-api/FinniganScan.md)
- [FinniganScanCentroidList](decoder-api/FinniganScanCentroidList.md)
- [FinniganScanEvent](decoder-api/FinniganScanEvent.md)
- [FinniganScanEventPreamble](decoder-api/FinniganScanEventPreamble.md)
- [FinniganScanEventTemplate](decoder-api/FinniganScanEventTemplate.md)
- [FinniganScanIndexEntry](decoder-api/FinniganScanIndexEntry.md)
- [FinniganScanParameters](decoder-api/FinniganScanParameters.md)
- [FinniganScanProfile](decoder-api/FinniganScanProfile.md)
- [FinniganScanProfileChunk](decoder-api/FinniganScanProfileChunk.md)
- [FinniganSeqRow](decoder-api/FinniganSeqRow.md)
- [APIChanges](decoder-api/APIChanges.md)

## Tools

- [UnfinniganASInfo](tools/UnfinniganASInfo.md)
- [UnfinniganError](tools/UnfinniganError.md)
- [UnfinniganHeader](tools/UnfinniganHeader.md)
- [UnfinniganIndex](tools/UnfinniganIndex.md)
- [UnfinniganInstID](tools/UnfinniganInstID.md)
- [UnfinniganLog](tools/UnfinniganLog.md)
- [UnfinniganMethodFile](tools/UnfinniganMethodFile.md)
- [UnfinniganMzML](tools/UnfinniganMzML.md)
- [UnfinniganMzXML](tools/UnfinniganMzXML.md)
- [UnfinniganRawFileInfo](tools/UnfinniganRawFileInfo.md)
- [UnfinniganRunHeader](tools/UnfinniganRunHeader.md)
- [UnfinniganScan](tools/UnfinniganScan.md)
- [UnfinniganScanLight](tools/UnfinniganScanLight.md)
- [UnfinniganScanParameters](tools/UnfinniganScanParameters.md)
- [UnfinniganSegments](tools/UnfinniganSegments.md)
- [UnfinniganSeqRow](tools/UnfinniganSeqRow.md)
- [UnfinniganTrailer](tools/UnfinniganTrailer.md)
- [UnfinniganTuneFile](tools/UnfinniganTuneFile.md)

- [ConversionTools](tools/ConversionTools.md)
- [HachoirParser](tools/HachoirParser.md)
- [Hexdump](tools/Hexdump.md)
- [Iconv](tools/Iconv.md)
- [MzXMLUnpack](tools/MzXMLUnpack.md)
- [Tools](tools/Tools.md)
- [UnixStrings](tools/UnixStrings.md)
- [bgrep](tools/bgrep.md)

## Meta

- [WikiSidebar](meta/WikiSidebar.md) -- original site navigation
