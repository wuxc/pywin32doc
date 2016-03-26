
## [win32crypt](#README.md#win32crypt).CertAddSerializedElementToStore

[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT)= **CertAddSerializedElementToStore( *CertStore*  *, Element*  *, AddDisposition*  *, ContextTypeFlags*  *, Flags* ** )
Imports a serialized Certificate context, CRL, or CTL

#### Parameters


     *CertStore* :[PyCERTSTORE](#README.md#PyCERTSTORE)

    Certificate Store to which the context will be added, can be None

     *Element* : buffer

    Serialized data

     *AddDisposition* : int

    one of CERT_STORE_ADD_* values

     *ContextTypeFlags=CERT_STORE_CERTIFICATE_CONTEXT_FLAG* : int

    One of CERT_STORE_*_CONTEXT_FLAG constants

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Currently only Certificate contexts are supported

## [win32crypt](#README.md#win32crypt).CertAlgIdToOID

string = **CertAlgIdToOID( *AlgId* ** )
Converts an integer ALG_ID to it's szOID_ string representation

#### Parameters


     *AlgId* : int

    An algorithm identifier

#### Comments
If there is no corresponding OID, None is returned

## [win32crypt](#README.md#win32crypt).CertEnumPhysicalStore

[[PyUnicode](#README.md#PyUnicode),...] = **CertEnumPhysicalStore( *pvSystemStore*  *, dwFlags* ** )
Lists physical stores on computer

#### Parameters


     *pvSystemStore* :[PyUnicode](#README.md#PyUnicode)

    Name of system store to enumerate physical locations for

     *dwFlags* : int

    CERT_SYSTEM_STORE_* constant, CERT_SYSTEM_STORE_RELOCATE_FLAG  not supported yet

## [win32crypt](#README.md#win32crypt).CertEnumSystemStore

[[PyUnicode](#README.md#PyUnicode),...] = **CertEnumSystemStore( *dwFlags*  *, pvSystemStoreLocationPara* ** )
Lists system stores

#### Parameters


     *dwFlags* : int

    CERT_SYSTEM_STORE_* location, can be combined with CERT_SYSTEM_STORE_RELOCATE_FLAG

     *pvSystemStoreLocationPara=None* : **PyCERT_SYSTEM_STORE_RELOCATE_PARA** 

    Optional - If flags contains CERT_SYSTEM_STORE_RELOCATE_FLAG must be a sequence (PyHkey, unicode) representing a CERT_SYSTEM_STORE_RELOCATE_PARA, otherwise should be a unicode store name

## [win32crypt](#README.md#win32crypt).CertEnumSystemStoreLocation

[[PyUnicode](#README.md#PyUnicode),...] = **CertEnumSystemStoreLocation( *Flags* ** )
Lists system store locations

#### Parameters


     *Flags=0* : int

    Reserved, must be 0 if passed in

## [win32crypt](#README.md#win32crypt).CertNameToStr

str = **CertNameToStr( *Name*  *, StrType*  *, CertEncodingType* ** )
Converts an encoded CERT_NAME_INFO into a formatted string

#### Parameters


     *Name* : str

    String containing an encoded CERT_NAME_INFO, as used with certificate Issuer and Subject

     *StrType=CERT_SIMPLE_NAME_STR* : int

    Type of string to format, one of CERT_SIMPLE_NAME_STR,CERT_OID_NAME_STR,CERT_X500_NAME_STR

     *CertEncodingType=X509_ASN_ENCODING* : int

    Input encoding

#### Comments
Usually this encoded data is contained in a CERT_NAME_BLOB

## [win32crypt](#README.md#win32crypt).CertOIDToAlgId

int = **CertOIDToAlgId( *ObjId* ** )
Converts a string object identfier to a numeric algorith identifier

#### Parameters


     *ObjId* : string

    String szOID_* identifier

#### Comments
If no matching ALG_ID is found, 0 is returned

## [win32crypt](#README.md#win32crypt).CertOpenStore

[PyCERTSTORE](#README.md#PyCERTSTORE)= **CertOpenStore( *StoreProvider*  *, MsgAndCertEncodingType*  *, CryptProv*  *, Flags*  *, Para* ** )
Opens a certificate store

#### Parameters


     *StoreProvider* : int

    CERT_STORE_PROV_*, currently does not accept string provider names

     *MsgAndCertEncodingType* : int

    Only used with CERT_STORE_PROV_MSG, CERT_STORE_PROV_PKCS7, and CERT_STORE_PROV_FILENAME. 

Usually should be X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

     *CryptProv* :[PyCRYPTPROV](#README.md#PyCRYPTPROV)

    Handle to a CSP, can be None to use default provider

     *Flags* : int

    Combination of CERT_STORE_*_FLAG flags

     *Para=None* : object

     **PyCERT_SYSTEM_STORE_RELOCATE_PARA** , or data specific to provider

## [win32crypt](#README.md#win32crypt).CertOpenSystemStore

[PyCERTSTORE](#README.md#PyCERTSTORE)= **CertOpenSystemStore( *SubsystemProtocol*  *, Prov* ** )
Opens most commonly used Certificate Stores

#### Parameters


     *SubsystemProtocol* :[PyUnicode](#README.md#PyUnicode)

    Name of store to open, will be created if it doesn't already exist

     *Prov=None* :[PyCRYPTPROV](#README.md#PyCRYPTPROV)

    Handle to CSP, use None for default provider

## [win32crypt](#README.md#win32crypt).CertRegisterSystemStore

 **CertRegisterSystemStore( *SystemStore*  *, Flags* ** )
Registers a certificate store

#### Parameters


     *SystemStore* :[PyUnicode](#README.md#PyUnicode)

    string/unicode name of store to be registered, or a sequence of (PyHkey, unicode) representing a CERT_SYSTEM_STORE_RELOCATE_PARA struct

     *Flags* : int

    One of the CERT_SYSTEM_STORE_* location constants, can also be combined with CERT_SYSTEM_STORE_RELOCATE_FLAG and CERT_STORE_CREATE_NEW_FLAG

## [win32crypt](#README.md#win32crypt).CertUnregisterSystemStore

 **CertUnregisterSystemStore( *SystemStore*  *, Flags* ** )
Unregisters a certificate store

#### Parameters


     *SystemStore* :[PyUnicode](#README.md#PyUnicode)

    Name of System store to be unregistered

     *Flags* : int

    CERT_SYSTEM_STORE_RELOCATE_FLAG, CERT_STORE_DELETE_FLAG (CERT_SYSTEM_STORE_RELOCATE_FLAG  not supported yet)

## [win32crypt](#README.md#win32crypt).CryptAcquireContext

[PyCRYPTPROV](#README.md#PyCRYPTPROV)= **CryptAcquireContext( *Container*  *, Provider*  *, ProvType*  *, Flags* ** )
Retrieve handle to a cryptographic service provider

#### Parameters


     *Container* :[PyUnicode](#README.md#PyUnicode)

    Name of key container, can be none to use a Provider's default key container (usually username)

     *Provider* :[PyUnicode](#README.md#PyUnicode)

    Name of cryptographic provider. (MS_*_PROV) Use None for user's default provider.

     *ProvType* : int

    One of the PROV_* constants

     *Flags* : int

    Combination of CRYPT_VERIFYCONTEXT,CRYPT_NEWKEYSET,CRYPT_MACHINE_KEYSET,CRYPT_DELETEKEYSET,CRYPT_SILENT

#### Return Value
Returns None if CRYPT_DELETEKEYSET is specified, otherwise returns a handle to the provider

## [win32crypt](#README.md#win32crypt).CryptBinaryToString

str = **CryptBinaryToString( *Binary*  *, Flags* ** )
Formats a binary buffer into the specified type of string

#### Parameters


     *Binary* : bytes

    Buffer containing raw data to be formatted

     *Flags* : int

    Type of output desired, win32cryptcon.CRYPT_STRING_* value

#### Win32 API References


    Search for *CryptBinaryToString* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CryptBinaryToString),[google](#README.md#http://www.google.com/search?q=CryptBinaryToString)or[google groups](#README.md#http://groups.google.com/groups?q=CryptBinaryToString).

## [win32crypt](#README.md#win32crypt).CryptDecodeMessage

dict = **CryptDecodeMessage( *EncodedBlob*  *, DecryptPara*  *, VerifyPara*  *, MsgTypeFlags*  *, SignerIndex*  *, PrevInnerContentType*  *, ReturnData* ** )
Decodes and decrypts a message, and verifies its signatures

#### Parameters


     *EncodedBlob* : buffer

    Data to be decoded

     *DecryptPara* : dict

    [PyCRYPT_DECRYPT_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTDECRYPT_MESSAGE_PARA)containing decryption parms

     *VerifyPara=None* : dict

    [PyCRYPT_VERIFY_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTVERIFY_MESSAGE_PARA)containing signature verification parms

     *MsgTypeFlags=CMSG_ALL_FLAGS* : int

    Combination of CMSG_DATA_FLAG, CMSG_SIGNED_FLAG, CMSG_ENVELOPED_FLAG, CMSG_SIGNED_AND_ENVELOPED_FLAG, or CMSG_HASHED_FLAG

     *SignerIndex=0* : int

    Index of the signer to verify,  ignored if message is not signed.

     *PrevInnerContentType=0* : int

    Content type returned from previous call, used during subsequent pass on a nested message

     *ReturnData=True* : boolean

    Indicates if decoded data should be returned.

#### Comments
Only one level of encoding is interpreted.  Some types of messages will need multiple calls to completely decode. 

For example, to decode a message created by[win32crypt::CryptSignAndEncryptMessage](#win32crypt.md#win32cryptCryptSignAndEncryptMessage), one pass with CMSG_ENVELOPED_FLAG 

and a second pass using CMSG_SIGNED_FLAG are required to recover the original message text.

#### Return Value
Output params are returned as a dict containing:
{MsgType:int},&#09&#09&#09&#09&#09&nbsp&nbsp##Type of message decoded, one of CMSG_DATA,CMSG_SIGNED,CMSG_ENVELOPED,CMSG_SIGNED_AND_ENVELOPED,CMSG_HASHED
InnerContentType:int,&#09&#09&#09&nbsp&nbsp##Type of decoded content returned, uses same set of values as MsgType.  CMSG_DATA indicates unencoded data.
Decoded:str,&#09&#09&#09&#09&#09&nbsp&nbsp##The decoded data, will be None if ReturnData is False.
XchgCert:[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT),&#09&nbsp&nbsp##Certificate used to decode message
SignerCert:[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT)}&#09&nbsp&nbsp##Certificate used to sign message

## [win32crypt](#README.md#win32crypt).CryptDecodeObjectEx

object = **CryptDecodeObjectEx( *StructType*  *, Encoded*  *, Flags*  *, CertEncodingType*  *, DecodePara* ** )
Decodes ASN encoded data

#### Parameters


     *StructType* : str/int

    An OID identifying the type of data to be decoded, can be either str or int

     *Encoded* : str

    String or buffer containing ASN encoded data

     *Flags=0* : int

    Encoding options, can be combination CRYPT_UNICODE_* constants.  CRYPT_ENCODE_ALLOC_FLAG is added to flags..

     *CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING* : int

    Encoding types

     *DecodePara=None* : object

    Not supported, use only None

 **OID**  **Object returned** szOID_ENHANCED_KEY_USAGESequence of OIDsX509_ENHANCED_KEY_USAGESequence of OIDsszOID_KEY_USAGE[PyCRYPT_BIT_BLOB](#PyCRYPT.md#PyCRYPTBIT_BLOB)X509_KEY_USAGE[PyCRYPT_BIT_BLOB](#PyCRYPT.md#PyCRYPTBIT_BLOB)X509_BITS[PyCRYPT_BIT_BLOB](#PyCRYPT.md#PyCRYPTBIT_BLOB)szOID_SUBJECT_ALT_NAME[PyCERT_ALT_NAME_INFO](#PyCERT.md#PyCERTALT_NAME_INFO)szOID_SUBJECT_ALT_NAME2[PyCERT_ALT_NAME_INFO](#PyCERT.md#PyCERTALT_NAME_INFO)szOID_ISSUER_ALT_NAME[PyCERT_ALT_NAME_INFO](#PyCERT.md#PyCERTALT_NAME_INFO)szOID_ISSUER_ALT_NAME2[PyCERT_ALT_NAME_INFO](#PyCERT.md#PyCERTALT_NAME_INFO)szOID_NEXT_UPDATE_LOCATION[PyCERT_ALT_NAME_INFO](#PyCERT.md#PyCERTALT_NAME_INFO)X509_ALTERNATE_NAME[PyCERT_ALT_NAME_INFO](#PyCERT.md#PyCERTALT_NAME_INFO)X509_NAME_VALUE[PyCERT_NAME_VALUE](#PyCERT.md#PyCERTNAME_VALUE)X509_UNICODE_ANY_STRING[PyCERT_NAME_VALUE](#PyCERT.md#PyCERTNAME_VALUE)X509_UNICODE_NAME_VALUE[PyCERT_NAME_VALUE](#PyCERT.md#PyCERTNAME_VALUE)X509_NAME[PyCERT_NAME_INFO](#PyCERT.md#PyCERTNAME_INFO)X509_UNICODE_NAME[PyCERT_NAME_INFO](#PyCERT.md#PyCERTNAME_INFO)szOID_KEY_ATTRIBUTES[PyCERT_KEY_ATTRIBUTES_INFO](#PyCERT.md#PyCERTKEY_ATTRIBUTES_INFO)X509_KEY_ATTRIBUTES[PyCERT_KEY_ATTRIBUTES_INFO](#PyCERT.md#PyCERTKEY_ATTRIBUTES_INFO)szOID_BASIC_CONSTRAINTS[PyCERT_BASIC_CONSTRAINTS_INFO](#PyCERT.md#PyCERTBASIC_CONSTRAINTS_INFO)X509_BASIC_CONSTRAINTS[PyCERT_BASIC_CONSTRAINTS_INFO](#PyCERT.md#PyCERTBASIC_CONSTRAINTS_INFO)szOID_BASIC_CONSTRAINTS2[PyCERT_BASIC_CONSTRAINTS2_INFO](#PyCERT.md#PyCERTBASIC_CONSTRAINTS2_INFO)X509_BASIC_CONSTRAINTS2[PyCERT_BASIC_CONSTRAINTS2_INFO](#PyCERT.md#PyCERTBASIC_CONSTRAINTS2_INFO)szOID_CERT_POLICIESSequence of[PyCERT_POLICY_INFO](#PyCERT.md#PyCERTPOLICY_INFO)objectsszOID_APPLICATION_CERT_POLICIESSequence of[PyCERT_POLICY_INFO](#PyCERT.md#PyCERTPOLICY_INFO)objectsX509_CERT_POLICIESSequence of[PyCERT_POLICY_INFO](#PyCERT.md#PyCERTPOLICY_INFO)objectsszOID_SUBJECT_KEY_IDENTIFIERBinary string containing the key identifierszOID_AUTHORITY_KEY_IDENTIFIER[PyCERT_AUTHORITY_KEY_ID_INFO](#PyCERT.md#PyCERTAUTHORITY_KEY_ID_INFO)X509_AUTHORITY_KEY_ID[PyCERT_AUTHORITY_KEY_ID_INFO](#PyCERT.md#PyCERTAUTHORITY_KEY_ID_INFO)
#### Return Value
Type of object returned is dependent on the StructType to be decoded

## [win32crypt](#README.md#win32crypt).CryptDecryptAndVerifyMessageSignature

dict = **CryptDecryptAndVerifyMessageSignature( *EncryptedBlob*  *, DecryptPara*  *, VerifyPara*  *, SignerIndex* ** )
Decrypts and decodes a signed message, and verifies its signatures

#### Parameters


     *EncryptedBlob* : buffer

    Encoded message to be decrypted.

     *DecryptPara* :[PyCRYPT_DECRYPT_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTDECRYPT_MESSAGE_PARA)

    Decryption parms

     *VerifyPara=None* :[PyCRYPT_VERIFY_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTVERIFY_MESSAGE_PARA)

    Signature verification parms

     *SignerIndex=0* : int

    Index of the signer to verify, zero-based.

#### Comments
Usage is similar to CryptDecodeMessage, except that it undoes all levels of encoding and 

returns the bare message.   This function is the counterpart of CryptSignAndEncryptMessage.

#### Return Value
Output params are returned as a dict containing:
Decrypted:str,&#09&#09&#09&#09&#09&nbsp&nbsp##The decrypted message contents
XchgCert:[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT),&#09&nbsp&nbsp##Certificate whose private key was used to decrypt message
SignerCert:[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT)&#09&nbsp&nbsp##Certificate used to sign message

## [win32crypt](#README.md#win32crypt).CryptDecryptMessage

str,[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT)= **CryptDecryptMessage( *DecryptPara*  *, EncryptedBlob* ** )
Decrypts an encrypted and encoded message

#### Parameters


     *DecryptPara* :[PyCRYPT_DECRYPT_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTDECRYPT_MESSAGE_PARA)

    Dictionary containing decryption parameters

     *EncryptedBlob* : buffer

    Buffer containing an encrypted message

#### Return Value
Returns the decrypted message and a handle to the certificate used to decrypt it

## [win32crypt](#README.md#win32crypt).CryptEncodeObjectEx

str = **CryptEncodeObjectEx( *StructType*  *, StructInfo*  *, Flags*  *, CertEncodingType*  *, EncodePara* ** )
Serializes and ASN encodes cryptographic structures

#### Parameters


     *StructType* : str/int

    OID identifying type of data to be encoded, either szOID_* string or a numeric id

     *StructInfo* : dict

    Information to be encoded.  Contents of dict are dependent on StructType

     *Flags=0* : int

    Encoding options, combination of CRYPT_UNICODE_* constants.  CRYPT_ENCODE_ALLOC_FLAG is added to flags..

     *CertEncodingType=X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING* : int

    Encoding types

     *EncodePara=None* : object

    Not supported, use only None


## [win32crypt](#README.md#win32crypt).CryptEncryptMessage

str = **CryptEncryptMessage( *EncryptPara*  *, RecipientCert*  *, ToBeEncrypted* ** )
Encrypts and encodes a message

#### Parameters


     *EncryptPara* :[PyCRYPT_ENCRYPT_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTENCRYPT_MESSAGE_PARA)

    Encryption parameters

     *RecipientCert* : ([PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT),...)

    Sequence of handles to recipients' certificates

     *ToBeEncrypted* : buffer

    Data to be encrypted

## [win32crypt](#README.md#win32crypt).CryptEnumKeyIdentifierProperties

list = **CryptEnumKeyIdentifierProperties( *KeyIdentifier*  *, PropId*  *, Flags*  *, ComputerName* ** )
Enumerates private keys for certificates and their properties

#### Parameters


     *KeyIdentifier=None* : string

    Id of a certificate key, can be None for all keys

     *PropId=0* : int

    CERT_*_PROP_ID constant. Limits returned values to specified propery, Use 0 for all

     *Flags=0* : int

    Can be CRYPT_KEYID_MACHINE_FLAG to list keys for local machine, or remote machine if ComputerName is given

     *ComputerName=None* :[PyUnicode](#README.md#PyUnicode)

    Name of remote computer, use None for local machine

## [win32crypt](#README.md#win32crypt).CryptEnumOIDInfo

list = **CryptEnumOIDInfo( *GroupId* ** )
Lists registered Object Identifiers that belong to specified group

#### Parameters


     *GroupId=0* : int

    The type of OIDs to enmerate, one of the CRYPT_*_OID_GROUP_ID constants or 0 to list all

## [win32crypt](#README.md#win32crypt).CryptEnumProviderTypes

[([PyUnicode](#README.md#PyUnicode),int),...] = **CryptEnumProviderTypes(** )
Lists available local cryptographic provider types

#### Comments
Windows XP sp3 has a bug that causes this function to always fail with ERROR_MORE_DATA (234) 

See KB959160 for a hotfix

#### Return Value
Returns a sequence of tuples containing name and identifier of provider types

## [win32crypt](#README.md#win32crypt).CryptEnumProviders

[([PyUnicode](#README.md#PyUnicode),int),...] = **CryptEnumProviders(** )
List cryptography providers

#### Return Value
Returns a sequence of tuples containing provider name and type

## [win32crypt](#README.md#win32crypt).CryptFindLocalizedName

[PyUnicode](#README.md#PyUnicode)= **CryptFindLocalizedName( *CryptName* ** )
Returns localized name for predefined system stores (Root, My, .Default, .LocalMachine)

#### Parameters


     *CryptName* :[PyUnicode](#README.md#PyUnicode)

    Name of a system store

## [win32crypt](#README.md#win32crypt).CryptFindOIDInfo

dict = **CryptFindOIDInfo( *KeyType*  *, Key*  *, GroupId* ** )
Returns information about an algorithm identifier or object identifier

#### Parameters


     *KeyType* : int

    One of CRYPT_OID_INFO_OID_KEY,CRYPT_OID_INFO_NAME_KEY,CRYPT_OID_INFO_ALGID_KEY,CRYPT_OID_INFO_SIGN_KEY

     *Key* : object

    Type is dependent on KeyType

     *GroupId=0* : int

    CRYPT_*_GROUP_ID constant, or 0

#### Return Value
Returns a dictionary of CRYPT_OID_INFO data


## [win32crypt](#README.md#win32crypt).CryptFormatObject

str = **CryptFormatObject( *StructType*  *, Encoded*  *, FormatStrType*  *, CertEncodingType*  *, FormatType*  *, FormatStruct* ** )
Formats an encoded buffer into a readable string

#### Parameters


     *StructType* : str/int

    OID identifying the type of encoded data, one of the szOID_* strings or an integer OID

     *Encoded* : str

    String containing encoded data to be formatted

     *FormatStrType=0* : int

    String formatting options, combination of CRYPT_FORMAT_STR_MULTI_LINE, CRYPT_FORMAT_STR_NO_HEX

     *CertEncodingType=X509_ASN_ENCODING* : int

    Input encoding

     *FormatType=0* : int

    Reserved, use only 0

     *FormatStruct=None* : None

    Reserved, use only None

#### Comments
Will handle all of the common certificate extension types

#### Win32 API References


    Search for *CryptFormatObject* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CryptFormatObject),[google](#README.md#http://www.google.com/search?q=CryptFormatObject)or[google groups](#README.md#http://groups.google.com/groups?q=CryptFormatObject).

## [win32crypt](#README.md#win32crypt).CryptGetDefaultProvider

[PyUnicode](#README.md#PyUnicode)= **CryptGetDefaultProvider( *ProvType*  *, Flags* ** )
Returns default provider for local machine or current user

#### Parameters


     *ProvType* : int

    Type of provider (PROV_* constant)

     *Flags* : int

    CRYPT_MACHINE_DEFAULT or CRYPT_USER_DEFAULT

## [win32crypt](#README.md#win32crypt).CryptGetKeyIdentifierProperty

object = **CryptGetKeyIdentifierProperty( *KeyIdentifier*  *, PropId*  *, Flags*  *, ComputerName* ** )
Retrieves a property from a certificate by its key indentifier

#### Parameters


     *KeyIdentifier* : string

    Hash that identifies a certificate key

     *PropId=CERT_KEY_PROV_INFO_PROP_ID* : int

    Property identifier, one of the CERT_*_PROP_ID values

     *Flags=0* : int

    Use CRYPT_KEYID_MACHINE_FLAG for machine keyset. (CRYPT_KEYID_ALLOC_FLAG is always added to Flags)

     *ComputerName=None* :[PyUnicode](#README.md#PyUnicode)

    Name of remote computer, use None for local machine

#### Comments
CERT_KEY_PROV_INFO_PROP_ID is only property currently supported

## [win32crypt](#README.md#win32crypt).CryptGetMessageCertificates

[PyCERTSTORE](#README.md#PyCERTSTORE)= **CryptGetMessageCertificates( *SignedBlob*  *, MsgAndCertEncodingType*  *, CryptProv*  *, Flags* ** )
Extracts certificates encoded in a message

#### Parameters


     *SignedBlob* : buffer

    Buffer containing a signed message

     *MsgAndCertEncodingType=X509_ASN_ENCODING|PKCS_7_ASN_ENCODING* : int

    Message and certificate encoding types

     *CryptProv=None* :[PyCRYPTPROV](#README.md#PyCRYPTPROV)

    Handle to a CSP, use None for default

     *Flags=0* : int

    Same flags used with[win32crypt::CertOpenStore](#win32crypt.md#win32cryptCertOpenStore)

## [win32crypt](#README.md#win32crypt).CryptGetMessageSignerCount

int = **CryptGetMessageSignerCount( *SignedBlob*  *, MsgEncodingType* ** )
Finds the number of signers of an encoded message

#### Parameters


     *SignedBlob* : buffer

    Buffer containing a signed message

     *MsgEncodingType=X509_ASN_ENCODING|PKCS_7_ASN_ENCODING* : int

    Message encoding type

## [win32crypt](#README.md#win32crypt).CryptProtectData

bytes = **CryptProtectData( *DataIn*  *, DataDescr*  *, OptionalEntropy*  *, Reserved*  *, PromptStruct*  *, Flags* ** )
Encrypts data using a session key derived from current user's logon credentials

#### Parameters


     *DataIn* : bytes

    Data to be encrypted.

     *DataDescr=None* :[PyUnicode](#README.md#PyUnicode)

    Description to add to the data

     *OptionalEntropy=None* : bytes

    Extra entropy (eg password) for encryption process, can be None

     *Reserved=None* : None

    Must be None

     *PromptStruct=None* :[PyCRYPTPROTECT_PROMPTSTRUCT](#PyCRYPTPROTECT.md#PyCRYPTPROTECTPROMPTSTRUCT)

    Contains options for UI display during encryption and decryption, can be None

     *Flags=0* : int

    Combination of CRYPTPROTECT_* flags

## [win32crypt](#README.md#win32crypt).CryptQueryObject

dict = **CryptQueryObject( *ObjectType*  *, Object*  *, ExpectedContentTypeFlags*  *, ExpectedFormatTypeFlags*  *, Flags* ** )
Determines the cryptographic type of input data

#### Parameters


     *ObjectType* : int

    Type of input, CERT_QUERY_OBJECT_BLOB or CERT_QUERY_OBJECT_FILE

     *Object* : str

    Raw data or a filename containing the data to be queried depending on ObjectType

     *ExpectedContentTypeFlags=CERT_QUERY_CONTENT_FLAG_ALL* : int

    One of the CERT_QUERY_CONTENT_FLAG_* constants

     *ExpectedFormatTypeFlags=CERT_QUERY_FORMAT_FLAG_ALL* : int

    One of the CERT_QUERY_FORMAT_FLAG_* constants

     *Flags=0* : int

    Reserved, use only 0

#### Return Value
Returns a dictionary containing
{MsgAndCertEncodingType:int,&#09## encoding type, usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING
ContentType:int,&#09&#09&#09&#09## One of the CERT_QUERY_CONTENT_* constants
FormatType:int,&#09&#09&#09&#09&#09## One of the CERT_QUERY_FORMAT_* constants
CertStore:[PyCERTSTORE](#README.md#PyCERTSTORE),&#09&#09## Handle to certificate store containing all certficates in the object, may be None
Msg:[PyCRYPTMSG](#README.md#PyCRYPTMSG),&#09&#09&#09&#09## If input doesn't contains a PKCS7 message, will be None
Context:[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT)}&#09&#09## A certificate, CRL, or CTL context depending on ContentType, may be None

## [win32crypt](#README.md#win32crypt).CryptSetProviderEx

 **CryptSetProviderEx( *ProvName*  *, ProvType*  *, Flags* ** )
Sets default provider (for machine or user) for specified type

#### Parameters


     *ProvName* :[PyUnicode](#README.md#PyUnicode)

    Name of new default provider (MS_*_PROV value)

     *ProvType* : int

    One of the PROV_* provider types

     *Flags* : int

    CRYPT_MACHINE_DEFAULT or CRYPT_USER_DEFAULT.  Combine with CRYPT_DELETE_DEFAULT to remove default.

## [win32crypt](#README.md#win32crypt).CryptSignAndEncryptMessage

str = **CryptSignAndEncryptMessage( *SignPara*  *, EncryptPara*  *, RecipientCert*  *, ToBeSignedAndEncrypted* ** )
Encrypts, encodes and signs a message using a certificate

#### Parameters


     *SignPara* :[PyCRYPT_SIGN_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTSIGN_MESSAGE_PARA)

    Message signing parameters

     *EncryptPara* :[PyCRYPT_ENCRYPT_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTENCRYPT_MESSAGE_PARA)

    Encryption parameters

     *RecipientCert* : ([PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT),...)

    Sequence of certificates of intended recipients

     *ToBeSignedAndEncrypted* : str

    Buffer containing data to be encoded in the message

## [win32crypt](#README.md#win32crypt).CryptSignMessage

str = **CryptSignMessage( *SignPara*  *, ToBeSigned*  *, DetachedSignature* ** )
Signs and encodes a message

#### Parameters


     *SignPara* :[PyCRYPT_SIGN_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTSIGN_MESSAGE_PARA)

    Message signing parameters

     *ToBeSigned* : (str,...)

    Sequence of strings containing message data.  Can only contain 1 string if DetachedSignature parm is False.

     *DetachedSignature=False* : boolean

    If True, only the signature itself is encoded in output msg.

## [win32crypt](#README.md#win32crypt).CryptStringToBinary

bytes, int, int = **CryptStringToBinary( *String*  *, Flags* ** )
Converts a formatted string back into raw bytes

#### Parameters


     *String* : str

    Formatted string to be converted to raw binary data

     *Flags* : int

    Input format (win32cryptcon.CRYPT_STRING_*)

#### Win32 API References


    Search for *CryptStringToBinary* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CryptStringToBinary),[google](#README.md#http://www.google.com/search?q=CryptStringToBinary)or[google groups](#README.md#http://groups.google.com/groups?q=CryptStringToBinary).

#### Return Value
Returns the decoded binary data, number of header characters skipped, and CRYPT_STRING_* value 

denoting the type of data found (used if input Flags is one of *_ANY values)

## [win32crypt](#README.md#win32crypt).CryptUnprotectData

(str, bytes) = **CryptUnprotectData( *DataIn*  *, OptionalEntropy*  *, Reserved*  *, PromptStruct*  *, Flags* ** )
Decrypts data that was encrypted using[win32crypt::CryptProtectData](#win32crypt.md#win32cryptCryptProtectData).

#### Parameters


     *DataIn* : bytes

    Data to be decrypted.

     *OptionalEntropy=None* : bytes

    Extra entropy passed to CryptProtectData

     *Reserved=None* : None

    Must be None

     *PromptStruct=None* :[PyCRYPTPROTECT_PROMPTSTRUCT](#PyCRYPTPROTECT.md#PyCRYPTPROTECTPROMPTSTRUCT)

    Contains options for UI display during encryption and decryption, can be None

     *Flags=0* : int

    Combination of CRYPTPROTECT_* flags

#### Return Value
The result is a tuple of (description, data) where description 

is the description that was passed to[win32crypt::CryptProtectData](#win32crypt.md#win32cryptCryptProtectData), and 

data is the unencrypted data.

## [win32crypt](#README.md#win32crypt).CryptVerifyDetachedMessageSignature

[PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT)= **CryptVerifyDetachedMessageSignature( *SignerIndex*  *, DetachedSignBlob*  *, ToBeSigned*  *, VerifyPara* ** )
Verifies a signature that is encoded separately from the data

#### Parameters


     *SignerIndex* : int

    Index of the signer to verify

     *DetachedSignBlob* : buffer

    Buffer containing an encoded signature

     *ToBeSigned* : (buffer,...)

    Sequence of buffers containing message data.

     *VerifyPara=None* :[PyCRYPT_VERIFY_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTVERIFY_MESSAGE_PARA)

    Signature verification parameters, use None for defaults

#### Return Value
Returns the signing certificate

## [win32crypt](#README.md#win32crypt).CryptVerifyMessageSignature

([PyCERT_CONTEXT](#PyCERT.md#PyCERTCONTEXT), str) = **CryptVerifyMessageSignature( *SignedBlob*  *, SignerIndex*  *, VerifyPara*  *, ReturnData* ** )
Verifies the signature of an encoded message

#### Parameters


     *SignedBlob* : str

    Buffer containing a signed message

     *SignerIndex=0* : int

    Index of the signer to verify, zero-based

     *VerifyPara=None* :[PyCRYPT_VERIFY_MESSAGE_PARA](#PyCRYPT.md#PyCRYPTVERIFY_MESSAGE_PARA)

    Signature verification parameters, use None for defaults

     *ReturnData=False* : boolean

    Indicates if decoded data should be returned.

#### Return Value
Returns the signing certificate and the decoded data.  If ReturnData parm is False, None is returned for data.

## [win32crypt](#README.md#win32crypt).PFXImportCertStore

[PyCERTSTORE](#README.md#PyCERTSTORE)= **PFXImportCertStore( *PFX*  *, Password*  *, Flags* ** )
Creates a certificate store from PKCS#12 data (*.PFX files)

#### Parameters


     *PFX* : bytes

    Buffer containing PKCS#12-formatted certificate(s)

     *Password* : str

    Password used to encrypt the data, may be None

     *Flags* : int

    Allowed flags are CRYPT_EXPORTABLE,CRYPT_USER_PROTECTED,CRYPT_MACHINE_KEYSET, and CRYPT_USER_KEYSET

#### Comments
MSDN docs specify that *one* of the Flags can be used, but in practice a combination is allowed
Depending on the encrypting application, a blank password ("") may be treated differently that a NULL 

password (None), so if you have a PFX with no password try both.

#### Win32 API References


    Search for *PFXImportCertStore* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PFXImportCertStore),[google](#README.md#http://www.google.com/search?q=PFXImportCertStore)or[google groups](#README.md#http://groups.google.com/groups?q=PFXImportCertStore).

## [win32crypt](#README.md#win32crypt).PFXIsPFXBlob

boolean = **PFXIsPFXBlob( *PFX* ** )
Checks if data buffer contains a PFX blob

#### Parameters


     *PFX* : bytes

    Buffer containing data to be checked

#### Win32 API References


    Search for *PFXIsPFXBlob* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PFXIsPFXBlob),[google](#README.md#http://www.google.com/search?q=PFXIsPFXBlob)or[google groups](#README.md#http://groups.google.com/groups?q=PFXIsPFXBlob).

## [win32crypt](#README.md#win32crypt).PFXVerifyPassword

boolean = **PFXVerifyPassword( *PFX*  *, Password*  *, Flags* ** )
Checks if a PFX blob can be decrypted with given password

#### Parameters


     *PFX* : bytes

    Buffer containing PKCS#12-formatted certificate(s)

     *Password* : str

    Password used to encrypt the data, may be None

     *Flags* : int

    Allowed flags are CRYPT_EXPORTABLE,CRYPT_USER_PROTECTED,CRYPT_MACHINE_KEYSET, and CRYPT_USER_KEYSET

#### Win32 API References


    Search for *PFXVerifyPassword* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PFXVerifyPassword),[google](#README.md#http://www.google.com/search?q=PFXVerifyPassword)or[google groups](#README.md#http://groups.google.com/groups?q=PFXVerifyPassword).