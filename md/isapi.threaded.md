# isapi.threaded

## Module isapi\.threaded\_extension

An ISAPI extension base class implemented using a thread-pool\.

#### Classes


  - [ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension)

    Base class for an ISAPI extension based around a thread-pool&nbsp;

## isapi\.threaded\_extension\.ThreadPoolExtension Object

Base class for an ISAPI extension based around a thread-pool

#### Methods


  - [HandleDispatchError](isapi.threaded.md#isapi.threadedextension.threadpoolextension_handledispatcherror)

    Handles errors in the Dispatch method\.&nbsp;

  - [Dispatch](isapi.threaded.md#isapi.threadedextension.threadpoolextension_dispatch)

    Overridden by the sub-class to handle connection requests\.&nbsp;

## [isapi\.threaded\_extension\.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension)\.Dispatch

 **Dispatch\(** \)
Overridden by the sub-class to handle connection requests\.

#### Comments
This class creates a thread-pool using a Windows completion port, 

and dispatches requests via this port\.  Sub-classes can generally 

implement each connection request using blocking reads and writes, and 

the thread-pool will still provide decent response to the end user\.
The sub-class can set a max\_workers attribute \(default is 20\)\.  Note 

that this generally does \*not\* mean 20 threads will all be concurrently 

running, via the magic of Windows completion ports\.
There is no default implementation - sub-classes must implement this\.

## [isapi\.threaded\_extension\.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension)\.Dispatch

 **Dispatch\( *self*  *, ecb* ** \)
Overridden by the sub-class to handle connection requests\.

#### Parameters


  -  *self* :

    self

  -  *ecb* :

    ecb

#### Comments
This class creates a thread-pool using a Windows completion port, 

and dispatches requests via this port\.  Sub-classes can generally 

implement each connection request using blocking reads and writes, and 

the thread-pool will still provide decent response to the end user\.
The sub-class can set a max\_workers attribute \(default is 20\)\.  Note 

that this generally does \*not\* mean 20 threads will all be concurrently 

running, via the magic of Windows completion ports\.
There is no default implementation - sub-classes must implement this\.

## [isapi\.threaded\_extension\.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension)\.HandleDispatchError

 **HandleDispatchError\(** \)
Handles errors in the Dispatch method\.

#### Comments
When a Dispatch method call fails, this method is called to handle 

the exception\.  The default implementation formats the traceback 

in the browser\.

## [isapi\.threaded\_extension\.ThreadPoolExtension](isapi.threaded.md#isapi.threadedextension.threadpoolextension)\.HandleDispatchError

 **HandleDispatchError\( *self*  *, ecb* ** \)
Handles errors in the Dispatch method\.

#### Parameters


  -  *self* :

    self

  -  *ecb* :

    ecb

#### Comments
When a Dispatch method call fails, this method is called to handle 

the exception\.  The default implementation formats the traceback 

in the browser\.

## INFINITE
 **const isapi\.threaded\_extension\.INFINITE;** 
INFINITE \= -1 \(0x-1\)

## ISAPI\_REQUEST
 **const isapi\.threaded\_extension\.ISAPI\_REQUEST;** 
ISAPI\_REQUEST \= 1 \(0x1\)

## ISAPI\_SHUTDOWN
 **const isapi\.threaded\_extension\.ISAPI\_SHUTDOWN;** 
ISAPI\_SHUTDOWN \= 2 \(0x2\)