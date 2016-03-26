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

## [PyIClientSecurity](#pyiclientsecurity).CopyProxy

[PyIUnknown](#pyiunknown)= __CopyProxy( *Proxy* __ )
Makes a private copy of a proxy interface

#### Parameters


  -  *Proxy* :[PyIUnknown](#pyiunknown)

    The remote interface to be copied

## [PyIClientSecurity](#pyiclientsecurity).QueryBlanket

dict = __QueryBlanket( *Proxy* __ )
Retrieves the authentication settings for an interface

#### Parameters


  -  *Proxy* :[PyIUnknown](#pyiunknown)

    An interface created through a proxy

## [PyIClientSecurity](#pyiclientsecurity).SetBlanket

 __SetBlanket( *Proxy*  *, AuthnSvc*  *, AuthzSvc*  *, ServerPrincipalName*  *, AuthnLevel*  *, ImpLevel*  *, AuthInfo*  *, Capabilities* __ )
Changes the authentication options used with an interface

#### Parameters


  -  *Proxy* :[PyIUnknown](#pyiunknown)

    The proxy interface for which to set security options

  -  *AuthnSvc* : int

    Authentication service identifier, pythoncom.RPC_C_AUTHN_* (but not RPC_C_AUTHN_LEVEL_*)

  -  *AuthzSvc* : int

    Authorization service identifier, pythoncom.RPC_C_AUTHZ_*

  -  *ServerPrincipalName* :[PyUnicode](#pyunicode)

    SPN that identifies the server, can be None

  -  *AuthnLevel* : int

    Authentication level, pythoncom.RPC_C_AUTHN_LEVEL_*

  -  *ImpLevel* : int

    Impersonation level, pythoncom.RPC_C_IMP_LEVEL_*

  -  *AuthInfo* : None

    Not supported yet, use only None

  -  *Capabilities* : int

    Combination of pythoncom.EOAC_* flags.  Must be a subset of the 

capabilities of the specified authentication service.