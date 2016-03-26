# PyACL

## PyACL Object

A Python object, representing a ACL structure

#### Methods


  - [Initialize](PyACL.md#pyaclinitialize)

    Initialize the ACL.&nbsp;

  - [IsValid](PyACL.md#pyaclisvalid)

    Validate the ACL.&nbsp;

  - [AddAccessAllowedAce](PyACL.md#pyacladdaccessallowedace)

    Adds an access-allowed ACE to an ACL object.&nbsp;

  - [AddAccessAllowedAceEx](PyACL.md#pyacladdaccessallowedaceex)

    Same as AddAccessAllowedAce, with addition of ace flags&nbsp;

  - [AddAccessAllowedObjectAce](PyACL.md#pyacladdaccessallowedobjectace)

    Adds an ACCESS_ALLOWED_OBJECT_ACE to the ACL&nbsp;

  - [AddAccessDeniedAce](PyACL.md#pyacladdaccessdeniedace)

    Adds an access-denied ACE to an ACL object.&nbsp;

  - [AddAccessDeniedAceEx](PyACL.md#pyacladdaccessdeniedaceex)

    Adds an access-denied ACE to an ACL object&nbsp;

  - [AddMandatoryAce](PyACL.md#pyacladdmandatoryace)

    Adds a mandatory integrity level ACE to a SACL&nbsp;

  - [AddAccessAllowedObjectAce](PyACL.md#pyacladdaccessallowedobjectace)

    Adds an ACCESS_DENIED_OBJECT_ACE to the ACL&nbsp;

  - [AddAuditAccessAce](PyACL.md#pyacladdauditaccessace)

    Adds an audit entry to a system access control list (SACL)&nbsp;

  - [AddAuditAccessAceEx](PyACL.md#pyacladdauditaccessaceex)

    Adds an audit ACE to an SACL with inheritance flags&nbsp;

  - [AddAuditAccessObjectAce](PyACL.md#pyacladdauditaccessobjectace)

    Adds an audit ACE for an object type identified by GUID&nbsp;

  - [GetAclSize](PyACL.md#pyaclgetaclsize)

    Returns the storage size of the ACL.&nbsp;

  - [GetAclRevision](PyACL.md#pyaclgetaclrevision)

    Returns the revision nbr of the ACL.&nbsp;

  - [GetAceCount](PyACL.md#pyaclgetacecount)

    Returns the number of ACEs in the ACL.&nbsp;

  - [GetAce](PyACL.md#pyaclgetace)

    Returns an ACE from the ACL.&nbsp;

  - [DeleteAce](PyACL.md#pyacldeleteace)

    Delete an access-control entry (ACE) from an ACL&nbsp;

  - [GetExplicitEntriesFromAcl](PyACL.md#pyaclgetexplicitentriesfromacl)

    Retrieve list of EXPLICIT_ACCESSs from the ACL&nbsp;

  - [SetEntriesInAcl](PyACL.md#pyaclsetentriesinacl)

    Adds a list of EXPLICIT_ACCESSs to an ACL&nbsp;

  - [GetEffectiveRightsFromAcl](PyACL.md#pyaclgeteffectiverightsfromacl)

    Return access rights (ACCESS_MASK) that the ACL grants to specified trustee&nbsp;

  - [GetAuditedPermissionsFromAcl](PyACL.md#pyaclgetauditedpermissionsfromacl)

    Return types of access for which ACL will generate an audit event for specified trustee&nbsp;

## [PyACL](#pyacl).AddAccessAllowedAce

 __AddAccessAllowedAce( *revision*  *, access*  *, sid* __ )
Adds an access-allowed ACE to an DACL object. The access is granted to a specified SID.

#### Parameters


  -  *revision* : int

    Pre-win2k, must be ACL_REVISION, otherwise also may be ACL_REVISION_DS.

  -  *access* : int

    Specifies the mask of access rights to be denied to the specified SID.

  -  *sid* :[PySID](#pysid)

    A SID object representing a user, group, or logon account being denied access.

#### Alternative Parameters


  -  *access* 

    Specifies the mask of access rights to be denied to the specified SID.

  -  *sid* 

    A SID object representing a user, group, or logon account being denied access.

#### Comments
Note that early versions of this function supported only 

two arguments.  This has been deprecated in preference of the 

three argument version, which reflects the win32 API and the new 

functions in this module.

## [PyACL](#pyacl).AddAccessAllowedAceEx

 __AddAccessAllowedAceEx( *revision*  *, aceflags*  *, access*  *, sid* __ )
Add access allowed ACE to an ACL with ACE flags (Requires Win2k or higher)

#### Parameters


  -  *revision* : int

    Must be at least ACL_REVISION_DS

  -  *aceflags* : int

    Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

  -  *access* : int

    Specifies the mask of access rights to be granted to the specified SID.

  -  *sid* :[PySID](#pysid)

    A SID object representing a user, group, or logon account being granted access.

## [PyACL](#pyacl).AddAccessAllowedObjectAce

 __AddAccessAllowedObjectAce( *AceRevision*  *, AceFlags*  *, AccessMask*  *, ObjectTypeGuid*  *, InheritedObjectTypeGuid*  *, sid* __ )
Adds an ACCESS_ALLOWED_OBJECT_ACE to the ACL

#### Parameters


  -  *AceRevision* : int

    Must be at least ACL_REVISION_DS

  -  *AceFlags* : int

    Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

  -  *AccessMask* : int

    Specifies the mask of access rights to be granted to the specified SID

  -  *ObjectTypeGuid* :[PyIID](#pyiid)

    GUID of object type or property set to which ace applies, can be None

  -  *InheritedObjectTypeGuid* :[PyIID](#pyiid)

    GUID of object type or property that will inherit ACE, can be None

  -  *sid* :[PySID](#pysid)

    A SID object representing a user, group, or logon account being granted access.

## [PyACL](#pyacl).AddAccessDeniedAce

 __AddAccessDeniedAce( *revision*  *, access*  *, sid* __ )
Adds an access-denied ACE to an ACL object. The access is denied to a specified SID.

#### Parameters


  -  *revision* : int

    Pre-win2k, must be ACL_REVISION, otherwise also may be ACL_REVISION_DS.

  -  *access* : int

    Specifies the mask of access rights to be denied to the specified SID.

  -  *sid* :[PySID](#pysid)

    A SID object representing a user, group, or logon account being denied access.

#### Alternative Parameters


  -  *access* 

    Specifies the mask of access rights to be denied to the specified SID.

  -  *sid* 

    A SID object representing a user, group, or logon account being denied access.

#### Comments
Note that early versions of this function supported only 

two arguments.  This has been deprecated in preference of the 

three argument version, which reflects the win32 API and the new 

functions in this module.

## [PyACL](#pyacl).AddAccessDeniedAceEx

 __AddAccessDeniedAceEx( *revision*  *, aceflags*  *, access*  *, sid* __ )
Add access denied ACE to an ACL with ACE flags (Requires Win2k or higher)

#### Parameters


  -  *revision* : int

    Must be at least ACL_REVISION_DS

  -  *aceflags* : int

    Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

  -  *access* : int

    Specifies the mask of access rights to be denied to the specified SID.

  -  *sid* :[PySID](#pysid)

    A SID object representing a user, group, or logon account being denied access.

## [PyACL](#pyacl).AddAccessDeniedObjectAce

 __AddAccessDeniedObjectAce( *AceRevision*  *, AceFlags*  *, AccessMask*  *, ObjectTypeGuid*  *, InheritedObjectTypeGuid*  *, sid* __ )
Adds an ACCESS_DENIED_OBJECT_ACE to the ACL

#### Parameters


  -  *AceRevision* : int

    Must be at least ACL_REVISION_DS

  -  *AceFlags* : int

    Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

  -  *AccessMask* : int

    Specifies the mask of access rights to be granted to the specified SID

  -  *ObjectTypeGuid* :[PyIID](#pyiid)

    GUID of object type or property set to which ace applies, can be None

  -  *InheritedObjectTypeGuid* :[PyIID](#pyiid)

    GUID of object type or property that will inherit ACE, can be None

  -  *sid* :[PySID](#pysid)

    A SID object representing a user, group, or logon account that will be denied access.

## [PyACL](#pyacl).AddAuditAccessAce

 __AddAuditAccessAce( *dwAceRevision*  *, dwAccessMask*  *, sid*  *, bAuditSuccess*  *, bAuditFailure* __ )
Adds an audit ACE to a Sacl

#### Parameters


  -  *dwAceRevision* : int

    Revision of ACL: Pre-Win2k, must be ACL_REVISION. Win2K on up, can also be ACL_REVISION_DS

  -  *dwAccessMask* : int

    Bitmask of access types to be audited

  -  *sid* :[PySID](#pysid)

    SID for whom system audit messages will be generated

  -  *bAuditSuccess* : int

    Set to 1 if access success should be audited, else 0

  -  *bAuditFailure* : int

    Set to 1 if access failure should be audited, else 0

## [PyACL](#pyacl).AddAuditAccessAceEx

 __AddAuditAccessAceEx( *dwAceRevision*  *, AceFlags*  *, dwAccessMask*  *, sid*  *, bAuditSuccess*  *, bAuditFailure* __ )
Adds an audit ACE to an Sacl, includes ace flags

#### Parameters


  -  *dwAceRevision* : int

    Revision of ACL: Must be at least ACL_REVISION_DS

  -  *AceFlags* : int

    Combination of FAILED_ACCESS_ACE_FLAG,SUCCESSFUL_ACCESS_ACE_FLAG,CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE and OBJECT_INHERIT_ACE

  -  *dwAccessMask* : int

    Bitmask of access types to be audited

  -  *sid* :[PySID](#pysid)

    SID for whom system audit messages will be generated

  -  *bAuditSuccess* : int

    Set to 1 if access success should be audited, else 0

  -  *bAuditFailure* : int

    Set to 1 if access failure should be audited, else 0

## [PyACL](#pyacl).AddAuditAccessObjectAce

 __AddAuditAccessObjectAce( *dwAceRevision*  *, AceFlags*  *, dwAccessMask*  *, ObjectTypeGuid*  *, InheritedObjectTypeGuid*  *, sid*  *, bAuditSuccess*  *, bAuditFailure* __ )
Adds an audit ACE for an object type identified by GUID

#### Parameters


  -  *dwAceRevision* : int

    Revision of ACL: Must be at least ACL_REVISION_DS

  -  *AceFlags* : int

    Combination of FAILED_ACCESS_ACE_FLAG,SUCCESSFUL_ACCESS_ACE_FLAG,CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE and OBJECT_INHERIT_ACE

  -  *dwAccessMask* : int

    Bitmask of access types to be audited

  -  *ObjectTypeGuid* :[PyIID](#pyiid)

    GUID of object type or property set to which ace applies, can be None

  -  *InheritedObjectTypeGuid* :[PyIID](#pyiid)

    GUID of object type or property that will inherit ACE, can be None

  -  *sid* :[PySID](#pysid)

    SID for whom system audit messages will be generated

  -  *bAuditSuccess* : int

    Set to 1 if access success should be audited, else 0

  -  *bAuditFailure* : int

    Set to 1 if access failure should be audited, else 0

## [PyACL](#pyacl).AddMandatoryAce

 __AddMandatoryAce( *AceRevision*  *, AceFlags*  *, MandatoryPolicy*  *, LabelSid* __ )
Adds a mandatory integrity level ACE to a SACL

#### Parameters


  -  *AceRevision* : int

    ACL_REVISION or ACL_REVISION_DS

  -  *AceFlags* : int

    Combination of ACE inheritance flags (CONTAINER_INHERIT_ACE,INHERIT_ONLY_ACE,INHERITED_ACE,NO_PROPAGATE_INHERIT_ACE, and OBJECT_INHERIT_ACE)

  -  *MandatoryPolicy* : int

    Access policy for processes with lower integrity level, combination of SYSTEM_MANDATORY_LABEL_* flags

  -  *LabelSid* :[PySID](#pysid)

    Integrity level SID.  This can be created using CreateWellKnownSid with Win*LabelSid.
Also can be constructed manually using SECURITY_MANDATORY_LABEL_AUTHORITY and a SECURITY_MANDATORY_*_RID

## [PyACL](#pyacl).DeleteAce

 __DeleteAce( *index* __ )
Deletes specified Ace from an ACL.

#### Parameters


  -  *index* : int

    Zero-based index of the ACE to delete.

## [PyACL](#pyacl).GetAce

tuple = __GetAce( *index* __ )
Gets an Ace from the ACL

#### Parameters


  -  *index* : int

    Zero-based index of the ACE to retrieve.

#### Return Value
Conventional ACE's (types ACCESS_ALLOWED_ACE, ACCESS_DENIED_ACE, SYSTEM_AUDIT_ACE) are returned 

as a tuple of:

#### Items


  - [0] *(int, int)* : aceType, AceFlags

    

  - [1] *int* : Mask

    

  - [2] *[PySID](#pysid)* : sid

    
Object ACE's (types ACCESS_ALLOWED_OBJECT_ACE, ACCESS_DENIED_OBJECT_ACE, SYSTEM_AUDIT_OBJECT_ACE) 

are returned as a tuple:

  - [0] *(int, int)* : aceType, AceFlags

    

  - [1] *int* : mask

    

  - [2] *[PyIID](#pyiid)* : ObjectType

    

  - [3] *[PyIID](#pyiid)* : InheritedObjectType

    

  - [4] *[PySID](#pysid)* : sid

    
For details see the API documentation.

## [PyACL](#pyacl).GetAceCount

int = __GetAceCount(__ )
Returns the number of ACEs in the ACL.

## [PyACL](#pyacl).GetAclRevision

int = __GetAclRevision(__ )
Returns revision of the ACL.

## [PyACL](#pyacl).GetAclSize

int = __GetAclSize(__ )
Returns the storage size of the ACL.

## [PyACL](#pyacl).GetAuditedPermissionsFromAcl

(SuccessfulAuditedRights,FailedAuditRights) = __GetAuditedPermissionsFromAcl( *trustee* __ )
Return types of access for which ACL will generate an audit event for specified trustee

#### Parameters


  -  *trustee* :[PyTRUSTEE](#pytrustee)

    Dictionary representing a TRUSTEE structure

#### Comments
This function is known to return the success and failure access masks in the the wrong order 

on Windows 2000 service pack 4.  Problem has been reported to Microsoft.

## [PyACL](#pyacl).GetEffectiveRightsFromAcl

ACCESS_MASK = __GetEffectiveRightsFromAcl( *trustee* __ )
Return access rights (ACCESS_MASK) that the ACL grants to specified trustee

#### Parameters


  -  *trustee* :[PyTRUSTEE](#pytrustee)

    Dictionary representing a TRUSTEE structure

## [PyACL](#pyacl).Initialize

 __Initialize(__ )
Initialize the ACL.

#### Comments
It should not be necessary to call this, as the ACL object 

is initialised by Python.  This method gives you a chance to trap 

any errors that may occur.

## [PyACL](#pyacl).IsValid

 __IsValid(__ )
Determines if the ACL is valid (IsValidAcl)