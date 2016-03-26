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


## [PyIInternetProtocolInfo](PyIInternetProtocolInfo.md#pyiinternetprotocolinfo)\.CombineUrl

CombineUrl\(pwzBaseUrl, pwzRelativeUrl, dwCombineFlags, cchResult, dwReserved\)
Description of CombineUrl\.

#### Parameters

  - pwzBaseUrl : unicode

    Description for pwzBaseUrl

  - pwzRelativeUrl : unicode

    Description for pwzRelativeUrl

  - dwCombineFlags : int

    Description for dwCombineFlags

  - cchResult : int

    Description for cchResult

  - dwReserved : int

    Description for dwReserved


## [PyIInternetProtocolInfo](PyIInternetProtocolInfo.md#pyiinternetprotocolinfo)\.CompareUrl

CompareUrl\(pwzUrl1, pwzUrl2, dwCompareFlags\)
Description of CompareUrl\.

#### Parameters

  - pwzUrl1 : unicode

    Description for pwzUrl1

  - pwzUrl2 : unicode

    Description for pwzUrl2

  - dwCompareFlags : int

    Description for dwCompareFlags


## [PyIInternetProtocolInfo](PyIInternetProtocolInfo.md#pyiinternetprotocolinfo)\.ParseUrl

ParseUrl\(pwzUrl, ParseAction, dwParseFlags, cchResult, dwReserved\)
Description of ParseUrl\.

#### Parameters

  - pwzUrl : unicode

    Description for pwzUrl

  - ParseAction : int

    Description for ParseAction

  - dwParseFlags : int

    Description for dwParseFlags

  - cchResult : int

    Description for cchResult

  - dwReserved : int

    Description for dwReserved


## [PyIInternetProtocolInfo](PyIInternetProtocolInfo.md#pyiinternetprotocolinfo)\.QueryInfo

int|string = QueryInfo\(pwzUrl, OueryOption

, dwQueryFlags

, cbBuffer

, dwReserved

\)
Description of QueryInfo\.

#### Parameters

  - pwzUrl : unicode

    Description for pwzUrl

  - OueryOption : int

    Description for OueryOption

  - dwQueryFlags : int

    Description for dwQueryFlags

  - cbBuffer : int

    Description for cbBuffer

  - dwReserved : int

    Description for dwReserved

#### Comments

If the buffer size is the size of an integer, an integer will be returned, otherwise a string\.