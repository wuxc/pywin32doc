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

    Changes an item's properties as specified by[PyITransferSource::SetProperties](PyITransferSource.md#pyitransfersourcesetproperties)&nbsp;

  - [GetDefaultDestinationName](PyITransferSource.md#pyitransfersourcegetdefaultdestinationname)

    Determines the name of an item as it would appear in a given folder&nbsp;

  - [EnterFolder](PyITransferSource.md#pyitransfersourceenterfolder)

    Informs the copy engine that a folder will be the target of a file operation&nbsp;

  - [LeaveFolder](PyITransferSource.md#pyitransfersourceleavefolder)

    Informs the copy engine that the operation on a destination folder is finished&nbsp;

## [PyITransferSource](#pyitransfersource)\.Advise



int =Advise\(Sink\)
Connects an advise sink to receive notifications

#### Parameters


  - Sink :[PyITransferAdviseSink](#pyitransferadvisesink)

    Event sink to respond to notifications

## [PyITransferSource](#pyitransfersource)\.ApplyPropertiesToItem

[PyIShellItem](#pyishellitem) =ApplyPropertiesToItem\(Source\)
Changes an item's properties as specified by[PyITransferSource::SetProperties](PyITransferSource.md#pyitransfersourcesetproperties)

#### Parameters


  - Source :[PyIShellItem](#pyishellitem)

    Item whose properties are to be changed

## [PyITransferSource](#pyitransfersource)\.EnterFolder



int =EnterFolder\(ChildFolderDest\)
Informs the copy engine that a folder will be the target of a file operation

#### Parameters


  - ChildFolderDest :[PyIShellItem](#pyishellitem)

    The destination folder for the operation

## [PyITransferSource](#pyitransfersource)\.GetDefaultDestinationName



str =GetDefaultDestinationName\(Source, ParentDest\)
Determines the name of an item as it would appear in a given folder

#### Parameters


  - Source :[PyIShellItem](#pyishellitem)

    The item whose name is wanted

  - ParentDest :[PyIShellItem](#pyishellitem)

    The destination folder

## [PyITransferSource](#pyitransfersource)\.LeaveFolder



int =LeaveFolder\(ChildFolderDest\)
Informs the copy engine that the operation on a destination folder is finished

#### Parameters


  - ChildFolderDest :[PyIShellItem](#pyishellitem)

    Destination folder

## [PyITransferSource](#pyitransfersource)\.LinkItem



\(int,[PyIShellItem](#pyishellitem) =LinkItem\(Source, ParentDest, NewName, flags\)
Not implemented, according to MSDN

#### Parameters


  - Source :[PyIShellItem](#pyishellitem)

    Description for psiSource

  - ParentDest :[PyIShellItem](#pyishellitem)

    Description for psiParentDest

  - NewName : str

    Description for NewName

  - flags : int

    Combination of shellcon\.TSF\_\* flags

## [PyITransferSource](#pyitransfersource)\.MoveItem



\(int,[PyIShellItem](#pyishellitem) =MoveItem\(Item, ParentDst, NameDst, flags\)
Moves a shell item into another folder

#### Parameters


  - Item :[PyIShellItem](#pyishellitem)

    Item to be moved

  - ParentDst :[PyIShellItem](#pyishellitem)

    The folder into which it will be moved

  - NameDst :unicode

    New name for item after move, None to keep same name

  - flags : int

    Combination of shellcon\.TSF\_\* flags

#### Return Value
Returns the HRESULT from the operation and the new shell item, which may be None 

when the code in one of the informational COPYENGINE\_S\_\* values\.  See MSDN for descriptions 

of expected actions for specific error codes\.

## [PyITransferSource](#pyitransfersource)\.OpenItem



\(int,[PyIShellItemResources](#pyishellitemresources)\) =OpenItem\(Item, flags, riid\)
Initiates the copying of an item

#### Parameters


  - Item :[PyIShellItem](#pyishellitem)

    The item to be copied\.

  - flags : int

    Combination of shellcon\.TSF\_\* flags

  - riid=IID\_IShellItemResources :[PyIID](#pyiid)

    The interface to return

## [PyITransferSource](#pyitransfersource)\.RecycleItem



\(int,[PyIShellItem](#pyishellitem) =RecycleItem\(Source, ParentDest, flags\)
Moves an item to the recycle bin

#### Parameters


  - Source :[PyIShellItem](#pyishellitem)

    The item to be recycled

  - ParentDest :[PyIShellItem](#pyishellitem)

    Shell item representing the recycle bin

  - flags : int

    Combination of shellcon\.TSF\_\* flags

## [PyITransferSource](#pyitransfersource)\.RemoveItem



int =RemoveItem\(Source, flags\)
Deletes an item without recycling

#### Parameters


  - Source :[PyIShellItem](#pyishellitem)

    The item to be deleted

  - flags : int

    Combination of shellcon\.TSF\_\* flags

#### Return Value
Returns the HRESULT of the operation

## [PyITransferSource](#pyitransfersource)\.RenameItem



\(int,[PyIShellItem](#pyishellitem)\) =RenameItem\(Source, NewName, flags\)
Renames a shell item

#### Parameters


  - Source :[PyIShellItem](#pyishellitem)

    Item to be renamed

  - NewName : str

    The name to be given to the item

  - flags : int

    Combination of shellcon\.TSF\_\* flags

## [PyITransferSource](#pyitransfersource)\.SetProperties

SetProperties\(proparray\)
Specifies changes to be applied to items' properties

#### Parameters


  - proparray :[PyIPropertyChangeArray](#pyipropertychangearray)

    Property changes to be applied by[PyITransferSource::ApplyPropertiesToItem](PyITransferSource.md#pyitransfersourceapplypropertiestoitem)

## [PyITransferSource](#pyitransfersource)\.Unadvise

Unadvise\(Cookie\)
Disconnects an event sink

#### Parameters


  - Cookie : int

    Connection id as returned by[PyITransferSource::Advise](PyITransferSource.md#pyitransfersourceadvise)