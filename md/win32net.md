# win32net


## Module win32net

A module encapsulating the Windows Network API\.

#### Methods

  - [NetGetJoinInformation](win32net.md#win32netnetgetjoininformation)

    Retrieves join status information for the specified computer\.&nbsp;

  - [NetGroupGetInfo](win32net.md#win32netnetgroupgetinfo)

    Retrieves information about a particular group on a server\.&nbsp;

  - [NetGroupGetUsers](win32net.md#win32netnetgroupgetusers)

    Enumerates the users in a group\.&nbsp;

  - [NetGroupSetUsers](win32net.md#win32netnetgroupsetusers)

    Sets the users in a group on server\.&nbsp;

  - [NetGroupSetInfo](win32net.md#win32netnetgroupsetinfo)

    Sets information about a particular group account on a server\.&nbsp;

  - [NetGroupAdd](win32net.md#win32netnetgroupadd)

    Creates a new group\.&nbsp;

  - [NetGroupAddUser](win32net.md#win32netnetgroupadduser)

    Adds a user to a group&nbsp;

  - [NetGroupDel](win32net.md#win32netnetgroupdel)

    Deletes a group\.&nbsp;

  - [NetGroupDelUser](win32net.md#win32netnetgroupdeluser)

    Deletes a user from the group&nbsp;

  - [NetGroupEnum](win32net.md#win32netnetgroupenum)

    Enumerates the groups\.&nbsp;

  - [NetGroupAdd](win32net.md#win32netnetgroupadd)

    Creates a new group\.&nbsp;

  - [NetLocalGroupAddMembers](win32net.md#win32netnetlocalgroupaddmembers)

    Adds users to a local group\.&nbsp;

  - [NetLocalGroupDelMembers](win32net.md#win32netnetlocalgroupdelmembers)

    Deletes users from a local group\.&nbsp;

  - [NetGroupDel](win32net.md#win32netnetgroupdel)

    Deletes a group\.&nbsp;

  - [NetGroupEnum](win32net.md#win32netnetgroupenum)

    Enumerates the groups\.&nbsp;

  - [NetGroupGetInfo](win32net.md#win32netnetgroupgetinfo)

    Retrieves information about a particular group on a server\.&nbsp;

  - [NetLocalGroupGetMembers](win32net.md#win32netnetlocalgroupgetmembers)

    Enumerates the members in a local group\.&nbsp;

  - [NetGroupSetInfo](win32net.md#win32netnetgroupsetinfo)

    Sets information about a particular group account on a server\.&nbsp;

  - [NetLocalGroupSetMembers](win32net.md#win32netnetlocalgroupsetmembers)

    Sets the members of a local group\.  Any existing members not listed are removed\.&nbsp;

  - [NetMessageBufferSend](win32net.md#win32netnetmessagebuffersend)

    sends a string to a registered message alias\.&nbsp;

  - [NetMessageNameAdd](win32net.md#win32netnetmessagenameadd)

    Add a message alias for a computer&nbsp;

  - [NetMessageNameDel](win32net.md#win32netnetmessagenamedel)

    Removes a message alias&nbsp;

  - [NetMessageNameEnum](win32net.md#win32netnetmessagenameenum)

    List message aliases for a computer&nbsp;

  - [NetServerEnum](win32net.md#win32netnetserverenum)

    Retrieves information about all servers of a specific type&nbsp;

  - [NetServerGetInfo](win32net.md#win32netnetservergetinfo)

    Retrieves information about a particular server\.&nbsp;

  - [NetServerSetInfo](win32net.md#win32netnetserversetinfo)

    Sets information about a particular server\.&nbsp;

  - [NetShareAdd](win32net.md#win32netnetshareadd)

    Creates a new share\.&nbsp;

  - [NetShareDel](win32net.md#win32netnetsharedel)

    Deletes a share&nbsp;

  - [NetShareCheck](win32net.md#win32netnetsharecheck)

    Checks if server is sharing a device&nbsp;

  - [NetShareEnum](win32net.md#win32netnetshareenum)

    Retrieves information about each shared resource on a server\.&nbsp;

  - [NetShareGetInfo](win32net.md#win32netnetsharegetinfo)

    Retrieves information about a particular share on a server\.&nbsp;

  - [NetShareSetInfo](win32net.md#win32netnetsharesetinfo)

    Sets information about a particular share on a server\.&nbsp;

  - [NetUserAdd](win32net.md#win32netnetuseradd)

    Creates a new user\.&nbsp;

  - [NetUserChangePassword](win32net.md#win32netnetuserchangepassword)

    Changes a users password on the specified domain\.&nbsp;

  - [NetUserEnum](win32net.md#win32netnetuserenum)

    Enumerates all users\.&nbsp;

  - [NetUserGetGroups](win32net.md#win32netnetusergetgroups)

    Returns a list of groups,attributes for all groups for the user\.&nbsp;

  - [NetUserGetInfo](win32net.md#win32netnetusergetinfo)

    Retrieves information about a particular user account on a server\.&nbsp;

  - [NetUserGetLocalGroups](win32net.md#win32netnetusergetlocalgroups)

    Retrieves a list of local groups to which a specified user belongs\.&nbsp;

  - [NetUserSetInfo](win32net.md#win32netnetusersetinfo)

    Sets information about a particular user account on a server\.&nbsp;

  - [NetUserDel](win32net.md#win32netnetuserdel)

    Deletes a user\.&nbsp;

  - [NetUserModalsGet](win32net.md#win32netnetusermodalsget)

    Retrieves global user information on a server\.&nbsp;

  - [NetUserModalsSet](win32net.md#win32netnetusermodalsset)

    Sets global user information on a server\.&nbsp;

  - [NetWkstaUserEnum](win32net.md#win32netnetwkstauserenum)

    Retrieves information about all users currently logged on to the workstation\.&nbsp;

  - [NetWkstaGetInfo](win32net.md#win32netnetwkstagetinfo)

    returns information about the configuration elements for a workstation\.&nbsp;

  - [NetWkstaSetInfo](win32net.md#win32netnetwkstasetinfo)

    Sets information about the configuration elements for a workstation\.&nbsp;

  - [NetWkstaTransportEnum](win32net.md#win32netnetwkstatransportenum)

    Retrieves information about transport protocols that are currently managed by the redirector\.&nbsp;

  - [NetWkstaTransportAdd](win32net.md#win32netnetwkstatransportadd)

    binds the redirector to a transport\.&nbsp;

  - [NetWkstaTransportDel](win32net.md#win32netnetwkstatransportdel)

    unbinds transport protocol from the redirector\.&nbsp;

  - [NetServerDiskEnum](win32net.md#win32netnetserverdiskenum)

    Retrieves the list of disk drives on a server\.&nbsp;

  - [NetUseAdd](win32net.md#win32netnetuseadd)

    Establishes connection between local or NULL device name and a shared resource through redirector\.&nbsp;

  - [NetUseDel](win32net.md#win32netnetusedel)

    Ends connection to a shared resource\.&nbsp;

  - [NetUseEnum](win32net.md#win32netnetuseenum)

    Enumerates connection between local machine and shared resources on remote computers\.&nbsp;

  - [NetUseGetInfo](win32net.md#win32netnetusegetinfo)

    Get information about locally mapped shared resource on remote computer\.&nbsp;

  - [NetGetAnyDCName](win32net.md#win32netnetgetanydcname)

    Returns the name of any domain controller trusted by the specified server\.&nbsp;

  - [NetGetDCName](win32net.md#win32netnetgetdcname)

    Returns the name of the primary domain controller \(PDC\)\.&nbsp;

  - [NetSessionEnum](win32net.md#win32netnetsessionenum)

    Returns network session for the server, limited to single client and/or user if specified\.&nbsp;

  - [NetSessionDel](win32net.md#win32netnetsessiondel)

    Delete network session for specified server, client computer and user\. Returns None on success\.&nbsp;

  - [NetSessionGetInfo](win32net.md#win32netnetsessiongetinfo)

    Get network session information\.&nbsp;

  - [NetFileEnum](win32net.md#win32netnetfileenum)

    Returns open file resources for server \(single client and/or user may also be passed as criteria\)\.&nbsp;

  - [NetFileClose](win32net.md#win32netnetfileclose)

    Closes file for specified server and file id\.&nbsp;

  - [NetFileGetInfo](win32net.md#win32netnetfilegetinfo)

    Get info about files open on the server\.&nbsp;

  - [NetStatisticsGet](win32net.md#win32netnetstatisticsget)

    Return server or workstation stats&nbsp;

  - [NetServerComputerNameAdd](win32net.md#win32netnetservercomputernameadd)

    Adds an extra network name for a server&nbsp;

  - [NetServerComputerNameDel](win32net.md#win32netnetservercomputernamedel)

    Deletes an emulated computer name created by win32net::PyNetServerComputerNameAdd

&nbsp;

  - [NetValidateName](win32net.md#win32netnetvalidatename)

    Verify that computer/domain name is valid for given context&nbsp;

  - [NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

    Allows an application to check password compliance against an application-provided account database\.&nbsp;


## [win32net](win32net.md#win32net)\.NetFileClose

NetFileClose\(servername, fileid\)
Closes an open network resource on a server

#### Parameters

  - servername : string/[PyUnicode](PyUnicode.md)

    Name of server on which to operate, local machine assumed if None

  - fileid : int

    Id of opened resource, as returned by [win32net::NetFileEnum](win32net.md#win32netnetfileenum)


## [win32net](win32net.md#win32net)\.NetFileEnum

\(dict,\.\.\.\) = NetFileEnum\(level, servername

, basepath

, username

\)
Lists remotely opened resources on a server

#### Parameters

  - level : int

    Level of information, 2 or 3 supported

  - servername=None : string/[PyUnicode](PyUnicode.md)

    The name of the server for which to list open resources, local machine assumed if None

  - basepath=None : string/[PyUnicode](PyUnicode.md)

    If specified, limits returned list to files on given path

  - username=None : string/[PyUnicode](PyUnicode.md)

    User that opened resource, or None to list open files for all users

#### Return Value
Returns a sequence of dictionaries representing FILE\_INFO\_\* structs, depending on level specified


## [win32net](win32net.md#win32net)\.NetFileGetInfo

dict = NetFileGetInfo\(level, servername

, fileid

\)
Returns information about an open network resource

#### Parameters

  - level : int

    Level of information to return, 2 or 3 supported

  - servername : string/[PyUnicode](PyUnicode.md)

    Server on which resource is open, local machine assumed if None

  - fileid : int

    Id of opened resource, as returned by [win32net::NetFileEnum](win32net.md#win32netnetfileenum)


## [win32net](win32net.md#win32net)\.NetGetAnyDCName

[PyUnicode](PyUnicode.md) = NetGetAnyDCName\(server, domain

\)
Returns the name of any domain controller trusted by the specified server\.

#### Parameters

  - server=None : [PyUnicode](PyUnicode.md)

    Specifies the name of the remote server on which the function is to execute\. If this parameter is None, the local computer is used\.

  - domain=None : [PyUnicode](PyUnicode.md)

    Specifies the name of the domain\. If this parameter is None, the name of the domain controller for the primary domain is used\.


## [win32net](win32net.md#win32net)\.NetGetDCName

[PyUnicode](PyUnicode.md) = NetGetDCName\(server, domain

\)
Returns the name of the primary domain controller \(PDC\)\.

#### Parameters

  - server=None : [PyUnicode](PyUnicode.md)

    Specifies the name of the remote server on which the function is to execute\. If this parameter is None, the local computer is used\.

  - domain=None : [PyUnicode](PyUnicode.md)

    Specifies the name of the domain\. If this parameter is None, the name of the domain controller for the primary domain is used\.


## [win32net](win32net.md#win32net)\.NetGetJoinInformation

[PyUnicode](PyUnicode.md), int = NetGetJoinInformation\(\)
Retrieves join status information for the specified computer\.


## [win32net](win32net.md#win32net)\.NetGroupAdd

NetGroupAdd\(server, level, data\)
Creates a new group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : [PyGROUP\_INFO\_\*](PyGROUP.md#pygroupinfo_.2a)

    A dictionary holding the group data\.

#### Win32 API References

  - Search for NetGroupAdd at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupAdd.md), [google](http://www.google.com/search?q=NetGroupAdd.md) or [google groups](http://groups.google.com/groups?q=NetGroupAdd.md)\.


## [win32net](win32net.md#win32net)\.NetGroupAddUser

NetGroupAddUser\(server, group, username\)
Adds a user to the group

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - group : string/[PyUnicode](PyUnicode.md)

    The group name

  - username : string/[PyUnicode](PyUnicode.md)

    The user to add to the group\.

#### Win32 API References

  - Search for NetGroupAddUser at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupAddUser.md), [google](http://www.google.com/search?q=NetGroupAddUser.md) or [google groups](http://groups.google.com/groups?q=NetGroupAddUser.md)\.


## [win32net](win32net.md#win32net)\.NetGroupDel

NetGroupDel\(server, groupname\)
Deletes a group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupname : string/[PyUnicode](PyUnicode.md)

    The group name

#### Win32 API References

  - Search for NetGroupDel at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupDel.md), [google](http://www.google.com/search?q=NetGroupDel.md) or [google groups](http://groups.google.com/groups?q=NetGroupDel.md)\.


## [win32net](win32net.md#win32net)\.NetGroupDelUser

NetGroupDelUser\(server, group, username\)
Deletes a user from the group

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - group : string/[PyUnicode](PyUnicode.md)

    The group name

  - username : string/[PyUnicode](PyUnicode.md)

    The user to delete from the group\.

#### Win32 API References

  - Search for NetGroupDelUser at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupDelUser.md), [google](http://www.google.com/search?q=NetGroupDelUser.md) or [google groups](http://groups.google.com/groups?q=NetGroupDelUser.md)\.


## [win32net](win32net.md#win32net)\.NetGroupEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetGroupEnum\(server, level

, resumeHandle

, prefLen

\)
Enumerates all groups\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetGroupEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupEnum.md), [google](http://www.google.com/search?q=NetGroupEnum.md) or [google groups](http://groups.google.com/groups?q=NetGroupEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyGROUP\_INFO\_\*](PyGROUP.md#pygroupinfo_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetGroupGetInfo

dict = NetGroupGetInfo\(server, groupname

, level

\)
Retrieves information about a particular group on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupname : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The information level contained in the data

#### Win32 API References

  - Search for NetGroupGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupGetInfo.md), [google](http://www.google.com/search?q=NetGroupGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetGroupGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PyGROUP\_INFO\_\*](PyGROUP.md#pygroupinfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetGroupGetUsers

\(\[dict, \.\.\.\], total, resumeHandle\) = NetGroupGetUsers\(server, groupName

, level

, resumeHandle

, prefLen

\)
Enumerates the users in a group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupName : string/[PyUnicode](PyUnicode.md)

    The name of the local group\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=4096 : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetGroupGetUsers at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupGetUsers.md), [google](http://www.google.com/search?q=NetGroupGetUsers.md) or [google groups](http://groups.google.com/groups?q=NetGroupGetUsers.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyGROUP\_USERS\_INFO\_\*](PyGROUP.md#pygroupusers_info_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetGroupSetInfo

NetGroupSetInfo\(server, groupname, level, data\)
Sets information about a particular group account on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupname : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The information level contained in the data

  - data : [PyGROUP\_INFO\_\*](PyGROUP.md#pygroupinfo_.2a)

    A dictionary holding the group data\.

#### Win32 API References

  - Search for NetGroupSetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupSetInfo.md), [google](http://www.google.com/search?q=NetGroupSetInfo.md) or [google groups](http://groups.google.com/groups?q=NetGroupSetInfo.md)\.


## [win32net](win32net.md#win32net)\.NetGroupSetUsers

NetGroupSetUsers\(server, group, level, members\)
Sets the members of a local group\.  Any existing members not listed are removed\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - group : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The level of information in the data\. Must be 0

  - members : \[[PyGROUP\_USERS\_INFO\_0](PyGROUP.md#pygroupusers_info_0), \.\.\]

    The list of new members 

to add\.

#### Win32 API References

  - Search for NetGroupSetUsers at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupSetUsers.md), [google](http://www.google.com/search?q=NetGroupSetUsers.md) or [google groups](http://groups.google.com/groups?q=NetGroupSetUsers.md)\.


## [win32net](win32net.md#win32net)\.NetLocalGroupAdd

NetLocalGroupAdd\(server, level, data\)
Creates a new group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : [PyLOCALGROUP\_INFO\_\*](PyLOCALGROUP.md#pylocalgroupinfo_.2a)

    A dictionary holding the group data\.

#### Win32 API References

  - Search for NetLocalGroupAdd at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupAdd.md), [google](http://www.google.com/search?q=NetLocalGroupAdd.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupAdd.md)\.


## [win32net](win32net.md#win32net)\.NetLocalGroupAddMembers

NetLocalGroupAddMembers\(server, group, level, members\)
Adds users to a local group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - group : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The level of information in the data\.

  - members : \[[PyLOCALGROUP\_MEMBERS\_INFO\_\*](PyLOCALGROUP.md#pylocalgroupmembers_info_.2a), \]

    The new members to add\.

#### Win32 API References

  - Search for NetLocalGroupAddMembers at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupAddMembers.md), [google](http://www.google.com/search?q=NetLocalGroupAddMembers.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupAddMembers.md)\.


## [win32net](win32net.md#win32net)\.NetLocalGroupDel

NetLocalGroupDel\(server, groupname\)
Deletes a group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupname : string/[PyUnicode](PyUnicode.md)

    The group name

#### Win32 API References

  - Search for NetLocalGroupDel at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupDel.md), [google](http://www.google.com/search?q=NetLocalGroupDel.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupDel.md)\.


## [win32net](win32net.md#win32net)\.NetLocalGroupDelMembers

NetLocalGroupDelMembers\(server, group, members\)
Deletes users from a local group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - group : string/[PyUnicode](PyUnicode.md)

    The group name

  - members : \[string, \.\.\.\]

    A list of strings with fully qualified user names to 

delete from a local group\.

#### Win32 API References

  - Search for NetLocalGroupDelMembers at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupDelMembers.md), [google](http://www.google.com/search?q=NetLocalGroupDelMembers.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupDelMembers.md)\.


## [win32net](win32net.md#win32net)\.NetLocalGroupEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetLocalGroupEnum\(server, level

, resumeHandle

, prefLen

\)
Enumerates all groups\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetLocalGroupEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupEnum.md), [google](http://www.google.com/search?q=NetLocalGroupEnum.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyGROUP\_INFO\_\*](PyGROUP.md#pygroupinfo_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetLocalGroupGetInfo

dict = NetLocalGroupGetInfo\(server, groupname

, level

\)
Retrieves information about a particular group on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupname : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The information level contained in the data

#### Win32 API References

  - Search for NetLocalGroupGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupGetInfo.md), [google](http://www.google.com/search?q=NetLocalGroupGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PyLOCALGROUP\_INFO\_\*](PyLOCALGROUP.md#pylocalgroupinfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetLocalGroupGetMembers

\(\[dict, \.\.\.\], total, resumeHandle\) = NetLocalGroupGetMembers\(server, groupName

, level

, resumeHandle

, prefLen

\)
Enumerates the members in a local group\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupName : string/[PyUnicode](PyUnicode.md)

    The name of the local group\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=4096 : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetLocalGroupGetMembers at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupGetMembers.md), [google](http://www.google.com/search?q=NetLocalGroupGetMembers.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupGetMembers.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyLOCALGROUP\_MEMBERS\_INFO\_\*](PyLOCALGROUP.md#pylocalgroupmembers_info_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetLocalGroupSetInfo

NetLocalGroupSetInfo\(server, groupname, level, data\)
Sets information about a particular group account on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - groupname : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The information level contained in the data

  - data : [PyLOCALGROUP\_INFO\_\*](PyLOCALGROUP.md#pylocalgroupinfo_.2a)

    A dictionary holding the group data\.

#### Win32 API References

  - Search for NetLocalGroupSetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupSetInfo.md), [google](http://www.google.com/search?q=NetLocalGroupSetInfo.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupSetInfo.md)\.


## [win32net](win32net.md#win32net)\.NetLocalGroupSetMembers

NetLocalGroupSetMembers\(server, group, level, members\)
Sets the members of a local group\. Any existing members not listed are removed\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - group : string/[PyUnicode](PyUnicode.md)

    The group name

  - level : int

    The level of information in the data\.

  - members : \[[PyLOCALGROUP\_MEMBERS\_INFO\_\*](PyLOCALGROUP.md#pylocalgroupmembers_info_.2a), \.\.\]

    The list of new members to add\.

#### Win32 API References

  - Search for NetLocalGroupSetMembers at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupSetMembers.md), [google](http://www.google.com/search?q=NetLocalGroupSetMembers.md) or [google groups](http://groups.google.com/groups?q=NetLocalGroupSetMembers.md)\.


## [win32net](win32net.md#win32net)\.NetMessageBufferSend

NetMessageBufferSend\(domain, userName, fromName, message\)
sends a string to a registered message alias\.

#### Parameters

  - domain : string

    Specifies the name of the remote server on which the function is to execute\. None or empty string the local computer\.

  - userName : string

    Specifies the message name to which the message buffer should be sent\.

  - fromName : string

    The user the message is to come from, or None for the current user\.

  - message : string

    The message text

#### Win32 API References

  - Search for NetMessageBufferSend at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetMessageBufferSend.md), [google](http://www.google.com/search?q=NetMessageBufferSend.md) or [google groups](http://groups.google.com/groups?q=NetMessageBufferSend.md)\.


## [win32net](win32net.md#win32net)\.NetMessageNameAdd

NetMessageNameAdd\(server, msgname\)
Adds a message alias for specified machine

#### Parameters

  - server : str/unicode

    Name of server on which to execute - leading backslashes required on NT - local machine used if None

  - msgname : str/unicode

    Message alias to add, 15 characters max


## [win32net](win32net.md#win32net)\.NetMessageNameDel

NetMessageNameDel\(server, msgname\)
Removes a message alias for specified machine

#### Parameters

  - server : str/unicode

    Name of server on which to execute - leading backslashes required on NT - local machine used if None

  - msgname : str/unicode

    Message alias to delete for specified machine


## [win32net](win32net.md#win32net)\.NetMessageNameEnum

NetMessageNameEnum\(Server\)
Lists aliases for a computer

#### Parameters

  - Server : str/unicode

    Name of server on which to execute - leading backslashes required on NT - local machine used if None


## [win32net](win32net.md#win32net)\.NetServerComputerNameAdd

NetServerComputerNameAdd\(ServerName, EmulatedDomainName, EmulatedServerName\)
Adds an additional network name for a server

#### Parameters

  - ServerName : string/[PyUnicode](PyUnicode.md)

    Name of server that will receive additional name

  - EmulatedDomainName : string/[PyUnicode](PyUnicode.md)

    Domain under which to add the new server name, can be None

  - EmulatedServerName : string/[PyUnicode](PyUnicode.md)

    New network name that server will respond to

#### Return Value
Returns none on success


## [win32net](win32net.md#win32net)\.NetServerComputerNameDel

NetServerComputerNameDel\(ServerName, EmulatedServerName\)
Removes a network name added by [win32net::NetServerComputerNameAdd](win32net.md#win32netnetservercomputernameadd)

#### Parameters

  - ServerName : string/[PyUnicode](PyUnicode.md)

    Name of server on which to operate

  - EmulatedServerName : string/[PyUnicode](PyUnicode.md)

    Network name to be removed

#### Return Value
Returns none on success


## [win32net](win32net.md#win32net)\.NetServerDiskEnum

list = NetServerDiskEnum\(server, level

\)
Retrieves the list of disk drives on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The level of data required\. Must be 0\.

#### Win32 API References

  - Search for NetServerDiskEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerDiskEnum.md), [google](http://www.google.com/search?q=NetServerDiskEnum.md) or [google groups](http://groups.google.com/groups?q=NetServerDiskEnum.md)\.

#### Return Value
The result is a list of drives on the server


## [win32net](win32net.md#win32net)\.NetServerEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetServerEnum\(server, level

, type

, domain

, resumeHandle

, prefLen

\)
Retrieves information about each server of a particular type

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The level of data required\.

  - type=SV\_TYPE\_ALL : int

    Type of server to return - one of the SV\_TYPE\_\* constants\.

  - domain=None : string/[PyUnicode](PyUnicode.md)

    The domain to enumerate, or None for the current domain\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetServerEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerEnum.md), [google](http://www.google.com/search?q=NetServerEnum.md) or [google groups](http://groups.google.com/groups?q=NetServerEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PySERVER\_INFO\_\*](PySERVER.md#pyserverinfo_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetServerGetInfo

dict = NetServerGetInfo\(server, level

\)
Retrieves information about a particular server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The information level contained in the data

#### Win32 API References

  - Search for NetServerGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerGetInfo.md), [google](http://www.google.com/search?q=NetServerGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetServerGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PySERVER\_INFO\_\*](PySERVER.md#pyserverinfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetServerSetInfo

NetServerSetInfo\(server, level, data\)
Sets information about a particular server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the share data\.

#### Win32 API References

  - Search for NetServerSetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerSetInfo.md), [google](http://www.google.com/search?q=NetServerSetInfo.md) or [google groups](http://groups.google.com/groups?q=NetServerSetInfo.md)\.


## [win32net](win32net.md#win32net)\.NetSessionDel

NetSessionDel\(server, client, username\)
Disconnects network connections on a server

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server on which to operate, local machine assumed if None or blank

  - client=None : string/[PyUnicode](PyUnicode.md)

    Name of client computer, or None

  - username=None : string/[PyUnicode](PyUnicode.md)

    User name, or None for all connected users

#### Return Value
Returns None on success


## [win32net](win32net.md#win32net)\.NetSessionEnum

\(dict,\.\.\.\) = NetSessionEnum\(level, server

, client

, username

\)
Returns network sessions for a server, limited to single client and/or user if specified\.

#### Parameters

  - level : int

    Level of information requested, currently accepts 0, 1, 2, 10, and 502

  - server=None : string/[PyUnicode](PyUnicode.md)

    The name of the server for which to list sessions, local machine assumed if None

  - client=None : string/[PyUnicode](PyUnicode.md)

    Name of client computer, or None to list all computer sessions

  - username=None : string/[PyUnicode](PyUnicode.md)

    User name, or None to list all connected users

#### Return Value
Returns a sequence of dictionaries representing SESSION\_INFO\_\* structs, depending on level specified


## [win32net](win32net.md#win32net)\.NetSessionGetInfo

dict = NetSessionGetInfo\(level, server

, client

, username

\)
Returns information for a network session from specified client

#### Parameters

  - level : int

    Level of information requested, currently accepts 0, 1, 2, 10, and 502

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server on which to operate, None or blank assumes local machine

  - client : string/[PyUnicode](PyUnicode.md)

    Name of client computer

  - username : string/[PyUnicode](PyUnicode.md)

    User that established session

#### Return Value
Returns a dictionary representing a SESSION\_INFO\_\* struct, depending on level specified


## [win32net](win32net.md#win32net)\.NetShareAdd

NetShareAdd\(server, level, data\)
Creates a new share\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data\.  Must be level 2 or 502\.

  - data : mapping

    A dictionary holding the share data, in the format of SHARE\_INFO\_\*

#### Win32 API References

  - Search for NetShareAdd at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareAdd.md), [google](http://www.google.com/search?q=NetShareAdd.md) or [google groups](http://groups.google.com/groups?q=NetShareAdd.md)\.


## [win32net](win32net.md#win32net)\.NetShareCheck

\(ret, type\) = NetShareCheck\(server, deviceName

\)
Checks if server is sharing a device

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - deviceName : string/[PyUnicode](PyUnicode.md)

    The share name

#### Win32 API References

  - Search for NetShareCheck at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareCheck.md), [google](http://www.google.com/search?q=NetShareCheck.md) or [google groups](http://groups.google.com/groups?q=NetShareCheck.md)\.

#### Return Value
The result is \(1, type-of-device\) if device is shared, \(0, None\) if it is not shared\.


## [win32net](win32net.md#win32net)\.NetShareDel

NetShareDel\(server, shareName, reserved\)
Deletes a share

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - shareName : string/[PyUnicode](PyUnicode.md)

    The share name

  - reserved=0 : int

    Must be zero\.

#### Win32 API References

  - Search for NetShareDel at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareDel.md), [google](http://www.google.com/search?q=NetShareDel.md) or [google groups](http://groups.google.com/groups?q=NetShareDel.md)\.


## [win32net](win32net.md#win32net)\.NetShareEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetShareEnum\(server, level

, resumeHandle

, prefLen

\)
Retrieves information about each shared resource on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Alternative Parameters

  - serverName

    The name of the server on which the call should execute, or None for the local computer\.

#### Comments

If the old style is used, the result is a list of \[\(shareName, type, remarks\), \.\.\.\]

#### Win32 API References

  - Search for NetShareEnum 

param 1 is not declared as const :-\( at [msdn](), [google]() or [google groups]()\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PySHARE\_INFO\_\*](PySHARE.md#pyshareinfo_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetShareGetInfo

dict = NetShareGetInfo\(server, netname

, level

\)
Retrieves information about a particular share on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - netname : string/[PyUnicode](PyUnicode.md)

    The network name

  - level : int

    The information level contained in the data

#### Win32 API References

  - Search for NetShareGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareGetInfo.md), [google](http://www.google.com/search?q=NetShareGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetShareGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PySHARE\_INFO\_\*](PySHARE.md#pyshareinfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetShareSetInfo

NetShareSetInfo\(server, netname, level, data\)
Sets information about a particular share on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - netname : string/[PyUnicode](PyUnicode.md)

    The network name

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the share data\.

#### Win32 API References

  - Search for NetShareSetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareSetInfo.md), [google](http://www.google.com/search?q=NetShareSetInfo.md) or [google groups](http://groups.google.com/groups?q=NetShareSetInfo.md)\.


## [win32net](win32net.md#win32net)\.NetStatisticsGet

dict = NetStatisticsGet\(server, service

, level

, options

\)
Retrieves network statistics for specified service on specified machine

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    Name of server/workstation to retrieve statistics for \(None or blank uses local\)\.

  - service : string/[PyUnicode](PyUnicode.md)

    SERVICE\_SERVER or SERVICE\_WORKSTATION

  - level : int

    Only 0 currently supported\.

  - options : int

    Must be zero\.

#### Return Value
The result is a dictionary representing a STAT\_SERVER\_0 or STAT\_WORKSTATION\_0 struct


## [win32net](win32net.md#win32net)\.NetUseAdd

NetUseAdd\(server, level, data\)
Establishes connection between local or NULL device name and a shared resource through redirector

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the share data in the format of [PyUSE\_INFO\_\*](PyUSE.md#pyuseinfo_.2a)\.

#### Win32 API References

  - Search for NetUseAdd at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseAdd.md), [google](http://www.google.com/search?q=NetUseAdd.md) or [google groups](http://groups.google.com/groups?q=NetUseAdd.md)\.


## [win32net](win32net.md#win32net)\.NetUseDel

NetUseDel\(server, useName, forceCond\)
Ends connection to a shared resource\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - useName : string/[PyUnicode](PyUnicode.md)

    The share name

  - forceCond=0 : int

    Level of force to use\. Can be USE\_FORCE or USE\_NOFORCE or USE\_LOTS\_OF\_FORCE

#### Win32 API References

  - Search for NetUseDel at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseDel.md), [google](http://www.google.com/search?q=NetUseDel.md) or [google groups](http://groups.google.com/groups?q=NetUseDel.md)\.


## [win32net](win32net.md#win32net)\.NetUseEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetUseEnum\(server, level

, resumeHandle

, prefLen

\)
Retrieves information about transport protocols that are currently managed by the redirector

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The level of data required\. Currently levels 0, 1 and 

2 are supported\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetUseEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseEnum.md), [google](http://www.google.com/search?q=NetUseEnum.md) or [google groups](http://groups.google.com/groups?q=NetUseEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyUSE\_INFO\_\*](PyUSE.md#pyuseinfo_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetUseGetInfo

dict = NetUseGetInfo\(server, usename

, level

\)
Retrieves information about the configuration elements for a workstation

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - usename : string/[PyUnicode](PyUnicode.md)

    The name of the locally mapped resource\.

  - level=0 : int

    The information level contained in the data\. NOTE: levels 302 and 402 don't seem to work correctly\. They return error 124\. So currently these info levels are not available\.

#### Win32 API References

  - Search for NetUseGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseGetInfo.md), [google](http://www.google.com/search?q=NetUseGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetUseGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PyUSE\_INFO\_\*](PyUSE.md#pyuseinfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetUserAdd

NetUserAdd\(server, level, data\)
Creates a new user\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the user data in the format of [PyUSER\_INFO\_\*](PyUSER.md#pyuserinfo_.2a)\.

#### Win32 API References

  - Search for NetUserAdd at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserAdd.md), [google](http://www.google.com/search?q=NetUserAdd.md) or [google groups](http://groups.google.com/groups?q=NetUserAdd.md)\.


## [win32net](win32net.md#win32net)\.NetUserChangePassword

NetUserChangePassword\(server, username, oldPassword, newPassword\)
Changes the password for a user\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - username : string/[PyUnicode](PyUnicode.md)

    The user name, or None for the current username\.

  - oldPassword : string/[PyUnicode](PyUnicode.md)

    The old password

  - newPassword : string/[PyUnicode](PyUnicode.md)

    The new password

#### Comments

A server or domain can be configured to require that a 

user log on to change the password on a user account\. 

If that is the case, you need administrator or account operator access 

to change the password for another user acount\. 

If logging on is not required, you can change the password for 

any user account, so long as you know the current password\.

#### Win32 API References

  - Search for NetUserChangePassword at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserChangePassword.md), [google](http://www.google.com/search?q=NetUserChangePassword.md) or [google groups](http://groups.google.com/groups?q=NetUserChangePassword.md)\.


## [win32net](win32net.md#win32net)\.NetUserDel

NetUserDel\(server, username\)
Deletes a user\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - username : string/[PyUnicode](PyUnicode.md)

    The user name

#### Win32 API References

  - Search for NetUserDel at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserDel.md), [google](http://www.google.com/search?q=NetUserDel.md) or [google groups](http://groups.google.com/groups?q=NetUserDel.md)\.


## [win32net](win32net.md#win32net)\.NetUserEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetUserEnum\(server, level

, filter

, resumeHandle

, prefLen

\)
Enumerates all users\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The level of data required\.

  - filter=win32netcon\.FILTER\_NORMAL\_ACCOUNT : int

    The types of accounts to enumerate\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetUserEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserEnum.md), [google](http://www.google.com/search?q=NetUserEnum.md) or [google groups](http://groups.google.com/groups?q=NetUserEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyUSER\_INFO\_\*](PyUSER.md#pyuserinfo_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetUserGetGroups

\[\(groupName, attribute\), \.\.\.\] = NetUserGetGroups\(serverName, userName

\)
Returns a list of groups,attributes for all groups for the user\.

#### Parameters

  - serverName : string

    The name of the remote server on which the function is to execute\. None or an empty string specifies the server program running on the local computer\.

  - userName : string

    The name of the user to search for in each group account\.

####  To Do
 This needs to be extended to support the new model, while 

not breaking existing code\.  A default arg would be perfect\.

#### Return Value
Always makes the level 1 call and returns all data\. 

Data return format is a Python List\.  Each "Item" 

is a tuple of \(groupname, attributes\)\.  "\(s,i\)" respectively\.  In NT 4 the attributes seem to be hardcoded to 7\. 

Earlier version of NT have not been tested\.


## [win32net](win32net.md#win32net)\.NetUserGetInfo

dict = NetUserGetInfo\(server, username

, level

\)
Retrieves information about a particular user account on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - username : string/[PyUnicode](PyUnicode.md)

    The user name

  - level : int

    The information level contained in the data

#### Win32 API References

  - Search for NetUserGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserGetInfo.md), [google](http://www.google.com/search?q=NetUserGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetUserGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PyUSER\_INFO\_\*](PyUSER.md#pyuserinfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetUserGetLocalGroups

\[groupName, \.\.\.\] = NetUserGetLocalGroups\(serverName, userName

, flags

\)
Retrieves a list of local groups to which a specified user belongs\.

#### Parameters

  - serverName : string

    The name of the remote server on which the function is to execute\. None or an empty string specifies the server program running on the local computer\.

  - userName : string

    The name of the user to search for in each group account\. This parameter can be of the form &ltUserName&gt, in which case the username is expected to be found on servername\. The user name can also be of the form &ltDomainName&gt\\\\&ltUserName&gt in which case &ltDomainName&gt is associated with servername and &ltUserName&gt is expected to be to be found on that domain\.

  - flags=LG\_INCLUDE\_INDIRECT : int

    Flags for the call\.

####  To Do
 This needs to be extended to support the new model, while 

not breaking existing code\.  A default arg would be perfect\.


## [win32net](win32net.md#win32net)\.NetUserModalsGet

dict = NetUserModalsGet\(server, level

\)
Retrieves global user information on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

#### Win32 API References

  - Search for NetUserModalsGet at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserModalsGet.md), [google](http://www.google.com/search?q=NetUserModalsGet.md) or [google groups](http://groups.google.com/groups?q=NetUserModalsGet.md)\.

#### Return Value
The result will be a dictionary in one of the [PyUSER\_MODALS\_INFO\_\*](PyUSER.md#pyusermodals_info_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetUserModalsSet

NetUserModalsSet\(server, level, data\)
Sets global user parameters on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the data in the format of [PyUSER\_MODALS\_INFO\_\*](PyUSER.md#pyusermodals_info_.2a)\.

#### Win32 API References

  - Search for NetUserModalsSet at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserModalsSet.md), [google](http://www.google.com/search?q=NetUserModalsSet.md) or [google groups](http://groups.google.com/groups?q=NetUserModalsSet.md)\.


## [win32net](win32net.md#win32net)\.NetUserSetInfo

NetUserSetInfo\(server, username, level, data\)
Sets information about a particular user account on a server\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - username : string/[PyUnicode](PyUnicode.md)

    The user name

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the user data in the format of [PyUSER\_INFO\_\*](PyUSER.md#pyuserinfo_.2a)

#### Win32 API References

  - Search for NetUserSetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserSetInfo.md), [google](http://www.google.com/search?q=NetUserSetInfo.md) or [google groups](http://groups.google.com/groups?q=NetUserSetInfo.md)\.


## [win32net](win32net.md#win32net)\.NetValidateName

NetValidateName\(Server, Name, NameType, Account, Password\)
Checks that domain/machine/workgroup name is valid for given context

#### Parameters

  - Server : string/[PyUnicode](PyUnicode.md)

    Name of server on which to execute \(None or blank uses local\)

  - Name : string/[PyUnicode](PyUnicode.md)

    Machine, domain, or workgroup name to validate

  - NameType : int

    Type of name to validate - from NETSETUP\_NAME\_TYPE enum \(win32net\.NetSetup\*\)

  - Account=None : string/[PyUnicode](PyUnicode.md)

    Account name to use while validating, current security context is used if not specified

  - Password=None : string/[PyUnicode](PyUnicode.md)

    Password for Account

#### Comments

If Account and Password aren't passed, current logon credentials are used

Will raise NotImplementedError if not available on this platform\.

#### Return Value
Returns none if valid, exception if not


## [win32net](win32net.md#win32net)\.NetValidatePasswordPolicy

NetValidatePasswordPolicy\(Server, Qualifier, ValidationType, arg\)
Allows an application to check 

password compliance against an application-provided account database and 

verify that passwords meet the complexity, aging, minimum length, and 

history reuse requirements of a password policy\.

#### Parameters

  - Server : string/[PyUnicode](PyUnicode.md)

    Name of server on which to execute \(None or blank uses local\)

  - Qualifier : None

    Reserved, must be None

  - ValidationType : int

    The type of password validation to perform

  - arg : dict/tuple

    Depends on the ValidationType param - either 

a [PyNET\_VALIDATE\_AUTHENTICATION\_INPUT\_ARG](PyNET.md#pynetvalidate_authentication_input_arg),  [PyNET\_VALIDATE\_PASSWORD\_CHANGE\_INPUT\_ARG](PyNET.md#pynetvalidate_password_change_input_arg) 

or PyNET\_VALIDATE\_PASSWORD\_RESET\_INPUT\_ARG

 tuple or dict\.

#### Comments

Will raise NotImplementedError if not available on this platform, or 

raise win32net\.error if the function fails\.

#### Return Value
Returns a tuple of \([PyNET\_VALIDATE\_PERSISTED\_FIELDS](PyNET.md#pynetvalidate_persisted_fields), int\) with 

the integer being the ValidationResult\.


## [win32net](win32net.md#win32net)\.NetWkstaGetInfo

dict = NetWkstaGetInfo\(server, level

\)
Retrieves information about the configuration elements for a workstation

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The information level contained in the data\. NOTE: levels 302 and 402 don't seem to work correctly\. They return error 124\. So currently these info levels are not available\.

#### Win32 API References

  - Search for NetWkstaGetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaGetInfo.md), [google](http://www.google.com/search?q=NetWkstaGetInfo.md) or [google groups](http://groups.google.com/groups?q=NetWkstaGetInfo.md)\.

#### Return Value
The result will be a dictionary in one of the [PyWKSTA\_INFO\_\*](PyWKSTA.md#pywkstainfo_.2a) 

formats, depending on the level parameter\.


## [win32net](win32net.md#win32net)\.NetWkstaSetInfo

NetWkstaSetInfo\(server, level, data\)
Sets information about the configuration elements for a workstation

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the share data\.

#### Win32 API References

  - Search for NetWkstaSetInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaSetInfo.md), [google](http://www.google.com/search?q=NetWkstaSetInfo.md) or [google groups](http://groups.google.com/groups?q=NetWkstaSetInfo.md)\.


## [win32net](win32net.md#win32net)\.NetWkstaTransportAdd

NetWkstaTransportAdd\(server, level, data\)
binds the redirector to a transport

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - level : int

    The information level contained in the data

  - data : mapping

    A dictionary holding the share data\.

#### Win32 API References

  - Search for NetWkstaTransportAdd at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaTransportAdd.md), [google](http://www.google.com/search?q=NetWkstaTransportAdd.md) or [google groups](http://groups.google.com/groups?q=NetWkstaTransportAdd.md)\.


## [win32net](win32net.md#win32net)\.NetWkstaTransportDel

NetWkstaTransportDel\(server, TransportName, ucond\)
unbinds the transport protocol from redirector

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server, or None\.

  - TransportName : string/[PyUnicode](PyUnicode.md)

    The name of the transport to delete\.

  - ucond=0 : int

    Level of force to use\. Can be USE\_FORCE or USE\_NOFORCE or USE\_LOTS\_OF\_FORCE

#### Win32 API References

  - Search for NetWkstaTransportDel at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaTransportDel.md), [google](http://www.google.com/search?q=NetWkstaTransportDel.md) or [google groups](http://groups.google.com/groups?q=NetWkstaTransportDel.md)\.


## [win32net](win32net.md#win32net)\.NetWkstaTransportEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetWkstaTransportEnum\(server, level

, resumeHandle

, prefLen

\)
Retrieves information about transport protocols that are currently managed by the redirector

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetWkstaTransportEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaTransportEnum.md), [google](http://www.google.com/search?q=NetWkstaTransportEnum.md) or [google groups](http://groups.google.com/groups?q=NetWkstaTransportEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyWKSTA\_TRANSPORT\_INFO\_\*](PyWKSTA.md#pywkstatransport_info_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.


## [win32net](win32net.md#win32net)\.NetWkstaUserEnum

\(\[dict, \.\.\.\], total, resumeHandle\) = NetWkstaUserEnum\(server, level

, resumeHandle

, prefLen

\)
Retrieves information about all users currently logged on to the workstation\.

#### Parameters

  - server : string/[PyUnicode](PyUnicode.md)

    The name of the server to execute on, or None\.

  - level : int

    The level of data required\.

  - resumeHandle=0 : int

    A resume handle\.  See the return description for more information\.

  - prefLen=MAX\_PREFERRED\_LENGTH : int

    The preferred length of the data buffer\.

#### Win32 API References

  - Search for NetWkstaUserEnum at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaUserEnum.md), [google](http://www.google.com/search?q=NetWkstaUserEnum.md) or [google groups](http://groups.google.com/groups?q=NetWkstaUserEnum.md)\.

#### Return Value
The result is a list of items read \(with each item being a dictionary of format 

[PyWKSTA\_USER\_INFO\_\*](PyWKSTA.md#pywkstauser_info_.2a), depending on the level parameter\), 

the total available, and a new "resume handle"\.  The first time you call 

this function, you should pass zero for the resume handle\.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data\. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read\.