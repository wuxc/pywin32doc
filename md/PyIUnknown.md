# PyIUnknown

## PyIUnknown Object



The base object for all PythonCOM objects\.  Wraps a COM IUnknown object\.

#### Methods


  - [QueryInterface](PyIUnknown.md#pyiunknownqueryinterface)

    Queries the object for an interface\.&nbsp;

#### Comments


Note that there are no reference counting functions that are typically exposed via COM\. 

This is because COM reference counts are automatically handled by PythonCOM - each interface 

object keeps exactly one COM reference, regardless of how many Python references\.  When the 

Python object destructs due to its reference count hitting zero, the COM reference is then 

released\.  It is not possible for force the closure of a PythonCOM object - the only 

way to ensure cleanup is to remove all Python references\.

## [PyIUnknown](#pyiunknown)\.QueryInterface

[PyIUnknown](#pyiunknown) =QueryInterface\(iid, useIID\)
Queries an object for a specific interface\.

#### Parameters


  - iid : IID

    The IID requested\.

  - useIID=None : IID

    If provided and not None, will return an 

interface for the specified IID if \(and only if\) a native interface can not be supported\. 

If the interface specified by iid is natively supported, this option is ignored\.

#### Comments


The useIID parameter is a very dangerous option, and should only 

be used when you are sure you need it\! 

By specifying this parameter, you are telling the COM framework that regardless 

of the true type of the result \(as specified by iid\), a Python wrapper 

of type useIID will be created\.  If iid does not derive from useIID, 

then it is almost certain that using the object will cause an Access Violation\.
For example, this option can be used to obtain a PyIUnknown object if 

pythoncom does not natively support the interface\. 

Another example might be to return an unsupported persistence interface as a 

PyIPersist instance\.
 

For backwards compatibility: the integer 0 implies None, and the 

integer 1 implies IID\_IUnknown\.

#### Return Value
The result is always an object derived from PyIUnknown\. 

Any error \(including E\_NOINTERFACE\) will generate a[com\_error](com.md#comerror) exception\.

## [PyIUnknown](#pyiunknown)\.\_\_cmp\_\_



int =\_\_cmp\_\_\(\)
Implements COM rules for object identity\.

#### Comments


As per the COM rules for object identity, both objects are queried for IUnknown, and these values compared\. 

The only meaningful test is for equality - the result of other comparisons is undefined 

\(ie, determined by the object's relative addresses in memory\.

## PyIUnknown::\_\_repr\_\_ method
string \_\_repr\_\_\(\)


Called to create a representation of a PyIUnknown object


Defined in: O:/SRC/PYWIN32/COM/WIN32COM/SRC/PYIUNKNOWN\.CPP

#### Comments


The repr of this object displays both the object's address, and its attached IUnknown's address