# win32ras


## Module win32ras

A module encapsulating the Windows Remote Access Service \(RAS\) API\.

#### Methods

  - [CreatePhonebookEntry](win32ras.md#win32rascreatephonebookentry)

    Creates a new phonebook entry\.  The function displays a dialog box into which the user can enter information about the entry\.&nbsp;

  - [Dial](win32ras.md#win32rasdial)

    Establishes a RAS connection to a RAS server\.&nbsp;

  - [EditPhonebookEntry](win32ras.md#win32raseditphonebookentry)

    Creates a new phonebook entry\.  The function displays a dialog box into which the user can enter information about the entry&nbsp;

  - [EnumConnections](win32ras.md#win32rasenumconnections)

    Returns a list of tuples, one for each active connection\.&nbsp;

  - [EnumEntries](win32ras.md#win32rasenumentries)

    Returns a list of tuples, one for each phonebook entry\.&nbsp;

  - [GetConnectStatus](win32ras.md#win32rasgetconnectstatus)

    Returns a tuple with connection information\.&nbsp;

  - [GetEntryDialParams](win32ras.md#win32rasgetentrydialparams)

    Returns a tuple with the most recently set dial parameters for the specified entry\.&nbsp;

  - [GetErrorString](win32ras.md#win32rasgeterrorstring)

    Returns an error string for a RAS error code\.&nbsp;

  - [HangUp](win32ras.md#win32rashangup)

    Terminates a remote access session\.&nbsp;

  - [IsHandleValid](win32ras.md#win32rasishandlevalid)

    Indicates if the given RAS handle is valid\.&nbsp;

  - [SetEntryDialParams](win32ras.md#win32rassetentrydialparams)

    Sets the dial parameters for the specified entry\.&nbsp;

  - [RASDIALEXTENSIONS](win32ras.md#win32rasrasdialextensions)

    Creates a new [RASDIALEXTENSIONS](RASDIALEXTENSIONS.md) object&nbsp;


## [win32ras](win32ras.md#win32ras)\.CreatePhonebookEntry

CreatePhonebookEntry\(hWnd, fileName\)
Creates a new phonebook entry\.  The function displays a dialog box into which the user can enter information about the entry

#### Parameters

  - hWnd : int

    Handle to the parent window of the dialog box\.

  - fileName=None : string

    Specifies the filename of the phonebook entry\.  Currently this is ignored\.

#### Win32 API References

  - Search for RasCreatePhonebookEntry at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasCreatePhonebookEntry.md), [google](http://www.google.com/search?q=RasCreatePhonebookEntry.md) or [google groups](http://groups.google.com/groups?q=RasCreatePhonebookEntry.md)\.


## [win32ras](win32ras.md#win32ras)\.Dial

int, int = Dial\(dialExtensions, fileName

, RasDialParams

, callback

\)
Establishes a RAS connection to a RAS server\.

#### Parameters

  - dialExtensions : PyRASDIALEXTENSIONS

    An object providing the RASDIALEXTENSIONS information, or None

  - fileName : string

    Specifies the filename of the phonebook entry, or None\.  Ignored on Win95\.

  - RasDialParams : [RASDIALPARAMS](RASDIALPARAMS.md)

    A tuple describing a RASDIALPARAMS structure\.

  - callback : method or hwnd

    The method to be called when RAS events occur, or None\.  If not None, the function must have the signature of [win32ras::RasDialFunc1](win32ras.md#win32rasrasdialfunc1)

#### Comments

Note - this handle must be closed using [win32ras::HangUp](win32ras.md#win32rashangup), or 

else the RAS port will remain open, even after the program has terminated\. 

Your operating system may need rebooting to clean up otherwise\!

#### Win32 API References

  - Search for RasDial at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasDial.md), [google](http://www.google.com/search?q=RasDial.md) or [google groups](http://groups.google.com/groups?q=RasDial.md)\.

#### Return Value
The return value is \(handle, retCode\)\. 

It is possible for a valid handle to be returned even on failure\. 

If the returned handle is = 0, then it can be assumed invalid\.


## [win32ras](win32ras.md#win32ras)\.EditPhonebookEntry

EditPhonebookEntry\(hWnd, fileName, entryName\)
Creates a new phonebook entry\.  The function displays a dialog box into which the user can enter information about the entry

#### Parameters

  - hWnd : int

    Handle to the parent window of the dialog box\.

  - fileName : string

    Specifies the filename of the phonebook entry, or None\.  Currently this is ignored\.

  - entryName=None : string

    Specifies the name of the phonebook entry to edit

#### Win32 API References

  - Search for RasEditPhonebookEntry at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasEditPhonebookEntry.md), [google](http://www.google.com/search?q=RasEditPhonebookEntry.md) or [google groups](http://groups.google.com/groups?q=RasEditPhonebookEntry.md)\.


## [win32ras](win32ras.md#win32ras)\.EnumConnections

list = EnumConnections\(\)
Returns a list of tuples, one for each active connection\.

#### Win32 API References

  - Search for RasEnumConnections at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasEnumConnections.md), [google](http://www.google.com/search?q=RasEnumConnections.md) or [google groups](http://groups.google.com/groups?q=RasEnumConnections.md)\.

#### Return Value
Each tuple is of format \(handle, entryName, deviceType, deviceName\)


## [win32ras](win32ras.md#win32ras)\.EnumEntries

EnumEntries\(reserved, fileName\)
Returns a list of tuples, one for each phonebook entry\.

#### Parameters

  - reserved=None : string

    Reserved - must be None

  - fileName=None : string

    The name of the phonebook file, or None\.


## [win32ras](win32ras.md#win32ras)\.GetConnectStatus

\(int, int, string, string\) = GetConnectStatus\(hrasconn\)
Returns a tuple with connection information\.

#### Parameters

  - hrasconn : int

    Handle to the RAS session\.

#### Win32 API References

  - Search for RasGetConnectStatus at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus.md), [google](http://www.google.com/search?q=RasGetConnectStatus.md) or [google groups](http://groups.google.com/groups?q=RasGetConnectStatus.md)\.

  - Search for RasGetConnectStatus at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus.md), [google](http://www.google.com/search?q=RasGetConnectStatus.md) or [google groups](http://groups.google.com/groups?q=RasGetConnectStatus.md)\.


## [win32ras](win32ras.md#win32ras)\.GetEntryDialParams

\(s,s,s,s,s,s\),i = GetEntryDialParams\(fileName, entryName

\)
Returns a tuple with the most recently set dial parameters for the specified entry\.

#### Parameters

  - fileName : string

    The filename of the phonebook, or None\.

  - entryName : string

    The name of the entry to retrieve the params for\.

#### Win32 API References

  - Search for RasGetEntryDialParams at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetEntryDialParams.md), [google](http://www.google.com/search?q=RasGetEntryDialParams.md) or [google groups](http://groups.google.com/groups?q=RasGetEntryDialParams.md)\.

  - Search for RasGetConnectStatus at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus.md), [google](http://www.google.com/search?q=RasGetConnectStatus.md) or [google groups](http://groups.google.com/groups?q=RasGetConnectStatus.md)\.

#### Return Value
The return value is a tuple describing the params retrieved, plus a BOOL integer 

indicating if the password was also retrieved\.


## [win32ras](win32ras.md#win32ras)\.GetErrorString

string = GetErrorString\(error\)
Returns an error string for a RAS error code\.

#### Parameters

  - error : int

    The error value being queried\.

#### Win32 API References

  - Search for RasGetErrorString at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetErrorString.md), [google](http://www.google.com/search?q=RasGetErrorString.md) or [google groups](http://groups.google.com/groups?q=RasGetErrorString.md)\.


## [win32ras](win32ras.md#win32ras)\.HangUp

HangUp\(hras\)
Terminates a remote access session\.

#### Parameters

  - hras : int

    The handle to the RAS connection to be terminated\.

#### Win32 API References

  - Search for RasHangUp at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasHangUp.md), [google](http://www.google.com/search?q=RasHangUp.md) or [google groups](http://groups.google.com/groups?q=RasHangUp.md)\.


## [win32ras](win32ras.md#win32ras)\.IsHandleValid

IsHandleValid\(hras\)
Indicates if the given RAS handle is valid\.

#### Parameters

  - hras : int

    The handle to the RAS connection being checked\.


## RASCS\_AllDevicesConnected

const win32ras\.RASCS\_AllDevicesConnected;

Constant for RAS state\.


## RASCS\_AuthAck

const win32ras\.RASCS\_AuthAck;

Constant for RAS state\.


## RASCS\_AuthCallback

const win32ras\.RASCS\_AuthCallback;

Constant for RAS state\.


## RASCS\_AuthChangePassword

const win32ras\.RASCS\_AuthChangePassword;

Constant for RAS state\.


## RASCS\_AuthLinkSpeed

const win32ras\.RASCS\_AuthLinkSpeed;

Constant for RAS state\.


## RASCS\_AuthNotify

const win32ras\.RASCS\_AuthNotify;

Constant for RAS state\.


## RASCS\_AuthProject

const win32ras\.RASCS\_AuthProject;

Constant for RAS state\.


## RASCS\_AuthRetry

const win32ras\.RASCS\_AuthRetry;

Constant for RAS state\.


## RASCS\_Authenticate

const win32ras\.RASCS\_Authenticate;

Constant for RAS state\.


## RASCS\_Authenticated

const win32ras\.RASCS\_Authenticated;

Constant for RAS state\.


## RASCS\_CallbackComplete

const win32ras\.RASCS\_CallbackComplete;

Constant for RAS state\.


## RASCS\_CallbackSetByCaller

const win32ras\.RASCS\_CallbackSetByCaller;

Constant for RAS state\.


## RASCS\_ConnectDevice

const win32ras\.RASCS\_ConnectDevice;

Constant for RAS state\.


## RASCS\_Connected

const win32ras\.RASCS\_Connected;

Constant for RAS state\.


## RASCS\_DeviceConnected

const win32ras\.RASCS\_DeviceConnected;

Constant for RAS state\.


## RASCS\_Disconnected

const win32ras\.RASCS\_Disconnected;

Constant for RAS state\.


## RASCS\_Interactive

const win32ras\.RASCS\_Interactive;

Constant for RAS state\.


## RASCS\_LogonNetwork

const win32ras\.RASCS\_LogonNetwork;

Constant for RAS state\.


## RASCS\_OpenPort

const win32ras\.RASCS\_OpenPort;

Constant for RAS state\.


## RASCS\_PasswordExpired

const win32ras\.RASCS\_PasswordExpired;

Constant for RAS state\.


## RASCS\_PortOpened

const win32ras\.RASCS\_PortOpened;

Constant for RAS state\.


## RASCS\_PrepareForCallback

const win32ras\.RASCS\_PrepareForCallback;

Constant for RAS state\.


## RASCS\_Projected

const win32ras\.RASCS\_Projected;

Constant for RAS state\.


## RASCS\_ReAuthenticate

const win32ras\.RASCS\_ReAuthenticate;

Constant for RAS state\.


## RASCS\_RetryAuthentication

const win32ras\.RASCS\_RetryAuthentication;

Constant for RAS state\.


## RASCS\_StartAuthentication

const win32ras\.RASCS\_StartAuthentication;

Constant for RAS state\.


## RASCS\_WaitForCallback

const win32ras\.RASCS\_WaitForCallback;

Constant for RAS state\.


## RASCS\_WaitForModemReset

const win32ras\.RASCS\_WaitForModemReset;

Constant for RAS state\.


## win32ras::RasDialFunc1 method

  RasDialFunc1\(\)

A placeholder for a RAS callback\.

Defined in: O:/SRC/PYWIN32/WIN32/SRC/WIN32RASMODULE\.CPP

#### Comments

Certain RAS function require a callback function to be passed\. 

This description describes the signature of the function you pass 

to these functions\.

#### Parameters

  - hrascon : int

    The handle to the RAS session\.

  - msg : int

    A message code identifying the reason for the callback\.

  - rascs : int

    Connection state about to be entered\.

  - error : int

    The error state of the connection

  - extendedError : int

    


## [win32ras](win32ras.md#win32ras)\.SetEntryDialParams

SetEntryDialParams\(fileName, RasDialParams, bSavePassword\)
Sets the dial parameters for the specified entry\.

#### Parameters

  - fileName : string

    The filename of the phonebook, or None\.

  - RasDialParams : \(tuple\)

    A tuple describing a RASDIALPARAMS structure\.

  - bSavePassword : int

    Indicates whether to remove password from entry's parameters\.

#### Win32 API References

  - Search for RasSetEntryDialParams at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasSetEntryDialParams.md), [google](http://www.google.com/search?q=RasSetEntryDialParams.md) or [google groups](http://groups.google.com/groups?q=RasSetEntryDialParams.md)\.

  - Search for RasGetConnectStatus at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RasGetConnectStatus.md), [google](http://www.google.com/search?q=RasGetConnectStatus.md) or [google groups](http://groups.google.com/groups?q=RasGetConnectStatus.md)\.