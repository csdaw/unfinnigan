**[Wiki page list](https://github.com/csdaw/unfinnigan/tree/wiki)**

**[Finnigan file structure](FileStructureTOC.md)**

**[Tools](Tools.md)**

**[Decoder API](DecoderTOC.md)**

Author: Gene Selkov Jr

License: Artistic License/GPL

## Decoding Finnigan raw files

This project has reached the stage at which it can deliver useful code. The file structure and the meaning of its most important elements, with the exception of the embedded method file, has been largely understood.

One of the Unfinnigan tools, [uf-mzxml](UnfinniganMzXML.md), can already replace readw where [mzXML](http://tools.proteomecenter.org/wiki/index.php?title=Formats:mzXML) is a suitable encoding. Unlike [readw](http://tools.proteomecenter.org/wiki/index.php?title=Software:ReAdW) and other tools that depend on the closed-source I/O library by Thermo, [uf-mzxml](UnfinniganMzXML.md) and other Unfinnigan tools read the data file directly and thus reduce the [confusion](http://www.mail-archive.com/spctools-discuss@googlegroups.com/msg01683.html) surrounding the provenance of important data elements.

Speed is another advantage gained by direct access to the data. The native Finnigan file format provides a more efficient storage than converted text-based formats.

### Supported versions

The Unfinnigan tools have been tested with the file versions **57**, **62**, **63** and **64**. The [Hachoir](http://bitbucket.org/haypo/hachoir/wiki/hachoir-core) parser, [finnigan.py](HachoirParser.md), can also read version **8** found among Xcalibur example files, but Hachoir can not do useful work; its purpose was to aid in the exploration of the file structure -- the role in which it has performed marvellously. Version 8 is probably only a historical curiosity, although some of its elements helped to unravel the structure of the present file formats.

If there is any interest in decoding early file versions, the information already available can be used to create decoder variants to support these versions. A variety of sample files for each version will be necessary to make that possible.

### News

I have received a few stripped-down samples of the new <b>v.64</b> Finnigan format. It seems to be essentially the same as <b>v.63</b>, with the only difference that the 32-bit seek addresses and offsets used in the earlier format are now replaced with the 64-bit ones. I have updated both the  [finnigan.py](HachoirParser.md) and the [Perl API](DecoderTOC.md) to work with the new format, but it may be too early to claim success, without further testing. If you would like to contribute a sample, please put it somewhere I can grab it.

## Motivations

Mass spectrometers by Thermo can encode raw specta (and even the time-domain transients) using the Finnigan "raw" file format, but they are seldom configured to do so. Most of the time, the programs used to control this family of instruments cook data in one way or another. But it is good to have unencumbered access to everything there is in those files, whether cooked or not. The reason is twofold.

One, it is important to understand the entire process leading from the physical sample to the calibrated mass spectra, which is presently obscured by the proprietary software used to run the instruments. It is reasonable to believe that the instrument vendor has taken all possible precautions to make the data processing valid and accurate, but science cannot rely on trust. I want to see what is happening to my data with my own eyes.
The second reason is the interoperability of software. I want to be able to use my own tools to process my data, and I can't be bothered to install Windows or any other proprietary software just in order to make the data visible.
So this project, which I am sure will be regarded by some as malicious reverse-engineering, is primarily driven by curiosity, meticulousness, and laziness, rather than malice or contempt.

The project is currently in what I call observation stage. I have examined enough data files to understand their composition and to extract the data I need in my present work. I have not yet built a parser that can reliably extract all data from all possible Finnigan file versions, recorded by every existing instrument in every possible scan mode. I do not think I can ever achieve all that by myself. The code I have created may fail to read the particular version of the file you have. But I believe that an accurate description of my observations and of the method I used to achieve my specific goals may help you achieve yours in mere days or hours, and if you add your observations to mine, we can soon have a reliable and versatile tool.

At the present stage, treat it as a testable description of the file format, supplemented with a bunch of tools that can be used to examine data files and their components.

