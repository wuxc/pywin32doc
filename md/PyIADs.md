# PyIADs


## PyIADs Object

An object representing the IADs interface\. 

In most cases you can achieve the same result via IDispatch - however, this 

interface allows you get get and set properties without the IDispatch 

overhead\.

#### Methods

  - [GetInfo](PyIADs.md#pyiadsgetinfo)

    Description of GetInfo&nbsp;

  - [SetInfo](PyIADs.md#pyiadssetinfo)

    Description of SetInfo&nbsp;

  - [Get](PyIADs.md#pyiadsget)

    Description of Get&nbsp;

  - [Put](PyIADs.md#pyiadsput)

    Description of Put&nbsp;

  - [get](PyIADs.md#pyiadsget)

    Synonym for Get&nbsp;

  - [put](PyIADs.md#pyiadsput)

    Synonym for Put&nbsp;

#### Properties

  - [PyUnicode](PyUnicode.md) ADsPath

    

  - [PyUnicode](PyUnicode.md) AdsPath

    Synonym for ADsPath

  - [PyUnicode](PyUnicode.md) Class

    

  - [PyUnicode](PyUnicode.md) GUID

    Like the IADs method, this returns a string rather than a GUID object\.

  - [PyUnicode](PyUnicode.md) Name

    

  - [PyUnicode](PyUnicode.md) Parent

    

  - [PyUnicode](PyUnicode.md) Schema

    


## [PyIADs](PyIADs.md#pyiads)\.Get

object = Get\(prop\)
Description of Get\.

#### Parameters

  - prop : [PyUnicode](PyUnicode.md)

    The name of the property to fetch

#### Return Value
The result is a Python object converted from a COM variant\.  It 

may be an array, or any types supported by COM variant\.


## [PyIADs](PyIADs.md#pyiads)\.GetInfo

GetInfo\(\)
Description of GetInfo\.


## [PyIADs](PyIADs.md#pyiads)\.Put

Put\(property, val\)
Description of Put\.

#### Parameters

  - property : [PyUnicode](PyUnicode.md)

    The property name to set

  - val : object

    The value to set\.


## [PyIADs](PyIADs.md#pyiads)\.SetInfo

SetInfo\(\)
Description of SetInfo\.