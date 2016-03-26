# PyIClassFactory


## PyIClassFactory Object

An object which represents the IClassFactory interface\.  Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [CreateInstance](PyIClassFactory.md#pyiclassfactorycreateinstance)

    Creates an uninitialized object\.&nbsp;

  - [LockServer](PyIClassFactory.md#pyiclassfactorylockserver)

    Called by the client of a class object to keep a server open in memory, allowing instances to be created more quickly\.&nbsp;


## [PyIClassFactory](PyIClassFactory.md#pyiclassfactory)\.CreateInstance

[PyIUnknown](PyIUnknown.md) = CreateInstance\(outerUnknown, iid

\)
Creates an uninitialized object\.

#### Parameters

  - outerUnknown : [PyIUnknown](PyIUnknown.md)

    Usually None, otherwise the outer unknown if the object is being created as part of an aggregate\.

  - iid : [PyIID](PyIID.md)

    The IID of the resultant object\.

#### Return Value
The result object will always be derived from PyIUnknown, but will be of the 

type specified by iid\.


## [PyIClassFactory](PyIClassFactory.md#pyiclassfactory)\.LockServer

LockServer\(bInc\)
Called by the client of a class object to keep a server open in memory, allowing instances to be created more quickly\.

#### Parameters

  - bInc : int

    1 of the server should be locked, 0 if the server should be unlocked\.