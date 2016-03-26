# PyIPropertyStoreCache

## PyIPropertyStoreCache Object

Property store that allows tracking of modification state.  Inherits all methods of[PyIPropertyStore](#pyipropertystore).

#### Methods


  - [GetState](PyIPropertyStoreCache.md#pyipropertystorecachegetstate)

    Retrieves the current state of a property&nbsp;

  - [GetValueAndState](PyIPropertyStoreCache.md#pyipropertystorecachegetvalueandstate)

    Retrieves the current value and state of a property&nbsp;

  - [SetState](PyIPropertyStoreCache.md#pyipropertystorecachesetstate)

    Sets the state of a property&nbsp;

  - [SetValueAndState](PyIPropertyStoreCache.md#pyipropertystorecachesetvalueandstate)

    Sets the value and state of a property&nbsp;

## [PyIPropertyStoreCache](#pyipropertystorecache).GetState

int = __GetState( *key* __ )
Retrieves the current state of a property

#### Parameters


  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Property identifier

#### Return Value
A value from the PSC_STATE enum (PSC_NORMAL, PSC_NOTINSOURCE. PSC_DIRTY)

## [PyIPropertyStoreCache](#pyipropertystorecache).GetValueAndState

([PyPROPVARIANT](#pypropvariant), int) = __GetValueAndState( *key* __ )
Retrieves the current value and state of a property

#### Parameters


  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Property identifier

## [PyIPropertyStoreCache](#pyipropertystorecache).SetState

 __SetState( *key*  *, state* __ )
Sets the state of a property

#### Parameters


  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Property identifier

  -  *state* : int

    Value from the PSC_STATE enum (pscon.PSC_*)

## [PyIPropertyStoreCache](#pyipropertystorecache).SetValueAndState

 __SetValueAndState( *key*  *, value*  *, state* __ )
Sets the value and state of a property

#### Parameters


  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Property identifier

  -  *value* :[PyPROPVARIANT](#pypropvariant)

    The new value

  -  *state* : int

    The new state (pscon.PSC_*)