---
title: ASInfo
original: https://code.google.com/p/unfinnigan/wiki/ASInfo
updated: 2012-05-26 16:17:10
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

ASInfo is a variable-length structure containing a static binary preamble ([ASInfoPreamble](ASInfoPreamble.md)) and a text string describing the auto-sampler (the letters A and S in 'CAS' stand for Auto-Sampler; I do not know what C stands for).

## Structure

| offset | size | type | key | example |
| --- | --- | --- | --- | --- |
| 0 | 24 | [ASInfoPreamble](ASInfoPreamble.md) | `preamble` | ... |
| 24 | 4 | [PascalStringWin32](PascalStringWin32.md) | `text` | `384 Well Plate` |
