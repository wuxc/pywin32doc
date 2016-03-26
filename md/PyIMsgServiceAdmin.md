# PyIMsgServiceAdmin

## PyIMsgServiceAdmin Object

An COM interface to MAPI's IMsgServiceAdmin interface\.
Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [CreateMsgService](PyIMsgServiceAdmin.md#pyimsgserviceadmincreatemsgservice)

    Creates a message service\.&nbsp;

  - [ConfigureMsgService](PyIMsgServiceAdmin.md#pyimsgserviceadminconfiguremsgservice)

    Reconfigures a message service\.&nbsp;

  - [GetMsgServiceTable](PyIMsgServiceAdmin.md#pyimsgserviceadmingetmsgservicetable)

    Retrieves a table of services\.&nbsp;

  - [GetProviderTable](PyIMsgServiceAdmin.md#pyimsgserviceadmingetprovidertable)

    Retrieves a table of service providers\.&nbsp;

  - [DeleteMsgService](PyIMsgServiceAdmin.md#pyimsgserviceadmindeletemsgservice)

    Deletes the specified service&nbsp;

  - [RenameMsgService](PyIMsgServiceAdmin.md#pyimsgserviceadminrenamemsgservice)

    Renames the specified service&nbsp;

  - [OpenProfileSection](PyIMsgServiceAdmin.md#pyimsgserviceadminopenprofilesection)

    Opens a profile section&nbsp;

  - [AdminProviders](PyIMsgServiceAdmin.md#pyimsgserviceadminadminproviders)

    Returns an object providing access 

to a provider administration object\.&nbsp;

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.AdminProviders

 **PyIProfSect** \= **AdminProviders\( *uuid*  *, flags* ** \)
Returns an object providing access 

to a provider administration object\.

#### Parameters


  -  *uuid* :[PyIID](#pyiid)

    The ID of the service

  -  *flags* : int

    

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.ConfigureMsgService

 **ConfigureMsgService\( *iid*  *, ulUIParam*  *, ulFlags*  *, \[SPropValue, \.\.\.\]* ** \)
Reconfigures a message service\.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The unique identifier for the message service to configure\.

  -  *ulUIParam* : int

    Handle of the parent window for the configuration property sheet\.

  -  *ulFlags* : int

    Bitmask of flags that controls the display of the property sheet\.

  -  *\[SPropValue, \.\.\.\]* : \[values, \.\.\.\]

    Property values describing the properties to display in the property sheet\.  Should not be None if the service is to be configured without a message service\.

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.CreateMsgService

 **CreateMsgService\( *serviceName*  *, displayName*  *, ulUIParam*  *, ulFlags* ** \)
Creates a message service\.

#### Parameters


  -  *serviceName* : string

    The name of the service\.

  -  *displayName* : string

    Display name of the service, or None

  -  *ulUIParam* : int

    Handle of the parent window for the configuration property sheet\.

  -  *ulFlags* : int

    Bitmask of flags that controls the display of the property sheet\.

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.DeleteMsgService

 **DeleteMsgService\( *uuid* ** \)
Deletes the specified service

#### Parameters


  -  *uuid* :[PyIID](#pyiid)

    The ID of the service

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.GetMsgServiceTable

[PyIMAPITable](#pyimapitable)\= **GetMsgServiceTable\( *flags* ** \)
Retrieves a table of services\.

#### Parameters


  -  *flags* : int

    

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.GetProviderTable

[PyIMAPITable](#pyimapitable)\= **GetProviderTable\( *flags* ** \)
Retrieves a table of service providers\.

#### Parameters


  -  *flags* : int

    

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.OpenProfileSection

 **PyIProfSect** \= **OpenProfileSection\( *uuid*  *, iid*  *, flags* ** \)
Opens a profile section

#### Parameters


  -  *uuid* :[PyIID](#pyiid)

    The ID of the service

  -  *iid* :[PyIID](#pyiid)

    The IID of the resulting object, or None for the default

  -  *flags* : int

    

## [PyIMsgServiceAdmin](#pyimsgserviceadmin)\.RenameMsgService

 **RenameMsgService\( *uuid*  *, flags*  *, newName* ** \)
Renames the specified service

#### Parameters


  -  *uuid* :[PyIID](#pyiid)

    The ID of the service

  -  *flags* : int

    

  -  *newName* : string

    The new name for the service\.