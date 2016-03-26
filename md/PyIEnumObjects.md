# PyIEnumObjects


## PyIEnumObjects Object

Iterates through a number of arbitrary interfaces

#### Methods

  - [Next](PyIEnumObjects.md#pyienumobjectsnext)

    Retrieves a specified number of items in the enumeration sequence\.&nbsp;

  - [Skip](PyIEnumObjects.md#pyienumobjectsskip)

    Skips over the next specified elementes\.&nbsp;

  - [Reset](PyIEnumObjects.md#pyienumobjectsreset)

    Resets the enumeration sequence to the beginning\.&nbsp;

  - [Clone](PyIEnumObjects.md#pyienumobjectsclone)

    Creates another enumerator that contains the same enumeration state as the current one\.&nbsp;


## [PyIEnumObjects](PyIEnumObjects.md#pyienumobjects)\.Clone

[PyIEnumObjects](PyIEnumObjects.md#pyienumobjects) = Clone\(\)
Creates another enumerator that contains the same enumeration state as the current one


## [PyIEnumObjects](PyIEnumObjects.md#pyienumobjects)\.Next

\([PyIUnknown](PyIUnknown.md),\.\.\.\) = Next\(num, riid

\)
Retrieves a specified number of items in the enumeration sequence\.

#### Parameters

  - num=1 : int

    Number of items to retrieve\.

  - riid=IID\_IUnknown : [PyIID](PyIID.md)

    The interfaces to return


## [PyIEnumObjects](PyIEnumObjects.md#pyienumobjects)\.Reset

Reset\(\)
Resets the enumeration sequence to the beginning\.


## [PyIEnumObjects](PyIEnumObjects.md#pyienumobjects)\.Skip

Skip\(\)
Skips over the next specified elementes\.