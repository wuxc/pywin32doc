# win32security

## Module win32security

An interface to the win32 security API's

#### Methods


  - [DsGetSpn](win32security.md#win32securitydsgetspn)

    Compose one or more service principal names to be registered using[win32security::DsWriteAccountSpn](win32security.md#win32securitydswriteaccountspn)&nbsp;

  - [DsWriteAccountSpn](win32security.md#win32securitydswriteaccountspn)

    Associates a set of service principal names with an account&nbsp;

  - [DsBind](win32security.md#win32securitydsbind)

    Creates a connection to a directory service&nbsp;

  - [DsUnBind](win32security.md#win32securitydsunbind)

    Closes a directory services handle created by[win32security::DsBind](win32security.md#win32securitydsbind)&nbsp;

  - [DsGetDcName](win32security.md#win32securitydsgetdcname)

    Returns the name of a domain controller (DC) in a specified domain. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.&nbsp;

  - [DsCrackNames](win32security.md#win32securitydscracknames)

    Converts an array of directory service object names from one format to another.&nbsp;

  - [DsListInfoForServer](win32security.md#win32securitydslistinfoforserver)

    Lists miscellaneous information for a server.&nbsp;

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

    Creates a new[PyACL](#pyacl)object.&nbsp;

  - [SID](win32security.md#win32securitysid)

    Creates a new[PySID](#pysid)object.&nbsp;

  - [SECURITY_ATTRIBUTES](win32security.md#win32securitysecurity_attributes)

    Creates a new[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)object.&nbsp;

  - [SECURITY_DESCRIPTOR](win32security.md#win32securitysecurity_descriptor)

    Creates a new[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)object.&nbsp;

  - [ImpersonateNamedPipeClient](win32security.md#win32securityimpersonatenamedpipeclient)

    Impersonates a named-pipe client application.&nbsp;

  - [ImpersonateLoggedOnUser](win32security.md#win32securityimpersonateloggedonuser)

    Impersonates a logged on user.&nbsp;

  - [ImpersonateAnonymousToken](win32security.md#win32securityimpersonateanonymoustoken)

    Cause a thread to act in the security context of an anonymous token&nbsp;

  - [IsTokenRestricted](win32security.md#win32securityistokenrestricted)

    Checks if a token contains restricted sids&nbsp;

  - [RevertToSelf](win32security.md#win32securityreverttoself)

    Terminates the impersonation of a client application.&nbsp;

  - [LogonUser](win32security.md#win32securitylogonuser)

    Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.&nbsp;

  - [LogonUserEx](win32security.md#win32securitylogonuserex)

    Log a user onto the local machine,&nbsp;

  - [LookupAccountName](win32security.md#win32securitylookupaccountname)

    Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.&nbsp;

  - [LookupAccountSid](win32security.md#win32securitylookupaccountsid)

    Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.&nbsp;

  - [GetBinarySid](win32security.md#win32securitygetbinarysid)

    Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.&nbsp;

  - [SetSecurityInfo](win32security.md#win32securitysetsecurityinfo)

    Sets security info for an object by handle&nbsp;

  - [GetSecurityInfo](win32security.md#win32securitygetsecurityinfo)

    Retrieve security info for an object by handle&nbsp;

  - [SetNamedSecurityInfo](win32security.md#win32securitysetnamedsecurityinfo)

    Sets security info for an object by name&nbsp;

  - [GetNamedSecurityInfo](win32security.md#win32securitygetnamedsecurityinfo)

    Retrieve security info for an object by name&nbsp;

  - [OpenProcessToken](win32security.md#win32securityopenprocesstoken)

    Opens the access token associated with a process.&nbsp;

  - [LookupPrivilegeValue](win32security.md#win32securitylookupprivilegevalue)

    Retrieves the locally unique id for a privilege name&nbsp;

  - [LookupPrivilegeName](win32security.md#win32securitylookupprivilegename)

    return the text name for a privilege LUID&nbsp;

  - [LookupPrivilegeDisplayName](win32security.md#win32securitylookupprivilegedisplayname)

    Returns long description for a privilege name&nbsp;

  - [AdjustTokenPrivileges](win32security.md#win32securityadjusttokenprivileges)

    Enables or disables privileges for an access token.&nbsp;

  - [AdjustTokenGroups](win32security.md#win32securityadjusttokengroups)

    Sets the groups associated to an access token.&nbsp;

  - [GetTokenInformation](win32security.md#win32securitygettokeninformation)

    Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.&nbsp;

  - [OpenThreadToken](win32security.md#win32securityopenthreadtoken)

    Opens the access token associated with a thread.&nbsp;

  - [SetThreadToken](win32security.md#win32securitysetthreadtoken)

    Assigns an impersonation token to a thread. The function 

can also cause a thread to stop using an impersonation token.&nbsp;

  - [GetFileSecurity](win32security.md#win32securitygetfilesecurity)

    Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

  - [SetFileSecurity](win32security.md#win32securitysetfilesecurity)

    Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

  - [GetUserObjectSecurity](win32security.md#win32securitygetuserobjectsecurity)

    Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

  - [SetUserObjectSecurity](win32security.md#win32securitysetuserobjectsecurity)

    Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

  - [GetKernelObjectSecurity](win32security.md#win32securitygetkernelobjectsecurity)

    Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

  - [SetKernelObjectSecurity](win32security.md#win32securitysetkernelobjectsecurity)

    Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

  - [SetTokenInformation](win32security.md#win32securitysettokeninformation)

    Set a specified type of information in an access token&nbsp;

  - [LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

    Opens a policy handle for the specified system&nbsp;

  - [LsaClose](win32security.md#win32securitylsaclose)

    Closes a policy handle created by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)&nbsp;

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

    Return string representation of a SECURITY_DESCRIPTOR&nbsp;

  - [ConvertStringSecurityDescriptorToSecurityDescriptor](win32security.md#win32securityconvertstringsecuritydescriptortosecuritydescriptor)

    Turns string representation of a SECURITY_DESCRIPTOR into the real thing&nbsp;

  - [LsaStorePrivateData](win32security.md#win32securitylsastoreprivatedata)

    Stores encrypted unicode data under specified Lsa registry key. Returns None on success&nbsp;

  - [LsaRetrievePrivateData](win32security.md#win32securitylsaretrieveprivatedata)

    Retreives encrypted unicode data from Lsa registry key.&nbsp;

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

    Extended version of DuplicateToken.&nbsp;

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

    Converts a directory service object name from one format to another.&nbsp;

  - [CreateWellKnownSid](win32security.md#win32securitycreatewellknownsid)

    Returns one of the predefined well known sids&nbsp;

  - [MapGenericMask](win32security.md#win32securitymapgenericmask)

    Translates generic access rights into specific rights&nbsp;

## ACCESS_ALLOWED_ACE_TYPE
 __const win32security.ACCESS_ALLOWED_ACE_TYPE;__ 
Access-allowed ACE that uses the ACCESS_ALLOWED_ACE structure.

## ACCESS_ALLOWED_OBJECT_ACE_TYPE
 __const win32security.ACCESS_ALLOWED_OBJECT_ACE_TYPE;__ 
Windows 2000/XP: Object-specific access-allowed ACE that uses the ACCESS_ALLOWED_OBJECT_ACE structure.

## ACCESS_DENIED_ACE_TYPE
 __const win32security.ACCESS_DENIED_ACE_TYPE;__ 
Access-denied ACE that uses the ACCESS_DENIED_ACE structure.

## ACCESS_DENIED_OBJECT_ACE_TYPE
 __const win32security.ACCESS_DENIED_OBJECT_ACE_TYPE;__ 
Windows 2000/XP: Object-specific access-denied ACE that uses the ACCESS_DENIED_OBJECT_ACE structure.

## [win32security](#win32security).ACL

PyACL = __ACL( *bufSize* __ )
Creates a new[PyACL](#pyacl)object.

#### Parameters


  -  *bufSize=64* : int

    The size of the buffer for the ACL.

## ACL_REVISION
 __const win32security.ACL_REVISION;__ 


## ACL_REVISION_DS
 __const win32security.ACL_REVISION_DS;__ 


## [win32security](#win32security).AcceptSecurityContext

(int, long, int) = __AcceptSecurityContext( *Credential*  *, Context*  *, pInput*  *, ContextReq*  *, TargetDataRep*  *, NewContext*  *, pOutput* __ )
Builds security context between server and client

#### Parameters


  -  *Credential* :[PyCredHandle](#pycredhandle)

    Handle to server's credentials (see AcquireCredentialsHandle)

  -  *Context* :[PyCtxtHandle](#pyctxthandle)

    Use None on initial call, then handle returned in NewContext thereafter

  -  *pInput* :[PySecBufferDesc](#pysecbufferdesc)

    Data buffer received from client

  -  *ContextReq* : int

    Combination of ASC_REQ_* flags

  -  *TargetDataRep* : int

    One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP

  -  *NewContext* :[PyCtxtHandle](#pyctxthandle)

    Uninitialized context handle to receive output

  -  *pOutput* :[PySecBufferDesc](#pysecbufferdesc)

    Buffer that receives output data, to be passed back as pInput on subsequent calls

#### Return Value
Returns a tuple of (return code, context attributes, context expiration time)

## [win32security](#win32security).AcquireCredentialsHandle

([PyCredHandle](#pycredhandle),[PyTime](#pytime)) = __AcquireCredentialsHandle( *Principal*  *, Package*  *, CredentialUse*  *, LogonID*  *, AuthData* __ )
Creates a handle to credentials for use with SSPI

#### Parameters


  -  *Principal* : str/unicode

    Use None for current security context

  -  *Package* : str/unicode

    Name of security package that credentials will be used with

  -  *CredentialUse* : int

    Intended use of requested credentials, SECPKG_CRED_INBOUND, SECPKG_CRED_OUTBOUND, or SECPKG_CRED_BOTH

  -  *LogonID* : long

    LUID representing a logon session, can be None

  -  *AuthData* : tuple

    Sequence of 3 strings: (User, Domain, Password) - use none for existing credentials

#### Return Value
Returns credential handle and credential's expiration time

## [win32security](#win32security).AdjustTokenGroups

[PyTOKEN_GROUPS](PyTOKEN.md#pytokengroups)= __AdjustTokenGroups( *TokenHandle*  *, ResetToDefault*  *, NewState* __ )
Sets the groups associated to an access token.

#### Parameters


  -  *TokenHandle* :[PyHANDLE](#pyhandle)

    The handle to access token to be modified

  -  *ResetToDefault* : boolean

    Sets groups to default enabled/disabled states,

  -  *NewState* :[PyTOKEN_GROUPS](PyTOKEN.md#pytokengroups)

    Groups and attributes to be set for token

#### Comments
Accepts keyword args.

#### Return Value
Returns previous state of groups modified

## [win32security](#win32security).AdjustTokenPrivileges

[PyTOKEN_PRIVILEGES](PyTOKEN.md#pytokenprivileges)= __AdjustTokenPrivileges( *TokenHandle*  *, bDisableAllPrivileges*  *, NewState* __ )
Enables or disables privileges for an access token.

#### Parameters


  -  *TokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token

  -  *bDisableAllPrivileges* : int

    Flag for disabling all privileges

  -  *NewState* :[PyTOKEN_PRIVILEGES](PyTOKEN.md#pytokenprivileges)

    The new state, can be None if bDisableAllPrivileges is True

#### Comments
Accepts keyword args.

#### Return Value
Returns modified privileges for later restoral.  Privileges deleted from the token using 

SE_PRIVILEGE_REMOVED are not returned.

## [win32security](#win32security).AllocateLocallyUniqueId

 __AllocateLocallyUniqueId(__ )
Creates a new LUID

## AuditCategoryAccountLogon
 __const win32security.AuditCategoryAccountLogon;__ 


## AuditCategoryAccountManagement
 __const win32security.AuditCategoryAccountManagement;__ 


## AuditCategoryDetailedTracking
 __const win32security.AuditCategoryDetailedTracking;__ 


## AuditCategoryDirectoryServiceAccess
 __const win32security.AuditCategoryDirectoryServiceAccess;__ 


## AuditCategoryLogon
 __const win32security.AuditCategoryLogon;__ 


## AuditCategoryObjectAccess
 __const win32security.AuditCategoryObjectAccess;__ 


## AuditCategoryPolicyChange
 __const win32security.AuditCategoryPolicyChange;__ 


## AuditCategoryPrivilegeUse
 __const win32security.AuditCategoryPrivilegeUse;__ 


## AuditCategorySystem
 __const win32security.AuditCategorySystem;__ 


## CONTAINER_INHERIT_ACE
 __const win32security.CONTAINER_INHERIT_ACE;__ 


## [win32security](#win32security).CheckTokenMembership

bool = __CheckTokenMembership( *TokenHandle*  *, SidToCheck* __ )
Checks if a SID is enabled in a token

#### Parameters


  -  *TokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token, current process token used if None

  -  *SidToCheck* :[PySID](#pysid)

    Sid to be checked for presence in token

## [win32security](#win32security).ConvertSecurityDescriptorToStringSecurityDescriptor

string = __ConvertSecurityDescriptorToStringSecurityDescriptor( *SecurityDescriptor*  *, RequestedStringSDRevision*  *, SecurityInformation* __ )
Return string representation of a SECURITY_DESCRIPTOR

#### Parameters


  -  *SecurityDescriptor* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    PySECURITY_DESCRIPTOR object

  -  *RequestedStringSDRevision* : int

    Only SDDL_REVISION_1 currently valid

  -  *SecurityInformation* : int

    Combination of bit flags from SECURITY_INFORMATION enum

## [win32security](#win32security).ConvertSidToStringSid

string = __ConvertSidToStringSid( *Sid* __ )
Return string representation of a SID

#### Parameters


  -  *Sid* :[PySID](#pysid)

    PySID object

## [win32security](#win32security).ConvertStringSecurityDescriptorToSecurityDescriptor

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __ConvertStringSecurityDescriptorToSecurityDescriptor( *StringSecurityDescriptor*  *, StringSDRevision* __ )
Turns string representation of a SECURITY_DESCRIPTOR into the real thing

#### Parameters


  -  *StringSecurityDescriptor* : string

    String representation of a SECURITY_DESCRIPTOR

  -  *StringSDRevision* : int

    Only SDDL_REVISION_1 currently valid

## [win32security](#win32security).ConvertStringSidToSid

[PySID](#pysid)= __ConvertStringSidToSid( *StringSid* __ )
Creates a SID from a string representation

#### Parameters


  -  *StringSid* : string

    String representation of a SID

## [win32security](#win32security).CreateRestrictedToken

[PyHANDLE](#pyhandle)= __CreateRestrictedToken( *ExistingTokenHandle*  *, Flags*  *, SidsToDisable*  *, PrivilegesToDelete*  *, SidsToRestrict* __ )
Creates a restricted copy of an access token with reduced privs - requires win2K or higher

#### Parameters


  -  *ExistingTokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token (see[win32security::LogonUser](win32security.md#win32securitylogonuser),[win32security::OpenProcessToken](win32security.md#win32securityopenprocesstoken)

  -  *Flags* : int

    Valid values are zero or a combination of DISABLE_MAX_PRIVILEGE and SANDBOX_INERT

  -  *SidsToDisable* : ([PySID_AND_ATTRIBUTES](PySID.md#pysidand_attributes),...)

    Ssequence of[PySID_AND_ATTRIBUTES](PySID.md#pysidand_attributes)tuples, or None

  -  *PrivilegesToDelete* : ([PyLUID_AND_ATTRIBUTES](PyLUID.md#pyluidand_attributes),...)

    Privilege LUIDS to remove from token (attributes are ignored), or None

  -  *SidsToRestrict* : ([PySID_AND_ATTRIBUTES](PySID.md#pysidand_attributes),...)

    Sequence of[PySID_AND_ATTRIBUTES](PySID.md#pysidand_attributes)tuples (attributes must be 0).  Can be None.

## [win32security](#win32security).CreateWellKnownSid

[PySID](#pysid)= __CreateWellKnownSid( *WellKnownSidType*  *, DomainSid* __ )
Returns one of the predefined well known sids

#### Parameters


  -  *WellKnownSidType* : int

    One of the Win*Sid constants

  -  *DomainSid=None* :[PySID](#pysid)

    Domain for the new SID, or None for local machine

## [win32security](#win32security).CryptEnumProviders

[([PyUnicode](#pyunicode),int),...] = __CryptEnumProviders(__ )
List cryptography providers

#### Return Value
Returns a sequence of tuples containing provider name and type

## DACL_SECURITY_INFORMATION
 __const win32security.DACL_SECURITY_INFORMATION;__ 
Indicates the discretionary ACL of the object is being referenced.

## DENY_ACCESS
 __const win32security.DENY_ACCESS;__ 


## DISABLE_MAX_PRIVILEGE
 __const win32security.DISABLE_MAX_PRIVILEGE;__ 


## DS_SPN_ADD_SPN_OP
 __const win32security.DS_SPN_ADD_SPN_OP;__ 


## DS_SPN_DELETE_SPN_OP
 __const win32security.DS_SPN_DELETE_SPN_OP;__ 


## DS_SPN_DNS_HOST
 __const win32security.DS_SPN_DNS_HOST;__ 


## DS_SPN_DN_HOST
 __const win32security.DS_SPN_DN_HOST;__ 


## DS_SPN_DOMAIN
 __const win32security.DS_SPN_DOMAIN;__ 


## DS_SPN_NB_DOMAIN
 __const win32security.DS_SPN_NB_DOMAIN;__ 


## DS_SPN_NB_HOST
 __const win32security.DS_SPN_NB_HOST;__ 


## DS_SPN_REPLACE_SPN_OP
 __const win32security.DS_SPN_REPLACE_SPN_OP;__ 


## DS_SPN_SERVICE
 __const win32security.DS_SPN_SERVICE;__ 


## [win32security](#win32security).DsBind

[PyDS_HANDLE](PyDS.md#pydshandle)= __DsBind( *DomainController*  *, DnsDomainName* __ )
Creates a connection to a directory service

#### Parameters


  -  *DomainController* :[PyUnicode](#pyunicode)

    Name of domain controller to contact, can be None

  -  *DnsDomainName* :[PyUnicode](#pyunicode)

    Dotted name of domain to bind to, can be None

## [win32security](#win32security).DsCrackNames

[ (status, domain, name) ] = __DsCrackNames( *hds*  *, flags*  *, formatOffered*  *, formatDesired*  *, names* __ )
Converts an array of directory service object names from one format to another.

#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

  -  *flags* : int

    

  -  *formatOffered* : int

    

  -  *formatDesired* : int

    

  -  *names* : [name, ...]

    

## [win32security](#win32security).DsGetDcName

dict = __DsGetDcName( *computerName*  *, domainName*  *, domainGUID*  *, siteName*  *, flags* __ )
Returns the name of a domain controller (DC) in a specified domain. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.

#### Parameters


  -  *computerName=None* :[PyUnicode](#pyunicode)

    

  -  *domainName=None* :[PyUnicode](#pyunicode)

    

  -  *domainGUID=None* :[PyIID](#pyiid)

    

  -  *siteName=None* :[PyUnicode](#pyunicode)

    

  -  *flags=0* : int

    

#### Comments
This function supports keyword arguments.

## [win32security](#win32security).DsGetSpn

([PyUnicode](#pyunicode),...) = __DsGetSpn( *ServiceType*  *, ServiceClass*  *, ServiceName*  *, InstancePort*  *, InstanceNames*  *, InstancePorts* __ )
Compose one or more service principal names to be registered using[win32security::DsWriteAccountSpn](win32security.md#win32securitydswriteaccountspn)

#### Parameters


  -  *ServiceType* : int

    Type of Spn to create, one of the DS_SPN_* constants

  -  *ServiceClass* :[PyUnicode](#pyunicode)

    Arbitrary string that describes type of service, eg http

  -  *ServiceName* :[PyUnicode](#pyunicode)

    Name of service, can be None (not required for DS_SPN_*_HOST Spn's)

  -  *InstancePort=0* : int

    Port nbr for service instance, use 0 for no port

  -  *InstanceNames=None* : ([PyUnicode](#pyunicode),...)

    A sequence of service instance names, can be None - not required for for host Spn's

  -  *InstancePorts=None* : (int,...)

    A sequence of extra instance ports.  If specified, must be same length as InstanceNames.

## [win32security](#win32security).DsListDomainsInSite

[[PyDS_NAME_RESULT_ITEM](PyDS.md#pydsname_result_item), ...] = __DsListDomainsInSite( *hds* __ )


#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

## [win32security](#win32security).DsListInfoForServer

[[PyDS_NAME_RESULT_ITEM](PyDS.md#pydsname_result_item), ...] = __DsListInfoForServer( *hds*  *, server* __ )
Lists miscellaneous information for a server.

#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

  -  *server* :[PyUnicode](#pyunicode)

    

## [win32security](#win32security).DsListRoles

[[PyDS_NAME_RESULT_ITEM](PyDS.md#pydsname_result_item), ...] = __DsListRoles( *hds* __ )


#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

## [win32security](#win32security).DsListServersInSite

[[PyDS_NAME_RESULT_ITEM](PyDS.md#pydsname_result_item), ...] = __DsListServersInSite( *hds*  *, site* __ )


#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

  -  *site* :[PyUnicode](#pyunicode)

    

## [win32security](#win32security).DsListServersInSite

[[PyDS_NAME_RESULT_ITEM](PyDS.md#pydsname_result_item), ...] = __DsListServersInSite( *hds*  *, domain*  *, site* __ )


#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

  -  *domain* :[PyUnicode](#pyunicode)

    

  -  *site* :[PyUnicode](#pyunicode)

    

## [win32security](#win32security).DsListServersInSite

[[PyDS_NAME_RESULT_ITEM](PyDS.md#pydsname_result_item), ...] = __DsListServersInSite( *hds* __ )


#### Parameters


  -  *hds* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

## [win32security](#win32security).DsUnBind

 __DsUnBind( *hDS* __ )
Closes a directory services handle created by[win32security::DsBind](win32security.md#win32securitydsbind)

#### Parameters


  -  *hDS* :[PyDS_HANDLE](PyDS.md#pydshandle)

    A handle to a directory service as returned by[win32security::DsBind](win32security.md#win32securitydsbind)

## [win32security](#win32security).DsWriteAccountSpn

 __DsWriteAccountSpn( *hDS*  *, Operation*  *, Account*  *, Spns* __ )
Associates a set of service principal names with an account

#### Parameters


  -  *hDS* :[PyDS_HANDLE](PyDS.md#pydshandle)

    Directory service handle as returned from[win32security::DsBind](win32security.md#win32securitydsbind)

  -  *Operation* : int

    Constant from DS_SPN_WRITE_OP enum

  -  *Account* :[PyUnicode](#pyunicode)

    Distinguished name of account whose Spn's will be modified

  -  *Spns* : ([PyUnicode](#pyunicode),...)

    A sequence of target Spn's as returned by[win32security::DsGetSpn](win32security.md#win32securitydsgetspn)

## [win32security](#win32security).DuplicateToken

[PyHANDLE](#pyhandle)= __DuplicateToken( *ExistingTokenHandle*  *, ImpersonationLevel* __ )
Creates a copy of an access token with specified impersonation level

#### Parameters


  -  *ExistingTokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token (see[win32security::LogonUser](win32security.md#win32securitylogonuser),[win32security::OpenProcessToken](win32security.md#win32securityopenprocesstoken))

  -  *ImpersonationLevel* : int

    A value from SECURITY_IMPERSONATION_LEVEL enum

## [win32security](#win32security).DuplicateTokenEx

[PyHANDLE](#pyhandle)= __DuplicateTokenEx( *ExistingToken*  *, ImpersonationLevel*  *, DesiredAccess*  *, TokenType*  *, TokenAttributes* __ )
Extended version of DuplicateToken.

#### Parameters


  -  *ExistingToken* :[PyHANDLE](#pyhandle)

    Logon token opened with TOKEN_DUPLICATE access

  -  *ImpersonationLevel* : int

    One of win32security.Security* values

  -  *DesiredAccess* : int

    Type of access required for the handle, combination of win32security.TOKEN_* flags

  -  *TokenType* : int

    Type of token to be created, TokenPrimary or TokenImpersonation

  -  *TokenAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security and inheritance for the new handle.  None results in default DACL and no inheritance,

#### Comments
Accepts keyword arguments

## [win32security](#win32security).EnumerateSecurityPackages

(dict,...) = __EnumerateSecurityPackages(__ )
List available security packages as a sequence of dictionaries representing SecPkgInfo structures

## FAILED_ACCESS_ACE_FLAG
 __const win32security.FAILED_ACCESS_ACE_FLAG;__ 


## GRANT_ACCESS
 __const win32security.GRANT_ACCESS;__ 


## GROUP_SECURITY_INFORMATION
 __const win32security.GROUP_SECURITY_INFORMATION;__ 
Indicates the primary group identifier of the object is being referenced.

## [win32security](#win32security).GetBinarySid

[PySID](#pysid)= __GetBinarySid( *SID* __ )
Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.

#### Parameters


  -  *SID* : string

    Textual representation of a SID. Textual SID example: S-1-5-32-544

## [win32security](#win32security).GetFileSecurity

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __GetFileSecurity( *filename*  *, info* __ )
Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


  -  *filename* : string

    The name of the file

  -  *info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION* : int

    Flags that specify the information requested.

#### Comments
This function reportedly will not return the INHERITED_ACE flag on some Windows XP SP1 systems 

Use GetNamedSecurityInfo if you encounter this problem.

## [win32security](#win32security).GetKernelObjectSecurity

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __GetKernelObjectSecurity( *handle*  *, info* __ )
Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the object

  -  *info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION* : int

    Flags that specify the information requested.

## [win32security](#win32security).GetNamedSecurityInfo

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __GetNamedSecurityInfo( *ObjectName*  *, ObjectType*  *, SecurityInfo* __ )
Retrieve security info for an object by name

#### Parameters


  -  *ObjectName* : str/unicode

    Name of object

  -  *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

  -  *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

#### Comments
Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from 

the returned PySECURITY_DESCRIPTOR

## [win32security](#win32security).GetSecurityInfo

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __GetSecurityInfo( *handle*  *, ObjectType*  *, SecurityInfo* __ )
Retrieve security info for an object by handle

#### Parameters


  -  *handle* : int/[PyHANDLE](#pyhandle)

    Handle to object

  -  *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

  -  *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

#### Comments
Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from 

the returned PySECURITY_DESCRIPTOR

## [win32security](#win32security).GetTokenInformation

object = __GetTokenInformation( *TokenHandle*  *, TokenInformationClass* __ )
Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.

#### Parameters


  -  *TokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token.

  -  *TokenInformationClass* : int

    Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.

#### Return Value
The following types are supported


## [win32security](#win32security).GetUserObjectSecurity

[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)= __GetUserObjectSecurity( *handle*  *, info* __ )
Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to the object

  -  *info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION* : int

    Flags that specify the information requested.

## INHERITED_ACE
 __const win32security.INHERITED_ACE;__ 


## INHERIT_ONLY_ACE
 __const win32security.INHERIT_ONLY_ACE;__ 


## [win32security](#win32security).ImpersonateAnonymousToken

 __ImpersonateAnonymousToken( *ThreadHandle* __ )
Cause a thread to act in the security context of an anonymous token

#### Parameters


  -  *ThreadHandle* :[PyHANDLE](#pyhandle)

    Handle to thread that will

## [win32security](#win32security).ImpersonateLoggedOnUser

 __ImpersonateLoggedOnUser( *handle* __ )
Impersonates a logged on user.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    Handle to a token that represents a logged-on user

## [win32security](#win32security).ImpersonateNamedPipeClient

 __ImpersonateNamedPipeClient( *handle* __ )
Impersonates a named-pipe client application.

#### Parameters


  -  *handle* : int

    handle of a named pipe.

## [win32security](#win32security).ImpersonateSelf

 __ImpersonateSelf( *ImpersonationLevel* __ )
Assigns an impersonation token for current security context to current process

#### Parameters


  -  *ImpersonationLevel* : int

    A value from SECURITY_IMPERSONATION_LEVEL enum

## [win32security](#win32security).InitializeSecurityContext

(int, int,[PyTime](#pytime)) = __InitializeSecurityContext( *Credential*  *, Context*  *, TargetName*  *, ContextReq*  *, TargetDataRep*  *, pInput*  *, NewContext*  *, pOutput* __ )
Creates a security context based on credentials created by AcquireCredentialsHandle

#### Parameters


  -  *Credential* :[PyCredHandle](#pycredhandle)

    A credentials handle as returned by[win32security::AcquireCredentialsHandle](win32security.md#win32securityacquirecredentialshandle)

  -  *Context* :[PyCtxtHandle](#pyctxthandle)

    Use None on initial call, then handle returned in NewContext thereafter

  -  *TargetName* : str/unicode

    Target of context, security package specific - Use None with NTLM

  -  *ContextReq* : int

    Combination of ISC_REQ_* flags

  -  *TargetDataRep* : int

    One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP

  -  *pInput* :[PySecBufferDesc](#pysecbufferdesc)

    Data buffer - use None initially

  -  *NewContext* :[PyCtxtHandle](#pyctxthandle)

    Uninitialized context handle to receive output

  -  *pOutput* :[PySecBufferDesc](#pysecbufferdesc)

    Buffer that receives output data for subsequent calls

#### Return Value
Return value is a tuple of (return code, attribute flags, expiration time)

## [win32security](#win32security).IsTokenRestricted

bool = __IsTokenRestricted( *TokenHandle* __ )
Checks if a token contains restricted sids

#### Parameters


  -  *TokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token

## LABEL_SECURITY_INFORMATION
 __const win32security.LABEL_SECURITY_INFORMATION;__ 


## LOGON32_LOGON_BATCH
 __const win32security.LOGON32_LOGON_BATCH;__ 
This logon type is intended for batch servers, where processes may be executing on behalf of a user without their direct intervention; or for higher performance servers that process many clear-text authentication attempts at a time, such as mail or web servers. LogonUser does not cache credentials for this logon type.

## LOGON32_LOGON_INTERACTIVE
 __const win32security.LOGON32_LOGON_INTERACTIVE;__ 
This logon type is intended for users who will be interactively using the machine, such as a user being logged on by a terminal server, remote shell, or similar process. This logon type has the additional expense of caching logon information for disconnected operation, and is therefore inappropriate for some client/server applications, such as a mail server.

## LOGON32_LOGON_NETWORK
 __const win32security.LOGON32_LOGON_NETWORK;__ 
This logon type is intended for high performance servers to authenticate clear text passwords. LogonUser does not cache credentials for this logon type. This is the fastest logon path, but there are two limitations. First, the function returns an impersonation token, not a primary token. You cannot use this token directly in the CreateProcessAsUser function. However, you can call the DuplicateTokenEx function to convert the token to a primary token, and then use it in CreateProcessAsUser. Second, if you convert the token to a primary token and use it in CreateProcessAsUser to start a process, the new process will not be able to access other network resources, such as remote servers or printers, through the redirector.

## LOGON32_LOGON_NETWORK_CLEARTEXT
 __const win32security.LOGON32_LOGON_NETWORK_CLEARTEXT;__ 


## LOGON32_LOGON_NEW_CREDENTIALS
 __const win32security.LOGON32_LOGON_NEW_CREDENTIALS;__ 


## LOGON32_LOGON_SERVICE
 __const win32security.LOGON32_LOGON_SERVICE;__ 
Indicates a service-type logon. The account provided must have the service privilege enabled.

## LOGON32_LOGON_UNLOCK
 __const win32security.LOGON32_LOGON_UNLOCK;__ 


## LOGON32_PROVIDER_DEFAULT
 __const win32security.LOGON32_PROVIDER_DEFAULT;__ 
Use the standard logon provider for the system. This is the recommended value for the dwLogonProvider parameter. It provides maximum compatibility with current and future releases of Windows NT.

## LOGON32_PROVIDER_WINNT35
 __const win32security.LOGON32_PROVIDER_WINNT35;__ 
Use the Windows NT 3.5 logon provider.

## LOGON32_PROVIDER_WINNT40
 __const win32security.LOGON32_PROVIDER_WINNT40;__ 
Use the Windows NT 4.0 logon provider

## LOGON32_PROVIDER_WINNT50
 __const win32security.LOGON32_PROVIDER_WINNT50;__ 
Use the Negotiate protocol

## [win32security](#win32security).LogonUser

[PyHANDLE](#pyhandle)= __LogonUser( *Username*  *, Domain*  *, Password*  *, LogonType*  *, LogonProvider* __ )
Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.

#### Parameters


  -  *Username* :[PyUnicode](#pyunicode)

    The name of the user account to log on to. 

This may also be a marshalled credential (see[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)).

  -  *Domain* :[PyUnicode](#pyunicode)

    The name of the domain, or None for the current domain

  -  *Password* :[PyUnicode](#pyunicode)

    User's password.  Use a blank string if Username contains a marshalled credential.

  -  *LogonType* : int

    One of LOGON32_LOGON_* values

  -  *LogonProvider* : int

    One of LOGON32_PROVIDER_* values

#### Comments
Accepts keyword args
On Windows 2000 and earlier, the calling process must have SE_TCB_NAME privilege.

## [win32security](#win32security).LogonUserEx

([PyHANDLE](#pyhandle),[PySID](#pysid), str, dict) = __LogonUserEx( *Username*  *, Domain*  *, Password*  *, LogonType*  *, LogonProvider* __ )
Log a user onto the local machine,

#### Parameters


  -  *Username* :[PyUnicode](#pyunicode)

    User account, may be specified as a UPN (user@domain.com). 

This may also be a marshalled credential (see[win32cred::CredMarshalCredential](win32cred.md#win32credcredmarshalcredential)).

  -  *Domain* :[PyUnicode](#pyunicode)

    User's domain. Can be None if Username is a full UPN.

  -  *Password* :[PyUnicode](#pyunicode)

    User's password.  Use a blank string if Username contains a marshalled credential.

  -  *LogonType* : int

    One of LOGON32_LOGON_* values

  -  *LogonProvider* : int

    One of LOGON32_PROVIDER_* values

#### Comments
Requires Windows XP or later
Accepts keyword args

#### Return Value
Returns access token, logon sid, profile buffer, and process quotas. 

Format of the profile buffer is not known, so returned object is subject to change.

## [win32security](#win32security).LookupAccountName

[PySID](#pysid), string, int = __LookupAccountName( *systemName*  *, accountName* __ )
Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.

#### Parameters


  -  *systemName* : string

    The system name, or None

  -  *accountName* : string

    The account name

#### Return Value
The result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.

## [win32security](#win32security).LookupAccountSid

string, string, int = __LookupAccountSid( *systemName*  *, sid* __ )
Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.

#### Parameters


  -  *systemName* : string

    The system name, or None

  -  *sid* :[PySID](#pysid)

    The SID

#### Return Value
The result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.

## [win32security](#win32security).LookupPrivilegeDisplayName

[PyUnicode](#pyunicode)= __LookupPrivilegeDisplayName( *SystemName*  *, Name* __ )
Returns long description for a privilege name

#### Parameters


  -  *SystemName* : string/[PyUnicode](#pyunicode)

    System name, local system assumed if not specified

  -  *Name* : string/[PyUnicode](#pyunicode)

    Name of privilege, Se...Privilege string constants (win32security.SE_*_NAME)

## [win32security](#win32security).LookupPrivilegeName

[PyUnicode](#pyunicode)= __LookupPrivilegeName( *SystemName*  *, luid* __ )
return the text name for a privilege LUID

#### Parameters


  -  *SystemName* : string/[PyUnicode](#pyunicode)

    System name, local system assumed if not specified

  -  *luid* : LARGE_INTEGER

    64 bit value representing a privilege

## [win32security](#win32security).LookupPrivilegeValue

[LARGE_INTEGER](LARGE.md#largeinteger)= __LookupPrivilegeValue( *systemName*  *, privilegeName* __ )
Retrieves the locally unique id for a privilege name

#### Parameters


  -  *systemName* : string

    String specifying the system, use None for local machine

  -  *privilegeName* : string

    String specifying the privilege (win32security.SE_*_NAME)

## [win32security](#win32security).LsaAddAccountRights

 __LsaAddAccountRights( *PolicyHandle*  *, AccountSid*  *, UserRights* __ )
Adds a list of privileges to an account

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *AccountSid* :[PySID](#pysid)

    Account to which privs will be added

  -  *UserRights* : (str/unicode,...)

    Sequence of privilege names (SE_*_NAME unicode constants)

#### Comments
Account is created if it doesn't already exist.
Accepts keyword args.

## [win32security](#win32security).LsaCallAuthenticationPackage

 __LsaCallAuthenticationPackage( *LsaHandle*  *, AuthenticationPackage*  *, MessageType*  *, ProtocolSubmitBuffer* __ )
Requests the services of an authentication package

#### Parameters


  -  *LsaHandle* :[PyLsaLogon_HANDLE](PyLsaLogon.md#pylsalogonhandle)

    Lsa handle as returned by[win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess)or[win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted)

  -  *AuthenticationPackage* : int

    Id of authentication package to call, as returned by[win32security::LsaLookupAuthenticationPackage](win32security.md#win32securitylsalookupauthenticationpackage)

  -  *MessageType* : int

    Type of request that is being made, Kerb*Message or MsV1_0* constant

  -  *ProtocolSubmitBuffer* : object

    Type is dependent on MessageType

#### Comments
Message type is embedded in different types of submit buffers in the API call, but passed separately 

from python for simplicity of parsing input

 __MessageType__  __Input type__ KerbQueryTicketCacheMessagelong - a logon id, use 0 for current logon sessionKerbRetrieveTicketMessagelong - a logon id, use 0 for current logon sessionKerbPurgeTicketCacheMessage(long,[PyUnicode](#pyunicode),[PyUnicode](#pyunicode)) - tuple containing (LogonId, ServerName, RealmName)KerbRetrieveEncodedTicketMessage(LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle) 

(int,[PyUnicode](#pyunicode), int, int, int,[PyCredHandle](#pycredhandle))
 __MessageType__  __Return type__ KerbQueryTicketCacheMessage(dict,...) - Returns all tickets for the specified logon session (form is KERB_TICKET_CACHE_INFO)KerbPurgeTicketCacheMessageNoneKerbRetrieveTicketMessageReturns the ticket granting ticket for the logon session as a KERB_EXTERNAL_TICKETKerbRetrieveEncodedTicketMessageReturns specified ticket as a KERB_EXTERNAL_TICKET
#### Return Value
Type of returned object is dependent on MessageType

## [win32security](#win32security).LsaClose

 __LsaClose( *PolicyHandle* __ )
Closes a policy handle created by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

#### Parameters


  -  *PolicyHandle* :[PyHANDLE](#pyhandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

## [win32security](#win32security).LsaConnectUntrusted

[PyLsaLogon_HANDLE](PyLsaLogon.md#pylsalogonhandle)= __LsaConnectUntrusted(__ )
Creates untrusted connection to LSA

#### Comments
You don't need SeTcbPrivilege to execute this function as you do with 

LsaRegisterLogonProcess, but functionality of handle is limited

## [win32security](#win32security).LsaDeregisterLogonProcess

 __LsaDeregisterLogonProcess( *LsaHandle* __ )
Closes connection to LSA server

#### Parameters


  -  *LsaHandle* :[PyLsaLogon_HANDLE](PyLsaLogon.md#pylsalogonhandle)

    An Lsa handle as returned by[win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted)or[win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess)

## [win32security](#win32security).LsaEnumerateAccountRights

[[PyUnicode](#pyunicode), ...] = __LsaEnumerateAccountRights( *PolicyHandle*  *, AccountSid* __ )
Lists privileges held by SID

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *AccountSid* :[PySID](#pysid)

    Security identifier of account for which to list privs

## [win32security](#win32security).LsaEnumerateAccountsWithUserRight

([PySID](#pysid),...) = __LsaEnumerateAccountsWithUserRight( *PolicyHandle*  *, UserRight* __ )
Return SIDs that hold specified priv

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *UserRight* : str/unicode

    Name of privilege (SE_*_NAME unicode constant)

## [win32security](#win32security).LsaEnumerateLogonSessions

(long,...) = __LsaEnumerateLogonSessions(__ )
Lists all current logon ids

## [win32security](#win32security).LsaGetLogonSessionData

(dict,...) = __LsaGetLogonSessionData( *LogonId* __ )
Returns information about a logon session

#### Parameters


  -  *LogonId* : __PyLARGE_INTEGER__ 

    An LUID identifying a logon session

#### Return Value
Returns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure

## [win32security](#win32security).LsaLookupAuthenticationPackage

int = __LsaLookupAuthenticationPackage( *LsaHandle*  *, PackageName* __ )
Retrieves the unique id for an authentication package

#### Parameters


  -  *LsaHandle* :[PyLsaLogon_HANDLE](PyLsaLogon.md#pylsalogonhandle)

    An Lsa handle as returned by[win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted)or[win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess)

  -  *PackageName* : string

    Name of security package to be identified

## [win32security](#win32security).LsaOpenPolicy

[PyLSA_HANDLE](PyLSA.md#pylsahandle)= __LsaOpenPolicy( *system_name*  *, access_mask* __ )
Opens a policy handle for the specified system

#### Parameters


  -  *system_name* : string/[PyUnicode](#pyunicode)

    System name, local system assumed if not specified

  -  *access_mask* : int

    Bitmask of requested access types

## [win32security](#win32security).LsaQueryInformationPolicy

 __LsaQueryInformationPolicy( *PolicyHandle*  *, InformationClass* __ )
Retrieves information from the policy handle

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *InformationClass* : int

    POLICY_INFORMATION_CLASS value


## [win32security](#win32security).LsaRegisterLogonProcess

[PyLsaLogon_HANDLE](PyLsaLogon.md#pylsalogonhandle)= __LsaRegisterLogonProcess( *LogonProcessName* __ )
Creates a trusted connection to LSA

#### Parameters


  -  *LogonProcessName* : string

    Name to use for this logon process

#### Comments
Requires SeTcbPrivilege (and must be enabled)

## [win32security](#win32security).LsaRegisterPolicyChangeNotification

 __LsaRegisterPolicyChangeNotification( *InformationClass*  *, NotificationEventHandle* __ )
Register an event handle to receive policy change events

#### Parameters


  -  *InformationClass* : int

    One of POLICY_NOTIFICATION_INFORMATION_CLASS contants

  -  *NotificationEventHandle* :[PyHANDLE](#pyhandle)

    Event handle to receives notification

## [win32security](#win32security).LsaRemoveAccountRights

 __LsaRemoveAccountRights( *PolicyHandle*  *, AccountSid*  *, AllRights*  *, UserRights* __ )
Removes privs from an account

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *AccountSid* :[PySID](#pysid)

    Account whose privileges will be removed

  -  *AllRights* : int

    Boolean value indicating if all privs should be removed from account

  -  *UserRights* : (str/unicode,...)

    List of privilege names to be removed (SE_*_NAME unicode constants)

#### Comments
If AllRights parm is true, account is *deleted*
Accepts keyword args.

## [win32security](#win32security).LsaRetrievePrivateData

[PyUnicode](#pyunicode)= __LsaRetrievePrivateData( *PolicyHandle*  *, KeyName* __ )
Retreives encrypted unicode data from Lsa registry key.

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *KeyName* : string

    Registry key to read

## [win32security](#win32security).LsaSetInformationPolicy

 __LsaSetInformationPolicy( *PolicyHandle*  *, InformationClass*  *, Information* __ )
Sets policy options

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *InformationClass* : int

    POLICY_INFORMATION_CLASS value

  -  *Information* : object

    Type is dependent on InformationClass

 __InformationClass__  __Type of input expected__ PolicyAuditEventsInformation(boolean, (int, ...))
First member imdicates whether auditing is enabled or not.

## [win32security](#win32security).LsaStorePrivateData

 __LsaStorePrivateData( *PolicyHandle*  *, KeyName*  *, PrivateData* __ )
Stores encrypted unicode data under specified Lsa registry key. Returns None on success

#### Parameters


  -  *PolicyHandle* :[PyLSA_HANDLE](PyLSA.md#pylsahandle)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](win32security.md#win32securitylsaopenpolicy)

  -  *KeyName* : string

    Registry key in which to store data

  -  *PrivateData* :[PyUNICODE](#pyunicode)

    Unicode string to be encrypted and stored

## [win32security](#win32security).LsaUnregisterPolicyChangeNotification

 __LsaUnregisterPolicyChangeNotification( *InformationClass*  *, NotificationEventHandle* __ )
Stop receiving policy change notification

#### Parameters


  -  *InformationClass* : int

    POLICY_NOTIFICATION_INFORMATION_CLASS constant

  -  *NotificationEventHandle* :[PyHANDLE](#pyhandle)

    Event handle previously registered to receive policy change events

## [win32security](#win32security).MapGenericMask

int = __MapGenericMask( *AccessMask*  *, GenericMapping* __ )
Translates generic access rights into specific rights

#### Parameters


  -  *AccessMask* : int

    A bitmask of generic rights to be interpreted according to GenericMapping

  -  *GenericMapping* : (int,int,int,int)

    A tuple of 4 bitmasks (GenericRead, GenericWrite, GenericExecute, GenericAll) 

containing the standard and specific rights that correspond to the generic rights.

#### Return Value
The input AccessMask will be returned with any generic access rights translated into specific equivalents

## NOT_USED_ACCESS
 __const win32security.NOT_USED_ACCESS;__ 


## NO_INHERITANCE
 __const win32security.NO_INHERITANCE;__ 


## NO_PROPAGATE_INHERIT_ACE
 __const win32security.NO_PROPAGATE_INHERIT_ACE;__ 


## OBJECT_INHERIT_ACE
 __const win32security.OBJECT_INHERIT_ACE;__ 


## OWNER_SECURITY_INFORMATION
 __const win32security.OWNER_SECURITY_INFORMATION;__ 
Indicates the owner identifier of the object is being referenced.

## [win32security](#win32security).OpenProcessToken

[PyHANDLE](#pyhandle)= __OpenProcessToken( *processHandle*  *, desiredAccess* __ )
Opens the access token associated with a process.

#### Parameters


  -  *processHandle* : int

    The handle of the process to open.

  -  *desiredAccess* : int

    Desired access to process

## [win32security](#win32security).OpenThreadToken

[PyHandle](#pyhandle)= __OpenThreadToken( *handle*  *, desiredAccess*  *, openAsSelf* __ )
Opens the access token associated with a thread.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    handle to thread

  -  *desiredAccess* : int

    access to process

  -  *openAsSelf* : int

    Flag for process or thread security

## POLICY_ALL_ACCESS
 __const win32security.POLICY_ALL_ACCESS;__ 


## POLICY_AUDIT_EVENT_FAILURE
 __const win32security.POLICY_AUDIT_EVENT_FAILURE;__ 
Generate audit records for failed attempts to cause an event of this type to occur.

## POLICY_AUDIT_EVENT_NONE
 __const win32security.POLICY_AUDIT_EVENT_NONE;__ 
Do not generate audit records for events of this type.

## POLICY_AUDIT_EVENT_SUCCESS
 __const win32security.POLICY_AUDIT_EVENT_SUCCESS;__ 
Generate audit records for successful events of this type.

## POLICY_AUDIT_EVENT_UNCHANGED
 __const win32security.POLICY_AUDIT_EVENT_UNCHANGED;__ 
For set operations, specify this value to leave the current options unchanged. This is the default.

## POLICY_AUDIT_LOG_ADMIN
 __const win32security.POLICY_AUDIT_LOG_ADMIN;__ 


## POLICY_CREATE_ACCOUNT
 __const win32security.POLICY_CREATE_ACCOUNT;__ 


## POLICY_CREATE_PRIVILEGE
 __const win32security.POLICY_CREATE_PRIVILEGE;__ 


## POLICY_CREATE_SECRET
 __const win32security.POLICY_CREATE_SECRET;__ 


## POLICY_EXECUTE
 __const win32security.POLICY_EXECUTE;__ 


## POLICY_GET_PRIVATE_INFORMATION
 __const win32security.POLICY_GET_PRIVATE_INFORMATION;__ 


## POLICY_LOOKUP_NAMES
 __const win32security.POLICY_LOOKUP_NAMES;__ 


## POLICY_NOTIFICATION
 __const win32security.POLICY_NOTIFICATION;__ 


## POLICY_READ
 __const win32security.POLICY_READ;__ 


## POLICY_SERVER_ADMIN
 __const win32security.POLICY_SERVER_ADMIN;__ 


## POLICY_SET_AUDIT_REQUIREMENTS
 __const win32security.POLICY_SET_AUDIT_REQUIREMENTS;__ 


## POLICY_SET_DEFAULT_QUOTA_LIMITS
 __const win32security.POLICY_SET_DEFAULT_QUOTA_LIMITS;__ 


## POLICY_TRUST_ADMIN
 __const win32security.POLICY_TRUST_ADMIN;__ 


## POLICY_VIEW_AUDIT_INFORMATION
 __const win32security.POLICY_VIEW_AUDIT_INFORMATION;__ 


## POLICY_VIEW_LOCAL_INFORMATION
 __const win32security.POLICY_VIEW_LOCAL_INFORMATION;__ 


## POLICY_WRITE
 __const win32security.POLICY_WRITE;__ 


## PROTECTED_DACL_SECURITY_INFORMATION
 __const win32security.PROTECTED_DACL_SECURITY_INFORMATION;__ 


## PROTECTED_SACL_SECURITY_INFORMATION
 __const win32security.PROTECTED_SACL_SECURITY_INFORMATION;__ 


## PolicyAccountDomainInformation
 __const win32security.PolicyAccountDomainInformation;__ 


## PolicyAuditEventsInformation
 __const win32security.PolicyAuditEventsInformation;__ 


## PolicyAuditFullQueryInformation
 __const win32security.PolicyAuditFullQueryInformation;__ 


## PolicyAuditFullSetInformation
 __const win32security.PolicyAuditFullSetInformation;__ 


## PolicyAuditLogInformation
 __const win32security.PolicyAuditLogInformation;__ 


## PolicyDefaultQuotaInformation
 __const win32security.PolicyDefaultQuotaInformation;__ 


## PolicyDnsDomainInformation
 __const win32security.PolicyDnsDomainInformation;__ 


## PolicyLsaServerRoleInformation
 __const win32security.PolicyLsaServerRoleInformation;__ 


## PolicyModificationInformation
 __const win32security.PolicyModificationInformation;__ 


## PolicyNotifyAccountDomainInformation
 __const win32security.PolicyNotifyAccountDomainInformation;__ 


## PolicyNotifyAuditEventsInformation
 __const win32security.PolicyNotifyAuditEventsInformation;__ 


## PolicyNotifyDnsDomainInformation
 __const win32security.PolicyNotifyDnsDomainInformation;__ 


## PolicyNotifyDomainEfsInformation
 __const win32security.PolicyNotifyDomainEfsInformation;__ 


## PolicyNotifyDomainKerberosTicketInformation
 __const win32security.PolicyNotifyDomainKerberosTicketInformation;__ 


## PolicyNotifyMachineAccountPasswordInformation
 __const win32security.PolicyNotifyMachineAccountPasswordInformation;__ 


## PolicyNotifyServerRoleInformation
 __const win32security.PolicyNotifyServerRoleInformation;__ 


## PolicyPdAccountInformation
 __const win32security.PolicyPdAccountInformation;__ 


## PolicyPrimaryDomainInformation
 __const win32security.PolicyPrimaryDomainInformation;__ 


## PolicyReplicaSourceInformation
 __const win32security.PolicyReplicaSourceInformation;__ 


## PolicyServerDisabled
 __const win32security.PolicyServerDisabled;__ 


## PolicyServerDisabled
 __const win32security.PolicyServerDisabled;__ 


## PolicyServerEnabled
 __const win32security.PolicyServerEnabled;__ 


## PolicyServerEnabled
 __const win32security.PolicyServerEnabled;__ 


## PolicyServerRoleBackup
 __const win32security.PolicyServerRoleBackup;__ 


## PolicyServerRolePrimary
 __const win32security.PolicyServerRolePrimary;__ 


## [win32security](#win32security).QuerySecurityPackageInfo

dict = __QuerySecurityPackageInfo( *PackageName* __ )
Retrieves parameters for a security package

#### Parameters


  -  *PackageName* :[PyUNICODE](#pyunicode)

    Name of the security package to query

#### Return Value
Returns a dictionary representing a SecPkgInfo struct

## REVOKE_ACCESS
 __const win32security.REVOKE_ACCESS;__ 


## [win32security](#win32security).RevertToSelf

 __RevertToSelf(__ )
Terminates the impersonation of a client application.

## SACL_SECURITY_INFORMATION
 __const win32security.SACL_SECURITY_INFORMATION;__ 
Indicates the system ACL of the object is being referenced.

## SANDBOX_INERT
 __const win32security.SANDBOX_INERT;__ 


## SDDL_REVISION_1
 __const win32security.SDDL_REVISION_1;__ 


## SECPKG_CRED_BOTH
 __const win32security.SECPKG_CRED_BOTH;__ 


## SECPKG_CRED_INBOUND
 __const win32security.SECPKG_CRED_INBOUND;__ 


## SECPKG_CRED_OUTBOUND
 __const win32security.SECPKG_CRED_OUTBOUND;__ 


## SECPKG_FLAG_ACCEPT_WIN32_NAME
 __const win32security.SECPKG_FLAG_ACCEPT_WIN32_NAME;__ 


## SECPKG_FLAG_CLIENT_ONLY
 __const win32security.SECPKG_FLAG_CLIENT_ONLY;__ 


## SECPKG_FLAG_CONNECTION
 __const win32security.SECPKG_FLAG_CONNECTION;__ 


## SECPKG_FLAG_DATAGRAM
 __const win32security.SECPKG_FLAG_DATAGRAM;__ 


## SECPKG_FLAG_EXTENDED_ERROR
 __const win32security.SECPKG_FLAG_EXTENDED_ERROR;__ 


## SECPKG_FLAG_IMPERSONATION
 __const win32security.SECPKG_FLAG_IMPERSONATION;__ 


## SECPKG_FLAG_INTEGRITY
 __const win32security.SECPKG_FLAG_INTEGRITY;__ 


## SECPKG_FLAG_MULTI_REQUIRED
 __const win32security.SECPKG_FLAG_MULTI_REQUIRED;__ 


## SECPKG_FLAG_PRIVACY
 __const win32security.SECPKG_FLAG_PRIVACY;__ 


## SECPKG_FLAG_STREAM
 __const win32security.SECPKG_FLAG_STREAM;__ 


## SECPKG_FLAG_TOKEN_ONLY
 __const win32security.SECPKG_FLAG_TOKEN_ONLY;__ 


## [win32security](#win32security).SECURITY_ATTRIBUTES

PySECURITY_ATTRIBUTES = __SECURITY_ATTRIBUTES(__ )
Creates a new[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)object.

## SECURITY_CREATOR_SID_AUTHORITY
 __const win32security.SECURITY_CREATOR_SID_AUTHORITY;__ 


## [win32security](#win32security).SECURITY_DESCRIPTOR

PySECURITY_DESCRIPTOR = __SECURITY_DESCRIPTOR(__ )
Creates a new[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)object.

## SECURITY_LOCAL_SID_AUTHORITY
 __const win32security.SECURITY_LOCAL_SID_AUTHORITY;__ 


## SECURITY_NON_UNIQUE_AUTHORITY
 __const win32security.SECURITY_NON_UNIQUE_AUTHORITY;__ 


## SECURITY_NT_AUTHORITY
 __const win32security.SECURITY_NT_AUTHORITY;__ 


## SECURITY_NULL_SID_AUTHORITY
 __const win32security.SECURITY_NULL_SID_AUTHORITY;__ 


## SECURITY_RESOURCE_MANAGER_AUTHORITY
 __const win32security.SECURITY_RESOURCE_MANAGER_AUTHORITY;__ 


## SECURITY_WORLD_SID_AUTHORITY
 __const win32security.SECURITY_WORLD_SID_AUTHORITY;__ 


## SET_ACCESS
 __const win32security.SET_ACCESS;__ 


## SET_AUDIT_FAILURE
 __const win32security.SET_AUDIT_FAILURE;__ 


## SET_AUDIT_SUCCESS
 __const win32security.SET_AUDIT_SUCCESS;__ 


## SE_DACL_AUTO_INHERITED
 __const win32security.SE_DACL_AUTO_INHERITED;__ 
win2k and up

## SE_DACL_DEFAULTED
 __const win32security.SE_DACL_DEFAULTED;__ 


## SE_DACL_PRESENT
 __const win32security.SE_DACL_PRESENT;__ 


## SE_DACL_PROTECTED
 __const win32security.SE_DACL_PROTECTED;__ 
win2k and up

## SE_DS_OBJECT
 __const win32security.SE_DS_OBJECT;__ 


## SE_DS_OBJECT_ALL
 __const win32security.SE_DS_OBJECT_ALL;__ 


## SE_FILE_OBJECT
 __const win32security.SE_FILE_OBJECT;__ 


## SE_GROUP_DEFAULTED
 __const win32security.SE_GROUP_DEFAULTED;__ 


## SE_GROUP_ENABLED
 __const win32security.SE_GROUP_ENABLED;__ 


## SE_GROUP_ENABLED_BY_DEFAULT
 __const win32security.SE_GROUP_ENABLED_BY_DEFAULT;__ 


## SE_GROUP_LOGON_ID
 __const win32security.SE_GROUP_LOGON_ID;__ 


## SE_GROUP_MANDATORY
 __const win32security.SE_GROUP_MANDATORY;__ 


## SE_GROUP_OWNER
 __const win32security.SE_GROUP_OWNER;__ 


## SE_GROUP_RESOURCE
 __const win32security.SE_GROUP_RESOURCE;__ 


## SE_GROUP_USE_FOR_DENY_ONLY
 __const win32security.SE_GROUP_USE_FOR_DENY_ONLY;__ 


## SE_KERNEL_OBJECT
 __const win32security.SE_KERNEL_OBJECT;__ 


## SE_LMSHARE
 __const win32security.SE_LMSHARE;__ 


## SE_OWNER_DEFAULTED
 __const win32security.SE_OWNER_DEFAULTED;__ 


## SE_PRINTER
 __const win32security.SE_PRINTER;__ 


## SE_PRIVILEGE_ENABLED
 __const win32security.SE_PRIVILEGE_ENABLED;__ 


## SE_PRIVILEGE_ENABLED_BY_DEFAULT
 __const win32security.SE_PRIVILEGE_ENABLED_BY_DEFAULT;__ 


## SE_PRIVILEGE_REMOVED
 __const win32security.SE_PRIVILEGE_REMOVED;__ 


## SE_PRIVILEGE_USED_FOR_ACCESS
 __const win32security.SE_PRIVILEGE_USED_FOR_ACCESS;__ 


## SE_PROVIDER_DEFINED_OBJECT
 __const win32security.SE_PROVIDER_DEFINED_OBJECT;__ 


## SE_REGISTRY_KEY
 __const win32security.SE_REGISTRY_KEY;__ 


## SE_REGISTRY_WOW64_32KEY
 __const win32security.SE_REGISTRY_WOW64_32KEY;__ 


## SE_SACL_AUTO_INHERITED
 __const win32security.SE_SACL_AUTO_INHERITED;__ 
win2k and up

## SE_SACL_DEFAULTED
 __const win32security.SE_SACL_DEFAULTED;__ 


## SE_SACL_PRESENT
 __const win32security.SE_SACL_PRESENT;__ 


## SE_SACL_PROTECTED
 __const win32security.SE_SACL_PROTECTED;__ 
win2k and up

## SE_SELF_RELATIVE
 __const win32security.SE_SELF_RELATIVE;__ 


## SE_SERVICE
 __const win32security.SE_SERVICE;__ 


## SE_UNKNOWN_OBJECT_TYPE
 __const win32security.SE_UNKNOWN_OBJECT_TYPE;__ 


## SE_WINDOW_OBJECT
 __const win32security.SE_WINDOW_OBJECT;__ 


## SE_WMIGUID_OBJECT
 __const win32security.SE_WMIGUID_OBJECT;__ 


## [win32security](#win32security).SID

PySID = __SID(__ )
Creates a new[PySID](#pysid)object.

## STYPE_DEVICE
 __const win32security.STYPE_DEVICE;__ 


## STYPE_DISKTREE
 __const win32security.STYPE_DISKTREE;__ 


## STYPE_IPC
 __const win32security.STYPE_IPC;__ 


## STYPE_PRINTQ
 __const win32security.STYPE_PRINTQ;__ 


## STYPE_SPECIAL
 __const win32security.STYPE_SPECIAL;__ 


## STYPE_TEMPORARY
 __const win32security.STYPE_TEMPORARY;__ 


## SUB_CONTAINERS_AND_OBJECTS_INHERIT
 __const win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT;__ 


## SUB_CONTAINERS_ONLY_INHERIT
 __const win32security.SUB_CONTAINERS_ONLY_INHERIT;__ 


## SUB_OBJECTS_ONLY_INHERIT
 __const win32security.SUB_OBJECTS_ONLY_INHERIT;__ 


## SUCCESSFUL_ACCESS_ACE_FLAG
 __const win32security.SUCCESSFUL_ACCESS_ACE_FLAG;__ 


## SYSTEM_AUDIT_ACE_TYPE
 __const win32security.SYSTEM_AUDIT_ACE_TYPE;__ 
System-audit ACE that uses the SYSTEM_AUDIT_ACE structure.

## SYSTEM_AUDIT_OBJECT_ACE_TYPE
 __const win32security.SYSTEM_AUDIT_OBJECT_ACE_TYPE;__ 


## SecurityAnonymous
 __const win32security.SecurityAnonymous;__ 


## SecurityDelegation
 __const win32security.SecurityDelegation;__ 


## SecurityIdentification
 __const win32security.SecurityIdentification;__ 


## SecurityImpersonation
 __const win32security.SecurityImpersonation;__ 


## [win32security](#win32security).SetFileSecurity

 __SetFileSecurity( *filename*  *, info*  *, security* __ )
Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


  -  *filename* : string

    The name of the file

  -  *info* : int

    The type of information to set.

  -  *security* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information

## [win32security](#win32security).SetKernelObjectSecurity

 __SetKernelObjectSecurity( *handle*  *, info*  *, security* __ )
Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to an object for which security information will be set.

  -  *info* : int

    The type of information to set - combination of SECURITY_INFORMATION values

  -  *security* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information

## [win32security](#win32security).SetNamedSecurityInfo

 __SetNamedSecurityInfo( *ObjectName*  *, ObjectType*  *, SecurityInfo*  *, Owner*  *, Group*  *, Dacl*  *, Sacl* __ )
Sets security info for an object by name

#### Parameters


  -  *ObjectName* : str/unicode

    Name of object

  -  *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

  -  *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

  -  *Owner* :[PySID](#pysid)

    Sid to set as owner of object, can be None

  -  *Group* :[PySID](#pysid)

    Group Sid, can be None

  -  *Dacl* :[PyACL](#pyacl)

    Discretionary ACL to set for object, can be None

  -  *Sacl* :[PyACL](#pyacl)

    System Audit ACL to set for object, can be None

## [win32security](#win32security).SetSecurityInfo

 __SetSecurityInfo( *handle*  *, ObjectType*  *, SecurityInfo*  *, Owner*  *, Group*  *, Dacl*  *, Sacl* __ )
Sets security info for an object by handle

#### Parameters


  -  *handle* : int/[PyHANDLE](#pyhandle)

    Handle to object

  -  *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

  -  *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

  -  *Owner* :[PySID](#pysid)

    Sid to set as owner of object, can be None

  -  *Group* :[PySID](#pysid)

    Group Sid, can be None

  -  *Dacl* :[PyACL](#pyacl)

    Discretionary ACL to set for object, can be None

  -  *Sacl* :[PyACL](#pyacl)

    System Audit ACL to set for object, can be None

## [win32security](#win32security).SetThreadToken

 __SetThreadToken( *Thread*  *, Token* __ )
Assigns an impersonation token to a thread. The function 

can also cause a thread to stop using an impersonation token.

#### Parameters


  -  *Thread* :[PyHANDLE](#pyhandle)

    Handle to a thread.  Use None to indicate calling thread.

  -  *Token* :[PyHANDLE](#pyhandle)

    Handle to an impersonation token.  Use None to end impersonation.

## [win32security](#win32security).SetTokenInformation

 __SetTokenInformation( *TokenHandle*  *, TokenInformationClass*  *, TokenInformation* __ )
Set a specified type of information in an access token

#### Parameters


  -  *TokenHandle* :[PyHANDLE](#pyhandle)

    Handle to an access token to be modified

  -  *TokenInformationClass* : int

    Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information to be modfied

  -  *TokenInformation* : object

    Type is dependent on TokenInformationClass


## [win32security](#win32security).SetUserObjectSecurity

 __SetUserObjectSecurity( *handle*  *, info*  *, security* __ )
Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to an object for which security information will be set.

  -  *info* : int

    The type of information to set - combination of SECURITY_INFORMATION values

  -  *security* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    The security information

## SidTypeAlias
 __const win32security.SidTypeAlias;__ 
Indicates an alias SID.

## SidTypeComputer
 __const win32security.SidTypeComputer;__ 
Indicates a computer SID

## SidTypeDeletedAccount
 __const win32security.SidTypeDeletedAccount;__ 
Indicates an SID for a deleted account.

## SidTypeDomain
 __const win32security.SidTypeDomain;__ 
Indicates a domain SID.

## SidTypeGroup
 __const win32security.SidTypeGroup;__ 
Indicates a group SID.

## SidTypeInvalid
 __const win32security.SidTypeInvalid;__ 
Indicates an invalid SID.

## SidTypeUnknown
 __const win32security.SidTypeUnknown;__ 
Indicates an unknown SID type.

## SidTypeUser
 __const win32security.SidTypeUser;__ 
Indicates a user SID.

## SidTypeWellKnownGroup
 __const win32security.SidTypeWellKnownGroup;__ 
Indicates an SID for a well-known group.

## TOKEN_ADJUST_DEFAULT
 __const win32security.TOKEN_ADJUST_DEFAULT;__ 
Required to change the default ACL, primary group, or owner of an access token.

## TOKEN_ADJUST_GROUPS
 __const win32security.TOKEN_ADJUST_GROUPS;__ 
Required to change the groups specified in an access token.

## TOKEN_ADJUST_PRIVILEGES
 __const win32security.TOKEN_ADJUST_PRIVILEGES;__ 
Required to change the privileges specified in an access token.

## TOKEN_ALL_ACCESS
 __const win32security.TOKEN_ALL_ACCESS;__ 
Combines the STANDARD_RIGHTS_REQUIRED standard access rights and all individual access rights for tokens.

## TOKEN_ASSIGN_PRIMARY
 __const win32security.TOKEN_ASSIGN_PRIMARY;__ 
Required to attach a primary token to a process in addition to the SE_CREATE_TOKEN_NAME privilege.

## TOKEN_DUPLICATE
 __const win32security.TOKEN_DUPLICATE;__ 
Required to duplicate an access token.

## TOKEN_EXECUTE
 __const win32security.TOKEN_EXECUTE;__ 
Combines the STANDARD_RIGHTS_EXECUTE standard access rights and the TOKEN_IMPERSONATE access right.

## TOKEN_IMPERSONATE
 __const win32security.TOKEN_IMPERSONATE;__ 
Required to attach an impersonation access token to a process.

## TOKEN_QUERY
 __const win32security.TOKEN_QUERY;__ 
Required to query the contents of an access token.

## TOKEN_QUERY_SOURCE
 __const win32security.TOKEN_QUERY_SOURCE;__ 
Required to query the source of an access token.

## TOKEN_READ
 __const win32security.TOKEN_READ;__ 
Combines the STANDARD_RIGHTS_READ standard access rights and the TOKEN_QUERY access right.

## TOKEN_WRITE
 __const win32security.TOKEN_WRITE;__ 
Combines the STANDARD_RIGHTS_WRITE standard access rights and the TOKEN_ADJUST_PRIVILEGES, TOKEN_ADJUST_GROUPS, and TOKEN_ADJUST_DEFAULT access rights.

## TRUSTEE_BAD_FORM
 __const win32security.TRUSTEE_BAD_FORM;__ 


## TRUSTEE_IS_ALIAS
 __const win32security.TRUSTEE_IS_ALIAS;__ 


## TRUSTEE_IS_COMPUTER
 __const win32security.TRUSTEE_IS_COMPUTER;__ 


## TRUSTEE_IS_DELETED
 __const win32security.TRUSTEE_IS_DELETED;__ 


## TRUSTEE_IS_DOMAIN
 __const win32security.TRUSTEE_IS_DOMAIN;__ 


## TRUSTEE_IS_GROUP
 __const win32security.TRUSTEE_IS_GROUP;__ 


## TRUSTEE_IS_INVALID
 __const win32security.TRUSTEE_IS_INVALID;__ 


## TRUSTEE_IS_NAME
 __const win32security.TRUSTEE_IS_NAME;__ 


## TRUSTEE_IS_OBJECTS_AND_NAME
 __const win32security.TRUSTEE_IS_OBJECTS_AND_NAME;__ 


## TRUSTEE_IS_OBJECTS_AND_SID
 __const win32security.TRUSTEE_IS_OBJECTS_AND_SID;__ 


## TRUSTEE_IS_SID
 __const win32security.TRUSTEE_IS_SID;__ 


## TRUSTEE_IS_UNKNOWN
 __const win32security.TRUSTEE_IS_UNKNOWN;__ 


## TRUSTEE_IS_USER
 __const win32security.TRUSTEE_IS_USER;__ 


## TRUSTEE_IS_WELL_KNOWN_GROUP
 __const win32security.TRUSTEE_IS_WELL_KNOWN_GROUP;__ 


## TokenImpersonation
 __const win32security.TokenImpersonation;__ 


## TokenPrimary
 __const win32security.TokenPrimary;__ 


## [win32security](#win32security).TranslateName

[PyUnicode](#pyunicode)= __TranslateName( *accountName*  *, accountNameFormat*  *, accountNameFormat*  *, numChars* __ )
Converts a directory service object name from one format to another.

#### Parameters


  -  *accountName* :[PyUnicode](#pyunicode)

    object name

  -  *accountNameFormat* : int

    A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the accountName name.

  -  *accountNameFormat* : int

    A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the desired name.

  -  *numChars=1024* : int

    Number of Unicode characters to allocate for the return buffer.

## TrustedControllersInformation
 __const win32security.TrustedControllersInformation;__ 


## TrustedDomainAuthInformation
 __const win32security.TrustedDomainAuthInformation;__ 


## TrustedDomainAuthInformationInternal
 __const win32security.TrustedDomainAuthInformationInternal;__ 


## TrustedDomainFullInformation
 __const win32security.TrustedDomainFullInformation;__ 


## TrustedDomainFullInformation2Internal
 __const win32security.TrustedDomainFullInformation2Internal;__ 


## TrustedDomainFullInformationInternal
 __const win32security.TrustedDomainFullInformationInternal;__ 


## TrustedDomainInformationBasic
 __const win32security.TrustedDomainInformationBasic;__ 


## TrustedDomainInformationEx
 __const win32security.TrustedDomainInformationEx;__ 


## TrustedDomainInformationEx2Internal
 __const win32security.TrustedDomainInformationEx2Internal;__ 


## TrustedDomainNameInformation
 __const win32security.TrustedDomainNameInformation;__ 


## TrustedPasswordInformation
 __const win32security.TrustedPasswordInformation;__ 


## TrustedPosixOffsetInformation
 __const win32security.TrustedPosixOffsetInformation;__ 


## UNPROTECTED_DACL_SECURITY_INFORMATION
 __const win32security.UNPROTECTED_DACL_SECURITY_INFORMATION;__ 


## UNPROTECTED_SACL_SECURITY_INFORMATION
 __const win32security.UNPROTECTED_SACL_SECURITY_INFORMATION;__ 
