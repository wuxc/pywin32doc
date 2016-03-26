# PyIShellItem2


## PyIShellItem2 Object

Extends the IShellItem interface, giving access to an item's properties

#### Methods

  - [GetPropertyStore](PyIShellItem2.md#pyishellitem2getpropertystore)

    Returns a collection of the item's properties&nbsp;

  - [GetPropertyStoreForKeys](PyIShellItem2.md#pyishellitem2getpropertystoreforkeys)

    Creates a property store containing just the specified properties of the item&nbsp;

  - [GetPropertyStoreWithCreateObject](PyIShellItem2.md#pyishellitem2getpropertystorewithcreateobject)

    Returns the property store for the item, with alternate handler instantiation&nbsp;

  - [GetPropertyDescriptionList](PyIShellItem2.md#pyishellitem2getpropertydescriptionlist)

    Retrieves descriptions of properties in a particular group&nbsp;

  - [Update](PyIShellItem2.md#pyishellitem2update)

    Refreshes properties that have been modified since interface was created&nbsp;

  - [GetProperty](PyIShellItem2.md#pyishellitem2getproperty)

    DRetrieves the value of a property, converted to an appropriate python type&nbsp;

  - [GetCLSID](PyIShellItem2.md#pyishellitem2getclsid)

    Retrieves the value of a property as a GUID&nbsp;

  - [GetFileTime](PyIShellItem2.md#pyishellitem2getfiletime)

    Retrieves the value of a property as a file time\.&nbsp;

  - [GetInt32](PyIShellItem2.md#pyishellitem2getint32)

    Retrieves the value of a property as a 32 bit int\.&nbsp;

  - [GetString](PyIShellItem2.md#pyishellitem2getstring)

    Retrieves the value of a property as a string&nbsp;

  - [GetUInt32](PyIShellItem2.md#pyishellitem2getuint32)

    Returns the value of a property as a 32 bit unsigned int&nbsp;

  - [GetUInt64](PyIShellItem2.md#pyishellitem2getuint64)

    Returns the value of a property as an unsigned 64-bit int&nbsp;

  - [GetBool](PyIShellItem2.md#pyishellitem2getbool)

    Returns the value of a property as a boolean&nbsp;


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetBool

boolean = GetBool\(key\)
Returns the value of a property as a boolean

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetCLSID

[PyIID](PyIID.md) = GetCLSID\(key\)
Retrieves the value of a property as a CLSID \(VT\_CLSID\)

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetFileTime

[PyTime](PyTime.md) = GetFileTime\(key\)
Retrieves the value of a property as a FILETIME

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetInt32

int = GetInt32\(key\)
Retrieves the value of a property as a 32 bit int\.

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetProperty

object = GetProperty\(key\)
Retrieves the value of a property, converted to an appropriate python type

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve

#### Return Value
Type of returned object is determined by the variant type of the property


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetPropertyDescriptionList

[PyIPropertyDescriptionList](PyIPropertyDescriptionList.md) = GetPropertyDescriptionList\(Type, riid

\)
Retrieves descriptions of properties in a particular group

#### Parameters

  - Type : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property list identifier \(pscon\.PKEY\_PropList\_\*\)

  - riid=IID\_IPropertyDescriptionList : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetPropertyStore

[PyIPropertyStore](PyIPropertyStore.md) = GetPropertyStore\(Flags, riid

\)
Returns a collection of the item's properties

#### Parameters

  - Flags=GPS\_DEFAULT : int

    Combination of GETPROPERTYSTOREFLAGS values \(shellcon\.GPS\_\*\)

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetPropertyStoreForKeys

[PyIPropertyStore](PyIPropertyStore.md) = GetPropertyStoreForKeys\(Keys, Flags

, riid

\)
Creates a property store containing just the specified properties of the item

#### Parameters

  - Keys : \(SHCOLUMNID

,\.\.\.\)\)

    A sequence of property identifiers

  - Flags=GPS\_DEFAULT : int

    Combination of GETPROPERTYSTOREFLAGS values \(shellcon\.GPS\_\*\)

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetPropertyStoreWithCreateObject

[PyIPropertyStore](PyIPropertyStore.md) = GetPropertyStoreWithCreateObject\(Flags, CreateObject

, riid

\)
Returns the property store for the item, with alternate handler instantiation

#### Parameters

  - Flags : int

    Combination of GETPROPERTYSTOREFLAGS values \(shellcon\.GPS\_\*\)

  - CreateObject : [PyIUnknown](PyIUnknown.md)

    An interface that implements ICreateObject, used to create the property handler

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to be created

#### Comments

Primarily used to create a handler in a separate process with reduced privileges


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetString

str = GetString\(key\)
Retrieves the value of a property as a string

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetUInt32

int = GetUInt32\(key\)
Returns the value of a property as a 32 bit unsigned int

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.GetUInt64

int = GetUInt64\(key\)
Returns the value of a property as an unsigned 64-bit int

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The id of the property to retrieve


## [PyIShellItem2](PyIShellItem2.md#pyishellitem2)\.Update

Update\(BindCtx\)
Refreshes properties that have been modified since interface was created

#### Parameters

  - BindCtx=None : PyIBindCxt

    Bind context used when requesting the interface, or None