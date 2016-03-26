# PyCERT

## PyCERT_ALT_NAME_ENTRY Object

Represented as a 2-tuple

#### Comments
First item is one of the CERT_ALT_NAME_* constants indicating the type.
Second item is either a string, or for CERT_ALT_NAME_OTHER_NAME a[PyCERT_OTHER_NAME](PyCERT.md#pycertother_name)

## PyCERT_ALT_NAME_INFO Object

Sequence of[PyCERT_ALT_NAME_ENTRY](PyCERT.md#pycertalt_name_entry)objects

## PyCERT_AUTHORITY_KEY_ID_INFO Object

Dict containing the identity of a CA

#### Properties

  -  __str KeyId__ 
    Unique identifier of private key, usually a hash

  -  __str CertIssuer__ 
    Encoded DN of the Certificate Authority.  Decode using X509_UNICODE_NAME

  -  __int CertSerialNumber__ 
    Serial nbr of the CA's signing certificate

## PyCERT_BASIC_CONSTRAINTS2_INFO Object

Dict representing a CERT_BASIC_CONSTRAINTS2_INFO struct

#### Properties

  -  __boolean fCA__ 
    Indicates if cert represents a certificate authority

  -  __boolean fPathLenConstraint__ 
    Indicates if PathLenConstraint member is used

  -  __int PathLenConstraint__ 
    Limits number of intermediate CA's between root CA and end user

## PyCERT_BASIC_CONSTRAINTS_INFO Object

Dict representing a CERT_BASIC_CONSTRAINTS_INFO struct

#### Properties

  -  __[PyCRYPT_BIT_BLOB](PyCRYPT.md#pycryptbit_blob)SubjectType__ 
    Contains a combination of CERT_CA_SUBJECT_FLAG,CERT_END_ENTITY_SUBJECT_FLAG

  -  __boolean fPathLenConstraint__ 
    Indicates if PathLenConstraint member is used

  -  __int PathLenConstraint__ 
    Limits number of intermediate CA's between root CA and end user

  -  __tuple SubtreesConstraint__ 
    Sequence of encoded name blobs

## PyCERT_CONTEXT Object

Handle to a certificate context

#### Methods


  - [CertFreeCertificateContext](PyCERT.md#pycertcontext_certfreecertificatecontext)

    Frees the context handle&nbsp;

  - [CertEnumCertificateContextProperties](PyCERT.md#pycertcontext_certenumcertificatecontextproperties)

    Lists property ids for the certificate&nbsp;

  - [CryptAcquireCertificatePrivateKey](PyCERT.md#pycertcontext_cryptacquirecertificateprivatekey)

    Retrieves the private key associated with the certificate&nbsp;

  - [CertGetIntendedKeyUsage](PyCERT.md#pycertcontext_certgetintendedkeyusage)

    Returns the intended key usage from the certificate extensions&nbsp;

  - [CertGetEnhancedKeyUsage](PyCERT.md#pycertcontext_certgetenhancedkeyusage)

    Finds the enhanced key usage property and/or extension for the certificate&nbsp;

  - [CertSerializeCertificateStoreElement](PyCERT.md#pycertcontext_certserializecertificatestoreelement)

    Serializes the certificate and its properties&nbsp;

  - [CertVerifySubjectCertificateContext](PyCERT.md#pycertcontext_certverifysubjectcertificatecontext)

    Checks the validity of the certificate&nbsp;

  - [CertDeleteCertificateFromStore](PyCERT.md#pycertcontext_certdeletecertificatefromstore)

    Removes the certificate from its store&nbsp;

  - [CertGetCertificateContextProperty](PyCERT.md#pycertcontext_certgetcertificatecontextproperty)

    Retrieves the specified property from the certificate&nbsp;

  - [CertSetCertificateContextProperty](PyCERT.md#pycertcontext_certsetcertificatecontextproperty)

    Sets a property for a certificate&nbsp;

#### Properties

  -  __int HANDLE__ 
    Pointer to CERT_CONTEXT struct

  -  __[PyCERTSTORE](#pycertstore)CertStore__ 
    Handle to the certificate store that contains this certificate

  -  __str CertEncoded__ 
    Content of the certificate as encoded bytes

  -  __int CertEncodingType__ 
    Method used to encode the certifcate, usually X509_ASN_ENCODING or PKCS_7_ASN_ENCODING

  -  __int Version__ 
    One of the CERT_V* values

  -  __[PyUnicode](#pyunicode)Subject__ 
    Encoded CERT_NAME_INFO struct containing the subject name. Can be decoded 

using __cryptoapi::CryptDecodeObjectEx__ with X509_UNICODE_NAME, or formatted using __cryptoapi::CertNameToStr__ 

  -  __[PyUnicode](#pyunicode)Issuer__ 
    Certificate Authority that issued certificate as encoded CERT_NAME_INFO.  Use __cryptoapi::CryptDecodeObjectEx__ to decode into individual components, or __cryptoapi::CertNameToStr__ to 

return a single formatted string

  -  __[PyTime](#pytime)NotBefore__ 
    Beginning of certificate's period of validity

  -  __[PyTime](#pytime)NotAfter__ 
    End of certificate's period of validity

  -  __str SignatureAlgorithm__ 
    Object id of the certifcate's signature algorithm

  -  __([PyCERT_EXTENSION](PyCERT.md#pycertextension),...) Extension__ 
    Sequence of CERT_EXTENSION dicts containing certificate's extensions

  -  __[PyCERT_PUBLIC_KEY_INFO](PyCERT.md#pycertpublic_key_info)SubjectPublicKeyInfo__ 
    Encoded public key of certificate

  -  __int SerialNumber__ 
    Serial number assigned by the issuer

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertDeleteCertificateFromStore

 __CertDeleteCertificateFromStore(__ )
Removes the certificate from its store

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertEnumCertificateContextProperties

[int,...] = __CertEnumCertificateContextProperties(__ )
Lists property ids for the certificate

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertFreeCertificateContext

 __CertFreeCertificateContext(__ )
Frees the certificate context

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertGetCertificateContextProperty

object = __CertGetCertificateContextProperty( *PropId* __ )
Retrieves the specified property from the certificate

#### Parameters


  -  *PropId* : int

    One of the CERT_*_PROP_ID constants

 __PropId__  __Returned value__ CERT_ARCHIVED_PROP_IDBooleanCERT_DATE_STAMP_PROP_ID[PyTime](#pytime)CERT_ACCESS_STATE_PROP_IDintCERT_KEY_SPEC_PROP_IDintCERT_DESCRIPTION_PROP_IDUnicodeCERT_FRIENDLY_NAME_PROP_IDUnicodeCERT_PVK_FILE_PROP_IDUnicodeCERT_AUTO_ENROLL_PROP_IDUnicodeCERT_HASH_PROP_IDString containing a hashCERT_SHA1_HASH_PROP_IDString containing a hashCERT_MD5_HASH_PROP_IDString containing a hashCERT_SIGNATURE_HASH_PROP_IDString containing a hashCERT_KEY_IDENTIFIER_PROP_IDString containing a hashCERT_SUBJECT_NAME_MD5_HASH_PROP_IDString containing a hashCERT_KEY_PROV_HANDLE_PROP_ID[PyCRYPTPROV](#pycryptprov)CERT_SUBJECT_PUBLIC_KEY_MD5_HASH_PROP_IDString containing a hashCERT_ISSUER_PUBLIC_KEY_MD5_HASH_PROP_IDString containing a hashCERT_CTL_USAGE_PROP_IDEncoded CTL_USAGE, decode as X509_ENHANCED_KEY_USAGE (CTL_USAGE and CERT_ENHKEY_USAGE are identical)CERT_ENHKEY_USAGE_PROP_IDEncoded CTL_USAGE. Can be decoded using __cryptoapi::CryptDecodeObjectEx__ with X509_ENHANCED_KEY_USAGECERT_KEY_PROV_INFO_PROP_IDCRYPT_KEY_PROV_INFO dictCERT_KEY_CONTEXT_PROP_IDDict representing CERT_KEY_CONTEXT structCERT_NEXT_UPDATE_LOCATION_PROP_IDEncoded CERT_ALT_NAME_INFO, decode using __cryptoapi::CryptDecodeObjectEx__ with szOID_NEXT_UPDATE_LOCATION
#### Return Value
Type of object returned is dependent on the property id requested.

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertGetEnhancedKeyUsage

tuple = __CertGetEnhancedKeyUsage( *Flags* __ )
Finds the enhanced key usage property and/or extension for the certificate

#### Parameters


  -  *Flags=0* : int

    CERT_FIND_EXT_ONLY_ENHKEY_USAGE_FLAG, CERT_FIND_PROP_ONLY_ENHKEY_USAGE_FLAG, or 0

#### Return Value
Returns a sequence of usage OIDs

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertGetIntendedKeyUsage

int = __CertGetIntendedKeyUsage(__ )
Returns the intended key usage from the certificate extensions (szOID_KEY_USAGE or szOID_KEY_ATTRIBUTES)

#### Return Value
Returns a combination of CERT_*_KEY_USAGE values

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertSerializeCertificateStoreElement

string = __CertSerializeCertificateStoreElement( *Flags* __ )
Serializes the certificate and its properties

#### Parameters


  -  *Flags=0* : int

    Reserved, use only 0 if passed in

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertSetCertificateContextProperty

 __CertSetCertificateContextProperty( *PropId*  *, Data*  *, Flags* __ )
Sets a property for a certificate

#### Parameters


  -  *PropId* : int

    Id of property to be set, CERT_*_PROP_ID

  -  *Data* : object

    The value to be set for the property.  Type is dependent on PropId. Use None to delete a property.

  -  *Flags=0* : int

    Combination of CERT_SET_* flags


## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CertVerifySubjectCertificateContext

int = __CertVerifySubjectCertificateContext( *Issuer*  *, Flags* __ )
Checks the validity of the certificate

#### Parameters


  -  *Issuer* :[PyCERT_CONTEXT](PyCERT.md#pycertcontext)

    Certificate of authority that issued the certificate

  -  *Flags* : int

    Combination of CERT_STORE_REVOCATION_FLAG,CERT_STORE_SIGNATURE_FLAG and CERT_STORE_TIME_VALIDITY_FLAG indicating which checks should be performed

#### Return Value
Returns flags indicating which validity checks failed, or 0 if all were successful.

## [PyCERT_CONTEXT](PyCERT.md#pycertcontext).CryptAcquireCertificatePrivateKey

(int,[PyCRYPTPROV](#pycryptprov)) = __CryptAcquireCertificatePrivateKey( *Flags* __ )
Retrieves the private key associated with the certificate

#### Parameters


  -  *Flags=0* : int

    Combination of CRYPT_ACQUIRE_*_FLAG constants

#### Comments
Only the owner of the certificate can use this method

#### Return Value
Returns the KeySpec (AT_KEYEXCHANGE or AT_SIGNATURE) and a CSP handle to the key

## PyCERT_EXTENSION Object

Dict containing a certificate extension

#### Properties

  -  __str ObjId__ 
    The OID identifying the type of extension

  -  __boolean Critical__ 
    If true, any contraints or limits contained in the extension should be considered absolute

  -  __str Value__ 
    Binary string containing ASN encoded data. 

To interpret or display extension data, see __cryptoapi::CryptDecodeObjectEx__ and __cryptoapi::CryptFormatObject__ .

#### Comments
These extensions are not yet handled by CryptDecodeObjectEx, but can be formatted with CryptFormatObject.
szOID_PRIVATEKEY_USAGE_PERIOD -- ???? CERT_PRIVATE_KEY_VALIDITY ????
szOID_KEY_USAGE_RESTRICTION - CERT_KEY_USAGE_RESTRICTION_INFO

## PyCERT_KEY_ATTRIBUTES_INFO Object

Dict representing a CERT_KEY_ATTRIBUTES_INFO struct

#### Properties

  -  __str KeyId__ 
    Usually a hash that uniquely identifies the key

  -  __[PyCRYPT_BIT_BLOB](PyCRYPT.md#pycryptbit_blob)IntendedKeyUsage__ 
    Contains a byte with CERT_*_KEY_USAGE flags

  -  __dict PrivateKeyUsagePeriod__ 
    Private key's begin and end effective dates, may be None

## PyCERT_NAME_INFO Object

Sequence of CERT_RDN's

## PyCERT_NAME_VALUE Object

Dict containing type (CERT_RDN_*) and a unicode string

## PyCERT_OTHER_NAME Object

Dict containing {ObjId, Value}. 

ObjId is one of the string object id's identifying the type of name. 

Value is a binary string containing an encoded CERT_NAME_VALUE that can be decoded 

using X509_UNICODE_NAME_VALUE to return the actual unicode string

## PyCERT_POLICY_INFO Object

Dict containing a certificate policy

#### Properties

  -  __str PolicyIdentifier__ 
    OID identifying the policy

  -  __tuple PolicyQualifier__ 
    Sequence of CERT_POLICY_QUALIFIER dicts

## PyCERT_PUBLIC_KEY_INFO Object

Dict containing an exported public key

#### Properties

  -  __[PyCRYPT_ALGORITHM_IDENTIFIER](PyCRYPT.md#pycryptalgorithm_identifier)Algorithm__ 
    Dict containing OID of the public key algorithm

  -  __[PyCRYPT_BIT_BLOB](PyCRYPT.md#pycryptbit_blob)PublicKey__ 
    Dict containing the encoded public key