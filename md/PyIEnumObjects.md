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

## [PyIEnumObjects](#pyienumobjects)\.Clone

[PyIEnumObjects](#pyienumobjects)\= **Clone\(** \)
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumObjects](#pyienumobjects)\.Next

\([PyIUnknown](#pyiunknown),\.\.\.\) \= **Next\( *num*  *, riid* ** \)
Retrieves a specified number of items in the enumeration sequence\.

#### Parameters


  -  *num\=1* : int

    Number of items to retrieve\.

  -  *riid\=IID\_IUnknown* :[PyIID](#pyiid)

    The interfaces to return

## [PyIEnumObjects](#pyienumobjects)\.Reset

 **Reset\(** \)
Resets the enumeration sequence to the beginning\.

## [PyIEnumObjects](#pyienumobjects)\.Skip

 **Skip\(** \)
Skips over the next specified elementes\.