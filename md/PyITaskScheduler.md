# PyITaskScheduler

## PyITaskScheduler Object

Interface to the Windows Task Scheduler

#### Methods


  - [SetTargetComputer](PyITaskScheduler.md#pyitaskschedulersettargetcomputer)

    Connect to another machine to manage its tasks&nbsp;

  - [GetTargetComputer](PyITaskScheduler.md#pyitaskschedulergettargetcomputer)

    Returns name of computer that the Task Scheduler is connected to&nbsp;

  - [Enum](PyITaskScheduler.md#pyitaskschedulerenum)

    Retrieve list of task names&nbsp;

  - [Activate](PyITaskScheduler.md#pyitaskscheduleractivate)

    Opens the specified task and returns an ITask interface for it&nbsp;

  - [Delete](PyITaskScheduler.md#pyitaskschedulerdelete)

    Delete task by name&nbsp;

  - [NewWorkItem](PyITaskScheduler.md#pyitaskschedulernewworkitem)

    Creates a new task&nbsp;

  - [AddWorkItem](PyITaskScheduler.md#pyitaskscheduleraddworkitem)

    Create a new scheduled task from PyITask object&nbsp;

  - [IsOfType](PyITaskScheduler.md#pyitaskschedulerisoftype)

    Check if named task supports specified interface&nbsp;

## [PyITaskScheduler](#pyitaskscheduler).Activate

[PyITask](#pyitask)= __Activate( *Name*  *, riid* __ )
Opens the specified task and returns an ITask interface for it

#### Parameters


  -  *Name* : __unicode__ 

    Name of task to retreive

  -  *riid=IID_ITask* :[PyIID](#pyiid)

    IID to return, currently only IID_ITask accepted

## [PyITaskScheduler](#pyitaskscheduler).AddWorkItem

 __AddWorkItem( *TaskName*  *, WorkItem* __ )
Create a new scheduled task from PyITask object

#### Parameters


  -  *TaskName* : __unicode__ 

    Name of task to be created

  -  *WorkItem* :[PyITask](#pyitask)

    Existing PyITask object

#### Comments
The PyItask passed in is modified in place and on success is associated with the new task, not the old one

## [PyITaskScheduler](#pyitaskscheduler).Delete

 __Delete( *TaskName* __ )
Delete task by name

#### Parameters


  -  *TaskName* : __unicode__ 

    Name of task to delete

## [PyITaskScheduler](#pyitaskscheduler).Enum

[PyUnicode](#pyunicode),... = __Enum(__ )
Retrieve list of task names

## [PyITaskScheduler](#pyitaskscheduler).GetTargetComputer

 __unicode__ = __GetTargetComputer(__ )
Returns name of computer that the Task Scheduler is connected to

## [PyITaskScheduler](#pyitaskscheduler).IsOfType

 __IsOfType( *Name*  *, riid* __ )
Check if named object supports specified interface

#### Parameters


  -  *Name* : __unicode__ 

    Name of object

  -  *riid* :[PyIID](#pyiid)

    Named object is checked that it supports the interface of this IID

## [PyITaskScheduler](#pyitaskscheduler).NewWorkItem

[PyITask](#pyitask)= __NewWorkItem( *TaskName*  *, rclsid*  *, riid* __ )
Creates a new task

#### Parameters


  -  *TaskName* : __unicode__ 

    Name of new task

  -  *rclsid=CLSID_CTask* :[PyIID](#pyiid)

    Class id of work item, currently only CLSID_CTask (defaults if not passed in)

  -  *riid=IID_ITask* :[PyIID](#pyiid)

    Interface IID to return, currently only IID_ITask (defaults if not passed in)

## [PyITaskScheduler](#pyitaskscheduler).SetTargetComputer

 __SetTargetComputer( *Computer* __ )
Connect to another machine to manage its tasks

#### Parameters


  -  *Computer* : __unicode__ 

    Name of system to connect to

#### Comments
Leading backslashes are required.  Call will succeed without them, but no other methods will work.