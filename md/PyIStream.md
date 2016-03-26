# PyIStream

## PyIStream Object

A Python interface to IStream

#### Methods


  - [Read](PyIStream.md#pyistreamread)

    Read the specified number of bytes from the string.&nbsp;

  - [read](PyIStream.md#pyistreamread)

    Alias for[PyIStream::Read](PyIStream.md#pyistreamread)&nbsp;

  - [Write](PyIStream.md#pyistreamwrite)

    Write data from a stream.&nbsp;

  - [write](PyIStream.md#pyistreamwrite)

    Alias for[PyIStream::Write](PyIStream.md#pyistreamwrite)&nbsp;

  - [Seek](PyIStream.md#pyistreamseek)

    Changes the seek pointer to a new location.&nbsp;

  - [SetSize](PyIStream.md#pyistreamsetsize)

    Changes the size of the stream object.&nbsp;

  - [CopyTo](PyIStream.md#pyistreamcopyto)

    Copies a specified number of bytes from the current seek pointer in the stream to the current seek pointer in another stream.&nbsp;

  - [Commit](PyIStream.md#pyistreamcommit)

    Ensures that any changes made to a stream object open in transacted mode are reflected in the parent storage.&nbsp;

  - [Revert](PyIStream.md#pyistreamrevert)

    Discards all changes that have been made to a transacted stream since the last[PyIStream::Commit](PyIStream.md#pyistreamcommit)call.&nbsp;

  - [LockRegion](PyIStream.md#pyistreamlockregion)

    Restricts access to a specified range of bytes in the stream.&nbsp;

  - [UnLockRegion](PyIStream.md#pyistreamunlockregion)

    Removes the access restriction on a range of bytes previously restricted with[PyIStream::LockRegion](PyIStream.md#pyistreamlockregion).&nbsp;

  - [Clone](PyIStream.md#pyistreamclone)

    Creates a new stream object with its own seek pointer that references the same bytes as the original stream.&nbsp;

  - [Stat](PyIStream.md#pyistreamstat)

    Returns information about a stream&nbsp;


## [PyIStream](#pyistream).Clone

[PyIStream](#pyistream)= __Clone(__ )
Creates a new stream object with its own seek pointer that references the same bytes as the original stream.

## [PyIStream](#pyistream).Commit

 __Commit( *flags* __ )
Ensures that any changes made to a stream object open in transacted mode are reflected in the parent storage.

#### Parameters


  -  *flags=STGC_DEFAULT* : int

    Controls how changes are performed.

## [PyIStream](#pyistream).CopyTo

ULARGE_INTEGER = __CopyTo( *stream*  *, cb* __ )
Copies a specified number of bytes from the current seek pointer in the stream to the current seek pointer in another stream.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    The stream to write to.

  -  *cb* : ULARGE_INTEGER

    The number of bytes to write.

#### Return Value
The return value is the number of bytes actually written.

## [PyIStream](#pyistream).LockRegion

 __LockRegion( *offset*  *, cb*  *, lockType* __ )
Restricts access to a specified range of bytes in the stream.

#### Parameters


  -  *offset* : ULARGE_INTEGER

    Integer that specifies the byte offset for the beginning of the range.

  -  *cb* : ULARGE_INTEGER

    The number of bytes to restrict.

  -  *lockType* : int

    Restrictions requested.

## [PyIStream](#pyistream).Read

string = __Read( *numBytes* __ )
Read the specified number of bytes from the string.

#### Parameters


  -  *numBytes* : int

    The number of bytes to read from the stream.  Must not be zero.

#### Return Value
The result is a string containing binary data.

## [PyIStream](#pyistream).Revert

 __Revert(__ )
Discards all changes that have been made to a transacted stream since the last[PyIStream::Commit](PyIStream.md#pyistreamcommit)call.

## [PyIStream](#pyistream).Seek

ULARGE_INTEGER = __Seek( *offset*  *, origin* __ )
Changes the seek pointer to a new location.

#### Parameters


  -  *offset* : int

    The new location

  -  *origin* : int

    Relative to where?

## [PyIStream](#pyistream).SetSize

 __SetSize( *newSize* __ )
Changes the size of the stream object.

#### Parameters


  -  *newSize* : ULARGE_INTEGER

    The new size

## [PyIStream](#pyistream).Stat

[STATSTG](#statstg)= __Stat( *grfStatFlag* __ )
Returns information about the stream

#### Parameters


  -  *grfStatFlag=0* : int

    Flags.

## [PyIStream](#pyistream).UnlockRegion

 __UnlockRegion( *offset*  *, cb*  *, lockType* __ )
Removes the access restriction on a range of bytes previously restricted with[PyIStream::LockRegion](PyIStream.md#pyistreamlockregion).

#### Parameters


  -  *offset* : ULARGE_INTEGER

    Integer that specifies the byte offset for the beginning of the range.

  -  *cb* : ULARGE_INTEGER

    The number of bytes to restrict.

  -  *lockType* : int

    Restrictions requested.

## [PyIStream](#pyistream).Write

 __Write( *data* __ )
Write data to a stream

#### Parameters


  -  *data* : string

    The binary data to write.