# PyCRYPTHASH

## PyCRYPTHASH Object

Handle to a cryptographic hash

#### Methods


  - [CryptDestroyHash](PyCRYPTHASH.md#pycrypthashcryptdestroyhash)

    Frees the hash object&nbsp;

  - [CryptDuplicateHash](PyCRYPTHASH.md#pycrypthashcryptduplicatehash)

    Clones the hash object&nbsp;

  - [CryptHashData](PyCRYPTHASH.md#pycrypthashcrypthashdata)

    Adds data to the hash&nbsp;

  - [CryptHashSessionKey](PyCRYPTHASH.md#pycrypthashcrypthashsessionkey)

    Hashes a session key&nbsp;

  - [CryptSignHash](PyCRYPTHASH.md#pycrypthashcryptsignhash)

    Signs the hash&nbsp;

  - [CryptVerifySignature](PyCRYPTHASH.md#pycrypthashcryptverifysignature)

    Verifies that a signature matches hashed data&nbsp;

  - [CryptGetHashParam](PyCRYPTHASH.md#pycrypthashcryptgethashparam)

    Retrieves the specified attribute of the hash&nbsp;

## [PyCRYPTHASH](#pycrypthash)\.CryptDestroyHash

 **CryptDestroyHash\(** \)
Frees the hash object

## [PyCRYPTHASH](#pycrypthash)\.CryptDuplicateHash

[PyCRYPTHASH](#pycrypthash)\= **CryptDuplicateHash\( *Flags* ** \)
Clones the hash object

#### Parameters


  -  *Flags\=0* : int

    Reserved, use 0 if passed

## [PyCRYPTHASH](#pycrypthash)\.CryptGetHashParam

int/str \= **CryptGetHashParam\( *Param*  *, Flags* ** \)
Retrieves the specified attribute of the hash

#### Parameters


  -  *Param* : int

    The parameter to retrieve: HP\_ALGID, HP\_HASHSIZE, or HP\_HASHVAL

  -  *Flags\=0* : int

    Reserved, use 0 if passed in

#### Comments
After this method has been called, no more data can be hashed

#### Return Value
Type of returned object is dependent on the Param passed in

## [PyCRYPTHASH](#pycrypthash)\.CryptHashData

 **CryptHashData\( *Data*  *, Flags* ** \)
Adds data to the hash

#### Parameters


  -  *Data* : string

    Data to be hashed

  -  *Flags\=0* : int

    CRYPT\_USERDATA or 0

#### Comments
If Flags is CRYPT\_USERDATA, provider is expected to prompt user to 

enter data\.  MSDN says that MS CSPs ignore this flag

## [PyCRYPTHASH](#pycrypthash)\.CryptHashSessionKey

 **CryptHashSessionKey\( *Key*  *, Flags* ** \)
Hashes a session key

#### Parameters


  -  *Key* :[PyCRYPTKEY](#pycryptkey)

    The session key to be hashed

  -  *Flags\=0* : int

    CRYPT\_LITTLE\_ENDIAN or 0

## [PyCRYPTHASH](#pycrypthash)\.CryptSignHash

string \= **CryptSignHash\( *KeySpec*  *, Flags* ** \)
Signs the hash

#### Parameters


  -  *KeySpec* : int

    The key to be used to sign the hash, AT\_KEYEXCHANGE,AT\_SIGNATURE

  -  *Flags\=0* : int

    CRYPT\_NOHASHOID,CRYPT\_X931\_FORMAT or 0

#### Comments
This methods signs only the hash, not the data that the hash represents

## [PyCRYPTHASH](#pycrypthash)\.CryptVerifySignature

 **CryptVerifySignature\( *Signature*  *, PubKey*  *, Flags* ** \)
Verifies that a signature matches hashed data

#### Parameters


  -  *Signature* : string

    Signature data to verify

  -  *PubKey* :[PyCRYPTKEY](#pycryptkey)

    Public key of signer

  -  *Flags\=0* : int

    CRYPT\_NOHASHOID,CRYPT\_X931\_FORMAT or 0