# PyIADs

## PyIADs Object

An object representing the IADs interface. 

In most cases you can achieve the same result via IDispatch - however, this 

interface allows you get get and set properties without the IDispatch 

overhead.

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

  -  __[PyUnicode](#pyunicode)ADsPath__ 
    

  -  __[PyUnicode](#pyunicode)AdsPath__ 
    Synonym for ADsPath

  -  __[PyUnicode](#pyunicode)Class__ 
    

  -  __[PyUnicode](#pyunicode)GUID__ 
    Like the IADs method, this returns a string rather than a GUID object.

  -  __[PyUnicode](#pyunicode)Name__ 
    

  -  __[PyUnicode](#pyunicode)Parent__ 
    

  -  __[PyUnicode](#pyunicode)Schema__ 
    

## [PyIADs](#pyiads).Get

object = __Get( *prop* __ )
Description of Get.

#### Parameters


  -  *prop* :[PyUnicode](#pyunicode)

    The name of the property to fetch

#### Return Value
The result is a Python object converted from a COM variant.  It 

may be an array, or any types supported by COM variant.

## [PyIADs](#pyiads).GetInfo

 __GetInfo(__ )
Description of GetInfo.

## [PyIADs](#pyiads).Put

 __Put( *property*  *, val* __ )
Description of Put.

#### Parameters


  -  *property* :[PyUnicode](#pyunicode)

    The property name to set

  -  *val* : object

    The value to set.

## [PyIADs](#pyiads).SetInfo

 __SetInfo(__ )
Description of SetInfo.