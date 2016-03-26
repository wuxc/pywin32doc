# PyIServerSecurity


## PyIServerSecurity Object

Interface used to access client security settings and perform impersonation

#### Comments

Can be created using [pythoncom::CoGetCallContext](pythoncom.md#pythoncomcogetcallcontext)

#### Methods

  - [QueryBlanket](PyIServerSecurity.md#pyiserversecurityqueryblanket)

    Retrieves security settings specified by the client&nbsp;

  - [ImpersonateClient](PyIServerSecurity.md#pyiserversecurityimpersonateclient)

    Initiates impersonation of client&nbsp;

  - [RevertToSelf](PyIServerSecurity.md#pyiserversecurityreverttoself)

    Ends impersonation of client&nbsp;

  - [IsImpersonating](PyIServerSecurity.md#pyiserversecurityisimpersonating)

    Determines if server is currently impersonating a client&nbsp;


## [PyIServerSecurity](PyIServerSecurity.md#pyiserversecurity)\.ImpersonateClient

ImpersonateClient\(\)
Initiates impersonation of client


## [PyIServerSecurity](PyIServerSecurity.md#pyiserversecurity)\.IsImpersonating

bool = IsImpersonating\(\)
Determines if server is currently impersonating a client


## [PyIServerSecurity](PyIServerSecurity.md#pyiserversecurity)\.QueryBlanket

dict = QueryBlanket\(Capabilities\)
Retrieves security settings specified by the client

#### Parameters

  - Capabilities=0 : int

    Can be EOAC\_MAKE\_FULLSIC for SChannel provider


## [PyIServerSecurity](PyIServerSecurity.md#pyiserversecurity)\.RevertToSelf

RevertToSelf\(\)
Ends impersonation of client