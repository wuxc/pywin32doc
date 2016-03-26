# PyIExtractIconW

## PyIExtractIconW Object

Description of the interface

#### Methods


  - [Extract](PyIExtractIconW.md#pyiextracticonwextract)

    Description of Extract&nbsp;

  - [GetIconLocation](PyIExtractIconW.md#pyiextracticonwgeticonlocation)

    Description of GetIconLocation&nbsp;

## [PyIExtractIconW](#pyiextracticonw)\.Extract

 **Extract\( *pszFile*  *, nIconIndex*  *, nIconSize* ** \)
Description of Extract\.

#### Parameters


  -  *pszFile* : **unicode** 

    Description for pszFile

  -  *nIconIndex* : int

    Description for nIconIndex

  -  *nIconSize* : int

    Description for nIconIndex

#### Return Value
The result is \(hicon\_large, hicon\_small\), or 

\(None,None\) if the underlying function returns S\_FALSE, indicating 

the calling application should extract it\.

## [PyIExtractIconW](#pyiextracticonw)\.GetIconLocation

 **GetIconLocation\( *uFlags*  *, cchMax* ** \)
Description of GetIconLocation\.

#### Parameters


  -  *uFlags* : int

    Description for uFlags

  -  *cchMax\=MAX\_PATH\+MAX\_FNAME* : int

    Buffer size to allocate for file name