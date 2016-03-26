# PyIPersistStream

## PyIPersistStream Object

A Python interface to IPersistStream

#### Methods


  - [IsDirty](PyIPersistStream.md#pyipersiststreamisdirty)

    Checks the object for changes since it was last saved\.&nbsp;

  - [Load](PyIPersistStream.md#pyipersiststreamload)

    Initializes an object from the stream where it was previously saved\.&nbsp;

  - [Save](PyIPersistStream.md#pyipersiststreamsave)

    Saves an object to the specified stream\.&nbsp;

  - [GetSizeMax](PyIPersistStream.md#pyipersiststreamgetsizemax)

    Returns the size in bytes of the stream needed to save the object\.&nbsp;


## [PyIPersistStream](#pyipersiststream)\.GetSizeMax

ULARGE\_INTEGER \= **GetSizeMax\(** \)
Returns the size in bytes of the stream needed to save the object\.

## [PyIPersistStream](#pyipersiststream)\.IsDirty

int \= **IsDirty\(** \)
Checks the object for changes since it was last saved\.

## [PyIPersistStream](#pyipersiststream)\.Load

 **Load\( *stream* ** \)
Initializes an object from the stream where it was previously saved\.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    Stream object to load from\.

#### Comments
This method loads an object from its associated stream\. The seek pointer is set as it was in the most recent[PyIPersistStream::Save](PyIPersistStream.md#pyipersiststreamsave)method\. This method can seek and read from the stream, but cannot write to it\.
On exit, the seek pointer must be in the same position it was in on entry, immediately past the end of the data\.

## [PyIPersistStream](#pyipersiststream)\.Save

 **Save\( *stream*  *, bClearDirty* ** \)
Saves an object to the specified stream\.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    The stream to save to\.

  -  *bClearDirty* : int

    Indicates whether to clear the dirty flag after the save is complete