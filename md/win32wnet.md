# win32wnet

## Module win32wnet



A module that exposes the Windows Networking API\.

#### Methods


  - [NETRESOURCE](win32wnet.md#win32wnetnetresource)

    The[PyNETRESOURCE](#pynetresource) type - can be used to create a new[PyNETRESOURCE](#pynetresource) object\.&nbsp;

  - [NCB](win32wnet.md#win32wnetncb)

    ThePyNCB

 type - can be used to create a newPyNCB

 object\.&nbsp;

  - [NCBBuffer](win32wnet.md#win32wnetncbbuffer)

    Creates a new buffer&nbsp;

  - [Netbios](win32wnet.md#win32wnetnetbios)

    Executes a Netbios call\.&nbsp;

  - [WNetAddConnection2](win32wnet.md#win32wnetwnetaddconnection2)

    Creates a connection to a network resource\.&nbsp;

  - [WNetAddConnection3](win32wnet.md#win32wnetwnetaddconnection3)

    Creates a connection to a network resource\.&nbsp;

  - [WNetCancelConnection2](win32wnet.md#win32wnetwnetcancelconnection2)

    Closes network connections made by WNetAddConnection2 or 3&nbsp;

  - [WNetOpenEnum](win32wnet.md#win32wnetwnetopenenum)

    Opens an Enumeration Handle for Enumerating Resources with[win32wnet::WNetEnumResource](win32wnet.md#win32wnetwnetenumresource)&nbsp;

  - [WNetCloseEnum](win32wnet.md#win32wnetwnetcloseenum)

    Closes a PyHANDLE that represents an Open Enumeration \(from[win32wnet::WNetOpenEnum](win32wnet.md#win32wnetwnetopenenum)\)&nbsp;

  - [WNetEnumResource](win32wnet.md#win32wnetwnetenumresource)

    Enumerates a list of resources&nbsp;

  - [WNetGetUser](win32wnet.md#win32wnetwnetgetuser)

    Retrieves the current default user name, or the user name used to establish a network connection\.&nbsp;

  - [WNetGetUniversalName](win32wnet.md#win32wnetwnetgetuniversalname)

    Takes a drive-based path for a network resource and returns an information structure that contains a more universal form of the name\.&nbsp;

  - [WNetGetResourceInformation](win32wnet.md#win32wnetwnetgetresourceinformation)

    Finds the type and provider of a network resource&nbsp;

  - [WNetGetLastError](win32wnet.md#win32wnetwnetgetlasterror)

    Retrieves extended error information set by a network provider when one of the WNet\* functions fails&nbsp;

  - [WNetGetResourceParent](win32wnet.md#win32wnetwnetgetresourceparent)

    Finds the parent resource of a network resource&nbsp;

  - [WNetGetConnection](win32wnet.md#win32wnetwnetgetconnection)

    Retrieves the name of the network resource associated with a local device\.&nbsp;

## [win32wnet](#win32wnet)\.NCBBuffer



buffer =NCBBuffer\(size\)
Creates an NCB buffer of the relevant size\.

#### Parameters


  - size : int

    The number of bytes to allocate\.

## [win32wnet](#win32wnet)\.Netbios



int =Netbios\(ncb\)
Executes a Netbios call\.

#### Parameters


  - ncb :[NCB](#ncb)

    The NCB object to use for the call\.

## [win32wnet](#win32wnet)\.WNetAddConnection2

WNetAddConnection2\(NetResource, Password, UserName, Flags\)
Creates a connection to a network resource\. The function can redirect 

a local device to the network resource\.

#### Parameters


  - NetResource :[PyNETRESOURCE](#pynetresource)

    Describes the network resource for the connection\.

  - Password=None : str

    The password to use\.  Use None for default credentials\.

  - UserName=None : str

    The user name to connect as\.  Use None for default credentials\.

  - Flags=0 : int

    Combination win32netcon\.CONNECT\_\* flags

#### Comments


This function also accepts backwards-compatible, positional-only 

arguments of \(dwType, lpLocalName, lpRemoteName\[, lpProviderName, Username, Password, flags\]\)


Accepts keyword arguments\.

#### Win32 API References


  - Search forWNetAddConnection2 at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=wnetaddconnection2),[google](#http://www.google.com/search?q=wnetaddconnection2) or[google groups](#http://groups.google.com/groups?q=wnetaddconnection2)\.

## [win32wnet](#win32wnet)\.WNetAddConnection3

WNetAddConnection3\(hwnd, NetResource, Password, UserName, Flags\)
Creates a connection to a network resource\.

#### Parameters


  - hwnd : int

    Handle to a parent window\.

  - NetResource :[PyNETRESOURCE](#pynetresource)

    Describes the network resource for the connection\.

  - Password=None : str

    The password to use\.  Use None for default credentials\.

  - UserName=None : str

    The user name to connect as\.  Use None for default credentials\.

  - Flags=0 : int

    Combination win32netcon\.CONNECT\_\* flags

#### Comments


Accepts keyword arguments\.

#### Win32 API References


  - Search forWNetAddConnection3 at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=wnetaddconnection3),[google](#http://www.google.com/search?q=wnetaddconnection3) or[google groups](#http://groups.google.com/groups?q=wnetaddconnection3)\.

## [win32wnet](#win32wnet)\.WNetCancelConnection2

WNetCancelConnection2\(name, flags, force\)
Closes network connections made by WNetAddConnection2 or 3

#### Parameters


  - name : string

    Name of existing connection to be closed

  - flags : int

    Currently determines if the persisent connection information will be updated as a result of this call\.

  - force : int

    indicates if the close operation should be forced\. \(i\.e\. ignore open files and connections\)

## [win32wnet](#win32wnet)\.WNetCloseEnum

WNetCloseEnum\(handle\)
Closes a PyHANDLE that represents an Open Enumeration \(from[win32wnet::WNetOpenEnum](win32wnet.md#win32wnetwnetopenenum)\)

#### Parameters


  - handle :[PyHANDLE](#pyhandle)

    The handle to close, as obtained from[win32wnet::WNetOpenEnum](win32wnet.md#win32wnetwnetopenenum)

#### Comments


You should perform a WNetClose for each handle returned from[win32wnet::WNetOpenEnum](win32wnet.md#win32wnetwnetopenenum)\.

## [win32wnet](#win32wnet)\.WNetEnumResource



\[[PyNETRESOURCE](#pynetresource), \.\.\.\] =WNetEnumResource\(handle, maxExtries\)
Enumerates a list of resources

#### Parameters


  - handle :[PyHANDLE](#pyhandle)

    A handle to an open Enumeration Object \(from[win32wnet::WNetOpenEnum](win32wnet.md#win32wnetwnetopenenum)\)

  - maxExtries=64 : int

    The maximum number of entries to return\. 

enforce the PyHANDLEType, Count is optional

#### Comments


Successive calls to win32wnet\.WNetEnumResource will enumerate starting where the previous call 

stopped\. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is 

closed and reopened\.  This lets you process an enumeration in small chunks \(as small as 1 item at a time\) 

and still fully enumerate a network object\!

#### Return Value
The list contains PyNETRESOURCE entries\. The total number of PyNETRESOURCE entries will be &lt= number 

requested \(excepting the default behavior of requesting 0, which returns up to 64\)

## [win32wnet](#win32wnet)\.WNetGetConnection



string =WNetGetConnection\(connection\)
Retrieves the name of the network resource associated with a local device\.

#### Parameters


  - connection=None : string

    A string that is a drive-based path for a network resource\. 

For example, if drive H has been mapped to a network drive share, and the network resource of interest is a file named Sample\.doc in the directory \\\\Win32\\\\Examples on that share, the drive-based path is H:\\\\Win32\\\\Examples\\\\Sample\.doc\.

## [win32wnet](#win32wnet)\.WNetGetLastError



\(int,str,str\) =WNetGetLastError\(\)
Retrieves extended error information set by a network provider when one of the WNet\* functions fails

#### Comments


The error description or the network provider name may be truncated if they exceed 1024 and 256 characters, respectively

#### Return Value
Returns the error code, a text description of the error, and the name of the network provider

## [win32wnet](#win32wnet)\.WNetGetResourceInformation



\([PyNETRESOURCE](#pynetresource), str\) =WNetGetResourceInformation\(NetResource\)
Finds the type and provider of a network resource

#### Parameters


  - NetResource :[PyNETRESOURCE](#pynetresource)

    Describes a network resource\.  lpRemoteName is required, dwType and lpProvider can be supplied if known

#### Return Value
Returns a NETRESOURCE and a string containing the trailing part of the remote path

## [win32wnet](#win32wnet)\.WNetGetResourceParent

[PyNETRESOURCE](#pynetresource) =WNetGetResourceParent\(NetResource\)
Finds the parent resource of a network resource

#### Parameters


  - NetResource :[PyNETRESOURCE](#pynetresource)

    Describes a network resource\.  lpRemoteName and lpProvider are required, dwType is recommended for efficiency

## [win32wnet](#win32wnet)\.WNetGetUniversalName



string/tuple =WNetGetUniversalName\(localPath, infoLevel\)
Takes a drive-based path for a network resource and returns an information structure that contains a more universal form of the name\.

#### Parameters


  - localPath : string

    A string that is a drive-based path for a network resource\.
For example, if drive H has been mapped to a network drive share, and the network 

resource of interest is a file named SAMPLE\.DOC in the directory \\\\WIN32\\\\EXAMPLES on 

that share, the drive-based path is H:\\\\WIN32\\\\EXAMPLES\\\\SAMPLE\.DOC\.

  - infoLevel=UNIVERSAL\_NAME\_INFO\_LEVEL : int

    Specifies the type of structure that the function stores in the buffer pointed to by the lpBuffer parameter\. 

This parameter can be one of the following values\.

ValueMeaningUNIVERSAL\_NAME\_INFO\_LEVEL \(=1\)The function returns a simple string with the UNC name\.REMOTE\_NAME\_INFO\_LEVEL \(=2\)The function returns a tuple based in the Win32 REMOTE\_NAME\_INFO data structure\.
#### Return Value
If the infoLevel parameter is REMOTE\_NAME\_INFO\_LEVEL, the result is a tuple of 3 strings: \(UNCName, connectionName, remainingPath\)

## [win32wnet](#win32wnet)\.WNetGetUser



string =WNetGetUser\(connection\)
Retrieves the current default user name, or the user name used to establish a network connection\.

#### Parameters


  - connection=None : string

    A string that specifies either the name of a local device that has been redirected to a network resource, or the remote name of a network resource to which a connection has been made without redirecting a local device\. 

If this parameter is None, the system returns the name of the current user for the process\.

## [win32wnet](#win32wnet)\.WNetOpenEnum

[PyHANDLE](#pyhandle) =WNetOpenEnum\(scope, type, usage, resource\)
Opens an Enumeration Handle for Enumerating Resources with[win32wnet::WNetEnumResource](win32wnet.md#win32wnetwnetenumresource)

#### Parameters


  - scope : int

    Specifies the scope of the enumeration\.

  - type : int

    Specifies the resource types to enumerate\.

  - usage : int

    Specifies the resource usage to be enumerated\.

  - resource :[PyNETRESOURCE](#pynetresource)

    Python NETRESOURCE object\.

#### Comments


See the Microsoft SDK  for complete information on WNetOpenEnum\.

#### Return Value
PyHANDLE representing the Win32 HANDLE for the open resource\. 

This handle will be automatically be closed via[win32wnet::WNetCloseEnum](win32wnet.md#win32wnetwnetcloseenum), but 

good style dictates it still be closed manually\.