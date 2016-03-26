# win32service

## Module win32service

An interface to the Windows NT Service API

#### Methods


  - [GetThreadDesktop](win32service.md#win32servicegetthreaddesktop)

    Retrieves a handle to the desktop for a thread&nbsp;

  - [EnumWindowStations](win32service.md#win32serviceenumwindowstations)

    Lists names of window stations&nbsp;

  - [GetUserObjectInformation](win32service.md#win32servicegetuserobjectinformation)

    Returns specified type of info about a window station or desktop&nbsp;

  - [SetUserObjectInformation](win32service.md#win32servicesetuserobjectinformation)

    Set specified type of info for a window station or desktop object&nbsp;

  - [OpenWindowStation](win32service.md#win32serviceopenwindowstation)

    Returns a handle to the specified window station&nbsp;

  - [OpenDesktop](win32service.md#win32serviceopendesktop)

    Opens a handle to a desktop&nbsp;

  - [CreateDesktop](win32service.md#win32servicecreatedesktop)

    Creates a new desktop in calling process's current window station&nbsp;

  - [OpenInputDesktop](win32service.md#win32serviceopeninputdesktop)

    Returns a handle to desktop for logged-in user&nbsp;

  - [GetProcessWindowStation](win32service.md#win32servicegetprocesswindowstation)

    Returns a handle to calling process's current window station&nbsp;

  - [CreateWindowStation](win32service.md#win32servicecreatewindowstation)

    Creates a new window station&nbsp;

  - [EnumServicesStatus](win32service.md#win32serviceenumservicesstatus)

    Returns a tuple of status info for each service that meets specified criteria&nbsp;

  - [EnumServicesStatusEx](win32service.md#win32serviceenumservicesstatusex)

    Lists the status of services that meet the specified criteria&nbsp;

  - [EnumDependentServices](win32service.md#win32serviceenumdependentservices)

    Lists services that depend on a service&nbsp;

  - [QueryServiceConfig](win32service.md#win32servicequeryserviceconfig)

    Retrieves configuration parameters for a service&nbsp;

  - [StartService](win32service.md#win32servicestartservice)

    Starts the specified service&nbsp;

  - [OpenService](win32service.md#win32serviceopenservice)

    Returns a handle to the specified service.&nbsp;

  - [OpenSCManager](win32service.md#win32serviceopenscmanager)

    Returns a handle to the service control manager&nbsp;

  - [CloseServiceHandle](win32service.md#win32servicecloseservicehandle)

    Closes a service or SCM handle&nbsp;

  - [QueryServiceStatus](win32service.md#win32servicequeryservicestatus)

    Queries a service status&nbsp;

  - [QueryServiceStatusEx](win32service.md#win32servicequeryservicestatusex)

    Queries a service status&nbsp;

  - [SetServiceObjectSecurity](win32service.md#win32servicesetserviceobjectsecurity)

    Set the security descriptor for a service&nbsp;

  - [QueryServiceObjectSecurity](win32service.md#win32servicequeryserviceobjectsecurity)

    Retrieves information from the security descriptor for a service&nbsp;

  - [GetServiceKeyName](win32service.md#win32servicegetservicekeyname)

    Translates a service display name into its registry key name&nbsp;

  - [GetServiceDisplayName](win32service.md#win32servicegetservicedisplayname)

    Translates an internal service name into its display name&nbsp;

  - [SetServiceStatus](win32service.md#win32servicesetservicestatus)

    Sets a service status&nbsp;

  - [ControlService](win32service.md#win32servicecontrolservice)

    Sends a control message to a service.&nbsp;

  - [DeleteService](win32service.md#win32servicedeleteservice)

    Deletes the specified service&nbsp;

  - [CreateService](win32service.md#win32servicecreateservice)

    Creates a new service.&nbsp;

  - [ChangeServiceConfig](win32service.md#win32servicechangeserviceconfig)

    Changes the configuration of an existing service.&nbsp;

  - [LockServiceDatabase](win32service.md#win32servicelockservicedatabase)

    Locks the service database.&nbsp;

  - [UnlockServiceDatabase](win32service.md#win32serviceunlockservicedatabase)

    Unlocks the service database.&nbsp;

  - [QueryServiceLockStatus](win32service.md#win32servicequeryservicelockstatus)

    Retrieves the lock status of the specified service control manager database.&nbsp;

  - [ChangeServiceConfig2](win32service.md#win32servicechangeserviceconfig2)

    Modifies advanced service parameters&nbsp;

  - [QueryServiceConfig2](win32service.md#win32servicequeryserviceconfig2)

    Retrieves advanced service configuration options&nbsp;

## [win32service](#win32service).ChangeServiceConfig

int/None = __ChangeServiceConfig( *hService*  *, serviceType*  *, startType*  *, errorControl*  *, binaryFile*  *, loadOrderGroup*  *, bFetchTag*  *, serviceDeps*  *, acctName*  *, password*  *, displayName* __ )
Changes the configuration of an existing service.

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    handle to service to be modified

  -  *serviceType* : int

    type of service, or SERVICE_NO_CHANGE

  -  *startType* : int

    When/how to start service, or SERVICE_NO_CHANGE

  -  *errorControl* : int

    severity if service fails to start, or SERVICE_NO_CHANGE

  -  *binaryFile* :[PyUnicode](#pyunicode)

    name of binary file, or None

  -  *loadOrderGroup* :[PyUnicode](#pyunicode)

    name of load ordering group , or None

  -  *bFetchTag* : int

    Should the tag be fetched and returned?  If TRUE, the result is the tag, else None.

  -  *serviceDeps* : [[PyUnicode](#pyunicode),...]

    sequence of dependency names

  -  *acctName* :[PyUnicode](#pyunicode)

    account name of service, or None

  -  *password* :[PyUnicode](#pyunicode)

    password for service account , or None

  -  *displayName* :[PyUnicode](#pyunicode)

    Display name

## [win32service](#win32service).ChangeServiceConfig2

 __ChangeServiceConfig2( *hService*  *, InfoLevel*  *, info* __ )
Modifies advanced service parameters

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Service handle as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)

  -  *InfoLevel* : int

    One of win32service.SERVICE_CONFIG_* values

  -  *info* : object

    Type depends on InfoLevel


## [win32service](#win32service).CloseServiceHandle

 __CloseServiceHandle( *scHandle* __ )
Closes a service or SCM handle

#### Parameters


  -  *scHandle* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to close

## [win32service](#win32service).ControlService

[SERVICE_STATUS](SERVICE.md#servicestatus)= __ControlService( *scHandle*  *, code* __ )
Sends a control message to a service.

#### Parameters


  -  *scHandle* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to control

  -  *code* : int

    The service control code.

#### Return Value
The result is the new service status.

## [win32service](#win32service).CreateDesktop

[PyHDESK](#pyhdesk)= __CreateDesktop( *Desktop*  *, Flags*  *, DesiredAccess*  *, SecurityAttributes* __ )
Creates a new desktop in calling process's current window station

#### Parameters


  -  *Desktop* : str/unicode

    Name of desktop to create

  -  *Flags* : int

    DF_ALLOWOTHERACCOUNTHOOK or 0

  -  *DesiredAccess* : int

    An ACCESS_MASK determining level of access available thru returned handle

  -  *SecurityAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and controls access to desktop

## [win32service](#win32service).CreateService

[PySC_HANDLE](PySC.md#pyschandle)/([PySC_HANDLE](PySC.md#pyschandle), int) = __CreateService( *scHandle*  *, name*  *, displayName*  *, desiredAccess*  *, serviceType*  *, startType*  *, errorControl*  *, binaryFile*  *, loadOrderGroup*  *, bFetchTag*  *, serviceDeps*  *, acctName*  *, password* __ )
Creates a new service.

#### Parameters


  -  *scHandle* :[PySC_HANDLE](PySC.md#pyschandle)

    handle to service control manager database

  -  *name* :[PyUnicode](#pyunicode)

    Name of service

  -  *displayName* :[PyUnicode](#pyunicode)

    Display name

  -  *desiredAccess* : int

    type of access to service

  -  *serviceType* : int

    type of service

  -  *startType* : int

    When/how to start service

  -  *errorControl* : int

    severity if service fails to start

  -  *binaryFile* :[PyUnicode](#pyunicode)

    name of binary file

  -  *loadOrderGroup* :[PyUnicode](#pyunicode)

    name of load ordering group , or None

  -  *bFetchTag* : int

    Should the tag be fetched and returned?  If TRUE, the result is a tuple of (handle, tag), otherwise just handle.

  -  *serviceDeps* : [[PyUnicode](#pyunicode),...]

    sequence of dependency names

  -  *acctName* :[PyUnicode](#pyunicode)

    account name of service, or None

  -  *password* :[PyUnicode](#pyunicode)

    password for service account , or None

## [win32service](#win32service).CreateWindowStation

[PyHWINSTA](#pyhwinsta)= __CreateWindowStation( *WindowStation*  *, Flags*  *, DesiredAccess*  *, SecurityAttributes* __ )
Creates a new window station

#### Parameters


  -  *WindowStation* : str/unicode

    Name of window station to create, or None

  -  *Flags* : int

    CWF_CREATE_ONLY or 0

  -  *DesiredAccess* : int

    Bitmask of access types available to returned handle

  -  *SecurityAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security for window station, and whether handle is inheritable

#### Comments
If name is None or empty string, name is formatteded from logon id

## DBT_CONFIGCHANGECANCELED
 __const win32service.DBT_CONFIGCHANGECANCELED;__ 


## DBT_CONFIGCHANGED
 __const win32service.DBT_CONFIGCHANGED;__ 


## DBT_CUSTOMEVENT
 __const win32service.DBT_CUSTOMEVENT;__ 
user-defined event

## DBT_DEVICEARRIVAL
 __const win32service.DBT_DEVICEARRIVAL;__ 
system detected a new device

## DBT_DEVICEQUERYREMOVE
 __const win32service.DBT_DEVICEQUERYREMOVE;__ 
wants to remove, may fail

## DBT_DEVICEQUERYREMOVEFAILED
 __const win32service.DBT_DEVICEQUERYREMOVEFAILED;__ 
removal aborted

## DBT_DEVICEREMOVECOMPLETE
 __const win32service.DBT_DEVICEREMOVECOMPLETE;__ 
device is gone

## DBT_DEVICEREMOVEPENDING
 __const win32service.DBT_DEVICEREMOVEPENDING;__ 
about to remove, still avail.

## DBT_DEVICETYPESPECIFIC
 __const win32service.DBT_DEVICETYPESPECIFIC;__ 
type specific event

## DBT_QUERYCHANGECONFIG
 __const win32service.DBT_QUERYCHANGECONFIG;__ 


## DF_ALLOWOTHERACCOUNTHOOK
 __const win32service.DF_ALLOWOTHERACCOUNTHOOK;__ 
#define CWF_CREATE_ONLY CWF_CREATE_ONLY

## [win32service](#win32service).DeleteService

 __DeleteService( *scHandle* __ )
Deletes the specified service

#### Parameters


  -  *scHandle* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service to be deleted

## [win32service](#win32service).EnumDependentServices

(tuple,...) = __EnumDependentServices( *hService*  *, ServiceState* __ )
Lists services that depend on a service

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service for which to list dependent services (as returned by[win32service::OpenService](win32service.md#win32serviceopenservice))

  -  *ServiceState=SERVICE_STATE_ALL* : int

    Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVE

#### Return Value
Returns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName,[SERVICE_STATUS](SERVICE.md#servicestatus))

## [win32service](#win32service).EnumServicesStatus

(tuple,...) = __EnumServicesStatus( *hSCManager*  *, ServiceType*  *, ServiceState* __ )
Returns a tuple of status info for each service that meets specified criteria

#### Parameters


  -  *hSCManager* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  -  *ServiceType=SERVICE_WIN32* : int

    Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)

  -  *ServiceState=SERVICE_STATE_ALL* : int

    Limits to services in specified state

#### Return Value
Returns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName,[SERVICE_STATUS](SERVICE.md#servicestatus))

## [win32service](#win32service).EnumServicesStatusEx

(dict,...) = __EnumServicesStatusEx( *SCManager*  *, ServiceType*  *, ServiceState*  *, GroupName*  *, InfoLevel* __ )
Lists the status of services that meet the specified criteria

#### Parameters


  -  *SCManager* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  -  *ServiceType=SERVICE_WIN32* : int

    Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)

  -  *ServiceState=SERVICE_STATE_ALL* : int

    Limits to services in specified state

  -  *GroupName=None* : str

    Name of group - use None for all, or '' for services that don't belong to a group

  -  *InfoLevel=SC_ENUM_PROCESS_INFO* : int

    Currently SC_ENUM_PROCESS_INFO is only level defined

#### Win32 API References


  - Search for *EnumServicesStatusEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=enumservicesstatusex),[google](#http://www.google.com/search?q=enumservicesstatusex)or[google groups](#http://groups.google.com/groups?q=enumservicesstatusex).

#### Return Value
Returns a sequence of dicts, whose contents depend on information level requested. 

Currently, only information level supported is SC_ENUM_PROCESS_INFO (returns ENUM_SERVICE_STATUS_PROCESS).

## [win32service](#win32service).EnumWindowStations

([PyUnicode](#pyunicode),,...) = __EnumWindowStations(__ )
Lists names of window stations

#### Comments
Only window stations for which you have WINSTA_ENUMERATE access will be returned

## [win32service](#win32service).GetProcessWindowStation

[PyHWINSTA](#pyhwinsta)= __GetProcessWindowStation(__ )
Returns a handle to calling process's current window station

## [win32service](#win32service).GetServiceDisplayName

[PyUNICODE](#pyunicode)= __GetServiceDisplayName( *hSCManager*  *, ServiceName* __ )
Translates an internal service name into its display name

#### Parameters


  -  *hSCManager* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  -  *ServiceName* :[PyUNICODE](#pyunicode)

    Name of service

## [win32service](#win32service).GetServiceKeyName

[PyUNICODE](#pyunicode)= __GetServiceKeyName( *hSCManager*  *, DisplayName* __ )
Translates a service display name into its registry key name

#### Parameters


  -  *hSCManager* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  -  *DisplayName* :[PyUNICODE](#pyunicode)

    Display name of a service

## [win32service](#win32service).GetThreadDesktop

[PyHDESK](#pyhdesk)= __GetThreadDesktop( *ThreadId* __ )
Retrieves a handle to the desktop for a thread

#### Parameters


  -  *ThreadId* : int

    Id of thread

## [win32service](#win32service).GetUserObjectInformation

 __GetUserObjectInformation( *Handle*  *, type* __ )
Returns specified type of info about a window station or desktop

#### Parameters


  -  *Handle* :[PyHANDLE](#pyhandle)

    Handle to window station or desktop

  -  *type* : int

    Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SID

#### Return Value
Return type is dependent on UOI_* constant passed in

## [win32service](#win32service).LockServiceDatabase

int = __LockServiceDatabase( *sc_handle* __ )
Locks the service database.

#### Parameters


  -  *sc_handle* :[PySC_HANDLE](PySC.md#pyschandle)

    A handle to the SCM.

## [win32service](#win32service).OpenDesktop

[PyHDESK](#pyhdesk)= __OpenDesktop( *szDesktop*  *, Flags*  *, Inherit*  *, DesiredAccess* __ )
Opens a handle to a desktop

#### Parameters


  -  *szDesktop* : str/unicode

    Name of desktop to open

  -  *Flags* : int

    DF_ALLOWOTHERACCOUNTHOOK or 0

  -  *Inherit* : bool

    Allow handle to be inherited

  -  *DesiredAccess* : int

    ACCESS_MASK specifying level of access for handle

## [win32service](#win32service).OpenInputDesktop

[PyHDESK](#pyhdesk)= __OpenInputDesktop( *Flags*  *, Inherit*  *, DesiredAccess* __ )
Returns a handle to desktop for logged-in user

#### Parameters


  -  *Flags* : int

    DF_ALLOWOTHERACCOUNTHOOK or 0

  -  *Inherit* : bool

    Specifies if handle will be inheritable

  -  *DesiredAccess* : int

    ACCESS_MASK specifying access available to returned handle

## [win32service](#win32service).OpenSCManager

[PySC_HANDLE](PySC.md#pyschandle)= __OpenSCManager( *machineName*  *, dbName*  *, desiredAccess* __ )
Returns a handle to the service control manager

#### Parameters


  -  *machineName* :[PyUnicode](#pyunicode)

    The name of the computer, or None

  -  *dbName* :[PyUnicode](#pyunicode)

    The name of the service database, or None

  -  *desiredAccess* : int

    The access desired. (combination of win32service.SC_MANAGER_* flags)

## [win32service](#win32service).OpenService

[PySC_HANDLE](PySC.md#pyschandle)= __OpenService( *scHandle*  *, name*  *, desiredAccess* __ )
Returns a handle to the specified service.

#### Parameters


  -  *scHandle* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to the Service Control Mananger

  -  *name* :[PyUnicode](#pyunicode)

    The name of the service to open.

  -  *desiredAccess* : int

    The access desired.

## [win32service](#win32service).OpenWindowStation

[PyHWINSTA](#pyhwinsta)= __OpenWindowStation( *szWinSta*  *, Inherit*  *, DesiredAccess* __ )
Returns a handle to the specified window station

#### Parameters


  -  *szWinSta* : str/PyUNICODE

    Name of window station

  -  *Inherit* : Bool

    Allow handle to be inherited by subprocesses

  -  *DesiredAccess* : int

    Bitmask of access types

## [win32service](#win32service).QueryServiceConfig

tuple = __QueryServiceConfig( *hService* __ )
Retrieves configuration parameters for a service

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Service handle as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)

#### Return Value
Returns a tuple representing a QUERY_SERVICE_CONFIG struct:

#### Items


  - [0] *int* : ServiceType

    Combination of SERVICE_*_DRIVER or SERVICE_*_PROCESS constants

  - [1] *int* : StartType

    One of SERVICE_*_START constants

  - [2] *int* : ErrorControl

    One of SERVICE_ERROR_* constants

  - [3] *[PyUnicode](#pyunicode)* : BinaryPathName

    Service's binary executable, can also contain command line args

  - [4] *[PyUnicode](#pyunicode)* : LoadOrderGroup

    Loading group that service is a member of

  - [5] *int* : TagId

    Order of service within its load order group

  - [6] *[[PyUnicode](#pyunicode),...]* : Dependencies

    Sequence of names of services on which this service depends

  - [7] *[PyUnicode](#pyunicode)* : ServiceStartName

    Account name under which service will run

  - [8] *[PyUnicode](#pyunicode)* : DisplayName

    Name of service

## [win32service](#win32service).QueryServiceConfig2

object = __QueryServiceConfig2( *hService*  *, InfoLevel* __ )
Retrieves advanced service configuration options

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Service handle as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)

  -  *InfoLevel* : int

    One of win32service.SERVICE_CONFIG_* values

 __InfoLevel__  __Type of value returned__ SERVICE_CONFIG_DESCRIPTIONUnicode stringSERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS structSERVICE_CONFIG_DELAYED_AUTO_START_INFOBooleanSERVICE_CONFIG_FAILURE_ACTIONS_FLAGBooleanSERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOList of unicode strings
#### Return Value
Type of returned object depends on InfoLevel

## [win32service](#win32service).QueryServiceLockStatus

(int,[PyUnicode](#pyunicode), int) = __QueryServiceLockStatus( *hSCManager* __ )
Retrieves the lock status of the specified service control manager database.

#### Parameters


  -  *hSCManager* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to the SCM.

#### Return Value
The result is a tuple of (bIsLocked, userName, lockDuration)

## [win32service](#win32service).QueryServiceObjectSecurity

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __QueryServiceObjectSecurity( *Handle*  *, SecurityInformation* __ )
Retrieves information from the security descriptor for a service

#### Parameters


  -  *Handle* :[PySC_HANDLE](PySC.md#pyschandle)

    Service handle

  -  *SecurityInformation* : int

    Type of infomation to retrieve, combination of values from SECURITY_INFORMATION enum

## [win32service](#win32service).QueryServiceStatus

[SERVICE_STATUS](SERVICE.md#servicestatus)= __QueryServiceStatus( *hService* __ )
Queries a service status

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service to be queried

## [win32service](#win32service).QueryServiceStatusEx

[SERVICE_STATUS](SERVICE.md#servicestatus)= __QueryServiceStatusEx( *hService* __ )
Queries a service status

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to service to be queried

## SC_ACTION_NONE
 __const win32service.SC_ACTION_NONE;__ 


## SC_ACTION_REBOOT
 __const win32service.SC_ACTION_REBOOT;__ 


## SC_ACTION_RESTART
 __const win32service.SC_ACTION_RESTART;__ 


## SC_ACTION_RUN_COMMAND
 __const win32service.SC_ACTION_RUN_COMMAND;__ 


## SC_ENUM_PROCESS_INFO
 __const win32service.SC_ENUM_PROCESS_INFO;__ 


## SC_GROUP_IDENTIFIER
 __const win32service.SC_GROUP_IDENTIFIER;__ 


## SC_MANAGER_ALL_ACCESS
 __const win32service.SC_MANAGER_ALL_ACCESS;__ 
Includes STANDARD_RIGHTS_REQUIRED, in addition to all of the access types listed in this table.

## SC_MANAGER_CONNECT
 __const win32service.SC_MANAGER_CONNECT;__ 
Enables connecting to the service control manager.

## SC_MANAGER_CREATE_SERVICE
 __const win32service.SC_MANAGER_CREATE_SERVICE;__ 
Enables calling of the CreateService function to create a service object and add it to the database.

## SC_MANAGER_ENUMERATE_SERVICE
 __const win32service.SC_MANAGER_ENUMERATE_SERVICE;__ 
Enables calling of the EnumServicesStatus function to list the services that are in the database.

## SC_MANAGER_LOCK
 __const win32service.SC_MANAGER_LOCK;__ 
Enables calling of the LockServiceDatabase function to acquire a lock on the database.

## SC_MANAGER_MODIFY_BOOT_CONFIG
 __const win32service.SC_MANAGER_MODIFY_BOOT_CONFIG;__ 


## SC_MANAGER_QUERY_LOCK_STATUS
 __const win32service.SC_MANAGER_QUERY_LOCK_STATUS;__ 
Enables calling of the QueryServiceLockStatus function to retrieve the lock status information for the database.

## SERVICE_ACCEPT_HARDWAREPROFILECHANGE
 __const win32service.SERVICE_ACCEPT_HARDWAREPROFILECHANGE;__ 


## SERVICE_ACCEPT_NETBINDCHANGE
 __const win32service.SERVICE_ACCEPT_NETBINDCHANGE;__ 


## SERVICE_ACCEPT_PARAMCHANGE
 __const win32service.SERVICE_ACCEPT_PARAMCHANGE;__ 


## SERVICE_ACCEPT_PAUSE_CONTINUE
 __const win32service.SERVICE_ACCEPT_PAUSE_CONTINUE;__ 
The service can be paused and continued. This enables the SERVICE_CONTROL_PAUSE and SERVICE_CONTROL_CONTINUE values.

## SERVICE_ACCEPT_POWEREVENT
 __const win32service.SERVICE_ACCEPT_POWEREVENT;__ 


## SERVICE_ACCEPT_PRESHUTDOWN
 __const win32service.SERVICE_ACCEPT_PRESHUTDOWN;__ 


## SERVICE_ACCEPT_SESSIONCHANGE
 __const win32service.SERVICE_ACCEPT_SESSIONCHANGE;__ 


## SERVICE_ACCEPT_SHUTDOWN
 __const win32service.SERVICE_ACCEPT_SHUTDOWN;__ 
The service is notified when system shutdown occurs. This enables the system to send a SERVICE_CONTROL_SHUTDOWN value to the service. The ControlService function cannot send this control

## SERVICE_ACCEPT_STOP
 __const win32service.SERVICE_ACCEPT_STOP;__ 
The service can be stopped. This enables the SERVICE_CONTROL_STOP value.

## SERVICE_ACTIVE
 __const win32service.SERVICE_ACTIVE;__ 


## SERVICE_ALL_ACCESS
 __const win32service.SERVICE_ALL_ACCESS;__ 
Includes STANDARD_RIGHTS_REQUIRED in addition to all of the access types listed in this table.

## SERVICE_AUTO_START
 __const win32service.SERVICE_AUTO_START;__ 
Specifies a device driver or Win32 service started by the service control manager automatically during system startup.

## SERVICE_BOOT_START
 __const win32service.SERVICE_BOOT_START;__ 
Specifies a device driver started by the operating system loader. This value is valid only if the service type is SERVICE_KERNEL_DRIVER or SERVICE_FILE_SYSTEM_DRIVER.

## SERVICE_CHANGE_CONFIG
 __const win32service.SERVICE_CHANGE_CONFIG;__ 
Enables calling of the ChangeServiceConfig function to change the service configuration.

## SERVICE_CONFIG_DELAYED_AUTO_START_INFO
 __const win32service.SERVICE_CONFIG_DELAYED_AUTO_START_INFO;__ 


## SERVICE_CONFIG_DESCRIPTION
 __const win32service.SERVICE_CONFIG_DESCRIPTION;__ 


## SERVICE_CONFIG_FAILURE_ACTIONS
 __const win32service.SERVICE_CONFIG_FAILURE_ACTIONS;__ 
These require Vista or above

## SERVICE_CONFIG_FAILURE_ACTIONS_FLAG
 __const win32service.SERVICE_CONFIG_FAILURE_ACTIONS_FLAG;__ 


## SERVICE_CONFIG_PRESHUTDOWN_INFO
 __const win32service.SERVICE_CONFIG_PRESHUTDOWN_INFO;__ 


## SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO
 __const win32service.SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO;__ 


## SERVICE_CONFIG_SERVICE_SID_INFO
 __const win32service.SERVICE_CONFIG_SERVICE_SID_INFO;__ 


## SERVICE_CONTINUE_PENDING
 __const win32service.SERVICE_CONTINUE_PENDING;__ 
The service continue is pending.

## SERVICE_CONTROL_CONTINUE
 __const win32service.SERVICE_CONTROL_CONTINUE;__ 
Requests the paused service to resume. The hService handle must have SERVICE_PAUSE_CONTINUE access.

## SERVICE_CONTROL_DEVICEEVENT
 __const win32service.SERVICE_CONTROL_DEVICEEVENT;__ 


## SERVICE_CONTROL_HARDWAREPROFILECHANGE
 __const win32service.SERVICE_CONTROL_HARDWAREPROFILECHANGE;__ 


## SERVICE_CONTROL_INTERROGATE
 __const win32service.SERVICE_CONTROL_INTERROGATE;__ 
Requests the service to update immediately its current status information to the service control manager. The hService handle must have SERVICE_INTERROGATE access.

## SERVICE_CONTROL_NETBINDADD
 __const win32service.SERVICE_CONTROL_NETBINDADD;__ 


## SERVICE_CONTROL_NETBINDDISABLE
 __const win32service.SERVICE_CONTROL_NETBINDDISABLE;__ 


## SERVICE_CONTROL_NETBINDENABLE
 __const win32service.SERVICE_CONTROL_NETBINDENABLE;__ 


## SERVICE_CONTROL_NETBINDREMOVE
 __const win32service.SERVICE_CONTROL_NETBINDREMOVE;__ 


## SERVICE_CONTROL_PARAMCHANGE
 __const win32service.SERVICE_CONTROL_PARAMCHANGE;__ 


## SERVICE_CONTROL_PAUSE
 __const win32service.SERVICE_CONTROL_PAUSE;__ 
Requests the service to pause. The hService handle must have SERVICE_PAUSE_CONTINUE access.

## SERVICE_CONTROL_POWEREVENT
 __const win32service.SERVICE_CONTROL_POWEREVENT;__ 


## SERVICE_CONTROL_PRESHUTDOWN
 __const win32service.SERVICE_CONTROL_PRESHUTDOWN;__ 


## SERVICE_CONTROL_SESSIONCHANGE
 __const win32service.SERVICE_CONTROL_SESSIONCHANGE;__ 


## SERVICE_CONTROL_SHUTDOWN
 __const win32service.SERVICE_CONTROL_SHUTDOWN;__ 
The ControlService function fails if this control code is specified.

## SERVICE_CONTROL_STOP
 __const win32service.SERVICE_CONTROL_STOP;__ 
Requests the service to stop. The hService handle must have SERVICE_STOP access.

## SERVICE_DEMAND_START
 __const win32service.SERVICE_DEMAND_START;__ 
Specifies a device driver or Win32 service started by the service control manager when a process calls the StartService function.

## SERVICE_DISABLED
 __const win32service.SERVICE_DISABLED;__ 
Specifies a device driver or Win32 service that can no longer be started.

## SERVICE_DRIVER
 __const win32service.SERVICE_DRIVER;__ 


## SERVICE_ENUMERATE_DEPENDENTS
 __const win32service.SERVICE_ENUMERATE_DEPENDENTS;__ 
Enables calling of the EnumDependentServices function to enumerate all the services dependent on the service.

## SERVICE_ERROR_CRITICAL
 __const win32service.SERVICE_ERROR_CRITICAL;__ 
The startup program logs the error, if possible. If the last-known good configuration is being started, 

the startup operation fails. Otherwise, the system is restarted with the last-known good configuration.

## SERVICE_ERROR_IGNORE
 __const win32service.SERVICE_ERROR_IGNORE;__ 
The startup (boot) program logs the error but continues the startup operation.

## SERVICE_ERROR_NORMAL
 __const win32service.SERVICE_ERROR_NORMAL;__ 
The startup program logs the error and displays a message box pop-up but continues the startup operation.

## SERVICE_ERROR_SEVERE
 __const win32service.SERVICE_ERROR_SEVERE;__ 
The startup program logs the error. If the last-known good configuration is being started, 

the startup operation continues. Otherwise, the system is restarted with the last-known-good configuration.

## SERVICE_FILE_SYSTEM_DRIVER
 __const win32service.SERVICE_FILE_SYSTEM_DRIVER;__ 
A service type flag that indicates a Windows NT file system driver.

## SERVICE_INACTIVE
 __const win32service.SERVICE_INACTIVE;__ 


## SERVICE_INTERACTIVE_PROCESS
 __const win32service.SERVICE_INTERACTIVE_PROCESS;__ 
A flag that indicates a Win32 service process that can interact with the desktop.

## SERVICE_INTERROGATE
 __const win32service.SERVICE_INTERROGATE;__ 
Enables calling of the ControlService function to ask the service to report its status immediately.

## SERVICE_KERNEL_DRIVER
 __const win32service.SERVICE_KERNEL_DRIVER;__ 
A service type flag that indicates a Windows NT device driver.

## SERVICE_NO_CHANGE
 __const win32service.SERVICE_NO_CHANGE;__ 
Indicates the parameter should not be changed.

## SERVICE_PAUSED
 __const win32service.SERVICE_PAUSED;__ 
The service is paused.

## SERVICE_PAUSE_CONTINUE
 __const win32service.SERVICE_PAUSE_CONTINUE;__ 
Enables calling of the ControlService function to pause or continue the service.

## SERVICE_PAUSE_PENDING
 __const win32service.SERVICE_PAUSE_PENDING;__ 
The service pause is pending.

## SERVICE_QUERY_CONFIG
 __const win32service.SERVICE_QUERY_CONFIG;__ 
Enables calling of the QueryServiceConfig function to query the service configuration.

## SERVICE_QUERY_STATUS
 __const win32service.SERVICE_QUERY_STATUS;__ 
Enables calling of the QueryServiceStatus function to ask the service control manager about the status of the service.

## SERVICE_RUNNING
 __const win32service.SERVICE_RUNNING;__ 
The service is running.

## SERVICE_SID_TYPE_NONE
 __const win32service.SERVICE_SID_TYPE_NONE;__ 


## SERVICE_SID_TYPE_RESTRICTED
 __const win32service.SERVICE_SID_TYPE_RESTRICTED;__ 


## SERVICE_SID_TYPE_UNRESTRICTED
 __const win32service.SERVICE_SID_TYPE_UNRESTRICTED;__ 


## SERVICE_SPECIFIC_ERROR
 __const win32service.SERVICE_SPECIFIC_ERROR;__ 
A service specific error has occurred.

## SERVICE_START
 __const win32service.SERVICE_START;__ 
Enables calling of the StartService function to start the service.

## SERVICE_START_PENDING
 __const win32service.SERVICE_START_PENDING;__ 
The service is starting.

## SERVICE_STATE_ALL
 __const win32service.SERVICE_STATE_ALL;__ 


## SERVICE_STOP
 __const win32service.SERVICE_STOP;__ 
Enables calling of the ControlService function to stop the service.

## SERVICE_STOPPED
 __const win32service.SERVICE_STOPPED;__ 
The service is not running.

## SERVICE_STOP_PENDING
 __const win32service.SERVICE_STOP_PENDING;__ 
The service is stopping.

## SERVICE_SYSTEM_START
 __const win32service.SERVICE_SYSTEM_START;__ 
Specifies a device driver started by the IoInitSystem function. This value is valid only if the service type is SERVICE_KERNEL_DRIVER or SERVICE_FILE_SYSTEM_DRIVER.

## SERVICE_USER_DEFINED_CONTROL
 __const win32service.SERVICE_USER_DEFINED_CONTROL;__ 
Enables calling of the ControlService function to specify a user-defined control code.

## SERVICE_WIN32
 __const win32service.SERVICE_WIN32;__ 


## SERVICE_WIN32_OWN_PROCESS
 __const win32service.SERVICE_WIN32_OWN_PROCESS;__ 
A service type flag that indicates a Win32 service that runs in its own process.

## SERVICE_WIN32_SHARE_PROCESS
 __const win32service.SERVICE_WIN32_SHARE_PROCESS;__ 
A service type flag that indicates a Win32 service that shares a process with other services.

## [win32service](#win32service).SetServiceObjectSecurity

 __SetServiceObjectSecurity( *Handle*  *, SecurityInformation*  *, SecurityDescriptor* __ )
Set the security descriptor for a service

#### Parameters


  -  *Handle* :[PySC_HANDLE](PySC.md#pyschandle)

    Service handle

  -  *SecurityInformation* : int

    Type of infomation to set, combination of values from SECURITY_INFORMATION enum

  -  *SecurityDescriptor* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    PySECURITY_DESCRIPTOR containing infomation to set

## [win32service](#win32service).SetServiceStatus

 __SetServiceStatus( *scHandle*  *, serviceStatus* __ )
Sets a service status

#### Parameters


  -  *scHandle* : int

    Handle to set

  -  *serviceStatus* :[SERVICE_STATUS](SERVICE.md#servicestatus)

    The new status

## [win32service](#win32service).SetUserObjectInformation

 __SetUserObjectInformation( *Handle*  *, info*  *, type* __ )
Set specified type of info for a window station or desktop object

#### Parameters


  -  *Handle* :[PyHANDLE](#pyhandle)

    Handle to window station or desktop

  -  *info* : object

    Information to set for handle, currently only a dictionary representing USEROBJECTFLAGS struct

  -  *type=UOI_FLAGS* : int

    Type of info to set, currently only accepts UOI_FLAGS

#### Comments
Currently only UOI_FLAGS supported

## [win32service](#win32service).StartService

 __StartService( *hService*  *, args* __ )
Starts the specified service

#### Parameters


  -  *hService* :[PySC_HANDLE](PySC.md#pyschandle)

    Handle to the service to be started

  -  *args* : [string, ...]

    Arguments to the service.

## UOI_FLAGS
 __const win32service.UOI_FLAGS;__ 


## UOI_NAME
 __const win32service.UOI_NAME;__ 


## UOI_TYPE
 __const win32service.UOI_TYPE;__ 


## UOI_USER_SID
 __const win32service.UOI_USER_SID;__ 


## [win32service](#win32service).UnlockServiceDatabase

int = __UnlockServiceDatabase( *lock* __ )
Unlocks the service database.

#### Parameters


  -  *lock* : int

    A lock provided by[win32service::LockServiceDatabase](win32service.md#win32servicelockservicedatabase)

## WSF_VISIBLE
 __const win32service.WSF_VISIBLE;__ 
