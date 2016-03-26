# HTTP

## HTTP_FILTER_AUTHENT Object

A Python representation of an ISAPI 

HTTP_FILTER_AUTHENT structure.

#### Properties

  -  __string User__ 
    

  -  __string Password__ 
    

## HTTP_FILTER_CONTEXT Object

A Python representation of an ISAPI 

HTTP_FILTER_CONTEXT structure.

#### Methods


  - [GetData](HTTP.md#httpfilter_context_getdata)

    &nbsp;

  - [GetServerVariable](HTTP.md#httpfilter_context_getservervariable)

    &nbsp;

  - [WriteClient](HTTP.md#httpfilter_context_writeclient)

    &nbsp;

  - [AddResponseHeaders](HTTP.md#httpfilter_context_addresponseheaders)

    Specifies a response header for IIS to send to the client.&nbsp;

  - [write](HTTP.md#httpfilter_context_write)

    A synonym for WriteClient, this allows you to 'print &gt&gt fc'&nbsp;

  - [SendResponseHeader](HTTP.md#httpfilter_context_sendresponseheader)

    &nbsp;

  - [DisableNotifications](HTTP.md#httpfilter_context_disablenotifications)

    &nbsp;

#### Properties

  -  __int Revision__ 
    (read-only)

  -  __bool fIsSecurePort__ 
    (read-only)

  -  __int NotificationType__ 
    (read-only)

  -  __object FilterContext__ 
    Any object you wish to associate with the request.

## [HTTP_FILTER_CONTEXT](HTTP.md#httpfilter_context).AddResponseHeaders

 __AddResponseHeaders( *data*  *, reserverd* __ )


#### Parameters


  -  *data* : string

    

  -  *reserverd=0* : int

    

## [HTTP_FILTER_CONTEXT](HTTP.md#httpfilter_context).DisableNotifications

 __DisableNotifications( *flags* __ )


#### Parameters


  -  *flags* : int

    

## [HTTP_FILTER_CONTEXT](HTTP.md#httpfilter_context).GetData

object = __GetData(__ )
Obtains the data passed to 

The HttpFilterProc function.  This is not techinally part of the 

HTTP_FILTER_CONTEXT structure, but packaged here for convenience.

#### Return Value
The result depends on the value of __HTTP_FILTER_CONTEXT::NotificationType__ 


## [HTTP_FILTER_CONTEXT](HTTP.md#httpfilter_context).GetServerVariable

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

## [HTTP_FILTER_CONTEXT](HTTP.md#httpfilter_context).SendResponseHeader

 __SendResponseHeader( *status*  *, header* __ )


#### Parameters


  -  *status* : string

    

  -  *header* : string

    

## [HTTP_FILTER_CONTEXT](HTTP.md#httpfilter_context).WriteClient

 __WriteClient( *data*  *, reserverd* __ )


#### Parameters


  -  *data* : string

    

  -  *reserverd=0* : int

    

## HTTP_FILTER_LOG Object

A Python representation of an ISAPI 

HTTP_FILTER_LOG structure.

#### Properties

  -  __string ClientHostName__ 
    

  -  __string ClientUserName__ 
    

  -  __string ServerName__ 
    

  -  __string Operation__ 
    

  -  __string Target__ 
    

  -  __string Parameters__ 
    

  -  __int HttpStatus__ 
    

  -  __int HttpStatus__ 
    

## HTTP_FILTER_PREPROC_HEADERS Object

A Python representation of an ISAPI 

HTTP_FILTER_PREPROC_HEADERS structure.

#### Methods


  - [GetHeader](HTTP.md#httpfilter_preproc_headers_getheader)

    &nbsp;

  - [SetHeader](HTTP.md#httpfilter_preproc_headers_setheader)

    &nbsp;

  - [AddHeader](HTTP.md#httpfilter_preproc_headers_addheader)

    &nbsp;

## [HTTP_FILTER_PREPROC_HEADERS](HTTP.md#httpfilter_preproc_headers).AddHeader

 __AddHeader(__ )


## [HTTP_FILTER_PREPROC_HEADERS](HTTP.md#httpfilter_preproc_headers).GetHeader

string = __GetHeader( *header*  *, default* __ )


#### Parameters


  -  *header* : string

    

  -  *default* : object

    If specified, this will be returned on error.

## [HTTP_FILTER_PREPROC_HEADERS](HTTP.md#httpfilter_preproc_headers).SetHeader

 __SetHeader( *name*  *, val* __ )


#### Parameters


  -  *name* : string

    

  -  *val* : string

    

## HTTP_FILTER_RAW_DATA Object

A Python representation of an ISAPI 

HTTP_FILTER_RAW_DATA structure.

#### Properties

  -  __string InData__ 
    

## HTTP_FILTER_URL_MAP Object

A Python representation of an ISAPI 

HTTP_FILTER_URL_MAP structure.

#### Properties

  -  __string URL__ 
    

  -  __string PhysicalPath__ 
    

## HTTP_FILTER_VERSION Object

A Python interface to the ISAPI HTTP_FILTER_VERSION 

structure.

#### Properties

  -  __int ServerFilterVersion__ 
    (read-only)

  -  __int FilterVersion__ 
    

  -  __int Flags__ 
    

  -  __string FilterDesc__ 
    