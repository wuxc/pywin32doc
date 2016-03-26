# PySECURITY


## PySECURITY\_ATTRIBUTES Object

A Python object, representing a SECURITY\_ATTRIBUTES structure

#### Properties

  - boolean bInheritHandle

    Specifies whether the returned handle is inherited when a new process is created\. If this member is TRUE, the new process inherits the handle\.

  - [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor) SECURITY\_DESCRIPTOR

    A PySECURITY\_DESCRIPTOR, or None

#### Comments

On platforms that support security descriptor operations, SECURITY\_DESCRIPTOR 

defaults to a blank security descriptor with no owner, group, dacl, or sacl\. 

Set to None to use a NULL security descriptor instead\. 

When PySECURITY\_ATTRIBUTES is created on Windows 95/98/Me, SECURITY\_DESCRIPTOR defaults 

to None and should not be changed\. 

When SECURITY\_DESCRIPTOR is not None, any of its methods can be invoked directly 

on the PySECURITY\_ATTRIBUTES object


## PySECURITY\_DESCRIPTOR Object

A Python object, representing a SECURITY\_DESCRIPTOR structure

#### Methods

  - [Initialize](PySECURITY.md#pysecuritydescriptor_initialize)

    Initializes the object\.&nbsp;

  - [GetSecurityDescriptorOwner](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorowner)

    Return the owner of the security descriptor\. SID is returned\.&nbsp;

  - [GetSecurityDescriptorOwner](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorowner)

    Return the group owning the security descriptor\. SID is returned\.&nbsp;

  - [GetSecurityDescriptorDacl](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptordacl)

    Return the discretionary ACL of the security descriptor\.&nbsp;

  - [GetSecurityDescriptorSacl](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorsacl)

    Return the system ACL of the security descriptor\.&nbsp;

  - [GetSecurityDescriptorControl](PySECURITY.md#pysecuritydescriptor_getsecuritydescriptorcontrol)

    Returns the control bit flags and revistion of the SD&nbsp;

  - [SetSecurityDescriptorOwner](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorowner)

    Set the owner of the security descriptor\. Returns non-zero on success\.&nbsp;

  - [SetSecurityDescriptorGroup](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorgroup)

    Set the primary group of the security descriptor\. Returns non-zero on success\.&nbsp;

  - [SetDacl](PySECURITY.md#pysecuritydescriptor_setdacl)

    Sets information in a discretionary access-control list\.&nbsp;

  - [SetSecurityDescriptorSacl](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorsacl)

    Sets the system access control list in the security descriptor&nbsp;

  - [IsValid](PySECURITY.md#pysecuritydescriptor_isvalid)

    Determine if security descriptor is valid \(IsValidSecurityDescriptor\)&nbsp;

  - [GetLength](PySECURITY.md#pysecuritydescriptor_getlength)

    Return length of security descriptor \(GetSecurityDescriptorLength\)&nbsp;

  - [IsSelfRelative](PySECURITY.md#pysecuritydescriptor_isselfrelative)

    Returns true if SD is self-relative, false if absolute&nbsp;

  - [SetSecurityDescriptorControl](PySECURITY.md#pysecuritydescriptor_setsecuritydescriptorcontrol)

    Sets control bitmask of a security descriptor&nbsp;

#### Comments

Note the PySECURITY\_DESCRIPTOR object supports the buffer interface\.  Thus buffer\(sd\) can be used to obtain the raw bytes\. 

tp\_as\_buffer


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.GetLength

GetLength\(\)
return length of security descriptor \(GetSecurityDescriptorLenght\)\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.GetSecurityDescriptorControl

\(int,int\) = GetSecurityDescriptorControl\(\)
Returns tuple of Control bit flags and revision of SD\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.GetSecurityDescriptorDacl

[PyACL](PyACL.md) = GetSecurityDescriptorDacl\(\)
Return the discretionary ACL of the security descriptor\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.GetSecurityDescriptorGroup

[PySID](PySID.md) = GetSecurityDescriptorGroup\(\)
Return the group owning the security descriptor\. SID is returned\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.GetSecurityDescriptorOwner

[PySID](PySID.md) = GetSecurityDescriptorOwner\(\)
Return the owner of the security descriptor\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.GetSecurityDescriptorSacl

[PyACL](PyACL.md) = GetSecurityDescriptorSacl\(\)
Return system access control list \(SACL\) of SD


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.Initialize

Initialize\(\)
Initialize the SD\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.IsSelfRelative

IsSelfRelative\(\)
Returns 1 if security descriptor is self relative, 0 if absolute


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.IsValid

IsValid\(\)
Determines if the security descriptor is valid\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.SetSecurityDescriptorControl

SetSecurityDescriptorControl\(ControlBitsOfInterest, ControlBitsToSet\)
Sets the control bit flags related to inheritance for a security descriptor

#### Parameters

  - ControlBitsOfInterest : int

    Bitmask of flags to be modified

  - ControlBitsToSet : int

    Bitmask containing flag values to set

#### Comments

Only exists on Windows 2000 or later


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.SetSecurityDescriptorDacl

SetSecurityDescriptorDacl\(bDaclPresent, DACL, bDaclDefaulted\)
Replaces DACL in a security descriptor\.

#### Parameters

  - bDaclPresent : int

    A flag indicating if the SE\_DACL\_PRESENT flag should be set\.

  - DACL : [PyACL](PyACL.md)

    The DACL to set\.  If None, a NULL ACL will be created allowing world access\.

  - bDaclDefaulted : int

    A flag indicating if the SE\_DACL\_DEFAULTED flag should be set\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.SetSecurityDescriptorGroup

int = SetSecurityDescriptorGroup\(sid, bOwnerDefaulted

\)
Set group SID\.

#### Parameters

  - sid : [PySID](PySID.md)

    The group sid to be set in the security descriptor\.

  - bOwnerDefaulted : int

    Normally set to false since this explicitely set the owner\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.SetSecurityDescriptorOwner

SetSecurityDescriptorOwner\(sid, bOwnerDefaulted\)
Set owner SID\.

#### Parameters

  - sid : [PySID](PySID.md)

    The sid to be set as owner in the security descriptor\.

  - bOwnerDefaulted : int

    Normally set to false since this explicitely set the owner\.


## [PySECURITY\_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)\.SetSecurityDescriptorSacl

SetSecurityDescriptorSacl\(bSaclPresent, SACL, bSaclDefaulted\)
Replaces system access control list \(SACL\) in the security descriptor\.

#### Parameters

  - bSaclPresent : int

    A flag indicating if SACL is to be used\. If false, last 2 parms are ignored\.

  - SACL : [PyACL](PyACL.md)

    The SACL to set in the security descriptor

  - bSaclDefaulted : int

    Flag, set to false if user has specifically set the SACL\.