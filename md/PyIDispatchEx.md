# PyIDispatchEx

## PyIDispatchEx Object

A OLE automation client object that uses the IDispatchEx scripting interface..

#### Methods


  - [GetDispID](PyIDispatchEx.md#pyidispatchexgetdispid)

    &nbsp;

  - [InvokeEx](PyIDispatchEx.md#pyidispatchexinvokeex)

    Provides access to properties and methods exposed by a __PyIDispatchEx__ object.&nbsp;

  - [DeleteMemberByName](PyIDispatchEx.md#pyidispatchexdeletememberbyname)

    &nbsp;

  - [DeleteMemberByDispID](PyIDispatchEx.md#pyidispatchexdeletememberbydispid)

    &nbsp;

  - [GetMemberProperties](PyIDispatchEx.md#pyidispatchexgetmemberproperties)

    &nbsp;

  - [GetMemberName](PyIDispatchEx.md#pyidispatchexgetmembername)

    Returns the name associated with a member id&nbsp;

  - [GetNextDispID](PyIDispatchEx.md#pyidispatchexgetnextdispid)

    Enumerates member ids.&nbsp;


## [PyIDispatchEx](#pyidispatchex).DeleteMemberByDispID

 __DeleteMemberByDispID( *dispid* __ )


#### Parameters


  -  *dispid* : int

    

## [PyIDispatchEx](#pyidispatchex).DeleteMemberByName

 __DeleteMemberByName( *name*  *, fdex* __ )


#### Parameters


  -  *name* :[PyUnicode](#pyunicode)

    Passed in name to be mapped

  -  *fdex* : int

    Determines the options

## [PyIDispatchEx](#pyidispatchex).GetDispID

int = __GetDispID( *name*  *, fdex* __ )
Returns the member id for a name

#### Parameters


  -  *name* :[PyUnicode](#pyunicode)

    Passed in name to be mapped

  -  *fdex* : int

    Determines the options for obtaining the member identifier. This can be a combination of the fdex* constants:

## [PyIDispatchEx](#pyidispatchex).GetMemberName

str = __GetMemberName( *dispid* __ )
Returns the name associated with a member id

#### Parameters


  -  *dispid* : int

    The member id

## [PyIDispatchEx](#pyidispatchex).GetMemberProperties

int = __GetMemberProperties( *dispid*  *, fdex* __ )
Returns mask of fdex* flags describing a member

#### Parameters


  -  *dispid* : int

    The member id

  -  *fdex* : int

    fdex* flags specifying which properties to return

## [PyIDispatchEx](#pyidispatchex).GetNextDispID

int = __GetNextDispID( *fdex*  *, dispid* __ )
Enumerates member ids.

#### Parameters


  -  *fdex* : int

    Determines the options

  -  *dispid* : int

    Current member, or DISPID_STARTENUM to begin enumeration. GetNextDispID will retrieve the item in the enumeration after this one.

## [PyIDispatchEx](#pyidispatchex).InvokeEx

object = __InvokeEx( *dispid*  *, lcid*  *, flags*  *, args*  *, types*  *, returnDesc*  *, serviceProvider* __ )
Provides access to properties and methods exposed by a[PyIDispatchEx](#pyidispatchex)object.

#### Parameters


  -  *dispid* : int

    

  -  *lcid* : int

    

  -  *flags* : int

    

  -  *args* : [object, ...]

    The arguments.

  -  *types=None* : [object, ...]

    A tuple of type description object, or None if type descriptions are not available.

  -  *returnDesc=1* : object|int

    If types==None, should be a BOOL indicating if the result is needed.  If types is a tuple, then should a be type description.

  -  *serviceProvider=None* :[PyIServiceProvider](#pyiserviceprovider)

    A service provider object supplied by the caller which allows the object to obtain services from the caller. Can be None.