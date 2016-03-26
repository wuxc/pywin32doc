# PyIEnumGUID


## PyIEnumGUID Object

A Python interface to IEnumGUID

#### Methods

  - [Next](PyIEnumGUID.md#pyienumguidnext)

    Retrieves a specified number of items in the enumeration sequence\.&nbsp;

  - [Skip](PyIEnumGUID.md#pyienumguidskip)

    Skips over the next specified elementes\.&nbsp;

  - [Reset](PyIEnumGUID.md#pyienumguidreset)

    Resets the enumeration sequence to the beginning\.&nbsp;

  - [Clone](PyIEnumGUID.md#pyienumguidclone)

    Creates another enumerator that contains the same enumeration state as the current one\.&nbsp;




## [PyIEnumGUID](PyIEnumGUID.md#pyienumguid)\.Clone

[PyIEnumGUID](PyIEnumGUID.md#pyienumguid) = Clone\(\)
Creates another enumerator that contains the same enumeration state as the current one


## [PyIEnumGUID](PyIEnumGUID.md#pyienumguid)\.Next

\([PyIID](PyIID.md), \.\.\.\) = Next\(num\)
Retrieves a specified number of items in the enumeration sequence\.

#### Parameters

  - num=1 : int

    Number of items to retrieve\.

#### Return Value
The result is a tuple of [PyIID](PyIID.md) objects, 

one for each element returned\.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned\.


## [PyIEnumGUID](PyIEnumGUID.md#pyienumguid)\.Reset

Reset\(\)
Resets the enumeration sequence to the beginning\.


## [PyIEnumGUID](PyIEnumGUID.md#pyienumguid)\.Skip

Skip\(num\)
Skips over the next specified elementes\.

#### Parameters

  - num : int

    The number of elements being requested\.