# PyIEnumShellItems

## PyIEnumShellItems Object

A Python interface to IEnumShellItems

#### Methods


  - [Next](PyIEnumShellItems.md#pyienumshellitemsnext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumShellItems.md#pyienumshellitemsskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumShellItems.md#pyienumshellitemsreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumShellItems.md#pyienumshellitemsclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;

## [PyIEnumShellItems](#pyienumshellitems).Clone

[PyIEnumShellItems](#pyienumshellitems)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumShellItems](#pyienumshellitems).Next

([PyIShellItem](#pyishellitem),...) = __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

## [PyIEnumShellItems](#pyienumshellitems).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumShellItems](#pyienumshellitems).Skip

 __Skip(__ )
Skips over the next specified elementes.