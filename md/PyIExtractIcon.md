# PyIExtractIcon

## PyIExtractIcon Object



Description of the interface

#### Methods


  - [Extract](PyIExtractIcon.md#pyiextracticonextract)

    Description of Extract&nbsp;

  - [GetIconLocation](PyIExtractIcon.md#pyiextracticongeticonlocation)

    Description of GetIconLocation&nbsp;

## [PyIExtractIcon](#pyiextracticon)\.Extract

Extract\(pszFile, nIconIndex, nIconSize\)
Description of Extract\.

#### Parameters


  - pszFile :unicode

    Description for pszFile

  - nIconIndex : int

    Description for nIconIndex

  - nIconSize : int

    Description for nIconIndex

#### Return Value
The result is \(hicon\_large, hicon\_small\), or 

\(None,None\) if the underlying function returns S\_FALSE, indicating 

the calling application should extract it\.

## [PyIExtractIcon](#pyiextracticon)\.GetIconLocation

GetIconLocation\(uFlags, cchMax\)
Description of GetIconLocation\.

#### Parameters


  - uFlags : int

    Description for uFlags

  - cchMax=MAX\_PATH\+MAX\_FNAME : int

    Buffer size to allocate for file name