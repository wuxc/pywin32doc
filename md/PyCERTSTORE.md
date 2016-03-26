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

    Finds all Certificate Trust Lists in store\.&nbsp;

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

    Exports certificates and associated private keys in PKCS\#12 format&nbsp;

#### Properties

  - int HCERTSTORE

    Integer handle


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertAddCTLContextToStore

[PyCTL\_CONTEXT](PyCTL.md#pyctlcontext) = CertAddCTLContextToStore\(CtlContext, AddDisposition

\)
Adds a certificate trust list to the store

#### Parameters

  - CtlContext : [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)

    CTL to be added

  - AddDisposition : int

    CERT\_STORE\_ADD\_\* constant


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertAddCTLLinkToStore

[PyCTL\_CONTEXT](PyCTL.md#pyctlcontext) = CertAddCTLLinkToStore\(CtlContext, AddDisposition

\)
Adds a link to a CTL in another store

#### Parameters

  - CtlContext : [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)

    CTL to be linked

  - AddDisposition : int

    One of the CERT\_STORE\_ADD\_\* values


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertAddCertificateContextToStore

[PyCERT\_CONTEXT](PyCERT.md#pycertcontext) = CertAddCertificateContextToStore\(CertContext, AddDisposition

\)
Adds a certificate context to the store

#### Parameters

  - CertContext : [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)

    Certificate context to be added

  - AddDisposition : int

    CERT\_STORE\_ADD\_\* constant


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertAddCertificateLinkToStore

[PyCERT\_CONTEXT](PyCERT.md#pycertcontext) = CertAddCertificateLinkToStore\(CertContext, AddDisposition

\)
Adds a link to a cert in another store

#### Parameters

  - CertContext : [PyCERT\_CONTEXT](PyCERT.md#pycertcontext)

    Certificate context to be linked

  - AddDisposition : int

    One of the CERT\_STORE\_ADD\_\* values


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertAddEncodedCertificateToStore

[PyCERT\_CONTEXT](PyCERT.md#pycertcontext) = CertAddEncodedCertificateToStore\(CertEncodingType, CertEncoded

, AddDisposition

\)
Imports an encoded certificate into the store

#### Parameters

  - CertEncodingType : int

    Usually X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

  - CertEncoded : buffer

    Data containing a serialized certificate

  - AddDisposition : int

    Combination of CERT\_STORE\_ADD\_\* flags


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertAddStoreToCollection

CertAddStoreToCollection\(SiblingStore, UpdateFlag, Priority\)
Adds a sibling store to a store collection

#### Parameters

  - SiblingStore : [PyCERTSTORE](PyCERTSTORE.md#pycertstore)

    Store to be added to the collection

  - UpdateFlag=0 : int

    Can be CERT\_PHYSICAL\_STORE\_ADD\_ENABLE\_FLAG to enable changes to persist

  - Priority=0 : int

    Determines order in which store are searched and updated

#### Comments

A collection store is created by using cryptoapi::CertOpenStore

 with CERT\_STORE\_PROV\_COLLECTION


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertCloseStore

CertCloseStore\(Flags\)
Closes the certificate store

#### Parameters

  - Flags=0 : int

    Combination of CERT\_CLOSE\_\*\_FLAG flags


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertControlStore

CertControlStore\(Flags, CtrlType, CtrlPara\)
Controls sychronization of the certificate store

#### Parameters

  - Flags : int

    One of the CERT\_STORE\_CTRL\_\*\_FLAG flags

  - CtrlType : int

    One of the CERT\_STORE\_CTRL\_\* flags

  - CtrlPara : [PyHANDLE](PyHANDLE.md)

    Event handle, can be None \(not used with CERT\_STORE\_CTRL\_COMMIT\)


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertEnumCTLsInStore

\[[PyCTL\_CONTEXT](PyCTL.md#pyctlcontext),\.\.\.\] = CertEnumCTLsInStore\(\)
Finds all Certificate Trust Lists in store


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertEnumCertificatesInStore

\[[PyCERT\_CONTEXT](PyCERT.md#pycertcontext),\.\.\.\] = CertEnumCertificatesInStore\(\)
Lists all certificates in the store


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertRemoveStoreFromCollection

CertRemoveStoreFromCollection\(SiblingStore\)
Removes a sibling store from a collection

#### Parameters

  - SiblingStore : [PyCERTSTORE](PyCERTSTORE.md#pycertstore)

    Store to be removed from the collection


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.CertSaveStore

CertSaveStore\(MsgAndCertEncodingType, SaveAs, SaveTo, SaveToPara, Flags\)
Serializes the store to memory or a file

#### Parameters

  - MsgAndCertEncodingType : int

    Only used when saveas is CERT\_STORE\_SAVE\_AS\_PKCS7 - usually X509\_ASN\_ENCODING combined with PKCS\_7\_ASN\_ENCODING

  - SaveAs : int

    One of the CERT\_STORE\_SAVE\_AS\_\* constants

  - SaveTo : int

    One of the CERT\_STORE\_SAVE\_TO\_\* constants \(CERT\_STORE\_SAVE\_TO\_MEMORY not supported yet\)

  - SaveToPara : [PyHANDLE](PyHANDLE.md)/string

    File name or open file handle depending on SaveTo parm

  - Flags=0 : int

    Reserved, use 0


## [PyCERTSTORE](PyCERTSTORE.md#pycertstore)\.PFXExportCertStoreEx

bytes = PFXExportCertStoreEx\(Password, Flags

\)
Exports certificates and associated private keys in PKCS\#12 format

#### Parameters

  - Password=None : str

    Passphrase to be used to encrypt the output

  - Flags=EXPORT\_PRIVATE\_KEYS|REPORT\_NO\_PRIVATE\_KEY|REPORT\_NOT\_ABLE\_TO\_EXPORT\_PRIVATE\_KEY : int

    Options to be used while exporting