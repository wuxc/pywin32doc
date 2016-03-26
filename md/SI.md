# SI

## SI_ACCESS Object

Tuple of 4 items representing SI_ACCESS struct

#### Items


  - [0] *[PyIID](#pyiid)* : guid

    GUID identifying the object type permissions apply to. Use GUID_NULL for object itself

  - [1] *int* : mask

    Bitmask of permissions

  - [2] *[PyUNICODE](#pyunicode)* : Name

    Description to be displayed for the permissions

  - [3] *int* : Flags

    Indicates which pages will display the permissions, and how they may be inherited. Combination of 

SI_ACCESS_SPECIFIC, SI_ACCESS_GENERAL, SI_ACCESS_CONTAINER, SI_ACCESS_PROPERTY, 

CONTAINER_INHERIT_ACE, INHERIT_ONLY_ACE, OBJECT_INHERIT_ACE

## SI_INHERIT_TYPE Object

Tuple of 3 items describing a method of inheritance

#### Items


  - [0] *[PyIID](#pyiid)* : guid

    GUID for type of child object, GUID_NULL indicates object itself

  - [1] *int* : Flags

    ACE inheritance flags, combination of OBJECT_INHERIT_ACE, CONTAINER_INHERIT_ACE, INHERIT_ONLY_ACE

  - [2] *[PyUNICODE](#pyunicode)* : Name

    Description that will be displayed on the Advanced page

## SI_OBJECT_INFO Object

Six-tuple representing SI_OBJECT_INFO struct

#### Items


  - [0] *int* : Flags

    Combination of ntsecuritycon.SI_* flags specifying options

  - [1] *[PyHANDLE](#pyhandle)* : hInstance

    Handle to a module containing string resources (not supported yet, use 0)

  - [2] *[PyUNICODE](#pyunicode)* : ServerName

    Name of authenticating server if not local machine

  - [3] *[PyUNICODE](#pyunicode)* : ObjectName

    Name of object whose security will be displayed

  - [4] *[PyUNICODE](#pyunicode)* : PageTitle

    Title to be used for basic propery sheet (SI_PAGE_TITLE must be passed in Flags)

  - [5] *[PyIID](#pyiid)* : ObjectType

    GUID identifying the type of object, usually IID_NULL