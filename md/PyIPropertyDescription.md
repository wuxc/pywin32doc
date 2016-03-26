# PyIPropertyDescription

## PyIPropertyDescription Object

Gives access to the details of a property definition

#### Methods


  - [GetPropertyKey](PyIPropertyDescription.md#pyipropertydescriptiongetpropertykey)

    Returns the unique identifier for a property&nbsp;

  - [GetCanonicalName](PyIPropertyDescription.md#pyipropertydescriptiongetcanonicalname)

    Returns the name of the property&nbsp;

  - [GetPropertyType](PyIPropertyDescription.md#pyipropertydescriptiongetpropertytype)

    Returns the variant type of the property (VT_*)&nbsp;

  - [GetDisplayName](PyIPropertyDescription.md#pyipropertydescriptiongetdisplayname)

    Returns the property name as shown in the UI&nbsp;

  - [GetEditInvitation](PyIPropertyDescription.md#pyipropertydescriptiongeteditinvitation)

    Returns the input prompt used in edit controls&nbsp;

  - [GetTypeFlags](PyIPropertyDescription.md#pyipropertydescriptiongettypeflags)

    Returns type flags for the property&nbsp;

  - [GetViewFlags](PyIPropertyDescription.md#pyipropertydescriptiongetviewflags)

    Returns the view flags that control how the property is displayed (PDVF_*)&nbsp;

  - [GetDefaultColumnWidth](PyIPropertyDescription.md#pyipropertydescriptiongetdefaultcolumnwidth)

    Returns the default width in characters&nbsp;

  - [GetDisplayType](PyIPropertyDescription.md#pyipropertydescriptiongetdisplaytype)

    Returns the display type (PDDT_*)&nbsp;

  - [GetColumnState](PyIPropertyDescription.md#pyipropertydescriptiongetcolumnstate)

    Returns flags that control how property is displayed in column (SHCOLSTATE_*)&nbsp;

  - [GetGroupingRange](PyIPropertyDescription.md#pyipropertydescriptiongetgroupingrange)

    Returns property's grouping attributes (PDGR_*)&nbsp;

  - [GetRelativeDescriptionType](PyIPropertyDescription.md#pyipropertydescriptiongetrelativedescriptiontype)

    Returns the relative description type (PDRDT_*)&nbsp;

  - [GetRelativeDescription](PyIPropertyDescription.md#pyipropertydescriptiongetrelativedescription)

    Compares two values&nbsp;

  - [GetSortDescription](PyIPropertyDescription.md#pyipropertydescriptiongetsortdescription)

    Returns value that determines how sorting options are displayed (PDSD_*)&nbsp;

  - [GetSortDescriptionLabel](PyIPropertyDescription.md#pyipropertydescriptiongetsortdescriptionlabel)

    Returns description of current sort order&nbsp;

  - [GetAggregationType](PyIPropertyDescription.md#pyipropertydescriptiongetaggregationtype)

    Describes how properties for multiple items are displayed (PDAT_*)&nbsp;

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

## [PyIPropertyDescription](#pyipropertydescription).CoerceToCanonicalValue

int = __CoerceToCanonicalValue( *Value* __ )
Converts a variant value to the exact type expected by the property

#### Parameters


  -  *Value* :[PyPROPVARIANT](#pypropvariant)

    The property value to be converted

#### Comments
This method mutates the PyPROPVARIANT in place.  It may be cleared on failure.

#### Return Value
Returns the HRESULT from the operation on success.

## [PyIPropertyDescription](#pyipropertydescription).FormatForDisplay

str = __FormatForDisplay( *Value*  *, Flags* __ )
Converts a value to its string representation

#### Parameters


  -  *Value* :[PyPROPVARIANT](#pypropvariant)

    The value to be formatted

  -  *Flags=PDFF_DEFAULT* : int

    Combination of PROPDESC_FORMAT_FLAGS (PDFF_*)

## [PyIPropertyDescription](#pyipropertydescription).GetAggregationType

int = __GetAggregationType(__ )
Describes how properties for multiple items are displayed (PDAT_*)

## [PyIPropertyDescription](#pyipropertydescription).GetCanonicalName

str = __GetCanonicalName(__ )
Returns the name of the property

## [PyIPropertyDescription](#pyipropertydescription).GetColumnState

int = __GetColumnState(__ )
Returns flags that control how property is displayed in column (SHCOLSTATE_*)

## [PyIPropertyDescription](#pyipropertydescription).GetConditionType

(int, int) = __GetConditionType(__ )
Returns options that determine how the property is used to build a search query

#### Return Value
Returns the condition type (PDCOT_*) and default operation (COP_*)

## [PyIPropertyDescription](#pyipropertydescription).GetDefaultColumnWidth

int = __GetDefaultColumnWidth(__ )
Returns the default width in characters

## [PyIPropertyDescription](#pyipropertydescription).GetDisplayName

str = __GetDisplayName(__ )
Returns the property name as shown in the UI

## [PyIPropertyDescription](#pyipropertydescription).GetDisplayType

int = __GetDisplayType(__ )
Returns the display type (PDDT_*)

## [PyIPropertyDescription](#pyipropertydescription).GetEditInvitation

str = __GetEditInvitation(__ )
Returns the input prompt used in edit controls

## [PyIPropertyDescription](#pyipropertydescription).GetEnumTypeList

[PyIPropertyEnumTypeList](#pyipropertyenumtypelist)= __GetEnumTypeList( *riid* __ )
Returns an interface used for querying valid property range

#### Parameters


  -  *riid=IID_IPropertyEnumTypeList* :[PyIID](#pyiid)

    IID of the requested interface

## [PyIPropertyDescription](#pyipropertydescription).GetGroupingRange

int = __GetGroupingRange(__ )
Returns property's grouping attributes (PDGR_*)

## [PyIPropertyDescription](#pyipropertydescription).GetPropertyKey

[PyPROPERTYKEY](#pypropertykey)= __GetPropertyKey(__ )
Returns the unique identifier for a property

## [PyIPropertyDescription](#pyipropertydescription).GetPropertyType

int = __GetPropertyType(__ )
Returns the variant type of the property (VT_*)

## [PyIPropertyDescription](#pyipropertydescription).GetRelativeDescription

(str, str) = __GetRelativeDescription( *var1*  *, var2* __ )
Compares two values

#### Parameters


  -  *var1* :[PyPROPVARIANT](#pypropvariant)

    The first value

  -  *var2* :[PyPROPVARIANT](#pypropvariant)

    The second value

## [PyIPropertyDescription](#pyipropertydescription).GetRelativeDescriptionType

int = __GetRelativeDescriptionType(__ )
Returns the relative description type (PDRDT_*)

## [PyIPropertyDescription](#pyipropertydescription).GetSortDescription

int = __GetSortDescription(__ )
Returns value that determines how sorting options are displayed (PDSD_*)

## [PyIPropertyDescription](#pyipropertydescription).GetSortDescriptionLabel

str = __GetSortDescriptionLabel( *Descending* __ )
Returns description of current sort order

#### Parameters


  -  *Descending* : bool

    Indicates if order is reversed

## [PyIPropertyDescription](#pyipropertydescription).GetTypeFlags

int = __GetTypeFlags( *mask* __ )
Returns type flags for the property

#### Parameters


  -  *mask=PDTF_MASK_ALL* : int

    Specifies which flags to retrieve (PDTF_*)

## [PyIPropertyDescription](#pyipropertydescription).GetViewFlags

int = __GetViewFlags(__ )
Returns the view flags that control how the property is displayed (PDVF_*)

## [PyIPropertyDescription](#pyipropertydescription).IsValueCanonical

bool = __IsValueCanonical( *Value* __ )
Determines if a value exactly matches the specification for the property

#### Parameters


  -  *Value* : PROPVARIANT

    The value to check