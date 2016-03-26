# PyIPropertyChangeArray

## PyIPropertyChangeArray Object

Container for a sequence of[PyIPropertyChange](#pyipropertychange)interfaces, as used with[PyIFileOperation](#pyifileoperation).
Create using pythoncom.CoCreateInstance(propsys.CLSID_PropertyChangeArray, ...)

#### Methods


  - [GetCount](PyIPropertyChangeArray.md#pyipropertychangearraygetcount)

    Returns the number of changes in the array&nbsp;

  - [GetAt](PyIPropertyChangeArray.md#pyipropertychangearraygetat)

    Returns a change by zero-based index&nbsp;

  - [InsertAt](PyIPropertyChangeArray.md#pyipropertychangearrayinsertat)

    Inserts a change at a specific position&nbsp;

  - [Append](PyIPropertyChangeArray.md#pyipropertychangearrayappend)

    Adds a change to the end of the array&nbsp;

  - [AppendOrReplace](PyIPropertyChangeArray.md#pyipropertychangearrayappendorreplace)

    Adds a change, or replaces an identical property key&nbsp;

  - [RemoveAt](PyIPropertyChangeArray.md#pyipropertychangearrayremoveat)

    Removes a change from the array&nbsp;

  - [IsKeyInArray](PyIPropertyChangeArray.md#pyipropertychangearrayiskeyinarray)

    Checks if array contains a change to a property&nbsp;

## [PyIPropertyChangeArray](#pyipropertychangearray).Append

 __Append( *PropChange* __ )
Adds a change to the end of the array

#### Parameters


  -  *PropChange* :[PyIPropertyChange](#pyipropertychange)

    The change to be added

## [PyIPropertyChangeArray](#pyipropertychangearray).AppendOrReplace

 __AppendOrReplace( *PropChange* __ )
Adds a change, or replaces if an identical property key is already in container

#### Parameters


  -  *PropChange* :[PyIPropertyChange](#pyipropertychange)

    The change to be added or replaced

## [PyIPropertyChangeArray](#pyipropertychangearray).GetAt

[PyIPropertyChange](#pyipropertychange)= __GetAt( *Index*  *, riid* __ )
Retrieves a change by zero-based index

#### Parameters


  -  *Index* : int

    Index of the change to retrieve

  -  *riid=IID_IPropertyChange* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertyChangeArray](#pyipropertychangearray).GetCount

int = __GetCount(__ )
Returns the number of changes in the array

## [PyIPropertyChangeArray](#pyipropertychangearray).InsertAt

 __InsertAt( *Index*  *, PropChange* __ )
Inserts a change at a specific position

#### Parameters


  -  *Index* : int

    Position at which to place the change

  -  *PropChange* :[PyIPropertyChange](#pyipropertychange)

    The change to be added

## [PyIPropertyChangeArray](#pyipropertychangearray).IsKeyInArray

boolean = __IsKeyInArray( *key* __ )
Checks if array contains a change to a property

#### Parameters


  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Property key to look for

## [PyIPropertyChangeArray](#pyipropertychangearray).RemoveAt

 __RemoveAt( *Index* __ )
Removes a change from the array

#### Parameters


  -  *Index* : int

    Index of change to be removed