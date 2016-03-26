# win32event

## Module win32event

A module which provides an interface to the win32 event/wait API

#### Methods


  - [CancelWaitableTimer](win32event.md#win32eventcancelwaitabletimer)

    Cancels a waiting timer\.&nbsp;

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

    Returns a handle of an existing named event object\.&nbsp;

  - [OpenMutex](win32event.md#win32eventopenmutex)

    Returns a handle of an existing named mutex object\.&nbsp;

  - [OpenSemaphore](win32event.md#win32eventopensemaphore)

    Returns a handle of an existing named semaphore object\.&nbsp;

  - [OpenWaitableTimer](win32event.md#win32eventopenwaitabletimer)

    Opens an existing named waitable timer object&nbsp;

  - [PulseEvent](win32event.md#win32eventpulseevent)

    Provides a single operation that sets \(to signaled\) the state of the specified event object and then resets it \(to nonsignaled\) after releasing the appropriate number of waiting threads\.&nbsp;

  - [ReleaseMutex](win32event.md#win32eventreleasemutex)

    Releases a mutex\.&nbsp;

  - [ReleaseSemaphore](win32event.md#win32eventreleasesemaphore)

    Releases a semaphore\.&nbsp;

  - [ResetEvent](win32event.md#win32eventresetevent)

    Resets an event&nbsp;

  - [SetEvent](win32event.md#win32eventsetevent)

    Sets an event&nbsp;

  - [SetWaitableTimer](win32event.md#win32eventsetwaitabletimer)

    Sets a waitable timer\.&nbsp;

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

## [win32event](#win32event)\.CancelWaitableTimer

 **CancelWaitableTimer\(** \)
Cancels a waiting timer\.

## [win32event](#win32event)\.CreateEvent

[PyHANDLE](#pyhandle)\= **CreateEvent\( *EventAttributes*  *, bManualReset*  *, bInitialState*  *, Name* ** \)
Creates a waitable event

#### Parameters


  -  *EventAttributes* :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *bManualReset* : bool

    flag for manual-reset event

  -  *bInitialState* : bool

    flag for initial state

  -  *Name* :[PyUnicode](#pyunicode)

    event-object name, or None

#### Return Value
The result is a handle to the created object

## [win32event](#win32event)\.CreateMutex

[PyHANDLE](#pyhandle)\= **CreateMutex\( *MutexAttributes*  *, InitialOwner*  *, Name* ** \)
Creates a mutex

#### Parameters


  -  *MutexAttributes* :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *InitialOwner* : bool

    flag for initial ownership

  -  *Name* :[PyUnicode](#pyunicode)

    Mutex-object name, or None

#### Return Value
The result is a handle to the created object

## [win32event](#win32event)\.CreateSemaphore

[PyHANDLE](#pyhandle)\= **CreateSemaphore\( *SemaphoreAttributes*  *, InitialCount*  *, MaximumCount*  *, SemaphoreName* ** \)
Creates a semaphore, or opens an existing one

#### Parameters


  -  *SemaphoreAttributes* :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *InitialCount* : int

    Initial count

  -  *MaximumCount* : int

    Maximum count

  -  *SemaphoreName* : str

    Semaphore-object name, or None

#### Win32 API References


  - Search for *CreateSemaphore* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createsemaphore),[google](#http://www.google.com/search?q=createsemaphore)or[google groups](#http://groups.google.com/groups?q=createsemaphore)\.

#### Return Value
The result is a handle to the object

## [win32event](#win32event)\.CreateWaitableTimer

[PyHANDLE](#pyhandle)\= **CreateWaitableTimer\( *TimerAttributes*  *, ManualReset*  *, TimerName* ** \)
Creates a waitable timer, or opens an existing one

#### Parameters


  -  *TimerAttributes* :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies inheritance and security descriptor for object, or None for defaults

  -  *ManualReset* : bool

    True for manual reset timer, or False to create a synchronization timer

  -  *TimerName* : str

    Timer object name, or None

#### Win32 API References


  - Search for *CreateWaitableTimer* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createwaitabletimer),[google](#http://www.google.com/search?q=createwaitabletimer)or[google groups](#http://groups.google.com/groups?q=createwaitabletimer)\.

#### Return Value
The result is a handle to the object

## EVENT\_ALL\_ACCESS
 **const win32event\.EVENT\_ALL\_ACCESS;** 
Specifies all possible access flags for the event object\.

## EVENT\_MODIFY\_STATE
 **const win32event\.EVENT\_MODIFY\_STATE;** 
Enables use of the event handle in the SetEvent and ResetEvent&\#160functions to modify the event&\#146s state\.

## INFINITE
 **const win32event\.INFINITE;** 


## MAXIMUM\_WAIT\_OBJECTS
 **const win32event\.MAXIMUM\_WAIT\_OBJECTS;** 


## [win32event](#win32event)\.MsgWaitForMultipleObjects

int \= **MsgWaitForMultipleObjects\( *handleList*  *, bWaitAll*  *, milliseconds*  *, wakeMask* ** \)
Returns when a message arrives of an event is signalled

#### Parameters


  -  *handleList* : \[[PyHANDLE](#pyhandle), \.\.\.\]

    A sequence of handles to wait on\.

  -  *bWaitAll* : bool

    If true, waits for all handles in the list\.

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *wakeMask* : int

    type of input events to wait for\.  One of the win32event\.QS\_ constants\.

#### Comments
Note that if bWaitAll is TRUE, the function will return when there is input in the queue, 

and all events are signalled\.  This is rarely what you want\! 

If input is waiting, the result is win32event\.WAIT\_OBJECT\_0\+len\(handles\)\)

## [win32event](#win32event)\.MsgWaitForMultipleObjectsEx

int \= **MsgWaitForMultipleObjectsEx\( *handleList*  *, milliseconds*  *, wakeMask*  *, waitFlags* ** \)
Returns when a message arrives of an event is signalled

#### Parameters


  -  *handleList* : \[[PyHANDLE](#pyhandle), \.\.\.\]

    A sequence of handles to wait on\.

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *wakeMask* : int

    type of input events to wait for

  -  *waitFlags* : int

    wait flags

#### Comments
This method will no longer raise a COM E\_NOTIMPL exception 

as it is no longer dynamically loaded\.

## [win32event](#win32event)\.OpenEvent

[PyHANDLE](#pyhandle)\= **OpenEvent\( *desiredAccess*  *, bInheritHandle*  *, name* ** \)
Returns a handle of an existing named event object\.

#### Parameters


  -  *desiredAccess* : int

    access flag - one of **win32event::EVENT\_ALL\_ACCESS** , **win32event::EVENT\_MODIFY\_STATE** , or \(NT only\) **win32event::SYNCHRONIZE** 

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](#pyunicode)

    name of event to open\.

## [win32event](#win32event)\.OpenMutex

[PyHANDLE](#pyhandle)\= **OpenMutex\( *desiredAccess*  *, bInheritHandle*  *, name* ** \)
Returns a handle of an existing named mutex object\.

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](#pyunicode)

    name of mutex to open\.

## [win32event](#win32event)\.OpenSemaphore

[PyHANDLE](#pyhandle)\= **OpenSemaphore\( *desiredAccess*  *, bInheritHandle*  *, name* ** \)
Returns a handle of an existing named semaphore object\.

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *name* :[PyUnicode](#pyunicode)

    name of semaphore to open\.

## [win32event](#win32event)\.OpenWaitableTimer

[PyHANDLE](#pyhandle)\= **OpenWaitableTimer\( *desiredAccess*  *, bInheritHandle*  *, timerName* ** \)
Opens an existing named waitable timer object

#### Parameters


  -  *desiredAccess* : int

    access flag

  -  *bInheritHandle* : bool

    inherit flag

  -  *timerName* : str

    pointer to timer object name

## [win32event](#win32event)\.PulseEvent

 **PulseEvent\( *hEvent* ** \)
Provides a single operation that sets \(to signaled\) the state of the specified event object and then resets it \(to nonsignaled\) after releasing the appropriate number of waiting threads\.

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of event object

## QS\_ALLEVENTS
 **const win32event\.QS\_ALLEVENTS;** 
An input, WM\_TIMER, WM\_PAINT, WM\_HOTKEY, or posted message is in the queue\.

## QS\_ALLINPUT
 **const win32event\.QS\_ALLINPUT;** 
Any message is in the queue\.

## QS\_HOTKEY
 **const win32event\.QS\_HOTKEY;** 
A WM\_HOTKEY message is in the queue\.

## QS\_INPUT
 **const win32event\.QS\_INPUT;** 
An input message is in the queue\.

## QS\_KEY
 **const win32event\.QS\_KEY;** 
A WM\_KEYUP, WM\_KEYDOWN, WM\_SYSKEYUP, or WM\_SYSKEYDOWN message is in the queue\.

## QS\_MOUSE
 **const win32event\.QS\_MOUSE;** 
A WM\_MOUSEMOVE message or mouse-button message \(WM\_LBUTTONUP, WM\_RBUTTONDOWN, and so on\)\.

## QS\_MOUSEBUTTON
 **const win32event\.QS\_MOUSEBUTTON;** 
A mouse-button message \(WM\_LBUTTONUP, WM\_RBUTTONDOWN, and so on\)\.

## QS\_MOUSEMOVE
 **const win32event\.QS\_MOUSEMOVE;** 
A WM\_MOUSEMOVE message is in the queue\.

## QS\_PAINT
 **const win32event\.QS\_PAINT;** 
A WM\_PAINT message is in the queue\.

## QS\_POSTMESSAGE
 **const win32event\.QS\_POSTMESSAGE;** 
A posted message \(other than those just listed\) is in the queue\.

## QS\_SENDMESSAGE
 **const win32event\.QS\_SENDMESSAGE;** 
A message sent by another thread or application is in the queue\.

## QS\_TIMER
 **const win32event\.QS\_TIMER;** 
A WM\_TIMER message is in the queue\.

## [win32event](#win32event)\.ReleaseMutex

 **ReleaseMutex\( *hEvent* ** \)
Releases a mutex\.

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of mutex object

## [win32event](#win32event)\.ReleaseSemaphore

int \= **ReleaseSemaphore\( *hEvent*  *, lReleaseCount* ** \)
Releases a semaphore\.

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of the semaphore object

  -  *lReleaseCount* : int

    amount to add to current count

#### Return Value
The result is the previous count of the semaphore\.

## [win32event](#win32event)\.ResetEvent

 **ResetEvent\( *hEvent* ** \)
Resets an event

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of event object

## SYNCHRONIZE
 **const win32event\.SYNCHRONIZE;** 
Windows NT only:&\#160Enables use of the event handle in any of the wait functions&\#160to wait for the event&\#146s state to be signaled\.

## [win32event](#win32event)\.SetEvent

 **SetEvent\( *hEvent* ** \)
Sets an event

#### Parameters


  -  *hEvent* :[PyHANDLE](#pyhandle)

    handle of event object

## [win32event](#win32event)\.SetWaitableTimer

 **SetWaitableTimer\( *handle*  *, dueTime*  *, period*  *, func*  *, param*  *, resume\_state* ** \)
Sets a waitable timer\.

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

  -  *resume\_state* : bool

    resume state

## WAIT\_ABANDONED
 **const win32event\.WAIT\_ABANDONED;** 


## WAIT\_ABANDONED\_0
 **const win32event\.WAIT\_ABANDONED\_0;** 


## WAIT\_FAILED
 **const win32event\.WAIT\_FAILED;** 


## WAIT\_IO\_COMPLETION
 **const win32event\.WAIT\_IO\_COMPLETION;** 


## WAIT\_OBJECT\_0
 **const win32event\.WAIT\_OBJECT\_0;** 


## WAIT\_TIMEOUT
 **const win32event\.WAIT\_TIMEOUT;** 


## [win32event](#win32event)\.WaitForInputIdle

int \= **WaitForInputIdle\( *hProcess*  *, milliseconds* ** \)
Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed

#### Parameters


  -  *hProcess* :[PyHANDLE](#pyhandle)

    handle of process to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

#### Return Value
The return value indicates wether the process is ready or wether it timed out\. This value can be one of the following\.


## [win32event](#win32event)\.WaitForMultipleObjects

int \= **WaitForMultipleObjects\( *handleList*  *, bWaitAll*  *, milliseconds* ** \)
Returns when an event is signalled

#### Parameters


  -  *handleList* : \[[PyHANDLE](#pyhandle), \.\.\.\]

    A sequence of handles to wait on\.

  -  *bWaitAll* : bool

    wait flag

  -  *milliseconds* : int

    time-out interval in milliseconds

## [win32event](#win32event)\.WaitForMultipleObjectsEx

int \= **WaitForMultipleObjectsEx\( *handleList*  *, bWaitAll*  *, milliseconds*  *, bAlertable* ** \)
Returns when an event is signalled

#### Parameters


  -  *handleList* : \[[PyHANDLE](#pyhandle), \.\.\.\]

    A sequence of handles to wait on\.

  -  *bWaitAll* : bool

    wait flag

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *bAlertable* : bool

    alertable wait flag\.

## [win32event](#win32event)\.WaitForSingleObject

int \= **WaitForSingleObject\( *hHandle*  *, milliseconds* ** \)
Returns when an event is signalled

#### Parameters


  -  *hHandle* :[PyHANDLE](#pyhandle)

    handle of object to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

#### Return Value
If the function succeeds, the return value indicates the event that caused the function to return\. This value can be one of the following\.


## [win32event](#win32event)\.WaitForSingleObjectEx

int \= **WaitForSingleObjectEx\( *hHandle*  *, milliseconds*  *, bAlertable* ** \)
Returns when an event is signalled

#### Parameters


  -  *hHandle* :[PyHANDLE](#pyhandle)

    handle of object to wait for

  -  *milliseconds* : int

    time-out interval in milliseconds

  -  *bAlertable* : bool

    alertable wait flag\.

#### Return Value
See[win32event::WaitForSingleObject](win32event.md#win32eventwaitforsingleobject)for return values\.