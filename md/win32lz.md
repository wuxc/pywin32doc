
## [win32lz](#README.md#win32lz).Close

 **Close( *handle* ** )
Closes a handle to an LZ file.

#### Parameters


     *handle* : int

    The handle of the LZ file to close.

#### Win32 API References


    Search for *LZClose* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LZClose),[google](#README.md#http://www.google.com/search?q=LZClose)or[google groups](#README.md#http://groups.google.com/groups?q=LZClose).

## [win32lz](#README.md#win32lz).Copy

int = **Copy( *hSrc*  *, hDest* ** )
Copies a source file to a destination file.

#### Parameters


     *hSrc* : int

    The handle of the source file to copy.

     *hDest* : int

    The handle of the destination file.

#### Comments
If the source file is compressed with the Microsoft File Compression Utility 

(COMPRESS.EXE), this function creates a decompressed destination file. 

If the source file is not compressed, this function duplicates the original file.

#### Win32 API References


    Search for *LZCopy* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LZCopy),[google](#README.md#http://www.google.com/search?q=LZCopy)or[google groups](#README.md#http://groups.google.com/groups?q=LZCopy).

## [win32lz](#README.md#win32lz).GetExpandedName

string = **GetExpandedName( *Source* ** )
Retrieves the original name of an expanded file,

#### Parameters


     *Source* : str

    Name of a compressed file

#### Win32 API References


    Search for *GetExpandedName* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetExpandedName),[google](#README.md#http://www.google.com/search?q=GetExpandedName)or[google groups](#README.md#http://groups.google.com/groups?q=GetExpandedName).

## [win32lz](#README.md#win32lz).Init

 **Init( *handle* ** )
Allocates memory for the internal data structures required to decompress files, and then creates and initializes them.

#### Parameters


     *handle* : int

    handle of source file

#### Win32 API References


    Search for *LZInit* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LZInit),[google](#README.md#http://www.google.com/search?q=LZInit)or[google groups](#README.md#http://groups.google.com/groups?q=LZInit).

## [win32lz](#README.md#win32lz).OpenFile

int,(tuple) = **OpenFile( *fileName*  *, action* ** )
Creates, opens, reopens, or deletes the specified file.

#### Parameters


     *fileName* : string

    Name of file to open

     *action* : int

    Can be one of the wi32con.OF_ constants (OF_CREATE, OF_DELETE, etc)

#### Win32 API References


    Search for *LZOpenFile* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LZOpenFile),[google](#README.md#http://www.google.com/search?q=LZOpenFile)or[google groups](#README.md#http://groups.google.com/groups?q=LZOpenFile).