# TYPEATTR

## TYPEATTR Object

A TYPEATTR object represents a COM TYPEATTR structure.

#### Properties

  -  __[PyIID](#pyiid)iid__ 
    The IID

  -  __int lcid__ 
    The lcid

  -  __int memidConstructor__ 
    ID of constructor

  -  __int memidDestructor__ 
    ID of destructor

  -  __int cbSizeInstance__ 
    The size of an instance of this type

  -  __int typekind__ 
    The kind of type this information describes.  One of the win32con.TKIND_* constants.

  -  __int cFuncs__ 
    Number of functions.

  -  __int cVars__ 
    Number of variables/data members.

  -  __int cImplTypes__ 
    Number of implemented interfaces.

  -  __int cbSizeVft__ 
    The size of this type's VTBL

  -  __int cbAlignment__ 
    Byte alignment for an instance of this type.

  -  __int wTypeFlags__ 
    One of the pythoncom TYPEFLAG_

  -  __int wMajorVerNum__ 
    Major version number.

  -  __int wMinorVerNum__ 
    Minor version number.

  -  __[TYPEDESC](#typedesc)tdescAlias__ 
    If TypeKind == pythoncom.TKIND_ALIAS, specifies the type for which this type is an alias.

  -  __[IDLDESC](#idldesc)idldeskType__ 
    IDL attributes of the described type.

#### Items


  - [0] *[PyIID](#pyiid)* : IID

    The IID

  - [1] *int* : lcid

    The lcid

  - [2] *int* : memidConstructor

    ID of constructor

  - [3] *int* : memidDestructor

    ID of destructor,

  - [4] *int* : cbSizeInstance

    The size of an instance of this type

  - [5] *int* : typekind

    The kind of type this information describes.  One of the win32con.TKIND_* constants.

  - [6] *int* : cFuncs

    Number of functions.

  - [7] *int* : cVars

    Number of variables/data members.

  - [8] *int* : cImplTypes

    Number of implemented interfaces.

  - [9] *int* : cbSizeVft

    The size of this type's VTBL

  - [10] *int* : cbAlignment

    Byte alignment for an instance of this type.

  - [11] *int* : wTypeFlags

    One of the pythoncom TYPEFLAG_* constants

  - [12] *int* : wMajorVerNum

    Major version number.

  - [13] *int* : wMinorVerNum

    Minor version number.

  - [14] *[TYPEDESC](#typedesc)* : obDescAlias

    If TypeKind == pythoncom.TKIND_ALIAS, specifies the type for which this type is an alias.

  - [15] *[IDLDESC](#idldesc)* : obIDLDesc

    IDL attributes of the described type.