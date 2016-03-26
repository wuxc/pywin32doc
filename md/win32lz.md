# win32lz

## Module win32lz

A module encapsulating the Windows LZ compression routines\.

#### Methods


  - [GetExpandedName](win32lz.md#win32lzgetexpandedname)

    Retrieves the original name of an expanded file,&nbsp;

  - [Close](win32lz.md#win32lzclose)

    Closes a handle to an LZ file\.&nbsp;

  - [Copy](win32lz.md#win32lzcopy)

    Copies a source file to a destination file\.&nbsp;

  - [Init](win32lz.md#win32lzinit)

    Allocates memory for the internal data structures required to decompress files, and then creates and initializes them\.&nbsp;

  - [OpenFile](win32lz.md#win32lzopenfile)

    Creates, opens, reopens, or deletes the specified file\.&nbsp;

## [win32lz](#win32lz)\.Close

 **Close\( *handle* ** \)
Closes a handle to an LZ file\.

#### Parameters


  -  *handle* : int

    The handle of the LZ file to close\.

#### Win32 API References


  - Search for *LZClose* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=lzclose),[google](#http://www.google.com/search?q=lzclose)or[google groups](#http://groups.google.com/groups?q=lzclose)\.

## [win32lz](#win32lz)\.Copy

int \= **Copy\( *hSrc*  *, hDest* ** \)
Copies a source file to a destination file\.

#### Parameters


  -  *hSrc* : int

    The handle of the source file to copy\.

  -  *hDest* : int

    The handle of the destination file\.

#### Comments
If the source file is compressed with the Microsoft File Compression Utility 

\(COMPRESS\.EXE\), this function creates a decompressed destination file\. 

If the source file is not compressed, this function duplicates the original file\.

#### Win32 API References


  - Search for *LZCopy* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=lzcopy),[google](#http://www.google.com/search?q=lzcopy)or[google groups](#http://groups.google.com/groups?q=lzcopy)\.

## [win32lz](#win32lz)\.GetExpandedName

string \= **GetExpandedName\( *Source* ** \)
Retrieves the original name of an expanded file,

#### Parameters


  -  *Source* : str

    Name of a compressed file

#### Win32 API References


  - Search for *GetExpandedName* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getexpandedname),[google](#http://www.google.com/search?q=getexpandedname)or[google groups](#http://groups.google.com/groups?q=getexpandedname)\.

## [win32lz](#win32lz)\.Init

 **Init\( *handle* ** \)
Allocates memory for the internal data structures required to decompress files, and then creates and initializes them\.

#### Parameters


  -  *handle* : int

    handle of source file

#### Win32 API References


  - Search for *LZInit* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=lzinit),[google](#http://www.google.com/search?q=lzinit)or[google groups](#http://groups.google.com/groups?q=lzinit)\.

## [win32lz](#win32lz)\.OpenFile

int,\(tuple\) \= **OpenFile\( *fileName*  *, action* ** \)
Creates, opens, reopens, or deletes the specified file\.

#### Parameters


  -  *fileName* : string

    Name of file to open

  -  *action* : int

    Can be one of the wi32con\.OF\_ constants \(OF\_CREATE, OF\_DELETE, etc\)

#### Win32 API References


  - Search for *LZOpenFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=lzopenfile),[google](#http://www.google.com/search?q=lzopenfile)or[google groups](#http://groups.google.com/groups?q=lzopenfile)\.