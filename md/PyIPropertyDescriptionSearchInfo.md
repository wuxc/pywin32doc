# PyIPropertyDescriptionSearchInfo

## PyIPropertyDescriptionSearchInfo Object

Interface that retrieves indexing options defined in a property's searchinfo XML element 

Inhererits all methods of[PyIPropertyDescription](#pyipropertydescription)

#### Methods


  - [GetSearchInfoFlags](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetsearchinfoflags)

    Returns flags controlling how property is indexed&nbsp;

  - [GetColumnIndexType](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetcolumnindextype)

    Returns flags indicating type of property&nbsp;

  - [GetProjectionString](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetprojectionstring)

    Returns the canonical name of the property&nbsp;

  - [GetMaxSize](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetmaxsize)

    Returns the maximum size specified in search options&nbsp;

## [PyIPropertyDescriptionSearchInfo](#pyipropertydescriptionsearchinfo).GetColumnIndexType

int = __GetColumnIndexType(__ )
Returns flags indicating type of property

#### Return Value
Returns a value from the PROPDESC_COLUMNINDEX_TYPE enum

## [PyIPropertyDescriptionSearchInfo](#pyipropertydescriptionsearchinfo).GetMaxSize

int = __GetMaxSize(__ )
Returns the maximum size specified in search options

## [PyIPropertyDescriptionSearchInfo](#pyipropertydescriptionsearchinfo).GetProjectionString

str = __GetProjectionString(__ )
Returns the canonical name of the property

## [PyIPropertyDescriptionSearchInfo](#pyipropertydescriptionsearchinfo).GetSearchInfoFlags

int = __GetSearchInfoFlags(__ )
Returns flags controlling how property is indexed

#### Return Value
Returns a combination of PROPDESC_SEARCHINFO_FLAGS values