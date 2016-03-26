# HTTP

## HTTP\_FILTER\_AUTHENT Object

A Python representation of an ISAPI 

HTTP\_FILTER\_AUTHENT structure\.

#### Properties

  -  **string User** 
    

  -  **string Password** 
    

## HTTP\_FILTER\_CONTEXT Object

A Python representation of an ISAPI 

HTTP\_FILTER\_CONTEXT structure\.

#### Methods


  - [GetData](HTTP.md#httpfilter_context_getdata)

    &nbsp;

  - [GetServerVariable](HTTP.md#httpfilter_context_getservervariable)

    &nbsp;

  - [WriteClient](HTTP.md#httpfilter_context_writeclient)

    &nbsp;

  - [AddResponseHeaders](HTTP.md#httpfilter_context_addresponseheaders)

    Specifies a response header for IIS to send to the client\.&nbsp;

  - [write](HTTP.md#httpfilter_context_write)

    A synonym for WriteClient, this allows you to 'print &gt&gt fc'&nbsp;

  - [SendResponseHeader](HTTP.md#httpfilter_context_sendresponseheader)

    &nbsp;

  - [DisableNotifications](HTTP.md#httpfilter_context_disablenotifications)

    &nbsp;

#### Properties

  -  **int Revision** 
    \(read-only\)

  -  **bool fIsSecurePort** 
    \(read-only\)

  -  **int NotificationType** 
    \(read-only\)

  -  **object FilterContext** 
    Any object you wish to associate with the request\.

## [HTTP\_FILTER\_CONTEXT](HTTP.md#httpfilter_context)\.AddResponseHeaders

 **AddResponseHeaders\( *data*  *, reserverd* ** \)


#### Parameters


  -  *data* : string

    

  -  *reserverd\=0* : int

    

## [HTTP\_FILTER\_CONTEXT](HTTP.md#httpfilter_context)\.DisableNotifications

 **DisableNotifications\( *flags* ** \)


#### Parameters


  -  *flags* : int

    

## [HTTP\_FILTER\_CONTEXT](HTTP.md#httpfilter_context)\.GetData

object \= **GetData\(** \)
Obtains the data passed to 

The HttpFilterProc function\.  This is not techinally part of the 

HTTP\_FILTER\_CONTEXT structure, but packaged here for convenience\.

#### Return Value
The result depends on the value of **HTTP\_FILTER\_CONTEXT::NotificationType** 


## [HTTP\_FILTER\_CONTEXT](HTTP.md#httpfilter_context)\.GetServerVariable

string \= **GetServerVariable\( *variable*  *, default* ** \)


#### Parameters


  -  *variable* : string

    

  -  *default* : object

    If specified, the function will return this 

value instead of raising an error if the variable could not be fetched\.

#### Return Value
The result is a string object, unless the server variable name 

begins with 'UNICODE\_', in which case it is a unicode object - see the 

ISAPI docs for more details\.

## [HTTP\_FILTER\_CONTEXT](HTTP.md#httpfilter_context)\.SendResponseHeader

 **SendResponseHeader\( *status*  *, header* ** \)


#### Parameters


  -  *status* : string

    

  -  *header* : string

    

## [HTTP\_FILTER\_CONTEXT](HTTP.md#httpfilter_context)\.WriteClient

 **WriteClient\( *data*  *, reserverd* ** \)


#### Parameters


  -  *data* : string

    

  -  *reserverd\=0* : int

    

## HTTP\_FILTER\_LOG Object

A Python representation of an ISAPI 

HTTP\_FILTER\_LOG structure\.

#### Properties

  -  **string ClientHostName** 
    

  -  **string ClientUserName** 
    

  -  **string ServerName** 
    

  -  **string Operation** 
    

  -  **string Target** 
    

  -  **string Parameters** 
    

  -  **int HttpStatus** 
    

  -  **int HttpStatus** 
    

## HTTP\_FILTER\_PREPROC\_HEADERS Object

A Python representation of an ISAPI 

HTTP\_FILTER\_PREPROC\_HEADERS structure\.

#### Methods


  - [GetHeader](HTTP.md#httpfilter_preproc_headers_getheader)

    &nbsp;

  - [SetHeader](HTTP.md#httpfilter_preproc_headers_setheader)

    &nbsp;

  - [AddHeader](HTTP.md#httpfilter_preproc_headers_addheader)

    &nbsp;

## [HTTP\_FILTER\_PREPROC\_HEADERS](HTTP.md#httpfilter_preproc_headers)\.AddHeader

 **AddHeader\(** \)


## [HTTP\_FILTER\_PREPROC\_HEADERS](HTTP.md#httpfilter_preproc_headers)\.GetHeader

string \= **GetHeader\( *header*  *, default* ** \)


#### Parameters


  -  *header* : string

    

  -  *default* : object

    If specified, this will be returned on error\.

## [HTTP\_FILTER\_PREPROC\_HEADERS](HTTP.md#httpfilter_preproc_headers)\.SetHeader

 **SetHeader\( *name*  *, val* ** \)


#### Parameters


  -  *name* : string

    

  -  *val* : string

    

## HTTP\_FILTER\_RAW\_DATA Object

A Python representation of an ISAPI 

HTTP\_FILTER\_RAW\_DATA structure\.

#### Properties

  -  **string InData** 
    

## HTTP\_FILTER\_URL\_MAP Object

A Python representation of an ISAPI 

HTTP\_FILTER\_URL\_MAP structure\.

#### Properties

  -  **string URL** 
    

  -  **string PhysicalPath** 
    

## HTTP\_FILTER\_VERSION Object

A Python interface to the ISAPI HTTP\_FILTER\_VERSION 

structure\.

#### Properties

  -  **int ServerFilterVersion** 
    \(read-only\)

  -  **int FilterVersion** 
    

  -  **int Flags** 
    

  -  **string FilterDesc** 
    