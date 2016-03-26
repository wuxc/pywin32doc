# PyCERT


## PyCERT\_ALT\_NAME\_ENTRY Object

Represented as a 2-tuple

#### Comments

First item is one of the CERT\_ALT\_NAME\_\* constants indicating the type\. 

Second item is either a string, or for CERT\_ALT\_NAME\_OTHER\_NAME a [PyCERT\_OTHER\_NAME](PyCERT.md#pycertother_name)


## PyCERT\_ALT\_NAME\_INFO Object

Sequence of [PyCERT\_ALT\_NAME\_ENTRY](PyCERT.md#pycertalt_name_entry) objects


## PyCERT\_AUTHORITY\_KEY\_ID\_INFO Object

Dict containing the identity of a CA

#### Properties

  - str KeyId

    Unique identifier of private key, usually a hash

  - str CertIssuer

    Encoded DN of the Certificate Authority\.  Decode using X509\_UNICODE\_NAME

  - int CertSerialNumber

    Serial nbr of the CA's signing certificate


## PyCERT\_BASIC\_CONSTRAINTS2\_INFO Object

Dict representing a CERT\_BASIC\_CONSTRAINTS2\_INFO struct

#### Properties

  - boolean fCA

    Indicates if cert represents a certificate authority

  - boolean fPathLenConstraint

    Indicates if PathLenConstraint member is used

  - int PathLenConstraint

    Limits number of intermediate CA's between root CA and end user


## PyCERT\_BASIC\_CONSTRAINTS\_INFO Object

Dict representing a CERT\_BASIC\_CONSTRAINTS\_INFO struct

#### Properties

  - [PyCRYPT\_BIT\_BLOB](PyCRYPT.md#pycryptbit_blob) SubjectType

    Contains a combination of CERT\_CA\_SUBJECT\_FLAG,CERT\_END\_ENTITY\_SUBJECT\_FLAG

  - boolean fPathLenConstraint

    Indicates if PathLenConstraint member is used

  - int PathLenConstraint

    Limits number of intermediate CA's between root CA and end user

  - tuple SubtreesConstraint

    Sequence of encoded name blobs


## PyCERT\_CONTEXT Object

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

  - int HANDLE

    Pointer to CERT\_CONTEXT struct

  - [PyCERTSTORE](PyCERTSTORE.md) CertStore

    Handle to the certificate store that contains this certificate

  - str CertEncoded

    Content of the certificate as encoded bytes

  - int CertEncodingType

    Method used to encode the certifcate, usually X509\_ASN\_ENCODING or PKCS\_7\_ASN\_ENCODING

  - int Version

    One of the CERT\_V\* values

  - [PyUnicode](PyUnicode.md) Subject

    Encoded CERT\_NAME\_INFO struct containing the subject name\. Can be decoded 

using cryptoapi::CryptDecodeObjectEx

 with X509\_UNICODE\_NAME, or formatted using cryptoapi::CertNameToStr

  - [PyUnicode](PyUnicode.md) Issuer

    Certificate Authority that issued certificate as encoded CERT\_NAME\_INFO\.  Use 

cryptoapi::CryptDecodeObjectEx

 to decode into individual components, or cryptoapi::CertNameToStr

 to 

return a single formatted string

  - [PyTime](PyTime.md) NotBefore

    Beginning of certificate's period of validity

  - [PyTime](PyTime.md) NotAfter

    End of certificate's period of validity

  - str SignatureAlgorithm

    Object id of the certifcate's signature algorithm

  - \([PyCERT\_EXTENSION](PyCERT.md#pycertextension),\.\.\.\) Extension

    Sequence of CERT\_EXTENSION dicts containing certificate's extensions

  - [PyCERT\_PUBLIC\_KEY\_INFO](PyCERT.md#pycertpublic_key_info) SubjectPublicKeyInfo

    Encoded public key of certificate

  - int SerialNumber

    Serial number assigned by the issuer


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertDeleteCertificateFromStore

CertDeleteCertificateFromStore\(\)
Removes the certificate from its store


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertEnumCertificateContextProperties

\[int,\.\.\.\] = CertEnumCertificateContextProperties\(\)
Lists property ids for the certificate


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertFreeCertificateContext

CertFreeCertificateContext\(\)
Frees the certificate context


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertGetCertificateContextProperty

object = CertGetCertificateContextProperty\(PropId\)
Retrieves the specified property from the certificate

#### Parameters

  - PropId : int

    One of the CERT\_\*\_PROP\_ID constants

   

       PropId

   

   

       Returned value

   

CERT\_ARCHIVED\_PROP\_IDBoolean

CERT\_DATE\_STAMP\_PROP\_ID[PyTime](PyTime.md)

CERT\_ACCESS\_STATE\_PROP\_IDint

CERT\_KEY\_SPEC\_PROP\_IDint

CERT\_DESCRIPTION\_PROP\_IDUnicode

CERT\_FRIENDLY\_NAME\_PROP\_IDUnicode

CERT\_PVK\_FILE\_PROP\_IDUnicode

CERT\_AUTO\_ENROLL\_PROP\_IDUnicode

CERT\_HASH\_PROP\_IDString containing a hash

CERT\_SHA1\_HASH\_PROP\_IDString containing a hash

CERT\_MD5\_HASH\_PROP\_IDString containing a hash

CERT\_SIGNATURE\_HASH\_PROP\_IDString containing a hash

CERT\_KEY\_IDENTIFIER\_PROP\_IDString containing a hash

CERT\_SUBJECT\_NAME\_MD5\_HASH\_PROP\_IDString containing a hash

CERT\_KEY\_PROV\_HANDLE\_PROP\_ID[PyCRYPTPROV](PyCRYPTPROV.md)

CERT\_SUBJECT\_PUBLIC\_KEY\_MD5\_HASH\_PROP\_IDString containing a hash

CERT\_ISSUER\_PUBLIC\_KEY\_MD5\_HASH\_PROP\_IDString containing a hash

CERT\_CTL\_USAGE\_PROP\_IDEncoded CTL\_USAGE, decode as X509\_ENHANCED\_KEY\_USAGE \(CTL\_USAGE and CERT\_ENHKEY\_USAGE are identical\)

CERT\_ENHKEY\_USAGE\_PROP\_IDEncoded CTL\_USAGE\. Can be decoded using cryptoapi::CryptDecodeObjectEx

 with X509\_ENHANCED\_KEY\_USAGE

CERT\_KEY\_PROV\_INFO\_PROP\_IDCRYPT\_KEY\_PROV\_INFO dict

CERT\_KEY\_CONTEXT\_PROP\_IDDict representing CERT\_KEY\_CONTEXT struct

CERT\_NEXT\_UPDATE\_LOCATION\_PROP\_IDEncoded CERT\_ALT\_NAME\_INFO, decode using cryptoapi::CryptDecodeObjectEx

 with szOID\_NEXT\_UPDATE\_LOCATION

#### Return Value
Type of object returned is dependent on the property id requested\.


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertGetEnhancedKeyUsage

tuple = CertGetEnhancedKeyUsage\(Flags\)
Finds the enhanced key usage property and/or extension for the certificate

#### Parameters

  - Flags=0 : int

    CERT\_FIND\_EXT\_ONLY\_ENHKEY\_USAGE\_FLAG, CERT\_FIND\_PROP\_ONLY\_ENHKEY\_USAGE\_FLAG, or 0

#### Return Value
Returns a sequence of usage OIDs


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertGetIntendedKeyUsage

int = CertGetIntendedKeyUsage\(\)
Returns the intended key usage from the certificate extensions \(szOID\_KEY\_USAGE or szOID\_KEY\_ATTRIBUTES\)

#### Return Value
Returns a combination of CERT\_\*\_KEY\_USAGE values


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertSerializeCertificateStoreElement

string = CertSerializeCertificateStoreElement\(Flags\)
Serializes the certificate and its properties

#### Parameters

  - Flags=0 : int

    Reserved, use only 0 if passed in


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertSetCertificateContextProperty

CertSetCertificateContextProperty\(PropId, Data, Flags\)
Sets a property for a certificate

#### Parameters

  - PropId : int

    Id of property to be set, CERT\_\*\_PROP\_ID

  - Data : object

    The value to be set for the property\.  Type is dependent on PropId\. Use None to delete a property\.

  - Flags=0 : int

    Combination of CERT\_SET\_\* flags




## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CertVerifySubjectCertificateContext

int = CertVerifySubjectCertificateContext\(Issuer, Flags

\)
Checks the validity of the certificate

#### Parameters

  - Issuer : [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)

    Certificate of authority that issued the certificate

  - Flags : int

    Combination of CERT\_STORE\_REVOCATION\_FLAG,CERT\_STORE\_SIGNATURE\_FLAG and CERT\_STORE\_TIME\_VALIDITY\_FLAG indicating which checks should be performed

#### Return Value
Returns flags indicating which validity checks failed, or 0 if all were successful\.


## [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)\.CryptAcquireCertificatePrivateKey

\(int,[PyCRYPTPROV](PyCRYPTPROV.md)\) = CryptAcquireCertificatePrivateKey\(Flags\)
Retrieves the private key associated with the certificate

#### Parameters

  - Flags=0 : int

    Combination of CRYPT\_ACQUIRE\_\*\_FLAG constants

#### Comments

Only the owner of the certificate can use this method

#### Return Value
Returns the KeySpec \(AT\_KEYEXCHANGE or AT\_SIGNATURE\) and a CSP handle to the key


## PyCERT\_EXTENSION Object

Dict containing a certificate extension

#### Properties

  - str ObjId

    The OID identifying the type of extension

  - boolean Critical

    If true, any contraints or limits contained in the extension should be considered absolute

  - str Value

    Binary string containing ASN encoded data\. 

To interpret or display extension data, see cryptoapi::CryptDecodeObjectEx

 and cryptoapi::CryptFormatObject

\.

#### Comments

These extensions are not yet handled by CryptDecodeObjectEx, but can be formatted with CryptFormatObject\. 

szOID\_PRIVATEKEY\_USAGE\_PERIOD -- ???? CERT\_PRIVATE\_KEY\_VALIDITY ???? 

szOID\_KEY\_USAGE\_RESTRICTION - CERT\_KEY\_USAGE\_RESTRICTION\_INFO


## PyCERT\_KEY\_ATTRIBUTES\_INFO Object

Dict representing a CERT\_KEY\_ATTRIBUTES\_INFO struct

#### Properties

  - str KeyId

    Usually a hash that uniquely identifies the key

  - [PyCRYPT\_BIT\_BLOB](PyCRYPT.md#pycryptbit_blob) IntendedKeyUsage

    Contains a byte with CERT\_\*\_KEY\_USAGE flags

  - dict PrivateKeyUsagePeriod

    Private key's begin and end effective dates, may be None


## PyCERT\_NAME\_INFO Object

Sequence of CERT\_RDN's


## PyCERT\_NAME\_VALUE Object

Dict containing type \(CERT\_RDN\_\*\) and a unicode string


## PyCERT\_OTHER\_NAME Object

Dict containing \{ObjId, Value\}\. 

ObjId is one of the string object id's identifying the type of name\. 

Value is a binary string containing an encoded CERT\_NAME\_VALUE that can be decoded 

using X509\_UNICODE\_NAME\_VALUE to return the actual unicode string


## PyCERT\_POLICY\_INFO Object

Dict containing a certificate policy

#### Properties

  - str PolicyIdentifier

    OID identifying the policy

  - tuple PolicyQualifier

    Sequence of CERT\_POLICY\_QUALIFIER dicts


## PyCERT\_PUBLIC\_KEY\_INFO Object

Dict containing an exported public key

#### Properties

  - [PyCRYPT\_ALGORITHM\_IDENTIFIER](PyCRYPT.md#pycryptalgorithm_identifier) Algorithm

    Dict containing OID of the public key algorithm

  - [PyCRYPT\_BIT\_BLOB](PyCRYPT.md#pycryptbit_blob) PublicKey

    Dict containing the encoded public key