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

    Registers a set of properties defined in a .propdesc file&nbsp;

  - [UnregisterPropertySchema](PyIPropertySystem.md#pyipropertysystemunregisterpropertyschema)

    Removes a set of registered properties&nbsp;

  - [RefreshPropertySchema](PyIPropertySystem.md#pyipropertysystemrefreshpropertyschema)

    Not currently implemented by the OS&nbsp;

## [PyIPropertySystem](#pyipropertysystem).EnumeratePropertyDescriptions

[PyIPropertyDescriptionList](#pyipropertydescriptionlist)= __EnumeratePropertyDescriptions( *Filter*  *, riid* __ )
Returns an interface used to list defined properties

#### Parameters


  -  *Filter=PDEF_ALL* : int

    Value from PROPDESC_ENUMFILTER (pscon.PDEF_*) that limits what types of properties are listed

  -  *riid=IID_IPropertyDescriptionList* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertySystem](#pyipropertysystem).FormatForDisplay

str = __FormatForDisplay( *Key*  *, Value*  *, Flags* __ )
Formats a property into a string

#### Parameters


  -  *Key* :[PyPROPERTYKEY](#pypropertykey)

    Fmtid and property id that identifies the property

  -  *Value* :[PyPROPVARIANT](#pypropvariant)

    The value to format

  -  *Flags=PDFF_DEFAULT* : int

    Combination of PROPDESC_FORMAT_FLAGS (pscon.PDFF_*) indicating formatting options

## [PyIPropertySystem](#pyipropertysystem).GetPropertyDescription

[PyIPropertyDescription](#pyipropertydescription)= __GetPropertyDescription( *Key*  *, riid* __ )
Returns an interface used to describe a property

#### Parameters


  -  *Key* :[PyPROPERTYKEY](#pypropertykey)

    Fmtid and propertyid that uniquely identifies a property

  -  *riid=IID_IPropertyDescription* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertySystem](#pyipropertysystem).GetPropertyDescriptionByName

[PyIPropertyDescription](#pyipropertydescription)= __GetPropertyDescriptionByName( *CanonicalName*  *, riid* __ )
Returns an interface used to describe a property

#### Parameters


  -  *CanonicalName* : str

    Registered name of the property

  -  *riid=IID_IPropertyDescription* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertySystem](#pyipropertysystem).GetPropertyDescriptionListFromString

[PyIPropertyDescriptionList](#pyipropertydescriptionlist)= __GetPropertyDescriptionListFromString( *PropList*  *, riid* __ )
Retrieves property descriptions from a string of property names

#### Parameters


  -  *PropList* : str

    String containing a list of properties and flags

  -  *riid=IPropertyDescriptionList* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertySystem](#pyipropertysystem).RefreshPropertySchema

 __RefreshPropertySchema(__ )
Not currently implemented by the OS

#### Comments
Not currently implemented, according to MSDN

## [PyIPropertySystem](#pyipropertysystem).RegisterPropertySchema

 __RegisterPropertySchema( *Path* __ )
Registers a set of properties defined in a .propdesc file

#### Parameters


  -  *Path* : str

    Path to a property schema XML file (.propdesc)

## [PyIPropertySystem](#pyipropertysystem).UnregisterPropertySchema

 __UnregisterPropertySchema( *Path* __ )
Removes a set of registered properties

#### Parameters


  -  *Path* : str

    Path to a property schema XML file (.propdesc)