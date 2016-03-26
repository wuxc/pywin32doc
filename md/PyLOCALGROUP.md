# PyLOCALGROUP

## PyLOCALGROUP_INFO_* Object

The following LOCALGROUP_INFO levels are supported.


## PyLOCALGROUP_INFO_0 Object

A dictionary holding the information in a Win32 LOCALGROUP_INFO_0 structure.

#### Properties

  -  __string/[PyUnicode](#pyunicode)name__ 
    Name of the group

## PyLOCALGROUP_INFO_1 Object

A dictionary holding the information in a Win32 LOCALGROUP_INFO_1 structure.

#### Properties

  -  __string/[PyUnicode](#pyunicode)name__ 
    Name of the group

  -  __string/[PyUnicode](#pyunicode)comment__ 
    The group's comment.

## PyLOCALGROUP_INFO_1002 Object

A dictionary holding the information in a Win32 LOCALGROUP_INFO_1002 structure.

#### Properties

  -  __string/[PyUnicode](#pyunicode)comment__ 
    

## PyLOCALGROUP_MEMBERS_INFO_* Object

The following LOCALGROUP_MEMBER_INFO levels are supported.


## PyLOCALGROUP_MEMBERS_INFO_0 Object

A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_0 structure.

#### Properties

  -  __[PySID](#pysid)sid__ 
    

## PyLOCALGROUP_MEMBERS_INFO_1 Object

A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_1 structure.

#### Properties

  -  __[PySID](#pysid)sid__ 
    

  -  __int sidusage__ 
    

  -  __string/[PyUnicode](#pyunicode)name__ 
    

## PyLOCALGROUP_MEMBERS_INFO_2 Object

A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_2 structure.

#### Properties

  -  __[PySID](#pysid)sid__ 
    

  -  __int sidusage__ 
    

  -  __string/[PyUnicode](#pyunicode)domainandname__ 
    string containing the name of the member prefixed by the domain name and the "\\" separator character

## PyLOCALGROUP_MEMBERS_INFO_3 Object

A dictionary holding the information in a Win32 LOCALGROUP_MEMBERS_INFO_3 structure.

#### Properties

  -  __string/[PyUnicode](#pyunicode)domainandname__ 
    string containing the name of the member prefixed by the domain name and the "\\" separator character