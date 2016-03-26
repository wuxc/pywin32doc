# PyITypeLib

## PyITypeLib Object

An object that implements the ITypeLib interface.

#### Methods


  - [GetDocumentation](PyITypeLib.md#pyitypelibgetdocumentation)

    Retrieves documentation information about the library.&nbsp;

  - [GetLibAttr](PyITypeLib.md#pyitypelibgetlibattr)

    Retrieves the libraries attributes&nbsp;

  - [GetTypeComp](PyITypeLib.md#pyitypelibgettypecomp)

    Retrieves a __ITypeComp__ object for Name to VARDESC/FUNCDESC mapping.&nbsp;

  - [GetTypeInfo](PyITypeLib.md#pyitypelibgettypeinfo)

    Retrieves the specified type description in the library.&nbsp;

  - [GetTypeInfoCount](PyITypeLib.md#pyitypelibgettypeinfocount)

    Retrieves the number of[PyITypeInfo](#pyitypeinfo)s in the type library.&nbsp;

  - [GetTypeInfoOfGuid](PyITypeLib.md#pyitypelibgettypeinfoofguid)

    Retrieves the type info of the specified GUID.&nbsp;

  - [GetTypeInfoType](PyITypeLib.md#pyitypelibgettypeinfotype)

    Retrieves the type of a type description. 

sentinel&nbsp;


## [PyITypeLib](#pyitypelib).GetDocumentation

tuple = __GetDocumentation( *index* __ )
Retrieves documentation information about the library.

#### Parameters


  -  *index* : int

    The index of the type description within the library

#### Return Value
The return type is a tuple of (name of item, documentation string, help context integer, help file name)

## [PyITypeLib](#pyitypelib).GetLibAttr

[TLIBATTR](#tlibattr)= __GetLibAttr(__ )
Retrieves the libraries attributes

## [PyITypeLib](#pyitypelib).GetTypeComp

[PyITypeComp](#pyitypecomp)= __GetTypeComp(__ )
Retrieves a __ITypeComp__ object for Name to VARDESC/FUNCDESC mapping.

## [PyITypeLib](#pyitypelib).GetTypeInfo

[PyITypeInfo](#pyitypeinfo)= __GetTypeInfo( *index* __ )
Retrieves the specified type description in the library.

#### Parameters


  -  *index* : int

    The index of the type description within the library

## [PyITypeLib](#pyitypelib).GetTypeInfoCount

int = __GetTypeInfoCount(__ )
Retrieves the number of[PyITypeInfo](#pyitypeinfo)s in the type library.

## [PyITypeLib](#pyitypelib).GetTypeInfoOfGuid

[PyITypeInfo](#pyitypeinfo)= __GetTypeInfoOfGuid( *iid* __ )
Retrieves the type info of the specified GUID.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    GUID of the type description.

## [PyITypeLib](#pyitypelib).GetTypeInfoType

 __TYPEKIND__ = __GetTypeInfoType( *index* __ )
Retrieves the type of a type description.

#### Parameters


  -  *index* : int

    The index of the type description within the library