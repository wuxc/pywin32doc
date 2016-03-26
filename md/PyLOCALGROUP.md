# PyLOCALGROUP


## PyLOCALGROUP\_INFO\_\* Object

The following LOCALGROUP\_INFO levels are supported\.




## PyLOCALGROUP\_INFO\_0 Object

A dictionary holding the information in a Win32 LOCALGROUP\_INFO\_0 structure\.

#### Properties

  - string/[PyUnicode](PyUnicode.md) name

    Name of the group


## PyLOCALGROUP\_INFO\_1 Object

A dictionary holding the information in a Win32 LOCALGROUP\_INFO\_1 structure\.

#### Properties

  - string/[PyUnicode](PyUnicode.md) name

    Name of the group

  - string/[PyUnicode](PyUnicode.md) comment

    The group's comment\.


## PyLOCALGROUP\_INFO\_1002 Object

A dictionary holding the information in a Win32 LOCALGROUP\_INFO\_1002 structure\.

#### Properties

  - string/[PyUnicode](PyUnicode.md) comment

    


## PyLOCALGROUP\_MEMBERS\_INFO\_\* Object

The following LOCALGROUP\_MEMBER\_INFO levels are supported\.




## PyLOCALGROUP\_MEMBERS\_INFO\_0 Object

A dictionary holding the information in a Win32 LOCALGROUP\_MEMBERS\_INFO\_0 structure\.

#### Properties

  - [PySID](PySID.md) sid

    


## PyLOCALGROUP\_MEMBERS\_INFO\_1 Object

A dictionary holding the information in a Win32 LOCALGROUP\_MEMBERS\_INFO\_1 structure\.

#### Properties

  - [PySID](PySID.md) sid

    

  - int sidusage

    

  - string/[PyUnicode](PyUnicode.md) name

    


## PyLOCALGROUP\_MEMBERS\_INFO\_2 Object

A dictionary holding the information in a Win32 LOCALGROUP\_MEMBERS\_INFO\_2 structure\.

#### Properties

  - [PySID](PySID.md) sid

    

  - int sidusage

    

  - string/[PyUnicode](PyUnicode.md) domainandname

    string containing the name of the member prefixed by the domain name and the "\\\\" separator character


## PyLOCALGROUP\_MEMBERS\_INFO\_3 Object

A dictionary holding the information in a Win32 LOCALGROUP\_MEMBERS\_INFO\_3 structure\.

#### Properties

  - string/[PyUnicode](PyUnicode.md) domainandname

    string containing the name of the member prefixed by the domain name and the "\\\\" separator character