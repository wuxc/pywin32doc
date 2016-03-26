# TYPEATTR

## TYPEATTR Object

A TYPEATTR object represents a COM TYPEATTR structure\.

#### Properties

  -  **[PyIID](#pyiid)iid** 
    The IID

  -  **int lcid** 
    The lcid

  -  **int memidConstructor** 
    ID of constructor

  -  **int memidDestructor** 
    ID of destructor

  -  **int cbSizeInstance** 
    The size of an instance of this type

  -  **int typekind** 
    The kind of type this information describes\.  One of the win32con\.TKIND\_\* constants\.

  -  **int cFuncs** 
    Number of functions\.

  -  **int cVars** 
    Number of variables/data members\.

  -  **int cImplTypes** 
    Number of implemented interfaces\.

  -  **int cbSizeVft** 
    The size of this type's VTBL

  -  **int cbAlignment** 
    Byte alignment for an instance of this type\.

  -  **int wTypeFlags** 
    One of the pythoncom TYPEFLAG\_

  -  **int wMajorVerNum** 
    Major version number\.

  -  **int wMinorVerNum** 
    Minor version number\.

  -  **[TYPEDESC](#typedesc)tdescAlias** 
    If TypeKind \=\= pythoncom\.TKIND\_ALIAS, specifies the type for which this type is an alias\.

  -  **[IDLDESC](#idldesc)idldeskType** 
    IDL attributes of the described type\.

#### Items


  - \[0\] *[PyIID](#pyiid)* : IID

    The IID

  - \[1\] *int* : lcid

    The lcid

  - \[2\] *int* : memidConstructor

    ID of constructor

  - \[3\] *int* : memidDestructor

    ID of destructor,

  - \[4\] *int* : cbSizeInstance

    The size of an instance of this type

  - \[5\] *int* : typekind

    The kind of type this information describes\.  One of the win32con\.TKIND\_\* constants\.

  - \[6\] *int* : cFuncs

    Number of functions\.

  - \[7\] *int* : cVars

    Number of variables/data members\.

  - \[8\] *int* : cImplTypes

    Number of implemented interfaces\.

  - \[9\] *int* : cbSizeVft

    The size of this type's VTBL

  - \[10\] *int* : cbAlignment

    Byte alignment for an instance of this type\.

  - \[11\] *int* : wTypeFlags

    One of the pythoncom TYPEFLAG\_\* constants

  - \[12\] *int* : wMajorVerNum

    Major version number\.

  - \[13\] *int* : wMinorVerNum

    Minor version number\.

  - \[14\] *[TYPEDESC](#typedesc)* : obDescAlias

    If TypeKind \=\= pythoncom\.TKIND\_ALIAS, specifies the type for which this type is an alias\.

  - \[15\] *[IDLDESC](#idldesc)* : obIDLDesc

    IDL attributes of the described type\.