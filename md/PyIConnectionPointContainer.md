# PyIConnectionPointContainer


## PyIConnectionPointContainer Object

A Python wrapper of a COM IConnectionPointContainer interface\.

#### Methods

  - [EnumConnectionPoints](PyIConnectionPointContainer.md#pyiconnectionpointcontainerenumconnectionpoints)

    Creates an enumerator object to iterate through all the connection points supported in the connectable object, one connection point per outgoing IID\.&nbsp;

  - [FindConnectionPoint](PyIConnectionPointContainer.md#pyiconnectionpointcontainerfindconnectionpoint)

    Finds a connection point for the given IID\.&nbsp;




## [PyIConnectionPointContainer](PyIConnectionPointContainer.md#pyiconnectionpointcontainer)\.EnumConnectionPoints

[PyIEnumConnectionPoints](PyIEnumConnectionPoints.md) = EnumConnectionPoints\(\)
Creates an enumerator object to iterate through all the connection points supported in the connectable object, one connection point per outgoing IID\.


## [PyIConnectionPointContainer](PyIConnectionPointContainer.md#pyiconnectionpointcontainer)\.FindConnectionPoint

[PyIConnectionPoint](PyIConnectionPoint.md) = FindConnectionPoint\(iid\)
Finds a connection point for the given IID

#### Parameters

  - iid : [PyIID](PyIID.md)

    The IID of the requested connection\.