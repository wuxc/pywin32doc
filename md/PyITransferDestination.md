# PyITransferDestination

## PyITransferDestination Object

Implemented by shell extensions that act as targets for item copy or move operations

#### Methods


  - [Advise](PyITransferDestination.md#pyitransferdestinationadvise)

    Connects an advise sink&nbsp;

  - [Unadvise](PyITransferDestination.md#pyitransferdestinationunadvise)

    Disconnects an advise sink&nbsp;

  - [CreateItem](PyITransferDestination.md#pyitransferdestinationcreateitem)

    Requests that a new item be created&nbsp;

## [PyITransferDestination](#pyitransferdestination).Advise

int = __Advise( *Sink* __ )
Connects an advise sink

#### Parameters


  -  *Sink* :[PyITransferAdviseSink](#pyitransferadvisesink)

    Event sink to receive notifications

#### Return Value
Returns an id for the connection, to be passed to[PyITransferDestination::Unadvise](PyITransferDestination.md#pyitransferdestinationunadvise)

## [PyITransferDestination](#pyitransferdestination).CreateItem

(int, interface, interface) = __CreateItem( *Name*  *, Attributes*  *, Size*  *, Flags*  *, riidItem*  *, riidResources* __ )
Requests that a new item be created

#### Parameters


  -  *Name* : str

    Filename to be created

  -  *Attributes* : int

    File attributes

  -  *Size* : int

    Size of file

  -  *Flags* : int

    Combination of shellcon.TSF_* flags

  -  *riidItem=IID_IShellItem* :[PyIID](#pyiid)

    Item interface to return

  -  *riidResources=IID_IShellItemResources* :[PyIID](#pyiid)

    Resource interface to return

#### Return Value
Returns the HRESULT and requested interfaces.  Interfaces may be None if 

function returns one of the informational codes (shellcon.COPYENGINE_S_*)

## [PyITransferDestination](#pyitransferdestination).Unadvise

 __Unadvise( *Cookie* __ )
Disconnects an advise sink

#### Parameters


  -  *Cookie* : int

    Connection identifier as returned by[PyITransferDestination::Advise](PyITransferDestination.md#pyitransferdestinationadvise)