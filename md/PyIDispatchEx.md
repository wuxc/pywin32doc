# PyIDispatchEx


## PyIDispatchEx Object

A OLE automation client object that uses the IDispatchEx scripting interface\.\.

#### Methods

  - [GetDispID](PyIDispatchEx.md#pyidispatchexgetdispid)

    &nbsp;

  - [InvokeEx](PyIDispatchEx.md#pyidispatchexinvokeex)

    Provides access to properties and methods exposed by a PyIDispatchEx object\.&nbsp;

  - [DeleteMemberByName](PyIDispatchEx.md#pyidispatchexdeletememberbyname)

    &nbsp;

  - [DeleteMemberByDispID](PyIDispatchEx.md#pyidispatchexdeletememberbydispid)

    &nbsp;

  - [GetMemberProperties](PyIDispatchEx.md#pyidispatchexgetmemberproperties)

    &nbsp;

  - [GetMemberName](PyIDispatchEx.md#pyidispatchexgetmembername)

    Returns the name associated with a member id&nbsp;

  - [GetNextDispID](PyIDispatchEx.md#pyidispatchexgetnextdispid)

    Enumerates member ids\.&nbsp;




## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.DeleteMemberByDispID

DeleteMemberByDispID\(dispid\)

#### Parameters

  - dispid : int

    


## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.DeleteMemberByName

DeleteMemberByName\(name, fdex\)

#### Parameters

  - name : [PyUnicode](PyUnicode.md)

    Passed in name to be mapped

  - fdex : int

    Determines the options


## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.GetDispID

int = GetDispID\(name, fdex

\)
Returns the member id for a name

#### Parameters

  - name : [PyUnicode](PyUnicode.md)

    Passed in name to be mapped

  - fdex : int

    Determines the options for obtaining the member identifier\. This can be a combination of the fdex\* constants:


## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.GetMemberName

str = GetMemberName\(dispid\)
Returns the name associated with a member id

#### Parameters

  - dispid : int

    The member id


## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.GetMemberProperties

int = GetMemberProperties\(dispid, fdex

\)
Returns mask of fdex\* flags describing a member

#### Parameters

  - dispid : int

    The member id

  - fdex : int

    fdex\* flags specifying which properties to return


## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.GetNextDispID

int = GetNextDispID\(fdex, dispid

\)
Enumerates member ids\.

#### Parameters

  - fdex : int

    Determines the options

  - dispid : int

    Current member, or DISPID\_STARTENUM to begin enumeration\. GetNextDispID will retrieve the item in the enumeration after this one\.


## [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex)\.InvokeEx

object = InvokeEx\(dispid, lcid

, flags

, args

, types

, returnDesc

, serviceProvider

\)
Provides access to properties and methods exposed by a [PyIDispatchEx](PyIDispatchEx.md#pyidispatchex) object\.

#### Parameters

  - dispid : int

    

  - lcid : int

    

  - flags : int

    

  - args : \[object, \.\.\.\]

    The arguments\.

  - types=None : \[object, \.\.\.\]

    A tuple of type description object, or None if type descriptions are not available\.

  - returnDesc=1 : object|int

    If types==None, should be a BOOL indicating if the result is needed\.  If types is a tuple, then should a be type description\.

  - serviceProvider=None : [PyIServiceProvider](PyIServiceProvider.md)

    A service provider object supplied by the caller which allows the object to obtain services from the caller\. Can be None\.