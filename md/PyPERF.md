# PyPERF

## PyPERF_COUNTER_DEFINITION Object

An object encapsulating a Windows NT Performance Monitor counter definition (PERF_COUNTER_DEFINITION).

#### Comments
Note that all the counter "set" functions will silently do nothing 

if the counter does not appear in a block.  This is so the application can avoid 

excessive tests for lack of performance monitor functionality. 

However, the method[PyPERF_COUNTER_DEFINITION::Get](PyPERF.md#pyperfcounter_definition_get)will raise a ValueError exception in this case.

#### Methods


  - [Increment](PyPERF.md#pyperfcounter_definition_increment)

    Increments the value of the performance counter&nbsp;

  - [Decrement](PyPERF.md#pyperfcounter_definition_decrement)

    Decrements the value of the performance counter&nbsp;

  - [Set](PyPERF.md#pyperfcounter_definition_set)

    Sets the counter to a specific value&nbsp;

  - [Get](PyPERF.md#pyperfcounter_definition_get)

    Gets the current value of the counter&nbsp;

#### Properties

  -  __integer DefaultScale__ 
    The default scale of the counter.

  -  __integer DetailLevel__ 
    The detail level of the counter.

  -  __integer CounterType__ 
    The counter type.

  -  __integer CounterNameTitleIndex__ 
    

  -  __integer CounterHelpTitleIndex__ 
    Sentinel

## [PyPERF_COUNTER_DEFINITION](PyPERF.md#pyperfcounter_definition).Decrement

 __Decrement(__ )
Decrements the value of the performance counter

## [PyPERF_COUNTER_DEFINITION](PyPERF.md#pyperfcounter_definition).Get

 __Get(__ )
Gets the current value of the counter

## [PyPERF_COUNTER_DEFINITION](PyPERF.md#pyperfcounter_definition).Increment

 __Increment(__ )
Increments the value of the performance counter

## [PyPERF_COUNTER_DEFINITION](PyPERF.md#pyperfcounter_definition).Set

 __Set(__ )
Sets the counter to a specific value

## PyPERF_OBJECT_TYPE Object

A Python object, representing a PERF_OBJECT_TYPE structure

#### Methods


  - [Close](PyPERF.md#pyperfobject_type_close)

    Closes all counters.&nbsp;

#### Properties

  -  __integer ObjectNameTitleIndex__ 
    

  -  __integer ObjectHelpTitleIndex__ 
    

  -  __integer DefaultCounterIndex__ 
    

## [PyPERF_OBJECT_TYPE](PyPERF.md#pyperfobject_type).Close

 __Close(__ )
Closes the object.