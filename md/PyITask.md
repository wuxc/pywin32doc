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

    Retrieve task flags (None currently defined)&nbsp;

  - [SetMaxRunTime](PyITask.md#pyitasksetmaxruntime)

    Sets maximun run time for task, use -1 to disable&nbsp;

  - [GetMaxRunTime](PyITask.md#pyitaskgetmaxruntime)

    Returns maximun run time for task&nbsp;


## [PyITask](#pyitask).GetApplicationName

[PyUNICODE](#pyunicode)= __GetApplicationName(__ )
Retrieve name of program that task will run

## [PyITask](#pyitask).GetMaxRunTime

int = __GetMaxRunTime(__ )
Returns maximun run time for task

## [PyITask](#pyitask).GetParameters

[PyUNICODE](#pyunicode)= __GetParameters(__ )
Returns command line parameters for task

## [PyITask](#pyitask).GetPriority

int = __GetPriority(__ )
Gets priority that will be assigned to process when task starts

## [PyITask](#pyitask).GetTaskFlags

int = __GetTaskFlags(__ )
Retrieve task flags (None currently defined)

## [PyITask](#pyitask).GetWorkingDirectory

[PyUNICODE](#pyunicode)= __GetWorkingDirectory(__ )
Return working directory that the task will start out in

## [PyITask](#pyitask).SetApplicationName

 __SetApplicationName( *ApplicationName* __ )
Specify which program the task will run

#### Parameters


  -  *ApplicationName* : __unicode__ 

    Program to execute

## [PyITask](#pyitask).SetMaxRunTime

 __SetMaxRunTime( *MaxRunTimeMS* __ )
Sets maximun run time for task, use -1 to disable

#### Parameters


  -  *MaxRunTimeMS* : int

    Specified in milliseconds (use -1 to disable, not 0)

## [PyITask](#pyitask).SetParameters

 __SetParameters( *Parameters* __ )
Sets command line parameters

#### Parameters


  -  *Parameters* : __unicode__ 

    String containing command line parameters

## [PyITask](#pyitask).SetPriority

 __SetPriority( *Priority* __ )
Sets priority for task

#### Parameters


  -  *Priority* : int

    One of REALTIME_PRIORITY_CLASS, HIGH_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, IDLE_PRIORITY_CLASS

## [PyITask](#pyitask).SetTaskFlags

 __SetTaskFlags( *dwFlags* __ )
Sets flag for task.

#### Parameters


  -  *dwFlags* : int

    None currently defined

## [PyITask](#pyitask).SetWorkingDirectory

 __SetWorkingDirectory( *WorkingDirectory* __ )
Sets initial working directory for task

#### Parameters


  -  *WorkingDirectory* : __unicode__ 

    Initial working directory