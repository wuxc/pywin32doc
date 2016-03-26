# PyIPropertyStore

## PyIPropertyStore Object

Contains a collection of properties

#### Methods


  - [GetCount](PyIPropertyStore.md#pyipropertystoregetcount)

    Returns the number of properties in the store&nbsp;

  - [GetAt](PyIPropertyStore.md#pyipropertystoregetat)

    Returns the property key for the specified property&nbsp;

  - [GetValue](PyIPropertyStore.md#pyipropertystoregetvalue)

    Retrieves the value of a property&nbsp;

  - [SetValue](PyIPropertyStore.md#pyipropertystoresetvalue)

    Sets the value of a property&nbsp;

  - [Commit](PyIPropertyStore.md#pyipropertystorecommit)

    Commits property changes&nbsp;

## [PyIPropertyStore](#pyipropertystore).Commit

 __Commit(__ )
Commits property changes

## [PyIPropertyStore](#pyipropertystore).GetAt

[PyPROPERTYKEY](#pypropertykey)= __GetAt( *iProp* __ )
Returns the property key for the specified property

#### Parameters


  -  *iProp* : int

    Zero-based index of property

## [PyIPropertyStore](#pyipropertystore).GetCount

int = __GetCount(__ )
Returns the number of properties in the store

## [PyIPropertyStore](#pyipropertystore).GetValue

[PyPROPVARIANT](#pypropvariant)= __GetValue( *Key* __ )
Retrieves the value of a property

#### Parameters


  -  *Key* :[PyPROPERTYKEY](#pypropertykey)

    Property key as returned by[PyIPropertyStore::GetAt](PyIPropertyStore.md#pyipropertystoregetat)

## [PyIPropertyStore](#pyipropertystore).SetValue

 __SetValue( *Key*  *, Value* __ )
Sets the value of a property

#### Parameters


  -  *Key* :[PyPROPERTYKEY](#pypropertykey)

    Property key (see[PyIPropertyStore::GetAt](PyIPropertyStore.md#pyipropertystoregetat))

  -  *Value* :[PyPROPVARIANT](#pypropvariant)

    Variant value which can be converted to the appropriate variant type for the property 

Pass a VT_EMPTY variant to indicate that the property should be removed.