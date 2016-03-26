# PyIInitializeWithFile

## PyIInitializeWithFile Object

Initializes a property handler that requires a file path instead of a stream

#### Methods


  - [Initialize](PyIInitializeWithFile.md#pyiinitializewithfileinitialize)

    Passes a file path to a property handler on startup&nbsp;

## [PyIInitializeWithFile](#pyiinitializewithfile).Initialize

 __Initialize( *FilePath*  *, Mode* __ )
Passes a file path to a property handler on startup

#### Parameters


  -  *FilePath* : str

    Full path to the file whose properties are to be accessed

  -  *Mode* : int

    Indicates if properties can be written, STGM_READ or STGM_READWRITE