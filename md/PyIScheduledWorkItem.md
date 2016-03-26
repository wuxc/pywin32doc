# PyIScheduledWorkItem

## PyIScheduledWorkItem Object

Python object that encapsulates the IScheduledWorkItem interface

#### Methods


  - [CreateTrigger](PyIScheduledWorkItem.md#pyischeduledworkitemcreatetrigger)

    Creates a new trigger for a task, returns index and new ITaskTrigger interface&nbsp;

  - [DeleteTrigger](PyIScheduledWorkItem.md#pyischeduledworkitemdeletetrigger)

    Deletes specified trigger&nbsp;

  - [GetTriggerCount](PyIScheduledWorkItem.md#pyischeduledworkitemgettriggercount)

    Returns number of triggers defined for the task&nbsp;

  - [GetTrigger](PyIScheduledWorkItem.md#pyischeduledworkitemgettrigger)

    Retrieves ITaskTrigger interface for specified trigger index&nbsp;

  - [GetTriggerString](PyIScheduledWorkItem.md#pyischeduledworkitemgettriggerstring)

    Creates a human-readable summary of specified trigger&nbsp;

  - [GetRunTimes](PyIScheduledWorkItem.md#pyischeduledworkitemgetruntimes)

    Return specified number of run times within given time frame&nbsp;

  - [GetNextRunTime](PyIScheduledWorkItem.md#pyischeduledworkitemgetnextruntime)

    Returns next time that task is scheduled to run&nbsp;

  - [SetIdleWait](PyIScheduledWorkItem.md#pyischeduledworkitemsetidlewait)

    Sets idle parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE&nbsp;

  - [GetIdleWait](PyIScheduledWorkItem.md#pyischeduledworkitemgetidlewait)

    Gets idle parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE&nbsp;

  - [Run](PyIScheduledWorkItem.md#pyischeduledworkitemrun)

    Starts task&nbsp;

  - [Terminate](PyIScheduledWorkItem.md#pyischeduledworkitemterminate)

    Terminate process if task is running&nbsp;

  - [EditWorkItem](PyIScheduledWorkItem.md#pyischeduledworkitemeditworkitem)

    Brings up standard Scheduled Task dialog&nbsp;

  - [GetMostRecentRunTime](PyIScheduledWorkItem.md#pyischeduledworkitemgetmostrecentruntime)

    Returns last time task ran&nbsp;

  - [GetStatus](PyIScheduledWorkItem.md#pyischeduledworkitemgetstatus)

    Returns status (SCHED_S_TASK... constants)&nbsp;

  - [GetExitCode](PyIScheduledWorkItem.md#pyischeduledworkitemgetexitcode)

    Returns tuple of task's exit code and error returned to Task Scheduler if process could not start&nbsp;

  - [SetComment](PyIScheduledWorkItem.md#pyischeduledworkitemsetcomment)

    Set comment string for task&nbsp;

  - [GetComment](PyIScheduledWorkItem.md#pyischeduledworkitemgetcomment)

    Return comment string associated with task.&nbsp;

  - [SetCreator](PyIScheduledWorkItem.md#pyischeduledworkitemsetcreator)

    Specify who (or what) created task, can be any string&nbsp;

  - [GetCreator](PyIScheduledWorkItem.md#pyischeduledworkitemgetcreator)

    Returns creator info, can be any string data&nbsp;

  - [SetWorkItemData](PyIScheduledWorkItem.md#pyischeduledworkitemsetworkitemdata)

    Set data associated with task (treated as uninterpreted bytes)&nbsp;

  - [GetWorkItemData](PyIScheduledWorkItem.md#pyischeduledworkitemgetworkitemdata)

    Retrieve data associated with task&nbsp;

  - [SetErrorRetryCount](PyIScheduledWorkItem.md#pyischeduledworkitemseterrorretrycount)

    Specify nbr of times to attempt to run task if it can't start (not currently implemented)&nbsp;

  - [GetErrorRetryCount](PyIScheduledWorkItem.md#pyischeduledworkitemgeterrorretrycount)

    Return nbr of times Task scheduler should try to run task (not currently implemented)&nbsp;

  - [SetErrorRetryInterval](PyIScheduledWorkItem.md#pyischeduledworkitemseterrorretryinterval)

    Interval in minutes between attempts to run task. Not implemented according to SDK&nbsp;

  - [GetErrorRetryInterval](PyIScheduledWorkItem.md#pyischeduledworkitemgeterrorretryinterval)

    Returns nbr of minutes between attempts to run task. Not implemented according to SDK&nbsp;

  - [SetFlags](PyIScheduledWorkItem.md#pyischeduledworkitemsetflags)

    Set flags for task&nbsp;

  - [GetFlags](PyIScheduledWorkItem.md#pyischeduledworkitemgetflags)

    Returns flags for task (TASK_FLAG_* constants)&nbsp;

  - [SetAccountInformation](PyIScheduledWorkItem.md#pyischeduledworkitemsetaccountinformation)

    Set username and password under which task will run&nbsp;

  - [GetAccountInformation](PyIScheduledWorkItem.md#pyischeduledworkitemgetaccountinformation)

    Returns username that task will run under&nbsp;

## [PyIScheduledWorkItem](#pyischeduledworkitem).CreateTrigger

int,PyITaskTrigger = __CreateTrigger(__ )
Creates a new trigger for a task, returns index and new ITaskTrigger interface

## [PyIScheduledWorkItem](#pyischeduledworkitem).DeleteTrigger

 __DeleteTrigger( *Trigger* __ )
Deletes specified trigger

#### Parameters


  -  *Trigger* : int

    Index of trigger to delete

## [PyIScheduledWorkItem](#pyischeduledworkitem).EditWorkItem

 __EditWorkItem( *hParent*  *, dwReserved* __ )
Brings up standard Scheduled Task dialog

#### Parameters


  -  *hParent* :[PyHANDLE](#pyhandle)

    Reserved, use 0 or None if passed

  -  *dwReserved* : int

    Reserved, use 0 if passed

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetAccountInformation

[PyUNICODE](#pyunicode)= __GetAccountInformation(__ )
Returns username that task will run under

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetComment

[PyUnicode](#pyunicode)= __GetComment(__ )
Return comment string associated with task.

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetCreator

 __GetCreator(__ )
Returns creator info, can be any string data

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetErrorRetryCount

 __GetErrorRetryCount(__ )
Return nbr of times Task scheduler should try to run task (not currently implemented)

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetErrorRetryInterval

 __GetErrorRetryInterval(__ )
Returns nbr of minutes between attempts to run task. Not implemented according to SDK

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetExitCode

(int,int) = __GetExitCode(__ )
Returns tuple of task's exit code and error returned to Task Scheduler if process could not start

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetFlags

int = __GetFlags(__ )
Returns flags for task (TASK_FLAG_* constants)

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetIdleWait

int,int = __GetIdleWait(__ )
Gets IdleMinutes and DeadlineMinutes parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetMostRecentRunTime

[PyTime](#pytime)= __GetMostRecentRunTime(__ )
Returns last time task ran

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetNextRunTime

[PyTime](#pytime)= __GetNextRunTime(__ )
Returns next time that task is scheduled to run

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetRunTimes

([PyTime](#pytime),,,) = __GetRunTimes( *Count*  *, Begin*  *, End* __ )
Return specified number of run times within given time frame

#### Parameters


  -  *Count* : int

    Number of run times to retrieve

  -  *Begin* :[PyTime](#pytime)

    Start time, defaults to current time if not passed or None

  -  *End* :[PyTime](#pytime)

    End time, defaults to unlimited if not passed or None

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetStatus

int = __GetStatus(__ )
Returns status (SCHED_S_TASK... constants)

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetTrigger

[PyITaskTrigger](#pyitasktrigger)= __GetTrigger( *iTrigger* __ )
Retrieves ITaskTrigger interface for specified trigger index

#### Parameters


  -  *iTrigger* : int

    Index of trigger to retrieve

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetTriggerCount

int = __GetTriggerCount(__ )
Returns number of triggers defined for the task

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetTriggerString

[PyUNICODE](#pyunicode)= __GetTriggerString(__ )
Creates a human-readable summary of specified trigger

## [PyIScheduledWorkItem](#pyischeduledworkitem).GetWorkItemData

string = __GetWorkItemData(__ )
Retrieve data associated with task

## [PyIScheduledWorkItem](#pyischeduledworkitem).Run

 __Run(__ )
Starts task

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetAccountInformation

 __SetAccountInformation( *AccountName*  *, Password* __ )
Set username and password under which task will run

#### Parameters


  -  *AccountName* : __unicode__ 

    AccountName, use "" for local system account (can only be used by Administrators)

  -  *Password* : __unicode__ 

    Password - Can be None for local System account, or if TASK_FLAG_RUN_ONLY_IF_LOGGED_ON is set

#### Comments
On some systems, username and password are verified at the time the task is saved, on others when the task tries to run

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetComment

 __SetComment( *Comment* __ )
Set comment string for task

#### Parameters


  -  *Comment* : __unicode__ 

    Freeform comment string

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetCreator

 __SetCreator( *Creator* __ )
Specify who (or what) created task, can be any string

#### Parameters


  -  *Creator* : __unicode__ 

    Originator of task, does not have to be valid username

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetErrorRetryCount

 __SetErrorRetryCount( *wRetryCount* __ )
Specify nbr of times to attempt to run task if it can't start (not currently implemented)

#### Parameters


  -  *wRetryCount* : int

    Nbr of attemps to start task

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetErrorRetryInterval

 __SetErrorRetryInterval( *RetryInterval* __ )
Interval in minutes between attempts to run task. Not implemented according to SDK

#### Parameters


  -  *RetryInterval* : int

    Interval in minutes

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetFlags

 __SetFlags( *dwFlags* __ )
Set flags for task

#### Parameters


  -  *dwFlags* : int

    Combination of TASK_FLAG_* constants

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetIdleWait

 __SetIdleWait( *wIdleMinutes*  *, wDeadlineMinutes* __ )
Sets idle parms for task with trigger of type TASK_EVENT_TRIGGER_ON_IDLE

#### Parameters


  -  *wIdleMinutes* : int

    Nbr of minutes computer must be idle before task fires

  -  *wDeadlineMinutes* : int

    Maximum nbr of minutes task will wait for computer to become idle

## [PyIScheduledWorkItem](#pyischeduledworkitem).SetWorkItemData

 __SetWorkItemData( *Data* __ )
Set data associated with task (treated as uninterpreted bytes)

#### Parameters


  -  *Data* : string

    Character data, treated as uninterpreted bytes

## [PyIScheduledWorkItem](#pyischeduledworkitem).Terminate

 __Terminate(__ )
Terminate process if task is running