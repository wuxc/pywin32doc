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

## [win32ts](#win32ts).ProcessIdToSessionId

int = __ProcessIdToSessionId( *ProcessId* __ )
Finds the session under which a process is running

#### Parameters


  -  *ProcessId* : int

    Id of a process as returned by[win32ts::WTSEnumerateProcesses](win32ts.md#win32tswtsenumerateprocesses)

## [win32ts](#win32ts).WTSCloseServer

 __WTSCloseServer( *Server* __ )
Closes a terminal server handle

#### Parameters


  -  *Server* :[PyHANDLE](#pyhandle)

    Terminal Server handle

## [win32ts](#win32ts).WTSDisconnectSession

 __WTSDisconnectSession( *Server*  *, SessionId*  *, Wait* __ )
Disconnects a session without logging it off

#### Parameters


  -  *Server* :[PyHANDLE](#pyhandle)

    Handle to a terminal server

  -  *SessionId* : int

    Terminal services session id as returned by[win32ts::WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

  -  *Wait* : boolean

    Indicates whether operation should be performed asynchronously

## [win32ts](#win32ts).WTSEnumerateProcesses

([PyUnicode](#pyunicode),...) = __WTSEnumerateProcesses( *Server*  *, Version*  *, Reserved* __ )
Lists processes on a terminal server

#### Parameters


  -  *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#pyhandle)

    Handle to a terminal server

  -  *Version=1* : int

    Version of request, currently 1 is only valid value

  -  *Reserved=0* : int

    Reserved, use 0 if passed in

## [win32ts](#win32ts).WTSEnumerateServers

([PyUnicode](#pyunicode),...) = __WTSEnumerateServers( *DomainName*  *, Version*  *, Reserved* __ )
Lists terminal servers in a domain

#### Parameters


  -  *DomainName=None* :[PyUnicode](#pyunicode)

    Use None for current domain

  -  *Version=1* : int

    Version of request, currently 1 is only valid value

  -  *Reserved=0* : int

    Reserved, use 0 if passed in

## [win32ts](#win32ts).WTSEnumerateSessions

(dict,...) = __WTSEnumerateSessions( *Server*  *, Version*  *, Reserved* __ )
Lists sessions on a server

#### Parameters


  -  *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#pyhandle)

    Handle to a terminal server

  -  *Version=1* : int

    Version of request, currently 1 is only valid value

  -  *Reserved=0* : int

    Reserved, use 0 if passed in

#### Return Value
Returns a sequence of dictionaries representing WTS_SESSION_INFO structs, containing {SessionId:int, WinStationName:str, State:int}

## [win32ts](#win32ts).WTSGetActiveConsoleSessionId

int = __WTSGetActiveConsoleSessionId(__ )
Returns the id of the console session

#### Comments
Returns 0xffffffff if no active console session exists

## [win32ts](#win32ts).WTSLogoffSession

 __WTSLogoffSession( *Server*  *, SessionId*  *, Wait* __ )
Logs off a user logged in through Terminal Services

#### Parameters


  -  *Server* :[PyHANDLE](#pyhandle)

    Handle to a terminal server

  -  *SessionId* : int

    Terminal services session id as returned by[win32ts::WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

  -  *Wait* : boolean

    Indicates whether operation should be performed asynchronously

## [win32ts](#win32ts).WTSOpenServer

[PyHANDLE](#pyhandle)= __WTSOpenServer( *ServerName* __ )
Opens a handle to a terminal server

#### Parameters


  -  *ServerName* :[PyUnicode](#pyunicode)

    Name ot terminal server to be opened

## [win32ts](#win32ts).WTSQuerySessionInformation

 __WTSQuerySessionInformation( *Server*  *, SessionId*  *, WTSInfoClass* __ )
Returns information about a terminal services session

#### Parameters


  -  *Server* :[PyHANDLE](#pyhandle)

    Handle to a terminal server as returned by[win32ts::WTSOpenServer](win32ts.md#win32tswtsopenserver)

  -  *SessionId* : int

    Terminal services session id as returned by[win32ts::WTSEnumerateSessions](win32ts.md#win32tswtsenumeratesessions)

  -  *WTSInfoClass* : int

    Type of information requested, from WTS_INFO_CLASS enum


## [win32ts](#win32ts).WTSQueryUserConfig

object = __WTSQueryUserConfig( *ServerName*  *, UserName*  *, ConfigClass* __ )
Returns user configuration

#### Parameters


  -  *ServerName* :[PyUnicode](#pyunicode)

    Name ot terminal server

  -  *UserName* :[PyUnicode](#pyunicode)

    Name of user

  -  *ConfigClass* : int

    Type of information to be returned, win32ts.WTSUserConfig*

 __ConfigClass__  __Returned value__ WTSUserConfigInitialProgramUnicode string, program to be run when user logs onWTSUserConfigWorkingDirectoryUnicode string, working dir for initial programWTSUserConfigModemCallbackPhoneNumberUnicode stringWTSUserConfigTerminalServerProfilePathUnicode stringWTSUserConfigTerminalServerHomeDirUnicode stringWTSUserConfigTerminalServerHomeDirDriveUnicode stringWTSUserConfigfInheritInitialProgramIntWTSUserConfigfAllowLogonTerminalServerInt, 1 if user can log on thru Terminal ServiceWTSUserConfigTimeoutSettingsConnectionsInt, max connection time (ms)WTSUserConfigTimeoutSettingsDisconnectionsIntWTSUserConfigTimeoutSettingsIdleInt, max idle time (ms)WTSUserConfigfDeviceClientDrivesIntWTSUserConfigfDeviceClientPrintersIntWTSUserConfigfDeviceClientDefaultPrinterIntWTSUserConfigBrokenTimeoutSettingsIntWTSUserConfigReconnectSettingsIntWTSUserConfigModemCallbackSettingsIntWTSUserConfigShadowingSettingsInt, indicates if user's session my be monitoredWTSUserConfigfTerminalServerRemoteHomeDirInt,
#### Return Value
The type of the returned value is dependent on the config class requested

## [win32ts](#win32ts).WTSQueryUserToken

[PyHANDLE](#pyhandle)= __WTSQueryUserToken( *SessionId* __ )
Retrieves the access token for a session

#### Parameters


  -  *SessionId* : int

    Terminal services session id

#### Comments
This function is intended only for use by trusted processes that have SE_TCB_PRIVILEGE enabled

## [win32ts](#win32ts).WTSRegisterSessionNotification

 __WTSRegisterSessionNotification( *Wnd*  *, Flags* __ )
Registers a window to receive terminal service notifications

#### Parameters


  -  *Wnd* :[PyHANDLE](#pyhandle)

    Window handle to receive terminal service messages

  -  *Flags* : int

    NOTIFY_FOR_THIS_SESSION or NOTIFY_FOR_ALL_SESSIONS

## [win32ts](#win32ts).WTSSendMessage

int = __WTSSendMessage( *Server*  *, SessionId*  *, Title*  *, Message*  *, Style*  *, Timeout*  *, Wait* __ )
Sends a popup message to a terminal services session

#### Parameters


  -  *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#pyhandle)

    Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE

  -  *SessionId* : int

    Terminal services session id

  -  *Title* :[PyUnicode](#pyunicode)

    Title of dialog

  -  *Message* :[PyUnicode](#pyunicode)

    Message to be displayed

  -  *Style* : int

    Usually MB_OK

  -  *Timeout* : int

    Seconds to wait before returning (only used if Wait is True)

  -  *Wait* : boolean

    Specifies if function should wait for user input before returning

#### Return Value
Returns one of IDABORT,IDCANCEL,IDIGNORE,IDNO,IDOK,IDRETRY,IDYES,IDASYNC,IDTIMEOUT,

## [win32ts](#win32ts).WTSSetUserConfig

 __WTSSetUserConfig( *ServerName*  *, UserName*  *, ConfigClass* __ )
Changes user configuration

#### Parameters


  -  *ServerName* :[PyUnicode](#pyunicode)

    Name ot terminal server

  -  *UserName* :[PyUnicode](#pyunicode)

    Name of user

  -  *ConfigClass* : int

    Type of information to be set, win32ts.WTSUserConfig*


## [win32ts](#win32ts).WTSShutdownSystem

 __WTSShutdownSystem( *Server*  *, ShutdownFlag* __ )
Issues a shutdown request to a terminal server

#### Parameters


  -  *Server* :[PyHANDLE](#pyhandle)

    Handle to a terminal server

  -  *ShutdownFlag* : int

    One of the win32ts.WTS_WSD_* values

## [win32ts](#win32ts).WTSTerminateProcess

 __WTSTerminateProcess( *Server*  *, ProcessId*  *, ExitCode* __ )
Kills a process on a terminal server

#### Parameters


  -  *Server* :[PyHANDLE](#pyhandle)

    Handle to a terminal server

  -  *ProcessId* : int

    Id of a process as returned by[win32ts::WTSEnumerateProcesses](win32ts.md#win32tswtsenumerateprocesses)

  -  *ExitCode* : int

    Exit code for the process

## [win32ts](#win32ts).WTSUnRegisterSessionNotification

 __WTSUnRegisterSessionNotification( *Wnd* __ )
Disables terminal service window messages

#### Parameters


  -  *Wnd* :[PyHANDLE](#pyhandle)

    Window previously registered to receive session notifications

## [win32ts](#win32ts).WTSWaitSystemEvent

int = __WTSWaitSystemEvent( *Server*  *, EventMask* __ )
Waits for an event to occur

#### Parameters


  -  *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#pyhandle)

    Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE

  -  *EventMask=WTS_EVENT_ALL* : int

    Combination of WTS_EVENT_* values

#### Return Value
Returns a bitmask of WTS_EVENT_* flags indication which event(s) occurred