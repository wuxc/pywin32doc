# PyCRYPT

## PyCRYPT_ALGORITHM_IDENTIFIER Object

Dictionary containing information that identifies an encryption 

algorithm and any extra parameters it requires

#### Properties

  -  __str ObjId__ 
    An szOID_* string identifying the algorithm

  -  __str Parameters__ 
    Blob of binary data containing encoded parameters

## PyCRYPT_ATTRIBUTE Object

Dict representing a CRYPT_ATTRIBUTE struct

#### Properties

  -  __str ObjId__ 
    An szOID_* string identifying the attribute

  -  __(buffer,...) Value__ 
    A sequence of buffers containing the attribute values

## PyCRYPT_BIT_BLOB Object

Dict containing raw data of a certain bit length

#### Properties

  -  __buffer Data__ 
    Binary data

  -  __int UnusedBits__ 
    Nbr of bits of last byte that are unused

## PyCRYPT_DECRYPT_MESSAGE_PARA Object

Dict containing message decryption parameters, 

used with __cryptoapi::CryptDecodeMessage__ and __cryptoapi::CryptDecryptMessage__ 

#### Properties

  -  __( __PyCERT_STORE__ ,...) CertStores__ 
    Sequence of certificate stores to be searched for a certificate 

with a private key that can be used to decrypt the message

  -  __int MsgAndCertEncodingType__ 
    Encoding types, optional. Defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

  -  __int Flags__ 
    Optional.  CRYPT_MESSAGE_SILENT_KEYSET_FLAG can be used to suppress any dialogs that might be triggered by 

accessing a key container, such as a request for a PIN.

## PyCRYPT_ENCRYPT_MESSAGE_PARA Object

Dictionary of encryption parameters used with __cryptoapi::CryptEncryptMessage__ 

#### Properties

  -  __[PyCRYPT_ALGORITHM_IDENTIFIER](PyCRYPT.md#pycryptalgorithm_identifier)ContentEncryptionAlgorithm__ 
    Identifies the algorithm to be used

  -  __[PyCRYPTPROV](#pycryptprov)CryptProv__ 
    Optional. Handle to provider that will perform encryption, can be None for default provider

  -  __object EncryptionAuxInfo__ 
    Optional. Extra info required by some CSP's.  Not supported yet, use only None

  -  __int Flags__ 
    Optional.  Combination of CRYPT_MESSAGE_*_FLAG constants

  -  __int InnerContentType__ 
    Optional.  Only used if message to be encrypted is already encoded

  -  __int MsgEncodingType__ 
    Optional.  Defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

## PyCRYPT_SIGN_MESSAGE_PARA Object

Dict of parms defining how a message will be signed

#### Properties

  -  __[PyCERT_CONTEXT](PyCERT.md#pycertcontext)SigningCert__ 
    Certficate to be used to sign message

  -  __[PyCRYPT_ALGORITHM_IDENTIFIER](PyCRYPT.md#pycryptalgorithm_identifier)HashAlgorithm__ 
    Algorithm to be used for signed hash

  -  __None HashAuxInfo__ 
    Optional.  Param is reserved, use only None.

  -  __([PyCERT_CONTEXT](PyCERT.md#pycertcontext),...) MsgCert__ 
    Optional sequence of certificate to be included in the message.

  -  __(CRL_CONTEXT,...) MsgCrl__ 
    Optional. Sequence of certificate revocation lists. Not yet supported, use only None.

  -  __([PyCRYPT_ATTRIBUTE](PyCRYPT.md#pycryptattribute),...) AuthAttr__ 
    Sequence of canonical attributes to be added to the message

  -  __([PyCRYPT_ATTRIBUTE](PyCRYPT.md#pycryptattribute),...) UnauthAttr__ 
    Sequence of arbitrary attributes

  -  __int Flags__ 
    Optional CRYPT_MESSAGE_*_FLAG that indicates content type if output is to be further encoded.

  -  __int InnerContentType__ 
    Optional, one of the CMSG_* content types if message is already encoded, .

  -  __int MsgEncodingType__ 
    Encoding types, optional. Defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

## PyCRYPT_VERIFY_MESSAGE_PARA Object

Dict of verification parameters to be used with __cryptoapi::CryptDecodeMessage__ or __cryptoapi::CryptVerifyMessageSignature__ .  All parameters are optional.  Can be either an empty dict or None 

to use all defaults.

#### Properties

  -  __int MsgAndCertEncodingType__ 
    Encoding types, defaults to X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

  -  __[PyCRYPTPROV](#pycryptprov)CryptProv__ 
    CSP to be used to verify signature. Use None for default provider.

  -  __function[PyGetSignerCertificate](#pygetsignercertificate)__ 
    Callback function that locates signer's certificate.

  -  __object GetArg__ 
    Argument to be passed to above function, can be any object.