# PyIPropertyEnumTypeList


## PyIPropertyEnumTypeList Object

Contains a collection of [PyIPropertyEnumType](PyIPropertyEnumType.md) objects that define the allowable values for a property

#### Methods

  - [GetCount](PyIPropertyEnumTypeList.md#pyipropertyenumtypelistgetcount)

    Returns the number of objects in the list&nbsp;

  - [GetAt](PyIPropertyEnumTypeList.md#pyipropertyenumtypelistgetat)

    Retrieves an item by index&nbsp;

  - [FindMatchingIndex](PyIPropertyEnumTypeList.md#pyipropertyenumtypelistfindmatchingindex)

    Attempts to match the specified value to one of the allowable values for the property&nbsp;


## [PyIPropertyEnumTypeList](PyIPropertyEnumTypeList.md#pyipropertyenumtypelist)\.FindMatchingIndex

int = FindMatchingIndex\(Cmp\)
Attempts to match the specified value to one of the allowable values for the property

#### Parameters

  - Cmp : [PyPROPVARIANT](PyPROPVARIANT.md)

    A value to match against the defined values of the property


## [PyIPropertyEnumTypeList](PyIPropertyEnumTypeList.md#pyipropertyenumtypelist)\.GetAt

[PyIPropertyEnumType](PyIPropertyEnumType.md) = GetAt\(itype, riid

\)
Retrieves an item by index

#### Parameters

  - itype : int

    Zero based index of type to return

  - riid=IID\_IPropertyEnumType : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertyEnumTypeList](PyIPropertyEnumTypeList.md#pyipropertyenumtypelist)\.GetCount

int = GetCount\(\)
Returns the number of objects in the list