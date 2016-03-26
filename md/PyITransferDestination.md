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


## [PyITransferDestination](PyITransferDestination.md#pyitransferdestination)\.Advise

int = Advise\(Sink\)
Connects an advise sink

#### Parameters

  - Sink : [PyITransferAdviseSink](PyITransferAdviseSink.md)

    Event sink to receive notifications

#### Return Value
Returns an id for the connection, to be passed to [PyITransferDestination::Unadvise](PyITransferDestination.md#pyitransferdestinationunadvise)


## [PyITransferDestination](PyITransferDestination.md#pyitransferdestination)\.CreateItem

\(int, interface, interface\) = CreateItem\(Name, Attributes

, Size

, Flags

, riidItem

, riidResources

\)
Requests that a new item be created

#### Parameters

  - Name : str

    Filename to be created

  - Attributes : int

    File attributes

  - Size : int

    Size of file

  - Flags : int

    Combination of shellcon\.TSF\_\* flags

  - riidItem=IID\_IShellItem : [PyIID](PyIID.md)

    Item interface to return

  - riidResources=IID\_IShellItemResources : [PyIID](PyIID.md)

    Resource interface to return

#### Return Value
Returns the HRESULT and requested interfaces\.  Interfaces may be None if 

function returns one of the informational codes \(shellcon\.COPYENGINE\_S\_\*\)


## [PyITransferDestination](PyITransferDestination.md#pyitransferdestination)\.Unadvise

Unadvise\(Cookie\)
Disconnects an advise sink

#### Parameters

  - Cookie : int

    Connection identifier as returned by [PyITransferDestination::Advise](PyITransferDestination.md#pyitransferdestinationadvise)