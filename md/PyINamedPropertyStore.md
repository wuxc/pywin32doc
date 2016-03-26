# PyINamedPropertyStore


## PyINamedPropertyStore Object

Contains a collection of properties indentified by name

#### Methods

  - [GetNamedValue](PyINamedPropertyStore.md#pyinamedpropertystoregetnamedvalue)

    Retrieves a property value by name&nbsp;

  - [SetNamedValue](PyINamedPropertyStore.md#pyinamedpropertystoresetnamedvalue)

    Sets the value of a property&nbsp;

  - [GetNameCount](PyINamedPropertyStore.md#pyinamedpropertystoregetnamecount)

    Retrieves the number of named properties in the store&nbsp;

  - [GetNameAt](PyINamedPropertyStore.md#pyinamedpropertystoregetnameat)

    Retrieves a property name by zero-based index&nbsp;


## [PyINamedPropertyStore](PyINamedPropertyStore.md#pyinamedpropertystore)\.GetNameAt

str = GetNameAt\(Index\)
Retrieves a property name by zero-based index

#### Parameters

  - Index : int

    Index of the property name


## [PyINamedPropertyStore](PyINamedPropertyStore.md#pyinamedpropertystore)\.GetNameCount

int = GetNameCount\(\)
Retrieves the number of named properties in the store


## [PyINamedPropertyStore](PyINamedPropertyStore.md#pyinamedpropertystore)\.GetNamedValue

[PyPROPVARIANT](PyPROPVARIANT.md) = GetNamedValue\(Name\)
Retrieves a property value by name

#### Parameters

  - Name : str

    Name of the property


## [PyINamedPropertyStore](PyINamedPropertyStore.md#pyinamedpropertystore)\.SetNamedValue

SetNamedValue\(propvar\)
Sets the value of a property

#### Parameters

  - propvar : Py\_\_RPC\_\_in REFPROPVARIANT

    Description for propvar