# wincerapi

## Module wincerapi

A module which provides an interface to the win32 CE Remote API

#### Methods


  - [CeRapiInit](wincerapi.md#wincerapicerapiinit)

    Initializes the remote API.&nbsp;

  - [CeRapiUninit](wincerapi.md#wincerapicerapiuninit)

    UnInitializes the remote API.&nbsp;

  - [CreateProcess](wincerapi.md#wincerapicreateprocess)

    Creates a new process and its primary thread. The new process executes the specified executable file.&nbsp;

  - [CeRapiInitEx](wincerapi.md#wincerapicerapiinitex)

    Initializes the remote API asynchronously.&nbsp;

  - [CeCopyFile](wincerapi.md#wincerapicecopyfile)

    Copies a file&nbsp;

  - [CeCheckPassword](wincerapi.md#wincerapicecheckpassword)

    This function compares a specified string to the system password.&nbsp;

  - [CeCreateFile](wincerapi.md#wincerapicecreatefile)

    Creates or opens the a file or other object and returns a handle that can be used to access the object.&nbsp;

  - [CeDeleteFile](wincerapi.md#wincerapicedeletefile)

    Deletes a file.&nbsp;

  - [CeMoveFile](wincerapi.md#wincerapicemovefile)

    Renames an existing file or a directory (including all its children).&nbsp;

  - [CeCreateDirectory](wincerapi.md#wincerapicecreatedirectory)

    Creates a directory&nbsp;

  - [CeRemoveDirectory](wincerapi.md#wincerapiceremovedirectory)

    Removes an existing directory&nbsp;

  - [CeGetTempPath](wincerapi.md#wincerapicegettemppath)

    Obtains the temp path on the device.&nbsp;

  - [CeGetSystemInfo](wincerapi.md#wincerapicegetsysteminfo)

    Retrieves information about the CE device.&nbsp;

  - [CeGetDesktopDeviceCaps](wincerapi.md#wincerapicegetdesktopdevicecaps)

    Retrieves information about the CE desktop.&nbsp;

  - [CeGetSystemMetrics](wincerapi.md#wincerapicegetsystemmetrics)

    Retrieves information about the CE system.&nbsp;

  - [CeGetSpecialFolderPath](wincerapi.md#wincerapicegetspecialfolderpath)

    Retrieves the location of special folders on the CE device.&nbsp;

  - [CeGetStoreInformation](wincerapi.md#wincerapicegetstoreinformation)

    Retrieves information about store on the CE system.&nbsp;

  - [CeGetSystemPowerStatusEx](wincerapi.md#wincerapicegetsystempowerstatusex)

    Retrieves the power status of the CE device.&nbsp;

  - [CeSHCreateShortcut](wincerapi.md#wincerapiceshcreateshortcut)

    Creates a shortcut on the remote device.&nbsp;

  - [CeSHGetShortcutTarget](wincerapi.md#wincerapiceshgetshortcuttarget)

    Retrieves the target of a shortcut.&nbsp;

  - [CeGetVersionEx](wincerapi.md#wincerapicegetversionex)

    Returns the current version of Windows, and information about the environment for the CE device.&nbsp;

  - [CeGlobalMemoryStatus](wincerapi.md#wincerapiceglobalmemorystatus)

    Returns information about current memory availability.&nbsp;

  - [FindFiles](wincerapi.md#wincerapifindfiles)

    Retrieves a list of matching filenames on the CE device.  An interface to the API CeFindFirstFile/CeFindNextFile functions.&nbsp;

  - [CeGetFileAttributes](wincerapi.md#wincerapicegetfileattributes)

    Determines a files attributes.&nbsp;

  - [CeSetFileAttributes](wincerapi.md#wincerapicesetfileattributes)

    Changes a file's attributes.&nbsp;

  - [CeGetFileSize](wincerapi.md#wincerapicegetfilesize)

    Determines the size of a file.&nbsp;

  - [CeReadFile](wincerapi.md#wincerapicereadfile)

    Reads a file from the CE device.&nbsp;

  - [WriteFile](wincerapi.md#wincerapiwritefile)

    Writes a string to a file&nbsp;

## [wincerapi](#wincerapi).CEHANDLE

[PyCEHANDLE](#pycehandle)= __CEHANDLE(__ )
Creates a new CEHANDLE object

## CSIDL_BITBUCKET
 __const wincerapi.CSIDL_BITBUCKET;__ 
Recycle bin-file system directory containing file objects in the user's recycle bin. The location of this directory is not in the registry; it is marked with the hidden and system attributes to prevent the user from moving or deleting it.

## CSIDL_COMMON_DESKTOPDIRECTORY
 __const wincerapi.CSIDL_COMMON_DESKTOPDIRECTORY;__ 
File system directory that contains files and folders that appear on the desktop for all users.

## CSIDL_COMMON_PROGRAMS
 __const wincerapi.CSIDL_COMMON_PROGRAMS;__ 
File system directory that contains the directories for the common program groups that appear on the Start menu for all users.

## CSIDL_COMMON_STARTMENU
 __const wincerapi.CSIDL_COMMON_STARTMENU;__ 
File system directory that contains the programs and folders that appear on the Start menu for all users.

## CSIDL_COMMON_STARTUP
 __const wincerapi.CSIDL_COMMON_STARTUP;__ 
File system directory that contains the programs that appear in the Startup folder for all users. The system starts these programs whenever any user logs on to a Windows desktop platform.

## CSIDL_CONTROLS
 __const wincerapi.CSIDL_CONTROLS;__ 
Control Panel-virtual folder containing icons for the control panel applications.

## CSIDL_DESKTOP
 __const wincerapi.CSIDL_DESKTOP;__ 
Windows desktop-virtual folder at the root of the name space.

## CSIDL_DESKTOPDIRECTORY
 __const wincerapi.CSIDL_DESKTOPDIRECTORY;__ 
File system directory used to physically store file objects on the desktop - not to be confused with the desktop folder itself.

## CSIDL_DRIVES
 __const wincerapi.CSIDL_DRIVES;__ 
My Computer-virtual folder containing everything on the local computer: storage devices, printers, and Control Panel. The folder can also contain mapped network drives.

## CSIDL_FONTS
 __const wincerapi.CSIDL_FONTS;__ 
Virtual folder containing fonts.

## CSIDL_NETHOOD
 __const wincerapi.CSIDL_NETHOOD;__ 
File system directory containing objects that appear in the network neighborhood.

## CSIDL_NETWORK
 __const wincerapi.CSIDL_NETWORK;__ 
Network Neighborhood-virtual folder representing the top level of the network hierarchy.

## CSIDL_PERSONAL
 __const wincerapi.CSIDL_PERSONAL;__ 
File system directory that serves as a common repository for documents.

## CSIDL_PRINTERS
 __const wincerapi.CSIDL_PRINTERS;__ 
Printers folder-virtual folder containing installed printers.

## CSIDL_PROGRAMS
 __const wincerapi.CSIDL_PROGRAMS;__ 
File system directory that contains the user's program groups which are also file system directories.

## CSIDL_RECENT
 __const wincerapi.CSIDL_RECENT;__ 
File system directory containing the user's most recently used documents.

## CSIDL_SENDTO
 __const wincerapi.CSIDL_SENDTO;__ 
File system directory containing Send To menu items.

## CSIDL_STARTMENU
 __const wincerapi.CSIDL_STARTMENU;__ 
File system directory containing Start menu items.

## CSIDL_STARTUP
 __const wincerapi.CSIDL_STARTUP;__ 
File system directory that corresponds to the user's Startup program group.

## CSIDL_TEMPLATES
 __const wincerapi.CSIDL_TEMPLATES;__ 
File system directory that serves as a common repository for document templates.

## [wincerapi](#wincerapi).CeCheckPassword

 __CeCheckPassword( *password* __ )
This function compares a specified string to the system password.

#### Parameters


  -  *password* :[PyUnicode](#pyunicode)

    The password to compare.

## [wincerapi](#wincerapi).CeCopyFile

 __CeCopyFile( *from*  *, to*  *, bFailIfExists* __ )
Copies a file

#### Parameters


  -  *from* :[PyUnicode](#pyunicode)

    The name of the file to copy from

  -  *to* :[PyUnicode](#pyunicode)

    The name of the file to copy to

  -  *bFailIfExists* : int

    Indicates if the operation should fail if the file exists.

## [wincerapi](#wincerapi).CeCreateDirectory

 __CeCreateDirectory( *name*  *, sa* __ )
Creates a directory

#### Parameters


  -  *name* :[PyUnicode](#pyunicode)

    The name of the directory to create

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

## [wincerapi](#wincerapi).CeCreateFile

[PyCEHANDLE](#pycehandle)= __CeCreateFile( *fileName*  *, desiredAccess*  *, shareMode*  *, attributes*  *, creationDisposition*  *, flagsAndAttributes*  *, hTemplateFile* __ )
Creates or opens the a file or other object and returns a handle that can be used to access the object.

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    The name of the file

  -  *desiredAccess* : int

    access (read-write) mode 

Specifies the type of access to the object. An application can obtain read access, write access, read-write access, or device query access. This parameter can be any combination of the following values.

 __Value__  __Meaning__ 0Specifies device query access to the object. An application can query device attributes without accessing the device.GENERIC_READSpecifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.GENERIC_WRITESpecifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.
  -  *shareMode* : int

    Set of bit flags that specifies how the object can be shared. If dwShareMode is 0, the object cannot be shared. Subsequent open operations on the object will fail, until the handle is closed. 

To share the object, use a combination of one or more of the following values:

 __Value__  __Meaning__ FILE_SHARE_DELETEWindows NT: Subsequent open operations on the object will succeed only if delete access is requested.FILE_SHARE_READSubsequent open operations on the object will succeed only if read access is requested.FILE_SHARE_WRITESubsequent open operations on the object will succeed only if write access is requested.
  -  *attributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *creationDisposition* : int

    Specifies which action to take on files that exist, and which action to take when files do not exist. For more information about this parameter, see the Remarks section. This parameter must be one of the following values:

 __Value__  __Meaning__ CREATE_NEWCreates a new file. The function fails if the specified file already exists.CREATE_ALWAYSCreates a new file. If the file exists, the function overwrites the file and clears the existing attributes.OPEN_EXISTINGOpens the file. The function fails if the file does not exist. 

See the Remarks section for a discussion of why you should use the OPEN_EXISTING flag if you are using the CreateFile function for devices, including the console.OPEN_ALWAYSOpens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE_NEW.TRUNCATE_EXISTINGOpens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.
  -  *flagsAndAttributes* : int

    file attributes

  -  *hTemplateFile* :[PyHANDLE](#pyhandle)

    Specifies a handle with GENERIC_READ access to a template file. The template file supplies file attributes and extended attributes for the file being created.   Under Win95, this must be 0, else an exception will be raised.

#### Comments
The following objects can be opened:
files
pipes
mailslots
communications resources
disk devices (Windows NT only)
consoles
directories (open only)

## [wincerapi](#wincerapi).CeDeleteFile

 __CeDeleteFile( *fileName* __ )
Deletes a file.

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    The filename to delete

## [wincerapi](#wincerapi).CeGetDesktopDeviceCaps

int = __CeGetDesktopDeviceCaps(__ )
Retrieves information about the CE desktop.

## [wincerapi](#wincerapi).CeGetFileAttributes

int = __CeGetFileAttributes( *fileName* __ )
Determines a files attributes.

#### Parameters


  -  *fileName* :[PyUnicode](#pyunicode)

    Name of the file to retrieve attributes for.

## [wincerapi](#wincerapi).CeGetFileSize

 __PyLARGE_INTEGER__ = __CeGetFileSize(__ )
Determines the size of a file.

## [wincerapi](#wincerapi).CeGetSpecialFolderPath

[PyUnicode](#pyunicode)= __CeGetSpecialFolderPath(__ )
Retrieves the location of special folders on the CE device.

## [wincerapi](#wincerapi).CeGetStoreInformation

int, int = __CeGetStoreInformation(__ )
Retrieves information about store on the CE system.

#### Return Value
The result is a tuple of (storeSize, freeSize)

## [wincerapi](#wincerapi).CeGetSystemInfo

tuple = __CeGetSystemInfo(__ )
Retrieves information about the CE device.

#### Win32 API References


  - Search for *GetSystemInfo* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=getsysteminfo),[google](#http://www.google.com/search?q=getsysteminfo)or[google groups](#http://groups.google.com/groups?q=getsysteminfo).

#### Return Value
The return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM_INFO structure.  The element names are:
dwOemId
dwPageSize
lpMinimumApplicationAddress
lpMaximumApplicationAddress
, 

dwActiveProcessorMask
dwNumberOfProcessors
dwProcessorType
dwAllocationGranularity
(wProcessorLevel,wProcessorRevision)

## [wincerapi](#wincerapi).CeGetSystemMetrics

int = __CeGetSystemMetrics(__ )
Retrieves information about the CE system.

## [wincerapi](#wincerapi).CeGetSystemPowerStatusEx

tuple = __CeGetSystemPowerStatusEx(__ )
Retrieves the power status of the CE device.

#### Return Value
The result is a tuple of (ACLineStatus, BatteryFlag, BatteryLifePercent, BatteryLifeTime, BatteryFullLifeTime, BackupBatteryFlag, BackupBatteryLifePercent, BackupBatteryLifeTime, BackupBatteryLifeTime);

## [wincerapi](#wincerapi).CeGetTempPath

[PyUnicode](#pyunicode)= __CeGetTempPath(__ )
Obtains the temp path on the device.

## [wincerapi](#wincerapi).CeGetVersionEx

(int,int,int,int,string) = __CeGetVersionEx(__ )
Returns the current version of Windows, and information about the environment for the CE device.

#### Return Value
The return value is a tuple with the following information.


## [wincerapi](#wincerapi).CeGlobalMemoryStatus

tuple = __CeGlobalMemoryStatus(__ )
Returns information about current memory availability.

#### Return Value
The return value is a tuple with the following information.


## [wincerapi](#wincerapi).CeMoveFile

 __CeMoveFile( *existingFileName*  *, newFileName* __ )
Renames an existing file or a directory (including all its children).

#### Parameters


  -  *existingFileName* :[PyUnicode](#pyunicode)

    Name of the existing file

  -  *newFileName* :[PyUnicode](#pyunicode)

    New name for the file

## [wincerapi](#wincerapi).CeRapiInit

 __CeRapiInit(__ )
Initializes the remote API.

## [wincerapi](#wincerapi).CeRapiInitEx

int = __CeRapiInitEx(__ )
Initializes the remote API asynchronously.

## [wincerapi](#wincerapi).CeRapiUninit

 __CeRapiUninit(__ )
UnInitializes the remote API.

## [wincerapi](#wincerapi).CeReadFile

string = __CeReadFile( *hFile*  *, bufSize* __ )
Reads a file from the CE device.

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *bufSize* : int

    Size of the buffer to create for the read.

## [wincerapi](#wincerapi).CeRemoveDirectory

 __CeRemoveDirectory( *lpPathName* __ )
Removes an existing directory

#### Parameters


  -  *lpPathName* :[PyUnicode](#pyunicode)

    Name of the path to remove.

## [wincerapi](#wincerapi).CeSHCreateShortcut

 __CeSHCreateShortcut(__ )
Creates a shortcut on the remote device.

## [wincerapi](#wincerapi).CeSHGetShortcutTarget

tuple = __CeSHGetShortcutTarget(__ )
Retrieves the target of a shortcut.

## [wincerapi](#wincerapi).CeSetFileAttributes

 __CeSetFileAttributes( *filename*  *, newAttributes* __ )
Changes a file's attributes.

#### Parameters


  -  *filename* :[PyUnicode](#pyunicode)

    filename

  -  *newAttributes* : int

    attributes to set

## [wincerapi](#wincerapi).CreateProcess

[PyHANDLE](#pyhandle),[PyHANDLE](#pyhandle), int, int = __CreateProcess( *appName*  *, commandLine*  *, processAttributes*  *, threadAttributes*  *, bInheritHandles*  *, dwCreationFlags*  *, newEnvironment*  *, currentDirectory*  *, startupinfo* __ )
Creates a new process and its primary thread. The new process executes the specified executable file.

#### Parameters


  -  *appName* : string

    name of executable module, or None

  -  *commandLine* : string

    command line string, or None

  -  *processAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    process security attributes, or None

  -  *threadAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    thread security attributes, or None

  -  *bInheritHandles* : int

    handle inheritance flag

  -  *dwCreationFlags* : int

    creation flags

  -  *newEnvironment* : None

    A dictionary of stringor Unicode pairs to define the environment for the process, or None to inherit the current environment.

  -  *currentDirectory* : string

    current directory name, or None

  -  *startupinfo* :[PySTARTUPINFO](#pystartupinfo)

    a STARTUPINFO object that specifies how the main window for the new process should appear.

#### Comments
The result is a tuple of (hProcess, hThread, dwProcessId, dwThreadId)

## [wincerapi](#wincerapi).FindFiles

list = __FindFiles( *fileSpec* __ )
Retrieves a list of matching filenames on the CE device.  An interface to the API CeFindFirstFile/CeFindNextFile functions.

#### Parameters


  -  *fileSpec* :[PyUnicode](#pyunicode)

    A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

#### Win32 API References


  - Search for *CeFindFirstFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=cefindfirstfile),[google](#http://www.google.com/search?q=cefindfirstfile)or[google groups](#http://groups.google.com/groups?q=cefindfirstfile).

  - Search for *FindNextFile* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=findnextfile),[google](#http://www.google.com/search?q=findnextfile)or[google groups](#http://groups.google.com/groups?q=findnextfile).

  - Search for *CloseHandle* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=closehandle),[google](#http://www.google.com/search?q=closehandle)or[google groups](#http://groups.google.com/groups?q=closehandle).

#### Return Value
The return value is a list of tuples, in the same format as the WIN32_FIND_DATA structure:

#### Items


  - [0] *int* : attributes

    File Attributes.  A combination of the win32com.FILE_ATTRIBUTE_* flags.

  - [1] *[PyTime](#pytime)* : createTime

    File creation time.

  - [2] *[PyTime](#pytime)* : accessTime

    File access time.

  - [3] *[PyTime](#pytime)* : writeTime

    Time of last file write

  - [4] *int* : nFileSizeHigh

    high order word of file size.

  - [5] *int* : nFileSizeLow

    low order word of file size.

  - [6] *int* : OID

    The object identifier for the file

  - [7] *int* : zero

    Filler

  - [8] *string* : fileName

    The name of the file.

  - [9] *None* : altName

    Always None

## [wincerapi](#wincerapi).WriteFile

int, int = __WriteFile( *hFile*  *, data* __ )
Writes a string to a file

#### Parameters


  -  *hFile* :[PyHANDLE](#pyhandle)/int

    Handle to the file

  -  *data* : string

    The data to write.

#### Return Value
The result is a tuple of (errCode, nBytesWritten). 

errCode will always be zero (until overlapped IO is supported!)