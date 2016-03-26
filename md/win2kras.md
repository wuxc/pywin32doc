# win2kras

## Module win2kras

A module encapsulating the Windows 2000 extensions to the Remote Access Service (RAS) API.

#### Methods


  - [RasGetEapUserIdentity](win2kras.md#win2krasrasgeteapuseridentity)

    Retrieves identity information for the current user. Use this information to call RasDial with a phone-book entry that requires Extensible Authentication Protocol (EAP).&nbsp;

## [win2kras](#win2kras).PyRasGetEapUserIdentity

 __PyRasGetEapUserIdentity( *phoneBook*  *, entry*  *, flags*  *, hwnd* __ )
Sets the dial parameters for the specified entry.

#### Parameters


  -  *phoneBook* : string

    string containing the full path of the phone-book (PBK) file. If this parameter is None, the function will use the system phone book.

  -  *entry* : string

    string containing an existing entry name.

  -  *flags* : int

    Specifies zero or more of the following flags that qualify the authentication process.

 __Flag__  __Description__ RASEAPF_NonInteractiveSpecifies that the authentication protocol should not bring up a graphical user-interface. If this flag is not present, it is okay for the protocol to display a user interface.RASEAPF_LogonSpecifies that the user data is obtained from Winlogon.RASEAPF_PreviewSpecifies that the user should be prompted for identity information before dialing.
  -  *hwnd=None* :[PyHANDLE](#pyhandle)

    Handle to the parent window for the UI dialog.

#### Win32 API References


  - Search for *RasGetEapUserIdentity* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=rasgeteapuseridentity),[google](#http://www.google.com/search?q=rasgeteapuseridentity)or[google groups](#http://groups.google.com/groups?q=rasgeteapuseridentity).

## RASEAPF_Logon
 __const win2kras.RASEAPF_Logon;__ 
Specifies that the user data is obtained from Winlogon.

## RASEAPF_NonInteractive
 __const win2kras.RASEAPF_NonInteractive;__ 
Specifies that the authentication protocol should not bring up a graphical user-interface. If this flag is not present, it is okay for the protocol to display a user interface.

## RASEAPF_Preview
 __const win2kras.RASEAPF_Preview;__ 
Specifies that the user should be prompted for identity information before dialing.