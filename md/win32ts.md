
## [win32ts](#README.md#win32ts).ProcessIdToSessionId

int = **ProcessIdToSessionId( *ProcessId* ** )
Finds the session under which a process is running

#### Parameters


     *ProcessId* : int

    Id of a process as returned by[win32ts::WTSEnumerateProcesses](#win32ts.md#win32tsWTSEnumerateProcesses)

## [win32ts](#README.md#win32ts).WTSCloseServer

 **WTSCloseServer( *Server* ** )
Closes a terminal server handle

#### Parameters


     *Server* :[PyHANDLE](#README.md#PyHANDLE)

    Terminal Server handle

## [win32ts](#README.md#win32ts).WTSDisconnectSession

 **WTSDisconnectSession( *Server*  *, SessionId*  *, Wait* ** )
Disconnects a session without logging it off

#### Parameters


     *Server* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server

     *SessionId* : int

    Terminal services session id as returned by[win32ts::WTSEnumerateSessions](#win32ts.md#win32tsWTSEnumerateSessions)

     *Wait* : boolean

    Indicates whether operation should be performed asynchronously

## [win32ts](#README.md#win32ts).WTSEnumerateProcesses

([PyUnicode](#README.md#PyUnicode),...) = **WTSEnumerateProcesses( *Server*  *, Version*  *, Reserved* ** )
Lists processes on a terminal server

#### Parameters


     *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server

     *Version=1* : int

    Version of request, currently 1 is only valid value

     *Reserved=0* : int

    Reserved, use 0 if passed in

## [win32ts](#README.md#win32ts).WTSEnumerateServers

([PyUnicode](#README.md#PyUnicode),...) = **WTSEnumerateServers( *DomainName*  *, Version*  *, Reserved* ** )
Lists terminal servers in a domain

#### Parameters


     *DomainName=None* :[PyUnicode](#README.md#PyUnicode)

    Use None for current domain

     *Version=1* : int

    Version of request, currently 1 is only valid value

     *Reserved=0* : int

    Reserved, use 0 if passed in

## [win32ts](#README.md#win32ts).WTSEnumerateSessions

(dict,...) = **WTSEnumerateSessions( *Server*  *, Version*  *, Reserved* ** )
Lists sessions on a server

#### Parameters


     *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server

     *Version=1* : int

    Version of request, currently 1 is only valid value

     *Reserved=0* : int

    Reserved, use 0 if passed in

#### Return Value
Returns a sequence of dictionaries representing WTS_SESSION_INFO structs, containing {SessionId:int, WinStationName:str, State:int}

## [win32ts](#README.md#win32ts).WTSGetActiveConsoleSessionId

int = **WTSGetActiveConsoleSessionId(** )
Returns the id of the console session

#### Comments
Returns 0xffffffff if no active console session exists

## [win32ts](#README.md#win32ts).WTSLogoffSession

 **WTSLogoffSession( *Server*  *, SessionId*  *, Wait* ** )
Logs off a user logged in through Terminal Services

#### Parameters


     *Server* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server

     *SessionId* : int

    Terminal services session id as returned by[win32ts::WTSEnumerateSessions](#win32ts.md#win32tsWTSEnumerateSessions)

     *Wait* : boolean

    Indicates whether operation should be performed asynchronously

## [win32ts](#README.md#win32ts).WTSOpenServer

[PyHANDLE](#README.md#PyHANDLE)= **WTSOpenServer( *ServerName* ** )
Opens a handle to a terminal server

#### Parameters


     *ServerName* :[PyUnicode](#README.md#PyUnicode)

    Name ot terminal server to be opened

## [win32ts](#README.md#win32ts).WTSQuerySessionInformation

 **WTSQuerySessionInformation( *Server*  *, SessionId*  *, WTSInfoClass* ** )
Returns information about a terminal services session

#### Parameters


     *Server* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server as returned by[win32ts::WTSOpenServer](#win32ts.md#win32tsWTSOpenServer)

     *SessionId* : int

    Terminal services session id as returned by[win32ts::WTSEnumerateSessions](#win32ts.md#win32tsWTSEnumerateSessions)

     *WTSInfoClass* : int

    Type of information requested, from WTS_INFO_CLASS enum


## [win32ts](#README.md#win32ts).WTSQueryUserConfig

object = **WTSQueryUserConfig( *ServerName*  *, UserName*  *, ConfigClass* ** )
Returns user configuration

#### Parameters


     *ServerName* :[PyUnicode](#README.md#PyUnicode)

    Name ot terminal server

     *UserName* :[PyUnicode](#README.md#PyUnicode)

    Name of user

     *ConfigClass* : int

    Type of information to be returned, win32ts.WTSUserConfig*

 **ConfigClass**  **Returned value** WTSUserConfigInitialProgramUnicode string, program to be run when user logs onWTSUserConfigWorkingDirectoryUnicode string, working dir for initial programWTSUserConfigModemCallbackPhoneNumberUnicode stringWTSUserConfigTerminalServerProfilePathUnicode stringWTSUserConfigTerminalServerHomeDirUnicode stringWTSUserConfigTerminalServerHomeDirDriveUnicode stringWTSUserConfigfInheritInitialProgramIntWTSUserConfigfAllowLogonTerminalServerInt, 1 if user can log on thru Terminal ServiceWTSUserConfigTimeoutSettingsConnectionsInt, max connection time (ms)WTSUserConfigTimeoutSettingsDisconnectionsIntWTSUserConfigTimeoutSettingsIdleInt, max idle time (ms)WTSUserConfigfDeviceClientDrivesIntWTSUserConfigfDeviceClientPrintersIntWTSUserConfigfDeviceClientDefaultPrinterIntWTSUserConfigBrokenTimeoutSettingsIntWTSUserConfigReconnectSettingsIntWTSUserConfigModemCallbackSettingsIntWTSUserConfigShadowingSettingsInt, indicates if user's session my be monitoredWTSUserConfigfTerminalServerRemoteHomeDirInt,
#### Return Value
The type of the returned value is dependent on the config class requested

## [win32ts](#README.md#win32ts).WTSQueryUserToken

[PyHANDLE](#README.md#PyHANDLE)= **WTSQueryUserToken( *SessionId* ** )
Retrieves the access token for a session

#### Parameters


     *SessionId* : int

    Terminal services session id

#### Comments
This function is intended only for use by trusted processes that have SE_TCB_PRIVILEGE enabled

## [win32ts](#README.md#win32ts).WTSRegisterSessionNotification

 **WTSRegisterSessionNotification( *Wnd*  *, Flags* ** )
Registers a window to receive terminal service notifications

#### Parameters


     *Wnd* :[PyHANDLE](#README.md#PyHANDLE)

    Window handle to receive terminal service messages

     *Flags* : int

    NOTIFY_FOR_THIS_SESSION or NOTIFY_FOR_ALL_SESSIONS

## [win32ts](#README.md#win32ts).WTSSendMessage

int = **WTSSendMessage( *Server*  *, SessionId*  *, Title*  *, Message*  *, Style*  *, Timeout*  *, Wait* ** )
Sends a popup message to a terminal services session

#### Parameters


     *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE

     *SessionId* : int

    Terminal services session id

     *Title* :[PyUnicode](#README.md#PyUnicode)

    Title of dialog

     *Message* :[PyUnicode](#README.md#PyUnicode)

    Message to be displayed

     *Style* : int

    Usually MB_OK

     *Timeout* : int

    Seconds to wait before returning (only used if Wait is True)

     *Wait* : boolean

    Specifies if function should wait for user input before returning

#### Return Value
Returns one of IDABORT,IDCANCEL,IDIGNORE,IDNO,IDOK,IDRETRY,IDYES,IDASYNC,IDTIMEOUT,

## [win32ts](#README.md#win32ts).WTSSetUserConfig

 **WTSSetUserConfig( *ServerName*  *, UserName*  *, ConfigClass* ** )
Changes user configuration

#### Parameters


     *ServerName* :[PyUnicode](#README.md#PyUnicode)

    Name ot terminal server

     *UserName* :[PyUnicode](#README.md#PyUnicode)

    Name of user

     *ConfigClass* : int

    Type of information to be set, win32ts.WTSUserConfig*


## [win32ts](#README.md#win32ts).WTSShutdownSystem

 **WTSShutdownSystem( *Server*  *, ShutdownFlag* ** )
Issues a shutdown request to a terminal server

#### Parameters


     *Server* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server

     *ShutdownFlag* : int

    One of the win32ts.WTS_WSD_* values

## [win32ts](#README.md#win32ts).WTSTerminateProcess

 **WTSTerminateProcess( *Server*  *, ProcessId*  *, ExitCode* ** )
Kills a process on a terminal server

#### Parameters


     *Server* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server

     *ProcessId* : int

    Id of a process as returned by[win32ts::WTSEnumerateProcesses](#win32ts.md#win32tsWTSEnumerateProcesses)

     *ExitCode* : int

    Exit code for the process

## [win32ts](#README.md#win32ts).WTSUnRegisterSessionNotification

 **WTSUnRegisterSessionNotification( *Wnd* ** )
Disables terminal service window messages

#### Parameters


     *Wnd* :[PyHANDLE](#README.md#PyHANDLE)

    Window previously registered to receive session notifications

## [win32ts](#README.md#win32ts).WTSWaitSystemEvent

int = **WTSWaitSystemEvent( *Server*  *, EventMask* ** )
Waits for an event to occur

#### Parameters


     *Server=WTS_CURRENT_SERVER_HANDLE* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE

     *EventMask=WTS_EVENT_ALL* : int

    Combination of WTS_EVENT_* values

#### Return Value
Returns a bitmask of WTS_EVENT_* flags indication which event(s) occurred