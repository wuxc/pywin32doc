# PyLsaLogon


## PyLsaLogon\_HANDLE Object

Lsa handle used to access authentication packages, returned by 

[win32security::LsaRegisterLogonProcess](win32security.md#win32securitylsaregisterlogonprocess) or [win32security::LsaConnectUntrusted](win32security.md#win32securitylsaconnectuntrusted)\. Base low-level object is a plain HANDLE\. 

Inherits all properties and methods of [PyHANDLE](PyHANDLE.md), but Close uses LsaDeregisterLogonProcess