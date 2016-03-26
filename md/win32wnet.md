
## [win32wnet](#README.md#win32wnet).NCBBuffer

buffer = **NCBBuffer( *size* ** )
Creates an NCB buffer of the relevant size.

#### Parameters


     *size* : int

    The number of bytes to allocate.

## [win32wnet](#README.md#win32wnet).Netbios

int = **Netbios( *ncb* ** )
Executes a Netbios call.

#### Parameters


     *ncb* :[NCB](#README.md#NCB)

    The NCB object to use for the call.

## [win32wnet](#README.md#win32wnet).WNetAddConnection2

 **WNetAddConnection2( *NetResource*  *, Password*  *, UserName*  *, Flags* ** )
Creates a connection to a network resource. The function can redirect 

a local device to the network resource.

#### Parameters


     *NetResource* :[PyNETRESOURCE](#README.md#PyNETRESOURCE)

    Describes the network resource for the connection.

     *Password=None* : str

    The password to use.  Use None for default credentials.

     *UserName=None* : str

    The user name to connect as.  Use None for default credentials.

     *Flags=0* : int

    Combination win32netcon.CONNECT_* flags

#### Comments
This function also accepts backwards-compatible, positional-only 

arguments of (dwType, lpLocalName, lpRemoteName[, lpProviderName, Username, Password, flags])
Accepts keyword arguments.

#### Win32 API References


    Search for *WNetAddConnection2* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WNetAddConnection2),[google](#README.md#http://www.google.com/search?q=WNetAddConnection2)or[google groups](#README.md#http://groups.google.com/groups?q=WNetAddConnection2).

## [win32wnet](#README.md#win32wnet).WNetAddConnection3

 **WNetAddConnection3( *hwnd*  *, NetResource*  *, Password*  *, UserName*  *, Flags* ** )
Creates a connection to a network resource.

#### Parameters


     *hwnd* : int

    Handle to a parent window.

     *NetResource* :[PyNETRESOURCE](#README.md#PyNETRESOURCE)

    Describes the network resource for the connection.

     *Password=None* : str

    The password to use.  Use None for default credentials.

     *UserName=None* : str

    The user name to connect as.  Use None for default credentials.

     *Flags=0* : int

    Combination win32netcon.CONNECT_* flags

#### Comments
Accepts keyword arguments.

#### Win32 API References


    Search for *WNetAddConnection3* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WNetAddConnection3),[google](#README.md#http://www.google.com/search?q=WNetAddConnection3)or[google groups](#README.md#http://groups.google.com/groups?q=WNetAddConnection3).

## [win32wnet](#README.md#win32wnet).WNetCancelConnection2

 **WNetCancelConnection2( *name*  *, flags*  *, force* ** )
Closes network connections made by WNetAddConnection2 or 3

#### Parameters


     *name* : string

    Name of existing connection to be closed

     *flags* : int

    Currently determines if the persisent connection information will be updated as a result of this call.

     *force* : int

    indicates if the close operation should be forced. (i.e. ignore open files and connections)

## [win32wnet](#README.md#win32wnet).WNetCloseEnum

 **WNetCloseEnum( *handle* ** )
Closes a PyHANDLE that represents an Open Enumeration (from[win32wnet::WNetOpenEnum](#win32wnet.md#win32wnetWNetOpenEnum))

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to close, as obtained from[win32wnet::WNetOpenEnum](#win32wnet.md#win32wnetWNetOpenEnum)

#### Comments
You should perform a WNetClose for each handle returned from[win32wnet::WNetOpenEnum](#win32wnet.md#win32wnetWNetOpenEnum).

## [win32wnet](#README.md#win32wnet).WNetEnumResource

[[PyNETRESOURCE](#README.md#PyNETRESOURCE), ...] = **WNetEnumResource( *handle*  *, maxExtries* ** )
Enumerates a list of resources

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    A handle to an open Enumeration Object (from[win32wnet::WNetOpenEnum](#win32wnet.md#win32wnetWNetOpenEnum))

     *maxExtries=64* : int

    The maximum number of entries to return. 

enforce the PyHANDLEType, Count is optional

#### Comments
Successive calls to win32wnet.WNetEnumResource will enumerate starting where the previous call 

stopped. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is 

closed and reopened.  This lets you process an enumeration in small chunks (as small as 1 item at a time) 

and still fully enumerate a network object!

#### Return Value
The list contains PyNETRESOURCE entries. The total number of PyNETRESOURCE entries will be &lt= number 

requested (excepting the default behavior of requesting 0, which returns up to 64)

## [win32wnet](#README.md#win32wnet).WNetGetConnection

string = **WNetGetConnection( *connection* ** )
Retrieves the name of the network resource associated with a local device.

#### Parameters


     *connection=None* : string

    A string that is a drive-based path for a network resource. 

For example, if drive H has been mapped to a network drive share, and the network resource of interest is a file named Sample.doc in the directory \\Win32\\Examples on that share, the drive-based path is H:\\Win32\\Examples\\Sample.doc.

## [win32wnet](#README.md#win32wnet).WNetGetLastError

(int,str,str) = **WNetGetLastError(** )
Retrieves extended error information set by a network provider when one of the WNet* functions fails

#### Comments
The error description or the network provider name may be truncated if they exceed 1024 and 256 characters, respectively

#### Return Value
Returns the error code, a text description of the error, and the name of the network provider

## [win32wnet](#README.md#win32wnet).WNetGetResourceInformation

([PyNETRESOURCE](#README.md#PyNETRESOURCE), str) = **WNetGetResourceInformation( *NetResource* ** )
Finds the type and provider of a network resource

#### Parameters


     *NetResource* :[PyNETRESOURCE](#README.md#PyNETRESOURCE)

    Describes a network resource.  lpRemoteName is required, dwType and lpProvider can be supplied if known

#### Return Value
Returns a NETRESOURCE and a string containing the trailing part of the remote path

## [win32wnet](#README.md#win32wnet).WNetGetResourceParent

[PyNETRESOURCE](#README.md#PyNETRESOURCE)= **WNetGetResourceParent( *NetResource* ** )
Finds the parent resource of a network resource

#### Parameters


     *NetResource* :[PyNETRESOURCE](#README.md#PyNETRESOURCE)

    Describes a network resource.  lpRemoteName and lpProvider are required, dwType is recommended for efficiency

## [win32wnet](#README.md#win32wnet).WNetGetUniversalName

string/tuple = **WNetGetUniversalName( *localPath*  *, infoLevel* ** )
Takes a drive-based path for a network resource and returns an information structure that contains a more universal form of the name.

#### Parameters


     *localPath* : string

    A string that is a drive-based path for a network resource.
For example, if drive H has been mapped to a network drive share, and the network 

resource of interest is a file named SAMPLE.DOC in the directory \\WIN32\\EXAMPLES on 

that share, the drive-based path is H:\\WIN32\\EXAMPLES\\SAMPLE.DOC.

     *infoLevel=UNIVERSAL_NAME_INFO_LEVEL* : int

    Specifies the type of structure that the function stores in the buffer pointed to by the lpBuffer parameter. 

This parameter can be one of the following values.

 **Value**  **Meaning** UNIVERSAL_NAME_INFO_LEVEL (=1)The function returns a simple string with the UNC name.REMOTE_NAME_INFO_LEVEL (=2)The function returns a tuple based in the Win32 REMOTE_NAME_INFO data structure.
#### Return Value
If the infoLevel parameter is REMOTE_NAME_INFO_LEVEL, the result is a tuple of 3 strings: (UNCName, connectionName, remainingPath)

## [win32wnet](#README.md#win32wnet).WNetGetUser

string = **WNetGetUser( *connection* ** )
Retrieves the current default user name, or the user name used to establish a network connection.

#### Parameters


     *connection=None* : string

    A string that specifies either the name of a local device that has been redirected to a network resource, or the remote name of a network resource to which a connection has been made without redirecting a local device. 

If this parameter is None, the system returns the name of the current user for the process.

## [win32wnet](#README.md#win32wnet).WNetOpenEnum

[PyHANDLE](#README.md#PyHANDLE)= **WNetOpenEnum( *scope*  *, type*  *, usage*  *, resource* ** )
Opens an Enumeration Handle for Enumerating Resources with[win32wnet::WNetEnumResource](#win32wnet.md#win32wnetWNetEnumResource)

#### Parameters


     *scope* : int

    Specifies the scope of the enumeration.

     *type* : int

    Specifies the resource types to enumerate.

     *usage* : int

    Specifies the resource usage to be enumerated.

     *resource* :[PyNETRESOURCE](#README.md#PyNETRESOURCE)

    Python NETRESOURCE object.

#### Comments
See the Microsoft SDK  for complete information on WNetOpenEnum.

#### Return Value
PyHANDLE representing the Win32 HANDLE for the open resource. 

This handle will be automatically be closed via[win32wnet::WNetCloseEnum](#win32wnet.md#win32wnetWNetCloseEnum), but 

good style dictates it still be closed manually.