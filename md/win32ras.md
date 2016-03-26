
## [win32ras](#README.md#win32ras).CreatePhonebookEntry

 **CreatePhonebookEntry( *hWnd*  *, fileName* ** )
Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry

#### Parameters


     *hWnd* : int

    Handle to the parent window of the dialog box.

     *fileName=None* : string

    Specifies the filename of the phonebook entry.  Currently this is ignored.

#### Win32 API References


    Search for *RasCreatePhonebookEntry* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasCreatePhonebookEntry),[google](#README.md#http://www.google.com/search?q=RasCreatePhonebookEntry)or[google groups](#README.md#http://groups.google.com/groups?q=RasCreatePhonebookEntry).

## [win32ras](#README.md#win32ras).Dial

int, int = **Dial( *dialExtensions*  *, fileName*  *, RasDialParams*  *, callback* ** )
Establishes a RAS connection to a RAS server.

#### Parameters


     *dialExtensions* : **PyRASDIALEXTENSIONS** 

    An object providing the RASDIALEXTENSIONS information, or None

     *fileName* : string

    Specifies the filename of the phonebook entry, or None.  Ignored on Win95.

     *RasDialParams* :[RASDIALPARAMS](#README.md#RASDIALPARAMS)

    A tuple describing a RASDIALPARAMS structure.

     *callback* : method or hwnd

    The method to be called when RAS events occur, or None.  If not None, the function must have the signature of[win32ras::RasDialFunc1](#win32ras.md#win32rasRasDialFunc1)

#### Comments
Note - this handle must be closed using[win32ras::HangUp](#win32ras.md#win32rasHangUp), or 

else the RAS port will remain open, even after the program has terminated. 

Your operating system may need rebooting to clean up otherwise!

#### Win32 API References


    Search for *RasDial* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasDial),[google](#README.md#http://www.google.com/search?q=RasDial)or[google groups](#README.md#http://groups.google.com/groups?q=RasDial).

#### Return Value
The return value is (handle, retCode).
It is possible for a valid handle to be returned even on failure.
If the returned handle is = 0, then it can be assumed invalid.

## [win32ras](#README.md#win32ras).EditPhonebookEntry

 **EditPhonebookEntry( *hWnd*  *, fileName*  *, entryName* ** )
Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry

#### Parameters


     *hWnd* : int

    Handle to the parent window of the dialog box.

     *fileName* : string

    Specifies the filename of the phonebook entry, or None.  Currently this is ignored.

     *entryName=None* : string

    Specifies the name of the phonebook entry to edit

#### Win32 API References


    Search for *RasEditPhonebookEntry* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasEditPhonebookEntry),[google](#README.md#http://www.google.com/search?q=RasEditPhonebookEntry)or[google groups](#README.md#http://groups.google.com/groups?q=RasEditPhonebookEntry).

## [win32ras](#README.md#win32ras).EnumConnections

list = **EnumConnections(** )
Returns a list of tuples, one for each active connection.

#### Win32 API References


    Search for *RasEnumConnections* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasEnumConnections),[google](#README.md#http://www.google.com/search?q=RasEnumConnections)or[google groups](#README.md#http://groups.google.com/groups?q=RasEnumConnections).

#### Return Value
Each tuple is of format (handle, entryName, deviceType, deviceName)

## [win32ras](#README.md#win32ras).EnumEntries

 **EnumEntries( *reserved*  *, fileName* ** )
Returns a list of tuples, one for each phonebook entry.

#### Parameters


     *reserved=None* : string

    Reserved - must be None

     *fileName=None* : string

    The name of the phonebook file, or None.

## [win32ras](#README.md#win32ras).GetConnectStatus

(int, int, string, string) = **GetConnectStatus( *hrasconn* ** )
Returns a tuple with connection information.

#### Parameters


     *hrasconn* : int

    Handle to the RAS session.

#### Win32 API References


    Search for *RasGetConnectStatus* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus),[google](#README.md#http://www.google.com/search?q=RasGetConnectStatus)or[google groups](#README.md#http://groups.google.com/groups?q=RasGetConnectStatus).

    Search for *RasGetConnectStatus* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus),[google](#README.md#http://www.google.com/search?q=RasGetConnectStatus)or[google groups](#README.md#http://groups.google.com/groups?q=RasGetConnectStatus).

## [win32ras](#README.md#win32ras).GetEntryDialParams

(s,s,s,s,s,s),i = **GetEntryDialParams( *fileName*  *, entryName* ** )
Returns a tuple with the most recently set dial parameters for the specified entry.

#### Parameters


     *fileName* : string

    The filename of the phonebook, or None.

     *entryName* : string

    The name of the entry to retrieve the params for.

#### Win32 API References


    Search for *RasGetEntryDialParams* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetEntryDialParams),[google](#README.md#http://www.google.com/search?q=RasGetEntryDialParams)or[google groups](#README.md#http://groups.google.com/groups?q=RasGetEntryDialParams).

    Search for *RasGetConnectStatus* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus),[google](#README.md#http://www.google.com/search?q=RasGetConnectStatus)or[google groups](#README.md#http://groups.google.com/groups?q=RasGetConnectStatus).

#### Return Value
The return value is a tuple describing the params retrieved, plus a BOOL integer 

indicating if the password was also retrieved.

## [win32ras](#README.md#win32ras).GetErrorString

string = **GetErrorString( *error* ** )
Returns an error string for a RAS error code.

#### Parameters


     *error* : int

    The error value being queried.

#### Win32 API References


    Search for *RasGetErrorString* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetErrorString),[google](#README.md#http://www.google.com/search?q=RasGetErrorString)or[google groups](#README.md#http://groups.google.com/groups?q=RasGetErrorString).

## [win32ras](#README.md#win32ras).HangUp

 **HangUp( *hras* ** )
Terminates a remote access session.

#### Parameters


     *hras* : int

    The handle to the RAS connection to be terminated.

#### Win32 API References


    Search for *RasHangUp* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasHangUp),[google](#README.md#http://www.google.com/search?q=RasHangUp)or[google groups](#README.md#http://groups.google.com/groups?q=RasHangUp).

## [win32ras](#README.md#win32ras).IsHandleValid

 **IsHandleValid( *hras* ** )
Indicates if the given RAS handle is valid.

#### Parameters


     *hras* : int

    The handle to the RAS connection being checked.

## RASCS_AllDevicesConnected
 **const win32ras.RASCS_AllDevicesConnected;** 
Constant for RAS state.

## RASCS_AuthAck
 **const win32ras.RASCS_AuthAck;** 
Constant for RAS state.

## RASCS_AuthCallback
 **const win32ras.RASCS_AuthCallback;** 
Constant for RAS state.

## RASCS_AuthChangePassword
 **const win32ras.RASCS_AuthChangePassword;** 
Constant for RAS state.

## RASCS_AuthLinkSpeed
 **const win32ras.RASCS_AuthLinkSpeed;** 
Constant for RAS state.

## RASCS_AuthNotify
 **const win32ras.RASCS_AuthNotify;** 
Constant for RAS state.

## RASCS_AuthProject
 **const win32ras.RASCS_AuthProject;** 
Constant for RAS state.

## RASCS_AuthRetry
 **const win32ras.RASCS_AuthRetry;** 
Constant for RAS state.

## RASCS_Authenticate
 **const win32ras.RASCS_Authenticate;** 
Constant for RAS state.

## RASCS_Authenticated
 **const win32ras.RASCS_Authenticated;** 
Constant for RAS state.

## RASCS_CallbackComplete
 **const win32ras.RASCS_CallbackComplete;** 
Constant for RAS state.

## RASCS_CallbackSetByCaller
 **const win32ras.RASCS_CallbackSetByCaller;** 
Constant for RAS state.

## RASCS_ConnectDevice
 **const win32ras.RASCS_ConnectDevice;** 
Constant for RAS state.

## RASCS_Connected
 **const win32ras.RASCS_Connected;** 
Constant for RAS state.

## RASCS_DeviceConnected
 **const win32ras.RASCS_DeviceConnected;** 
Constant for RAS state.

## RASCS_Disconnected
 **const win32ras.RASCS_Disconnected;** 
Constant for RAS state.

## RASCS_Interactive
 **const win32ras.RASCS_Interactive;** 
Constant for RAS state.

## RASCS_LogonNetwork
 **const win32ras.RASCS_LogonNetwork;** 
Constant for RAS state.

## RASCS_OpenPort
 **const win32ras.RASCS_OpenPort;** 
Constant for RAS state.

## RASCS_PasswordExpired
 **const win32ras.RASCS_PasswordExpired;** 
Constant for RAS state.

## RASCS_PortOpened
 **const win32ras.RASCS_PortOpened;** 
Constant for RAS state.

## RASCS_PrepareForCallback
 **const win32ras.RASCS_PrepareForCallback;** 
Constant for RAS state.

## RASCS_Projected
 **const win32ras.RASCS_Projected;** 
Constant for RAS state.

## RASCS_ReAuthenticate
 **const win32ras.RASCS_ReAuthenticate;** 
Constant for RAS state.

## RASCS_RetryAuthentication
 **const win32ras.RASCS_RetryAuthentication;** 
Constant for RAS state.

## RASCS_StartAuthentication
 **const win32ras.RASCS_StartAuthentication;** 
Constant for RAS state.

## RASCS_WaitForCallback
 **const win32ras.RASCS_WaitForCallback;** 
Constant for RAS state.

## RASCS_WaitForModemReset
 **const win32ras.RASCS_WaitForModemReset;** 
Constant for RAS state.

## win32ras::RasDialFunc1 method
 **RasDialFunc1(**  **)** 
A placeholder for a RAS callback.
Defined in: O:/SRC/PYWIN32/WIN32/SRC/WIN32RASMODULE.CPP

#### Comments
Certain RAS function require a callback function to be passed. 

This description describes the signature of the function you pass 

to these functions.

#### Parameters


     *hrascon* : int

    The handle to the RAS session.

     *msg* : int

    A message code identifying the reason for the callback.

     *rascs* : int

    Connection state about to be entered.

     *error* : int

    The error state of the connection

     *extendedError* : int

    

## [win32ras](#README.md#win32ras).SetEntryDialParams

 **SetEntryDialParams( *fileName*  *, RasDialParams*  *, bSavePassword* ** )
Sets the dial parameters for the specified entry.

#### Parameters


     *fileName* : string

    The filename of the phonebook, or None.

     *RasDialParams* : (tuple)

    A tuple describing a RASDIALPARAMS structure.

     *bSavePassword* : int

    Indicates whether to remove password from entry's parameters.

#### Win32 API References


    Search for *RasSetEntryDialParams* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasSetEntryDialParams),[google](#README.md#http://www.google.com/search?q=RasSetEntryDialParams)or[google groups](#README.md#http://groups.google.com/groups?q=RasSetEntryDialParams).

    Search for *RasGetConnectStatus* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus),[google](#README.md#http://www.google.com/search?q=RasGetConnectStatus)or[google groups](#README.md#http://groups.google.com/groups?q=RasGetConnectStatus).