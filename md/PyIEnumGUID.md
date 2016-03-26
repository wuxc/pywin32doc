# PyIEnumGUID

## PyIEnumGUID Object

A Python interface to IEnumGUID

#### Methods


  - [Next](PyIEnumGUID.md#pyienumguidnext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumGUID.md#pyienumguidskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumGUID.md#pyienumguidreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumGUID.md#pyienumguidclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;


## [PyIEnumGUID](#pyienumguid).Clone

[PyIEnumGUID](#pyienumguid)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumGUID](#pyienumguid).Next

([PyIID](#pyiid), ...) = __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

#### Return Value
The result is a tuple of[PyIID](#pyiid)objects, 

one for each element returned.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned.

## [PyIEnumGUID](#pyienumguid).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumGUID](#pyienumguid).Skip

 __Skip( *num* __ )
Skips over the next specified elementes.

#### Parameters


  -  *num* : int

    The number of elements being requested.