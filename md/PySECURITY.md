# PySECURITY

## PySECURITY_ATTRIBUTES Object

A Python object, representing a SECURITY_ATTRIBUTES structure

#### Properties

  -  __boolean bInheritHandle__ 
    Specifies whether the returned handle is inherited when a new process is created. If this member is TRUE, the new process inherits the handle.

  -  __[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)SECURITY_DESCRIPTOR__ 
    A PySECURITY_DESCRIPTOR, or None

#### Comments
On platforms that support security descriptor operations, SECURITY_DESCRIPTOR 

defaults to a blank security descriptor with no owner, group, dacl, or sacl. 

Set to None to use a NULL security descriptor instead. 

When PySECURITY_ATTRIBUTES is created on Windows 95/98/Me, SECURITY_DESCRIPTOR defaults 

to None and should not be changed. 

When SECURITY_DESCRIPTOR is not None, any of its methods can be invoked directly 

on the PySECURITY_ATTRIBUTES object

## PySECURITY_DESCRIPTOR Object

A Python object, representing a SECURITY_DESCRIPTOR structure

#### Methods


  - [Initialize](PySECURITY.md#pysecuritydescriptor_initialize)

    Initializes the object.&nbsp;

  - [GetSecurityDescriptorOwner](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorowner)

    Return the owner of the security descriptor. SID is returned.&nbsp;

  - [GetSecurityDescriptorOwner](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorowner)

    Return the group owning the security descriptor. SID is returned.&nbsp;

  - [GetSecurityDescriptorDacl](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptordacl)

    Return the discretionary ACL of the security descriptor.&nbsp;

  - [GetSecurityDescriptorSacl](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorsacl)

    Return the system ACL of the security descriptor.&nbsp;

  - [GetSecurityDescriptorControl](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorcontrol)

    Returns the control bit flags and revistion of the SD&nbsp;

  - [SetSecurityDescriptorOwner](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorowner)

    Set the owner of the security descriptor. Returns non-zero on success.&nbsp;

  - [SetSecurityDescriptorGroup](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorgroup)

    Set the primary group of the security descriptor. Returns non-zero on success.&nbsp;

  - [SetDacl](PySECURITY.md#pysecuritydescriptor_setdacl)

    Sets information in a discretionary access-control list.&nbsp;

  - [SetSecurityDescriptorSacl](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorsacl)

    Sets the system access control list in the security descriptor&nbsp;

  - [IsValid](PySECURITY.md#pysecuritydescriptor_isvalid)

    Determine if security descriptor is valid (IsValidSecurityDescriptor)&nbsp;

  - [GetLength](PySECURITY.md#pysecuritydescriptor_getlength)

    Return length of security descriptor (GetSecurityDescriptorLength)&nbsp;

  - [IsSelfRelative](PySECURITY.md#pysecuritydescriptor_isselfrelative)

    Returns true if SD is self-relative, false if absolute&nbsp;

  - [SetSecurityDescriptorControl](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorcontrol)

    Sets control bitmask of a security descriptor&nbsp;

#### Comments
Note the PySECURITY_DESCRIPTOR object supports the buffer interface.  Thus buffer(sd) can be used to obtain the raw bytes. 

tp_as_buffer

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).GetLength

 __GetLength(__ )
return length of security descriptor (GetSecurityDescriptorLenght).

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).GetSecurityDescriptorControl

(int,int) = __GetSecurityDescriptorControl(__ )
Returns tuple of Control bit flags and revision of SD.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).GetSecurityDescriptorDacl

[PyACL](#pyacl)= __GetSecurityDescriptorDacl(__ )
Return the discretionary ACL of the security descriptor.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).GetSecurityDescriptorGroup

[PySID](#pysid)= __GetSecurityDescriptorGroup(__ )
Return the group owning the security descriptor. SID is returned.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).GetSecurityDescriptorOwner

[PySID](#pysid)= __GetSecurityDescriptorOwner(__ )
Return the owner of the security descriptor.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).GetSecurityDescriptorSacl

[PyACL](#pyacl)= __GetSecurityDescriptorSacl(__ )
Return system access control list (SACL) of SD

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).Initialize

 __Initialize(__ )
Initialize the SD.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).IsSelfRelative

 __IsSelfRelative(__ )
Returns 1 if security descriptor is self relative, 0 if absolute

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).IsValid

 __IsValid(__ )
Determines if the security descriptor is valid.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).SetSecurityDescriptorControl

 __SetSecurityDescriptorControl( *ControlBitsOfInterest*  *, ControlBitsToSet* __ )
Sets the control bit flags related to inheritance for a security descriptor

#### Parameters


  -  *ControlBitsOfInterest* : int

    Bitmask of flags to be modified

  -  *ControlBitsToSet* : int

    Bitmask containing flag values to set

#### Comments
Only exists on Windows 2000 or later

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).SetSecurityDescriptorDacl

 __SetSecurityDescriptorDacl( *bDaclPresent*  *, DACL*  *, bDaclDefaulted* __ )
Replaces DACL in a security descriptor.

#### Parameters


  -  *bDaclPresent* : int

    A flag indicating if the SE_DACL_PRESENT flag should be set.

  -  *DACL* :[PyACL](#pyacl)

    The DACL to set.  If None, a NULL ACL will be created allowing world access.

  -  *bDaclDefaulted* : int

    A flag indicating if the SE_DACL_DEFAULTED flag should be set.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).SetSecurityDescriptorGroup

int = __SetSecurityDescriptorGroup( *sid*  *, bOwnerDefaulted* __ )
Set group SID.

#### Parameters


  -  *sid* :[PySID](#pysid)

    The group sid to be set in the security descriptor.

  -  *bOwnerDefaulted* : int

    Normally set to false since this explicitely set the owner.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).SetSecurityDescriptorOwner

 __SetSecurityDescriptorOwner( *sid*  *, bOwnerDefaulted* __ )
Set owner SID.

#### Parameters


  -  *sid* :[PySID](#pysid)

    The sid to be set as owner in the security descriptor.

  -  *bOwnerDefaulted* : int

    Normally set to false since this explicitely set the owner.

## [PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor).SetSecurityDescriptorSacl

 __SetSecurityDescriptorSacl( *bSaclPresent*  *, SACL*  *, bSaclDefaulted* __ )
Replaces system access control list (SACL) in the security descriptor.

#### Parameters


  -  *bSaclPresent* : int

    A flag indicating if SACL is to be used. If false, last 2 parms are ignored.

  -  *SACL* :[PyACL](#pyacl)

    The SACL to set in the security descriptor

  -  *bSaclDefaulted* : int

    Flag, set to false if user has specifically set the SACL.