# PyIPropertyChangeArray


## PyIPropertyChangeArray Object

Container for a sequence of [PyIPropertyChange](PyIPropertyChange.md) interfaces, as used with [PyIFileOperation](PyIFileOperation.md)\. 

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


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.Append

Append\(PropChange\)
Adds a change to the end of the array

#### Parameters

  - PropChange : [PyIPropertyChange](PyIPropertyChange.md)

    The change to be added


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.AppendOrReplace

AppendOrReplace\(PropChange\)
Adds a change, or replaces if an identical property key is already in container

#### Parameters

  - PropChange : [PyIPropertyChange](PyIPropertyChange.md)

    The change to be added or replaced


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.GetAt

[PyIPropertyChange](PyIPropertyChange.md) = GetAt\(Index, riid

\)
Retrieves a change by zero-based index

#### Parameters

  - Index : int

    Index of the change to retrieve

  - riid=IID\_IPropertyChange : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.GetCount

int = GetCount\(\)
Returns the number of changes in the array


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.InsertAt

InsertAt\(Index, PropChange\)
Inserts a change at a specific position

#### Parameters

  - Index : int

    Position at which to place the change

  - PropChange : [PyIPropertyChange](PyIPropertyChange.md)

    The change to be added


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.IsKeyInArray

boolean = IsKeyInArray\(key\)
Checks if array contains a change to a property

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property key to look for


## [PyIPropertyChangeArray](PyIPropertyChangeArray.md#pyipropertychangearray)\.RemoveAt

RemoveAt\(Index\)
Removes a change from the array

#### Parameters

  - Index : int

    Index of change to be removed