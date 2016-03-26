
## [win32pipe](#README.md#win32pipe).CallNamedPipe

string = **CallNamedPipe( *pipeName*  *, data*  *, bufSize*  *, timeOut* ** )
Opens and performs a transaction on a named pipe.

#### Parameters


     *pipeName* :[PyUNICODE](#README.md#PyUNICODE)

    The name of the pipe.

     *data* : string

    The data to write.

     *bufSize* : int

    The size of the result buffer to allocate for the read.

     *timeOut* : int

    Specifies the number of milliseconds to wait for the named pipe to be available. In addition to numeric values, the following special values can be specified.


## [win32pipe](#README.md#win32pipe).ConnectNamedPipe

int = **ConnectNamedPipe( *hPipe*  *, overlapped* ** )
Connects to a named pipe

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

     *overlapped=None* :[PyOVERLAPPED](#README.md#PyOVERLAPPED)

    An overlapped object to use, else None

#### Comments
The result is zero if the function succeeds.  If the function fails, 

GetLastError() is called, and if the result is ERROR_IO_PENDING or ERROR_PIPE_CONNECTED 

(common when passing an overlapped object), this value is returned.  All 

other error values raise a win32 exception (from which the error code 

can be extracted)

## [win32pipe](#README.md#win32pipe).CreateNamedPipe

[PyHANDLE](#README.md#PyHANDLE)= **CreateNamedPipe( *pipeName*  *, openMode*  *, pipeMode*  *, nMaxInstances*  *, nOutBufferSize*  *, nInBufferSize*  *, nDefaultTimeOut*  *, sa* ** )
Creates an instance of a named pipe and returns a handle for subsequent pipe operations

#### Parameters


     *pipeName* :[PyUnicode](#README.md#PyUnicode)

    The name of the pipe

     *openMode* : int

    OpenMode of the pipe

     *pipeMode* : int

    

     *nMaxInstances* : int

    

     *nOutBufferSize* : int

    

     *nInBufferSize* : int

    

     *nDefaultTimeOut* : int

    

     *sa* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    

## [win32pipe](#README.md#win32pipe).CreatePipe

([PyHANDLE](#README.md#PyHANDLE),[PyHANDLE](#README.md#PyHANDLE)) = **CreatePipe( *sa*  *, nSize* ** )
Creates an anonymous pipe, and returns handles to the read and write ends of the pipe

#### Parameters


     *sa* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    

     *nSize* : int

    

## [win32pipe](#README.md#win32pipe).DisconnectNamedPipe

 **DisconnectNamedPipe( *hFile* ** )
Disconnects the server end of a named pipe instance from a client process.

#### Parameters


     *hFile* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe to disconnect.

## [win32pipe](#README.md#win32pipe).FdCreatePipe

(int, int) = **FdCreatePipe( *sa*  *, nSize*  *, mode* ** )
As CreatePipe but returns file descriptors

#### Parameters


     *sa* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies security and inheritance for the pipe

     *nSize* : int

    Buffer size for pipe.  Use 0 for default size.

     *mode* : int

    O_TEXT or O_BINARY

## [win32pipe](#README.md#win32pipe).GetNamedPipeClientProcessId

int = **GetNamedPipeClientProcessId( *hPipe* ** )
Returns the process id of client that is connected to a named pipe

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

#### Comments
Requires Vista or later

## [win32pipe](#README.md#win32pipe).GetNamedPipeClientSessionId

int = **GetNamedPipeClientSessionId( *hPipe* ** )
Returns the session id of client that is connected to a named pipe

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

#### Comments
Requires Vista or later

## [win32pipe](#README.md#win32pipe).GetNamedPipeHandleState

(int, int, int/None, int/None,[PyUnicode](#README.md#PyUnicode)= **GetNamedPipeHandleState( *hPipe*  *, bGetCollectionData* ** )
Determines the state of the named pipe.

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

     *bGetCollectionData=0* : int

    Determines of the collection data should be returned.  If not, None is returned in their place.

## [win32pipe](#README.md#win32pipe).GetNamedPipeInfo

(int, int, int, int) = **GetNamedPipeInfo( *hNamedPipe* ** )
Returns pipe's flags, buffer sizes, and max instances

#### Parameters


     *hNamedPipe* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a named pipe

## [win32pipe](#README.md#win32pipe).GetNamedPipeServerProcessId

int = **GetNamedPipeServerProcessId( *hPipe* ** )
Returns pid of server process that created a named pipe

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

#### Comments
Requires Vista or later

## [win32pipe](#README.md#win32pipe).GetNamedPipeServerSessionId

int = **GetNamedPipeServerSessionId( *hPipe* ** )
Returns session id of server process that created a named pipe

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

#### Comments
Requires Vista or later

## [win32pipe](#README.md#win32pipe).GetOverlappedResult

int = **GetOverlappedResult( *hFile*  *, overlapped*  *, bWait* ** )
Determines the result of the most recent call with an OVERLAPPED object.

#### Parameters


     *hFile* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe or file

     *overlapped* :[PyOVERLAPPED](#README.md#PyOVERLAPPED)

    The overlapped object to check.

     *bWait* : int

    Indicates if the function should wait for data to become available.

#### Comments
The result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

## NMPWAIT_NOWAIT
 **const win32pipe.NMPWAIT_NOWAIT;** 


## NMPWAIT_USE_DEFAULT_WAIT
 **const win32pipe.NMPWAIT_USE_DEFAULT_WAIT;** 


## NMPWAIT_WAIT_FOREVER
 **const win32pipe.NMPWAIT_WAIT_FOREVER;** 


## PIPE_ACCESS_DUPLEX
 **const win32pipe.PIPE_ACCESS_DUPLEX;** 


## PIPE_ACCESS_INBOUND
 **const win32pipe.PIPE_ACCESS_INBOUND;** 


## PIPE_ACCESS_OUTBOUND
 **const win32pipe.PIPE_ACCESS_OUTBOUND;** 


## PIPE_NOWAIT
 **const win32pipe.PIPE_NOWAIT;** 


## PIPE_READMODE_BYTE
 **const win32pipe.PIPE_READMODE_BYTE;** 


## PIPE_READMODE_MESSAGE
 **const win32pipe.PIPE_READMODE_MESSAGE;** 


## PIPE_TYPE_BYTE
 **const win32pipe.PIPE_TYPE_BYTE;** 


## PIPE_TYPE_MESSAGE
 **const win32pipe.PIPE_TYPE_MESSAGE;** 


## PIPE_UNLIMITED_INSTANCES
 **const win32pipe.PIPE_UNLIMITED_INSTANCES;** 


## PIPE_WAIT
 **const win32pipe.PIPE_WAIT;** 


## [win32pipe](#README.md#win32pipe).PeekNamedPipe

(string, int, int) = **PeekNamedPipe( *hPipe*  *, size* ** )
Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

     *size* : int

    The size of the buffer.

## [win32pipe](#README.md#win32pipe).SetNamedPipeHandleState

 **SetNamedPipeHandleState( *hPipe*  *, Mode*  *, MaxCollectionCount*  *, CollectDataTimeout* ** )
Sets the state of the named pipe.

#### Parameters


     *hPipe* :[PyHANDLE](#README.md#PyHANDLE)

    The handle to the pipe.

     *Mode* : int/None

    The pipe read mode.

     *MaxCollectionCount* : int/None

    Maximum bytes collected before transmission to the server.

     *CollectDataTimeout* : int/None

    Maximum time to wait, in milliseconds, before transmission to server.

## [win32pipe](#README.md#win32pipe).TransactNamedPipe

string/buffer = **TransactNamedPipe( *pipeName*  *, writeData*  *, buffer/bufSize*  *, overlapped* ** )
Combines the functions that write a 

message to and read a message from the specified named pipe into a single 

network operation.

#### Parameters


     *pipeName* :[PyUNICODE](#README.md#PyUNICODE)

    The name of the pipe.

     *writeData* : string/buffer

    The data to write to the pipe.

     *buffer/bufSize* :[PyOVERLAPPEDReadBuffer](#README.md#PyOVERLAPPEDReadBuffer)/int

    Size of the buffer to create for the result, 

or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is 

the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, 

built from the buffer, but with a length that reflects the data actually read.

     *overlapped=None* :[PyOVERLAPPED](#README.md#PyOVERLAPPED)

    An overlapped structure or None

#### Comments
This function is modelled on[win32file::ReadFile](#win32file.md#win32fileReadFile)- for overlapped 

operations you are expected to provide a buffer which will be filled 

asynchronously.

## [win32pipe](#README.md#win32pipe).WaitNamedPipe

 **WaitNamedPipe( *pipeName*  *, timeout* ** )
Waits until either a time-out interval elapses or an instance of the specified named pipe is available to be connected to (that is, the pipe's server process has a pending[win32pipe::ConnectNamedPipe](#win32pipe.md#win32pipeConnectNamedPipe)operation on the pipe).

#### Parameters


     *pipeName* :[PyUnicode](#README.md#PyUnicode)

    The name of the pipe

     *timeout* : int

    The number of milliseconds the function will wait. 

instead of a literal value, you can specify one of the following values for the timeout:


## [win32pipe](#README.md#win32pipe).popen

pipe = **popen( *cmdstring*  *, mode* ** )
Popen that works from a GUI.

#### Parameters


     *cmdstring* : string

    The cmdstring to pass to the shell

     *mode* : string

    Either 'r' or 'w'

#### Return Value
The result of this function is a pipe (file) connected to the 

processes stdin or stdout, depending on the requested mode.

## [win32pipe](#README.md#win32pipe).popen2

(pipe, pipe) = **popen2( *cmdstring*  *, mode* ** )
Variation on[win32pipe::popen](#win32pipe.md#win32pipepopen)

#### Parameters


     *cmdstring* : string

    The cmdstring to pass to the shell

     *mode* : string

    Either 't' or 'b'

#### Return Value
The result of this function is a pipe (file) connected to the 

processes stdin, and a pipe connected to the processes stdout.

## [win32pipe](#README.md#win32pipe).popen3

(pipe, pipe, pipe) = **popen3( *cmdstring*  *, mode* ** )
Variation on[win32pipe::popen](#win32pipe.md#win32pipepopen)

#### Parameters


     *cmdstring* : string

    The cmdstring to pass to the shell

     *mode* : string

    Either 't' or 'b'

#### Return Value
The result of this function is 3 pipes - the processes stdin, stdout and stderr

## [win32pipe](#README.md#win32pipe).popen4

(pipe, pipe) = **popen4( *cmdstring*  *, mode* ** )
Variation on[win32pipe::popen](#win32pipe.md#win32pipepopen)

#### Parameters


     *cmdstring* : string

    The cmdstring to pass to the shell

     *mode* : string

    Either 't' or 'b'

#### Return Value
The result of this function is 2 pipes - the processes stdin, 

and stdout+stderr combined as a single pipe.