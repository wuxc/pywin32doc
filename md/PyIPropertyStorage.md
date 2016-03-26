# PyIPropertyStorage

## PyIPropertyStorage Object



Structured storage object that contains a set of properties\. 

Supports iteration to list properties\.

#### Methods


  - [ReadMultiple](PyIPropertyStorage.md#pyipropertystoragereadmultiple)

    Reads specified properties from the current property set\.&nbsp;

  - [WriteMultiple](PyIPropertyStorage.md#pyipropertystoragewritemultiple)

    Creates or modifies properties in the property set&nbsp;

  - [DeleteMultiple](PyIPropertyStorage.md#pyipropertystoragedeletemultiple)

    Deletes properties from the property set&nbsp;

  - [ReadPropertyNames](PyIPropertyStorage.md#pyipropertystoragereadpropertynames)

    Retrieves any existing string names for the specified property identifiers\.&nbsp;

  - [WritePropertyNames](PyIPropertyStorage.md#pyipropertystoragewritepropertynames)

    Assigns string names to a specified array of property IDs in the current property set\.&nbsp;

  - [DeletePropertyNames](PyIPropertyStorage.md#pyipropertystoragedeletepropertynames)

    Removes property names from specified properties\.&nbsp;

  - [Commit](PyIPropertyStorage.md#pyipropertystoragecommit)

    Persists the property set to its base storage&nbsp;

  - [Revert](PyIPropertyStorage.md#pyipropertystoragerevert)

    Discards any changes that have been made&nbsp;

  - [Enum](PyIPropertyStorage.md#pyipropertystorageenum)

    Creates an enumerator for properties in the property set&nbsp;

  - [SetTimes](PyIPropertyStorage.md#pyipropertystoragesettimes)

    Sets the creation, last access, and modification time&nbsp;

  - [SetClass](PyIPropertyStorage.md#pyipropertystoragesetclass)

    Sets the GUID for the property set&nbsp;

  - [Stat](PyIPropertyStorage.md#pyipropertystoragestat)

    Returns various infomation about the property set&nbsp;

## [PyIPropertyStorage](#pyipropertystorage)\.Commit

Commit\(CommitFlags\)
Persists the property set to its base storage

#### Parameters


  - CommitFlags : int

    Combination of storagecon\.STGC\_\* flags

## [PyIPropertyStorage](#pyipropertystorage)\.DeleteMultiple

DeleteMultiple\(props\)
Deletes properties from the property set

#### Parameters


  - props : \([PROPSPEC](#propspec), \.\.\.\)

    Sequence containing names or IDs of properties to be deleted

## [PyIPropertyStorage](#pyipropertystorage)\.DeletePropertyNames

DeletePropertyNames\(props\)
Removes property names from specified properties\.

#### Parameters


  - props : \(int, \.\.\.\)

    Sequence of ints containing property IDs\.

## [PyIPropertyStorage](#pyipropertystorage)\.Enum

[PyIEnumSTATPROPSTG](#pyienumstatpropstg) =Enum\(\)
Creates an enumerator for properties in the property set

## [PyIPropertyStorage](#pyipropertystorage)\.ReadMultiple



\(object, \.\.\.\) =ReadMultiple\(props\)
Reads specified properties from the current property set\.

#### Parameters


  - props : \([PROPSPEC](#propspec), \.\.\.\)

    Sequence of property IDs or names\.

#### Return Value
Returned values are automatically converted to an appropriate python type

## [PyIPropertyStorage](#pyipropertystorage)\.ReadPropertyNames



\(str,\.\.\.\) =ReadPropertyNames\(props\)
Retrieves any existing string names for the specified property identifiers\.

#### Parameters


  - props : \(int, \.\.\.\)

    Sequence of ints containing property IDs\.

## [PyIPropertyStorage](#pyipropertystorage)\.Revert

Revert\(\)
Discards any changes that have been made

## [PyIPropertyStorage](#pyipropertystorage)\.SetClass

SetClass\(clsid\)
Sets the GUID for the property set

#### Parameters


  - clsid :[PyIID](#pyiid)

    Description for clsid

## [PyIPropertyStorage](#pyipropertystorage)\.SetTimes

SetTimes\(ctime, atime, mtime\)
Sets the creation, last access, and modification time

#### Parameters


  - ctime :[PyTime](#pytime)

    Creation time, or None for no change

  - atime :[PyTime](#pytime)

    Last access time, or None for no change

  - mtime :[PyTime](#pytime)

    Modification time, or None for no change

#### Comments


Some property sets do not support these times\.

## [PyIPropertyStorage](#pyipropertystorage)\.Stat



tuple =Stat\(\)
Returns various infomation about the property set

#### Return Value
Returns a tuple representing a STATPROPSETSTG struct\.

## [PyIPropertyStorage](#pyipropertystorage)\.WriteMultiple

WriteMultiple\(props, values, propidNameFirst\)
Creates or modifies properties in the property set

#### Parameters


  - props : \([PROPSPEC](#propspec), \.\.\.\)

    Sequence containing names or integer ids of properties to write

  - values : \(PROPVARIANT

, \.\.\.\)

    The values for the properties\.

  - propidNameFirst=2 : int

    Minimum property id to be assigned to new properties specified by name

## [PyIPropertyStorage](#pyipropertystorage)\.WritePropertyNames

WritePropertyNames\(props, names\)
Assigns string names to a specified array of property IDs in the current property set\.

#### Parameters


  - props : \(int, \.\.\.\)

    Sequence containing the property IDs\.

  - names : \(string, \.\.\.\)

    Equal length sequence of property names\.