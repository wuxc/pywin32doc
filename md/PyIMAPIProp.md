# PyIMAPIProp

## PyIMAPIProp Object

An COM interface to MAPI
Derived from[PyIUnknown](#pyiunknown)

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

## [PyIMAPIProp](#pyimapiprop)\.CopyProps

int, \[problems, \] \= **CopyProps\( *propTags*  *, uiFlags*  *, progress*  *, resultIID*  *, dest*  *, flags* ** \)
Copies a set of properties to another object

#### Parameters


  -  *propTags* :[PySPropTagArray](#pysproptagarray)

    The property tags to copy

  -  *uiFlags* : int

    Flags for the progress object

  -  *progress* : None

    Reserved - must pass None

  -  *resultIID* :[PyIID](#pyiid)

    IID of the destination object

  -  *dest* :[PyIMAPIProp](#pyimapiprop)

    The destination object

  -  *flags* : int

    flags

## [PyIMAPIProp](#pyimapiprop)\.CopyTo

int, \[problems, \] \= **CopyTo\( *IIDExcludeList*  *, propTags*  *, uiFlags*  *, progress*  *, resultIID*  *, dest*  *, flags* ** \)
Copies an object to another

#### Parameters


  -  *IIDExcludeList* : \[[PyIID](#pyiid), \]

    A sequence of IIDs to exclude\.

  -  *propTags* :[PySPropTagArray](#pysproptagarray)

    The property tags to copy

  -  *uiFlags* : int

    Flags for the progress object

  -  *progress* : None

    Reserved - must pass None

  -  *resultIID* :[PyIID](#pyiid)

    IID of the destination object

  -  *dest* :[PyIMAPIProp](#pyimapiprop)

    The destination object

  -  *flags* : int

    flags

## [PyIMAPIProp](#pyimapiprop)\.DeleteProps

int, \[problems, \] \= **DeleteProps\( *propList* ** \)
Deletes a set of properties\.

#### Parameters


  -  *propList* :[PySPropTagArray](#pysproptagarray)

    The list of properties

## [PyIMAPIProp](#pyimapiprop)\.GetIDsFromNames

[PySPropTagArray](#pysproptagarray)\= **GetIDsFromNames\( *nameIds*  *, flags* ** \)
Determines property IDs

#### Parameters


  -  *nameIds* : PyMAPINAMEIDArray

    Sequence of name ids

  -  *flags\=0* : int

    

## [PyIMAPIProp](#pyimapiprop)\.GetLastError

 **MAPIERROR** \= **GetLastError\( *hr*  *, flags* ** \)
Returns the last error code for the object\.

#### Parameters


  -  *hr* : int

    Contains the error code generated in the previous method call\.

  -  *flags* : int

    Indicates for format for the output\.

## [PyIMAPIProp](#pyimapiprop)\.GetNamesFromIDs

HRESULT,[PySPropTagArray](#pysproptagarray),[PyMAPINAMEIDArray](#pymapinameidarray)\= **GetNamesFromIDs\( *propTags*  *, propSetGuid*  *, flags* ** \)
Determines property names

#### Parameters


  -  *propTags* :[PySPropTagArray](#pysproptagarray)

    Sequence of property tags, or None

  -  *propSetGuid\=None* :[PyIID](#pyiid)

    a globally unique identifier, identifying a property set, or None

  -  *flags\=0* : int

    

## [PyIMAPIProp](#pyimapiprop)\.GetPropList

[PySPropTagArray](#pysproptagarray)\= **GetPropList\( *flags* ** \)
Gets a list of properties

#### Parameters


  -  *flags* : int

    flags

## [PyIMAPIProp](#pyimapiprop)\.GetProps

int, \[items, \] \= **GetProps\( *propList*  *, flags* ** \)
Returns a list of property values\.

#### Parameters


  -  *propList* :[PySPropTagArray](#pysproptagarray)

    The list of properties

  -  *flags\=0* : int

    

## [PyIMAPIProp](#pyimapiprop)\.OpenProperty

[PyIUnknown](#pyiunknown)\= **OpenProperty\( *propTag*  *, iid*  *, interfaceOptions*  *, flags* ** \)
Returns an interface object to be used to access a property\.

#### Parameters


  -  *propTag* : ULONG

    The property tag to open

  -  *iid* :[PyIID](#pyiid)

    The IID of the resulting interface\.

  -  *interfaceOptions* : int

    Data that relates to the interface identified by the lpiid parameter\.

  -  *flags* : int

    flags

## [PyIMAPIProp](#pyimapiprop)\.SaveChanges

 **SaveChanges\( *flags* ** \)
Saves pending changes to the object

#### Parameters


  -  *flags* : int

    flags

## [PyIMAPIProp](#pyimapiprop)\.SetProps

int, \[problems, \] \= **SetProps\( *propList* ** \)
Sets a set of properties\.

#### Parameters


  -  *propList* : \[[PySPropValue](#pyspropvalue), \]

    The list of properties