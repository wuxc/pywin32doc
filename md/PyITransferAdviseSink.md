# PyITransferAdviseSink

## PyITransferAdviseSink Object

Interface that receives notifications from[PyITransferSource](#pyitransfersource)or[PyITransferDestination](#pyitransferdestination)

#### Methods


  - [UpdateProgress](PyITransferAdviseSink.md#pyitransferadvisesinkupdateprogress)

    Gives an estimate of amount of work completed&nbsp;

  - [UpdateTransferState](PyITransferAdviseSink.md#pyitransferadvisesinkupdatetransferstate)

    Notifies client of current operation state&nbsp;

  - [ConfirmOverwrite](PyITransferAdviseSink.md#pyitransferadvisesinkconfirmoverwrite)

    Asks user for permission to overwrite an existing item&nbsp;

  - [ConfirmEncryptionLoss](PyITransferAdviseSink.md#pyitransferadvisesinkconfirmencryptionloss)

    Notifies user when an item can't be encrypted at destination&nbsp;

  - [FileFailure](PyITransferAdviseSink.md#pyitransferadvisesinkfilefailure)

    Notifies user of failure, and queries how to proceed&nbsp;

  - [SubStreamFailure](PyITransferAdviseSink.md#pyitransferadvisesinksubstreamfailure)

    Notifies user of failure on a substream, and queries how to proceed&nbsp;

  - [PropertyFailure](PyITransferAdviseSink.md#pyitransferadvisesinkpropertyfailure)

    Notifies user of failure to set an item's properties&nbsp;

## [PyITransferAdviseSink](#pyitransferadvisesink).ConfirmEncryptionLoss

int = __ConfirmEncryptionLoss( *Source* __ )
Notifies user when an item can't be encrypted at destination

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    Item that failed to be encrypted

## [PyITransferAdviseSink](#pyitransferadvisesink).ConfirmOverwrite

int = __ConfirmOverwrite( *Source*  *, DestParent*  *, Name* __ )
Asks user for permission to overwrite an existing item

#### Parameters


  -  *Source* :[PyIShellItem](#pyishellitem)

    The item that will replace existing item

  -  *DestParent* :[PyIShellItem](#pyishellitem)

    Folder into which item will be placed

  -  *Name* : str

    New name for item, or None if item is to keep original name

## [PyITransferAdviseSink](#pyitransferadvisesink).FileFailure

(int,str) = __FileFailure( *Item*  *, ItemName*  *, Error* __ )
Notifies user of failure, and queries how to proceed

#### Parameters


  -  *Item* :[PyIShellItem](#pyishellitem)

    The shell item that caused the failure

  -  *ItemName* : str

    Name of item if different than above, can be None

  -  *Error* : int

    HRESULT error code from operation

#### Return Value
Returns the HRESULT and new file name if renaming resolved the failure

## [PyITransferAdviseSink](#pyitransferadvisesink).PropertyFailure

int = __PropertyFailure( *Item*  *, key*  *, Error* __ )
Notifies user of failure to set an item's properties

#### Parameters


  -  *Item* :[PyIShellItem](#pyishellitem)

    The item whose property could not be set

  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Identifies the property that caused the error, or None if all properties failed

  -  *Error* : int

    HRESULT error code returned by the operation

#### Return Value
Returns COPYENGINE_S_* to indicate that the failure was handled, or 

COPYENGINE_E_USERCANCELLED to cancel pending operations

## [PyITransferAdviseSink](#pyitransferadvisesink).SubStreamFailure

int = __SubStreamFailure( *Item*  *, StreamName*  *, Error* __ )
Notifies user of failure on a substream, and queries how to proceed

#### Parameters


  -  *Item* :[PyIShellItem](#pyishellitem)

    The item whose stream couldn't be created

  -  *StreamName* : str

    Name of the failed stream

  -  *Error* : int

    HRESULT failure code from operation

#### Return Value
Returns COPYENGINE_S_* if operation is to continue, or COPYENGINE_E_* HRESULT if cancelled

## [PyITransferAdviseSink](#pyitransferadvisesink).UpdateProgress

 __UpdateProgress( *SizeCurrent*  *, SizeTotal*  *, FilesCurrent*  *, FilesTotal*  *, FoldersCurrent*  *, FoldersTotal* __ )
Gives an estimate of amount of work completed

#### Parameters


  -  *SizeCurrent* : int

    Bytes transferred so far

  -  *SizeTotal* : int

    Total number of bytes

  -  *FilesCurrent* : int

    Number of files processed already

  -  *FilesTotal* : int

    Total number of files

  -  *FoldersCurrent* : int

    Number of folders processed already

  -  *FoldersTotal* : int

    Total number of folder

## [PyITransferAdviseSink](#pyitransferadvisesink).UpdateTransferState

 __UpdateTransferState( *State* __ )
Notifies client of current operation state

#### Parameters


  -  *State* : int

    A TRANSFER_ADVISE_STATE value (shellcon.TS_*)