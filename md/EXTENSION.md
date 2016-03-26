# EXTENSION

## EXTENSION_CONTROL_BLOCK Object

A python representation of an ISAPI 

EXTENSION_CONTROL_BLOCK.

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

    A synonym for DoneWithSession.&nbsp;

  - [Redirect](EXTENSION.md#extensioncontrol_block_redirect)

    &nbsp;

  - [IsKeepAlive](EXTENSION.md#extensioncontrol_block_iskeepalive)

    &nbsp;

  - [GetAnonymousToken](EXTENSION.md#extensioncontrol_block_getanonymoustoken)

    Calls ServerSupportFunction with HSE_REQ_GET_ANONYMOUS_TOKEN or HSE_REQ_GET_UNICODE_ANONYMOUS_TOKEN&nbsp;

  - [GetImpersonationToken](EXTENSION.md#extensioncontrol_block_getimpersonationtoken)

    &nbsp;

  - [IsKeepConn](EXTENSION.md#extensioncontrol_block_iskeepconn)

    Calls ServerSupportFunction with HSE_REQ_IS_KEEP_CONN&nbsp;

  - [ExecURL](EXTENSION.md#extensioncontrol_block_execurl)

    Calls ServerSupportFunction with HSE_REQ_EXEC_URL&nbsp;

  - [GetExecURLStatus](EXTENSION.md#extensioncontrol_block_getexecurlstatus)

    Calls ServerSupportFunction with HSE_REQ_GET_EXEC_URL_STATUS&nbsp;

  - [IOCompletion](EXTENSION.md#extensioncontrol_block_iocompletion)

    Calls ServerSupportFunction with HSE_REQ_IO_COMPLETION&nbsp;

  - [ReportUnhealthy](EXTENSION.md#extensioncontrol_block_reportunhealthy)

    Calls ServerSupportFunction with HSE_REQ_REPORT_UNHEALTHY&nbsp;

  - [IOCallback](EXTENSION.md#extensioncontrol_block_iocallback)

    A placeholder for a user-supplied callback function.&nbsp;

#### Properties

  -  __integer Version__ 
    Version info of this spec (read-only)

  -  __int TotalBytes__ 
    Total bytes indicated from client

  -  __int AvailableBytes__ 
    Available number of bytes

  -  __int HttpStatusCode__ 
    The status of the current transaction when the request is completed.

  -  __bytes Method__ 
    REQUEST_METHOD

  -  __long ConnID__ 
    Context number (read-only)

  -  __bytes QueryString__ 
    QUERY_STRING

  -  __bytes PathInfo__ 
    PATH_INFO

  -  __bytes PathTranslated__ 
    PATH_TRANSLATED

  -  __bytes AvailableData__ 
    Pointer to cbAvailable bytes

  -  __bytes ContentType__ 
    Content type of client data

  -  __bytes LogData__ 
    log data string

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).DoneWithSession

 __DoneWithSession( *status* __ )
Calls ServerSupportFunction with HSE_REQ_DONE_WITH_SESSION

#### Parameters


  -  *status=HSE_STATUS_SUCCESS* : int

    An optional status. 

HSE_STATUS_SUCCESS_AND_KEEP_CONN is supported by IIS to keep the connection alive.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).ExecURL

int = __ExecURL( *url*  *, method*  *, clientHeaders*  *, info*  *, entity*  *, flags* __ )
Calls ServerSupportFunction with HSE_REQ_EXEC_URL

#### Parameters


  -  *url* : string

    

  -  *method* : string

    

  -  *clientHeaders* : string

    

  -  *info* : object

    Must be None

  -  *entity* : object

    Must be None

  -  *flags* : int

    

#### Comments
This function is only available in IIS6 and later.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).GetAnonymousToken

int = __GetAnonymousToken( *metabase_path* __ )
Calls ServerSupportFunction with HSE_REQ_GET_ANONYMOUS_TOKEN or HSE_REQ_GET_UNICODE_ANONYMOUS_TOKEN

#### Parameters


  -  *metabase_path* : string/unicode

    

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).GetExecURLStatus

int = __GetExecURLStatus(__ )
Calls ServerSupportFunction with HSE_REQ_GET_EXEC_URL_STATUS

#### Win32 API References


  - Search for *HSE_EXEC_URL_STATUS* at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=HSE.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=hseexec_url_status),[google](http://www.google.com/search?q=HSE.md#http://www.google.com/search?q=hseexec_url_status)or[google groups](http://groups.google.com/groups?q=HSE.md#http://groups.google.com/groups?q=hseexec_url_status).

#### Return Value
The result of a tuple of 3 integers - (uHttpStatusCode, uHttpSubStatus, dwWin32Error)

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).GetImpersonationToken

int = __GetImpersonationToken(__ )
Calls ServerSupportFunction with HSE_REQ_GET_IMPERSONATION_TOKEN

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).GetServerVariable

string = __GetServerVariable( *variable*  *, default* __ )


#### Parameters


  -  *variable* : string

    

  -  *default* : object

    If specified, the function will return this 

value instead of raising an error if the variable could not be fetched.

#### Return Value
The result is a string object, unless the server variable name 

begins with 'UNICODE_', in which case it is a unicode object - see the 

ISAPI docs for more details.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).IOCallback

None = __IOCallback( *ecb*  *, arg*  *, cbIO*  *, dwError* __ )
A placeholder for a user-supplied callback function.

#### Parameters


  -  *ecb* :[EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block)

    The extension control block that is associated with the current, active request.

  -  *arg* : object

    The user-supplied argument supplied to the[EXTENSION_CONTROL_BLOCK::IOCompletion](EXTENSION.md#extensioncontrol_block_iocompletion)function.

  -  *cbIO* : int

    An integer that contains the number of bytes of I/O in the last call.

  -  *dwError* : int

    The error code returned.

#### Comments
This is not a function you can call, it describes the signature of 

the callback function supplied to the[EXTENSION_CONTROL_BLOCK::IOCompletion](EXTENSION.md#extensioncontrol_block_iocompletion)function.

#### Return Value
The result of this function is ignored.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).IOCompletion

int = __IOCompletion( *func*  *, arg* __ )
Set a callback that will be used for handling asynchronous I/O operations.

#### Parameters


  -  *func* : callable

    The function to call, as described by the[EXTENSION_CONTROL_BLOCK::IOCallback](EXTENSION.md#extensioncontrol_block_iocallback)method.

  -  *arg=None* : object

    Any object which will be supplied as an argument to the callback function.

#### Comments
If you call this multiple times, the previous callback will be discarded.
A reference to the callback and args are held until[EXTENSION_CONTROL_BLOCK::DoneWithSession](EXTENSION.md#extensioncontrol_block_donewithsession)is called. If the callback 

function fails, DoneWithSession(HSE_STATUS_ERROR) will automatically be 

called and no further callbacks for the ECB will be made.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).IsKeepAlive

 __IsKeepAlive(__ )


#### Comments
This method simply checks a HTTP_CONNECTION header for 'keep-alive', 

making it fairly useless.  See __EXTENSION_CONTROL_BLOCK::IsKeepCon__ 

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).IsKeepConn

int = __IsKeepConn(__ )
Calls ServerSupportFunction with HSE_REQ_IS_KEEP_CONN

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).MapURLToPath

 __MapURLToPath(__ )
Calls ServerSupportFunction with HSE_REQ_MAP_URL_TO_PATH

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).ReadClient

string = __ReadClient( *nbytes* __ )


#### Parameters


  -  *nbytes* : int

    Default is to read all available data.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).Redirect

 __Redirect( *url* __ )
Calls ServerSupportFunction with HSE_REQ_SEND_URL_REDIRECT_RESP

#### Parameters


  -  *url* : string

    The URL to redirect to

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).ReportUnhealthy

