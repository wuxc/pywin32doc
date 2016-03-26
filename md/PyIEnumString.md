# PyIEnumString

## PyIEnumString Object

An enumerator interface to list strings

#### Methods


  - [Next](PyIEnumString.md#pyienumstringnext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumString.md#pyienumstringskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumString.md#pyienumstringreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumString.md#pyienumstringclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;


## [PyIEnumString](#pyienumstring).Clone

[PyIEnumString](#pyienumstring)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumString](#pyienumstring).Next

([PyUnicode](#pyunicode),...) = __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

## [PyIEnumString](#pyienumstring).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumString](#pyienumstring).Skip

 __Skip(__ )
Skips over the next specified elementes.