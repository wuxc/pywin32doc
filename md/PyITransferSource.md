# PyITransferSource


## PyITransferSource Object

Implemented by shell folders that can act as the source of shell item operations

#### Methods

  - [Advise](PyITransferSource.md#pyitransfersourceadvise)

    Connects an advise sink to receive notifications&nbsp;

  - [Unadvise](PyITransferSource.md#pyitransfersourceunadvise)

    Disconnects an event sink&nbsp;

  - [SetProperties](PyITransferSource.md#pyitransfersourcesetproperties)

    Specifies changes to be applied to items' properties&nbsp;

  - [OpenItem](PyITransferSource.md#pyitransfersourceopenitem)

    Initiates the copying of an item&nbsp;

  - [MoveItem](PyITransferSource.md#pyitransfersourcemoveitem)

    Moves a shell item into another folder&nbsp;

  - [RecycleItem](PyITransferSource.md#pyitransfersourcerecycleitem)

    Moves an item to the recycle bin&nbsp;

  - [RemoveItem](PyITransferSource.md#pyitransfersourceremoveitem)

    Deletes an item without recycling&nbsp;

  - [RenameItem](PyITransferSource.md#pyitransfersourcerenameitem)

    Renames a shell item&nbsp;

  - [LinkItem](PyITransferSource.md#pyitransfersourcelinkitem)

    Not implemented, according to MSDN&nbsp;

  - [ApplyPropertiesToItem](PyITransferSource.md#pyitransfersourceapplypropertiestoitem)

    Changes an item's properties as specified by [PyITransferSource::SetProperties](PyITransferSource.md#pyitransfersourcesetproperties)&nbsp;

  - [GetDefaultDestinationName](PyITransferSource.md#pyitransfersourcegetdefaultdestinationname)

    Determines the name of an item as it would appear in a given folder&nbsp;

  - [EnterFolder](PyITransferSource.md#pyitransfersourceenterfolder)

    Informs the copy engine that a folder will be the target of a file operation&nbsp;

  - [LeaveFolder](PyITransferSource.md#pyitransfersourceleavefolder)

    Informs the copy engine that the operation on a destination folder is finished&nbsp;


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.Advise

int = Advise\(Sink\)
Connects an advise sink to receive notifications

#### Parameters

  - Sink : [PyITransferAdviseSink](PyITransferAdviseSink.md)

    Event sink to respond to notifications


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.ApplyPropertiesToItem

[PyIShellItem](PyIShellItem.md) = ApplyPropertiesToItem\(Source\)
Changes an item's properties as specified by [PyITransferSource::SetProperties](PyITransferSource.md#pyitransfersourcesetproperties)

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    Item whose properties are to be changed


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.EnterFolder

int = EnterFolder\(ChildFolderDest\)
Informs the copy engine that a folder will be the target of a file operation

#### Parameters

  - ChildFolderDest : [PyIShellItem](PyIShellItem.md)

    The destination folder for the operation


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.GetDefaultDestinationName

str = GetDefaultDestinationName\(Source, ParentDest

\)
Determines the name of an item as it would appear in a given folder

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    The item whose name is wanted

  - ParentDest : [PyIShellItem](PyIShellItem.md)

    The destination folder


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.LeaveFolder

int = LeaveFolder\(ChildFolderDest\)
Informs the copy engine that the operation on a destination folder is finished

#### Parameters

  - ChildFolderDest : [PyIShellItem](PyIShellItem.md)

    Destination folder


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.LinkItem

\(int, [PyIShellItem](PyIShellItem.md) = LinkItem\(Source, ParentDest

, NewName

, flags

\)
Not implemented, according to MSDN

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    Description for psiSource

  - ParentDest : [PyIShellItem](PyIShellItem.md)

    Description for psiParentDest

  - NewName : str

    Description for NewName

  - flags : int

    Combination of shellcon\.TSF\_\* flags


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.MoveItem

\(int, [PyIShellItem](PyIShellItem.md) = MoveItem\(Item, ParentDst

, NameDst

, flags

\)
Moves a shell item into another folder

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    Item to be moved

  - ParentDst : [PyIShellItem](PyIShellItem.md)

    The folder into which it will be moved

  - NameDst : unicode

    New name for item after move, None to keep same name

  - flags : int

    Combination of shellcon\.TSF\_\* flags

#### Return Value
Returns the HRESULT from the operation and the new shell item, which may be None 

when the code in one of the informational COPYENGINE\_S\_\* values\.  See MSDN for descriptions 

of expected actions for specific error codes\.


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.OpenItem

\(int, [PyIShellItemResources](PyIShellItemResources.md)\) = OpenItem\(Item, flags

, riid

\)
Initiates the copying of an item

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The item to be copied\.

  - flags : int

    Combination of shellcon\.TSF\_\* flags

  - riid=IID\_IShellItemResources : [PyIID](PyIID.md)

    The interface to return


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.RecycleItem

\(int, [PyIShellItem](PyIShellItem.md) = RecycleItem\(Source, ParentDest

, flags

\)
Moves an item to the recycle bin

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    The item to be recycled

  - ParentDest : [PyIShellItem](PyIShellItem.md)

    Shell item representing the recycle bin

  - flags : int

    Combination of shellcon\.TSF\_\* flags


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.RemoveItem

int = RemoveItem\(Source, flags

\)
Deletes an item without recycling

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    The item to be deleted

  - flags : int

    Combination of shellcon\.TSF\_\* flags

#### Return Value
Returns the HRESULT of the operation


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.RenameItem

\(int, [PyIShellItem](PyIShellItem.md)\) = RenameItem\(Source, NewName

, flags

\)
Renames a shell item

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    Item to be renamed

  - NewName : str

    The name to be given to the item

  - flags : int

    Combination of shellcon\.TSF\_\* flags


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.SetProperties

SetProperties\(proparray\)
Specifies changes to be applied to items' properties

#### Parameters

  - proparray : [PyIPropertyChangeArray](PyIPropertyChangeArray.md)

    Property changes to be applied by [PyITransferSource::ApplyPropertiesToItem](PyITransferSource.md#pyitransfersourceapplypropertiestoitem)


## [PyITransferSource](PyITransferSource.md#pyitransfersource)\.Unadvise

Unadvise\(Cookie\)
Disconnects an event sink

#### Parameters

  - Cookie : int

    Connection id as returned by [PyITransferSource::Advise](PyITransferSource.md#pyitransfersourceadvise)