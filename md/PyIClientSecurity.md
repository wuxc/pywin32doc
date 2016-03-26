# PyIClientSecurity

## PyIClientSecurity Object

Description of the interface

#### Methods


  - [QueryBlanket](PyIClientSecurity.md#pyiclientsecurityqueryblanket)

    Retrieves the authentication settings for an interface&nbsp;

  - [SetBlanket](PyIClientSecurity.md#pyiclientsecuritysetblanket)

    Changes the authentication options used with an interface&nbsp;

  - [CopyProxy](PyIClientSecurity.md#pyiclientsecuritycopyproxy)

    Makes a private copy of a proxy interface&nbsp;

## [PyIClientSecurity](#pyiclientsecurity)\.CopyProxy

[PyIUnknown](#pyiunknown)\= **CopyProxy\( *Proxy* ** \)
Makes a private copy of a proxy interface

#### Parameters


  -  *Proxy* :[PyIUnknown](#pyiunknown)

    The remote interface to be copied

## [PyIClientSecurity](#pyiclientsecurity)\.QueryBlanket

dict \= **QueryBlanket\( *Proxy* ** \)
Retrieves the authentication settings for an interface

#### Parameters


  -  *Proxy* :[PyIUnknown](#pyiunknown)

    An interface created through a proxy

## [PyIClientSecurity](#pyiclientsecurity)\.SetBlanket

 **SetBlanket\( *Proxy*  *, AuthnSvc*  *, AuthzSvc*  *, ServerPrincipalName*  *, AuthnLevel*  *, ImpLevel*  *, AuthInfo*  *, Capabilities* ** \)
Changes the authentication options used with an interface

#### Parameters


  -  *Proxy* :[PyIUnknown](#pyiunknown)

    The proxy interface for which to set security options

  -  *AuthnSvc* : int

    Authentication service identifier, pythoncom\.RPC\_C\_AUTHN\_\* \(but not RPC\_C\_AUTHN\_LEVEL\_\*\)

  -  *AuthzSvc* : int

    Authorization service identifier, pythoncom\.RPC\_C\_AUTHZ\_\*

  -  *ServerPrincipalName* :[PyUnicode](#pyunicode)

    SPN that identifies the server, can be None

  -  *AuthnLevel* : int

    Authentication level, pythoncom\.RPC\_C\_AUTHN\_LEVEL\_\*

  -  *ImpLevel* : int

    Impersonation level, pythoncom\.RPC\_C\_IMP\_LEVEL\_\*

  -  *AuthInfo* : None

    Not supported yet, use only None

  -  *Capabilities* : int

    Combination of pythoncom\.EOAC\_\* flags\.  Must be a subset of the 

capabilities of the specified authentication service\.