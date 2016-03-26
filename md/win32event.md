
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

## [win32event](README.md#win32event).CancelWaitableTimer

 **CancelWaitableTimer(** )
Cancels a waiting timer.

## [win32event](README.md#win32event).CreateEvent

[PyHANDLE](README.md#pyhandle)= **CreateEvent( *EventAttributes*  *, bManualReset*  *, bInitialState*  *, Name* ** )
Creates a waitable event

#### Parameters


  -  *EventAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *bManualReset* : bool

    flag for manual-reset event

  -  *bInitialState* : bool

    flag for initial state

  -  *Name* :[PyUnicode](README.md#pyunicode)

    event-object name, or None

#### Return Value
The result is a handle to the created object

## [win32event](README.md#win32event).CreateMutex

[PyHANDLE](README.md#pyhandle)= **CreateMutex( *MutexAttributes*  *, InitialOwner*  *, Name* ** )
Creates a mutex

#### Parameters


  -  *MutexAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *InitialOwner* : bool

    flag for initial ownership

  -  *Name* :[PyUnicode](README.md#pyunicode)

    Mutex-object name, or None

#### Return Value
The result is a handle to the created object

## [win32event](README.md#win32event).CreateSemaphore

[PyHANDLE](README.md#pyhandle)= **CreateSemaphore( *SemaphoreAttributes*  *, InitialCount*  *, MaximumCount*  *, SemaphoreName* ** )
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


  - Search for *CreateSemaphore* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createsemaphore),[google](README.md#http://www.google.com/search?q=createsemaphore)or[google groups](README.md#http://groups.google.com/groups?q=createsemaphore).

#### Return Value
The result is a handle to the object

## [win32event](README.md#win32event).CreateWaitableTimer

[PyHANDLE](README.md#pyhandle)= **CreateWaitableTimer( *TimerAttributes*  *, ManualReset*  *, TimerName* ** )
Creates a waitable timer, or opens an existing one

#### Parameters


  -  *TimerAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *ManualReset* : bool

    True for manual reset timer, or False to create a synchronization timer

  -  *TimerName* : str

    Timer object name, or None

#### Win32 API References


  - Search for *CreateWaitableTimer* at[msdn](README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createwaitabletimer),[google](README.md#http://www.google.com/search?q=createwaitabletimer)or[google groups](README.md#http://groups.google.com/groups?q=createwaitabletimer).

#### Return Value
The result is a handle to the object

## EVENT_ALL_ACCESS
 **const win32event.EVENT_ALL_ACCESS;** 
Specifies all possible access flags for the event object.

## EVENT_MODIFY_STATE
 **const win32event.EVENT_MODIFY_STATE;** 
Enables use of the event handle in the SetEvent and ResetEvent&#160functions to modify the event&#146s state.

## INFINITE
 **const win32event.INFINITE;** 


## MAXIMUM_WAIT_OBJECTS
 **const win32event.MAXIMUM_WAIT_OBJECTS;** 


## [win32event](README.md#win32event).MsgWaitForMultipleObjects

int = **MsgWaitForMultipleObjects( *handleList*  *, bWaitAll*  *, milliseconds*  *, wakeMask* ** )
Returns when a message arrives of an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](README.md#pyhandle), ...]

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

## [win32event](README.md#win32event).MsgWaitForMultipleObjectsEx

int = **MsgWaitForMultipleObjectsEx( *handleList*  *, milliseconds*  *, wakeMask*  *, waitFlags* ** )
Returns when a message arrives of an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](README.md#pyhandle), ...]

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

## [win32event](README.md#win32event).OpenEvent

[PyHANDLE](README.md#pyhandle)= **OpenEvent( *desiredAccess*  *, bInheritHandle*  *, name* ** )
Returns a handle of an existing named event object.

#### Parameters


  -  *desiredAccess* : int

    access flag - one of **win32event::EVENT_ALL_ACCESS** , **win32event::EVENT_MODIFY_STATE** , or (NT only) **win32event::SYNCHRONIZE** 

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](README.md#pyunicode)

    name of event to open.

## [win32event](README.md#win32event).OpenMutex

[PyHANDLE](README.md#pyhandle)= **OpenMutex( *desiredAccess*  *, bInheritHandle*  *, name* ** )
Returns a handle of an existing named mutex object.

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](README.md#pyunicode)

    name of mutex to open.

## [win32event](README.md#win32event).OpenSemaphore

[PyHANDLE](README.md#pyhandle)= **OpenSemaphore( *desiredAccess*  *, bInheritHandle*  *, name* ** )
Returns a handle of an existing named semaphore object.

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](README.md#pyunicode)

    name of semaphore to open.

## [win32event](README.md#win32event).OpenWaitableTimer

[PyHANDLE](README.md#pyhandle)= **OpenWaitableTimer( *desiredAccess*  *, bInheritHandle*  *, timerName* ** )
Opens an existing named waitable timer object

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *timerName* : str

    pointer to timer object name

## [win32event](README.md#win32event).PulseEvent

 **PulseEvent( *hEvent* ** )
Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.

#### Parameters


  -  *hEvent* :[PyHANDLE](README.md#pyhandle)

    handle of event object

## QS_ALLEVENTS
 **const win32event.QS_ALLEVENTS;** 
An input, WM_TIMER, WM_PAINT, WM_HOTKEY, or posted message is in the queue.

## QS_ALLINPUT
 **const win32event.QS_ALLINPUT;** 
Any message is in the queue.

## QS_HOTKEY
 **const win32event.QS_HOTKEY;** 
A WM_HOTKEY message is in the queue.

## QS_INPUT
 **const win32event.QS_INPUT;** 
An input message is in the queue.

## QS_KEY
 **const win32event.QS_KEY;** 
A WM_KEYUP, WM_KEYDOWN, WM_SYSKEYUP, or WM_SYSKEYDOWN message is in the queue.

## QS_MOUSE
 **const win32event.QS_MOUSE;** 
A WM_MOUSEMOVE message or mouse-button message (WM_LBUTTONUP, WM_RBUTTONDOWN, and so on).

## QS_MOUSEBUTTON
 **const win32event.QS_MOUSEBUTTON;** 
A mouse-button message (WM_LBUTTONUP, WM_RBUTTONDOWN, and so on).

## QS_MOUSEMOVE
 **const win32event.QS_MOUSEMOVE;** 
A WM_MOUSEMOVE message is in the queue.

## QS_PAINT
 **const win32event.QS_PAINT;** 
A WM_PAINT message is in the queue.

## QS_POSTMESSAGE
 **const win32event.QS_POSTMESSAGE;** 
A posted message (other than those just listed) is in the queue.

## QS_SENDMESSAGE
 **const win32event.QS_SENDMESSAGE;** 
A message sent by another thread or application is in the queue.

## QS_TIMER
 **const win32event.QS_TIMER;** 
A WM_TIMER message is in the queue.

## [win32event](README.md#win32event).ReleaseMutex

 **ReleaseMutex( *hEvent* ** )
Releases a mutex.

#### Parameters


  -  *hEvent* :[PyHANDLE](README.md#pyhandle)

    handle of mutex object

## [win32event](README.md#win32event).ReleaseSemaphore

int = **ReleaseSemaphore( *hEvent*  *, lReleaseCount* ** )
Releases a semaphore.

#### Parameters


  -  *hEvent* :[PyHANDLE](README.md#pyhandle)

    handle of the semaphore object

  -  *lReleaseCount* : int

    amount to add to current count

#### Return Value
The result is the previous count of the semaphore.

## [win32event](README.md#win32event).ResetEvent

 **ResetEvent( *hEvent* ** )
Resets an event

#### Parameters


  -  *hEvent* :[PyHANDLE](README.md#pyhandle)

    handle of event object

## SYNCHRONIZE
 **const win32event.SYNCHRONIZE;** 
Windows NT only:&#160Enables use of the event handle in any of the wait functions&#160to wait for the event&#146s state to be signaled.

## [win32event](README.md#win32event).SetEvent

 **SetEvent( *hEvent* ** )
Sets an event

#### Parameters


  -  *hEvent* :[PyHANDLE](README.md#pyhandle)

    handle of event object

## [win32event](README.md#win32event).SetWaitableTimer

 **SetWaitableTimer( *handle*  *, dueTime*  *, period*  *, func*  *, param*  *, resume_state* ** )
Sets a waitable timer.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

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
 **const win32event.WAIT_ABANDONED;** 


## WAIT_ABANDONED_0
 **const win32event.WAIT_ABANDONED_0;** 


## WAIT_FAILED
 **const win32event.WAIT_FAILED;** 


## WAIT_IO_COMPLETION
 **const win32event.WAIT_IO_COMPLETION;** 


## WAIT_OBJECT_0
 **const win32event.WAIT_OBJECT_0;** 


## WAIT_TIMEOUT
 **const win32event.WAIT_TIMEOUT;** 


## [win32event](README.md#win32event).WaitForInputIdle

int = **WaitForInputIdle( *hProcess*  *, milliseconds* ** )
Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    handle of process to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

#### Return Value
The return value indicates wether the process is ready or wether it timed out. This value can be one of the following.


## [win32event](README.md#win32event).WaitForMultipleObjects

int = **WaitForMultipleObjects( *handleList*  *, bWaitAll*  *, milliseconds* ** )
Returns when an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](README.md#pyhandle), ...]

    A sequence of handles to wait on.

  -  *bWaitAll* : bool

    wait flag

  -  *milliseconds* : int

    time-out interval in milliseconds

## [win32event](README.md#win32event).WaitForMultipleObjectsEx

int = **WaitForMultipleObjectsEx( *handleList*  *, bWaitAll*  *, milliseconds*  *, bAlertable* ** )
Returns when an event is signalled

#### Parameters


  -  *handleList* : [[PyHANDLE](README.md#pyhandle), ...]

    A sequence of handles to wait on.

  -  *bWaitAll* : bool

    wait flag

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *bAlertable* : bool

    alertable wait flag.

## [win32event](README.md#win32event).WaitForSingleObject

int = **WaitForSingleObject( *hHandle*  *, milliseconds* ** )
Returns when an event is signalled

#### Parameters


  -  *hHandle* :[PyHANDLE](README.md#pyhandle)

    handle of object to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

#### Return Value
If the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.


## [win32event](README.md#win32event).WaitForSingleObjectEx

int = **WaitForSingleObjectEx( *hHandle*  *, milliseconds*  *, bAlertable* ** )
Returns when an event is signalled

#### Parameters


  -  *hHandle* :[PyHANDLE](README.md#pyhandle)

    handle of object to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *bAlertable* : bool

    alertable wait flag.

#### Return Value
See[win32event::WaitForSingleObject](win32event.md#win32eventwaitforsingleobject)for return values.