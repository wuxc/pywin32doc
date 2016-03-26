# PyIPropertyDescriptionSearchInfo


## PyIPropertyDescriptionSearchInfo Object

Interface that retrieves indexing options defined in a property's searchinfo XML element 

Inhererits all methods of [PyIPropertyDescription](PyIPropertyDescription.md)

#### Methods

  - [GetSearchInfoFlags](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetsearchinfoflags)

    Returns flags controlling how property is indexed&nbsp;

  - [GetColumnIndexType](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetcolumnindextype)

    Returns flags indicating type of property&nbsp;

  - [GetProjectionString](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetprojectionstring)

    Returns the canonical name of the property&nbsp;

  - [GetMaxSize](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfogetmaxsize)

    Returns the maximum size specified in search options&nbsp;


## [PyIPropertyDescriptionSearchInfo](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfo)\.GetColumnIndexType

int = GetColumnIndexType\(\)
Returns flags indicating type of property

#### Return Value
Returns a value from the PROPDESC\_COLUMNINDEX\_TYPE enum


## [PyIPropertyDescriptionSearchInfo](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfo)\.GetMaxSize

int = GetMaxSize\(\)
Returns the maximum size specified in search options


## [PyIPropertyDescriptionSearchInfo](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfo)\.GetProjectionString

str = GetProjectionString\(\)
Returns the canonical name of the property


## [PyIPropertyDescriptionSearchInfo](PyIPropertyDescriptionSearchInfo.md#pyipropertydescriptionsearchinfo)\.GetSearchInfoFlags

int = GetSearchInfoFlags\(\)
Returns flags controlling how property is indexed

#### Return Value
Returns a combination of PROPDESC\_SEARCHINFO\_FLAGS values