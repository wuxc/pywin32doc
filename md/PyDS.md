# PyDS

## PyDS\_HANDLE Object



Directory service handle, returned by[win32security::DsBind](win32security.md#win32securitydsbind) 

Subtype of[PyHANDLE](#pyhandle), inherits all properties and methods\.
 

When closed, DsUnBind is called\.

## PyDS\_NAME\_RESULT\_ITEM Object



A tuple representing a DS\_NAME\_RESULT\_ITEM

#### Items


  - \[0\]int : status

    One of ntsecuritycon\.DS\_NAME\_\* error codes

  - \[1\][PyUnicode](#pyunicode) : Domain

    Dns domain that object belongs to

  - \[2\][PyUnicode](#pyunicode) : Name

    Formatted object name