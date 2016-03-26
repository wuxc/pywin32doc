# PyITypeLib


## PyITypeLib Object

An object that implements the ITypeLib interface\.

#### Methods

  - [GetDocumentation](PyITypeLib.md#pyitypelibgetdocumentation)

    Retrieves documentation information about the library\.&nbsp;

  - [GetLibAttr](PyITypeLib.md#pyitypelibgetlibattr)

    Retrieves the libraries attributes&nbsp;

  - [GetTypeComp](PyITypeLib.md#pyitypelibgettypecomp)

    Retrieves a ITypeComp

 object for Name to VARDESC/FUNCDESC mapping\.&nbsp;

  - [GetTypeInfo](PyITypeLib.md#pyitypelibgettypeinfo)

    Retrieves the specified type description in the library\.&nbsp;

  - [GetTypeInfoCount](PyITypeLib.md#pyitypelibgettypeinfocount)

    Retrieves the number of [PyITypeInfo](PyITypeInfo.md)s in the type library\.&nbsp;

  - [GetTypeInfoOfGuid](PyITypeLib.md#pyitypelibgettypeinfoofguid)

    Retrieves the type info of the specified GUID\.&nbsp;

  - [GetTypeInfoType](PyITypeLib.md#pyitypelibgettypeinfotype)

    Retrieves the type of a type description\. 

sentinel&nbsp;




## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetDocumentation

tuple = GetDocumentation\(index\)
Retrieves documentation information about the library\.

#### Parameters

  - index : int

    The index of the type description within the library

#### Return Value
The return type is a tuple of \(name of item, documentation string, help context integer, help file name\)


## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetLibAttr

[TLIBATTR](TLIBATTR.md) = GetLibAttr\(\)
Retrieves the libraries attributes


## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetTypeComp

[PyITypeComp](PyITypeComp.md) = GetTypeComp\(\)
Retrieves a ITypeComp

 object for Name to VARDESC/FUNCDESC mapping\.


## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetTypeInfo

[PyITypeInfo](PyITypeInfo.md) = GetTypeInfo\(index\)
Retrieves the specified type description in the library\.

#### Parameters

  - index : int

    The index of the type description within the library


## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetTypeInfoCount

int = GetTypeInfoCount\(\)
Retrieves the number of [PyITypeInfo](PyITypeInfo.md)s in the type library\.


## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetTypeInfoOfGuid

[PyITypeInfo](PyITypeInfo.md) = GetTypeInfoOfGuid\(iid\)
Retrieves the type info of the specified GUID\.

#### Parameters

  - iid : [PyIID](PyIID.md)

    GUID of the type description\.


## [PyITypeLib](PyITypeLib.md#pyitypelib)\.GetTypeInfoType

TYPEKIND

 = GetTypeInfoType\(index\)
Retrieves the type of a type description\.

#### Parameters

  - index : int

    The index of the type description within the library