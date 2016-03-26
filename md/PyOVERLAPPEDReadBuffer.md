# PyOVERLAPPEDReadBuffer

## PyOVERLAPPEDReadBuffer Object

An alias for a standard Python buffer object. 

Previous versions of the Windows extensions had a custom object for 

holding a read buffer.  This has been replaced with the standard Python buffer object.
Python does not provide a method for creating a read-write buffer 

of arbitary size, so currently this can only be created by[win32file::AllocateReadBuffer](win32file.md#win32fileallocatereadbuffer).