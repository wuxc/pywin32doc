# PyIInternetProtocolInfo

## PyIInternetProtocolInfo Object

Description of the interface

#### Methods


  - [ParseUrl](PyIInternetProtocolInfo.md#pyiinternetprotocolinfoparseurl)

    Description of ParseUrl&nbsp;

  - [CombineUrl](PyIInternetProtocolInfo.md#pyiinternetprotocolinfocombineurl)

    Description of CombineUrl&nbsp;

  - [CompareUrl](PyIInternetProtocolInfo.md#pyiinternetprotocolinfocompareurl)

    Description of CompareUrl&nbsp;

  - [QueryInfo](PyIInternetProtocolInfo.md#pyiinternetprotocolinfoqueryinfo)

    Description of QueryInfo&nbsp;

## [PyIInternetProtocolInfo](#pyiinternetprotocolinfo).CombineUrl

 __CombineUrl( *pwzBaseUrl*  *, pwzRelativeUrl*  *, dwCombineFlags*  *, cchResult*  *, dwReserved* __ )
Description of CombineUrl.

#### Parameters


  -  *pwzBaseUrl* : __unicode__ 

    Description for pwzBaseUrl

  -  *pwzRelativeUrl* : __unicode__ 

    Description for pwzRelativeUrl

  -  *dwCombineFlags* : int

    Description for dwCombineFlags

  -  *cchResult* : int

    Description for cchResult

  -  *dwReserved* : int

    Description for dwReserved

## [PyIInternetProtocolInfo](#pyiinternetprotocolinfo).CompareUrl

 __CompareUrl( *pwzUrl1*  *, pwzUrl2*  *, dwCompareFlags* __ )
Description of CompareUrl.

#### Parameters


  -  *pwzUrl1* : __unicode__ 

    Description for pwzUrl1

  -  *pwzUrl2* : __unicode__ 

    Description for pwzUrl2

  -  *dwCompareFlags* : int

    Description for dwCompareFlags

## [PyIInternetProtocolInfo](#pyiinternetprotocolinfo).ParseUrl

 __ParseUrl( *pwzUrl*  *, ParseAction*  *, dwParseFlags*  *, cchResult*  *, dwReserved* __ )
Description of ParseUrl.

#### Parameters


  -  *pwzUrl* : __unicode__ 

    Description for pwzUrl

  -  *ParseAction* : int

    Description for ParseAction

  -  *dwParseFlags* : int

    Description for dwParseFlags

  -  *cchResult* : int

    Description for cchResult

  -  *dwReserved* : int

    Description for dwReserved

## [PyIInternetProtocolInfo](#pyiinternetprotocolinfo).QueryInfo

int|string = __QueryInfo( *pwzUrl*  *, OueryOption*  *, dwQueryFlags*  *, cbBuffer*  *, dwReserved* __ )
Description of QueryInfo.

#### Parameters


  -  *pwzUrl* : __unicode__ 

    Description for pwzUrl

  -  *OueryOption* : int

    Description for OueryOption

  -  *dwQueryFlags* : int

    Description for dwQueryFlags

  -  *cbBuffer* : int

    Description for cbBuffer

  -  *dwReserved* : int

    Description for dwReserved

#### Comments
If the buffer size is the size of an integer, an integer will be returned, otherwise a string.