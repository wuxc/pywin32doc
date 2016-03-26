# win32inet


## Module win32inet

An interface to the Windows internet \(wininet\) API

#### Methods

  - [InternetSetCookie](win32inet.md#win32inetinternetsetcookie)

    Creates a cookie associated with the specified URL\.&nbsp;

  - [InternetGetCookie](win32inet.md#win32inetinternetgetcookie)

    Retrieves the cookie for the specified URL&nbsp;

  - [InternetAttemptConnect](win32inet.md#win32inetinternetattemptconnect)

    Attempts to make a connection to the Internet\.&nbsp;

  - [InternetCheckConnection](win32inet.md#win32inetinternetcheckconnection)

    Allows an application to check if a connection to the Internet can be established&nbsp;

  - [InternetGoOnline](win32inet.md#win32inetinternetgoonline)

    Prompts the user for permission to initiate connection to a URL\.&nbsp;

  - [InternetCloseHandle](win32inet.md#win32inetinternetclosehandle)

    &nbsp;

  - [InternetConnect](win32inet.md#win32inetinternetconnect)

    Opens an FTP, Gopher, or HTTP session for a given site\.&nbsp;

  - [InternetOpen](win32inet.md#win32inetinternetopen)

    Initializes an application's use of the Microsoft&\#174 Win32&\#174 Internet functions\.&nbsp;

  - [InternetOpenUrl](win32inet.md#win32inetinternetopenurl)

    Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL\.&nbsp;

  - [InternetCanonicalizeUrl](win32inet.md#win32inetinternetcanonicalizeurl)

    Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences\.&nbsp;

  - [InternetGetLastResponseInfo](win32inet.md#win32inetinternetgetlastresponseinfo)

    Retrieves the last Win32&\#174 Internet function error description or server response on the thread calling this function\.&nbsp;

  - [InternetReadFile](win32inet.md#win32inetinternetreadfile)

    Reads data from a handle opened by the 

[win32inet::InternetOpenUrl](win32inet.md#win32inetinternetopenurl), [win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile), 

win32inet::GopherOpenFile

, or win32inet::HttpOpenRequest

 function\.&nbsp;

  - [InternetWriteFile](win32inet.md#win32inetinternetwritefile)

    Writes data to a handle opened by [win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile)\.&nbsp;

  - [FtpOpenFile](win32inet.md#win32inetftpopenfile)

    Initiates access to a remote file on an FTP server for reading or writing\.&nbsp;

  - [FtpCommand](win32inet.md#win32inetftpcommand)

    Allows an application to send commands directly to an FTP server\.&nbsp;

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


## [win32inet](win32inet.md#win32inet)\.CommitUrlCacheEntry

str = CommitUrlCacheEntry\(UrlName, LocalFileName

, ExpireTime

, LastModifiedTime

, CacheEntryType

, HeaderInfo

, OriginalUrl

\)
Commits a cache entry

#### Parameters

  - UrlName : str

    The Url for which to create an entry

  - LocalFileName : str

    Filename returned from [win32inet::CreateUrlCacheEntry](win32inet.md#win32inetcreateurlcacheentry)\. 

Can be None when creating a history entry\.

  - ExpireTime=None : [PyTime](PyTime.md)

    Time at which entry expires

  - LastModifiedTime=None : [PyTime](PyTime.md)

    Modification time of URL

  - CacheEntryType=NORMAL\_CACHE\_ENTRY : int

    Combination of \*\_CACHE\_ENTRY flags

  - HeaderInfo=None : str

    Header data used to request Url

  - OriginalUrl=None : str

    If redirected, original site requested

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for CommitUrlCacheEntry at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CommitUrlCacheEntry.md), [google](http://www.google.com/search?q=CommitUrlCacheEntry.md) or [google groups](http://groups.google.com/groups?q=CommitUrlCacheEntry.md)\.


## [win32inet](win32inet.md#win32inet)\.CreateUrlCacheEntry

str = CreateUrlCacheEntry\(UrlName, ExpectedFileSize

, FileExtension

\)
Creates a cache entry for a URL

#### Parameters

  - UrlName : str

    The Url for which to create an entry

  - ExpectedFileSize : int

    Size of content, use 0 if unknown

  - FileExtension : str

    Extension to use for filename

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for CreateUrlCacheEntry at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateUrlCacheEntry.md), [google](http://www.google.com/search?q=CreateUrlCacheEntry.md) or [google groups](http://groups.google.com/groups?q=CreateUrlCacheEntry.md)\.

#### Return Value
Returns the filename to which content should be written


## [win32inet](win32inet.md#win32inet)\.CreateUrlCacheGroup

long = CreateUrlCacheGroup\(Flags\)
Creates a new cache group

#### Parameters

  - Flags=0 : int

    Combination of CACHEGROUP\_FLAG\_\* flags

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for CreateUrlCacheGroup at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateUrlCacheGroup.md), [google](http://www.google.com/search?q=CreateUrlCacheGroup.md) or [google groups](http://groups.google.com/groups?q=CreateUrlCacheGroup.md)\.


## [win32inet](win32inet.md#win32inet)\.DeleteUrlCacheEntry

DeleteUrlCacheEntry\(UrlName\)
Deletes the cache entry for a URL

#### Parameters

  - UrlName : str

    Cached url to be deleted


## [win32inet](win32inet.md#win32inet)\.DeleteUrlCacheGroup

DeleteUrlCacheGroup\(GroupId, Attributes\)
Deletes a cache group

#### Parameters

  - GroupId : int

    Group id

  - Attributes=CACHEGROUP\_FLAG\_FLUSHURL\_ONDELETE : int

    Combination of CACHEGROUP\_FLAG\_\* flags

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for DeleteUrlCacheGroup at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteUrlCacheGroup.md), [google](http://www.google.com/search?q=DeleteUrlCacheGroup.md) or [google groups](http://groups.google.com/groups?q=DeleteUrlCacheGroup.md)\.


## [win32inet](win32inet.md#win32inet)\.FindCloseUrlCache

FindCloseUrlCache\(EnumHandle\)
Closes a cache enumeration handle

#### Parameters

  - EnumHandle : [PyUrlCacheHANDLE](PyUrlCacheHANDLE.md)

    Cache enumeration handle as returned by [win32inet::FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindCloseUrlCache at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindCloseUrlCache.md), [google](http://www.google.com/search?q=FindCloseUrlCache.md) or [google groups](http://groups.google.com/groups?q=FindCloseUrlCache.md)\.


## [win32inet](win32inet.md#win32inet)\.FindFirstUrlCacheEntry

\([PyUrlCacheHANDLE](PyUrlCacheHANDLE.md), dict\) = FindFirstUrlCacheEntry\(SearchPattern\)
Initiates an enumeration of the browser cache

#### Parameters

  - SearchPattern=None : str

    Type of entry to find, can be 'visited:', 'cookie:', or None

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindFirstUrlCacheEntry at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstUrlCacheEntry.md), [google](http://www.google.com/search?q=FindFirstUrlCacheEntry.md) or [google groups](http://groups.google.com/groups?q=FindFirstUrlCacheEntry.md)\.

#### Return Value
Returns a handle that can be passed to [win32inet::FindNextUrlCacheEntry](win32inet.md#win32inetfindnexturlcacheentry), and a dict 

containing information for the first entry found\.  Throws error code ERROR\_NO\_MORE\_ITEMS 

if no items are found\.


## [win32inet](win32inet.md#win32inet)\.FindFirstUrlCacheEntryEx

\([PyUrlCacheHANDLE](PyUrlCacheHANDLE.md), dict\) = FindFirstUrlCacheEntryEx\(SearchPattern, Flags

, Filter

, GroupId

\)
Initiates an enumeration of the browser cache

#### Parameters

  - SearchPattern=None : str

    Type of entry to find, can be 'visited:', 'cookie:', or None

  - Flags=0 : int

    None currently defined

  - Filter=0 : int

    Types of entries to return, combination of \*\_CACHE\_ENTRY values

  - GroupId=0 : int

    Cache group to enumerate, use 0 for all

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindFirstUrlCacheEntryEx at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstUrlCacheEntryEx.md), [google](http://www.google.com/search?q=FindFirstUrlCacheEntryEx.md) or [google groups](http://groups.google.com/groups?q=FindFirstUrlCacheEntryEx.md)\.

#### Return Value
Returns a handle that can be passed to [win32inet::FindNextUrlCacheEntry](win32inet.md#win32inetfindnexturlcacheentry), and a dict 

containing information for the first entry found\.  Throws error code ERROR\_NO\_MORE\_ITEMS 

if no items are found\.


## [win32inet](win32inet.md#win32inet)\.FindFirstUrlCacheGroup

\([PyUrlCacheHANDLE](PyUrlCacheHANDLE.md), int\) = FindFirstUrlCacheGroup\(Filter\)
Initiates enumeration of Url cache groups

#### Parameters

  - Filter=CACHEGROUP\_SEARCH\_ALL : int

    CACHEGROUP\_SEARCH\_\*

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindFirstUrlCacheGroup at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstUrlCacheGroup.md), [google](http://www.google.com/search?q=FindFirstUrlCacheGroup.md) or [google groups](http://groups.google.com/groups?q=FindFirstUrlCacheGroup.md)\.

#### Return Value
Returns a handle that can be passed to [win32inet::FindNextUrlCacheGroup](win32inet.md#win32inetfindnexturlcachegroup), and the id 

of the first group found\.


## [win32inet](win32inet.md#win32inet)\.FindNextUrlCacheEntry

dict = FindNextUrlCacheEntry\(EnumHandle\)
Continues enumeration of cached files

#### Parameters

  - EnumHandle : [PyUrlCacheHANDLE](PyUrlCacheHANDLE.md)

    Cache enumeration handle as returned by [win32inet::FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindNextUrlCacheEntry at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextUrlCacheEntry.md), [google](http://www.google.com/search?q=FindNextUrlCacheEntry.md) or [google groups](http://groups.google.com/groups?q=FindNextUrlCacheEntry.md)\.

#### Return Value
Returns a dict representing a INTERNET\_CACHE\_ENTRY\_INFO strunct


## [win32inet](win32inet.md#win32inet)\.FindNextUrlCacheEntryEx

dict = FindNextUrlCacheEntryEx\(EnumHandle\)
Continues enumeration of cached files

#### Parameters

  - EnumHandle : [PyUrlCacheHANDLE](PyUrlCacheHANDLE.md)

    Cache enumeration handle as returned by [win32inet::FindFirstUrlCacheEntryEx](win32inet.md#win32inetfindfirsturlcacheentryex)

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindNextUrlCacheEntryEx at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextUrlCacheEntryEx.md), [google](http://www.google.com/search?q=FindNextUrlCacheEntryEx.md) or [google groups](http://groups.google.com/groups?q=FindNextUrlCacheEntryEx.md)\.

#### Return Value
Returns a dict representing a INTERNET\_CACHE\_ENTRY\_INFO strunct


## [win32inet](win32inet.md#win32inet)\.FindNextUrlCacheGroup

int = FindNextUrlCacheGroup\(Find\)
Continues enumeration of cache groups

#### Parameters

  - Find : [PyHANDLE](PyHANDLE.md)

    Group enumeration handle as returned by [win32inet::FindFirstUrlCacheGroup](win32inet.md#win32inetfindfirsturlcachegroup)

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for FindNextUrlCacheGroup at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextUrlCacheGroup.md), [google](http://www.google.com/search?q=FindNextUrlCacheGroup.md) or [google groups](http://groups.google.com/groups?q=FindNextUrlCacheGroup.md)\.


## [win32inet](win32inet.md#win32inet)\.FtpCommand

[PyHINTERNET](PyHINTERNET.md) = FtpCommand\(Connect, ExpectResponse

, Flags

, Command

, Context

\)
Allows an application to send commands directly to an FTP server\.

#### Parameters

  - Connect : [PyHINTERNET](PyHINTERNET.md)

    Valid HINTERNET&\#09handle to an FTP session\.

  - ExpectResponse : bool

    Boolean value&\#09that indicates whether or not 

the application expects a response&\#09from the FTP server\. 

This must be set to True if a response&\#09is expected, or&\#09False otherwise\.

  - Flags : int

    Unsigned long integer value that contains the flags that 

control this function\. This can be set to&\#09either FTP\_TRANSFER\_TYPE\_ASCII or 

FTP\_TRANSFER\_TYPE\_BINARY

  - Command : string

    The command to send to the FTP server\.

  - Context=None : object

    Arbitrary object&\#09to be passed to&\#09callback

#### Comments

This function may cause a crash on 32-bit XP and Vista due to an internal error in win32inet\.dll\.

Accepts keyword args


## [win32inet](win32inet.md#win32inet)\.FtpOpenFile

[PyHINTERNET](PyHINTERNET.md) = FtpOpenFile\(hConnect, FileName

, Access

, Flags

, Context

\)
Initiates access to a remote file on an FTP server for reading or writing\.

#### Parameters

  - hConnect : [PyHINTERNET](PyHINTERNET.md)

    Valid HINTERNET handle to an FTP session\.

  - FileName : string

    The name of the file to access on the remote system\.

  - Access : int

    Integer value that determines how the file will be accessed\. This can be GENERIC\_READ or GENERIC\_WRITE, but not both\.

  - Flags : int

    Integer value that contains the conditions under which the 

transfers occur\. The application should select one transfer type and 

any of the flags that indicate how the caching of the file will be 

controlled\.  The transfer type can be one of the FTP\_TRANSFER\_TYPE\* values

  - Context=None : object

    Arbitrary object that will be passed to handle's callback function

#### Comments

Accepts keyword args


## [win32inet](win32inet.md#win32inet)\.GetUrlCacheEntryInfo

dict = GetUrlCacheEntryInfo\(UrlName\)
Retrieves cache info for a URL

#### Parameters

  - UrlName : str

    Cache enumeration handle as returned by [win32inet::FindFirstUrlCacheEntry](win32inet.md#win32inetfindfirsturlcacheentry)

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for GetUrlCacheEntryInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUrlCacheEntryInfo.md), [google](http://www.google.com/search?q=GetUrlCacheEntryInfo.md) or [google groups](http://groups.google.com/groups?q=GetUrlCacheEntryInfo.md)\.

#### Return Value
Returns a dict representing a INTERNET\_CACHE\_ENTRY\_INFO strunct


## [win32inet](win32inet.md#win32inet)\.GetUrlCacheGroupAttribute

dict = GetUrlCacheGroupAttribute\(GroupId, Attributes

\)
Retrieves attributes for a cache group

#### Parameters

  - GroupId : int

    Group id

  - Attributes=CACHEGROUP\_ATTRIBUTE\_GET\_ALL : int

    Attributes to retrieve, CACHEGROUP\_ATTRIBUTE\_\*

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for GetUrlCacheGroupAttribute at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUrlCacheGroupAttribute.md), [google](http://www.google.com/search?q=GetUrlCacheGroupAttribute.md) or [google groups](http://groups.google.com/groups?q=GetUrlCacheGroupAttribute.md)\.

#### Return Value
Returns a dict representing a INTERNET\_CACHE\_GROUP\_INFO struct


## [win32inet](win32inet.md#win32inet)\.InternetAttemptConnect

InternetAttemptConnect\(Reserved\)
Attempts to make a connection to the Internet\.

#### Parameters

  - Reserved=0 : int

    Use only 0\.


## [win32inet](win32inet.md#win32inet)\.InternetCanonicalizeUrl

string = InternetCanonicalizeUrl\(url, flags

\)
Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences\.

#### Parameters

  - url : string

    The URL to canonicalize\.

  - flags=0 : int

    integer value that contains the flags that control 

canonicalization\. This can be one of the following values:


## [win32inet](win32inet.md#win32inet)\.InternetCheckConnection

InternetCheckConnection\(Url, Flags, Reserved\)
Allows an application to check if a connection to the Internet can be established

#### Parameters

  - Url : string

    Url to attempt to connect to, can be None

  - Flags=0 : int

    FLAG\_ICC\_FORCE\_CONNECTION is only defined flag

  - Reserved=0 : int

    Use only 0\.


## [win32inet](win32inet.md#win32inet)\.InternetCloseHandle

InternetCloseHandle\(handle\)

#### Parameters

  - handle : [PyHINTERNET](PyHINTERNET.md)

    

#### Comments

It should not be necessary to call this function - all handles are 

[PyHINTERNET](PyHINTERNET.md) objects, so can have their Close method called, and will 

otherwise be automatically closed\.


## [win32inet](win32inet.md#win32inet)\.InternetConnect

InternetConnect\(Internet, ServerName, ServerPort, Username, Password, Service, Flags, Context\)
Opens an FTP, Gopher, or HTTP session for a given site\.

#### Parameters

  - Internet : [PyHINTERNET](PyHINTERNET.md)

    Valid HINTERNET handle returned by a previous call to [win32inet::InternetOpen](win32inet.md#win32inetinternetopen)\.

  - ServerName : string

    A string that contains the host name of an Internet 

server\. Alternately, the string can contain the IP number of the site, 

in ASCII dotted-decimal format \(for example, 11\.0\.1\.45\)\.

  - ServerPort : int

    Number of the TCP/IP port on the server to connect to\. 

These flags set only the port that will be used\. The service is set by 

the value of dwService\. This can be one of the INTERNET\_DEFAULT\_\*\_PORT 

constants or INTERNET\_INVALID\_PORT\_NUMBER, which uses the default 

port for the service specified by dwService\.

  - Username : string

    A string that contains the name of the user 

to log on\. If this parameter is&\#09None, the function uses&\#09an appropriate 

default, except&\#09for&\#09HTTP; a&\#09NULL parameter in HTTP causes the server 

to return an error\.&\#09For&\#09the&\#09FTP&\#09protocol, the default is "anonymous"\.

  - Password : string

    Address&\#09of a null-terminated string&\#09that 

contains the password to use to&\#09log&\#09on\.&\#09If both&\#09Password 

and&\#09Username are None, the function&\#09uses the default 

"anonymous"&\#09password\. In the case of FTP, the default password 

is the user's e-mail name\. If lpszPassword is None,&\#09but&\#09lpszUsername 

is not None, the function uses a blank password\.

  - Service : int

    Iinteger value that contains the type&\#09of service to 

access\.&\#09This can be&\#09one&\#09of INTERNET\_SERVICE\_FTP, INTERNET\_SERVICE\_GOPHER, 

or INTERNET\_SERVICE\_HTTP\.

  - Flags : int

    Integer value that contains the flags specific to 

the&\#09service&\#09used\. When the value of&\#09dwService is INTERNET\_SERVICE\_FTP, 

INTERNET\_FLAG\_PASSIVE causes the application to&\#09use&\#09passive&\#09FTP&\#09semantics\.

  - Context=None : object

    Arbitrary object to be passed to callback function

#### Comments

Accepts keyword args


## [win32inet](win32inet.md#win32inet)\.InternetGetCookie

string = InternetGetCookie\(Url, CookieName

\)
Retrieves the cookie for the specified URL

#### Parameters

  - Url : string

    Site for which to retrieve cookie

  - CookieName : string

    Name of cookie \(documented on MSDN as not implemented\)


## [win32inet](win32inet.md#win32inet)\.InternetGetLastResponseInfo

int, string = InternetGetLastResponseInfo\(\)
Retrieves the last Win32&\#174 Internet function error description or server response on the thread calling this function\.


## [win32inet](win32inet.md#win32inet)\.InternetGoOnline

InternetGoOnline\(Url, Parent, Flags\)
Prompts the user for permission to initiate connection to a URL\.

#### Parameters

  - Url : string

    Web site to connect to

  - Parent=None : int

    Handle to parent window

  - Flags=0 : int

    INTERNET\_GOONLINE\_REFRESH is only available flag


## [win32inet](win32inet.md#win32inet)\.InternetOpen

InternetOpen\(agent, proxyName, proxyBypass, flags\)
Initializes an application's use of the Microsoft&\#174 Win32&\#174 Internet functions\.

#### Parameters

  - agent : string

    A string that contains the name of the application 

or entity calling the Internet functions\. This name is used as the user 

agent in the HTTP protocol\.

  - proxyName : string

    

  - proxyBypass : string

    

  - flags : int

    Combination of INTERNET\_FLAG\_ASYNC,INTERNET\_FLAG\_FROM\_CACHE, or INTERNET\_FLAG\_OFFLINE


## [win32inet](win32inet.md#win32inet)\.InternetOpenUrl

[PyHINTERNET](PyHINTERNET.md) = InternetOpenUrl\(Internet, Url

, Headers

, Flags

, Context

\)
Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL\.

#### Parameters

  - Internet : [PyHINTERNET](PyHINTERNET.md)

    Internet handle as returned by [win32inet::InternetOpen](win32inet.md#win32inetinternetopen)

  - Url : string

    A string that contains the URL to begin reading\.  Only URLs beginning with ftp:, gopher:, http:, or https: are supported\.

  - Headers=None : string

    a string&\#09variable that contains the headers to be sent to the HTTP server\.

  - Flags=0 : int

    INTERNET\_FLAG\_\*

  - Context=None : object

    An arbitrary object to be passed to the status callback function

#### Comments

Accepts keyword args\.

#### Return Value
Returns None in async mode \(Internet handle created with INTERNET\_FLAG\_ASYNC\)\. 

When handle is created, it will be passed to callback function of parent handle\.


## [win32inet](win32inet.md#win32inet)\.InternetQueryOption

object = InternetQueryOption\(hInternet, Option

\)
Retrieves an option for an internet handle

#### Parameters

  - hInternet : [PyHINTERNET](PyHINTERNET.md)

    Internet handle, or None for global defaults

  - Option : int

    INTERNET\_OPTION\_\* value

   

       Option

   

   

       Returned type

   

INTERNET\_OPTION\_CALLBACKPython callback function

INTERNET\_OPTION\_CONTEXT\_VALUEContext object

INTERNET\_OPTION\_SEND\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_CONTROL\_SEND\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_RECEIVE\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_CONTROL\_RECEIVE\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_CODEPAGEInt - Codepage of host part of URL

INTERNET\_OPTION\_CODEPAGE\_PATHInt - Codepage for URL

INTERNET\_OPTION\_CODEPAGE\_EXTRAInt - Codepage for path part of URL

INTERNET\_OPTION\_CONNECT\_RETRIESInt - Number of time to try to reconnect to host

INTERNET\_OPTION\_CONNECT\_TIMEOUTInt - Connection timeout in milliseconds

INTERNET\_OPTION\_CONNECTED\_STATEInt - Connection state, INTERNET\_STATE\_\*

INTERNET\_OPTION\_HANDLE\_TYPEInt, INTERNET\_HANDLE\_TYPE\_\*

INTERNET\_OPTION\_ERROR\_MASKInt, combination of INTERNET\_ERROR\_MASK\_\*

INTERNET\_OPTION\_EXTENDED\_ERRORInt, ERROR\_INTERNET\_\*

INTERNET\_OPTION\_FROM\_CACHE\_TIMEOUTInt - Timeout in ms before cached copy is used

INTERNET\_OPTION\_IDNInt, INTERNET\_FLAG\_IDN\_\*

INTERNET\_OPTION\_MAX\_CONNS\_PER\_1\_0\_SERVERInt

INTERNET\_OPTION\_MAX\_CONNS\_PER\_SERVERInt

INTERNET\_OPTION\_READ\_BUFFER\_SIZEInt

INTERNET\_OPTION\_WRITE\_BUFFER\_SIZEInt

INTERNET\_OPTION\_REQUEST\_FLAGSInt, combination of INTERNET\_REQFLAG\_\*

INTERNET\_OPTION\_REQUEST\_PRIORITYInt

INTERNET\_OPTION\_SECURITY\_FLAGSInt, SECURITY\_FLAG\_\*

INTERNET\_OPTION\_SECURITY\_KEY\_BITNESSInt

INTERNET\_OPTION\_BYPASS\_EDITED\_ENTRYBoolean

INTERNET\_OPTION\_HTTP\_DECODINGBoolean

INTERNET\_OPTION\_IGNORE\_OFFLINEBoolean

INTERNET\_OPTION\_DATAFILE\_NAMEString - Name of internet cache file

INTERNET\_OPTION\_USERNAMEString - Username passed to InternetConnect

INTERNET\_OPTION\_PASSWORDString - Password passed to InternetConnect

INTERNET\_OPTION\_PROXY\_PASSWORDString

INTERNET\_OPTION\_PROXY\_USERNAMEString

INTERNET\_OPTION\_SECONDARY\_CACHE\_KEYString

INTERNET\_OPTION\_SECURITY\_CERTIFICATEString

INTERNET\_OPTION\_URLString

INTERNET\_OPTION\_USER\_AGENTString

INTERNET\_OPTION\_CACHE\_TIMESTAMPSdict - Expiration and last modified times

INTERNET\_OPTION\_HTTP\_VERSIONdict - HTTP\_VERSION\_INFO

INTERNET\_OPTION\_VERSIONdict - INTERNET\_VERSION\_INFO

INTERNET\_OPTION\_PARENT\_HANDLE[PyHINTERNET](PyHINTERNET.md)

INTERNET\_OPTION\_PROXYdict - INTERNET\_PROXY\_INFO

INTERNET\_OPTION\_DIAGNOSTIC\_SOCKET\_INFONot yet supported \(INTERNET\_DIAGNOSTIC\_SOCKET\_INFO\)

INTERNET\_OPTION\_PER\_CONNECTION\_OPTIONNot yet supported \(INTERNET\_PER\_CONN\_OPTION\_LIST\)

INTERNET\_OPTION\_SECURITY\_CERTIFICATE\_STRUCTNot yet supported \(INTERNET\_CERTIFICATE\_INFO\)

INTERNET\_OPTION\_ALTER\_IDENTITYNot supported

INTERNET\_OPTION\_ASYNCNot supported

INTERNET\_OPTION\_ASYNC\_IDNot supported

INTERNET\_OPTION\_ASYNC\_PRIORITYNot supported

INTERNET\_OPTION\_CACHE\_STREAM\_HANDLENot supported

INTERNET\_OPTION\_CALLBACK\_FILTERNot supported

INTERNET\_OPTION\_CLIENT\_CERT\_CONTEXTNot supported

INTERNET\_OPTION\_DATA\_RECEIVE\_TIMEOUTNot supported

INTERNET\_OPTION\_DATA\_SEND\_TIMEOUTNot supported

INTERNET\_OPTION\_CONNECT\_BACKOFFNot supported

INTERNET\_OPTION\_CONNECT\_TIMENot supported

INTERNET\_OPTION\_DISABLE\_AUTODIALNot supported

INTERNET\_OPTION\_DISCONNECTED\_TIMEOUTNot supported

INTERNET\_OPTION\_IDENTITYNot supported

INTERNET\_OPTION\_IDLE\_STATENot supported

INTERNET\_OPTION\_KEEP\_CONNECTIONNot supported

INTERNET\_OPTION\_LISTEN\_TIMEOUTNot supported

INTERNET\_OPTION\_OFFLINE\_MODENot supported

INTERNET\_OPTION\_OFFLINE\_SEMANTICSNot supported

INTERNET\_OPTION\_POLICYNot supported

INTERNET\_OPTION\_RECEIVE\_THROUGHPUTNot supported

INTERNET\_OPTION\_REMOVE\_IDENTITYNot supported

INTERNET\_OPTION\_SEND\_THROUGHPUTNot supported

INTERNET\_OPTION\_DATAFILE\_EXTOnly valid for InternetSetOption

INTERNET\_OPTION\_DIGEST\_AUTH\_UNLOADOnly valid for InternetSetOption

INTERNET\_OPTION\_END\_BROWSER\_SESSIONOnly valid for InternetSetOption

INTERNET\_OPTION\_REFRESHOnly valid for InternetSetOption

INTERNET\_OPTION\_RESET\_URLCACHE\_SESSIONOnly valid for InternetSetOption

INTERNET\_OPTION\_SETTINGS\_CHANGEDOnly valid for InternetSetOption

#### Win32 API References

  - Search for InternetQueryOption at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InternetQueryOption.md), [google](http://www.google.com/search?q=InternetQueryOption.md) or [google groups](http://groups.google.com/groups?q=InternetQueryOption.md)\.

#### Return Value
The type of object returned is dependent on the option requested


## [win32inet](win32inet.md#win32inet)\.InternetReadFile

string = InternetReadFile\(hInternet, size

\)
Reads data from a handle opened by the 

[win32inet::InternetOpenUrl](win32inet.md#win32inetinternetopenurl), [win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile), 

win32inet::GopherOpenFile

, or win32inet::HttpOpenRequest

 function\.

#### Parameters

  - hInternet : [PyHINTERNET](PyHINTERNET.md)

    

  - size : int

    Number of bytes to read\.

#### Return Value
The result will be a string of zero bytes when the end is reached\.


## [win32inet](win32inet.md#win32inet)\.InternetSetCookie

InternetSetCookie\(url, lpszCookieName, data\)
Creates a cookie associated with the specified URL\.

#### Parameters

  - url : string

    

  - lpszCookieName : string

    

  - data : string

    


## [win32inet](win32inet.md#win32inet)\.InternetSetOption

InternetSetOption\(hInternet, Option, Buffer\)
Sets an option for an internet handle

#### Parameters

  - hInternet : [PyHINTERNET](PyHINTERNET.md)

    Internet handle, or None for global defaults

  - Option : int

    The option to set, INTERNET\_OPTION\_\*

  - Buffer : object

    Type is dependent on Option

   

       Option

   

   

       Type of input object

   

INTERNET\_OPTION\_CALLBACKPython function called on status change

INTERNET\_OPTION\_CONTEXT\_VALUEAny Python object to be passed to callback function

INTERNET\_OPTION\_SEND\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_CONTROL\_SEND\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_RECEIVE\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_CONTROL\_RECEIVE\_TIMEOUTInt - timeout in millseconds

INTERNET\_OPTION\_CODEPAGEInt - Codepage of host part of URL

INTERNET\_OPTION\_CODEPAGE\_PATHCodepage for URL

INTERNET\_OPTION\_CODEPAGE\_EXTRAInt - Codepage for path part of URL

INTERNET\_OPTION\_CONNECT\_RETRIESInt - Number of time to try to reconnect to host

INTERNET\_OPTION\_CONNECT\_TIMEOUTInt - Connection timeout in milliseconds

INTERNET\_OPTION\_CONNECTED\_STATEInt - Connection state, INTERNET\_STATE\_\*

INTERNET\_OPTION\_ERROR\_MASKInt, combination of INTERNET\_ERROR\_MASK\_\*

INTERNET\_OPTION\_FROM\_CACHE\_TIMEOUTInt - Timeout in ms before cached copy is used

INTERNET\_OPTION\_IDNInt, INTERNET\_FLAG\_IDN\_\*

INTERNET\_OPTION\_MAX\_CONNS\_PER\_1\_0\_SERVERInt

INTERNET\_OPTION\_MAX\_CONNS\_PER\_SERVERInt

INTERNET\_OPTION\_READ\_BUFFER\_SIZEInt

INTERNET\_OPTION\_WRITE\_BUFFER\_SIZEInt

INTERNET\_OPTION\_REQUEST\_PRIORITYInt

INTERNET\_OPTION\_DIGEST\_AUTH\_UNLOADNone

INTERNET\_OPTION\_END\_BROWSER\_SESSIONNone

INTERNET\_OPTION\_REFRESHNone

INTERNET\_OPTION\_RESET\_URLCACHE\_SESSIONNone

INTERNET\_OPTION\_SETTINGS\_CHANGEDNone

INTERNET\_OPTION\_BYPASS\_EDITED\_ENTRYBoolean

INTERNET\_OPTION\_HTTP\_DECODINGBoolean

INTERNET\_OPTION\_IGNORE\_OFFLINEBoolean

INTERNET\_OPTION\_USERNAMEString - Username passed to InternetConnect

INTERNET\_OPTION\_PASSWORDString - Password passed to InternetConnect

INTERNET\_OPTION\_PROXY\_PASSWORDString

INTERNET\_OPTION\_PROXY\_USERNAMEString

INTERNET\_OPTION\_SECONDARY\_CACHE\_KEYString

INTERNET\_OPTION\_USER\_AGENTString

INTERNET\_OPTION\_DATAFILE\_EXTString - Extension to use for download cache file

INTERNET\_OPTION\_PROXYDict representing INTERNET\_PROXY\_INFO struct

INTERNET\_OPTION\_HTTP\_VERSIONNot yet supported - HTTP\_VERSION\_INFO

INTERNET\_OPTION\_PER\_CONNECTION\_OPTIONNot yet supported \(INTERNET\_PER\_CONN\_OPTION\_LIST\)

INTERNET\_OPTION\_ALTER\_IDENTITYNot supported

INTERNET\_OPTION\_ASYNCNot supported

INTERNET\_OPTION\_ASYNC\_IDNot supported

INTERNET\_OPTION\_ASYNC\_PRIORITYNot supported

INTERNET\_OPTION\_CACHE\_STREAM\_HANDLENot supported

INTERNET\_OPTION\_CALLBACK\_FILTERNot supported

INTERNET\_OPTION\_CLIENT\_CERT\_CONTEXTNot supported

INTERNET\_OPTION\_DATA\_RECEIVE\_TIMEOUTNot supported

INTERNET\_OPTION\_DATA\_SEND\_TIMEOUTNot supported

INTERNET\_OPTION\_CONNECT\_BACKOFFNot supported

INTERNET\_OPTION\_CONNECT\_TIMENot supported

INTERNET\_OPTION\_DISABLE\_AUTODIALNot supported

INTERNET\_OPTION\_DISCONNECTED\_TIMEOUTNot supported

INTERNET\_OPTION\_IDENTITYNot supported

INTERNET\_OPTION\_IDLE\_STATENot supported

INTERNET\_OPTION\_KEEP\_CONNECTIONNot supported

INTERNET\_OPTION\_LISTEN\_TIMEOUTNot supported

INTERNET\_OPTION\_OFFLINE\_MODENot supported

INTERNET\_OPTION\_OFFLINE\_SEMANTICSNot supported

INTERNET\_OPTION\_POLICYNot supported

INTERNET\_OPTION\_RECEIVE\_THROUGHPUTNot supported

INTERNET\_OPTION\_REMOVE\_IDENTITYNot supported

INTERNET\_OPTION\_SEND\_THROUGHPUTNot supported

INTERNET\_OPTION\_CACHE\_TIMESTAMPSOnly valid for InternetQueryOption

INTERNET\_OPTION\_HANDLE\_TYPEOnly valid for InternetQueryOption

INTERNET\_OPTION\_DATAFILE\_NAMEOnly valid for InternetQueryOption

INTERNET\_OPTION\_PARENT\_HANDLEOnly valid for InternetQueryOption

INTERNET\_OPTION\_SECURITY\_CERTIFICATEOnly valid for InternetQueryOption

INTERNET\_OPTION\_SECURITY\_CERTIFICATE\_STRUCTOnly valid for InternetQueryOption

INTERNET\_OPTION\_SECURITY\_FLAGSOnly valid for InternetQueryOption

INTERNET\_OPTION\_SECURITY\_KEY\_BITNESSOnly valid for InternetQueryOption

INTERNET\_OPTION\_DIAGNOSTIC\_SOCKET\_INFOOnly valid for InternetQueryOption

INTERNET\_OPTION\_VERSIONOnly valid for InternetQueryOption

INTERNET\_OPTION\_EXTENDED\_ERROROnly valid for InternetQueryOption

INTERNET\_OPTION\_REQUEST\_FLAGSOnly valid for InternetQueryOption

INTERNET\_OPTION\_URLOnly valid for InternetQueryOption

#### Win32 API References

  - Search for InternetSetOption at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InternetSetOption.md), [google](http://www.google.com/search?q=InternetSetOption.md) or [google groups](http://groups.google.com/groups?q=InternetSetOption.md)\.


## [win32inet](win32inet.md#win32inet)\.InternetWriteFile

int = InternetWriteFile\(File, Buffer

\)
Writes data to a handle opened by [win32inet::FtpOpenFile](win32inet.md#win32inetftpopenfile)\.

#### Parameters

  - File : [PyHINTERNET](PyHINTERNET.md)

    Writeable internet&\#09handle

  - Buffer : string

    String or&\#09buffer containing data to be written


## [win32inet](win32inet.md#win32inet)\.SetUrlCacheEntryGroup

SetUrlCacheEntryGroup\(UrlName, Flags, GroupId\)
Associates a cache entry with a group

#### Parameters

  - UrlName : str

    Url whose cache is to be added to the group

  - Flags : int

    INTERNET\_CACHE\_GROUP\_ADD or INTERNET\_CACHE\_GROUP\_REMOVE

  - GroupId : int

    Id of a cache group

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for SetUrlCacheEntryGroup at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetUrlCacheEntryGroup.md), [google](http://www.google.com/search?q=SetUrlCacheEntryGroup.md) or [google groups](http://groups.google.com/groups?q=SetUrlCacheEntryGroup.md)\.


## [win32inet](win32inet.md#win32inet)\.SetUrlCacheGroupAttribute

SetUrlCacheGroupAttribute\(GroupId, Attributes, GroupInfo, Flags\)
Changes the attributes of a cache group

#### Parameters

  - GroupId : int

    Id of a cache group

  - Attributes : int

    Bitmask of CACHEGROUP\_ATTRIBUTE\_\* flags indicating which attributes to set

  - GroupInfo : dict

    INTERNET\_CACHE\_GROUP\_INFO dict as returned by [win32inet::GetUrlCacheGroupAttribute](win32inet.md#win32inetgeturlcachegroupattribute)

  - Flags=0 : int

    Reserved, use 0

#### Comments

Accepts keyword args

#### Win32 API References

  - Search for SetUrlCacheGroupAttribute at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetUrlCacheGroupAttribute.md), [google](http://www.google.com/search?q=SetUrlCacheGroupAttribute.md) or [google groups](http://groups.google.com/groups?q=SetUrlCacheGroupAttribute.md)\.


## [win32inet](win32inet.md#win32inet)\.WinHttpGetDefaultProxyConfiguration

[PyWINHTTP\_PROXY\_INFO](PyWINHTTP.md#pywinhttpproxy_info) = WinHttpGetDefaultProxyConfiguration\(\)
Retrieves the default WinHTTP proxy configuration from the registry\.


## [win32inet](win32inet.md#win32inet)\.WinHttpGetIEProxyConfigForCurrentUser

tuple = WinHttpGetIEProxyConfigForCurrentUser\(\)
Obtains 

the Internet Explorer proxy configuration for the current user\.

#### Win32 API References

  - Search for WinHttpGetIEProxyConfigForCurrentUser at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHttpGetIEProxyConfigForCurrentUser.md), [google](http://www.google.com/search?q=WinHttpGetIEProxyConfigForCurrentUser.md) or [google groups](http://groups.google.com/groups?q=WinHttpGetIEProxyConfigForCurrentUser.md)\.

  - Search for WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WINHTTP.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=winhttpcurrent_user_ie_proxy_config), [google](http://www.google.com/search?q=WINHTTP.md#http://www.google.com/search?q=winhttpcurrent_user_ie_proxy_config) or [google groups](http://groups.google.com/groups?q=WINHTTP.md#http://groups.google.com/groups?q=winhttpcurrent_user_ie_proxy_config)\.

#### Return Value
The result is a windows WINHTTP\_CURRENT\_USER\_IE\_PROXY\_CONFIG 

structure; a tuple of an int \(bool\) and 3 unicode strings 

\(fAutoDetect, lpszAutoConfigUrl, lpszProxy, lpszProxyBypass\)\.


## [win32inet](win32inet.md#win32inet)\.WinHttpGetProxyForUrl

[PyWINHTTP\_PROXY\_INFO](PyWINHTTP.md#pywinhttpproxy_info) = WinHttpGetProxyForUrl\(handle, url

, options

\)
Obtains 

the Internet Explorer proxy configuration for the specified URL\.

#### Parameters

  - handle : HANDLE

/int

    

  - url : unicode/string

    

  - options : [PyWINHTTP\_AUTOPROXY\_OPTIONS](PyWINHTTP.md#pywinhttpautoproxy_options)

    


## [win32inet](win32inet.md#win32inet)\.WinHttpOpen

[PyHINTERNET](PyHINTERNET.md) = WinHttpOpen\(lpszUserAgent, dwAccessType

, lpszProxyName

, lpszProxyBypass

, dwFlags

\)
Opens a winhttp session\.

#### Parameters

  - lpszUserAgent : string

    

  - dwAccessType : int

    

  - lpszProxyName : string

    

  - lpszProxyBypass : string

    

  - dwFlags : int

    

#### Win32 API References

  - Search for WinHttpOpen at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHttpOpen.md), [google](http://www.google.com/search?q=WinHttpOpen.md) or [google groups](http://groups.google.com/groups?q=WinHttpOpen.md)\.