# PyIProvideTaskPage


## PyIProvideTaskPage Object

Description of the interface

#### Methods

  - [GetPage](PyIProvideTaskPage.md#pyiprovidetaskpagegetpage)

    Return a property sheet page handle for the spedified type \(TASKPAGE\_TASK,TASKPAGE\_SCHEDULE,TASKPAGE\_SETTINGS\)&nbsp;


## [PyIProvideTaskPage](PyIProvideTaskPage.md#pyiprovidetaskpage)\.GetPage

GetPage\(tpType, PersistChanges\)
Return a property sheet page handle for the spedified type \(TASKPAGE\_TASK,TASKPAGE\_SCHEDULE,TASKPAGE\_SETTINGS\)

#### Parameters

  - tpType : int

    Type of page to retreive \(TASKPAGE\_TASK,TASKPAGE\_SCHEDULE,TASKPAGE\_SETTINGS\)

  - PersistChanges : bool

    Indicates if changes should be saved automatically

#### Comments

There's not yet anything useful that can be done with this handle - return type subject to change