# PyIExternalConnection

## PyIExternalConnection Object

A Python wrapper for a COM IExternalConnection interface\.

#### Comments
The IExternalConnection interface manages a server object's count of marshaled, or external, connections\. A server that maintains such a count can detect when it has no external connections and shut itself down in an orderly fashion\.

#### Methods


  - [AddConnection](PyIExternalConnection.md#pyiexternalconnectionaddconnection)

    Increments an object's count of its strong external connections \(links\)\.&nbsp;

  - [ReleaseConnection](PyIExternalConnection.md#pyiexternalconnectionreleaseconnection)

    Decrements an object's count of its strong external connections \(references\)\.&nbsp;


## [PyIExternalConnection](#pyiexternalconnection)\.AddConnection

int \= **AddConnection\( *extconn*  *, reserved* ** \)
Increments an object's count of its strong external connections \(links\)\.

#### Parameters


  -  *extconn* : int

    Type of external connection to the object\. The only type of external connection currently supported by this interface is strong, which means that the object must remain alive as long as this external connection exists\. Strong external connections are represented by the value EXTCONN\_STRONG \= 0x0001, which is defined in the enumeration EXTCON

  -  *reserved\=0* : int

    A reserved parameter

#### Return Value
The result is the number of reference counts on the object; used for debugging purposes only\.

## [PyIExternalConnection](#pyiexternalconnection)\.ReleaseConnection

int \= **ReleaseConnection\( *extconn*  *, reserved*  *, fLastReleaseCloses* ** \)
Decrements an object's count of its strong external connections \(references\)\.

#### Parameters


  -  *extconn* : int

    Type of external connection

  -  *reserved* : int

    A reserved parameter\.

  -  *fLastReleaseCloses* : int

    TRUE specifies that if the connection being released is the last external lock on the object, the object should close\. FALSE specifies that the object should remain open until closed by the user or another process\.

#### Return Value
The result is the number of reference counts on the object; used for debugging purposes only\.