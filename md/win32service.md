
## [win32service](#README.md#win32service).ChangeServiceConfig

int/None = **ChangeServiceConfig( *hService*  *, serviceType*  *, startType*  *, errorControl*  *, binaryFile*  *, loadOrderGroup*  *, bFetchTag*  *, serviceDeps*  *, acctName*  *, password*  *, displayName* ** )
Changes the configuration of an existing service.

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    handle to service to be modified

     *serviceType* : int

    type of service, or SERVICE_NO_CHANGE

     *startType* : int

    When/how to start service, or SERVICE_NO_CHANGE

     *errorControl* : int

    severity if service fails to start, or SERVICE_NO_CHANGE

     *binaryFile* :[PyUnicode](#README.md#PyUnicode)

    name of binary file, or None

     *loadOrderGroup* :[PyUnicode](#README.md#PyUnicode)

    name of load ordering group , or None

     *bFetchTag* : int

    Should the tag be fetched and returned?  If TRUE, the result is the tag, else None.

     *serviceDeps* : [[PyUnicode](#README.md#PyUnicode),...]

    sequence of dependency names

     *acctName* :[PyUnicode](#README.md#PyUnicode)

    account name of service, or None

     *password* :[PyUnicode](#README.md#PyUnicode)

    password for service account , or None

     *displayName* :[PyUnicode](#README.md#PyUnicode)

    Display name

## [win32service](#README.md#win32service).ChangeServiceConfig2

 **ChangeServiceConfig2( *hService*  *, InfoLevel*  *, info* ** )
Modifies advanced service parameters

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Service handle as returned by[win32service::OpenService](#win32service.md#win32serviceOpenService)

     *InfoLevel* : int

    One of win32service.SERVICE_CONFIG_* values

     *info* : object

    Type depends on InfoLevel


## [win32service](#README.md#win32service).CloseServiceHandle

 **CloseServiceHandle( *scHandle* ** )
Closes a service or SCM handle

#### Parameters


     *scHandle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to close

## [win32service](#README.md#win32service).ControlService

[SERVICE_STATUS](#SERVICE.md#SERVICESTATUS)= **ControlService( *scHandle*  *, code* ** )
Sends a control message to a service.

#### Parameters


     *scHandle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to control

     *code* : int

    The service control code.

#### Return Value
The result is the new service status.

## [win32service](#README.md#win32service).CreateDesktop

[PyHDESK](#README.md#PyHDESK)= **CreateDesktop( *Desktop*  *, Flags*  *, DesiredAccess*  *, SecurityAttributes* ** )
Creates a new desktop in calling process's current window station

#### Parameters


     *Desktop* : str/unicode

    Name of desktop to create

     *Flags* : int

    DF_ALLOWOTHERACCOUNTHOOK or 0

     *DesiredAccess* : int

    An ACCESS_MASK determining level of access available thru returned handle

     *SecurityAttributes* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies inheritance and controls access to desktop

## [win32service](#README.md#win32service).CreateService

[PySC_HANDLE](#PySC.md#PySCHANDLE)/([PySC_HANDLE](#PySC.md#PySCHANDLE), int) = **CreateService( *scHandle*  *, name*  *, displayName*  *, desiredAccess*  *, serviceType*  *, startType*  *, errorControl*  *, binaryFile*  *, loadOrderGroup*  *, bFetchTag*  *, serviceDeps*  *, acctName*  *, password* ** )
Creates a new service.

#### Parameters


     *scHandle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    handle to service control manager database

     *name* :[PyUnicode](#README.md#PyUnicode)

    Name of service

     *displayName* :[PyUnicode](#README.md#PyUnicode)

    Display name

     *desiredAccess* : int

    type of access to service

     *serviceType* : int

    type of service

     *startType* : int

    When/how to start service

     *errorControl* : int

    severity if service fails to start

     *binaryFile* :[PyUnicode](#README.md#PyUnicode)

    name of binary file

     *loadOrderGroup* :[PyUnicode](#README.md#PyUnicode)

    name of load ordering group , or None

     *bFetchTag* : int

    Should the tag be fetched and returned?  If TRUE, the result is a tuple of (handle, tag), otherwise just handle.

     *serviceDeps* : [[PyUnicode](#README.md#PyUnicode),...]

    sequence of dependency names

     *acctName* :[PyUnicode](#README.md#PyUnicode)

    account name of service, or None

     *password* :[PyUnicode](#README.md#PyUnicode)

    password for service account , or None

## [win32service](#README.md#win32service).CreateWindowStation

[PyHWINSTA](#README.md#PyHWINSTA)= **CreateWindowStation( *WindowStation*  *, Flags*  *, DesiredAccess*  *, SecurityAttributes* ** )
Creates a new window station

#### Parameters


     *WindowStation* : str/unicode

    Name of window station to create, or None

     *Flags* : int

    CWF_CREATE_ONLY or 0

     *DesiredAccess* : int

    Bitmask of access types available to returned handle

     *SecurityAttributes* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies security for window station, and whether handle is inheritable

#### Comments
If name is None or empty string, name is formatteded from logon id

## DBT_CONFIGCHANGECANCELED
 **const win32service.DBT_CONFIGCHANGECANCELED;** 


## DBT_CONFIGCHANGED
 **const win32service.DBT_CONFIGCHANGED;** 


## DBT_CUSTOMEVENT
 **const win32service.DBT_CUSTOMEVENT;** 
user-defined event

## DBT_DEVICEARRIVAL
 **const win32service.DBT_DEVICEARRIVAL;** 
system detected a new device

## DBT_DEVICEQUERYREMOVE
 **const win32service.DBT_DEVICEQUERYREMOVE;** 
wants to remove, may fail

## DBT_DEVICEQUERYREMOVEFAILED
 **const win32service.DBT_DEVICEQUERYREMOVEFAILED;** 
removal aborted

## DBT_DEVICEREMOVECOMPLETE
 **const win32service.DBT_DEVICEREMOVECOMPLETE;** 
device is gone

## DBT_DEVICEREMOVEPENDING
 **const win32service.DBT_DEVICEREMOVEPENDING;** 
about to remove, still avail.

## DBT_DEVICETYPESPECIFIC
 **const win32service.DBT_DEVICETYPESPECIFIC;** 
type specific event

## DBT_QUERYCHANGECONFIG
 **const win32service.DBT_QUERYCHANGECONFIG;** 


## DF_ALLOWOTHERACCOUNTHOOK
 **const win32service.DF_ALLOWOTHERACCOUNTHOOK;** 
#define CWF_CREATE_ONLY CWF_CREATE_ONLY

## [win32service](#README.md#win32service).DeleteService

 **DeleteService( *scHandle* ** )
Deletes the specified service

#### Parameters


     *scHandle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service to be deleted

## [win32service](#README.md#win32service).EnumDependentServices

(tuple,...) = **EnumDependentServices( *hService*  *, ServiceState* ** )
Lists services that depend on a service

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service for which to list dependent services (as returned by[win32service::OpenService](#win32service.md#win32serviceOpenService))

     *ServiceState=SERVICE_STATE_ALL* : int

    Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVE

#### Return Value
Returns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName,[SERVICE_STATUS](#SERVICE.md#SERVICESTATUS))

## [win32service](#README.md#win32service).EnumServicesStatus

(tuple,...) = **EnumServicesStatus( *hSCManager*  *, ServiceType*  *, ServiceState* ** )
Returns a tuple of status info for each service that meets specified criteria

#### Parameters


     *hSCManager* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service control manager as returned by[win32service::OpenSCManager](#win32service.md#win32serviceOpenSCManager)

     *ServiceType=SERVICE_WIN32* : int

    Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)

     *ServiceState=SERVICE_STATE_ALL* : int

    Limits to services in specified state

#### Return Value
Returns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName,[SERVICE_STATUS](#SERVICE.md#SERVICESTATUS))

## [win32service](#README.md#win32service).EnumServicesStatusEx

(dict,...) = **EnumServicesStatusEx( *SCManager*  *, ServiceType*  *, ServiceState*  *, GroupName*  *, InfoLevel* ** )
Lists the status of services that meet the specified criteria

#### Parameters


     *SCManager* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service control manager as returned by[win32service::OpenSCManager](#win32service.md#win32serviceOpenSCManager)

     *ServiceType=SERVICE_WIN32* : int

    Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)

     *ServiceState=SERVICE_STATE_ALL* : int

    Limits to services in specified state

     *GroupName=None* : str

    Name of group - use None for all, or '' for services that don't belong to a group

     *InfoLevel=SC_ENUM_PROCESS_INFO* : int

    Currently SC_ENUM_PROCESS_INFO is only level defined

#### Win32 API References


    Search for *EnumServicesStatusEx* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=EnumServicesStatusEx),[google](#README.md#http://www.google.com/search?q=EnumServicesStatusEx)or[google groups](#README.md#http://groups.google.com/groups?q=EnumServicesStatusEx).

#### Return Value
Returns a sequence of dicts, whose contents depend on information level requested. 

Currently, only information level supported is SC_ENUM_PROCESS_INFO (returns ENUM_SERVICE_STATUS_PROCESS).

## [win32service](#README.md#win32service).EnumWindowStations

([PyUnicode](#README.md#PyUnicode),,...) = **EnumWindowStations(** )
Lists names of window stations

#### Comments
Only window stations for which you have WINSTA_ENUMERATE access will be returned

## [win32service](#README.md#win32service).GetProcessWindowStation

[PyHWINSTA](#README.md#PyHWINSTA)= **GetProcessWindowStation(** )
Returns a handle to calling process's current window station

## [win32service](#README.md#win32service).GetServiceDisplayName

[PyUNICODE](#README.md#PyUNICODE)= **GetServiceDisplayName( *hSCManager*  *, ServiceName* ** )
Translates an internal service name into its display name

#### Parameters


     *hSCManager* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service control manager as returned by[win32service::OpenSCManager](#win32service.md#win32serviceOpenSCManager)

     *ServiceName* :[PyUNICODE](#README.md#PyUNICODE)

    Name of service

## [win32service](#README.md#win32service).GetServiceKeyName

[PyUNICODE](#README.md#PyUNICODE)= **GetServiceKeyName( *hSCManager*  *, DisplayName* ** )
Translates a service display name into its registry key name

#### Parameters


     *hSCManager* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service control manager as returned by[win32service::OpenSCManager](#win32service.md#win32serviceOpenSCManager)

     *DisplayName* :[PyUNICODE](#README.md#PyUNICODE)

    Display name of a service

## [win32service](#README.md#win32service).GetThreadDesktop

[PyHDESK](#README.md#PyHDESK)= **GetThreadDesktop( *ThreadId* ** )
Retrieves a handle to the desktop for a thread

#### Parameters


     *ThreadId* : int

    Id of thread

## [win32service](#README.md#win32service).GetUserObjectInformation

 **GetUserObjectInformation( *Handle*  *, type* ** )
Returns specified type of info about a window station or desktop

#### Parameters


     *Handle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to window station or desktop

     *type* : int

    Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SID

#### Return Value
Return type is dependent on UOI_* constant passed in

## [win32service](#README.md#win32service).LockServiceDatabase

int = **LockServiceDatabase( *sc_handle* ** )
Locks the service database.

#### Parameters


     *sc_handle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    A handle to the SCM.

## [win32service](#README.md#win32service).OpenDesktop

[PyHDESK](#README.md#PyHDESK)= **OpenDesktop( *szDesktop*  *, Flags*  *, Inherit*  *, DesiredAccess* ** )
Opens a handle to a desktop

#### Parameters


     *szDesktop* : str/unicode

    Name of desktop to open

     *Flags* : int

    DF_ALLOWOTHERACCOUNTHOOK or 0

     *Inherit* : bool

    Allow handle to be inherited

     *DesiredAccess* : int

    ACCESS_MASK specifying level of access for handle

## [win32service](#README.md#win32service).OpenInputDesktop

[PyHDESK](#README.md#PyHDESK)= **OpenInputDesktop( *Flags*  *, Inherit*  *, DesiredAccess* ** )
Returns a handle to desktop for logged-in user

#### Parameters


     *Flags* : int

    DF_ALLOWOTHERACCOUNTHOOK or 0

     *Inherit* : bool

    Specifies if handle will be inheritable

     *DesiredAccess* : int

    ACCESS_MASK specifying access available to returned handle

## [win32service](#README.md#win32service).OpenSCManager

[PySC_HANDLE](#PySC.md#PySCHANDLE)= **OpenSCManager( *machineName*  *, dbName*  *, desiredAccess* ** )
Returns a handle to the service control manager

#### Parameters


     *machineName* :[PyUnicode](#README.md#PyUnicode)

    The name of the computer, or None

     *dbName* :[PyUnicode](#README.md#PyUnicode)

    The name of the service database, or None

     *desiredAccess* : int

    The access desired. (combination of win32service.SC_MANAGER_* flags)

## [win32service](#README.md#win32service).OpenService

[PySC_HANDLE](#PySC.md#PySCHANDLE)= **OpenService( *scHandle*  *, name*  *, desiredAccess* ** )
Returns a handle to the specified service.

#### Parameters


     *scHandle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to the Service Control Mananger

     *name* :[PyUnicode](#README.md#PyUnicode)

    The name of the service to open.

     *desiredAccess* : int

    The access desired.

## [win32service](#README.md#win32service).OpenWindowStation

[PyHWINSTA](#README.md#PyHWINSTA)= **OpenWindowStation( *szWinSta*  *, Inherit*  *, DesiredAccess* ** )
Returns a handle to the specified window station

#### Parameters


     *szWinSta* : str/PyUNICODE

    Name of window station

     *Inherit* : Bool

    Allow handle to be inherited by subprocesses

     *DesiredAccess* : int

    Bitmask of access types

## [win32service](#README.md#win32service).QueryServiceConfig

tuple = **QueryServiceConfig( *hService* ** )
Retrieves configuration parameters for a service

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Service handle as returned by[win32service::OpenService](#win32service.md#win32serviceOpenService)

#### Return Value
Returns a tuple representing a QUERY_SERVICE_CONFIG struct:

#### Items


    [0] *int* : ServiceType

    Combination of SERVICE_*_DRIVER or SERVICE_*_PROCESS constants

    [1] *int* : StartType

    One of SERVICE_*_START constants

    [2] *int* : ErrorControl

    One of SERVICE_ERROR_* constants

    [3] *[PyUnicode](#README.md#PyUnicode)* : BinaryPathName

    Service's binary executable, can also contain command line args

    [4] *[PyUnicode](#README.md#PyUnicode)* : LoadOrderGroup

    Loading group that service is a member of

    [5] *int* : TagId

    Order of service within its load order group

    [6] *[[PyUnicode](#README.md#PyUnicode),...]* : Dependencies

    Sequence of names of services on which this service depends

    [7] *[PyUnicode](#README.md#PyUnicode)* : ServiceStartName

    Account name under which service will run

    [8] *[PyUnicode](#README.md#PyUnicode)* : DisplayName

    Name of service

## [win32service](#README.md#win32service).QueryServiceConfig2

object = **QueryServiceConfig2( *hService*  *, InfoLevel* ** )
Retrieves advanced service configuration options

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Service handle as returned by[win32service::OpenService](#win32service.md#win32serviceOpenService)

     *InfoLevel* : int

    One of win32service.SERVICE_CONFIG_* values

 **InfoLevel**  **Type of value returned** SERVICE_CONFIG_DESCRIPTIONUnicode stringSERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS structSERVICE_CONFIG_DELAYED_AUTO_START_INFOBooleanSERVICE_CONFIG_FAILURE_ACTIONS_FLAGBooleanSERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOList of unicode strings
#### Return Value
Type of returned object depends on InfoLevel

## [win32service](#README.md#win32service).QueryServiceLockStatus

(int,[PyUnicode](#README.md#PyUnicode), int) = **QueryServiceLockStatus( *hSCManager* ** )
Retrieves the lock status of the specified service control manager database.

#### Parameters


     *hSCManager* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to the SCM.

#### Return Value
The result is a tuple of (bIsLocked, userName, lockDuration)

## [win32service](#README.md#win32service).QueryServiceObjectSecurity

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **QueryServiceObjectSecurity( *Handle*  *, SecurityInformation* ** )
Retrieves information from the security descriptor for a service

#### Parameters


     *Handle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Service handle

     *SecurityInformation* : int

    Type of infomation to retrieve, combination of values from SECURITY_INFORMATION enum

## [win32service](#README.md#win32service).QueryServiceStatus

[SERVICE_STATUS](#SERVICE.md#SERVICESTATUS)= **QueryServiceStatus( *hService* ** )
Queries a service status

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service to be queried

## [win32service](#README.md#win32service).QueryServiceStatusEx

[SERVICE_STATUS](#SERVICE.md#SERVICESTATUS)= **QueryServiceStatusEx( *hService* ** )
Queries a service status

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to service to be queried

## SC_ACTION_NONE
 **const win32service.SC_ACTION_NONE;** 


## SC_ACTION_REBOOT
 **const win32service.SC_ACTION_REBOOT;** 


## SC_ACTION_RESTART
 **const win32service.SC_ACTION_RESTART;** 


## SC_ACTION_RUN_COMMAND
 **const win32service.SC_ACTION_RUN_COMMAND;** 


## SC_ENUM_PROCESS_INFO
 **const win32service.SC_ENUM_PROCESS_INFO;** 


## SC_GROUP_IDENTIFIER
 **const win32service.SC_GROUP_IDENTIFIER;** 


## SC_MANAGER_ALL_ACCESS
 **const win32service.SC_MANAGER_ALL_ACCESS;** 
Includes STANDARD_RIGHTS_REQUIRED, in addition to all of the access types listed in this table.

## SC_MANAGER_CONNECT
 **const win32service.SC_MANAGER_CONNECT;** 
Enables connecting to the service control manager.

## SC_MANAGER_CREATE_SERVICE
 **const win32service.SC_MANAGER_CREATE_SERVICE;** 
Enables calling of the CreateService function to create a service object and add it to the database.

## SC_MANAGER_ENUMERATE_SERVICE
 **const win32service.SC_MANAGER_ENUMERATE_SERVICE;** 
Enables calling of the EnumServicesStatus function to list the services that are in the database.

## SC_MANAGER_LOCK
 **const win32service.SC_MANAGER_LOCK;** 
Enables calling of the LockServiceDatabase function to acquire a lock on the database.

## SC_MANAGER_MODIFY_BOOT_CONFIG
 **const win32service.SC_MANAGER_MODIFY_BOOT_CONFIG;** 


## SC_MANAGER_QUERY_LOCK_STATUS
 **const win32service.SC_MANAGER_QUERY_LOCK_STATUS;** 
Enables calling of the QueryServiceLockStatus function to retrieve the lock status information for the database.

## SERVICE_ACCEPT_HARDWAREPROFILECHANGE
 **const win32service.SERVICE_ACCEPT_HARDWAREPROFILECHANGE;** 


## SERVICE_ACCEPT_NETBINDCHANGE
 **const win32service.SERVICE_ACCEPT_NETBINDCHANGE;** 


## SERVICE_ACCEPT_PARAMCHANGE
 **const win32service.SERVICE_ACCEPT_PARAMCHANGE;** 


## SERVICE_ACCEPT_PAUSE_CONTINUE
 **const win32service.SERVICE_ACCEPT_PAUSE_CONTINUE;** 
The service can be paused and continued. This enables the SERVICE_CONTROL_PAUSE and SERVICE_CONTROL_CONTINUE values.

## SERVICE_ACCEPT_POWEREVENT
 **const win32service.SERVICE_ACCEPT_POWEREVENT;** 


## SERVICE_ACCEPT_PRESHUTDOWN
 **const win32service.SERVICE_ACCEPT_PRESHUTDOWN;** 


## SERVICE_ACCEPT_SESSIONCHANGE
 **const win32service.SERVICE_ACCEPT_SESSIONCHANGE;** 


## SERVICE_ACCEPT_SHUTDOWN
 **const win32service.SERVICE_ACCEPT_SHUTDOWN;** 
The service is notified when system shutdown occurs. This enables the system to send a SERVICE_CONTROL_SHUTDOWN value to the service. The ControlService function cannot send this control

## SERVICE_ACCEPT_STOP
 **const win32service.SERVICE_ACCEPT_STOP;** 
The service can be stopped. This enables the SERVICE_CONTROL_STOP value.

## SERVICE_ACTIVE
 **const win32service.SERVICE_ACTIVE;** 


## SERVICE_ALL_ACCESS
 **const win32service.SERVICE_ALL_ACCESS;** 
Includes STANDARD_RIGHTS_REQUIRED in addition to all of the access types listed in this table.

## SERVICE_AUTO_START
 **const win32service.SERVICE_AUTO_START;** 
Specifies a device driver or Win32 service started by the service control manager automatically during system startup.

## SERVICE_BOOT_START
 **const win32service.SERVICE_BOOT_START;** 
Specifies a device driver started by the operating system loader. This value is valid only if the service type is SERVICE_KERNEL_DRIVER or SERVICE_FILE_SYSTEM_DRIVER.

## SERVICE_CHANGE_CONFIG
 **const win32service.SERVICE_CHANGE_CONFIG;** 
Enables calling of the ChangeServiceConfig function to change the service configuration.

## SERVICE_CONFIG_DELAYED_AUTO_START_INFO
 **const win32service.SERVICE_CONFIG_DELAYED_AUTO_START_INFO;** 


## SERVICE_CONFIG_DESCRIPTION
 **const win32service.SERVICE_CONFIG_DESCRIPTION;** 


## SERVICE_CONFIG_FAILURE_ACTIONS
 **const win32service.SERVICE_CONFIG_FAILURE_ACTIONS;** 
These require Vista or above

## SERVICE_CONFIG_FAILURE_ACTIONS_FLAG
 **const win32service.SERVICE_CONFIG_FAILURE_ACTIONS_FLAG;** 


## SERVICE_CONFIG_PRESHUTDOWN_INFO
 **const win32service.SERVICE_CONFIG_PRESHUTDOWN_INFO;** 


## SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO
 **const win32service.SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO;** 


## SERVICE_CONFIG_SERVICE_SID_INFO
 **const win32service.SERVICE_CONFIG_SERVICE_SID_INFO;** 


## SERVICE_CONTINUE_PENDING
 **const win32service.SERVICE_CONTINUE_PENDING;** 
The service continue is pending.

## SERVICE_CONTROL_CONTINUE
 **const win32service.SERVICE_CONTROL_CONTINUE;** 
Requests the paused service to resume. The hService handle must have SERVICE_PAUSE_CONTINUE access.

## SERVICE_CONTROL_DEVICEEVENT
 **const win32service.SERVICE_CONTROL_DEVICEEVENT;** 


## SERVICE_CONTROL_HARDWAREPROFILECHANGE
 **const win32service.SERVICE_CONTROL_HARDWAREPROFILECHANGE;** 


## SERVICE_CONTROL_INTERROGATE
 **const win32service.SERVICE_CONTROL_INTERROGATE;** 
Requests the service to update immediately its current status information to the service control manager. The hService handle must have SERVICE_INTERROGATE access.

## SERVICE_CONTROL_NETBINDADD
 **const win32service.SERVICE_CONTROL_NETBINDADD;** 


## SERVICE_CONTROL_NETBINDDISABLE
 **const win32service.SERVICE_CONTROL_NETBINDDISABLE;** 


## SERVICE_CONTROL_NETBINDENABLE
 **const win32service.SERVICE_CONTROL_NETBINDENABLE;** 


## SERVICE_CONTROL_NETBINDREMOVE
 **const win32service.SERVICE_CONTROL_NETBINDREMOVE;** 


## SERVICE_CONTROL_PARAMCHANGE
 **const win32service.SERVICE_CONTROL_PARAMCHANGE;** 


## SERVICE_CONTROL_PAUSE
 **const win32service.SERVICE_CONTROL_PAUSE;** 
Requests the service to pause. The hService handle must have SERVICE_PAUSE_CONTINUE access.

## SERVICE_CONTROL_POWEREVENT
 **const win32service.SERVICE_CONTROL_POWEREVENT;** 


## SERVICE_CONTROL_PRESHUTDOWN
 **const win32service.SERVICE_CONTROL_PRESHUTDOWN;** 


## SERVICE_CONTROL_SESSIONCHANGE
 **const win32service.SERVICE_CONTROL_SESSIONCHANGE;** 


## SERVICE_CONTROL_SHUTDOWN
 **const win32service.SERVICE_CONTROL_SHUTDOWN;** 
The ControlService function fails if this control code is specified.

## SERVICE_CONTROL_STOP
 **const win32service.SERVICE_CONTROL_STOP;** 
Requests the service to stop. The hService handle must have SERVICE_STOP access.

## SERVICE_DEMAND_START
 **const win32service.SERVICE_DEMAND_START;** 
Specifies a device driver or Win32 service started by the service control manager when a process calls the StartService function.

## SERVICE_DISABLED
 **const win32service.SERVICE_DISABLED;** 
Specifies a device driver or Win32 service that can no longer be started.

## SERVICE_DRIVER
 **const win32service.SERVICE_DRIVER;** 


## SERVICE_ENUMERATE_DEPENDENTS
 **const win32service.SERVICE_ENUMERATE_DEPENDENTS;** 
Enables calling of the EnumDependentServices function to enumerate all the services dependent on the service.

## SERVICE_ERROR_CRITICAL
 **const win32service.SERVICE_ERROR_CRITICAL;** 
The startup program logs the error, if possible. If the last-known good configuration is being started, 

the startup operation fails. Otherwise, the system is restarted with the last-known good configuration.

## SERVICE_ERROR_IGNORE
 **const win32service.SERVICE_ERROR_IGNORE;** 
The startup (boot) program logs the error but continues the startup operation.

## SERVICE_ERROR_NORMAL
 **const win32service.SERVICE_ERROR_NORMAL;** 
The startup program logs the error and displays a message box pop-up but continues the startup operation.

## SERVICE_ERROR_SEVERE
 **const win32service.SERVICE_ERROR_SEVERE;** 
The startup program logs the error. If the last-known good configuration is being started, 

the startup operation continues. Otherwise, the system is restarted with the last-known-good configuration.

## SERVICE_FILE_SYSTEM_DRIVER
 **const win32service.SERVICE_FILE_SYSTEM_DRIVER;** 
A service type flag that indicates a Windows NT file system driver.

## SERVICE_INACTIVE
 **const win32service.SERVICE_INACTIVE;** 


## SERVICE_INTERACTIVE_PROCESS
 **const win32service.SERVICE_INTERACTIVE_PROCESS;** 
A flag that indicates a Win32 service process that can interact with the desktop.

## SERVICE_INTERROGATE
 **const win32service.SERVICE_INTERROGATE;** 
Enables calling of the ControlService function to ask the service to report its status immediately.

## SERVICE_KERNEL_DRIVER
 **const win32service.SERVICE_KERNEL_DRIVER;** 
A service type flag that indicates a Windows NT device driver.

## SERVICE_NO_CHANGE
 **const win32service.SERVICE_NO_CHANGE;** 
Indicates the parameter should not be changed.

## SERVICE_PAUSED
 **const win32service.SERVICE_PAUSED;** 
The service is paused.

## SERVICE_PAUSE_CONTINUE
 **const win32service.SERVICE_PAUSE_CONTINUE;** 
Enables calling of the ControlService function to pause or continue the service.

## SERVICE_PAUSE_PENDING
 **const win32service.SERVICE_PAUSE_PENDING;** 
The service pause is pending.

## SERVICE_QUERY_CONFIG
 **const win32service.SERVICE_QUERY_CONFIG;** 
Enables calling of the QueryServiceConfig function to query the service configuration.

## SERVICE_QUERY_STATUS
 **const win32service.SERVICE_QUERY_STATUS;** 
Enables calling of the QueryServiceStatus function to ask the service control manager about the status of the service.

## SERVICE_RUNNING
 **const win32service.SERVICE_RUNNING;** 
The service is running.

## SERVICE_SID_TYPE_NONE
 **const win32service.SERVICE_SID_TYPE_NONE;** 


## SERVICE_SID_TYPE_RESTRICTED
 **const win32service.SERVICE_SID_TYPE_RESTRICTED;** 


## SERVICE_SID_TYPE_UNRESTRICTED
 **const win32service.SERVICE_SID_TYPE_UNRESTRICTED;** 


## SERVICE_SPECIFIC_ERROR
 **const win32service.SERVICE_SPECIFIC_ERROR;** 
A service specific error has occurred.

## SERVICE_START
 **const win32service.SERVICE_START;** 
Enables calling of the StartService function to start the service.

## SERVICE_START_PENDING
 **const win32service.SERVICE_START_PENDING;** 
The service is starting.

## SERVICE_STATE_ALL
 **const win32service.SERVICE_STATE_ALL;** 


## SERVICE_STOP
 **const win32service.SERVICE_STOP;** 
Enables calling of the ControlService function to stop the service.

## SERVICE_STOPPED
 **const win32service.SERVICE_STOPPED;** 
The service is not running.

## SERVICE_STOP_PENDING
 **const win32service.SERVICE_STOP_PENDING;** 
The service is stopping.

## SERVICE_SYSTEM_START
 **const win32service.SERVICE_SYSTEM_START;** 
Specifies a device driver started by the IoInitSystem function. This value is valid only if the service type is SERVICE_KERNEL_DRIVER or SERVICE_FILE_SYSTEM_DRIVER.

## SERVICE_USER_DEFINED_CONTROL
 **const win32service.SERVICE_USER_DEFINED_CONTROL;** 
Enables calling of the ControlService function to specify a user-defined control code.

## SERVICE_WIN32
 **const win32service.SERVICE_WIN32;** 


## SERVICE_WIN32_OWN_PROCESS
 **const win32service.SERVICE_WIN32_OWN_PROCESS;** 
A service type flag that indicates a Win32 service that runs in its own process.

## SERVICE_WIN32_SHARE_PROCESS
 **const win32service.SERVICE_WIN32_SHARE_PROCESS;** 
A service type flag that indicates a Win32 service that shares a process with other services.

## [win32service](#README.md#win32service).SetServiceObjectSecurity

 **SetServiceObjectSecurity( *Handle*  *, SecurityInformation*  *, SecurityDescriptor* ** )
Set the security descriptor for a service

#### Parameters


     *Handle* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Service handle

     *SecurityInformation* : int

    Type of infomation to set, combination of values from SECURITY_INFORMATION enum

     *SecurityDescriptor* :[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)

    PySECURITY_DESCRIPTOR containing infomation to set

## [win32service](#README.md#win32service).SetServiceStatus

 **SetServiceStatus( *scHandle*  *, serviceStatus* ** )
Sets a service status

#### Parameters


     *scHandle* : int

    Handle to set

     *serviceStatus* :[SERVICE_STATUS](#SERVICE.md#SERVICESTATUS)

    The new status

## [win32service](#README.md#win32service).SetUserObjectInformation

 **SetUserObjectInformation( *Handle*  *, info*  *, type* ** )
Set specified type of info for a window station or desktop object

#### Parameters


     *Handle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to window station or desktop

     *info* : object

    Information to set for handle, currently only a dictionary representing USEROBJECTFLAGS struct

     *type=UOI_FLAGS* : int

    Type of info to set, currently only accepts UOI_FLAGS

#### Comments
Currently only UOI_FLAGS supported

## [win32service](#README.md#win32service).StartService

 **StartService( *hService*  *, args* ** )
Starts the specified service

#### Parameters


     *hService* :[PySC_HANDLE](#PySC.md#PySCHANDLE)

    Handle to the service to be started

     *args* : [string, ...]

    Arguments to the service.

## UOI_FLAGS
 **const win32service.UOI_FLAGS;** 


## UOI_NAME
 **const win32service.UOI_NAME;** 


## UOI_TYPE
 **const win32service.UOI_TYPE;** 


## UOI_USER_SID
 **const win32service.UOI_USER_SID;** 


## [win32service](#README.md#win32service).UnlockServiceDatabase

int = **UnlockServiceDatabase( *lock* ** )
Unlocks the service database.

#### Parameters


     *lock* : int

    A lock provided by[win32service::LockServiceDatabase](#win32service.md#win32serviceLockServiceDatabase)

## WSF_VISIBLE
 **const win32service.WSF_VISIBLE;** 
