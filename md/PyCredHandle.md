# PyCredHandle

## PyCredHandle Object

Handle to a set of logon credentials, used with sspi authentication functions

#### Comments
This object is usually created using[win32security::AcquireCredentialsHandle](win32security.md#win32securityacquirecredentialshandle). 

An uninitialized handle can also be created using win32security.PyCredHandleType()

#### Methods


  - [Detach](PyCredHandle.md#pycredhandledetach)

    Disassociates object from handle and returns integer value of handle (prevents automatic freeing of credentials when object is deallocated),&nbsp;

  - [FreeCredentialsHandle](PyCredHandle.md#pycredhandlefreecredentialshandle)

    Releases the credentials handle&nbsp;

  - [QueryCredentialsAttributes](PyCredHandle.md#pycredhandlequerycredentialsattributes)

    Returns information about the credentials&nbsp;

## [PyCredHandle](#pycredhandle).Detach

long = __Detach(__ )
Disassociates object from handle and returns integer value of handle,

## [PyCredHandle](#pycredhandle).FreeCredentialsHandle

 __FreeCredentialsHandle(__ )
Releases the credentials handle and makes object unusable

## [PyCredHandle](#pycredhandle).QueryCredentialsAttributes

 __QueryCredentialsAttributes( *Attribute* __ )
Returns information about the credentials

#### Parameters


  -  *Attribute* : int

    SECPKG_* constant specifying which type of information to return

#### Comments
Only SECPKG_CRED_ATTR_NAMES currently supported

 __Attribute__  __Return type__ SECPKG_CRED_ATTR_NAMES[PyUnicode](#pyunicode)- returns username that credentials representSECPKG_ATTR_SUPPORTED_ALGSNot supported yet 

SecPkgCred_SupportedAlgs:SECPKG_ATTR_CIPHER_STRENGTHSNot supported yet 

SecPkgCred_CipherStrengths:SECPKG_ATTR_SUPPORTED_PROTOCOLSNot supported yet 

SecPkgCred_SupportedProtocols:
#### Return Value
Type of returned values is dependent on Attribute