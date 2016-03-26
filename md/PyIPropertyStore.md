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


## [PyIPropertyStore](PyIPropertyStore.md#pyipropertystore)\.Commit

Commit\(\)
Commits property changes


## [PyIPropertyStore](PyIPropertyStore.md#pyipropertystore)\.GetAt

[PyPROPERTYKEY](PyPROPERTYKEY.md) = GetAt\(iProp\)
Returns the property key for the specified property

#### Parameters

  - iProp : int

    Zero-based index of property


## [PyIPropertyStore](PyIPropertyStore.md#pyipropertystore)\.GetCount

int = GetCount\(\)
Returns the number of properties in the store


## [PyIPropertyStore](PyIPropertyStore.md#pyipropertystore)\.GetValue

[PyPROPVARIANT](PyPROPVARIANT.md) = GetValue\(Key\)
Retrieves the value of a property

#### Parameters

  - Key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property key as returned by [PyIPropertyStore::GetAt](PyIPropertyStore.md#pyipropertystoregetat)


## [PyIPropertyStore](PyIPropertyStore.md#pyipropertystore)\.SetValue

SetValue\(Key, Value\)
Sets the value of a property

#### Parameters

  - Key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property key \(see [PyIPropertyStore::GetAt](PyIPropertyStore.md#pyipropertystoregetat)\)

  - Value : [PyPROPVARIANT](PyPROPVARIANT.md)

    Variant value which can be converted to the appropriate variant type for the property 

Pass a VT\_EMPTY variant to indicate that the property should be removed\.