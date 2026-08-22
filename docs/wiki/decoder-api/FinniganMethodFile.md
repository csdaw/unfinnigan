---
title: FinniganMethodFile
original: https://code.google.com/p/unfinnigan/wiki/FinniganMethodFile
updated: 2011-04-04 09:16:23
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

# `Finnigan::MethodFile`

[source]

## SYNOPSIS

```
use Finnigan;

my $mf = Finnigan::MethodFile->decode(\*INPUT);
say $mf->header->version;
say $mf->container->size;
my $dirent = $mf->container->find($path);
```

## Description

This object decodes the outer container for a Windows OLE2 directory ([Finnigan::OLE2File](FinniganOLE2File.md)), which in turn contains a set of method files for various instruments, both in binary and text representations.

The outer container also contains a name translation table mapping the names of the instruments into the names used inside the method files.

## Methods

- **decode($stream)**
> The constructor method

- **header**
> Get the [Finnigan::FileHeader](FinniganFileHeader.md) object attached to the method file

- **n**
> Get the number of entries in the name translation table

- **translation_table**
> Get the name translation table

- **instrument_name($i)**
> Get the translation pair at index $i in the name translation table

- **file_size**
> Get the size of the [Finnigan::OLE2File](FinniganOLE2File.md) container

- **container**
> Get the [Finnigan::OLE2File ](FinniganOLE2File.md) object

## See Also

[Method file structure overview](../structures/MethodFileStructure.md)

[FileHeader](../structures/FileHeader.md) (structure)

[Finnigan::FileHeader](FinniganFileHeader.md) (decoder object)

[Finnigan::OLE2File](FinniganOLE2File.md) (decoder object)
