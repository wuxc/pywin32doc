# win32event

## Module win32event

A module which provides an interface to the win32 event/wait API

#### Methods


  - [CancelWaitableTimer](win32event.md#win32eventcancelwaitabletimer)

    Cancels a waiting timer.&nbsp;

  - [CreateEvent](win32event.md#win32eventcreateevent)

    Creates a waitable event&nbsp;

  - [CreateMutex](win32event.md#win32eventcreatemutex)

    Creates a mutex&nbsp;

  - [CreateSemaphore](win32event.md#win32eventcreatesemaphore)

    Creates a semaphore, or opens an existing one&nbsp;

  - [CreateWaitableTimer](win32event.md#win32eventcreatewaitabletimer)

    Creates a waitable timer, or opens an existing one&nbsp;

  - [MsgWaitForMultipleObjects](win32event.md#win32eventmsgwaitformultipleobjects)

    Returns when a message arrives of an event is signalled&nbsp;

  - [MsgWaitForMultipleObjectsEx](win32event.md#win32eventmsgwaitformultipleobjectsex)

    Returns when a message arrives of an event is signalled&nbsp;

  - [OpenEvent](win32event.md#win32eventopenevent)

    Returns a handle of an existing named event object.&nbsp;

  - [OpenMutex](win32event.md#win32eventopenmutex)

    Returns a handle of an existing named mutex object.&nbsp;

  - [OpenSemaphore](win32event.md#win32eventopensemaphore)

    Returns a handle of an existing named semaphore object.&nbsp;

  - [OpenWaitableTimer](win32event.md#win32eventopenwaitabletimer)

    Opens an existing named waitable timer object&nbsp;

  - [PulseEvent](win32event.md#win32eventpulseevent)

    Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.&nbsp;

  - [ReleaseMutex](win32event.md#win32eventreleasemutex)

    Releases a mutex.&nbsp;

  - [ReleaseSemaphore](win32event.md#win32eventreleasesemaphore)

    Releases a semaphore.&nbsp;

  - [ResetEvent](win32event.md#win32eventresetevent)

    Resets an event&nbsp;

  - [SetEvent](win32event.md#win32eventsetevent)

    Sets an event&nbsp;

  - [SetWaitableTimer](win32event.md#win32eventsetwaitabletimer)

    Sets a waitable timer.&nbsp;

  - [WaitForMultipleObjects](win32event.md#win32eventwaitformultipleobjects)

    Returns when an event is signalled&nbsp;

  - [WaitForMultipleObjectsEx](win32event.md#win32eventwaitformultipleobjectsex)

    Returns when an event is signalled&nbsp;

  - [WaitForSingleObject](win32event.md#win32eventwaitforsingleobject)

    Returns when an event is signalled&nbsp;

  - [WaitForSingleObjectEx](win32event.md#win32eventwaitforsingleobjectex)

    Returns when an event is signalled&nbsp;

  - [WaitForInputIdle](win32event.md#win32eventwaitforinputidle)

    Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed&nbsp;

## [win32event](#win32event).CancelWaitableTimer

 __CancelWaitableTimer(__ )
Cancels a waiting timer.

## [win32event](#win32event).CreateEvent

[PyHANDLE](#pyhandle)= __CreateEvent( *EventAttributes*  *, bManualReset*  *, bInitialState*  *, Name* __ )
Creates a waitable event

#### Parameters


  -  *EventAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *bManualReset* : bool

    flag for manual-reset event

  -  *bInitialState* : bool

    flag for initial state

  -  *Name* :[PyUnicode](#pyunicode)

    event-object name, or None

#### Return Value
The result is a handle to the created object

## [win32event](#win32event).CreateMutex

[PyHANDLE](#pyhandle)= __CreateMutex( *MutexAttributes*  *, InitialOwner*  *, Name* __ )
Creates a mutex

#### Parameters


  -  *MutexAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *InitialOwner* : bool

    flag for initial ownership

  -  *Name* :[PyUnicode](#pyunicode)

    Mutex-object name, or None

#### Return Value
The result is a handle to the created object

## [win32event](#win32event).CreateSemaphore

[PyHANDLE](#pyhandle)= __CreateSemaphore( *SemaphoreAttributes*  *, InitialCount*  *, MaximumCount*  *, SemaphoreName* __ )
Creates a semaphore, or opens an existing one

#### Parameters


  -  *SemaphoreAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *InitialCount* : int

    Initial count

  -  *MaximumCount* : int

    Maximum count

  -  *SemaphoreName* : str

    Semaphore-object name, or None

#### Win32 API References


  - Search for *CreateSemaphore* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createsemaphore),[google](#http://www.google.com/search?q=createsemaphore)or[google groups](#http://groups.google.com/groups?q=createsemaphore).

#### Return Value
The result is a handle to the object

## [win32event](#win32event).CreateWaitableTimer

[PyHANDLE](#pyhandle)= __CreateWaitableTimer( *TimerAttributes*  *, ManualReset*  *, TimerName* __ )
Creates a waitable timer, or opens an existing one

#### Parameters


  -  *TimerAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *ManualReset* : bool

    True for manual reset timer, or False to create a synchronization timer

  -  *TimerName* : str

    Timer object name, or None

#### Win32 API References


  - Search for *CreateWaitableTimer* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createwaitabletimer),[google](#http://www.google.com/search?q=createwaitabletimer)or[google groups](#http://groups.google.com/groups?q=createwaitabletimer).

#### Return Value
The result is a handle to the object

## EVENT_ALL_ACCESS
 __const win32event.EVENT_ALL_ACCESS;__ 
Specifies all possible access flags for the event object.

## EVENT_MODIFY_STATE
 __const win32event.EVENT_MODIFY_STATE;__ 
Enables use of the event handle in the SetEvent and ResetEvent&#160functions to modify the event&#146s state.

## INFINITE
 __const win32event.INFINITE;__ 


## MAXIMUM_WAIT_OBJECTS
 __const win32event.MAXIMUM_WAIT_OBJECTS;__ 


## [win32event](#win32event).MsgWaitForMultipleObjects

int = __MsgWaitForMultipleObjects( *handleList*  *, bWaitAll*  *, milliseconds*  *, wakeMask* __ )
Returns when a message arrives of an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](#pyhandle), ...]

    A sequence of handles to wait on.

  -  *bWaitAll* : bool

    If true, waits for all handles in the list.

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *wakeMask* : int

    type of input events to wait for.  One of the win32event.QS_ constants.

#### Comments
Note that if bWaitAll is TRUE, the function will return when there is input in the queue, 

and all events are signalled.  This is rarely what you want! 

If input is waiting, the result is win32event.WAIT_OBJECT_0+len(handles))

## [win32event](#win32event).MsgWaitForMultipleObjectsEx

int = __MsgWaitForMultipleObjectsEx( *handleList*  *, milliseconds*  *, wakeMask*  *, waitFlags* __ )
Returns when a message arrives of an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](#pyhandle), ...]

    A sequence of handles to wait on.

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *wakeMask* : int

    type of input events to wait for

  -  *waitFlags* : int

    wait flags

#### Comments
This method will no longer raise a COM E_NOTIMPL exception 

as it is no longer dynamically loaded.

## [win32event](#win32event).OpenEvent

[PyHANDLE](#pyhandle)= __OpenEvent( *desiredAccess*  *, bInheritHandle*  *, name* __ )
Returns a handle of an existing named event object.

#### Parameters


  -  *desiredAccess* : int

    access flag - one of __win32event::EVENT_ALL_ACCESS__ , __win32event::EVENT_MODIFY_STATE__ , or (NT only) __win32event::SYNCHRONIZE__ 

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](#pyunicode)

    name of event to open.

## [win32event](#win32event).OpenMutex

[PyHANDLE](#pyhandle)= __OpenMutex( *desiredAccess*  *, bInheritHandle*  *, name* __ )
Returns a handle of an existing named mutex object.

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](#pyunicode)

    name of mutex to open.

## [win32event](#win32event).OpenSemaphore

[PyHANDLE](#pyhandle)= __OpenSemaphore( *desiredAccess*  *, bInheritHandle*  *, name* __ )
Returns a handle of an existing named semaphore object.

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](#pyunicode)

    name of semaphore to open.

## [win32event](#win32event).OpenWaitableTimer

[PyHANDLE](#pyhandle)= __OpenWaitableTimer( *desiredAccess*  *, bInheritHandle*  *, timerName* __ )
Opens an existing named waitable timer object

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *timerName* : str

    pointer to timer object name

## [win32event](#win32event).PulseEvent

 __PulseEvent( *hEvent* __ )
Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of event object

## QS_ALLEVENTS
 __const win32event.QS_ALLEVENTS;__ 
An input, WM_TIMER, WM_PAINT, WM_HOTKEY, or posted message is in the queue.

## QS_ALLINPUT
 __const win32event.QS_ALLINPUT;__ 
Any message is in the queue.

## QS_HOTKEY
 __const win32event.QS_HOTKEY;__ 
A WM_HOTKEY message is in the queue.

## QS_INPUT
 __const win32event.QS_INPUT;__ 
An input message is in the queue.

## QS_KEY
 __const win32event.QS_KEY;__ 
A WM_KEYUP, WM_KEYDOWN, WM_SYSKEYUP, or WM_SYSKEYDOWN message is in the queue.

## QS_MOUSE
 __const win32event.QS_MOUSE;__ 
A WM_MOUSEMOVE message or mouse-button message (WM_LBUTTONUP, WM_RBUTTONDOWN, and so on).

## QS_MOUSEBUTTON
 __const win32event.QS_MOUSEBUTTON;__ 
A mouse-button message (WM_LBUTTONUP, WM_RBUTTONDOWN, and so on).

## QS_MOUSEMOVE
 __const win32event.QS_MOUSEMOVE;__ 
A WM_MOUSEMOVE message is in the queue.

## QS_PAINT
 __const win32event.QS_PAINT;__ 
A WM_PAINT message is in the queue.

## QS_POSTMESSAGE
 __const win32event.QS_POSTMESSAGE;__ 
A posted message (other than those just listed) is in the queue.

## QS_SENDMESSAGE
 __const win32event.QS_SENDMESSAGE;__ 
A message sent by another thread or application is in the queue.

## QS_TIMER
 __const win32event.QS_TIMER;__ 
A WM_TIMER message is in the queue.

## [win32event](#win32event).ReleaseMutex

 __ReleaseMutex( *hEvent* __ )
Releases a mutex.

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of mutex object

## [win32event](#win32event).ReleaseSemaphore

int = __ReleaseSemaphore( *hEvent*  *, lReleaseCount* __ )
Releases a semaphore.

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of the semaphore object

  -  *lReleaseCount* : int

    amount to add to current count

#### Return Value
The result is the previous count of the semaphore.

## [win32event](#win32event).ResetEvent

 __ResetEvent( *hEvent* __ )
Resets an event

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of event object

## SYNCHRONIZE
 __const win32event.SYNCHRONIZE;__ 
Windows NT only:&#160Enables use of the event handle in any of the wait functions&#160to wait for the event&#146s state to be signaled.

## [win32event](#win32event).SetEvent

 __SetEvent( *hEvent* __ )
Sets an event

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of event object

## [win32event](#win32event).SetWaitableTimer

 __SetWaitableTimer( *handle*  *, dueTime*  *, period*  *, func*  *, param*  *, resume_state* __ )
Sets a waitable timer.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    handle to timer

  -  *dueTime* : long

    timer due time

  -  *period* : int

    timer interval

  -  *func* : object

    completion routine - must be None

  -  *param* : object

    completion routine parameter - must be None

  -  *resume_state* : bool

    resume state

## WAIT_ABANDONED
 __const win32event.WAIT_ABANDONED;__ 


## WAIT_ABANDONED_0
 __const win32event.WAIT_ABANDONED_0;__ 


## WAIT_FAILED
 __const win32event.WAIT_FAILED;__ 


## WAIT_IO_COMPLETION
 __const win32event.WAIT_IO_COMPLETION;__ 


## WAIT_OBJECT_0
 __const win32event.WAIT_OBJECT_0;__ 


## WAIT_TIMEOUT
 __const win32event.WAIT_TIMEOUT;__ 


## [win32event](#win32event).WaitForInputIdle

int = __WaitForInputIdle( *hProcess*  *, milliseconds* __ )
Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed

#### Parameters


  -  *hProcess* :[PyHANDLE](#pyhandle)

    handle of process to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

#### Return Value
The return value indicates wether the process is ready or wether it timed out. This value can be one of the following.


## [win32event](#win32event).WaitForMultipleObjects

int = __WaitForMultipleObjects( *handleList*  *, bWaitAll*  *, milliseconds* __ )
Returns when an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](#pyhandle), ...]

    A sequence of handles to wait on.

  -  *bWaitAll* : bool

    wait flag

  -  *milliseconds* : int

    time-out interval in milliseconds

## [win32event](#win32event).WaitForMultipleObjectsEx

int = __WaitForMultipleObjectsEx( *handleList*  *, bWaitAll*  *, milliseconds*  *, bAlertable* __ )
Returns when an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](#pyhandle), ...]

    A sequence of handles to wait on.

  -  *bWaitAll* : bool

    wait flag

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *bAlertable* : bool

    alertable wait flag.

## [win32event](#win32event).WaitForSingleObject

int = __WaitForSingleObject( *hHandle*  *, milliseconds* __ )
Returns when an event is signalled

#### Parameters


  -  *hHandle* :[PyHANDLE](#pyhandle)

    handle of object to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

#### Return Value
If the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.


## [win32event](#win32event).WaitForSingleObjectEx

int = __WaitForSingleObjectEx( *hHandle*  *, milliseconds*  *, bAlertable* __ )
Returns when an event is signalled

#### Parameters


  -  *hHandle* :[PyHANDLE](#pyhandle)

    handle of object to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *bAlertable* : bool

    alertable wait flag.

#### Return Value
See[win32event::WaitForSingleObject](win32event.md#win32eventwaitforsingleobject)for return values.