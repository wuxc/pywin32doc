# PyGFileOperationProgressSink

## PyGFileOperationProgressSink Object

Implement-only gateway for IFileOperationProgressSink, 

used to receive events from a[PyIFileOperation](#pyifileoperation)object\.
To abort the operation, an implementation of any method can raise a 

com\_error with an appropriate HRESULT\.

#### Methods


  - [StartOperations](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkstartoperations)

    Called as operation begins, before any modifications are done&nbsp;

  - [FinishOperations](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkfinishoperations)

    Called after all actions have been performed&nbsp;

  - [PreRenameItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkprerenameitem)

    Called before each file rename&nbsp;

  - [PostRenameItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpostrenameitem)

    Called after each file rename&nbsp;

  - [PreMoveItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpremoveitem)

    Called before each move operation&nbsp;

  - [PostMoveItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpostmoveitem)

    Called after each move operation&nbsp;

  - [PreCopyItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkprecopyitem)

    Called before each copy operation&nbsp;

  - [PostCopyItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpostcopyitem)

    Called after each copy operation&nbsp;

  - [PreDeleteItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpredeleteitem)

    Called before each delete operation&nbsp;

  - [PostDeleteItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpostdeleteitem)

    Called after each delete operation&nbsp;

  - [PreNewItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkprenewitem)

    Called before each new file is created&nbsp;

  - [PostNewItem](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpostnewitem)

    Called after each new file is created&nbsp;

  - [UpdateProgress](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkupdateprogress)

    Gives an estimate of total work completed&nbsp;

  - [ResetTimer](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkresettimer)

    Not implemented, according to MSDN&nbsp;

  - [PauseTimer](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkpausetimer)

    Not implemented, according to MSDN&nbsp;

  - [ResumeTimer](PyGFileOperationProgressSink.md#pygfileoperationprogresssinkresumetimer)

    Not implemented, according to MSDN&nbsp;

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.FinishOperations

 **FinishOperations\( *Result* ** \)
Called after all actions have been performed

#### Parameters


  -  *Result* : int

    HRESULT of last operation performed

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PauseTimer

 **PauseTimer\(** \)
Not implemented, according to MSDN

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PostCopyItem

 **PostCopyItem\( *Flags*  *, Item*  *, DestinationFolder*  *, NewName*  *, hrCopy*  *, NewlyCreated* ** \)
Called after each copy operation

#### Parameters


  -  *Flags* : int

    Flags specifying copy behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    The original item

  -  *DestinationFolder* :[PyIShellItem](#pyishellitem)

    Folder into which it was copied

  -  *NewName* : str

    Name of item after copy, may be mangled in case of name conflict

  -  *hrCopy* : int

    HRESULT of the copy operation

  -  *NewlyCreated* :[PyIShellItem](#pyishellitem)

    Shell interface of the copy

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PostDeleteItem

 **PostDeleteItem\( *Flags*  *, Item*  *, hrDelete*  *, NewlyCreated* ** \)
Called after each delete operation

#### Parameters


  -  *Flags* : int

    Flags specifying delete behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    Item that was deleted

  -  *hrDelete* : int

    HRESULT of the delete operation

  -  *NewlyCreated* :[PyIShellItem](#pyishellitem)

    Item in the recycle bin, or None if deleted without recycling

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PostMoveItem

 **PostMoveItem\( *Flags*  *, Item*  *, DestinationFolder*  *, NewName*  *, hrMove*  *, NewlyCreated* ** \)
Called after each move operation

#### Parameters


  -  *Flags* : int

    Flags specifying move behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    Interface of the item before it was moved

  -  *DestinationFolder* :[PyIShellItem](#pyishellitem)

    The folder into which it was moved

  -  *NewName* : str

    Name of item in its new location, may be mangled in case of conflict

  -  *hrMove* : int

    HRESULT of the move operation

  -  *NewlyCreated* :[PyIShellItem](#pyishellitem)

    Shell interface of the item in its new location

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PostNewItem

 **PostNewItem\( *Flags*  *, DestinationFolder*  *, NewName*  *, TemplateName*  *, FileAttributes*  *, hrNew*  *, NewItem* ** \)
Called after each new file is created

#### Parameters


  -  *Flags* : int

    Flags specifying creation behaviour, combination of shellcon\.TSF\_\* flags

  -  *DestinationFolder* :[PyIShellItem](#pyishellitem)

    Folder in which item was created

  -  *NewName* : str

    Name of created item, may be mangled if file name conflicts occurred

  -  *TemplateName* : str

    Template file used to initialize new item

  -  *FileAttributes* : int

    File attributes of new item

  -  *hrNew* : int

    HRESULT of the create operation

  -  *NewItem* :[PyIShellItem](#pyishellitem)

    Shell interface of created item

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PostRenameItem

 **PostRenameItem\( *Flags*  *, Item*  *, NewName*  *, hrRename*  *, NewlyCreated* ** \)
Called after each file rename

#### Parameters


  -  *Flags* : int

    Flags specifying rename behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    Shell interface of item before rename

  -  *NewName* : str

    The new name of the item, may be mangled to resolve filename conflicts

  -  *hrRename* : int

    HRESULT of the rename operation

  -  *NewlyCreated* :[PyIShellItem](#pyishellitem)

    Shell interface of the item after rename

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PreCopyItem

 **PreCopyItem\( *Flags*  *, Item*  *, DestinationFolder*  *, NewName* ** \)
Called before each copy operation

#### Parameters


  -  *Flags* : int

    Flags specifying copy behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    The item to be copied

  -  *DestinationFolder* :[PyIShellItem](#pyishellitem)

    Folder into which it will be copied

  -  *NewName* : str

    Name to be given to the copy, will be None if keeping original name

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PreDeleteItem

 **PreDeleteItem\( *Flags*  *, Item* ** \)
Called before each delete operation

#### Parameters


  -  *Flags* : int

    Flags specifying delete behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    Item to be deleted

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PreMoveItem

 **PreMoveItem\( *Flags*  *, Item*  *, DestinationFolder*  *, NewName* ** \)
Called before each move operation

#### Parameters


  -  *Flags* : int

    Flags specifying move behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    The item to be moved

  -  *DestinationFolder* :[PyIShellItem](#pyishellitem)

    The folder into which it will be moved

  -  *NewName* : str

    Name of moved item, may be None if not to be changed

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PreNewItem

 **PreNewItem\( *Flags*  *, DestinationFolder*  *, NewName* ** \)
Called before each new file is created

#### Parameters


  -  *Flags* : int

    Flags specifying creation behaviour, combination of shellcon\.TSF\_\* flags

  -  *DestinationFolder* :[PyIShellItem](#pyishellitem)

    Folder where item will be created

  -  *NewName* : str

    Name of item to be created

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.PreRenameItem

 **PreRenameItem\( *Flags*  *, Item*  *, NewName* ** \)
Called before each file rename

#### Parameters


  -  *Flags* : int

    Flags specifying copy behaviour, combination of shellcon\.TSF\_\* flags

  -  *Item* :[PyIShellItem](#pyishellitem)

    Shell interface of the copied item

  -  *NewName* : str

    New display name of the item

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.ResetTimer

 **ResetTimer\(** \)
Not implemented, according to MSDN

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.ResumeTimer

 **ResumeTimer\(** \)
Not implemented, according to MSDN

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.StartOperations

 **StartOperations\(** \)
Called as operation begins, before any modifications are done

## [PyGFileOperationProgressSink](#pygfileoperationprogresssink)\.UpdateProgress

 **UpdateProgress\( *WorkTotal*  *, WorkSoFar* ** \)
Gives an estimate of total work completed

#### Parameters


  -  *WorkTotal* : int

    Undimensioned number representing total amount of work

  -  *WorkSoFar* : int

    Undimensioned number representing amount already completed