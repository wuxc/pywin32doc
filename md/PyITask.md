# PyITask


## PyITask Object

Python object that encapsulates the ITask interface, inherits all the methods of PyIScheduledWorkItem

#### Methods

  - [SetApplicationName](PyITask.md#pyitasksetapplicationname)

    Specify which program the task will run&nbsp;

  - [GetApplicationName](PyITask.md#pyitaskgetapplicationname)

    Retrieve name of program that task will run&nbsp;

  - [SetParameters](PyITask.md#pyitasksetparameters)

    Sets command line parameters&nbsp;

  - [GetParameters](PyITask.md#pyitaskgetparameters)

    Returns command line parameters for task&nbsp;

  - [SetWorkingDirectory](PyITask.md#pyitasksetworkingdirectory)

    Sets initial working directory for task&nbsp;

  - [GetWorkingDirectory](PyITask.md#pyitaskgetworkingdirectory)

    Return working directory that the task will start out in&nbsp;

  - [SetPriority](PyITask.md#pyitasksetpriority)

    Sets priority for task&nbsp;

  - [GetPriority](PyITask.md#pyitaskgetpriority)

    Gets priority that will be assigned to process when task starts&nbsp;

  - [SetTaskFlags](PyITask.md#pyitasksettaskflags)

    Sets flag for task&nbsp;

  - [GetTaskFlags](PyITask.md#pyitaskgettaskflags)

    Retrieve task flags \(None currently defined\)&nbsp;

  - [SetMaxRunTime](PyITask.md#pyitasksetmaxruntime)

    Sets maximun run time for task, use -1 to disable&nbsp;

  - [GetMaxRunTime](PyITask.md#pyitaskgetmaxruntime)

    Returns maximun run time for task&nbsp;




## [PyITask](PyITask.md#pyitask)\.GetApplicationName

[PyUNICODE](PyUNICODE.md) = GetApplicationName\(\)
Retrieve name of program that task will run


## [PyITask](PyITask.md#pyitask)\.GetMaxRunTime

int = GetMaxRunTime\(\)
Returns maximun run time for task


## [PyITask](PyITask.md#pyitask)\.GetParameters

[PyUNICODE](PyUNICODE.md) = GetParameters\(\)
Returns command line parameters for task


## [PyITask](PyITask.md#pyitask)\.GetPriority

int = GetPriority\(\)
Gets priority that will be assigned to process when task starts


## [PyITask](PyITask.md#pyitask)\.GetTaskFlags

int = GetTaskFlags\(\)
Retrieve task flags \(None currently defined\)


## [PyITask](PyITask.md#pyitask)\.GetWorkingDirectory

[PyUNICODE](PyUNICODE.md) = GetWorkingDirectory\(\)
Return working directory that the task will start out in


## [PyITask](PyITask.md#pyitask)\.SetApplicationName

SetApplicationName\(ApplicationName\)
Specify which program the task will run

#### Parameters

  - ApplicationName : unicode

    Program to execute


## [PyITask](PyITask.md#pyitask)\.SetMaxRunTime

SetMaxRunTime\(MaxRunTimeMS\)
Sets maximun run time for task, use -1 to disable

#### Parameters

  - MaxRunTimeMS : int

    Specified in milliseconds \(use -1 to disable, not 0\)


## [PyITask](PyITask.md#pyitask)\.SetParameters

SetParameters\(Parameters\)
Sets command line parameters

#### Parameters

  - Parameters : unicode

    String containing command line parameters


## [PyITask](PyITask.md#pyitask)\.SetPriority

SetPriority\(Priority\)
Sets priority for task

#### Parameters

  - Priority : int

    One of REALTIME\_PRIORITY\_CLASS, HIGH\_PRIORITY\_CLASS, NORMAL\_PRIORITY\_CLASS, IDLE\_PRIORITY\_CLASS


## [PyITask](PyITask.md#pyitask)\.SetTaskFlags

SetTaskFlags\(dwFlags\)
Sets flag for task\.

#### Parameters

  - dwFlags : int

    None currently defined


## [PyITask](PyITask.md#pyitask)\.SetWorkingDirectory

SetWorkingDirectory\(WorkingDirectory\)
Sets initial working directory for task

#### Parameters

  - WorkingDirectory : unicode

    Initial working directory