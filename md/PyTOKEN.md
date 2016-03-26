# PyTOKEN

## PyTOKEN\_GROUPS Object



A sequence of[PySID\_AND\_ATTRIBUTES](PySID.md#pysidand_attributes) sequences, eg \[\([PySID](#pysid),int\),\.\.\.\] representing a TOKEN\_GROUPS structure

## PyTOKEN\_PRIVILEGES Object



An object representing Win32 token privileges\.

#### Comments


This is a sequence \(eg, list\) of \(\(id, attributes\),\.\.\.\) where id is a 

privilege LUID as returned by[win32security::LookupPrivilegeValue](win32security.md#win32securitylookupprivilegevalue) and 

attributes is a combination of SE\_PRIVILEGE\_ENABLED, SE\_PRIVILEGE\_ENABLED\_BY\_DEFAULT, 

and SE\_PRIVILEGE\_USED\_FOR\_ACCESS