# PyNET

## PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG Object

A dictionary or tuple passed as input to[win32net::NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

#### Parameters


  -  *InputPersistedFields=None* : __NET_VALIDATE_PERSISTED_FIELDS__ 

    

  -  *PasswordMatched=0* : int

    

## PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG Object

A dictionary or tuple passed as input to[win32net::NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

#### Parameters


  -  *InputPersistedFields=None* : __NET_VALIDATE_PERSISTED_FIELDS__ 

    

  -  *ClearPassword=None* :[PyUnicode](#pyunicode)

    

  -  *UserAccountName=None* :[PyUnicode](#pyunicode)

    

  -  *HashedPassword=None* : buffer

    A string or anything else holding bytes.

  -  *PasswordMatch=0* : int

    Note MSDN incorrectly documents this member as PasswordMatched

## PyNET_VALIDATE_PERSISTED_FIELDS Object

A dictionary returned by[win32net::NetValidatePasswordPolicy](win32net.md#win32netnetvalidatepasswordpolicy)

#### Comments
Note that these fields will only appear if the PresentFields 

structure element indicates the fields are valid.  Thus, the result 

dictionary may contain none, all, or any combination of these.

#### Parameters


  -  *PasswordLastSet* :[PyTime](#pytime)

    

  -  *BadPasswordTime* :[PyTime](#pytime)

    

  -  *LockoutTime* :[PyTime](#pytime)

    

  -  *BadPasswordCount* : int

    

  -  *PasswordHistoryLength* : int

    

  -  *PasswordHistory* : None/string

    