# PyNET


## PyNET\_VALIDATE\_AUTHENTICATION\_INPUT\_ARG Object

A dictionary or tuple passed as input to [win32net::NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

#### Parameters

  - InputPersistedFields=None : NET\_VALIDATE\_PERSISTED\_FIELDS

    

  - PasswordMatched=0 : int

    


## PyNET\_VALIDATE\_PASSWORD\_CHANGE\_INPUT\_ARG Object

A dictionary or tuple passed as input to [win32net::NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

#### Parameters

  - InputPersistedFields=None : NET\_VALIDATE\_PERSISTED\_FIELDS

    

  - ClearPassword=None : [PyUnicode](PyUnicode.md)

    

  - UserAccountName=None : [PyUnicode](PyUnicode.md)

    

  - HashedPassword=None : buffer

    A string or anything else holding bytes\.

  - PasswordMatch=0 : int

    Note MSDN incorrectly documents this member as PasswordMatched


## PyNET\_VALIDATE\_PERSISTED\_FIELDS Object

A dictionary returned by [win32net::NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

#### Comments

Note that these fields will only appear if the PresentFields 

structure element indicates the fields are valid\.  Thus, the result 

dictionary may contain none, all, or any combination of these\.

#### Parameters

  - PasswordLastSet : [PyTime](PyTime.md)

    

  - BadPasswordTime : [PyTime](PyTime.md)

    

  - LockoutTime : [PyTime](PyTime.md)

    

  - BadPasswordCount : int

    

  - PasswordHistoryLength : int

    

  - PasswordHistory : None/string

    