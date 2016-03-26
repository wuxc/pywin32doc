# PyIPropertySetStorage

## PyIPropertySetStorage Object



Container for a collection of property sets\. 

Can be iterated over to enumerate property sets\.

#### Methods


  - [Create](PyIPropertySetStorage.md#pyipropertysetstoragecreate)

    Creates a new property set in the storage object&nbsp;

  - [Open](PyIPropertySetStorage.md#pyipropertysetstorageopen)

    Opens an existing property set&nbsp;

  - [Delete](PyIPropertySetStorage.md#pyipropertysetstoragedelete)

    Removes a property set from this storage object&nbsp;

  - [Enum](PyIPropertySetStorage.md#pyipropertysetstorageenum)

    Creates an iterator to enumerate contained property sets&nbsp;

## [PyIPropertySetStorage](#pyipropertysetstorage)\.Create

[PyIPropertyStorage](#pyipropertystorage) =Create\(fmtid, clsid, Flags, Mode\)
Creates a new property set in the storage object

#### Parameters


  - fmtid :[PyIID](#pyiid)

    GUID identifying a property set, pythoncom\.FMTID\_\*

  - clsid :[PyIID](#pyiid)

    CLSID of property set handler, usually same as fmtid

  - Flags : int

    Specifies behaviour of property set, storagecon\.PROPSETFLAG\_\*

  - Mode : int

    Access mode, combination of storagecon\.STGM\_\* flags

## [PyIPropertySetStorage](#pyipropertysetstorage)\.Delete

Delete\(fmtid\)
Removes a property set from this storage object

#### Parameters


  - fmtid :[PyIID](#pyiid)

    GUID of a property set, pythoncom\.FMTID\_\*

## [PyIPropertySetStorage](#pyipropertysetstorage)\.Enum

[PyIEnumSTATPROPSETSTG](#pyienumstatpropsetstg) =Enum\(\)
Creates an iterator to enumerate contained property sets

## [PyIPropertySetStorage](#pyipropertysetstorage)\.Open

[PyIPropertyStorage](#pyipropertystorage) =Open\(fmtid, Mode\)
Opens an existing property set

#### Parameters


  - fmtid :[PyIID](#pyiid)

    GUID of a property set, pythoncom\.FMTID\_\*

  - Mode=STGM\_READ | STGM\_SHARE\_EXCLUSIVE : int

    Access mode, combination of storagecon\.STGM\_\* flags