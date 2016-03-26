# PyIRunningObjectTable


## PyIRunningObjectTable Object

A Python interface to IRunningObjectTable

#### Methods

  - [Register](PyIRunningObjectTable.md#pyirunningobjecttableregister)

    Registers an object in the ROT&nbsp;

  - [Revoke](PyIRunningObjectTable.md#pyirunningobjecttablerevoke)

    Revokes a previously registered object&nbsp;

  - [IsRunning](PyIRunningObjectTable.md#pyirunningobjecttableisrunning)

    Checks whether an object is running\.&nbsp;

  - [GetObject](PyIRunningObjectTable.md#pyirunningobjecttablegetobject)

    Checks whether an object is running\.&nbsp;

  - [EnumRunning](PyIRunningObjectTable.md#pyirunningobjecttableenumrunning)

    Creates an enumerator that can list the monikers of all the objects currently registered in the Running Object Table \(ROT\)\.&nbsp;




## [PyIRunningObjectTable](PyIRunningObjectTable.md#pyirunningobjecttable)\.EnumRunning

[PyIEnumMoniker](PyIEnumMoniker.md) = EnumRunning\(\)
Creates an enumerator that can list the monikers of all the objects currently registered in the Running Object Table \(ROT\)\.


## [PyIRunningObjectTable](PyIRunningObjectTable.md#pyirunningobjecttable)\.GetObject

[PyIUnknown](PyIUnknown.md) = GetObject\(objectName\)
Checks whether an object is running\.

#### Parameters

  - objectName : [PyIMoniker](PyIMoniker.md)

    The [PyIMoniker](PyIMoniker.md) interface on the moniker to search for in the Running Object Table\.


## [PyIRunningObjectTable](PyIRunningObjectTable.md#pyirunningobjecttable)\.IsRunning

int = IsRunning\(objectName\)
Checks whether an object is running\.

#### Parameters

  - objectName : [PyIMoniker](PyIMoniker.md)

    The [PyIMoniker](PyIMoniker.md) interface on the moniker to search for in the Running Object Table\.


## [PyIRunningObjectTable](PyIRunningObjectTable.md#pyirunningobjecttable)\.Register

int = Register\(\)
Registers an object and its identifying moniker in the Running Object Table \(ROT\)\.


## [PyIRunningObjectTable](PyIRunningObjectTable.md#pyirunningobjecttable)\.Revoke

int = Revoke\(\)
Removes from the Running Object Table 

\(ROT\) an entry that was previously registered by a call to [PyIRunningObjectTable::Register](PyIRunningObjectTable.md#pyirunningobjecttableregister)\.