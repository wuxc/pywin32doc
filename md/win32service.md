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

    Returns a handle to the specified service\.&nbsp;

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

    Sends a control message to a service\.&nbsp;

  - [DeleteService](win32service.md#win32servicedeleteservice)

    Deletes the specified service&nbsp;

  - [CreateService](win32service.md#win32servicecreateservice)

    Creates a new service\.&nbsp;

  - [ChangeServiceConfig](win32service.md#win32servicechangeserviceconfig)

    Changes the configuration of an existing service\.&nbsp;

  - [LockServiceDatabase](win32service.md#win32servicelockservicedatabase)

    Locks the service database\.&nbsp;

  - [UnlockServiceDatabase](win32service.md#win32serviceunlockservicedatabase)

    Unlocks the service database\.&nbsp;

  - [QueryServiceLockStatus](win32service.md#win32servicequeryservicelockstatus)

    Retrieves the lock status of the specified service control manager database\.&nbsp;

  - [ChangeServiceConfig2](win32service.md#win32servicechangeserviceconfig2)

    Modifies advanced service parameters&nbsp;

  - [QueryServiceConfig2](win32service.md#win32servicequeryserviceconfig2)

    Retrieves advanced service configuration options&nbsp;

## [win32service](#win32service)\.ChangeServiceConfig



int/None =ChangeServiceConfig\(hService, serviceType, startType, errorControl, binaryFile, loadOrderGroup, bFetchTag, serviceDeps, acctName, password, displayName\)
Changes the configuration of an existing service\.

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    handle to service to be modified

  - serviceType : int

    type of service, or SERVICE\_NO\_CHANGE

  - startType : int

    When/how to start service, or SERVICE\_NO\_CHANGE

  - errorControl : int

    severity if service fails to start, or SERVICE\_NO\_CHANGE

  - binaryFile :[PyUnicode](#pyunicode)

    name of binary file, or None

  - loadOrderGroup :[PyUnicode](#pyunicode)

    name of load ordering group , or None

  - bFetchTag : int

    Should the tag be fetched and returned?  If TRUE, the result is the tag, else None\.

  - serviceDeps : \[[PyUnicode](#pyunicode),\.\.\.\]

    sequence of dependency names

  - acctName :[PyUnicode](#pyunicode)

    account name of service, or None

  - password :[PyUnicode](#pyunicode)

    password for service account , or None

  - displayName :[PyUnicode](#pyunicode)

    Display name

## [win32service](#win32service)\.ChangeServiceConfig2

ChangeServiceConfig2\(hService, InfoLevel, info\)
Modifies advanced service parameters

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Service handle as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)

  - InfoLevel : int

    One of win32service\.SERVICE\_CONFIG\_\* values

  - info : object

    Type depends on InfoLevel


## [win32service](#win32service)\.CloseServiceHandle

CloseServiceHandle\(scHandle\)
Closes a service or SCM handle

#### Parameters


  - scHandle :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to close

## [win32service](#win32service)\.ControlService

[SERVICE\_STATUS](SERVICE.md#servicestatus) =ControlService\(scHandle, code\)
Sends a control message to a service\.

#### Parameters


  - scHandle :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to control

  - code : int

    The service control code\.

#### Return Value
The result is the new service status\.

## [win32service](#win32service)\.CreateDesktop

[PyHDESK](#pyhdesk) =CreateDesktop\(Desktop, Flags, DesiredAccess, SecurityAttributes\)
Creates a new desktop in calling process's current window station

#### Parameters


  - Desktop : str/unicode

    Name of desktop to create

  - Flags : int

    DF\_ALLOWOTHERACCOUNTHOOK or 0

  - DesiredAccess : int

    An ACCESS\_MASK determining level of access available thru returned handle

  - SecurityAttributes :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and controls access to desktop

## [win32service](#win32service)\.CreateService

[PySC\_HANDLE](PySC.md#pyschandle)/\([PySC\_HANDLE](PySC.md#pyschandle), int\) =CreateService\(scHandle, name, displayName, desiredAccess, serviceType, startType, errorControl, binaryFile, loadOrderGroup, bFetchTag, serviceDeps, acctName, password\)
Creates a new service\.

#### Parameters


  - scHandle :[PySC\_HANDLE](PySC.md#pyschandle)

    handle to service control manager database

  - name :[PyUnicode](#pyunicode)

    Name of service

  - displayName :[PyUnicode](#pyunicode)

    Display name

  - desiredAccess : int

    type of access to service

  - serviceType : int

    type of service

  - startType : int

    When/how to start service

  - errorControl : int

    severity if service fails to start

  - binaryFile :[PyUnicode](#pyunicode)

    name of binary file

  - loadOrderGroup :[PyUnicode](#pyunicode)

    name of load ordering group , or None

  - bFetchTag : int

    Should the tag be fetched and returned?  If TRUE, the result is a tuple of \(handle, tag\), otherwise just handle\.

  - serviceDeps : \[[PyUnicode](#pyunicode),\.\.\.\]

    sequence of dependency names

  - acctName :[PyUnicode](#pyunicode)

    account name of service, or None

  - password :[PyUnicode](#pyunicode)

    password for service account , or None

## [win32service](#win32service)\.CreateWindowStation

[PyHWINSTA](#pyhwinsta) =CreateWindowStation\(WindowStation, Flags, DesiredAccess, SecurityAttributes\)
Creates a new window station

#### Parameters


  - WindowStation : str/unicode

    Name of window station to create, or None

  - Flags : int

    CWF\_CREATE\_ONLY or 0

  - DesiredAccess : int

    Bitmask of access types available to returned handle

  - SecurityAttributes :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security for window station, and whether handle is inheritable

#### Comments


If name is None or empty string, name is formatteded from logon id

## DBT\_CONFIGCHANGECANCELED
const win32service\.DBT\_CONFIGCHANGECANCELED;


## DBT\_CONFIGCHANGED
const win32service\.DBT\_CONFIGCHANGED;


## DBT\_CUSTOMEVENT
const win32service\.DBT\_CUSTOMEVENT;


user-defined event

## DBT\_DEVICEARRIVAL
const win32service\.DBT\_DEVICEARRIVAL;


system detected a new device

## DBT\_DEVICEQUERYREMOVE
const win32service\.DBT\_DEVICEQUERYREMOVE;


wants to remove, may fail

## DBT\_DEVICEQUERYREMOVEFAILED
const win32service\.DBT\_DEVICEQUERYREMOVEFAILED;


removal aborted

## DBT\_DEVICEREMOVECOMPLETE
const win32service\.DBT\_DEVICEREMOVECOMPLETE;


device is gone

## DBT\_DEVICEREMOVEPENDING
const win32service\.DBT\_DEVICEREMOVEPENDING;


about to remove, still avail\.

## DBT\_DEVICETYPESPECIFIC
const win32service\.DBT\_DEVICETYPESPECIFIC;


type specific event

## DBT\_QUERYCHANGECONFIG
const win32service\.DBT\_QUERYCHANGECONFIG;


## DF\_ALLOWOTHERACCOUNTHOOK
const win32service\.DF\_ALLOWOTHERACCOUNTHOOK;


\#define CWF\_CREATE\_ONLY CWF\_CREATE\_ONLY

## [win32service](#win32service)\.DeleteService

DeleteService\(scHandle\)
Deletes the specified service

#### Parameters


  - scHandle :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service to be deleted

## [win32service](#win32service)\.EnumDependentServices



\(tuple,\.\.\.\) =EnumDependentServices\(hService, ServiceState\)
Lists services that depend on a service

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service for which to list dependent services \(as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)\)

  - ServiceState=SERVICE\_STATE\_ALL : int

    Limits to services in specified state - One of SERVICE\_STATE\_ALL, SERVICE\_ACTIVE, SERVICE\_INACTIVE

#### Return Value
Returns a sequence of tuples representing ENUM\_SERVICE\_STATUS structs: \(ServiceName, DisplayName,[SERVICE\_STATUS](SERVICE.md#servicestatus)\)

## [win32service](#win32service)\.EnumServicesStatus



\(tuple,\.\.\.\) =EnumServicesStatus\(hSCManager, ServiceType, ServiceState\)
Returns a tuple of status info for each service that meets specified criteria

#### Parameters


  - hSCManager :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  - ServiceType=SERVICE\_WIN32 : int

    Types of services to enumerate \(SERVICE\_DRIVER and/or SERVICE\_WIN32\)

  - ServiceState=SERVICE\_STATE\_ALL : int

    Limits to services in specified state

#### Return Value
Returns a sequence of tuples representing ENUM\_SERVICE\_STATUS structs: \(ServiceName, DisplayName,[SERVICE\_STATUS](SERVICE.md#servicestatus)\)

## [win32service](#win32service)\.EnumServicesStatusEx



\(dict,\.\.\.\) =EnumServicesStatusEx\(SCManager, ServiceType, ServiceState, GroupName, InfoLevel\)
Lists the status of services that meet the specified criteria

#### Parameters


  - SCManager :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  - ServiceType=SERVICE\_WIN32 : int

    Types of services to enumerate \(SERVICE\_DRIVER and/or SERVICE\_WIN32\)

  - ServiceState=SERVICE\_STATE\_ALL : int

    Limits to services in specified state

  - GroupName=None : str

    Name of group - use None for all, or '' for services that don't belong to a group

  - InfoLevel=SC\_ENUM\_PROCESS\_INFO : int

    Currently SC\_ENUM\_PROCESS\_INFO is only level defined

#### Win32 API References


  - Search forEnumServicesStatusEx at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=enumservicesstatusex),[google](#http://www.google.com/search?q=enumservicesstatusex) or[google groups](#http://groups.google.com/groups?q=enumservicesstatusex)\.

#### Return Value
Returns a sequence of dicts, whose contents depend on information level requested\. 

Currently, only information level supported is SC\_ENUM\_PROCESS\_INFO \(returns ENUM\_SERVICE\_STATUS\_PROCESS\)\.

## [win32service](#win32service)\.EnumWindowStations



\([PyUnicode](#pyunicode),,\.\.\.\) =EnumWindowStations\(\)
Lists names of window stations

#### Comments


Only window stations for which you have WINSTA\_ENUMERATE access will be returned

## [win32service](#win32service)\.GetProcessWindowStation

[PyHWINSTA](#pyhwinsta) =GetProcessWindowStation\(\)
Returns a handle to calling process's current window station

## [win32service](#win32service)\.GetServiceDisplayName

[PyUNICODE](#pyunicode) =GetServiceDisplayName\(hSCManager, ServiceName\)
Translates an internal service name into its display name

#### Parameters


  - hSCManager :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  - ServiceName :[PyUNICODE](#pyunicode)

    Name of service

## [win32service](#win32service)\.GetServiceKeyName

[PyUNICODE](#pyunicode) =GetServiceKeyName\(hSCManager, DisplayName\)
Translates a service display name into its registry key name

#### Parameters


  - hSCManager :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service control manager as returned by[win32service::OpenSCManager](win32service.md#win32serviceopenscmanager)

  - DisplayName :[PyUNICODE](#pyunicode)

    Display name of a service

## [win32service](#win32service)\.GetThreadDesktop

[PyHDESK](#pyhdesk) =GetThreadDesktop\(ThreadId\)
Retrieves a handle to the desktop for a thread

#### Parameters


  - ThreadId : int

    Id of thread

## [win32service](#win32service)\.GetUserObjectInformation

GetUserObjectInformation\(Handle, type\)
Returns specified type of info about a window station or desktop

#### Parameters


  - Handle :[PyHANDLE](#pyhandle)

    Handle to window station or desktop

  - type : int

    Type of info to return, one of UOI\_FLAGS,UOI\_NAME, UOI\_TYPE, or UOI\_USER\_SID

#### Return Value
Return type is dependent on UOI\_\* constant passed in

## [win32service](#win32service)\.LockServiceDatabase



int =LockServiceDatabase\(sc\_handle\)
Locks the service database\.

#### Parameters


  - sc\_handle :[PySC\_HANDLE](PySC.md#pyschandle)

    A handle to the SCM\.

## [win32service](#win32service)\.OpenDesktop

[PyHDESK](#pyhdesk) =OpenDesktop\(szDesktop, Flags, Inherit, DesiredAccess\)
Opens a handle to a desktop

#### Parameters


  - szDesktop : str/unicode

    Name of desktop to open

  - Flags : int

    DF\_ALLOWOTHERACCOUNTHOOK or 0

  - Inherit : bool

    Allow handle to be inherited

  - DesiredAccess : int

    ACCESS\_MASK specifying level of access for handle

## [win32service](#win32service)\.OpenInputDesktop

[PyHDESK](#pyhdesk) =OpenInputDesktop\(Flags, Inherit, DesiredAccess\)
Returns a handle to desktop for logged-in user

#### Parameters


  - Flags : int

    DF\_ALLOWOTHERACCOUNTHOOK or 0

  - Inherit : bool

    Specifies if handle will be inheritable

  - DesiredAccess : int

    ACCESS\_MASK specifying access available to returned handle

## [win32service](#win32service)\.OpenSCManager

[PySC\_HANDLE](PySC.md#pyschandle) =OpenSCManager\(machineName, dbName, desiredAccess\)
Returns a handle to the service control manager

#### Parameters


  - machineName :[PyUnicode](#pyunicode)

    The name of the computer, or None

  - dbName :[PyUnicode](#pyunicode)

    The name of the service database, or None

  - desiredAccess : int

    The access desired\. \(combination of win32service\.SC\_MANAGER\_\* flags\)

## [win32service](#win32service)\.OpenService

[PySC\_HANDLE](PySC.md#pyschandle) =OpenService\(scHandle, name, desiredAccess\)
Returns a handle to the specified service\.

#### Parameters


  - scHandle :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to the Service Control Mananger

  - name :[PyUnicode](#pyunicode)

    The name of the service to open\.

  - desiredAccess : int

    The access desired\.

## [win32service](#win32service)\.OpenWindowStation

[PyHWINSTA](#pyhwinsta) =OpenWindowStation\(szWinSta, Inherit, DesiredAccess\)
Returns a handle to the specified window station

#### Parameters


  - szWinSta : str/PyUNICODE

    Name of window station

  - Inherit : Bool

    Allow handle to be inherited by subprocesses

  - DesiredAccess : int

    Bitmask of access types

## [win32service](#win32service)\.QueryServiceConfig



tuple =QueryServiceConfig\(hService\)
Retrieves configuration parameters for a service

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Service handle as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)

#### Return Value
Returns a tuple representing a QUERY\_SERVICE\_CONFIG struct:

#### Items


  - \[0\]int : ServiceType

    Combination of SERVICE\_\*\_DRIVER or SERVICE\_\*\_PROCESS constants

  - \[1\]int : StartType

    One of SERVICE\_\*\_START constants

  - \[2\]int : ErrorControl

    One of SERVICE\_ERROR\_\* constants

  - \[3\][PyUnicode](#pyunicode) : BinaryPathName

    Service's binary executable, can also contain command line args

  - \[4\][PyUnicode](#pyunicode) : LoadOrderGroup

    Loading group that service is a member of

  - \[5\]int : TagId

    Order of service within its load order group

  - \[6\]\[[PyUnicode](#pyunicode),\.\.\.\] : Dependencies

    Sequence of names of services on which this service depends

  - \[7\][PyUnicode](#pyunicode) : ServiceStartName

    Account name under which service will run

  - \[8\][PyUnicode](#pyunicode) : DisplayName

    Name of service

## [win32service](#win32service)\.QueryServiceConfig2



object =QueryServiceConfig2\(hService, InfoLevel\)
Retrieves advanced service configuration options

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Service handle as returned by[win32service::OpenService](win32service.md#win32serviceopenservice)

  - InfoLevel : int

    One of win32service\.SERVICE\_CONFIG\_\* values

InfoLevelType of value returnedSERVICE\_CONFIG\_DESCRIPTIONUnicode stringSERVICE\_CONFIG\_FAILURE\_ACTIONSDict representing a SERVICE\_FAILURE\_ACTIONS structSERVICE\_CONFIG\_DELAYED\_AUTO\_START\_INFOBooleanSERVICE\_CONFIG\_FAILURE\_ACTIONS\_FLAGBooleanSERVICE\_CONFIG\_PRESHUTDOWN\_INFOint \(shutdown timeout in milliseconds\)SERVICE\_CONFIG\_SERVICE\_SID\_INFOint \(SERVICE\_SID\_TYPE\_\*\)SERVICE\_CONFIG\_REQUIRED\_PRIVILEGES\_INFOList of unicode strings
#### Return Value
Type of returned object depends on InfoLevel

## [win32service](#win32service)\.QueryServiceLockStatus



\(int,[PyUnicode](#pyunicode), int\) =QueryServiceLockStatus\(hSCManager\)
Retrieves the lock status of the specified service control manager database\.

#### Parameters


  - hSCManager :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to the SCM\.

#### Return Value
The result is a tuple of \(bIsLocked, userName, lockDuration\)

## [win32service](#win32service)\.QueryServiceObjectSecurity

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) =QueryServiceObjectSecurity\(Handle, SecurityInformation\)
Retrieves information from the security descriptor for a service

#### Parameters


  - Handle :[PySC\_HANDLE](PySC.md#pyschandle)

    Service handle

  - SecurityInformation : int

    Type of infomation to retrieve, combination of values from SECURITY\_INFORMATION enum

## [win32service](#win32service)\.QueryServiceStatus

[SERVICE\_STATUS](SERVICE.md#servicestatus) =QueryServiceStatus\(hService\)
Queries a service status

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service to be queried

## [win32service](#win32service)\.QueryServiceStatusEx

[SERVICE\_STATUS](SERVICE.md#servicestatus) =QueryServiceStatusEx\(hService\)
Queries a service status

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to service to be queried

## SC\_ACTION\_NONE
const win32service\.SC\_ACTION\_NONE;


## SC\_ACTION\_REBOOT
const win32service\.SC\_ACTION\_REBOOT;


## SC\_ACTION\_RESTART
const win32service\.SC\_ACTION\_RESTART;


## SC\_ACTION\_RUN\_COMMAND
const win32service\.SC\_ACTION\_RUN\_COMMAND;


## SC\_ENUM\_PROCESS\_INFO
const win32service\.SC\_ENUM\_PROCESS\_INFO;


## SC\_GROUP\_IDENTIFIER
const win32service\.SC\_GROUP\_IDENTIFIER;


## SC\_MANAGER\_ALL\_ACCESS
const win32service\.SC\_MANAGER\_ALL\_ACCESS;


Includes STANDARD\_RIGHTS\_REQUIRED, in addition to all of the access types listed in this table\.

## SC\_MANAGER\_CONNECT
const win32service\.SC\_MANAGER\_CONNECT;


Enables connecting to the service control manager\.

## SC\_MANAGER\_CREATE\_SERVICE
const win32service\.SC\_MANAGER\_CREATE\_SERVICE;


Enables calling of the CreateService function to create a service object and add it to the database\.

## SC\_MANAGER\_ENUMERATE\_SERVICE
const win32service\.SC\_MANAGER\_ENUMERATE\_SERVICE;


Enables calling of the EnumServicesStatus function to list the services that are in the database\.

## SC\_MANAGER\_LOCK
const win32service\.SC\_MANAGER\_LOCK;


Enables calling of the LockServiceDatabase function to acquire a lock on the database\.

## SC\_MANAGER\_MODIFY\_BOOT\_CONFIG
const win32service\.SC\_MANAGER\_MODIFY\_BOOT\_CONFIG;


## SC\_MANAGER\_QUERY\_LOCK\_STATUS
const win32service\.SC\_MANAGER\_QUERY\_LOCK\_STATUS;


Enables calling of the QueryServiceLockStatus function to retrieve the lock status information for the database\.

## SERVICE\_ACCEPT\_HARDWAREPROFILECHANGE
const win32service\.SERVICE\_ACCEPT\_HARDWAREPROFILECHANGE;


## SERVICE\_ACCEPT\_NETBINDCHANGE
const win32service\.SERVICE\_ACCEPT\_NETBINDCHANGE;


## SERVICE\_ACCEPT\_PARAMCHANGE
const win32service\.SERVICE\_ACCEPT\_PARAMCHANGE;


## SERVICE\_ACCEPT\_PAUSE\_CONTINUE
const win32service\.SERVICE\_ACCEPT\_PAUSE\_CONTINUE;


The service can be paused and continued\. This enables the SERVICE\_CONTROL\_PAUSE and SERVICE\_CONTROL\_CONTINUE values\.

## SERVICE\_ACCEPT\_POWEREVENT
const win32service\.SERVICE\_ACCEPT\_POWEREVENT;


## SERVICE\_ACCEPT\_PRESHUTDOWN
const win32service\.SERVICE\_ACCEPT\_PRESHUTDOWN;


## SERVICE\_ACCEPT\_SESSIONCHANGE
const win32service\.SERVICE\_ACCEPT\_SESSIONCHANGE;


## SERVICE\_ACCEPT\_SHUTDOWN
const win32service\.SERVICE\_ACCEPT\_SHUTDOWN;


The service is notified when system shutdown occurs\. This enables the system to send a SERVICE\_CONTROL\_SHUTDOWN value to the service\. The ControlService function cannot send this control

## SERVICE\_ACCEPT\_STOP
const win32service\.SERVICE\_ACCEPT\_STOP;


The service can be stopped\. This enables the SERVICE\_CONTROL\_STOP value\.

## SERVICE\_ACTIVE
const win32service\.SERVICE\_ACTIVE;


## SERVICE\_ALL\_ACCESS
const win32service\.SERVICE\_ALL\_ACCESS;


Includes STANDARD\_RIGHTS\_REQUIRED in addition to all of the access types listed in this table\.

## SERVICE\_AUTO\_START
const win32service\.SERVICE\_AUTO\_START;


Specifies a device driver or Win32 service started by the service control manager automatically during system startup\.

## SERVICE\_BOOT\_START
const win32service\.SERVICE\_BOOT\_START;


Specifies a device driver started by the operating system loader\. This value is valid only if the service type is SERVICE\_KERNEL\_DRIVER or SERVICE\_FILE\_SYSTEM\_DRIVER\.

## SERVICE\_CHANGE\_CONFIG
const win32service\.SERVICE\_CHANGE\_CONFIG;


Enables calling of the ChangeServiceConfig function to change the service configuration\.

## SERVICE\_CONFIG\_DELAYED\_AUTO\_START\_INFO
const win32service\.SERVICE\_CONFIG\_DELAYED\_AUTO\_START\_INFO;


## SERVICE\_CONFIG\_DESCRIPTION
const win32service\.SERVICE\_CONFIG\_DESCRIPTION;


## SERVICE\_CONFIG\_FAILURE\_ACTIONS
const win32service\.SERVICE\_CONFIG\_FAILURE\_ACTIONS;


These require Vista or above

## SERVICE\_CONFIG\_FAILURE\_ACTIONS\_FLAG
const win32service\.SERVICE\_CONFIG\_FAILURE\_ACTIONS\_FLAG;


## SERVICE\_CONFIG\_PRESHUTDOWN\_INFO
const win32service\.SERVICE\_CONFIG\_PRESHUTDOWN\_INFO;


## SERVICE\_CONFIG\_REQUIRED\_PRIVILEGES\_INFO
const win32service\.SERVICE\_CONFIG\_REQUIRED\_PRIVILEGES\_INFO;


## SERVICE\_CONFIG\_SERVICE\_SID\_INFO
const win32service\.SERVICE\_CONFIG\_SERVICE\_SID\_INFO;


## SERVICE\_CONTINUE\_PENDING
const win32service\.SERVICE\_CONTINUE\_PENDING;


The service continue is pending\.

## SERVICE\_CONTROL\_CONTINUE
const win32service\.SERVICE\_CONTROL\_CONTINUE;


Requests the paused service to resume\. The hService handle must have SERVICE\_PAUSE\_CONTINUE access\.

## SERVICE\_CONTROL\_DEVICEEVENT
const win32service\.SERVICE\_CONTROL\_DEVICEEVENT;


## SERVICE\_CONTROL\_HARDWAREPROFILECHANGE
const win32service\.SERVICE\_CONTROL\_HARDWAREPROFILECHANGE;


## SERVICE\_CONTROL\_INTERROGATE
const win32service\.SERVICE\_CONTROL\_INTERROGATE;


Requests the service to update immediately its current status information to the service control manager\. The hService handle must have SERVICE\_INTERROGATE access\.

## SERVICE\_CONTROL\_NETBINDADD
const win32service\.SERVICE\_CONTROL\_NETBINDADD;


## SERVICE\_CONTROL\_NETBINDDISABLE
const win32service\.SERVICE\_CONTROL\_NETBINDDISABLE;


## SERVICE\_CONTROL\_NETBINDENABLE
const win32service\.SERVICE\_CONTROL\_NETBINDENABLE;


## SERVICE\_CONTROL\_NETBINDREMOVE
const win32service\.SERVICE\_CONTROL\_NETBINDREMOVE;


## SERVICE\_CONTROL\_PARAMCHANGE
const win32service\.SERVICE\_CONTROL\_PARAMCHANGE;


## SERVICE\_CONTROL\_PAUSE
const win32service\.SERVICE\_CONTROL\_PAUSE;


Requests the service to pause\. The hService handle must have SERVICE\_PAUSE\_CONTINUE access\.

## SERVICE\_CONTROL\_POWEREVENT
const win32service\.SERVICE\_CONTROL\_POWEREVENT;


## SERVICE\_CONTROL\_PRESHUTDOWN
const win32service\.SERVICE\_CONTROL\_PRESHUTDOWN;


## SERVICE\_CONTROL\_SESSIONCHANGE
const win32service\.SERVICE\_CONTROL\_SESSIONCHANGE;


## SERVICE\_CONTROL\_SHUTDOWN
const win32service\.SERVICE\_CONTROL\_SHUTDOWN;


The ControlService function fails if this control code is specified\.

## SERVICE\_CONTROL\_STOP
const win32service\.SERVICE\_CONTROL\_STOP;


Requests the service to stop\. The hService handle must have SERVICE\_STOP access\.

## SERVICE\_DEMAND\_START
const win32service\.SERVICE\_DEMAND\_START;


Specifies a device driver or Win32 service started by the service control manager when a process calls the StartService function\.

## SERVICE\_DISABLED
const win32service\.SERVICE\_DISABLED;


Specifies a device driver or Win32 service that can no longer be started\.

## SERVICE\_DRIVER
const win32service\.SERVICE\_DRIVER;


## SERVICE\_ENUMERATE\_DEPENDENTS
const win32service\.SERVICE\_ENUMERATE\_DEPENDENTS;


Enables calling of the EnumDependentServices function to enumerate all the services dependent on the service\.

## SERVICE\_ERROR\_CRITICAL
const win32service\.SERVICE\_ERROR\_CRITICAL;


The startup program logs the error, if possible\. If the last-known good configuration is being started, 

the startup operation fails\. Otherwise, the system is restarted with the last-known good configuration\.

## SERVICE\_ERROR\_IGNORE
const win32service\.SERVICE\_ERROR\_IGNORE;


The startup \(boot\) program logs the error but continues the startup operation\.

## SERVICE\_ERROR\_NORMAL
const win32service\.SERVICE\_ERROR\_NORMAL;


The startup program logs the error and displays a message box pop-up but continues the startup operation\.

## SERVICE\_ERROR\_SEVERE
const win32service\.SERVICE\_ERROR\_SEVERE;


The startup program logs the error\. If the last-known good configuration is being started, 

the startup operation continues\. Otherwise, the system is restarted with the last-known-good configuration\.

## SERVICE\_FILE\_SYSTEM\_DRIVER
const win32service\.SERVICE\_FILE\_SYSTEM\_DRIVER;


A service type flag that indicates a Windows NT file system driver\.

## SERVICE\_INACTIVE
const win32service\.SERVICE\_INACTIVE;


## SERVICE\_INTERACTIVE\_PROCESS
const win32service\.SERVICE\_INTERACTIVE\_PROCESS;


A flag that indicates a Win32 service process that can interact with the desktop\.

## SERVICE\_INTERROGATE
const win32service\.SERVICE\_INTERROGATE;


Enables calling of the ControlService function to ask the service to report its status immediately\.

## SERVICE\_KERNEL\_DRIVER
const win32service\.SERVICE\_KERNEL\_DRIVER;


A service type flag that indicates a Windows NT device driver\.

## SERVICE\_NO\_CHANGE
const win32service\.SERVICE\_NO\_CHANGE;


Indicates the parameter should not be changed\.

## SERVICE\_PAUSED
const win32service\.SERVICE\_PAUSED;


The service is paused\.

## SERVICE\_PAUSE\_CONTINUE
const win32service\.SERVICE\_PAUSE\_CONTINUE;


Enables calling of the ControlService function to pause or continue the service\.

## SERVICE\_PAUSE\_PENDING
const win32service\.SERVICE\_PAUSE\_PENDING;


The service pause is pending\.

## SERVICE\_QUERY\_CONFIG
const win32service\.SERVICE\_QUERY\_CONFIG;


Enables calling of the QueryServiceConfig function to query the service configuration\.

## SERVICE\_QUERY\_STATUS
const win32service\.SERVICE\_QUERY\_STATUS;


Enables calling of the QueryServiceStatus function to ask the service control manager about the status of the service\.

## SERVICE\_RUNNING
const win32service\.SERVICE\_RUNNING;


The service is running\.

## SERVICE\_SID\_TYPE\_NONE
const win32service\.SERVICE\_SID\_TYPE\_NONE;


## SERVICE\_SID\_TYPE\_RESTRICTED
const win32service\.SERVICE\_SID\_TYPE\_RESTRICTED;


## SERVICE\_SID\_TYPE\_UNRESTRICTED
const win32service\.SERVICE\_SID\_TYPE\_UNRESTRICTED;


## SERVICE\_SPECIFIC\_ERROR
const win32service\.SERVICE\_SPECIFIC\_ERROR;


A service specific error has occurred\.

## SERVICE\_START
const win32service\.SERVICE\_START;


Enables calling of the StartService function to start the service\.

## SERVICE\_START\_PENDING
const win32service\.SERVICE\_START\_PENDING;


The service is starting\.

## SERVICE\_STATE\_ALL
const win32service\.SERVICE\_STATE\_ALL;


## SERVICE\_STOP
const win32service\.SERVICE\_STOP;


Enables calling of the ControlService function to stop the service\.

## SERVICE\_STOPPED
const win32service\.SERVICE\_STOPPED;


The service is not running\.

## SERVICE\_STOP\_PENDING
const win32service\.SERVICE\_STOP\_PENDING;


The service is stopping\.

## SERVICE\_SYSTEM\_START
const win32service\.SERVICE\_SYSTEM\_START;


Specifies a device driver started by the IoInitSystem function\. This value is valid only if the service type is SERVICE\_KERNEL\_DRIVER or SERVICE\_FILE\_SYSTEM\_DRIVER\.

## SERVICE\_USER\_DEFINED\_CONTROL
const win32service\.SERVICE\_USER\_DEFINED\_CONTROL;


Enables calling of the ControlService function to specify a user-defined control code\.

## SERVICE\_WIN32
const win32service\.SERVICE\_WIN32;


## SERVICE\_WIN32\_OWN\_PROCESS
const win32service\.SERVICE\_WIN32\_OWN\_PROCESS;


A service type flag that indicates a Win32 service that runs in its own process\.

## SERVICE\_WIN32\_SHARE\_PROCESS
const win32service\.SERVICE\_WIN32\_SHARE\_PROCESS;


A service type flag that indicates a Win32 service that shares a process with other services\.

## [win32service](#win32service)\.SetServiceObjectSecurity

SetServiceObjectSecurity\(Handle, SecurityInformation, SecurityDescriptor\)
Set the security descriptor for a service

#### Parameters


  - Handle :[PySC\_HANDLE](PySC.md#pyschandle)

    Service handle

  - SecurityInformation : int

    Type of infomation to set, combination of values from SECURITY\_INFORMATION enum

  - SecurityDescriptor :[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    PySECURITY\_DESCRIPTOR containing infomation to set

## [win32service](#win32service)\.SetServiceStatus

SetServiceStatus\(scHandle, serviceStatus\)
Sets a service status

#### Parameters


  - scHandle : int

    Handle to set

  - serviceStatus :[SERVICE\_STATUS](SERVICE.md#servicestatus)

    The new status

## [win32service](#win32service)\.SetUserObjectInformation

SetUserObjectInformation\(Handle, info, type\)
Set specified type of info for a window station or desktop object

#### Parameters


  - Handle :[PyHANDLE](#pyhandle)

    Handle to window station or desktop

  - info : object

    Information to set for handle, currently only a dictionary representing USEROBJECTFLAGS struct

  - type=UOI\_FLAGS : int

    Type of info to set, currently only accepts UOI\_FLAGS

#### Comments


Currently only UOI\_FLAGS supported

## [win32service](#win32service)\.StartService

StartService\(hService, args\)
Starts the specified service

#### Parameters


  - hService :[PySC\_HANDLE](PySC.md#pyschandle)

    Handle to the service to be started

  - args : \[string, \.\.\.\]

    Arguments to the service\.

## UOI\_FLAGS
const win32service\.UOI\_FLAGS;


## UOI\_NAME
const win32service\.UOI\_NAME;


## UOI\_TYPE
const win32service\.UOI\_TYPE;


## UOI\_USER\_SID
const win32service\.UOI\_USER\_SID;


## [win32service](#win32service)\.UnlockServiceDatabase



int =UnlockServiceDatabase\(lock\)
Unlocks the service database\.

#### Parameters


  - lock : int

    A lock provided by[win32service::LockServiceDatabase](win32service.md#win32servicelockservicedatabase)

## WSF\_VISIBLE
const win32service\.WSF\_VISIBLE;
