# PyCTL

## PyCTL_CONTEXT Object

Object containing a Certificate Trust List

#### Methods


  - [CertFreeCTLContext](PyCTL.md#pyctlcontext_certfreectlcontext)

    Closes the context handle&nbsp;

  - [CertEnumCTLContextProperties](PyCTL.md#pyctlcontext_certenumctlcontextproperties)

    Lists property id's for the context&nbsp;

  - [CertEnumSubjectInSortedCTL](PyCTL.md#pyctlcontext_certenumsubjectinsortedctl)

    Retrieves trusted subjects contained in CTL&nbsp;

  - [CertDeleteCTLFromStore](PyCTL.md#pyctlcontext_certdeletectlfromstore)

    Removes the CTL from the store that it is contained in&nbsp;

  - [CertSerializeCTLStoreElement](PyCTL.md#pyctlcontext_certserializectlstoreelement)

    Serializes the CTL and its properties&nbsp;

#### Properties

  -  __int HCTL_CONTEXT__ 
    Raw message handle

## [PyCTL_CONTEXT](PyCTL.md#pyctlcontext).CertDeleteCTLFromStore

 __CertDeleteCTLFromStore(__ )
Removes the CTL from the store that it is contained in

## [PyCTL_CONTEXT](PyCTL.md#pyctlcontext).CertEnumCTLContextProperties

(int,...) = __CertEnumCTLContextProperties(__ )
Lists property id's for the context

## [PyCTL_CONTEXT](PyCTL.md#pyctlcontext).CertEnumSubjectInSortedCTL

((str,str),...) = __CertEnumSubjectInSortedCTL(__ )
Retrieves trusted subjects contained in CRL

#### Return Value
Returns a sequence of tuples containing two strings (SubjectIdentifier, EncodedAttributes)

## [PyCTL_CONTEXT](PyCTL.md#pyctlcontext).CertFreeCTLContext

 __CertFreeCTLContext(__ )
Closes the CTL handle

## [PyCTL_CONTEXT](PyCTL.md#pyctlcontext).CertSerializeCTLStoreElement

string = __CertSerializeCTLStoreElement( *Flags* __ )
Serializes the CTL and its properties

#### Parameters


  -  *Flags=0* : int

    Reserved, use only 0 if passed in

## PyCTL_USAGE Object

Sequence of string OIDs (szOID_*).  This struct is identical to CERT_ENHKEY_USAGE.