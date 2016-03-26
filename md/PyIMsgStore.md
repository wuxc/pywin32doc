# PyIMsgStore

## PyIMsgStore Object

An COM interface to MAPI
Derived from[PyIMAPIProp](#pyimapiprop)

#### Methods


  - [OpenEntry](PyIMsgStore.md#pyimsgstoreopenentry)

    Opens a folder or message and returns an interface object for further access.&nbsp;

  - [GetReceiveFolder](PyIMsgStore.md#pyimsgstoregetreceivefolder)

    Obtains the folder that was established as the destination for incoming messages of a specified message class or the default receive folder for the message store.&nbsp;

  - [GetReceiveFolderTable](PyIMsgStore.md#pyimsgstoregetreceivefoldertable)

    provides access to the receive folder table, a table that includes information about all of the receive folders for the message store.&nbsp;

  - [CompareEntryIDs](PyIMsgStore.md#pyimsgstorecompareentryids)

    Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object&nbsp;

  - [GetLastError](PyIMsgStore.md#pyimsgstoregetlasterror)

    Returns the last error associated with this object&nbsp;

  - [AbortSubmit](PyIMsgStore.md#pyimsgstoreabortsubmit)

    Attempts to remove a message from the outgoing queue.&nbsp;

## [PyIMsgStore](#pyimsgstore).AbortSubmit

int = __AbortSubmit( *entryId*  *, flags* __ )
Attempts to remove a message from the outgoing queue.

#### Parameters


  -  *entryId* : string

    The entry ID of the item to be aborted.

  -  *flags=0* : int

    Reserved - must be zero.

## [PyIMsgStore](#pyimsgstore).CompareEntryIDs

int = __CompareEntryIDs( *entryId*  *, entryId*  *, flags* __ )
Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

#### Parameters


  -  *entryId* : string

    The first entry ID to be compared

  -  *entryId* : string

    The second entry ID to be compared

  -  *flags=0* : int

    Reserved - must be zero.

#### Return Value
The result is set to TRUE if the two entry identifiers refer to the same object, and FALSE otherwise.

## [PyIMsgStore](#pyimsgstore).GetLastError

 __PyMAPIError__ = __GetLastError( *hr*  *, flags* __ )
Returns the last error associated with this object

#### Parameters


  -  *hr* : int

    The HRESULT

  -  *flags* : int

    

## [PyIMsgStore](#pyimsgstore).GetReceiveFolder

[PyIID](#pyiid), string = __GetReceiveFolder( **  *, flags* __ )
Obtains the folder that was established as the destination for incoming messages of a specified message class or the default receive folder for the message store.

#### Parameters


  -  ** : string

    Message class that is associated with a receive folder. If thid parameter is set to None or an empty string, GetReceiveFolder returns the default receive folder for the message store.

  -  *flags* : int

    

## [PyIMsgStore](#pyimsgstore).GetReceiveFolderTable

[PyIMAPITable](#pyimapitable)= __GetReceiveFolderTable( *flags* __ )
provides access to the receive folder table, a table that includes information about all of the receive folders for the message store.

#### Parameters


  -  *flags* : int

    Bitmask of flags that controls table access

## [PyIMsgStore](#pyimsgstore).OpenEntry

 __PyIInterface__ = __OpenEntry( *entryId*  *, iid*  *, flags* __ )
Opens a folder or message and returns an interface object for further access.

#### Parameters


  -  *entryId* : string

    The entryID of the object

  -  *iid* :[PyIID](#pyiid)

    The IID of the object to return, or None for the default IID

  -  *flags* : int

    Bitmask of flags that controls how the object is opened.