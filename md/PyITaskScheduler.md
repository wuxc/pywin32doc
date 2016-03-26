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


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.Activate

[PyITask](PyITask.md) = Activate\(Name, riid

\)
Opens the specified task and returns an ITask interface for it

#### Parameters

  - Name : unicode

    Name of task to retreive

  - riid=IID\_ITask : [PyIID](PyIID.md)

    IID to return, currently only IID\_ITask accepted


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.AddWorkItem

AddWorkItem\(TaskName, WorkItem\)
Create a new scheduled task from PyITask object

#### Parameters

  - TaskName : unicode

    Name of task to be created

  - WorkItem : [PyITask](PyITask.md)

    Existing PyITask object

#### Comments

The PyItask passed in is modified in place and on success is associated with the new task, not the old one


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.Delete

Delete\(TaskName\)
Delete task by name

#### Parameters

  - TaskName : unicode

    Name of task to delete


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.Enum

[PyUnicode](PyUnicode.md),\.\.\. = Enum\(\)
Retrieve list of task names


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.GetTargetComputer

unicode

 = GetTargetComputer\(\)
Returns name of computer that the Task Scheduler is connected to


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.IsOfType

IsOfType\(Name, riid\)
Check if named object supports specified interface

#### Parameters

  - Name : unicode

    Name of object

  - riid : [PyIID](PyIID.md)

    Named object is checked that it supports the interface of this IID


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.NewWorkItem

[PyITask](PyITask.md) = NewWorkItem\(TaskName, rclsid

, riid

\)
Creates a new task

#### Parameters

  - TaskName : unicode

    Name of new task

  - rclsid=CLSID\_CTask : [PyIID](PyIID.md)

    Class id of work item, currently only CLSID\_CTask \(defaults if not passed in\)

  - riid=IID\_ITask : [PyIID](PyIID.md)

    Interface IID to return, currently only IID\_ITask \(defaults if not passed in\)


## [PyITaskScheduler](PyITaskScheduler.md#pyitaskscheduler)\.SetTargetComputer

SetTargetComputer\(Computer\)
Connect to another machine to manage its tasks

#### Parameters

  - Computer : unicode

    Name of system to connect to

#### Comments

Leading backslashes are required\.  Call will succeed without them, but no other methods will work\.