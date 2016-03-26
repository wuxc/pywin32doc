# win32security


## Module win32security

An interface to the win32 security API's

#### Methods

  - [DsGetSpn](win32security.md#win32securitydsgetspn)

    Compose one or more service principal names to be registered using [win32security::DsWriteAccountSpn](win32security.md#win32securitydswriteaccountspn)&nbsp;

  - [DsWriteAccountSpn](win32security.md#win32securitydswriteaccountspn)

    Associates a set of service principal names with an account&nbsp;

  - [DsBind](win32security.md#win32securitydsbind)

    Creates a connection to a directory service&nbsp;

  - [DsUnBind](win32security.md#win32securitydsunbind)

    Closes a directory services handle created by [win32security::DsBind](win32security.md#win32securitydsbind)&nbsp;

  - [DsGetDcName](win32security.md#win32securitydsgetdcname)

    Returns the name of a domain controller \(DC\) in a specified domain\. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics\.&nbsp;

  - [DsCrackNames](win32security.md#win32securitydscracknames)

    Converts an array of directory service object names from one format to another\.&nbsp;

  - [DsListInfoForServer](win32security.md#win32securitydslistinfoforserver)

    Lists miscellaneous information for a server\.&nbsp;

  - [DsListServersInSite](win32security.md#win32securitydslistserversinsite)

    &nbsp;

  - [DsListServersInSite](win32security.md#win32securitydslistserversinsite)

    &nbsp;

  - [DsListServersInSite](win32security.md#win32securitydslistserversinsite)

    &nbsp;

  - [DsListRoles](win32security.md#win32securitydslistroles)

    &nbsp;

  - [DsListDomainsInSite](win32security.md#win32securitydslistdomainsinsite)

    &nbsp;

  - [ACL](win32security.md#win32securityacl)

    Creates a new [PyACL](PyACL.md) object\.&nbsp;

  - [SID](win32security.md#win32securitysid)

    Creates a new [PySID](PySID.md) object\.&nbsp;

  - [SECURITY\_ATTRIBUTES](win32security.md#win32securitysecurity_attributes)

    Creates a new [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes) object\.&nbsp;

  - [SECURITY\_DESCRIPTOR](win32security.md#win32securitysecurity_descriptor)

    Creates a new [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) object\.&nbsp;

  - [ImpersonateNamedPipeClient](win32security.md#win32securityimpersonatenamedpipeclient)

    Impersonates a named-pipe client application\.&nbsp;

  - [ImpersonateLoggedOnUser](win32security.md#win32securityimpersonateloggedonuser)

    Impersonates a logged on user\.&nbsp;

  - [ImpersonateAnonymousToken](win32security.md#win32securityimpersonateanonymoustoken)

    Cause a thread to act in the security context of an anonymous token&nbsp;

  - [IsTokenRestricted](win32security.md#win32securityistokenrestricted)

    Checks if a token contains restricted sids&nbsp;

  - [RevertToSelf](win32security.md#win32securityreverttoself)

    Terminates the impersonation of a client application\.&nbsp;

  - [LogonUser](win32security.md#win32securitylogonuser)

    Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called\. You cannot use LogonUser to log on to a remote computer\.&nbsp;

  - [LogonUserEx](win32security.md#win32securitylogonuserex)

    Log a user onto the local machine,&nbsp;

  - [LookupAccountName](win32security.md#win32securitylookupaccountname)

    Accepts the name of a system and an account as input\. It retrieves a security identifier \(SID\) for the account and the name of the domain on which the account was found\.&nbsp;

  - [LookupAccountSid](win32security.md#win32securitylookupaccountsid)

    Accepts a security identifier \(SID\) as input\. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found\.&nbsp;

  - [GetBinarySid](win32security.md#win32securitygetbinarysid)

    Accepts a SID string \(eg: S-1-5-32-544\) and returns the SID as a PySID object\.&nbsp;

  - [SetSecurityInfo](win32security.md#win32securitysetsecurityinfo)

    Sets security info for an object by handle&nbsp;

  - [GetSecurityInfo](win32security.md#win32securitygetsecurityinfo)

    Retrieve security info for an object by handle&nbsp;

  - [SetNamedSecurityInfo](win32security.md#win32securitysetnamedsecurityinfo)

    Sets security info for an object by name&nbsp;

  - [GetNamedSecurityInfo](win32security.md#win32securitygetnamedsecurityinfo)

    Retrieve security info for an object by name&nbsp;

  - [OpenProcessToken](win32security.md#win32securityopenprocesstoken)

    Opens the access token associated with a process\.&nbsp;

  - [LookupPrivilegeValue](win32security.md#win32securitylookupprivilegevalue)

    Retrieves the locally unique id for a privilege name&nbsp;

  - [LookupPrivilegeName](win32security.md#win32securitylookupprivilegename)

    return the text name for a privilege LUID&nbsp;

  - [LookupPrivilegeDisplayName](win32security.md#win32securitylookupprivilegedisplayname)

    Returns long description for a privilege name&nbsp;

  - [AdjustTokenPrivileges](win32security.md#win32securityadjusttokenprivileges)

    Enables or disables privileges for an access token\.&nbsp;

  - [AdjustTokenGroups](win32security.md#win32securityadjusttokengroups)

    Sets the groups associated to an access token\.&nbsp;

  - [GetTokenInformation](win32security.md#win32securitygettokeninformation)

    Retrieves a specified type of information about an access token\. The calling process must have appropriate access rights to obtain the information\.&nbsp;

  - [OpenThreadToken](win32security.md#win32securityopenthreadtoken)

    Opens the access token associated with a thread\.&nbsp;

  - [SetThreadToken](win32security.md#win32securitysetthreadtoken)

    Assigns an impersonation token to a thread\. The function 

can also cause a thread to stop using an impersonation token\.&nbsp;

  - [GetFileSecurity](win32security.md#win32securitygetfilesecurity)

    Obtains specified information about the security of a file or directory\. The information obtained is constrained by the caller's access rights and privileges\.&nbsp;

  - [SetFileSecurity](win32security.md#win32securitysetfilesecurity)

    Sets information about the security of a file or directory\. The information obtained is constrained by the caller's access rights and privileges\.&nbsp;

  - [GetUserObjectSecurity](win32security.md#win32securitygetuserobjectsecurity)

    Obtains specified information about the security of a user object\. The information obtained is constrained by the caller's access rights and privileges\.&nbsp;

  - [SetUserObjectSecurity](win32security.md#win32securitysetuserobjectsecurity)

    Sets information about the security of a user object\. The information obtained is constrained by the caller's access rights and privileges\.&nbsp;

  - [GetKernelObjectSecurity](win32security.md#win32securitygetkernelobjectsecurity)

    Obtains specified information about the security of a kernel object\. The information obtained is constrained by the caller's access rights and privileges\.&nbsp;

  - [SetKernelObjectSecurity](win32security.md#win32securitysetkernelobjectsecurity)

    Sets information about the security of a kernel object\. The information obtained is constrained by the caller's access rights and privileges\.&nbsp;

  - [SetTokenInformation](win32security.md#win32securitysettokeninformation)

    Set a specified type of information in an access token&nbsp;

  - [LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

    Opens a policy handle for the specified system&nbsp;

  - [LsaClose](win32security.md#win32securitylsaclose)

    Closes a policy handle created by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)&nbsp;

  - [LsaQueryInformationPolicy](win32security.md#win32securitylsaqueryinformationpolicy)

    Retrieves information from the policy handle&nbsp;

  - [LsaSetInformationPolicy](win32security.md#win32securitylsasetinformationpolicy)

    Sets policy options&nbsp;

  - [LsaAddAccountRights](win32security.md#win32securitylsaaddaccountrights)

    Adds a list of privileges to an account&nbsp;

  - [LsaRemoveAccountRights](win32security.md#win32securitylsaremoveaccountrights)

    Removes privs from an account&nbsp;

  - [LsaEnumerateAccountRights](win32security.md#win32securitylsaenumerateaccountrights)

    Lists privileges held by SID&nbsp;

  - [LsaEnumerateAccountsWithUserRight](win32security.md#win32securitylsaenumerateaccountswithuserright)

    Return SIDs that hold specified priv&nbsp;

  - [ConvertSidToStringSid](win32security.md#win32securityconvertsidtostringsid)

    Return string representation of a SID&nbsp;

  - [ConvertStringSidToSid](win32security.md#win32securityconvertstringsidtosid)

    Creates a SID from a string representation&nbsp;

  - [ConvertSecurityDescriptorToStringSecurityDescriptor](win32security.md#win32securityconvertsecuritydescriptortostringsecuritydescriptor)

    Return string representation of a SECURITY\_DESCRIPTOR&nbsp;

  - [ConvertStringSecurityDescriptorToSecurityDescriptor](win32security.md#win32securityconvertstringsecuritydescriptortosecuritydescriptor)

    Turns string representation of a SECURITY\_DESCRIPTOR into the real thing&nbsp;

  - [LsaStorePrivateData](win32security.md#win32securitylsastoreprivatedata)

    Stores encrypted unicode data under specified Lsa registry key\. Returns None on success&nbsp;

  - [LsaRetrievePrivateData](win32security.md#win32securitylsaretrieveprivatedata)

    Retreives encrypted unicode data from Lsa registry key\.&nbsp;

  - [LsaRegisterPolicyChangeNotification](win32security.md#win32securitylsaregisterpolicychangenotification)

    Register an event handle to receive policy change events&nbsp;

  - [LsaUnregisterPolicyChangeNotification](win32security.md#win32securitylsaunregisterpolicychangenotification)

    Stop receiving policy change notification&nbsp;

  - [CryptEnumProviders](win32security.md#win32securitycryptenumproviders)

    List cryptography providers&nbsp;

  - [EnumerateSecurityPackages](win32security.md#win32securityenumeratesecuritypackages)

    List available security packages as a sequence of dictionaries representing SecPkgInfo structures&nbsp;

  - [AllocateLocallyUniqueId](win32security.md#win32securityallocatelocallyuniqueid)

    Creates a new LUID&nbsp;

  - [ImpersonateSelf](win32security.md#win32securityimpersonateself)

    Assigns an impersonation token for current security context to current process&nbsp;

  - [DuplicateToken](win32security.md#win32securityduplicatetoken)

    Creates a copy of an access token with specified impersonation level&nbsp;

  - [DuplicateTokenEx](win32security.md#win32securityduplicatetokenex)

    Extended version of DuplicateToken\.&nbsp;

  - [CheckTokenMembership](win32security.md#win32securitychecktokenmembership)

    Checks if a SID is enabled in a token&nbsp;

  - [CreateRestrictedToken](win32security.md#win32securitycreaterestrictedtoken)

    Creates a restricted copy of an access token with reduced privs - requires win2K or higher&nbsp;

  - [LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess)

    Creates a trusted connection to LSA&nbsp;

  - [LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted)

    Creates untrusted connection to LSA&nbsp;

  - [LsaDeregisterLogonProcess](win32security.md#win32securitylsaderegisterlogonprocess)

    Closes connection to LSA server&nbsp;

  - [LsaLookupAuthenticationPackage](win32security.md#win32securitylsalookupauthenticationpackage)

    Retrieves the unique id for an authentication package&nbsp;

  - [LsaEnumerateLogonSessions](win32security.md#win32securitylsaenumeratelogonsessions)

    Lists all current logon ids&nbsp;

  - [LsaGetLogonSessionData](win32security.md#win32securitylsagetlogonsessiondata)

    Returns information about a logon session&nbsp;

  - [AcquireCredentialsHandle](win32security.md#win32securityacquirecredentialshandle)

    Creates a handle to credentials for use with SSPI&nbsp;

  - [InitializeSecurityContext](win32security.md#win32securityinitializesecuritycontext)

    Creates a security context based on credentials created by AcquireCredentialsHandle&nbsp;

  - [AcceptSecurityContext](win32security.md#win32securityacceptsecuritycontext)

    Builds security context between server and client&nbsp;

  - [QuerySecurityPackageInfo](win32security.md#win32securityquerysecuritypackageinfo)

    Retrieves parameters for a security package&nbsp;

  - [LsaCallAuthenticationPackage](win32security.md#win32securitylsacallauthenticationpackage)

    Requests the services of an authentication package&nbsp;

  - [TranslateName](win32security.md#win32securitytranslatename)

    Converts a directory service object name from one format to another\.&nbsp;

  - [CreateWellKnownSid](win32security.md#win32securitycreatewellknownsid)

    Returns one of the predefined well known sids&nbsp;

  - [MapGenericMask](win32security.md#win32securitymapgenericmask)

    Translates generic access rights into specific rights&nbsp;


## ACCESS\_ALLOWED\_ACE\_TYPE

const win32security\.ACCESS\_ALLOWED\_ACE\_TYPE;

Access-allowed ACE that uses the ACCESS\_ALLOWED\_ACE structure\.


## ACCESS\_ALLOWED\_OBJECT\_ACE\_TYPE

const win32security\.ACCESS\_ALLOWED\_OBJECT\_ACE\_TYPE;

Windows 2000/XP: Object-specific access-allowed ACE that uses the ACCESS\_ALLOWED\_OBJECT\_ACE structure\.


## ACCESS\_DENIED\_ACE\_TYPE

const win32security\.ACCESS\_DENIED\_ACE\_TYPE;

Access-denied ACE that uses the ACCESS\_DENIED\_ACE structure\.


## ACCESS\_DENIED\_OBJECT\_ACE\_TYPE

const win32security\.ACCESS\_DENIED\_OBJECT\_ACE\_TYPE;

Windows 2000/XP: Object-specific access-denied ACE that uses the ACCESS\_DENIED\_OBJECT\_ACE structure\.


## [win32security](win32security.md#win32security)\.ACL

PyACL = ACL\(bufSize\)
Creates a new [PyACL](PyACL.md) object\.

#### Parameters

  - bufSize=64 : int

    The size of the buffer for the ACL\.


## ACL\_REVISION

const win32security\.ACL\_REVISION;




## ACL\_REVISION\_DS

const win32security\.ACL\_REVISION\_DS;




## [win32security](win32security.md#win32security)\.AcceptSecurityContext

\(int, long, int\) = AcceptSecurityContext\(Credential, Context

, pInput

, ContextReq

, TargetDataRep

, NewContext

, pOutput

\)
Builds security context between server and client

#### Parameters

  - Credential : [PyCredHandle](PyCredHandle.md)

    Handle to server's credentials \(see AcquireCredentialsHandle\)

  - Context : [PyCtxtHandle](PyCtxtHandle.md)

    Use None on initial call, then handle returned in NewContext thereafter

  - pInput : [PySecBufferDesc](PySecBufferDesc.md)

    Data buffer received from client

  - ContextReq : int

    Combination of ASC\_REQ\_\* flags

  - TargetDataRep : int

    One of SECURITY\_NATIVE\_DREP,SECURITY\_NETWORK\_DREP

  - NewContext : [PyCtxtHandle](PyCtxtHandle.md)

    Uninitialized context handle to receive output

  - pOutput : [PySecBufferDesc](PySecBufferDesc.md)

    Buffer that receives output data, to be passed back as pInput on subsequent calls

#### Return Value
Returns a tuple of \(return code, context attributes, context expiration time\)


## [win32security](win32security.md#win32security)\.AcquireCredentialsHandle

\([PyCredHandle](PyCredHandle.md),[PyTime](PyTime.md)\) = AcquireCredentialsHandle\(Principal, Package

, CredentialUse

, LogonID

, AuthData

\)
Creates a handle to credentials for use with SSPI

#### Parameters

  - Principal : str/unicode

    Use None for current security context

  - Package : str/unicode

    Name of security package that credentials will be used with

  - CredentialUse : int

    Intended use of requested credentials, SECPKG\_CRED\_INBOUND, SECPKG\_CRED\_OUTBOUND, or SECPKG\_CRED\_BOTH

  - LogonID : long

    LUID representing a logon session, can be None

  - AuthData : tuple

    Sequence of 3 strings: \(User, Domain, Password\) - use none for existing credentials

#### Return Value
Returns credential handle and credential's expiration time


## [win32security](win32security.md#win32security)\.AdjustTokenGroups

[PyTOKEN\_GROUPS](PyTOKEN.md#pytokengroups) = AdjustTokenGroups\(TokenHandle, ResetToDefault

, NewState

\)
Sets the groups associated to an access token\.

#### Parameters

  - TokenHandle : [PyHANDLE](PyHANDLE.md)

    The handle to access token to be modified

  - ResetToDefault : boolean

    Sets groups to default enabled/disabled states,

  - NewState : [PyTOKEN\_GROUPS](PyTOKEN.md#pytokengroups)

    Groups and attributes to be set for token

#### Comments

Accepts keyword args\.

#### Return Value
Returns previous state of groups modified


## [win32security](win32security.md#win32security)\.AdjustTokenPrivileges

[PyTOKEN\_PRIVILEGES](PyTOKEN.md#pytokenprivileges) = AdjustTokenPrivileges\(TokenHandle, bDisableAllPrivileges

, NewState

\)
Enables or disables privileges for an access token\.

#### Parameters

  - TokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token

  - bDisableAllPrivileges : int

    Flag for disabling all privileges

  - NewState : [PyTOKEN\_PRIVILEGES](PyTOKEN.md#pytokenprivileges)

    The new state, can be None if bDisableAllPrivileges is True

#### Comments

Accepts keyword args\.

#### Return Value
Returns modified privileges for later restoral\.  Privileges deleted from the token using 

SE\_PRIVILEGE\_REMOVED are not returned\.


## [win32security](win32security.md#win32security)\.AllocateLocallyUniqueId

AllocateLocallyUniqueId\(\)
Creates a new LUID


## AuditCategoryAccountLogon

const win32security\.AuditCategoryAccountLogon;




## AuditCategoryAccountManagement

const win32security\.AuditCategoryAccountManagement;




## AuditCategoryDetailedTracking

const win32security\.AuditCategoryDetailedTracking;




## AuditCategoryDirectoryServiceAccess

const win32security\.AuditCategoryDirectoryServiceAccess;




## AuditCategoryLogon

const win32security\.AuditCategoryLogon;




## AuditCategoryObjectAccess

const win32security\.AuditCategoryObjectAccess;




## AuditCategoryPolicyChange

const win32security\.AuditCategoryPolicyChange;




## AuditCategoryPrivilegeUse

const win32security\.AuditCategoryPrivilegeUse;




## AuditCategorySystem

const win32security\.AuditCategorySystem;




## CONTAINER\_INHERIT\_ACE

const win32security\.CONTAINER\_INHERIT\_ACE;




## [win32security](win32security.md#win32security)\.CheckTokenMembership

bool = CheckTokenMembership\(TokenHandle, SidToCheck

\)
Checks if a SID is enabled in a token

#### Parameters

  - TokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token, current process token used if None

  - SidToCheck : [PySID](PySID.md)

    Sid to be checked for presence in token


## [win32security](win32security.md#win32security)\.ConvertSecurityDescriptorToStringSecurityDescriptor

string = ConvertSecurityDescriptorToStringSecurityDescriptor\(SecurityDescriptor, RequestedStringSDRevision

, SecurityInformation

\)
Return string representation of a SECURITY\_DESCRIPTOR

#### Parameters

  - SecurityDescriptor : [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    PySECURITY\_DESCRIPTOR object

  - RequestedStringSDRevision : int

    Only SDDL\_REVISION\_1 currently valid

  - SecurityInformation : int

    Combination of bit flags from SECURITY\_INFORMATION enum


## [win32security](win32security.md#win32security)\.ConvertSidToStringSid

string = ConvertSidToStringSid\(Sid\)
Return string representation of a SID

#### Parameters

  - Sid : [PySID](PySID.md)

    PySID object


## [win32security](win32security.md#win32security)\.ConvertStringSecurityDescriptorToSecurityDescriptor

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = ConvertStringSecurityDescriptorToSecurityDescriptor\(StringSecurityDescriptor, StringSDRevision

\)
Turns string representation of a SECURITY\_DESCRIPTOR into the real thing

#### Parameters

  - StringSecurityDescriptor : string

    String representation of a SECURITY\_DESCRIPTOR

  - StringSDRevision : int

    Only SDDL\_REVISION\_1 currently valid


## [win32security](win32security.md#win32security)\.ConvertStringSidToSid

[PySID](PySID.md) = ConvertStringSidToSid\(StringSid\)
Creates a SID from a string representation

#### Parameters

  - StringSid : string

    String representation of a SID


## [win32security](win32security.md#win32security)\.CreateRestrictedToken

[PyHANDLE](PyHANDLE.md) = CreateRestrictedToken\(ExistingTokenHandle, Flags

, SidsToDisable

, PrivilegesToDelete

, SidsToRestrict

\)
Creates a restricted copy of an access token with reduced privs - requires win2K or higher

#### Parameters

  - ExistingTokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token \(see [win32security::LogonUser](win32security.md#win32securitylogonuser),[win32security::OpenProcessToken](win32security.md#win32securityopenprocesstoken)

  - Flags : int

    Valid values are zero or a combination of DISABLE\_MAX\_PRIVILEGE and SANDBOX\_INERT

  - SidsToDisable : \([PySID\_AND\_ATTRIBUTES](PySID.md#pysidand_attributes),\.\.\.\)

    Ssequence of [PySID\_AND\_ATTRIBUTES](PySID.md#pysidand_attributes) tuples, or None

  - PrivilegesToDelete : \([PyLUID\_AND\_ATTRIBUTES](PyLUID.md#pyluidand_attributes),\.\.\.\)

    Privilege LUIDS to remove from token \(attributes are ignored\), or None

  - SidsToRestrict : \([PySID\_AND\_ATTRIBUTES](PySID.md#pysidand_attributes),\.\.\.\)

    Sequence of [PySID\_AND\_ATTRIBUTES](PySID.md#pysidand_attributes) tuples \(attributes must be 0\)\.  Can be None\.


## [win32security](win32security.md#win32security)\.CreateWellKnownSid

[PySID](PySID.md) = CreateWellKnownSid\(WellKnownSidType, DomainSid

\)
Returns one of the predefined well known sids

#### Parameters

  - WellKnownSidType : int

    One of the Win\*Sid constants

  - DomainSid=None : [PySID](PySID.md)

    Domain for the new SID, or None for local machine


## [win32security](win32security.md#win32security)\.CryptEnumProviders

\[\([PyUnicode](PyUnicode.md),int\),\.\.\.\] = CryptEnumProviders\(\)
List cryptography providers

#### Return Value
Returns a sequence of tuples containing provider name and type


## DACL\_SECURITY\_INFORMATION

const win32security\.DACL\_SECURITY\_INFORMATION;

Indicates the discretionary ACL of the object is being referenced\.


## DENY\_ACCESS

const win32security\.DENY\_ACCESS;




## DISABLE\_MAX\_PRIVILEGE

const win32security\.DISABLE\_MAX\_PRIVILEGE;




## DS\_SPN\_ADD\_SPN\_OP

const win32security\.DS\_SPN\_ADD\_SPN\_OP;




## DS\_SPN\_DELETE\_SPN\_OP

const win32security\.DS\_SPN\_DELETE\_SPN\_OP;




## DS\_SPN\_DNS\_HOST

const win32security\.DS\_SPN\_DNS\_HOST;




## DS\_SPN\_DN\_HOST

const win32security\.DS\_SPN\_DN\_HOST;




## DS\_SPN\_DOMAIN

const win32security\.DS\_SPN\_DOMAIN;




## DS\_SPN\_NB\_DOMAIN

const win32security\.DS\_SPN\_NB\_DOMAIN;




## DS\_SPN\_NB\_HOST

const win32security\.DS\_SPN\_NB\_HOST;




## DS\_SPN\_REPLACE\_SPN\_OP

const win32security\.DS\_SPN\_REPLACE\_SPN\_OP;




## DS\_SPN\_SERVICE

const win32security\.DS\_SPN\_SERVICE;




## [win32security](win32security.md#win32security)\.DsBind

[PyDS\_HANDLE](PyDS.md#pydshandle) = DsBind\(DomainController, DnsDomainName

\)
Creates a connection to a directory service

#### Parameters

  - DomainController : [PyUnicode](PyUnicode.md)

    Name of domain controller to contact, can be None

  - DnsDomainName : [PyUnicode](PyUnicode.md)

    Dotted name of domain to bind to, can be None


## [win32security](win32security.md#win32security)\.DsCrackNames

\[ \(status, domain, name\) \] = DsCrackNames\(hds, flags

, formatOffered

, formatDesired

, names

\)
Converts an array of directory service object names from one format to another\.

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)

  - flags : int

    

  - formatOffered : int

    

  - formatDesired : int

    

  - names : \[name, \.\.\.\]

    


## [win32security](win32security.md#win32security)\.DsGetDcName

dict = DsGetDcName\(computerName, domainName

, domainGUID

, siteName

, flags

\)
Returns the name of a domain controller \(DC\) in a specified domain\. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics\.

#### Parameters

  - computerName=None : [PyUnicode](PyUnicode.md)

    

  - domainName=None : [PyUnicode](PyUnicode.md)

    

  - domainGUID=None : [PyIID](PyIID.md)

    

  - siteName=None : [PyUnicode](PyUnicode.md)

    

  - flags=0 : int

    

#### Comments

This function supports keyword arguments\.


## [win32security](win32security.md#win32security)\.DsGetSpn

\([PyUnicode](PyUnicode.md),\.\.\.\) = DsGetSpn\(ServiceType, ServiceClass

, ServiceName

, InstancePort

, InstanceNames

, InstancePorts

\)
Compose one or more service principal names to be registered using [win32security::DsWriteAccountSpn](win32security.md#win32securitydswriteaccountspn)

#### Parameters

  - ServiceType : int

    Type of Spn to create, one of the DS\_SPN\_\* constants

  - ServiceClass : [PyUnicode](PyUnicode.md)

    Arbitrary string that describes type of service, eg http

  - ServiceName : [PyUnicode](PyUnicode.md)

    Name of service, can be None \(not required for DS\_SPN\_\*\_HOST Spn's\)

  - InstancePort=0 : int

    Port nbr for service instance, use 0 for no port

  - InstanceNames=None : \([PyUnicode](PyUnicode.md),\.\.\.\)

    A sequence of service instance names, can be None - not required for for host Spn's

  - InstancePorts=None : \(int,\.\.\.\)

    A sequence of extra instance ports\.  If specified, must be same length as InstanceNames\.


## [win32security](win32security.md#win32security)\.DsListDomainsInSite

\[ [PyDS\_NAME\_RESULT\_ITEM](PyDS.md#pydsname_result_item), \.\.\.\] = DsListDomainsInSite\(hds\)

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)


## [win32security](win32security.md#win32security)\.DsListInfoForServer

\[ [PyDS\_NAME\_RESULT\_ITEM](PyDS.md#pydsname_result_item), \.\.\.\] = DsListInfoForServer\(hds, server

\)
Lists miscellaneous information for a server\.

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)

  - server : [PyUnicode](PyUnicode.md)

    


## [win32security](win32security.md#win32security)\.DsListRoles

\[ [PyDS\_NAME\_RESULT\_ITEM](PyDS.md#pydsname_result_item), \.\.\.\] = DsListRoles\(hds\)

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)


## [win32security](win32security.md#win32security)\.DsListServersInSite

\[ [PyDS\_NAME\_RESULT\_ITEM](PyDS.md#pydsname_result_item), \.\.\.\] = DsListServersInSite\(hds, site

\)

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)

  - site : [PyUnicode](PyUnicode.md)

    


## [win32security](win32security.md#win32security)\.DsListServersInSite

\[ [PyDS\_NAME\_RESULT\_ITEM](PyDS.md#pydsname_result_item), \.\.\.\] = DsListServersInSite\(hds, domain

, site

\)

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)

  - domain : [PyUnicode](PyUnicode.md)

    

  - site : [PyUnicode](PyUnicode.md)

    


## [win32security](win32security.md#win32security)\.DsListServersInSite

\[ [PyDS\_NAME\_RESULT\_ITEM](PyDS.md#pydsname_result_item), \.\.\.\] = DsListServersInSite\(hds\)

#### Parameters

  - hds : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by [win32security::DsBind](win32security.md#win32securitydsbind)


## [win32security](win32security.md#win32security)\.DsUnBind

DsUnBind\(hDS\)
Closes a directory services handle created by [win32security::DsBind](win32security.md#win32securitydsbind)

#### Parameters

  - hDS : [PyDS\_HANDLE](PyDS.md#pydshandle)

    A handle to a directory service as returned by [win32security::DsBind](win32security.md#win32securitydsbind)


## [win32security](win32security.md#win32security)\.DsWriteAccountSpn

DsWriteAccountSpn\(hDS, Operation, Account, Spns\)
Associates a set of service principal names with an account

#### Parameters

  - hDS : [PyDS\_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned from [win32security::DsBind](win32security.md#win32securitydsbind)

  - Operation : int

    Constant from DS\_SPN\_WRITE\_OP enum

  - Account : [PyUnicode](PyUnicode.md)

    Distinguished name of account whose Spn's will be modified

  - Spns : \([PyUnicode](PyUnicode.md),\.\.\.\)

    A sequence of target Spn's as returned by [win32security::DsGetSpn](win32security.md#win32securitydsgetspn)


## [win32security](win32security.md#win32security)\.DuplicateToken

[PyHANDLE](PyHANDLE.md) = DuplicateToken\(ExistingTokenHandle, ImpersonationLevel

\)
Creates a copy of an access token with specified impersonation level

#### Parameters

  - ExistingTokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token \(see [win32security::LogonUser](win32security.md#win32securitylogonuser),[win32security::OpenProcessToken](win32security.md#win32securityopenprocesstoken)\)

  - ImpersonationLevel : int

    A value from SECURITY\_IMPERSONATION\_LEVEL enum


## [win32security](win32security.md#win32security)\.DuplicateTokenEx

[PyHANDLE](PyHANDLE.md) = DuplicateTokenEx\(ExistingToken, ImpersonationLevel

, DesiredAccess

, TokenType

, TokenAttributes

\)
Extended version of DuplicateToken\.

#### Parameters

  - ExistingToken : [PyHANDLE](PyHANDLE.md)

    Logon token opened with TOKEN\_DUPLICATE access

  - ImpersonationLevel : int

    One of win32security\.Security\* values

  - DesiredAccess : int

    Type of access required for the handle, combination of win32security\.TOKEN\_\* flags

  - TokenType : int

    Type of token to be created, TokenPrimary or TokenImpersonation

  - TokenAttributes=None : [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security and inheritance for the new handle\.  None results in default DACL and no inheritance,

#### Comments

Accepts keyword arguments


## [win32security](win32security.md#win32security)\.EnumerateSecurityPackages

\(dict,\.\.\.\) = EnumerateSecurityPackages\(\)
List available security packages as a sequence of dictionaries representing SecPkgInfo structures


## FAILED\_ACCESS\_ACE\_FLAG

const win32security\.FAILED\_ACCESS\_ACE\_FLAG;




## GRANT\_ACCESS

const win32security\.GRANT\_ACCESS;




## GROUP\_SECURITY\_INFORMATION

const win32security\.GROUP\_SECURITY\_INFORMATION;

Indicates the primary group identifier of the object is being referenced\.


## [win32security](win32security.md#win32security)\.GetBinarySid

[PySID](PySID.md) = GetBinarySid\(SID\)
Accepts a SID string \(eg: S-1-5-32-544\) and returns the SID as a PySID object\.

#### Parameters

  - SID : string

    Textual representation of a SID\. Textual SID example: S-1-5-32-544


## [win32security](win32security.md#win32security)\.GetFileSecurity

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = GetFileSecurity\(filename, info

\)
Obtains specified information about the security of a file or directory\. The information obtained is constrained by the caller's access rights and privileges\.

#### Parameters

  - filename : string

    The name of the file

  - info=OWNER\_SECURITY\_INFORMATION | GROUP\_SECURITY\_INFORMATION | DACL\_SECURITY\_INFORMATION | SACL\_SECURITY\_INFORMATION : int

    Flags that specify the information requested\.

#### Comments

This function reportedly will not return the INHERITED\_ACE flag on some Windows XP SP1 systems 

Use GetNamedSecurityInfo if you encounter this problem\.


## [win32security](win32security.md#win32security)\.GetKernelObjectSecurity

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = GetKernelObjectSecurity\(handle, info

\)
Obtains specified information about the security of a kernel object\. The information obtained is constrained by the caller's access rights and privileges\.

#### Parameters

  - handle : [PyHANDLE](PyHANDLE.md)

    The handle to the object

  - info=OWNER\_SECURITY\_INFORMATION | GROUP\_SECURITY\_INFORMATION | DACL\_SECURITY\_INFORMATION | SACL\_SECURITY\_INFORMATION : int

    Flags that specify the information requested\.


## [win32security](win32security.md#win32security)\.GetNamedSecurityInfo

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = GetNamedSecurityInfo\(ObjectName, ObjectType

, SecurityInfo

\)
Retrieve security info for an object by name

#### Parameters

  - ObjectName : str/unicode

    Name of object

  - ObjectType : int

    Value from SE\_OBJECT\_TYPE enum

  - SecurityInfo : int

    Combination of SECURITY\_INFORMATION constants

#### Comments

Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from 

the returned PySECURITY\_DESCRIPTOR


## [win32security](win32security.md#win32security)\.GetSecurityInfo

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = GetSecurityInfo\(handle, ObjectType

, SecurityInfo

\)
Retrieve security info for an object by handle

#### Parameters

  - handle : int/[PyHANDLE](PyHANDLE.md)

    Handle to object

  - ObjectType : int

    Value from SE\_OBJECT\_TYPE enum

  - SecurityInfo : int

    Combination of SECURITY\_INFORMATION constants

#### Comments

Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from 

the returned PySECURITY\_DESCRIPTOR


## [win32security](win32security.md#win32security)\.GetTokenInformation

object = GetTokenInformation\(TokenHandle, TokenInformationClass

\)
Retrieves a specified type of information about an access token\. The calling process must have appropriate access rights to obtain the information\.

#### Parameters

  - TokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token\.

  - TokenInformationClass : int

    Specifies a value from the TOKEN\_INFORMATION\_CLASS enumerated type identifying the type of information the function retrieves\.

#### Return Value
The following types are supported




## [win32security](win32security.md#win32security)\.GetUserObjectSecurity

[PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) = GetUserObjectSecurity\(handle, info

\)
Obtains specified information about the security of a user object\. The information obtained is constrained by the caller's access rights and privileges\.

#### Parameters

  - handle : [PyHANDLE](PyHANDLE.md)

    The handle to the object

  - info=OWNER\_SECURITY\_INFORMATION | GROUP\_SECURITY\_INFORMATION | DACL\_SECURITY\_INFORMATION | SACL\_SECURITY\_INFORMATION : int

    Flags that specify the information requested\.


## INHERITED\_ACE

const win32security\.INHERITED\_ACE;




## INHERIT\_ONLY\_ACE

const win32security\.INHERIT\_ONLY\_ACE;




## [win32security](win32security.md#win32security)\.ImpersonateAnonymousToken

ImpersonateAnonymousToken\(ThreadHandle\)
Cause a thread to act in the security context of an anonymous token

#### Parameters

  - ThreadHandle : [PyHANDLE](PyHANDLE.md)

    Handle to thread that will


## [win32security](win32security.md#win32security)\.ImpersonateLoggedOnUser

ImpersonateLoggedOnUser\(handle\)
Impersonates a logged on user\.

#### Parameters

  - handle : [PyHANDLE](PyHANDLE.md)

    Handle to a token that represents a logged-on user


## [win32security](win32security.md#win32security)\.ImpersonateNamedPipeClient

ImpersonateNamedPipeClient\(handle\)
Impersonates a named-pipe client application\.

#### Parameters

  - handle : int

    handle of a named pipe\.


## [win32security](win32security.md#win32security)\.ImpersonateSelf

ImpersonateSelf\(ImpersonationLevel\)
Assigns an impersonation token for current security context to current process

#### Parameters

  - ImpersonationLevel : int

    A value from SECURITY\_IMPERSONATION\_LEVEL enum


## [win32security](win32security.md#win32security)\.InitializeSecurityContext

\(int, int, [PyTime](PyTime.md)\) = InitializeSecurityContext\(Credential, Context

, TargetName

, ContextReq

, TargetDataRep

, pInput

, NewContext

, pOutput

\)
Creates a security context based on credentials created by AcquireCredentialsHandle

#### Parameters

  - Credential : [PyCredHandle](PyCredHandle.md)

    A credentials handle as returned by [win32security::AcquireCredentialsHandle](win32security.md#win32securityacquirecredentialshandle)

  - Context : [PyCtxtHandle](PyCtxtHandle.md)

    Use None on initial call, then handle returned in NewContext thereafter

  - TargetName : str/unicode

    Target of context, security package specific - Use None with NTLM

  - ContextReq : int

    Combination of ISC\_REQ\_\* flags

  - TargetDataRep : int

    One of SECURITY\_NATIVE\_DREP,SECURITY\_NETWORK\_DREP

  - pInput : [PySecBufferDesc](PySecBufferDesc.md)

    Data buffer - use None initially

  - NewContext : [PyCtxtHandle](PyCtxtHandle.md)

    Uninitialized context handle to receive output

  - pOutput : [PySecBufferDesc](PySecBufferDesc.md)

    Buffer that receives output data for subsequent calls

#### Return Value
Return value is a tuple of \(return code, attribute flags, expiration time\)


## [win32security](win32security.md#win32security)\.IsTokenRestricted

bool = IsTokenRestricted\(TokenHandle\)
Checks if a token contains restricted sids

#### Parameters

  - TokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token


## LABEL\_SECURITY\_INFORMATION

const win32security\.LABEL\_SECURITY\_INFORMATION;




## LOGON32\_LOGON\_BATCH

const win32security\.LOGON32\_LOGON\_BATCH;

This logon type is intended for batch servers, where processes may be executing on behalf of a user without their direct intervention; or for higher performance servers that process many clear-text authentication attempts at a time, such as mail or web servers\. LogonUser does not cache credentials for this logon type\.


## LOGON32\_LOGON\_INTERACTIVE

const win32security\.LOGON32\_LOGON\_INTERACTIVE;

This logon type is intended for users who will be interactively using the machine, such as a user being logged on by a terminal server, remote shell, or similar process\. This logon type has the additional expense of caching logon information for disconnected operation, and is therefore inappropriate for some client/server applications, such as a mail server\.


## LOGON32\_LOGON\_NETWORK

const win32security\.LOGON32\_LOGON\_NETWORK;

This logon type is intended for high performance servers to authenticate clear text passwords\. LogonUser does not cache credentials for this logon type\. This is the fastest logon path, but there are two limitations\. First, the function returns an impersonation token, not a primary token\. You cannot use this token directly in the CreateProcessAsUser function\. However, you can call the DuplicateTokenEx function to convert the token to a primary token, and then use it in CreateProcessAsUser\. Second, if you convert the token to a primary token and use it in CreateProcessAsUser to start a process, the new process will not be able to access other network resources, such as remote servers or printers, through the redirector\.


## LOGON32\_LOGON\_NETWORK\_CLEARTEXT

const win32security\.LOGON32\_LOGON\_NETWORK\_CLEARTEXT;




## LOGON32\_LOGON\_NEW\_CREDENTIALS

const win32security\.LOGON32\_LOGON\_NEW\_CREDENTIALS;




## LOGON32\_LOGON\_SERVICE

const win32security\.LOGON32\_LOGON\_SERVICE;

Indicates a service-type logon\. The account provided must have the service privilege enabled\.


## LOGON32\_LOGON\_UNLOCK

const win32security\.LOGON32\_LOGON\_UNLOCK;




## LOGON32\_PROVIDER\_DEFAULT

const win32security\.LOGON32\_PROVIDER\_DEFAULT;

Use the standard logon provider for the system\. This is the recommended value for the dwLogonProvider parameter\. It provides maximum compatibility with current and future releases of Windows NT\.


## LOGON32\_PROVIDER\_WINNT35

const win32security\.LOGON32\_PROVIDER\_WINNT35;

Use the Windows NT 3\.5 logon provider\.


## LOGON32\_PROVIDER\_WINNT40

const win32security\.LOGON32\_PROVIDER\_WINNT40;

Use the Windows NT 4\.0 logon provider


## LOGON32\_PROVIDER\_WINNT50

const win32security\.LOGON32\_PROVIDER\_WINNT50;

Use the Negotiate protocol


## [win32security](win32security.md#win32security)\.LogonUser

[PyHANDLE](PyHANDLE.md) = LogonUser\(Username, Domain

, Password

, LogonType

, LogonProvider

\)
Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called\. You cannot use LogonUser to log on to a remote computer\.

#### Parameters

  - Username : [PyUnicode](PyUnicode.md)

    The name of the user account to log on to\. 

This may also be a marshalled credential \(see [win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)\)\.

  - Domain : [PyUnicode](PyUnicode.md)

    The name of the domain, or None for the current domain

  - Password : [PyUnicode](PyUnicode.md)

    User's password\.  Use a blank string if Username contains a marshalled credential\.

  - LogonType : int

    One of LOGON32\_LOGON\_\* values

  - LogonProvider : int

    One of LOGON32\_PROVIDER\_\* values

#### Comments

Accepts keyword args

On Windows 2000 and earlier, the calling process must have SE\_TCB\_NAME privilege\.


## [win32security](win32security.md#win32security)\.LogonUserEx

\([PyHANDLE](PyHANDLE.md), [PySID](PySID.md), str, dict\) = LogonUserEx\(Username, Domain

, Password

, LogonType

, LogonProvider

\)
Log a user onto the local machine,

#### Parameters

  - Username : [PyUnicode](PyUnicode.md)

    User account, may be specified as a UPN \(user@domain\.com\)\. 

This may also be a marshalled credential \(see [win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)\)\.

  - Domain : [PyUnicode](PyUnicode.md)

    User's domain\. Can be None if Username is a full UPN\.

  - Password : [PyUnicode](PyUnicode.md)

    User's password\.  Use a blank string if Username contains a marshalled credential\.

  - LogonType : int

    One of LOGON32\_LOGON\_\* values

  - LogonProvider : int

    One of LOGON32\_PROVIDER\_\* values

#### Comments

Requires Windows XP or later

Accepts keyword args

#### Return Value
Returns access token, logon sid, profile buffer, and process quotas\. 

Format of the profile buffer is not known, so returned object is subject to change\.


## [win32security](win32security.md#win32security)\.LookupAccountName

[PySID](PySID.md), string, int = LookupAccountName\(systemName, accountName

\)
Accepts the name of a system and an account as input\. It retrieves a security identifier \(SID\) for the account and the name of the domain on which the account was found\.

#### Parameters

  - systemName : string

    The system name, or None

  - accountName : string

    The account name

#### Return Value
The result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for\.


## [win32security](win32security.md#win32security)\.LookupAccountSid

string, string, int = LookupAccountSid\(systemName, sid

\)
Accepts a security identifier \(SID\) as input\. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found\.

#### Parameters

  - systemName : string

    The system name, or None

  - sid : [PySID](PySID.md)

    The SID

#### Return Value
The result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for\.


## [win32security](win32security.md#win32security)\.LookupPrivilegeDisplayName

[PyUnicode](PyUnicode.md) = LookupPrivilegeDisplayName\(SystemName, Name

\)
Returns long description for a privilege name

#### Parameters

  - SystemName : string/[PyUnicode](PyUnicode.md)

    System name, local system assumed if not specified

  - Name : string/[PyUnicode](PyUnicode.md)

    Name of privilege, Se\.\.\.Privilege string constants \(win32security\.SE\_\*\_NAME\)


## [win32security](win32security.md#win32security)\.LookupPrivilegeName

[PyUnicode](PyUnicode.md) = LookupPrivilegeName\(SystemName, luid

\)
return the text name for a privilege LUID

#### Parameters

  - SystemName : string/[PyUnicode](PyUnicode.md)

    System name, local system assumed if not specified

  - luid : LARGE\_INTEGER

    64 bit value representing a privilege


## [win32security](win32security.md#win32security)\.LookupPrivilegeValue

[LARGE\_INTEGER](LARGE.md#largeinteger) = LookupPrivilegeValue\(systemName, privilegeName

\)
Retrieves the locally unique id for a privilege name

#### Parameters

  - systemName : string

    String specifying the system, use None for local machine

  - privilegeName : string

    String specifying the privilege \(win32security\.SE\_\*\_NAME\)


## [win32security](win32security.md#win32security)\.LsaAddAccountRights

LsaAddAccountRights\(PolicyHandle, AccountSid, UserRights\)
Adds a list of privileges to an account

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - AccountSid : [PySID](PySID.md)

    Account to which privs will be added

  - UserRights : \(str/unicode,\.\.\.\)

    Sequence of privilege names \(SE\_\*\_NAME unicode constants\)

#### Comments

Account is created if it doesn't already exist\.

Accepts keyword args\.


## [win32security](win32security.md#win32security)\.LsaCallAuthenticationPackage

LsaCallAuthenticationPackage\(LsaHandle, AuthenticationPackage, MessageType, ProtocolSubmitBuffer\)
Requests the services of an authentication package

#### Parameters

  - LsaHandle : [PyLsaLogon\_HANDLE](PyLsaLogon.md#pylsalogonhandle)

    Lsa handle as returned by [win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess) or [win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted)

  - AuthenticationPackage : int

    Id of authentication package to call, as returned by [win32security::LsaLookupAuthenticationPackage](win32security.md#win32securitylsalookupauthenticationpackage)

  - MessageType : int

    Type of request that is being made, Kerb\*Message or MsV1\_0\* constant

  - ProtocolSubmitBuffer : object

    Type is dependent on MessageType

#### Comments

Message type is embedded in different types of submit buffers in the API call, but passed separately 

from python for simplicity of parsing input

   

       MessageType

   

   

       Input type

   

KerbQueryTicketCacheMessagelong - a logon id, use 0 for current logon session

KerbRetrieveTicketMessagelong - a logon id, use 0 for current logon session

KerbPurgeTicketCacheMessage\(long, [PyUnicode](PyUnicode.md), [PyUnicode](PyUnicode.md)\) - tuple containing \(LogonId, ServerName, RealmName\)

KerbRetrieveEncodedTicketMessage\(LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle\) 

\(int, [PyUnicode](PyUnicode.md), int, int, int, [PyCredHandle](PyCredHandle.md)\)

   

       MessageType

   

   

       Return type

   

KerbQueryTicketCacheMessage\(dict,\.\.\.\) - Returns all tickets for the specified logon session \(form is KERB\_TICKET\_CACHE\_INFO\)

KerbPurgeTicketCacheMessageNone

KerbRetrieveTicketMessageReturns the ticket granting ticket for the logon session as a KERB\_EXTERNAL\_TICKET

KerbRetrieveEncodedTicketMessageReturns specified ticket as a KERB\_EXTERNAL\_TICKET

#### Return Value
Type of returned object is dependent on MessageType


## [win32security](win32security.md#win32security)\.LsaClose

LsaClose\(PolicyHandle\)
Closes a policy handle created by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

#### Parameters

  - PolicyHandle : [PyHANDLE](PyHANDLE.md)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)


## [win32security](win32security.md#win32security)\.LsaConnectUntrusted

[PyLsaLogon\_HANDLE](PyLsaLogon.md#pylsalogonhandle) = LsaConnectUntrusted\(\)
Creates untrusted connection to LSA

#### Comments

You don't need SeTcbPrivilege to execute this function as you do with 

LsaRegisterLogonProcess, but functionality of handle is limited


## [win32security](win32security.md#win32security)\.LsaDeregisterLogonProcess

LsaDeregisterLogonProcess\(LsaHandle\)
Closes connection to LSA server

#### Parameters

  - LsaHandle : [PyLsaLogon\_HANDLE](PyLsaLogon.md#pylsalogonhandle)

    An Lsa handle as returned by [win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted) or [win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess)


## [win32security](win32security.md#win32security)\.LsaEnumerateAccountRights

\[[PyUnicode](PyUnicode.md), \.\.\.\] = LsaEnumerateAccountRights\(PolicyHandle, AccountSid

\)
Lists privileges held by SID

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - AccountSid : [PySID](PySID.md)

    Security identifier of account for which to list privs


## [win32security](win32security.md#win32security)\.LsaEnumerateAccountsWithUserRight

\([PySID](PySID.md),\.\.\.\) = LsaEnumerateAccountsWithUserRight\(PolicyHandle, UserRight

\)
Return SIDs that hold specified priv

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - UserRight : str/unicode

    Name of privilege \(SE\_\*\_NAME unicode constant\)


## [win32security](win32security.md#win32security)\.LsaEnumerateLogonSessions

\(long,\.\.\.\) = LsaEnumerateLogonSessions\(\)
Lists all current logon ids


## [win32security](win32security.md#win32security)\.LsaGetLogonSessionData

\(dict,\.\.\.\) = LsaGetLogonSessionData\(LogonId\)
Returns information about a logon session

#### Parameters

  - LogonId : PyLARGE\_INTEGER

    An LUID identifying a logon session

#### Return Value
Returns a dictionary representing a SECURITY\_LOGON\_SESSION\_DATA structure


## [win32security](win32security.md#win32security)\.LsaLookupAuthenticationPackage

int = LsaLookupAuthenticationPackage\(LsaHandle, PackageName

\)
Retrieves the unique id for an authentication package

#### Parameters

  - LsaHandle : [PyLsaLogon\_HANDLE](PyLsaLogon.md#pylsalogonhandle)

    An Lsa handle as returned by [win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted) or [win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess)

  - PackageName : string

    Name of security package to be identified


## [win32security](win32security.md#win32security)\.LsaOpenPolicy

[PyLSA\_HANDLE](PyLSA.md#pylsahandle) = LsaOpenPolicy\(system\_name, access\_mask

\)
Opens a policy handle for the specified system

#### Parameters

  - system\_name : string/[PyUnicode](PyUnicode.md)

    System name, local system assumed if not specified

  - access\_mask : int

    Bitmask of requested access types


## [win32security](win32security.md#win32security)\.LsaQueryInformationPolicy

LsaQueryInformationPolicy\(PolicyHandle, InformationClass\)
Retrieves information from the policy handle

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - InformationClass : int

    POLICY\_INFORMATION\_CLASS value



## [win32security](win32security.md#win32security)\.LsaRegisterLogonProcess

[PyLsaLogon\_HANDLE](PyLsaLogon.md#pylsalogonhandle) = LsaRegisterLogonProcess\(LogonProcessName\)
Creates a trusted connection to LSA

#### Parameters

  - LogonProcessName : string

    Name to use for this logon process

#### Comments

Requires SeTcbPrivilege \(and must be enabled\)


## [win32security](win32security.md#win32security)\.LsaRegisterPolicyChangeNotification

LsaRegisterPolicyChangeNotification\(InformationClass, NotificationEventHandle\)
Register an event handle to receive policy change events

#### Parameters

  - InformationClass : int

    One of POLICY\_NOTIFICATION\_INFORMATION\_CLASS contants

  - NotificationEventHandle : [PyHANDLE](PyHANDLE.md)

    Event handle to receives notification


## [win32security](win32security.md#win32security)\.LsaRemoveAccountRights

LsaRemoveAccountRights\(PolicyHandle, AccountSid, AllRights, UserRights\)
Removes privs from an account

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - AccountSid : [PySID](PySID.md)

    Account whose privileges will be removed

  - AllRights : int

    Boolean value indicating if all privs should be removed from account

  - UserRights : \(str/unicode,\.\.\.\)

    List of privilege names to be removed \(SE\_\*\_NAME unicode constants\)

#### Comments

If AllRights parm is true, account is \*deleted\*

Accepts keyword args\.


## [win32security](win32security.md#win32security)\.LsaRetrievePrivateData

[PyUnicode](PyUnicode.md) = LsaRetrievePrivateData\(PolicyHandle, KeyName

\)
Retreives encrypted unicode data from Lsa registry key\.

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - KeyName : string

    Registry key to read


## [win32security](win32security.md#win32security)\.LsaSetInformationPolicy

LsaSetInformationPolicy\(PolicyHandle, InformationClass, Information\)
Sets policy options

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - InformationClass : int

    POLICY\_INFORMATION\_CLASS value

  - Information : object

    Type is dependent on InformationClass

   

       InformationClass

   

   

       Type of input expected

   

PolicyAuditEventsInformation\(boolean, \(int, \.\.\.\)\) 

First member imdicates whether auditing is enabled or not\. 




## [win32security](win32security.md#win32security)\.LsaStorePrivateData

LsaStorePrivateData\(PolicyHandle, KeyName, PrivateData\)
Stores encrypted unicode data under specified Lsa registry key\. Returns None on success

#### Parameters

  - PolicyHandle : [PyLSA\_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by [win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  - KeyName : string

    Registry key in which to store data

  - PrivateData : [PyUNICODE](PyUNICODE.md)

    Unicode string to be encrypted and stored


## [win32security](win32security.md#win32security)\.LsaUnregisterPolicyChangeNotification

LsaUnregisterPolicyChangeNotification\(InformationClass, NotificationEventHandle\)
Stop receiving policy change notification

#### Parameters

  - InformationClass : int

    POLICY\_NOTIFICATION\_INFORMATION\_CLASS constant

  - NotificationEventHandle : [PyHANDLE](PyHANDLE.md)

    Event handle previously registered to receive policy change events


## [win32security](win32security.md#win32security)\.MapGenericMask

int = MapGenericMask\(AccessMask, GenericMapping

\)
Translates generic access rights into specific rights

#### Parameters

  - AccessMask : int

    A bitmask of generic rights to be interpreted according to GenericMapping

  - GenericMapping : \(int,int,int,int\)

    A tuple of 4 bitmasks \(GenericRead, GenericWrite, GenericExecute, GenericAll\) 

containing the standard and specific rights that correspond to the generic rights\.

#### Return Value
The input AccessMask will be returned with any generic access rights translated into specific equivalents


## NOT\_USED\_ACCESS

const win32security\.NOT\_USED\_ACCESS;




## NO\_INHERITANCE

const win32security\.NO\_INHERITANCE;




## NO\_PROPAGATE\_INHERIT\_ACE

const win32security\.NO\_PROPAGATE\_INHERIT\_ACE;




## OBJECT\_INHERIT\_ACE

const win32security\.OBJECT\_INHERIT\_ACE;




## OWNER\_SECURITY\_INFORMATION

const win32security\.OWNER\_SECURITY\_INFORMATION;

Indicates the owner identifier of the object is being referenced\.


## [win32security](win32security.md#win32security)\.OpenProcessToken

[PyHANDLE](PyHANDLE.md) = OpenProcessToken\(processHandle, desiredAccess

\)
Opens the access token associated with a process\.

#### Parameters

  - processHandle : int

    The handle of the process to open\.

  - desiredAccess : int

    Desired access to process


## [win32security](win32security.md#win32security)\.OpenThreadToken

[PyHandle](PyHandle.md) = OpenThreadToken\(handle, desiredAccess

, openAsSelf

\)
Opens the access token associated with a thread\.

#### Parameters

  - handle : [PyHANDLE](PyHANDLE.md)

    handle to thread

  - desiredAccess : int

    access to process

  - openAsSelf : int

    Flag for process or thread security


## POLICY\_ALL\_ACCESS

const win32security\.POLICY\_ALL\_ACCESS;




## POLICY\_AUDIT\_EVENT\_FAILURE

const win32security\.POLICY\_AUDIT\_EVENT\_FAILURE;

Generate audit records for failed attempts to cause an event of this type to occur\.


## POLICY\_AUDIT\_EVENT\_NONE

const win32security\.POLICY\_AUDIT\_EVENT\_NONE;

Do not generate audit records for events of this type\.


## POLICY\_AUDIT\_EVENT\_SUCCESS

const win32security\.POLICY\_AUDIT\_EVENT\_SUCCESS;

Generate audit records for successful events of this type\.


## POLICY\_AUDIT\_EVENT\_UNCHANGED

const win32security\.POLICY\_AUDIT\_EVENT\_UNCHANGED;

For set operations, specify this value to leave the current options unchanged\. This is the default\.


## POLICY\_AUDIT\_LOG\_ADMIN

const win32security\.POLICY\_AUDIT\_LOG\_ADMIN;




## POLICY\_CREATE\_ACCOUNT

const win32security\.POLICY\_CREATE\_ACCOUNT;




## POLICY\_CREATE\_PRIVILEGE

const win32security\.POLICY\_CREATE\_PRIVILEGE;




## POLICY\_CREATE\_SECRET

const win32security\.POLICY\_CREATE\_SECRET;




## POLICY\_EXECUTE

const win32security\.POLICY\_EXECUTE;




## POLICY\_GET\_PRIVATE\_INFORMATION

const win32security\.POLICY\_GET\_PRIVATE\_INFORMATION;




## POLICY\_LOOKUP\_NAMES

const win32security\.POLICY\_LOOKUP\_NAMES;




## POLICY\_NOTIFICATION

const win32security\.POLICY\_NOTIFICATION;




## POLICY\_READ

const win32security\.POLICY\_READ;




## POLICY\_SERVER\_ADMIN

const win32security\.POLICY\_SERVER\_ADMIN;




## POLICY\_SET\_AUDIT\_REQUIREMENTS

const win32security\.POLICY\_SET\_AUDIT\_REQUIREMENTS;




## POLICY\_SET\_DEFAULT\_QUOTA\_LIMITS

const win32security\.POLICY\_SET\_DEFAULT\_QUOTA\_LIMITS;




## POLICY\_TRUST\_ADMIN

const win32security\.POLICY\_TRUST\_ADMIN;




## POLICY\_VIEW\_AUDIT\_INFORMATION

const win32security\.POLICY\_VIEW\_AUDIT\_INFORMATION;




## POLICY\_VIEW\_LOCAL\_INFORMATION

const win32security\.POLICY\_VIEW\_LOCAL\_INFORMATION;




## POLICY\_WRITE

const win32security\.POLICY\_WRITE;




## PROTECTED\_DACL\_SECURITY\_INFORMATION

const win32security\.PROTECTED\_DACL\_SECURITY\_INFORMATION;




## PROTECTED\_SACL\_SECURITY\_INFORMATION

const win32security\.PROTECTED\_SACL\_SECURITY\_INFORMATION;




## PolicyAccountDomainInformation

const win32security\.PolicyAccountDomainInformation;




## PolicyAuditEventsInformation

const win32security\.PolicyAuditEventsInformation;




## PolicyAuditFullQueryInformation

const win32security\.PolicyAuditFullQueryInformation;




## PolicyAuditFullSetInformation

const win32security\.PolicyAuditFullSetInformation;




## PolicyAuditLogInformation

const win32security\.PolicyAuditLogInformation;




## PolicyDefaultQuotaInformation

const win32security\.PolicyDefaultQuotaInformation;




## PolicyDnsDomainInformation

const win32security\.PolicyDnsDomainInformation;




## PolicyLsaServerRoleInformation

const win32security\.PolicyLsaServerRoleInformation;




## PolicyModificationInformation

const win32security\.PolicyModificationInformation;




## PolicyNotifyAccountDomainInformation

const win32security\.PolicyNotifyAccountDomainInformation;




## PolicyNotifyAuditEventsInformation

const win32security\.PolicyNotifyAuditEventsInformation;




## PolicyNotifyDnsDomainInformation

const win32security\.PolicyNotifyDnsDomainInformation;




## PolicyNotifyDomainEfsInformation

const win32security\.PolicyNotifyDomainEfsInformation;




## PolicyNotifyDomainKerberosTicketInformation

const win32security\.PolicyNotifyDomainKerberosTicketInformation;




## PolicyNotifyMachineAccountPasswordInformation

const win32security\.PolicyNotifyMachineAccountPasswordInformation;




## PolicyNotifyServerRoleInformation

const win32security\.PolicyNotifyServerRoleInformation;




## PolicyPdAccountInformation

const win32security\.PolicyPdAccountInformation;




## PolicyPrimaryDomainInformation

const win32security\.PolicyPrimaryDomainInformation;




## PolicyReplicaSourceInformation

const win32security\.PolicyReplicaSourceInformation;




## PolicyServerDisabled

const win32security\.PolicyServerDisabled;




## PolicyServerDisabled

const win32security\.PolicyServerDisabled;




## PolicyServerEnabled

const win32security\.PolicyServerEnabled;




## PolicyServerEnabled

const win32security\.PolicyServerEnabled;




## PolicyServerRoleBackup

const win32security\.PolicyServerRoleBackup;




## PolicyServerRolePrimary

const win32security\.PolicyServerRolePrimary;




## [win32security](win32security.md#win32security)\.QuerySecurityPackageInfo

dict = QuerySecurityPackageInfo\(PackageName\)
Retrieves parameters for a security package

#### Parameters

  - PackageName : [PyUNICODE](PyUNICODE.md)

    Name of the security package to query

#### Return Value
Returns a dictionary representing a SecPkgInfo struct


## REVOKE\_ACCESS

const win32security\.REVOKE\_ACCESS;




## [win32security](win32security.md#win32security)\.RevertToSelf

RevertToSelf\(\)
Terminates the impersonation of a client application\.


## SACL\_SECURITY\_INFORMATION

const win32security\.SACL\_SECURITY\_INFORMATION;

Indicates the system ACL of the object is being referenced\.


## SANDBOX\_INERT

const win32security\.SANDBOX\_INERT;




## SDDL\_REVISION\_1

const win32security\.SDDL\_REVISION\_1;




## SECPKG\_CRED\_BOTH

const win32security\.SECPKG\_CRED\_BOTH;




## SECPKG\_CRED\_INBOUND

const win32security\.SECPKG\_CRED\_INBOUND;




## SECPKG\_CRED\_OUTBOUND

const win32security\.SECPKG\_CRED\_OUTBOUND;




## SECPKG\_FLAG\_ACCEPT\_WIN32\_NAME

const win32security\.SECPKG\_FLAG\_ACCEPT\_WIN32\_NAME;




## SECPKG\_FLAG\_CLIENT\_ONLY

const win32security\.SECPKG\_FLAG\_CLIENT\_ONLY;




## SECPKG\_FLAG\_CONNECTION

const win32security\.SECPKG\_FLAG\_CONNECTION;




## SECPKG\_FLAG\_DATAGRAM

const win32security\.SECPKG\_FLAG\_DATAGRAM;




## SECPKG\_FLAG\_EXTENDED\_ERROR

const win32security\.SECPKG\_FLAG\_EXTENDED\_ERROR;




## SECPKG\_FLAG\_IMPERSONATION

const win32security\.SECPKG\_FLAG\_IMPERSONATION;




## SECPKG\_FLAG\_INTEGRITY

const win32security\.SECPKG\_FLAG\_INTEGRITY;




## SECPKG\_FLAG\_MULTI\_REQUIRED

const win32security\.SECPKG\_FLAG\_MULTI\_REQUIRED;




## SECPKG\_FLAG\_PRIVACY

const win32security\.SECPKG\_FLAG\_PRIVACY;




## SECPKG\_FLAG\_STREAM

const win32security\.SECPKG\_FLAG\_STREAM;




## SECPKG\_FLAG\_TOKEN\_ONLY

const win32security\.SECPKG\_FLAG\_TOKEN\_ONLY;




## [win32security](win32security.md#win32security)\.SECURITY\_ATTRIBUTES

PySECURITY\_ATTRIBUTES = SECURITY\_ATTRIBUTES\(\)
Creates a new [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes) object\.


## SECURITY\_CREATOR\_SID\_AUTHORITY

const win32security\.SECURITY\_CREATOR\_SID\_AUTHORITY;




## [win32security](win32security.md#win32security)\.SECURITY\_DESCRIPTOR

PySECURITY\_DESCRIPTOR = SECURITY\_DESCRIPTOR\(\)
Creates a new [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) object\.


## SECURITY\_LOCAL\_SID\_AUTHORITY

const win32security\.SECURITY\_LOCAL\_SID\_AUTHORITY;




## SECURITY\_NON\_UNIQUE\_AUTHORITY

const win32security\.SECURITY\_NON\_UNIQUE\_AUTHORITY;




## SECURITY\_NT\_AUTHORITY

const win32security\.SECURITY\_NT\_AUTHORITY;




## SECURITY\_NULL\_SID\_AUTHORITY

const win32security\.SECURITY\_NULL\_SID\_AUTHORITY;




## SECURITY\_RESOURCE\_MANAGER\_AUTHORITY

const win32security\.SECURITY\_RESOURCE\_MANAGER\_AUTHORITY;




## SECURITY\_WORLD\_SID\_AUTHORITY

const win32security\.SECURITY\_WORLD\_SID\_AUTHORITY;




## SET\_ACCESS

const win32security\.SET\_ACCESS;




## SET\_AUDIT\_FAILURE

const win32security\.SET\_AUDIT\_FAILURE;




## SET\_AUDIT\_SUCCESS

const win32security\.SET\_AUDIT\_SUCCESS;




## SE\_DACL\_AUTO\_INHERITED

const win32security\.SE\_DACL\_AUTO\_INHERITED;

win2k and up


## SE\_DACL\_DEFAULTED

const win32security\.SE\_DACL\_DEFAULTED;




## SE\_DACL\_PRESENT

const win32security\.SE\_DACL\_PRESENT;




## SE\_DACL\_PROTECTED

const win32security\.SE\_DACL\_PROTECTED;

win2k and up


## SE\_DS\_OBJECT

const win32security\.SE\_DS\_OBJECT;




## SE\_DS\_OBJECT\_ALL

const win32security\.SE\_DS\_OBJECT\_ALL;




## SE\_FILE\_OBJECT

const win32security\.SE\_FILE\_OBJECT;




## SE\_GROUP\_DEFAULTED

const win32security\.SE\_GROUP\_DEFAULTED;




## SE\_GROUP\_ENABLED

const win32security\.SE\_GROUP\_ENABLED;




## SE\_GROUP\_ENABLED\_BY\_DEFAULT

const win32security\.SE\_GROUP\_ENABLED\_BY\_DEFAULT;




## SE\_GROUP\_LOGON\_ID

const win32security\.SE\_GROUP\_LOGON\_ID;




## SE\_GROUP\_MANDATORY

const win32security\.SE\_GROUP\_MANDATORY;




## SE\_GROUP\_OWNER

const win32security\.SE\_GROUP\_OWNER;




## SE\_GROUP\_RESOURCE

const win32security\.SE\_GROUP\_RESOURCE;




## SE\_GROUP\_USE\_FOR\_DENY\_ONLY

const win32security\.SE\_GROUP\_USE\_FOR\_DENY\_ONLY;




## SE\_KERNEL\_OBJECT

const win32security\.SE\_KERNEL\_OBJECT;




## SE\_LMSHARE

const win32security\.SE\_LMSHARE;




## SE\_OWNER\_DEFAULTED

const win32security\.SE\_OWNER\_DEFAULTED;




## SE\_PRINTER

const win32security\.SE\_PRINTER;




## SE\_PRIVILEGE\_ENABLED

const win32security\.SE\_PRIVILEGE\_ENABLED;




## SE\_PRIVILEGE\_ENABLED\_BY\_DEFAULT

const win32security\.SE\_PRIVILEGE\_ENABLED\_BY\_DEFAULT;




## SE\_PRIVILEGE\_REMOVED

const win32security\.SE\_PRIVILEGE\_REMOVED;




## SE\_PRIVILEGE\_USED\_FOR\_ACCESS

const win32security\.SE\_PRIVILEGE\_USED\_FOR\_ACCESS;




## SE\_PROVIDER\_DEFINED\_OBJECT

const win32security\.SE\_PROVIDER\_DEFINED\_OBJECT;




## SE\_REGISTRY\_KEY

const win32security\.SE\_REGISTRY\_KEY;




## SE\_REGISTRY\_WOW64\_32KEY

const win32security\.SE\_REGISTRY\_WOW64\_32KEY;




## SE\_SACL\_AUTO\_INHERITED

const win32security\.SE\_SACL\_AUTO\_INHERITED;

win2k and up


## SE\_SACL\_DEFAULTED

const win32security\.SE\_SACL\_DEFAULTED;




## SE\_SACL\_PRESENT

const win32security\.SE\_SACL\_PRESENT;




## SE\_SACL\_PROTECTED

const win32security\.SE\_SACL\_PROTECTED;

win2k and up


## SE\_SELF\_RELATIVE

const win32security\.SE\_SELF\_RELATIVE;




## SE\_SERVICE

const win32security\.SE\_SERVICE;




## SE\_UNKNOWN\_OBJECT\_TYPE

const win32security\.SE\_UNKNOWN\_OBJECT\_TYPE;




## SE\_WINDOW\_OBJECT

const win32security\.SE\_WINDOW\_OBJECT;




## SE\_WMIGUID\_OBJECT

const win32security\.SE\_WMIGUID\_OBJECT;




## [win32security](win32security.md#win32security)\.SID

PySID = SID\(\)
Creates a new [PySID](PySID.md) object\.


## STYPE\_DEVICE

const win32security\.STYPE\_DEVICE;




## STYPE\_DISKTREE

const win32security\.STYPE\_DISKTREE;




## STYPE\_IPC

const win32security\.STYPE\_IPC;




## STYPE\_PRINTQ

const win32security\.STYPE\_PRINTQ;




## STYPE\_SPECIAL

const win32security\.STYPE\_SPECIAL;




## STYPE\_TEMPORARY

const win32security\.STYPE\_TEMPORARY;




## SUB\_CONTAINERS\_AND\_OBJECTS\_INHERIT

const win32security\.SUB\_CONTAINERS\_AND\_OBJECTS\_INHERIT;




## SUB\_CONTAINERS\_ONLY\_INHERIT

const win32security\.SUB\_CONTAINERS\_ONLY\_INHERIT;




## SUB\_OBJECTS\_ONLY\_INHERIT

const win32security\.SUB\_OBJECTS\_ONLY\_INHERIT;




## SUCCESSFUL\_ACCESS\_ACE\_FLAG

const win32security\.SUCCESSFUL\_ACCESS\_ACE\_FLAG;




## SYSTEM\_AUDIT\_ACE\_TYPE

const win32security\.SYSTEM\_AUDIT\_ACE\_TYPE;

System-audit ACE that uses the SYSTEM\_AUDIT\_ACE structure\.


## SYSTEM\_AUDIT\_OBJECT\_ACE\_TYPE

const win32security\.SYSTEM\_AUDIT\_OBJECT\_ACE\_TYPE;




## SecurityAnonymous

const win32security\.SecurityAnonymous;




## SecurityDelegation

const win32security\.SecurityDelegation;




## SecurityIdentification

const win32security\.SecurityIdentification;




## SecurityImpersonation

const win32security\.SecurityImpersonation;




## [win32security](win32security.md#win32security)\.SetFileSecurity

SetFileSecurity\(filename, info, security\)
Sets information about the security of a file or directory\. The information obtained is constrained by the caller's access rights and privileges\.

#### Parameters

  - filename : string

    The name of the file

  - info : int

    The type of information to set\.

  - security : [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information


## [win32security](win32security.md#win32security)\.SetKernelObjectSecurity

SetKernelObjectSecurity\(handle, info, security\)
Sets information about the security of a kernel object\. The information obtained is constrained by the caller's access rights and privileges\.

#### Parameters

  - handle : [PyHANDLE](PyHANDLE.md)

    The handle to an object for which security information will be set\.

  - info : int

    The type of information to set - combination of SECURITY\_INFORMATION values

  - security : [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information


## [win32security](win32security.md#win32security)\.SetNamedSecurityInfo

SetNamedSecurityInfo\(ObjectName, ObjectType, SecurityInfo, Owner, Group, Dacl, Sacl\)
Sets security info for an object by name

#### Parameters

  - ObjectName : str/unicode

    Name of object

  - ObjectType : int

    Value from SE\_OBJECT\_TYPE enum

  - SecurityInfo : int

    Combination of SECURITY\_INFORMATION constants

  - Owner : [PySID](PySID.md)

    Sid to set as owner of object, can be None

  - Group : [PySID](PySID.md)

    Group Sid, can be None

  - Dacl : [PyACL](PyACL.md)

    Discretionary ACL to set for object, can be None

  - Sacl : [PyACL](PyACL.md)

    System Audit ACL to set for object, can be None


## [win32security](win32security.md#win32security)\.SetSecurityInfo

SetSecurityInfo\(handle, ObjectType, SecurityInfo, Owner, Group, Dacl, Sacl\)
Sets security info for an object by handle

#### Parameters

  - handle : int/[PyHANDLE](PyHANDLE.md)

    Handle to object

  - ObjectType : int

    Value from SE\_OBJECT\_TYPE enum

  - SecurityInfo : int

    Combination of SECURITY\_INFORMATION constants

  - Owner : [PySID](PySID.md)

    Sid to set as owner of object, can be None

  - Group : [PySID](PySID.md)

    Group Sid, can be None

  - Dacl : [PyACL](PyACL.md)

    Discretionary ACL to set for object, can be None

  - Sacl : [PyACL](PyACL.md)

    System Audit ACL to set for object, can be None


## [win32security](win32security.md#win32security)\.SetThreadToken

SetThreadToken\(Thread, Token\)
Assigns an impersonation token to a thread\. The function 

can also cause a thread to stop using an impersonation token\.

#### Parameters

  - Thread : [PyHANDLE](PyHANDLE.md)

    Handle to a thread\.  Use None to indicate calling thread\.

  - Token : [PyHANDLE](PyHANDLE.md)

    Handle to an impersonation token\.  Use None to end impersonation\.


## [win32security](win32security.md#win32security)\.SetTokenInformation

SetTokenInformation\(TokenHandle, TokenInformationClass, TokenInformation\)
Set a specified type of information in an access token

#### Parameters

  - TokenHandle : [PyHANDLE](PyHANDLE.md)

    Handle to an access token to be modified

  - TokenInformationClass : int

    Specifies a value from the TOKEN\_INFORMATION\_CLASS enumerated type identifying the type of information to be modfied

  - TokenInformation : object

    Type is dependent on TokenInformationClass



## [win32security](win32security.md#win32security)\.SetUserObjectSecurity

SetUserObjectSecurity\(handle, info, security\)
Sets information about the security of a user object\. The information obtained is constrained by the caller's access rights and privileges\.

#### Parameters

  - handle : [PyHANDLE](PyHANDLE.md)

    The handle to an object for which security information will be set\.

  - info : int

    The type of information to set - combination of SECURITY\_INFORMATION values

  - security : [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information


## SidTypeAlias

const win32security\.SidTypeAlias;

Indicates an alias SID\.


## SidTypeComputer

const win32security\.SidTypeComputer;

Indicates a computer SID


## SidTypeDeletedAccount

const win32security\.SidTypeDeletedAccount;

Indicates an SID for a deleted account\.


## SidTypeDomain

const win32security\.SidTypeDomain;

Indicates a domain SID\.


## SidTypeGroup

const win32security\.SidTypeGroup;

Indicates a group SID\.


## SidTypeInvalid

const win32security\.SidTypeInvalid;

Indicates an invalid SID\.


## SidTypeUnknown

const win32security\.SidTypeUnknown;

Indicates an unknown SID type\.


## SidTypeUser

const win32security\.SidTypeUser;

Indicates a user SID\.


## SidTypeWellKnownGroup

const win32security\.SidTypeWellKnownGroup;

Indicates an SID for a well-known group\.


## TOKEN\_ADJUST\_DEFAULT

const win32security\.TOKEN\_ADJUST\_DEFAULT;

Required to change the default ACL, primary group, or owner of an access token\.


## TOKEN\_ADJUST\_GROUPS

const win32security\.TOKEN\_ADJUST\_GROUPS;

Required to change the groups specified in an access token\.


## TOKEN\_ADJUST\_PRIVILEGES

const win32security\.TOKEN\_ADJUST\_PRIVILEGES;

Required to change the privileges specified in an access token\.


## TOKEN\_ALL\_ACCESS

const win32security\.TOKEN\_ALL\_ACCESS;

Combines the STANDARD\_RIGHTS\_REQUIRED standard access rights and all individual access rights for tokens\.


## TOKEN\_ASSIGN\_PRIMARY

const win32security\.TOKEN\_ASSIGN\_PRIMARY;

Required to attach a primary token to a process in addition to the SE\_CREATE\_TOKEN\_NAME privilege\.


## TOKEN\_DUPLICATE

const win32security\.TOKEN\_DUPLICATE;

Required to duplicate an access token\.


## TOKEN\_EXECUTE

const win32security\.TOKEN\_EXECUTE;

Combines the STANDARD\_RIGHTS\_EXECUTE standard access rights and the TOKEN\_IMPERSONATE access right\.


## TOKEN\_IMPERSONATE

const win32security\.TOKEN\_IMPERSONATE;

Required to attach an impersonation access token to a process\.


## TOKEN\_QUERY

const win32security\.TOKEN\_QUERY;

Required to query the contents of an access token\.


## TOKEN\_QUERY\_SOURCE

const win32security\.TOKEN\_QUERY\_SOURCE;

Required to query the source of an access token\.


## TOKEN\_READ

const win32security\.TOKEN\_READ;

Combines the STANDARD\_RIGHTS\_READ standard access rights and the TOKEN\_QUERY access right\.


## TOKEN\_WRITE

const win32security\.TOKEN\_WRITE;

Combines the STANDARD\_RIGHTS\_WRITE standard access rights and the TOKEN\_ADJUST\_PRIVILEGES, TOKEN\_ADJUST\_GROUPS, and TOKEN\_ADJUST\_DEFAULT access rights\.


## TRUSTEE\_BAD\_FORM

const win32security\.TRUSTEE\_BAD\_FORM;




## TRUSTEE\_IS\_ALIAS

const win32security\.TRUSTEE\_IS\_ALIAS;




## TRUSTEE\_IS\_COMPUTER

const win32security\.TRUSTEE\_IS\_COMPUTER;




## TRUSTEE\_IS\_DELETED

const win32security\.TRUSTEE\_IS\_DELETED;




## TRUSTEE\_IS\_DOMAIN

const win32security\.TRUSTEE\_IS\_DOMAIN;




## TRUSTEE\_IS\_GROUP

const win32security\.TRUSTEE\_IS\_GROUP;




## TRUSTEE\_IS\_INVALID

const win32security\.TRUSTEE\_IS\_INVALID;




## TRUSTEE\_IS\_NAME

const win32security\.TRUSTEE\_IS\_NAME;




## TRUSTEE\_IS\_OBJECTS\_AND\_NAME

const win32security\.TRUSTEE\_IS\_OBJECTS\_AND\_NAME;




## TRUSTEE\_IS\_OBJECTS\_AND\_SID

const win32security\.TRUSTEE\_IS\_OBJECTS\_AND\_SID;




## TRUSTEE\_IS\_SID

const win32security\.TRUSTEE\_IS\_SID;




## TRUSTEE\_IS\_UNKNOWN

const win32security\.TRUSTEE\_IS\_UNKNOWN;




## TRUSTEE\_IS\_USER

const win32security\.TRUSTEE\_IS\_USER;




## TRUSTEE\_IS\_WELL\_KNOWN\_GROUP

const win32security\.TRUSTEE\_IS\_WELL\_KNOWN\_GROUP;




## TokenImpersonation

const win32security\.TokenImpersonation;




## TokenPrimary

const win32security\.TokenPrimary;




## [win32security](win32security.md#win32security)\.TranslateName

[PyUnicode](PyUnicode.md) = TranslateName\(accountName, accountNameFormat

, accountNameFormat

, numChars

\)
Converts a directory service object name from one format to another\.

#### Parameters

  - accountName : [PyUnicode](PyUnicode.md)

    object name

  - accountNameFormat : int

    A value from the EXTENDED\_NAME\_FORMAT enumeration type indicating the format of the accountName name\.

  - accountNameFormat : int

    A value from the EXTENDED\_NAME\_FORMAT enumeration type indicating the format of the desired name\.

  - numChars=1024 : int

    Number of Unicode characters to allocate for the return buffer\.


## TrustedControllersInformation

const win32security\.TrustedControllersInformation;




## TrustedDomainAuthInformation

const win32security\.TrustedDomainAuthInformation;




## TrustedDomainAuthInformationInternal

const win32security\.TrustedDomainAuthInformationInternal;




## TrustedDomainFullInformation

const win32security\.TrustedDomainFullInformation;




## TrustedDomainFullInformation2Internal

const win32security\.TrustedDomainFullInformation2Internal;




## TrustedDomainFullInformationInternal

const win32security\.TrustedDomainFullInformationInternal;




## TrustedDomainInformationBasic

const win32security\.TrustedDomainInformationBasic;




## TrustedDomainInformationEx

const win32security\.TrustedDomainInformationEx;




## TrustedDomainInformationEx2Internal

const win32security\.TrustedDomainInformationEx2Internal;




## TrustedDomainNameInformation

const win32security\.TrustedDomainNameInformation;




## TrustedPasswordInformation

const win32security\.TrustedPasswordInformation;




## TrustedPosixOffsetInformation

const win32security\.TrustedPosixOffsetInformation;




## UNPROTECTED\_DACL\_SECURITY\_INFORMATION

const win32security\.UNPROTECTED\_DACL\_SECURITY\_INFORMATION;




## UNPROTECTED\_SACL\_SECURITY\_INFORMATION

const win32security\.UNPROTECTED\_SACL\_SECURITY\_INFORMATION;

