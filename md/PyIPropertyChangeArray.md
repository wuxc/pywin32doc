# PyIPropertyChangeArray

## PyIPropertyChangeArray Object



Container for a sequence of[PyIPropertyChange](#pyipropertychange) interfaces, as used with[PyIFileOperation](#pyifileoperation)\.
Create using pythoncom\.CoCreateInstance\(propsys\.CLSID\_PropertyChangeArray, \.\.\.\)

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

## [PyIPropertyChangeArray](#pyipropertychangearray)\.Append

Append\(PropChange\)
Adds a change to the end of the array

#### Parameters


  - PropChange :[PyIPropertyChange](#pyipropertychange)

    The change to be added

## [PyIPropertyChangeArray](#pyipropertychangearray)\.AppendOrReplace

AppendOrReplace\(PropChange\)
Adds a change, or replaces if an identical property key is already in container

#### Parameters


  - PropChange :[PyIPropertyChange](#pyipropertychange)

    The change to be added or replaced

## [PyIPropertyChangeArray](#pyipropertychangearray)\.GetAt

[PyIPropertyChange](#pyipropertychange) =GetAt\(Index, riid\)
Retrieves a change by zero-based index

#### Parameters


  - Index : int

    Index of the change to retrieve

  - riid=IID\_IPropertyChange :[PyIID](#pyiid)

    The interface to return

## [PyIPropertyChangeArray](#pyipropertychangearray)\.GetCount



int =GetCount\(\)
Returns the number of changes in the array

## [PyIPropertyChangeArray](#pyipropertychangearray)\.InsertAt

InsertAt\(Index, PropChange\)
Inserts a change at a specific position

#### Parameters


  - Index : int

    Position at which to place the change

  - PropChange :[PyIPropertyChange](#pyipropertychange)

    The change to be added

## [PyIPropertyChangeArray](#pyipropertychangearray)\.IsKeyInArray



boolean =IsKeyInArray\(key\)
Checks if array contains a change to a property

#### Parameters


  - key :[PyPROPERTYKEY](#pypropertykey)

    Property key to look for

## [PyIPropertyChangeArray](#pyipropertychangearray)\.RemoveAt

RemoveAt\(Index\)
Removes a change from the array

#### Parameters


  - Index : int

    Index of change to be removed