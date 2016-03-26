# PyITypeInfo


## PyITypeInfo Object

An OLE automation type info object\.  Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [GetContainingTypeLib](PyITypeInfo.md#pyitypeinfogetcontainingtypelib)

    Retrieves the containing type library and the index of the type description within that type library\.&nbsp;

  - [GetDocumentation](PyITypeInfo.md#pyitypeinfogetdocumentation)

    Retrieves the documentation string, the complete Help file name and path, and the context ID for the Help topic for a specified type description\.&nbsp;

  - [GetFuncDesc](PyITypeInfo.md#pyitypeinfogetfuncdesc)

    Retrieves the [FUNCDESC](FUNCDESC.md) object that contains information about a specified function\.&nbsp;

  - [GetImplTypeFlags](PyITypeInfo.md#pyitypeinfogetimpltypeflags)

    Retrieves the IMPLTYPEFLAGS enumeration for one implemented interface or base interface in a type description\.&nbsp;

  - [GetIDsOfNames](PyITypeInfo.md#pyitypeinfogetidsofnames)

    Maps between member names and member IDs, and parameter names and parameter IDs\.&nbsp;

  - [GetNames](PyITypeInfo.md#pyitypeinfogetnames)

    Retrieves the variable with the specified member ID \(or the name of the property or method and its parameters\) that correspond to the specified function ID\.&nbsp;

  - [GetTypeAttr](PyITypeInfo.md#pyitypeinfogettypeattr)

    Retrieves a [TYPEATTR](TYPEATTR.md) object that contains the attributes of the type description\.&nbsp;

  - [GetRefTypeInfo](PyITypeInfo.md#pyitypeinfogetreftypeinfo)

    If a type description references other type descriptions, it retrieves the referenced type descriptions\.&nbsp;

  - [GetRefTypeOfImplType](PyITypeInfo.md#pyitypeinfogetreftypeofimpltype)

    Retrieves the type description of the implemented interface types\.&nbsp;

  - [GetVarDesc](PyITypeInfo.md#pyitypeinfogetvardesc)

    Retrieves a [VARDESC](VARDESC.md) object that describes the specified variable\.&nbsp;

  - [GetTypeComp](PyITypeInfo.md#pyitypeinfogettypecomp)

    Retrieves a ITypeComp

 object for Name to VARDESC/FUNCDESC mapping\.&nbsp;




## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetContainingTypeLib

[PyITypeLib](PyITypeLib.md), int = GetContainingTypeLib\(\)
Retrieves the containing type library and the index of the type description within that type library\.


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetDocumentation

\(name, docstring, helpContext, helpFile\) = GetDocumentation\(memberId\)
Retrieves the documentation string, the complete Help file name and path, and the context ID for the Help topic for a specified type description\.

#### Parameters

  - memberId : int

    


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetFuncDesc

[FUNCDESC](FUNCDESC.md) = GetFuncDesc\(memberId\)
Retrieves the [FUNCDESC](FUNCDESC.md) object that contains information about a specified function\.

#### Parameters

  - memberId : int

    


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetIDsOfNames

int = GetIDsOfNames\(\)
Maps between member names and member IDs, and parameter names and parameter IDs\.


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetImplTypeFlags

int = GetImplTypeFlags\(index\)
Retrieves the IMPLTYPEFLAGS enumeration for one implemented interface or base interface in a type description\.

#### Parameters

  - index : int

    


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetNames

\(tuple of strings\) = GetNames\(memberId\)
Retrieves the variable with the specified member ID \(or the name of the property or method and its parameters\) that correspond to the specified function ID\.

#### Parameters

  - memberId : int

    


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetRefTypeInfo

[PyITypeInfo](PyITypeInfo.md#pyitypeinfo) = GetRefTypeInfo\(hRefType\)
If a type description references other type descriptions, it retrieves the referenced type descriptions\.

#### Parameters

  - hRefType : int

    


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetRefTypeOfImplType

int = GetRefTypeOfImplType\(hRefType\)
Retrieves the type description of the implemented interface types\.

#### Parameters

  - hRefType : int

    

#### Comments

If a type description describes a COM class, it retrieves the type 

description of the implemented interface types\. For an interface, 

GetRefTypeOfImplType returns the type information for inherited 

interfaces, if any exist\.


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetTypeAttr

[TYPEATTR](TYPEATTR.md) = GetTypeAttr\(\)
Retrieves a [TYPEATTR](TYPEATTR.md) object that contains the attributes of the type description\.


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetTypeComp

[PyITypeComp](PyITypeComp.md) = GetTypeComp\(\)
Retrieves a ITypeComp

 object for Name to VARDESC/FUNCDESC mapping\.


## [PyITypeInfo](PyITypeInfo.md#pyitypeinfo)\.GetVarDesc

[VARDESC](VARDESC.md) = GetVarDesc\(memberId\)
Retrieves a [VARDESC](VARDESC.md) object that describes the specified variable\.

#### Parameters

  - memberId : int

    