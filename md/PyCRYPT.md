# PyCRYPT

## PyCRYPT\_ALGORITHM\_IDENTIFIER Object

Dictionary containing information that identifies an encryption 

algorithm and any extra parameters it requires

#### Properties

  -  **str ObjId** 
    An szOID\_\* string identifying the algorithm

  -  **str Parameters** 
    Blob of binary data containing encoded parameters

## PyCRYPT\_ATTRIBUTE Object

Dict representing a CRYPT\_ATTRIBUTE struct

#### Properties

  -  **str ObjId** 
    An szOID\_\* string identifying the attribute

  -  **\(buffer,\.\.\.\) Value** 
    A sequence of buffers containing the attribute values

## PyCRYPT\_BIT\_BLOB Object

Dict containing raw data of a certain bit length

#### Properties

  -  **buffer Data** 
    Binary data

  -  **int UnusedBits** 
    Nbr of bits of last byte that are unused

## PyCRYPT\_DECRYPT\_MESSAGE\_PARA Object

Dict containing message decryption parameters, 

used with **cryptoapi::CryptDecodeMessage** and **cryptoapi::CryptDecryptMessage** 

#### Properties

  -  **\( **PyCERT\_STORE** ,\.\.\.\) CertStores** 
    Sequence of certificate stores to be searched for a certificate 

with a private key that can be used to decrypt the message

  -  **int MsgAndCertEncodingType** 
    Encoding types, optional\. Defaults to X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

  -  **int Flags** 
    Optional\.  CRYPT\_MESSAGE\_SILENT\_KEYSET\_FLAG can be used to suppress any dialogs that might be triggered by 

accessing a key container, such as a request for a PIN\.

## PyCRYPT\_ENCRYPT\_MESSAGE\_PARA Object

Dictionary of encryption parameters used with **cryptoapi::CryptEncryptMessage** 

#### Properties

  -  **[PyCRYPT\_ALGORITHM\_IDENTIFIER](PyCRYPT.md#pycryptalgorithm_identifier)ContentEncryptionAlgorithm** 
    Identifies the algorithm to be used

  -  **[PyCRYPTPROV](#pycryptprov)CryptProv** 
    Optional\. Handle to provider that will perform encryption, can be None for default provider

  -  **object EncryptionAuxInfo** 
    Optional\. Extra info required by some CSP's\.  Not supported yet, use only None

  -  **int Flags** 
    Optional\.  Combination of CRYPT\_MESSAGE\_\*\_FLAG constants

  -  **int InnerContentType** 
    Optional\.  Only used if message to be encrypted is already encoded

  -  **int MsgEncodingType** 
    Optional\.  Defaults to X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

## PyCRYPT\_SIGN\_MESSAGE\_PARA Object

Dict of parms defining how a message will be signed

#### Properties

  -  **[PyCERT\_CONTEXT](PyCERT.md#pycertcontext)SigningCert** 
    Certficate to be used to sign message

  -  **[PyCRYPT\_ALGORITHM\_IDENTIFIER](PyCRYPT.md#pycryptalgorithm_identifier)HashAlgorithm** 
    Algorithm to be used for signed hash

  -  **None HashAuxInfo** 
    Optional\.  Param is reserved, use only None\.

  -  **\([PyCERT\_CONTEXT](PyCERT.md#pycertcontext),\.\.\.\) MsgCert** 
    Optional sequence of certificate to be included in the message\.

  -  **\(CRL\_CONTEXT,\.\.\.\) MsgCrl** 
    Optional\. Sequence of certificate revocation lists\. Not yet supported, use only None\.

  -  **\([PyCRYPT\_ATTRIBUTE](PyCRYPT.md#pycryptattribute),\.\.\.\) AuthAttr** 
    Sequence of canonical attributes to be added to the message

  -  **\([PyCRYPT\_ATTRIBUTE](PyCRYPT.md#pycryptattribute),\.\.\.\) UnauthAttr** 
    Sequence of arbitrary attributes

  -  **int Flags** 
    Optional CRYPT\_MESSAGE\_\*\_FLAG that indicates content type if output is to be further encoded\.

  -  **int InnerContentType** 
    Optional, one of the CMSG\_\* content types if message is already encoded, \.

  -  **int MsgEncodingType** 
    Encoding types, optional\. Defaults to X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

## PyCRYPT\_VERIFY\_MESSAGE\_PARA Object

Dict of verification parameters to be used with **cryptoapi::CryptDecodeMessage** or **cryptoapi::CryptVerifyMessageSignature** \.  All parameters are optional\.  Can be either an empty dict or None 

to use all defaults\.

#### Properties

  -  **int MsgAndCertEncodingType** 
    Encoding types, defaults to X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

  -  **[PyCRYPTPROV](#pycryptprov)CryptProv** 
    CSP to be used to verify signature\. Use None for default provider\.

  -  **function[PyGetSignerCertificate](#pygetsignercertificate)** 
    Callback function that locates signer's certificate\.

  -  **object GetArg** 
    Argument to be passed to above function, can be any object\.