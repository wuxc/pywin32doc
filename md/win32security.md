
## ACCESS_ALLOWED_ACE_TYPE
 **const win32security.ACCESS_ALLOWED_ACE_TYPE;** 
Access-allowed ACE that uses the ACCESS_ALLOWED_ACE structure.

## ACCESS_ALLOWED_OBJECT_ACE_TYPE
 **const win32security.ACCESS_ALLOWED_OBJECT_ACE_TYPE;** 
Windows 2000/XP: Object-specific access-allowed ACE that uses the ACCESS_ALLOWED_OBJECT_ACE structure.

## ACCESS_DENIED_ACE_TYPE
 **const win32security.ACCESS_DENIED_ACE_TYPE;** 
Access-denied ACE that uses the ACCESS_DENIED_ACE structure.

## ACCESS_DENIED_OBJECT_ACE_TYPE
 **const win32security.ACCESS_DENIED_OBJECT_ACE_TYPE;** 
Windows 2000/XP: Object-specific access-denied ACE that uses the ACCESS_DENIED_OBJECT_ACE structure.

## [win32security](#README.md#win32security).ACL

PyACL = **ACL( *bufSize* ** )
Creates a new[PyACL](#README.md#PyACL)object.

#### Parameters


     *bufSize=64* : int

    The size of the buffer for the ACL.

## ACL_REVISION
 **const win32security.ACL_REVISION;** 


## ACL_REVISION_DS
 **const win32security.ACL_REVISION_DS;** 


## [win32security](#README.md#win32security).AcceptSecurityContext

(int, long, int) = **AcceptSecurityContext( *Credential*  *, Context*  *, pInput*  *, ContextReq*  *, TargetDataRep*  *, NewContext*  *, pOutput* ** )
Builds security context between server and client

#### Parameters


     *Credential* :[PyCredHandle](#README.md#PyCredHandle)

    Handle to server's credentials (see AcquireCredentialsHandle)

     *Context* :[PyCtxtHandle](#README.md#PyCtxtHandle)

    Use None on initial call, then handle returned in NewContext thereafter

     *pInput* :[PySecBufferDesc](#README.md#PySecBufferDesc)

    Data buffer received from client

     *ContextReq* : int

    Combination of ASC_REQ_* flags

     *TargetDataRep* : int

    One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP

     *NewContext* :[PyCtxtHandle](#README.md#PyCtxtHandle)

    Uninitialized context handle to receive output

     *pOutput* :[PySecBufferDesc](#README.md#PySecBufferDesc)

    Buffer that receives output data, to be passed back as pInput on subsequent calls

#### Return Value
Returns a tuple of (return code, context attributes, context expiration time)

## [win32security](#README.md#win32security).AcquireCredentialsHandle

([PyCredHandle](#README.md#PyCredHandle),[PyTime](#README.md#PyTime)) = **AcquireCredentialsHandle( *Principal*  *, Package*  *, CredentialUse*  *, LogonID*  *, AuthData* ** )
Creates a handle to credentials for use with SSPI

#### Parameters


     *Principal* : str/unicode

    Use None for current security context

     *Package* : str/unicode

    Name of security package that credentials will be used with

     *CredentialUse* : int

    Intended use of requested credentials, SECPKG_CRED_INBOUND, SECPKG_CRED_OUTBOUND, or SECPKG_CRED_BOTH

     *LogonID* : long

    LUID representing a logon session, can be None

     *AuthData* : tuple

    Sequence of 3 strings: (User, Domain, Password) - use none for existing credentials

#### Return Value
Returns credential handle and credential's expiration time

## [win32security](#README.md#win32security).AdjustTokenGroups

[PyTOKEN_GROUPS](#PyTOKEN.md#PyTOKENGROUPS)= **AdjustTokenGroups( *TokenHandle*  *, ResetToDefault*  *, NewState* ** )
Sets the groups associated to an access token.

#### Parameters


     *TokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to access token to be modified

     *ResetToDefault* : boolean

    Sets groups to default enabled/disabled states,

     *NewState* :[PyTOKEN_GROUPS](#PyTOKEN.md#PyTOKENGROUPS)

    Groups and attributes to be set for token

#### Comments
Accepts keyword args.

#### Return Value
Returns previous state of groups modified

## [win32security](#README.md#win32security).AdjustTokenPrivileges

[PyTOKEN_PRIVILEGES](#PyTOKEN.md#PyTOKENPRIVILEGES)= **AdjustTokenPrivileges( *TokenHandle*  *, bDisableAllPrivileges*  *, NewState* ** )
Enables or disables privileges for an access token.

#### Parameters


     *TokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token

     *bDisableAllPrivileges* : int

    Flag for disabling all privileges

     *NewState* :[PyTOKEN_PRIVILEGES](#PyTOKEN.md#PyTOKENPRIVILEGES)

    The new state, can be None if bDisableAllPrivileges is True

#### Comments
Accepts keyword args.

#### Return Value
Returns modified privileges for later restoral.  Privileges deleted from the token using 

SE_PRIVILEGE_REMOVED are not returned.

## [win32security](#README.md#win32security).AllocateLocallyUniqueId

 **AllocateLocallyUniqueId(** )
Creates a new LUID

## AuditCategoryAccountLogon
 **const win32security.AuditCategoryAccountLogon;** 


## AuditCategoryAccountManagement
 **const win32security.AuditCategoryAccountManagement;** 


## AuditCategoryDetailedTracking
 **const win32security.AuditCategoryDetailedTracking;** 


## AuditCategoryDirectoryServiceAccess
 **const win32security.AuditCategoryDirectoryServiceAccess;** 


## AuditCategoryLogon
 **const win32security.AuditCategoryLogon;** 


## AuditCategoryObjectAccess
 **const win32security.AuditCategoryObjectAccess;** 


## AuditCategoryPolicyChange
 **const win32security.AuditCategoryPolicyChange;** 


## AuditCategoryPrivilegeUse
 **const win32security.AuditCategoryPrivilegeUse;** 


## AuditCategorySystem
 **const win32security.AuditCategorySystem;** 


## CONTAINER_INHERIT_ACE
 **const win32security.CONTAINER_INHERIT_ACE;** 


## [win32security](#README.md#win32security).CheckTokenMembership

bool = **CheckTokenMembership( *TokenHandle*  *, SidToCheck* ** )
Checks if a SID is enabled in a token

#### Parameters


     *TokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token, current process token used if None

     *SidToCheck* :[PySID](#README.md#PySID)

    Sid to be checked for presence in token

## [win32security](#README.md#win32security).ConvertSecurityDescriptorToStringSecurityDescriptor

string = **ConvertSecurityDescriptorToStringSecurityDescriptor( *SecurityDescriptor*  *, RequestedStringSDRevision*  *, SecurityInformation* ** )
Return string representation of a SECURITY_DESCRIPTOR

#### Parameters


     *SecurityDescriptor* :[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)

    PySECURITY_DESCRIPTOR object

     *RequestedStringSDRevision* : int

    Only SDDL_REVISION_1 currently valid

     *SecurityInformation* : int

    Combination of bit flags from SECURITY_INFORMATION enum

## [win32security](#README.md#win32security).ConvertSidToStringSid

string = **ConvertSidToStringSid( *Sid* ** )
Return string representation of a SID

#### Parameters


     *Sid* :[PySID](#README.md#PySID)

    PySID object

## [win32security](#README.md#win32security).ConvertStringSecurityDescriptorToSecurityDescriptor

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **ConvertStringSecurityDescriptorToSecurityDescriptor( *StringSecurityDescriptor*  *, StringSDRevision* ** )
Turns string representation of a SECURITY_DESCRIPTOR into the real thing

#### Parameters


     *StringSecurityDescriptor* : string

    String representation of a SECURITY_DESCRIPTOR

     *StringSDRevision* : int

    Only SDDL_REVISION_1 currently valid

## [win32security](#README.md#win32security).ConvertStringSidToSid

[PySID](#README.md#PySID)= **ConvertStringSidToSid( *StringSid* ** )
Creates a SID from a string representation

#### Parameters


     *StringSid* : string

    String representation of a SID

## [win32security](#README.md#win32security).CreateRestrictedToken

[PyHANDLE](#README.md#PyHANDLE)= **CreateRestrictedToken( *ExistingTokenHandle*  *, Flags*  *, SidsToDisable*  *, PrivilegesToDelete*  *, SidsToRestrict* ** )
Creates a restricted copy of an access token with reduced privs - requires win2K or higher

#### Parameters


     *ExistingTokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token (see[win32security::LogonUser](#win32security.md#win32securityLogonUser),[win32security::OpenProcessToken](#win32security.md#win32securityOpenProcessToken)

     *Flags* : int

    Valid values are zero or a combination of DISABLE_MAX_PRIVILEGE and SANDBOX_INERT

     *SidsToDisable* : ([PySID_AND_ATTRIBUTES](#PySID.md#PySIDAND_ATTRIBUTES),...)

    Ssequence of[PySID_AND_ATTRIBUTES](#PySID.md#PySIDAND_ATTRIBUTES)tuples, or None

     *PrivilegesToDelete* : ([PyLUID_AND_ATTRIBUTES](#PyLUID.md#PyLUIDAND_ATTRIBUTES),...)

    Privilege LUIDS to remove from token (attributes are ignored), or None

     *SidsToRestrict* : ([PySID_AND_ATTRIBUTES](#PySID.md#PySIDAND_ATTRIBUTES),...)

    Sequence of[PySID_AND_ATTRIBUTES](#PySID.md#PySIDAND_ATTRIBUTES)tuples (attributes must be 0).  Can be None.

## [win32security](#README.md#win32security).CreateWellKnownSid

[PySID](#README.md#PySID)= **CreateWellKnownSid( *WellKnownSidType*  *, DomainSid* ** )
Returns one of the predefined well known sids

#### Parameters


     *WellKnownSidType* : int

    One of the Win*Sid constants

     *DomainSid=None* :[PySID](#README.md#PySID)

    Domain for the new SID, or None for local machine

## [win32security](#README.md#win32security).CryptEnumProviders

[([PyUnicode](#README.md#PyUnicode),int),...] = **CryptEnumProviders(** )
List cryptography providers

#### Return Value
Returns a sequence of tuples containing provider name and type

## DACL_SECURITY_INFORMATION
 **const win32security.DACL_SECURITY_INFORMATION;** 
Indicates the discretionary ACL of the object is being referenced.

## DENY_ACCESS
 **const win32security.DENY_ACCESS;** 


## DISABLE_MAX_PRIVILEGE
 **const win32security.DISABLE_MAX_PRIVILEGE;** 


## DS_SPN_ADD_SPN_OP
 **const win32security.DS_SPN_ADD_SPN_OP;** 


## DS_SPN_DELETE_SPN_OP
 **const win32security.DS_SPN_DELETE_SPN_OP;** 


## DS_SPN_DNS_HOST
 **const win32security.DS_SPN_DNS_HOST;** 


## DS_SPN_DN_HOST
 **const win32security.DS_SPN_DN_HOST;** 


## DS_SPN_DOMAIN
 **const win32security.DS_SPN_DOMAIN;** 


## DS_SPN_NB_DOMAIN
 **const win32security.DS_SPN_NB_DOMAIN;** 


## DS_SPN_NB_HOST
 **const win32security.DS_SPN_NB_HOST;** 


## DS_SPN_REPLACE_SPN_OP
 **const win32security.DS_SPN_REPLACE_SPN_OP;** 


## DS_SPN_SERVICE
 **const win32security.DS_SPN_SERVICE;** 


## [win32security](#README.md#win32security).DsBind

[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)= **DsBind( *DomainController*  *, DnsDomainName* ** )
Creates a connection to a directory service

#### Parameters


     *DomainController* :[PyUnicode](#README.md#PyUnicode)

    Name of domain controller to contact, can be None

     *DnsDomainName* :[PyUnicode](#README.md#PyUnicode)

    Dotted name of domain to bind to, can be None

## [win32security](#README.md#win32security).DsCrackNames

[ (status, domain, name) ] = **DsCrackNames( *hds*  *, flags*  *, formatOffered*  *, formatDesired*  *, names* ** )
Converts an array of directory service object names from one format to another.

#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

     *flags* : int

    

     *formatOffered* : int

    

     *formatDesired* : int

    

     *names* : [name, ...]

    

## [win32security](#README.md#win32security).DsGetDcName

dict = **DsGetDcName( *computerName*  *, domainName*  *, domainGUID*  *, siteName*  *, flags* ** )
Returns the name of a domain controller (DC) in a specified domain. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.

#### Parameters


     *computerName=None* :[PyUnicode](#README.md#PyUnicode)

    

     *domainName=None* :[PyUnicode](#README.md#PyUnicode)

    

     *domainGUID=None* :[PyIID](#README.md#PyIID)

    

     *siteName=None* :[PyUnicode](#README.md#PyUnicode)

    

     *flags=0* : int

    

#### Comments
This function supports keyword arguments.

## [win32security](#README.md#win32security).DsGetSpn

([PyUnicode](#README.md#PyUnicode),...) = **DsGetSpn( *ServiceType*  *, ServiceClass*  *, ServiceName*  *, InstancePort*  *, InstanceNames*  *, InstancePorts* ** )
Compose one or more service principal names to be registered using[win32security::DsWriteAccountSpn](#win32security.md#win32securityDsWriteAccountSpn)

#### Parameters


     *ServiceType* : int

    Type of Spn to create, one of the DS_SPN_* constants

     *ServiceClass* :[PyUnicode](#README.md#PyUnicode)

    Arbitrary string that describes type of service, eg http

     *ServiceName* :[PyUnicode](#README.md#PyUnicode)

    Name of service, can be None (not required for DS_SPN_*_HOST Spn's)

     *InstancePort=0* : int

    Port nbr for service instance, use 0 for no port

     *InstanceNames=None* : ([PyUnicode](#README.md#PyUnicode),...)

    A sequence of service instance names, can be None - not required for for host Spn's

     *InstancePorts=None* : (int,...)

    A sequence of extra instance ports.  If specified, must be same length as InstanceNames.

## [win32security](#README.md#win32security).DsListDomainsInSite

[[PyDS_NAME_RESULT_ITEM](#PyDS.md#PyDSNAME_RESULT_ITEM), ...] = **DsListDomainsInSite( *hds* ** )


#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

## [win32security](#README.md#win32security).DsListInfoForServer

[[PyDS_NAME_RESULT_ITEM](#PyDS.md#PyDSNAME_RESULT_ITEM), ...] = **DsListInfoForServer( *hds*  *, server* ** )
Lists miscellaneous information for a server.

#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

     *server* :[PyUnicode](#README.md#PyUnicode)

    

## [win32security](#README.md#win32security).DsListRoles

[[PyDS_NAME_RESULT_ITEM](#PyDS.md#PyDSNAME_RESULT_ITEM), ...] = **DsListRoles( *hds* ** )


#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

## [win32security](#README.md#win32security).DsListServersInSite

[[PyDS_NAME_RESULT_ITEM](#PyDS.md#PyDSNAME_RESULT_ITEM), ...] = **DsListServersInSite( *hds*  *, site* ** )


#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

     *site* :[PyUnicode](#README.md#PyUnicode)

    

## [win32security](#README.md#win32security).DsListServersInSite

[[PyDS_NAME_RESULT_ITEM](#PyDS.md#PyDSNAME_RESULT_ITEM), ...] = **DsListServersInSite( *hds*  *, domain*  *, site* ** )


#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

     *domain* :[PyUnicode](#README.md#PyUnicode)

    

     *site* :[PyUnicode](#README.md#PyUnicode)

    

## [win32security](#README.md#win32security).DsListServersInSite

[[PyDS_NAME_RESULT_ITEM](#PyDS.md#PyDSNAME_RESULT_ITEM), ...] = **DsListServersInSite( *hds* ** )


#### Parameters


     *hds* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

## [win32security](#README.md#win32security).DsUnBind

 **DsUnBind( *hDS* ** )
Closes a directory services handle created by[win32security::DsBind](#win32security.md#win32securityDsBind)

#### Parameters


     *hDS* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    A handle to a directory service as returned by[win32security::DsBind](#win32security.md#win32securityDsBind)

## [win32security](#README.md#win32security).DsWriteAccountSpn

 **DsWriteAccountSpn( *hDS*  *, Operation*  *, Account*  *, Spns* ** )
Associates a set of service principal names with an account

#### Parameters


     *hDS* :[PyDS_HANDLE](#PyDS.md#PyDSHANDLE)

    Directory service handle as returned from[win32security::DsBind](#win32security.md#win32securityDsBind)

     *Operation* : int

    Constant from DS_SPN_WRITE_OP enum

     *Account* :[PyUnicode](#README.md#PyUnicode)

    Distinguished name of account whose Spn's will be modified

     *Spns* : ([PyUnicode](#README.md#PyUnicode),...)

    A sequence of target Spn's as returned by[win32security::DsGetSpn](#win32security.md#win32securityDsGetSpn)

## [win32security](#README.md#win32security).DuplicateToken

[PyHANDLE](#README.md#PyHANDLE)= **DuplicateToken( *ExistingTokenHandle*  *, ImpersonationLevel* ** )
Creates a copy of an access token with specified impersonation level

#### Parameters


     *ExistingTokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token (see[win32security::LogonUser](#win32security.md#win32securityLogonUser),[win32security::OpenProcessToken](#win32security.md#win32securityOpenProcessToken))

     *ImpersonationLevel* : int

    A value from SECURITY_IMPERSONATION_LEVEL enum

## [win32security](#README.md#win32security).DuplicateTokenEx

[PyHANDLE](#README.md#PyHANDLE)= **DuplicateTokenEx( *ExistingToken*  *, ImpersonationLevel*  *, DesiredAccess*  *, TokenType*  *, TokenAttributes* ** )
Extended version of DuplicateToken.

#### Parameters


     *ExistingToken* :[PyHANDLE](#README.md#PyHANDLE)

    Logon token opened with TOKEN_DUPLICATE access

     *ImpersonationLevel* : int

    One of win32security.Security* values

     *DesiredAccess* : int

    Type of access required for the handle, combination of win32security.TOKEN_* flags

     *TokenType* : int

    Type of token to be created, TokenPrimary or TokenImpersonation

     *TokenAttributes=None* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies security and inheritance for the new handle.  None results in default DACL and no inheritance,

#### Comments
Accepts keyword arguments

## [win32security](#README.md#win32security).EnumerateSecurityPackages

(dict,...) = **EnumerateSecurityPackages(** )
List available security packages as a sequence of dictionaries representing SecPkgInfo structures

## FAILED_ACCESS_ACE_FLAG
 **const win32security.FAILED_ACCESS_ACE_FLAG;** 


## GRANT_ACCESS
 **const win32security.GRANT_ACCESS;** 


## GROUP_SECURITY_INFORMATION
 **const win32security.GROUP_SECURITY_INFORMATION;** 
Indicates the primary group identifier of the object is being referenced.

## [win32security](#README.md#win32security).GetBinarySid

[PySID](#README.md#PySID)= **GetBinarySid( *SID* ** )
Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.

#### Parameters


     *SID* : string

    Textual representation of a SID. Textual SID example: S-1-5-32-544

## [win32security](#README.md#win32security).GetFileSecurity

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **GetFileSecurity( *filename*  *, info* ** )
Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


     *filename* : string

    The name of the file

     *info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION* : int

    Flags that specify the information requested.

#### Comments
This function reportedly will not return the INHERITED_ACE flag on some Windows XP SP1 systems 

Use GetNamedSecurityInfo if you encounter this problem.

## [win32security](#README.md#win32security).GetKernelObjectSecurity

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **GetKernelObjectSecurity( *handle*  *, info* ** )
Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the object

     *info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION* : int

    Flags that specify the information requested.

## [win32security](#README.md#win32security).GetNamedSecurityInfo

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **GetNamedSecurityInfo( *ObjectName*  *, ObjectType*  *, SecurityInfo* ** )
Retrieve security info for an object by name

#### Parameters


     *ObjectName* : str/unicode

    Name of object

     *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

     *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

#### Comments
Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from 

the returned PySECURITY_DESCRIPTOR

## [win32security](#README.md#win32security).GetSecurityInfo

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **GetSecurityInfo( *handle*  *, ObjectType*  *, SecurityInfo* ** )
Retrieve security info for an object by handle

#### Parameters


     *handle* : int/[PyHANDLE](#README.md#PyHANDLE)

    Handle to object

     *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

     *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

#### Comments
Separate owner, group, dacl, and sacl are not returned as they can be easily retrieved from 

the returned PySECURITY_DESCRIPTOR

## [win32security](#README.md#win32security).GetTokenInformation

object = **GetTokenInformation( *TokenHandle*  *, TokenInformationClass* ** )
Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.

#### Parameters


     *TokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token.

     *TokenInformationClass* : int

    Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.

#### Return Value
The following types are supported


## [win32security](#README.md#win32security).GetUserObjectSecurity

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **GetUserObjectSecurity( *handle*  *, info* ** )
Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the object

     *info=OWNER_SECURITY_INFORMATION | GROUP_SECURITY_INFORMATION | DACL_SECURITY_INFORMATION | SACL_SECURITY_INFORMATION* : int

    Flags that specify the information requested.

## INHERITED_ACE
 **const win32security.INHERITED_ACE;** 


## INHERIT_ONLY_ACE
 **const win32security.INHERIT_ONLY_ACE;** 


## [win32security](#README.md#win32security).ImpersonateAnonymousToken

 **ImpersonateAnonymousToken( *ThreadHandle* ** )
Cause a thread to act in the security context of an anonymous token

#### Parameters


     *ThreadHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to thread that will

## [win32security](#README.md#win32security).ImpersonateLoggedOnUser

 **ImpersonateLoggedOnUser( *handle* ** )
Impersonates a logged on user.

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a token that represents a logged-on user

## [win32security](#README.md#win32security).ImpersonateNamedPipeClient

 **ImpersonateNamedPipeClient( *handle* ** )
Impersonates a named-pipe client application.

#### Parameters


     *handle* : int

    handle of a named pipe.

## [win32security](#README.md#win32security).ImpersonateSelf

 **ImpersonateSelf( *ImpersonationLevel* ** )
Assigns an impersonation token for current security context to current process

#### Parameters


     *ImpersonationLevel* : int

    A value from SECURITY_IMPERSONATION_LEVEL enum

## [win32security](#README.md#win32security).InitializeSecurityContext

(int, int,[PyTime](#README.md#PyTime)) = **InitializeSecurityContext( *Credential*  *, Context*  *, TargetName*  *, ContextReq*  *, TargetDataRep*  *, pInput*  *, NewContext*  *, pOutput* ** )
Creates a security context based on credentials created by AcquireCredentialsHandle

#### Parameters


     *Credential* :[PyCredHandle](#README.md#PyCredHandle)

    A credentials handle as returned by[win32security::AcquireCredentialsHandle](#win32security.md#win32securityAcquireCredentialsHandle)

     *Context* :[PyCtxtHandle](#README.md#PyCtxtHandle)

    Use None on initial call, then handle returned in NewContext thereafter

     *TargetName* : str/unicode

    Target of context, security package specific - Use None with NTLM

     *ContextReq* : int

    Combination of ISC_REQ_* flags

     *TargetDataRep* : int

    One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP

     *pInput* :[PySecBufferDesc](#README.md#PySecBufferDesc)

    Data buffer - use None initially

     *NewContext* :[PyCtxtHandle](#README.md#PyCtxtHandle)

    Uninitialized context handle to receive output

     *pOutput* :[PySecBufferDesc](#README.md#PySecBufferDesc)

    Buffer that receives output data for subsequent calls

#### Return Value
Return value is a tuple of (return code, attribute flags, expiration time)

## [win32security](#README.md#win32security).IsTokenRestricted

bool = **IsTokenRestricted( *TokenHandle* ** )
Checks if a token contains restricted sids

#### Parameters


     *TokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token

## LABEL_SECURITY_INFORMATION
 **const win32security.LABEL_SECURITY_INFORMATION;** 


## LOGON32_LOGON_BATCH
 **const win32security.LOGON32_LOGON_BATCH;** 
This logon type is intended for batch servers, where processes may be executing on behalf of a user without their direct intervention; or for higher performance servers that process many clear-text authentication attempts at a time, such as mail or web servers. LogonUser does not cache credentials for this logon type.

## LOGON32_LOGON_INTERACTIVE
 **const win32security.LOGON32_LOGON_INTERACTIVE;** 
This logon type is intended for users who will be interactively using the machine, such as a user being logged on by a terminal server, remote shell, or similar process. This logon type has the additional expense of caching logon information for disconnected operation, and is therefore inappropriate for some client/server applications, such as a mail server.

## LOGON32_LOGON_NETWORK
 **const win32security.LOGON32_LOGON_NETWORK;** 
This logon type is intended for high performance servers to authenticate clear text passwords. LogonUser does not cache credentials for this logon type. This is the fastest logon path, but there are two limitations. First, the function returns an impersonation token, not a primary token. You cannot use this token directly in the CreateProcessAsUser function. However, you can call the DuplicateTokenEx function to convert the token to a primary token, and then use it in CreateProcessAsUser. Second, if you convert the token to a primary token and use it in CreateProcessAsUser to start a process, the new process will not be able to access other network resources, such as remote servers or printers, through the redirector.

## LOGON32_LOGON_NETWORK_CLEARTEXT
 **const win32security.LOGON32_LOGON_NETWORK_CLEARTEXT;** 


## LOGON32_LOGON_NEW_CREDENTIALS
 **const win32security.LOGON32_LOGON_NEW_CREDENTIALS;** 


## LOGON32_LOGON_SERVICE
 **const win32security.LOGON32_LOGON_SERVICE;** 
Indicates a service-type logon. The account provided must have the service privilege enabled.

## LOGON32_LOGON_UNLOCK
 **const win32security.LOGON32_LOGON_UNLOCK;** 


## LOGON32_PROVIDER_DEFAULT
 **const win32security.LOGON32_PROVIDER_DEFAULT;** 
Use the standard logon provider for the system. This is the recommended value for the dwLogonProvider parameter. It provides maximum compatibility with current and future releases of Windows NT.

## LOGON32_PROVIDER_WINNT35
 **const win32security.LOGON32_PROVIDER_WINNT35;** 
Use the Windows NT 3.5 logon provider.

## LOGON32_PROVIDER_WINNT40
 **const win32security.LOGON32_PROVIDER_WINNT40;** 
Use the Windows NT 4.0 logon provider

## LOGON32_PROVIDER_WINNT50
 **const win32security.LOGON32_PROVIDER_WINNT50;** 
Use the Negotiate protocol

## [win32security](#README.md#win32security).LogonUser

[PyHANDLE](#README.md#PyHANDLE)= **LogonUser( *Username*  *, Domain*  *, Password*  *, LogonType*  *, LogonProvider* ** )
Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.

#### Parameters


     *Username* :[PyUnicode](#README.md#PyUnicode)

    The name of the user account to log on to. 

This may also be a marshalled credential (see[win32cred::CredMarshalCredential](#win32cred.md#win32credCredMarshalCredential)).

     *Domain* :[PyUnicode](#README.md#PyUnicode)

    The name of the domain, or None for the current domain

     *Password* :[PyUnicode](#README.md#PyUnicode)

    User's password.  Use a blank string if Username contains a marshalled credential.

     *LogonType* : int

    One of LOGON32_LOGON_* values

     *LogonProvider* : int

    One of LOGON32_PROVIDER_* values

#### Comments
Accepts keyword args
On Windows 2000 and earlier, the calling process must have SE_TCB_NAME privilege.

## [win32security](#README.md#win32security).LogonUserEx

([PyHANDLE](#README.md#PyHANDLE),[PySID](#README.md#PySID), str, dict) = **LogonUserEx( *Username*  *, Domain*  *, Password*  *, LogonType*  *, LogonProvider* ** )
Log a user onto the local machine,

#### Parameters


     *Username* :[PyUnicode](#README.md#PyUnicode)

    User account, may be specified as a UPN (user@domain.com). 

This may also be a marshalled credential (see[win32cred::CredMarshalCredential](#win32cred.md#win32credCredMarshalCredential)).

     *Domain* :[PyUnicode](#README.md#PyUnicode)

    User's domain. Can be None if Username is a full UPN.

     *Password* :[PyUnicode](#README.md#PyUnicode)

    User's password.  Use a blank string if Username contains a marshalled credential.

     *LogonType* : int

    One of LOGON32_LOGON_* values

     *LogonProvider* : int

    One of LOGON32_PROVIDER_* values

#### Comments
Requires Windows XP or later
Accepts keyword args

#### Return Value
Returns access token, logon sid, profile buffer, and process quotas. 

Format of the profile buffer is not known, so returned object is subject to change.

## [win32security](#README.md#win32security).LookupAccountName

[PySID](#README.md#PySID), string, int = **LookupAccountName( *systemName*  *, accountName* ** )
Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.

#### Parameters


     *systemName* : string

    The system name, or None

     *accountName* : string

    The account name

#### Return Value
The result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.

## [win32security](#README.md#win32security).LookupAccountSid

string, string, int = **LookupAccountSid( *systemName*  *, sid* ** )
Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.

#### Parameters


     *systemName* : string

    The system name, or None

     *sid* :[PySID](#README.md#PySID)

    The SID

#### Return Value
The result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.

## [win32security](#README.md#win32security).LookupPrivilegeDisplayName

[PyUnicode](#README.md#PyUnicode)= **LookupPrivilegeDisplayName( *SystemName*  *, Name* ** )
Returns long description for a privilege name

#### Parameters


     *SystemName* : string/[PyUnicode](#README.md#PyUnicode)

    System name, local system assumed if not specified

     *Name* : string/[PyUnicode](#README.md#PyUnicode)

    Name of privilege, Se...Privilege string constants (win32security.SE_*_NAME)

## [win32security](#README.md#win32security).LookupPrivilegeName

[PyUnicode](#README.md#PyUnicode)= **LookupPrivilegeName( *SystemName*  *, luid* ** )
return the text name for a privilege LUID

#### Parameters


     *SystemName* : string/[PyUnicode](#README.md#PyUnicode)

    System name, local system assumed if not specified

     *luid* : LARGE_INTEGER

    64 bit value representing a privilege

## [win32security](#README.md#win32security).LookupPrivilegeValue

[LARGE_INTEGER](#LARGE.md#LARGEINTEGER)= **LookupPrivilegeValue( *systemName*  *, privilegeName* ** )
Retrieves the locally unique id for a privilege name

#### Parameters


     *systemName* : string

    String specifying the system, use None for local machine

     *privilegeName* : string

    String specifying the privilege (win32security.SE_*_NAME)

## [win32security](#README.md#win32security).LsaAddAccountRights

 **LsaAddAccountRights( *PolicyHandle*  *, AccountSid*  *, UserRights* ** )
Adds a list of privileges to an account

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *AccountSid* :[PySID](#README.md#PySID)

    Account to which privs will be added

     *UserRights* : (str/unicode,...)

    Sequence of privilege names (SE_*_NAME unicode constants)

#### Comments
Account is created if it doesn't already exist.
Accepts keyword args.

## [win32security](#README.md#win32security).LsaCallAuthenticationPackage

 **LsaCallAuthenticationPackage( *LsaHandle*  *, AuthenticationPackage*  *, MessageType*  *, ProtocolSubmitBuffer* ** )
Requests the services of an authentication package

#### Parameters


     *LsaHandle* :[PyLsaLogon_HANDLE](#PyLsaLogon.md#PyLsaLogonHANDLE)

    Lsa handle as returned by[win32security::LsaRegisterLogonProcess](#win32security.md#win32securityLsaRegisterLogonProcess)or[win32security::LsaConnectUntrusted](#win32security.md#win32securityLsaConnectUntrusted)

     *AuthenticationPackage* : int

    Id of authentication package to call, as returned by[win32security::LsaLookupAuthenticationPackage](#win32security.md#win32securityLsaLookupAuthenticationPackage)

     *MessageType* : int

    Type of request that is being made, Kerb*Message or MsV1_0* constant

     *ProtocolSubmitBuffer* : object

    Type is dependent on MessageType

#### Comments
Message type is embedded in different types of submit buffers in the API call, but passed separately 

from python for simplicity of parsing input

 **MessageType**  **Input type** KerbQueryTicketCacheMessagelong - a logon id, use 0 for current logon sessionKerbRetrieveTicketMessagelong - a logon id, use 0 for current logon sessionKerbPurgeTicketCacheMessage(long,[PyUnicode](#README.md#PyUnicode),[PyUnicode](#README.md#PyUnicode)) - tuple containing (LogonId, ServerName, RealmName)KerbRetrieveEncodedTicketMessage(LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle) 

(int,[PyUnicode](#README.md#PyUnicode), int, int, int,[PyCredHandle](#README.md#PyCredHandle))
 **MessageType**  **Return type** KerbQueryTicketCacheMessage(dict,...) - Returns all tickets for the specified logon session (form is KERB_TICKET_CACHE_INFO)KerbPurgeTicketCacheMessageNoneKerbRetrieveTicketMessageReturns the ticket granting ticket for the logon session as a KERB_EXTERNAL_TICKETKerbRetrieveEncodedTicketMessageReturns specified ticket as a KERB_EXTERNAL_TICKET
#### Return Value
Type of returned object is dependent on MessageType

## [win32security](#README.md#win32security).LsaClose

 **LsaClose( *PolicyHandle* ** )
Closes a policy handle created by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

#### Parameters


     *PolicyHandle* :[PyHANDLE](#README.md#PyHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

## [win32security](#README.md#win32security).LsaConnectUntrusted

[PyLsaLogon_HANDLE](#PyLsaLogon.md#PyLsaLogonHANDLE)= **LsaConnectUntrusted(** )
Creates untrusted connection to LSA

#### Comments
You don't need SeTcbPrivilege to execute this function as you do with 

LsaRegisterLogonProcess, but functionality of handle is limited

## [win32security](#README.md#win32security).LsaDeregisterLogonProcess

 **LsaDeregisterLogonProcess( *LsaHandle* ** )
Closes connection to LSA server

#### Parameters


     *LsaHandle* :[PyLsaLogon_HANDLE](#PyLsaLogon.md#PyLsaLogonHANDLE)

    An Lsa handle as returned by[win32security::LsaConnectUntrusted](#win32security.md#win32securityLsaConnectUntrusted)or[win32security::LsaRegisterLogonProcess](#win32security.md#win32securityLsaRegisterLogonProcess)

## [win32security](#README.md#win32security).LsaEnumerateAccountRights

[[PyUnicode](#README.md#PyUnicode), ...] = **LsaEnumerateAccountRights( *PolicyHandle*  *, AccountSid* ** )
Lists privileges held by SID

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *AccountSid* :[PySID](#README.md#PySID)

    Security identifier of account for which to list privs

## [win32security](#README.md#win32security).LsaEnumerateAccountsWithUserRight

([PySID](#README.md#PySID),...) = **LsaEnumerateAccountsWithUserRight( *PolicyHandle*  *, UserRight* ** )
Return SIDs that hold specified priv

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *UserRight* : str/unicode

    Name of privilege (SE_*_NAME unicode constant)

## [win32security](#README.md#win32security).LsaEnumerateLogonSessions

(long,...) = **LsaEnumerateLogonSessions(** )
Lists all current logon ids

## [win32security](#README.md#win32security).LsaGetLogonSessionData

(dict,...) = **LsaGetLogonSessionData( *LogonId* ** )
Returns information about a logon session

#### Parameters


     *LogonId* : **PyLARGE_INTEGER** 

    An LUID identifying a logon session

#### Return Value
Returns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure

## [win32security](#README.md#win32security).LsaLookupAuthenticationPackage

int = **LsaLookupAuthenticationPackage( *LsaHandle*  *, PackageName* ** )
Retrieves the unique id for an authentication package

#### Parameters


     *LsaHandle* :[PyLsaLogon_HANDLE](#PyLsaLogon.md#PyLsaLogonHANDLE)

    An Lsa handle as returned by[win32security::LsaConnectUntrusted](#win32security.md#win32securityLsaConnectUntrusted)or[win32security::LsaRegisterLogonProcess](#win32security.md#win32securityLsaRegisterLogonProcess)

     *PackageName* : string

    Name of security package to be identified

## [win32security](#README.md#win32security).LsaOpenPolicy

[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)= **LsaOpenPolicy( *system_name*  *, access_mask* ** )
Opens a policy handle for the specified system

#### Parameters


     *system_name* : string/[PyUnicode](#README.md#PyUnicode)

    System name, local system assumed if not specified

     *access_mask* : int

    Bitmask of requested access types

## [win32security](#README.md#win32security).LsaQueryInformationPolicy

 **LsaQueryInformationPolicy( *PolicyHandle*  *, InformationClass* ** )
Retrieves information from the policy handle

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *InformationClass* : int

    POLICY_INFORMATION_CLASS value


## [win32security](#README.md#win32security).LsaRegisterLogonProcess

[PyLsaLogon_HANDLE](#PyLsaLogon.md#PyLsaLogonHANDLE)= **LsaRegisterLogonProcess( *LogonProcessName* ** )
Creates a trusted connection to LSA

#### Parameters


     *LogonProcessName* : string

    Name to use for this logon process

#### Comments
Requires SeTcbPrivilege (and must be enabled)

## [win32security](#README.md#win32security).LsaRegisterPolicyChangeNotification

 **LsaRegisterPolicyChangeNotification( *InformationClass*  *, NotificationEventHandle* ** )
Register an event handle to receive policy change events

#### Parameters


     *InformationClass* : int

    One of POLICY_NOTIFICATION_INFORMATION_CLASS contants

     *NotificationEventHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Event handle to receives notification

## [win32security](#README.md#win32security).LsaRemoveAccountRights

 **LsaRemoveAccountRights( *PolicyHandle*  *, AccountSid*  *, AllRights*  *, UserRights* ** )
Removes privs from an account

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *AccountSid* :[PySID](#README.md#PySID)

    Account whose privileges will be removed

     *AllRights* : int

    Boolean value indicating if all privs should be removed from account

     *UserRights* : (str/unicode,...)

    List of privilege names to be removed (SE_*_NAME unicode constants)

#### Comments
If AllRights parm is true, account is *deleted*
Accepts keyword args.

## [win32security](#README.md#win32security).LsaRetrievePrivateData

[PyUnicode](#README.md#PyUnicode)= **LsaRetrievePrivateData( *PolicyHandle*  *, KeyName* ** )
Retreives encrypted unicode data from Lsa registry key.

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *KeyName* : string

    Registry key to read

## [win32security](#README.md#win32security).LsaSetInformationPolicy

 **LsaSetInformationPolicy( *PolicyHandle*  *, InformationClass*  *, Information* ** )
Sets policy options

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *InformationClass* : int

    POLICY_INFORMATION_CLASS value

     *Information* : object

    Type is dependent on InformationClass

 **InformationClass**  **Type of input expected** PolicyAuditEventsInformation(boolean, (int, ...))
First member imdicates whether auditing is enabled or not.

## [win32security](#README.md#win32security).LsaStorePrivateData

 **LsaStorePrivateData( *PolicyHandle*  *, KeyName*  *, PrivateData* ** )
Stores encrypted unicode data under specified Lsa registry key. Returns None on success

#### Parameters


     *PolicyHandle* :[PyLSA_HANDLE](#PyLSA.md#PyLSAHANDLE)

    An LSA policy handle as returned by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

     *KeyName* : string

    Registry key in which to store data

     *PrivateData* :[PyUNICODE](#README.md#PyUNICODE)

    Unicode string to be encrypted and stored

## [win32security](#README.md#win32security).LsaUnregisterPolicyChangeNotification

 **LsaUnregisterPolicyChangeNotification( *InformationClass*  *, NotificationEventHandle* ** )
Stop receiving policy change notification

#### Parameters


     *InformationClass* : int

    POLICY_NOTIFICATION_INFORMATION_CLASS constant

     *NotificationEventHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Event handle previously registered to receive policy change events

## [win32security](#README.md#win32security).MapGenericMask

int = **MapGenericMask( *AccessMask*  *, GenericMapping* ** )
Translates generic access rights into specific rights

#### Parameters


     *AccessMask* : int

    A bitmask of generic rights to be interpreted according to GenericMapping

     *GenericMapping* : (int,int,int,int)

    A tuple of 4 bitmasks (GenericRead, GenericWrite, GenericExecute, GenericAll) 

containing the standard and specific rights that correspond to the generic rights.

#### Return Value
The input AccessMask will be returned with any generic access rights translated into specific equivalents

## NOT_USED_ACCESS
 **const win32security.NOT_USED_ACCESS;** 


## NO_INHERITANCE
 **const win32security.NO_INHERITANCE;** 


## NO_PROPAGATE_INHERIT_ACE
 **const win32security.NO_PROPAGATE_INHERIT_ACE;** 


## OBJECT_INHERIT_ACE
 **const win32security.OBJECT_INHERIT_ACE;** 


## OWNER_SECURITY_INFORMATION
 **const win32security.OWNER_SECURITY_INFORMATION;** 
Indicates the owner identifier of the object is being referenced.

## [win32security](#README.md#win32security).OpenProcessToken

[PyHANDLE](#README.md#PyHANDLE)= **OpenProcessToken( *processHandle*  *, desiredAccess* ** )
Opens the access token associated with a process.

#### Parameters


     *processHandle* : int

    The handle of the process to open.

     *desiredAccess* : int

    Desired access to process

## [win32security](#README.md#win32security).OpenThreadToken

[PyHandle](#README.md#PyHandle)= **OpenThreadToken( *handle*  *, desiredAccess*  *, openAsSelf* ** )
Opens the access token associated with a thread.

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    handle to thread

     *desiredAccess* : int

    access to process

     *openAsSelf* : int

    Flag for process or thread security

## POLICY_ALL_ACCESS
 **const win32security.POLICY_ALL_ACCESS;** 


## POLICY_AUDIT_EVENT_FAILURE
 **const win32security.POLICY_AUDIT_EVENT_FAILURE;** 
Generate audit records for failed attempts to cause an event of this type to occur.

## POLICY_AUDIT_EVENT_NONE
 **const win32security.POLICY_AUDIT_EVENT_NONE;** 
Do not generate audit records for events of this type.

## POLICY_AUDIT_EVENT_SUCCESS
 **const win32security.POLICY_AUDIT_EVENT_SUCCESS;** 
Generate audit records for successful events of this type.

## POLICY_AUDIT_EVENT_UNCHANGED
 **const win32security.POLICY_AUDIT_EVENT_UNCHANGED;** 
For set operations, specify this value to leave the current options unchanged. This is the default.

## POLICY_AUDIT_LOG_ADMIN
 **const win32security.POLICY_AUDIT_LOG_ADMIN;** 


## POLICY_CREATE_ACCOUNT
 **const win32security.POLICY_CREATE_ACCOUNT;** 


## POLICY_CREATE_PRIVILEGE
 **const win32security.POLICY_CREATE_PRIVILEGE;** 


## POLICY_CREATE_SECRET
 **const win32security.POLICY_CREATE_SECRET;** 


## POLICY_EXECUTE
 **const win32security.POLICY_EXECUTE;** 


## POLICY_GET_PRIVATE_INFORMATION
 **const win32security.POLICY_GET_PRIVATE_INFORMATION;** 


## POLICY_LOOKUP_NAMES
 **const win32security.POLICY_LOOKUP_NAMES;** 


## POLICY_NOTIFICATION
 **const win32security.POLICY_NOTIFICATION;** 


## POLICY_READ
 **const win32security.POLICY_READ;** 


## POLICY_SERVER_ADMIN
 **const win32security.POLICY_SERVER_ADMIN;** 


## POLICY_SET_AUDIT_REQUIREMENTS
 **const win32security.POLICY_SET_AUDIT_REQUIREMENTS;** 


## POLICY_SET_DEFAULT_QUOTA_LIMITS
 **const win32security.POLICY_SET_DEFAULT_QUOTA_LIMITS;** 


## POLICY_TRUST_ADMIN
 **const win32security.POLICY_TRUST_ADMIN;** 


## POLICY_VIEW_AUDIT_INFORMATION
 **const win32security.POLICY_VIEW_AUDIT_INFORMATION;** 


## POLICY_VIEW_LOCAL_INFORMATION
 **const win32security.POLICY_VIEW_LOCAL_INFORMATION;** 


## POLICY_WRITE
 **const win32security.POLICY_WRITE;** 


## PROTECTED_DACL_SECURITY_INFORMATION
 **const win32security.PROTECTED_DACL_SECURITY_INFORMATION;** 


## PROTECTED_SACL_SECURITY_INFORMATION
 **const win32security.PROTECTED_SACL_SECURITY_INFORMATION;** 


## PolicyAccountDomainInformation
 **const win32security.PolicyAccountDomainInformation;** 


## PolicyAuditEventsInformation
 **const win32security.PolicyAuditEventsInformation;** 


## PolicyAuditFullQueryInformation
 **const win32security.PolicyAuditFullQueryInformation;** 


## PolicyAuditFullSetInformation
 **const win32security.PolicyAuditFullSetInformation;** 


## PolicyAuditLogInformation
 **const win32security.PolicyAuditLogInformation;** 


## PolicyDefaultQuotaInformation
 **const win32security.PolicyDefaultQuotaInformation;** 


## PolicyDnsDomainInformation
 **const win32security.PolicyDnsDomainInformation;** 


## PolicyLsaServerRoleInformation
 **const win32security.PolicyLsaServerRoleInformation;** 


## PolicyModificationInformation
 **const win32security.PolicyModificationInformation;** 


## PolicyNotifyAccountDomainInformation
 **const win32security.PolicyNotifyAccountDomainInformation;** 


## PolicyNotifyAuditEventsInformation
 **const win32security.PolicyNotifyAuditEventsInformation;** 


## PolicyNotifyDnsDomainInformation
 **const win32security.PolicyNotifyDnsDomainInformation;** 


## PolicyNotifyDomainEfsInformation
 **const win32security.PolicyNotifyDomainEfsInformation;** 


## PolicyNotifyDomainKerberosTicketInformation
 **const win32security.PolicyNotifyDomainKerberosTicketInformation;** 


## PolicyNotifyMachineAccountPasswordInformation
 **const win32security.PolicyNotifyMachineAccountPasswordInformation;** 


## PolicyNotifyServerRoleInformation
 **const win32security.PolicyNotifyServerRoleInformation;** 


## PolicyPdAccountInformation
 **const win32security.PolicyPdAccountInformation;** 


## PolicyPrimaryDomainInformation
 **const win32security.PolicyPrimaryDomainInformation;** 


## PolicyReplicaSourceInformation
 **const win32security.PolicyReplicaSourceInformation;** 


## PolicyServerDisabled
 **const win32security.PolicyServerDisabled;** 


## PolicyServerDisabled
 **const win32security.PolicyServerDisabled;** 


## PolicyServerEnabled
 **const win32security.PolicyServerEnabled;** 


## PolicyServerEnabled
 **const win32security.PolicyServerEnabled;** 


## PolicyServerRoleBackup
 **const win32security.PolicyServerRoleBackup;** 


## PolicyServerRolePrimary
 **const win32security.PolicyServerRolePrimary;** 


## [win32security](#README.md#win32security).QuerySecurityPackageInfo

dict = **QuerySecurityPackageInfo( *PackageName* ** )
Retrieves parameters for a security package

#### Parameters


     *PackageName* :[PyUNICODE](#README.md#PyUNICODE)

    Name of the security package to query

#### Return Value
Returns a dictionary representing a SecPkgInfo struct

## REVOKE_ACCESS
 **const win32security.REVOKE_ACCESS;** 


## [win32security](#README.md#win32security).RevertToSelf

 **RevertToSelf(** )
Terminates the impersonation of a client application.

## SACL_SECURITY_INFORMATION
 **const win32security.SACL_SECURITY_INFORMATION;** 
Indicates the system ACL of the object is being referenced.

## SANDBOX_INERT
 **const win32security.SANDBOX_INERT;** 


## SDDL_REVISION_1
 **const win32security.SDDL_REVISION_1;** 


## SECPKG_CRED_BOTH
 **const win32security.SECPKG_CRED_BOTH;** 


## SECPKG_CRED_INBOUND
 **const win32security.SECPKG_CRED_INBOUND;** 


## SECPKG_CRED_OUTBOUND
 **const win32security.SECPKG_CRED_OUTBOUND;** 


## SECPKG_FLAG_ACCEPT_WIN32_NAME
 **const win32security.SECPKG_FLAG_ACCEPT_WIN32_NAME;** 


## SECPKG_FLAG_CLIENT_ONLY
 **const win32security.SECPKG_FLAG_CLIENT_ONLY;** 


## SECPKG_FLAG_CONNECTION
 **const win32security.SECPKG_FLAG_CONNECTION;** 


## SECPKG_FLAG_DATAGRAM
 **const win32security.SECPKG_FLAG_DATAGRAM;** 


## SECPKG_FLAG_EXTENDED_ERROR
 **const win32security.SECPKG_FLAG_EXTENDED_ERROR;** 


## SECPKG_FLAG_IMPERSONATION
 **const win32security.SECPKG_FLAG_IMPERSONATION;** 


## SECPKG_FLAG_INTEGRITY
 **const win32security.SECPKG_FLAG_INTEGRITY;** 


## SECPKG_FLAG_MULTI_REQUIRED
 **const win32security.SECPKG_FLAG_MULTI_REQUIRED;** 


## SECPKG_FLAG_PRIVACY
 **const win32security.SECPKG_FLAG_PRIVACY;** 


## SECPKG_FLAG_STREAM
 **const win32security.SECPKG_FLAG_STREAM;** 


## SECPKG_FLAG_TOKEN_ONLY
 **const win32security.SECPKG_FLAG_TOKEN_ONLY;** 


## [win32security](#README.md#win32security).SECURITY_ATTRIBUTES

PySECURITY_ATTRIBUTES = **SECURITY_ATTRIBUTES(** )
Creates a new[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)object.

## SECURITY_CREATOR_SID_AUTHORITY
 **const win32security.SECURITY_CREATOR_SID_AUTHORITY;** 


## [win32security](#README.md#win32security).SECURITY_DESCRIPTOR

PySECURITY_DESCRIPTOR = **SECURITY_DESCRIPTOR(** )
Creates a new[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)object.

## SECURITY_LOCAL_SID_AUTHORITY
 **const win32security.SECURITY_LOCAL_SID_AUTHORITY;** 


## SECURITY_NON_UNIQUE_AUTHORITY
 **const win32security.SECURITY_NON_UNIQUE_AUTHORITY;** 


## SECURITY_NT_AUTHORITY
 **const win32security.SECURITY_NT_AUTHORITY;** 


## SECURITY_NULL_SID_AUTHORITY
 **const win32security.SECURITY_NULL_SID_AUTHORITY;** 


## SECURITY_RESOURCE_MANAGER_AUTHORITY
 **const win32security.SECURITY_RESOURCE_MANAGER_AUTHORITY;** 


## SECURITY_WORLD_SID_AUTHORITY
 **const win32security.SECURITY_WORLD_SID_AUTHORITY;** 


## SET_ACCESS
 **const win32security.SET_ACCESS;** 


## SET_AUDIT_FAILURE
 **const win32security.SET_AUDIT_FAILURE;** 


## SET_AUDIT_SUCCESS
 **const win32security.SET_AUDIT_SUCCESS;** 


## SE_DACL_AUTO_INHERITED
 **const win32security.SE_DACL_AUTO_INHERITED;** 
win2k and up

## SE_DACL_DEFAULTED
 **const win32security.SE_DACL_DEFAULTED;** 


## SE_DACL_PRESENT
 **const win32security.SE_DACL_PRESENT;** 


## SE_DACL_PROTECTED
 **const win32security.SE_DACL_PROTECTED;** 
win2k and up

## SE_DS_OBJECT
 **const win32security.SE_DS_OBJECT;** 


## SE_DS_OBJECT_ALL
 **const win32security.SE_DS_OBJECT_ALL;** 


## SE_FILE_OBJECT
 **const win32security.SE_FILE_OBJECT;** 


## SE_GROUP_DEFAULTED
 **const win32security.SE_GROUP_DEFAULTED;** 


## SE_GROUP_ENABLED
 **const win32security.SE_GROUP_ENABLED;** 


## SE_GROUP_ENABLED_BY_DEFAULT
 **const win32security.SE_GROUP_ENABLED_BY_DEFAULT;** 


## SE_GROUP_LOGON_ID
 **const win32security.SE_GROUP_LOGON_ID;** 


## SE_GROUP_MANDATORY
 **const win32security.SE_GROUP_MANDATORY;** 


## SE_GROUP_OWNER
 **const win32security.SE_GROUP_OWNER;** 


## SE_GROUP_RESOURCE
 **const win32security.SE_GROUP_RESOURCE;** 


## SE_GROUP_USE_FOR_DENY_ONLY
 **const win32security.SE_GROUP_USE_FOR_DENY_ONLY;** 


## SE_KERNEL_OBJECT
 **const win32security.SE_KERNEL_OBJECT;** 


## SE_LMSHARE
 **const win32security.SE_LMSHARE;** 


## SE_OWNER_DEFAULTED
 **const win32security.SE_OWNER_DEFAULTED;** 


## SE_PRINTER
 **const win32security.SE_PRINTER;** 


## SE_PRIVILEGE_ENABLED
 **const win32security.SE_PRIVILEGE_ENABLED;** 


## SE_PRIVILEGE_ENABLED_BY_DEFAULT
 **const win32security.SE_PRIVILEGE_ENABLED_BY_DEFAULT;** 


## SE_PRIVILEGE_REMOVED
 **const win32security.SE_PRIVILEGE_REMOVED;** 


## SE_PRIVILEGE_USED_FOR_ACCESS
 **const win32security.SE_PRIVILEGE_USED_FOR_ACCESS;** 


## SE_PROVIDER_DEFINED_OBJECT
 **const win32security.SE_PROVIDER_DEFINED_OBJECT;** 


## SE_REGISTRY_KEY
 **const win32security.SE_REGISTRY_KEY;** 


## SE_REGISTRY_WOW64_32KEY
 **const win32security.SE_REGISTRY_WOW64_32KEY;** 


## SE_SACL_AUTO_INHERITED
 **const win32security.SE_SACL_AUTO_INHERITED;** 
win2k and up

## SE_SACL_DEFAULTED
 **const win32security.SE_SACL_DEFAULTED;** 


## SE_SACL_PRESENT
 **const win32security.SE_SACL_PRESENT;** 


## SE_SACL_PROTECTED
 **const win32security.SE_SACL_PROTECTED;** 
win2k and up

## SE_SELF_RELATIVE
 **const win32security.SE_SELF_RELATIVE;** 


## SE_SERVICE
 **const win32security.SE_SERVICE;** 


## SE_UNKNOWN_OBJECT_TYPE
 **const win32security.SE_UNKNOWN_OBJECT_TYPE;** 


## SE_WINDOW_OBJECT
 **const win32security.SE_WINDOW_OBJECT;** 


## SE_WMIGUID_OBJECT
 **const win32security.SE_WMIGUID_OBJECT;** 


## [win32security](#README.md#win32security).SID

PySID = **SID(** )
Creates a new[PySID](#README.md#PySID)object.

## STYPE_DEVICE
 **const win32security.STYPE_DEVICE;** 


## STYPE_DISKTREE
 **const win32security.STYPE_DISKTREE;** 


## STYPE_IPC
 **const win32security.STYPE_IPC;** 


## STYPE_PRINTQ
 **const win32security.STYPE_PRINTQ;** 


## STYPE_SPECIAL
 **const win32security.STYPE_SPECIAL;** 


## STYPE_TEMPORARY
 **const win32security.STYPE_TEMPORARY;** 


## SUB_CONTAINERS_AND_OBJECTS_INHERIT
 **const win32security.SUB_CONTAINERS_AND_OBJECTS_INHERIT;** 


## SUB_CONTAINERS_ONLY_INHERIT
 **const win32security.SUB_CONTAINERS_ONLY_INHERIT;** 


## SUB_OBJECTS_ONLY_INHERIT
 **const win32security.SUB_OBJECTS_ONLY_INHERIT;** 


## SUCCESSFUL_ACCESS_ACE_FLAG
 **const win32security.SUCCESSFUL_ACCESS_ACE_FLAG;** 


## SYSTEM_AUDIT_ACE_TYPE
 **const win32security.SYSTEM_AUDIT_ACE_TYPE;** 
System-audit ACE that uses the SYSTEM_AUDIT_ACE structure.

## SYSTEM_AUDIT_OBJECT_ACE_TYPE
 **const win32security.SYSTEM_AUDIT_OBJECT_ACE_TYPE;** 


## SecurityAnonymous
 **const win32security.SecurityAnonymous;** 


## SecurityDelegation
 **const win32security.SecurityDelegation;** 


## SecurityIdentification
 **const win32security.SecurityIdentification;** 


## SecurityImpersonation
 **const win32security.SecurityImpersonation;** 


## [win32security](#README.md#win32security).SetFileSecurity

 **SetFileSecurity( *filename*  *, info*  *, security* ** )
Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


     *filename* : string

    The name of the file

     *info* : int

    The type of information to set.

     *security* :[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)

    The security information

## [win32security](#README.md#win32security).SetKernelObjectSecurity

 **SetKernelObjectSecurity( *handle*  *, info*  *, security* ** )
Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to an object for which security information will be set.

     *info* : int

    The type of information to set - combination of SECURITY_INFORMATION values

     *security* :[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)

    The security information

## [win32security](#README.md#win32security).SetNamedSecurityInfo

 **SetNamedSecurityInfo( *ObjectName*  *, ObjectType*  *, SecurityInfo*  *, Owner*  *, Group*  *, Dacl*  *, Sacl* ** )
Sets security info for an object by name

#### Parameters


     *ObjectName* : str/unicode

    Name of object

     *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

     *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

     *Owner* :[PySID](#README.md#PySID)

    Sid to set as owner of object, can be None

     *Group* :[PySID](#README.md#PySID)

    Group Sid, can be None

     *Dacl* :[PyACL](#README.md#PyACL)

    Discretionary ACL to set for object, can be None

     *Sacl* :[PyACL](#README.md#PyACL)

    System Audit ACL to set for object, can be None

## [win32security](#README.md#win32security).SetSecurityInfo

 **SetSecurityInfo( *handle*  *, ObjectType*  *, SecurityInfo*  *, Owner*  *, Group*  *, Dacl*  *, Sacl* ** )
Sets security info for an object by handle

#### Parameters


     *handle* : int/[PyHANDLE](#README.md#PyHANDLE)

    Handle to object

     *ObjectType* : int

    Value from SE_OBJECT_TYPE enum

     *SecurityInfo* : int

    Combination of SECURITY_INFORMATION constants

     *Owner* :[PySID](#README.md#PySID)

    Sid to set as owner of object, can be None

     *Group* :[PySID](#README.md#PySID)

    Group Sid, can be None

     *Dacl* :[PyACL](#README.md#PyACL)

    Discretionary ACL to set for object, can be None

     *Sacl* :[PyACL](#README.md#PyACL)

    System Audit ACL to set for object, can be None

## [win32security](#README.md#win32security).SetThreadToken

 **SetThreadToken( *Thread*  *, Token* ** )
Assigns an impersonation token to a thread. The function 

can also cause a thread to stop using an impersonation token.

#### Parameters


     *Thread* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a thread.  Use None to indicate calling thread.

     *Token* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an impersonation token.  Use None to end impersonation.

## [win32security](#README.md#win32security).SetTokenInformation

 **SetTokenInformation( *TokenHandle*  *, TokenInformationClass*  *, TokenInformation* ** )
Set a specified type of information in an access token

#### Parameters


     *TokenHandle* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an access token to be modified

     *TokenInformationClass* : int

    Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information to be modfied

     *TokenInformation* : object

    Type is dependent on TokenInformationClass


## [win32security](#README.md#win32security).SetUserObjectSecurity

 **SetUserObjectSecurity( *handle*  *, info*  *, security* ** )
Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

#### Parameters


     *handle* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to an object for which security information will be set.

     *info* : int

    The type of information to set - combination of SECURITY_INFORMATION values

     *security* :[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)

    The security information

## SidTypeAlias
 **const win32security.SidTypeAlias;** 
Indicates an alias SID.

## SidTypeComputer
 **const win32security.SidTypeComputer;** 
Indicates a computer SID

## SidTypeDeletedAccount
 **const win32security.SidTypeDeletedAccount;** 
Indicates an SID for a deleted account.

## SidTypeDomain
 **const win32security.SidTypeDomain;** 
Indicates a domain SID.

## SidTypeGroup
 **const win32security.SidTypeGroup;** 
Indicates a group SID.

## SidTypeInvalid
 **const win32security.SidTypeInvalid;** 
Indicates an invalid SID.

## SidTypeUnknown
 **const win32security.SidTypeUnknown;** 
Indicates an unknown SID type.

## SidTypeUser
 **const win32security.SidTypeUser;** 
Indicates a user SID.

## SidTypeWellKnownGroup
 **const win32security.SidTypeWellKnownGroup;** 
Indicates an SID for a well-known group.

## TOKEN_ADJUST_DEFAULT
 **const win32security.TOKEN_ADJUST_DEFAULT;** 
Required to change the default ACL, primary group, or owner of an access token.

## TOKEN_ADJUST_GROUPS
 **const win32security.TOKEN_ADJUST_GROUPS;** 
Required to change the groups specified in an access token.

## TOKEN_ADJUST_PRIVILEGES
 **const win32security.TOKEN_ADJUST_PRIVILEGES;** 
Required to change the privileges specified in an access token.

## TOKEN_ALL_ACCESS
 **const win32security.TOKEN_ALL_ACCESS;** 
Combines the STANDARD_RIGHTS_REQUIRED standard access rights and all individual access rights for tokens.

## TOKEN_ASSIGN_PRIMARY
 **const win32security.TOKEN_ASSIGN_PRIMARY;** 
Required to attach a primary token to a process in addition to the SE_CREATE_TOKEN_NAME privilege.

## TOKEN_DUPLICATE
 **const win32security.TOKEN_DUPLICATE;** 
Required to duplicate an access token.

## TOKEN_EXECUTE
 **const win32security.TOKEN_EXECUTE;** 
Combines the STANDARD_RIGHTS_EXECUTE standard access rights and the TOKEN_IMPERSONATE access right.

## TOKEN_IMPERSONATE
 **const win32security.TOKEN_IMPERSONATE;** 
Required to attach an impersonation access token to a process.

## TOKEN_QUERY
 **const win32security.TOKEN_QUERY;** 
Required to query the contents of an access token.

## TOKEN_QUERY_SOURCE
 **const win32security.TOKEN_QUERY_SOURCE;** 
Required to query the source of an access token.

## TOKEN_READ
 **const win32security.TOKEN_READ;** 
Combines the STANDARD_RIGHTS_READ standard access rights and the TOKEN_QUERY access right.

## TOKEN_WRITE
 **const win32security.TOKEN_WRITE;** 
Combines the STANDARD_RIGHTS_WRITE standard access rights and the TOKEN_ADJUST_PRIVILEGES, TOKEN_ADJUST_GROUPS, and TOKEN_ADJUST_DEFAULT access rights.

## TRUSTEE_BAD_FORM
 **const win32security.TRUSTEE_BAD_FORM;** 


## TRUSTEE_IS_ALIAS
 **const win32security.TRUSTEE_IS_ALIAS;** 


## TRUSTEE_IS_COMPUTER
 **const win32security.TRUSTEE_IS_COMPUTER;** 


## TRUSTEE_IS_DELETED
 **const win32security.TRUSTEE_IS_DELETED;** 


## TRUSTEE_IS_DOMAIN
 **const win32security.TRUSTEE_IS_DOMAIN;** 


## TRUSTEE_IS_GROUP
 **const win32security.TRUSTEE_IS_GROUP;** 


## TRUSTEE_IS_INVALID
 **const win32security.TRUSTEE_IS_INVALID;** 


## TRUSTEE_IS_NAME
 **const win32security.TRUSTEE_IS_NAME;** 


## TRUSTEE_IS_OBJECTS_AND_NAME
 **const win32security.TRUSTEE_IS_OBJECTS_AND_NAME;** 


## TRUSTEE_IS_OBJECTS_AND_SID
 **const win32security.TRUSTEE_IS_OBJECTS_AND_SID;** 


## TRUSTEE_IS_SID
 **const win32security.TRUSTEE_IS_SID;** 


## TRUSTEE_IS_UNKNOWN
 **const win32security.TRUSTEE_IS_UNKNOWN;** 


## TRUSTEE_IS_USER
 **const win32security.TRUSTEE_IS_USER;** 


## TRUSTEE_IS_WELL_KNOWN_GROUP
 **const win32security.TRUSTEE_IS_WELL_KNOWN_GROUP;** 


## TokenImpersonation
 **const win32security.TokenImpersonation;** 


## TokenPrimary
 **const win32security.TokenPrimary;** 


## [win32security](#README.md#win32security).TranslateName

[PyUnicode](#README.md#PyUnicode)= **TranslateName( *accountName*  *, accountNameFormat*  *, accountNameFormat*  *, numChars* ** )
Converts a directory service object name from one format to another.

#### Parameters


     *accountName* :[PyUnicode](#README.md#PyUnicode)

    object name

     *accountNameFormat* : int

    A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the accountName name.

     *accountNameFormat* : int

    A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the desired name.

     *numChars=1024* : int

    Number of Unicode characters to allocate for the return buffer.

## TrustedControllersInformation
 **const win32security.TrustedControllersInformation;** 


## TrustedDomainAuthInformation
 **const win32security.TrustedDomainAuthInformation;** 


## TrustedDomainAuthInformationInternal
 **const win32security.TrustedDomainAuthInformationInternal;** 


## TrustedDomainFullInformation
 **const win32security.TrustedDomainFullInformation;** 


## TrustedDomainFullInformation2Internal
 **const win32security.TrustedDomainFullInformation2Internal;** 


## TrustedDomainFullInformationInternal
 **const win32security.TrustedDomainFullInformationInternal;** 


## TrustedDomainInformationBasic
 **const win32security.TrustedDomainInformationBasic;** 


## TrustedDomainInformationEx
 **const win32security.TrustedDomainInformationEx;** 


## TrustedDomainInformationEx2Internal
 **const win32security.TrustedDomainInformationEx2Internal;** 


## TrustedDomainNameInformation
 **const win32security.TrustedDomainNameInformation;** 


## TrustedPasswordInformation
 **const win32security.TrustedPasswordInformation;** 


## TrustedPosixOffsetInformation
 **const win32security.TrustedPosixOffsetInformation;** 


## UNPROTECTED_DACL_SECURITY_INFORMATION
 **const win32security.UNPROTECTED_DACL_SECURITY_INFORMATION;** 


## UNPROTECTED_SACL_SECURITY_INFORMATION
 **const win32security.UNPROTECTED_SACL_SECURITY_INFORMATION;** 
