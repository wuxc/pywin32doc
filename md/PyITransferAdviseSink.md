# PyITransferAdviseSink


## PyITransferAdviseSink Object

Interface that receives notifications from [PyITransferSource](PyITransferSource.md) or [PyITransferDestination](PyITransferDestination.md)

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


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.ConfirmEncryptionLoss

int = ConfirmEncryptionLoss\(Source\)
Notifies user when an item can't be encrypted at destination

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    Item that failed to be encrypted


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.ConfirmOverwrite

int = ConfirmOverwrite\(Source, DestParent

, Name

\)
Asks user for permission to overwrite an existing item

#### Parameters

  - Source : [PyIShellItem](PyIShellItem.md)

    The item that will replace existing item

  - DestParent : [PyIShellItem](PyIShellItem.md)

    Folder into which item will be placed

  - Name : str

    New name for item, or None if item is to keep original name


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.FileFailure

\(int,str\) = FileFailure\(Item, ItemName

, Error

\)
Notifies user of failure, and queries how to proceed

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The shell item that caused the failure

  - ItemName : str

    Name of item if different than above, can be None

  - Error : int

    HRESULT error code from operation

#### Return Value
Returns the HRESULT and new file name if renaming resolved the failure


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.PropertyFailure

int = PropertyFailure\(Item, key

, Error

\)
Notifies user of failure to set an item's properties

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The item whose property could not be set

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Identifies the property that caused the error, or None if all properties failed

  - Error : int

    HRESULT error code returned by the operation

#### Return Value
Returns COPYENGINE\_S\_\* to indicate that the failure was handled, or 

COPYENGINE\_E\_USERCANCELLED to cancel pending operations


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.SubStreamFailure

int = SubStreamFailure\(Item, StreamName

, Error

\)
Notifies user of failure on a substream, and queries how to proceed

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    The item whose stream couldn't be created

  - StreamName : str

    Name of the failed stream

  - Error : int

    HRESULT failure code from operation

#### Return Value
Returns COPYENGINE\_S\_\* if operation is to continue, or COPYENGINE\_E\_\* HRESULT if cancelled


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.UpdateProgress

UpdateProgress\(SizeCurrent, SizeTotal, FilesCurrent, FilesTotal, FoldersCurrent, FoldersTotal\)
Gives an estimate of amount of work completed

#### Parameters

  - SizeCurrent : int

    Bytes transferred so far

  - SizeTotal : int

    Total number of bytes

  - FilesCurrent : int

    Number of files processed already

  - FilesTotal : int

    Total number of files

  - FoldersCurrent : int

    Number of folders processed already

  - FoldersTotal : int

    Total number of folder


## [PyITransferAdviseSink](PyITransferAdviseSink.md#pyitransferadvisesink)\.UpdateTransferState

UpdateTransferState\(State\)
Notifies client of current operation state

#### Parameters

  - State : int

    A TRANSFER\_ADVISE\_STATE value \(shellcon\.TS\_\*\)