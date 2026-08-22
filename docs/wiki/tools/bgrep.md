---
title: bgrep
original: https://code.google.com/p/unfinnigan/wiki/bgrep
updated: 2013-05-25 13:13:53
author: selko...@gmail.com
source: Internet Archive copy of Google Code wiki
---

[Bgrep](https://github.com/tmbinc/bgrep) allows searching for strings of bytes with wildcards in a binary file.

Because it requires the search pattern to be supplied in the big-endian order, I wrote this wrapper to reverse the order:

```
#!/usr/bin/env perl

my ($hex, $file) = @ARGV;
my $bits = pack("V*", unpack("N*", pack("H*", $hex)));
my $le = unpack("H*", $bits);
exec "bgrep $le $file";
```

It doesn't handle wildcards, though.
