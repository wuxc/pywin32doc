# PyIBindCtx


## PyIBindCtx Object

A Python interface to IBindCtx\.  Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [GetRunningObjectTable](PyIBindCtx.md#pyibindctxgetrunningobjecttable)

    Retrieves the running object table\.&nbsp;

  - [GetBindOptions](PyIBindCtx.md#pyibindctxgetbindoptions)

    Retrieves bind options&nbsp;

  - [SetBindOptions](PyIBindCtx.md#pyibindctxsetbindoptions)

    Sets the bind options for the bind context&nbsp;

  - [RegisterObjectParam](PyIBindCtx.md#pyibindctxregisterobjectparam)

    Associates a COM object to the bind context&nbsp;

  - [RevokeObjectParam](PyIBindCtx.md#pyibindctxrevokeobjectparam)

    Removes one of the bind context's associated objects&nbsp;

  - [GetObjectParam](PyIBindCtx.md#pyibindctxgetobjectparam)

    Retrieves one of the contexts string-keyed objects&nbsp;

  - [EnumObjectParam](PyIBindCtx.md#pyibindctxenumobjectparam)

    Creates an enumerator to list context's string keys&nbsp;




## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.EnumObjectParam

[PyIEnumString](PyIEnumString.md) = EnumObjectParam\(\)
Creates an enumerator to list context's string keys


## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.GetBindOptions

[PyBIND\_OPTS](PyBIND.md#pybindopts) = GetBindOptions\(\)
Retrieves the bind options for the bind context


## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.GetObjectParam

[PyIUnknown](PyIUnknown.md) = GetObjectParam\(Key\)
Returns one of the bind context's associated objects

#### Parameters

  - Key : [PyUnicode](PyUnicode.md)

    The string key for the object to be returned


## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.GetRunningObjectTable

[PyIRunningObjectTable](PyIRunningObjectTable.md) = GetRunningObjectTable\(\)
Retrieves an object interfacing to the Running Object Table\.


## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.RegisterObjectParam

RegisterObjectParam\(Key, punk\)
Adds an object to the context's keyed table of associated objects

#### Parameters

  - Key : [PyUnicode](PyUnicode.md)

    The string key for the object to be registered

  - punk : [PyIUnknown](PyIUnknown.md)

    COM object to be registered with the bind context


## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.RevokeObjectParam

RevokeObjectParam\(Key\)
Removes one of the bind context's registered objects

#### Parameters

  - Key : [PyUnicode](PyUnicode.md)

    The string key for the object to be removed


## [PyIBindCtx](PyIBindCtx.md#pyibindctx)\.SetBindOptions

SetBindOptions\(bindopts\)
Sets the bind options for the context

#### Parameters

  - bindopts : dict

    [PyBIND\_OPTS](PyBIND.md#pybindopts) dictionary containing the binding options