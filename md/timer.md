# timer

## Module timer

Extension that wraps Win32 Timer functions

#### Methods


  - [set_timer](timer.md#timerset_timer)

    Creates a timer that executes a callback function&nbsp;

  - [kill_timer](timer.md#timerkill_timer)

    Stops a timer&nbsp;

## [timer](#timer).kill_timer

boolean = __kill_timer( *IDEvent* __ )
Creates a timer that executes a callback function

#### Parameters


  -  *IDEvent* : int

    Timer id as returned by[timer::set_timer](timer.md#timerset_timer)

#### Comments
Uses the KillTimer API function.

## [timer](#timer).set_timer

int = __set_timer( *Elapse*  *, TimerFunc* __ )
Creates a timer that executes a callback function

#### Parameters


  -  *Elapse* : int

    Timer period, in milliseconds

  -  *TimerFunc* : function

    Callback function.  Will be called with with 2 int args: (timer_id, time)

#### Comments
Uses the SetTimer function.

#### Return Value
Returns the id of the timer, which can be passed to kill_timer to stop it.