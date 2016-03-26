# PyICreateTypeInfo


## PyICreateTypeInfo Object

Description of the interface

#### Methods

  - [SetGuid](PyICreateTypeInfo.md#pyicreatetypeinfosetguid)

    Description of SetGuid&nbsp;

  - [SetTypeFlags](PyICreateTypeInfo.md#pyicreatetypeinfosettypeflags)

    Description of SetTypeFlags&nbsp;

  - [SetDocString](PyICreateTypeInfo.md#pyicreatetypeinfosetdocstring)

    Description of SetDocString&nbsp;

  - [SetHelpContext](PyICreateTypeInfo.md#pyicreatetypeinfosethelpcontext)

    Description of SetHelpContext&nbsp;

  - [SetVersion](PyICreateTypeInfo.md#pyicreatetypeinfosetversion)

    Description of SetVersion&nbsp;

  - [AddRefTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfoaddreftypeinfo)

    Description of AddRefTypeInfo&nbsp;

  - [AddFuncDesc](PyICreateTypeInfo.md#pyicreatetypeinfoaddfuncdesc)

    Description of AddFuncDesc&nbsp;

  - [AddImplType](PyICreateTypeInfo.md#pyicreatetypeinfoaddimpltype)

    Description of AddImplType&nbsp;

  - [SetImplTypeFlags](PyICreateTypeInfo.md#pyicreatetypeinfosetimpltypeflags)

    Description of SetImplTypeFlags&nbsp;

  - [SetAlignment](PyICreateTypeInfo.md#pyicreatetypeinfosetalignment)

    Description of SetAlignment&nbsp;

  - [SetSchema](PyICreateTypeInfo.md#pyicreatetypeinfosetschema)

    Description of SetSchema&nbsp;

  - [AddVarDesc](PyICreateTypeInfo.md#pyicreatetypeinfoaddvardesc)

    Description of AddVarDesc&nbsp;

  - [SetFuncAndParamNames](PyICreateTypeInfo.md#pyicreatetypeinfosetfuncandparamnames)

    Description of SetFuncAndParamNames&nbsp;

  - [SetVarName](PyICreateTypeInfo.md#pyicreatetypeinfosetvarname)

    Description of SetVarName&nbsp;

  - [SetTypeDescAlias](PyICreateTypeInfo.md#pyicreatetypeinfosettypedescalias)

    Description of SetTypeDescAlias&nbsp;

  - [DefineFuncAsDllEntry](PyICreateTypeInfo.md#pyicreatetypeinfodefinefuncasdllentry)

    Description of DefineFuncAsDllEntry&nbsp;

  - [SetFuncDocString](PyICreateTypeInfo.md#pyicreatetypeinfosetfuncdocstring)

    Description of SetFuncDocString&nbsp;

  - [SetVarDocString](PyICreateTypeInfo.md#pyicreatetypeinfosetvardocstring)

    Description of SetVarDocString&nbsp;

  - [SetFuncHelpContext](PyICreateTypeInfo.md#pyicreatetypeinfosetfunchelpcontext)

    Description of SetFuncHelpContext&nbsp;

  - [SetVarHelpContext](PyICreateTypeInfo.md#pyicreatetypeinfosetvarhelpcontext)

    Description of SetVarHelpContext&nbsp;

  - [SetMops](PyICreateTypeInfo.md#pyicreatetypeinfosetmops)

    Description of SetMops&nbsp;

  - [LayOut](PyICreateTypeInfo.md#pyicreatetypeinfolayout)

    Description of LayOut&nbsp;


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.AddFuncDesc

AddFuncDesc\(index\)
Description of AddFuncDesc\.

#### Parameters

  - index : int

    Description for index


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.AddImplType

AddImplType\(index, hRefType\)
Description of AddImplType\.

#### Parameters

  - index : int

    Description for index

  - hRefType : int

    A hRefType


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.AddRefTypeInfo

AddRefTypeInfo\(pTInfo\)
Description of AddRefTypeInfo\.

#### Parameters

  - pTInfo : [PyITypeInfo](PyITypeInfo.md)

    Description for pTInfo


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.AddVarDesc

AddVarDesc\(index\)
Description of AddVarDesc\.

#### Parameters

  - index : int

    Description for index


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.DefineFuncAsDllEntry

DefineFuncAsDllEntry\(index, szDllName, szProcName\)
Description of DefineFuncAsDllEntry\.

#### Parameters

  - index : int

    Description for index

  - szDllName : unicode

    Description for szDllName

  - szProcName : unicode

    Description for szProcName


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.LayOut

LayOut\(\)
Description of LayOut\.


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetAlignment

SetAlignment\(cbAlignment\)
Description of SetAlignment\.

#### Parameters

  - cbAlignment : int

    Description for cbAlignment


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetDocString

SetDocString\(pStrDoc\)
Description of SetDocString\.

#### Parameters

  - pStrDoc : unicode

    Description for pStrDoc


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetFuncAndParamNames

SetFuncAndParamNames\(index, rgszNames\)
Description of SetFuncAndParamNames\.

#### Parameters

  - index : int

    Index of the item to set\.

  - rgszNames : \(unicode

, \.\.\.\)

    A sequence of unicode or String objects\.


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetFuncDocString

SetFuncDocString\(index, szDocString\)
Description of SetFuncDocString\.

#### Parameters

  - index : int

    Description for index

  - szDocString : unicode

    Description for szDocString


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetFuncHelpContext

SetFuncHelpContext\(index, dwHelpContext\)
Description of SetFuncHelpContext\.

#### Parameters

  - index : int

    Description for index

  - dwHelpContext : int

    Description for dwHelpContext


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetGuid

SetGuid\(guid\)
Description of SetGuid\.

#### Parameters

  - guid : [PyIID](PyIID.md)

    Description for guid


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetHelpContext

SetHelpContext\(dwHelpContext\)
Description of SetHelpContext\.

#### Parameters

  - dwHelpContext : int

    Description for dwHelpContext


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetImplTypeFlags

SetImplTypeFlags\(index, implTypeFlags\)
Description of SetImplTypeFlags\.

#### Parameters

  - index : int

    Description for index

  - implTypeFlags : int

    Description for implTypeFlags


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetMops

SetMops\(index, bstrMops\)
Description of SetMops\.

#### Parameters

  - index : int

    Description for index

  - bstrMops : unicode

    Description for bstrMops


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetSchema

SetSchema\(pStrSchema\)
Description of SetSchema\.

#### Parameters

  - pStrSchema : unicode

    Description for pStrSchema


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetTypeDescAlias

SetTypeDescAlias\(\)
Description of SetTypeDescAlias\.


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetTypeFlags

SetTypeFlags\(uTypeFlags\)
Description of SetTypeFlags\.

#### Parameters

  - uTypeFlags : int

    Description for uTypeFlags


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetVarDocString

SetVarDocString\(index, szDocString\)
Description of SetVarDocString\.

#### Parameters

  - index : int

    Description for index

  - szDocString : unicode

    Description for szDocString


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetVarHelpContext

SetVarHelpContext\(index, dwHelpContext\)
Description of SetVarHelpContext\.

#### Parameters

  - index : int

    Description for index

  - dwHelpContext : int

    Description for dwHelpContext


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetVarName

SetVarName\(index, szName\)
Description of SetVarName\.

#### Parameters

  - index : int

    Description for index

  - szName : unicode

    Description for szName


## [PyICreateTypeInfo](PyICreateTypeInfo.md#pyicreatetypeinfo)\.SetVersion

SetVersion\(wMajorVerNum, wMinorVerNum\)
Description of SetVersion\.

#### Parameters

  - wMajorVerNum : int

    Description for wMajorVerNum

  - wMinorVerNum : int

    Description for wMinorVerNum