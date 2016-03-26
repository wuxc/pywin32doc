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

## [PyITransferSource](#pyitransfersource).Advise

int = __Advise( *Sink* __ )
Connects an advise sink to receive notifications

#### Parameters


  -  *Sink* :[PyITransferAdviseSink](#pyitransferadvisesink)

    Event sink to respond to notifications

## [PyITransferSource](#pyitransfersource).ApplyPropertiesToItem

[PyIShellItem](#pyishellitem)= __ApplyPropertiesToItem( *Source* __ )
Changes an item's properties as specified by[PyITransferSource::SetProperties](PyITransferSource.md#pyitransfersourcesetproperties)

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    Item whose properties are to be changed

## [PyITransferSource](#pyitransfersource).EnterFolder

int = __EnterFolder( *ChildFolderDest* __ )
Informs the copy engine that a folder will be the target of a file operation

#### Parameters


  -  *ChildFolderDest* :[PyIShellItem](#pyishellitem)

    The destination folder for the operation

## [PyITransferSource](#pyitransfersource).GetDefaultDestinationName

str = __GetDefaultDestinationName( *Source*  *, ParentDest* __ )
Determines the name of an item as it would appear in a given folder

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    The item whose name is wanted

  -  *ParentDest* :[PyIShellItem](#pyishellitem)

    The destination folder

## [PyITransferSource](#pyitransfersource).LeaveFolder

int = __LeaveFolder( *ChildFolderDest* __ )
Informs the copy engine that the operation on a destination folder is finished

#### Parameters


  -  *ChildFolderDest* :[PyIShellItem](#pyishellitem)

    Destination folder

## [PyITransferSource](#pyitransfersource).LinkItem

(int,[PyIShellItem](#pyishellitem)= __LinkItem( *Source*  *, ParentDest*  *, NewName*  *, flags* __ )
Not implemented, according to MSDN

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    Description for psiSource

  -  *ParentDest* :[PyIShellItem](#pyishellitem)

    Description for psiParentDest

  -  *NewName* : str

    Description for NewName

  -  *flags* : int

    Combination of shellcon.TSF_* flags

## [PyITransferSource](#pyitransfersource).MoveItem

(int,[PyIShellItem](#pyishellitem)= __MoveItem( *Item*  *, ParentDst*  *, NameDst*  *, flags* __ )
Moves a shell item into another folder

#### Parameters


  -  *Item* :[PyIShellItem](#pyishellitem)

    Item to be moved

  -  *ParentDst* :[PyIShellItem](#pyishellitem)

    The folder into which it will be moved

  -  *NameDst* : __unicode__ 

    New name for item after move, None to keep same name

  -  *flags* : int

    Combination of shellcon.TSF_* flags

#### Return Value
Returns the HRESULT from the operation and the new shell item, which may be None 

when the code in one of the informational COPYENGINE_S_* values.  See MSDN for descriptions 

of expected actions for specific error codes.

## [PyITransferSource](#pyitransfersource).OpenItem

(int,[PyIShellItemResources](#pyishellitemresources)) = __OpenItem( *Item*  *, flags*  *, riid* __ )
Initiates the copying of an item

#### Parameters


  -  *Item* :[PyIShellItem](#pyishellitem)

    The item to be copied.

  -  *flags* : int

    Combination of shellcon.TSF_* flags

  -  *riid=IID_IShellItemResources* :[PyIID](#pyiid)

    The interface to return

## [PyITransferSource](#pyitransfersource).RecycleItem

(int,[PyIShellItem](#pyishellitem)= __RecycleItem( *Source*  *, ParentDest*  *, flags* __ )
Moves an item to the recycle bin

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    The item to be recycled

  -  *ParentDest* :[PyIShellItem](#pyishellitem)

    Shell item representing the recycle bin

  -  *flags* : int

    Combination of shellcon.TSF_* flags

## [PyITransferSource](#pyitransfersource).RemoveItem

int = __RemoveItem( *Source*  *, flags* __ )
Deletes an item without recycling

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    The item to be deleted

  -  *flags* : int

    Combination of shellcon.TSF_* flags

#### Return Value
Returns the HRESULT of the operation

## [PyITransferSource](#pyitransfersource).RenameItem

(int,[PyIShellItem](#pyishellitem)) = __RenameItem( *Source*  *, NewName*  *, flags* __ )
Renames a shell item

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    Item to be renamed

  -  *NewName* : str

    The name to be given to the item

  -  *flags* : int

    Combination of shellcon.TSF_* flags

## [PyITransferSource](#pyitransfersource).SetProperties

 __SetProperties( *proparray* __ )
Specifies changes to be applied to items' properties

#### Parameters


  -  *proparray* :[PyIPropertyChangeArray](#pyipropertychangearray)

    Property changes to be applied by[PyITransferSource::ApplyPropertiesToItem](PyITransferSource.md#pyitransfersourceapplypropertiestoitem)

## [PyITransferSource](#pyitransfersource).Unadvise

 __Unadvise( *Cookie* __ )
Disconnects an event sink

#### Parameters


  -  *Cookie* : int

    Connection id as returned by[PyITransferSource::Advise](PyITransferSource.md#pyitransfersourceadvise)