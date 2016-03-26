# PyIProvideTaskPage

## PyIProvideTaskPage Object

Description of the interface

#### Methods


  - [GetPage](PyIProvideTaskPage.md#pyiprovidetaskpagegetpage)

    Return a property sheet page handle for the spedified type (TASKPAGE_TASK,TASKPAGE_SCHEDULE,TASKPAGE_SETTINGS)&nbsp;

## [PyIProvideTaskPage](#pyiprovidetaskpage).GetPage

 __GetPage( *tpType*  *, PersistChanges* __ )
Return a property sheet page handle for the spedified type (TASKPAGE_TASK,TASKPAGE_SCHEDULE,TASKPAGE_SETTINGS)

#### Parameters


  -  *tpType* : int

    Type of page to retreive (TASKPAGE_TASK,TASKPAGE_SCHEDULE,TASKPAGE_SETTINGS)

  -  *PersistChanges* : bool

    Indicates if changes should be saved automatically

#### Comments
There's not yet anything useful that can be done with this handle - return type subject to change