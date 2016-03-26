# PyIPropertySetStorage

## PyIPropertySetStorage Object

Container for a collection of property sets. 

Can be iterated over to enumerate property sets.

#### Methods


  - [Create](PyIPropertySetStorage.md#pyipropertysetstoragecreate)

    Creates a new property set in the storage object&nbsp;

  - [Open](PyIPropertySetStorage.md#pyipropertysetstorageopen)

    Opens an existing property set&nbsp;

  - [Delete](PyIPropertySetStorage.md#pyipropertysetstoragedelete)

    Removes a property set from this storage object&nbsp;

  - [Enum](PyIPropertySetStorage.md#pyipropertysetstorageenum)

    Creates an iterator to enumerate contained property sets&nbsp;

## [PyIPropertySetStorage](#pyipropertysetstorage).Create

[PyIPropertyStorage](#pyipropertystorage)= __Create( *fmtid*  *, clsid*  *, Flags*  *, Mode* __ )
Creates a new property set in the storage object

#### Parameters


  -  *fmtid* :[PyIID](#pyiid)

    GUID identifying a property set, pythoncom.FMTID_*

  -  *clsid* :[PyIID](#pyiid)

    CLSID of property set handler, usually same as fmtid

  -  *Flags* : int

    Specifies behaviour of property set, storagecon.PROPSETFLAG_*

  -  *Mode* : int

    Access mode, combination of storagecon.STGM_* flags

## [PyIPropertySetStorage](#pyipropertysetstorage).Delete

 __Delete( *fmtid* __ )
Removes a property set from this storage object

#### Parameters


  -  *fmtid* :[PyIID](#pyiid)

    GUID of a property set, pythoncom.FMTID_*

## [PyIPropertySetStorage](#pyipropertysetstorage).Enum

[PyIEnumSTATPROPSETSTG](#pyienumstatpropsetstg)= __Enum(__ )
Creates an iterator to enumerate contained property sets

## [PyIPropertySetStorage](#pyipropertysetstorage).Open

[PyIPropertyStorage](#pyipropertystorage)= __Open( *fmtid*  *, Mode* __ )
Opens an existing property set

#### Parameters


  -  *fmtid* :[PyIID](#pyiid)

    GUID of a property set, pythoncom.FMTID_*

  -  *Mode=STGM_READ | STGM_SHARE_EXCLUSIVE* : int

    Access mode, combination of storagecon.STGM_* flags