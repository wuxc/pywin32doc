# win32crypt

## Module win32crypt

An interface to the win32 Cryptography API

#### Methods


  - [CryptProtectData](win32crypt.md#win32cryptcryptprotectdata)

    Encrypts data using a session key derived from current user's logon credentials&nbsp;

  - [CryptUnprotectData](win32crypt.md#win32cryptcryptunprotectdata)

    Decrypts data that was encrypted using[win32crypt::CryptProtectData](win32crypt.md#win32cryptcryptprotectdata)&nbsp;

  - [CryptEnumProviders](win32crypt.md#win32cryptcryptenumproviders)

    Lists available cryptographic providers&nbsp;

  - [CryptEnumProviderTypes](win32crypt.md#win32cryptcryptenumprovidertypes)

    Lists available local cryptographic provider types&nbsp;

  - [CryptGetDefaultProvider](win32crypt.md#win32cryptcryptgetdefaultprovider)

    Returns default provider for local machine or current user&nbsp;

  - [CryptSetProviderEx](win32crypt.md#win32cryptcryptsetproviderex)

    Sets default provider (for machine or user) for specified type&nbsp;

  - [CryptAcquireContext](win32crypt.md#win32cryptcryptacquirecontext)

    Retrieve handle to a cryptographic service provider&nbsp;

  - [CryptFindLocalizedName](win32crypt.md#win32cryptcryptfindlocalizedname)

    Return localized name for predefined system stores (Root, My, .Default, .LocalMachine)&nbsp;

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

    Converts an integer ALG_ID to it's szOID_ string representation&nbsp;

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

    Converts an encoded CERT_NAME_INFO into a formatted string&nbsp;

  - [CryptFormatObject](win32crypt.md#win32cryptcryptformatobject)

    Formats an encoded buffer into a readable string&nbsp;

  - [PFXImportCertStore](win32crypt.md#win32cryptpfximportcertstore)

    Creates a certificate store from PKCS#12 data (*.PFX files)&nbsp;

  - [PFXVerifyPassword](win32crypt.md#win32cryptpfxverifypassword)

    Checks if a PFX blob can be decrypted with given password&nbsp;

  - [PFXIsPFXBlob](win32crypt.md#win32cryptpfxispfxblob)

    Checks if data buffer contains a PFX blob&nbsp;

  - [CryptBinaryToString](win32crypt.md#win32cryptcryptbinarytostring)

    Formats a binary buffer into the specified type of string&nbsp;

  - [CryptStringToBinary](win32crypt.md#win32cryptcryptstringtobinary)

    Converts a formatted string back into raw bytes&nbsp;

## [win32crypt](#win32crypt).CertAddSerializedElementToStore

[PyCERT_CONTEXT](PyCERT.md#pycertcontext)= __CertAddSerializedElementToStore( *CertStore*  *, Element*  *, AddDisposition*  *, ContextTypeFlags*  *, Flags* __ )
Imports a serialized Certificate context, CRL, or CTL

#### Parameters


  -  *CertStore* :[PyCERTSTORE](#pycertstore)

    Certificate Store to which the context will be added, can be None

  -  *Element* : buffer

    Serialized data

  -  *AddDisposition* : int

    one of CERT_STORE_ADD_* values

  -  *ContextTypeFlags=CERT_STORE_CERTIFICATE_CONTEXT_FLAG* : int

    One of CERT_STORE_*_CONTEXT_FLAG constants

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Currently only Certificate contexts are supported

## [win32crypt](#win32crypt).CertAlgIdToOID

string = __CertAlgIdToOID( *AlgId* __ )
Converts an integer ALG_ID to it's szOID_ string representation

#### Parameters


  -  *AlgId* : int

    An algorithm identifier

#### Comments
If there is no corresponding OID, None is returned

## [win32crypt](#win32crypt).CertEnumPhysicalStore

[[PyUnicode](#pyunicode),...] = __CertEnumPhysicalStore( *pvSystemStore*  *, dwFlags* __ )
Lists physical stores on computer

#### Parameters


  -  *pvSystemStore* :[PyUnicode](#pyunicode)

    Name of system store to enumerate physical locations for

  -  *dwFlags* : int

    CERT_SYSTEM_STORE_* constant, CERT_SYSTEM_STORE_RELOCATE_FLAG  not supported yet

## [win32crypt](#win32crypt).CertEnumSystemStore

[[PyUnicode](#pyunicode),...] = __CertEnumSystemStore( *dwFlags*  *, pvSystemStoreLocationPara* __ )
Lists system stores

#### Parameters


  -  *dwFlags* : int

    CERT_SYSTEM_STORE_* location, can be combined with CERT_SYSTEM_STORE_RELOCATE_FLAG

  -  *pvSystemStoreLocationPara=None* : __PyCERT_SYSTEM_STORE_RELOCATE_PARA__ 

    Optional - If flags contains CERT_SYSTEM_STORE_RELOCATE_FLAG must be a sequence (PyHkey, unicode) representing a CERT_SYSTEM_STORE_RELOCATE_PARA, otherwise should be a unicode store name

## [win32crypt](#win32crypt).CertEnumSystemStoreLocation

[[PyUnicode](#pyunicode),...] = __CertEnumSystemStoreLocation( *Flags* __ )
Lists system store locations

#### Parameters


  -  *Flags=0* : int

    Reserved, must be 0 if passed in

## [win32crypt](#win32crypt).CertNameToStr

str = __CertNameToStr( *Name*  *, StrType*  *, CertEncodingType* __ )
Converts an encoded CERT_NAME_INFO into a formatted string

#### Parameters


  -  *Name* : str

    String containing an encoded CERT_NAME_INFO, as used with certificate Issuer and Subject

  -  *StrType=CERT_SIMPLE_NAME_STR* : int

    Type of string to format, one of CERT_SIMPLE_NAME_STR,CERT_OID_NAME_STR,CERT_X500_NAME_STR

  -  *CertEncodingType=X509_ASN_ENCODING* : int

    Input encoding

#### Comments
Usually this encoded data is contained in a CERT_NAME_BLOB

## [win32crypt](#win32crypt).CertOIDToAlgId

int = __CertOIDToAlgId( *ObjId* __ )
Converts a string object identfier to a numeric algorith identifier

#### Parameters


  -  *ObjId* : string

    String szOID_* identifier

#### Comments
If no matching ALG_ID is found, 0 is returned

## [win32crypt](#win32crypt).CertOpenStore

[PyCERTSTORE](#pycertstore)= __CertOpenStore( *StoreProvider*  *, MsgAndCertEncodingType*  *, CryptProv*  *, Flags*  *, Para* __ )
Opens a certificate store

#### Parameters


  -  *StoreProvider* : int

    CERT_STORE_PROV_*, currently does not accept string provider names

  -  *MsgAndCertEncodingType* : int

    Only used with CERT_STORE_PROV_MSG, CERT_STORE_PROV_PKCS7, and CERT_STORE_PROV_FILENAME. 

Usually should be X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

  -  *CryptProv* :[PyCRYPTPROV](#pycryptprov)

    Handle to a CSP, can be None to use default provider

  -  *Flags* : int

    Combination of CERT_STORE_*_FLAG flags

  -  *Para=None* : object

     __PyCERT_SYSTEM_STORE_RELOCATE_PARA__ , or data specific to provider

## [win32crypt](#win32crypt).CertOpenSystemStore

[PyCERTSTORE](#pycertstore)= __CertOpenSystemStore( *SubsystemProtocol*  *, Prov* __ )
Opens most commonly used Certificate Stores

#### Parameters


  -  *SubsystemProtocol* :[PyUnicode](#pyunicode)

    Name of store to open, will be created if it doesn't already exist

  -  *Prov=None* :[PyCRYPTPROV](#pycryptprov)

    Handle to CSP, use None for default provider

## [win32crypt](#win32crypt).CertRegisterSystemStore

 __CertRegisterSystemStore( *SystemStore*  *, Flags* __ )
Registers a certificate store

#### Parameters


  -  *SystemStore* :[PyUnicode](#pyunicode)

    string/unicode name of store to be registered, or a sequence of (PyHkey, unicode) representing a CERT_SYSTEM_STORE_RELOCATE_PARA struct

  -  *Flags* : int

    One of the CERT_SYSTEM_STORE_* location constants, can also be combined with CERT_SYSTEM_STORE_RELOCATE_FLAG and CERT_STORE_CREATE_NEW_FLAG

## [win32crypt](#win32crypt).CertUnregisterSystemStore

 __CertUnregisterSystemStore( *SystemStore*  *, Flags* __ )
Unregisters a certificate store

#### Parameters


  -  *SystemStore* :[PyUnicode](#pyunicode)

    Name of System store to be unregistered

  -  *Flags* : int

    CERT_SYSTEM_STORE_RELOCATE_FLAG, CERT_STORE_DELETE_FLAG (CERT_SYSTEM_STORE_RELOCATE_FLAG  not supported yet)

## [win32crypt](#win32crypt).CryptAcquireContext

[PyCRYPTPROV](#pycryptprov)= __CryptAcquireContext( *Container*  *, Provider*  *, ProvType*  *, Flags* __ )
Retrieve handle to a cryptographic service provider

#### Parameters


  -  *Container* :[PyUnicode](#pyunicode)

    Name of key container, can be none to use a Provider's default key container (usually username)

  -  *Provider* :[PyUnicode](#pyunicode)

    Name of cryptographic provider. (MS_*_PROV) Use None for user's default provider.

  -  *ProvType* : int

    One of the PROV_* constants

  -  *Flags* : int

    Combination of CRYPT_VERIFYCONTEXT,CRYPT_NEWKEYSET,CRYPT_MACHINE_KEYSET,CRYPT_DELETEKEYSET,CRYPT_SILENT

#### Return Value
Returns None if CRYPT_DELETEKEYSET is specified, otherwise returns a handle to the provider

## [win32crypt](#win32crypt).CryptBinaryToString

str = __CryptBinaryToString( *Binary*  *, Flags* __ )
Formats a binary buffer into the specified type of string

#### Parameters


  -  *Binary* : bytes

    Buffer containing raw data to be formatted

  -  *Flags* : int

    Type of output desired, win32cryptcon.CRYPT_STRING_* value

#### Win32 API References


  - Search for *CryptBinaryToString* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=cryptbinarytostring),[google](#http://www.google.com/search?q=cryptbinarytostring)or[google groups](#http://groups.google.com/groups?q=cryptbinarytostring).

## [win32crypt](#win32crypt).CryptDecodeMessage

dict = __CryptDecodeMessage( *EncodedBlob*  *, DecryptPara*  *, VerifyPara*  *, MsgTypeFlags*  *, SignerIndex*  *, PrevInnerContentType*  *, ReturnData* __ )
Decodes and decrypts a message, and verifies its signatures

#### Parameters


  -  *EncodedBlob* : buffer

    Data to be decoded

  -  *DecryptPara* : dict

    [PyCRYPT_DECRYPT_MESSAGE_PARA](PyCRYPT.md#pycryptdecrypt_message_para)containing decryption parms

  -  *VerifyPara=None* : dict

    [PyCRYPT_VERIFY_MESSAGE_PARA](PyCRYPT.md#pycryptverify_message_para)containing signature verification parms

  -  *MsgTypeFlags=CMSG_ALL_FLAGS* : int

    Combination of CMSG_DATA_FLAG, CMSG_SIGNED_FLAG, CMSG_ENVELOPED_FLAG, CMSG_SIGNED_AND_ENVELOPED_FLAG, or CMSG_HASHED_FLAG

  -  *SignerIndex=0* : int

    Index of the signer to verify,  ignored if message is not signed.

  -  *PrevInnerContentType=0* : int

    Content type returned from previous call, used during subsequent pass on a nested message

  -  *ReturnData=True* : boolean

    Indicates if decoded data should be returned.

#### Comments
Only one level of encoding is interpreted.  Some types of messages will need multiple calls to completely decode. 

For example, to decode a message created by[win32crypt::CryptSignAndEncryptMessage](win32crypt.md#win32cryptcryptsignandencryptmessage), one pass with CMSG_ENVELOPED_FLAG 

and a second pass using CMSG_SIGNED_FLAG are required to recover the original message text.

#### Return Value
Output params are returned as a dict containing:
{MsgType:int},&#09&#09&#09&#09&#09&nbsp&nbsp##Type of message decoded, one of CMSG_DATA,CMSG_SIGNED,CMSG_ENVELOPED,CMSG_SIGNED_AND_ENVELOPED,CMSG_HASHED
InnerContentType:int,&#09&#09&#09&nbsp&nbsp##Type of decoded content returned, uses same set of values as MsgType.  CMSG_DATA indicates unencoded data.
Decoded:str,&#09&#09&#09&#09&#09&nbsp&nbsp##The decoded data, will be None if ReturnData is False.
XchgCert:[PyCERT_CONTEXT](PyCERT.md#pycertcontext),&#09&nbsp&nbsp##Certificate used to decode message
SignerCert:[PyCERT_CONTEXT](PyCERT.md#pycertcontext)}&#09&nbsp&nbsp##Certificate used to sign message

## [win32crypt](#win32crypt).CryptDecodeObjectEx

object = __CryptDecodeObjectEx( *StructType*  *, Encoded*  *, Flags*  *, CertEncodingType*  *, DecodePara* __ )
Decodes ASN encoded data

#### Parameters


  -  *StructType* : str/int

    An OID identifying the type of data to be decoded, can be either str or int

  -  *Encoded* : str

    String or buffer containing ASN encoded data

  -  *Flags=0* : int

    Encoding options, can be combination CRYPT_UNICODE_* constants.  CRYPT_ENCODE_ALLOC_FLAG is added to flags..

  -  *CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING* : int

    Encoding types

  -  *DecodePara=None* : object

    Not supported, use only None

 __OID__  __Object returned__ szOID_ENHANCED_KEY_USAGESequence of OIDsX509_ENHANCED_KEY_USAGESequence of OIDsszOID_KEY_USAGE[PyCRYPT_BIT_BLOB](PyCRYPT.md#pycryptbit_blob)X509_KEY_USAGE[PyCRYPT_BIT_BLOB](PyCRYPT.md#pycryptbit_blob)X509_BITS[PyCRYPT_BIT_BLOB](PyCRYPT.md#pycryptbit_blob)szOID_SUBJECT_ALT_NAME[PyCERT_ALT_NAME_INFO](PyCERT.md#pycertalt_name_info)szOID_SUBJECT_ALT_NAME2[PyCERT_ALT_NAME_INFO](PyCERT.md#pycertalt_name_info)szOID_ISSUER_ALT_NAME[PyCERT_ALT_NAME_INFO](PyCERT.md#pycertalt_name_info)szOID_ISSUER_ALT_NAME2[PyCERT_ALT_NAME_INFO](PyCERT.md#pycertalt_name_info)szOID_NEXT_UPDATE_LOCATION[PyCERT_ALT_NAME_INFO](PyCERT.md#pycertalt_name_info)X509_ALTERNATE_NAME[PyCERT_ALT_NAME_INFO](PyCERT.md#pycertalt_name_info)X509_NAME_VALUE[PyCERT_NAME_VALUE](PyCERT.md#pycertname_value)X509_UNICODE_ANY_STRING[PyCERT_NAME_VALUE](PyCERT.md#pycertname_value)X509_UNICODE_NAME_VALUE[PyCERT_NAME_VALUE](PyCERT.md#pycertname_value)X509_NAME[PyCERT_NAME_INFO](PyCERT.md#pycertname_info)X509_UNICODE_NAME[PyCERT_NAME_INFO](PyCERT.md#pycertname_info)szOID_KEY_ATTRIBUTES[PyCERT_KEY_ATTRIBUTES_INFO](PyCERT.md#pycertkey_attributes_info)X509_KEY_ATTRIBUTES[PyCERT_KEY_ATTRIBUTES_INFO](PyCERT.md#pycertkey_attributes_info)szOID_BASIC_CONSTRAINTS[PyCERT_BASIC_CONSTRAINTS_INFO](PyCERT.md#pycertbasic_constraints_info)X509_BASIC_CONSTRAINTS[PyCERT_BASIC_CONSTRAINTS_INFO](PyCERT.md#pycertbasic_constraints_info)szOID_BASIC_CONSTRAINTS2[PyCERT_BASIC_CONSTRAINTS2_INFO](PyCERT.md#pycertbasic_constraints2_info)X509_BASIC_CONSTRAINTS2[PyCERT_BASIC_CONSTRAINTS2_INFO](PyCERT.md#pycertbasic_constraints2_info)szOID_CERT_POLICIESSequence of[PyCERT_POLICY_INFO](PyCERT.md#pycertpolicy_info)objectsszOID_APPLICATION_CERT_POLICIESSequence of[PyCERT_POLICY_INFO](PyCERT.md#pycertpolicy_info)objectsX509_CERT_POLICIESSequence of[PyCERT_POLICY_INFO](PyCERT.md#pycertpolicy_info)objectsszOID_SUBJECT_KEY_IDENTIFIERBinary string containing the key identifierszOID_AUTHORITY_KEY_IDENTIFIER[PyCERT_AUTHORITY_KEY_ID_INFO](PyCERT.md#pycertauthority_key_id_info)X509_AUTHORITY_KEY_ID[PyCERT_AUTHORITY_KEY_ID_INFO](PyCERT.md#pycertauthority_key_id_info)
#### Return Value
Type of object returned is dependent on the StructType to be decoded

## [win32crypt](#win32crypt).CryptDecryptAndVerifyMessageSignature

dict = __CryptDecryptAndVerifyMessageSignature( *EncryptedBlob*  *, DecryptPara*  *, VerifyPara*  *, SignerIndex* __ )
Decrypts and decodes a signed message, and verifies its signatures

#### Parameters


  -  *EncryptedBlob* : buffer

    Encoded message to be decrypted.

  -  *DecryptPara* :[PyCRYPT_DECRYPT_MESSAGE_PARA](PyCRYPT.md#pycryptdecrypt_message_para)

    Decryption parms

  -  *VerifyPara=None* :[PyCRYPT_VERIFY_MESSAGE_PARA](PyCRYPT.md#pycryptverify_message_para)

    Signature verification parms

  -  *SignerIndex=0* : int

    Index of the signer to verify, zero-based.

#### Comments
Usage is similar to CryptDecodeMessage, except that it undoes all levels of encoding and 

returns the bare message.   This function is the counterpart of CryptSignAndEncryptMessage.

#### Return Value
Output params are returned as a dict containing:
Decrypted:str,&#09&#09&#09&#09&#09&nbsp&nbsp##The decrypted message contents
XchgCert:[PyCERT_CONTEXT](PyCERT.md#pycertcontext),&#09&nbsp&nbsp##Certificate whose private key was used to decrypt message
SignerCert:[PyCERT_CONTEXT](PyCERT.md#pycertcontext)&#09&nbsp&nbsp##Certificate used to sign message

## [win32crypt](#win32crypt).CryptDecryptMessage

str,[PyCERT_CONTEXT](PyCERT.md#pycertcontext)= __CryptDecryptMessage( *DecryptPara*  *, EncryptedBlob* __ )
Decrypts an encrypted and encoded message

#### Parameters


  -  *DecryptPara* :[PyCRYPT_DECRYPT_MESSAGE_PARA](PyCRYPT.md#pycryptdecrypt_message_para)

    Dictionary containing decryption parameters

  -  *EncryptedBlob* : buffer

    Buffer containing an encrypted message

#### Return Value
Returns the decrypted message and a handle to the certificate used to decrypt it

## [win32crypt](#win32crypt).CryptEncodeObjectEx

str = __CryptEncodeObjectEx( *StructType*  *, StructInfo*  *, Flags*  *, CertEncodingType*  *, EncodePara* __ )
Serializes and ASN encodes cryptographic structures

#### Parameters


  -  *StructType* : str/int

    OID identifying type of data to be encoded, either szOID_* string or a numeric id

  -  *StructInfo* : dict

    Information to be encoded.  Contents of dict are dependent on StructType

  -  *Flags=0* : int

    Encoding options, combination of CRYPT_UNICODE_* constants.  CRYPT_ENCODE_ALLOC_FLAG is added to flags..

  -  *CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING* : int

    Encoding types

  -  *EncodePara=None* : object

    Not supported, use only None


## [win32crypt](#win32crypt).CryptEncryptMessage

str = __CryptEncryptMessage( *EncryptPara*  *, RecipientCert*  *, ToBeEncrypted* __ )
Encrypts and encodes a message

#### Parameters


  -  *EncryptPara* :[PyCRYPT_ENCRYPT_MESSAGE_PARA](PyCRYPT.md#pycryptencrypt_message_para)

    Encryption parameters

  -  *RecipientCert* : ([PyCERT_CONTEXT](PyCERT.md#pycertcontext),...)

    Sequence of handles to recipients' certificates

  -  *ToBeEncrypted* : buffer

    Data to be encrypted

## [win32crypt](#win32crypt).CryptEnumKeyIdentifierProperties

list = __CryptEnumKeyIdentifierProperties( *KeyIdentifier*  *, PropId*  *, Flags*  *, ComputerName* __ )
Enumerates private keys for certificates and their properties

#### Parameters


  -  *KeyIdentifier=None* : string

    Id of a certificate key, can be None for all keys

  -  *PropId=0* : int

    CERT_*_PROP_ID constant. Limits returned values to specified propery, Use 0 for all

  -  *Flags=0* : int

    Can be CRYPT_KEYID_MACHINE_FLAG to list keys for local machine, or remote machine if ComputerName is given

  -  *ComputerName=None* :[PyUnicode](#pyunicode)

    Name of remote computer, use None for local machine

## [win32crypt](#win32crypt).CryptEnumOIDInfo

list = __CryptEnumOIDInfo( *GroupId* __ )
Lists registered Object Identifiers that belong to specified group

#### Parameters


  -  *GroupId=0* : int

    The type of OIDs to enmerate, one of the CRYPT_*_OID_GROUP_ID constants or 0 to list all

## [win32crypt](#win32crypt).CryptEnumProviderTypes

[([PyUnicode](#pyunicode),int),...] = __CryptEnumProviderTypes(__ )
Lists available local cryptographic provider types

#### Comments
Windows XP sp3 has a bug that causes this function to always fail with ERROR_MORE_DATA (234) 

See KB959160 for a hotfix

#### Return Value
Returns a sequence of tuples containing name and identifier of provider types

## [win32crypt](#win32crypt).CryptEnumProviders

[([PyUnicode](#pyunicode),int),...] = __CryptEnumProviders(__ )
List cryptography providers

#### Return Value
Returns a sequence of tuples containing provider name and type

## [win32crypt](#win32crypt).CryptFindLocalizedName

[PyUnicode](#pyunicode)= __CryptFindLocalizedName( *CryptName* __ )
Returns localized name for predefined system stores (Root, My, .Default, .LocalMachine)

#### Parameters


  -  *CryptName* :[PyUnicode](#pyunicode)

    Name of a system store

## [win32crypt](#win32crypt).CryptFindOIDInfo

dict = __CryptFindOIDInfo( *KeyType*  *, Key*  *, GroupId* __ )
Returns information about an algorithm identifier or object identifier

#### Parameters


  -  *KeyType* : int

    One of CRYPT_OID_INFO_OID_KEY,CRYPT_OID_INFO_NAME_KEY,CRYPT_OID_INFO_ALGID_KEY,CRYPT_OID_INFO_SIGN_KEY

  -  *Key* : object

    Type is dependent on KeyType

  -  *GroupId=0* : int

    CRYPT_*_GROUP_ID constant, or 0

#### Return Value
Returns a dictionary of CRYPT_OID_INFO data


## [win32crypt](#win32crypt).CryptFormatObject

str = __CryptFormatObject( *StructType*  *, Encoded*  *, FormatStrType*  *, CertEncodingType*  *, FormatType*  *, FormatStruct* __ )
Formats an encoded buffer into a readable string

#### Parameters


  -  *StructType* : str/int

    OID identifying the type of encoded data, one of the szOID_* strings or an integer OID

  -  *Encoded* : str

    String containing encoded data to be formatted

  -  *FormatStrType=0* : int

    String formatting options, combination of CRYPT_FORMAT_STR_MULTI_LINE, CRYPT_FORMAT_STR_NO_HEX

  -  *CertEncodingType=X509_ASN_ENCODING* : int

    Input encoding

  -  *FormatType=0* : int

    Reserved, use only 0

  -  *FormatStruct=None* : None

    Reserved, use only None

#### Comments
Will handle all of the common certificate extension types

#### Win32 API References


  - Search for *CryptFormatObject* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=cryptformatobject),[google](#http://www.google.com/search?q=cryptformatobject)or[google groups](#http://groups.google.com/groups?q=cryptformatobject).

## [win32crypt](#win32crypt).CryptGetDefaultProvider

[PyUnicode](#pyunicode)= __CryptGetDefaultProvider( *ProvType*  *, Flags* __ )
Returns default provider for local machine or current user

#### Parameters


  -  *ProvType* : int

    Type of provider (PROV_* constant)

  -  *Flags* : int

    CRYPT_MACHINE_DEFAULT or CRYPT_USER_DEFAULT

## [win32crypt](#win32crypt).CryptGetKeyIdentifierProperty

object = __CryptGetKeyIdentifierProperty( *KeyIdentifier*  *, PropId*  *, Flags*  *, ComputerName* __ )
Retrieves a property from a certificate by its key indentifier

#### Parameters


  -  *KeyIdentifier* : string

    Hash that identifies a certificate key

  -  *PropId=CERT_KEY_PROV_INFO_PROP_ID* : int

    Property identifier, one of the CERT_*_PROP_ID values

  -  *Flags=0* : int

    Use CRYPT_KEYID_MACHINE_FLAG for machine keyset. (CRYPT_KEYID_ALLOC_FLAG is always added to Flags)

  -  *ComputerName=None* :[PyUnicode](#pyunicode)

    Name of remote computer, use None for local machine

#### Comments
CERT_KEY_PROV_INFO_PROP_ID is only property currently supported

## [win32crypt](#win32crypt).CryptGetMessageCertificates

[PyCERTSTORE](#pycertstore)= __CryptGetMessageCertificates( *SignedBlob*  *, MsgAndCertEncodingType*  *, CryptProv*  *, Flags* __ )
Extracts certificates encoded in a message

#### Parameters


  -  *SignedBlob* : buffer

    Buffer containing a signed message

  -  *MsgAndCertEncodingType=X509_ASN_ENCODING|PKCS_7_ASN_ENCODING* : int

    Message and certificate encoding types

  -  *CryptProv=None* :[PyCRYPTPROV](#pycryptprov)

    Handle to a CSP, use None for default

  -  *Flags=0* : int

    Same flags used with[win32crypt::CertOpenStore](win32crypt.md#win32cryptcertopenstore)

## [win32crypt](#win32crypt).CryptGetMessageSignerCount

int = __CryptGetMessageSignerCount( *SignedBlob*  *, MsgEncodingType* __ )
Finds the number of signers of an encoded message

#### Parameters


  -  *SignedBlob* : buffer

    Buffer containing a signed message

  -  *MsgEncodingType=X509_ASN_ENCODING|PKCS_7_ASN_ENCODING* : int

    Message encoding type

## [win32crypt](#win32crypt).CryptProtectData

bytes = __CryptProtectData( *DataIn*  *, DataDescr*  *, OptionalEntropy*  *, Reserved*  *, PromptStruct*  *, Flags* __ )
Encrypts data using a session key derived from current user's logon credentials

#### Parameters


  -  *DataIn* : bytes

    Data to be encrypted.

  -  *DataDescr=None* :[PyUnicode](#pyunicode)

    Description to add to the data

  -  *OptionalEntropy=None* : bytes

    Extra entropy (eg password) for encryption process, can be None

  -  *Reserved=None* : None

    Must be None

  -  *PromptStruct=None* :[PyCRYPTPROTECT_PROMPTSTRUCT](PyCRYPTPROTECT.md#pycryptprotectpromptstruct)

    Contains options for UI display during encryption and decryption, can be None

  -  *Flags=0* : int

    Combination of CRYPTPROTECT_* flags

## [win32crypt](#win32crypt).CryptQueryObject

dict = __CryptQueryObject( *ObjectType*  *, Object*  *, ExpectedContentTypeFlags*  *, ExpectedFormatTypeFlags*  *, Flags* __ )
Determines the cryptographic type of input data

#### Parameters


  -  *ObjectType* : int

    Type of input, CERT_QUERY_OBJECT_BLOB or CERT_QUERY_OBJECT_FILE

  -  *Object* : str

    Raw data or a filename containing the data to be queried depending on ObjectType

  -  *ExpectedContentTypeFlags=CERT_QUERY_CONTENT_FLAG_ALL* : int

    One of the CERT_QUERY_CONTENT_FLAG_* constants

  -  *ExpectedFormatTypeFlags=CERT_QUERY_FORMAT_FLAG_ALL* : int

    One of the CERT_QUERY_FORMAT_FLAG_* constants

  -  *Flags=0* : int

    Reserved, use only 0

#### Return Value
Returns a dictionary containing
{MsgAndCertEncodingType:int,&#09## encoding type, usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING
ContentType:int,&#09&#09&#09&#09## One of the CERT_QUERY_CONTENT_* constants
FormatType:int,&#09&#09&#09&#09&#09## One of the CERT_QUERY_FORMAT_* constants
CertStore:[PyCERTSTORE](#pycertstore),&#09&#09## Handle to certificate store containing all certficates in the object, may be None
Msg:[PyCRYPTMSG](#pycryptmsg),&#09&#09&#09&#09## If input doesn't contains a PKCS7 message, will be None
Context:[PyCERT_CONTEXT](PyCERT.md#pycertcontext)}&#09&#09## A certificate, CRL, or CTL context depending on ContentType, may be None

## [win32crypt](#win32crypt).CryptSetProviderEx

 __CryptSetProviderEx( *ProvName*  *, ProvType*  *, Flags* __ )
Sets default provider (for machine or user) for specified type

#### Parameters


  -  *ProvName* :[PyUnicode](#pyunicode)

    Name of new default provider (MS_*_PROV value)

  -  *ProvType* : int

    One of the PROV_* provider types

  -  *Flags* : int

    CRYPT_MACHINE_DEFAULT or CRYPT_USER_DEFAULT.  Combine with CRYPT_DELETE_DEFAULT to remove default.

## [win32crypt](#win32crypt).CryptSignAndEncryptMessage

str = __CryptSignAndEncryptMessage( *SignPara*  *, EncryptPara*  *, RecipientCert*  *, ToBeSignedAndEncrypted* __ )
Encrypts, encodes and signs a message using a certificate

#### Parameters


  -  *SignPara* :[PyCRYPT_SIGN_MESSAGE_PARA](PyCRYPT.md#pycryptsign_message_para)

    Message signing parameters

  -  *EncryptPara* :[PyCRYPT_ENCRYPT_MESSAGE_PARA](PyCRYPT.md#pycryptencrypt_message_para)

    Encryption parameters

  -  *RecipientCert* : ([PyCERT_CONTEXT](PyCERT.md#pycertcontext),...)

    Sequence of certificates of intended recipients

  -  *ToBeSignedAndEncrypted* : str

    Buffer containing data to be encoded in the message

## [win32crypt](#win32crypt).CryptSignMessage

str = __CryptSignMessage( *SignPara*  *, ToBeSigned*  *, DetachedSignature* __ )
Signs and encodes a message

#### Parameters


  -  *SignPara* :[PyCRYPT_SIGN_MESSAGE_PARA](PyCRYPT.md#pycryptsign_message_para)

    Message signing parameters

  -  *ToBeSigned* : (str,...)

    Sequence of strings containing message data.  Can only contain 1 string if DetachedSignature parm is False.

  -  *DetachedSignature=False* : boolean

    If True, only the signature itself is encoded in output msg.

## [win32crypt](#win32crypt).CryptStringToBinary

bytes, int, int = __CryptStringToBinary( *String*  *, Flags* __ )
Converts a formatted string back into raw bytes

#### Parameters


  -  *String* : str

    Formatted string to be converted to raw binary data

  -  *Flags* : int

    Input format (win32cryptcon.CRYPT_STRING_*)

#### Win32 API References


  - Search for *CryptStringToBinary* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=cryptstringtobinary),[google](#http://www.google.com/search?q=cryptstringtobinary)or[google groups](#http://groups.google.com/groups?q=cryptstringtobinary).

#### Return Value
Returns the decoded binary data, number of header characters skipped, and CRYPT_STRING_* value 

denoting the type of data found (used if input Flags is one of *_ANY values)

## [win32crypt](#win32crypt).CryptUnprotectData

(str, bytes) = __CryptUnprotectData( *DataIn*  *, OptionalEntropy*  *, Reserved*  *, PromptStruct*  *, Flags* __ )
Decrypts data that was encrypted using[win32crypt::CryptProtectData](win32crypt.md#win32cryptcryptprotectdata).

#### Parameters


  -  *DataIn* : bytes

    Data to be decrypted.

  -  *OptionalEntropy=None* : bytes

    Extra entropy passed to CryptProtectData

  -  *Reserved=None* : None

    Must be None

  -  *PromptStruct=None* :[PyCRYPTPROTECT_PROMPTSTRUCT](PyCRYPTPROTECT.md#pycryptprotectpromptstruct)

    Contains options for UI display during encryption and decryption, can be None

  -  *Flags=0* : int

    Combination of CRYPTPROTECT_* flags

#### Return Value
The result is a tuple of (description, data) where description 

is the description that was passed to[win32crypt::CryptProtectData](win32crypt.md#win32cryptcryptprotectdata), and 

data is the unencrypted data.

## [win32crypt](#win32crypt).CryptVerifyDetachedMessageSignature

[PyCERT_CONTEXT](PyCERT.md#pycertcontext)= __CryptVerifyDetachedMessageSignature( *SignerIndex*  *, DetachedSignBlob*  *, ToBeSigned*  *, VerifyPara* __ )
Verifies a signature that is encoded separately from the data

#### Parameters


  -  *SignerIndex* : int

    Index of the signer to verify

  -  *DetachedSignBlob* : buffer

    Buffer containing an encoded signature

  -  *ToBeSigned* : (buffer,...)

    Sequence of buffers containing message data.

  -  *VerifyPara=None* :[PyCRYPT_VERIFY_MESSAGE_PARA](PyCRYPT.md#pycryptverify_message_para)

    Signature verification parameters, use None for defaults

#### Return Value
Returns the signing certificate

## [win32crypt](#win32crypt).CryptVerifyMessageSignature

([PyCERT_CONTEXT](PyCERT.md#pycertcontext), str) = __CryptVerifyMessageSignature( *SignedBlob*  *, SignerIndex*  *, VerifyPara*  *, ReturnData* __ )
Verifies the signature of an encoded message

#### Parameters


  -  *SignedBlob* : str

    Buffer containing a signed message

  -  *SignerIndex=0* : int

    Index of the signer to verify, zero-based

  -  *VerifyPara=None* :[PyCRYPT_VERIFY_MESSAGE_PARA](PyCRYPT.md#pycryptverify_message_para)

    Signature verification parameters, use None for defaults

  -  *ReturnData=False* : boolean

    Indicates if decoded data should be returned.

#### Return Value
Returns the signing certificate and the decoded data.  If ReturnData parm is False, None is returned for data.

## [win32crypt](#win32crypt).PFXImportCertStore

[PyCERTSTORE](#pycertstore)= __PFXImportCertStore( *PFX*  *, Password*  *, Flags* __ )
Creates a certificate store from PKCS#12 data (*.PFX files)

#### Parameters


  -  *PFX* : bytes

    Buffer containing PKCS#12-formatted certificate(s)

  -  *Password* : str

    Password used to encrypt the data, may be None

  -  *Flags* : int

    Allowed flags are CRYPT_EXPORTABLE,CRYPT_USER_PROTECTED,CRYPT_MACHINE_KEYSET, and CRYPT_USER_KEYSET

#### Comments
MSDN docs specify that *one* of the Flags can be used, but in practice a combination is allowed
Depending on the encrypting application, a blank password ("") may be treated differently that a NULL 

password (None), so if you have a PFX with no password try both.

#### Win32 API References


  - Search for *PFXImportCertStore* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=pfximportcertstore),[google](#http://www.google.com/search?q=pfximportcertstore)or[google groups](#http://groups.google.com/groups?q=pfximportcertstore).

## [win32crypt](#win32crypt).PFXIsPFXBlob

boolean = __PFXIsPFXBlob( *PFX* __ )
Checks if data buffer contains a PFX blob

#### Parameters


  -  *PFX* : bytes

    Buffer containing data to be checked

#### Win32 API References


  - Search for *PFXIsPFXBlob* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=pfxispfxblob),[google](#http://www.google.com/search?q=pfxispfxblob)or[google groups](#http://groups.google.com/groups?q=pfxispfxblob).

## [win32crypt](#win32crypt).PFXVerifyPassword

boolean = __PFXVerifyPassword( *PFX*  *, Password*  *, Flags* __ )
Checks if a PFX blob can be decrypted with given password

#### Parameters


  -  *PFX* : bytes

    Buffer containing PKCS#12-formatted certificate(s)

  -  *Password* : str

    Password used to encrypt the data, may be None

  -  *Flags* : int

    Allowed flags are CRYPT_EXPORTABLE,CRYPT_USER_PROTECTED,CRYPT_MACHINE_KEYSET, and CRYPT_USER_KEYSET

#### Win32 API References


  - Search for *PFXVerifyPassword* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=pfxverifypassword),[google](#http://www.google.com/search?q=pfxverifypassword)or[google groups](#http://groups.google.com/groups?q=pfxverifypassword).