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


## [PyIRunningObjectTable](#pyirunningobjecttable)\.EnumRunning

[PyIEnumMoniker](#pyienummoniker) =EnumRunning\(\)
Creates an enumerator that can list the monikers of all the objects currently registered in the Running Object Table \(ROT\)\.

## [PyIRunningObjectTable](#pyirunningobjecttable)\.GetObject

[PyIUnknown](#pyiunknown) =GetObject\(objectName\)
Checks whether an object is running\.

#### Parameters


  - objectName :[PyIMoniker](#pyimoniker)

    The[PyIMoniker](#pyimoniker) interface on the moniker to search for in the Running Object Table\.

## [PyIRunningObjectTable](#pyirunningobjecttable)\.IsRunning



int =IsRunning\(objectName\)
Checks whether an object is running\.

#### Parameters


  - objectName :[PyIMoniker](#pyimoniker)

    The[PyIMoniker](#pyimoniker) interface on the moniker to search for in the Running Object Table\.

## [PyIRunningObjectTable](#pyirunningobjecttable)\.Register



int =Register\(\)
Registers an object and its identifying moniker in the Running Object Table \(ROT\)\.

## [PyIRunningObjectTable](#pyirunningobjecttable)\.Revoke



int =Revoke\(\)
Removes from the Running Object Table 

\(ROT\) an entry that was previously registered by a call to[PyIRunningObjectTable::Register](PyIRunningObjectTable.md#pyirunningobjecttableregister)\.