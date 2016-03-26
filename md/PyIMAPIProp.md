# PyIMAPIProp


## PyIMAPIProp Object

An COM interface to MAPI 

Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [GetProps](PyIMAPIProp.md#pyimapipropgetprops)

    Returns a list of property values\.&nbsp;

  - [DeleteProps](PyIMAPIProp.md#pyimapipropdeleteprops)

    Deletes a set of properties\.&nbsp;

  - [SetProps](PyIMAPIProp.md#pyimapipropsetprops)

    Sets a set of properties\.&nbsp;

  - [CopyTo](PyIMAPIProp.md#pyimapipropcopyto)

    Copies an object to another&nbsp;

  - [CopyProps](PyIMAPIProp.md#pyimapipropcopyprops)

    Copies a set of properties to another object&nbsp;

  - [OpenProperty](PyIMAPIProp.md#pyimapipropopenproperty)

    Returns an interface object to be used to access a property\.&nbsp;

  - [GetIDsFromNames](PyIMAPIProp.md#pyimapipropgetidsfromnames)

    Determines property IDs&nbsp;

  - [GetNamesFromIDs](PyIMAPIProp.md#pyimapipropgetnamesfromids)

    Determines property names&nbsp;

  - [GetLastError](PyIMAPIProp.md#pyimapipropgetlasterror)

    Returns the last error code for the object\.&nbsp;

  - [SaveChanges](PyIMAPIProp.md#pyimapipropsavechanges)

    Saves pending changes to the object&nbsp;

  - [GetPropList](PyIMAPIProp.md#pyimapipropgetproplist)

    Gets a list of properties&nbsp;


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.CopyProps

int, \[problems, \] = CopyProps\(propTags, uiFlags

, progress

, resultIID

, dest

, flags

\)
Copies a set of properties to another object

#### Parameters

  - propTags : [PySPropTagArray](PySPropTagArray.md)

    The property tags to copy

  - uiFlags : int

    Flags for the progress object

  - progress : None

    Reserved - must pass None

  - resultIID : [PyIID](PyIID.md)

    IID of the destination object

  - dest : [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)

    The destination object

  - flags : int

    flags


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.CopyTo

int, \[problems, \] = CopyTo\(IIDExcludeList, propTags

, uiFlags

, progress

, resultIID

, dest

, flags

\)
Copies an object to another

#### Parameters

  - IIDExcludeList : \[[PyIID](PyIID.md), \]

    A sequence of IIDs to exclude\.

  - propTags : [PySPropTagArray](PySPropTagArray.md)

    The property tags to copy

  - uiFlags : int

    Flags for the progress object

  - progress : None

    Reserved - must pass None

  - resultIID : [PyIID](PyIID.md)

    IID of the destination object

  - dest : [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)

    The destination object

  - flags : int

    flags


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.DeleteProps

int, \[problems, \] = DeleteProps\(propList\)
Deletes a set of properties\.

#### Parameters

  - propList : [PySPropTagArray](PySPropTagArray.md)

    The list of properties


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.GetIDsFromNames

[PySPropTagArray](PySPropTagArray.md) = GetIDsFromNames\(nameIds, flags

\)
Determines property IDs

#### Parameters

  - nameIds : PyMAPINAMEIDArray

    Sequence of name ids

  - flags=0 : int

    


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.GetLastError

MAPIERROR

 = GetLastError\(hr, flags

\)
Returns the last error code for the object\.

#### Parameters

  - hr : int

    Contains the error code generated in the previous method call\.

  - flags : int

    Indicates for format for the output\.


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.GetNamesFromIDs

HRESULT, [PySPropTagArray](PySPropTagArray.md), [PyMAPINAMEIDArray](PyMAPINAMEIDArray.md) = GetNamesFromIDs\(propTags, propSetGuid

, flags

\)
Determines property names

#### Parameters

  - propTags : [PySPropTagArray](PySPropTagArray.md)

    Sequence of property tags, or None

  - propSetGuid=None : [PyIID](PyIID.md)

    a globally unique identifier, identifying a property set, or None

  - flags=0 : int

    


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.GetPropList

[PySPropTagArray](PySPropTagArray.md) = GetPropList\(flags\)
Gets a list of properties

#### Parameters

  - flags : int

    flags


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.GetProps

int, \[items, \] = GetProps\(propList, flags

\)
Returns a list of property values\.

#### Parameters

  - propList : [PySPropTagArray](PySPropTagArray.md)

    The list of properties

  - flags=0 : int

    


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.OpenProperty

[PyIUnknown](PyIUnknown.md) = OpenProperty\(propTag, iid

, interfaceOptions

, flags

\)
Returns an interface object to be used to access a property\.

#### Parameters

  - propTag : ULONG

    The property tag to open

  - iid : [PyIID](PyIID.md)

    The IID of the resulting interface\.

  - interfaceOptions : int

    Data that relates to the interface identified by the lpiid parameter\.

  - flags : int

    flags


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.SaveChanges

SaveChanges\(flags\)
Saves pending changes to the object

#### Parameters

  - flags : int

    flags


## [PyIMAPIProp](PyIMAPIProp.md#pyimapiprop)\.SetProps

int, \[problems, \] = SetProps\(propList\)
Sets a set of properties\.

#### Parameters

  - propList : \[[PySPropValue](PySPropValue.md), \]

    The list of properties