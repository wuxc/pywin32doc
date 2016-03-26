# PyDS

## PyDS_HANDLE Object

Directory service handle, returned by[win32security::DsBind](win32security.md#win32securitydsbind)Subtype of[PyHANDLE](#pyhandle), inherits all properties and methods.
When closed, DsUnBind is called.

## PyDS_NAME_RESULT_ITEM Object

A tuple representing a DS_NAME_RESULT_ITEM

#### Items


  - [0] *int* : status

    One of ntsecuritycon.DS_NAME_* error codes

  - [1] *[PyUnicode](#pyunicode)* : Domain

    Dns domain that object belongs to

  - [2] *[PyUnicode](#pyunicode)* : Name

    Formatted object name