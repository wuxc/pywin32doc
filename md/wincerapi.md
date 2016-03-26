# wincerapi


## Module wincerapi

A module which provides an interface to the win32 CE Remote API

#### Methods

  - [CeRapiInit](wincerapi.md#wincerapicerapiinit)

    Initializes the remote API\.&nbsp;

  - [CeRapiUninit](wincerapi.md#wincerapicerapiuninit)

    UnInitializes the remote API\.&nbsp;

  - [CreateProcess](wincerapi.md#wincerapicreateprocess)

    Creates a new process and its primary thread\. The new process executes the specified executable file\.&nbsp;

  - [CeRapiInitEx](wincerapi.md#wincerapicerapiinitex)

    Initializes the remote API asynchronously\.&nbsp;

  - [CeCopyFile](wincerapi.md#wincerapicecopyfile)

    Copies a file&nbsp;

  - [CeCheckPassword](wincerapi.md#wincerapicecheckpassword)

    This function compares a specified string to the system password\.&nbsp;

  - [CeCreateFile](wincerapi.md#wincerapicecreatefile)

    Creates or opens the a file or other object and returns a handle that can be used to access the object\.&nbsp;

  - [CeDeleteFile](wincerapi.md#wincerapicedeletefile)

    Deletes a file\.&nbsp;

  - [CeMoveFile](wincerapi.md#wincerapicemovefile)

    Renames an existing file or a directory \(including all its children\)\.&nbsp;

  - [CeCreateDirectory](wincerapi.md#wincerapicecreatedirectory)

    Creates a directory&nbsp;

  - [CeRemoveDirectory](wincerapi.md#wincerapiceremovedirectory)

    Removes an existing directory&nbsp;

  - [CeGetTempPath](wincerapi.md#wincerapicegettemppath)

    Obtains the temp path on the device\.&nbsp;

  - [CeGetSystemInfo](wincerapi.md#wincerapicegetsysteminfo)

    Retrieves information about the CE device\.&nbsp;

  - [CeGetDesktopDeviceCaps](wincerapi.md#wincerapicegetdesktopdevicecaps)

    Retrieves information about the CE desktop\.&nbsp;

  - [CeGetSystemMetrics](wincerapi.md#wincerapicegetsystemmetrics)

    Retrieves information about the CE system\.&nbsp;

  - [CeGetSpecialFolderPath](wincerapi.md#wincerapicegetspecialfolderpath)

    Retrieves the location of special folders on the CE device\.&nbsp;

  - [CeGetStoreInformation](wincerapi.md#wincerapicegetstoreinformation)

    Retrieves information about store on the CE system\.&nbsp;

  - [CeGetSystemPowerStatusEx](wincerapi.md#wincerapicegetsystempowerstatusex)

    Retrieves the power status of the CE device\.&nbsp;

  - [CeSHCreateShortcut](wincerapi.md#wincerapiceshcreateshortcut)

    Creates a shortcut on the remote device\.&nbsp;

  - [CeSHGetShortcutTarget](wincerapi.md#wincerapiceshgetshortcuttarget)

    Retrieves the target of a shortcut\.&nbsp;

  - [CeGetVersionEx](wincerapi.md#wincerapicegetversionex)

    Returns the current version of Windows, and information about the environment for the CE device\.&nbsp;

  - [CeGlobalMemoryStatus](wincerapi.md#wincerapiceglobalmemorystatus)

    Returns information about current memory availability\.&nbsp;

  - [FindFiles](wincerapi.md#wincerapifindfiles)

    Retrieves a list of matching filenames on the CE device\.  An interface to the API CeFindFirstFile/CeFindNextFile functions\.&nbsp;

  - [CeGetFileAttributes](wincerapi.md#wincerapicegetfileattributes)

    Determines a files attributes\.&nbsp;

  - [CeSetFileAttributes](wincerapi.md#wincerapicesetfileattributes)

    Changes a file's attributes\.&nbsp;

  - [CeGetFileSize](wincerapi.md#wincerapicegetfilesize)

    Determines the size of a file\.&nbsp;

  - [CeReadFile](wincerapi.md#wincerapicereadfile)

    Reads a file from the CE device\.&nbsp;

  - [WriteFile](wincerapi.md#wincerapiwritefile)

    Writes a string to a file&nbsp;


## [wincerapi](wincerapi.md#wincerapi)\.CEHANDLE

[PyCEHANDLE](PyCEHANDLE.md) = CEHANDLE\(\)
Creates a new CEHANDLE object


## CSIDL\_BITBUCKET

const wincerapi\.CSIDL\_BITBUCKET;

Recycle bin-file system directory containing file objects in the user's recycle bin\. The location of this directory is not in the registry; it is marked with the hidden and system attributes to prevent the user from moving or deleting it\.


## CSIDL\_COMMON\_DESKTOPDIRECTORY

const wincerapi\.CSIDL\_COMMON\_DESKTOPDIRECTORY;

File system directory that contains files and folders that appear on the desktop for all users\.


## CSIDL\_COMMON\_PROGRAMS

const wincerapi\.CSIDL\_COMMON\_PROGRAMS;

File system directory that contains the directories for the common program groups that appear on the Start menu for all users\.


## CSIDL\_COMMON\_STARTMENU

const wincerapi\.CSIDL\_COMMON\_STARTMENU;

File system directory that contains the programs and folders that appear on the Start menu for all users\.


## CSIDL\_COMMON\_STARTUP

const wincerapi\.CSIDL\_COMMON\_STARTUP;

File system directory that contains the programs that appear in the Startup folder for all users\. The system starts these programs whenever any user logs on to a Windows desktop platform\.


## CSIDL\_CONTROLS

const wincerapi\.CSIDL\_CONTROLS;

Control Panel-virtual folder containing icons for the control panel applications\.


## CSIDL\_DESKTOP

const wincerapi\.CSIDL\_DESKTOP;

Windows desktop-virtual folder at the root of the name space\.


## CSIDL\_DESKTOPDIRECTORY

const wincerapi\.CSIDL\_DESKTOPDIRECTORY;

File system directory used to physically store file objects on the desktop - not to be confused with the desktop folder itself\.


## CSIDL\_DRIVES

const wincerapi\.CSIDL\_DRIVES;

My Computer-virtual folder containing everything on the local computer: storage devices, printers, and Control Panel\. The folder can also contain mapped network drives\.


## CSIDL\_FONTS

const wincerapi\.CSIDL\_FONTS;

Virtual folder containing fonts\.


## CSIDL\_NETHOOD

const wincerapi\.CSIDL\_NETHOOD;

File system directory containing objects that appear in the network neighborhood\.


## CSIDL\_NETWORK

const wincerapi\.CSIDL\_NETWORK;

Network Neighborhood-virtual folder representing the top level of the network hierarchy\.


## CSIDL\_PERSONAL

const wincerapi\.CSIDL\_PERSONAL;

File system directory that serves as a common repository for documents\.


## CSIDL\_PRINTERS

const wincerapi\.CSIDL\_PRINTERS;

Printers folder-virtual folder containing installed printers\.


## CSIDL\_PROGRAMS

const wincerapi\.CSIDL\_PROGRAMS;

File system directory that contains the user's program groups which are also file system directories\.


## CSIDL\_RECENT

const wincerapi\.CSIDL\_RECENT;

File system directory containing the user's most recently used documents\.


## CSIDL\_SENDTO

const wincerapi\.CSIDL\_SENDTO;

File system directory containing Send To menu items\.


## CSIDL\_STARTMENU

const wincerapi\.CSIDL\_STARTMENU;

File system directory containing Start menu items\.


## CSIDL\_STARTUP

const wincerapi\.CSIDL\_STARTUP;

File system directory that corresponds to the user's Startup program group\.


## CSIDL\_TEMPLATES

const wincerapi\.CSIDL\_TEMPLATES;

File system directory that serves as a common repository for document templates\.


## [wincerapi](wincerapi.md#wincerapi)\.CeCheckPassword

CeCheckPassword\(password\)
This function compares a specified string to the system password\.

#### Parameters

  - password : [PyUnicode](PyUnicode.md)

    The password to compare\.


## [wincerapi](wincerapi.md#wincerapi)\.CeCopyFile

CeCopyFile\(from, to, bFailIfExists\)
Copies a file

#### Parameters

  - from : [PyUnicode](PyUnicode.md)

    The name of the file to copy from

  - to : [PyUnicode](PyUnicode.md)

    The name of the file to copy to

  - bFailIfExists : int

    Indicates if the operation should fail if the file exists\.


## [wincerapi](wincerapi.md#wincerapi)\.CeCreateDirectory

CeCreateDirectory\(name, sa\)
Creates a directory

#### Parameters

  - name : [PyUnicode](PyUnicode.md)

    The name of the directory to create

  - sa : [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None


## [wincerapi](wincerapi.md#wincerapi)\.CeCreateFile

[PyCEHANDLE](PyCEHANDLE.md) = CeCreateFile\(fileName, desiredAccess

, shareMode

, attributes

, creationDisposition

, flagsAndAttributes

, hTemplateFile

\)
Creates or opens the a file or other object and returns a handle that can be used to access the object\.

#### Parameters

  - fileName : [PyUnicode](PyUnicode.md)

    The name of the file

  - desiredAccess : int

    access \(read-write\) mode 

Specifies the type of access to the object\. An application can obtain read access, write access, read-write access, or device query access\. This parameter can be any combination of the following values\.

   

       Value

   

   

       Meaning

   

0Specifies device query access to the object\. An application can query device attributes without accessing the device\.

GENERIC\_READSpecifies read access to the object\. Data can be read from the file and the file pointer can be moved\. Combine with GENERIC\_WRITE for read-write access\.

GENERIC\_WRITESpecifies write access to the object\. Data can be written to the file and the file pointer can be moved\. Combine with GENERIC\_READ for read-write access\.

  - shareMode : int

    Set of bit flags that specifies how the object can be shared\. If dwShareMode is 0, the object cannot be shared\. Subsequent open operations on the object will fail, until the handle is closed\. 

To share the object, use a combination of one or more of the following values:

   

       Value

   

   

       Meaning

   

FILE\_SHARE\_DELETEWindows NT: Subsequent open operations on the object will succeed only if delete access is requested\.

FILE\_SHARE\_READSubsequent open operations on the object will succeed only if read access is requested\.

FILE\_SHARE\_WRITESubsequent open operations on the object will succeed only if write access is requested\.

  - attributes : [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  - creationDisposition : int

    Specifies which action to take on files that exist, and which action to take when files do not exist\. For more information about this parameter, see the Remarks section\. This parameter must be one of the following values:

   

       Value

   

   

       Meaning

   

CREATE\_NEWCreates a new file\. The function fails if the specified file already exists\.

CREATE\_ALWAYSCreates a new file\. If the file exists, the function overwrites the file and clears the existing attributes\.

OPEN\_EXISTINGOpens the file\. The function fails if the file does not exist\. 

See the Remarks section for a discussion of why you should use the OPEN\_EXISTING flag if you are using the CreateFile function for devices, including the console\.

OPEN\_ALWAYSOpens the file, if it exists\. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE\_NEW\.

TRUNCATE\_EXISTINGOpens the file\. Once opened, the file is truncated so that its size is zero bytes\. The calling process must open the file with at least GENERIC\_WRITE access\. The function fails if the file does not exist\.

  - flagsAndAttributes : int

    file attributes

  - hTemplateFile : [PyHANDLE](PyHANDLE.md)

    Specifies a handle with GENERIC\_READ access to a template file\. The template file supplies file attributes and extended attributes for the file being created\.   Under Win95, this must be 0, else an exception will be raised\.

#### Comments

The following objects can be opened:
files
pipes
mailslots
communications resources
disk devices \(Windows NT only\)
consoles
directories \(open only\)


## [wincerapi](wincerapi.md#wincerapi)\.CeDeleteFile

CeDeleteFile\(fileName\)
Deletes a file\.

#### Parameters

  - fileName : [PyUnicode](PyUnicode.md)

    The filename to delete


## [wincerapi](wincerapi.md#wincerapi)\.CeGetDesktopDeviceCaps

int = CeGetDesktopDeviceCaps\(\)
Retrieves information about the CE desktop\.


## [wincerapi](wincerapi.md#wincerapi)\.CeGetFileAttributes

int = CeGetFileAttributes\(fileName\)
Determines a files attributes\.

#### Parameters

  - fileName : [PyUnicode](PyUnicode.md)

    Name of the file to retrieve attributes for\.


## [wincerapi](wincerapi.md#wincerapi)\.CeGetFileSize

PyLARGE\_INTEGER

 = CeGetFileSize\(\)
Determines the size of a file\.


## [wincerapi](wincerapi.md#wincerapi)\.CeGetSpecialFolderPath

[PyUnicode](PyUnicode.md) = CeGetSpecialFolderPath\(\)
Retrieves the location of special folders on the CE device\.


## [wincerapi](wincerapi.md#wincerapi)\.CeGetStoreInformation

int, int = CeGetStoreInformation\(\)
Retrieves information about store on the CE system\.

#### Return Value
The result is a tuple of \(storeSize, freeSize\)


## [wincerapi](wincerapi.md#wincerapi)\.CeGetSystemInfo

tuple = CeGetSystemInfo\(\)
Retrieves information about the CE device\.

#### Win32 API References

  - Search for GetSystemInfo at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemInfo.md), [google](http://www.google.com/search?q=GetSystemInfo.md) or [google groups](http://groups.google.com/groups?q=GetSystemInfo.md)\.

#### Return Value
The return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM\_INFO structure\.  The element names are: 

dwOemId
dwPageSize
lpMinimumApplicationAddress
lpMaximumApplicationAddress
, 

dwActiveProcessorMask
dwNumberOfProcessors
 

dwProcessorType
dwAllocationGranularity
\(wProcessorLevel,wProcessorRevision\)


## [wincerapi](wincerapi.md#wincerapi)\.CeGetSystemMetrics

int = CeGetSystemMetrics\(\)
Retrieves information about the CE system\.


## [wincerapi](wincerapi.md#wincerapi)\.CeGetSystemPowerStatusEx

tuple = CeGetSystemPowerStatusEx\(\)
Retrieves the power status of the CE device\.

#### Return Value
The result is a tuple of \(ACLineStatus, BatteryFlag, BatteryLifePercent, BatteryLifeTime, BatteryFullLifeTime, BackupBatteryFlag, BackupBatteryLifePercent, BackupBatteryLifeTime, BackupBatteryLifeTime\);


## [wincerapi](wincerapi.md#wincerapi)\.CeGetTempPath

[PyUnicode](PyUnicode.md) = CeGetTempPath\(\)
Obtains the temp path on the device\.


## [wincerapi](wincerapi.md#wincerapi)\.CeGetVersionEx

\(int,int,int,int,string\) = CeGetVersionEx\(\)
Returns the current version of Windows, and information about the environment for the CE device\.

#### Return Value
The return value is a tuple with the following information\.



## [wincerapi](wincerapi.md#wincerapi)\.CeGlobalMemoryStatus

tuple = CeGlobalMemoryStatus\(\)
Returns information about current memory availability\.

#### Return Value
The return value is a tuple with the following information\.



## [wincerapi](wincerapi.md#wincerapi)\.CeMoveFile

CeMoveFile\(existingFileName, newFileName\)
Renames an existing file or a directory \(including all its children\)\.

#### Parameters

  - existingFileName : [PyUnicode](PyUnicode.md)

    Name of the existing file

  - newFileName : [PyUnicode](PyUnicode.md)

    New name for the file


## [wincerapi](wincerapi.md#wincerapi)\.CeRapiInit

CeRapiInit\(\)
Initializes the remote API\.


## [wincerapi](wincerapi.md#wincerapi)\.CeRapiInitEx

int = CeRapiInitEx\(\)
Initializes the remote API asynchronously\.


## [wincerapi](wincerapi.md#wincerapi)\.CeRapiUninit

CeRapiUninit\(\)
UnInitializes the remote API\.


## [wincerapi](wincerapi.md#wincerapi)\.CeReadFile

string = CeReadFile\(hFile, bufSize

\)
Reads a file from the CE device\.

#### Parameters

  - hFile : [PyHANDLE](PyHANDLE.md)/int

    Handle to the file

  - bufSize : int

    Size of the buffer to create for the read\.


## [wincerapi](wincerapi.md#wincerapi)\.CeRemoveDirectory

CeRemoveDirectory\(lpPathName\)
Removes an existing directory

#### Parameters

  - lpPathName : [PyUnicode](PyUnicode.md)

    Name of the path to remove\.


## [wincerapi](wincerapi.md#wincerapi)\.CeSHCreateShortcut

CeSHCreateShortcut\(\)
Creates a shortcut on the remote device\.


## [wincerapi](wincerapi.md#wincerapi)\.CeSHGetShortcutTarget

tuple = CeSHGetShortcutTarget\(\)
Retrieves the target of a shortcut\.


## [wincerapi](wincerapi.md#wincerapi)\.CeSetFileAttributes

CeSetFileAttributes\(filename, newAttributes\)
Changes a file's attributes\.

#### Parameters

  - filename : [PyUnicode](PyUnicode.md)

    filename

  - newAttributes : int

    attributes to set


## [wincerapi](wincerapi.md#wincerapi)\.CreateProcess

[PyHANDLE](PyHANDLE.md), [PyHANDLE](PyHANDLE.md), int, int = CreateProcess\(appName, commandLine

, processAttributes

, threadAttributes

, bInheritHandles

, dwCreationFlags

, newEnvironment

, currentDirectory

, startupinfo

\)
Creates a new process and its primary thread\. The new process executes the specified executable file\.

#### Parameters

  - appName : string

    name of executable module, or None

  - commandLine : string

    command line string, or None

  - processAttributes : [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    process security attributes, or None

  - threadAttributes : [PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    thread security attributes, or None

  - bInheritHandles : int

    handle inheritance flag

  - dwCreationFlags : int

    creation flags

  - newEnvironment : None

    A dictionary of stringor Unicode pairs to define the environment for the process, or None to inherit the current environment\.

  - currentDirectory : string

    current directory name, or None

  - startupinfo : [PySTARTUPINFO](PySTARTUPINFO.md)

    a STARTUPINFO object that specifies how the main window for the new process should appear\.

#### Comments

The result is a tuple of \(hProcess, hThread, dwProcessId, dwThreadId\)


## [wincerapi](wincerapi.md#wincerapi)\.FindFiles

list = FindFiles\(fileSpec\)
Retrieves a list of matching filenames on the CE device\.  An interface to the API CeFindFirstFile/CeFindNextFile functions\.

#### Parameters

  - fileSpec : [PyUnicode](PyUnicode.md)

    A string that specifies a valid directory or path and filename, which can contain wildcard characters \(\* and ?\)\.

#### Win32 API References

  - Search for CeFindFirstFile at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CeFindFirstFile.md), [google](http://www.google.com/search?q=CeFindFirstFile.md) or [google groups](http://groups.google.com/groups?q=CeFindFirstFile.md)\.

  - Search for FindNextFile at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextFile.md), [google](http://www.google.com/search?q=FindNextFile.md) or [google groups](http://groups.google.com/groups?q=FindNextFile.md)\.

  - Search for CloseHandle at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CloseHandle.md), [google](http://www.google.com/search?q=CloseHandle.md) or [google groups](http://groups.google.com/groups?q=CloseHandle.md)\.

#### Return Value
The return value is a list of tuples, in the same format as the WIN32\_FIND\_DATA structure:

#### Items

  - \[0\] int : attributes

    File Attributes\.  A combination of the win32com\.FILE\_ATTRIBUTE\_\* flags\.

  - \[1\] [PyTime](PyTime.md) : createTime

    File creation time\.

  - \[2\] [PyTime](PyTime.md) : accessTime

    File access time\.

  - \[3\] [PyTime](PyTime.md) : writeTime

    Time of last file write

  - \[4\] int : nFileSizeHigh

    high order word of file size\.

  - \[5\] int : nFileSizeLow

    low order word of file size\.

  - \[6\] int : OID

    The object identifier for the file

  - \[7\] int : zero

    Filler

  - \[8\] string : fileName

    The name of the file\.

  - \[9\] None : altName

    Always None


## [wincerapi](wincerapi.md#wincerapi)\.WriteFile

int, int = WriteFile\(hFile, data

\)
Writes a string to a file

#### Parameters

  - hFile : [PyHANDLE](PyHANDLE.md)/int

    Handle to the file

  - data : string

    The data to write\.

#### Return Value
The result is a tuple of \(errCode, nBytesWritten\)\. 

errCode will always be zero \(until overlapped IO is supported\!\)