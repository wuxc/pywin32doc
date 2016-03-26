# win32pdh

## Module win32pdh



A module, encapsulating the Windows Performance Data Helpers API

#### Methods


  - [AddCounter](win32pdh.md#win32pdhaddcounter)

    Adds a new counter&nbsp;

  - [AddEnglishCounter](win32pdh.md#win32pdhaddenglishcounter)

    Adds a counter to a query by its English name&nbsp;

  - [RemoveCounter](win32pdh.md#win32pdhremovecounter)

    Removes an open counter\.&nbsp;

  - [EnumObjectItems](win32pdh.md#win32pdhenumobjectitems)

    Enumerates an object's items&nbsp;

  - [EnumObjects](win32pdh.md#win32pdhenumobjects)

    Enumerates objects&nbsp;

  - [OpenQuery](win32pdh.md#win32pdhopenquery)

    Opens a new query&nbsp;

  - [CloseQuery](win32pdh.md#win32pdhclosequery)

    Closes an open query\.&nbsp;

  - [MakeCounterPath](win32pdh.md#win32pdhmakecounterpath)

    Makes a fully resolved counter path&nbsp;

  - [GetCounterInfo](win32pdh.md#win32pdhgetcounterinfo)

    Retrieves information about a counter, such as data size, counter type, path, and user-supplied data values\.&nbsp;

  - [GetFormattedCounterValue](win32pdh.md#win32pdhgetformattedcountervalue)

    Retrieves a formatted counter value&nbsp;

  - [CollectQueryData](win32pdh.md#win32pdhcollectquerydata)

    Collects the current raw data value for all counters in the specified query and updates the status code of each counter\.&nbsp;

  - [ValidatePath](win32pdh.md#win32pdhvalidatepath)

    Validates that the specified counter is present on the machine specified in the counter path\.&nbsp;

  - [ExpandCounterPath](win32pdh.md#win32pdhexpandcounterpath)

    Examines the specified machine \(or local machine if none is specified\) for counters and instances of counters that match the wild card strings in the counter path\.&nbsp;

  - [ParseCounterPath](win32pdh.md#win32pdhparsecounterpath)

    Parses the elements of the counter path\.&nbsp;

  - [ParseInstanceName](win32pdh.md#win32pdhparseinstancename)

    Parses the elements of the instance name&nbsp;

  - [SetCounterScaleFactor](win32pdh.md#win32pdhsetcounterscalefactor)

    Sets the scale factor that is applied to the calculated value of the specified counter when you request the formatted counter value\.&nbsp;

  - [BrowseCounters](win32pdh.md#win32pdhbrowsecounters)

    Displays the counter browsing dialog box so that the user can select the counters to be returned to the caller\.&nbsp;

  - [ConnectMachine](win32pdh.md#win32pdhconnectmachine)

    connects to the specified machine, and creates and initializes a machine entry in the PDH DLL\.&nbsp;

  - [LookupPerfIndexByName](win32pdh.md#win32pdhlookupperfindexbyname)

    Returns the counter index corresponding to the specified counter name\.&nbsp;

  - [LookupPerfNameByIndex](win32pdh.md#win32pdhlookupperfnamebyindex)

    Returns the performance object name corresponding to the specified index\.&nbsp;

## [win32pdh](#win32pdh)\.AddCounter



int =AddCounter\(hQuery, path, userData\)
Adds a new counter

#### Parameters


  - hQuery : int

    Handle to an open query\.

  - path : string

    Full path to the performance data

  - userData=0 : int

    User data associated with the counter\.

#### Comments


See also[win32pdh::RemoveCounter](win32pdh.md#win32pdhremovecounter)

## [win32pdh](#win32pdh)\.AddEnglishCounter



int =AddEnglishCounter\(hQuery, path, userData\)
Adds a counter to a query by its English name

#### Parameters


  - hQuery : int

    Handle to an open query\.

  - path : string

    Full counter path with standard English names\.

  - userData=0 : int

    User data associated with the counter\.

#### Comments


Available on Vista and later


See also[win32pdh::RemoveCounter](win32pdh.md#win32pdhremovecounter)

#### Return Value
Returns a handle to the counter

## [win32pdh](#win32pdh)\.BrowseCounters



string =BrowseCounters\(Flags, hWndOwner, CallBack, DefaultDetailLevel, DialogBoxCaption, InitialPath, DataSource, ReturnMultiple, CallBackArg\)
Displays the counter browsing dialog box so that the user can select the counters to be returned to the caller\.

#### Parameters


  - Flags : \(boolean, \.\.\.\)

    Sequence of boolean flags, or None\. All default to False\. 

\(bIncludeInstanceIndex, bSingleCounterPerAdd, bSingleCounterPerDialog, bLocalCountersOnly, bWildCardInstances, 

bHideDetailBox, bInitializePath, bDisableMachineSelection, bIncludeCostlyObjects, bShowObjectBrowser\)

  - hWndOwner :[PyHANDLE](#pyhandle)

    Parent for the dialog\.

  - CallBack : object

    A callable object to function as the callback\.

  - DefaultDetailLevel : int

    The default detail level to show on startup in the Detail Level combo box\. If the Detail Level combo box is not shown, this is the detail level to use in filtering the displayed performance counters and objects\.

  - DialogBoxCaption=None : string

    The dialog caption, or None for default\.

  - InitialPath=None : str

    Counter to be selected initially, or None for default

  - DataSource=None : str

    Name of a performance log file, or None for live counters

  - ReturnMultiple=False : boolean

    Return all selected counter paths as a sequence of strings\. 

Previously, this function only returned a single path even when multiple counters were selected\.

  - CallBackArg=None : object

    Extra argument to be passed to callback function\.  For backward compatibility, 

the callback will only receive a single argument if this is not given\.

## [win32pdh](#win32pdh)\.CloseQuery

CloseQuery\(handle\)
Closes a query

#### Parameters


  - handle : int

    Handle to an open query\.

#### Comments


See also[win32pdh::OpenQuery](win32pdh.md#win32pdhopenquery)

## [win32pdh](#win32pdh)\.CollectQueryData

CollectQueryData\(hQuery\)
Collects the current raw data value for all counters in the specified query and updates the status code of each counter\.

#### Parameters


  - hQuery : int

    Handle to an open query\.

## [win32pdh](#win32pdh)\.ConnectMachine



string =ConnectMachine\(machineName\)
connects to the specified machine, and creates and initializes a machine entry in the PDH DLL\.

#### Parameters


  - machineName : string

    The machine name\.

## [win32pdh](#win32pdh)\.EnumObjectItems



tuple =EnumObjectItems\(DataSource, machine, object, detailLevel, flags\)
Enumerates an object's items

#### Parameters


  - DataSource : string

    Path of a performance log file, or None for machine counters

  - machine : string

    The machine to use, or None

  - object : string

    The type of object

  - detailLevel : int

    The level of data required, win32pdh\.PERF\_DETAIL\_\*

  - flags=0 : int

    Flags - must be zero

## [win32pdh](#win32pdh)\.EnumObjects



list =EnumObjects\(DataSource, machine, detailLevel, refresh\)
Enumerates objects

#### Parameters


  - DataSource : string

    Path to a performance log file, or None for machine counters

  - machine : string

    The machine to use, or None

  - detailLevel : int

    The level of data required\.

  - refresh=1 : int

    Should the list be refreshed\.

## [win32pdh](#win32pdh)\.ExpandCounterPath



\[string,\] =ExpandCounterPath\(wildCardPath\)
Examines the specified machine \(or local machine if none is specified\) for counters and instances of counters that match the wild card strings in the counter path\.

#### Parameters


  - wildCardPath : string

    The counter path to expand\.

#### Comments


The counter path format is assumed to be:
\\\\machine\\\\object\(parent/instance\#index\)\\\\countername
and the parent, instance, index, and countername elements 

may contain either a valid name or a wild card character\.


The API function leaks memory on Windows XP\.

## [win32pdh](#win32pdh)\.GetCounterInfo

GetCounterInfo\(handle, bRetrieveExplainText\)
Retrieves information about a counter, such as data size, counter type, path, and user-supplied data values\.

#### Parameters


  - handle : int

    The handle of the item to query

  - bRetrieveExplainText : int

    Should explain text be retrieved?

## [win32pdh](#win32pdh)\.GetFormattedCounterValue



\(int,object\) =GetFormattedCounterValue\(handle, format\)
Retrieves a formatted counter value

#### Parameters


  - handle : int

    Handle to the counter

  - format : int

    Format of result\.  Can be PDH\_FMT\_DOUBLE, PDH\_FMT\_LARGE, PDH\_FMT\_LONG and or'd with PDH\_FMT\_NOSCALE, PDH\_FMT\_1000

## [win32pdh](#win32pdh)\.LookupPerfIndexByName



int =LookupPerfIndexByName\(machineName, instanceName\)
Returns the counter index corresponding to the specified counter name\.

#### Parameters


  - machineName : string

    The name of the machine where the specified counter is located\. The machine name can be specified by the DNS name or the IP address\.

  - instanceName : string

    The full name of the counter\.

## [win32pdh](#win32pdh)\.LookupPerfNameByIndex



string =LookupPerfNameByIndex\(machineName, index\)
Returns the performance object name corresponding to the specified index\.

#### Parameters


  - machineName : string

    The name of the machine where the specified counter is located\. The machine name can be specified by the DNS name or the IP address\.

  - index : int

    The index of the performance object\.

## [win32pdh](#win32pdh)\.MakeCounterPath

MakeCounterPath\(elements, flags\)
Makes a fully resolved counter path

#### Parameters


  - elements : \(machineName, objectName, instanceName, parentInstance, instanceIndex, counterName\)

    The elements to use to create the path\.

  - flags=0 : int

    PDH\_PATH\_WBEM\_RESULT, PDH\_PATH\_WBEM\_INPUT, or 0

## [win32pdh](#win32pdh)\.OpenQuery



int =OpenQuery\(DataSource, userData\)
Opens a new query

#### Parameters


  - DataSource=None : str

    Name of a performaance log file, or None for live data

  - userData=0 : int

    User data associated with the query\.

#### Comments


See also[win32pdh::CloseQuery](win32pdh.md#win32pdhclosequery)

## [win32pdh](#win32pdh)\.ParseCounterPath



\(machineName, objectName, instanceName, parentInstance, instanceIndex, counterName\) =ParseCounterPath\(path, flags\)
Parses the elements of the counter path\.

#### Parameters


  - path : string

    The counter path to parse\.

  - flags=0 : int

    Reserved - must be zero\.

## [win32pdh](#win32pdh)\.ParseInstanceName



\(name, parent, instance\) =ParseInstanceName\(instanceName\)
Parses the elements of the instance name

#### Parameters


  - instanceName : string

    The instance name to parse\.

## [win32pdh](#win32pdh)\.RemoveCounter

RemoveCounter\(handle\)
Removes a previously opened counter

#### Parameters


  - handle : int

    Handle to an open counter\.

#### Comments


See also[win32pdh::AddCounter](win32pdh.md#win32pdhaddcounter)

## [win32pdh](#win32pdh)\.SetCounterScaleFactor

SetCounterScaleFactor\(hCounter, factor\)
Sets the scale factor that is applied to the calculated value of the specified counter when you request the formatted counter value\.

#### Parameters


  - hCounter : int

    Handle to the counter\.

  - factor : int

    power of ten used to multiply value\.

## [win32pdh](#win32pdh)\.ValidatePath



int =ValidatePath\(path\)
Validates that the specified counter is present on the machine specified in the counter path\.

#### Parameters


  - path : string

    The counter path to validate\.

#### Comments


This method returns an integer result code\.  No exception is 

ever thrown\.  Zero result indicates success\.