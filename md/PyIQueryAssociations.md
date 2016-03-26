# PyIQueryAssociations


## PyIQueryAssociations Object

Description of the interface

#### Methods

  - [Init](PyIQueryAssociations.md#pyiqueryassociationsinit)

    Initializes the IQueryAssociations interface and sets the root key to the appropriate ProgID\.&nbsp;

  - [GetKey](PyIQueryAssociations.md#pyiqueryassociationsgetkey)

    Searches for and retrieves a file association-related key from the registry\.&nbsp;

  - [GetString](PyIQueryAssociations.md#pyiqueryassociationsgetstring)

    Searches for and retrieves a file association-related string from the registry\.&nbsp;


## [PyIQueryAssociations](PyIQueryAssociations.md#pyiqueryassociations)\.GetKey

int = GetKey\(flags, assocKey

, 

\)
Searches for and retrieves a file association-related key from the registry\.

#### Parameters

  - flags : int

    Used to control the search\.

  - assocKey : int

    Specifies the type of key that is to be returned\.

  - =extra : string

    Optional string with information about the location of the key\. 

It is normally set to a shell verb such as 'open'\. Set this parameter to None if it is not used\.


## [PyIQueryAssociations](PyIQueryAssociations.md#pyiqueryassociations)\.GetString

int = GetString\(flags, assocStr

, 

\)
Searches for and retrieves a file association-related string from the registry\.

#### Parameters

  - flags : int

    Used to control the search\.

  - assocStr : int

    Specifies the type of string that is to be returned\.

  - =extra : string

    Optional string with information about the location of the key\. 

It is normally set to a shell verb such as 'open'\. Set this parameter to None if it is not used\.

#### Comments

Note that ASSOCF\_NOTRUNCATE semantics are currently not supported - 

the buffer passed is 2048 bytes long, and will be truncated by the 

shell if too small\.


## [PyIQueryAssociations](PyIQueryAssociations.md#pyiqueryassociations)\.Init

Init\(flags, assoc, hkeyProgId, hwnd\)
Initializes the IQueryAssociations interface and sets the root key to the appropriate ProgID\.

#### Parameters

  - flags : int

    One of shellcon\.ASSOCF\_\* flags

  - assoc : string

    The string data \(ie, extension, prog-id, etc\)

  - hkeyProgId=None : [PyHKEY](PyHKEY.md)

    Root registry key, can be None

  - hwnd=None : [PyHANDLE](PyHANDLE.md)

    Reserved, must be 0 or None