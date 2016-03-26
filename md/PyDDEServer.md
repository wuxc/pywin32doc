# PyDDEServer

## PyDDEServer Object

A DDE server.

#### Methods


  - [AddTopic](PyDDEServer.md#pyddeserveraddtopic)

    Adds a topic to the server.&nbsp;

  - [Create](PyDDEServer.md#pyddeservercreate)

    Creates a DDE server&nbsp;

  - [Destroy](PyDDEServer.md#pyddeserverdestroy)

    Destroys the underlying C++ object.&nbsp;

  - [GetLastError](PyDDEServer.md#pyddeservergetlasterror)

    Returns the last DDE error.&nbsp;

  - [Shutdown](PyDDEServer.md#pyddeservershutdown)

    Shutsdown the server. 

sentinel&nbsp;

## [PyDDEServer](#pyddeserver).AddTopic

 __AddTopic( *topic* __ )


#### Parameters


  -  *topic* :[PyDDETopic](#pyddetopic)

    The topic to add.

## [PyDDEServer](#pyddeserver).Create

 __Create( *name*  *, filterFlags* __ )
Create a server

#### Parameters


  -  *name* : string

    Name of the server to start.

  -  *filterFlags=0* : int

    Filter flags.

#### Comments
Note there can only be one server per application.

## [PyDDEServer](#pyddeserver).Destroy

 __Destroy(__ )


## [PyDDEServer](#pyddeserver).GetLastError

int = __GetLastError(__ )


## [PyDDEServer](#pyddeserver).Shutdown

 __Shutdown(__ )


#### Comments
Note the underlying DDE object (ie, Server, Topics and Items) are not cleaned up by this call.