---
title: UnfinniganMethodFile
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganMethodFile
updated: 2011-04-02 11:42:50
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-meth

## SYNOPSIS

`uf-meth [options] <file>`

## OPTIONS

***-help*** Print a brief help message and exit.

***-e`[`xtract`]`*** extract the entire OLE2 container (Microsoft Compound File)

***-l`[`ist`]`*** list the container contents

***-d`[`ump`]`*** Prints a table listing all structure elements with their seek addresses, sizes, acess keys and values. Complex sub-structures are represented by short summaries and their contents can be examined separately (see the***-H''' and***-p''' options}

***-h`[`tml`]`*** Dump as html table.

***-w`[`iki`]`*** Dump as a wiki-style table.

***-s`[`ize`]`*** Show overall structure size in bytes.

***-r`[`elative`]`*** Show relative addresses of all itmes. The default is to show the absolute seek address.

***-H`[`eader`]`*** Dump the contents of [FileHeader](../structures/FileHeader.md), instead of the parent object.

***-p`[`ath`]`** `<`path`>`* Give the full path to extract a single component from the compound OLE2 container.

## DESCRIPTION

`uf-meth` displays the contents of the [MethodFile](../structures/MethodFile.md) structure, its component [FileHeader](../structures/FileHeader.md). and the compound file (OLE2) storage embedded within.

By default, it lists the instrument methods comtained in the compound file, along with with their directory names.

## SEE ALSO

[MethodFile](../structures/MethodFile.md)

### EXAMPLES

- `uf-meth sample.raw`

> (names all instruments described in the file, one name per line)

> *Example output*:
>
> ```
> Surveyor Sample Pump -> Surveyor Sample Pump
> Surveyor MS Pump -> Surveyor MS Pump
> Micro AS -> Micro AS
> LTQ-FT MS -> LTQ
> ```

- `uf-meth -l sample.raw`

> (lists the compound file's directory, one node per line)

> *Example output*:
>
> ```
> LTQ 
>   Data (2560 bytes)
>   Text (11742 bytes)
>   Header (1396 bytes)
> Micro AS 
>   Data (641 bytes)
>   Text (1164 bytes)
> Surveyor MS Pump 
>   Data (228 bytes)
>   Text (1176 bytes)
>   Comments (4 bytes)
> Surveyor Sample Pump 
>   Data (228 bytes)
>   Text (1176 bytes)
>   Comments (4 bytes)
> ```

- `uf-meth sample.raw -p LTQ/Text > method.ltq`

> (writes the text description of the analyzer method)

- `uf-meth sample.raw -p LTQ/Data > method.ltq.data`

> (writes the raw binary data of the analyzer method)

- `uf-meth sample.raw -dp LTQ/Header`

> (prints the hex dump of LTQ/Header)

> *Example output*:

```
  0x0000 : 05 A1 54 00 68 00 65 00 72 00 6D 00 6F 00 20 00 : ..T.h.e.r.m.o...
  0x0010 : 46 00 69 00 6E 00 6E 00 69 00 67 00 61 00 6E 00 : F.i.n.n.i.g.a.n.
  0x0020 : 20 00 4C 00 54 00 51 00 00 00 00 00 00 00 00 00 : ..L.T.Q.........
  0x0030 : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 : ................
  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
```

- `uf-meth -dr sample.raw`

> (dumps the [MethodFile](../structures/MethodFile.md) structure with relative addresses)

- `uf-meth -drH sample.raw`

> (dumps the Finnigan header residing in the [MethodFile](../structures/MethodFile.md), with relative addresses)
