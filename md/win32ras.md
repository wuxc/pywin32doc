# win32ras

## Module win32ras

A module encapsulating the Windows Remote Access Service (RAS) API.

#### Methods


  - [CreatePhonebookEntry](win32ras.md#win32rascreatephonebookentry)

    Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry.&nbsp;

  - [Dial](win32ras.md#win32rasdial)

    Establishes a RAS connection to a RAS server.&nbsp;

  - [EditPhonebookEntry](win32ras.md#win32raseditphonebookentry)

    Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry&nbsp;

  - [EnumConnections](win32ras.md#win32rasenumconnections)

    Returns a list of tuples, one for each active connection.&nbsp;

  - [EnumEntries](win32ras.md#win32rasenumentries)

    Returns a list of tuples, one for each phonebook entry.&nbsp;

  - [GetConnectStatus](win32ras.md#win32rasgetconnectstatus)

    Returns a tuple with connection information.&nbsp;

  - [GetEntryDialParams](win32ras.md#win32rasgetentrydialparams)

    Returns a tuple with the most recently set dial parameters for the specified entry.&nbsp;

  - [GetErrorString](win32ras.md#win32rasgeterrorstring)

    Returns an error string for a RAS error code.&nbsp;

  - [HangUp](win32ras.md#win32rashangup)

    Terminates a remote access session.&nbsp;

  - [IsHandleValid](win32ras.md#win32rasishandlevalid)

    Indicates if the given RAS handle is valid.&nbsp;

  - [SetEntryDialParams](win32ras.md#win32rassetentrydialparams)

    Sets the dial parameters for the specified entry.&nbsp;

  - [RASDIALEXTENSIONS](win32ras.md#win32rasrasdialextensions)

    Creates a new[RASDIALEXTENSIONS](#rasdialextensions)object&nbsp;

## [win32ras](#win32ras).CreatePhonebookEntry

 __CreatePhonebookEntry( *hWnd*  *, fileName* __ )
Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry

#### Parameters


  -  *hWnd* : int

    Handle to the parent window of the dialog box.

  -  *fileName=None* : string

    Specifies the filename of the phonebook entry.  Currently this is ignored.

#### Win32 API References


  - Search for *RasCreatePhonebookEntry* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rascreatephonebookentry),[google](#http://www.google.com/search?q=rascreatephonebookentry)or[google groups](#http://groups.google.com/groups?q=rascreatephonebookentry).

## [win32ras](#win32ras).Dial

int, int = __Dial( *dialExtensions*  *, fileName*  *, RasDialParams*  *, callback* __ )
Establishes a RAS connection to a RAS server.

#### Parameters


  -  *dialExtensions* : __PyRASDIALEXTENSIONS__ 

    An object providing the RASDIALEXTENSIONS information, or None

  -  *fileName* : string

    Specifies the filename of the phonebook entry, or None.  Ignored on Win95.

  -  *RasDialParams* :[RASDIALPARAMS](#rasdialparams)

    A tuple describing a RASDIALPARAMS structure.

  -  *callback* : method or hwnd

    The method to be called when RAS events occur, or None.  If not None, the function must have the signature of[win32ras::RasDialFunc1](win32ras.md#win32rasrasdialfunc1)

#### Comments
Note - this handle must be closed using[win32ras::HangUp](win32ras.md#win32rashangup), or 

else the RAS port will remain open, even after the program has terminated. 

Your operating system may need rebooting to clean up otherwise!

#### Win32 API References


  - Search for *RasDial* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasdial),[google](#http://www.google.com/search?q=rasdial)or[google groups](#http://groups.google.com/groups?q=rasdial).

#### Return Value
The return value is (handle, retCode).
It is possible for a valid handle to be returned even on failure.
If the returned handle is = 0, then it can be assumed invalid.

## [win32ras](#win32ras).EditPhonebookEntry

 __EditPhonebookEntry( *hWnd*  *, fileName*  *, entryName* __ )
Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry

#### Parameters


  -  *hWnd* : int

    Handle to the parent window of the dialog box.

  -  *fileName* : string

    Specifies the filename of the phonebook entry, or None.  Currently this is ignored.

  -  *entryName=None* : string

    Specifies the name of the phonebook entry to edit

#### Win32 API References


  - Search for *RasEditPhonebookEntry* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=raseditphonebookentry),[google](#http://www.google.com/search?q=raseditphonebookentry)or[google groups](#http://groups.google.com/groups?q=raseditphonebookentry).

## [win32ras](#win32ras).EnumConnections

list = __EnumConnections(__ )
Returns a list of tuples, one for each active connection.

#### Win32 API References


  - Search for *RasEnumConnections* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasenumconnections),[google](#http://www.google.com/search?q=rasenumconnections)or[google groups](#http://groups.google.com/groups?q=rasenumconnections).

#### Return Value
Each tuple is of format (handle, entryName, deviceType, deviceName)

## [win32ras](#win32ras).EnumEntries

 __EnumEntries( *reserved*  *, fileName* __ )
Returns a list of tuples, one for each phonebook entry.

#### Parameters


  -  *reserved=None* : string

    Reserved - must be None

  -  *fileName=None* : string

    The name of the phonebook file, or None.

## [win32ras](#win32ras).GetConnectStatus

(int, int, string, string) = __GetConnectStatus( *hrasconn* __ )
Returns a tuple with connection information.

#### Parameters


  -  *hrasconn* : int

    Handle to the RAS session.

#### Win32 API References


  - Search for *RasGetConnectStatus* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgetconnectstatus),[google](#http://www.google.com/search?q=rasgetconnectstatus)or[google groups](#http://groups.google.com/groups?q=rasgetconnectstatus).

  - Search for *RasGetConnectStatus* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgetconnectstatus),[google](#http://www.google.com/search?q=rasgetconnectstatus)or[google groups](#http://groups.google.com/groups?q=rasgetconnectstatus).

## [win32ras](#win32ras).GetEntryDialParams

(s,s,s,s,s,s),i = __GetEntryDialParams( *fileName*  *, entryName* __ )
Returns a tuple with the most recently set dial parameters for the specified entry.

#### Parameters


  -  *fileName* : string

    The filename of the phonebook, or None.

  -  *entryName* : string

    The name of the entry to retrieve the params for.

#### Win32 API References


  - Search for *RasGetEntryDialParams* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgetentrydialparams),[google](#http://www.google.com/search?q=rasgetentrydialparams)or[google groups](#http://groups.google.com/groups?q=rasgetentrydialparams).

  - Search for *RasGetConnectStatus* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgetconnectstatus),[google](#http://www.google.com/search?q=rasgetconnectstatus)or[google groups](#http://groups.google.com/groups?q=rasgetconnectstatus).

#### Return Value
The return value is a tuple describing the params retrieved, plus a BOOL integer 

indicating if the password was also retrieved.

## [win32ras](#win32ras).GetErrorString

string = __GetErrorString( *error* __ )
Returns an error string for a RAS error code.

#### Parameters


  -  *error* : int

    The error value being queried.

#### Win32 API References


  - Search for *RasGetErrorString* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgeterrorstring),[google](#http://www.google.com/search?q=rasgeterrorstring)or[google groups](#http://groups.google.com/groups?q=rasgeterrorstring).

## [win32ras](#win32ras).HangUp

 __HangUp( *hras* __ )
Terminates a remote access session.

#### Parameters


  -  *hras* : int

    The handle to the RAS connection to be terminated.

#### Win32 API References


  - Search for *RasHangUp* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rashangup),[google](#http://www.google.com/search?q=rashangup)or[google groups](#http://groups.google.com/groups?q=rashangup).

## [win32ras](#win32ras).IsHandleValid

 __IsHandleValid( *hras* __ )
Indicates if the given RAS handle is valid.

#### Parameters


  -  *hras* : int

    The handle to the RAS connection being checked.

## RASCS_AllDevicesConnected
 __const win32ras.RASCS_AllDevicesConnected;__ 
Constant for RAS state.

## RASCS_AuthAck
 __const win32ras.RASCS_AuthAck;__ 
Constant for RAS state.

## RASCS_AuthCallback
 __const win32ras.RASCS_AuthCallback;__ 
Constant for RAS state.

## RASCS_AuthChangePassword
 __const win32ras.RASCS_AuthChangePassword;__ 
Constant for RAS state.

## RASCS_AuthLinkSpeed
 __const win32ras.RASCS_AuthLinkSpeed;__ 
Constant for RAS state.

## RASCS_AuthNotify
 __const win32ras.RASCS_AuthNotify;__ 
Constant for RAS state.

## RASCS_AuthProject
 __const win32ras.RASCS_AuthProject;__ 
Constant for RAS state.

## RASCS_AuthRetry
 __const win32ras.RASCS_AuthRetry;__ 
Constant for RAS state.

## RASCS_Authenticate
 __const win32ras.RASCS_Authenticate;__ 
Constant for RAS state.

## RASCS_Authenticated
 __const win32ras.RASCS_Authenticated;__ 
Constant for RAS state.

## RASCS_CallbackComplete
 __const win32ras.RASCS_CallbackComplete;__ 
Constant for RAS state.

## RASCS_CallbackSetByCaller
 __const win32ras.RASCS_CallbackSetByCaller;__ 
Constant for RAS state.

## RASCS_ConnectDevice
 __const win32ras.RASCS_ConnectDevice;__ 
Constant for RAS state.

## RASCS_Connected
 __const win32ras.RASCS_Connected;__ 
Constant for RAS state.

## RASCS_DeviceConnected
 __const win32ras.RASCS_DeviceConnected;__ 
Constant for RAS state.

## RASCS_Disconnected
 __const win32ras.RASCS_Disconnected;__ 
Constant for RAS state.

## RASCS_Interactive
 __const win32ras.RASCS_Interactive;__ 
Constant for RAS state.

## RASCS_LogonNetwork
 __const win32ras.RASCS_LogonNetwork;__ 
Constant for RAS state.

## RASCS_OpenPort
 __const win32ras.RASCS_OpenPort;__ 
Constant for RAS state.

## RASCS_PasswordExpired
 __const win32ras.RASCS_PasswordExpired;__ 
Constant for RAS state.

## RASCS_PortOpened
 __const win32ras.RASCS_PortOpened;__ 
Constant for RAS state.

## RASCS_PrepareForCallback
 __const win32ras.RASCS_PrepareForCallback;__ 
Constant for RAS state.

## RASCS_Projected
 __const win32ras.RASCS_Projected;__ 
Constant for RAS state.

## RASCS_ReAuthenticate
 __const win32ras.RASCS_ReAuthenticate;__ 
Constant for RAS state.

## RASCS_RetryAuthentication
 __const win32ras.RASCS_RetryAuthentication;__ 
Constant for RAS state.

## RASCS_StartAuthentication
 __const win32ras.RASCS_StartAuthentication;__ 
Constant for RAS state.

## RASCS_WaitForCallback
 __const win32ras.RASCS_WaitForCallback;__ 
Constant for RAS state.

## RASCS_WaitForModemReset
 __const win32ras.RASCS_WaitForModemReset;__ 
Constant for RAS state.

## win32ras::RasDialFunc1 method
 __RasDialFunc1(__  __)__ 
A placeholder for a RAS callback.
Defined in: O:/SRC/PYWIN32/WIN32/SRC/WIN32RASMODULE.CPP

#### Comments
Certain RAS function require a callback function to be passed. 

This description describes the signature of the function you pass 

to these functions.

#### Parameters


  -  *hrascon* : int

    The handle to the RAS session.

  -  *msg* : int

    A message code identifying the reason for the callback.

  -  *rascs* : int

    Connection state about to be entered.

  -  *error* : int

    The error state of the connection

  -  *extendedError* : int

    

## [win32ras](#win32ras).SetEntryDialParams

 __SetEntryDialParams( *fileName*  *, RasDialParams*  *, bSavePassword* __ )
Sets the dial parameters for the specified entry.

#### Parameters


  -  *fileName* : string

    The filename of the phonebook, or None.

  -  *RasDialParams* : (tuple)

    A tuple describing a RASDIALPARAMS structure.

  -  *bSavePassword* : int

    Indicates whether to remove password from entry's parameters.

#### Win32 API References


  - Search for *RasSetEntryDialParams* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rassetentrydialparams),[google](#http://www.google.com/search?q=rassetentrydialparams)or[google groups](#http://groups.google.com/groups?q=rassetentrydialparams).

  - Search for *RasGetConnectStatus* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgetconnectstatus),[google](#http://www.google.com/search?q=rasgetconnectstatus)or[google groups](#http://groups.google.com/groups?q=rasgetconnectstatus).