# PyIEnumCATEGORYINFO

## PyIEnumCATEGORYINFO Object

A Python interface to IEnumCATEGORYINFO

#### Methods


  - [Next](PyIEnumCATEGORYINFO.md#pyienumcategoryinfonext)

    Retrieves a specified number of items in the enumeration sequence\.&nbsp;

  - [Skip](PyIEnumCATEGORYINFO.md#pyienumcategoryinfoskip)

    Skips over the next specified elementes\.&nbsp;

  - [Reset](PyIEnumCATEGORYINFO.md#pyienumcategoryinforeset)

    Resets the enumeration sequence to the beginning\.&nbsp;

  - [Clone](PyIEnumCATEGORYINFO.md#pyienumcategoryinfoclone)

    Creates another enumerator that contains the same enumeration state as the current one\.&nbsp;


## [PyIEnumCATEGORYINFO](#pyienumcategoryinfo)\.Clone

[PyIEnumCATEGORYINFO](#pyienumcategoryinfo)\= **Clone\(** \)
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumCATEGORYINFO](#pyienumcategoryinfo)\.Next

\( \([PyIID](#pyiid), int, string\), \.\.\.\) \= **Next\( *num* ** \)
Retrieves a specified number of items in the enumeration sequence\.

#### Parameters


  -  *num\=1* : int

    Number of items to retrieve\.

#### Return Value
The result is a tuple of \(IID object, LCID, string description\) tuples, 

one for each element returned\.

## [PyIEnumCATEGORYINFO](#pyienumcategoryinfo)\.Reset

 **Reset\(** \)
Resets the enumeration sequence to the beginning\.

## [PyIEnumCATEGORYINFO](#pyienumcategoryinfo)\.Skip

 **Skip\( *num* ** \)
Skips over the next specified elementes\.

#### Parameters


  -  *num* : int

    The number of elements being requested\.