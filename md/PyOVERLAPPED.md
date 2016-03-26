# PyOVERLAPPED


## PyOVERLAPPED Object

A Python object, representing an overlapped structure

#### Comments

Typically you create a PyOVERLAPPED object, and set its hEvent property\. 

The object can then be passed to any function which takes an OVERLAPPED object, and 

the object attributes will be automatically updated\.

#### Properties

  - integer Offset

    Specifies a file position at which to start the transfer\. The file position is a byte offset from the start of the file\. The calling process sets this member before calling the ReadFile&\#160or WriteFile function\. This member is ignored when reading from or writing to named pipes and communications devices\.

  - integer OffsetHigh

    Specifies the high word of the byte offset at which to start the transfer\.

  - object object

    Any python object that you want to attach to your overlapped I/O request\.

  - int dword

    An integer buffer that may be used by overlapped functions \(eg, [win32file::WaitCommEvent](win32file.md#win32filewaitcommevent)\)

  - [PyHANDLE](PyHANDLE.md) hEvent

    Identifies an event set to the signaled state when the transfer has been completed\. The calling process sets this member before calling the [win32file::ReadFile](win32file.md#win32filereadfile), [win32file::WriteFile](win32file.md#win32filewritefile), [win32pipe::ConnectNamedPipe](win32pipe.md#win32pipeconnectnamedpipe), or [win32pipe::TransactNamedPipe](win32pipe.md#win32pipetransactnamedpipe)&\#160function\.

  - integer Internal

    Reserved for operating system use\. \(pointer-sized value\)

  - integer InternalHigh

    Reserved for operating system use\. \(pointer-sized value\)