# PyCRYPTPROV

## PyCRYPTPROV Object



Handle to a cryptographic provider, created usingcryptoapi::CryptAcquireContext

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

## [PyCRYPTPROV](#pycryptprov)\.CryptCreateHash

[PyCRYPTHASH](#pycrypthash) =CryptCreateHash\(Algid, Key, Flags\)
Creates a hash object for hashing large amounts of data

#### Parameters


  - Algid : int

    An algorithm identifier, CALG\_\*\.

  - Key=None :[PyCRYPTKEY](#pycryptkey)

    Used only for keyed hashes \(MAC or HMAC\), use None otherwise

  - Flags=0 : int

    Reserved, use 0 if passed in

## [PyCRYPTPROV](#pycryptprov)\.CryptExportPublicKeyInfo

[PyCERT\_PUBLIC\_KEY\_INFO](PyCERT.md#pycertpublic_key_info) =CryptExportPublicKeyInfo\(KeySpec, CertEncodingType\)
Exports a public key to send to other users 

Returned dict can be serialized for sending to another python application using pickle\.dump

#### Parameters


  - KeySpec : int

    AT\_KEYEXCHANGE or AT\_SIGNATURE

  - CertEncodingType=X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING : int

    Specifies encoding for exported key info

## [PyCRYPTPROV](#pycryptprov)\.CryptGenKey

[PyCRYPTKEY](#pycryptkey) =CryptGenKey\(Algid, Flags, KeyLen\)
Generates a key pair or a session key

#### Parameters


  - Algid : int

    Algorithm identifier, one of the CALG\_\* values, or AT\_KEYEXCHANGE/AT\_SIGNATURE

  - Flags : int

    Combination of CRYPT\_CREATE\_SALT,CRYPT\_EXPORTABLE,CRYPT\_NO\_SALT,CRYPT\_PREGEN,CRYPT\_USER\_PROTECTED,CRYPT\_ARCHIVABLE

  - KeyLen=0 : int

    Length of key to generate, can be 0 to use provider's default key length

#### Comments


Differs from Api call in that the length is passed in separately

## [PyCRYPTPROV](#pycryptprov)\.CryptGenRandom



string =CryptGenRandom\(Len, SeedData\)
Generates random data of specified length

#### Parameters


  - Len : int

    Number of bytes to generate

  - SeedData=None : string

    Random seed data

## [PyCRYPTPROV](#pycryptprov)\.CryptGetProvParam

CryptGetProvParam\(Param, Flags\)
Retrieves specified attribute of provider

#### Parameters


  - Param : int

    One of the PP\_\* values

  - Flags=0 : int

    If param if PP\_KEYSET\_SEC\_DESCR, can be a combination of OWNER\_SECURITY\_INFORMATION,GROUP\_SECURITY\_INFORMATION,DACL\_SECURITY\_INFORMATION,SACL\_SECURITY\_INFORMATION

#### Return Value
Type of returned object is dependent on the attribute requested

## [PyCRYPTPROV](#pycryptprov)\.CryptGetUserKey

[PyCRYPTKEY](#pycryptkey) =CryptGetUserKey\(KeySpec\)
Returns a handle to one of user's key pairs

#### Parameters


  - KeySpec : int

    AT\_KEYEXCHANGE or AT\_SIGNATURE \(some providers may implement extra key specs\)

## [PyCRYPTPROV](#pycryptprov)\.CryptImportKey

[PyCRYPTKEY](#pycryptkey) =CryptImportKey\(Data, PubKey, Flags\)
Imports a key exported by[PyCRYPTKEY::CryptExportKey](PyCRYPTKEY.md#pycryptkeycryptexportkey)

#### Parameters


  - Data : buffer

    The key blob to be imported

  - PubKey=None :[PyCRYPTKEY](#pycryptkey)

    Key to be used to decrypt the blob, not used for importing public keys

  - Flags=0 : int

    Combination of CRYPT\_EXPORTABLE, CRYPT\_OAEP, CRYPT\_NO\_SALT, CRYPT\_USER\_PROTECTED

## [PyCRYPTPROV](#pycryptprov)\.CryptImportPublicKeyInfo

[PyCRYPTKEY](#pycryptkey) =CryptImportPublicKeyInfo\(Info, CertEncodingType\)
Imports another user's public key

#### Parameters


  - Info : dict

    [PyCERT\_PUBLIC\_KEY\_INFO](PyCERT.md#pycertpublic_key_info) dictionary as returned by[PyCRYPTPROV::CryptExportPublicKeyInfo](PyCRYPTPROV.md#pycryptprovcryptexportpublickeyinfo)

  - CertEncodingType=X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING : int

    Specifies encoding for exported key info

## [PyCRYPTPROV](#pycryptprov)\.CryptReleaseContext

CryptReleaseContext\(Flags\)
Releases the CSP handle

#### Parameters


  - Flags=0 : int

    Reserved, use 0 if passed in