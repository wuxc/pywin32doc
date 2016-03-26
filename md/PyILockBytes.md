# PyILockBytes


## PyILockBytes Object

Description of the interface

#### Methods

  - [ReadAt](PyILockBytes.md#pyilockbytesreadat)

    Reads a specified number of bytes starting at a specified offset from the beginning of the byte array object\.&nbsp;

  - [WriteAt](PyILockBytes.md#pyilockbyteswriteat)

    Writes the specified number of bytes starting at a specified offset from the beginning of the byte array\.&nbsp;

  - [Flush](PyILockBytes.md#pyilockbytesflush)

    Ensures that any internal buffers maintained by the byte array object are written out to the backing storage\.&nbsp;

  - [SetSize](PyILockBytes.md#pyilockbytessetsize)

    Changes the size of the byte array\.&nbsp;

  - [LockRegion](PyILockBytes.md#pyilockbyteslockregion)

    Restricts access to a specified range of bytes in the byte array\.&nbsp;

  - [UnlockRegion](PyILockBytes.md#pyilockbytesunlockregion)

    Removes the access restriction on a range of bytes previously restricted with [PyILockBytes::LockRegion](PyILockBytes.md#pyilockbyteslockregion)\.&nbsp;

  - [Stat](PyILockBytes.md#pyilockbytesstat)

    Retrieves a [STATSTG](STATSTG.md) structure for this byte array object\.&nbsp;




## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.Flush

Flush\(\)
Ensures that any internal buffers maintained by the byte array object are written out to the backing storage\.


## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.LockRegion

LockRegion\(libOffset, cb, dwLockType\)
Restricts access to a specified range of bytes in the byte array\.

#### Parameters

  - libOffset : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    The beginning of the region to lock\.

  - cb : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    The number of bytes to lock\.

  - dwLockType : int

    Specifies the restrictions being requested on accessing the range\.


## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.ReadAt

string = ReadAt\(ulOffset, cb

\)
Reads a specified number of bytes starting at a specified offset from the beginning of the byte array object\.

#### Parameters

  - ulOffset : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    Offset to start reading

  - cb : int

    Number of bytes to read

#### Comments

The result is a binary buffer returned in a string\.


## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.SetSize

SetSize\(cb\)
Changes the size of the byte array\.

#### Parameters

  - cb : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    The new size\.


## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.Stat

[STATSTG](STATSTG.md) = Stat\(grfStatFlag\)
Retrieves a [STATSTG](STATSTG.md) structure for this byte array object\.

#### Parameters

  - grfStatFlag : int

    Specifies that this method does not return some of the fields in the STATSTG structure, thus saving a memory allocation operation\. Values are taken from the STATFLAG enumerationg


## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.UnlockRegion

UnlockRegion\(libOffset, cb, dwLockType\)
Removes the access restriction on a range of bytes previously restricted with [PyILockBytes::LockRegion](PyILockBytes.md#pyilockbyteslockregion)\.

#### Parameters

  - libOffset : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    The beginning of the region to unlock\.

  - cb : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    The number of bytes to lock\.

  - dwLockType : int

    Specifies the restrictions being requested on accessing the range\.


## [PyILockBytes](PyILockBytes.md#pyilockbytes)\.WriteAt

int = WriteAt\(ulOffset, data

\)
Writes the specified number of bytes starting at a specified offset from the beginning of the byte array\.

#### Parameters

  - ulOffset : [ULARGE\_INTEGER](ULARGE.md#ulargeinteger)

    Offset to write at\.

  - data : string

    Data to write

#### Return Value
The result is the number of bytes actually written\.