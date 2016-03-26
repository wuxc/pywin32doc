# PyIPersistPropertyBag

## PyIPersistPropertyBag Object

A Python wrapper for a COM IPersistPropertyBag interface.

#### Methods


  - [InitNew](PyIPersistPropertyBag.md#pyipersistpropertybaginitnew)

    Called by the container when the control is initialized to initialize the property bag.&nbsp;

  - [Load](PyIPersistPropertyBag.md#pyipersistpropertybagload)

    Called by the container to load the control's properties.&nbsp;

  - [Save](PyIPersistPropertyBag.md#pyipersistpropertybagsave)

    Called by the container to save the object's properties.&nbsp;


## [PyIPersistPropertyBag](#pyipersistpropertybag).InitNew

 __InitNew(__ )
Called by the container when the control is initialized to initialize the property bag.

## [PyIPersistPropertyBag](#pyipersistpropertybag).Load

 __Load( *bag*  *, log* __ )
Called by the container to load the control's properties.

#### Parameters


  -  *bag* :[PyIPropertyBag](#pyipropertybag)

    the caller's property bag.

  -  *log=None* :[PyIErrorLog](#pyierrorlog)

    the caller's error log, or None

## [PyIPersistPropertyBag](#pyipersistpropertybag).Save

 __Save( *bag*  *, clearDirty*  *, saveProperties* __ )
Called by the container to save the object's properties.

#### Parameters


  -  *bag* :[PyIPropertyBag](#pyipropertybag)

    the caller's property bag.

  -  *clearDirty* : int

    Specifies whether to clear the dirty flag.

  -  *saveProperties* : int

    Specifies whether to save all properties or just those that have changed