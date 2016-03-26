# PyITypeInfo

## PyITypeInfo Object



An OLE automation type info object\.  Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [GetContainingTypeLib](PyITypeInfo.md#pyitypeinfogetcontainingtypelib)

    Retrieves the containing type library and the index of the type description within that type library\.&nbsp;

  - [GetDocumentation](PyITypeInfo.md#pyitypeinfogetdocumentation)

    Retrieves the documentation string, the complete Help file name and path, and the context ID for the Help topic for a specified type description\.&nbsp;

  - [GetFuncDesc](PyITypeInfo.md#pyitypeinfogetfuncdesc)

    Retrieves the[FUNCDESC](#funcdesc) object that contains information about a specified function\.&nbsp;

  - [GetImplTypeFlags](PyITypeInfo.md#pyitypeinfogetimpltypeflags)

    Retrieves the IMPLTYPEFLAGS enumeration for one implemented interface or base interface in a type description\.&nbsp;

  - [GetIDsOfNames](PyITypeInfo.md#pyitypeinfogetidsofnames)

    Maps between member names and member IDs, and parameter names and parameter IDs\.&nbsp;

  - [GetNames](PyITypeInfo.md#pyitypeinfogetnames)

    Retrieves the variable with the specified member ID \(or the name of the property or method and its parameters\) that correspond to the specified function ID\.&nbsp;

  - [GetTypeAttr](PyITypeInfo.md#pyitypeinfogettypeattr)

    Retrieves a[TYPEATTR](#typeattr) object that contains the attributes of the type description\.&nbsp;

  - [GetRefTypeInfo](PyITypeInfo.md#pyitypeinfogetreftypeinfo)

    If a type description references other type descriptions, it retrieves the referenced type descriptions\.&nbsp;

  - [GetRefTypeOfImplType](PyITypeInfo.md#pyitypeinfogetreftypeofimpltype)

    Retrieves the type description of the implemented interface types\.&nbsp;

  - [GetVarDesc](PyITypeInfo.md#pyitypeinfogetvardesc)

    Retrieves a[VARDESC](#vardesc) object that describes the specified variable\.&nbsp;

  - [GetTypeComp](PyITypeInfo.md#pyitypeinfogettypecomp)

    Retrieves aITypeComp

 object for Name to VARDESC/FUNCDESC mapping\.&nbsp;


## [PyITypeInfo](#pyitypeinfo)\.GetContainingTypeLib

[PyITypeLib](#pyitypelib), int =GetContainingTypeLib\(\)
Retrieves the containing type library and the index of the type description within that type library\.

## [PyITypeInfo](#pyitypeinfo)\.GetDocumentation



\(name, docstring, helpContext, helpFile\) =GetDocumentation\(memberId\)
Retrieves the documentation string, the complete Help file name and path, and the context ID for the Help topic for a specified type description\.

#### Parameters


  - memberId : int

    

## [PyITypeInfo](#pyitypeinfo)\.GetFuncDesc

[FUNCDESC](#funcdesc) =GetFuncDesc\(memberId\)
Retrieves the[FUNCDESC](#funcdesc) object that contains information about a specified function\.

#### Parameters


  - memberId : int

    

## [PyITypeInfo](#pyitypeinfo)\.GetIDsOfNames



int =GetIDsOfNames\(\)
Maps between member names and member IDs, and parameter names and parameter IDs\.

## [PyITypeInfo](#pyitypeinfo)\.GetImplTypeFlags



int =GetImplTypeFlags\(index\)
Retrieves the IMPLTYPEFLAGS enumeration for one implemented interface or base interface in a type description\.

#### Parameters


  - index : int

    

## [PyITypeInfo](#pyitypeinfo)\.GetNames



\(tuple of strings\) =GetNames\(memberId\)
Retrieves the variable with the specified member ID \(or the name of the property or method and its parameters\) that correspond to the specified function ID\.

#### Parameters


  - memberId : int

    

## [PyITypeInfo](#pyitypeinfo)\.GetRefTypeInfo

[PyITypeInfo](#pyitypeinfo) =GetRefTypeInfo\(hRefType\)
If a type description references other type descriptions, it retrieves the referenced type descriptions\.

#### Parameters


  - hRefType : int

    

## [PyITypeInfo](#pyitypeinfo)\.GetRefTypeOfImplType



int =GetRefTypeOfImplType\(hRefType\)
Retrieves the type description of the implemented interface types\.

#### Parameters


  - hRefType : int

    

#### Comments


If a type description describes a COM class, it retrieves the type 

description of the implemented interface types\. For an interface, 

GetRefTypeOfImplType returns the type information for inherited 

interfaces, if any exist\.

## [PyITypeInfo](#pyitypeinfo)\.GetTypeAttr

[TYPEATTR](#typeattr) =GetTypeAttr\(\)
Retrieves a[TYPEATTR](#typeattr) object that contains the attributes of the type description\.

## [PyITypeInfo](#pyitypeinfo)\.GetTypeComp

[PyITypeComp](#pyitypecomp) =GetTypeComp\(\)
Retrieves aITypeComp

 object for Name to VARDESC/FUNCDESC mapping\.

## [PyITypeInfo](#pyitypeinfo)\.GetVarDesc

[VARDESC](#vardesc) =GetVarDesc\(memberId\)
Retrieves a[VARDESC](#vardesc) object that describes the specified variable\.

#### Parameters


  - memberId : int

    