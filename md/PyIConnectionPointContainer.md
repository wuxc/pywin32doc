# PyIConnectionPointContainer

## PyIConnectionPointContainer Object

A Python wrapper of a COM IConnectionPointContainer interface.

#### Methods


  - [EnumConnectionPoints](PyIConnectionPointContainer.md#pyiconnectionpointcontainerenumconnectionpoints)

    Creates an enumerator object to iterate through all the connection points supported in the connectable object, one connection point per outgoing IID.&nbsp;

  - [FindConnectionPoint](PyIConnectionPointContainer.md#pyiconnectionpointcontainerfindconnectionpoint)

    Finds a connection point for the given IID.&nbsp;


## [PyIConnectionPointContainer](#pyiconnectionpointcontainer).EnumConnectionPoints

[PyIEnumConnectionPoints](#pyienumconnectionpoints)= __EnumConnectionPoints(__ )
Creates an enumerator object to iterate through all the connection points supported in the connectable object, one connection point per outgoing IID.

## [PyIConnectionPointContainer](#pyiconnectionpointcontainer).FindConnectionPoint

[PyIConnectionPoint](#pyiconnectionpoint)= __FindConnectionPoint( *iid* __ )
Finds a connection point for the given IID

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the requested connection.