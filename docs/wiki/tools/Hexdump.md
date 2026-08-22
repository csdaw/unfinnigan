---
title: Hexdump
original: https://code.google.com/p/unfinnigan/wiki/Hexdump
updated: 2010-05-23 14:13:34
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

`hexdump` has all the same functions as `od`, but its options are somewhat easier to type. The following command will dump the data part of the instrument method in a raw data file:

```
uf-meth sample.raw -p LTQ/Data | hexdump -C
```
