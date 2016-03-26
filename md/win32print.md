
## [win32print](#README.md#win32print).AbortDoc

 **AbortDoc( *hdc* ** )
Cancels a print job

#### Parameters


     *hdc* :[PyHANDLE](#README.md#PyHANDLE)

    Printer device context handle as returned by[win32gui::CreateDC](#win32gui.md#win32guiCreateDC)

## [win32print](#README.md#win32print).AbortPrinter

 **AbortPrinter( *hPrinter* ** )
Deletes spool file for a printer

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle to printer as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

## [win32print](#README.md#win32print).AddForm

 **AddForm( *hprinter*  *, Form* ** )
Adds a form for a printer

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *Form* : dict

    [FORM_INFO_1](#FORM.md#FORMINFO_1)dictionary

#### Return Value
Returns None on success, throws an exception otherwise

## [win32print](#README.md#win32print).AddJob

 **AddJob( *hprinter* ** )
Add a job to be spooled to a printer queue

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

#### Return Value
Returns the file name to which data should be written and the job id of the new job

## [win32print](#README.md#win32print).AddPrinter

[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)= **AddPrinter( *Name*  *, Level*  *, pPrinter* ** )
Installs a printer on a server

#### Parameters


     *Name* : string

    Name of server on which to install printer, None indicates local machine

     *Level* : int

    Level of data contained in pPrinter, only level 2 currently supported

     *pPrinter* : dict

    PRINTER_INFO_2 dict as returned by[win32print::GetPrinter](#win32print.md#win32printGetPrinter)

#### Comments
pPrinterName, pPortName, pDriverName, and pPrintProcessor are required

#### Return Value
Returns a handle to the new printer

## [win32print](#README.md#win32print).AddPrinterConnection

None = **AddPrinterConnection( *printer* ** )
Connects to remote printer

#### Parameters


     *printer* : string

    printer to connect to (eg: \\server\\printer).

## [win32print](#README.md#win32print).ClosePrinter

 **ClosePrinter( *hPrinter* ** )
Closes a handle to a printer.

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    handle to printer object

## [win32print](#README.md#win32print).DeleteForm

 **DeleteForm( *hprinter*  *, FormName* ** )
Deletes a form defined for a printer

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *FormName* :[PyUnicode](#README.md#PyUnicode)

    Name of form to be deleted

#### Return Value
Returns None on success, throws an exception otherwise

## [win32print](#README.md#win32print).DeletePrinter

 **DeletePrinter( *hPrinter* ** )
Deletes an existing printer

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle to printer as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)or[win32print::AddPrinter](#win32print.md#win32printAddPrinter)

#### Comments
Printer handle must be opened for PRINTER_ACCESS_ADMINISTER 

If there are any pending print jobs for the printer, actual deletion does not happen until they are done

## [win32print](#README.md#win32print).DeletePrinterConnection

None = **DeletePrinterConnection( *printer* ** )
Removes connection to remote printer

#### Parameters


     *printer* : string

    printer to disconnect from (eg: \\server\\printer).

## [win32print](#README.md#win32print).DeletePrinterDriver

 **DeletePrinterDriver( *Server*  *, Environment*  *, DriverName* ** )
Removes the specified printer driver from a server

#### Parameters


     *Server* : string/[PyUnicode](#README.md#PyUnicode)

    Name of print server, use None for local machine

     *Environment* : string/[PyUnicode](#README.md#PyUnicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

     *DriverName* : string/[PyUnicode](#README.md#PyUnicode)

    Name of driver to remove

#### Comments
Does not delete associated driver files - use[win32print::DeletePrinterDriverEx](#win32print.md#win32printDeletePrinterDriverEx)if this is required

## [win32print](#README.md#win32print).DeletePrinterDriverEx

 **DeletePrinterDriverEx( *Server*  *, Environment*  *, DriverName*  *, DeleteFlag*  *, VersionFlag* ** )
Deletes a printer driver and its associated files

#### Parameters


     *Server* : string/[PyUnicode](#README.md#PyUnicode)

    Name of print server, use None for local machine

     *Environment* : string/[PyUnicode](#README.md#PyUnicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

     *DriverName* : string/[PyUnicode](#README.md#PyUnicode)

    Name of driver to remove

     *DeleteFlag* : int

    Combination of DPD_DELETE_SPECIFIC_VERSION, DPD_DELETE_UNUSED_FILES, and DPD_DELETE_ALL_FILES

     *VersionFlag* : int

    Can be 0,1,2, or 3.  Only used if DPD_DELETE_SPECIFIC_VERSION is specified in DeleteFlag

## [win32print](#README.md#win32print).DeviceCapabilities

 **DeviceCapabilities( *Device*  *, Port*  *, Capability*  *, DEVMODE* ** )
Queries a printer for its capabilities

#### Parameters


     *Device* : string

    Name of printer

     *Port* : string

    Port that printer is using

     *Capability* : int

    Type of capability to return - DC_* constant

     *DEVMODE=None* :[PyDEVMODE](#README.md#PyDEVMODE)

    If present, function returns values from it, otherwise the printer defaults are used


## [win32print](#README.md#win32print).DocumentProperties

int = **DocumentProperties( *HWnd*  *, hPrinter*  *, DeviceName*  *, DevModeOutput*  *, DevModeInput*  *, Mode* ** )
Changes printer configuration for a printer

#### Parameters


     *HWnd* :[PyHANDLE](#README.md#PyHANDLE)

    Parent window handle to use if DM_IN_PROMPT is specified to display printer dialog

     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *DeviceName* : string

    Name of printer

     *DevModeOutput* :[PyDEVMODE](#README.md#PyDEVMODE)

    PyDEVMODE object that receives modified info, can be None if DM_OUT_BUFFER not specified

     *DevModeInput* :[PyDEVMODE](#README.md#PyDEVMODE)

    PyDEVMODE that specifies initial configuration, can be None if DM_IN_BUFFER not specified

     *Mode* : int

    A combination of DM_IN_BUFFER, DM_OUT_BUFFER, and DM_IN_PROMPT - pass 0 to retrieve driver data size

#### Return Value
If DM_IN_PROMPT is specified, returned value will be IDOK or IDCANCEL

## [win32print](#README.md#win32print).EndDoc

 **EndDoc( *hdc* ** )
Stops spooling a print job on a printer device context

#### Parameters


     *hdc* :[PyHANDLE](#README.md#PyHANDLE)

    Printer device context handle as returned by[win32gui::CreateDC](#win32gui.md#win32guiCreateDC)

## [win32print](#README.md#win32print).EndDocPrinter

None = **EndDocPrinter( *hPrinter* ** )
The EndDocPrinter function ends a print job for the specified printer. To be used after using WritePrinter.

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    handle to printer (from[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter))

## [win32print](#README.md#win32print).EndPage

 **EndPage( *hdc* ** )
Ends a page on a printer device context

#### Parameters


     *hdc* :[PyHANDLE](#README.md#PyHANDLE)

    Printer device context handle as returned by[win32gui::CreateDC](#win32gui.md#win32guiCreateDC)

## [win32print](#README.md#win32print).EndPagePrinter

 **EndPagePrinter( *hprinter* ** )
Ends a page in a print job

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

## [win32print](#README.md#win32print).EnumForms

([FORM_INFO_1](#FORM.md#FORMINFO_1),...) = **EnumForms( *hprinter* ** )
Lists forms for a printer

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

#### Return Value
Returns a sequence of dictionaries representing FORM_INFO_1 structures

## [win32print](#README.md#win32print).EnumJobs

tuple = **EnumJobs( *hPrinter*  *, FirstJob*  *, NoJobs*  *, Level* ** )
Enumerates print jobs on specified printer.

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle of printer.

     *FirstJob* : int

    location of first job in print queue to enumerate.

     *NoJobs* : int

    Number of jobs to enumerate.

     *Level=1* : int

    Level of information to return (JOB_INFO_1, JOB_INFO_2, JOB_INFO_3 supported).

#### Return Value
Returns a sequence of dictionaries representing JOB_INFO_* structures, depending on level

## [win32print](#README.md#win32print).EnumMonitors

(dict,...) = **EnumMonitors( *Name*  *, Level* ** )
Lists installed printer port monitors

#### Parameters


     *Name* : str/[PyUnicode](#README.md#PyUnicode)

    Name of server, use None for local machine

     *Level* : int

    Level of information to return, 1 and 2 supported

#### Return Value
Returns a sequence of dicts representing MONITOR_INFO_* structures depending on level

## [win32print](#README.md#win32print).EnumPorts

(dict,...) = **EnumPorts( *Name*  *, Level* ** )
Lists printer port on a server

#### Parameters


     *Name* : str/[PyUnicode](#README.md#PyUnicode)

    Name of server, use None for local machine

     *Level* : int

    Level of information to return, 1 and 2 supported

#### Return Value
Returns a sequence of dicts representing PORT_INFO_* structures depending on level

## [win32print](#README.md#win32print).EnumPrintProcessorDatatypes

([PyUnicode](#README.md#PyUnicode),...) = **EnumPrintProcessorDatatypes( *ServerName*  *, PrintProcessorName* ** )
List data types that specified print provider recognizes

#### Parameters


     *ServerName* : string/[PyUnicode](#README.md#PyUnicode)

    Name of print server, use None for local machine

     *PrintProcessorName* : string/[PyUnicode](#README.md#PyUnicode)

    Name of print processor

## [win32print](#README.md#win32print).EnumPrintProcessors

([PyUnicode](#README.md#PyUnicode),...) = **EnumPrintProcessors( *Server*  *, Environment* ** )
List printer processors for specified server and environment

#### Parameters


     *Server=None* : string/[PyUnicode](#README.md#PyUnicode)

    Name of print server, use None for local machine

     *Environment=None* : string/[PyUnicode](#README.md#PyUnicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

## [win32print](#README.md#win32print).EnumPrinterDrivers

(dict,...) = **EnumPrinterDrivers( *Server*  *, Environment*  *, Level* ** )
Lists installed printer drivers

#### Parameters


     *Server=None* : string/unicode

    Name of print server, use None for local machine

     *Environment=None* : string/unicode

    Environment - eg 'Windows NT x86' - use None for current client environment

     *Level=1* : int

    Level of information to return, 1-6 (not all levels are supported on all platforms)

#### Comments
On Win2k and up, 'all' can be passed for environment

#### Return Value
Returns a sequence of dictionaries representing DRIVER_INFO_* structures

## [win32print](#README.md#win32print).EnumPrinters

tuple = **EnumPrinters( *flags*  *, name*  *, level* ** )
Enumerates printers, print servers, domains and print providers.

#### Parameters


     *flags* : int

    types of printer objects to enumerate (combination of PRINTER_ENUM_* constants).

     *name=None* : string

    name of printer object.

     *level=1* : int

    type of printer info structure (Levels 1,2,4,5 supported)

#### Comments
Use Flags=PRINTER_ENUM_NAME, Name=None, Level=1 to enumerate print providers.
Use Flags=PRINTER_ENUM_NAME, Name=\\servername, Level=2 or 5 to list printers on another server.
See MSDN docs for EnumPrinters for other specific combinations

#### Return Value
Level 1 returns a tuple of tuples for backward compatibility. 

Each individual element is a tuple of (flags, description, name, comment)
All other levels return a tuple of dictionaries representing PRINTER_INFO_* structures

## [win32print](#README.md#win32print).FlushPrinter

int = **FlushPrinter( *Printer*  *, Buf*  *, Sleep* ** )
Clears printer from error state if WritePrinter fails

#### Parameters


     *Printer* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle to a printer

     *Buf* : str

    Data to be sent to printer

     *Sleep* : int

    Number of milliseconds to suspend printer

#### Return Value
Returns the number of bytes actually written to the printer

## [win32print](#README.md#win32print).GetDefaultPrinter

string = **GetDefaultPrinter(** )
Returns the default printer.

## [win32print](#README.md#win32print).GetDefaultPrinterW

[PyUnicode](#README.md#PyUnicode)= **GetDefaultPrinterW(** )
Returns the default printer.

#### Comments
Unlike[win32print::GetDefaultPrinter](#win32print.md#win32printGetDefaultPrinter), this method calls the GetDefaultPrinter API function.

## [win32print](#README.md#win32print).GetDeviceCaps

int = **GetDeviceCaps( *hdc*  *, Index* ** )
Retrieves device-specific parameters and settings

#### Parameters


     *hdc* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a printer or display device context

     *Index* : int

    The capability to return.  See MSDN for valid values.

#### Comments
Can also be used for Display DCs in addition to printer DCs

#### Win32 API References


    Search for *GetDeviceCaps* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDeviceCaps),[google](#README.md#http://www.google.com/search?q=GetDeviceCaps)or[google groups](#README.md#http://groups.google.com/groups?q=GetDeviceCaps).

## [win32print](#README.md#win32print).GetForm

 **GetForm( *hprinter*  *, FormName* ** )
Retrieves information about a form defined for a printer

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *FormName* :[PyUnicode](#README.md#PyUnicode)

    Name of form for which to retrieve info

#### Return Value
Returns a[FORM_INFO_1](#FORM.md#FORMINFO_1)dict

## [win32print](#README.md#win32print).GetJob

dictionary = **GetJob( *hPrinter*  *, JobID*  *, Level* ** )
Returns dictionary of information about a specified print job.

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle to a printer as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter).

     *JobID* : int

    Job Identifier.

     *Level=1* : int

    Level of information to return (JOB_INFO_1, JOB_INFO_2, JOB_INFO_3 supported).

#### Return Value
Returns a dict representing a JOB_INFO_* struct, depending on level

## [win32print](#README.md#win32print).GetPrintProcessorDirectory

[PyUnicode](#README.md#PyUnicode)= **GetPrintProcessorDirectory( *Name*  *, Environment* ** )
Returns the directory where print processor files reside

#### Parameters


     *Name* : str/[PyUnicode](#README.md#PyUnicode)

    Name of server, use None for local machine

     *Environment* : str/[PyUnicode](#README.md#PyUnicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

## [win32print](#README.md#win32print).GetPrinter

dict = **GetPrinter( *hPrinter*  *, Level* ** )
Retrieves information about a printer

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    handle to printer object as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *Level=2* : int

    Level of data returned (1,2,3,4,5,7,8,9)

#### Comments
Original implementation used level 2 only and returned a tuple 

Pass single arg as indicator to use old behaviour for backward compatibility

#### Return Value
Returns a dictionary containing PRINTER_INFO_* data for level, or 

returns a tuple of PRINTER_INFO_2 data if no level is passed in.

## [win32print](#README.md#win32print).GetPrinterDriverDirectory

[PyUnicode](#README.md#PyUnicode)= **GetPrinterDriverDirectory( *Name*  *, Environment* ** )
Returns the directory where printer drivers are installed

#### Parameters


     *Name* : str/[PyUnicode](#README.md#PyUnicode)

    Name of server, use None for local machine

     *Environment* : str/[PyUnicode](#README.md#PyUnicode)

    Environment - eg 'Windows NT x86' - use None for current client environment

## [win32print](#README.md#win32print).OpenPrinter

[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)= **OpenPrinter( *printer*  *, Defaults* ** )
Retrieves a handle to a printer.

#### Parameters


     *printer* : string

    Printer or print server name.  Use None to open local print server.

     *Defaults=None* : dict

    [PRINTER_DEFAULTS](#PRINTER.md#PRINTERDEFAULTS)dict, or None

## [win32print](#README.md#win32print).ScheduleJob

 **ScheduleJob( *hprinter*  *, JobId* ** )
Schedules a spooled job to be printed

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *JobId* : int

    Job Id as returned by[win32print::AddJob](#win32print.md#win32printAddJob)

## [win32print](#README.md#win32print).SetDefaultPrinter

None = **SetDefaultPrinter( *printer* ** )
Sets the default printer.

#### Parameters


     *printer* : string

    printer to set as default

#### Comments
This function uses the pre-win2k method of WriteProfileString rather than the SetDefaultPrinter API function

## [win32print](#README.md#win32print).SetDefaultPrinterW

None = **SetDefaultPrinterW( *Printer* ** )
Sets the default printer

#### Parameters


     *Printer* :[PyUnicode](#README.md#PyUnicode)

    Name of printer, can be None to use first available printer

#### Comments
Unlike[win32print::SetDefaultPrinter](#win32print.md#win32printSetDefaultPrinter), this method calls the SetDefaultPrinter API function.

## [win32print](#README.md#win32print).SetForm

 **SetForm( *hprinter*  *, FormName*  *, Form* ** )
Change information for a form

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *FormName* :[PyUnicode](#README.md#PyUnicode)

    Name of form

     *Form* : dict

    [FORM_INFO_1](#FORM.md#FORMINFO_1)dictionary

#### Return Value
Returns None on success

## [win32print](#README.md#win32print).SetJob

None = **SetJob( *hPrinter*  *, JobID*  *, Level*  *, JobInfo*  *, Command* ** )
Pause, cancel, resume, set priority levels on a print job.

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle of printer.

     *JobID* : int

    Job Identifier.

     *Level* : int

    Level of information in JobInfo dict (0, 1, 2, and 3 are supported).

     *JobInfo* : dict

    JOB_INFO_* Dictionary as returned by[win32print::GetJob](#win32print.md#win32printGetJob)or[win32print::EnumJobs](#win32print.md#win32printEnumJobs)(can be None if Level is 0).

     *Command* : int

    Job command value (JOB_CONTROL_*).

#### Comments
If printer is not opened with at least PRINTER_ACCESS_ADMINISTER access, 'Position' member of 

JOB_INFO_1 and JOB_INFO_2 must be set to JOB_POSITION_UNSPECIFIED

## [win32print](#README.md#win32print).SetPrinter

 **SetPrinter( *hPrinter*  *, Level*  *, pPrinter*  *, Command* ** )
Change printer configuration and status

#### Parameters


     *hPrinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

     *Level* : int

    Level of data contained in pPrinter

     *pPrinter* : dict

    PRINTER_INFO_* dict as returned by[win32print::GetPrinter](#win32print.md#win32printGetPrinter), can be None if level is 0

     *Command* : int

    Command to send to printer - one of the PRINTER_CONTROL_* constants, or 0

#### Comments
If Level is 0 and Command is PRINTER_CONTROL_SET_STATUS, pPrinter should be an integer, 

and is interpreted as the new printer status to set (one of the PRINTER_STATUS_* constants).

## [win32print](#README.md#win32print).StartDoc

int = **StartDoc( *hdc*  *, docinfo* ** )
Starts spooling a print job on a printer device context

#### Parameters


     *hdc* :[PyHANDLE](#README.md#PyHANDLE)

    Printer device context handle as returned by[win32gui::CreateDC](#win32gui.md#win32guiCreateDC)

     *docinfo* : tuple

    [DOCINFO](#README.md#DOCINFO)tuple specifying print job parameters

#### Return Value
On success, returns the job id of the print job

## [win32print](#README.md#win32print).StartDocPrinter

int = **StartDocPrinter( *hprinter*  *, level*  *, tuple* ** )
Notifies the print spooler that a document is to be spooled for printing. To be used before using WritePrinter. Returns the Jobid of the started job.

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    handle to printer (from[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter))

     *level=1* : int

    type of docinfo structure (only docinfo level 1 supported)

     *tuple* : data

    A tuple corresponding to the level parameter.

#### Comments
For level 1, the tuple is:

#### Items


    [0] *string* : docName

    Specifies the name of the document.

    [1] *string* : outputFile

    Specifies the name of an output file. To print to a printer, set this to None.

    [2] *string* : dataType

    Identifies the type of data used to record the document, such 

as "raw" or "emf", used to record the print job. This member can be None. If it is not None, 

the StartDoc function passes it to the printer driver. Note that the printer driver might 

ignore the requested data type.

## [win32print](#README.md#win32print).StartPage

 **StartPage( *hdc* ** )
Starts a page on a printer device context

#### Parameters


     *hdc* :[PyHANDLE](#README.md#PyHANDLE)

    Printer device context handle as returned by[win32gui::CreateDC](#win32gui.md#win32guiCreateDC)

## [win32print](#README.md#win32print).StartPagePrinter

 **StartPagePrinter( *hprinter* ** )
Notifies the print spooler that a page is to be printed on specified printer

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Printer handle as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter)

## [win32print](#README.md#win32print).WritePrinter

int = **WritePrinter( *hprinter*  *, buf* ** )
Copies the specified bytes to the specified printer. 

Suitable for copying raw Postscript or HPGL files to a printer. 

StartDocPrinter and EndDocPrinter should be called before and after.

#### Parameters


     *hprinter* :[PyPrinterHANDLE](#README.md#PyPrinterHANDLE)

    Handle to printer as returned by[win32print::OpenPrinter](#win32print.md#win32printOpenPrinter).

     *buf* : string

    String or buffer containing data to send to printer. Embedded NULL bytes are allowed.

#### Return Value
Returns number of bytes written to printer.