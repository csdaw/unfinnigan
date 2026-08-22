---
title: UnfinniganHeader
original: https://code.google.com/p/unfinnigan/wiki/UnfinniganHeader
updated: 2011-04-02 08:45:09
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# uf-header

## SYNOPSIS

```
 uf-header [options] <file>
```

## OPTIONS

***--help*** Print a brief help message and exit.

***--man*** Print the manual page and exit.

***--dump*** Prints the table listing all header fields with their seek addresses, sizes, acess keys and values.

***--html*** Dump as an html table

***--wiki*** Dump as a wiki table

***--size*** Show header size in bytes.

***--atag*** Dump the contents of the first [AuditTag](../structures/AuditTag.md) object, rather than the header itself.

***--relative*** Show relative addresses of all elements. The default is to show the absolute seek address.

## DESCRIPTION

`uf-header` will read the given input file and display the contents of its header or the [AuditTag](../structures/AuditTag.md) structures embedded into it.

It will return an error message if the file is not a Finnigan raw file.

By default, it prints a few header items (version number and parts of its [AuditTag](../structures/AuditTag.md)) on a single line.

## SEE ALSO

[FileHeader](../structures/FileHeader.md) (structure)

[Finnigan::FileHeader](../decoder-api/FinniganFileHeader.md) (decoder)

## EXAMPLES

```
 uf-header sample.raw
```

> (will print the file version and creation date)

```
 uf-header -d sample.raw
```

> (will dump all header fields)

```
 uf-header -d --atag sample.raw
```

> (will dump the contents of the first [AuditTag](../structures/AuditTag.md))
