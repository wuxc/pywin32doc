# PyCERTSTORE

## PyCERTSTORE Object

Handle to a certificate store

#### Methods


  - [CertCloseStore](PyCERTSTORE.md#pycertstorecertclosestore)

    Closes the certificate store&nbsp;

  - [CertControlStore](PyCERTSTORE.md#pycertstorecertcontrolstore)

    Controls sychronization of the certificate store&nbsp;

  - [CertEnumCertificatesInStore](PyCERTSTORE.md#pycertstorecertenumcertificatesinstore)

    Lists all certificates in the store&nbsp;

  - [CertEnumCTLsInStore](PyCERTSTORE.md#pycertstorecertenumctlsinstore)

    Finds all Certificate Trust Lists in store.&nbsp;

  - [CertSaveStore](PyCERTSTORE.md#pycertstorecertsavestore)

    Serializes the store to memory or a file&nbsp;

  - [CertAddEncodedCertificateToStore](PyCERTSTORE.md#pycertstorecertaddencodedcertificatetostore)

    Imports an encoded certificate into the store&nbsp;

  - [CertAddCertificateContextToStore](PyCERTSTORE.md#pycertstorecertaddcertificatecontexttostore)

    Adds a certificate context to the store&nbsp;

  - [CertAddCertificateLinkToStore](PyCERTSTORE.md#pycertstorecertaddcertificatelinktostore)

    Adds a link to a cert in another store&nbsp;

  - [CertAddCTLContextToStore](PyCERTSTORE.md#pycertstorecertaddctlcontexttostore)

    Adds a certificate trust list to the store&nbsp;

  - [CertAddCTLLinkToStore](PyCERTSTORE.md#pycertstorecertaddctllinktostore)

    Adds a link to a CTL in another store&nbsp;

  - [CertAddStoreToCollection](PyCERTSTORE.md#pycertstorecertaddstoretocollection)

    Adds a sibling store to a store collection&nbsp;

  - [CertRemoveStoreFromCollection](PyCERTSTORE.md#pycertstorecertremovestorefromcollection)

    Removes a sibling store from a store collection&nbsp;

  - [PFXExportCertStoreEx](PyCERTSTORE.md#pycertstorepfxexportcertstoreex)

    Exports certificates and associated private keys in PKCS#12 format&nbsp;

#### Properties

  -  __int HCERTSTORE__ 
    Integer handle

## [PyCERTSTORE](#pycertstore).CertAddCTLContextToStore

[PyCTL_CONTEXT](PyCTL.md#pyctlcontext)= __CertAddCTLContextToStore( *CtlContext*  *, AddDisposition* __ )
Adds a certificate trust list to the store

#### Parameters


  -  *CtlContext* :[PyCTL_CONTEXT](PyCTL.md#pyctlcontext)

    CTL to be added

  -  *AddDisposition* : int

    CERT_STORE_ADD_* constant

## [PyCERTSTORE](#pycertstore).CertAddCTLLinkToStore

[PyCTL_CONTEXT](PyCTL.md#pyctlcontext)= __CertAddCTLLinkToStore( *CtlContext*  *, AddDisposition* __ )
Adds a link to a CTL in another store

#### Parameters


  -  *CtlContext* :[PyCTL_CONTEXT](PyCTL.md#pyctlcontext)

    CTL to be linked

  -  *AddDisposition* : int

    One of the CERT_STORE_ADD_* values

## [PyCERTSTORE](#pycertstore).CertAddCertificateContextToStore

[PyCERT_CONTEXT](PyCERT.md#pycertcontext)= __CertAddCertificateContextToStore( *CertContext*  *, AddDisposition* __ )
Adds a certificate context to the store

#### Parameters


  -  *CertContext* :[PyCERT_CONTEXT](PyCERT.md#pycertcontext)

    Certificate context to be added

  -  *AddDisposition* : int

    CERT_STORE_ADD_* constant

## [PyCERTSTORE](#pycertstore).CertAddCertificateLinkToStore

[PyCERT_CONTEXT](PyCERT.md#pycertcontext)= __CertAddCertificateLinkToStore( *CertContext*  *, AddDisposition* __ )
Adds a link to a cert in another store

#### Parameters


  -  *CertContext* :[PyCERT_CONTEXT](PyCERT.md#pycertcontext)

    Certificate context to be linked

  -  *AddDisposition* : int

    One of the CERT_STORE_ADD_* values

## [PyCERTSTORE](#pycertstore).CertAddEncodedCertificateToStore

[PyCERT_CONTEXT](PyCERT.md#pycertcontext)= __CertAddEncodedCertificateToStore( *CertEncodingType*  *, CertEncoded*  *, AddDisposition* __ )
Imports an encoded certificate into the store

#### Parameters


  -  *CertEncodingType* : int

    Usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

  -  *CertEncoded* : buffer

    Data containing a serialized certificate

  -  *AddDisposition* : int

    Combination of CERT_STORE_ADD_* flags

## [PyCERTSTORE](#pycertstore).CertAddStoreToCollection

 __CertAddStoreToCollection( *SiblingStore*  *, UpdateFlag*  *, Priority* __ )
Adds a sibling store to a store collection

#### Parameters


  -  *SiblingStore* :[PyCERTSTORE](#pycertstore)

    Store to be added to the collection

  -  *UpdateFlag=0* : int

    Can be CERT_PHYSICAL_STORE_ADD_ENABLE_FLAG to enable changes to persist

  -  *Priority=0* : int

    Determines order in which store are searched and updated

#### Comments
A collection store is created by using __cryptoapi::CertOpenStore__ with CERT_STORE_PROV_COLLECTION

## [PyCERTSTORE](#pycertstore).CertCloseStore

 __CertCloseStore( *Flags* __ )
Closes the certificate store

#### Parameters


  -  *Flags=0* : int

    Combination of CERT_CLOSE_*_FLAG flags

## [PyCERTSTORE](#pycertstore).CertControlStore

 __CertControlStore( *Flags*  *, CtrlType*  *, CtrlPara* __ )
Controls sychronization of the certificate store

#### Parameters


  -  *Flags* : int

    One of the CERT_STORE_CTRL_*_FLAG flags

  -  *CtrlType* : int

    One of the CERT_STORE_CTRL_* flags

  -  *CtrlPara* :[PyHANDLE](#pyhandle)

    Event handle, can be None (not used with CERT_STORE_CTRL_COMMIT)

## [PyCERTSTORE](#pycertstore).CertEnumCTLsInStore

[[PyCTL_CONTEXT](PyCTL.md#pyctlcontext),...] = __CertEnumCTLsInStore(__ )
Finds all Certificate Trust Lists in store

## [PyCERTSTORE](#pycertstore).CertEnumCertificatesInStore

[[PyCERT_CONTEXT](PyCERT.md#pycertcontext),...] = __CertEnumCertificatesInStore(__ )
Lists all certificates in the store

## [PyCERTSTORE](#pycertstore).CertRemoveStoreFromCollection

 __CertRemoveStoreFromCollection( *SiblingStore* __ )
Removes a sibling store from a collection

#### Parameters


  -  *SiblingStore* :[PyCERTSTORE](#pycertstore)

    Store to be removed from the collection

## [PyCERTSTORE](#pycertstore).CertSaveStore

 __CertSaveStore( *MsgAndCertEncodingType*  *, SaveAs*  *, SaveTo*  *, SaveToPara*  *, Flags* __ )
Serializes the store to memory or a file

#### Parameters


  -  *MsgAndCertEncodingType* : int

    Only used when saveas is CERT_STORE_SAVE_AS_PKCS7 - usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING

  -  *SaveAs* : int

    One of the CERT_STORE_SAVE_AS_* constants

  -  *SaveTo* : int

    One of the CERT_STORE_SAVE_TO_* constants (CERT_STORE_SAVE_TO_MEMORY not supported yet)

  -  *SaveToPara* :[PyHANDLE](#pyhandle)/string

    File name or open file handle depending on SaveTo parm

  -  *Flags=0* : int

    Reserved, use 0

## [PyCERTSTORE](#pycertstore).PFXExportCertStoreEx

bytes = __PFXExportCertStoreEx( *Password*  *, Flags* __ )
Exports certificates and associated private keys in PKCS#12 format

#### Parameters


  -  *Password=None* : str

    Passphrase to be used to encrypt the output

  -  *Flags=EXPORT_PRIVATE_KEYS|REPORT_NO_PRIVATE_KEY|REPORT_NOT_ABLE_TO_EXPORT_PRIVATE_KEY* : int

    Options to be used while exporting