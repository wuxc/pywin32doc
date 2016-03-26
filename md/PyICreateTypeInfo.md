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

## [PyICreateTypeInfo](#pyicreatetypeinfo).AddFuncDesc

 __AddFuncDesc( *index* __ )
Description of AddFuncDesc.

#### Parameters


  -  *index* : int

    Description for index

## [PyICreateTypeInfo](#pyicreatetypeinfo).AddImplType

 __AddImplType( *index*  *, hRefType* __ )
Description of AddImplType.

#### Parameters


  -  *index* : int

    Description for index

  -  *hRefType* : int

    A hRefType

## [PyICreateTypeInfo](#pyicreatetypeinfo).AddRefTypeInfo

 __AddRefTypeInfo( *pTInfo* __ )
Description of AddRefTypeInfo.

#### Parameters


  -  *pTInfo* :[PyITypeInfo](#pyitypeinfo)

    Description for pTInfo

## [PyICreateTypeInfo](#pyicreatetypeinfo).AddVarDesc

 __AddVarDesc( *index* __ )
Description of AddVarDesc.

#### Parameters


  -  *index* : int

    Description for index

## [PyICreateTypeInfo](#pyicreatetypeinfo).DefineFuncAsDllEntry

 __DefineFuncAsDllEntry( *index*  *, szDllName*  *, szProcName* __ )
Description of DefineFuncAsDllEntry.

#### Parameters


  -  *index* : int

    Description for index

  -  *szDllName* : __unicode__ 

    Description for szDllName

  -  *szProcName* : __unicode__ 

    Description for szProcName

## [PyICreateTypeInfo](#pyicreatetypeinfo).LayOut

 __LayOut(__ )
Description of LayOut.

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetAlignment

 __SetAlignment( *cbAlignment* __ )
Description of SetAlignment.

#### Parameters


  -  *cbAlignment* : int

    Description for cbAlignment

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetDocString

 __SetDocString( *pStrDoc* __ )
Description of SetDocString.

#### Parameters


  -  *pStrDoc* : __unicode__ 

    Description for pStrDoc

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetFuncAndParamNames

 __SetFuncAndParamNames( *index*  *, rgszNames* __ )
Description of SetFuncAndParamNames.

#### Parameters


  -  *index* : int

    Index of the item to set.

  -  *rgszNames* : ( __unicode__ , ...)

    A sequence of unicode or String objects.

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetFuncDocString

 __SetFuncDocString( *index*  *, szDocString* __ )
Description of SetFuncDocString.

#### Parameters


  -  *index* : int

    Description for index

  -  *szDocString* : __unicode__ 

    Description for szDocString

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetFuncHelpContext

 __SetFuncHelpContext( *index*  *, dwHelpContext* __ )
Description of SetFuncHelpContext.

#### Parameters


  -  *index* : int

    Description for index

  -  *dwHelpContext* : int

    Description for dwHelpContext

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetGuid

 __SetGuid( *guid* __ )
Description of SetGuid.

#### Parameters


  -  *guid* :[PyIID](#pyiid)

    Description for guid

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetHelpContext

 __SetHelpContext( *dwHelpContext* __ )
Description of SetHelpContext.

#### Parameters


  -  *dwHelpContext* : int

    Description for dwHelpContext

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetImplTypeFlags

 __SetImplTypeFlags( *index*  *, implTypeFlags* __ )
Description of SetImplTypeFlags.

#### Parameters


  -  *index* : int

    Description for index

  -  *implTypeFlags* : int

    Description for implTypeFlags

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetMops

 __SetMops( *index*  *, bstrMops* __ )
Description of SetMops.

#### Parameters


  -  *index* : int

    Description for index

  -  *bstrMops* : __unicode__ 

    Description for bstrMops

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetSchema

 __SetSchema( *pStrSchema* __ )
Description of SetSchema.

#### Parameters


  -  *pStrSchema* : __unicode__ 

    Description for pStrSchema

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetTypeDescAlias

 __SetTypeDescAlias(__ )
Description of SetTypeDescAlias.

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetTypeFlags

 __SetTypeFlags( *uTypeFlags* __ )
Description of SetTypeFlags.

#### Parameters


  -  *uTypeFlags* : int

    Description for uTypeFlags

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetVarDocString

 __SetVarDocString( *index*  *, szDocString* __ )
Description of SetVarDocString.

#### Parameters


  -  *index* : int

    Description for index

  -  *szDocString* : __unicode__ 

    Description for szDocString

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetVarHelpContext

 __SetVarHelpContext( *index*  *, dwHelpContext* __ )
Description of SetVarHelpContext.

#### Parameters


  -  *index* : int

    Description for index

  -  *dwHelpContext* : int

    Description for dwHelpContext

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetVarName

 __SetVarName( *index*  *, szName* __ )
Description of SetVarName.

#### Parameters


  -  *index* : int

    Description for index

  -  *szName* : __unicode__ 

    Description for szName

## [PyICreateTypeInfo](#pyicreatetypeinfo).SetVersion

 __SetVersion( *wMajorVerNum*  *, wMinorVerNum* __ )
Description of SetVersion.

#### Parameters


  -  *wMajorVerNum* : int

    Description for wMajorVerNum

  -  *wMinorVerNum* : int

    Description for wMinorVerNum