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

## [PyIContext](#pyicontext)\.EnumContextProps

[PyIEnumContextProps](#pyienumcontextprops)\= **EnumContextProps\(** \)
Returns an enumerator for the context properties

## [PyIContext](#pyicontext)\.GetProperty

\(int,[PyIUnknown](#pyiunknown)\) \= **GetProperty\( *rGuid* ** \)
Retrieves a context property

#### Parameters


  -  *rGuid* :[PyIID](#pyiid)

    GUID that identifies a context property

#### Return Value
Returns flags \(CPFLAGS is reserved, no defined values\) and the IUnknown interface set for the property

## [PyIContext](#pyicontext)\.RemoveProperty

 **RemoveProperty\( *rPolicyId* ** \)
Removes a property from the context

#### Parameters


  -  *rPolicyId* :[PyIID](#pyiid)

    GUID that identifies a context property

## [PyIContext](#pyicontext)\.SetProperty

 **SetProperty\( *rpolicyId*  *, flags*  *, pUnk* ** \)
Sets a property on the context

#### Parameters


  -  *rpolicyId* :[PyIID](#pyiid)

    GUID identifying the property to be set

  -  *flags* : int

    Reserved, use only 0

  -  *pUnk* :[PyIUnknown](#pyiunknown)

    The property value