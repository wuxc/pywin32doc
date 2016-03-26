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

## [PyCRYPTHASH](#pycrypthash).CryptDestroyHash

 __CryptDestroyHash(__ )
Frees the hash object

## [PyCRYPTHASH](#pycrypthash).CryptDuplicateHash

[PyCRYPTHASH](#pycrypthash)= __CryptDuplicateHash( *Flags* __ )
Clones the hash object

#### Parameters


  -  *Flags=0* : int

    Reserved, use 0 if passed

## [PyCRYPTHASH](#pycrypthash).CryptGetHashParam

int/str = __CryptGetHashParam( *Param*  *, Flags* __ )
Retrieves the specified attribute of the hash

#### Parameters


  -  *Param* : int

    The parameter to retrieve: HP_ALGID, HP_HASHSIZE, or HP_HASHVAL

  -  *Flags=0* : int

    Reserved, use 0 if passed in

#### Comments
After this method has been called, no more data can be hashed

#### Return Value
Type of returned object is dependent on the Param passed in

## [PyCRYPTHASH](#pycrypthash).CryptHashData

 __CryptHashData( *Data*  *, Flags* __ )
Adds data to the hash

#### Parameters


  -  *Data* : string

    Data to be hashed

  -  *Flags=0* : int

    CRYPT_USERDATA or 0

#### Comments
If Flags is CRYPT_USERDATA, provider is expected to prompt user to 

enter data.  MSDN says that MS CSPs ignore this flag

## [PyCRYPTHASH](#pycrypthash).CryptHashSessionKey

 __CryptHashSessionKey( *Key*  *, Flags* __ )
Hashes a session key

#### Parameters


  -  *Key* :[PyCRYPTKEY](#pycryptkey)

    The session key to be hashed

  -  *Flags=0* : int

    CRYPT_LITTLE_ENDIAN or 0

## [PyCRYPTHASH](#pycrypthash).CryptSignHash

string = __CryptSignHash( *KeySpec*  *, Flags* __ )
Signs the hash

#### Parameters


  -  *KeySpec* : int

    The key to be used to sign the hash, AT_KEYEXCHANGE,AT_SIGNATURE

  -  *Flags=0* : int

    CRYPT_NOHASHOID,CRYPT_X931_FORMAT or 0

#### Comments
This methods signs only the hash, not the data that the hash represents

## [PyCRYPTHASH](#pycrypthash).CryptVerifySignature

 __CryptVerifySignature( *Signature*  *, PubKey*  *, Flags* __ )
Verifies that a signature matches hashed data

#### Parameters


  -  *Signature* : string

    Signature data to verify

  -  *PubKey* :[PyCRYPTKEY](#pycryptkey)

    Public key of signer

  -  *Flags=0* : int

    CRYPT_NOHASHOID,CRYPT_X931_FORMAT or 0