# isapi.threaded

## Module isapi.threaded_extension

An ISAPI extension base class implemented using a thread-pool.

#### Classes


  - [ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension)

    Base class for an ISAPI extension based around a thread-pool&nbsp;

## isapi.threaded_extension.ThreadPoolExtension Object

Base class for an ISAPI extension based around a thread-pool

#### Methods


  - [HandleDispatchError](isapi.threaded.md#isapi.threadedextension.threadpoolextension_handledispatcherror)

    Handles errors in the Dispatch method.&nbsp;

  - [Dispatch](isapi.threaded.md#isapi.threadedextension.threadpoolextension_dispatch)

    Overridden by the sub-class to handle connection requests.&nbsp;

## [isapi.threaded_extension.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension).Dispatch

 __Dispatch(__ )
Overridden by the sub-class to handle connection requests.

#### Comments
This class creates a thread-pool using a Windows completion port, 

and dispatches requests via this port.  Sub-classes can generally 

implement each connection request using blocking reads and writes, and 

the thread-pool will still provide decent response to the end user.
The sub-class can set a max_workers attribute (default is 20).  Note 

that this generally does *not* mean 20 threads will all be concurrently 

running, via the magic of Windows completion ports.
There is no default implementation - sub-classes must implement this.

## [isapi.threaded_extension.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension).Dispatch

 __Dispatch( *self*  *, ecb* __ )
Overridden by the sub-class to handle connection requests.

#### Parameters


  -  *self* :

    self

  -  *ecb* :

    ecb

#### Comments
This class creates a thread-pool using a Windows completion port, 

and dispatches requests via this port.  Sub-classes can generally 

implement each connection request using blocking reads and writes, and 

the thread-pool will still provide decent response to the end user.
The sub-class can set a max_workers attribute (default is 20).  Note 

that this generally does *not* mean 20 threads will all be concurrently 

running, via the magic of Windows completion ports.
There is no default implementation - sub-classes must implement this.

## [isapi.threaded_extension.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension).HandleDispatchError

 __HandleDispatchError(__ )
Handles errors in the Dispatch method.

#### Comments
When a Dispatch method call fails, this method is called to handle 

the exception.  The default implementation formats the traceback 

in the browser.

## [isapi.threaded_extension.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension).HandleDispatchError

 __HandleDispatchError( *self*  *, ecb* __ )
Handles errors in the Dispatch method.

#### Parameters


  -  *self* :

    self

  -  *ecb* :

    ecb

#### Comments
When a Dispatch method call fails, this method is called to handle 

the exception.  The default implementation formats the traceback 

in the browser.

## INFINITE
 __const isapi.threaded_extension.INFINITE;__ 
INFINITE = -1 (0x-1)

## ISAPI_REQUEST
 __const isapi.threaded_extension.ISAPI_REQUEST;__ 
ISAPI_REQUEST = 1 (0x1)

## ISAPI_SHUTDOWN
 __const isapi.threaded_extension.ISAPI_SHUTDOWN;__ 
ISAPI_SHUTDOWN = 2 (0x2)