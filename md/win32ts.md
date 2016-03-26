# win32ts


## Module win32ts

Interface to the Terminal Services Api 

All functions in this module accept keyword arguments

#### Methods

  - [WTSOpenServer](win32ts.md#win32tswtsopenserver)

    Opens a handle to a terminal server&nbsp;

  - [WTSCloseServer](win32ts.md#win32tswtscloseserver)

    Closes a terminal server handle&nbsp;

  - [WTSQueryUserConfig](win32ts.md#win32tswtsqueryuserconfig)

    Returns user configuration&nbsp;

  - [WTSSetUserConfig](win32ts.md#win32tswtssetuserconfig)

    Changes user configuration&nbsp;

  - [WTSEnumerateServers](win32ts.md#win32tswtsenumerateservers)

    Lists terminal servers in a domain&nbsp;

  - [WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

    Lists sessions on a server&nbsp;

  - [WTSLogoffSession](win32ts.md#win32tswtslogoffsession)

    Logs off a user logged in through Terminal Services&nbsp;

  - [WTSDisconnectSession](win32ts.md#win32tswtsdisconnectsession)

    Disconnects a session without logging it off&nbsp;

  - [WTSQuerySessionInformation](win32ts.md#win32tswtsquerysessioninformation)

    Retrieve information about a session&nbsp;

  - [WTSEnumerateProcesses](win32ts.md#win32tswtsenumerateprocesses)

    Lists processes on a terminal server&nbsp;

  - [WTSQueryUserToken](win32ts.md#win32tswtsqueryusertoken)

    Retrieves the access token for a session&nbsp;

  - [WTSShutdownSystem](win32ts.md#win32tswtsshutdownsystem)

    Issues a shutdown request to a terminal server&nbsp;

  - [WTSTerminateProcess](win32ts.md#win32tswtsterminateprocess)

    Kills a process on a terminal server&nbsp;

  - [ProcessIdToSessionId](win32ts.md#win32tsprocessidtosessionid)

    Finds the session under which a process is running&nbsp;

  - [WTSGetActiveConsoleSessionId](win32ts.md#win32tswtsgetactiveconsolesessionid)

    Returns the id of the console session&nbsp;

  - [WTSRegisterSessionNotification](win32ts.md#win32tswtsregistersessionnotification)

    Registers a window to receive terminal service notifications&nbsp;

  - [WTSUnRegisterSessionNotification](win32ts.md#win32tswtsunregistersessionnotification)

    Disables terminal service window messages&nbsp;

  - [WTSWaitSystemEvent](win32ts.md#win32tswtswaitsystemevent)

    Waits for an event to occur&nbsp;

  - [WTSSendMessage](win32ts.md#win32tswtssendmessage)

    Sends a popup message to a terminal services session&nbsp;


## [win32ts](win32ts.md#win32ts)\.ProcessIdToSessionId

int = ProcessIdToSessionId\(ProcessId\)
Finds the session under which a process is running

#### Parameters

  - ProcessId : int

    Id of a process as returned by [win32ts::WTSEnumerateProcesses](win32ts.md#win32tswtsenumerateprocesses)


## [win32ts](win32ts.md#win32ts)\.WTSCloseServer

WTSCloseServer\(Server\)
Closes a terminal server handle

#### Parameters

  - Server : [PyHANDLE](PyHANDLE.md)

    Terminal Server handle


## [win32ts](win32ts.md#win32ts)\.WTSDisconnectSession

WTSDisconnectSession\(Server, SessionId, Wait\)
Disconnects a session without logging it off

#### Parameters

  - Server : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server

  - SessionId : int

    Terminal services session id as returned by [win32ts::WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

  - Wait : boolean

    Indicates whether operation should be performed asynchronously


## [win32ts](win32ts.md#win32ts)\.WTSEnumerateProcesses

\([PyUnicode](PyUnicode.md),\.\.\.\) = WTSEnumerateProcesses\(Server, Version

, Reserved

\)
Lists processes on a terminal server

#### Parameters

  - Server=WTS\_CURRENT\_SERVER\_HANDLE : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server

  - Version=1 : int

    Version of request, currently 1 is only valid value

  - Reserved=0 : int

    Reserved, use 0 if passed in


## [win32ts](win32ts.md#win32ts)\.WTSEnumerateServers

\([PyUnicode](PyUnicode.md),\.\.\.\) = WTSEnumerateServers\(DomainName, Version

, Reserved

\)
Lists terminal servers in a domain

#### Parameters

  - DomainName=None : [PyUnicode](PyUnicode.md)

    Use None for current domain

  - Version=1 : int

    Version of request, currently 1 is only valid value

  - Reserved=0 : int

    Reserved, use 0 if passed in


## [win32ts](win32ts.md#win32ts)\.WTSEnumerateSessions

\(dict,\.\.\.\) = WTSEnumerateSessions\(Server, Version

, Reserved

\)
Lists sessions on a server

#### Parameters

  - Server=WTS\_CURRENT\_SERVER\_HANDLE : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server

  - Version=1 : int

    Version of request, currently 1 is only valid value

  - Reserved=0 : int

    Reserved, use 0 if passed in

#### Return Value
Returns a sequence of dictionaries representing WTS\_SESSION\_INFO structs, containing \{SessionId:int, WinStationName:str, State:int\}


## [win32ts](win32ts.md#win32ts)\.WTSGetActiveConsoleSessionId

int = WTSGetActiveConsoleSessionId\(\)
Returns the id of the console session

#### Comments

Returns 0xffffffff if no active console session exists


## [win32ts](win32ts.md#win32ts)\.WTSLogoffSession

WTSLogoffSession\(Server, SessionId, Wait\)
Logs off a user logged in through Terminal Services

#### Parameters

  - Server : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server

  - SessionId : int

    Terminal services session id as returned by [win32ts::WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

  - Wait : boolean

    Indicates whether operation should be performed asynchronously


## [win32ts](win32ts.md#win32ts)\.WTSOpenServer

[PyHANDLE](PyHANDLE.md) = WTSOpenServer\(ServerName\)
Opens a handle to a terminal server

#### Parameters

  - ServerName : [PyUnicode](PyUnicode.md)

    Name ot terminal server to be opened


## [win32ts](win32ts.md#win32ts)\.WTSQuerySessionInformation

WTSQuerySessionInformation\(Server, SessionId, WTSInfoClass\)
Returns information about a terminal services session

#### Parameters

  - Server : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server as returned by [win32ts::WTSOpenServer](win32ts.md#win32tswtsopenserver)

  - SessionId : int

    Terminal services session id as returned by [win32ts::WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

  - WTSInfoClass : int

    Type of information requested, from WTS\_INFO\_CLASS enum



## [win32ts](win32ts.md#win32ts)\.WTSQueryUserConfig

object = WTSQueryUserConfig\(ServerName, UserName

, ConfigClass

\)
Returns user configuration

#### Parameters

  - ServerName : [PyUnicode](PyUnicode.md)

    Name ot terminal server

  - UserName : [PyUnicode](PyUnicode.md)

    Name of user

  - ConfigClass : int

    Type of information to be returned, win32ts\.WTSUserConfig\*

   

       ConfigClass

   

   

       Returned value

   

WTSUserConfigInitialProgramUnicode string, program to be run when user logs on

WTSUserConfigWorkingDirectoryUnicode string, working dir for initial program

WTSUserConfigModemCallbackPhoneNumberUnicode string

WTSUserConfigTerminalServerProfilePathUnicode string

WTSUserConfigTerminalServerHomeDirUnicode string

WTSUserConfigTerminalServerHomeDirDriveUnicode string

WTSUserConfigfInheritInitialProgramInt

WTSUserConfigfAllowLogonTerminalServerInt, 1 if user can log on thru Terminal Service

WTSUserConfigTimeoutSettingsConnectionsInt, max connection time \(ms\)

WTSUserConfigTimeoutSettingsDisconnectionsInt

WTSUserConfigTimeoutSettingsIdleInt, max idle time \(ms\)

WTSUserConfigfDeviceClientDrivesInt

WTSUserConfigfDeviceClientPrintersInt

WTSUserConfigfDeviceClientDefaultPrinterInt

WTSUserConfigBrokenTimeoutSettingsInt

WTSUserConfigReconnectSettingsInt

WTSUserConfigModemCallbackSettingsInt

WTSUserConfigShadowingSettingsInt, indicates if user's session my be monitored

WTSUserConfigfTerminalServerRemoteHomeDirInt,

#### Return Value
The type of the returned value is dependent on the config class requested


## [win32ts](win32ts.md#win32ts)\.WTSQueryUserToken

[PyHANDLE](PyHANDLE.md) = WTSQueryUserToken\(SessionId\)
Retrieves the access token for a session

#### Parameters

  - SessionId : int

    Terminal services session id

#### Comments

This function is intended only for use by trusted processes that have SE\_TCB\_PRIVILEGE enabled


## [win32ts](win32ts.md#win32ts)\.WTSRegisterSessionNotification

WTSRegisterSessionNotification\(Wnd, Flags\)
Registers a window to receive terminal service notifications

#### Parameters

  - Wnd : [PyHANDLE](PyHANDLE.md)

    Window handle to receive terminal service messages

  - Flags : int

    NOTIFY\_FOR\_THIS\_SESSION or NOTIFY\_FOR\_ALL\_SESSIONS


## [win32ts](win32ts.md#win32ts)\.WTSSendMessage

int = WTSSendMessage\(Server, SessionId

, Title

, Message

, Style

, Timeout

, Wait

\)
Sends a popup message to a terminal services session

#### Parameters

  - Server=WTS\_CURRENT\_SERVER\_HANDLE : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server, or WTS\_CURRENT\_SERVER\_HANDLE

  - SessionId : int

    Terminal services session id

  - Title : [PyUnicode](PyUnicode.md)

    Title of dialog

  - Message : [PyUnicode](PyUnicode.md)

    Message to be displayed

  - Style : int

    Usually MB\_OK

  - Timeout : int

    Seconds to wait before returning \(only used if Wait is True\)

  - Wait : boolean

    Specifies if function should wait for user input before returning

#### Return Value
Returns one of IDABORT,IDCANCEL,IDIGNORE,IDNO,IDOK,IDRETRY,IDYES,IDASYNC,IDTIMEOUT,


## [win32ts](win32ts.md#win32ts)\.WTSSetUserConfig

WTSSetUserConfig\(ServerName, UserName, ConfigClass\)
Changes user configuration

#### Parameters

  - ServerName : [PyUnicode](PyUnicode.md)

    Name ot terminal server

  - UserName : [PyUnicode](PyUnicode.md)

    Name of user

  - ConfigClass : int

    Type of information to be set, win32ts\.WTSUserConfig\*



## [win32ts](win32ts.md#win32ts)\.WTSShutdownSystem

WTSShutdownSystem\(Server, ShutdownFlag\)
Issues a shutdown request to a terminal server

#### Parameters

  - Server : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server

  - ShutdownFlag : int

    One of the win32ts\.WTS\_WSD\_\* values


## [win32ts](win32ts.md#win32ts)\.WTSTerminateProcess

WTSTerminateProcess\(Server, ProcessId, ExitCode\)
Kills a process on a terminal server

#### Parameters

  - Server : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server

  - ProcessId : int

    Id of a process as returned by [win32ts::WTSEnumerateProcesses](win32ts.md#win32tswtsenumerateprocesses)

  - ExitCode : int

    Exit code for the process


## [win32ts](win32ts.md#win32ts)\.WTSUnRegisterSessionNotification

WTSUnRegisterSessionNotification\(Wnd\)
Disables terminal service window messages

#### Parameters

  - Wnd : [PyHANDLE](PyHANDLE.md)

    Window previously registered to receive session notifications


## [win32ts](win32ts.md#win32ts)\.WTSWaitSystemEvent

int = WTSWaitSystemEvent\(Server, EventMask

\)
Waits for an event to occur

#### Parameters

  - Server=WTS\_CURRENT\_SERVER\_HANDLE : [PyHANDLE](PyHANDLE.md)

    Handle to a terminal server, or WTS\_CURRENT\_SERVER\_HANDLE

  - EventMask=WTS\_EVENT\_ALL : int

    Combination of WTS\_EVENT\_\* values

#### Return Value
Returns a bitmask of WTS\_EVENT\_\* flags indication which event\(s\) occurred