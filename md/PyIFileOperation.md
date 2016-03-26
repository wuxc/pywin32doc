# PyIFileOperation


## PyIFileOperation Object

Interface used to build a collection of file system modifications to be 

performed by the shell as a unit\.  Serves as a replacement for [shell::SHFileOperation](shell.md#shellshfileoperation)\. 

No changes are actually made until PerformOperations is called\. 

Progress can be monitored by implementing [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)\. 

Requires Vista or later\.

#### Methods

  - [Advise](PyIFileOperation.md#pyifileoperationadvise)

    Connects an event sink to receive updates&nbsp;

  - [Unadvise](PyIFileOperation.md#pyifileoperationunadvise)

    Disconnects a progress sink&nbsp;

  - [SetOperationFlags](PyIFileOperation.md#pyifileoperationsetoperationflags)

    Sets option flags&nbsp;

  - [SetProgressMessage](PyIFileOperation.md#pyifileoperationsetprogressmessage)

    Not implemented&nbsp;

  - [SetProgressDialog](PyIFileOperation.md#pyifileoperationsetprogressdialog)

    Provides an interface used to display progress&nbsp;

  - [SetProperties](PyIFileOperation.md#pyifileoperationsetproperties)

    Specifies a set of properties to be changed&nbsp;

  - [SetOwnerWindow](PyIFileOperation.md#pyifileoperationsetownerwindow)

    Sets the parent window for any UI displayed\.&nbsp;

  - [ApplyPropertiesToItem](PyIFileOperation.md#pyifileoperationapplypropertiestoitem)

    Specifies the item that will receive property changes&nbsp;

  - [ApplyPropertiesToItems](PyIFileOperation.md#pyifileoperationapplypropertiestoitems)

    Specifies multiple items that will receive property changes&nbsp;

  - [RenameItem](PyIFileOperation.md#pyifileoperationrenameitem)

    Adds a rename to the operation sequence&nbsp;

  - [RenameItems](PyIFileOperation.md#pyifileoperationrenameitems)

    Adds multiple renames to the operation sequence&nbsp;

  - [MoveItem](PyIFileOperation.md#pyifileoperationmoveitem)

    Adds a move operation to the configuration&nbsp;

  - [MoveItems](PyIFileOperation.md#pyifileoperationmoveitems)

    Adds multiple move operations to the configuration&nbsp;

  - [CopyItem](PyIFileOperation.md#pyifileoperationcopyitem)

    Adds a copy operation to the configuration&nbsp;

  - [CopyItems](PyIFileOperation.md#pyifileoperationcopyitems)

    Adds multiple copy operations to the configuration&nbsp;

  - [DeleteItem](PyIFileOperation.md#pyifileoperationdeleteitem)

    Adds a delete operation to the configuration&nbsp;

  - [DeleteItems](PyIFileOperation.md#pyifileoperationdeleteitems)

    Adds multiple delete operations to the configuration&nbsp;

  - [NewItem](PyIFileOperation.md#pyifileoperationnewitem)

    Creates a new file as part of the operation&nbsp;

  - [PerformOperations](PyIFileOperation.md#pyifileoperationperformoperations)

    Effects all configured file system modifications&nbsp;

  - [GetAnyOperationsAborted](PyIFileOperation.md#pyifileoperationgetanyoperationsaborted)

    Determines if any operations were terminated&nbsp;


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.Advise

int = Advise\(Sink\)
Connects an event sink to receive updates

#### Parameters

  - Sink : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Interface that receives progress updates

#### Return Value
Returns a cookie to be passed to [PyIFileOperation::Unadvise](PyIFileOperation.md#pyifileoperationunadvise) to disconnect


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.ApplyPropertiesToItem

ApplyPropertiesToItem\(Item\)
Specifies the item that will receive property changes

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The item to which property changes will be applied


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.ApplyPropertiesToItems

ApplyPropertiesToItems\(Items\)
Specifies multiple items that will receive property changes

#### Parameters

  - Items : [PyIUnknown](PyIUnknown.md)

    [PyIShellItemArray](PyIShellItemArray.md), [PyIDataObject](PyIDataObject.md), or [PyIEnumShellItems](PyIEnumShellItems.md) containing the target items


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.CopyItem

CopyItem\(Item, DestinationFolder, CopyName, Sink\)
Adds a copy operation to the configuration

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    Item to be copied

  - DestinationFolder : [PyIShellItem](PyIShellItem.md)

    Folder into which it will be copied

  - CopyName=None : str

    New name for the copied file, use None to keep original name

  - Sink=None : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Progress sink for just this operation


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.CopyItems

CopyItems\(Items, DestinationFolder\)
Adds multiple copy operations to the configuration

#### Parameters

  - Items : [PyIUnknown](PyIUnknown.md)

    [PyIShellItemArray](PyIShellItemArray.md), [PyIDataObject](PyIDataObject.md), or [PyIEnumShellItems](PyIEnumShellItems.md) containing items to be copied

  - DestinationFolder : [PyIShellItem](PyIShellItem.md)

    Folder into which they will be copied


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.DeleteItem

DeleteItem\(Item, Sink\)
Adds a delete operation to the configuration

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    Description for psiItem

  - Sink=None : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Progress sink for just this operation


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.DeleteItems

DeleteItems\(Items\)
Adds multiple delete operations to the configuration

#### Parameters

  - Items : [PyIUnknown](PyIUnknown.md)

    [PyIShellItemArray](PyIShellItemArray.md), [PyIDataObject](PyIDataObject.md), or [PyIEnumShellItems](PyIEnumShellItems.md) containing the items to be deleted


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.GetAnyOperationsAborted

boolean = GetAnyOperationsAborted\(\)
Determines if any operations were terminated


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.MoveItem

MoveItem\(Item, DestinationFolder, pszNewName, Sink\)
Adds a move operation to the configuration

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The item to be moved

  - DestinationFolder : [PyIShellItem](PyIShellItem.md)

    The folder into which it will be moved

  - pszNewName=None : str

    Name to be given to moved item, use None to keep original name

  - Sink=None : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Progress sink to receive notification for just this operation


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.MoveItems

MoveItems\(Items, DestinationFolder\)
Adds multiple move operations to the configuration

#### Parameters

  - Items : [PyIUnknown](PyIUnknown.md)

    [PyIShellItemArray](PyIShellItemArray.md), [PyIDataObject](PyIDataObject.md), or [PyIEnumShellItems](PyIEnumShellItems.md) containing the items to be moved

  - DestinationFolder : [PyIShellItem](PyIShellItem.md)

    Folder into which all items will be moved


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.NewItem

NewItem\(DestinationFolder, FileAttributes, Name, TemplateName, Sink\)
Creates a new file as part of the operation

#### Parameters

  - DestinationFolder : [PyIShellItem](PyIShellItem.md)

    Folder in which to create the file

  - FileAttributes : int

    Combination of win32con\.FILE\_ATTRIBUTE\_\* flags

  - Name : str

    Name of the new file

  - TemplateName=None : str

    Template file used to initialize the new file

  - Sink=None : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Progress sink for just this operation


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.PerformOperations

PerformOperations\(\)
Effects all configured file system modifications


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.RenameItem

RenameItem\(Item, NewName, Sink\)
Adds a rename to the operation sequence

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The item to be renamed

  - NewName : str

    The new name

  - Sink=None : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Progress sink for this operation only\.


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.RenameItems

RenameItems\(pUnkItems, NewName\)
Adds multiple renames to the operation sequence

#### Parameters

  - pUnkItems : [PyIUnknown](PyIUnknown.md)

    [PyIShellItemArray](PyIShellItemArray.md), [PyIDataObject](PyIDataObject.md), or [PyIEnumShellItems](PyIEnumShellItems.md) containing items to be renamed

  - NewName : str

    New name for all items\.  Collisions handled automatically\.


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.SetOperationFlags

SetOperationFlags\(OperationFlags\)
Sets option flags for the operation

#### Parameters

  - OperationFlags : int

    Combination of shellcon\.FOF\_\* and FOFX\_\* flags


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.SetOwnerWindow

SetOwnerWindow\(Owner\)
Sets the parent window for any UI displayed\.

#### Parameters

  - Owner : [PyHANDLE](PyHANDLE.md)

    Handle to parent window


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.SetProgressDialog

SetProgressDialog\(popd\)
Provides an interface used to display a progress dialog

#### Parameters

  - popd : PyIOperationsProgressDialog

    Progress dialog interface

#### Comments

IOperationsProgressDialog is not yet supported


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.SetProgressMessage

SetProgressMessage\(Message\)
Not implemented\.

#### Parameters

  - Message : str

    Description for Message


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.SetProperties

SetProperties\(proparray\)
Specifies a set of properties to be changed\.

#### Parameters

  - proparray : [PyIPropertyChangeArray](PyIPropertyChangeArray.md)

    Sequence of property changes to be performed \(see [propsys::PSCreatePropertyChangeArray](propsys.md#propsyspscreatepropertychangearray)\)

#### Comments

Note that these properties will be set for \*any\* files created by the operation, not 

just items passed to ApplyPropertiesToItem\(s\)\.  New items created as the result of a 

rename, copy, or move must have a property handler, or the operation fails with the vague 

com\_error: \(-2147467259, 'Unspecified error', None, None\) \(E\_FAIL, or 0x80004005 in hex\) 

even though the given file operation was actually performed\.


## [PyIFileOperation](PyIFileOperation.md#pyifileoperation)\.Unadvise

Unadvise\(Cookie\)
Disconnects a progress sink

#### Parameters

  - Cookie : int

    Identifies the sink to disconnect, as returned by [PyIFileOperation::Advise](PyIFileOperation.md#pyifileoperationadvise)