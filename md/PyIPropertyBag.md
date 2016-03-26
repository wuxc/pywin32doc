# PyIPropertyBag

## PyIPropertyBag Object

A Python wrapper for a COM IPropertyBag interface.

#### Comments
The IPropertyBag interface provides an object with a property bag in which the object can persistently save its properties.
When a client wishes to have exact control over how individually named properties of an object are saved, it would attempt to use an object's IPersistPropertyBag interface as a persistence mechanism. In that case the client supplies a property bag to the object in the form of an IPropertyBag interface.

#### Methods


  - [Read](PyIPropertyBag.md#pyipropertybagread)

    Called by the control to read a property from the storage provided by the container.&nbsp;

  - [Write](PyIPropertyBag.md#pyipropertybagwrite)

    Called by the control to write each property in turn to the storage provided by the container.&nbsp;


## [PyIPropertyBag](#pyipropertybag).Read

object = __Read( *propName*  *, propType*  *, errorLog* __ )
Called by the control to read a property from the storage provided by the container.

#### Parameters


  -  *propName* : str

    Name of the property to read.

  -  *propType* : int

    The type of the object to read.  Must be a VT_* Variant Type constant.

  -  *errorLog=None* :[PyIErrorLog](#pyierrorlog)

    The caller's[PyIErrorLog](#pyierrorlog)object in which the property bag stores any errors that occur during reads. Can be None in which case the caller is not interested in errors.

#### Comments
The result is a Python object, mapped from a COM VARIANT of type as specified in the propType parameter.

## [PyIPropertyBag](#pyipropertybag).Write

 __Write( *propName*  *, value* __ )
Called by the control to write each property in turn to the storage provided by the container.

#### Parameters


  -  *propName* : str

    Name of the property to read.

  -  *value* : object

    The value for the property.  The value must be able to be converted to a COM VARIANT.