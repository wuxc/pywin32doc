# win32print

## Module win32print

A module encapsulating the Windows printing API.

#### Methods


  - [OpenPrinter](win32print.md#win32printopenprinter)

    Retrieves a handle to a printer.&nbsp;

  - [GetPrinter](win32print.md#win32printgetprinter)

    Retrieves information about a printer&nbsp;

  - [SetPrinter](win32print.md#win32printsetprinter)

    Changes printer configuration and status&nbsp;

  - [ClosePrinter](win32print.md#win32printcloseprinter)

    Closes a handle to a printer.&nbsp;

  - [AddPrinterConnection](win32print.md#win32printaddprinterconnection)

    Connects to a network printer.&nbsp;

  - [DeletePrinterConnection](win32print.md#win32printdeleteprinterconnection)

    Disconnects from a network printer.&nbsp;

  - [EnumPrinters](win32print.md#win32printenumprinters)

    Enumerates printers, print servers, domains and print providers.&nbsp;

  - [GetDefaultPrinter](win32print.md#win32printgetdefaultprinter)

    Returns the default printer.&nbsp;

  - [GetDefaultPrinterW](win32print.md#win32printgetdefaultprinterw)

    Returns the default printer.&nbsp;

  - [SetDefaultPrinter](win32print.md#win32printsetdefaultprinter)

    Sets the default printer.&nbsp;

  - [SetDefaultPrinterW](win32print.md#win32printsetdefaultprinterw)

    Sets the default printer.&nbsp;

  - [StartDocPrinter](win32print.md#win32printstartdocprinter)

    Notifies the print spooler that a document is to be spooled for printing. Returns the Jobid of the started job.&nbsp;

  - [EndDocPrinter](win32print.md#win32printenddocprinter)

    The EndDocPrinter function ends a print job for the specified printer.&nbsp;

  - [AbortPrinter](win32print.md#win32printabortprinter)

    Deletes spool file for printer&nbsp;

  - [StartPagePrinter](win32print.md#win32printstartpageprinter)

    Notifies the print spooler that a page is to be printed on specified printer&nbsp;

  - [EndPagePrinter](win32print.md#win32printendpageprinter)

    Ends a page in a print job&nbsp;

  - [StartDoc](win32print.md#win32printstartdoc)

    Starts spooling a print job on a printer device context&nbsp;

  - [EndDoc](win32print.md#win32printenddoc)

    Stops spooling a print job on a printer device context&nbsp;

  - [AbortDoc](win32print.md#win32printabortdoc)

    Cancels print job on a printer device context&nbsp;

  - [StartPage](win32print.md#win32printstartpage)

    Starts a page on a printer device context&nbsp;

  - [EndPage](win32print.md#win32printendpage)

    Ends a page on a printer device context&nbsp;

  - [WritePrinter](win32print.md#win32printwriteprinter)

    Copies the specified bytes to the specified printer. StartDocPrinter and EndDocPrinter should be called before and after. Returns number of bytes written to printer.&nbsp;

  - [EnumJobs](win32print.md#win32printenumjobs)

    Enumerates print jobs on specified printer.&nbsp;

  - [GetJob](win32print.md#win32printgetjob)

    Returns dictionary of information about a specified print job.&nbsp;

  - [SetJob](win32print.md#win32printsetjob)

    Pause, cancel, resume, set priority levels on a print job.&nbsp;

  - [DocumentProperties](win32print.md#win32printdocumentproperties)

    Changes printer configuration&nbsp;

  - [EnumPrintProcessors](win32print.md#win32printenumprintprocessors)

    List printer providers for specified server and environment&nbsp;

  - [EnumPrintProcessorDatatypes](win32print.md#win32printenumprintprocessordatatypes)

    Lists data types that specified print provider supports&nbsp;

  - [EnumPrinterDrivers](win32print.md#win32printenumprinterdrivers)

    Lists installed printer drivers&nbsp;

  - [EnumForms](win32print.md#win32printenumforms)

    Lists forms for a printer&nbsp;

  - [AddForm](win32print.md#win32printaddform)

    Adds a form for a printer&nbsp;

  - [DeleteForm](win32print.md#win32printdeleteform)

    Deletes a form defined for a printer&nbsp;

  - [GetForm](win32print.md#win32printgetform)

    Retrieves information about a defined form&nbsp;

  - [SetForm](win32print.md#win32printsetform)

    Change information for a form&nbsp;

  - [AddJob](win32print.md#win32printaddjob)

    Adds a job to be spooled to a printer queue&nbsp;

  - [ScheduleJob](win32print.md#win32printschedulejob)

    Schedules a spooled job to be printed&nbsp;

  - [DeviceCapabilities](win32print.md#win32printdevicecapabilities)

    Queries a printer for its capabilities&nbsp;

  - [GetDeviceCaps](win32print.md#win32printgetdevicecaps)

    Retrieves device-specific parameters and settings&nbsp;

  - [EnumMonitors](win32print.md#win32printenummonitors)

    Lists installed printer port monitors&nbsp;

  - [EnumPorts](win32print.md#win32printenumports)

    Lists printer ports on a server&nbsp;

  - [GetPrintProcessorDirectory](win32print.md#win32printgetprintprocessordirectory)

    Returns the directory where print processor files reside&nbsp;

  - [GetPrinterDriverDirectory](win32print.md#win32printgetprinterdriverdirectory)

    Returns the directory where printer drivers are installed&nbsp;

  - [AddPrinter](win32print.md#win32printaddprinter)

    Adds a new printer on a server&nbsp;

  - [DeletePrinter](win32print.md#win32printdeleteprinter)

    Deletes an existing printer&nbsp;

  - [DeletePrinterDriver](win32print.md#win32printdeleteprinterdriver)

    Deletes the specified driver from a server&nbsp;

  - [DeletePrinterDriverEx](win32print.md#win32printdeleteprinterdriverex)

    Deletes a printer driver and associated files&nbsp;

  - [FlushPrinter](win32print.md#win32printflushprinter)

    Clears printer from error state if WritePrinter fails&nbsp;

## [win32print](#win32print).AbortDoc

 __AbortDoc( *hdc* __ )
Cancels a print job

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Printer device context handle as returned by[win32gui::CreateDC](win32gui.md#win32guicreatedc)

## [win32print](#win32print).AbortPrinter

 __AbortPrinter( *hPrinter* __ )
Deletes spool file for a printer

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle to printer as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

## [win32print](#win32print).AddForm

 __AddForm( *hprinter*  *, Form* __ )
Adds a form for a printer

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *Form* : dict

    [FORM_INFO_1](FORM.md#forminfo_1)dictionary

#### Return Value
Returns None on success, throws an exception otherwise

## [win32print](#win32print).AddJob

 __AddJob( *hprinter* __ )
Add a job to be spooled to a printer queue

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

#### Return Value
Returns the file name to which data should be written and the job id of the new job

## [win32print](#win32print).AddPrinter

[PyPrinterHANDLE](#pyprinterhandle)= __AddPrinter( *Name*  *, Level*  *, pPrinter* __ )
Installs a printer on a server

#### Parameters


  -  *Name* : string

    Name of server on which to install printer, None indicates local machine

  -  *Level* : int

    Level of data contained in pPrinter, only level 2 currently supported

  -  *pPrinter* : dict

    PRINTER_INFO_2 dict as returned by[win32print::GetPrinter](win32print.md#win32printgetprinter)

#### Comments
pPrinterName, pPortName, pDriverName, and pPrintProcessor are required

#### Return Value
Returns a handle to the new printer

## [win32print](#win32print).AddPrinterConnection

None = __AddPrinterConnection( *printer* __ )
Connects to remote printer

#### Parameters


  -  *printer* : string

    printer to connect to (eg: \\server\\printer).

## [win32print](#win32print).ClosePrinter

 __ClosePrinter( *hPrinter* __ )
Closes a handle to a printer.

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    handle to printer object

## [win32print](#win32print).DeleteForm

 __DeleteForm( *hprinter*  *, FormName* __ )
Deletes a form defined for a printer

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *FormName* :[PyUnicode](#pyunicode)

    Name of form to be deleted

#### Return Value
Returns None on success, throws an exception otherwise

## [win32print](#win32print).DeletePrinter

 __DeletePrinter( *hPrinter* __ )
Deletes an existing printer

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle to printer as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)or[win32print::AddPrinter](win32print.md#win32printaddprinter)

#### Comments
Printer handle must be opened for PRINTER_ACCESS_ADMINISTER 

If there are any pending print jobs for the printer, actual deletion does not happen until they are done

## [win32print](#win32print).DeletePrinterConnection

None = __DeletePrinterConnection( *printer* __ )
Removes connection to remote printer

#### Parameters


  -  *printer* : string

    printer to disconnect from (eg: \\server\\printer).

## [win32print](#win32print).DeletePrinterDriver

 __DeletePrinterDriver( *Server*  *, Environment*  *, DriverName* __ )
Removes the specified printer driver from a server

#### Parameters


  -  *Server* : string/[PyUnicode](#pyunicode)

    Name of print server, use None for local machine

  -  *Environment* : string/[PyUnicode](#pyunicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

  -  *DriverName* : string/[PyUnicode](#pyunicode)

    Name of driver to remove

#### Comments
Does not delete associated driver files - use[win32print::DeletePrinterDriverEx](win32print.md#win32printdeleteprinterdriverex)if this is required

## [win32print](#win32print).DeletePrinterDriverEx

 __DeletePrinterDriverEx( *Server*  *, Environment*  *, DriverName*  *, DeleteFlag*  *, VersionFlag* __ )
Deletes a printer driver and its associated files

#### Parameters


  -  *Server* : string/[PyUnicode](#pyunicode)

    Name of print server, use None for local machine

  -  *Environment* : string/[PyUnicode](#pyunicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

  -  *DriverName* : string/[PyUnicode](#pyunicode)

    Name of driver to remove

  -  *DeleteFlag* : int

    Combination of DPD_DELETE_SPECIFIC_VERSION, DPD_DELETE_UNUSED_FILES, and DPD_DELETE_ALL_FILES

  -  *VersionFlag* : int

    Can be 0,1,2, or 3.  Only used if DPD_DELETE_SPECIFIC_VERSION is specified in DeleteFlag

## [win32print](#win32print).DeviceCapabilities

 __DeviceCapabilities( *Device*  *, Port*  *, Capability*  *, DEVMODE* __ )
Queries a printer for its capabilities

#### Parameters


  -  *Device* : string

    Name of printer

  -  *Port* : string

    Port that printer is using

  -  *Capability* : int

    Type of capability to return - DC_* constant

  -  *DEVMODE=None* :[PyDEVMODE](#pydevmode)

    If present, function returns values from it, otherwise the printer defaults are used


## [win32print](#win32print).DocumentProperties

int = __DocumentProperties( *HWnd*  *, hPrinter*  *, DeviceName*  *, DevModeOutput*  *, DevModeInput*  *, Mode* __ )
Changes printer configuration for a printer

#### Parameters


  -  *HWnd* :[PyHANDLE](#pyhandle)

    Parent window handle to use if DM_IN_PROMPT is specified to display printer dialog

  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *DeviceName* : string

    Name of printer

  -  *DevModeOutput* :[PyDEVMODE](#pydevmode)

    PyDEVMODE object that receives modified info, can be None if DM_OUT_BUFFER not specified

  -  *DevModeInput* :[PyDEVMODE](#pydevmode)

    PyDEVMODE that specifies initial configuration, can be None if DM_IN_BUFFER not specified

  -  *Mode* : int

    A combination of DM_IN_BUFFER, DM_OUT_BUFFER, and DM_IN_PROMPT - pass 0 to retrieve driver data size

#### Return Value
If DM_IN_PROMPT is specified, returned value will be IDOK or IDCANCEL

## [win32print](#win32print).EndDoc

 __EndDoc( *hdc* __ )
Stops spooling a print job on a printer device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Printer device context handle as returned by[win32gui::CreateDC](win32gui.md#win32guicreatedc)

## [win32print](#win32print).EndDocPrinter

None = __EndDocPrinter( *hPrinter* __ )
The EndDocPrinter function ends a print job for the specified printer. To be used after using WritePrinter.

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    handle to printer (from[win32print::OpenPrinter](win32print.md#win32printopenprinter))

## [win32print](#win32print).EndPage

 __EndPage( *hdc* __ )
Ends a page on a printer device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Printer device context handle as returned by[win32gui::CreateDC](win32gui.md#win32guicreatedc)

## [win32print](#win32print).EndPagePrinter

 __EndPagePrinter( *hprinter* __ )
Ends a page in a print job

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

## [win32print](#win32print).EnumForms

([FORM_INFO_1](FORM.md#forminfo_1),...) = __EnumForms( *hprinter* __ )
Lists forms for a printer

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

#### Return Value
Returns a sequence of dictionaries representing FORM_INFO_1 structures

## [win32print](#win32print).EnumJobs

tuple = __EnumJobs( *hPrinter*  *, FirstJob*  *, NoJobs*  *, Level* __ )
Enumerates print jobs on specified printer.

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle of printer.

  -  *FirstJob* : int

    location of first job in print queue to enumerate.

  -  *NoJobs* : int

    Number of jobs to enumerate.

  -  *Level=1* : int

    Level of information to return (JOB_INFO_1, JOB_INFO_2, JOB_INFO_3 supported).

#### Return Value
Returns a sequence of dictionaries representing JOB_INFO_* structures, depending on level

## [win32print](#win32print).EnumMonitors

(dict,...) = __EnumMonitors( *Name*  *, Level* __ )
Lists installed printer port monitors

#### Parameters


  -  *Name* : str/[PyUnicode](#pyunicode)

    Name of server, use None for local machine

  -  *Level* : int

    Level of information to return, 1 and 2 supported

#### Return Value
Returns a sequence of dicts representing MONITOR_INFO_* structures depending on level

## [win32print](#win32print).EnumPorts

(dict,...) = __EnumPorts( *Name*  *, Level* __ )
Lists printer port on a server

#### Parameters


  -  *Name* : str/[PyUnicode](#pyunicode)

    Name of server, use None for local machine

  -  *Level* : int

    Level of information to return, 1 and 2 supported

#### Return Value
Returns a sequence of dicts representing PORT_INFO_* structures depending on level

## [win32print](#win32print).EnumPrintProcessorDatatypes

([PyUnicode](#pyunicode),...) = __EnumPrintProcessorDatatypes( *ServerName*  *, PrintProcessorName* __ )
List data types that specified print provider recognizes

#### Parameters


  -  *ServerName* : string/[PyUnicode](#pyunicode)

    Name of print server, use None for local machine

  -  *PrintProcessorName* : string/[PyUnicode](#pyunicode)

    Name of print processor

## [win32print](#win32print).EnumPrintProcessors

([PyUnicode](#pyunicode),...) = __EnumPrintProcessors( *Server*  *, Environment* __ )
List printer processors for specified server and environment

#### Parameters


  -  *Server=None* : string/[PyUnicode](#pyunicode)

    Name of print server, use None for local machine

  -  *Environment=None* : string/[PyUnicode](#pyunicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

## [win32print](#win32print).EnumPrinterDrivers

(dict,...) = __EnumPrinterDrivers( *Server*  *, Environment*  *, Level* __ )
Lists installed printer drivers

#### Parameters


  -  *Server=None* : string/unicode

    Name of print server, use None for local machine

  -  *Environment=None* : string/unicode

    Environment - eg 'Windows NT x86' - use None for current client environment

  -  *Level=1* : int

    Level of information to return, 1-6 (not all levels are supported on all platforms)

#### Comments
On Win2k and up, 'all' can be passed for environment

#### Return Value
Returns a sequence of dictionaries representing DRIVER_INFO_* structures

## [win32print](#win32print).EnumPrinters

tuple = __EnumPrinters( *flags*  *, name*  *, level* __ )
Enumerates printers, print servers, domains and print providers.

#### Parameters


  -  *flags* : int

    types of printer objects to enumerate (combination of PRINTER_ENUM_* constants).

  -  *name=None* : string

    name of printer object.

  -  *level=1* : int

    type of printer info structure (Levels 1,2,4,5 supported)

#### Comments
Use Flags=PRINTER_ENUM_NAME, Name=None, Level=1 to enumerate print providers.
Use Flags=PRINTER_ENUM_NAME, Name=\\servername, Level=2 or 5 to list printers on another server.
See MSDN docs for EnumPrinters for other specific combinations

#### Return Value
Level 1 returns a tuple of tuples for backward compatibility. 

Each individual element is a tuple of (flags, description, name, comment)
All other levels return a tuple of dictionaries representing PRINTER_INFO_* structures

## [win32print](#win32print).FlushPrinter

int = __FlushPrinter( *Printer*  *, Buf*  *, Sleep* __ )
Clears printer from error state if WritePrinter fails

#### Parameters


  -  *Printer* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle to a printer

  -  *Buf* : str

    Data to be sent to printer

  -  *Sleep* : int

    Number of milliseconds to suspend printer

#### Return Value
Returns the number of bytes actually written to the printer

## [win32print](#win32print).GetDefaultPrinter

string = __GetDefaultPrinter(__ )
Returns the default printer.

## [win32print](#win32print).GetDefaultPrinterW

[PyUnicode](#pyunicode)= __GetDefaultPrinterW(__ )
Returns the default printer.

#### Comments
Unlike[win32print::GetDefaultPrinter](win32print.md#win32printgetdefaultprinter), this method calls the GetDefaultPrinter API function.

## [win32print](#win32print).GetDeviceCaps

int = __GetDeviceCaps( *hdc*  *, Index* __ )
Retrieves device-specific parameters and settings

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a printer or display device context

  -  *Index* : int

    The capability to return.  See MSDN for valid values.

#### Comments
Can also be used for Display DCs in addition to printer DCs

#### Win32 API References


  - Search for *GetDeviceCaps* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getdevicecaps),[google](#http://www.google.com/search?q=getdevicecaps)or[google groups](#http://groups.google.com/groups?q=getdevicecaps).

## [win32print](#win32print).GetForm

 __GetForm( *hprinter*  *, FormName* __ )
Retrieves information about a form defined for a printer

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *FormName* :[PyUnicode](#pyunicode)

    Name of form for which to retrieve info

#### Return Value
Returns a[FORM_INFO_1](FORM.md#forminfo_1)dict

## [win32print](#win32print).GetJob

dictionary = __GetJob( *hPrinter*  *, JobID*  *, Level* __ )
Returns dictionary of information about a specified print job.

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle to a printer as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter).

  -  *JobID* : int

    Job Identifier.

  -  *Level=1* : int

    Level of information to return (JOB_INFO_1, JOB_INFO_2, JOB_INFO_3 supported).

#### Return Value
Returns a dict representing a JOB_INFO_* struct, depending on level

## [win32print](#win32print).GetPrintProcessorDirectory

[PyUnicode](#pyunicode)= __GetPrintProcessorDirectory( *Name*  *, Environment* __ )
Returns the directory where print processor files reside

#### Parameters


  -  *Name* : str/[PyUnicode](#pyunicode)

    Name of server, use None for local machine

  -  *Environment* : str/[PyUnicode](#pyunicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

## [win32print](#win32print).GetPrinter

dict = __GetPrinter( *hPrinter*  *, Level* __ )
Retrieves information about a printer

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    handle to printer object as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *Level=2* : int

    Level of data returned (1,2,3,4,5,7,8,9)

#### Comments
Original implementation used level 2 only and returned a tuple 

Pass single arg as indicator to use old behaviour for backward compatibility

#### Return Value
Returns a dictionary containing PRINTER_INFO_* data for level, or 

returns a tuple of PRINTER_INFO_2 data if no level is passed in.

## [win32print](#win32print).GetPrinterDriverDirectory

[PyUnicode](#pyunicode)= __GetPrinterDriverDirectory( *Name*  *, Environment* __ )
Returns the directory where printer drivers are installed

#### Parameters


  -  *Name* : str/[PyUnicode](#pyunicode)

    Name of server, use None for local machine

  -  *Environment* : str/[PyUnicode](#pyunicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

## [win32print](#win32print).OpenPrinter

[PyPrinterHANDLE](#pyprinterhandle)= __OpenPrinter( *printer*  *, Defaults* __ )
Retrieves a handle to a printer.

#### Parameters


  -  *printer* : string

    Printer or print server name.  Use None to open local print server.

  -  *Defaults=None* : dict

    [PRINTER_DEFAULTS](PRINTER.md#printerdefaults)dict, or None

## [win32print](#win32print).ScheduleJob

 __ScheduleJob( *hprinter*  *, JobId* __ )
Schedules a spooled job to be printed

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *JobId* : int

    Job Id as returned by[win32print::AddJob](win32print.md#win32printaddjob)

## [win32print](#win32print).SetDefaultPrinter

None = __SetDefaultPrinter( *printer* __ )
Sets the default printer.

#### Parameters


  -  *printer* : string

    printer to set as default

#### Comments
This function uses the pre-win2k method of WriteProfileString rather than the SetDefaultPrinter API function

## [win32print](#win32print).SetDefaultPrinterW

None = __SetDefaultPrinterW( *Printer* __ )
Sets the default printer

#### Parameters


  -  *Printer* :[PyUnicode](#pyunicode)

    Name of printer, can be None to use first available printer

#### Comments
Unlike[win32print::SetDefaultPrinter](win32print.md#win32printsetdefaultprinter), this method calls the SetDefaultPrinter API function.

## [win32print](#win32print).SetForm

 __SetForm( *hprinter*  *, FormName*  *, Form* __ )
Change information for a form

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *FormName* :[PyUnicode](#pyunicode)

    Name of form

  -  *Form* : dict

    [FORM_INFO_1](FORM.md#forminfo_1)dictionary

#### Return Value
Returns None on success

## [win32print](#win32print).SetJob

None = __SetJob( *hPrinter*  *, JobID*  *, Level*  *, JobInfo*  *, Command* __ )
Pause, cancel, resume, set priority levels on a print job.

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle of printer.

  -  *JobID* : int

    Job Identifier.

  -  *Level* : int

    Level of information in JobInfo dict (0, 1, 2, and 3 are supported).

  -  *JobInfo* : dict

    JOB_INFO_* Dictionary as returned by[win32print::GetJob](win32print.md#win32printgetjob)or[win32print::EnumJobs](win32print.md#win32printenumjobs)(can be None if Level is 0).

  -  *Command* : int

    Job command value (JOB_CONTROL_*).

#### Comments
If printer is not opened with at least PRINTER_ACCESS_ADMINISTER access, 'Position' member of 

JOB_INFO_1 and JOB_INFO_2 must be set to JOB_POSITION_UNSPECIFIED

## [win32print](#win32print).SetPrinter

 __SetPrinter( *hPrinter*  *, Level*  *, pPrinter*  *, Command* __ )
Change printer configuration and status

#### Parameters


  -  *hPrinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

  -  *Level* : int

    Level of data contained in pPrinter

  -  *pPrinter* : dict

    PRINTER_INFO_* dict as returned by[win32print::GetPrinter](win32print.md#win32printgetprinter), can be None if level is 0

  -  *Command* : int

    Command to send to printer - one of the PRINTER_CONTROL_* constants, or 0

#### Comments
If Level is 0 and Command is PRINTER_CONTROL_SET_STATUS, pPrinter should be an integer, 

and is interpreted as the new printer status to set (one of the PRINTER_STATUS_* constants).

## [win32print](#win32print).StartDoc

int = __StartDoc( *hdc*  *, docinfo* __ )
Starts spooling a print job on a printer device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Printer device context handle as returned by[win32gui::CreateDC](win32gui.md#win32guicreatedc)

  -  *docinfo* : tuple

    [DOCINFO](#docinfo)tuple specifying print job parameters

#### Return Value
On success, returns the job id of the print job

## [win32print](#win32print).StartDocPrinter

int = __StartDocPrinter( *hprinter*  *, level*  *, tuple* __ )
Notifies the print spooler that a document is to be spooled for printing. To be used before using WritePrinter. Returns the Jobid of the started job.

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    handle to printer (from[win32print::OpenPrinter](win32print.md#win32printopenprinter))

  -  *level=1* : int

    type of docinfo structure (only docinfo level 1 supported)

  -  *tuple* : data

    A tuple corresponding to the level parameter.

#### Comments
For level 1, the tuple is:

#### Items


  - [0] *string* : docName

    Specifies the name of the document.

  - [1] *string* : outputFile

    Specifies the name of an output file. To print to a printer, set this to None.

  - [2] *string* : dataType

    Identifies the type of data used to record the document, such 

as "raw" or "emf", used to record the print job. This member can be None. If it is not None, 

the StartDoc function passes it to the printer driver. Note that the printer driver might 

ignore the requested data type.

## [win32print](#win32print).StartPage

 __StartPage( *hdc* __ )
Starts a page on a printer device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Printer device context handle as returned by[win32gui::CreateDC](win32gui.md#win32guicreatedc)

## [win32print](#win32print).StartPagePrinter

 __StartPagePrinter( *hprinter* __ )
Notifies the print spooler that a page is to be printed on specified printer

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Printer handle as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter)

## [win32print](#win32print).WritePrinter

int = __WritePrinter( *hprinter*  *, buf* __ )
Copies the specified bytes to the specified printer. 

Suitable for copying raw Postscript or HPGL files to a printer. 

StartDocPrinter and EndDocPrinter should be called before and after.

#### Parameters


  -  *hprinter* :[PyPrinterHANDLE](#pyprinterhandle)

    Handle to printer as returned by[win32print::OpenPrinter](win32print.md#win32printopenprinter).

  -  *buf* : string

    String or buffer containing data to send to printer. Embedded NULL bytes are allowed.

#### Return Value
Returns number of bytes written to printer.