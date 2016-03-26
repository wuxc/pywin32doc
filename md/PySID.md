# PySID

## PySID Object

A Python object, representing a SID structure

#### Methods


  - [Initialize](PySID.md#pysidinitialize)

    Initialize the SID.&nbsp;

  - [IsValid](PySID.md#pysidisvalid)

    Determines if the SID is valid.&nbsp;

  - [SetSubAuthority](PySID.md#pysidsetsubauthority)

    Sets a SID SubAuthority&nbsp;

  - [GetLength](PySID.md#pysidgetlength)

    Return length of sid (GetLengthSid)&nbsp;

  - [GetSubAuthorityCount](PySID.md#pysidgetsubauthoritycount)

    Return nbr of subauthorities from SID&nbsp;

  - [GetSubAuthority](PySID.md#pysidgetsubauthority)

    Return specified subauthory from SID&nbsp;

  - [GetSidIdentifierAuthority](PySID.md#pysidgetsididentifierauthority)

    Return identifier for the authority who issued the SID (one of the SID_IDENTIFIER_AUTHORITY constants)&nbsp;

#### Comments
Note the PySID object supports the buffer interface.  Thus buffer(sid) can be used to obtain the raw bytes. 

tp_as_buffer

## PySID_AND_ATTRIBUTES Object

A sequence containing ([PySID](#pysid),Attributes) Representing a SID_AND_ATTRIBUTES structure

#### Comments
Attributes is an integer containing flags that depend on intended usage

## [PySID](#pysid).GetLength

int = __GetLength(__ )
return length of SID (GetLengthSid).

## [PySID](#pysid).GetSidIdentifierAuthority

(int,int,int,int,int,int) = __GetSidIdentifierAuthority(__ )
Returns a tuple of 6 SID_IDENTIFIER_AUTHORITY constants

## [PySID](#pysid).GetSubAuthority

int = __GetSubAuthority(__ )
Returns specified subauthority from SID

## [PySID](#pysid).GetSubAuthorityCount

int = __GetSubAuthorityCount(__ )
return nbr of subauthorities from SID

## [PySID](#pysid).Initialize

 __Initialize( *idAuthority*  *, numSubauthorities* __ )
Initialize the SID.

#### Parameters


  -  *idAuthority* : __SID_IDENTIFIER_AUTHORITY__ 

    The identifier authority.

  -  *numSubauthorities* : int

    The number of sub authorities to allocate.

## [PySID](#pysid).IsValid

 __IsValid(__ )
Determines if the SID is valid.

## [PySID](#pysid).SetSubAuthority

 __SetSubAuthority( *index*  *, val* __ )
Sets a SID SubAuthority

#### Parameters


  -  *index* : int

    The index of the sub authority to set

  -  *val* : int

    The value for the sub authority

#### Comments
See the function SetSidSubAuthority