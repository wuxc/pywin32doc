# servicemanager

## Module servicemanager



A module that interfaces with the Windows Service Control Manager\.  While this 

module can be imported by regular Python programs, it is only useful when used by a Python program 

hosting a service - and even then is generally used automatically by the Python Service framework\. 

See the pipeTestService sample for an example of using this module\.
The module[win32service](#win32service) andwin32serviceutil

 provide other facilities for controlling 

and managing services\.

#### Methods


  - [CoInitializeEx](servicemanager.md#servicemanagercoinitializeex)

    &nbsp;

  - [CoUninitialize](servicemanager.md#servicemanagercouninitialize)

    &nbsp;

  - [RegisterServiceCtrlHandler](servicemanager.md#servicemanagerregisterservicectrlhandler)

    Registers a function to retrieve service control notification messages\.&nbsp;

  - [LogMsg](servicemanager.md#servicemanagerlogmsg)

    Write an specific message to the log\.&nbsp;

  - [LogInfoMsg](servicemanager.md#servicemanagerloginfomsg)

    Write an informational message to the log\.&nbsp;

  - [LogErrorMsg](servicemanager.md#servicemanagerlogerrormsg)

    Write an error message to the log\.&nbsp;

  - [LogWarningMsg](servicemanager.md#servicemanagerlogwarningmsg)

    Logs a generic warning message to the event log&nbsp;

  - [PumpWaitingMessages](servicemanager.md#servicemanagerpumpwaitingmessages)

    Pumps waiting window messages for the service\.&nbsp;

  - [Debugging](servicemanager.md#servicemanagerdebugging)

    Indicates if the service is running in debug mode\.&nbsp;

  - [StartServiceCtrlDispatcher](servicemanager.md#servicemanagerstartservicectrldispatcher)

    Starts the service by calling the win32 StartServiceCtrlDispatcher function\.&nbsp;

  - [Initialize](servicemanager.md#servicemanagerinitialize)

    &nbsp;

  - [Finalize](servicemanager.md#servicemanagerfinalize)

    &nbsp;

  - [PrepareToHostSingle](servicemanager.md#servicemanagerpreparetohostsingle)

    &nbsp;

  - [PrepareToHostMultiple](servicemanager.md#servicemanagerpreparetohostmultiple)

    &nbsp;

  - [RunningAsService](servicemanager.md#servicemanagerrunningasservice)

    Indicates if the code is running as a service\.&nbsp;

  - [SetEventSourceName](servicemanager.md#servicemanagerseteventsourcename)

    Sets the event source name for event log entries written by the service\.&nbsp;

## [servicemanager](#servicemanager)\.CoInitializeEx

CoInitializeEx\(\)
Initialize OLE with additional options\.

## [servicemanager](#servicemanager)\.CoUninitialize

CoUninitialize\(\)
Unitialize OLE

## [servicemanager](#servicemanager)\.Debugging



True/False =Debugging\(newVal\)
Indicates if the service is running in debug mode 

and optionally toggles the debug flag\.

#### Parameters


  - newVal=-1 : int

    If not -1, a new value for the debugging flag\. 

The result is the value of the flag before it is changed\.

## [servicemanager](#servicemanager)\.Finalize

Finalize\(\)


## [servicemanager](#servicemanager)\.Initialize

Initialize\(eventSourceName, eventSourceFile\)
Initialize the module for hosting a service\.  This is generally called automatically

#### Parameters


  - eventSourceName=None :[PyUnicode](#pyunicode)

    The event source name

  - eventSourceFile=None :[PyUnicode](#pyunicode)

    The name of the file 

\(generally a DLL\) with the event source messages\.

## [servicemanager](#servicemanager)\.LogErrorMsg

LogErrorMsg\(msg\)
Logs a generic error message to the event log

#### Parameters


  - msg :[PyUnicode](#pyunicode)

    The message to write\.

## [servicemanager](#servicemanager)\.LogInfoMsg

LogInfoMsg\(msg\)
Logs a generic informational message to the event log

#### Parameters


  - msg :[PyUnicode](#pyunicode)

    The message to write\.

## [servicemanager](#servicemanager)\.LogMsg

LogMsg\(errorType, eventId, inserts\)
Logs a specific message

#### Parameters


  - errorType : int

    

  - eventId : int

    

  - inserts=None : \(string, \)

    

## [servicemanager](#servicemanager)\.LogWarningMsg

LogWarningMsg\(msg\)
Logs a generic warning message to the event log

#### Parameters


  - msg :[PyUnicode](#pyunicode)

    The message to write\.

## [servicemanager](#servicemanager)\.PrepareToHostMultiple

PrepareToHostMultiple\(service\_name, klass\)
Prepare for hosting a multiple services in this EXE

#### Parameters


  - service\_name : string/unicode

    The name of the service hosted by the class

  - klass : object

    The Python class to host\.

## [servicemanager](#servicemanager)\.PrepareToHostSingle

PrepareToHostSingle\(klass\)
Prepare for hosting a single service in this EXE

#### Parameters


  - klass=None : object

    The Python class to host\.  If not specified, the 

service name is looked up in the registry and the specified class instantiated\.

## [servicemanager](#servicemanager)\.PumpWaitingMessages



int =PumpWaitingMessages\(\)
Pumps all waiting messages\.

#### Return Value
Returns 1 if a WM\_QUIT message was received, else 0

## [servicemanager](#servicemanager)\.RegisterServiceCtrlHandler



int/None =RegisterServiceCtrlHandler\(serviceName, callback, extra\_args\)
Registers the Python service control handler function\.

#### Parameters


  - serviceName :[PyUnicode](#pyunicode)

    The name of the service\.  This is provided in args\[0\] of the service class \_\_init\_\_ method\.

  - callback : object

    The Python function that performs as the control function\.  This will be called with an integer status argument\.

  - extra\_args=False : bool

    Is this callback expecting the additional 2 args passed by HandlerEx?

#### Return Value
If the service manager is in debug mode, this returns None, indicating 

there is no service control manager handle, otherwise the handle to the Win32 service manager\.

## [servicemanager](#servicemanager)\.RunningAsService



True/False =RunningAsService\(\)
Indicates if the code is 

being executed as a service\.

## [servicemanager](#servicemanager)\.SetEventSourceName

SetEventSourceName\(sourceName, registerNow\)
Sets the event source name 

for event log entries written by the service\.

#### Parameters


  - sourceName : string

    The event source name

  - registerNow=False : bool

    If True, the event source name in the 

registry will be updated immediately\. 

If False, the name will be registered the first time an event log entry 

is written via any pythonservice methods \(or possibly never if no record 

if written\)\.
Note that in some cases, the service itself will not have permission 

to write the event source in the registry\.  Therefore, it would be 

prudent for your installation program to call this function with 

registerNow=True, to ensure your services can write useful entries\.