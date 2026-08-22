---
title: ScanData
original: https://code.google.com/p/unfinnigan/wiki/ScanData
updated: 2010-03-17 20:09:17
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

This is an abstract object that has no properties and no implementation. It is just a handy name for the stream of DataPacket objects.

The stream is directly addressable: each [ScanIndexEntry](ScanIndexEntry.md) stores a byte offset of the corresponding DataPacket within ScanData.
