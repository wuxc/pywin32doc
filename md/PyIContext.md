# PyIContext


## PyIContext Object

Allows access to properties defined for the current context \(Requires win2k or later\)

#### Methods

  - [SetProperty](PyIContext.md#pyicontextsetproperty)

    Sets a property on the context&nbsp;

  - [RemoveProperty](PyIContext.md#pyicontextremoveproperty)

    Removes a property from the context&nbsp;

  - [GetProperty](PyIContext.md#pyicontextgetproperty)

    Retrieves a context property&nbsp;

  - [EnumContextProps](PyIContext.md#pyicontextenumcontextprops)

    Returns an enumerator for the context properties&nbsp;


## [PyIContext](PyIContext.md#pyicontext)\.EnumContextProps

[PyIEnumContextProps](PyIEnumContextProps.md) = EnumContextProps\(\)
Returns an enumerator for the context properties


## [PyIContext](PyIContext.md#pyicontext)\.GetProperty

\(int, [PyIUnknown](PyIUnknown.md)\) = GetProperty\(rGuid\)
Retrieves a context property

#### Parameters

  - rGuid : [PyIID](PyIID.md)

    GUID that identifies a context property

#### Return Value
Returns flags \(CPFLAGS is reserved, no defined values\) and the IUnknown interface set for the property


## [PyIContext](PyIContext.md#pyicontext)\.RemoveProperty

RemoveProperty\(rPolicyId\)
Removes a property from the context

#### Parameters

  - rPolicyId : [PyIID](PyIID.md)

    GUID that identifies a context property


## [PyIContext](PyIContext.md#pyicontext)\.SetProperty

SetProperty\(rpolicyId, flags, pUnk\)
Sets a property on the context

#### Parameters

  - rpolicyId : [PyIID](PyIID.md)

    GUID identifying the property to be set

  - flags : int

    Reserved, use only 0

  - pUnk : [PyIUnknown](PyIUnknown.md)

    The property value