
## [win32api](#win32api.md#win32api).AbortSystemShutdown

 **AbortSystemShutdown( _computerName_ ** )
Aborts a system shutdown

#### Parameters


	 _computerName_ : string/[PyUnicode](#PyUnicode.md#PyUnicode)

	Specifies the name of the computer where the shutdown is to be stopped.

#### Win32 API References


	Search for _AbortSystemShutdown_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown),[google](#http://www.google.com/search?q=AbortSystemShutdown.md#http://www.google.com/search?q=AbortSystemShutdown)or[google groups](#http://groups.google.com/groups?q=AbortSystemShutdown.md#http://groups.google.com/groups?q=AbortSystemShutdown).

## [win32api](#win32api.md#win32api).Apply

object = **Apply( _exceptionHandler_  _, func_  _, args_ ** )
Calls a Python function, but traps Win32 exceptions.

#### Parameters


	 _exceptionHandler_ : object

	An object which will be called when a win32 exception occurs.

	 _func_ : object

	The function call call under the protection of the Win32 exception handler.

	 _args_ : tuple

	Args for the function.

#### Comments
Calls the specified function in a manner similar to 

the built-in function apply(), but allows Win32 exceptions 

to be handled by Python.  If a Win32 exception occurs calling 

the function, the specified exceptionHandler is called, and its 

return value determines the action taken.


## [win32api](#win32api.md#win32api).Beep

 **Beep( _freq_  _, dur_ ** )
Generates simple tones on the speaker.

#### Parameters


	 _freq_ : int

	Specifies the frequency, in hertz, of the sound. This parameter must be in the range 37 through 32,767 (0x25 through 0x7FFF).

	 _dur_ : int

	Specifies the duration, in milliseconds, of the sound.~ 

One value has a special meaning: If dwDuration is  - 1, the function 

operates asynchronously and produces sound until called again.

#### Win32 API References


	Search for _Beep_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=Beep.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=Beep),[google](#http://www.google.com/search?q=Beep.md#http://www.google.com/search?q=Beep)or[google groups](#http://groups.google.com/groups?q=Beep.md#http://groups.google.com/groups?q=Beep).

## [win32api](#win32api.md#win32api).BeginUpdateResource

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **BeginUpdateResource( _filename_  _, delete_ ** )
Begins an update cycle for a PE file.

#### Parameters


	 _filename_ : string

	File in which to update resources.

	 _delete_ : int

	Flag to indicate that all existing resources should be deleted.

## [win32api](#win32api.md#win32api).ChangeDisplaySettingsEx

int = **ChangeDisplaySettingsEx( _DeviceName_  _, DevMode_  _, Flags_ ** )
Changes video mode for specified display

#### Parameters


	 _DeviceName=None_ : str

	Name of device as returned by[win32api::EnumDisplayDevices](#win32api.md#win32api_EnumDisplayDevices_meth), use None for default display device

	 _DevMode=None_ :[PyDEVMODE](#PyDEVMODE.md#PyDEVMODE)

	A PyDEVMODE object as returned from[win32api::EnumDisplaySettings](#win32api.md#win32api_EnumDisplaySettings_meth), or None to reset to default settings from registry

	 _Flags=0_ : int

	One of the win32con.CDS_* constants, or 0

#### Comments
Accepts keyword arguments

#### Return Value
Returns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

## [win32api](#win32api.md#win32api).ChangeDisplaySettings

int = **ChangeDisplaySettings( _DevMode_  _, Flags_ ** )
Changes video mode for default display

#### Parameters


	 _DevMode_ :[PyDEVMODE](#PyDEVMODE.md#PyDEVMODE)

	A PyDEVMODE object as returned from EnumDisplaySettings, or None to reset to default settings from registry

	 _Flags_ : int

	One of the win32con.CDS_* constants, or 0

#### Return Value
Returns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

## [win32api](#win32api.md#win32api).ClipCursor

 **ClipCursor( _left, top, right, bottom_ ** )
Confines the cursor to a rectangular area on the screen.

#### Parameters


	 _left, top, right, bottom_ : (int, int, int, int)

	contains the screen coordinates of the upper-left and lower-right corners of the confining rectangle. If this parameter is omitted or (0,0,0,0), the cursor is free to move anywhere on the screen.

#### Win32 API References


	Search for _ClipCursor_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ClipCursor.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ClipCursor),[google](#http://www.google.com/search?q=ClipCursor.md#http://www.google.com/search?q=ClipCursor)or[google groups](#http://groups.google.com/groups?q=ClipCursor.md#http://groups.google.com/groups?q=ClipCursor).

## [win32api](#win32api.md#win32api).CloseHandle

 **CloseHandle( _handle_ ** )
Closes an open handle.

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)/int

	A previously opened handle.

## [win32api](#win32api.md#win32api).CopyFile

 **CopyFile( _src_  _, dest_  _, bFailOnExist_ ** )
Copies an existing file to a new file

#### Parameters


	 _src_ : string[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of an existing file.

	 _dest_ : string/[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of file to copy to.

	 _bFailOnExist=0_ : int

	Indicates if the operation should fail if the file exists.

#### Win32 API References


	Search for _CopyFile_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CopyFile.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CopyFile),[google](#http://www.google.com/search?q=CopyFile.md#http://www.google.com/search?q=CopyFile)or[google groups](#http://groups.google.com/groups?q=CopyFile.md#http://groups.google.com/groups?q=CopyFile).

## [win32api](#win32api.md#win32api).DebugBreak

 **DebugBreak(** )
Breaks into the C debugger

#### Win32 API References


	Search for _DebugBreak_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DebugBreak.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DebugBreak),[google](#http://www.google.com/search?q=DebugBreak.md#http://www.google.com/search?q=DebugBreak)or[google groups](#http://groups.google.com/groups?q=DebugBreak.md#http://groups.google.com/groups?q=DebugBreak).

## [win32api](#win32api.md#win32api).DeleteFile

 **DeleteFile( _fileName_ ** )
Deletes the specified file.

#### Parameters


	 _fileName_ : string/[PyUnicode](#PyUnicode.md#PyUnicode)

	File to delete.

#### Win32 API References


	Search for _DeleteFile_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteFile.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteFile),[google](#http://www.google.com/search?q=DeleteFile.md#http://www.google.com/search?q=DeleteFile)or[google groups](#http://groups.google.com/groups?q=DeleteFile.md#http://groups.google.com/groups?q=DeleteFile).

## [win32api](#win32api.md#win32api).DragFinish

 **DragFinish( _hDrop_ ** )
Releases the memory stored by Windows for the filenames.

#### Parameters


	 _hDrop_ : int

	Handle identifying the structure containing the file names.

#### Win32 API References


	Search for _DragFinish_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DragFinish.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DragFinish),[google](#http://www.google.com/search?q=DragFinish.md#http://www.google.com/search?q=DragFinish)or[google groups](#http://groups.google.com/groups?q=DragFinish.md#http://groups.google.com/groups?q=DragFinish).

## [win32api](#win32api.md#win32api).DragQueryFile

string/int = **DragQueryFile( _hDrop_  _, fileNum_ ** )
Retrieves the file names of dropped files.

#### Parameters


	 _hDrop_ : int

	Handle identifying the structure containing the file names.

	 _fileNum=0xFFFFFFFF_ : int

	Specifies the index of the file to query.

#### Win32 API References


	Search for _DragQueryFile_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DragQueryFile.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DragQueryFile),[google](#http://www.google.com/search?q=DragQueryFile.md#http://www.google.com/search?q=DragQueryFile)or[google groups](#http://groups.google.com/groups?q=DragQueryFile.md#http://groups.google.com/groups?q=DragQueryFile).

#### Return Value
If the fileNum parameter is 0xFFFFFFFF (the default) then the return value 

is an integer with the count of files dropped.  If fileNum is between 0 and Count, 

the return value is a string containing the filename.
If an error occurs, and exception is raised.

## [win32api](#win32api.md#win32api).DuplicateHandle

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **DuplicateHandle( _hSourceProcess_  _, hSource_  _, hTargetProcessHandle_  _, desiredAccess_  _, bInheritHandle_  _, options_ ** )
Duplicates a handle.

#### Parameters


	 _hSourceProcess_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Identifies the process containing the handle to duplicate.

	 _hSource_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Identifies the handle to duplicate. This is an open object handle that is valid in the context of the source process.

	 _hTargetProcessHandle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Identifies the process that is to receive the duplicated handle. The handle must have PROCESS_DUP_HANDLE access.

	 _desiredAccess_ : int

	Specifies the access requested for the new handle. This parameter is ignored if the dwOptions parameter specifies the DUPLICATE_SAME_ACCESS flag. Otherwise, the flags that can be specified depend on the type of object whose handle is being duplicated. For the flags that can be specified for each object type, see the following Remarks section. Note that the new handle can have more access than the original handle.

	 _bInheritHandle_ : int

	Indicates whether the handle is inheritable. If TRUE, the duplicate handle can be inherited by new processes created by the target process. If FALSE, the new handle cannot be inherited.

	 _options_ : int

	Specifies optional actions. This parameter can be zero, or any combination of the following flags
DUPLICATE_CLOSE_SOURCEloses the source handle. This occurs regardless of any error status returned.DUPLICATE_SAME_ACCESSIgnores the dwDesiredAccess parameter. The duplicate handle has the same access as the source handle.
#### Comments
When duplicating a handle for a different process, you should either keep a 

reference to the returned PyHANDLE, or call .Detach() on it to prevent it 

from being closed prematurely.

## [win32api](#win32api.md#win32api).EndUpdateResource

 **EndUpdateResource( _handle_  _, discard_ ** )
Ends a resource update cycle of a PE file.

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The update-file handle.

	 _discard_ : int

	Flag to discard all writes.

## [win32api](#win32api.md#win32api).EnumDisplayDevices

[PyDISPLAY_DEVICE](#PyDISPLAY.md#PyDISPLAYDEVICE)= **EnumDisplayDevices( _Device_  _, DevNum_  _, Flags_ ** )
Obtain information about the display devices in a system

#### Parameters


	 _Device=None_ : string

	Name of device, use None to obtain information for the display adapter(s) on the machine, based on DevNum

	 _DevNum=0_ : int

	Index of device of interest, starting with zero

	 _Flags=0_ : int

	Reserved, use 0 if passed in

#### Comments
Accepts keyword arguments

## [win32api](#win32api.md#win32api).EnumDisplayMonitors

list = **EnumDisplayMonitors( _hdc_  _, rcClip_ ** )
Lists display monitors for a given device context and area

#### Parameters


	 _hdc=None_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to device context, use None for virtual desktop

	 _rcClip=None_ :[PyRECT](#PyRECT.md#PyRECT)

	Clipping rectangle, can be None

#### Comments
Accepts keyword arguments

#### Return Value
Returns a sequence of tuples.  For each monitor found, returns a handle to the monitor, 

device context handle, and intersection rectangle: (hMonitor, hdcMonitor,[PyRECT](#PyRECT.md#PyRECT))

## [win32api](#win32api.md#win32api).EnumDisplaySettingsEx

[PyDEVMODE](#PyDEVMODE.md#PyDEVMODE)= **EnumDisplaySettingsEx( _DeviceName_  _, ModeNum_  _, Flags_ ** )
Lists available modes for a display device, with optional flags

#### Parameters


	 _DeviceName=None_ : string

	Name of device as returned by[win32api::EnumDisplayDevices](#win32api.md#win32api_EnumDisplayDevices_meth). Can be None for default display

	 _ModeNum_ : int

	Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS

	 _Flags=0_ : int

	EDS_RAWMODE (2) is only defined flag

#### Comments
Accepts keyword arguments

## [win32api](#win32api.md#win32api).EnumDisplaySettings

[PyDEVMODE](#PyDEVMODE.md#PyDEVMODE)= **EnumDisplaySettings( _DeviceName_  _, ModeNum_ ** )
List available modes for specified display device

#### Parameters


	 _DeviceName=None_ : string

	Name of device as returned by[win32api::EnumDisplayDevices](#win32api.md#win32api_EnumDisplayDevices_meth), use None for default display device

	 _ModeNum=0_ : int

	Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS

#### Comments
Accepts keyword arguments

## [win32api](#win32api.md#win32api).EnumResourceLanguages

[int,...] = **EnumResourceLanguages( _hmodule_  _, lpType_  _, lpName_ ** )
List languages for a resource

#### Parameters


	 _hmodule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to the module that contains resource

	 _lpType_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	Resource type, can be string or integer

	 _lpName_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	Resource name, can be string or integer

## [win32api](#win32api.md#win32api).EnumResourceNames

[string, ...] = **EnumResourceNames( _hmodule_  _, resType_ ** )
Enumerates all the resources of the specified type from the nominated file.

#### Parameters


	 _hmodule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle to the module to enumerate.

	 _resType_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	The type of resource to enumerate. (win32con.RT_*). 

If passed as a string, form is '#' sign followed by decimal number. eg RT_ANICURSOR would be '#21'

#### Return Value
The result is a list of string or integers, one for each resource enumerated.

## [win32api](#win32api.md#win32api).EnumResourceTypes

[[PyUnicode](#PyUnicode.md#PyUnicode),...] = **EnumResourceTypes( _hmodule_ ** )
Return name or integer id of all resource types contained in module

#### Parameters


	 _hmodule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle to the module to enumerate.

## [win32api](#win32api.md#win32api).ExitWindowsEx

 **ExitWindowsEx( _flags_  _, reserved_ ** )
either logs off the current user, shuts down the system, or shuts down and restarts the system.

#### Parameters


	 _flags_ : int

	The shutdown operation

	 _reserved=0_ : int

	

#### Comments
It sends the WM_QUERYENDSESSION message to all applications to determine if they can be terminated.

#### Win32 API References


	Search for _AbortSystemShutdown_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown),[google](#http://www.google.com/search?q=AbortSystemShutdown.md#http://www.google.com/search?q=AbortSystemShutdown)or[google groups](#http://groups.google.com/groups?q=AbortSystemShutdown.md#http://groups.google.com/groups?q=AbortSystemShutdown).

## [win32api](#win32api.md#win32api).ExitWindows

 **ExitWindows( _reserved1_  _, reserved2_ ** )
Logs off the current user

#### Parameters


	 _reserved1=0_ : int

	

	 _reserved2=0_ : int

	

#### Win32 API References


	Search for _AbortSystemShutdown_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown),[google](#http://www.google.com/search?q=AbortSystemShutdown.md#http://www.google.com/search?q=AbortSystemShutdown)or[google groups](#http://groups.google.com/groups?q=AbortSystemShutdown.md#http://groups.google.com/groups?q=AbortSystemShutdown).

## [win32api](#win32api.md#win32api).ExpandEnvironmentStrings

string = **ExpandEnvironmentStrings( _in_ ** )
Expands environment-variable strings and replaces them with their defined values.

#### Parameters


	 _in_ : string

	String to expand

#### Win32 API References


	Search for _ExpandEnvironmentStrings_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ExpandEnvironmentStrings.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ExpandEnvironmentStrings),[google](#http://www.google.com/search?q=ExpandEnvironmentStrings.md#http://www.google.com/search?q=ExpandEnvironmentStrings)or[google groups](#http://groups.google.com/groups?q=ExpandEnvironmentStrings.md#http://groups.google.com/groups?q=ExpandEnvironmentStrings).

## [win32api](#win32api.md#win32api).FindCloseChangeNotification

 **FindCloseChangeNotification( _handle_ ** )
Closes the change notification handle.

#### Parameters


	 _handle_ : int

	The handle returned from[win32api::FindFirstChangeNotification](#win32api.md#win32api_FindFirstChangeNotification_meth)

## [win32api](#win32api.md#win32api).FindExecutable

(int, string) = **FindExecutable( _filename_  _, dir_ ** )
Retrieves the name and handle of the executable (.EXE) file associated with the specified filename.

#### Parameters


	 _filename_ : string

	A file name.  This can be either a document or executable file.

	 _dir_ : string

	The default directory.

#### Comments
The function will raise an exception if it fails.

#### Win32 API References


	Search for _FindExecutable_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindExecutable.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindExecutable),[google](#http://www.google.com/search?q=FindExecutable.md#http://www.google.com/search?q=FindExecutable)or[google groups](#http://groups.google.com/groups?q=FindExecutable.md#http://groups.google.com/groups?q=FindExecutable).

#### Return Value
The return value is a tuple of (integer, string)
The integer is the instance handle of the executable file associated 

with the specified filename. (This handle could also be the handle of 

a dynamic data exchange [DDE] server application.)
The may contain the path to the DDE server started if no server responds to a request to initiate a DDE conversation.

## [win32api](#win32api.md#win32api).FindFiles

list = **FindFiles( _fileSpec_ ** )
Retrieves a list of matching filenames.  An interface to the API FindFirstFile/FindNextFile/Find close functions.

#### Parameters


	 _fileSpec_ : string

	A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

#### Win32 API References


	Search for _FindFirstFile_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstFile.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstFile),[google](#http://www.google.com/search?q=FindFirstFile.md#http://www.google.com/search?q=FindFirstFile)or[google groups](#http://groups.google.com/groups?q=FindFirstFile.md#http://groups.google.com/groups?q=FindFirstFile).

	Search for _FindNextFile_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextFile.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextFile),[google](#http://www.google.com/search?q=FindNextFile.md#http://www.google.com/search?q=FindNextFile)or[google groups](#http://groups.google.com/groups?q=FindNextFile.md#http://groups.google.com/groups?q=FindNextFile).

	Search for _FindClose_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindClose.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindClose),[google](#http://www.google.com/search?q=FindClose.md#http://www.google.com/search?q=FindClose)or[google groups](#http://groups.google.com/groups?q=FindClose.md#http://groups.google.com/groups?q=FindClose).

#### Return Value
Returns a sequence of[WIN32_FIND_DATA](#WIN32.md#WIN32FIND_DATA)tuples

## [win32api](#win32api.md#win32api).FindFirstChangeNotification

int = **FindFirstChangeNotification( _pathName_  _, bSubDirs_  _, filter_ ** )
Creates a change notification handle and sets up initial change notification filter conditions.

#### Parameters


	 _pathName_ : string

	Specifies the path of the directory to watch.

	 _bSubDirs_ : int

	Specifies whether the function will monitor the directory or the directory tree. If this parameter is TRUE, the function monitors the directory tree rooted at the specified directory; if it is FALSE, it monitors only the specified directory

	 _filter_ : int

	Specifies the filter conditions that satisfy a change notification wait. This parameter can be one or more of the following values:

 **Value**  **Meaning** FILE_NOTIFY_CHANGE_FILE_NAMEAny file name change in the watched directory or subtree causes a change notification wait operation to return. Changes include renaming, creating, or deleting a file name.FILE_NOTIFY_CHANGE_DIR_NAMEAny directory-name change in the watched directory or subtree causes a change notification wait operation to return. Changes include creating or deleting a directory.FILE_NOTIFY_CHANGE_ATTRIBUTESAny attribute change in the watched directory or subtree causes a change notification wait operation to return.FILE_NOTIFY_CHANGE_SIZEAny file-size change in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change in file size only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.FILE_NOTIFY_CHANGE_LAST_WRITEAny change to the last write-time of files in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change to the last write-time only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.FILE_NOTIFY_CHANGE_SECURITYAny security-descriptor change in the watched directory or subtree causes a change notification wait operation to return
#### Return Value
Although the result is a handle, the handle can not be closed via CloseHandle() - therefore a PyHandle object is not used.

## [win32api](#win32api.md#win32api).FindNextChangeNotification

 **FindNextChangeNotification( _handle_ ** )
Requests that the operating system signal a change notification handle the next time it detects an appropriate change.

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle returned from[win32api::FindFirstChangeNotification](#win32api.md#win32api_FindFirstChangeNotification_meth)

## [win32api](#win32api.md#win32api).FormatMessageW

[PyUnicode](#PyUnicode.md#PyUnicode)= **FormatMessageW( _errCode_ ** )
Returns an error message from the system error file.

#### Parameters


	 _errCode=0_ : int

	The error code to return the message for,  If this value is 0, 

then GetLastError() is called to determine the error code.

#### Alternative Parameters


	 _flags_ 

	Flags for the call.  Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.

	 _source_ 

	The source object.  If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int or[PyHANDLE](#PyHANDLE.md#PyHANDLE); 

if flags contain FORMAT_MESSAGE_FROM_STRING it should be a unicode string; 

otherwise it is ignored.

	 _messageId_ 

	The message ID.

	 _languageID_ 

	The language ID.

	 _inserts_ 

	The string inserts to insert.

#### Win32 API References


	Search for _GetLastError_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError),[google](#http://www.google.com/search?q=GetLastError.md#http://www.google.com/search?q=GetLastError)or[google groups](#http://groups.google.com/groups?q=GetLastError.md#http://groups.google.com/groups?q=GetLastError).

	Search for _FormatMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FormatMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FormatMessage),[google](#http://www.google.com/search?q=FormatMessage.md#http://www.google.com/search?q=FormatMessage)or[google groups](#http://groups.google.com/groups?q=FormatMessage.md#http://groups.google.com/groups?q=FormatMessage).

## [win32api](#win32api.md#win32api).FormatMessage

string = **FormatMessage( _errCode_ ** )
Returns an error message from the system error file.

#### Parameters


	 _errCode=0_ : int

	The error code to return the message for,  If this value is 0, then GetLastError() is called to determine the error code.

#### Alternative Parameters


	 _flags_ 

	Flags for the call.  Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.

	 _source_ 

	The source object.  If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int; 

if flags contain FORMAT_MESSAGE_FROM_STRING it should be a string containing the error msg; 

otherwise it is ignored.

	 _messageId_ 

	The message ID.

	 _languageID_ 

	The language ID.

	 _inserts_ 

	The string inserts to insert.

#### Win32 API References


	Search for _GetLastError_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError),[google](#http://www.google.com/search?q=GetLastError.md#http://www.google.com/search?q=GetLastError)or[google groups](#http://groups.google.com/groups?q=GetLastError.md#http://groups.google.com/groups?q=GetLastError).

	Search for _FormatMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FormatMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FormatMessage),[google](#http://www.google.com/search?q=FormatMessage.md#http://www.google.com/search?q=FormatMessage)or[google groups](#http://groups.google.com/groups?q=FormatMessage.md#http://groups.google.com/groups?q=FormatMessage).

## [win32api](#win32api.md#win32api).FreeLibrary

 **FreeLibrary( _hModule_ ** )
Decrements the reference count of the loaded dynamic-link library (DLL) module.

#### Parameters


	 _hModule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Specifies the handle to the module.

#### Win32 API References


	Search for _FreeLibrary_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FreeLibrary.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FreeLibrary),[google](#http://www.google.com/search?q=FreeLibrary.md#http://www.google.com/search?q=FreeLibrary)or[google groups](#http://groups.google.com/groups?q=FreeLibrary.md#http://groups.google.com/groups?q=FreeLibrary).

## [win32api](#win32api.md#win32api).GenerateConsoleCtrlEvent

int = **GenerateConsoleCtrlEvent( _controlEvent_  _, processGroupId_ ** )
Send a specified signal to a console process group that shares the console associated with the calling process.

#### Parameters


	 _controlEvent_ : int

	Signal to generate.

	 _processGroupId_ : int

	Process group to get signal.

#### Win32 API References


	Search for _GenerateConsoleCtrlEvent_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GenerateConsoleCtrlEvent.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GenerateConsoleCtrlEvent),[google](#http://www.google.com/search?q=GenerateConsoleCtrlEvent.md#http://www.google.com/search?q=GenerateConsoleCtrlEvent)or[google groups](#http://groups.google.com/groups?q=GenerateConsoleCtrlEvent.md#http://groups.google.com/groups?q=GenerateConsoleCtrlEvent).

## [win32api](#win32api.md#win32api).GetAsyncKeyState

int = **GetAsyncKeyState( _key_ ** )
Retrieves the status of the specified key.

#### Parameters


	 _key_ : int

	Specifies one of 256 possible virtual-key codes.

#### Comments
An application can use the virtual-key code constants win32con.VK_SHIFT, 

win32con.VK_CONTROL, and win32con.VK_MENU as values for the key parameter. 

This gives the state of the SHIFT, CTRL, or ALT keys without distinguishing 

between left and right. An application can also use the following virtual-key 

code constants as values for key to distinguish between the left and 

right instances of those keys:
win32con.VK_LSHIFT
win32con.VK_RSHIFT
win32con.VK_LCONTROL
win32con.VK_RCONTROL
win32con.VK_LMENU
win32con.VK_RMENU
The GetAsyncKeyState method works with mouse buttons. However, it checks on 

the state of the physical mouse buttons, not on the logical mouse buttons that 

the physical buttons are mapped to.

#### Win32 API References


	Search for _GetAsyncKeyState_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetAsyncKeyState.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetAsyncKeyState),[google](#http://www.google.com/search?q=GetAsyncKeyState.md#http://www.google.com/search?q=GetAsyncKeyState)or[google groups](#http://groups.google.com/groups?q=GetAsyncKeyState.md#http://groups.google.com/groups?q=GetAsyncKeyState).

#### Return Value
The return value specifies whether the key was pressed since the last 

call to GetAsyncKeyState, and whether the key is currently up or down. If 

the most significant bit is set, the key is down, and if the least significant 

bit is set, the key was pressed after the previous call to GetAsyncKeyState.
The return value is zero if a window in another thread or process currently has the 

keyboard focus.

## [win32api](#win32api.md#win32api).GetCommandLine

string = **GetCommandLine(** )
Retrieves the current application's command line.

#### Win32 API References


	Search for _GetCommandLine_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCommandLine.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCommandLine),[google](#http://www.google.com/search?q=GetCommandLine.md#http://www.google.com/search?q=GetCommandLine)or[google groups](#http://groups.google.com/groups?q=GetCommandLine.md#http://groups.google.com/groups?q=GetCommandLine).

## [win32api](#win32api.md#win32api).GetComputerNameEx

string = **GetComputerNameEx( _NameType_ ** )
Retrieves a NetBIOS or DNS name associated with the local computer

#### Parameters


	 _NameType_ : int

	Value from COMPUTER_NAME_FORMAT enum, win32con.ComputerName*

#### Win32 API References


	Search for _GetComputerNameEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerNameEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerNameEx),[google](#http://www.google.com/search?q=GetComputerNameEx.md#http://www.google.com/search?q=GetComputerNameEx)or[google groups](#http://groups.google.com/groups?q=GetComputerNameEx.md#http://groups.google.com/groups?q=GetComputerNameEx).

## [win32api](#win32api.md#win32api).GetComputerName

string = **GetComputerName(** )
Returns the local computer name

#### Win32 API References


	Search for _GetComputerName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerName),[google](#http://www.google.com/search?q=GetComputerName.md#http://www.google.com/search?q=GetComputerName)or[google groups](#http://groups.google.com/groups?q=GetComputerName.md#http://groups.google.com/groups?q=GetComputerName).

## [win32api](#win32api.md#win32api).GetComputerObjectName

string = **GetComputerObjectName( _NameFormat_ ** )
Retrieves the local computer's name in a specified format.

#### Parameters


	 _NameFormat_ : int

	EXTENDED_NAME_FORMAT value, win32con.Name*

#### Win32 API References


	Search for _GetComputerObjectName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerObjectName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerObjectName),[google](#http://www.google.com/search?q=GetComputerObjectName.md#http://www.google.com/search?q=GetComputerObjectName)or[google groups](#http://groups.google.com/groups?q=GetComputerObjectName.md#http://groups.google.com/groups?q=GetComputerObjectName).

## [win32api](#win32api.md#win32api).GetConsoleTitle

string = **GetConsoleTitle(** )
Returns the title for the current console.

## [win32api](#win32api.md#win32api).GetCurrentProcessId

int = **GetCurrentProcessId(** )
Returns the thread ID for the current process.

#### Win32 API References


	Search for _GetCurrentProcessId_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentProcessId.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentProcessId),[google](#http://www.google.com/search?q=GetCurrentProcessId.md#http://www.google.com/search?q=GetCurrentProcessId)or[google groups](#http://groups.google.com/groups?q=GetCurrentProcessId.md#http://groups.google.com/groups?q=GetCurrentProcessId).

## [win32api](#win32api.md#win32api).GetCurrentProcess

int = **GetCurrentProcess(** )
Returns a pseudohandle for the current process.

#### Comments
A pseudohandle is a special constant that is interpreted as the current thread handle. The calling thread can use this handle to specify itself whenever a thread handle is required. Pseudohandles are not inherited by child processes. 

The method[win32api::DuplicateHandle](#win32api.md#win32api_DuplicateHandle_meth)can be used to create a handle that other threads and processes can use. 

As this handle can not be closed, and integer is returned rather than 

a[PyHANDLE](#PyHANDLE.md#PyHANDLE)object, which would attempt to automatically close the handle.

#### Win32 API References


	Search for _GetCurrentProcess_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentProcess.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentProcess),[google](#http://www.google.com/search?q=GetCurrentProcess.md#http://www.google.com/search?q=GetCurrentProcess)or[google groups](#http://groups.google.com/groups?q=GetCurrentProcess.md#http://groups.google.com/groups?q=GetCurrentProcess).

## [win32api](#win32api.md#win32api).GetCurrentThreadId

int = **GetCurrentThreadId(** )
Returns the thread ID for the current thread.

#### Win32 API References


	Search for _GetCurrentThreadId_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentThreadId.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentThreadId),[google](#http://www.google.com/search?q=GetCurrentThreadId.md#http://www.google.com/search?q=GetCurrentThreadId)or[google groups](#http://groups.google.com/groups?q=GetCurrentThreadId.md#http://groups.google.com/groups?q=GetCurrentThreadId).

## [win32api](#win32api.md#win32api).GetCurrentThread

int = **GetCurrentThread(** )
Returns a pseudohandle for the current thread.

#### Comments
A pseudohandle is a special constant that is interpreted as the current thread handle. The calling thread can use this handle to specify itself whenever a thread handle is required. Pseudohandles are not inherited by child processes. 

The method[win32api::DuplicateHandle](#win32api.md#win32api_DuplicateHandle_meth)can be used to create a handle that other threads and processes can use. 

As this handle can not be closed, and integer is returned rather than 

a[PyHANDLE](#PyHANDLE.md#PyHANDLE)object, which would attempt to automatically close the handle.

#### Win32 API References


	Search for _GetCurrentThread_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentThread.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentThread),[google](#http://www.google.com/search?q=GetCurrentThread.md#http://www.google.com/search?q=GetCurrentThread)or[google groups](#http://groups.google.com/groups?q=GetCurrentThread.md#http://groups.google.com/groups?q=GetCurrentThread).

## [win32api](#win32api.md#win32api).GetCursorPos

int, int = **GetCursorPos(** )
Returns the position of the cursor, in screen co-ordinates.

#### Win32 API References


	Search for _GetCursorPos_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCursorPos.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCursorPos),[google](#http://www.google.com/search?q=GetCursorPos.md#http://www.google.com/search?q=GetCursorPos)or[google groups](#http://groups.google.com/groups?q=GetCursorPos.md#http://groups.google.com/groups?q=GetCursorPos).

## [win32api](#win32api.md#win32api).GetDateFormat

string = **GetDateFormat( _locale_  _, flags_  _, time_  _, format_ ** )
Formats a date as a date string for a specified locale. The function formats either a specified date or the local system date.

#### Parameters


	 _locale_ : int

	

	 _flags_ : int

	

	 _time_ :[PyTime](#PyTime.md#PyTime)

	The time to use, or None to use the current time.

	 _format_ : string

	May be None

## [win32api](#win32api.md#win32api).GetDiskFreeSpaceEx

tuple = **GetDiskFreeSpaceEx( _rootPath_ ** )
Retrieves information about the specified disk, including the amount of free space available.

#### Parameters


	 _rootPath_ : string

	Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.

#### Win32 API References


	Search for _GetDiskFreeSpaceEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDiskFreeSpaceEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDiskFreeSpaceEx),[google](#http://www.google.com/search?q=GetDiskFreeSpaceEx.md#http://www.google.com/search?q=GetDiskFreeSpaceEx)or[google groups](#http://groups.google.com/groups?q=GetDiskFreeSpaceEx.md#http://groups.google.com/groups?q=GetDiskFreeSpaceEx).

#### Return Value
The return value is a tuple of 3 integers, containing 

the number of free bytes available 

the total number of bytes available on disk 

the total number of free bytes on disk 

the above values may be less, if user-quotas are in effect
If the function fails, an error is returned.

## [win32api](#win32api.md#win32api).GetDiskFreeSpace

tuple = **GetDiskFreeSpace( _rootPath_ ** )
Retrieves information about the specified disk, including the amount of free space available.

#### Parameters


	 _rootPath_ : string

	Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.

#### Win32 API References


	Search for _GetDiskFreeSpace_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDiskFreeSpace.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDiskFreeSpace),[google](#http://www.google.com/search?q=GetDiskFreeSpace.md#http://www.google.com/search?q=GetDiskFreeSpace)or[google groups](#http://groups.google.com/groups?q=GetDiskFreeSpace.md#http://groups.google.com/groups?q=GetDiskFreeSpace).

#### Return Value
The return value is a tuple of 4 integers, containing 

the number of sectors per cluster, the number of bytes per sector, 

the total number of free clusters on the disk and the total number of clusters on the disk.
If the function fails, an error is returned.

## [win32api](#win32api.md#win32api).GetDllDirectory

[PyUnicode](#PyUnicode.md#PyUnicode)= **GetDllDirectory(** )
Returns the DLL search path

#### Win32 API References


	Search for _GetDllDirectory_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDllDirectory.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDllDirectory),[google](#http://www.google.com/search?q=GetDllDirectory.md#http://www.google.com/search?q=GetDllDirectory)or[google groups](#http://groups.google.com/groups?q=GetDllDirectory.md#http://groups.google.com/groups?q=GetDllDirectory).

## [win32api](#win32api.md#win32api).GetDomainName

string = **GetDomainName(** )
Returns the current domain name

#### Comments
This is a convenience wrapper of the Win32 function LookupAccountSid()

## [win32api](#win32api.md#win32api).GetEnvironmentVariableW

[PyUnicode](#PyUnicode.md#PyUnicode)= **GetEnvironmentVariableW( _Name_ ** )
Retrieves the unicode value of an environment variable.

#### Parameters


	 _Name_ : str

	The variable to retrieve

#### Win32 API References


	Search for _GetEnvironmentVariableW_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetEnvironmentVariableW.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetEnvironmentVariableW),[google](#http://www.google.com/search?q=GetEnvironmentVariableW.md#http://www.google.com/search?q=GetEnvironmentVariableW)or[google groups](#http://groups.google.com/groups?q=GetEnvironmentVariableW.md#http://groups.google.com/groups?q=GetEnvironmentVariableW).

#### Return Value
Returns None if environment variable is not found

## [win32api](#win32api.md#win32api).GetEnvironmentVariable

str = **GetEnvironmentVariable( _variable_ ** )
Retrieves the value of an environment variable.

#### Parameters


	 _variable_ : str

	The variable to get

#### Win32 API References


	Search for _GetEnvironmentVariable_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetEnvironmentVariable.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetEnvironmentVariable),[google](#http://www.google.com/search?q=GetEnvironmentVariable.md#http://www.google.com/search?q=GetEnvironmentVariable)or[google groups](#http://groups.google.com/groups?q=GetEnvironmentVariable.md#http://groups.google.com/groups?q=GetEnvironmentVariable).

#### Return Value
Returns None if environment variable is not found

## [win32api](#win32api.md#win32api).GetFileAttributes

int = **GetFileAttributes( _pathName_ ** )
Retrieves the attributes for the named file.

#### Parameters


	 _pathName_ : string

	The name of the file whose attributes are to be returned. 

If this param is a unicode object, GetFileAttributesW is called.

#### Win32 API References


	Search for _GetFileAttributes_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributes.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributes),[google](#http://www.google.com/search?q=GetFileAttributes.md#http://www.google.com/search?q=GetFileAttributes)or[google groups](#http://groups.google.com/groups?q=GetFileAttributes.md#http://groups.google.com/groups?q=GetFileAttributes).

	Search for _GetFileAttributesW_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributesW.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributesW),[google](#http://www.google.com/search?q=GetFileAttributesW.md#http://www.google.com/search?q=GetFileAttributesW)or[google groups](#http://groups.google.com/groups?q=GetFileAttributesW.md#http://groups.google.com/groups?q=GetFileAttributesW).

#### Return Value
The return value is a combination of the win32con.FILE_ATTRIBUTE_* constants.
An exception is raised on failure.

## [win32api](#win32api.md#win32api).GetFileVersionInfo

 **GetFileVersionInfo( _Filename_  _, SubBlock_ ** )
Retrieve version info for specified file

#### Parameters


	 _Filename_ : string/unicode

	File to query for version info

	 _SubBlock_ : string/unicode

	Information to return: \\ for VS_FIXEDFILEINFO, \\VarFileInfo\\Translation for languages/codepages available

## [win32api](#win32api.md#win32api).GetFocus

int = **GetFocus(** )
Retrieves the handle of the keyboard focus window associated with the thread that called the method.

#### Win32 API References


	Search for _GetFocus_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFocus.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFocus),[google](#http://www.google.com/search?q=GetFocus.md#http://www.google.com/search?q=GetFocus)or[google groups](#http://groups.google.com/groups?q=GetFocus.md#http://groups.google.com/groups?q=GetFocus).

#### Return Value
The method raises an exception if no window with the focus exists.

## [win32api](#win32api.md#win32api).GetFullPathName

string = **GetFullPathName( _fileName_ ** )
Returns the full path of a (possibly relative) path

#### Parameters


	 _fileName_ : string

	The file name.

#### Comments
Please use[win32file::GetFullPathName](#win32file.md#win32file_GetFullPathName_meth)instead - it has better Unicode semantics.

## [win32api](#win32api.md#win32api).GetHandleInformation

int = **GetHandleInformation( _Object_ ** )
Retrieves a handle's flags.

#### Parameters


	 _Object_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to an object

#### Comments
Not available on Win98/Me

#### Return Value
Returns a combination of HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE

## [win32api](#win32api.md#win32api).GetKeyState

int = **GetKeyState( _key_ ** )
Retrieves the status of the specified key.

#### Parameters


	 _key_ : int

	Specifies a virtual key. If the desired virtual key is a letter or digit (A through Z, a through z, or 0 through 9), key must be set to the ASCII value of that character. For other keys, it must be a virtual-key code.

#### Comments
The key status returned from this function changes as a given thread 

reads key messages from its message queue. The status does not reflect the 

interrupt-level state associated with the hardware. Use the[win32api::GetAsyncKeyState](#win32api.md#win32api_GetAsyncKeyState_meth)method to retrieve that information.

#### Win32 API References


	Search for _GetKeyState_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetKeyState.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetKeyState),[google](#http://www.google.com/search?q=GetKeyState.md#http://www.google.com/search?q=GetKeyState)or[google groups](#http://groups.google.com/groups?q=GetKeyState.md#http://groups.google.com/groups?q=GetKeyState).

#### Return Value
The return value specifies the status of 

the given virtual key. If the high-order bit is 1, the key is down; 

otherwise, it is up. If the low-order bit is 1, the key is toggled. 

A key, such as the CAPS LOCK key, is toggled if it is turned on. 

The key is off and untoggled if the low-order bit is 0. A toggle key's 

indicator light (if any) on the keyboard will be on when the key is 

toggled, and off when the key is untoggled.

## [win32api](#win32api.md#win32api).GetKeyboardLayoutList

(int,..) = **GetKeyboardLayoutList(** )
Returns a sequence of all locale ids currently loaded

## [win32api](#win32api.md#win32api).GetKeyboardLayoutName

int = **GetKeyboardLayoutName(** )
Retrieves the name of the active input locale identifier (formerly called the keyboard layout).

## [win32api](#win32api.md#win32api).GetKeyboardLayout

int = **GetKeyboardLayout( _threadId_ ** )
retrieves the active input locale identifier (formerly called the keyboard layout) for the specified thread.

#### Parameters


	 _threadId=0_ : int

	

#### Comments
If the idThread parameter is zero, the input locale identifier for the active thread is returned.

## [win32api](#win32api.md#win32api).GetKeyboardState

string = **GetKeyboardState(** )
Retrieves the status of the 256 virtual keys on the keyboard.

#### Win32 API References


	Search for _GetKeyboardState_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetKeyboardState.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetKeyboardState),[google](#http://www.google.com/search?q=GetKeyboardState.md#http://www.google.com/search?q=GetKeyboardState)or[google groups](#http://groups.google.com/groups?q=GetKeyboardState.md#http://groups.google.com/groups?q=GetKeyboardState).

#### Return Value
The return value is a string of exactly 256 characters. 

Each character represents the bitmask for a key - see the Win32 

documentation for more details.

## [win32api](#win32api.md#win32api).GetLastError

int = **GetLastError(** )
Retrieves the calling thread's last error code value.

#### Win32 API References


	Search for _GetLastError_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError),[google](#http://www.google.com/search?q=GetLastError.md#http://www.google.com/search?q=GetLastError)or[google groups](#http://groups.google.com/groups?q=GetLastError.md#http://groups.google.com/groups?q=GetLastError).

## [win32api](#win32api.md#win32api).GetLastInputInfo

int = **GetLastInputInfo(** )
Returns time of last input event in tick count

#### Win32 API References


	Search for _GetLastInputInfo_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastInputInfo.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastInputInfo),[google](#http://www.google.com/search?q=GetLastInputInfo.md#http://www.google.com/search?q=GetLastInputInfo)or[google groups](#http://groups.google.com/groups?q=GetLastInputInfo.md#http://groups.google.com/groups?q=GetLastInputInfo).

## [win32api](#win32api.md#win32api).GetLocalTime

tuple = **GetLocalTime(** )
Returns the current local time

## [win32api](#win32api.md#win32api).GetLogicalDriveStrings

string = **GetLogicalDriveStrings(** )
Returns a string with all logical drives currently mapped.

#### Win32 API References


	Search for _GetLogicalDriveStrings_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLogicalDriveStrings.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLogicalDriveStrings),[google](#http://www.google.com/search?q=GetLogicalDriveStrings.md#http://www.google.com/search?q=GetLogicalDriveStrings)or[google groups](#http://groups.google.com/groups?q=GetLogicalDriveStrings.md#http://groups.google.com/groups?q=GetLogicalDriveStrings).

#### Return Value
The return value is a single string, with each drive 

letter NULL terminated.
Use "s.split('\\0')" to split into components.

## [win32api](#win32api.md#win32api).GetLogicalDrives

int = **GetLogicalDrives(** )
Returns a bitmask representing the currently available disk drives.

#### Win32 API References


	Search for _GetLogicalDrives_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLogicalDrives.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLogicalDrives),[google](#http://www.google.com/search?q=GetLogicalDrives.md#http://www.google.com/search?q=GetLogicalDrives)or[google groups](#http://groups.google.com/groups?q=GetLogicalDrives.md#http://groups.google.com/groups?q=GetLogicalDrives).

## [win32api](#win32api.md#win32api).GetLongPathNameW

[PyUnicode](#PyUnicode.md#PyUnicode)= **GetLongPathNameW( _fileName_ ** )
Converts the specified path to its long form.

#### Parameters


	 _fileName_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	The file name.

#### Comments
This function may raise a NotImplementedError exception if the version 

of Windows does not support this function.

## [win32api](#win32api.md#win32api).GetLongPathName

string = **GetLongPathName( _fileName_ ** )
Converts the specified path to its long form.

#### Parameters


	 _fileName_ : string

	The file name.

#### Comments
This function may raise a NotImplementedError exception if the version 

of Windows does not support this function.

## [win32api](#win32api.md#win32api).GetModuleFileNameW

[PyUnicode](#PyUnicode.md#PyUnicode)= **GetModuleFileNameW( _hModule_ ** )
Retrieves the unicode filename of the specified module.

#### Parameters


	 _hModule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Specifies the handle to the module.

#### Win32 API References


	Search for _GetModuleFileName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName),[google](#http://www.google.com/search?q=GetModuleFileName.md#http://www.google.com/search?q=GetModuleFileName)or[google groups](#http://groups.google.com/groups?q=GetModuleFileName.md#http://groups.google.com/groups?q=GetModuleFileName).

## [win32api](#win32api.md#win32api).GetModuleFileName

string = **GetModuleFileName( _hModule_ ** )
Retrieves the filename of the specified module.

#### Parameters


	 _hModule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Specifies the handle to the module.

#### Win32 API References


	Search for _GetModuleFileName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName),[google](#http://www.google.com/search?q=GetModuleFileName.md#http://www.google.com/search?q=GetModuleFileName)or[google groups](#http://groups.google.com/groups?q=GetModuleFileName.md#http://groups.google.com/groups?q=GetModuleFileName).

## [win32api](#win32api.md#win32api).GetModuleHandle

int = **GetModuleHandle( _fileName_ ** )
Returns the handle of an already loaded DLL.

#### Parameters


	 _fileName=None_ : string

	Specifies the file name of the module to load.

#### Win32 API References


	Search for _GetModuleHandle_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleHandle.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleHandle),[google](#http://www.google.com/search?q=GetModuleHandle.md#http://www.google.com/search?q=GetModuleHandle)or[google groups](#http://groups.google.com/groups?q=GetModuleHandle.md#http://groups.google.com/groups?q=GetModuleHandle).

## [win32api](#win32api.md#win32api).GetMonitorInfo

dict = **GetMonitorInfo( _hMonitor_ ** )
Retrieves information for a monitor by handle

#### Parameters


	 _hMonitor_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to a monitor

#### Comments
Accepts keyword args

#### Return Value
Returns a dictionary representing a MONITORINFOEX structure

## [win32api](#win32api.md#win32api).GetNativeSystemInfo

tuple = **GetNativeSystemInfo(** )
Retrieves information about the current system for a Wow64 process.

#### Win32 API References


	Search for _GetNativeSystemInfo_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetNativeSystemInfo.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetNativeSystemInfo),[google](#http://www.google.com/search?q=GetNativeSystemInfo.md#http://www.google.com/search?q=GetNativeSystemInfo)or[google groups](#http://groups.google.com/groups?q=GetNativeSystemInfo.md#http://groups.google.com/groups?q=GetNativeSystemInfo).

#### Return Value
The return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM_INFO structure.  The element names are:
wProcessorArchitecture
dwPageSize
lpMinimumApplicationAddress
lpMaximumApplicationAddress
dwActiveProcessorMask
dwNumberOfProcessors
dwProcessorType
dwAllocationGranularity
(wProcessorLevel,wProcessorRevision)

## [win32api](#win32api.md#win32api).GetProcAddress

int = **GetProcAddress( _hModule_  _, functionName_ ** )
Returns the address of the specified exported dynamic-link library (DLL) function.

#### Parameters


	 _hModule_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Specifies the handle to the module.

	 _functionName_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	Specifies the name of the procedure, or its ordinal value

#### Win32 API References


	Search for _GetProcAddress_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProcAddress.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProcAddress),[google](#http://www.google.com/search?q=GetProcAddress.md#http://www.google.com/search?q=GetProcAddress)or[google groups](#http://groups.google.com/groups?q=GetProcAddress.md#http://groups.google.com/groups?q=GetProcAddress).

## [win32api](#win32api.md#win32api).GetProfileSection

list = **GetProfileSection( _section_  _, iniName_ ** )
Retrieves all entries from a section in an INI file.

#### Parameters


	 _section_ : string

	The section in the INI file to retrieve a entries for.

	 _iniName=None_ : string

	The name of the INI file.  If None, the system INI file is used.

#### Comments
This function is obsolete, applications should use the registry instead.

#### Win32 API References


	Search for _GetProfileSection_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileSection.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileSection),[google](#http://www.google.com/search?q=GetProfileSection.md#http://www.google.com/search?q=GetProfileSection)or[google groups](#http://groups.google.com/groups?q=GetProfileSection.md#http://groups.google.com/groups?q=GetProfileSection).

#### Return Value
The return value is a list of strings.

## [win32api](#win32api.md#win32api).GetProfileVal

int/string = **GetProfileVal( _section_  _, entry_  _, defValue_  _, iniName_ ** )
Retrieves entries from a windows INI file.  This method encapsulates GetProfileString, GetProfileInt, GetPrivateProfileString and GetPrivateProfileInt.

#### Parameters


	 _section_ : string

	The section in the INI file to retrieve a value for.

	 _entry_ : string

	The entry within the section in the INI file to retrieve a value for.

	 _defValue_ : int/string

	The default value.  The type of this parameter determines the methods return type.

	 _iniName=None_ : string

	The name of the INI file.  If None, the system INI file is used.

#### Comments
This function is obsolete, applications should use the registry instead.

#### Win32 API References


	Search for _GetProfileString_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileString.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileString),[google](#http://www.google.com/search?q=GetProfileString.md#http://www.google.com/search?q=GetProfileString)or[google groups](#http://groups.google.com/groups?q=GetProfileString.md#http://groups.google.com/groups?q=GetProfileString).

	Search for _GetProfileInt_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileInt.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileInt),[google](#http://www.google.com/search?q=GetProfileInt.md#http://www.google.com/search?q=GetProfileInt)or[google groups](#http://groups.google.com/groups?q=GetProfileInt.md#http://groups.google.com/groups?q=GetProfileInt).

	Search for _GetPrivateProfileString_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPrivateProfileString.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPrivateProfileString),[google](#http://www.google.com/search?q=GetPrivateProfileString.md#http://www.google.com/search?q=GetPrivateProfileString)or[google groups](#http://groups.google.com/groups?q=GetPrivateProfileString.md#http://groups.google.com/groups?q=GetPrivateProfileString).

	Search for _GetPrivateProfileInt_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPrivateProfileInt.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPrivateProfileInt),[google](#http://www.google.com/search?q=GetPrivateProfileInt.md#http://www.google.com/search?q=GetPrivateProfileInt)or[google groups](#http://groups.google.com/groups?q=GetPrivateProfileInt.md#http://groups.google.com/groups?q=GetPrivateProfileInt).

#### Return Value
The return value is the same type as the default parameter.

## [win32api](#win32api.md#win32api).GetPwrCapabilities

dict = **GetPwrCapabilities(** )
Retrieves system's power capabilities

#### Comments
Requires Win2k or later.

#### Win32 API References


	Search for _GetPwrCapabilities_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPwrCapabilities.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPwrCapabilities),[google](#http://www.google.com/search?q=GetPwrCapabilities.md#http://www.google.com/search?q=GetPwrCapabilities)or[google groups](#http://groups.google.com/groups?q=GetPwrCapabilities.md#http://groups.google.com/groups?q=GetPwrCapabilities).

#### Return Value
Returns a dict representing a SYSTEM_POWER_CAPABILITIES struct

## [win32api](#win32api.md#win32api).GetShortPathName

string = **GetShortPathName( _path_ ** )
Obtains the short path form of the specified path.

#### Parameters


	 _path_ : string/unicode

	If a unicode object is passed, 

GetShortPathNameW will be called and a unicode object returned.

#### Comments
The short path name is an 8.3 compatible file name.  As the input path does 

not need to be absolute, the returned name may be longer than the input path.

#### Win32 API References


	Search for _GetShortPathName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetShortPathName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetShortPathName),[google](#http://www.google.com/search?q=GetShortPathName.md#http://www.google.com/search?q=GetShortPathName)or[google groups](#http://groups.google.com/groups?q=GetShortPathName.md#http://groups.google.com/groups?q=GetShortPathName).

## [win32api](#win32api.md#win32api).GetStdHandle

 **GetStdHandle( _handle_ ** )
Returns a handle for the standard input, standard output, or standard error device

#### Parameters


	 _handle_ : int

	input, output, or error device

## [win32api](#win32api.md#win32api).GetSysColor

int = **GetSysColor( _index_ ** )
Returns the current system color for the specified element.

#### Parameters


	 _index_ : int

	The Id of the element to return.  See the API for full details.

#### Win32 API References


	Search for _GetSysColor_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSysColor.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSysColor),[google](#http://www.google.com/search?q=GetSysColor.md#http://www.google.com/search?q=GetSysColor)or[google groups](#http://groups.google.com/groups?q=GetSysColor.md#http://groups.google.com/groups?q=GetSysColor).

#### Return Value
The return value is a windows RGB color representation.

## [win32api](#win32api.md#win32api).GetSystemDefaultLCID

int = **GetSystemDefaultLCID(** )
Retrieves the system default locale identifier.

#### Win32 API References


	Search for _GetSystemDefaultLCID_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDefaultLCID.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDefaultLCID),[google](#http://www.google.com/search?q=GetSystemDefaultLCID.md#http://www.google.com/search?q=GetSystemDefaultLCID)or[google groups](#http://groups.google.com/groups?q=GetSystemDefaultLCID.md#http://groups.google.com/groups?q=GetSystemDefaultLCID).

## [win32api](#win32api.md#win32api).GetSystemDefaultLangID

int = **GetSystemDefaultLangID(** )
Retrieves the system default language identifier.

#### Win32 API References


	Search for _GetSystemDefaultLangID_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDefaultLangID.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDefaultLangID),[google](#http://www.google.com/search?q=GetSystemDefaultLangID.md#http://www.google.com/search?q=GetSystemDefaultLangID)or[google groups](#http://groups.google.com/groups?q=GetSystemDefaultLangID.md#http://groups.google.com/groups?q=GetSystemDefaultLangID).

## [win32api](#win32api.md#win32api).GetSystemDirectory

string = **GetSystemDirectory(** )
Returns the path of the Windows system directory.

#### Win32 API References


	Search for _GetSystemDirectory_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDirectory.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDirectory),[google](#http://www.google.com/search?q=GetSystemDirectory.md#http://www.google.com/search?q=GetSystemDirectory)or[google groups](#http://groups.google.com/groups?q=GetSystemDirectory.md#http://groups.google.com/groups?q=GetSystemDirectory).

## [win32api](#win32api.md#win32api).GetSystemFileCacheSize

tuple = **GetSystemFileCacheSize(** )
Returns the amount of memory reserved for file cache

#### Return Value
Returns a tuple containing the minimum and maximum cache sizes, and flags (combination of win32con.MM_WORKING_SET_* flags)

## [win32api](#win32api.md#win32api).GetSystemInfo

tuple = **GetSystemInfo(** )
Retrieves information about the current system.

#### Win32 API References


	Search for _GetSystemInfo_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemInfo.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemInfo),[google](#http://www.google.com/search?q=GetSystemInfo.md#http://www.google.com/search?q=GetSystemInfo)or[google groups](#http://groups.google.com/groups?q=GetSystemInfo.md#http://groups.google.com/groups?q=GetSystemInfo).

#### Return Value
The return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM_INFO structure.  The element names are:
wProcessorArchitecture
dwPageSize
lpMinimumApplicationAddress
lpMaximumApplicationAddress
dwActiveProcessorMask
dwNumberOfProcessors
dwProcessorType
dwAllocationGranularity
(wProcessorLevel,wProcessorRevision)

## [win32api](#win32api.md#win32api).GetSystemMetrics

int = **GetSystemMetrics( _index_ ** )
Retrieves various system metrics and system configuration settings.

#### Parameters


	 _index_ : int

	Which metric is being requested.  See the API documentation for a full list.

#### Win32 API References


	Search for _GetSystemMetrics_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemMetrics.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemMetrics),[google](#http://www.google.com/search?q=GetSystemMetrics.md#http://www.google.com/search?q=GetSystemMetrics)or[google groups](#http://groups.google.com/groups?q=GetSystemMetrics.md#http://groups.google.com/groups?q=GetSystemMetrics).

## [win32api](#win32api.md#win32api).GetSystemTime

tuple = **GetSystemTime(** )
Returns the current system time

## [win32api](#win32api.md#win32api).GetTempFileName

tuple = **GetTempFileName( _path_  _, prefix_  _, nUnique_ ** )
Returns creates a temporary filename of the following form: path\\preuuuu.tmp.

#### Parameters


	 _path_ : string

	Specifies the path where the method creates the temporary filename. 

Applications typically specify a period (.) or the result of the GetTempPath function for this parameter.

	 _prefix_ : string

	Specifies the temporary filename prefix.

	 _nUnique_ : int

	Specifies an nteger used in creating the temporary filename. 

If this parameter is nonzero, it is appended to the temporary filename. 

If this parameter is zero, Windows uses the current system time to create a number to append to the filename.

#### Win32 API References


	Search for _GetTempFileName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetTempFileName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetTempFileName),[google](#http://www.google.com/search?q=GetTempFileName.md#http://www.google.com/search?q=GetTempFileName)or[google groups](#http://groups.google.com/groups?q=GetTempFileName.md#http://groups.google.com/groups?q=GetTempFileName).

#### Return Value
The return value is a tuple of (string, int), where string is the 

filename, and rc is the unique number used to generate the filename.

## [win32api](#win32api.md#win32api).GetTempPath

string = **GetTempPath(** )
Retrieves the path of the directory designated for temporary files.

## [win32api](#win32api.md#win32api).GetThreadLocale

int = **GetThreadLocale(** )
Returns the current thread's locale.

## [win32api](#win32api.md#win32api).GetTickCount

int = **GetTickCount(** )
Returns the number of milliseconds since windows started.

## [win32api](#win32api.md#win32api).GetTimeFormat

string = **GetTimeFormat( _locale_  _, flags_  _, time_  _, format_ ** )
Formats a time as a time string for a specified locale. The function formats either a specified time or the local system time.

#### Parameters


	 _locale_ : int

	

	 _flags_ : int

	

	 _time_ :[PyTime](#PyTime.md#PyTime)

	The time to use, or None to use the current time.

	 _format_ : string

	May be None

## [win32api](#win32api.md#win32api).GetTimeZoneInformation

tuple = **GetTimeZoneInformation( _times_as_tuples_ ** )
Retrieves the system time-zone information.

#### Parameters


	 _times_as_tuples=False_ : bool

	If true, the SYSTEMTIME elements are returned as tuples instead of a time object.

#### Return Value
The return value is a tuple of (rc, tzinfo), where rc is 

the integer return code from ::GetTimezoneInformation(), which may be

 **value**  **description** TIME_ZONE_ID_STANDARDif in standard timeTIME_ZONE_ID_DAYLIGHTif in daylight savings timeTIME_ZONE_ID_UNKNOWNif the timezone in question doesn't use daylight savings time, (eg. indiana time).tzinfo is a tuple of:

#### Items


	[0] _int_ : bias

	Specifies the current bias, in minutes, for local time translation on this computer. The bias is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. All translations between UTC and local time are based on the following formula:

UTC = local time + bias



	[1] _unicode_ : standardName

	Specifies a string associated with standard time on this operating system. For example, this member could contain "EST" to indicate Eastern Standard Time. This string is not used by the operating system, so anything stored there using the SetTimeZoneInformation function is returned unchanged by the GetTimeZoneInformation function. This string can be empty.

	[2] _[PyTime](#PyTime.md#PyTime)/tuple_ : standardTime

	Specifies a SYSTEMTIME object that contains a date and local time when the transition from daylight saving time to standard time occurs on this operating system. If this date is not specified, the wMonth member in the SYSTEMTIME structure must be zero. If this date is specified, the DaylightDate value in the TIME_ZONE_INFORMATION structure must also be specified.
To select the correct day in the month, set the wYear member to zero, the wDayOfWeek member to an appropriate weekday, and the wDay member to a value in the range 1 through 5. Using this notation, the first Sunday in April can be specified, as can the last Thursday in October (5 is equal to "the last").

	[3] _int_ : standardBias

	Specifies a bias value to be used during local time translations that occur during standard time. This member is ignored if a value for the StandardDate member is not supplied.
This value is added to the value of the Bias member to form the bias used during standard time. In most time zones, the value of this member is zero.

	[4] _unicode_ : daylightName

	

	[5] _[PyTime](#PyTime.md#PyTime)/tuple_ : daylightTime

	

	[6] _int_ : daylightBias

	Specifies a bias value to be used during local time translations that occur during daylight saving time. This member is ignored if a value for the DaylightDate member is not supplied.
This value is added to the value of the Bias member to form the bias used during daylight saving time. In most time zones, the value of this member is &#150 60.

## [win32api](#win32api.md#win32api).GetUserDefaultLCID

int = **GetUserDefaultLCID(** )
Retrieves the user default locale identifier.

#### Win32 API References


	Search for _GetUserDefaultLCID_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserDefaultLCID.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserDefaultLCID),[google](#http://www.google.com/search?q=GetUserDefaultLCID.md#http://www.google.com/search?q=GetUserDefaultLCID)or[google groups](#http://groups.google.com/groups?q=GetUserDefaultLCID.md#http://groups.google.com/groups?q=GetUserDefaultLCID).

## [win32api](#win32api.md#win32api).GetUserDefaultLangID

int = **GetUserDefaultLangID(** )
Retrieves the user default language identifier.

#### Win32 API References


	Search for _GetUserDefaultLangID_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserDefaultLangID.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserDefaultLangID),[google](#http://www.google.com/search?q=GetUserDefaultLangID.md#http://www.google.com/search?q=GetUserDefaultLangID)or[google groups](#http://groups.google.com/groups?q=GetUserDefaultLangID.md#http://groups.google.com/groups?q=GetUserDefaultLangID).

## [win32api](#win32api.md#win32api).GetUserNameEx

string = **GetUserNameEx( _NameFormat_ ** )
Returns the current user name in format from EXTENDED_NAME_FORMAT enum

#### Parameters


	 _NameFormat_ : int

	EXTENDED_NAME_FORMAT value, win32con.Name*

#### Win32 API References


	Search for _GetUserNameEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserNameEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserNameEx),[google](#http://www.google.com/search?q=GetUserNameEx.md#http://www.google.com/search?q=GetUserNameEx)or[google groups](#http://groups.google.com/groups?q=GetUserNameEx.md#http://groups.google.com/groups?q=GetUserNameEx).

## [win32api](#win32api.md#win32api).GetUserName

string = **GetUserName(** )
Returns the current user name

#### Win32 API References


	Search for _GetUserName_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserName.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserName),[google](#http://www.google.com/search?q=GetUserName.md#http://www.google.com/search?q=GetUserName)or[google groups](#http://groups.google.com/groups?q=GetUserName.md#http://groups.google.com/groups?q=GetUserName).

## [win32api](#win32api.md#win32api).GetVersionEx

tuple = **GetVersionEx( _format_ ** )
Returns the current version of Windows, and information about the environment.

#### Parameters


	 _format=0_ : int

	The format of the version info to return. 

May be 0 (for OSVERSIONINFO) or 1 (for OSVERSIONINFOEX)

#### Return Value
The return value is a tuple with the following information.


#### Items


	[0] _int_ : majorVersion

	Identifies the major version number of the operating system.


	[1] _int_ : minorVersion

	Identifies the minor version number of the operating system.


	[2] _int_ : buildNumber

	Identifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)


	[3] _int_ : platformId

	Identifies the platform supported by the operating system.  May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT


	[4] _string_ : version

	Contains arbitrary additional information about the operating system.

#### Return Value
or if the format param is 1, the return value is a tuple with:


#### Items


	[0] _int_ : majorVersion

	Identifies the major version number of the operating system.


	[1] _int_ : minorVersion

	Identifies the minor version number of the operating system.


	[2] _int_ : buildNumber

	Identifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)


	[3] _int_ : platformId

	Identifies the platform supported by the operating system.  May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT


	[4] _string_ : version

	Contains arbitrary additional information about the operating system.

	[5] _int_ : wServicePackMajor

	Major version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the major version number is 3. If no Service Pack has been installed, the value is zero.

	[6] _int_ : wServicePackMinor

	Minor version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the minor version number is 0.

	[7] _int_ : wSuiteMask

	Bit flags that identify the product suites available on the system. This member can be a combination of the VER_SUITE_* values.

	[8] _int_ : wProductType

	Additional information about the system. This member can be one of the VER_NT_* values.

	[9] _int_ : wReserved

	

## [win32api](#win32api.md#win32api).GetVersion

int = **GetVersion(** )
Returns the current version of Windows, and information about the environment.

#### Return Value
The return value's low word is the major/minor version of Windows.  The high 

word is 0 if the platform is Windows NT, or 1 if Win32s on Windows 3.1

## [win32api](#win32api.md#win32api).GetVolumeInformation

tuple = **GetVolumeInformation( _path_ ** )
Returns information about a file system and colume whose root directory is specified.

#### Parameters


	 _path_ : string

	The root path of the volume on which information is being requested.

#### Return Value
The return is a tuple of:
string - Volume Name
long - Volume serial number.
long - Maximum Component Length of a file name.
long - Sys Flags - other flags specific to the file system.  See the api for details.
string - File System Name

## [win32api](#win32api.md#win32api).GetWindowLong

int = **GetWindowLong( _hwnd_  _, offset_ ** )
Retrieves a long value at the specified offset into the extra window memory of the given window.

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle to the window.

	 _offset_ : int

	Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

#### Comments
This function calls the GetWindowLongPtr Api function

## [win32api](#win32api.md#win32api).GetWindowsDirectory

string = **GetWindowsDirectory(** )
Returns the path of the Windows directory.

## [win32api](#win32api.md#win32api).GlobalMemoryStatusEx

dict = **GlobalMemoryStatusEx(** )
Returns physical and virtual memory usage

#### Comments
Only available on Win2k and later.

#### Return Value
Returns a dictionary representing a MEMORYSTATUSEX structure

## [win32api](#win32api.md#win32api).GlobalMemoryStatus

dict = **GlobalMemoryStatus(** )
Returns systemwide memory usage

#### Return Value
Returns a dictionary representing a MEMORYSTATUS structure

## [win32api](#win32api.md#win32api).HIBYTE

int = **HIBYTE( _val_ ** )
An interface to the win32api HIBYTE macro.

#### Parameters


	 _val_ : int

	The value to retrieve the HIBYTE from.

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).HIWORD

int = **HIWORD( _val_ ** )
An interface to the win32api HIWORD macro.

#### Parameters


	 _val_ : int

	The value to retrieve the HIWORD from.

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).InitiateSystemShutdown

 **InitiateSystemShutdown( _computerName_  _, message_  _, timeOut_  _, bForceClose_  _, bRebootAfterShutdown_ ** )
Initiates a shutdown and optional restart of the specified computer.

#### Parameters


	 _computerName_ : string/[PyUnicode](#PyUnicode.md#PyUnicode)

	Specifies the name of the computer to shut-down, or None

	 _message_ : string/[PyUnicode](#PyUnicode.md#PyUnicode)

	Message to display in a dialog box

	 _timeOut_ : int

	Specifies the time (in seconds) that the dialog box should be displayed. While this dialog box is displayed, the shutdown can be stopped by the AbortSystemShutdown function. 

If dwTimeout is zero, the computer shuts down without displaying the dialog box, and the shutdown cannot be stopped by AbortSystemShutdown.

	 _bForceClose_ : int

	Specifies whether applications with unsaved changes are to be forcibly closed. If this parameter is TRUE, such applications are closed. If this parameter is FALSE, a dialog box is displayed prompting the user to close the applications.

	 _bRebootAfterShutdown_ : int

	Specifies whether the computer is to restart immediately after shutting down. If this parameter is TRUE, the computer is to restart. If this parameter is FALSE, the system flushes all caches to disk, clears the screen, and displays a message indicating that it is safe to power down.

#### Win32 API References


	Search for _InitiateSystemShutdown_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InitiateSystemShutdown.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InitiateSystemShutdown),[google](#http://www.google.com/search?q=InitiateSystemShutdown.md#http://www.google.com/search?q=InitiateSystemShutdown)or[google groups](#http://groups.google.com/groups?q=InitiateSystemShutdown.md#http://groups.google.com/groups?q=InitiateSystemShutdown).

## [win32api](#win32api.md#win32api).LOBYTE

int = **LOBYTE( _val_ ** )
An interface to the win32api LOBYTE macro.

#### Parameters


	 _val_ : int

	The value to retrieve the LOBYTE from.

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).LOWORD

int = **LOWORD( _val_ ** )
An interface to the win32api LOWORD macro.

#### Parameters


	 _val_ : int

	The value to retrieve the LOWORD from.

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).LoadCursor

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **LoadCursor( _hInstance_  _, cursorid_ ** )
Loads a cursor.

#### Parameters


	 _hInstance_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to the instance to load the resource from, or None to load a standard system cursor

	 _cursorid_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	The ID of the cursor.  Can be a resource id or for system cursors, one of win32con.IDC_*

#### Win32 API References


	Search for _LoadCursor_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadCursor.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadCursor),[google](#http://www.google.com/search?q=LoadCursor.md#http://www.google.com/search?q=LoadCursor)or[google groups](#http://groups.google.com/groups?q=LoadCursor.md#http://groups.google.com/groups?q=LoadCursor).

## [win32api](#win32api.md#win32api).LoadKeyboardLayout

int = **LoadKeyboardLayout( _KLID_  _, Flags_ ** )
Loads a new locale id

#### Parameters


	 _KLID_ : string

	Hex string containing a locale id, eg "00000409"

	 _Flags=0_ : int

	Combination of win32con.KLF_* constants

#### Return Value
Returns the numeric locale id that was loaded

## [win32api](#win32api.md#win32api).LoadLibraryEx

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **LoadLibraryEx( _fileName_  _, handle_  _, handle_ ** )
Loads the specified DLL, and returns the handle.

#### Parameters


	 _fileName_ : string

	Specifies the file name of the module to load.

	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Reserved - must be zero

	 _handle_ : flags

	Specifies the action to take when loading the module.

#### Win32 API References


	Search for _LoadLibraryEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadLibraryEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadLibraryEx),[google](#http://www.google.com/search?q=LoadLibraryEx.md#http://www.google.com/search?q=LoadLibraryEx)or[google groups](#http://groups.google.com/groups?q=LoadLibraryEx.md#http://groups.google.com/groups?q=LoadLibraryEx).

## [win32api](#win32api.md#win32api).LoadLibrary

int = **LoadLibrary( _fileName_ ** )
Loads the specified DLL, and returns the handle.

#### Parameters


	 _fileName_ : string

	Specifies the file name of the module to load.

#### Win32 API References


	Search for _LoadLibrary_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadLibrary.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadLibrary),[google](#http://www.google.com/search?q=LoadLibrary.md#http://www.google.com/search?q=LoadLibrary)or[google groups](#http://groups.google.com/groups?q=LoadLibrary.md#http://groups.google.com/groups?q=LoadLibrary).

## [win32api](#win32api.md#win32api).LoadResource

string = **LoadResource( _handle_  _, type_  _, name_  _, language_ ** )
Finds and loads a resource from a PE file.

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle of the module containing the resource.  Use None for currrent process executable.

	 _type_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	The type of resource to load.

	 _name_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	The name or Id of the resource to load.

	 _language=NEUTRAL_ : int

	Language to use, defaults to LANG_NEUTRAL.

## [win32api](#win32api.md#win32api).LoadString

[PyUnicode](#PyUnicode.md#PyUnicode)= **LoadString( _handle_  _, stringId_  _, numChars_ ** )
Loads a string from a resource file.

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle of the module containing the resource.

	 _stringId_ : int

	The ID of the string to load.

	 _numChars=1024_ : int

	Number of characters to allocate for the return buffer.

## [win32api](#win32api.md#win32api).MAKELANGID

int = **MAKELANGID( _PrimaryLanguage_  _, SubLanguage_ ** )
Creates a language identifier from a primary language identifier and a sublanguage identifier.

#### Parameters


	 _PrimaryLanguage_ : int

	Primary language identifier

	 _SubLanguage_ : int

	The sublanguage identifier

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).MAKELONG

int = **MAKELONG( _low_  _, high_ ** )
creates a LONG value by concatenating the specified values.

#### Parameters


	 _low_ : int

	Specifies the low-order byte of the new value.

	 _high_ : int

	Specifies the high-order byte of the new value.

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).MAKEWORD

int = **MAKEWORD( _low_  _, high_ ** )
creates a WORD value by concatenating the specified values.

#### Parameters


	 _low_ : int

	Specifies the low-order byte of the new value.

	 _high_ : int

	Specifies the high-order byte of the new value.

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).MapVirtualKey

int = **MapVirtualKey( _vk_  _, type_  _, hlayout_ ** )
Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code.

#### Parameters


	 _vk_ : int

	The virtual key code.

	 _type_ : int

	The type of conversion to make - see the API

	 _hlayout=None_ : handle

	The keyboard layout to use.  If not 

specified, the API function MapVirtualKey will be called.  If it 

is specified MapVirtualKeyEx will be called.

#### Comments
implemented by calling the unicode versions of the API (MapVirtualKeyW/MapVirtualKeyExW)

## [win32api](#win32api.md#win32api).MessageBeep

int = **MessageBeep( _type_ ** )
Plays a predefined waveform sound.

#### Parameters


	 _type=win32con.MB_OK_ : int

	Specifies the sound type, as 

identified by an entry in the [sounds] section of the 

registry. This parameter can be one of MB_ICONASTERISK, 

MB_ICONEXCLAMATION, MB_ICONHAND, MB_ICONQUESTION or MB_OK.

#### Comments
The waveform sound for each sound type is identified by an entry in the [sounds] section of the registry.

## [win32api](#win32api.md#win32api).MessageBox

int = **MessageBox( _hwnd_  _, message_  _, title_  _, style_  _, language_ ** )
Display a message box.

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle of the parent window.  See the comments section.

	 _message_ : string

	The message to be displayed in the message box.

	 _title_ : string/None

	The title for the message box.  If None, the applications title will be used.

	 _style=win32con.MB_OK_ : int

	The style of the message box.

	 _language=win32api.MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT)_ : int

	The language ID to use.

#### Comments
Normally, a program in a GUI environment will use one of the MessageBox 

methods supplied by the GUI (eg,[win32ui::MessageBox](#win32ui.md#win32ui_MessageBox_meth)or[PyCWnd::MessageBox](#PyCWnd.md#PyCWnd_MessageBox_meth))

#### Return Value
An integer identifying the button pressed to dismiss the dialog.

## [win32api](#win32api.md#win32api).MonitorFromPoint

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **MonitorFromPoint( _pt_  _, Flags_ ** )
Finds monitor that contains a point

#### Parameters


	 _pt_ : (int, int)

	Tuple of 2 ints (x,y) specifying screen coordinates

	 _Flags=0_ : int

	Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

#### Comments
Accepts keyword arguments

#### Return Value
Returns None if no monitor was found

## [win32api](#win32api.md#win32api).MonitorFromRect

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **MonitorFromRect( _rc_  _, Flags_ ** )
Finds monitor that has largest intersection with a rectangle

#### Parameters


	 _rc_ :[PyRECT](#PyRECT.md#PyRECT)

	Rectangle to be examined

	 _Flags=0_ : int

	Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

#### Comments
Accepts keyword arguments

#### Return Value
Returns None if no monitor was found

## [win32api](#win32api.md#win32api).MonitorFromWindow

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **MonitorFromWindow( _hwnd_  _, Flags_ ** )
Finds monitor that contains a window

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to a window

	 _Flags=0_ : int

	Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

#### Comments
Accepts keyword arguments

#### Return Value
Returns None if no monitor was found

## [win32api](#win32api.md#win32api).MoveFileEx

 **MoveFileEx( _srcName_  _, destName_  _, flag_ ** )
Renames a file.

#### Parameters


	 _srcName_ : string

	The name of the source file.

	 _destName_ : string

	The name of the destination file.  May be None.

	 _flag_ : int

	Flags indicating how the move is to be performed.  See the API for full details.

#### Comments
This method can move files across volumes.
If destName is None, and flags contains win32con.MOVEFILE_DELAY_UNTIL_REBOOT, the 

file will be deleted next reboot.

#### Win32 API References


	Search for _MoveFileEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MoveFileEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MoveFileEx),[google](#http://www.google.com/search?q=MoveFileEx.md#http://www.google.com/search?q=MoveFileEx)or[google groups](#http://groups.google.com/groups?q=MoveFileEx.md#http://groups.google.com/groups?q=MoveFileEx).

## [win32api](#win32api.md#win32api).MoveFile

 **MoveFile( _srcName_  _, destName_ ** )
Renames a file, or a directory (including its children).

#### Parameters


	 _srcName_ : string

	The name of the source file.

	 _destName_ : string

	The name of the destination file.

#### Comments
This method can not move files across volumes.

#### Win32 API References


	Search for _MoveFile._ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MoveFile..md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MoveFile.),[google](#http://www.google.com/search?q=MoveFile..md#http://www.google.com/search?q=MoveFile.)or[google groups](#http://groups.google.com/groups?q=MoveFile..md#http://groups.google.com/groups?q=MoveFile.).

## [win32api](#win32api.md#win32api).OpenProcess

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **OpenProcess( _reqdAccess_  _, bInherit_  _, pid_ ** )
Retrieves a handle to an existing process

#### Parameters


	 _reqdAccess_ : int

	The required access.

	 _bInherit_ : int

	Specifies whether the returned handle can be inherited by a new process created by the current process. If TRUE, the handle is inheritable.

	 _pid_ : int

	The process ID

## [win32api](#win32api.md#win32api).OutputDebugString

 **OutputDebugString( _msg_ ** )
Sends a string to the Windows debugging device.

#### Parameters


	 _msg_ : string

	The string to write.

## [win32api](#win32api.md#win32api).PostMessage

 **PostMessage( _hwnd_  _, idMessage_  _, wParam_  _, lParam_ ** )
Post a message to a window.

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The hWnd of the window to receive the message.

	 _idMessage_ : int

	The ID of the message to post.

	 _wParam=None_ : int

	The wParam for the message

	 _lParam=None_ : int

	The lParam for the message

#### Win32 API References


	Search for _PostMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostMessage),[google](#http://www.google.com/search?q=PostMessage.md#http://www.google.com/search?q=PostMessage)or[google groups](#http://groups.google.com/groups?q=PostMessage.md#http://groups.google.com/groups?q=PostMessage).

## [win32api](#win32api.md#win32api).PostQuitMessage

 **PostQuitMessage( _exitCode_ ** )
Post a quit message to an app.

#### Parameters


	 _exitCode=0_ : int

	The exit code

#### Win32 API References


	Search for _PostQuitMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostQuitMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostQuitMessage),[google](#http://www.google.com/search?q=PostQuitMessage.md#http://www.google.com/search?q=PostQuitMessage)or[google groups](#http://groups.google.com/groups?q=PostQuitMessage.md#http://groups.google.com/groups?q=PostQuitMessage).

## [win32api](#win32api.md#win32api).PostThreadMessage

 **PostThreadMessage( _tid_  _, idMessage_  _, wParam_  _, lParam_ ** )
Post a message to the specified thread.

#### Parameters


	 _tid_ : int

	Identifier of the thread to which the message will be posted.

	 _idMessage_ : int

	The ID of the message to post.

	 _wParam=None_ : int/str

	The wParam for the message

	 _lParam=None_ : int/str

	The lParam for the message

#### Win32 API References


	Search for _PostThreadMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostThreadMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostThreadMessage),[google](#http://www.google.com/search?q=PostThreadMessage.md#http://www.google.com/search?q=PostThreadMessage)or[google groups](#http://groups.google.com/groups?q=PostThreadMessage.md#http://groups.google.com/groups?q=PostThreadMessage).

## [win32api](#win32api.md#win32api).RGB

int = **RGB( _red_  _, green_  _, blue_ ** )
An interface to the win32api RGB macro.

#### Parameters


	 _red_ : int

	The red value

	 _green_ : int

	The green value

	 _blue_ : int

	The blue value

#### Comments
This is simply a wrapper to a C++ macro.

## [win32api](#win32api.md#win32api).RegCloseKey

 **RegCloseKey( _key_ ** )
Closes a previously opened registry key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	The key to be closed.

#### Win32 API References


	Search for _RegCloseKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCloseKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCloseKey),[google](#http://www.google.com/search?q=RegCloseKey.md#http://www.google.com/search?q=RegCloseKey)or[google groups](#http://groups.google.com/groups?q=RegCloseKey.md#http://groups.google.com/groups?q=RegCloseKey).

## [win32api](#win32api.md#win32api).RegConnectRegistry

int = **RegConnectRegistry( _computerName_  _, key_ ** )
Establishes a connection to a predefined registry handle on another computer.

#### Parameters


	 _computerName_ : string

	The name of the remote computer, of the form \\\\computername.  If None, the local computer is used.

	 _key_ : int

	The predefined handle.  May be win32con.HKEY_LOCAL_MACHINE or win32con.HKEY_USERS.

#### Win32 API References


	Search for _RegConnectRegistry_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegConnectRegistry.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegConnectRegistry),[google](#http://www.google.com/search?q=RegConnectRegistry.md#http://www.google.com/search?q=RegConnectRegistry)or[google groups](#http://groups.google.com/groups?q=RegConnectRegistry.md#http://groups.google.com/groups?q=RegConnectRegistry).

#### Return Value
The return value is the handle of the opened key. 

If the function fails, an exception is raised.

## [win32api](#win32api.md#win32api).RegCopyTree

 **RegCopyTree( _KeySrc_  _, SubKey_  _, KeyDest_ ** )
Copies an entire registry key to another location

#### Parameters


	 _KeySrc_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Registry key to be copied

	 _SubKey_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Subkey to be copied, can be None

	 _KeyDest_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	The destination key

#### Comments
Accepts keyword args.
Requires Vista or later.

## [win32api](#win32api.md#win32api).RegCreateKeyEx

[PyHKEY](#PyHKEY.md#PyHKEY), int = **RegCreateKeyEx( _Key_  _, SubKey_  _, samDesired_  _, Class_  _, Options_  _, SecurityAttributes_  _, Transaction_ ** )
Extended version of RegCreateKey

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	Registry key or one of win32con.HKEY_* values

	 _SubKey_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of subkey to open or create.

	 _samDesired_ : int

	Access allowed to handle, combination of win32con.KEY_* constants.  Can also contain 

standard access rights such as DELETE, WRITE_OWNER, etc.

	 _Class=None_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of registry key class

	 _Options=REG_OPTION_NON_VOLATILE_ : int

	One of the winnt.REG_OPTION_* values

	 _SecurityAttributes=None_ :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

	Specifies security for key and handle inheritance

	 _Transaction=None_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to a transaction as returned by[win32transaction::CreateTransaction](#win32transaction.md#win32transaction_CreateTransaction_meth)

#### Comments
Implemented only as Unicode (RegCreateKeyExW).  Accepts keyword arguments.
If a transaction handle is passed in, RegCreateKeyTransacted will be called (requires Vista or later)

#### Win32 API References


	Search for _RegCreateKeyEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKeyEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKeyEx),[google](#http://www.google.com/search?q=RegCreateKeyEx.md#http://www.google.com/search?q=RegCreateKeyEx)or[google groups](#http://groups.google.com/groups?q=RegCreateKeyEx.md#http://groups.google.com/groups?q=RegCreateKeyEx).

	Search for _RegCreateKeyTransacted_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKeyTransacted.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKeyTransacted),[google](#http://www.google.com/search?q=RegCreateKeyTransacted.md#http://www.google.com/search?q=RegCreateKeyTransacted)or[google groups](#http://groups.google.com/groups?q=RegCreateKeyTransacted.md#http://groups.google.com/groups?q=RegCreateKeyTransacted).

#### Return Value
Returns registry handle and flag indicating if key was opened or created (REG_CREATED_NEW_KEY or REG_OPENED_EXISTING_KEY)

## [win32api](#win32api.md#win32api).RegCreateKey

[PyHKEY](#PyHKEY.md#PyHKEY)= **RegCreateKey( _key_  _, subKey_ ** )
Creates the specified key, or opens the key if it already exists.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _subKey_ : string

	The name of a key that this method opens or creates. 

This key must be a subkey of the key identified by the key parameter. 

If key is one of the predefined keys, subKey may be None. In that case, 

the handle returned is the same hkey handle passed in to the function.

#### Win32 API References


	Search for _RegCreateKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKey),[google](#http://www.google.com/search?q=RegCreateKey.md#http://www.google.com/search?q=RegCreateKey)or[google groups](#http://groups.google.com/groups?q=RegCreateKey.md#http://groups.google.com/groups?q=RegCreateKey).

#### Return Value
The return value is the handle of the opened key. 

If the function fails, an exception is raised.

## [win32api](#win32api.md#win32api).RegDeleteKeyEx

 **RegDeleteKeyEx( _Key_  _, SubKey_  _, samDesired_  _, Transaction_ ** )
Deletes a registry key from 32 or 64 bit registry view

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	Registry key or one of win32con.HKEY_* values

	 _SubKey_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of subkey to be deleted.

	 _samDesired=0_ : int

	Can be KEY_WOW64_32KEY or KEY_WOW64_64KEY to specify alternate registry view

	 _Transaction=None_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to a transaction as returned by[win32transaction::CreateTransaction](#win32transaction.md#win32transaction_CreateTransaction_meth)

#### Comments
Accepts keyword args.
Requires 64-bit XP, Vista, or later.
Key to be deleted cannot contain subkeys
If a transaction handle is specified, RegDeleteKeyTransacted is called

#### Win32 API References


	Search for _RegDeleteKeyEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKeyEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKeyEx),[google](#http://www.google.com/search?q=RegDeleteKeyEx.md#http://www.google.com/search?q=RegDeleteKeyEx)or[google groups](#http://groups.google.com/groups?q=RegDeleteKeyEx.md#http://groups.google.com/groups?q=RegDeleteKeyEx).

	Search for _RegDeleteKeyTransacted_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKeyTransacted.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKeyTransacted),[google](#http://www.google.com/search?q=RegDeleteKeyTransacted.md#http://www.google.com/search?q=RegDeleteKeyTransacted)or[google groups](#http://groups.google.com/groups?q=RegDeleteKeyTransacted.md#http://groups.google.com/groups?q=RegDeleteKeyTransacted).

## [win32api](#win32api.md#win32api).RegDeleteKey

 **RegDeleteKey( _key_  _, subKey_ ** )
Deletes the specified key.  This method can not delete keys with subkeys.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _subKey_ : string

	The name of the key to delete. 

This key must be a subkey of the key identified by the key parameter. 

This value must not be None, and the key may not have subkeys.

#### Comments
If the method succeeds, the entire key, including all of its values, is removed. 

If the method fails, and exception is raised.

#### Win32 API References


	Search for _RegDeleteKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKey),[google](#http://www.google.com/search?q=RegDeleteKey.md#http://www.google.com/search?q=RegDeleteKey)or[google groups](#http://groups.google.com/groups?q=RegDeleteKey.md#http://groups.google.com/groups?q=RegDeleteKey).

## [win32api](#win32api.md#win32api).RegDeleteTree

 **RegDeleteTree( _Key_  _, SubKey_ ** )
Recursively deletes a key's subkeys and values

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Handle to a registry key

	 _SubKey_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of subkey to be deleted, or None for all subkeys and values

#### Comments
Accepts keyword args.
Requires Vista or later.

## [win32api](#win32api.md#win32api).RegDeleteValue

 **RegDeleteValue( _key_  _, value_ ** )
Removes a named value from the specified registry key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _value_ : string

	The name of the value to remove.

#### Win32 API References


	Search for _RegDeleteValue_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteValue.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteValue),[google](#http://www.google.com/search?q=RegDeleteValue.md#http://www.google.com/search?q=RegDeleteValue)or[google groups](#http://groups.google.com/groups?q=RegDeleteValue.md#http://groups.google.com/groups?q=RegDeleteValue).

## [win32api](#win32api.md#win32api).RegEnumKeyExW

tuple = **RegEnumKeyExW( _Key_ ** )
Unicode version of RegEnumKeyEx

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Registry handle opened with KEY_ENUMERATE_SUB_KEYS, or one of win32con.HKEY_* constants

#### Return Value
Returns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

## [win32api](#win32api.md#win32api).RegEnumKeyEx

tuple = **RegEnumKeyEx( _Key_ ** )
Lists subkeys of a registry key

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS.

#### Return Value
Returns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

## [win32api](#win32api.md#win32api).RegEnumKey

string = **RegEnumKey( _key_  _, index_ ** )
Enumerates subkeys of the specified open registry key. The function retrieves the name of one subkey each time it is called.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _index_ : int

	The index of the key to retrieve.

#### Win32 API References


	Search for _RegEnumKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegEnumKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegEnumKey),[google](#http://www.google.com/search?q=RegEnumKey.md#http://www.google.com/search?q=RegEnumKey)or[google groups](#http://groups.google.com/groups?q=RegEnumKey.md#http://groups.google.com/groups?q=RegEnumKey).

## [win32api](#win32api.md#win32api).RegEnumValue

(string,object,type) = **RegEnumValue( _key_  _, index_ ** )
Enumerates values of the specified open registry key. The function retrieves the name of one subkey each time it is called.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _index_ : int

	The index of the key to retrieve.

#### Comments
This function is typically called repeatedly, until an exception is raised, indicating no more values.

#### Win32 API References


	Search for _PyRegEnumValue_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PyRegEnumValue.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PyRegEnumValue),[google](#http://www.google.com/search?q=PyRegEnumValue.md#http://www.google.com/search?q=PyRegEnumValue)or[google groups](#http://groups.google.com/groups?q=PyRegEnumValue.md#http://groups.google.com/groups?q=PyRegEnumValue).

## [win32api](#win32api.md#win32api).RegFlushKey

 **RegFlushKey( _key_ ** )
Writes all the attributes of the specified key to the registry.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

#### Comments
It is not necessary to call RegFlushKey to change a key. 

Registry changes are flushed to disk by the registry using its lazy flusher. 

Registry changes are also flushed to disk at system shutdown.
Unlike[win32api::RegCloseKey](#win32api.md#win32api_RegCloseKey_meth), the RegFlushKey method returns only when all the data has been written to the registry.
An application should only call RegFlushKey if it requires absolute certainty that registry changes are on disk. If you don't know whether a RegFlushKey call is required, it probably isn't.

#### Win32 API References


	Search for _RegFlushKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegFlushKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegFlushKey),[google](#http://www.google.com/search?q=RegFlushKey.md#http://www.google.com/search?q=RegFlushKey)or[google groups](#http://groups.google.com/groups?q=RegFlushKey.md#http://groups.google.com/groups?q=RegFlushKey).

## [win32api](#win32api.md#win32api).RegGetKeySecurity

[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)= **RegGetKeySecurity( _key_  _, security_info_ ** )
Retrieves the security on the specified registry key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	Handle to an open key for which the security descriptor is set.

	 _security_info_ : int

	Specifies the components of the security descriptor to retrieve. The value can be a combination of the *_SECURITY_INFORMATION constants.

#### Win32 API References


	Search for _RegGetKeySecurity_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegGetKeySecurity.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegGetKeySecurity),[google](#http://www.google.com/search?q=RegGetKeySecurity.md#http://www.google.com/search?q=RegGetKeySecurity)or[google groups](#http://groups.google.com/groups?q=RegGetKeySecurity.md#http://groups.google.com/groups?q=RegGetKeySecurity).

## [win32api](#win32api.md#win32api).RegLoadKey

 **RegLoadKey( _key_  _, subKey_  _, filename_ ** )
The RegLoadKey method creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE 

and stores registration information from a specified file into that subkey.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _subKey_ : string

	The name of the key to delete. 

This key must be a subkey of the key identified by the key parameter. 

This value must not be None, and the key may not have subkeys.

	 _filename_ : string

	The name of the file to load registry data from. 

This file must have been created with the[win32api::RegSaveKey](#win32api.md#win32api_RegSaveKey_meth)function. 

Under the file allocation table (FAT) file system, the filename may not have an extension.

#### Comments
A call to RegLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege.
If hkey is a handle returned by[win32api::RegConnectRegistry](#win32api.md#win32api_RegConnectRegistry_meth), then the path specified in fileName is relative to the remote computer.

#### Win32 API References


	Search for _RegLoadKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegLoadKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegLoadKey),[google](#http://www.google.com/search?q=RegLoadKey.md#http://www.google.com/search?q=RegLoadKey)or[google groups](#http://groups.google.com/groups?q=RegLoadKey.md#http://groups.google.com/groups?q=RegLoadKey).

## [win32api](#win32api.md#win32api).RegNotifyChangeKeyValue

 **RegNotifyChangeKeyValue( _key_  _, bWatchSubTree_  _, dwNotifyFilter_  _, hKey_  _, fAsynchronous_ ** )
Receive notification of registry changes

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	Handle to an open registry key

	 _bWatchSubTree_ : int

	Boolean, notify of changes to subkeys if True

	 _dwNotifyFilter_ : int

	Combination of REG_NOTIFY_CHANGE_* constants

	 _hKey_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Event handle to be signalled, use None if fAsynchronous is False

	 _fAsynchronous_ : int

	Boolean, function returns immediately if True, waits for change if False

## [win32api](#win32api.md#win32api).RegOpenCurrentUser

[PyHKEY](#PyHKEY.md#PyHKEY)= **RegOpenCurrentUser( _samDesired_ ** )
Opens HKEY_CURRENT_USER for impersonated user

#### Parameters


	 _samDesired=MAXIMUM_ALLOWED_ : int

	Desired access, combination of win32con.KEY_*

#### Win32 API References


	Search for _RegOpenCurrentUser_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenCurrentUser.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenCurrentUser),[google](#http://www.google.com/search?q=RegOpenCurrentUser.md#http://www.google.com/search?q=RegOpenCurrentUser)or[google groups](#http://groups.google.com/groups?q=RegOpenCurrentUser.md#http://groups.google.com/groups?q=RegOpenCurrentUser).

## [win32api](#win32api.md#win32api).RegOpenKeyEx

[PyHKEY](#PyHKEY.md#PyHKEY)= **RegOpenKeyEx( _key_  _, subKey_  _, reserved_  _, sam_ ** )
Opens the specified key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _subKey_ : string

	The name of a key that this method opens. 

This key must be a subkey of the key identified by the key parameter. 

If key is one of the predefined keys, subKey may be None. In that case, 

the handle returned is the same key handle passed in to the function.

	 _reserved=0_ : int

	Reserved.  Must be zero.

	 _sam=KEY_READ_ : int

	Specifies an access mask that describes the desired security access for the new key. This parameter can be a combination of the following win32con constants:
KEY_ALL_ACCESS
KEY_CREATE_LINK
KEY_CREATE_SUB_KEY
KEY_ENUMERATE_SUB_KEYS
KEY_EXECUTE
KEY_NOTIFY
KEY_QUERY_VALUE
KEY_READ
KEY_SET_VALUE
KEY_WRITE


#### Win32 API References


	Search for _RegOpenKeyEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenKeyEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenKeyEx),[google](#http://www.google.com/search?q=RegOpenKeyEx.md#http://www.google.com/search?q=RegOpenKeyEx)or[google groups](#http://groups.google.com/groups?q=RegOpenKeyEx.md#http://groups.google.com/groups?q=RegOpenKeyEx).

#### Return Value
The return value is the handle of the opened key. 

If the function fails, an exception is raised.

## [win32api](#win32api.md#win32api).RegOpenKeyTransacted

[PyHKEY](#PyHKEY.md#PyHKEY)= **RegOpenKeyTransacted( _Key_  _, SubKey_  _, samDesired_  _, Transaction_  _, Options_ ** )
Opens a registry key as part of a transaction

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	Registry key or one of win32con.HKEY_* values

	 _SubKey_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of subkey to open.  Can be None to reopen an existing key.

	 _samDesired_ : int

	Access allowed to handle, combination of win32con.KEY_* constants.  Can also contain 

standard access rights such as DELETE, WRITE_OWNER, etc.

	 _Transaction_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to a transaction as returned by[win32transaction::CreateTransaction](#win32transaction.md#win32transaction_CreateTransaction_meth)

	 _Options=0_ : int

	Reserved, use only 0

#### Comments
Accepts keyword arguments.
Requires Vista or later.

#### Win32 API References


	Search for _RegOpenKeyTransacted_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenKeyTransacted.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenKeyTransacted),[google](#http://www.google.com/search?q=RegOpenKeyTransacted.md#http://www.google.com/search?q=RegOpenKeyTransacted)or[google groups](#http://groups.google.com/groups?q=RegOpenKeyTransacted.md#http://groups.google.com/groups?q=RegOpenKeyTransacted).

#### Return Value
Returns a transacted registry handle.  Note that operations on subkeys are not automatically transacted.

## [win32api](#win32api.md#win32api).RegOpenKey

[PyHKEY](#PyHKEY.md#PyHKEY)= **RegOpenKey(** )
Opens the specified key.

#### Comments
This funcion is implemented using[win32api::RegOpenKeyEx](#win32api.md#win32api_RegOpenKeyEx_meth), by taking advantage 

of default parameters.  See[win32api::RegOpenKeyEx](#win32api.md#win32api_RegOpenKeyEx_meth)for more details.

## [win32api](#win32api.md#win32api).RegOverridePredefKey

 **RegOverridePredefKey( _Key_  _, NewKey_ ** )
Redirects one of the predefined keys to different key

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	One of the predefined registry keys (win32con.HKEY_*)

	 _NewKey_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Registry key to which it will be redirected.  Pass None to restore original key.

#### Comments
Requires Windows 2000 or later.

#### Win32 API References


	Search for _RegOverridePredefKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOverridePredefKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOverridePredefKey),[google](#http://www.google.com/search?q=RegOverridePredefKey.md#http://www.google.com/search?q=RegOverridePredefKey)or[google groups](#http://groups.google.com/groups?q=RegOverridePredefKey.md#http://groups.google.com/groups?q=RegOverridePredefKey).

## [win32api](#win32api.md#win32api).RegQueryInfoKeyW

dict = **RegQueryInfoKeyW( _Key_ ** )
Returns information about an open registry key

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Handle to a registry key, or one of win32con.HKEY_* constants

#### Win32 API References


	Search for _RegQueryInfoKeyW_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryInfoKeyW.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryInfoKeyW),[google](#http://www.google.com/search?q=RegQueryInfoKeyW.md#http://www.google.com/search?q=RegQueryInfoKeyW)or[google groups](#http://groups.google.com/groups?q=RegQueryInfoKeyW.md#http://groups.google.com/groups?q=RegQueryInfoKeyW).

## [win32api](#win32api.md#win32api).RegQueryInfoKey

(int, int, long) = **RegQueryInfoKey( _key_ ** )
Returns the number of 

subkeys, the number of values a key has, 

and if available the last time the key was modified as 

100's of nanoseconds since Jan 1, 1600.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or or any one of the following win32con 

constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

#### Win32 API References


	Search for _RegQueryInfoKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryInfoKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryInfoKey),[google](#http://www.google.com/search?q=RegQueryInfoKey.md#http://www.google.com/search?q=RegQueryInfoKey)or[google groups](#http://groups.google.com/groups?q=RegQueryInfoKey.md#http://groups.google.com/groups?q=RegQueryInfoKey).

## [win32api](#win32api.md#win32api).RegQueryValueEx

(object,type) = **RegQueryValueEx( _key_  _, valueName_ ** )
Retrieves the type and data for a specified value name associated with an open registry key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _valueName_ : string

	The name of the value to query.

#### Comments
Values in the registry have name, type, and data components. This method 

retrieves the data for the given value.

#### Win32 API References


	Search for _RegQueryValueEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryValueEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryValueEx),[google](#http://www.google.com/search?q=RegQueryValueEx.md#http://www.google.com/search?q=RegQueryValueEx)or[google groups](#http://groups.google.com/groups?q=RegQueryValueEx.md#http://groups.google.com/groups?q=RegQueryValueEx).

## [win32api](#win32api.md#win32api).RegQueryValue

string = **RegQueryValue( _key_  _, subKey_ ** )
The RegQueryValue method retrieves the value associated with 

the unnamed value for a specified key in the registry.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _subKey_ : string

	The name of the subkey with which the value is associated. 

If this parameter is None or empty, the function retrieves the value set by the[win32api::RegSetValue](#win32api.md#win32api_RegSetValue_meth)method for the key identified by key.

#### Comments
Values in the registry have name, type, and data components. This method 

retrieves the data for a key's first value that has a NULL name. 

But the underlying API call doesn't return the type, Lame Lame Lame, DONT USE THIS!!!

#### Win32 API References


	Search for _RegQueryValue_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryValue.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryValue),[google](#http://www.google.com/search?q=RegQueryValue.md#http://www.google.com/search?q=RegQueryValue)or[google groups](#http://groups.google.com/groups?q=RegQueryValue.md#http://groups.google.com/groups?q=RegQueryValue).

## [win32api](#win32api.md#win32api).RegRestoreKey

 **RegRestoreKey( _Key_  _, File_  _, Flags_ ** )
Restores a key and subkeys from a saved registry file

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Handle to registry key to be restored.  Can also be one of win32con.HKEY_* values.

	 _File_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	File from which to restore registry data

	 _Flags=0_ : int

	One of REG_FORCE_RESTORE,REG_NO_LAZY_FLUSH,REG_REFRESH_HIVE,REG_WHOLE_HIVE_VOLATILE (from winnt)

#### Comments
Implemented only as Unicode (RegRestoreKeyW).  Accepts keyword arguments.
Requires SeBackupPrivilege and SeRestorePrivilege

#### Win32 API References


	Search for _RegRestoreKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegRestoreKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegRestoreKey),[google](#http://www.google.com/search?q=RegRestoreKey.md#http://www.google.com/search?q=RegRestoreKey)or[google groups](#http://groups.google.com/groups?q=RegRestoreKey.md#http://groups.google.com/groups?q=RegRestoreKey).

## [win32api](#win32api.md#win32api).RegSaveKeyEx

 **RegSaveKeyEx( _Key_  _, File_  _, SecurityAttributes_  _, Flags_ ** )
Extended version of RegSaveKey

#### Parameters


	 _Key_ :[PyHKEY](#PyHKEY.md#PyHKEY)

	Handle to a registry key or one of HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER

	 _File_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Name of file in which to save data.  File must not already exist.

	 _SecurityAttributes=None_ :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

	Specifies security for the file to be created

	 _Flags=REG_LATEST_FORMAT_ : int

	One of REG_STANDARD_FORMAT,REG_LATEST_FORMAT,REG_NO_COMPRESSION (from winnt.py)

#### Comments
Implemented only as Unicode (RegSaveKeyExW).  Accepts keyword arguments.
SE_BACKUP_NAME privilege must be enabled.

#### Win32 API References


	Search for _RegSaveKeyEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSaveKeyEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSaveKeyEx),[google](#http://www.google.com/search?q=RegSaveKeyEx.md#http://www.google.com/search?q=RegSaveKeyEx)or[google groups](#http://groups.google.com/groups?q=RegSaveKeyEx.md#http://groups.google.com/groups?q=RegSaveKeyEx).

## [win32api](#win32api.md#win32api).RegSaveKey

 **RegSaveKey( _key_  _, filename_  _, sa_ ** )
The RegSaveKey method saves the specified key, and all its subkeys to the specified file.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _filename_ : string

	The name of the file to save registry data to. 

This file cannot already exist. If this filename includes an extension, it cannot be used on file allocation table (FAT) file systems by the[win32api::RegLoadKey](#win32api.md#win32api_RegLoadKey_meth), **win32api::RegReplaceKey** , or[win32api::RegRestoreKey](#win32api.md#win32api_RegRestoreKey_meth)methods.

	 _sa=None_ :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

	The security attributes of the created file.

#### Comments
If key represents a key on a remote computer, the path described by fileName is relative to the remote computer.
The caller of this method must possess the SeBackupPrivilege security privilege.

#### Win32 API References


	Search for _RegSaveKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSaveKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSaveKey),[google](#http://www.google.com/search?q=RegSaveKey.md#http://www.google.com/search?q=RegSaveKey)or[google groups](#http://groups.google.com/groups?q=RegSaveKey.md#http://groups.google.com/groups?q=RegSaveKey).

## [win32api](#win32api.md#win32api).RegSetKeySecurity

 **RegSetKeySecurity( _key_  _, security_info_  _, sd_ ** )
Sets the security on the specified registry key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	Handle to an open key for which the security descriptor is set.

	 _security_info_ : int

	Specifies the components of the security descriptor to set. The value can be a combination of the *_SECURITY_INFORMATION constants.

	 _sd_ :[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)

	The new security descriptor for the key

#### Comments
If key is one of the predefined keys, the predefined key should be closed with[win32api::RegCloseKey](#win32api.md#win32api_RegCloseKey_meth). That ensures that the new security information is in effect the next time the predefined key is referenced.

#### Win32 API References


	Search for _PyRegSetKeySecurity_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PyRegSetKeySecurity.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PyRegSetKeySecurity),[google](#http://www.google.com/search?q=PyRegSetKeySecurity.md#http://www.google.com/search?q=PyRegSetKeySecurity)or[google groups](#http://groups.google.com/groups?q=PyRegSetKeySecurity.md#http://groups.google.com/groups?q=PyRegSetKeySecurity).

## [win32api](#win32api.md#win32api).RegSetValueEx

 **RegSetValueEx( _key_  _, valueName_  _, reserved_  _, type_  _, value_ ** )
Stores data in the value field of an open registry key.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _valueName_ : string

	The name of the value to set. 

If a value with this name is not already present in the key, the method adds it to the key.
If this parameter is None or an empty string and the type parameter is the win32api.REG_SZ type, this function sets the same value the[win32api::RegSetValue](#win32api.md#win32api_RegSetValue_meth)method would set.

	 _reserved_ : any

	Place holder for reserved argument.  Zero will always be passed to the API function.

	 _type_ : int

	Type of data.

 **Value**  **Meaning** REG_BINARYBinary data in any form.REG_DWORDA 32-bit number.REG_DWORD_LITTLE_ENDIANA 32-bit number in little-endian format. This is equivalent to REG_DWORD.
In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format.REG_QWORDA 64-bit number.REG_QWORD_LITTLE_ENDIANA 64-bit number in little-endian format. This is equivalent to REG_QWORD.
In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format. 

Windows NT and Windows 95 are designed to run on little-endian computer architectures. A user may connect to computers that have big-endian architectures, such as some UNIX systems.REG_DWORD_BIG_ENDIANA 32-bit number in big-endian format. 

In big-endian format, a multi-byte value is stored in memory from the highest byte (the big end) to the lowest byte. For example, the value 0x12345678 is stored as (0x12 0x34 0x56 0x78) in big-endian format.REG_EXPAND_SZA null-terminated string that contains unexpanded references to environment variables (for example, %PATH%). It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions.REG_LINKA Unicode symbolic link.REG_MULTI_SZAn array of null-terminated strings, terminated by two null characters.REG_NONENo defined value type.REG_RESOURCE_LISTA device-driver resource list.REG_SZA null-terminated string. It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions
	 _value_ : registry data

	The value to be stored with the specified value name.

#### Comments
This method can also set additional value and type information for the specified key.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access. 

To open the key, use the[win32api::RegCreateKeyEx](#win32api.md#win32api_RegCreateKeyEx_meth)or[win32api::RegOpenKeyEx](#win32api.md#win32api_RegOpenKeyEx_meth)methods.
Value lengths are limited by available memory. 

Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. 

This helps the registry perform efficiently.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access.

#### Win32 API References


	Search for _RegSetValueEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSetValueEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSetValueEx),[google](#http://www.google.com/search?q=RegSetValueEx.md#http://www.google.com/search?q=RegSetValueEx)or[google groups](#http://groups.google.com/groups?q=RegSetValueEx.md#http://groups.google.com/groups?q=RegSetValueEx).

## [win32api](#win32api.md#win32api).RegSetValue

 **RegSetValue( _key_  _, subKey_  _, type_  _, value_ ** )
Associates a value with a specified key.  Currently, only strings are supported.

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

	 _subKey_ : string

	The name of the subkey with which the value is associated. 

This parameter can be None or empty, in which case the value will be added to the key identified by the key parameter.

	 _type_ : int

	Type of data. Must be win32con.REG_SZ

	 _value_ : string

	The value to associate with the key.

#### Comments
If the key specified by the lpszSubKey parameter does not exist, the RegSetValue function creates it.
Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access.

#### Win32 API References


	Search for _RegSetValue_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSetValue.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSetValue),[google](#http://www.google.com/search?q=RegSetValue.md#http://www.google.com/search?q=RegSetValue)or[google groups](#http://groups.google.com/groups?q=RegSetValue.md#http://groups.google.com/groups?q=RegSetValue).

## [win32api](#win32api.md#win32api).RegUnLoadKey

 **RegUnLoadKey( _key_  _, subKey_ ** )
The RegUnLoadKey function unloads the specified registry key and its subkeys from the registry. 

The key should have been created by a previous call to[win32api::RegLoadKey](#win32api.md#win32api_RegLoadKey_meth).

#### Parameters


	 _key_ :[PyHKEY](#PyHKEY.md#PyHKEY)/int

	An already open key, or any one of the following win32con constants:
HKEY_USERS
HKEY_LOCAL_MACHINE

	 _subKey_ : string

	The name of the key to unload. 

This key must be a subkey of the key identified by the key parameter. 

This value must not be None.

#### Comments
A call to RegUnLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege.
If hkey is a handle returned by[win32api::RegConnectRegistry](#win32api.md#win32api_RegConnectRegistry_meth), then the path specified in fileName is relative to the remote computer.

#### Win32 API References


	Search for _RegUnLoadKey_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegUnLoadKey.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegUnLoadKey),[google](#http://www.google.com/search?q=RegUnLoadKey.md#http://www.google.com/search?q=RegUnLoadKey)or[google groups](#http://groups.google.com/groups?q=RegUnLoadKey.md#http://groups.google.com/groups?q=RegUnLoadKey).

## [win32api](#win32api.md#win32api).RegisterWindowMessage

 **RegisterWindowMessage( _msgString_ ** )
The RegisterWindowMessage method, given a string, returns a system wide unique 

message ID, suitable for sending messages between applications who both register the same string.

#### Parameters


	 _msgString_ : string

	The name of the message to register. 

All applications that register this message string will get the same message. 

ID back.  It will be unique in the system and suitable for applications to 

use to exchange messages.

#### Comments
Only use RegisterWindowMessage when more than one application must process the
same message. For sending private messages within a window class, an application
can use any integer in the range WM_USER through 0x7FFF. (Messages in this range
are private to a window class, not to an application. For example, predefined
control classes such as BUTTON, EDIT, LISTBOX, and COMBOBOX may use values in
this range.)

#### Win32 API References


	Search for _RegisterWindowMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegisterWindowMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegisterWindowMessage),[google](#http://www.google.com/search?q=RegisterWindowMessage.md#http://www.google.com/search?q=RegisterWindowMessage)or[google groups](#http://groups.google.com/groups?q=RegisterWindowMessage.md#http://groups.google.com/groups?q=RegisterWindowMessage).

## [win32api](#win32api.md#win32api).SearchPath

int = **SearchPath( _path_  _, fileName_  _, fileExt_ ** )
Searches a path for the specified file.

#### Parameters


	 _path_ : string

	The path to search.  If None, searches the standard paths.

	 _fileName_ : string

	The name of the file to search for.

	 _fileExt=None_ : string

	specifies an extension to be added to the filename when searching for the file. 

The first character of the filename extension must be a period (.). 

The extension is added only if the specified filename does not end with an extension. 

If a filename extension is not required or if the filename contains an extension, this parameter can be None.

#### Win32 API References


	Search for _SearchPath_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SearchPath.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SearchPath),[google](#http://www.google.com/search?q=SearchPath.md#http://www.google.com/search?q=SearchPath)or[google groups](#http://groups.google.com/groups?q=SearchPath.md#http://groups.google.com/groups?q=SearchPath).

#### Return Value
The return value is a tuple of (string, int).  string is the full 

path name located.  int is the offset in the string of the base name 

of the file.

## [win32api](#win32api.md#win32api).SendMessage

 **SendMessage( _hwnd_  _, idMessage_  _, wParam_  _, lParam_ ** )
Send a message to a window.

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The hWnd of the window to receive the message.

	 _idMessage_ : int

	The ID of the message to send.

	 _wParam=None_ : int/string

	The wParam for the message

	 _lParam=None_ : int/string

	The lParam for the message

#### Win32 API References


	Search for _SendMessage_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SendMessage.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SendMessage),[google](#http://www.google.com/search?q=SendMessage.md#http://www.google.com/search?q=SendMessage)or[google groups](#http://groups.google.com/groups?q=SendMessage.md#http://groups.google.com/groups?q=SendMessage).

## [win32api](#win32api.md#win32api).SetClassLong

int = **SetClassLong( _hwnd_  _, offset_  _, val_ ** )
Replaces the specified 32 or 64 bit value at the specified offset into the extra class memory for the window.

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle to the window.

	 _offset_ : int

	Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

	 _val_ : int

	Specifies the long value to place in the window's reserved memory.

#### Comments
This function calls the SetClassLongPtr Api function

## [win32api](#win32api.md#win32api).SetClassWord

int = **SetClassWord( _hwnd_  _, offset_  _, val_ ** )


#### Parameters


	 _hwnd_ : int

	The handle to the window.

	 _offset_ : int

	Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

	 _val_ : int

	Specifies the long value to place in the window's reserved memory.

#### Comments
This function is obsolete, use[win32api::SetClassLong](#win32api.md#win32api_SetClassLong_meth)instead

## [win32api](#win32api.md#win32api).SetConsoleCtrlHandler

 **SetConsoleCtrlHandler( _ctrlHandler_  _, bAdd_ ** )
Adds or removes an application-defined HandlerRoutine function from the list of handler functions for the calling process.

#### Parameters


	 _ctrlHandler_ : callable

	The function to call.  This function 

should accept one param - the type of signal.

	 _bAdd_ : int

	True if the handler is being added, false if removed.

#### Comments
Note that the implementation is a single CtrlHandler in C, which 

keeps a list of the handlers added by this function.  So although this 

function uses the same semantics as the Win32 function (ie, last 

registered first called, and first to return True stops the calls) the 

true order of all Python and C implemented CtrlHandlers may not match 

what would happen if all were implemented in C.
This handler must acquire the Python lock before it can call any 

of the registered handlers.  This means the handler may not be called 

until the current Python thread yields the lock.
A console process can use the[win32api::GenerateConsoleCtrlEvent](#win32api.md#win32api_GenerateConsoleCtrlEvent_meth)function to send a CTRL+C or CTRL+BREAK signal to a console process 

group.
The system generates CTRL_CLOSE_EVENT, CTRL_LOGOFF_EVENT, and 

CTRL_SHUTDOWN_EVENT signals when the user closes the console, logs off, 

or shuts down the system so that the process has an opportunity to 

clean up before termination.

#### Win32 API References


	Search for _SetConsoleCtrlHandler_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetConsoleCtrlHandler.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetConsoleCtrlHandler),[google](#http://www.google.com/search?q=SetConsoleCtrlHandler.md#http://www.google.com/search?q=SetConsoleCtrlHandler)or[google groups](#http://groups.google.com/groups?q=SetConsoleCtrlHandler.md#http://groups.google.com/groups?q=SetConsoleCtrlHandler).

## [win32api](#win32api.md#win32api).SetConsoleTitle

 **SetConsoleTitle( _title_ ** )
Sets the title for the current console.

#### Parameters


	 _title_ : string

	The new title

#### Win32 API References


	Search for _SetConsoleTitle_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetConsoleTitle.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetConsoleTitle),[google](#http://www.google.com/search?q=SetConsoleTitle.md#http://www.google.com/search?q=SetConsoleTitle)or[google groups](#http://groups.google.com/groups?q=SetConsoleTitle.md#http://groups.google.com/groups?q=SetConsoleTitle).

## [win32api](#win32api.md#win32api).SetCursorPos

 **SetCursorPos( _x,y_ ** )
The SetCursorPos function moves the cursor to the specified screen coordinates.

#### Parameters


	 _x,y_ : (int, int)

	The new position.

#### Win32 API References


	Search for _SetCursorPos_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetCursorPos.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetCursorPos),[google](#http://www.google.com/search?q=SetCursorPos.md#http://www.google.com/search?q=SetCursorPos)or[google groups](#http://groups.google.com/groups?q=SetCursorPos.md#http://groups.google.com/groups?q=SetCursorPos).

## [win32api](#win32api.md#win32api).SetCursor

[PyHANDLE](#PyHANDLE.md#PyHANDLE)= **SetCursor( _hCursor_ ** )
Set the cursor to the HCURSOR object.

#### Parameters


	 _hCursor_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The new cursor. Can be None to remove cursor.

#### Win32 API References


	Search for _SetCursor_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetCursor.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetCursor),[google](#http://www.google.com/search?q=SetCursor.md#http://www.google.com/search?q=SetCursor)or[google groups](#http://groups.google.com/groups?q=SetCursor.md#http://groups.google.com/groups?q=SetCursor).

#### Return Value
The result is the previous cursor if there was one.

## [win32api](#win32api.md#win32api).SetDllDirectory

 **SetDllDirectory( _PathName_ ** )
Modifies the application-specific DLL search path

#### Parameters


	 _PathName_ :[PyUnicode](#PyUnicode.md#PyUnicode)

	Directory to be added to search path, can be None to restore defaults

#### Win32 API References


	Search for _SetDllDirectory_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetDllDirectory.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetDllDirectory),[google](#http://www.google.com/search?q=SetDllDirectory.md#http://www.google.com/search?q=SetDllDirectory)or[google groups](#http://groups.google.com/groups?q=SetDllDirectory.md#http://groups.google.com/groups?q=SetDllDirectory).

## [win32api](#win32api.md#win32api).SetEnvironmentVariableW

 **SetEnvironmentVariableW( _Name_  _, Value_ ** )
Creates, deletes, or changes the value of an environment variable.

#### Parameters


	 _Name_ : str

	Name of the environment variable

	 _Value_ : str

	Value to be set, or None to remove variable

#### Win32 API References


	Search for _SetEnvironmentVariable_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetEnvironmentVariable.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetEnvironmentVariable),[google](#http://www.google.com/search?q=SetEnvironmentVariable.md#http://www.google.com/search?q=SetEnvironmentVariable)or[google groups](#http://groups.google.com/groups?q=SetEnvironmentVariable.md#http://groups.google.com/groups?q=SetEnvironmentVariable).

## [win32api](#win32api.md#win32api).SetEnvironmentVariable

 **SetEnvironmentVariable( _Name_  _, Value_ ** )
Creates, deletes, or changes the value of an environment variable.

#### Parameters


	 _Name_ : str/unicode

	Name of the environment variable

	 _Value_ : str/unicode

	Value to be set, use None to remove variable

#### Win32 API References


	Search for _SetEnvironmentVariable_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetEnvironmentVariable.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetEnvironmentVariable),[google](#http://www.google.com/search?q=SetEnvironmentVariable.md#http://www.google.com/search?q=SetEnvironmentVariable)or[google groups](#http://groups.google.com/groups?q=SetEnvironmentVariable.md#http://groups.google.com/groups?q=SetEnvironmentVariable).

## [win32api](#win32api.md#win32api).SetErrorMode

int = **SetErrorMode( _errorMode_ ** )
Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.

#### Parameters


	 _errorMode_ : int

	A set of bit flags that specify the process error mode

#### Win32 API References


	Search for _SetErrorMode_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetErrorMode.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetErrorMode),[google](#http://www.google.com/search?q=SetErrorMode.md#http://www.google.com/search?q=SetErrorMode)or[google groups](#http://groups.google.com/groups?q=SetErrorMode.md#http://groups.google.com/groups?q=SetErrorMode).

#### Return Value
The result is an integer containing the old error flags.

## [win32api](#win32api.md#win32api).SetFileAttributes

int = **SetFileAttributes( _pathName_  _, attrs_ ** )
Sets the named file's attributes.

#### Parameters


	 _pathName_ : string

	The name of the file.

	 _attrs_ : int

	The attributes to set.  Must be a combination of the win32con.FILE_ATTRIBUTE_* constants.

## [win32api](#win32api.md#win32api).SetHandleInformation

 **SetHandleInformation( _Object_  _, Mask_  _, Flags_ ** )
Sets a handles's flags

#### Parameters


	 _Object_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to an object

	 _Mask_ : int

	Bitmask specifying which flags should be set

	 _Flags_ : int

	Bitmask of flag values to be set. Valid Flags are HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE

#### Comments
Not available on Win98/Me

## [win32api](#win32api.md#win32api).SetLastError

int = **SetLastError(** )
Sets the calling thread's last error code value.

#### Win32 API References


	Search for _SetLastError_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetLastError.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetLastError),[google](#http://www.google.com/search?q=SetLastError.md#http://www.google.com/search?q=SetLastError)or[google groups](#http://groups.google.com/groups?q=SetLastError.md#http://groups.google.com/groups?q=SetLastError).

## [win32api](#win32api.md#win32api).SetLocalTime

 **SetLocalTime( _SystemTime_ ** )
Changes the system's local time

#### Parameters


	 _SystemTime_ :[PyTime](#PyTime.md#PyTime)

	The local time to be set.  Can also be a time tuple.

## [win32api](#win32api.md#win32api).SetStdHandle

 **SetStdHandle( _handle_  _, handle_ ** )
Set the handle for the standard input, standard output, or standard error device

#### Parameters


	 _handle_ : int

	input, output, or error device

	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)/int

	A previously opened handle to be a standard handle

## [win32api](#win32api.md#win32api).SetSysColors

 **SetSysColors( _Elements_  _, RgbValues_ ** )
Changes color of various window elements

#### Parameters


	 _Elements_ : tuple

	A tuple of ints, COLOR_* constants indicating which window element to change

	 _RgbValues_ : tuple

	An equal length tuple of ints representing RGB values (see[win32api::RGB](#win32api.md#win32api_RGB_meth))

## [win32api](#win32api.md#win32api).SetSystemFileCacheSize

 **SetSystemFileCacheSize( _MinimumFileCacheSize_  _, MaximumFileCacheSize_  _, Flags_ ** )
Sets the amount of memory reserved for file cache

#### Parameters


	 _MinimumFileCacheSize_ : long

	Minimum size in bytes.

	 _MaximumFileCacheSize_ : long

	Maximum size in bytes.

	 _Flags=0_ : int

	Combination of win32con.MM_WORKING_SET_* flags

#### Comments
Requires SE_INCREASE_QUOTA_NAME priv
Pass -1 for both min and max to flush file cache.
Accepts keyword args.

## [win32api](#win32api.md#win32api).SetSystemPowerState

 **SetSystemPowerState( _Suspend_  _, Force_ ** )
Initiates low power mode to make system sleep or hibernate

#### Parameters


	 _Suspend_ : boolean

	True - system is suspended. False - initiates hibernation.

	 _Force_ : boolean

	True - power state occurs unconditionally. False - applications are queried for permission.

#### Comments
Requires Win2k or later.
SE_SHUTDOWN_NAME privilege must be enabled.

#### Win32 API References


	Search for _SetSystemPowerState_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetSystemPowerState.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetSystemPowerState),[google](#http://www.google.com/search?q=SetSystemPowerState.md#http://www.google.com/search?q=SetSystemPowerState)or[google groups](#http://groups.google.com/groups?q=SetSystemPowerState.md#http://groups.google.com/groups?q=SetSystemPowerState).

## [win32api](#win32api.md#win32api).SetSystemTime

int = **SetSystemTime( _year_  _, month_  _, dayOfWeek_  _, day_  _, hour_  _, minute_  _, second_  _, millseconds_ ** )
Returns the current system time

#### Parameters


	 _year_ : int

	

	 _month_ : int

	

	 _dayOfWeek_ : int

	

	 _day_ : int

	

	 _hour_ : int

	

	 _minute_ : int

	

	 _second_ : int

	

	 _millseconds_ : int

	

## [win32api](#win32api.md#win32api).SetThreadLocale

 **SetThreadLocale( _lcid_ ** )
Sets the current thread's locale.

#### Parameters


	 _lcid_ : int

	The new LCID

## [win32api](#win32api.md#win32api).SetTimeZoneInformation

tuple = **SetTimeZoneInformation( _tzi_ ** )
Sets the system time-zone information.

#### Parameters


	 _tzi_ : tuple

	A tuple with the timezone info

#### Comments
The tuple is of form:

#### Items


	[0] _int_ : Bias

	

	[1] _string_ : StandardName

	

	[2] _SYSTEMTIME tuple_ : StandardDate

	

	[3] _int_ : StandardBias

	

	[4] _string_ : DaylightName

	

	[5] _SYSTEMTIME tuple_ : DaylightDate

	

	[6] _int_ : DaylightBias

	

## [win32api](#win32api.md#win32api).SetWindowLong

int = **SetWindowLong( _hwnd_  _, offset_  _, val_ ** )
Places a long value at the specified offset into the extra window memory of the given window.

#### Parameters


	 _hwnd_ : int

	The handle to the window.

	 _offset_ : int

	Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

	 _val_ : int

	Specifies the long value to place in the window's reserved memory.

#### Comments
This function calls the SetWindowLongPtr Api function

## [win32api](#win32api.md#win32api).SetWindowWord

int = **SetWindowWord( _hwnd_  _, offset_  _, val_ ** )


#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle to the window.

	 _offset_ : int

	Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

	 _val_ : int

	Specifies the long value to place in the window's reserved memory.

#### Comments
This function is obsolete, use[win32api::SetWindowLong](#win32api.md#win32api_SetWindowLong_meth)instead

## [win32api](#win32api.md#win32api).ShellExecute

int = **ShellExecute( _hwnd_  _, op_  _, file_  _, params_  _, dir_  _, bShow_ ** )
Opens or prints a file.

#### Parameters


	 _hwnd_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle of the parent window, or 0 for no parent.  This window receives any message boxes an application produces (for example, for error reporting).

	 _op_ : string

	The operation to perform.  May be "open", "print", or None, which defaults to "open".

	 _file_ : string

	The name of the file to open.

	 _params_ : string

	The parameters to pass, if the file name contains an executable.  Should be None for a document file.

	 _dir_ : string

	The initial directory for the application.

	 _bShow_ : int

	Specifies whether the application is shown when it is opened. If the lpszFile parameter specifies a document file, this parameter is zero.

#### Win32 API References


	Search for _ShellExecute_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ShellExecute.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ShellExecute),[google](#http://www.google.com/search?q=ShellExecute.md#http://www.google.com/search?q=ShellExecute)or[google groups](#http://groups.google.com/groups?q=ShellExecute.md#http://groups.google.com/groups?q=ShellExecute).

#### Return Value
The instance handle of the application that was run. (This handle could also be the handle of a dynamic data exchange [DDE] server application.) 

If there is an error, the method raises an exception.

## [win32api](#win32api.md#win32api).ShowCursor

int = **ShowCursor( _show_ ** )
The ShowCursor method displays or hides the cursor.

#### Parameters


	 _show_ : int

	Visiblilty flag

#### Comments
This function sets an internal display counter that 

determines whether the cursor should be displayed. The 

cursor is displayed only if the display count is greater 

than or equal to 0. If a mouse is installed, the initial display 

count is 0. If no mouse is installed, the display count is -1.

#### Win32 API References


	Search for _ShowCursor_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ShowCursor.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ShowCursor),[google](#http://www.google.com/search?q=ShowCursor.md#http://www.google.com/search?q=ShowCursor)or[google groups](#http://groups.google.com/groups?q=ShowCursor.md#http://groups.google.com/groups?q=ShowCursor).

#### Return Value
The return value specifies the new display counter

## [win32api](#win32api.md#win32api).Sleep

int = **Sleep( _time_  _, bAlterable_ ** )
Suspends execution of the current thread for the specified time.

#### Parameters


	 _time_ : int

	The number of milli-seconds to sleep for,

	 _bAlterable=0_ : int

	Specifies whether the function may terminate early due to an I/O completion callback function.

#### Win32 API References


	Search for _Sleep_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=Sleep.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=Sleep),[google](#http://www.google.com/search?q=Sleep.md#http://www.google.com/search?q=Sleep)or[google groups](#http://groups.google.com/groups?q=Sleep.md#http://groups.google.com/groups?q=Sleep).

	Search for _SleepEx_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SleepEx.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SleepEx),[google](#http://www.google.com/search?q=SleepEx.md#http://www.google.com/search?q=SleepEx)or[google groups](#http://groups.google.com/groups?q=SleepEx.md#http://groups.google.com/groups?q=SleepEx).

#### Return Value
The return value is zero if the specified time interval expired.

## [win32api](#win32api.md#win32api).TerminateProcess

 **TerminateProcess( _handle_  _, exitCode_ ** )
Kills a process

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The handle of the process to terminate.

	 _exitCode_ : int

	The exit code for the process.

#### Comments
See also[win32api::OpenProcess](#win32api.md#win32api_OpenProcess_meth)

## [win32api](#win32api.md#win32api).ToAsciiEx

bytes = **ToAsciiEx( _vk_  _, scancode_  _, keyboardstate_  _, flags_  _, hlayout_ ** )
Translates the specified virtual-key code and keyboard state to the corresponding character or characters.

#### Parameters


	 _vk_ : int

	The virtual key code.

	 _scancode_ : int

	The scan code.

	 _keyboardstate_ : bytes

	A string of exactly 256 characters.

	 _flags=0_ : int

	

	 _hlayout=None_ : handle

	The keyboard layout to use

## [win32api](#win32api.md#win32api).Unicode

[PyUnicode](#PyUnicode.md#PyUnicode)= **Unicode(** )
Creates a new Unicode object

## [win32api](#win32api.md#win32api).UpdateResource

 **UpdateResource( _handle_  _, type_  _, name_  _, data_  _, language_ ** )
Updates a resource in a PE file.

#### Parameters


	 _handle_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	The update-file handle.

	 _type_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	The type of resource to update

	 _name_ :[PyResourceId](#PyResourceId.md#PyResourceId)

	The id/name of the resource to update

	 _data_ : string

	The data to place into the resource.

	 _language=NEUTRAL_ : int

	Language to use, defaults to LANG_NEUTRAL.

## [win32api](#win32api.md#win32api).VkKeyScanEx

int = **VkKeyScanEx( _char_  _, hkl_ ** )
Translates a character to the corresponding virtual-key code and shift state.

#### Parameters


	 _char_ : string or unicode

	A byte or unicode string of length 1.  If a byte string is passed 

VkKeyScanExA will be called, otherwise VkKeyScanExW will be called.

	 _hkl_ :[PyHANDLE](#PyHANDLE.md#PyHANDLE)

	Handle to a keyboard layout at returned by[win32api::LoadKeyboardLayout](#win32api.md#win32api_LoadKeyboardLayout_meth)

#### Win32 API References


	Search for _VkKeyScanExA_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanExA.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanExA),[google](#http://www.google.com/search?q=VkKeyScanExA.md#http://www.google.com/search?q=VkKeyScanExA)or[google groups](#http://groups.google.com/groups?q=VkKeyScanExA.md#http://groups.google.com/groups?q=VkKeyScanExA).

	Search for _VkKeyScanExW_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanExW.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanExW),[google](#http://www.google.com/search?q=VkKeyScanExW.md#http://www.google.com/search?q=VkKeyScanExW)or[google groups](#http://groups.google.com/groups?q=VkKeyScanExW.md#http://groups.google.com/groups?q=VkKeyScanExW).

## [win32api](#win32api.md#win32api).VkKeyScan

int = **VkKeyScan( _char_  _, char_ ** )
Translates a character to the corresponding virtual-key code and shift state.

#### Parameters


	 _char_ : string or unicode

	A byte or unicode string of length 1.  If a byte string is passed 

VkKeyScanA will be called, otherwise VkKeyScanW will be called.

	 _char_ : chr

	Specifies a character

#### Win32 API References


	Search for _VkKeyScanA_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanA.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanA),[google](#http://www.google.com/search?q=VkKeyScanA.md#http://www.google.com/search?q=VkKeyScanA)or[google groups](#http://groups.google.com/groups?q=VkKeyScanA.md#http://groups.google.com/groups?q=VkKeyScanA).

	Search for _VkKeyScanW_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanW.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanW),[google](#http://www.google.com/search?q=VkKeyScanW.md#http://www.google.com/search?q=VkKeyScanW)or[google groups](#http://groups.google.com/groups?q=VkKeyScanW.md#http://groups.google.com/groups?q=VkKeyScanW).

## [win32api](#win32api.md#win32api).WinExec

 **WinExec( _cmdLine_  _, show_ ** )
Runs the specified application.

#### Parameters


	 _cmdLine_ : string

	The command line to execute.

	 _show=win32con.SW_SHOWNORMAL_ : int

	The initial state of the applications window.

#### Win32 API References


	Search for _WinExec_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinExec.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinExec),[google](#http://www.google.com/search?q=WinExec.md#http://www.google.com/search?q=WinExec)or[google groups](#http://groups.google.com/groups?q=WinExec.md#http://groups.google.com/groups?q=WinExec).

## [win32api](#win32api.md#win32api).WinHelp

 **WinHelp( _hwnd_  _, hlpFile_  _, cmd_  _, data_ ** )
Invokes the Windows Help system.

#### Parameters


	 _hwnd_ : int

	The handle of the window requesting help.

	 _hlpFile_ : string

	The name of the help file.

	 _cmd_ : int

	The type of help.  See the api for full details.

	 _data=0_ : int/string

	Additional data specific to the help call.

#### Win32 API References


	Search for _WinHelp_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHelp.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHelp),[google](#http://www.google.com/search?q=WinHelp.md#http://www.google.com/search?q=WinHelp)or[google groups](#http://groups.google.com/groups?q=WinHelp.md#http://groups.google.com/groups?q=WinHelp).

#### Return Value
The method raises an exception if an error occurs.

## [win32api](#win32api.md#win32api).WriteProfileSection

list = **WriteProfileSection( _section_  _, data_  _, iniName_ ** )
Writes a complete section to an INI file or registry.

#### Parameters


	 _section_ : string

	The section in the INI file to be written.

	 _data_ : string

	The data to write.  Can be None to delete the section.  Otherwise, must be string, 

with each entry terminated with '\\0', followed by another terminating '\\0'

	 _iniName=None_ : string

	Name of INI file.  If specified, WritePrivateProfileSection will be called.

#### Comments
This function is obsolete, applications should use the registry instead.

#### Win32 API References


	Search for _WriteProfileSection_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WriteProfileSection.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WriteProfileSection),[google](#http://www.google.com/search?q=WriteProfileSection.md#http://www.google.com/search?q=WriteProfileSection)or[google groups](#http://groups.google.com/groups?q=WriteProfileSection.md#http://groups.google.com/groups?q=WriteProfileSection).

	Search for _WritePrivateProfileSection_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WritePrivateProfileSection.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WritePrivateProfileSection),[google](#http://www.google.com/search?q=WritePrivateProfileSection.md#http://www.google.com/search?q=WritePrivateProfileSection)or[google groups](#http://groups.google.com/groups?q=WritePrivateProfileSection.md#http://groups.google.com/groups?q=WritePrivateProfileSection).

## [win32api](#win32api.md#win32api).WriteProfileVal

 **WriteProfileVal( _section_  _, entry_  _, value_  _, iniName_ ** )
Writes a value to a Windows INI file.

#### Parameters


	 _section_ : string

	The section in the INI file to write to.

	 _entry_ : string

	The entry within the section in the INI file to write to.

	 _value_ : int/string

	The value to write.

	 _iniName=None_ : string

	The name of the INI file.  If None, the system INI file is used.

#### Comments
This function is obsolete, applications should use the registry instead.

#### Win32 API References


	Search for _WritePrivateProfileString_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WritePrivateProfileString.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WritePrivateProfileString),[google](#http://www.google.com/search?q=WritePrivateProfileString.md#http://www.google.com/search?q=WritePrivateProfileString)or[google groups](#http://groups.google.com/groups?q=WritePrivateProfileString.md#http://groups.google.com/groups?q=WritePrivateProfileString).

	Search for _WriteProfileString_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WriteProfileString.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WriteProfileString),[google](#http://www.google.com/search?q=WriteProfileString.md#http://www.google.com/search?q=WriteProfileString)or[google groups](#http://groups.google.com/groups?q=WriteProfileString.md#http://groups.google.com/groups?q=WriteProfileString).

## [win32api](#win32api.md#win32api).keybd_event

 **keybd_event( _bVk_  _, bScan_  _, dwFlags_  _, dwExtraInfo_ ** )
Simulate a keyboard event

#### Parameters


	 _bVk_ : BYTE

	Virtual-key code

	 _bScan_ : BYTE

	Hardware scan code

	 _dwFlags=0_ : DWORD

	Flags specifying various function options

	 _dwExtraInfo=0_ : DWORD

	Additional data associated with keystroke

#### Win32 API References


	Search for _keybd_event_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=keybd.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=keybdevent),[google](#http://www.google.com/search?q=keybd.md#http://www.google.com/search?q=keybdevent)or[google groups](#http://groups.google.com/groups?q=keybd.md#http://groups.google.com/groups?q=keybdevent).

## [win32api](#win32api.md#win32api).mouse_event

 **mouse_event( _dwFlags_  _, dx_  _, dy_  _, dwData_  _, dwExtraInfo_ ** )
Simulate a mouse event

#### Parameters


	 _dwFlags=0_ : DWORD

	Flags specifying various function options

	 _dx_ : DWORD

	Horizontal position of mouse

	 _dy_ : DWORD

	Vertical position of mouse

	 _dwData_ : DWORD

	Flag specific parameter

	 _dwExtraInfo=0_ : DWORD

	Additional data associated with mouse event

#### Win32 API References


	Search for _mouse_event_ at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=mouse.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=mouseevent),[google](#http://www.google.com/search?q=mouse.md#http://www.google.com/search?q=mouseevent)or[google groups](#http://groups.google.com/groups?q=mouse.md#http://groups.google.com/groups?q=mouseevent).