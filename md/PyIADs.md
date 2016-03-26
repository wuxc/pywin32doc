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

  - [PyUnicode](#pyunicode) ADsPath
    

  - [PyUnicode](#pyunicode) AdsPath
    Synonym for ADsPath

  - [PyUnicode](#pyunicode) Class
    

  - [PyUnicode](#pyunicode) GUID
    Like the IADs method, this returns a string rather than a GUID object\.

  - [PyUnicode](#pyunicode) Name
    

  - [PyUnicode](#pyunicode) Parent
    

  - [PyUnicode](#pyunicode) Schema
    

## [PyIADs](#pyiads)\.Get



object =Get\(prop\)
Description of Get\.

#### Parameters


  - prop :[PyUnicode](#pyunicode)

    The name of the property to fetch

#### Return Value
The result is a Python object converted from a COM variant\.  It 

may be an array, or any types supported by COM variant\.

## [PyIADs](#pyiads)\.GetInfo

GetInfo\(\)
Description of GetInfo\.

## [PyIADs](#pyiads)\.Put

Put\(property, val\)
Description of Put\.

#### Parameters


  - property :[PyUnicode](#pyunicode)

    The property name to set

  - val : object

    The value to set\.

## [PyIADs](#pyiads)\.SetInfo

SetInfo\(\)
Description of SetInfo\.