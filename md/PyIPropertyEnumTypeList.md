# PyIPropertyEnumTypeList

## PyIPropertyEnumTypeList Object

Contains a collection of[PyIPropertyEnumType](#pyipropertyenumtype)objects that define the allowable values for a property

#### Methods


  - [GetCount](PyIPropertyEnumTypeList.md#pyipropertyenumtypelistgetcount)

    Returns the number of objects in the list&nbsp;

  - [GetAt](PyIPropertyEnumTypeList.md#pyipropertyenumtypelistgetat)

    Retrieves an item by index&nbsp;

  - [FindMatchingIndex](PyIPropertyEnumTypeList.md#pyipropertyenumtypelistfindmatchingindex)

    Attempts to match the specified value to one of the allowable values for the property&nbsp;

## [PyIPropertyEnumTypeList](#pyipropertyenumtypelist).FindMatchingIndex

int = __FindMatchingIndex( *Cmp* __ )
Attempts to match the specified value to one of the allowable values for the property

#### Parameters


  -  *Cmp* :[PyPROPVARIANT](#pypropvariant)

    A value to match against the defined values of the property

## [PyIPropertyEnumTypeList](#pyipropertyenumtypelist).GetAt

[PyIPropertyEnumType](#pyipropertyenumtype)= __GetAt( *itype*  *, riid* __ )
Retrieves an item by index

#### Parameters


  -  *itype* : int

    Zero based index of type to return

  -  *riid=IID_IPropertyEnumType* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertyEnumTypeList](#pyipropertyenumtypelist).GetCount

int = __GetCount(__ )
Returns the number of objects in the list