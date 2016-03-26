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

    Sets idle parms for task with trigger of type TASK\_EVENT\_TRIGGER\_ON\_IDLE&nbsp;

  - [GetIdleWait](PyIScheduledWorkItem.md#pyischeduledworkitemgetidlewait)

    Gets idle parms for task with trigger of type TASK\_EVENT\_TRIGGER\_ON\_IDLE&nbsp;

  - [Run](PyIScheduledWorkItem.md#pyischeduledworkitemrun)

    Starts task&nbsp;

  - [Terminate](PyIScheduledWorkItem.md#pyischeduledworkitemterminate)

    Terminate process if task is running&nbsp;

  - [EditWorkItem](PyIScheduledWorkItem.md#pyischeduledworkitemeditworkitem)

    Brings up standard Scheduled Task dialog&nbsp;

  - [GetMostRecentRunTime](PyIScheduledWorkItem.md#pyischeduledworkitemgetmostrecentruntime)

    Returns last time task ran&nbsp;

  - [GetStatus](PyIScheduledWorkItem.md#pyischeduledworkitemgetstatus)

    Returns status \(SCHED\_S\_TASK\.\.\. constants\)&nbsp;

  - [GetExitCode](PyIScheduledWorkItem.md#pyischeduledworkitemgetexitcode)

    Returns tuple of task's exit code and error returned to Task Scheduler if process could not start&nbsp;

  - [SetComment](PyIScheduledWorkItem.md#pyischeduledworkitemsetcomment)

    Set comment string for task&nbsp;

  - [GetComment](PyIScheduledWorkItem.md#pyischeduledworkitemgetcomment)

    Return comment string associated with task\.&nbsp;

  - [SetCreator](PyIScheduledWorkItem.md#pyischeduledworkitemsetcreator)

    Specify who \(or what\) created task, can be any string&nbsp;

  - [GetCreator](PyIScheduledWorkItem.md#pyischeduledworkitemgetcreator)

    Returns creator info, can be any string data&nbsp;

  - [SetWorkItemData](PyIScheduledWorkItem.md#pyischeduledworkitemsetworkitemdata)

    Set data associated with task \(treated as uninterpreted bytes\)&nbsp;

  - [GetWorkItemData](PyIScheduledWorkItem.md#pyischeduledworkitemgetworkitemdata)

    Retrieve data associated with task&nbsp;

  - [SetErrorRetryCount](PyIScheduledWorkItem.md#pyischeduledworkitemseterrorretrycount)

    Specify nbr of times to attempt to run task if it can't start \(not currently implemented\)&nbsp;

  - [GetErrorRetryCount](PyIScheduledWorkItem.md#pyischeduledworkitemgeterrorretrycount)

    Return nbr of times Task scheduler should try to run task \(not currently implemented\)&nbsp;

  - [SetErrorRetryInterval](PyIScheduledWorkItem.md#pyischeduledworkitemseterrorretryinterval)

    Interval in minutes between attempts to run task\. Not implemented according to SDK&nbsp;

  - [GetErrorRetryInterval](PyIScheduledWorkItem.md#pyischeduledworkitemgeterrorretryinterval)

    Returns nbr of minutes between attempts to run task\. Not implemented according to SDK&nbsp;

  - [SetFlags](PyIScheduledWorkItem.md#pyischeduledworkitemsetflags)

    Set flags for task&nbsp;

  - [GetFlags](PyIScheduledWorkItem.md#pyischeduledworkitemgetflags)

    Returns flags for task \(TASK\_FLAG\_\* constants\)&nbsp;

  - [SetAccountInformation](PyIScheduledWorkItem.md#pyischeduledworkitemsetaccountinformation)

    Set username and password under which task will run&nbsp;

  - [GetAccountInformation](PyIScheduledWorkItem.md#pyischeduledworkitemgetaccountinformation)

    Returns username that task will run under&nbsp;

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.CreateTrigger



int,PyITaskTrigger =CreateTrigger\(\)
Creates a new trigger for a task, returns index and new ITaskTrigger interface

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.DeleteTrigger

DeleteTrigger\(Trigger\)
Deletes specified trigger

#### Parameters


  - Trigger : int

    Index of trigger to delete

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.EditWorkItem

EditWorkItem\(hParent, dwReserved\)
Brings up standard Scheduled Task dialog

#### Parameters


  - hParent :[PyHANDLE](#pyhandle)

    Reserved, use 0 or None if passed

  - dwReserved : int

    Reserved, use 0 if passed

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetAccountInformation

[PyUNICODE](#pyunicode) =GetAccountInformation\(\)
Returns username that task will run under

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetComment

[PyUnicode](#pyunicode) =GetComment\(\)
Return comment string associated with task\.

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetCreator

GetCreator\(\)
Returns creator info, can be any string data

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetErrorRetryCount

GetErrorRetryCount\(\)
Return nbr of times Task scheduler should try to run task \(not currently implemented\)

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetErrorRetryInterval

GetErrorRetryInterval\(\)
Returns nbr of minutes between attempts to run task\. Not implemented according to SDK

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetExitCode



\(int,int\) =GetExitCode\(\)
Returns tuple of task's exit code and error returned to Task Scheduler if process could not start

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetFlags



int =GetFlags\(\)
Returns flags for task \(TASK\_FLAG\_\* constants\)

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetIdleWait



int,int =GetIdleWait\(\)
Gets IdleMinutes and DeadlineMinutes parms for task with trigger of type TASK\_EVENT\_TRIGGER\_ON\_IDLE

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetMostRecentRunTime

[PyTime](#pytime) =GetMostRecentRunTime\(\)
Returns last time task ran

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetNextRunTime

[PyTime](#pytime) =GetNextRunTime\(\)
Returns next time that task is scheduled to run

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetRunTimes



\([PyTime](#pytime),,,\) =GetRunTimes\(Count, Begin, End\)
Return specified number of run times within given time frame

#### Parameters


  - Count : int

    Number of run times to retrieve

  - Begin :[PyTime](#pytime)

    Start time, defaults to current time if not passed or None

  - End :[PyTime](#pytime)

    End time, defaults to unlimited if not passed or None

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetStatus



int =GetStatus\(\)
Returns status \(SCHED\_S\_TASK\.\.\. constants\)

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetTrigger

[PyITaskTrigger](#pyitasktrigger) =GetTrigger\(iTrigger\)
Retrieves ITaskTrigger interface for specified trigger index

#### Parameters


  - iTrigger : int

    Index of trigger to retrieve

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetTriggerCount



int =GetTriggerCount\(\)
Returns number of triggers defined for the task

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetTriggerString

[PyUNICODE](#pyunicode) =GetTriggerString\(\)
Creates a human-readable summary of specified trigger

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.GetWorkItemData



string =GetWorkItemData\(\)
Retrieve data associated with task

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.Run

Run\(\)
Starts task

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetAccountInformation

SetAccountInformation\(AccountName, Password\)
Set username and password under which task will run

#### Parameters


  - AccountName :unicode

    AccountName, use "" for local system account \(can only be used by Administrators\)

  - Password :unicode

    Password - Can be None for local System account, or if TASK\_FLAG\_RUN\_ONLY\_IF\_LOGGED\_ON is set

#### Comments


On some systems, username and password are verified at the time the task is saved, on others when the task tries to run

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetComment

SetComment\(Comment\)
Set comment string for task

#### Parameters


  - Comment :unicode

    Freeform comment string

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetCreator

SetCreator\(Creator\)
Specify who \(or what\) created task, can be any string

#### Parameters


  - Creator :unicode

    Originator of task, does not have to be valid username

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetErrorRetryCount

SetErrorRetryCount\(wRetryCount\)
Specify nbr of times to attempt to run task if it can't start \(not currently implemented\)

#### Parameters


  - wRetryCount : int

    Nbr of attemps to start task

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetErrorRetryInterval

SetErrorRetryInterval\(RetryInterval\)
Interval in minutes between attempts to run task\. Not implemented according to SDK

#### Parameters


  - RetryInterval : int

    Interval in minutes

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetFlags

SetFlags\(dwFlags\)
Set flags for task

#### Parameters


  - dwFlags : int

    Combination of TASK\_FLAG\_\* constants

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetIdleWait

SetIdleWait\(wIdleMinutes, wDeadlineMinutes\)
Sets idle parms for task with trigger of type TASK\_EVENT\_TRIGGER\_ON\_IDLE

#### Parameters


  - wIdleMinutes : int

    Nbr of minutes computer must be idle before task fires

  - wDeadlineMinutes : int

    Maximum nbr of minutes task will wait for computer to become idle

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.SetWorkItemData

SetWorkItemData\(Data\)
Set data associated with task \(treated as uninterpreted bytes\)

#### Parameters


  - Data : string

    Character data, treated as uninterpreted bytes

## [PyIScheduledWorkItem](#pyischeduledworkitem)\.Terminate

Terminate\(\)
Terminate process if task is running