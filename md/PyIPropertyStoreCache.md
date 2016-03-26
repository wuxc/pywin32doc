# PyIPropertyStoreCache


## PyIPropertyStoreCache Object

Property store that allows tracking of modification state\.  Inherits all methods of [PyIPropertyStore](PyIPropertyStore.md)\.

#### Methods

  - [GetState](PyIPropertyStoreCache.md#pyipropertystorecachegetstate)

    Retrieves the current state of a property&nbsp;

  - [GetValueAndState](PyIPropertyStoreCache.md#pyipropertystorecachegetvalueandstate)

    Retrieves the current value and state of a property&nbsp;

  - [SetState](PyIPropertyStoreCache.md#pyipropertystorecachesetstate)

    Sets the state of a property&nbsp;

  - [SetValueAndState](PyIPropertyStoreCache.md#pyipropertystorecachesetvalueandstate)

    Sets the value and state of a property&nbsp;


## [PyIPropertyStoreCache](PyIPropertyStoreCache.md#pyipropertystorecache)\.GetState

int = GetState\(key\)
Retrieves the current state of a property

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property identifier

#### Return Value
A value from the PSC\_STATE enum \(PSC\_NORMAL, PSC\_NOTINSOURCE\. PSC\_DIRTY\)


## [PyIPropertyStoreCache](PyIPropertyStoreCache.md#pyipropertystorecache)\.GetValueAndState

\([PyPROPVARIANT](PyPROPVARIANT.md), int\) = GetValueAndState\(key\)
Retrieves the current value and state of a property

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property identifier


## [PyIPropertyStoreCache](PyIPropertyStoreCache.md#pyipropertystorecache)\.SetState

SetState\(key, state\)
Sets the state of a property

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property identifier

  - state : int

    Value from the PSC\_STATE enum \(pscon\.PSC\_\*\)


## [PyIPropertyStoreCache](PyIPropertyStoreCache.md#pyipropertystorecache)\.SetValueAndState

SetValueAndState\(key, value, state\)
Sets the value and state of a property

#### Parameters

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property identifier

  - value : [PyPROPVARIANT](PyPROPVARIANT.md)

    The new value

  - state : int

    The new state \(pscon\.PSC\_\*\)