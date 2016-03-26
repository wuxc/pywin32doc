# PyIStorage

## PyIStorage Object

Structured storage compound storage object

#### Comments
This object acts as an iterator through[PyIStorage::EnumElements](PyIStorage.md#pyistorageenumelements)

#### Methods


  - [CreateStream](PyIStorage.md#pyistoragecreatestream)

    Creates and opens a stream object with the specified name contained in this storage object\.&nbsp;

  - [OpenStream](PyIStorage.md#pyistorageopenstream)

    Opens an existing stream object\.&nbsp;

  - [CreateStorage](PyIStorage.md#pyistoragecreatestorage)

    Creates and opens a new storage object nested within this storage object\.&nbsp;

  - [OpenStorage](PyIStorage.md#pyistorageopenstorage)

    Opens an existing storage object with the specified name in the specified access mode\.&nbsp;

  - [CopyTo](PyIStorage.md#pyistoragecopyto)

    Copies the entire contents of an open storage object to another storage object\.&nbsp;

  - [MoveElementTo](PyIStorage.md#pyistoragemoveelementto)

    Copies or moves a substorage or stream from this storage object to another storage object\.&nbsp;

  - [Commit](PyIStorage.md#pyistoragecommit)

    Ensures that any changes made to a storage object open in transacted mode are reflected in the parent storage\.&nbsp;

  - [Revert](PyIStorage.md#pyistoragerevert)

    Discards all changes that have been made to the storage object since the last commit\.&nbsp;

  - [EnumElements](PyIStorage.md#pyistorageenumelements)

    Retrieves an enumerator object that can be used to enumerate the storage and stream objects contained within this storage object\.&nbsp;

  - [DestroyElement](PyIStorage.md#pyistoragedestroyelement)

    Removes the specified storage or stream from this storage object\.&nbsp;

  - [RenameElement](PyIStorage.md#pyistoragerenameelement)

    Renames the specified substorage or stream in this storage object\.&nbsp;

  - [SetElementTimes](PyIStorage.md#pyistoragesetelementtimes)

    Sets the modification, access, and creation times of the specified storage element, if supported by the underlying file system\.&nbsp;

  - [SetClass](PyIStorage.md#pyistoragesetclass)

    Assigns the specified CLSID to this storage object\.&nbsp;

  - [SetStateBits](PyIStorage.md#pyistoragesetstatebits)

    Stores up to 32 bits of state information in this storage object\.&nbsp;

  - [Stat](PyIStorage.md#pyistoragestat)

    Retrieves the STATSTG structure for this open storage object\.&nbsp;


## [PyIStorage](#pyistorage)\.Commit

 **Commit\( *grfCommitFlags* ** \)
Ensures that any changes made to a storage object open in transacted mode are reflected in the parent storage; 

for a root storage, reflects the changes in the actual device, for example, a file on disk\. 

For a root storage object opened in direct mode, this method has no effect except to flush all memory buffers to the disk\. For non-root storage objects in direct mode, this method has no effect\.

#### Parameters


  -  *grfCommitFlags* : int

    Controls how the changes are committed to the storage object\. See the STGC enumeration for a definition of these values\.

## [PyIStorage](#pyistorage)\.CopyTo

 **CopyTo\( *rgiidExclude*  *, snbExclude*  *, stgDest* ** \)
Copies the entire contents of an open storage object to another storage object\.

#### Parameters


  -  *rgiidExclude* : \[[PyIID](#pyiid),\]

    List of IID's to be excluded\.  Use empty seq to exclude all objects, or None to indicate no excludes\.

  -  *snbExclude* : **SNB** 

    Reserved for later - Must be None

  -  *stgDest* :[PyIStorage](#pyistorage)

    The open storage object into which this storage object is to be copied\. 

The destination storage object can be a different implementation of the[PyIStorage](#pyistorage)interface from the source storage object\. 

Thus, **IStorage::CopyTo** can only use publicly available methods of the destination storage object\. 

If stgDest is open in transacted mode, it can be reverted by calling its[PyIStorage::Revert](PyIStorage.md#pyistoragerevert)method\.

## [PyIStorage](#pyistorage)\.CreateStorage

[PyIStorage](#pyistorage)\= **CreateStorage\( *Name*  *, Mode*  *, StgFmt*  *, reserved2* ** \)
Creates and opens a new storage object nested within this storage object\.

#### Parameters


  -  *Name* : str

    The name of the newly created stream\.

  -  *Mode* : int

    Access mode - combination of storagecon\.STGM\_\* flags

  -  *StgFmt* : int

    Documented as "reserved"\!

  -  *reserved2\=0* : int

    Description for reserved2

## [PyIStorage](#pyistorage)\.CreateStream

[PyIStream](#pyistream)\= **CreateStream\( *Name*  *, Mode*  *, reserved1*  *, reserved2* ** \)
Creates and opens a stream object with the specified name contained in this storage object\. All elements within a storage object &\#151 both streams and other storage objects &\#151 are kept in the same name space\.

#### Parameters


  -  *Name* : str

    Name of the new stream

  -  *Mode* : int

    Access mode, storagecon\.STGM\_\*

  -  *reserved1\=0* : int

    Reserved - must be zero\.

  -  *reserved2\=0* : int

    Reserved - must be zero\.

## [PyIStorage](#pyistorage)\.DestroyElement

 **DestroyElement\( *name* ** \)
Removes the specified storage or stream from this storage object\.

#### Parameters


  -  *name* : string

    The name of the element to be removed\.

## [PyIStorage](#pyistorage)\.EnumElements

[PyIEnumSTATSTG](#pyienumstatstg)\= **EnumElements\( *reserved1*  *, reserved2*  *, reserved3* ** \)
Retrieves an enumerator object that can be used to enumerate the storage and stream objects contained within this storage object\.

#### Parameters


  -  *reserved1\=0* : int

    Reserved - must be zero\.

  -  *reserved2\=None* : object

    A reserved param\.  Always pass None\.  NULL is always passed to the COM function

  -  *reserved3\=0* : int

    Reserved - must be zero\.

## [PyIStorage](#pyistorage)\.MoveElementTo

 **MoveElementTo\( *Name*  *, stgDest*  *, NewName*  *, Flags* ** \)
Copies or moves a substorage or stream from this storage object to another storage object\.

#### Parameters


  -  *Name* : str

    A string that contains the name of the element in this storage object to be moved or copied\.

  -  *stgDest* :[PyIStorage](#pyistorage)

    [PyIStorage](#pyistorage)for the destination storage object\.

  -  *NewName* : str

    A string that contains the new name for the element in its new storage object\.

  -  *Flags* : int

    Specifies whether to move or copy \(storagecon\.STGMOVE\_MOVE or STGMOVE\_COPY\)

## [PyIStorage](#pyistorage)\.OpenStorage

[PyIStorage](#pyistorage)\= **OpenStorage\( *Name*  *, Priority*  *, Mode*  *, snbExclude*  *, reserved* ** \)
Opens an existing storage object with the specified name in the specified access mode\.

#### Parameters


  -  *Name* : str

    Name of the storage, or None\.

  -  *Priority* :[PyIStorage](#pyistorage)

    If the pstgPriority parameter is not None, it is a[PyIStorage](#pyistorage)object to a previous opening of an element of the storage object, 

usually one that was opened in priority mode\. The storage object should be closed and re-opened 

according to grfMode\. When the[PyIStorage::OpenStorage](PyIStorage.md#pyistorageopenstorage)method returns, pstgPriority is no longer valid - use the result value\. 

If the pstgPriority parameter is None, it is ignored\.

  -  *Mode* : int

    Access mode - combination of storagecon\.STGM\_\* flags \(must include STGM\_SHARE\_EXCLUSIVE\)

  -  *snbExclude* : **SNB** 

    Reserved for later - Must be None

  -  *reserved\=0* : int

    Reserved integer param\.

## [PyIStorage](#pyistorage)\.OpenStream

[PyIStream](#pyistream)\= **OpenStream\( *Name*  *, reserved1*  *, Mode*  *, reserved2* ** \)
Opens an existing stream object within this storage object in the specified access mode\.

#### Parameters


  -  *Name* : str

    Name of stream to be opened

  -  *reserved1* : object

    A reserved param\.  Always pass None\.  NULL is always passed to the COM function

  -  *Mode* : int

    Access mode, storagecon\.STGM\_\*

  -  *reserved2\=0* : int

    Reserved - must be zero\.

## [PyIStorage](#pyistorage)\.RenameElement

 **RenameElement\( *OldName*  *, NewName* ** \)
Renames the specified substorage or stream in this storage object\.

#### Parameters


  -  *OldName* : str

    The name of the substorage or stream to be changed\.

  -  *NewName* : str

    The new name for the specified sustorage or stream\.

## [PyIStorage](#pyistorage)\.Revert

 **Revert\(** \)
Discards all changes that have been made to the storage object since the last commit\.

## [PyIStorage](#pyistorage)\.SetClass

 **SetClass\( *clsid* ** \)
Assigns the specified CLSID to this storage object\.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    The class identifier \(CLSID\) that is to be associated with the storage object\.

## [PyIStorage](#pyistorage)\.SetElementTimes

 **SetElementTimes\( *name*  *, ctime*  *, atime*  *, mtime* ** \)
Sets the modification, access, and creation times of the specified storage element, if supported by the underlying file system\.

#### Parameters


  -  *name* : str

    The name of the storage object element whose times are to be modified\. If NULL, the time is set on the root storage rather than one of its elements\.

  -  *ctime* :[PyTime](#pytime)

    Either the new creation time for the element or None if the creation time is not to be modified\.

  -  *atime* :[PyTime](#pytime)

    Either the new access time for the element or None if the access time is not to be modified\.

  -  *mtime* :[PyTime](#pytime)

    Either the new modification time for the element or None if the modification time is not to be modified\.

## [PyIStorage](#pyistorage)\.SetStateBits

 **SetStateBits\( *grfStateBits*  *, grfMask* ** \)
Stores up to 32 bits of state information in this storage object\.

#### Parameters


  -  *grfStateBits* : int

    Specifies the new values of the bits to set\. No legal values are defined for these bits; they are all reserved for future use and must not be used by applications\.

  -  *grfMask* : int

    A binary mask indicating which bits in grfStateBits are significant in this call\.

## [PyIStorage](#pyistorage)\.Stat

[STATSTG](#statstg)\= **Stat\( *grfStatFlag* ** \)
Retrieves the STATSTG structure for this open storage object\.

#### Parameters


  -  *grfStatFlag* : int

    Specifies that some of the fields in the STATSTG structure are not returned, thus saving a memory allocation operation\. Values are taken from the STATFLAG enumeration\.