int = __ReportUnhealthy( *reason* __ )
Calls ServerSupportFunction with HSE_REQ_REPORT_UNHEALTHY

#### Parameters


  -  *reason=None* : string

    An optional reason to be written to the log.

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).SendResponseHeaders

 __SendResponseHeaders( *reply*  *, headers*  *, keepAlive* __ )
Calls ServerSupportFunction with HSE_REQ_SEND_RESPONSE_HEADER_EX

#### Parameters


  -  *reply* : string

    

  -  *headers* : string

    

  -  *keepAlive=False* : bool

    

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).SetFlushFlag

 __SetFlushFlag( *flag* __ )
Calls ServerSupportFunction with HSE_REQ_SET_FLUSH_FLAG.

#### Parameters


  -  *flag* : bool

    

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).TransmitFile

int = __TransmitFile( *callback*  *, param*  *, hFile*  *, statusCode*  *, BytesToWrite*  *, Offset*  *, head*  *, tail*  *, flags* __ )
Calls ServerSupportFunction with HSE_REQ_TRANSMIT_FILE

#### Parameters


  -  *callback* : callable

    

  -  *param* : object

    Any object - passed as 2nd arg to callback.

  -  *hFile* : int

    

  -  *statusCode* : string

    

  -  *BytesToWrite* : int

    

  -  *Offset* : int

    

  -  *head* : string

    

  -  *tail* : string

    

  -  *flags* : int

    

#### Comments
The callback is called with 4 args - ( __PyECB__ , param, cbIO, dwErrCode)

## [EXTENSION_CONTROL_BLOCK](EXTENSION.md#extensioncontrol_block).WriteClient

int = __WriteClient( *data*  *, reserved* __ )


#### Parameters


  -  *data* : string/buffer

    The data to write

  -  *reserved=0* : int

    

#### Return Value
the result is the number of bytes written.