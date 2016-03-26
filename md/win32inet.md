# win32inet

## Module win32inet

An interface to the Windows internet (wininet) API

#### Methods


  - [InternetSetCookie](win32inet.md#win32inetinternetsetcookie)

    Creates a cookie associated with the specified URL.&nbsp;

  - [InternetGetCookie](win32inet.md#win32inetinternetgetcookie)

    Retrieves the cookie for the specified URL&nbsp;

  - [InternetAttemptConnect](win32inet.md#win32inetinternetattemptconnect)

    Attempts to make a connection to the Internet.&nbsp;

  - [InternetCheckConnection](win32inet.md#win32inetinternetcheckconnection)

    Allows an application to check if a connection to the Internet can be established&nbsp;

  - [InternetGoOnline](win32inet.md#win32inetinternetgoonline)

    Prompts the user for permission to initiate connection to a URL.&nbsp;

  - [InternetCloseHandle](win32inet.md#win32inetinternetclosehandle)

    &nbsp;

  - [InternetConnect](win32inet.md#win32inetinternetconnect)

    Opens an FTP, Gopher, or HTTP session for a given site.&nbsp;

  - [InternetOpen](win32inet.md#win32inetinternetopen)

    Initializes an application's use of the Microsoft&#174 Win32&#174 Internet functions.&nbsp;

  - [InternetOpenUrl](win32inet.md#win32inetinternetopenurl)

    Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL.&nbsp;

  - [InternetCanonicalizeUrl](win32inet.md#win32inetinternetcanonicalizeurl)

    Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences.&nbsp;

  - [InternetGetLastResponseInfo](win32inet.md#win32inetinternetgetlastresponseinfo)

    Retrieves the last Win32&#174 Internet function error description or server response on the thread calling this function.&nbsp;

  - [InternetReadFile](win32inet.md#win32inetinternetreadfile)

    Reads data from a handle opened by the[win32inet::InternetOpenUrl](win32inet.md#win32inetinternetopenurl),[win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile), __win32inet::GopherOpenFile__ , or __win32inet::HttpOpenRequest__ function.&nbsp;

  - [InternetWriteFile](win32inet.md#win32inetinternetwritefile)

    Writes data to a handle opened by[win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile).&nbsp;

  - [FtpOpenFile](win32inet.md#win32inetftpopenfile)

    Initiates access to a remote file on an FTP server for reading or writing.&nbsp;

  - [FtpCommand](win32inet.md#win32inetftpcommand)

    Allows an application to send commands directly to an FTP server.&nbsp;

  - [InternetQueryOption](win32inet.md#win32inetinternetqueryoption)

    Retrieves an option for an internet handle&nbsp;

  - [InternetSetOption](win32inet.md#win32inetinternetsetoption)

    Sets an option for an internet handle&nbsp;

  - [FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

    Initiates an enumeration of the browser cache&nbsp;

  - [FindNextUrlCacheEntry](win32inet.md#win32inetfindnexturlcacheentry)

    Continues enumeration of cached files&nbsp;

  - [FindFirstUrlCacheEntryEx](win32inet.md#win32inetfindfirsturlcacheentryex)

    Initiates an enumeration of the browser cache&nbsp;

  - [FindNextUrlCacheEntryEx](win32inet.md#win32inetfindnexturlcacheentryex)

    Continues enumeration of cached files&nbsp;

  - [FindCloseUrlCache](win32inet.md#win32inetfindcloseurlcache)

    Closes a cache enumeration handle&nbsp;

  - [FindFirstUrlCacheGroup](win32inet.md#win32inetfindfirsturlcachegroup)

    Initiates enumeration of Url cache groups&nbsp;

  - [FindNextUrlCacheGroup](win32inet.md#win32inetfindnexturlcachegroup)

    Continues enumeration of cache groups&nbsp;

  - [GetUrlCacheEntryInfo](win32inet.md#win32inetgeturlcacheentryinfo)

    Retrieves cache info for a URL&nbsp;

  - [DeleteUrlCacheGroup](win32inet.md#win32inetdeleteurlcachegroup)

    Deletes a cache group&nbsp;

  - [CreateUrlCacheGroup](win32inet.md#win32inetcreateurlcachegroup)

    Creates a new cache group&nbsp;

  - [CreateUrlCacheEntry](win32inet.md#win32inetcreateurlcacheentry)

    Creates a cache entry for a URL&nbsp;

  - [CommitUrlCacheEntry](win32inet.md#win32inetcommiturlcacheentry)

    Commits a cache entry&nbsp;

  - [SetUrlCacheEntryGroup](win32inet.md#win32inetseturlcacheentrygroup)

    Associates a cache entry with a group&nbsp;

  - [GetUrlCacheGroupAttribute](win32inet.md#win32inetgeturlcachegroupattribute)

    Retrieves attributes for a cache group&nbsp;

  - [SetUrlCacheGroupAttribute](win32inet.md#win32inetseturlcachegroupattribute)

    Changes the attributes of a cache group&nbsp;

  - [DeleteUrlCacheEntry](win32inet.md#win32inetdeleteurlcacheentry)

    Deletes the cache entry for a URL&nbsp;

## [win32inet](#win32inet).CommitUrlCacheEntry

str = __CommitUrlCacheEntry( *UrlName*  *, LocalFileName*  *, ExpireTime*  *, LastModifiedTime*  *, CacheEntryType*  *, HeaderInfo*  *, OriginalUrl* __ )
Commits a cache entry

#### Parameters


  -  *UrlName* : str

    The Url for which to create an entry

  -  *LocalFileName* : str

    Filename returned from[win32inet::CreateUrlCacheEntry](win32inet.md#win32inetcreateurlcacheentry). 

Can be None when creating a history entry.

  -  *ExpireTime=None* :[PyTime](#pytime)

    Time at which entry expires

  -  *LastModifiedTime=None* :[PyTime](#pytime)

    Modification time of URL

  -  *CacheEntryType=NORMAL_CACHE_ENTRY* : int

    Combination of *_CACHE_ENTRY flags

  -  *HeaderInfo=None* : str

    Header data used to request Url

  -  *OriginalUrl=None* : str

    If redirected, original site requested

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *CommitUrlCacheEntry* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=commiturlcacheentry),[google](#http://www.google.com/search?q=commiturlcacheentry)or[google groups](#http://groups.google.com/groups?q=commiturlcacheentry).

## [win32inet](#win32inet).CreateUrlCacheEntry

str = __CreateUrlCacheEntry( *UrlName*  *, ExpectedFileSize*  *, FileExtension* __ )
Creates a cache entry for a URL

#### Parameters


  -  *UrlName* : str

    The Url for which to create an entry

  -  *ExpectedFileSize* : int

    Size of content, use 0 if unknown

  -  *FileExtension* : str

    Extension to use for filename

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *CreateUrlCacheEntry* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createurlcacheentry),[google](#http://www.google.com/search?q=createurlcacheentry)or[google groups](#http://groups.google.com/groups?q=createurlcacheentry).

#### Return Value
Returns the filename to which content should be written

## [win32inet](#win32inet).CreateUrlCacheGroup

long = __CreateUrlCacheGroup( *Flags* __ )
Creates a new cache group

#### Parameters


  -  *Flags=0* : int

    Combination of CACHEGROUP_FLAG_* flags

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *CreateUrlCacheGroup* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createurlcachegroup),[google](#http://www.google.com/search?q=createurlcachegroup)or[google groups](#http://groups.google.com/groups?q=createurlcachegroup).

## [win32inet](#win32inet).DeleteUrlCacheEntry

 __DeleteUrlCacheEntry( *UrlName* __ )
Deletes the cache entry for a URL

#### Parameters


  -  *UrlName* : str

    Cached url to be deleted

## [win32inet](#win32inet).DeleteUrlCacheGroup

 __DeleteUrlCacheGroup( *GroupId*  *, Attributes* __ )
Deletes a cache group

#### Parameters


  -  *GroupId* : int

    Group id

  -  *Attributes=CACHEGROUP_FLAG_FLUSHURL_ONDELETE* : int

    Combination of CACHEGROUP_FLAG_* flags

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *DeleteUrlCacheGroup* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=deleteurlcachegroup),[google](#http://www.google.com/search?q=deleteurlcachegroup)or[google groups](#http://groups.google.com/groups?q=deleteurlcachegroup).

## [win32inet](#win32inet).FindCloseUrlCache

 __FindCloseUrlCache( *EnumHandle* __ )
Closes a cache enumeration handle

#### Parameters


  -  *EnumHandle* :[PyUrlCacheHANDLE](#pyurlcachehandle)

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindCloseUrlCache* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findcloseurlcache),[google](#http://www.google.com/search?q=findcloseurlcache)or[google groups](#http://groups.google.com/groups?q=findcloseurlcache).

## [win32inet](#win32inet).FindFirstUrlCacheEntry

([PyUrlCacheHANDLE](#pyurlcachehandle), dict) = __FindFirstUrlCacheEntry( *SearchPattern* __ )
Initiates an enumeration of the browser cache

#### Parameters


  -  *SearchPattern=None* : str

    Type of entry to find, can be 'visited:', 'cookie:', or None

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindFirstUrlCacheEntry* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findfirsturlcacheentry),[google](#http://www.google.com/search?q=findfirsturlcacheentry)or[google groups](#http://groups.google.com/groups?q=findfirsturlcacheentry).

#### Return Value
Returns a handle that can be passed to[win32inet::FindNextUrlCacheEntry](win32inet.md#win32inetfindnexturlcacheentry), and a dict 

containing information for the first entry found.  Throws error code ERROR_NO_MORE_ITEMS 

if no items are found.

## [win32inet](#win32inet).FindFirstUrlCacheEntryEx

([PyUrlCacheHANDLE](#pyurlcachehandle), dict) = __FindFirstUrlCacheEntryEx( *SearchPattern*  *, Flags*  *, Filter*  *, GroupId* __ )
Initiates an enumeration of the browser cache

#### Parameters


  -  *SearchPattern=None* : str

    Type of entry to find, can be 'visited:', 'cookie:', or None

  -  *Flags=0* : int

    None currently defined

  -  *Filter=0* : int

    Types of entries to return, combination of *_CACHE_ENTRY values

  -  *GroupId=0* : int

    Cache group to enumerate, use 0 for all

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindFirstUrlCacheEntryEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findfirsturlcacheentryex),[google](#http://www.google.com/search?q=findfirsturlcacheentryex)or[google groups](#http://groups.google.com/groups?q=findfirsturlcacheentryex).

#### Return Value
Returns a handle that can be passed to[win32inet::FindNextUrlCacheEntry](win32inet.md#win32inetfindnexturlcacheentry), and a dict 

containing information for the first entry found.  Throws error code ERROR_NO_MORE_ITEMS 

if no items are found.

## [win32inet](#win32inet).FindFirstUrlCacheGroup

([PyUrlCacheHANDLE](#pyurlcachehandle), int) = __FindFirstUrlCacheGroup( *Filter* __ )
Initiates enumeration of Url cache groups

#### Parameters


  -  *Filter=CACHEGROUP_SEARCH_ALL* : int

    CACHEGROUP_SEARCH_*

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindFirstUrlCacheGroup* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findfirsturlcachegroup),[google](#http://www.google.com/search?q=findfirsturlcachegroup)or[google groups](#http://groups.google.com/groups?q=findfirsturlcachegroup).

#### Return Value
Returns a handle that can be passed to[win32inet::FindNextUrlCacheGroup](win32inet.md#win32inetfindnexturlcachegroup), and the id 

of the first group found.

## [win32inet](#win32inet).FindNextUrlCacheEntry

dict = __FindNextUrlCacheEntry( *EnumHandle* __ )
Continues enumeration of cached files

#### Parameters


  -  *EnumHandle* :[PyUrlCacheHANDLE](#pyurlcachehandle)

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindNextUrlCacheEntry* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findnexturlcacheentry),[google](#http://www.google.com/search?q=findnexturlcacheentry)or[google groups](#http://groups.google.com/groups?q=findnexturlcacheentry).

#### Return Value
Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

## [win32inet](#win32inet).FindNextUrlCacheEntryEx

dict = __FindNextUrlCacheEntryEx( *EnumHandle* __ )
Continues enumeration of cached files

#### Parameters


  -  *EnumHandle* :[PyUrlCacheHANDLE](#pyurlcachehandle)

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntryEx](win32inet.md#win32inetfindfirsturlcacheentryex)

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindNextUrlCacheEntryEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findnexturlcacheentryex),[google](#http://www.google.com/search?q=findnexturlcacheentryex)or[google groups](#http://groups.google.com/groups?q=findnexturlcacheentryex).

#### Return Value
Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

## [win32inet](#win32inet).FindNextUrlCacheGroup

int = __FindNextUrlCacheGroup( *Find* __ )
Continues enumeration of cache groups

#### Parameters


  -  *Find* :[PyHANDLE](#pyhandle)

    Group enumeration handle as returned by[win32inet::FindFirstUrlCacheGroup](win32inet.md#win32inetfindfirsturlcachegroup)

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *FindNextUrlCacheGroup* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findnexturlcachegroup),[google](#http://www.google.com/search?q=findnexturlcachegroup)or[google groups](#http://groups.google.com/groups?q=findnexturlcachegroup).

## [win32inet](#win32inet).FtpCommand

[PyHINTERNET](#pyhinternet)= __FtpCommand( *Connect*  *, ExpectResponse*  *, Flags*  *, Command*  *, Context* __ )
Allows an application to send commands directly to an FTP server.

#### Parameters


  -  *Connect* :[PyHINTERNET](#pyhinternet)

    Valid HINTERNET&#09handle to an FTP session.

  -  *ExpectResponse* : bool

    Boolean value&#09that indicates whether or not 

the application expects a response&#09from the FTP server. 

This must be set to True if a response&#09is expected, or&#09False otherwise.

  -  *Flags* : int

    Unsigned long integer value that contains the flags that 

control this function. This can be set to&#09either FTP_TRANSFER_TYPE_ASCII or 

FTP_TRANSFER_TYPE_BINARY

  -  *Command* : string

    The command to send to the FTP server.

  -  *Context=None* : object

    Arbitrary object&#09to be passed to&#09callback

#### Comments
This function may cause a crash on 32-bit XP and Vista due to an internal error in win32inet.dll.
Accepts keyword args

## [win32inet](#win32inet).FtpOpenFile

[PyHINTERNET](#pyhinternet)= __FtpOpenFile( *hConnect*  *, FileName*  *, Access*  *, Flags*  *, Context* __ )
Initiates access to a remote file on an FTP server for reading or writing.

#### Parameters


  -  *hConnect* :[PyHINTERNET](#pyhinternet)

    Valid HINTERNET handle to an FTP session.

  -  *FileName* : string

    The name of the file to access on the remote system.

  -  *Access* : int

    Integer value that determines how the file will be accessed. This can be GENERIC_READ or GENERIC_WRITE, but not both.

  -  *Flags* : int

    Integer value that contains the conditions under which the 

transfers occur. The application should select one transfer type and 

any of the flags that indicate how the caching of the file will be 

controlled.  The transfer type can be one of the FTP_TRANSFER_TYPE* values

  -  *Context=None* : object

    Arbitrary object that will be passed to handle's callback function

#### Comments
Accepts keyword args

## [win32inet](#win32inet).GetUrlCacheEntryInfo

dict = __GetUrlCacheEntryInfo( *UrlName* __ )
Retrieves cache info for a URL

#### Parameters


  -  *UrlName* : str

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *GetUrlCacheEntryInfo* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=geturlcacheentryinfo),[google](#http://www.google.com/search?q=geturlcacheentryinfo)or[google groups](#http://groups.google.com/groups?q=geturlcacheentryinfo).

#### Return Value
Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

## [win32inet](#win32inet).GetUrlCacheGroupAttribute

dict = __GetUrlCacheGroupAttribute( *GroupId*  *, Attributes* __ )
Retrieves attributes for a cache group

#### Parameters


  -  *GroupId* : int

    Group id

  -  *Attributes=CACHEGROUP_ATTRIBUTE_GET_ALL* : int

    Attributes to retrieve, CACHEGROUP_ATTRIBUTE_*

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *GetUrlCacheGroupAttribute* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=geturlcachegroupattribute),[google](#http://www.google.com/search?q=geturlcachegroupattribute)or[google groups](#http://groups.google.com/groups?q=geturlcachegroupattribute).

#### Return Value
Returns a dict representing a INTERNET_CACHE_GROUP_INFO struct

## [win32inet](#win32inet).InternetAttemptConnect

 __InternetAttemptConnect( *Reserved* __ )
Attempts to make a connection to the Internet.

#### Parameters


  -  *Reserved=0* : int

    Use only 0.

## [win32inet](#win32inet).InternetCanonicalizeUrl

string = __InternetCanonicalizeUrl( *url*  *, flags* __ )
Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences.

#### Parameters


  -  *url* : string

    The URL to canonicalize.

  -  *flags=0* : int

    integer value that contains the flags that control 

canonicalization. This can be one of the following values:

## [win32inet](#win32inet).InternetCheckConnection

 __InternetCheckConnection( *Url*  *, Flags*  *, Reserved* __ )
Allows an application to check if a connection to the Internet can be established

#### Parameters


  -  *Url* : string

    Url to attempt to connect to, can be None

  -  *Flags=0* : int

    FLAG_ICC_FORCE_CONNECTION is only defined flag

  -  *Reserved=0* : int

    Use only 0.

## [win32inet](#win32inet).InternetCloseHandle

 __InternetCloseHandle( *handle* __ )


#### Parameters


  -  *handle* :[PyHINTERNET](#pyhinternet)

    

#### Comments
It should not be necessary to call this function - all handles are[PyHINTERNET](#pyhinternet)objects, so can have their Close method called, and will 

otherwise be automatically closed.

## [win32inet](#win32inet).InternetConnect

 __InternetConnect( *Internet*  *, ServerName*  *, ServerPort*  *, Username*  *, Password*  *, Service*  *, Flags*  *, Context* __ )
Opens an FTP, Gopher, or HTTP session for a given site.

#### Parameters


  -  *Internet* :[PyHINTERNET](#pyhinternet)

    Valid HINTERNET handle returned by a previous call to[win32inet::InternetOpen](win32inet.md#win32inetinternetopen).

  -  *ServerName* : string

    A string that contains the host name of an Internet 

server. Alternately, the string can contain the IP number of the site, 

in ASCII dotted-decimal format (for example, 11.0.1.45).

  -  *ServerPort* : int

    Number of the TCP/IP port on the server to connect to. 

These flags set only the port that will be used. The service is set by 

the value of dwService. This can be one of the INTERNET_DEFAULT_*_PORT 

constants or INTERNET_INVALID_PORT_NUMBER, which uses the default 

port for the service specified by dwService.

  -  *Username* : string

    A string that contains the name of the user 

to log on. If this parameter is&#09None, the function uses&#09an appropriate 

default, except&#09for&#09HTTP; a&#09NULL parameter in HTTP causes the server 

to return an error.&#09For&#09the&#09FTP&#09protocol, the default is "anonymous".

  -  *Password* : string

    Address&#09of a null-terminated string&#09that 

contains the password to use to&#09log&#09on.&#09If both&#09Password 

and&#09Username are None, the function&#09uses the default 

"anonymous"&#09password. In the case of FTP, the default password 

is the user's e-mail name. If lpszPassword is None,&#09but&#09lpszUsername 

is not None, the function uses a blank password.

  -  *Service* : int

    Iinteger value that contains the type&#09of service to 

access.&#09This can be&#09one&#09of INTERNET_SERVICE_FTP, INTERNET_SERVICE_GOPHER, 

or INTERNET_SERVICE_HTTP.

  -  *Flags* : int

    Integer value that contains the flags specific to 

the&#09service&#09used. When the value of&#09dwService is INTERNET_SERVICE_FTP, 

INTERNET_FLAG_PASSIVE causes the application to&#09use&#09passive&#09FTP&#09semantics.

  -  *Context=None* : object

    Arbitrary object to be passed to callback function

#### Comments
Accepts keyword args

## [win32inet](#win32inet).InternetGetCookie

string = __InternetGetCookie( *Url*  *, CookieName* __ )
Retrieves the cookie for the specified URL

#### Parameters


  -  *Url* : string

    Site for which to retrieve cookie

  -  *CookieName* : string

    Name of cookie (documented on MSDN as not implemented)

## [win32inet](#win32inet).InternetGetLastResponseInfo

int, string = __InternetGetLastResponseInfo(__ )
Retrieves the last Win32&#174 Internet function error description or server response on the thread calling this function.

## [win32inet](#win32inet).InternetGoOnline

 __InternetGoOnline( *Url*  *, Parent*  *, Flags* __ )
Prompts the user for permission to initiate connection to a URL.

#### Parameters


  -  *Url* : string

    Web site to connect to

  -  *Parent=None* : int

    Handle to parent window

  -  *Flags=0* : int

    INTERNET_GOONLINE_REFRESH is only available flag

## [win32inet](#win32inet).InternetOpen

 __InternetOpen( *agent*  *, proxyName*  *, proxyBypass*  *, flags* __ )
Initializes an application's use of the Microsoft&#174 Win32&#174 Internet functions.

#### Parameters


  -  *agent* : string

    A string that contains the name of the application 

or entity calling the Internet functions. This name is used as the user 

agent in the HTTP protocol.

  -  *proxyName* : string

    

  -  *proxyBypass* : string

    

  -  *flags* : int

    Combination of INTERNET_FLAG_ASYNC,INTERNET_FLAG_FROM_CACHE, or INTERNET_FLAG_OFFLINE

## [win32inet](#win32inet).InternetOpenUrl

[PyHINTERNET](#pyhinternet)= __InternetOpenUrl( *Internet*  *, Url*  *, Headers*  *, Flags*  *, Context* __ )
Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL.

#### Parameters


  -  *Internet* :[PyHINTERNET](#pyhinternet)

    Internet handle as returned by[win32inet::InternetOpen](win32inet.md#win32inetinternetopen)

  -  *Url* : string

    A string that contains the URL to begin reading.  Only URLs beginning with ftp:, gopher:, http:, or https: are supported.

  -  *Headers=None* : string

    a string&#09variable that contains the headers to be sent to the HTTP server.

  -  *Flags=0* : int

    INTERNET_FLAG_*

  -  *Context=None* : object

    An arbitrary object to be passed to the status callback function

#### Comments
Accepts keyword args.

#### Return Value
Returns None in async mode (Internet handle created with INTERNET_FLAG_ASYNC). 

When handle is created, it will be passed to callback function of parent handle.

## [win32inet](#win32inet).InternetQueryOption

object = __InternetQueryOption( *hInternet*  *, Option* __ )
Retrieves an option for an internet handle

#### Parameters


  -  *hInternet* :[PyHINTERNET](#pyhinternet)

    Internet handle, or None for global defaults

  -  *Option* : int

    INTERNET_OPTION_* value

 __Option__  __Returned type__ INTERNET_OPTION_CALLBACKPython callback functionINTERNET_OPTION_CONTEXT_VALUEContext objectINTERNET_OPTION_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CODEPAGEInt - Codepage of host part of URLINTERNET_OPTION_CODEPAGE_PATHInt - Codepage for URLINTERNET_OPTION_CODEPAGE_EXTRAInt - Codepage for path part of URLINTERNET_OPTION_CONNECT_RETRIESInt - Number of time to try to reconnect to hostINTERNET_OPTION_CONNECT_TIMEOUTInt - Connection timeout in millisecondsINTERNET_OPTION_CONNECTED_STATEInt - Connection state, INTERNET_STATE_*INTERNET_OPTION_HANDLE_TYPEInt, INTERNET_HANDLE_TYPE_*INTERNET_OPTION_ERROR_MASKInt, combination of INTERNET_ERROR_MASK_*INTERNET_OPTION_EXTENDED_ERRORInt, ERROR_INTERNET_*INTERNET_OPTION_FROM_CACHE_TIMEOUTInt - Timeout in ms before cached copy is usedINTERNET_OPTION_IDNInt, INTERNET_FLAG_IDN_*INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVERIntINTERNET_OPTION_MAX_CONNS_PER_SERVERIntINTERNET_OPTION_READ_BUFFER_SIZEIntINTERNET_OPTION_WRITE_BUFFER_SIZEIntINTERNET_OPTION_REQUEST_FLAGSInt, combination of INTERNET_REQFLAG_*INTERNET_OPTION_REQUEST_PRIORITYIntINTERNET_OPTION_SECURITY_FLAGSInt, SECURITY_FLAG_*INTERNET_OPTION_SECURITY_KEY_BITNESSIntINTERNET_OPTION_BYPASS_EDITED_ENTRYBooleanINTERNET_OPTION_HTTP_DECODINGBooleanINTERNET_OPTION_IGNORE_OFFLINEBooleanINTERNET_OPTION_DATAFILE_NAMEString - Name of internet cache fileINTERNET_OPTION_USERNAMEString - Username passed to InternetConnectINTERNET_OPTION_PASSWORDString - Password passed to InternetConnectINTERNET_OPTION_PROXY_PASSWORDStringINTERNET_OPTION_PROXY_USERNAMEStringINTERNET_OPTION_SECONDARY_CACHE_KEYStringINTERNET_OPTION_SECURITY_CERTIFICATEStringINTERNET_OPTION_URLStringINTERNET_OPTION_USER_AGENTStringINTERNET_OPTION_CACHE_TIMESTAMPSdict - Expiration and last modified timesINTERNET_OPTION_HTTP_VERSIONdict - HTTP_VERSION_INFOINTERNET_OPTION_VERSIONdict - INTERNET_VERSION_INFOINTERNET_OPTION_PARENT_HANDLE[PyHINTERNET](#pyhinternet)INTERNET_OPTION_PROXYdict - INTERNET_PROXY_INFOINTERNET_OPTION_DIAGNOSTIC_SOCKET_INFONot yet supported (INTERNET_DIAGNOSTIC_SOCKET_INFO)INTERNET_OPTION_PER_CONNECTION_OPTIONNot yet supported (INTERNET_PER_CONN_OPTION_LIST)INTERNET_OPTION_SECURITY_CERTIFICATE_STRUCTNot yet supported (INTERNET_CERTIFICATE_INFO)INTERNET_OPTION_ALTER_IDENTITYNot supportedINTERNET_OPTION_ASYNCNot supportedINTERNET_OPTION_ASYNC_IDNot supportedINTERNET_OPTION_ASYNC_PRIORITYNot supportedINTERNET_OPTION_CACHE_STREAM_HANDLENot supportedINTERNET_OPTION_CALLBACK_FILTERNot supportedINTERNET_OPTION_CLIENT_CERT_CONTEXTNot supportedINTERNET_OPTION_DATA_RECEIVE_TIMEOUTNot supportedINTERNET_OPTION_DATA_SEND_TIMEOUTNot supportedINTERNET_OPTION_CONNECT_BACKOFFNot supportedINTERNET_OPTION_CONNECT_TIMENot supportedINTERNET_OPTION_DISABLE_AUTODIALNot supportedINTERNET_OPTION_DISCONNECTED_TIMEOUTNot supportedINTERNET_OPTION_IDENTITYNot supportedINTERNET_OPTION_IDLE_STATENot supportedINTERNET_OPTION_KEEP_CONNECTIONNot supportedINTERNET_OPTION_LISTEN_TIMEOUTNot supportedINTERNET_OPTION_OFFLINE_MODENot supportedINTERNET_OPTION_OFFLINE_SEMANTICSNot supportedINTERNET_OPTION_POLICYNot supportedINTERNET_OPTION_RECEIVE_THROUGHPUTNot supportedINTERNET_OPTION_REMOVE_IDENTITYNot supportedINTERNET_OPTION_SEND_THROUGHPUTNot supportedINTERNET_OPTION_DATAFILE_EXTOnly valid for InternetSetOptionINTERNET_OPTION_DIGEST_AUTH_UNLOADOnly valid for InternetSetOptionINTERNET_OPTION_END_BROWSER_SESSIONOnly valid for InternetSetOptionINTERNET_OPTION_REFRESHOnly valid for InternetSetOptionINTERNET_OPTION_RESET_URLCACHE_SESSIONOnly valid for InternetSetOptionINTERNET_OPTION_SETTINGS_CHANGEDOnly valid for InternetSetOption
#### Win32 API References


  - Search for *InternetQueryOption* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=internetqueryoption),[google](#http://www.google.com/search?q=internetqueryoption)or[google groups](#http://groups.google.com/groups?q=internetqueryoption).

#### Return Value
The type of object returned is dependent on the option requested

## [win32inet](#win32inet).InternetReadFile

string = __InternetReadFile( *hInternet*  *, size* __ )
Reads data from a handle opened by the[win32inet::InternetOpenUrl](win32inet.md#win32inetinternetopenurl),[win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile), __win32inet::GopherOpenFile__ , or __win32inet::HttpOpenRequest__ function.

#### Parameters


  -  *hInternet* :[PyHINTERNET](#pyhinternet)

    

  -  *size* : int

    Number of bytes to read.

#### Return Value
The result will be a string of zero bytes when the end is reached.

## [win32inet](#win32inet).InternetSetCookie

 __InternetSetCookie( *url*  *, lpszCookieName*  *, data* __ )
Creates a cookie associated with the specified URL.

#### Parameters


  -  *url* : string

    

  -  *lpszCookieName* : string

    

  -  *data* : string

    

## [win32inet](#win32inet).InternetSetOption

 __InternetSetOption( *hInternet*  *, Option*  *, Buffer* __ )
Sets an option for an internet handle

#### Parameters


  -  *hInternet* :[PyHINTERNET](#pyhinternet)

    Internet handle, or None for global defaults

  -  *Option* : int

    The option to set, INTERNET_OPTION_*

  -  *Buffer* : object

    Type is dependent on Option

 __Option__  __Type of input object__ INTERNET_OPTION_CALLBACKPython function called on status changeINTERNET_OPTION_CONTEXT_VALUEAny Python object to be passed to callback functionINTERNET_OPTION_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CODEPAGEInt - Codepage of host part of URLINTERNET_OPTION_CODEPAGE_PATHCodepage for URLINTERNET_OPTION_CODEPAGE_EXTRAInt - Codepage for path part of URLINTERNET_OPTION_CONNECT_RETRIESInt - Number of time to try to reconnect to hostINTERNET_OPTION_CONNECT_TIMEOUTInt - Connection timeout in millisecondsINTERNET_OPTION_CONNECTED_STATEInt - Connection state, INTERNET_STATE_*INTERNET_OPTION_ERROR_MASKInt, combination of INTERNET_ERROR_MASK_*INTERNET_OPTION_FROM_CACHE_TIMEOUTInt - Timeout in ms before cached copy is usedINTERNET_OPTION_IDNInt, INTERNET_FLAG_IDN_*INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVERIntINTERNET_OPTION_MAX_CONNS_PER_SERVERIntINTERNET_OPTION_READ_BUFFER_SIZEIntINTERNET_OPTION_WRITE_BUFFER_SIZEIntINTERNET_OPTION_REQUEST_PRIORITYIntINTERNET_OPTION_DIGEST_AUTH_UNLOADNoneINTERNET_OPTION_END_BROWSER_SESSIONNoneINTERNET_OPTION_REFRESHNoneINTERNET_OPTION_RESET_URLCACHE_SESSIONNoneINTERNET_OPTION_SETTINGS_CHANGEDNoneINTERNET_OPTION_BYPASS_EDITED_ENTRYBooleanINTERNET_OPTION_HTTP_DECODINGBooleanINTERNET_OPTION_IGNORE_OFFLINEBooleanINTERNET_OPTION_USERNAMEString - Username passed to InternetConnectINTERNET_OPTION_PASSWORDString - Password passed to InternetConnectINTERNET_OPTION_PROXY_PASSWORDStringINTERNET_OPTION_PROXY_USERNAMEStringINTERNET_OPTION_SECONDARY_CACHE_KEYStringINTERNET_OPTION_USER_AGENTStringINTERNET_OPTION_DATAFILE_EXTString - Extension to use for download cache fileINTERNET_OPTION_PROXYDict representing INTERNET_PROXY_INFO structINTERNET_OPTION_HTTP_VERSIONNot yet supported - HTTP_VERSION_INFOINTERNET_OPTION_PER_CONNECTION_OPTIONNot yet supported (INTERNET_PER_CONN_OPTION_LIST)INTERNET_OPTION_ALTER_IDENTITYNot supportedINTERNET_OPTION_ASYNCNot supportedINTERNET_OPTION_ASYNC_IDNot supportedINTERNET_OPTION_ASYNC_PRIORITYNot supportedINTERNET_OPTION_CACHE_STREAM_HANDLENot supportedINTERNET_OPTION_CALLBACK_FILTERNot supportedINTERNET_OPTION_CLIENT_CERT_CONTEXTNot supportedINTERNET_OPTION_DATA_RECEIVE_TIMEOUTNot supportedINTERNET_OPTION_DATA_SEND_TIMEOUTNot supportedINTERNET_OPTION_CONNECT_BACKOFFNot supportedINTERNET_OPTION_CONNECT_TIMENot supportedINTERNET_OPTION_DISABLE_AUTODIALNot supportedINTERNET_OPTION_DISCONNECTED_TIMEOUTNot supportedINTERNET_OPTION_IDENTITYNot supportedINTERNET_OPTION_IDLE_STATENot supportedINTERNET_OPTION_KEEP_CONNECTIONNot supportedINTERNET_OPTION_LISTEN_TIMEOUTNot supportedINTERNET_OPTION_OFFLINE_MODENot supportedINTERNET_OPTION_OFFLINE_SEMANTICSNot supportedINTERNET_OPTION_POLICYNot supportedINTERNET_OPTION_RECEIVE_THROUGHPUTNot supportedINTERNET_OPTION_REMOVE_IDENTITYNot supportedINTERNET_OPTION_SEND_THROUGHPUTNot supportedINTERNET_OPTION_CACHE_TIMESTAMPSOnly valid for InternetQueryOptionINTERNET_OPTION_HANDLE_TYPEOnly valid for InternetQueryOptionINTERNET_OPTION_DATAFILE_NAMEOnly valid for InternetQueryOptionINTERNET_OPTION_PARENT_HANDLEOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_CERTIFICATEOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_CERTIFICATE_STRUCTOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_FLAGSOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_KEY_BITNESSOnly valid for InternetQueryOptionINTERNET_OPTION_DIAGNOSTIC_SOCKET_INFOOnly valid for InternetQueryOptionINTERNET_OPTION_VERSIONOnly valid for InternetQueryOptionINTERNET_OPTION_EXTENDED_ERROROnly valid for InternetQueryOptionINTERNET_OPTION_REQUEST_FLAGSOnly valid for InternetQueryOptionINTERNET_OPTION_URLOnly valid for InternetQueryOption
#### Win32 API References


  - Search for *InternetSetOption* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=internetsetoption),[google](#http://www.google.com/search?q=internetsetoption)or[google groups](#http://groups.google.com/groups?q=internetsetoption).

## [win32inet](#win32inet).InternetWriteFile

int = __InternetWriteFile( *File*  *, Buffer* __ )
Writes data to a handle opened by[win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile).

#### Parameters


  -  *File* :[PyHINTERNET](#pyhinternet)

    Writeable internet&#09handle

  -  *Buffer* : string

    String or&#09buffer containing data to be written

## [win32inet](#win32inet).SetUrlCacheEntryGroup

 __SetUrlCacheEntryGroup( *UrlName*  *, Flags*  *, GroupId* __ )
Associates a cache entry with a group

#### Parameters


  -  *UrlName* : str

    Url whose cache is to be added to the group

  -  *Flags* : int

    INTERNET_CACHE_GROUP_ADD or INTERNET_CACHE_GROUP_REMOVE

  -  *GroupId* : int

    Id of a cache group

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *SetUrlCacheEntryGroup* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=seturlcacheentrygroup),[google](#http://www.google.com/search?q=seturlcacheentrygroup)or[google groups](#http://groups.google.com/groups?q=seturlcacheentrygroup).

## [win32inet](#win32inet).SetUrlCacheGroupAttribute

 __SetUrlCacheGroupAttribute( *GroupId*  *, Attributes*  *, GroupInfo*  *, Flags* __ )
Changes the attributes of a cache group

#### Parameters


  -  *GroupId* : int

    Id of a cache group

  -  *Attributes* : int

    Bitmask of CACHEGROUP_ATTRIBUTE_* flags indicating which attributes to set

  -  *GroupInfo* : dict

    INTERNET_CACHE_GROUP_INFO dict as returned by[win32inet::GetUrlCacheGroupAttribute](win32inet.md#win32inetgeturlcachegroupattribute)

  -  *Flags=0* : int

    Reserved, use 0

#### Comments
Accepts keyword args

#### Win32 API References


  - Search for *SetUrlCacheGroupAttribute* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=seturlcachegroupattribute),[google](#http://www.google.com/search?q=seturlcachegroupattribute)or[google groups](#http://groups.google.com/groups?q=seturlcachegroupattribute).

## [win32inet](#win32inet).WinHttpGetDefaultProxyConfiguration

[PyWINHTTP_PROXY_INFO](PyWINHTTP.md#pywinhttpproxy_info)= __WinHttpGetDefaultProxyConfiguration(__ )
Retrieves the default WinHTTP proxy configuration from the registry.

## [win32inet](#win32inet).WinHttpGetIEProxyConfigForCurrentUser

tuple = __WinHttpGetIEProxyConfigForCurrentUser(__ )
Obtains 

the Internet Explorer proxy configuration for the current user.

#### Win32 API References


  - Search for *WinHttpGetIEProxyConfigForCurrentUser* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=winhttpgetieproxyconfigforcurrentuser),[google](#http://www.google.com/search?q=winhttpgetieproxyconfigforcurrentuser)or[google groups](#http://groups.google.com/groups?q=winhttpgetieproxyconfigforcurrentuser).

  - Search for *WINHTTP_CURRENT_USER_IE_PROXY_CONFIG* at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WINHTTP.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=winhttpcurrent_user_ie_proxy_config),[google](http://www.google.com/search?q=WINHTTP.md#http://www.google.com/search?q=winhttpcurrent_user_ie_proxy_config)or[google groups](http://groups.google.com/groups?q=WINHTTP.md#http://groups.google.com/groups?q=winhttpcurrent_user_ie_proxy_config).

#### Return Value
The result is a windows WINHTTP_CURRENT_USER_IE_PROXY_CONFIG 

structure; a tuple of an int (bool) and 3 unicode strings 

(fAutoDetect, lpszAutoConfigUrl, lpszProxy, lpszProxyBypass).

## [win32inet](#win32inet).WinHttpGetProxyForUrl

[PyWINHTTP_PROXY_INFO](PyWINHTTP.md#pywinhttpproxy_info)= __WinHttpGetProxyForUrl( *handle*  *, url*  *, options* __ )
Obtains 

the Internet Explorer proxy configuration for the specified URL.

#### Parameters


  -  *handle* : __HANDLE__ /int

    

  -  *url* : unicode/string

    

  -  *options* :[PyWINHTTP_AUTOPROXY_OPTIONS](PyWINHTTP.md#pywinhttpautoproxy_options)

    

## [win32inet](#win32inet).WinHttpOpen

[PyHINTERNET](#pyhinternet)= __WinHttpOpen( *lpszUserAgent*  *, dwAccessType*  *, lpszProxyName*  *, lpszProxyBypass*  *, dwFlags* __ )
Opens a winhttp session.

#### Parameters


  -  *lpszUserAgent* : string

    

  -  *dwAccessType* : int

    

  -  *lpszProxyName* : string

    

  -  *lpszProxyBypass* : string

    

  -  *dwFlags* : int

    

#### Win32 API References


  - Search for *WinHttpOpen* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=winhttpopen),[google](#http://www.google.com/search?q=winhttpopen)or[google groups](#http://groups.google.com/groups?q=winhttpopen).