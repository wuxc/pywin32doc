# PyIPropertyDescription


## PyIPropertyDescription Object

Gives access to the details of a property definition

#### Methods

  - [GetPropertyKey](PyIPropertyDescription.md#pyipropertydescriptiongetpropertykey)

    Returns the unique identifier for a property&nbsp;

  - [GetCanonicalName](PyIPropertyDescription.md#pyipropertydescriptiongetcanonicalname)

    Returns the name of the property&nbsp;

  - [GetPropertyType](PyIPropertyDescription.md#pyipropertydescriptiongetpropertytype)

    Returns the variant type of the property \(VT\_\*\)&nbsp;

  - [GetDisplayName](PyIPropertyDescription.md#pyipropertydescriptiongetdisplayname)

    Returns the property name as shown in the UI&nbsp;

  - [GetEditInvitation](PyIPropertyDescription.md#pyipropertydescriptiongeteditinvitation)

    Returns the input prompt used in edit controls&nbsp;

  - [GetTypeFlags](PyIPropertyDescription.md#pyipropertydescriptiongettypeflags)

    Returns type flags for the property&nbsp;

  - [GetViewFlags](PyIPropertyDescription.md#pyipropertydescriptiongetviewflags)

    Returns the view flags that control how the property is displayed \(PDVF\_\*\)&nbsp;

  - [GetDefaultColumnWidth](PyIPropertyDescription.md#pyipropertydescriptiongetdefaultcolumnwidth)

    Returns the default width in characters&nbsp;

  - [GetDisplayType](PyIPropertyDescription.md#pyipropertydescriptiongetdisplaytype)

    Returns the display type \(PDDT\_\*\)&nbsp;

  - [GetColumnState](PyIPropertyDescription.md#pyipropertydescriptiongetcolumnstate)

    Returns flags that control how property is displayed in column \(SHCOLSTATE\_\*\)&nbsp;

  - [GetGroupingRange](PyIPropertyDescription.md#pyipropertydescriptiongetgroupingrange)

    Returns property's grouping attributes \(PDGR\_\*\)&nbsp;

  - [GetRelativeDescriptionType](PyIPropertyDescription.md#pyipropertydescriptiongetrelativedescriptiontype)

    Returns the relative description type \(PDRDT\_\*\)&nbsp;

  - [GetRelativeDescription](PyIPropertyDescription.md#pyipropertydescriptiongetrelativedescription)

    Compares two values&nbsp;

  - [GetSortDescription](PyIPropertyDescription.md#pyipropertydescriptiongetsortdescription)

    Returns value that determines how sorting options are displayed \(PDSD\_\*\)&nbsp;

  - [GetSortDescriptionLabel](PyIPropertyDescription.md#pyipropertydescriptiongetsortdescriptionlabel)

    Returns description of current sort order&nbsp;

  - [GetAggregationType](PyIPropertyDescription.md#pyipropertydescriptiongetaggregationtype)

    Describes how properties for multiple items are displayed \(PDAT\_\*\)&nbsp;

  - [GetConditionType](PyIPropertyDescription.md#pyipropertydescriptiongetconditiontype)

    Returns options that determine how the property is used to build a search query&nbsp;

  - [GetEnumTypeList](PyIPropertyDescription.md#pyipropertydescriptiongetenumtypelist)

    Returns an interface used for querying valid property range&nbsp;

  - [CoerceToCanonicalValue](PyIPropertyDescription.md#pyipropertydescriptioncoercetocanonicalvalue)

    Converts a variant value to the exact type expected by the property&nbsp;

  - [FormatForDisplay](PyIPropertyDescription.md#pyipropertydescriptionformatfordisplay)

    Converts a value to its string representation&nbsp;

  - [IsValueCanonical](PyIPropertyDescription.md#pyipropertydescriptionisvaluecanonical)

    Determines if a value exactly matches the specification for the property&nbsp;


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.CoerceToCanonicalValue

int = CoerceToCanonicalValue\(Value\)
Converts a variant value to the exact type expected by the property

#### Parameters

  - Value : [PyPROPVARIANT](PyPROPVARIANT.md)

    The property value to be converted

#### Comments

This method mutates the PyPROPVARIANT in place\.  It may be cleared on failure\.

#### Return Value
Returns the HRESULT from the operation on success\.


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.FormatForDisplay

str = FormatForDisplay\(Value, Flags

\)
Converts a value to its string representation

#### Parameters

  - Value : [PyPROPVARIANT](PyPROPVARIANT.md)

    The value to be formatted

  - Flags=PDFF\_DEFAULT : int

    Combination of PROPDESC\_FORMAT\_FLAGS \(PDFF\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetAggregationType

int = GetAggregationType\(\)
Describes how properties for multiple items are displayed \(PDAT\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetCanonicalName

str = GetCanonicalName\(\)
Returns the name of the property


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetColumnState

int = GetColumnState\(\)
Returns flags that control how property is displayed in column \(SHCOLSTATE\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetConditionType

\(int, int\) = GetConditionType\(\)
Returns options that determine how the property is used to build a search query

#### Return Value
Returns the condition type \(PDCOT\_\*\) and default operation \(COP\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetDefaultColumnWidth

int = GetDefaultColumnWidth\(\)
Returns the default width in characters


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetDisplayName

str = GetDisplayName\(\)
Returns the property name as shown in the UI


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetDisplayType

int = GetDisplayType\(\)
Returns the display type \(PDDT\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetEditInvitation

str = GetEditInvitation\(\)
Returns the input prompt used in edit controls


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetEnumTypeList

[PyIPropertyEnumTypeList](PyIPropertyEnumTypeList.md) = GetEnumTypeList\(riid\)
Returns an interface used for querying valid property range

#### Parameters

  - riid=IID\_IPropertyEnumTypeList : [PyIID](PyIID.md)

    IID of the requested interface


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetGroupingRange

int = GetGroupingRange\(\)
Returns property's grouping attributes \(PDGR\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetPropertyKey

[PyPROPERTYKEY](PyPROPERTYKEY.md) = GetPropertyKey\(\)
Returns the unique identifier for a property


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetPropertyType

int = GetPropertyType\(\)
Returns the variant type of the property \(VT\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetRelativeDescription

\(str, str\) = GetRelativeDescription\(var1, var2

\)
Compares two values

#### Parameters

  - var1 : [PyPROPVARIANT](PyPROPVARIANT.md)

    The first value

  - var2 : [PyPROPVARIANT](PyPROPVARIANT.md)

    The second value


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetRelativeDescriptionType

int = GetRelativeDescriptionType\(\)
Returns the relative description type \(PDRDT\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetSortDescription

int = GetSortDescription\(\)
Returns value that determines how sorting options are displayed \(PDSD\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetSortDescriptionLabel

str = GetSortDescriptionLabel\(Descending\)
Returns description of current sort order

#### Parameters

  - Descending : bool

    Indicates if order is reversed


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetTypeFlags

int = GetTypeFlags\(mask\)
Returns type flags for the property

#### Parameters

  - mask=PDTF\_MASK\_ALL : int

    Specifies which flags to retrieve \(PDTF\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.GetViewFlags

int = GetViewFlags\(\)
Returns the view flags that control how the property is displayed \(PDVF\_\*\)


## [PyIPropertyDescription](PyIPropertyDescription.md#pyipropertydescription)\.IsValueCanonical

bool = IsValueCanonical\(Value\)
Determines if a value exactly matches the specification for the property

#### Parameters

  - Value : PROPVARIANT

    The value to check