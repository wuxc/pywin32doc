# PyIPropertySystem


## PyIPropertySystem Object

Wraps the IPropertySystem interface

#### Methods

  - [GetPropertyDescription](PyIPropertySystem.md#pyipropertysystemgetpropertydescription)

    Returns an interface used to describe a property&nbsp;

  - [GetPropertyDescriptionByName](PyIPropertySystem.md#pyipropertysystemgetpropertydescriptionbyname)

    Returns an interface used to describe a property&nbsp;

  - [GetPropertyDescriptionListFromString](PyIPropertySystem.md#pyipropertysystemgetpropertydescriptionlistfromstring)

    Retrieves property descriptions from a string of property names&nbsp;

  - [EnumeratePropertyDescriptions](PyIPropertySystem.md#pyipropertysystemenumeratepropertydescriptions)

    Returns an interface used to list defined properties&nbsp;

  - [FormatForDisplay](PyIPropertySystem.md#pyipropertysystemformatfordisplay)

    Formats a property into a string&nbsp;

  - [RegisterPropertySchema](PyIPropertySystem.md#pyipropertysystemregisterpropertyschema)

    Registers a set of properties defined in a \.propdesc file&nbsp;

  - [UnregisterPropertySchema](PyIPropertySystem.md#pyipropertysystemunregisterpropertyschema)

    Removes a set of registered properties&nbsp;

  - [RefreshPropertySchema](PyIPropertySystem.md#pyipropertysystemrefreshpropertyschema)

    Not currently implemented by the OS&nbsp;


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.EnumeratePropertyDescriptions

[PyIPropertyDescriptionList](PyIPropertyDescriptionList.md) = EnumeratePropertyDescriptions\(Filter, riid

\)
Returns an interface used to list defined properties

#### Parameters

  - Filter=PDEF\_ALL : int

    Value from PROPDESC\_ENUMFILTER \(pscon\.PDEF\_\*\) that limits what types of properties are listed

  - riid=IID\_IPropertyDescriptionList : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.FormatForDisplay

str = FormatForDisplay\(Key, Value

, Flags

\)
Formats a property into a string

#### Parameters

  - Key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Fmtid and property id that identifies the property

  - Value : [PyPROPVARIANT](PyPROPVARIANT.md)

    The value to format

  - Flags=PDFF\_DEFAULT : int

    Combination of PROPDESC\_FORMAT\_FLAGS \(pscon\.PDFF\_\*\) indicating formatting options


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.GetPropertyDescription

[PyIPropertyDescription](PyIPropertyDescription.md) = GetPropertyDescription\(Key, riid

\)
Returns an interface used to describe a property

#### Parameters

  - Key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Fmtid and propertyid that uniquely identifies a property

  - riid=IID\_IPropertyDescription : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.GetPropertyDescriptionByName

[PyIPropertyDescription](PyIPropertyDescription.md) = GetPropertyDescriptionByName\(CanonicalName, riid

\)
Returns an interface used to describe a property

#### Parameters

  - CanonicalName : str

    Registered name of the property

  - riid=IID\_IPropertyDescription : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.GetPropertyDescriptionListFromString

[PyIPropertyDescriptionList](PyIPropertyDescriptionList.md) = GetPropertyDescriptionListFromString\(PropList, riid

\)
Retrieves property descriptions from a string of property names

#### Parameters

  - PropList : str

    String containing a list of properties and flags

  - riid=IPropertyDescriptionList : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.RefreshPropertySchema

RefreshPropertySchema\(\)
Not currently implemented by the OS

#### Comments

Not currently implemented, according to MSDN


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.RegisterPropertySchema

RegisterPropertySchema\(Path\)
Registers a set of properties defined in a \.propdesc file

#### Parameters

  - Path : str

    Path to a property schema XML file \(\.propdesc\)


## [PyIPropertySystem](PyIPropertySystem.md#pyipropertysystem)\.UnregisterPropertySchema

UnregisterPropertySchema\(Path\)
Removes a set of registered properties

#### Parameters

  - Path : str

    Path to a property schema XML file \(\.propdesc\)