# PyIEnumContextProps

## PyIEnumContextProps Object

A Python interface to IEnumContextProps

#### Methods


  - [Next](PyIEnumContextProps.md#pyienumcontextpropsnext)

    Retrieves a specified number of items in the enumeration sequence.&nbsp;

  - [Skip](PyIEnumContextProps.md#pyienumcontextpropsskip)

    Skips over the next specified elementes.&nbsp;

  - [Reset](PyIEnumContextProps.md#pyienumcontextpropsreset)

    Resets the enumeration sequence to the beginning.&nbsp;

  - [Clone](PyIEnumContextProps.md#pyienumcontextpropsclone)

    Creates another enumerator that contains the same enumeration state as the current one.&nbsp;

## [PyIEnumContextProps](#pyienumcontextprops).Clone

[PyIEnumContextProps](#pyienumcontextprops)= __Clone(__ )
Creates another enumerator that contains the same enumeration state as the current one

## [PyIEnumContextProps](#pyienumcontextprops).Next

(([PyIID](#pyiid), int,[PyIUnknown](#pyiunknown)), ...) = __Next( *num* __ )
Retrieves a specified number of items in the enumeration sequence.

#### Parameters


  -  *num=1* : int

    Number of items to retrieve.

#### Return Value
Returns a tuple of 3-tuples representing ContextProperty structs:
First item is GUID identifying the property, second is Flags (reserved), third is the interface set as the property value

## [PyIEnumContextProps](#pyienumcontextprops).Reset

 __Reset(__ )
Resets the enumeration sequence to the beginning.

## [PyIEnumContextProps](#pyienumcontextprops).Skip

 __Skip(__ )
Skips over the next specified elementes.