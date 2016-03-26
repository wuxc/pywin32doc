# timer

## Module timer

Extension that wraps Win32 Timer functions

#### Methods


  - [set\_timer](timer.md#timerset_timer)

    Creates a timer that executes a callback function&nbsp;

  - [kill\_timer](timer.md#timerkill_timer)

    Stops a timer&nbsp;

## [timer](#timer)\.kill\_timer

boolean \= **kill\_timer\( *IDEvent* ** \)
Creates a timer that executes a callback function

#### Parameters


  -  *IDEvent* : int

    Timer id as returned by[timer::set\_timer](timer.md#timerset_timer)

#### Comments
Uses the KillTimer API function\.

## [timer](#timer)\.set\_timer

int \= **set\_timer\( *Elapse*  *, TimerFunc* ** \)
Creates a timer that executes a callback function

#### Parameters


  -  *Elapse* : int

    Timer period, in milliseconds

  -  *TimerFunc* : function

    Callback function\.  Will be called with with 2 int args: \(timer\_id, time\)

#### Comments
Uses the SetTimer function\.

#### Return Value
Returns the id of the timer, which can be passed to kill\_timer to stop it\.