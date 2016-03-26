# PyPERF


## PyPERF\_COUNTER\_DEFINITION Object

An object encapsulating a Windows NT Performance Monitor counter definition \(PERF\_COUNTER\_DEFINITION\)\.

#### Comments

Note that all the counter "set" functions will silently do nothing 

if the counter does not appear in a block\.  This is so the application can avoid 

excessive tests for lack of performance monitor functionality\. 

However, the method [PyPERF\_COUNTER\_DEFINITION::Get](PyPERF.md#pyperfcounter_definition_get) will raise a ValueError exception in this case\.

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

  - integer DefaultScale

    The default scale of the counter\.

  - integer DetailLevel

    The detail level of the counter\.

  - integer CounterType

    The counter type\.

  - integer CounterNameTitleIndex

    

  - integer CounterHelpTitleIndex

    Sentinel


## [PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition)\.Decrement

Decrement\(\)
Decrements the value of the performance counter


## [PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition)\.Get

Get\(\)
Gets the current value of the counter


## [PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition)\.Increment

Increment\(\)
Increments the value of the performance counter


## [PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition)\.Set

Set\(\)
Sets the counter to a specific value


## PyPERF\_OBJECT\_TYPE Object

A Python object, representing a PERF\_OBJECT\_TYPE structure

#### Methods

  - [Close](PyPERF.md#pyperfobject_type_close)

    Closes all counters\.&nbsp;

#### Properties

  - integer ObjectNameTitleIndex

    

  - integer ObjectHelpTitleIndex

    

  - integer DefaultCounterIndex

    


## [PyPERF\_OBJECT\_TYPE](PyPERF.md#pyperfobject_type)\.Close

Close\(\)
Closes the object\.