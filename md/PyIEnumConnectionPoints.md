# PyIEnumConnectionPoints

## PyIEnumConnectionPoints Object

A Python interface to IEnumConnectionPoints

#### Methods


  - [Next](PyIEnumConnectionPoints.md#pyienumconnectionpointsnext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumConnectionPoints.md#pyienumconnectionpointsskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumConnectionPoints.md#pyienumconnectionpointsreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumConnectionPoints.md#pyienumconnectionpointsclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;


## [PyIEnumConnectionPoints](#pyienumconnectionpoints).Clone

[PyIEnumConnectionPoints](#pyienumconnectionpoints)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumConnectionPoints](#pyienumconnectionpoints).Next

([PyIConnectionPoint](#pyiconnectionpoint), ...) = __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

## [PyIEnumConnectionPoints](#pyienumconnectionpoints).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumConnectionPoints](#pyienumconnectionpoints).Skip

 __Skip(__ )
Skips over the next specified elementes.