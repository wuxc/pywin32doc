# PyIEnumMoniker

## PyIEnumMoniker Object

A Python interface to IEnumMoniker

#### Methods


  - [Next](PyIEnumMoniker.md#pyienummonikernext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumMoniker.md#pyienummonikerskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumMoniker.md#pyienummonikerreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumMoniker.md#pyienummonikerclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;


## [PyIEnumMoniker](#pyienummoniker).Clone

[PyIEnumMoniker](#pyienummoniker)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumMoniker](#pyienummoniker).Next

[PyIMoniker](#pyimoniker)= __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

#### Return Value
The result is a tuple of[PyIID](#pyiid)objects, 

one for each element returned.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned.

## [PyIEnumMoniker](#pyienummoniker).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumMoniker](#pyienummoniker).Skip

 __Skip( *num* __ )
Skips over the next specified elementes.

#### Parameters


  -  *num* : int

    The number of elements being requested.