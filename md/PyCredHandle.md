# PyCredHandle

## PyCredHandle Object



Handle to a set of logon credentials, used with sspi authentication functions

#### Comments


This object is usually created using[win32security::AcquireCredentialsHandle](win32security.md#win32securityacquirecredentialshandle)\. 

An uninitialized handle can also be created using win32security\.PyCredHandleType\(\)

#### Methods


  - [Detach](PyCredHandle.md#pycredhandledetach)

    Disassociates object from handle and returns integer value of handle \(prevents automatic freeing of credentials when object is deallocated\),&nbsp;

  - [FreeCredentialsHandle](PyCredHandle.md#pycredhandlefreecredentialshandle)

    Releases the credentials handle&nbsp;

  - [QueryCredentialsAttributes](PyCredHandle.md#pycredhandlequerycredentialsattributes)

    Returns information about the credentials&nbsp;

## [PyCredHandle](#pycredhandle)\.Detach



long =Detach\(\)
Disassociates object from handle and returns integer value of handle,

## [PyCredHandle](#pycredhandle)\.FreeCredentialsHandle

FreeCredentialsHandle\(\)
Releases the credentials handle and makes object unusable

## [PyCredHandle](#pycredhandle)\.QueryCredentialsAttributes

QueryCredentialsAttributes\(Attribute\)
Returns information about the credentials

#### Parameters


  - Attribute : int

    SECPKG\_\* constant specifying which type of information to return

#### Comments


Only SECPKG\_CRED\_ATTR\_NAMES currently supported

AttributeReturn typeSECPKG\_CRED\_ATTR\_NAMES[PyUnicode](#pyunicode) - returns username that credentials representSECPKG\_ATTR\_SUPPORTED\_ALGSNot supported yet 

SecPkgCred\_SupportedAlgs:SECPKG\_ATTR\_CIPHER\_STRENGTHSNot supported yet 

SecPkgCred\_CipherStrengths:SECPKG\_ATTR\_SUPPORTED\_PROTOCOLSNot supported yet 

SecPkgCred\_SupportedProtocols:
#### Return Value
Type of returned values is dependent on Attribute