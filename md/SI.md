# SI

## SI\_ACCESS Object

Tuple of 4 items representing SI\_ACCESS struct

#### Items


  - \[0\] *[PyIID](#pyiid)* : guid

    GUID identifying the object type permissions apply to\. Use GUID\_NULL for object itself

  - \[1\] *int* : mask

    Bitmask of permissions

  - \[2\] *[PyUNICODE](#pyunicode)* : Name

    Description to be displayed for the permissions

  - \[3\] *int* : Flags

    Indicates which pages will display the permissions, and how they may be inherited\. Combination of 

SI\_ACCESS\_SPECIFIC, SI\_ACCESS\_GENERAL, SI\_ACCESS\_CONTAINER, SI\_ACCESS\_PROPERTY, 

CONTAINER\_INHERIT\_ACE, INHERIT\_ONLY\_ACE, OBJECT\_INHERIT\_ACE

## SI\_INHERIT\_TYPE Object

Tuple of 3 items describing a method of inheritance

#### Items


  - \[0\] *[PyIID](#pyiid)* : guid

    GUID for type of child object, GUID\_NULL indicates object itself

  - \[1\] *int* : Flags

    ACE inheritance flags, combination of OBJECT\_INHERIT\_ACE, CONTAINER\_INHERIT\_ACE, INHERIT\_ONLY\_ACE

  - \[2\] *[PyUNICODE](#pyunicode)* : Name

    Description that will be displayed on the Advanced page

## SI\_OBJECT\_INFO Object

Six-tuple representing SI\_OBJECT\_INFO struct

#### Items


  - \[0\] *int* : Flags

    Combination of ntsecuritycon\.SI\_\* flags specifying options

  - \[1\] *[PyHANDLE](#pyhandle)* : hInstance

    Handle to a module containing string resources \(not supported yet, use 0\)

  - \[2\] *[PyUNICODE](#pyunicode)* : ServerName

    Name of authenticating server if not local machine

  - \[3\] *[PyUNICODE](#pyunicode)* : ObjectName

    Name of object whose security will be displayed

  - \[4\] *[PyUNICODE](#pyunicode)* : PageTitle

    Title to be used for basic propery sheet \(SI\_PAGE\_TITLE must be passed in Flags\)

  - \[5\] *[PyIID](#pyiid)* : ObjectType

    GUID identifying the type of object, usually IID\_NULL