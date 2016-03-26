# PyDDEServer


## PyDDEServer Object

A DDE server\.

#### Methods

  - [AddTopic](PyDDEServer.md#pyddeserveraddtopic)

    Adds a topic to the server\.&nbsp;

  - [Create](PyDDEServer.md#pyddeservercreate)

    Creates a DDE server&nbsp;

  - [Destroy](PyDDEServer.md#pyddeserverdestroy)

    Destroys the underlying C\+\+ object\.&nbsp;

  - [GetLastError](PyDDEServer.md#pyddeservergetlasterror)

    Returns the last DDE error\.&nbsp;

  - [Shutdown](PyDDEServer.md#pyddeservershutdown)

    Shutsdown the server\. 

sentinel&nbsp;


## [PyDDEServer](PyDDEServer.md#pyddeserver)\.AddTopic

AddTopic\(topic\)

#### Parameters

  - topic : [PyDDETopic](PyDDETopic.md)

    The topic to add\.


## [PyDDEServer](PyDDEServer.md#pyddeserver)\.Create

Create\(name, filterFlags\)
Create a server

#### Parameters

  - name : string

    Name of the server to start\.

  - filterFlags=0 : int

    Filter flags\.

#### Comments

Note there can only be one server per application\.


## [PyDDEServer](PyDDEServer.md#pyddeserver)\.Destroy

Destroy\(\)



## [PyDDEServer](PyDDEServer.md#pyddeserver)\.GetLastError

int = GetLastError\(\)



## [PyDDEServer](PyDDEServer.md#pyddeserver)\.Shutdown

Shutdown\(\)

#### Comments

Note the underlying DDE object \(ie, Server, Topics and Items\) are not cleaned up by this call\.