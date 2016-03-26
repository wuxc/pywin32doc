# PyCRYPTKEY

## PyCRYPTKEY Object

Handle to a cryptographic key

#### Methods


  - [CryptDestroyKey](PyCRYPTKEY.md#pycryptkeycryptdestroykey)

    Releases the handle to the key&nbsp;

  - [CryptExportKey](PyCRYPTKEY.md#pycryptkeycryptexportkey)

    Securely exports key or key pair&nbsp;

  - [CryptGetKeyParam](PyCRYPTKEY.md#pycryptkeycryptgetkeyparam)

    Retrieves key parameters&nbsp;

  - [CryptDuplicateKey](PyCRYPTKEY.md#pycryptkeycryptduplicatekey)

    Creates an independent copy of the key&nbsp;

  - [CryptEncrypt](PyCRYPTKEY.md#pycryptkeycryptencrypt)

    Encrypts data&nbsp;

  - [CryptDecrypt](PyCRYPTKEY.md#pycryptkeycryptdecrypt)

    Decrypts data&nbsp;

#### Properties

  -  __int HCRYPTPROV__ 
    CSP used by the key

  -  __int HCRYPTKEY__ 
    Plain integer handle to the key

## [PyCRYPTKEY](#pycryptkey).CryptDecrypt

str = __CryptDecrypt( *Final*  *, Data*  *, Hash*  *, Flags* __ )
Decrypts data

#### Parameters


  -  *Final* : int

    Boolean, use True is this is last (or only) operation

  -  *Data* : buffer

    Data to be decrypted

  -  *Hash=None* :[PyCRYPTHASH](#pycrypthash)

    Hash to be used in signature verification, can be None

  -  *Flags=0* : int

    Reserved, use only 0

## [PyCRYPTKEY](#pycryptkey).CryptDestroyKey

 __CryptDestroyKey(__ )
Releases the handle to the key (does not delete permanent keys)

## [PyCRYPTKEY](#pycryptkey).CryptDuplicateKey

[PyCRYPTKEY](#pycryptkey)= __CryptDuplicateKey( *Reserved*  *, Flags* __ )
Creates an independent copy of the key

#### Parameters


  -  *Reserved=0* : int

    Use 0 if passed in

  -  *Flags=0* : int

    Also reserved, use 0

## [PyCRYPTKEY](#pycryptkey).CryptEncrypt

str = __CryptEncrypt( *Final*  *, Data*  *, Hash*  *, Flags* __ )
Encrypts and optionally hashes data

#### Parameters


  -  *Final* : int

    Boolean, use True if this is final encryption operation

  -  *Data* : buffer

    Data to be encrypted

  -  *Hash=None* :[PyCRYPTHASH](#pycrypthash)

    Hash to be updated with data passed in, can be None

  -  *Flags=0* : int

    Reserved, use 0 if passed in

## [PyCRYPTKEY](#pycryptkey).CryptExportKey

str = __CryptExportKey( *ExpKey*  *, BlobType*  *, Flags* __ )
Exports key or key pair as an encrypted blob

#### Parameters


  -  *ExpKey* :[PyCRYPTKEY](#pycryptkey)

    Public key or session key of destination user.  Use None if exporting a PUBLICKEYBLOB

  -  *BlobType* : int

    One of OPAQUEKEYBLOB,PRIVATEKEYBLOB,PUBLICKEYBLOB,SIMPLEBLOB,PLAINTEXTKEYBLOB,SYMMETRICWRAPKEYBLOB

  -  *Flags=0* : int

    Combination of CRYPT_DESTROYKEY,CRYPT_SSL2_FALLBACK,CRYPT_OAEP or 0

#### Return Value
Returns a binary blob that can be imported via[PyCRYPTPROV::CryptImportKey](PyCRYPTPROV.md#pycryptprovcryptimportkey)

## [PyCRYPTKEY](#pycryptkey).CryptGetKeyParam

object = __CryptGetKeyParam( *Param*  *, Flags* __ )
Retrieves key parameters

#### Parameters


  -  *Param* : int

    One of the KP_* constants

  -  *Flags=0* : int

    Reserved, use only 0

#### Return Value
Type of returned object is dependent on the requested attribute