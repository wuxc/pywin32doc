# EXTENSION

## EXTENSION\_CONTROL\_BLOCK Object



A python representation of an ISAPI 

EXTENSION\_CONTROL\_BLOCK\.

#### Methods


  - [write](EXTENSION.md#extensioncontrol_block_write)

    A synonym for WriteClient, this allows you to 'print &gt&gt ecb'&nbsp;

  - [WriteClient](EXTENSION.md#extensioncontrol_block_writeclient)

    &nbsp;

  - [GetServerVariable](EXTENSION.md#extensioncontrol_block_getservervariable)

    &nbsp;

  - [ReadClient](EXTENSION.md#extensioncontrol_block_readclient)

    &nbsp;

  - [SendResponseHeaders](EXTENSION.md#extensioncontrol_block_sendresponseheaders)

    &nbsp;

  - [SetFlushFlag](EXTENSION.md#extensioncontrol_block_setflushflag)

    &nbsp;

  - [TransmitFile](EXTENSION.md#extensioncontrol_block_transmitfile)

    &nbsp;

  - [MapURLToPath](EXTENSION.md#extensioncontrol_block_mapurltopath)

    &nbsp;

  - [DoneWithSession](EXTENSION.md#extensioncontrol_block_donewithsession)

    &nbsp;

  - [close](EXTENSION.md#extensioncontrol_block_close)

    A synonym for DoneWithSession\.&nbsp;

  - [Redirect](EXTENSION.md#extensioncontrol_block_redirect)

    &nbsp;

  - [IsKeepAlive](EXTENSION.md#extensioncontrol_block_iskeepalive)

    &nbsp;

  - [GetAnonymousToken](EXTENSION.md#extensioncontrol_block_getanonymoustoken)

    Calls ServerSupportFunction with HSE\_REQ\_GET\_ANONYMOUS\_TOKEN or HSE\_REQ\_GET\_UNICODE\_ANONYMOUS\_TOKEN&nbsp;

  - [GetImpersonationToken](EXTENSION.md#extensioncontrol_block_getimpersonationtoken)

    &nbsp;

  - [IsKeepConn](EXTENSION.md#extensioncontrol_block_iskeepconn)

    Calls ServerSupportFunction with HSE\_REQ\_IS\_KEEP\_CONN&nbsp;

  - [ExecURL](EXTENSION.md#extensioncontrol_block_execurl)

    Calls ServerSupportFunction with HSE\_REQ\_EXEC\_URL&nbsp;

  - [GetExecURLStatus](EXTENSION.md#extensioncontrol_block_getexecurlstatus)

    Calls ServerSupportFunction with HSE\_REQ\_GET\_EXEC\_URL\_STATUS&nbsp;

  - [IOCompletion](EXTENSION.md#extensioncontrol_block_iocompletion)

    Calls ServerSupportFunction with HSE\_REQ\_IO\_COMPLETION&nbsp;

  - [ReportUnhealthy](EXTENSION.md#extensioncontrol_block_reportunhealthy)

    Calls ServerSupportFunction with HSE\_REQ\_REPORT\_UNHEALTHY&nbsp;

  - [IOCallback](EXTENSION.md#extensioncontrol_block_iocallback)

    A placeholder for a user-supplied callback function\.&nbsp;

#### Properties

  - integer Version
    Version info of this spec \(read-only\)

  - int TotalBytes
    Total bytes indicated from client

  - int AvailableBytes
    Available number of bytes

  - int HttpStatusCode
    The status of the current transaction when the request is completed\.

  - bytes Method
    REQUEST\_METHOD

  - long ConnID
    Context number \(read-only\)

  - bytes QueryString
    QUERY\_STRING

  - bytes PathInfo
    PATH\_INFO

  - bytes PathTranslated
    PATH\_TRANSLATED

  - bytes AvailableData
    Pointer to cbAvailable bytes

  - bytes ContentType
    Content type of client data

  - bytes LogData
    log data string

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.DoneWithSession

DoneWithSession\(status\)
Calls ServerSupportFunction with HSE\_REQ\_DONE\_WITH\_SESSION

#### Parameters


  - status=HSE\_STATUS\_SUCCESS : int

    An optional status\. 

HSE\_STATUS\_SUCCESS\_AND\_KEEP\_CONN is supported by IIS to keep the connection alive\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.ExecURL



int =ExecURL\(url, method, clientHeaders, info, entity, flags\)
Calls ServerSupportFunction with HSE\_REQ\_EXEC\_URL

#### Parameters


  - url : string

    

  - method : string

    

  - clientHeaders : string

    

  - info : object

    Must be None

  - entity : object

    Must be None

  - flags : int

    

#### Comments


This function is only available in IIS6 and later\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.GetAnonymousToken



int =GetAnonymousToken\(metabase\_path\)
Calls ServerSupportFunction with HSE\_REQ\_GET\_ANONYMOUS\_TOKEN or HSE\_REQ\_GET\_UNICODE\_ANONYMOUS\_TOKEN

#### Parameters


  - metabase\_path : string/unicode

    

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.GetExecURLStatus



int =GetExecURLStatus\(\)
Calls ServerSupportFunction with HSE\_REQ\_GET\_EXEC\_URL\_STATUS

#### Win32 API References


  - Search forHSE\_EXEC\_URL\_STATUS at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=HSE.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=hseexec_url_status),[google](http://www.google.com/search?q=HSE.md#http://www.google.com/search?q=hseexec_url_status) or[google groups](http://groups.google.com/groups?q=HSE.md#http://groups.google.com/groups?q=hseexec_url_status)\.

#### Return Value
The result of a tuple of 3 integers - \(uHttpStatusCode, uHttpSubStatus, dwWin32Error\)

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.GetImpersonationToken



int =GetImpersonationToken\(\)
Calls ServerSupportFunction with HSE\_REQ\_GET\_IMPERSONATION\_TOKEN

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.GetServerVariable



string =GetServerVariable\(variable, default\)


#### Parameters


  - variable : string

    

  - default : object

    If specified, the function will return this 

value instead of raising an error if the variable could not be fetched\.

#### Return Value
The result is a string object, unless the server variable name 

begins with 'UNICODE\_', in which case it is a unicode object - see the 

ISAPI docs for more details\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.IOCallback



None =IOCallback\(ecb, arg, cbIO, dwError\)
A placeholder for a user-supplied callback function\.

#### Parameters


  - ecb :[EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)

    The extension control block that is associated with the current, active request\.

  - arg : object

    The user-supplied argument supplied to the[EXTENSION\_CONTROL\_BLOCK::IOCompletion](EXTENSION.md#extensioncontrol_block_iocompletion) function\.

  - cbIO : int

    An integer that contains the number of bytes of I/O in the last call\.

  - dwError : int

    The error code returned\.

#### Comments


This is not a function you can call, it describes the signature of 

the callback function supplied to the[EXTENSION\_CONTROL\_BLOCK::IOCompletion](EXTENSION.md#extensioncontrol_block_iocompletion) 

function\.

#### Return Value
The result of this function is ignored\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.IOCompletion



int =IOCompletion\(func, arg\)
Set a callback that will be used for handling asynchronous I/O operations\.

#### Parameters


  - func : callable

    The function to call, as described by the[EXTENSION\_CONTROL\_BLOCK::IOCallback](EXTENSION.md#extensioncontrol_block_iocallback) method\.

  - arg=None : object

    Any object which will be supplied as an argument to the callback function\.

#### Comments


If you call this multiple times, the previous callback will be discarded\.


A reference to the callback and args are held until[EXTENSION\_CONTROL\_BLOCK::DoneWithSession](EXTENSION.md#extensioncontrol_block_donewithsession) is called\. If the callback 

function fails, DoneWithSession\(HSE\_STATUS\_ERROR\) will automatically be 

called and no further callbacks for the ECB will be made\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.IsKeepAlive

IsKeepAlive\(\)


#### Comments


This method simply checks a HTTP\_CONNECTION header for 'keep-alive', 

making it fairly useless\.  SeeEXTENSION\_CONTROL\_BLOCK::IsKeepCon

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.IsKeepConn



int =IsKeepConn\(\)
Calls ServerSupportFunction with HSE\_REQ\_IS\_KEEP\_CONN

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.MapURLToPath

MapURLToPath\(\)
Calls ServerSupportFunction with HSE\_REQ\_MAP\_URL\_TO\_PATH

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.ReadClient



string =ReadClient\(nbytes\)


#### Parameters


  - nbytes : int

    Default is to read all available data\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.Redirect

Redirect\(url\)
Calls ServerSupportFunction with HSE\_REQ\_SEND\_URL\_REDIRECT\_RESP

#### Parameters


  - url : string

    The URL to redirect to

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.ReportUnhealthy



int =ReportUnhealthy\(reason\)
Calls ServerSupportFunction with HSE\_REQ\_REPORT\_UNHEALTHY

#### Parameters


  - reason=None : string

    An optional reason to be written to the log\.

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.SendResponseHeaders

SendResponseHeaders\(reply, headers, keepAlive\)
Calls ServerSupportFunction with HSE\_REQ\_SEND\_RESPONSE\_HEADER\_EX

#### Parameters


  - reply : string

    

  - headers : string

    

  - keepAlive=False : bool

    

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.SetFlushFlag

SetFlushFlag\(flag\)
Calls ServerSupportFunction with HSE\_REQ\_SET\_FLUSH\_FLAG\.

#### Parameters


  - flag : bool

    

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.TransmitFile



int =TransmitFile\(callback, param, hFile, statusCode, BytesToWrite, Offset, head, tail, flags\)
Calls ServerSupportFunction with HSE\_REQ\_TRANSMIT\_FILE

#### Parameters


  - callback : callable

    

  - param : object

    Any object - passed as 2nd arg to callback\.

  - hFile : int

    

  - statusCode : string

    

  - BytesToWrite : int

    

  - Offset : int

    

  - head : string

    

  - tail : string

    

  - flags : int

    

#### Comments


The callback is called with 4 args - \(PyECB

, param, cbIO, dwErrCode\)

## [EXTENSION\_CONTROL\_BLOCK](EXTENSION.md#extensioncontrol_block)\.WriteClient



int =WriteClient\(data, reserved\)


#### Parameters


  - data : string/buffer

    The data to write

  - reserved=0 : int

    

#### Return Value
the result is the number of bytes written\.