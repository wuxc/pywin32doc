
## [win32inet](#README.md#win32inet).CommitUrlCacheEntry

str = **CommitUrlCacheEntry( *UrlName*  *, LocalFileName*  *, ExpireTime*  *, LastModifiedTime*  *, CacheEntryType*  *, HeaderInfo*  *, OriginalUrl* ** )
Commits a cache entry

#### Parameters


     *UrlName* : str

    The Url for which to create an entry

     *LocalFileName* : str

    Filename returned from[win32inet::CreateUrlCacheEntry](#win32inet.md#win32inetCreateUrlCacheEntry). 

Can be None when creating a history entry.

     *ExpireTime=None* :[PyTime](#README.md#PyTime)

    Time at which entry expires

     *LastModifiedTime=None* :[PyTime](#README.md#PyTime)

    Modification time of URL

     *CacheEntryType=NORMAL_CACHE_ENTRY* : int

    Combination of *_CACHE_ENTRY flags

     *HeaderInfo=None* : str

    Header data used to request Url

     *OriginalUrl=None* : str

    If redirected, original site requested

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *CommitUrlCacheEntry* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CommitUrlCacheEntry),[google](#README.md#http://www.google.com/search?q=CommitUrlCacheEntry)or[google groups](#README.md#http://groups.google.com/groups?q=CommitUrlCacheEntry).

## [win32inet](#README.md#win32inet).CreateUrlCacheEntry

str = **CreateUrlCacheEntry( *UrlName*  *, ExpectedFileSize*  *, FileExtension* ** )
Creates a cache entry for a URL

#### Parameters


     *UrlName* : str

    The Url for which to create an entry

     *ExpectedFileSize* : int

    Size of content, use 0 if unknown

     *FileExtension* : str

    Extension to use for filename

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *CreateUrlCacheEntry* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateUrlCacheEntry),[google](#README.md#http://www.google.com/search?q=CreateUrlCacheEntry)or[google groups](#README.md#http://groups.google.com/groups?q=CreateUrlCacheEntry).

#### Return Value
Returns the filename to which content should be written

## [win32inet](#README.md#win32inet).CreateUrlCacheGroup

long = **CreateUrlCacheGroup( *Flags* ** )
Creates a new cache group

#### Parameters


     *Flags=0* : int

    Combination of CACHEGROUP_FLAG_* flags

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *CreateUrlCacheGroup* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateUrlCacheGroup),[google](#README.md#http://www.google.com/search?q=CreateUrlCacheGroup)or[google groups](#README.md#http://groups.google.com/groups?q=CreateUrlCacheGroup).

## [win32inet](#README.md#win32inet).DeleteUrlCacheEntry

 **DeleteUrlCacheEntry( *UrlName* ** )
Deletes the cache entry for a URL

#### Parameters


     *UrlName* : str

    Cached url to be deleted

## [win32inet](#README.md#win32inet).DeleteUrlCacheGroup

 **DeleteUrlCacheGroup( *GroupId*  *, Attributes* ** )
Deletes a cache group

#### Parameters


     *GroupId* : int

    Group id

     *Attributes=CACHEGROUP_FLAG_FLUSHURL_ONDELETE* : int

    Combination of CACHEGROUP_FLAG_* flags

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *DeleteUrlCacheGroup* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteUrlCacheGroup),[google](#README.md#http://www.google.com/search?q=DeleteUrlCacheGroup)or[google groups](#README.md#http://groups.google.com/groups?q=DeleteUrlCacheGroup).

## [win32inet](#README.md#win32inet).FindCloseUrlCache

 **FindCloseUrlCache( *EnumHandle* ** )
Closes a cache enumeration handle

#### Parameters


     *EnumHandle* :[PyUrlCacheHANDLE](#README.md#PyUrlCacheHANDLE)

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntry](#win32inet.md#win32inetFindFirstUrlCacheEntry)

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindCloseUrlCache* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindCloseUrlCache),[google](#README.md#http://www.google.com/search?q=FindCloseUrlCache)or[google groups](#README.md#http://groups.google.com/groups?q=FindCloseUrlCache).

## [win32inet](#README.md#win32inet).FindFirstUrlCacheEntry

([PyUrlCacheHANDLE](#README.md#PyUrlCacheHANDLE), dict) = **FindFirstUrlCacheEntry( *SearchPattern* ** )
Initiates an enumeration of the browser cache

#### Parameters


     *SearchPattern=None* : str

    Type of entry to find, can be 'visited:', 'cookie:', or None

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindFirstUrlCacheEntry* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstUrlCacheEntry),[google](#README.md#http://www.google.com/search?q=FindFirstUrlCacheEntry)or[google groups](#README.md#http://groups.google.com/groups?q=FindFirstUrlCacheEntry).

#### Return Value
Returns a handle that can be passed to[win32inet::FindNextUrlCacheEntry](#win32inet.md#win32inetFindNextUrlCacheEntry), and a dict 

containing information for the first entry found.  Throws error code ERROR_NO_MORE_ITEMS 

if no items are found.

## [win32inet](#README.md#win32inet).FindFirstUrlCacheEntryEx

([PyUrlCacheHANDLE](#README.md#PyUrlCacheHANDLE), dict) = **FindFirstUrlCacheEntryEx( *SearchPattern*  *, Flags*  *, Filter*  *, GroupId* ** )
Initiates an enumeration of the browser cache

#### Parameters


     *SearchPattern=None* : str

    Type of entry to find, can be 'visited:', 'cookie:', or None

     *Flags=0* : int

    None currently defined

     *Filter=0* : int

    Types of entries to return, combination of *_CACHE_ENTRY values

     *GroupId=0* : int

    Cache group to enumerate, use 0 for all

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindFirstUrlCacheEntryEx* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstUrlCacheEntryEx),[google](#README.md#http://www.google.com/search?q=FindFirstUrlCacheEntryEx)or[google groups](#README.md#http://groups.google.com/groups?q=FindFirstUrlCacheEntryEx).

#### Return Value
Returns a handle that can be passed to[win32inet::FindNextUrlCacheEntry](#win32inet.md#win32inetFindNextUrlCacheEntry), and a dict 

containing information for the first entry found.  Throws error code ERROR_NO_MORE_ITEMS 

if no items are found.

## [win32inet](#README.md#win32inet).FindFirstUrlCacheGroup

([PyUrlCacheHANDLE](#README.md#PyUrlCacheHANDLE), int) = **FindFirstUrlCacheGroup( *Filter* ** )
Initiates enumeration of Url cache groups

#### Parameters


     *Filter=CACHEGROUP_SEARCH_ALL* : int

    CACHEGROUP_SEARCH_*

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindFirstUrlCacheGroup* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstUrlCacheGroup),[google](#README.md#http://www.google.com/search?q=FindFirstUrlCacheGroup)or[google groups](#README.md#http://groups.google.com/groups?q=FindFirstUrlCacheGroup).

#### Return Value
Returns a handle that can be passed to[win32inet::FindNextUrlCacheGroup](#win32inet.md#win32inetFindNextUrlCacheGroup), and the id 

of the first group found.

## [win32inet](#README.md#win32inet).FindNextUrlCacheEntry

dict = **FindNextUrlCacheEntry( *EnumHandle* ** )
Continues enumeration of cached files

#### Parameters


     *EnumHandle* :[PyUrlCacheHANDLE](#README.md#PyUrlCacheHANDLE)

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntry](#win32inet.md#win32inetFindFirstUrlCacheEntry)

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindNextUrlCacheEntry* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextUrlCacheEntry),[google](#README.md#http://www.google.com/search?q=FindNextUrlCacheEntry)or[google groups](#README.md#http://groups.google.com/groups?q=FindNextUrlCacheEntry).

#### Return Value
Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

## [win32inet](#README.md#win32inet).FindNextUrlCacheEntryEx

dict = **FindNextUrlCacheEntryEx( *EnumHandle* ** )
Continues enumeration of cached files

#### Parameters


     *EnumHandle* :[PyUrlCacheHANDLE](#README.md#PyUrlCacheHANDLE)

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntryEx](#win32inet.md#win32inetFindFirstUrlCacheEntryEx)

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindNextUrlCacheEntryEx* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextUrlCacheEntryEx),[google](#README.md#http://www.google.com/search?q=FindNextUrlCacheEntryEx)or[google groups](#README.md#http://groups.google.com/groups?q=FindNextUrlCacheEntryEx).

#### Return Value
Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

## [win32inet](#README.md#win32inet).FindNextUrlCacheGroup

int = **FindNextUrlCacheGroup( *Find* ** )
Continues enumeration of cache groups

#### Parameters


     *Find* :[PyHANDLE](#README.md#PyHANDLE)

    Group enumeration handle as returned by[win32inet::FindFirstUrlCacheGroup](#win32inet.md#win32inetFindFirstUrlCacheGroup)

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *FindNextUrlCacheGroup* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextUrlCacheGroup),[google](#README.md#http://www.google.com/search?q=FindNextUrlCacheGroup)or[google groups](#README.md#http://groups.google.com/groups?q=FindNextUrlCacheGroup).

## [win32inet](#README.md#win32inet).FtpCommand

[PyHINTERNET](#README.md#PyHINTERNET)= **FtpCommand( *Connect*  *, ExpectResponse*  *, Flags*  *, Command*  *, Context* ** )
Allows an application to send commands directly to an FTP server.

#### Parameters


     *Connect* :[PyHINTERNET](#README.md#PyHINTERNET)

    Valid HINTERNET&#09handle to an FTP session.

     *ExpectResponse* : bool

    Boolean value&#09that indicates whether or not 

the application expects a response&#09from the FTP server. 

This must be set to True if a response&#09is expected, or&#09False otherwise.

     *Flags* : int

    Unsigned long integer value that contains the flags that 

control this function. This can be set to&#09either FTP_TRANSFER_TYPE_ASCII or 

FTP_TRANSFER_TYPE_BINARY

     *Command* : string

    The command to send to the FTP server.

     *Context=None* : object

    Arbitrary object&#09to be passed to&#09callback

#### Comments
This function may cause a crash on 32-bit XP and Vista due to an internal error in win32inet.dll.
Accepts keyword args

## [win32inet](#README.md#win32inet).FtpOpenFile

[PyHINTERNET](#README.md#PyHINTERNET)= **FtpOpenFile( *hConnect*  *, FileName*  *, Access*  *, Flags*  *, Context* ** )
Initiates access to a remote file on an FTP server for reading or writing.

#### Parameters


     *hConnect* :[PyHINTERNET](#README.md#PyHINTERNET)

    Valid HINTERNET handle to an FTP session.

     *FileName* : string

    The name of the file to access on the remote system.

     *Access* : int

    Integer value that determines how the file will be accessed. This can be GENERIC_READ or GENERIC_WRITE, but not both.

     *Flags* : int

    Integer value that contains the conditions under which the 

transfers occur. The application should select one transfer type and 

any of the flags that indicate how the caching of the file will be 

controlled.  The transfer type can be one of the FTP_TRANSFER_TYPE* values

     *Context=None* : object

    Arbitrary object that will be passed to handle's callback function

#### Comments
Accepts keyword args

## [win32inet](#README.md#win32inet).GetUrlCacheEntryInfo

dict = **GetUrlCacheEntryInfo( *UrlName* ** )
Retrieves cache info for a URL

#### Parameters


     *UrlName* : str

    Cache enumeration handle as returned by[win32inet::FindFirstUrlCacheEntry](#win32inet.md#win32inetFindFirstUrlCacheEntry)

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *GetUrlCacheEntryInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUrlCacheEntryInfo),[google](#README.md#http://www.google.com/search?q=GetUrlCacheEntryInfo)or[google groups](#README.md#http://groups.google.com/groups?q=GetUrlCacheEntryInfo).

#### Return Value
Returns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

## [win32inet](#README.md#win32inet).GetUrlCacheGroupAttribute

dict = **GetUrlCacheGroupAttribute( *GroupId*  *, Attributes* ** )
Retrieves attributes for a cache group

#### Parameters


     *GroupId* : int

    Group id

     *Attributes=CACHEGROUP_ATTRIBUTE_GET_ALL* : int

    Attributes to retrieve, CACHEGROUP_ATTRIBUTE_*

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *GetUrlCacheGroupAttribute* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUrlCacheGroupAttribute),[google](#README.md#http://www.google.com/search?q=GetUrlCacheGroupAttribute)or[google groups](#README.md#http://groups.google.com/groups?q=GetUrlCacheGroupAttribute).

#### Return Value
Returns a dict representing a INTERNET_CACHE_GROUP_INFO struct

## [win32inet](#README.md#win32inet).InternetAttemptConnect

 **InternetAttemptConnect( *Reserved* ** )
Attempts to make a connection to the Internet.

#### Parameters


     *Reserved=0* : int

    Use only 0.

## [win32inet](#README.md#win32inet).InternetCanonicalizeUrl

string = **InternetCanonicalizeUrl( *url*  *, flags* ** )
Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences.

#### Parameters


     *url* : string

    The URL to canonicalize.

     *flags=0* : int

    integer value that contains the flags that control 

canonicalization. This can be one of the following values:

## [win32inet](#README.md#win32inet).InternetCheckConnection

 **InternetCheckConnection( *Url*  *, Flags*  *, Reserved* ** )
Allows an application to check if a connection to the Internet can be established

#### Parameters


     *Url* : string

    Url to attempt to connect to, can be None

     *Flags=0* : int

    FLAG_ICC_FORCE_CONNECTION is only defined flag

     *Reserved=0* : int

    Use only 0.

## [win32inet](#README.md#win32inet).InternetCloseHandle

 **InternetCloseHandle( *handle* ** )


#### Parameters


     *handle* :[PyHINTERNET](#README.md#PyHINTERNET)

    

#### Comments
It should not be necessary to call this function - all handles are[PyHINTERNET](#README.md#PyHINTERNET)objects, so can have their Close method called, and will 

otherwise be automatically closed.

## [win32inet](#README.md#win32inet).InternetConnect

 **InternetConnect( *Internet*  *, ServerName*  *, ServerPort*  *, Username*  *, Password*  *, Service*  *, Flags*  *, Context* ** )
Opens an FTP, Gopher, or HTTP session for a given site.

#### Parameters


     *Internet* :[PyHINTERNET](#README.md#PyHINTERNET)

    Valid HINTERNET handle returned by a previous call to[win32inet::InternetOpen](#win32inet.md#win32inetInternetOpen).

     *ServerName* : string

    A string that contains the host name of an Internet 

server. Alternately, the string can contain the IP number of the site, 

in ASCII dotted-decimal format (for example, 11.0.1.45).

     *ServerPort* : int

    Number of the TCP/IP port on the server to connect to. 

These flags set only the port that will be used. The service is set by 

the value of dwService. This can be one of the INTERNET_DEFAULT_*_PORT 

constants or INTERNET_INVALID_PORT_NUMBER, which uses the default 

port for the service specified by dwService.

     *Username* : string

    A string that contains the name of the user 

to log on. If this parameter is&#09None, the function uses&#09an appropriate 

default, except&#09for&#09HTTP; a&#09NULL parameter in HTTP causes the server 

to return an error.&#09For&#09the&#09FTP&#09protocol, the default is "anonymous".

     *Password* : string

    Address&#09of a null-terminated string&#09that 

contains the password to use to&#09log&#09on.&#09If both&#09Password 

and&#09Username are None, the function&#09uses the default 

"anonymous"&#09password. In the case of FTP, the default password 

is the user's e-mail name. If lpszPassword is None,&#09but&#09lpszUsername 

is not None, the function uses a blank password.

     *Service* : int

    Iinteger value that contains the type&#09of service to 

access.&#09This can be&#09one&#09of INTERNET_SERVICE_FTP, INTERNET_SERVICE_GOPHER, 

or INTERNET_SERVICE_HTTP.

     *Flags* : int

    Integer value that contains the flags specific to 

the&#09service&#09used. When the value of&#09dwService is INTERNET_SERVICE_FTP, 

INTERNET_FLAG_PASSIVE causes the application to&#09use&#09passive&#09FTP&#09semantics.

     *Context=None* : object

    Arbitrary object to be passed to callback function

#### Comments
Accepts keyword args

## [win32inet](#README.md#win32inet).InternetGetCookie

string = **InternetGetCookie( *Url*  *, CookieName* ** )
Retrieves the cookie for the specified URL

#### Parameters


     *Url* : string

    Site for which to retrieve cookie

     *CookieName* : string

    Name of cookie (documented on MSDN as not implemented)

## [win32inet](#README.md#win32inet).InternetGetLastResponseInfo

int, string = **InternetGetLastResponseInfo(** )
Retrieves the last Win32&#174 Internet function error description or server response on the thread calling this function.

## [win32inet](#README.md#win32inet).InternetGoOnline

 **InternetGoOnline( *Url*  *, Parent*  *, Flags* ** )
Prompts the user for permission to initiate connection to a URL.

#### Parameters


     *Url* : string

    Web site to connect to

     *Parent=None* : int

    Handle to parent window

     *Flags=0* : int

    INTERNET_GOONLINE_REFRESH is only available flag

## [win32inet](#README.md#win32inet).InternetOpen

 **InternetOpen( *agent*  *, proxyName*  *, proxyBypass*  *, flags* ** )
Initializes an application's use of the Microsoft&#174 Win32&#174 Internet functions.

#### Parameters


     *agent* : string

    A string that contains the name of the application 

or entity calling the Internet functions. This name is used as the user 

agent in the HTTP protocol.

     *proxyName* : string

    

     *proxyBypass* : string

    

     *flags* : int

    Combination of INTERNET_FLAG_ASYNC,INTERNET_FLAG_FROM_CACHE, or INTERNET_FLAG_OFFLINE

## [win32inet](#README.md#win32inet).InternetOpenUrl

[PyHINTERNET](#README.md#PyHINTERNET)= **InternetOpenUrl( *Internet*  *, Url*  *, Headers*  *, Flags*  *, Context* ** )
Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL.

#### Parameters


     *Internet* :[PyHINTERNET](#README.md#PyHINTERNET)

    Internet handle as returned by[win32inet::InternetOpen](#win32inet.md#win32inetInternetOpen)

     *Url* : string

    A string that contains the URL to begin reading.  Only URLs beginning with ftp:, gopher:, http:, or https: are supported.

     *Headers=None* : string

    a string&#09variable that contains the headers to be sent to the HTTP server.

     *Flags=0* : int

    INTERNET_FLAG_*

     *Context=None* : object

    An arbitrary object to be passed to the status callback function

#### Comments
Accepts keyword args.

#### Return Value
Returns None in async mode (Internet handle created with INTERNET_FLAG_ASYNC). 

When handle is created, it will be passed to callback function of parent handle.

## [win32inet](#README.md#win32inet).InternetQueryOption

object = **InternetQueryOption( *hInternet*  *, Option* ** )
Retrieves an option for an internet handle

#### Parameters


     *hInternet* :[PyHINTERNET](#README.md#PyHINTERNET)

    Internet handle, or None for global defaults

     *Option* : int

    INTERNET_OPTION_* value

 **Option**  **Returned type** INTERNET_OPTION_CALLBACKPython callback functionINTERNET_OPTION_CONTEXT_VALUEContext objectINTERNET_OPTION_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CODEPAGEInt - Codepage of host part of URLINTERNET_OPTION_CODEPAGE_PATHInt - Codepage for URLINTERNET_OPTION_CODEPAGE_EXTRAInt - Codepage for path part of URLINTERNET_OPTION_CONNECT_RETRIESInt - Number of time to try to reconnect to hostINTERNET_OPTION_CONNECT_TIMEOUTInt - Connection timeout in millisecondsINTERNET_OPTION_CONNECTED_STATEInt - Connection state, INTERNET_STATE_*INTERNET_OPTION_HANDLE_TYPEInt, INTERNET_HANDLE_TYPE_*INTERNET_OPTION_ERROR_MASKInt, combination of INTERNET_ERROR_MASK_*INTERNET_OPTION_EXTENDED_ERRORInt, ERROR_INTERNET_*INTERNET_OPTION_FROM_CACHE_TIMEOUTInt - Timeout in ms before cached copy is usedINTERNET_OPTION_IDNInt, INTERNET_FLAG_IDN_*INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVERIntINTERNET_OPTION_MAX_CONNS_PER_SERVERIntINTERNET_OPTION_READ_BUFFER_SIZEIntINTERNET_OPTION_WRITE_BUFFER_SIZEIntINTERNET_OPTION_REQUEST_FLAGSInt, combination of INTERNET_REQFLAG_*INTERNET_OPTION_REQUEST_PRIORITYIntINTERNET_OPTION_SECURITY_FLAGSInt, SECURITY_FLAG_*INTERNET_OPTION_SECURITY_KEY_BITNESSIntINTERNET_OPTION_BYPASS_EDITED_ENTRYBooleanINTERNET_OPTION_HTTP_DECODINGBooleanINTERNET_OPTION_IGNORE_OFFLINEBooleanINTERNET_OPTION_DATAFILE_NAMEString - Name of internet cache fileINTERNET_OPTION_USERNAMEString - Username passed to InternetConnectINTERNET_OPTION_PASSWORDString - Password passed to InternetConnectINTERNET_OPTION_PROXY_PASSWORDStringINTERNET_OPTION_PROXY_USERNAMEStringINTERNET_OPTION_SECONDARY_CACHE_KEYStringINTERNET_OPTION_SECURITY_CERTIFICATEStringINTERNET_OPTION_URLStringINTERNET_OPTION_USER_AGENTStringINTERNET_OPTION_CACHE_TIMESTAMPSdict - Expiration and last modified timesINTERNET_OPTION_HTTP_VERSIONdict - HTTP_VERSION_INFOINTERNET_OPTION_VERSIONdict - INTERNET_VERSION_INFOINTERNET_OPTION_PARENT_HANDLE[PyHINTERNET](#README.md#PyHINTERNET)INTERNET_OPTION_PROXYdict - INTERNET_PROXY_INFOINTERNET_OPTION_DIAGNOSTIC_SOCKET_INFONot yet supported (INTERNET_DIAGNOSTIC_SOCKET_INFO)INTERNET_OPTION_PER_CONNECTION_OPTIONNot yet supported (INTERNET_PER_CONN_OPTION_LIST)INTERNET_OPTION_SECURITY_CERTIFICATE_STRUCTNot yet supported (INTERNET_CERTIFICATE_INFO)INTERNET_OPTION_ALTER_IDENTITYNot supportedINTERNET_OPTION_ASYNCNot supportedINTERNET_OPTION_ASYNC_IDNot supportedINTERNET_OPTION_ASYNC_PRIORITYNot supportedINTERNET_OPTION_CACHE_STREAM_HANDLENot supportedINTERNET_OPTION_CALLBACK_FILTERNot supportedINTERNET_OPTION_CLIENT_CERT_CONTEXTNot supportedINTERNET_OPTION_DATA_RECEIVE_TIMEOUTNot supportedINTERNET_OPTION_DATA_SEND_TIMEOUTNot supportedINTERNET_OPTION_CONNECT_BACKOFFNot supportedINTERNET_OPTION_CONNECT_TIMENot supportedINTERNET_OPTION_DISABLE_AUTODIALNot supportedINTERNET_OPTION_DISCONNECTED_TIMEOUTNot supportedINTERNET_OPTION_IDENTITYNot supportedINTERNET_OPTION_IDLE_STATENot supportedINTERNET_OPTION_KEEP_CONNECTIONNot supportedINTERNET_OPTION_LISTEN_TIMEOUTNot supportedINTERNET_OPTION_OFFLINE_MODENot supportedINTERNET_OPTION_OFFLINE_SEMANTICSNot supportedINTERNET_OPTION_POLICYNot supportedINTERNET_OPTION_RECEIVE_THROUGHPUTNot supportedINTERNET_OPTION_REMOVE_IDENTITYNot supportedINTERNET_OPTION_SEND_THROUGHPUTNot supportedINTERNET_OPTION_DATAFILE_EXTOnly valid for InternetSetOptionINTERNET_OPTION_DIGEST_AUTH_UNLOADOnly valid for InternetSetOptionINTERNET_OPTION_END_BROWSER_SESSIONOnly valid for InternetSetOptionINTERNET_OPTION_REFRESHOnly valid for InternetSetOptionINTERNET_OPTION_RESET_URLCACHE_SESSIONOnly valid for InternetSetOptionINTERNET_OPTION_SETTINGS_CHANGEDOnly valid for InternetSetOption
#### Win32 API References


    Search for *InternetQueryOption* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InternetQueryOption),[google](#README.md#http://www.google.com/search?q=InternetQueryOption)or[google groups](#README.md#http://groups.google.com/groups?q=InternetQueryOption).

#### Return Value
The type of object returned is dependent on the option requested

## [win32inet](#README.md#win32inet).InternetReadFile

string = **InternetReadFile( *hInternet*  *, size* ** )
Reads data from a handle opened by the[win32inet::InternetOpenUrl](#win32inet.md#win32inetInternetOpenUrl),[win32inet::FtpOpenFile](#win32inet.md#win32inetFtpOpenFile), **win32inet::GopherOpenFile** , or **win32inet::HttpOpenRequest** function.

#### Parameters


     *hInternet* :[PyHINTERNET](#README.md#PyHINTERNET)

    

     *size* : int

    Number of bytes to read.

#### Return Value
The result will be a string of zero bytes when the end is reached.

## [win32inet](#README.md#win32inet).InternetSetCookie

 **InternetSetCookie( *url*  *, lpszCookieName*  *, data* ** )
Creates a cookie associated with the specified URL.

#### Parameters


     *url* : string

    

     *lpszCookieName* : string

    

     *data* : string

    

## [win32inet](#README.md#win32inet).InternetSetOption

 **InternetSetOption( *hInternet*  *, Option*  *, Buffer* ** )
Sets an option for an internet handle

#### Parameters


     *hInternet* :[PyHINTERNET](#README.md#PyHINTERNET)

    Internet handle, or None for global defaults

     *Option* : int

    The option to set, INTERNET_OPTION_*

     *Buffer* : object

    Type is dependent on Option

 **Option**  **Type of input object** INTERNET_OPTION_CALLBACKPython function called on status changeINTERNET_OPTION_CONTEXT_VALUEAny Python object to be passed to callback functionINTERNET_OPTION_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CODEPAGEInt - Codepage of host part of URLINTERNET_OPTION_CODEPAGE_PATHCodepage for URLINTERNET_OPTION_CODEPAGE_EXTRAInt - Codepage for path part of URLINTERNET_OPTION_CONNECT_RETRIESInt - Number of time to try to reconnect to hostINTERNET_OPTION_CONNECT_TIMEOUTInt - Connection timeout in millisecondsINTERNET_OPTION_CONNECTED_STATEInt - Connection state, INTERNET_STATE_*INTERNET_OPTION_ERROR_MASKInt, combination of INTERNET_ERROR_MASK_*INTERNET_OPTION_FROM_CACHE_TIMEOUTInt - Timeout in ms before cached copy is usedINTERNET_OPTION_IDNInt, INTERNET_FLAG_IDN_*INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVERIntINTERNET_OPTION_MAX_CONNS_PER_SERVERIntINTERNET_OPTION_READ_BUFFER_SIZEIntINTERNET_OPTION_WRITE_BUFFER_SIZEIntINTERNET_OPTION_REQUEST_PRIORITYIntINTERNET_OPTION_DIGEST_AUTH_UNLOADNoneINTERNET_OPTION_END_BROWSER_SESSIONNoneINTERNET_OPTION_REFRESHNoneINTERNET_OPTION_RESET_URLCACHE_SESSIONNoneINTERNET_OPTION_SETTINGS_CHANGEDNoneINTERNET_OPTION_BYPASS_EDITED_ENTRYBooleanINTERNET_OPTION_HTTP_DECODINGBooleanINTERNET_OPTION_IGNORE_OFFLINEBooleanINTERNET_OPTION_USERNAMEString - Username passed to InternetConnectINTERNET_OPTION_PASSWORDString - Password passed to InternetConnectINTERNET_OPTION_PROXY_PASSWORDStringINTERNET_OPTION_PROXY_USERNAMEStringINTERNET_OPTION_SECONDARY_CACHE_KEYStringINTERNET_OPTION_USER_AGENTStringINTERNET_OPTION_DATAFILE_EXTString - Extension to use for download cache fileINTERNET_OPTION_PROXYDict representing INTERNET_PROXY_INFO structINTERNET_OPTION_HTTP_VERSIONNot yet supported - HTTP_VERSION_INFOINTERNET_OPTION_PER_CONNECTION_OPTIONNot yet supported (INTERNET_PER_CONN_OPTION_LIST)INTERNET_OPTION_ALTER_IDENTITYNot supportedINTERNET_OPTION_ASYNCNot supportedINTERNET_OPTION_ASYNC_IDNot supportedINTERNET_OPTION_ASYNC_PRIORITYNot supportedINTERNET_OPTION_CACHE_STREAM_HANDLENot supportedINTERNET_OPTION_CALLBACK_FILTERNot supportedINTERNET_OPTION_CLIENT_CERT_CONTEXTNot supportedINTERNET_OPTION_DATA_RECEIVE_TIMEOUTNot supportedINTERNET_OPTION_DATA_SEND_TIMEOUTNot supportedINTERNET_OPTION_CONNECT_BACKOFFNot supportedINTERNET_OPTION_CONNECT_TIMENot supportedINTERNET_OPTION_DISABLE_AUTODIALNot supportedINTERNET_OPTION_DISCONNECTED_TIMEOUTNot supportedINTERNET_OPTION_IDENTITYNot supportedINTERNET_OPTION_IDLE_STATENot supportedINTERNET_OPTION_KEEP_CONNECTIONNot supportedINTERNET_OPTION_LISTEN_TIMEOUTNot supportedINTERNET_OPTION_OFFLINE_MODENot supportedINTERNET_OPTION_OFFLINE_SEMANTICSNot supportedINTERNET_OPTION_POLICYNot supportedINTERNET_OPTION_RECEIVE_THROUGHPUTNot supportedINTERNET_OPTION_REMOVE_IDENTITYNot supportedINTERNET_OPTION_SEND_THROUGHPUTNot supportedINTERNET_OPTION_CACHE_TIMESTAMPSOnly valid for InternetQueryOptionINTERNET_OPTION_HANDLE_TYPEOnly valid for InternetQueryOptionINTERNET_OPTION_DATAFILE_NAMEOnly valid for InternetQueryOptionINTERNET_OPTION_PARENT_HANDLEOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_CERTIFICATEOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_CERTIFICATE_STRUCTOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_FLAGSOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_KEY_BITNESSOnly valid for InternetQueryOptionINTERNET_OPTION_DIAGNOSTIC_SOCKET_INFOOnly valid for InternetQueryOptionINTERNET_OPTION_VERSIONOnly valid for InternetQueryOptionINTERNET_OPTION_EXTENDED_ERROROnly valid for InternetQueryOptionINTERNET_OPTION_REQUEST_FLAGSOnly valid for InternetQueryOptionINTERNET_OPTION_URLOnly valid for InternetQueryOption
#### Win32 API References


    Search for *InternetSetOption* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InternetSetOption),[google](#README.md#http://www.google.com/search?q=InternetSetOption)or[google groups](#README.md#http://groups.google.com/groups?q=InternetSetOption).

## [win32inet](#README.md#win32inet).InternetWriteFile

int = **InternetWriteFile( *File*  *, Buffer* ** )
Writes data to a handle opened by[win32inet::FtpOpenFile](#win32inet.md#win32inetFtpOpenFile).

#### Parameters


     *File* :[PyHINTERNET](#README.md#PyHINTERNET)

    Writeable internet&#09handle

     *Buffer* : string

    String or&#09buffer containing data to be written

## [win32inet](#README.md#win32inet).SetUrlCacheEntryGroup

 **SetUrlCacheEntryGroup( *UrlName*  *, Flags*  *, GroupId* ** )
Associates a cache entry with a group

#### Parameters


     *UrlName* : str

    Url whose cache is to be added to the group

     *Flags* : int

    INTERNET_CACHE_GROUP_ADD or INTERNET_CACHE_GROUP_REMOVE

     *GroupId* : int

    Id of a cache group

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *SetUrlCacheEntryGroup* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetUrlCacheEntryGroup),[google](#README.md#http://www.google.com/search?q=SetUrlCacheEntryGroup)or[google groups](#README.md#http://groups.google.com/groups?q=SetUrlCacheEntryGroup).

## [win32inet](#README.md#win32inet).SetUrlCacheGroupAttribute

 **SetUrlCacheGroupAttribute( *GroupId*  *, Attributes*  *, GroupInfo*  *, Flags* ** )
Changes the attributes of a cache group

#### Parameters


     *GroupId* : int

    Id of a cache group

     *Attributes* : int

    Bitmask of CACHEGROUP_ATTRIBUTE_* flags indicating which attributes to set

     *GroupInfo* : dict

    INTERNET_CACHE_GROUP_INFO dict as returned by[win32inet::GetUrlCacheGroupAttribute](#win32inet.md#win32inetGetUrlCacheGroupAttribute)

     *Flags=0* : int

    Reserved, use 0

#### Comments
Accepts keyword args

#### Win32 API References


    Search for *SetUrlCacheGroupAttribute* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetUrlCacheGroupAttribute),[google](#README.md#http://www.google.com/search?q=SetUrlCacheGroupAttribute)or[google groups](#README.md#http://groups.google.com/groups?q=SetUrlCacheGroupAttribute).

## [win32inet](#README.md#win32inet).WinHttpGetDefaultProxyConfiguration

[PyWINHTTP_PROXY_INFO](#PyWINHTTP.md#PyWINHTTPPROXY_INFO)= **WinHttpGetDefaultProxyConfiguration(** )
Retrieves the default WinHTTP proxy configuration from the registry.

## [win32inet](#README.md#win32inet).WinHttpGetIEProxyConfigForCurrentUser

tuple = **WinHttpGetIEProxyConfigForCurrentUser(** )
Obtains 

the Internet Explorer proxy configuration for the current user.

#### Win32 API References


    Search for *WinHttpGetIEProxyConfigForCurrentUser* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHttpGetIEProxyConfigForCurrentUser),[google](#README.md#http://www.google.com/search?q=WinHttpGetIEProxyConfigForCurrentUser)or[google groups](#README.md#http://groups.google.com/groups?q=WinHttpGetIEProxyConfigForCurrentUser).

    Search for *WINHTTP_CURRENT_USER_IE_PROXY_CONFIG* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WINHTTP.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WINHTTPCURRENT_USER_IE_PROXY_CONFIG),[google](#http://www.google.com/search?q=WINHTTP.md#http://www.google.com/search?q=WINHTTPCURRENT_USER_IE_PROXY_CONFIG)or[google groups](#http://groups.google.com/groups?q=WINHTTP.md#http://groups.google.com/groups?q=WINHTTPCURRENT_USER_IE_PROXY_CONFIG).

#### Return Value
The result is a windows WINHTTP_CURRENT_USER_IE_PROXY_CONFIG 

structure; a tuple of an int (bool) and 3 unicode strings 

(fAutoDetect, lpszAutoConfigUrl, lpszProxy, lpszProxyBypass).

## [win32inet](#README.md#win32inet).WinHttpGetProxyForUrl

[PyWINHTTP_PROXY_INFO](#PyWINHTTP.md#PyWINHTTPPROXY_INFO)= **WinHttpGetProxyForUrl( *handle*  *, url*  *, options* ** )
Obtains 

the Internet Explorer proxy configuration for the specified URL.

#### Parameters


     *handle* : **HANDLE** /int

    

     *url* : unicode/string

    

     *options* :[PyWINHTTP_AUTOPROXY_OPTIONS](#PyWINHTTP.md#PyWINHTTPAUTOPROXY_OPTIONS)

    

## [win32inet](#README.md#win32inet).WinHttpOpen

[PyHINTERNET](#README.md#PyHINTERNET)= **WinHttpOpen( *lpszUserAgent*  *, dwAccessType*  *, lpszProxyName*  *, lpszProxyBypass*  *, dwFlags* ** )
Opens a winhttp session.

#### Parameters


     *lpszUserAgent* : string

    

     *dwAccessType* : int

    

     *lpszProxyName* : string

    

     *lpszProxyBypass* : string

    

     *dwFlags* : int

    

#### Win32 API References


    Search for *WinHttpOpen* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHttpOpen),[google](#README.md#http://www.google.com/search?q=WinHttpOpen)or[google groups](#README.md#http://groups.google.com/groups?q=WinHttpOpen).