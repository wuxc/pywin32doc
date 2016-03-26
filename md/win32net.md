
## [win32net](#README.md#win32net).NetFileClose

 **NetFileClose( *servername*  *, fileid* ** )
Closes an open network resource on a server

#### Parameters


     *servername* : string/[PyUnicode](#README.md#PyUnicode)

    Name of server on which to operate, local machine assumed if None

     *fileid* : int

    Id of opened resource, as returned by[win32net::NetFileEnum](#win32net.md#win32netNetFileEnum)

## [win32net](#README.md#win32net).NetFileEnum

(dict,...) = **NetFileEnum( *level*  *, servername*  *, basepath*  *, username* ** )
Lists remotely opened resources on a server

#### Parameters


     *level* : int

    Level of information, 2 or 3 supported

     *servername=None* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server for which to list open resources, local machine assumed if None

     *basepath=None* : string/[PyUnicode](#README.md#PyUnicode)

    If specified, limits returned list to files on given path

     *username=None* : string/[PyUnicode](#README.md#PyUnicode)

    User that opened resource, or None to list open files for all users

#### Return Value
Returns a sequence of dictionaries representing FILE_INFO_* structs, depending on level specified

## [win32net](#README.md#win32net).NetFileGetInfo

dict = **NetFileGetInfo( *level*  *, servername*  *, fileid* ** )
Returns information about an open network resource

#### Parameters


     *level* : int

    Level of information to return, 2 or 3 supported

     *servername* : string/[PyUnicode](#README.md#PyUnicode)

    Server on which resource is open, local machine assumed if None

     *fileid* : int

    Id of opened resource, as returned by[win32net::NetFileEnum](#win32net.md#win32netNetFileEnum)

## [win32net](#README.md#win32net).NetGetAnyDCName

[PyUnicode](#README.md#PyUnicode)= **NetGetAnyDCName( *server*  *, domain* ** )
Returns the name of any domain controller trusted by the specified server.

#### Parameters


     *server=None* :[PyUnicode](#README.md#PyUnicode)

    Specifies the name of the remote server on which the function is to execute. If this parameter is None, the local computer is used.

     *domain=None* :[PyUnicode](#README.md#PyUnicode)

    Specifies the name of the domain. If this parameter is None, the name of the domain controller for the primary domain is used.

## [win32net](#README.md#win32net).NetGetDCName

[PyUnicode](#README.md#PyUnicode)= **NetGetDCName( *server*  *, domain* ** )
Returns the name of the primary domain controller (PDC).

#### Parameters


     *server=None* :[PyUnicode](#README.md#PyUnicode)

    Specifies the name of the remote server on which the function is to execute. If this parameter is None, the local computer is used.

     *domain=None* :[PyUnicode](#README.md#PyUnicode)

    Specifies the name of the domain. If this parameter is None, the name of the domain controller for the primary domain is used.

## [win32net](#README.md#win32net).NetGetJoinInformation

[PyUnicode](#README.md#PyUnicode), int = **NetGetJoinInformation(** )
Retrieves join status information for the specified computer.

## [win32net](#README.md#win32net).NetGroupAdd

 **NetGroupAdd( *server*  *, level*  *, data* ** )
Creates a new group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* :[PyGROUP_INFO_*](#PyGROUP.md#PyGROUPINFO_.2a)

    A dictionary holding the group data.

#### Win32 API References


    Search for *NetGroupAdd* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupAdd),[google](#README.md#http://www.google.com/search?q=NetGroupAdd)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupAdd).

## [win32net](#README.md#win32net).NetGroupAddUser

 **NetGroupAddUser( *server*  *, group*  *, username* ** )
Adds a user to the group

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *group* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    The user to add to the group.

#### Win32 API References


    Search for *NetGroupAddUser* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupAddUser),[google](#README.md#http://www.google.com/search?q=NetGroupAddUser)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupAddUser).

## [win32net](#README.md#win32net).NetGroupDel

 **NetGroupDel( *server*  *, groupname* ** )
Deletes a group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupname* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

#### Win32 API References


    Search for *NetGroupDel* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupDel),[google](#README.md#http://www.google.com/search?q=NetGroupDel)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupDel).

## [win32net](#README.md#win32net).NetGroupDelUser

 **NetGroupDelUser( *server*  *, group*  *, username* ** )
Deletes a user from the group

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *group* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    The user to delete from the group.

#### Win32 API References


    Search for *NetGroupDelUser* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupDelUser),[google](#README.md#http://www.google.com/search?q=NetGroupDelUser)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupDelUser).

## [win32net](#README.md#win32net).NetGroupEnum

([dict, ...], total, resumeHandle) = **NetGroupEnum( *server*  *, level*  *, resumeHandle*  *, prefLen* ** )
Enumerates all groups.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetGroupEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupEnum),[google](#README.md#http://www.google.com/search?q=NetGroupEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyGROUP_INFO_*](#PyGROUP.md#PyGROUPINFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetGroupGetInfo

dict = **NetGroupGetInfo( *server*  *, groupname*  *, level* ** )
Retrieves information about a particular group on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupname* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The information level contained in the data

#### Win32 API References


    Search for *NetGroupGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupGetInfo),[google](#README.md#http://www.google.com/search?q=NetGroupGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupGetInfo).

#### Return Value
The result will be a dictionary in one of the[PyGROUP_INFO_*](#PyGROUP.md#PyGROUPINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetGroupGetUsers

([dict, ...], total, resumeHandle) = **NetGroupGetUsers( *server*  *, groupName*  *, level*  *, resumeHandle*  *, prefLen* ** )
Enumerates the users in a group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupName* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the local group.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=4096* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetGroupGetUsers* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupGetUsers),[google](#README.md#http://www.google.com/search?q=NetGroupGetUsers)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupGetUsers).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyGROUP_USERS_INFO_*](#PyGROUP.md#PyGROUPUSERS_INFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetGroupSetInfo

 **NetGroupSetInfo( *server*  *, groupname*  *, level*  *, data* ** )
Sets information about a particular group account on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupname* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The information level contained in the data

     *data* :[PyGROUP_INFO_*](#PyGROUP.md#PyGROUPINFO_.2a)

    A dictionary holding the group data.

#### Win32 API References


    Search for *NetGroupSetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupSetInfo),[google](#README.md#http://www.google.com/search?q=NetGroupSetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupSetInfo).

## [win32net](#README.md#win32net).NetGroupSetUsers

 **NetGroupSetUsers( *server*  *, group*  *, level*  *, members* ** )
Sets the members of a local group.  Any existing members not listed are removed.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *group* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The level of information in the data. Must be 0

     *members* : [[PyGROUP_USERS_INFO_0](#PyGROUP.md#PyGROUPUSERS_INFO_0), ..]

    The list of new members 

to add.

#### Win32 API References


    Search for *NetGroupSetUsers* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetGroupSetUsers),[google](#README.md#http://www.google.com/search?q=NetGroupSetUsers)or[google groups](#README.md#http://groups.google.com/groups?q=NetGroupSetUsers).

## [win32net](#README.md#win32net).NetLocalGroupAdd

 **NetLocalGroupAdd( *server*  *, level*  *, data* ** )
Creates a new group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* :[PyLOCALGROUP_INFO_*](#PyLOCALGROUP.md#PyLOCALGROUPINFO_.2a)

    A dictionary holding the group data.

#### Win32 API References


    Search for *NetLocalGroupAdd* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupAdd),[google](#README.md#http://www.google.com/search?q=NetLocalGroupAdd)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupAdd).

## [win32net](#README.md#win32net).NetLocalGroupAddMembers

 **NetLocalGroupAddMembers( *server*  *, group*  *, level*  *, members* ** )
Adds users to a local group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *group* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The level of information in the data.

     *members* : [[PyLOCALGROUP_MEMBERS_INFO_*](#PyLOCALGROUP.md#PyLOCALGROUPMEMBERS_INFO_.2a), ]

    The new members to add.

#### Win32 API References


    Search for *NetLocalGroupAddMembers* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupAddMembers),[google](#README.md#http://www.google.com/search?q=NetLocalGroupAddMembers)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupAddMembers).

## [win32net](#README.md#win32net).NetLocalGroupDel

 **NetLocalGroupDel( *server*  *, groupname* ** )
Deletes a group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupname* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

#### Win32 API References


    Search for *NetLocalGroupDel* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupDel),[google](#README.md#http://www.google.com/search?q=NetLocalGroupDel)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupDel).

## [win32net](#README.md#win32net).NetLocalGroupDelMembers

 **NetLocalGroupDelMembers( *server*  *, group*  *, members* ** )
Deletes users from a local group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *group* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *members* : [string, ...]

    A list of strings with fully qualified user names to 

delete from a local group.

#### Win32 API References


    Search for *NetLocalGroupDelMembers* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupDelMembers),[google](#README.md#http://www.google.com/search?q=NetLocalGroupDelMembers)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupDelMembers).

## [win32net](#README.md#win32net).NetLocalGroupEnum

([dict, ...], total, resumeHandle) = **NetLocalGroupEnum( *server*  *, level*  *, resumeHandle*  *, prefLen* ** )
Enumerates all groups.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetLocalGroupEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupEnum),[google](#README.md#http://www.google.com/search?q=NetLocalGroupEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyGROUP_INFO_*](#PyGROUP.md#PyGROUPINFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetLocalGroupGetInfo

dict = **NetLocalGroupGetInfo( *server*  *, groupname*  *, level* ** )
Retrieves information about a particular group on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupname* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The information level contained in the data

#### Win32 API References


    Search for *NetLocalGroupGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupGetInfo),[google](#README.md#http://www.google.com/search?q=NetLocalGroupGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupGetInfo).

#### Return Value
The result will be a dictionary in one of the[PyLOCALGROUP_INFO_*](#PyLOCALGROUP.md#PyLOCALGROUPINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetLocalGroupGetMembers

([dict, ...], total, resumeHandle) = **NetLocalGroupGetMembers( *server*  *, groupName*  *, level*  *, resumeHandle*  *, prefLen* ** )
Enumerates the members in a local group.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupName* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the local group.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=4096* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetLocalGroupGetMembers* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupGetMembers),[google](#README.md#http://www.google.com/search?q=NetLocalGroupGetMembers)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupGetMembers).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyLOCALGROUP_MEMBERS_INFO_*](#PyLOCALGROUP.md#PyLOCALGROUPMEMBERS_INFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetLocalGroupSetInfo

 **NetLocalGroupSetInfo( *server*  *, groupname*  *, level*  *, data* ** )
Sets information about a particular group account on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *groupname* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The information level contained in the data

     *data* :[PyLOCALGROUP_INFO_*](#PyLOCALGROUP.md#PyLOCALGROUPINFO_.2a)

    A dictionary holding the group data.

#### Win32 API References


    Search for *NetLocalGroupSetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupSetInfo),[google](#README.md#http://www.google.com/search?q=NetLocalGroupSetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupSetInfo).

## [win32net](#README.md#win32net).NetLocalGroupSetMembers

 **NetLocalGroupSetMembers( *server*  *, group*  *, level*  *, members* ** )
Sets the members of a local group. Any existing members not listed are removed.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *group* : string/[PyUnicode](#README.md#PyUnicode)

    The group name

     *level* : int

    The level of information in the data.

     *members* : [[PyLOCALGROUP_MEMBERS_INFO_*](#PyLOCALGROUP.md#PyLOCALGROUPMEMBERS_INFO_.2a), ..]

    The list of new members to add.

#### Win32 API References


    Search for *NetLocalGroupSetMembers* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetLocalGroupSetMembers),[google](#README.md#http://www.google.com/search?q=NetLocalGroupSetMembers)or[google groups](#README.md#http://groups.google.com/groups?q=NetLocalGroupSetMembers).

## [win32net](#README.md#win32net).NetMessageBufferSend

 **NetMessageBufferSend( *domain*  *, userName*  *, fromName*  *, message* ** )
sends a string to a registered message alias.

#### Parameters


     *domain* : string

    Specifies the name of the remote server on which the function is to execute. None or empty string the local computer.

     *userName* : string

    Specifies the message name to which the message buffer should be sent.

     *fromName* : string

    The user the message is to come from, or None for the current user.

     *message* : string

    The message text

#### Win32 API References


    Search for *NetMessageBufferSend* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetMessageBufferSend),[google](#README.md#http://www.google.com/search?q=NetMessageBufferSend)or[google groups](#README.md#http://groups.google.com/groups?q=NetMessageBufferSend).

## [win32net](#README.md#win32net).NetMessageNameAdd

 **NetMessageNameAdd( *server*  *, msgname* ** )
Adds a message alias for specified machine

#### Parameters


     *server* : str/unicode

    Name of server on which to execute - leading backslashes required on NT - local machine used if None

     *msgname* : str/unicode

    Message alias to add, 15 characters max

## [win32net](#README.md#win32net).NetMessageNameDel

 **NetMessageNameDel( *server*  *, msgname* ** )
Removes a message alias for specified machine

#### Parameters


     *server* : str/unicode

    Name of server on which to execute - leading backslashes required on NT - local machine used if None

     *msgname* : str/unicode

    Message alias to delete for specified machine

## [win32net](#README.md#win32net).NetMessageNameEnum

 **NetMessageNameEnum( *Server* ** )
Lists aliases for a computer

#### Parameters


     *Server* : str/unicode

    Name of server on which to execute - leading backslashes required on NT - local machine used if None

## [win32net](#README.md#win32net).NetServerComputerNameAdd

 **NetServerComputerNameAdd( *ServerName*  *, EmulatedDomainName*  *, EmulatedServerName* ** )
Adds an additional network name for a server

#### Parameters


     *ServerName* : string/[PyUnicode](#README.md#PyUnicode)

    Name of server that will receive additional name

     *EmulatedDomainName* : string/[PyUnicode](#README.md#PyUnicode)

    Domain under which to add the new server name, can be None

     *EmulatedServerName* : string/[PyUnicode](#README.md#PyUnicode)

    New network name that server will respond to

#### Return Value
Returns none on success

## [win32net](#README.md#win32net).NetServerComputerNameDel

 **NetServerComputerNameDel( *ServerName*  *, EmulatedServerName* ** )
Removes a network name added by[win32net::NetServerComputerNameAdd](#win32net.md#win32netNetServerComputerNameAdd)

#### Parameters


     *ServerName* : string/[PyUnicode](#README.md#PyUnicode)

    Name of server on which to operate

     *EmulatedServerName* : string/[PyUnicode](#README.md#PyUnicode)

    Network name to be removed

#### Return Value
Returns none on success

## [win32net](#README.md#win32net).NetServerDiskEnum

list = **NetServerDiskEnum( *server*  *, level* ** )
Retrieves the list of disk drives on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The level of data required. Must be 0.

#### Win32 API References


    Search for *NetServerDiskEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerDiskEnum),[google](#README.md#http://www.google.com/search?q=NetServerDiskEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetServerDiskEnum).

#### Return Value
The result is a list of drives on the server

## [win32net](#README.md#win32net).NetServerEnum

([dict, ...], total, resumeHandle) = **NetServerEnum( *server*  *, level*  *, type*  *, domain*  *, resumeHandle*  *, prefLen* ** )
Retrieves information about each server of a particular type

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The level of data required.

     *type=SV_TYPE_ALL* : int

    Type of server to return - one of the SV_TYPE_* constants.

     *domain=None* : string/[PyUnicode](#README.md#PyUnicode)

    The domain to enumerate, or None for the current domain.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetServerEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerEnum),[google](#README.md#http://www.google.com/search?q=NetServerEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetServerEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PySERVER_INFO_*](#PySERVER.md#PySERVERINFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetServerGetInfo

dict = **NetServerGetInfo( *server*  *, level* ** )
Retrieves information about a particular server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The information level contained in the data

#### Win32 API References


    Search for *NetServerGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerGetInfo),[google](#README.md#http://www.google.com/search?q=NetServerGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetServerGetInfo).

#### Return Value
The result will be a dictionary in one of the[PySERVER_INFO_*](#PySERVER.md#PySERVERINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetServerSetInfo

 **NetServerSetInfo( *server*  *, level*  *, data* ** )
Sets information about a particular server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the share data.

#### Win32 API References


    Search for *NetServerSetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetServerSetInfo),[google](#README.md#http://www.google.com/search?q=NetServerSetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetServerSetInfo).

## [win32net](#README.md#win32net).NetSessionDel

 **NetSessionDel( *server*  *, client*  *, username* ** )
Disconnects network connections on a server

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server on which to operate, local machine assumed if None or blank

     *client=None* : string/[PyUnicode](#README.md#PyUnicode)

    Name of client computer, or None

     *username=None* : string/[PyUnicode](#README.md#PyUnicode)

    User name, or None for all connected users

#### Return Value
Returns None on success

## [win32net](#README.md#win32net).NetSessionEnum

(dict,...) = **NetSessionEnum( *level*  *, server*  *, client*  *, username* ** )
Returns network sessions for a server, limited to single client and/or user if specified.

#### Parameters


     *level* : int

    Level of information requested, currently accepts 0, 1, 2, 10, and 502

     *server=None* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server for which to list sessions, local machine assumed if None

     *client=None* : string/[PyUnicode](#README.md#PyUnicode)

    Name of client computer, or None to list all computer sessions

     *username=None* : string/[PyUnicode](#README.md#PyUnicode)

    User name, or None to list all connected users

#### Return Value
Returns a sequence of dictionaries representing SESSION_INFO_* structs, depending on level specified

## [win32net](#README.md#win32net).NetSessionGetInfo

dict = **NetSessionGetInfo( *level*  *, server*  *, client*  *, username* ** )
Returns information for a network session from specified client

#### Parameters


     *level* : int

    Level of information requested, currently accepts 0, 1, 2, 10, and 502

     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server on which to operate, None or blank assumes local machine

     *client* : string/[PyUnicode](#README.md#PyUnicode)

    Name of client computer

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    User that established session

#### Return Value
Returns a dictionary representing a SESSION_INFO_* struct, depending on level specified

## [win32net](#README.md#win32net).NetShareAdd

 **NetShareAdd( *server*  *, level*  *, data* ** )
Creates a new share.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data.  Must be level 2 or 502.

     *data* : mapping

    A dictionary holding the share data, in the format of **SHARE_INFO_*** 

#### Win32 API References


    Search for *NetShareAdd* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareAdd),[google](#README.md#http://www.google.com/search?q=NetShareAdd)or[google groups](#README.md#http://groups.google.com/groups?q=NetShareAdd).

## [win32net](#README.md#win32net).NetShareCheck

(ret, type) = **NetShareCheck( *server*  *, deviceName* ** )
Checks if server is sharing a device

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *deviceName* : string/[PyUnicode](#README.md#PyUnicode)

    The share name

#### Win32 API References


    Search for *NetShareCheck* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareCheck),[google](#README.md#http://www.google.com/search?q=NetShareCheck)or[google groups](#README.md#http://groups.google.com/groups?q=NetShareCheck).

#### Return Value
The result is (1, type-of-device) if device is shared, (0, None) if it is not shared.

## [win32net](#README.md#win32net).NetShareDel

 **NetShareDel( *server*  *, shareName*  *, reserved* ** )
Deletes a share

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *shareName* : string/[PyUnicode](#README.md#PyUnicode)

    The share name

     *reserved=0* : int

    Must be zero.

#### Win32 API References


    Search for *NetShareDel* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareDel),[google](#README.md#http://www.google.com/search?q=NetShareDel)or[google groups](#README.md#http://groups.google.com/groups?q=NetShareDel).

## [win32net](#README.md#win32net).NetShareEnum

([dict, ...], total, resumeHandle) = **NetShareEnum( *server*  *, level*  *, resumeHandle*  *, prefLen* ** )
Retrieves information about each shared resource on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Alternative Parameters


     *serverName* 

    The name of the server on which the call should execute, or None for the local computer.

#### Comments
If the old style is used, the result is a list of [(shareName, type, remarks), ...]

#### Win32 API References


    Search for *NetShareEnum 

param 1 is not declared as const :-(* at[msdn](#),[google](#)or[google groups](#).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PySHARE_INFO_*](#PySHARE.md#PySHAREINFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetShareGetInfo

dict = **NetShareGetInfo( *server*  *, netname*  *, level* ** )
Retrieves information about a particular share on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *netname* : string/[PyUnicode](#README.md#PyUnicode)

    The network name

     *level* : int

    The information level contained in the data

#### Win32 API References


    Search for *NetShareGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareGetInfo),[google](#README.md#http://www.google.com/search?q=NetShareGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetShareGetInfo).

#### Return Value
The result will be a dictionary in one of the[PySHARE_INFO_*](#PySHARE.md#PySHAREINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetShareSetInfo

 **NetShareSetInfo( *server*  *, netname*  *, level*  *, data* ** )
Sets information about a particular share on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *netname* : string/[PyUnicode](#README.md#PyUnicode)

    The network name

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the share data.

#### Win32 API References


    Search for *NetShareSetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetShareSetInfo),[google](#README.md#http://www.google.com/search?q=NetShareSetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetShareSetInfo).

## [win32net](#README.md#win32net).NetStatisticsGet

dict = **NetStatisticsGet( *server*  *, service*  *, level*  *, options* ** )
Retrieves network statistics for specified service on specified machine

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    Name of server/workstation to retrieve statistics for (None or blank uses local).

     *service* : string/[PyUnicode](#README.md#PyUnicode)

    SERVICE_SERVER or SERVICE_WORKSTATION

     *level* : int

    Only 0 currently supported.

     *options* : int

    Must be zero.

#### Return Value
The result is a dictionary representing a STAT_SERVER_0 or STAT_WORKSTATION_0 struct

## [win32net](#README.md#win32net).NetUseAdd

 **NetUseAdd( *server*  *, level*  *, data* ** )
Establishes connection between local or NULL device name and a shared resource through redirector

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the share data in the format of[PyUSE_INFO_*](#PyUSE.md#PyUSEINFO_.2a).

#### Win32 API References


    Search for *NetUseAdd* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseAdd),[google](#README.md#http://www.google.com/search?q=NetUseAdd)or[google groups](#README.md#http://groups.google.com/groups?q=NetUseAdd).

## [win32net](#README.md#win32net).NetUseDel

 **NetUseDel( *server*  *, useName*  *, forceCond* ** )
Ends connection to a shared resource.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *useName* : string/[PyUnicode](#README.md#PyUnicode)

    The share name

     *forceCond=0* : int

    Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCE

#### Win32 API References


    Search for *NetUseDel* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseDel),[google](#README.md#http://www.google.com/search?q=NetUseDel)or[google groups](#README.md#http://groups.google.com/groups?q=NetUseDel).

## [win32net](#README.md#win32net).NetUseEnum

([dict, ...], total, resumeHandle) = **NetUseEnum( *server*  *, level*  *, resumeHandle*  *, prefLen* ** )
Retrieves information about transport protocols that are currently managed by the redirector

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The level of data required. Currently levels 0, 1 and 

2 are supported.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetUseEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseEnum),[google](#README.md#http://www.google.com/search?q=NetUseEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetUseEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyUSE_INFO_*](#PyUSE.md#PyUSEINFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetUseGetInfo

dict = **NetUseGetInfo( *server*  *, usename*  *, level* ** )
Retrieves information about the configuration elements for a workstation

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *usename* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the locally mapped resource.

     *level=0* : int

    The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.

#### Win32 API References


    Search for *NetUseGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUseGetInfo),[google](#README.md#http://www.google.com/search?q=NetUseGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetUseGetInfo).

#### Return Value
The result will be a dictionary in one of the[PyUSE_INFO_*](#PyUSE.md#PyUSEINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetUserAdd

 **NetUserAdd( *server*  *, level*  *, data* ** )
Creates a new user.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the user data in the format of[PyUSER_INFO_*](#PyUSER.md#PyUSERINFO_.2a).

#### Win32 API References


    Search for *NetUserAdd* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserAdd),[google](#README.md#http://www.google.com/search?q=NetUserAdd)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserAdd).

## [win32net](#README.md#win32net).NetUserChangePassword

 **NetUserChangePassword( *server*  *, username*  *, oldPassword*  *, newPassword* ** )
Changes the password for a user.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    The user name, or None for the current username.

     *oldPassword* : string/[PyUnicode](#README.md#PyUnicode)

    The old password

     *newPassword* : string/[PyUnicode](#README.md#PyUnicode)

    The new password

#### Comments
A server or domain can be configured to require that a 

user log on to change the password on a user account. 

If that is the case, you need administrator or account operator access 

to change the password for another user acount. 

If logging on is not required, you can change the password for 

any user account, so long as you know the current password.

#### Win32 API References


    Search for *NetUserChangePassword* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserChangePassword),[google](#README.md#http://www.google.com/search?q=NetUserChangePassword)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserChangePassword).

## [win32net](#README.md#win32net).NetUserDel

 **NetUserDel( *server*  *, username* ** )
Deletes a user.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    The user name

#### Win32 API References


    Search for *NetUserDel* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserDel),[google](#README.md#http://www.google.com/search?q=NetUserDel)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserDel).

## [win32net](#README.md#win32net).NetUserEnum

([dict, ...], total, resumeHandle) = **NetUserEnum( *server*  *, level*  *, filter*  *, resumeHandle*  *, prefLen* ** )
Enumerates all users.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The level of data required.

     *filter=win32netcon.FILTER_NORMAL_ACCOUNT* : int

    The types of accounts to enumerate.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetUserEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserEnum),[google](#README.md#http://www.google.com/search?q=NetUserEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyUSER_INFO_*](#PyUSER.md#PyUSERINFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetUserGetGroups

[(groupName, attribute), ...] = **NetUserGetGroups( *serverName*  *, userName* ** )
Returns a list of groups,attributes for all groups for the user.

#### Parameters


     *serverName* : string

    The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.

     *userName* : string

    The name of the user to search for in each group account.

#### To Do
This needs to be extended to support the new model, while 

not breaking existing code.  A default arg would be perfect.

#### Return Value
Always makes the level 1 call and returns all data. 

Data return format is a Python List.  Each "Item" 

is a tuple of (groupname, attributes).  "(s,i)" respectively.  In NT 4 the attributes seem to be hardcoded to 7. 

Earlier version of NT have not been tested.

## [win32net](#README.md#win32net).NetUserGetInfo

dict = **NetUserGetInfo( *server*  *, username*  *, level* ** )
Retrieves information about a particular user account on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    The user name

     *level* : int

    The information level contained in the data

#### Win32 API References


    Search for *NetUserGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserGetInfo),[google](#README.md#http://www.google.com/search?q=NetUserGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserGetInfo).

#### Return Value
The result will be a dictionary in one of the[PyUSER_INFO_*](#PyUSER.md#PyUSERINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetUserGetLocalGroups

[groupName, ...] = **NetUserGetLocalGroups( *serverName*  *, userName*  *, flags* ** )
Retrieves a list of local groups to which a specified user belongs.

#### Parameters


     *serverName* : string

    The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.

     *userName* : string

    The name of the user to search for in each group account. This parameter can be of the form &ltUserName&gt, in which case the username is expected to be found on servername. The user name can also be of the form &ltDomainName&gt\\&ltUserName&gt in which case &ltDomainName&gt is associated with servername and &ltUserName&gt is expected to be to be found on that domain.

     *flags=LG_INCLUDE_INDIRECT* : int

    Flags for the call.

#### To Do
This needs to be extended to support the new model, while 

not breaking existing code.  A default arg would be perfect.

## [win32net](#README.md#win32net).NetUserModalsGet

dict = **NetUserModalsGet( *server*  *, level* ** )
Retrieves global user information on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

#### Win32 API References


    Search for *NetUserModalsGet* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserModalsGet),[google](#README.md#http://www.google.com/search?q=NetUserModalsGet)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserModalsGet).

#### Return Value
The result will be a dictionary in one of the[PyUSER_MODALS_INFO_*](#PyUSER.md#PyUSERMODALS_INFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetUserModalsSet

 **NetUserModalsSet( *server*  *, level*  *, data* ** )
Sets global user parameters on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the data in the format of[PyUSER_MODALS_INFO_*](#PyUSER.md#PyUSERMODALS_INFO_.2a).

#### Win32 API References


    Search for *NetUserModalsSet* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserModalsSet),[google](#README.md#http://www.google.com/search?q=NetUserModalsSet)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserModalsSet).

## [win32net](#README.md#win32net).NetUserSetInfo

 **NetUserSetInfo( *server*  *, username*  *, level*  *, data* ** )
Sets information about a particular user account on a server.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *username* : string/[PyUnicode](#README.md#PyUnicode)

    The user name

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the user data in the format of[PyUSER_INFO_*](#PyUSER.md#PyUSERINFO_.2a)

#### Win32 API References


    Search for *NetUserSetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetUserSetInfo),[google](#README.md#http://www.google.com/search?q=NetUserSetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetUserSetInfo).

## [win32net](#README.md#win32net).NetValidateName

 **NetValidateName( *Server*  *, Name*  *, NameType*  *, Account*  *, Password* ** )
Checks that domain/machine/workgroup name is valid for given context

#### Parameters


     *Server* : string/[PyUnicode](#README.md#PyUnicode)

    Name of server on which to execute (None or blank uses local)

     *Name* : string/[PyUnicode](#README.md#PyUnicode)

    Machine, domain, or workgroup name to validate

     *NameType* : int

    Type of name to validate - from NETSETUP_NAME_TYPE enum (win32net.NetSetup*)

     *Account=None* : string/[PyUnicode](#README.md#PyUnicode)

    Account name to use while validating, current security context is used if not specified

     *Password=None* : string/[PyUnicode](#README.md#PyUnicode)

    Password for Account

#### Comments
If Account and Password aren't passed, current logon credentials are used
Will raise NotImplementedError if not available on this platform.

#### Return Value
Returns none if valid, exception if not

## [win32net](#README.md#win32net).NetValidatePasswordPolicy

 **NetValidatePasswordPolicy( *Server*  *, Qualifier*  *, ValidationType*  *, arg* ** )
Allows an application to check 

password compliance against an application-provided account database and 

verify that passwords meet the complexity, aging, minimum length, and 

history reuse requirements of a password policy.

#### Parameters


     *Server* : string/[PyUnicode](#README.md#PyUnicode)

    Name of server on which to execute (None or blank uses local)

     *Qualifier* : None

    Reserved, must be None

     *ValidationType* : int

    The type of password validation to perform

     *arg* : dict/tuple

    Depends on the ValidationType param - either 

a[PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG](#PyNET.md#PyNETVALIDATE_AUTHENTICATION_INPUT_ARG),[PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG](#PyNET.md#PyNETVALIDATE_PASSWORD_CHANGE_INPUT_ARG)or **PyNET_VALIDATE_PASSWORD_RESET_INPUT_ARG** tuple or dict.

#### Comments
Will raise NotImplementedError if not available on this platform, or 

raise win32net.error if the function fails.

#### Return Value
Returns a tuple of ([PyNET_VALIDATE_PERSISTED_FIELDS](#PyNET.md#PyNETVALIDATE_PERSISTED_FIELDS), int) with 

the integer being the ValidationResult.

## [win32net](#README.md#win32net).NetWkstaGetInfo

dict = **NetWkstaGetInfo( *server*  *, level* ** )
Retrieves information about the configuration elements for a workstation

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.

#### Win32 API References


    Search for *NetWkstaGetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaGetInfo),[google](#README.md#http://www.google.com/search?q=NetWkstaGetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetWkstaGetInfo).

#### Return Value
The result will be a dictionary in one of the[PyWKSTA_INFO_*](#PyWKSTA.md#PyWKSTAINFO_.2a)formats, depending on the level parameter.

## [win32net](#README.md#win32net).NetWkstaSetInfo

 **NetWkstaSetInfo( *server*  *, level*  *, data* ** )
Sets information about the configuration elements for a workstation

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the share data.

#### Win32 API References


    Search for *NetWkstaSetInfo* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaSetInfo),[google](#README.md#http://www.google.com/search?q=NetWkstaSetInfo)or[google groups](#README.md#http://groups.google.com/groups?q=NetWkstaSetInfo).

## [win32net](#README.md#win32net).NetWkstaTransportAdd

 **NetWkstaTransportAdd( *server*  *, level*  *, data* ** )
binds the redirector to a transport

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *level* : int

    The information level contained in the data

     *data* : mapping

    A dictionary holding the share data.

#### Win32 API References


    Search for *NetWkstaTransportAdd* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaTransportAdd),[google](#README.md#http://www.google.com/search?q=NetWkstaTransportAdd)or[google groups](#README.md#http://groups.google.com/groups?q=NetWkstaTransportAdd).

## [win32net](#README.md#win32net).NetWkstaTransportDel

 **NetWkstaTransportDel( *server*  *, TransportName*  *, ucond* ** )
unbinds the transport protocol from redirector

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server, or None.

     *TransportName* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the transport to delete.

     *ucond=0* : int

    Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCE

#### Win32 API References


    Search for *NetWkstaTransportDel* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaTransportDel),[google](#README.md#http://www.google.com/search?q=NetWkstaTransportDel)or[google groups](#README.md#http://groups.google.com/groups?q=NetWkstaTransportDel).

## [win32net](#README.md#win32net).NetWkstaTransportEnum

([dict, ...], total, resumeHandle) = **NetWkstaTransportEnum( *server*  *, level*  *, resumeHandle*  *, prefLen* ** )
Retrieves information about transport protocols that are currently managed by the redirector

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetWkstaTransportEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaTransportEnum),[google](#README.md#http://www.google.com/search?q=NetWkstaTransportEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetWkstaTransportEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyWKSTA_TRANSPORT_INFO_*](#PyWKSTA.md#PyWKSTATRANSPORT_INFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

## [win32net](#README.md#win32net).NetWkstaUserEnum

([dict, ...], total, resumeHandle) = **NetWkstaUserEnum( *server*  *, level*  *, resumeHandle*  *, prefLen* ** )
Retrieves information about all users currently logged on to the workstation.

#### Parameters


     *server* : string/[PyUnicode](#README.md#PyUnicode)

    The name of the server to execute on, or None.

     *level* : int

    The level of data required.

     *resumeHandle=0* : int

    A resume handle.  See the return description for more information.

     *prefLen=MAX_PREFERRED_LENGTH* : int

    The preferred length of the data buffer.

#### Win32 API References


    Search for *NetWkstaUserEnum* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=NetWkstaUserEnum),[google](#README.md#http://www.google.com/search?q=NetWkstaUserEnum)or[google groups](#README.md#http://groups.google.com/groups?q=NetWkstaUserEnum).

#### Return Value
The result is a list of items read (with each item being a dictionary of format[PyWKSTA_USER_INFO_*](#PyWKSTA.md#PyWKSTAUSER_INFO_.2a), depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.