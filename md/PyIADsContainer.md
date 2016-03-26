# PyIADsContainer

## PyIADsContainer Object

A COM interface to ADSI's IADsContainer interface.
Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [GetObject](PyIADsContainer.md#pyiadscontainergetobject)

    &nbsp;

  - [get_Count](PyIADsContainer.md#pyiadscontainerget_count)

    &nbsp;

  - [get_Filter](PyIADsContainer.md#pyiadscontainerget_filter)

    &nbsp;

  - [put_Filter](PyIADsContainer.md#pyiadscontainerput_filter)

    &nbsp;

  - [get_Hints](PyIADsContainer.md#pyiadscontainerget_hints)

    &nbsp;

  - [put_Hints](PyIADsContainer.md#pyiadscontainerput_hints)

    &nbsp;

## [PyIADsContainer](#pyiadscontainer).GetObject

[PyIDispatch](#pyidispatch)= __GetObject( *class*  *, relativeName* __ )


#### Parameters


  -  *class* : string

    Specifies the name of the object class as known in the underlying directory and identical to the one retrieved through the get_Class property method. If the class name is None, the provider returns the first item found in the container.

  -  *relativeName* : string

    Specifies the name of the object as known in the underlying directory and identical to the one retrieved through the get_Name property method.

## [PyIADsContainer](#pyiadscontainer).get_Count

int = __get_Count(__ )


## [PyIADsContainer](#pyiadscontainer).get_Filter

object = __get_Filter(__ )


## [PyIADsContainer](#pyiadscontainer).get_Hints

object = __get_Hints(__ )


## [PyIADsContainer](#pyiadscontainer).put_Filter

 __put_Filter( *val* __ )


#### Parameters


  -  *val* : object

    

## [PyIADsContainer](#pyiadscontainer).put_Hints

 __put_Hints( *val* __ )


#### Parameters


  -  *val* : object

    