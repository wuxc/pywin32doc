# PyACL

## PyACL Object



A Python object, representing a ACL structure

#### Methods


  - [Initialize](PyACL.md#pyaclinitialize)

    Initialize the ACL\.&nbsp;

  - [IsValid](PyACL.md#pyaclisvalid)

    Validate the ACL\.&nbsp;

  - [AddAccessAllowedAce](PyACL.md#pyacladdaccessallowedace)

    Adds an access-allowed ACE to an ACL object\.&nbsp;

  - [AddAccessAllowedAceEx](PyACL.md#pyacladdaccessallowedaceex)

    Same as AddAccessAllowedAce, with addition of ace flags&nbsp;

  - [AddAccessAllowedObjectAce](PyACL.md#pyacladdaccessallowedobjectace)

    Adds an ACCESS\_ALLOWED\_OBJECT\_ACE to the ACL&nbsp;

  - [AddAccessDeniedAce](PyACL.md#pyacladdaccessdeniedace)

    Adds an access-denied ACE to an ACL object\.&nbsp;

  - [AddAccessDeniedAceEx](PyACL.md#pyacladdaccessdeniedaceex)

    Adds an access-denied ACE to an ACL object&nbsp;

  - [AddMandatoryAce](PyACL.md#pyacladdmandatoryace)

    Adds a mandatory integrity level ACE to a SACL&nbsp;

  - [AddAccessAllowedObjectAce](PyACL.md#pyacladdaccessallowedobjectace)

    Adds an ACCESS\_DENIED\_OBJECT\_ACE to the ACL&nbsp;

  - [AddAuditAccessAce](PyACL.md#pyacladdauditaccessace)

    Adds an audit entry to a system access control list \(SACL\)&nbsp;

  - [AddAuditAccessAceEx](PyACL.md#pyacladdauditaccessaceex)

    Adds an audit ACE to an SACL with inheritance flags&nbsp;

  - [AddAuditAccessObjectAce](PyACL.md#pyacladdauditaccessobjectace)

    Adds an audit ACE for an object type identified by GUID&nbsp;

  - [GetAclSize](PyACL.md#pyaclgetaclsize)

    Returns the storage size of the ACL\.&nbsp;

  - [GetAclRevision](PyACL.md#pyaclgetaclrevision)

    Returns the revision nbr of the ACL\.&nbsp;

  - [GetAceCount](PyACL.md#pyaclgetacecount)

    Returns the number of ACEs in the ACL\.&nbsp;

  - [GetAce](PyACL.md#pyaclgetace)

    Returns an ACE from the ACL\.&nbsp;

  - [DeleteAce](PyACL.md#pyacldeleteace)

    Delete an access-control entry \(ACE\) from an ACL&nbsp;

  - [GetExplicitEntriesFromAcl](PyACL.md#pyaclgetexplicitentriesfromacl)

    Retrieve list of EXPLICIT\_ACCESSs from the ACL&nbsp;

  - [SetEntriesInAcl](PyACL.md#pyaclsetentriesinacl)

    Adds a list of EXPLICIT\_ACCESSs to an ACL&nbsp;

  - [GetEffectiveRightsFromAcl](PyACL.md#pyaclgeteffectiverightsfromacl)

    Return access rights \(ACCESS\_MASK\) that the ACL grants to specified trustee&nbsp;

  - [GetAuditedPermissionsFromAcl](PyACL.md#pyaclgetauditedpermissionsfromacl)

    Return types of access for which ACL will generate an audit event for specified trustee&nbsp;

## [PyACL](#pyacl)\.AddAccessAllowedAce

AddAccessAllowedAce\(revision, access, sid\)
Adds an access-allowed ACE to an DACL object\. The access is granted to a specified SID\.

#### Parameters


  - revision : int

    Pre-win2k, must be ACL\_REVISION, otherwise also may be ACL\_REVISION\_DS\.

  - access : int

    Specifies the mask of access rights to be denied to the specified SID\.

  - sid :[PySID](#pysid)

    A SID object representing a user, group, or logon account being denied access\.

#### Alternative Parameters


  - access

    Specifies the mask of access rights to be denied to the specified SID\.

  - sid

    A SID object representing a user, group, or logon account being denied access\.

#### Comments


Note that early versions of this function supported only 

two arguments\.  This has been deprecated in preference of the 

three argument version, which reflects the win32 API and the new 

functions in this module\.

## [PyACL](#pyacl)\.AddAccessAllowedAceEx

AddAccessAllowedAceEx\(revision, aceflags, access, sid\)
Add access allowed ACE to an ACL with ACE flags \(Requires Win2k or higher\)

#### Parameters


  - revision : int

    Must be at least ACL\_REVISION\_DS

  - aceflags : int

    Combination of ACE inheritance flags \(CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE, and OBJECT\_INHERIT\_ACE\)

  - access : int

    Specifies the mask of access rights to be granted to the specified SID\.

  - sid :[PySID](#pysid)

    A SID object representing a user, group, or logon account being granted access\.

## [PyACL](#pyacl)\.AddAccessAllowedObjectAce

AddAccessAllowedObjectAce\(AceRevision, AceFlags, AccessMask, ObjectTypeGuid, InheritedObjectTypeGuid, sid\)
Adds an ACCESS\_ALLOWED\_OBJECT\_ACE to the ACL

#### Parameters


  - AceRevision : int

    Must be at least ACL\_REVISION\_DS

  - AceFlags : int

    Combination of ACE inheritance flags \(CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE, and OBJECT\_INHERIT\_ACE\)

  - AccessMask : int

    Specifies the mask of access rights to be granted to the specified SID

  - ObjectTypeGuid :[PyIID](#pyiid)

    GUID of object type or property set to which ace applies, can be None

  - InheritedObjectTypeGuid :[PyIID](#pyiid)

    GUID of object type or property that will inherit ACE, can be None

  - sid :[PySID](#pysid)

    A SID object representing a user, group, or logon account being granted access\.

## [PyACL](#pyacl)\.AddAccessDeniedAce

AddAccessDeniedAce\(revision, access, sid\)
Adds an access-denied ACE to an ACL object\. The access is denied to a specified SID\.

#### Parameters


  - revision : int

    Pre-win2k, must be ACL\_REVISION, otherwise also may be ACL\_REVISION\_DS\.

  - access : int

    Specifies the mask of access rights to be denied to the specified SID\.

  - sid :[PySID](#pysid)

    A SID object representing a user, group, or logon account being denied access\.

#### Alternative Parameters


  - access

    Specifies the mask of access rights to be denied to the specified SID\.

  - sid

    A SID object representing a user, group, or logon account being denied access\.

#### Comments


Note that early versions of this function supported only 

two arguments\.  This has been deprecated in preference of the 

three argument version, which reflects the win32 API and the new 

functions in this module\.

## [PyACL](#pyacl)\.AddAccessDeniedAceEx

AddAccessDeniedAceEx\(revision, aceflags, access, sid\)
Add access denied ACE to an ACL with ACE flags \(Requires Win2k or higher\)

#### Parameters


  - revision : int

    Must be at least ACL\_REVISION\_DS

  - aceflags : int

    Combination of ACE inheritance flags \(CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE, and OBJECT\_INHERIT\_ACE\)

  - access : int

    Specifies the mask of access rights to be denied to the specified SID\.

  - sid :[PySID](#pysid)

    A SID object representing a user, group, or logon account being denied access\.

## [PyACL](#pyacl)\.AddAccessDeniedObjectAce

AddAccessDeniedObjectAce\(AceRevision, AceFlags, AccessMask, ObjectTypeGuid, InheritedObjectTypeGuid, sid\)
Adds an ACCESS\_DENIED\_OBJECT\_ACE to the ACL

#### Parameters


  - AceRevision : int

    Must be at least ACL\_REVISION\_DS

  - AceFlags : int

    Combination of ACE inheritance flags \(CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE, and OBJECT\_INHERIT\_ACE\)

  - AccessMask : int

    Specifies the mask of access rights to be granted to the specified SID

  - ObjectTypeGuid :[PyIID](#pyiid)

    GUID of object type or property set to which ace applies, can be None

  - InheritedObjectTypeGuid :[PyIID](#pyiid)

    GUID of object type or property that will inherit ACE, can be None

  - sid :[PySID](#pysid)

    A SID object representing a user, group, or logon account that will be denied access\.

## [PyACL](#pyacl)\.AddAuditAccessAce

AddAuditAccessAce\(dwAceRevision, dwAccessMask, sid, bAuditSuccess, bAuditFailure\)
Adds an audit ACE to a Sacl

#### Parameters


  - dwAceRevision : int

    Revision of ACL: Pre-Win2k, must be ACL\_REVISION\. Win2K on up, can also be ACL\_REVISION\_DS

  - dwAccessMask : int

    Bitmask of access types to be audited

  - sid :[PySID](#pysid)

    SID for whom system audit messages will be generated

  - bAuditSuccess : int

    Set to 1 if access success should be audited, else 0

  - bAuditFailure : int

    Set to 1 if access failure should be audited, else 0

## [PyACL](#pyacl)\.AddAuditAccessAceEx

AddAuditAccessAceEx\(dwAceRevision, AceFlags, dwAccessMask, sid, bAuditSuccess, bAuditFailure\)
Adds an audit ACE to an Sacl, includes ace flags

#### Parameters


  - dwAceRevision : int

    Revision of ACL: Must be at least ACL\_REVISION\_DS

  - AceFlags : int

    Combination of FAILED\_ACCESS\_ACE\_FLAG,SUCCESSFUL\_ACCESS\_ACE\_FLAG,CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE and OBJECT\_INHERIT\_ACE

  - dwAccessMask : int

    Bitmask of access types to be audited

  - sid :[PySID](#pysid)

    SID for whom system audit messages will be generated

  - bAuditSuccess : int

    Set to 1 if access success should be audited, else 0

  - bAuditFailure : int

    Set to 1 if access failure should be audited, else 0

## [PyACL](#pyacl)\.AddAuditAccessObjectAce

AddAuditAccessObjectAce\(dwAceRevision, AceFlags, dwAccessMask, ObjectTypeGuid, InheritedObjectTypeGuid, sid, bAuditSuccess, bAuditFailure\)
Adds an audit ACE for an object type identified by GUID

#### Parameters


  - dwAceRevision : int

    Revision of ACL: Must be at least ACL\_REVISION\_DS

  - AceFlags : int

    Combination of FAILED\_ACCESS\_ACE\_FLAG,SUCCESSFUL\_ACCESS\_ACE\_FLAG,CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE and OBJECT\_INHERIT\_ACE

  - dwAccessMask : int

    Bitmask of access types to be audited

  - ObjectTypeGuid :[PyIID](#pyiid)

    GUID of object type or property set to which ace applies, can be None

  - InheritedObjectTypeGuid :[PyIID](#pyiid)

    GUID of object type or property that will inherit ACE, can be None

  - sid :[PySID](#pysid)

    SID for whom system audit messages will be generated

  - bAuditSuccess : int

    Set to 1 if access success should be audited, else 0

  - bAuditFailure : int

    Set to 1 if access failure should be audited, else 0

## [PyACL](#pyacl)\.AddMandatoryAce

AddMandatoryAce\(AceRevision, AceFlags, MandatoryPolicy, LabelSid\)
Adds a mandatory integrity level ACE to a SACL

#### Parameters


  - AceRevision : int

    ACL\_REVISION or ACL\_REVISION\_DS

  - AceFlags : int

    Combination of ACE inheritance flags \(CONTAINER\_INHERIT\_ACE,INHERIT\_ONLY\_ACE,INHERITED\_ACE,NO\_PROPAGATE\_INHERIT\_ACE, and OBJECT\_INHERIT\_ACE\)

  - MandatoryPolicy : int

    Access policy for processes with lower integrity level, combination of SYSTEM\_MANDATORY\_LABEL\_\* flags

  - LabelSid :[PySID](#pysid)

    Integrity level SID\.  This can be created using CreateWellKnownSid with Win\*LabelSid\.
Also can be constructed manually using SECURITY\_MANDATORY\_LABEL\_AUTHORITY and a SECURITY\_MANDATORY\_\*\_RID

## [PyACL](#pyacl)\.DeleteAce

DeleteAce\(index\)
Deletes specified Ace from an ACL\.

#### Parameters


  - index : int

    Zero-based index of the ACE to delete\.

## [PyACL](#pyacl)\.GetAce



tuple =GetAce\(index\)
Gets an Ace from the ACL

#### Parameters


  - index : int

    Zero-based index of the ACE to retrieve\.

#### Return Value
Conventional ACE's \(types ACCESS\_ALLOWED\_ACE, ACCESS\_DENIED\_ACE, SYSTEM\_AUDIT\_ACE\) are returned 

as a tuple of:

#### Items


  - \[0\]\(int, int\) : aceType, AceFlags

    

  - \[1\]int : Mask

    

  - \[2\][PySID](#pysid) : sid

    
Object ACE's \(types ACCESS\_ALLOWED\_OBJECT\_ACE, ACCESS\_DENIED\_OBJECT\_ACE, SYSTEM\_AUDIT\_OBJECT\_ACE\) 

are returned as a tuple:

  - \[0\]\(int, int\) : aceType, AceFlags

    

  - \[1\]int : mask

    

  - \[2\][PyIID](#pyiid) : ObjectType

    

  - \[3\][PyIID](#pyiid) : InheritedObjectType

    

  - \[4\][PySID](#pysid) : sid

    
For details see the API documentation\.

## [PyACL](#pyacl)\.GetAceCount



int =GetAceCount\(\)
Returns the number of ACEs in the ACL\.

## [PyACL](#pyacl)\.GetAclRevision



int =GetAclRevision\(\)
Returns revision of the ACL\.

## [PyACL](#pyacl)\.GetAclSize



int =GetAclSize\(\)
Returns the storage size of the ACL\.

## [PyACL](#pyacl)\.GetAuditedPermissionsFromAcl



\(SuccessfulAuditedRights,FailedAuditRights\) =GetAuditedPermissionsFromAcl\(trustee\)
Return types of access for which ACL will generate an audit event for specified trustee

#### Parameters


  - trustee :[PyTRUSTEE](#pytrustee)

    Dictionary representing a TRUSTEE structure

#### Comments


This function is known to return the success and failure access masks in the the wrong order 

on Windows 2000 service pack 4\.  Problem has been reported to Microsoft\.

## [PyACL](#pyacl)\.GetEffectiveRightsFromAcl



ACCESS\_MASK =GetEffectiveRightsFromAcl\(trustee\)
Return access rights \(ACCESS\_MASK\) that the ACL grants to specified trustee

#### Parameters


  - trustee :[PyTRUSTEE](#pytrustee)

    Dictionary representing a TRUSTEE structure

## [PyACL](#pyacl)\.Initialize

Initialize\(\)
Initialize the ACL\.

#### Comments


It should not be necessary to call this, as the ACL object 

is initialised by Python\.  This method gives you a chance to trap 

any errors that may occur\.

## [PyACL](#pyacl)\.IsValid

IsValid\(\)
Determines if the ACL is valid \(IsValidAcl\)