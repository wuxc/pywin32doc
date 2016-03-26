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

## [PyINamedPropertyStore](#pyinamedpropertystore).GetNameAt

str = __GetNameAt( *Index* __ )
Retrieves a property name by zero-based index

#### Parameters


  -  *Index* : int

    Index of the property name

## [PyINamedPropertyStore](#pyinamedpropertystore).GetNameCount

int = __GetNameCount(__ )
Retrieves the number of named properties in the store

## [PyINamedPropertyStore](#pyinamedpropertystore).GetNamedValue

[PyPROPVARIANT](#pypropvariant)= __GetNamedValue( *Name* __ )
Retrieves a property value by name

#### Parameters


  -  *Name* : str

    Name of the property

## [PyINamedPropertyStore](#pyinamedpropertystore).SetNamedValue

 __SetNamedValue( *propvar* __ )
Sets the value of a property

#### Parameters


  -  *propvar* : __Py__RPC__in REFPROPVARIANT__ 

    Description for propvar