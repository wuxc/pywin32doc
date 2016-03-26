# PySID

## PySID Object



A Python object, representing a SID structure

#### Methods


  - [Initialize](PySID.md#pysidinitialize)

    Initialize the SID\.&nbsp;

  - [IsValid](PySID.md#pysidisvalid)

    Determines if the SID is valid\.&nbsp;

  - [SetSubAuthority](PySID.md#pysidsetsubauthority)

    Sets a SID SubAuthority&nbsp;

  - [GetLength](PySID.md#pysidgetlength)

    Return length of sid \(GetLengthSid\)&nbsp;

  - [GetSubAuthorityCount](PySID.md#pysidgetsubauthoritycount)

    Return nbr of subauthorities from SID&nbsp;

  - [GetSubAuthority](PySID.md#pysidgetsubauthority)

    Return specified subauthory from SID&nbsp;

  - [GetSidIdentifierAuthority](PySID.md#pysidgetsididentifierauthority)

    Return identifier for the authority who issued the SID \(one of the SID\_IDENTIFIER\_AUTHORITY constants\)&nbsp;

#### Comments


Note the PySID object supports the buffer interface\.  Thus buffer\(sid\) can be used to obtain the raw bytes\. 

tp\_as\_buffer

## PySID\_AND\_ATTRIBUTES Object



A sequence containing \([PySID](#pysid),Attributes\) Representing a SID\_AND\_ATTRIBUTES structure

#### Comments


Attributes is an integer containing flags that depend on intended usage

## [PySID](#pysid)\.GetLength



int =GetLength\(\)
return length of SID \(GetLengthSid\)\.

## [PySID](#pysid)\.GetSidIdentifierAuthority



\(int,int,int,int,int,int\) =GetSidIdentifierAuthority\(\)
Returns a tuple of 6 SID\_IDENTIFIER\_AUTHORITY constants

## [PySID](#pysid)\.GetSubAuthority



int =GetSubAuthority\(\)
Returns specified subauthority from SID

## [PySID](#pysid)\.GetSubAuthorityCount



int =GetSubAuthorityCount\(\)
return nbr of subauthorities from SID

## [PySID](#pysid)\.Initialize

Initialize\(idAuthority, numSubauthorities\)
Initialize the SID\.

#### Parameters


  - idAuthority :SID\_IDENTIFIER\_AUTHORITY

    The identifier authority\.

  - numSubauthorities : int

    The number of sub authorities to allocate\.

## [PySID](#pysid)\.IsValid

IsValid\(\)
Determines if the SID is valid\.

## [PySID](#pysid)\.SetSubAuthority

SetSubAuthority\(index, val\)
Sets a SID SubAuthority

#### Parameters


  - index : int

    The index of the sub authority to set

  - val : int

    The value for the sub authority

#### Comments


See the function SetSidSubAuthority