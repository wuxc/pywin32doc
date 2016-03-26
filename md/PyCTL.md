# PyCTL


## PyCTL\_CONTEXT Object

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

  - int HCTL\_CONTEXT

    Raw message handle


## [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)\.CertDeleteCTLFromStore

CertDeleteCTLFromStore\(\)
Removes the CTL from the store that it is contained in


## [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)\.CertEnumCTLContextProperties

\(int,\.\.\.\) = CertEnumCTLContextProperties\(\)
Lists property id's for the context


## [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)\.CertEnumSubjectInSortedCTL

\(\(str,str\),\.\.\.\) = CertEnumSubjectInSortedCTL\(\)
Retrieves trusted subjects contained in CRL

#### Return Value
Returns a sequence of tuples containing two strings \(SubjectIdentifier, EncodedAttributes\)


## [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)\.CertFreeCTLContext

CertFreeCTLContext\(\)
Closes the CTL handle


## [PyCTL\_CONTEXT](PyCTL.md#pyctlcontext)\.CertSerializeCTLStoreElement

string = CertSerializeCTLStoreElement\(Flags\)
Serializes the CTL and its properties

#### Parameters

  - Flags=0 : int

    Reserved, use only 0 if passed in


## PyCTL\_USAGE Object

Sequence of string OIDs \(szOID\_\*\)\.  This struct is identical to CERT\_ENHKEY\_USAGE\.