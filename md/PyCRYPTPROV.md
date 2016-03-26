# PyCRYPTPROV

## PyCRYPTPROV Object

Handle to a cryptographic provider, created using __cryptoapi::CryptAcquireContext__ 

#### Methods


  - [CryptReleaseContext](PyCRYPTPROV.md#pycryptprovcryptreleasecontext)

    Releases the CSP handle&nbsp;

  - [CryptGenKey](PyCRYPTPROV.md#pycryptprovcryptgenkey)

    Generates a key pair or a session key&nbsp;

  - [CryptGetProvParam](PyCRYPTPROV.md#pycryptprovcryptgetprovparam)

    Retrieves specified attribute of provider&nbsp;

  - [CryptGetUserKey](PyCRYPTPROV.md#pycryptprovcryptgetuserkey)

    Returns a handle to one of user's key pairs&nbsp;

  - [CryptGenRandom](PyCRYPTPROV.md#pycryptprovcryptgenrandom)

    Generates random data of specified length&nbsp;

  - [CryptCreateHash](PyCRYPTPROV.md#pycryptprovcryptcreatehash)

    Creates a hash object for hashing large amounts of data&nbsp;

  - [CryptImportKey](PyCRYPTPROV.md#pycryptprovcryptimportkey)

    Imports a key exported by[PyCRYPTKEY::CryptExportKey](PyCRYPTKEY.md#pycryptkeycryptexportkey)&nbsp;

  - [CryptExportPublicKeyInfo](PyCRYPTPROV.md#pycryptprovcryptexportpublickeyinfo)

    Exports a public key to send to other users&nbsp;

  - [CryptImportPublicKeyInfo](PyCRYPTPROV.md#pycryptprovcryptimportpublickeyinfo)

    Imports another user's public key&nbsp;

## [PyCRYPTPROV](#pycryptprov).CryptCreateHash

[PyCRYPTHASH](#pycrypthash)= __CryptCreateHash( *Algid*  *, Key*  *, Flags* __ )
Creates a hash object for hashing large amounts of data

#### Parameters


  -  *Algid* : int

    An algorithm identifier, CALG_*.

  -  *Key=None* :[PyCRYPTKEY](#pycryptkey)

    Used only for keyed hashes (MAC or HMAC), use None otherwise

  -  *Flags=0* : int

    Reserved, use 0 if passed in

## [PyCRYPTPROV](#pycryptprov).CryptExportPublicKeyInfo

[PyCERT_PUBLIC_KEY_INFO](PyCERT.md#pycertpublic_key_info)= __CryptExportPublicKeyInfo( *KeySpec*  *, CertEncodingType* __ )
Exports a public key to send to other users 

Returned dict can be serialized for sending to another python application using pickle.dump

#### Parameters


  -  *KeySpec* : int

    AT_KEYEXCHANGE or AT_SIGNATURE

  -  *CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING* : int

    Specifies encoding for exported key info

## [PyCRYPTPROV](#pycryptprov).CryptGenKey

[PyCRYPTKEY](#pycryptkey)= __CryptGenKey( *Algid*  *, Flags*  *, KeyLen* __ )
Generates a key pair or a session key

#### Parameters


  -  *Algid* : int

    Algorithm identifier, one of the CALG_* values, or AT_KEYEXCHANGE/AT_SIGNATURE

  -  *Flags* : int

    Combination of CRYPT_CREATE_SALT,CRYPT_EXPORTABLE,CRYPT_NO_SALT,CRYPT_PREGEN,CRYPT_USER_PROTECTED,CRYPT_ARCHIVABLE

  -  *KeyLen=0* : int

    Length of key to generate, can be 0 to use provider's default key length

#### Comments
Differs from Api call in that the length is passed in separately

## [PyCRYPTPROV](#pycryptprov).CryptGenRandom

string = __CryptGenRandom( *Len*  *, SeedData* __ )
Generates random data of specified length

#### Parameters


  -  *Len* : int

    Number of bytes to generate

  -  *SeedData=None* : string

    Random seed data

## [PyCRYPTPROV](#pycryptprov).CryptGetProvParam

 __CryptGetProvParam( *Param*  *, Flags* __ )
Retrieves specified attribute of provider

#### Parameters


  -  *Param* : int

    One of the PP_* values

  -  *Flags=0* : int

    If param if PP_KEYSET_SEC_DESCR, can be a combination of OWNER_SECURITY_INFORMATION,GROUP_SECURITY_INFORMATION,DACL_SECURITY_INFORMATION,SACL_SECURITY_INFORMATION

#### Return Value
Type of returned object is dependent on the attribute requested

## [PyCRYPTPROV](#pycryptprov).CryptGetUserKey

[PyCRYPTKEY](#pycryptkey)= __CryptGetUserKey( *KeySpec* __ )
Returns a handle to one of user's key pairs

#### Parameters


  -  *KeySpec* : int

    AT_KEYEXCHANGE or AT_SIGNATURE (some providers may implement extra key specs)

## [PyCRYPTPROV](#pycryptprov).CryptImportKey

[PyCRYPTKEY](#pycryptkey)= __CryptImportKey( *Data*  *, PubKey*  *, Flags* __ )
Imports a key exported by[PyCRYPTKEY::CryptExportKey](PyCRYPTKEY.md#pycryptkeycryptexportkey)

#### Parameters


  -  *Data* : buffer

    The key blob to be imported

  -  *PubKey=None* :[PyCRYPTKEY](#pycryptkey)

    Key to be used to decrypt the blob, not used for importing public keys

  -  *Flags=0* : int

    Combination of CRYPT_EXPORTABLE, CRYPT_OAEP, CRYPT_NO_SALT, CRYPT_USER_PROTECTED

## [PyCRYPTPROV](#pycryptprov).CryptImportPublicKeyInfo

[PyCRYPTKEY](#pycryptkey)= __CryptImportPublicKeyInfo( *Info*  *, CertEncodingType* __ )
Imports another user's public key

#### Parameters


  -  *Info* : dict

    [PyCERT_PUBLIC_KEY_INFO](PyCERT.md#pycertpublic_key_info)dictionary as returned by[PyCRYPTPROV::CryptExportPublicKeyInfo](PyCRYPTPROV.md#pycryptprovcryptexportpublickeyinfo)

  -  *CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING* : int

    Specifies encoding for exported key info

## [PyCRYPTPROV](#pycryptprov).CryptReleaseContext

 __CryptReleaseContext( *Flags* __ )
Releases the CSP handle

#### Parameters


  -  *Flags=0* : int

    Reserved, use 0 if passed in