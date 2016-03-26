# perfmon

## Module perfmon



A module which wraps Performance Monitor functions\.

#### Methods


  - [LoadPerfCounterTextStrings](perfmon.md#perfmonloadperfcountertextstrings)

    &nbsp;

  - [UnloadPerfCounterTextStrings](perfmon.md#perfmonunloadperfcountertextstrings)

    &nbsp;

  - [CounterDefinition](perfmon.md#perfmoncounterdefinition)

    Creates a new[PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition) object&nbsp;

  - [ObjectType](perfmon.md#perfmonobjecttype)

    Creates a new[PyPERF\_OBJECT\_TYPE](PyPERF.md#pyperfobject_type) object&nbsp;

  - [PerfMonManager](perfmon.md#perfmonperfmonmanager)

    Creates a new[PyPerfMonManager](#pyperfmonmanager) objects&gt&nbsp;

## [perfmon](#perfmon)\.CounterDefinition

[PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition) =CounterDefinition\(\)
Creates a new[PyPERF\_COUNTER\_DEFINITION](PyPERF.md#pyperfcounter_definition) object

## [perfmon](#perfmon)\.LoadPerfCounterTextStrings

LoadPerfCounterTextStrings\(\)


## [perfmon](#perfmon)\.ObjectType

[PyPERF\_OBJECT\_TYPE](PyPERF.md#pyperfobject_type) =ObjectType\(\)
Creates a new PERF\_OBJECT\_TYPE object

## [perfmon](#perfmon)\.PerfMonManager

[PyPerfMonManager](#pyperfmonmanager) =PerfMonManager\(serviceName, seqPerfObTypes, mappingName, eventSourceName\)
Creates a new PERF\_OBJECT\_TYPE object

#### Parameters


  - serviceName :[PyUnicode](#pyunicode)

    The name of the service for which data is being provided\.

  - seqPerfObTypes : \[[PyPERF\_OBJECT\_TYPE](PyPERF.md#pyperfobject_type), \.\.\.\]

    A sequence of objects to use in the performance monitor\.  At this stage, len\(seqPerfObTypes\) must == 1\.

  - mappingName=None :[PyUnicode](#pyunicode)

    The name of the mapping to open\.  This must be the same as the DLL name providing the information\.  If None, the serviceName is used\.

  - eventSourceName=None :[PyUnicode](#pyunicode)

    The name used by the DLL for error messages in the registry\.  If None, the serviceName is used\.

#### Comments


The application need not be a service, but it must have an entry in the 

Services section of the registry\.  This limits the performance monitor to being able to 

provide only one 'counter type', but still many counters within that type\. 

See the documentation for the Performance Monitor API for more details\.

## [perfmon](#perfmon)\.UnloadPerfCounterTextStrings

UnloadPerfCounterTextStrings\(\)
