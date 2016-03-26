# PyIEnumSTATSTG

## PyIEnumSTATSTG Object

An enumerator for elements contained in a[PyIStorage](#pyistorage)object

#### Methods


  - [Next](PyIEnumSTATSTG.md#pyienumstatstgnext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumSTATSTG.md#pyienumstatstgskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumSTATSTG.md#pyienumstatstgreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumSTATSTG.md#pyienumstatstgclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;


## [PyIEnumSTATSTG](#pyienumstatstg).Clone

[PyIEnumSTATSTG](#pyienumstatstg)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumSTATSTG](#pyienumstatstg).Next

([STATSTG](#statstg), ...) = __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

## [PyIEnumSTATSTG](#pyienumstatstg).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumSTATSTG](#pyienumstatstg).Skip

 __Skip(__ )
Skips over the next specified elementes.