# PyIExtractIcon

## PyIExtractIcon Object

Description of the interface

#### Methods


  - [Extract](PyIExtractIcon.md#pyiextracticonextract)

    Description of Extract&nbsp;

  - [GetIconLocation](PyIExtractIcon.md#pyiextracticongeticonlocation)

    Description of GetIconLocation&nbsp;

## [PyIExtractIcon](#pyiextracticon).Extract

 __Extract( *pszFile*  *, nIconIndex*  *, nIconSize* __ )
Description of Extract.

#### Parameters


  -  *pszFile* : __unicode__ 

    Description for pszFile

  -  *nIconIndex* : int

    Description for nIconIndex

  -  *nIconSize* : int

    Description for nIconIndex

#### Return Value
The result is (hicon_large, hicon_small), or 

(None,None) if the underlying function returns S_FALSE, indicating 

the calling application should extract it.

## [PyIExtractIcon](#pyiextracticon).GetIconLocation

 __GetIconLocation( *uFlags*  *, cchMax* __ )
Description of GetIconLocation.

#### Parameters


  -  *uFlags* : int

    Description for uFlags

  -  *cchMax=MAX_PATH+MAX_FNAME* : int

    Buffer size to allocate for file name