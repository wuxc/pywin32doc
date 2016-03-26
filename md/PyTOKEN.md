# PyTOKEN

## PyTOKEN_GROUPS Object

A sequence of[PySID_AND_ATTRIBUTES](PySID.md#pysidand_attributes)sequences, eg [([PySID](#pysid),int),...] representing a TOKEN_GROUPS structure

## PyTOKEN_PRIVILEGES Object

An object representing Win32 token privileges.

#### Comments
This is a sequence (eg, list) of ((id, attributes),...) where id is a 

privilege LUID as returned by[win32security::LookupPrivilegeValue](win32security.md#win32securitylookupprivilegevalue)and 

attributes is a combination of SE_PRIVILEGE_ENABLED, SE_PRIVILEGE_ENABLED_BY_DEFAULT, 

and SE_PRIVILEGE_USED_FOR_ACCESS