# PyIADsContainer


## PyIADsContainer Object

A COM interface to ADSI's IADsContainer interface\. 

Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [GetObject](PyIADsContainer.md#pyiadscontainergetobject)

    &nbsp;

  - [get\_Count](PyIADsContainer.md#pyiadscontainerget_count)

    &nbsp;

  - [get\_Filter](PyIADsContainer.md#pyiadscontainerget_filter)

    &nbsp;

  - [put\_Filter](PyIADsContainer.md#pyiadscontainerput_filter)

    &nbsp;

  - [get\_Hints](PyIADsContainer.md#pyiadscontainerget_hints)

    &nbsp;

  - [put\_Hints](PyIADsContainer.md#pyiadscontainerput_hints)

    &nbsp;


## [PyIADsContainer](PyIADsContainer.md#pyiadscontainer)\.GetObject

[PyIDispatch](PyIDispatch.md) = GetObject\(class, relativeName

\)

#### Parameters

  - class : string

    Specifies the name of the object class as known in the underlying directory and identical to the one retrieved through the get\_Class property method\. If the class name is None, the provider returns the first item found in the container\.

  - relativeName : string

    Specifies the name of the object as known in the underlying directory and identical to the one retrieved through the get\_Name property method\.


## [PyIADsContainer](PyIADsContainer.md#pyiadscontainer)\.get\_Count

int = get\_Count\(\)



## [PyIADsContainer](PyIADsContainer.md#pyiadscontainer)\.get\_Filter

object = get\_Filter\(\)



## [PyIADsContainer](PyIADsContainer.md#pyiadscontainer)\.get\_Hints

object = get\_Hints\(\)



## [PyIADsContainer](PyIADsContainer.md#pyiadscontainer)\.put\_Filter

put\_Filter\(val\)

#### Parameters

  - val : object

    


## [PyIADsContainer](PyIADsContainer.md#pyiadscontainer)\.put\_Hints

put\_Hints\(val\)

#### Parameters

  - val : object

    