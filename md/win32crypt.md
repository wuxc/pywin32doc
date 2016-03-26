# win32crypt


## Module win32crypt

An interface to the win32 Cryptography API

#### Methods

  - [CryptProtectData](win32crypt.md#win32cryptcryptprotectdata)

    Encrypts data using a session key derived from current user's logon credentials&nbsp;

  - [CryptUnprotectData](win32crypt.md#win32cryptcryptunprotectdata)

    Decrypts data that was encrypted using [win32crypt::CryptProtectData](win32crypt.md#win32cryptcryptprotectdata)&nbsp;

  - [CryptEnumProviders](win32crypt.md#win32cryptcryptenumproviders)

    Lists available cryptographic providers&nbsp;

  - [CryptEnumProviderTypes](win32crypt.md#win32cryptcryptenumprovidertypes)

    Lists available local cryptographic provider types&nbsp;

  - [CryptGetDefaultProvider](win32crypt.md#win32cryptcryptgetdefaultprovider)

    Returns default provider for local machine or current user&nbsp;

  - [CryptSetProviderEx](win32crypt.md#win32cryptcryptsetproviderex)

    Sets default provider \(for machine or user\) for specified type&nbsp;

  - [CryptAcquireContext](win32crypt.md#win32cryptcryptacquirecontext)

    Retrieve handle to a cryptographic service provider&nbsp;

  - [CryptFindLocalizedName](win32crypt.md#win32cryptcryptfindlocalizedname)

    Return localized name for predefined system stores \(Root, My, \.Default, \.LocalMachine\)&nbsp;

  - [CertEnumSystemStore](win32crypt.md#win32cryptcertenumsystemstore)

    Lists system stores&nbsp;

  - [CertEnumSystemStoreLocation](win32crypt.md#win32cryptcertenumsystemstorelocation)

    Lists system store locations&nbsp;

  - [CertEnumPhysicalStore](win32crypt.md#win32cryptcertenumphysicalstore)

    Lists physical stores on computer&nbsp;

  - [CertRegisterSystemStore](win32crypt.md#win32cryptcertregistersystemstore)

    Creates a new system certificate store&nbsp;

  - [CertUnregisterSystemStore](win32crypt.md#win32cryptcertunregistersystemstore)

    Unregister specified store, optionally deleting it&nbsp;

  - [CertOpenStore](win32crypt.md#win32cryptcertopenstore)

    Opens a certificate store&nbsp;

  - [CertOpenSystemStore](win32crypt.md#win32cryptcertopensystemstore)

    Opens most commonly used Certificate Stores&nbsp;

  - [CryptFindOIDInfo](win32crypt.md#win32cryptcryptfindoidinfo)

    Retreives information about an object identifier or alorithm identifier&nbsp;

  - [CertAlgIdToOID](win32crypt.md#win32cryptcertalgidtooid)

    Converts an integer ALG\_ID to it's szOID\_ string representation&nbsp;

  - [CertOIDToAlgId](win32crypt.md#win32cryptcertoidtoalgid)

    Converts a string object identfier to a numeric algorith identifier&nbsp;

  - [CryptGetKeyIdentifierProperty](win32crypt.md#win32cryptcryptgetkeyidentifierproperty)

    Retrieves a property from a certificate by it's key indentifier&nbsp;

  - [CryptEnumKeyIdentifierProperties](win32crypt.md#win32cryptcryptenumkeyidentifierproperties)

    Lists private keys for user or machine&nbsp;

  - [CryptEnumOIDInfo](win32crypt.md#win32cryptcryptenumoidinfo)

    Lists registered object identfiers&nbsp;

  - [CertAddSerializedElementToStore](win32crypt.md#win32cryptcertaddserializedelementtostore)

    Creates a new Certificate, CRL, or CTL context from serialized data&nbsp;

  - [CryptQueryObject](win32crypt.md#win32cryptcryptqueryobject)

    Determines the type of serialized or encoded data&nbsp;

  - [CryptDecodeMessage](win32crypt.md#win32cryptcryptdecodemessage)

    Decrypts an encoded message and verifies a signature&nbsp;

  - [CryptEncryptMessage](win32crypt.md#win32cryptcryptencryptmessage)

    Encrypts and encodes a message&nbsp;

  - [CryptDecryptMessage](win32crypt.md#win32cryptcryptdecryptmessage)

    Decrypts an encrypted and encoded message&nbsp;

  - [CryptSignAndEncryptMessage](win32crypt.md#win32cryptcryptsignandencryptmessage)

    Decrypts an encrypted and encoded message&nbsp;

  - [CryptVerifyMessageSignature](win32crypt.md#win32cryptcryptverifymessagesignature)

    Verifies a message signature&nbsp;

  - [CryptGetMessageCertificates](win32crypt.md#win32cryptcryptgetmessagecertificates)

    Extracts certificates encoded in a message&nbsp;

  - [CryptGetMessageSignerCount](win32crypt.md#win32cryptcryptgetmessagesignercount)

    Finds the number of signers of an encoded message&nbsp;

  - [CryptSignMessage](win32crypt.md#win32cryptcryptsignmessage)

    Signs and encodes a message&nbsp;

  - [CryptVerifyDetachedMessageSignature](win32crypt.md#win32cryptcryptverifydetachedmessagesignature)

    Verifies a signature that is encoded separately from the data&nbsp;

  - [CryptDecryptAndVerifyMessageSignature](win32crypt.md#win32cryptcryptdecryptandverifymessagesignature)

    Decrypts and decodes a signed message, and verifies its signatures&nbsp;

  - [CryptEncodeObjectEx](win32crypt.md#win32cryptcryptencodeobjectex)

    Serializes and ASN encodes cryptographic structures&nbsp;

  - [CryptDecodeObjectEx](win32crypt.md#win32cryptcryptdecodeobjectex)

    Decodes ASN encodes data&nbsp;

  - [CertNameToStr](win32crypt.md#win32cryptcertnametostr)

    Converts an encoded CERT\_NAME\_INFO into a formatted string&nbsp;

  - [CryptFormatObject](win32crypt.md#win32cryptcryptformatobject)

    Formats an encoded buffer into a readable string&nbsp;

  - [PFXImportCertStore](win32crypt.md#win32cryptpfximportcertstore)

    Creates a certificate store from PKCS\#12 data \(\*\.PFX files\)&nbsp;

  - [PFXVerifyPassword](win32crypt.md#win32cryptpfxverifypassword)

    Checks if a PFX blob can be decrypted with given password&nbsp;

  - [PFXIsPFXBlob](win32crypt.md#win32cryptpfxispfxblob)

    Checks if data buffer contains a PFX blob&nbsp;

  - [CryptBinaryToString](win32crypt.md#win32cryptcryptbinarytostring)

    Formats a binary buffer into the specified type of string&nbsp;

  - [CryptStringToBinary](win32crypt.md#win32cryptcryptstringtobinary)

    Converts a formatted string back into raw bytes&nbsp;


## [win32crypt](win32crypt.md#win32crypt)\.CertAddSerializedElementToStore

[PyCERT\_CONTEXT](PyCERT.md#pycertcontext) = CertAddSerializedElementToStore\(CertStore, Element

, AddDisposition

, ContextTypeFlags

, Flags

\)
Imports a serialized Certificate context, CRL, or CTL

#### Parameters

  - CertStore : [PyCERTSTORE](PyCERTSTORE.md)

    Certificate Store to which the context will be added, can be None

  - Element : buffer

    Serialized data

  - AddDisposition : int

    one of CERT\_STORE\_ADD\_\* values

  - ContextTypeFlags=CERT\_STORE\_CERTIFICATE\_CONTEXT\_FLAG : int

    One of CERT\_STORE\_\*\_CONTEXT\_FLAG constants

  - Flags=0 : int

    Reserved, use only 0

#### Comments

Currently only Certificate contexts are supported


## [win32crypt](win32crypt.md#win32crypt)\.CertAlgIdToOID

string = CertAlgIdToOID\(AlgId\)
Converts an integer ALG\_ID to it's szOID\_ string representation

#### Parameters

  - AlgId : int

    An algorithm identifier

#### Comments

If there is no corresponding OID, None is returned


## [win32crypt](win32crypt.md#win32crypt)\.CertEnumPhysicalStore

\[[PyUnicode](PyUnicode.md),\.\.\.\] = CertEnumPhysicalStore\(pvSystemStore, dwFlags

\)
Lists physical stores on computer

#### Parameters

  - pvSystemStore : [PyUnicode](PyUnicode.md)

    Name of system store to enumerate physical locations for

  - dwFlags : int

    CERT\_SYSTEM\_STORE\_\* constant, CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG  not supported yet


## [win32crypt](win32crypt.md#win32crypt)\.CertEnumSystemStore

\[[PyUnicode](PyUnicode.md),\.\.\.\] = CertEnumSystemStore\(dwFlags, pvSystemStoreLocationPara

\)
Lists system stores

#### Parameters

  - dwFlags : int

    CERT\_SYSTEM\_STORE\_\* location, can be combined with CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG

  - pvSystemStoreLocationPara=None : PyCERT\_SYSTEM\_STORE\_RELOCATE\_PARA

    Optional - If flags contains CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG must be a sequence \(PyHkey, unicode\) representing a CERT\_SYSTEM\_STORE\_RELOCATE\_PARA, otherwise should be a unicode store name


## [win32crypt](win32crypt.md#win32crypt)\.CertEnumSystemStoreLocation

\[[PyUnicode](PyUnicode.md),\.\.\.\] = CertEnumSystemStoreLocation\(Flags\)
Lists system store locations

#### Parameters

  - Flags=0 : int

    Reserved, must be 0 if passed in


## [win32crypt](win32crypt.md#win32crypt)\.CertNameToStr

str = CertNameToStr\(Name, StrType

, CertEncodingType

\)
Converts an encoded CERT\_NAME\_INFO into a formatted string

#### Parameters

  - Name : str

    String containing an encoded CERT\_NAME\_INFO, as used with certificate Issuer and Subject

  - StrType=CERT\_SIMPLE\_NAME\_STR : int

    Type of string to format, one of CERT\_SIMPLE\_NAME\_STR,CERT\_OID\_NAME\_STR,CERT\_X500\_NAME\_STR

  - CertEncodingType=X509\_ASN\_ENCODING : int

    Input encoding

#### Comments

Usually this encoded data is contained in a CERT\_NAME\_BLOB


## [win32crypt](win32crypt.md#win32crypt)\.CertOIDToAlgId

int = CertOIDToAlgId\(ObjId\)
Converts a string object identfier to a numeric algorith identifier

#### Parameters

  - ObjId : string

    String szOID\_\* identifier

#### Comments

If no matching ALG\_ID is found, 0 is returned


## [win32crypt](win32crypt.md#win32crypt)\.CertOpenStore

[PyCERTSTORE](PyCERTSTORE.md) = CertOpenStore\(StoreProvider, MsgAndCertEncodingType

, CryptProv

, Flags

, Para

\)
Opens a certificate store

#### Parameters

  - StoreProvider : int

    CERT\_STORE\_PROV\_\*, currently does not accept string provider names

  - MsgAndCertEncodingType : int

    Only used with CERT\_STORE\_PROV\_MSG, CERT\_STORE\_PROV\_PKCS7, and CERT\_STORE\_PROV\_FILENAME\. 

Usually should be X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

  - CryptProv : [PyCRYPTPROV](PyCRYPTPROV.md)

    Handle to a CSP, can be None to use default provider

  - Flags : int

    Combination of CERT\_STORE\_\*\_FLAG flags

  - Para=None : object

    PyCERT\_SYSTEM\_STORE\_RELOCATE\_PARA

, or data specific to provider


## [win32crypt](win32crypt.md#win32crypt)\.CertOpenSystemStore

[PyCERTSTORE](PyCERTSTORE.md) = CertOpenSystemStore\(SubsystemProtocol, Prov

\)
Opens most commonly used Certificate Stores

#### Parameters

  - SubsystemProtocol : [PyUnicode](PyUnicode.md)

    Name of store to open, will be created if it doesn't already exist

  - Prov=None : [PyCRYPTPROV](PyCRYPTPROV.md)

    Handle to CSP, use None for default provider


## [win32crypt](win32crypt.md#win32crypt)\.CertRegisterSystemStore

CertRegisterSystemStore\(SystemStore, Flags\)
Registers a certificate store

#### Parameters

  - SystemStore : [PyUnicode](PyUnicode.md)

    string/unicode name of store to be registered, or a sequence of \(PyHkey, unicode\) representing a CERT\_SYSTEM\_STORE\_RELOCATE\_PARA struct

  - Flags : int

    One of the CERT\_SYSTEM\_STORE\_\* location constants, can also be combined with CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG and CERT\_STORE\_CREATE\_NEW\_FLAG


## [win32crypt](win32crypt.md#win32crypt)\.CertUnregisterSystemStore

CertUnregisterSystemStore\(SystemStore, Flags\)
Unregisters a certificate store

#### Parameters

  - SystemStore : [PyUnicode](PyUnicode.md)

    Name of System store to be unregistered

  - Flags : int

    CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG, CERT\_STORE\_DELETE\_FLAG \(CERT\_SYSTEM\_STORE\_RELOCATE\_FLAG  not supported yet\)


## [win32crypt](win32crypt.md#win32crypt)\.CryptAcquireContext

[PyCRYPTPROV](PyCRYPTPROV.md) = CryptAcquireContext\(Container, Provider

, ProvType

, Flags

\)
Retrieve handle to a cryptographic service provider

#### Parameters

  - Container : [PyUnicode](PyUnicode.md)

    Name of key container, can be none to use a Provider's default key container \(usually username\)

  - Provider : [PyUnicode](PyUnicode.md)

    Name of cryptographic provider\. \(MS\_\*\_PROV\) Use None for user's default provider\.

  - ProvType : int

    One of the PROV\_\* constants

  - Flags : int

    Combination of CRYPT\_VERIFYCONTEXT,CRYPT\_NEWKEYSET,CRYPT\_MACHINE\_KEYSET,CRYPT\_DELETEKEYSET,CRYPT\_SILENT

#### Return Value
Returns None if CRYPT\_DELETEKEYSET is specified, otherwise returns a handle to the provider


## [win32crypt](win32crypt.md#win32crypt)\.CryptBinaryToString

str = CryptBinaryToString\(Binary, Flags

\)
Formats a binary buffer into the specified type of string

#### Parameters

  - Binary : bytes

    Buffer containing raw data to be formatted

  - Flags : int

    Type of output desired, win32cryptcon\.CRYPT\_STRING\_\* value

#### Win32 API References

  - Search for CryptBinaryToString at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CryptBinaryToString.md), [google](http://www.google.com/search?q=CryptBinaryToString.md) or [google groups](http://groups.google.com/groups?q=CryptBinaryToString.md)\.


## [win32crypt](win32crypt.md#win32crypt)\.CryptDecodeMessage

dict = CryptDecodeMessage\(EncodedBlob, DecryptPara

, VerifyPara

, MsgTypeFlags

, SignerIndex

, PrevInnerContentType

, ReturnData

\)
Decodes and decrypts a message, and verifies its signatures

#### Parameters

  - EncodedBlob : buffer

    Data to be decoded

  - DecryptPara : dict

    [PyCRYPT\_DECRYPT\_MESSAGE\_PARA](PyCRYPT.md#pycryptdecrypt_message_para) containing decryption parms

  - VerifyPara=None : dict

    [PyCRYPT\_VERIFY\_MESSAGE\_PARA](PyCRYPT.md#pycryptverify_message_para) containing signature verification parms

  - MsgTypeFlags=CMSG\_ALL\_FLAGS : int

    Combination of CMSG\_DATA\_FLAG, CMSG\_SIGNED\_FLAG, CMSG\_ENVELOPED\_FLAG, CMSG\_SIGNED\_AND\_ENVELOPED\_FLAG, or CMSG\_HASHED\_FLAG

  - SignerIndex=0 : int

    Index of the signer to verify,  ignored if message is not signed\.

  - PrevInnerContentType=0 : int

    Content type returned from previous call, used during subsequent pass on a nested message

  - ReturnData=True : boolean

    Indicates if decoded data should be returned\.

#### Comments

Only one level of encoding is interpreted\.  Some types of messages will need multiple calls to completely decode\. 

For example, to decode a message created by [win32crypt::CryptSignAndEncryptMessage](win32crypt.md#win32cryptcryptsignandencryptmessage), one pass with CMSG\_ENVELOPED\_FLAG 

and a second pass using CMSG\_SIGNED\_FLAG are required to recover the original message text\.

#### Return Value
Output params are returned as a dict containing: 

\{MsgType:int\},&\#09&\#09&\#09&\#09&\#09&nbsp&nbsp\#\#Type of message decoded, one of CMSG\_DATA,CMSG\_SIGNED,CMSG\_ENVELOPED,CMSG\_SIGNED\_AND\_ENVELOPED,CMSG\_HASHED 

InnerContentType:int,&\#09&\#09&\#09&nbsp&nbsp\#\#Type of decoded content returned, uses same set of values as MsgType\.  CMSG\_DATA indicates unencoded data\. 

Decoded:str,&\#09&\#09&\#09&\#09&\#09&nbsp&nbsp\#\#The decoded data, will be None if ReturnData is False\. 

XchgCert:[PyCERT\_CONTEXT](PyCERT.md#pycertcontext),&\#09&nbsp&nbsp\#\#Certificate used to decode message 

SignerCert:[PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\}&\#09&nbsp&nbsp\#\#Certificate used to sign message


## [win32crypt](win32crypt.md#win32crypt)\.CryptDecodeObjectEx

object = CryptDecodeObjectEx\(StructType, Encoded

, Flags

, CertEncodingType

, DecodePara

\)
Decodes ASN encoded data

#### Parameters

  - StructType : str/int

    An OID identifying the type of data to be decoded, can be either str or int

  - Encoded : str

    String or buffer containing ASN encoded data

  - Flags=0 : int

    Encoding options, can be combination CRYPT\_UNICODE\_\* constants\.  CRYPT\_ENCODE\_ALLOC\_FLAG is added to flags\.\.

  - CertEncodingType=X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING : int

    Encoding types

  - DecodePara=None : object

    Not supported, use only None

   

       OID

   

   

       Object returned

   

szOID\_ENHANCED\_KEY\_USAGESequence of OIDs

X509\_ENHANCED\_KEY\_USAGESequence of OIDs

szOID\_KEY\_USAGE[PyCRYPT\_BIT\_BLOB](PyCRYPT.md#pycryptbit_blob)

X509\_KEY\_USAGE[PyCRYPT\_BIT\_BLOB](PyCRYPT.md#pycryptbit_blob)

X509\_BITS[PyCRYPT\_BIT\_BLOB](PyCRYPT.md#pycryptbit_blob)

szOID\_SUBJECT\_ALT\_NAME[PyCERT\_ALT\_NAME\_INFO](PyCERT.md#pycertalt_name_info)

szOID\_SUBJECT\_ALT\_NAME2[PyCERT\_ALT\_NAME\_INFO](PyCERT.md#pycertalt_name_info)

szOID\_ISSUER\_ALT\_NAME[PyCERT\_ALT\_NAME\_INFO](PyCERT.md#pycertalt_name_info)

szOID\_ISSUER\_ALT\_NAME2[PyCERT\_ALT\_NAME\_INFO](PyCERT.md#pycertalt_name_info)

szOID\_NEXT\_UPDATE\_LOCATION[PyCERT\_ALT\_NAME\_INFO](PyCERT.md#pycertalt_name_info)

X509\_ALTERNATE\_NAME[PyCERT\_ALT\_NAME\_INFO](PyCERT.md#pycertalt_name_info)

X509\_NAME\_VALUE[PyCERT\_NAME\_VALUE](PyCERT.md#pycertname_value)

X509\_UNICODE\_ANY\_STRING[PyCERT\_NAME\_VALUE](PyCERT.md#pycertname_value)

X509\_UNICODE\_NAME\_VALUE[PyCERT\_NAME\_VALUE](PyCERT.md#pycertname_value)

X509\_NAME[PyCERT\_NAME\_INFO](PyCERT.md#pycertname_info)

X509\_UNICODE\_NAME[PyCERT\_NAME\_INFO](PyCERT.md#pycertname_info)

szOID\_KEY\_ATTRIBUTES[PyCERT\_KEY\_ATTRIBUTES\_INFO](PyCERT.md#pycertkey_attributes_info)

X509\_KEY\_ATTRIBUTES[PyCERT\_KEY\_ATTRIBUTES\_INFO](PyCERT.md#pycertkey_attributes_info)

szOID\_BASIC\_CONSTRAINTS[PyCERT\_BASIC\_CONSTRAINTS\_INFO](PyCERT.md#pycertbasic_constraints_info)

X509\_BASIC\_CONSTRAINTS[PyCERT\_BASIC\_CONSTRAINTS\_INFO](PyCERT.md#pycertbasic_constraints_info)

szOID\_BASIC\_CONSTRAINTS2[PyCERT\_BASIC\_CONSTRAINTS2\_INFO](PyCERT.md#pycertbasic_constraints2_info)

X509\_BASIC\_CONSTRAINTS2[PyCERT\_BASIC\_CONSTRAINTS2\_INFO](PyCERT.md#pycertbasic_constraints2_info)

szOID\_CERT\_POLICIESSequence of [PyCERT\_POLICY\_INFO](PyCERT.md#pycertpolicy_info) objects

szOID\_APPLICATION\_CERT\_POLICIESSequence of [PyCERT\_POLICY\_INFO](PyCERT.md#pycertpolicy_info) objects

X509\_CERT\_POLICIESSequence of [PyCERT\_POLICY\_INFO](PyCERT.md#pycertpolicy_info) objects

szOID\_SUBJECT\_KEY\_IDENTIFIERBinary string containing the key identifier

szOID\_AUTHORITY\_KEY\_IDENTIFIER[PyCERT\_AUTHORITY\_KEY\_ID\_INFO](PyCERT.md#pycertauthority_key_id_info)

X509\_AUTHORITY\_KEY\_ID[PyCERT\_AUTHORITY\_KEY\_ID\_INFO](PyCERT.md#pycertauthority_key_id_info)

#### Return Value
Type of object returned is dependent on the StructType to be decoded


## [win32crypt](win32crypt.md#win32crypt)\.CryptDecryptAndVerifyMessageSignature

dict = CryptDecryptAndVerifyMessageSignature\(EncryptedBlob, DecryptPara

, VerifyPara

, SignerIndex

\)
Decrypts and decodes a signed message, and verifies its signatures

#### Parameters

  - EncryptedBlob : buffer

    Encoded message to be decrypted\.

  - DecryptPara : [PyCRYPT\_DECRYPT\_MESSAGE\_PARA](PyCRYPT.md#pycryptdecrypt_message_para)

    Decryption parms

  - VerifyPara=None : [PyCRYPT\_VERIFY\_MESSAGE\_PARA](PyCRYPT.md#pycryptverify_message_para)

    Signature verification parms

  - SignerIndex=0 : int

    Index of the signer to verify, zero-based\.

#### Comments

Usage is similar to CryptDecodeMessage, except that it undoes all levels of encoding and 

returns the bare message\.   This function is the counterpart of CryptSignAndEncryptMessage\.

#### Return Value
Output params are returned as a dict containing: 

Decrypted:str,&\#09&\#09&\#09&\#09&\#09&nbsp&nbsp\#\#The decrypted message contents 

XchgCert:[PyCERT\_CONTEXT](PyCERT.md#pycertcontext),&\#09&nbsp&nbsp\#\#Certificate whose private key was used to decrypt message 

SignerCert:[PyCERT\_CONTEXT](PyCERT.md#pycertcontext)&\#09&nbsp&nbsp\#\#Certificate used to sign message


## [win32crypt](win32crypt.md#win32crypt)\.CryptDecryptMessage

str, [PyCERT\_CONTEXT](PyCERT.md#pycertcontext) = CryptDecryptMessage\(DecryptPara, EncryptedBlob

\)
Decrypts an encrypted and encoded message

#### Parameters

  - DecryptPara : [PyCRYPT\_DECRYPT\_MESSAGE\_PARA](PyCRYPT.md#pycryptdecrypt_message_para)

    Dictionary containing decryption parameters

  - EncryptedBlob : buffer

    Buffer containing an encrypted message

#### Return Value
Returns the decrypted message and a handle to the certificate used to decrypt it


## [win32crypt](win32crypt.md#win32crypt)\.CryptEncodeObjectEx

str = CryptEncodeObjectEx\(StructType, StructInfo

, Flags

, CertEncodingType

, EncodePara

\)
Serializes and ASN encodes cryptographic structures

#### Parameters

  - StructType : str/int

    OID identifying type of data to be encoded, either szOID\_\* string or a numeric id

  - StructInfo : dict

    Information to be encoded\.  Contents of dict are dependent on StructType

  - Flags=0 : int

    Encoding options, combination of CRYPT\_UNICODE\_\* constants\.  CRYPT\_ENCODE\_ALLOC\_FLAG is added to flags\.\.

  - CertEncodingType=X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING : int

    Encoding types

  - EncodePara=None : object

    Not supported, use only None




## [win32crypt](win32crypt.md#win32crypt)\.CryptEncryptMessage

str = CryptEncryptMessage\(EncryptPara, RecipientCert

, ToBeEncrypted

\)
Encrypts and encodes a message

#### Parameters

  - EncryptPara : [PyCRYPT\_ENCRYPT\_MESSAGE\_PARA](PyCRYPT.md#pycryptencrypt_message_para)

    Encryption parameters

  - RecipientCert : \([PyCERT\_CONTEXT](PyCERT.md#pycertcontext),\.\.\.\)

    Sequence of handles to recipients' certificates

  - ToBeEncrypted : buffer

    Data to be encrypted


## [win32crypt](win32crypt.md#win32crypt)\.CryptEnumKeyIdentifierProperties

list = CryptEnumKeyIdentifierProperties\(KeyIdentifier, PropId

, Flags

, ComputerName

\)
Enumerates private keys for certificates and their properties

#### Parameters

  - KeyIdentifier=None : string

    Id of a certificate key, can be None for all keys

  - PropId=0 : int

    CERT\_\*\_PROP\_ID constant\. Limits returned values to specified propery, Use 0 for all

  - Flags=0 : int

    Can be CRYPT\_KEYID\_MACHINE\_FLAG to list keys for local machine, or remote machine if ComputerName is given

  - ComputerName=None : [PyUnicode](PyUnicode.md)

    Name of remote computer, use None for local machine


## [win32crypt](win32crypt.md#win32crypt)\.CryptEnumOIDInfo

list = CryptEnumOIDInfo\(GroupId\)
Lists registered Object Identifiers that belong to specified group

#### Parameters

  - GroupId=0 : int

    The type of OIDs to enmerate, one of the CRYPT\_\*\_OID\_GROUP\_ID constants or 0 to list all


## [win32crypt](win32crypt.md#win32crypt)\.CryptEnumProviderTypes

\[\([PyUnicode](PyUnicode.md),int\),\.\.\.\] = CryptEnumProviderTypes\(\)
Lists available local cryptographic provider types

#### Comments

Windows XP sp3 has a bug that causes this function to always fail with ERROR\_MORE\_DATA \(234\) 

See KB959160 for a hotfix

#### Return Value
Returns a sequence of tuples containing name and identifier of provider types


## [win32crypt](win32crypt.md#win32crypt)\.CryptEnumProviders

\[\([PyUnicode](PyUnicode.md),int\),\.\.\.\] = CryptEnumProviders\(\)
List cryptography providers

#### Return Value
Returns a sequence of tuples containing provider name and type


## [win32crypt](win32crypt.md#win32crypt)\.CryptFindLocalizedName

[PyUnicode](PyUnicode.md) = CryptFindLocalizedName\(CryptName\)
Returns localized name for predefined system stores \(Root, My, \.Default, \.LocalMachine\)

#### Parameters

  - CryptName : [PyUnicode](PyUnicode.md)

    Name of a system store


## [win32crypt](win32crypt.md#win32crypt)\.CryptFindOIDInfo

dict = CryptFindOIDInfo\(KeyType, Key

, GroupId

\)
Returns information about an algorithm identifier or object identifier

#### Parameters

  - KeyType : int

    One of CRYPT\_OID\_INFO\_OID\_KEY,CRYPT\_OID\_INFO\_NAME\_KEY,CRYPT\_OID\_INFO\_ALGID\_KEY,CRYPT\_OID\_INFO\_SIGN\_KEY

  - Key : object

    Type is dependent on KeyType

  - GroupId=0 : int

    CRYPT\_\*\_GROUP\_ID constant, or 0

#### Return Value
Returns a dictionary of CRYPT\_OID\_INFO data




## [win32crypt](win32crypt.md#win32crypt)\.CryptFormatObject

str = CryptFormatObject\(StructType, Encoded

, FormatStrType

, CertEncodingType

, FormatType

, FormatStruct

\)
Formats an encoded buffer into a readable string

#### Parameters

  - StructType : str/int

    OID identifying the type of encoded data, one of the szOID\_\* strings or an integer OID

  - Encoded : str

    String containing encoded data to be formatted

  - FormatStrType=0 : int

    String formatting options, combination of CRYPT\_FORMAT\_STR\_MULTI\_LINE, CRYPT\_FORMAT\_STR\_NO\_HEX

  - CertEncodingType=X509\_ASN\_ENCODING : int

    Input encoding

  - FormatType=0 : int

    Reserved, use only 0

  - FormatStruct=None : None

    Reserved, use only None

#### Comments

Will handle all of the common certificate extension types

#### Win32 API References

  - Search for CryptFormatObject at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CryptFormatObject.md), [google](http://www.google.com/search?q=CryptFormatObject.md) or [google groups](http://groups.google.com/groups?q=CryptFormatObject.md)\.


## [win32crypt](win32crypt.md#win32crypt)\.CryptGetDefaultProvider

[PyUnicode](PyUnicode.md) = CryptGetDefaultProvider\(ProvType, Flags

\)
Returns default provider for local machine or current user

#### Parameters

  - ProvType : int

    Type of provider \(PROV\_\* constant\)

  - Flags : int

    CRYPT\_MACHINE\_DEFAULT or CRYPT\_USER\_DEFAULT


## [win32crypt](win32crypt.md#win32crypt)\.CryptGetKeyIdentifierProperty

object = CryptGetKeyIdentifierProperty\(KeyIdentifier, PropId

, Flags

, ComputerName

\)
Retrieves a property from a certificate by its key indentifier

#### Parameters

  - KeyIdentifier : string

    Hash that identifies a certificate key

  - PropId=CERT\_KEY\_PROV\_INFO\_PROP\_ID : int

    Property identifier, one of the CERT\_\*\_PROP\_ID values

  - Flags=0 : int

    Use CRYPT\_KEYID\_MACHINE\_FLAG for machine keyset\. \(CRYPT\_KEYID\_ALLOC\_FLAG is always added to Flags\)

  - ComputerName=None : [PyUnicode](PyUnicode.md)

    Name of remote computer, use None for local machine

#### Comments

CERT\_KEY\_PROV\_INFO\_PROP\_ID is only property currently supported


## [win32crypt](win32crypt.md#win32crypt)\.CryptGetMessageCertificates

[PyCERTSTORE](PyCERTSTORE.md) = CryptGetMessageCertificates\(SignedBlob, MsgAndCertEncodingType

, CryptProv

, Flags

\)
Extracts certificates encoded in a message

#### Parameters

  - SignedBlob : buffer

    Buffer containing a signed message

  - MsgAndCertEncodingType=X509\_ASN\_ENCODING|PKCS\_7\_ASN\_ENCODING : int

    Message and certificate encoding types

  - CryptProv=None : [PyCRYPTPROV](PyCRYPTPROV.md)

    Handle to a CSP, use None for default

  - Flags=0 : int

    Same flags used with [win32crypt::CertOpenStore](win32crypt.md#win32cryptcertopenstore)


## [win32crypt](win32crypt.md#win32crypt)\.CryptGetMessageSignerCount

int = CryptGetMessageSignerCount\(SignedBlob, MsgEncodingType

\)
Finds the number of signers of an encoded message

#### Parameters

  - SignedBlob : buffer

    Buffer containing a signed message

  - MsgEncodingType=X509\_ASN\_ENCODING|PKCS\_7\_ASN\_ENCODING : int

    Message encoding type


## [win32crypt](win32crypt.md#win32crypt)\.CryptProtectData

bytes = CryptProtectData\(DataIn, DataDescr

, OptionalEntropy

, Reserved

, PromptStruct

, Flags

\)
Encrypts data using a session key derived from current user's logon credentials

#### Parameters

  - DataIn : bytes

    Data to be encrypted\.

  - DataDescr=None : [PyUnicode](PyUnicode.md)

    Description to add to the data

  - OptionalEntropy=None : bytes

    Extra entropy \(eg password\) for encryption process, can be None

  - Reserved=None : None

    Must be None

  - PromptStruct=None : [PyCRYPTPROTECT\_PROMPTSTRUCT](PyCRYPTPROTECT.md#pycryptprotectpromptstruct)

    Contains options for UI display during encryption and decryption, can be None

  - Flags=0 : int

    Combination of CRYPTPROTECT\_\* flags


## [win32crypt](win32crypt.md#win32crypt)\.CryptQueryObject

dict = CryptQueryObject\(ObjectType, Object

, ExpectedContentTypeFlags

, ExpectedFormatTypeFlags

, Flags

\)
Determines the cryptographic type of input data

#### Parameters

  - ObjectType : int

    Type of input, CERT\_QUERY\_OBJECT\_BLOB or CERT\_QUERY\_OBJECT\_FILE

  - Object : str

    Raw data or a filename containing the data to be queried depending on ObjectType

  - ExpectedContentTypeFlags=CERT\_QUERY\_CONTENT\_FLAG\_ALL : int

    One of the CERT\_QUERY\_CONTENT\_FLAG\_\* constants

  - ExpectedFormatTypeFlags=CERT\_QUERY\_FORMAT\_FLAG\_ALL : int

    One of the CERT\_QUERY\_FORMAT\_FLAG\_\* constants

  - Flags=0 : int

    Reserved, use only 0

#### Return Value
Returns a dictionary containing 

\{MsgAndCertEncodingType:int,&\#09\#\# encoding type, usually X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING 

ContentType:int,&\#09&\#09&\#09&\#09\#\# One of the CERT\_QUERY\_CONTENT\_\* constants 

FormatType:int,&\#09&\#09&\#09&\#09&\#09\#\# One of the CERT\_QUERY\_FORMAT\_\* constants 

CertStore:[PyCERTSTORE](PyCERTSTORE.md),&\#09&\#09\#\# Handle to certificate store containing all certficates in the object, may be None 

Msg:[PyCRYPTMSG](PyCRYPTMSG.md),&\#09&\#09&\#09&\#09\#\# If input doesn't contains a PKCS7 message, will be None 

Context:[PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\}&\#09&\#09\#\# A certificate, CRL, or CTL context depending on ContentType, may be None


## [win32crypt](win32crypt.md#win32crypt)\.CryptSetProviderEx

CryptSetProviderEx\(ProvName, ProvType, Flags\)
Sets default provider \(for machine or user\) for specified type

#### Parameters

  - ProvName : [PyUnicode](PyUnicode.md)

    Name of new default provider \(MS\_\*\_PROV value\)

  - ProvType : int

    One of the PROV\_\* provider types

  - Flags : int

    CRYPT\_MACHINE\_DEFAULT or CRYPT\_USER\_DEFAULT\.  Combine with CRYPT\_DELETE\_DEFAULT to remove default\.


## [win32crypt](win32crypt.md#win32crypt)\.CryptSignAndEncryptMessage

str = CryptSignAndEncryptMessage\(SignPara, EncryptPara

, RecipientCert

, ToBeSignedAndEncrypted

\)
Encrypts, encodes and signs a message using a certificate

#### Parameters

  - SignPara : [PyCRYPT\_SIGN\_MESSAGE\_PARA](PyCRYPT.md#pycryptsign_message_para)

    Message signing parameters

  - EncryptPara : [PyCRYPT\_ENCRYPT\_MESSAGE\_PARA](PyCRYPT.md#pycryptencrypt_message_para)

    Encryption parameters

  - RecipientCert : \([PyCERT\_CONTEXT](PyCERT.md#pycertcontext),\.\.\.\)

    Sequence of certificates of intended recipients

  - ToBeSignedAndEncrypted : str

    Buffer containing data to be encoded in the message


## [win32crypt](win32crypt.md#win32crypt)\.CryptSignMessage

str = CryptSignMessage\(SignPara, ToBeSigned

, DetachedSignature

\)
Signs and encodes a message

#### Parameters

  - SignPara : [PyCRYPT\_SIGN\_MESSAGE\_PARA](PyCRYPT.md#pycryptsign_message_para)

    Message signing parameters

  - ToBeSigned : \(str,\.\.\.\)

    Sequence of strings containing message data\.  Can only contain 1 string if DetachedSignature parm is False\.

  - DetachedSignature=False : boolean

    If True, only the signature itself is encoded in output msg\.


## [win32crypt](win32crypt.md#win32crypt)\.CryptStringToBinary

bytes, int, int = CryptStringToBinary\(String, Flags

\)
Converts a formatted string back into raw bytes

#### Parameters

  - String : str

    Formatted string to be converted to raw binary data

  - Flags : int

    Input format \(win32cryptcon\.CRYPT\_STRING\_\*\)

#### Win32 API References

  - Search for CryptStringToBinary at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CryptStringToBinary.md), [google](http://www.google.com/search?q=CryptStringToBinary.md) or [google groups](http://groups.google.com/groups?q=CryptStringToBinary.md)\.

#### Return Value
Returns the decoded binary data, number of header characters skipped, and CRYPT\_STRING\_\* value 

denoting the type of data found \(used if input Flags is one of \*\_ANY values\)


## [win32crypt](win32crypt.md#win32crypt)\.CryptUnprotectData

\(str, bytes\) = CryptUnprotectData\(DataIn, OptionalEntropy

, Reserved

, PromptStruct

, Flags

\)
Decrypts data that was encrypted using [win32crypt::CryptProtectData](win32crypt.md#win32cryptcryptprotectdata)\.

#### Parameters

  - DataIn : bytes

    Data to be decrypted\.

  - OptionalEntropy=None : bytes

    Extra entropy passed to CryptProtectData

  - Reserved=None : None

    Must be None

  - PromptStruct=None : [PyCRYPTPROTECT\_PROMPTSTRUCT](PyCRYPTPROTECT.md#pycryptprotectpromptstruct)

    Contains options for UI display during encryption and decryption, can be None

  - Flags=0 : int

    Combination of CRYPTPROTECT\_\* flags

#### Return Value
The result is a tuple of \(description, data\) where description 

is the description that was passed to [win32crypt::CryptProtectData](win32crypt.md#win32cryptcryptprotectdata), and 

data is the unencrypted data\.


## [win32crypt](win32crypt.md#win32crypt)\.CryptVerifyDetachedMessageSignature

[PyCERT\_CONTEXT](PyCERT.md#pycertcontext) = CryptVerifyDetachedMessageSignature\(SignerIndex, DetachedSignBlob

, ToBeSigned

, VerifyPara

\)
Verifies a signature that is encoded separately from the data

#### Parameters

  - SignerIndex : int

    Index of the signer to verify

  - DetachedSignBlob : buffer

    Buffer containing an encoded signature

  - ToBeSigned : \(buffer,\.\.\.\)

    Sequence of buffers containing message data\.

  - VerifyPara=None : [PyCRYPT\_VERIFY\_MESSAGE\_PARA](PyCRYPT.md#pycryptverify_message_para)

    Signature verification parameters, use None for defaults

#### Return Value
Returns the signing certificate


## [win32crypt](win32crypt.md#win32crypt)\.CryptVerifyMessageSignature

\([PyCERT\_CONTEXT](PyCERT.md#pycertcontext), str\) = CryptVerifyMessageSignature\(SignedBlob, SignerIndex

, VerifyPara

, ReturnData

\)
Verifies the signature of an encoded message

#### Parameters

  - SignedBlob : str

    Buffer containing a signed message

  - SignerIndex=0 : int

    Index of the signer to verify, zero-based

  - VerifyPara=None : [PyCRYPT\_VERIFY\_MESSAGE\_PARA](PyCRYPT.md#pycryptverify_message_para)

    Signature verification parameters, use None for defaults

  - ReturnData=False : boolean

    Indicates if decoded data should be returned\.

#### Return Value
Returns the signing certificate and the decoded data\.  If ReturnData parm is False, None is returned for data\.


## [win32crypt](win32crypt.md#win32crypt)\.PFXImportCertStore

[PyCERTSTORE](PyCERTSTORE.md) = PFXImportCertStore\(PFX, Password

, Flags

\)
Creates a certificate store from PKCS\#12 data \(\*\.PFX files\)

#### Parameters

  - PFX : bytes

    Buffer containing PKCS\#12-formatted certificate\(s\)

  - Password : str

    Password used to encrypt the data, may be None

  - Flags : int

    Allowed flags are CRYPT\_EXPORTABLE,CRYPT\_USER\_PROTECTED,CRYPT\_MACHINE\_KEYSET, and CRYPT\_USER\_KEYSET

#### Comments

MSDN docs specify that \*one\* of the Flags can be used, but in practice a combination is allowed

Depending on the encrypting application, a blank password \(""\) may be treated differently that a NULL 

password \(None\), so if you have a PFX with no password try both\.

#### Win32 API References

  - Search for PFXImportCertStore at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PFXImportCertStore.md), [google](http://www.google.com/search?q=PFXImportCertStore.md) or [google groups](http://groups.google.com/groups?q=PFXImportCertStore.md)\.


## [win32crypt](win32crypt.md#win32crypt)\.PFXIsPFXBlob

boolean = PFXIsPFXBlob\(PFX\)
Checks if data buffer contains a PFX blob

#### Parameters

  - PFX : bytes

    Buffer containing data to be checked

#### Win32 API References

  - Search for PFXIsPFXBlob at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PFXIsPFXBlob.md), [google](http://www.google.com/search?q=PFXIsPFXBlob.md) or [google groups](http://groups.google.com/groups?q=PFXIsPFXBlob.md)\.


## [win32crypt](win32crypt.md#win32crypt)\.PFXVerifyPassword

boolean = PFXVerifyPassword\(PFX, Password

, Flags

\)
Checks if a PFX blob can be decrypted with given password

#### Parameters

  - PFX : bytes

    Buffer containing PKCS\#12-formatted certificate\(s\)

  - Password : str

    Password used to encrypt the data, may be None

  - Flags : int

    Allowed flags are CRYPT\_EXPORTABLE,CRYPT\_USER\_PROTECTED,CRYPT\_MACHINE\_KEYSET, and CRYPT\_USER\_KEYSET

#### Win32 API References

  - Search for PFXVerifyPassword at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PFXVerifyPassword.md), [google](http://www.google.com/search?q=PFXVerifyPassword.md) or [google groups](http://groups.google.com/groups?q=PFXVerifyPassword.md)\.