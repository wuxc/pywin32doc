# PyIErrorLog

## PyIErrorLog Object



A Python wrapper for a COM IErrorLog interface\.

#### Comments


The IErrorLog interface is an abstraction for an error log that is used to 

communicate detailed error information between a client and an object\. 

The caller of the single interface method,[PyIErrorLog::AddError](PyIErrorLog.md#pyierrorlogadderror), simply logs an error 

where the error is an EXCEPINFO structure related to a specific property\. 

The implementer of the interface is responsible for handling the error in whatever way it desires\.
IErrorLog is used in the protocol between a client that implements[PyIPropertyBag](#pyipropertybag) and an 

object that implements[PyIPersistPropertyBag](#pyipersistpropertybag)\.

#### Methods


  - [AddError](PyIErrorLog.md#pyierrorlogadderror)

    Adds an error to the error log\.&nbsp;


## [PyIErrorLog](#pyierrorlog)\.AddError

AddError\(propName, excepInfo\)
Adds an error to the error log\.

#### Parameters


  - propName : string

    The name of the error

  - excepInfo=None : exception

    A COM exception\.  Must be a complete COM exception \(ie, pythoncom\.com\_error, or win32com\.server\.exceptions\.COMException\(\)\)