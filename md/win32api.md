
<span id="win32api">win32api</span>
===

## Module win32api
A module, encapsulating the Windows Win32 API.

### Methods

[AbortSystemShutdown](#win32api.AbortSystemShutdown)

Aborts a system shutdown&nbsp;

[InitiateSystemShutdown](#win32api.InitiateSystemShutdown)

Initiates a shutdown and optional restart of the specified computer.&nbsp;

[Apply](#win32api.Apply)

Calls a Python function, but traps Win32 exceptions.&nbsp;

[Beep](#win32api.Beep)

Generates a simple tone on the speaker.&nbsp;

[BeginUpdateResource](#win32api.BeginUpdateResource)

Begins an update cycle for a PE file.&nbsp;

[ChangeDisplaySettings](#win32api.ChangeDisplaySettings)

Changes video mode for default display&nbsp;

[ChangeDisplaySettingsEx](#win32api.ChangeDisplaySettingsEx)

Changes video mode for specified display&nbsp;

[ClipCursor](#win32api.ClipCursor)

Confines the cursor to a rectangular area on the screen.&nbsp;

[CloseHandle](#win32api.CloseHandle)

Closes an open handle.&nbsp;

[CopyFile](#win32api.CopyFile)

Copy a file.&nbsp;

[DebugBreak](#win32api.DebugBreak)

Breaks into the C debugger.&nbsp;

[DeleteFile](#win32api.DeleteFile)

Deletes the specified file.&nbsp;

[DragQueryFile](#win32api.DragQueryFile)

Retrieve the file names for dropped files.&nbsp;

[DragFinish](#win32api.DragFinish)

Free memory associated with dropped files.&nbsp;

[DuplicateHandle](#win32api.DuplicateHandle)

Duplicates a handle.&nbsp;

[EndUpdateResource](#win32api.EndUpdateResource)

Ends a resource update cycle of a PE file.&nbsp;

[EnumDisplayDevices](#win32api.EnumDisplayDevices)

Obtain information about the display devices in a system&nbsp;

[EnumDisplayMonitors](#win32api.EnumDisplayMonitors)

Lists monitors for a device context&nbsp;

[EnumDisplaySettings](#win32api.EnumDisplaySettings)

Lists available modes for specified device&nbsp;

[EnumDisplaySettingsEx](#win32api.EnumDisplaySettingsEx)

Lists available modes for a display device, with optional flags&nbsp;

[EnumResourceLanguages](#win32api.EnumResourceLanguages)

List languages for specified resource&nbsp;

[EnumResourceNames](#win32api.EnumResourceNames)

Enumerates all the resources of the specified type from the nominated file.&nbsp;

[EnumResourceTypes](#win32api.EnumResourceTypes)

Return list of all resource types contained in module&nbsp;

[ExpandEnvironmentStrings](#win32api.ExpandEnvironmentStrings)

Expands environment-variable strings and replaces them with their defined values.&nbsp;

[ExitWindows](#win32api.ExitWindows)

Logs off the current user&nbsp;

[ExitWindowsEx](#win32api.ExitWindowsEx)

either logs off the current user, shuts down the system, or shuts down and restarts the system.&nbsp;

[FindFiles](#win32api.FindFiles)

Find files matching a file spec.&nbsp;

[FindFirstChangeNotification](#win32api.FindFirstChangeNotification)

Creates a change notification handle and sets up initial change notification filter conditions.&nbsp;

[FindNextChangeNotification](#win32api.FindNextChangeNotification)

Requests that the operating system signal a change notification handle the next time it detects an appropriate change.&nbsp;

[FindCloseChangeNotification](#win32api.FindCloseChangeNotification)

Closes the change notification handle.&nbsp;

[FindExecutable](#win32api.FindExecutable)

Find an executable associated with a document.&nbsp;

[FormatMessage](#win32api.FormatMessage)

Return an error message string.&nbsp;

[FormatMessageW](#win32api.FormatMessageW)

Return an error message string (as a Unicode object).&nbsp;

[FreeLibrary](#win32api.FreeLibrary)

Decrements the reference count of the loaded dynamic-link library (DLL) module.&nbsp;

[GenerateConsoleCtrlEvent](#win32api.GenerateConsoleCtrlEvent)

Send a specified signal to a console process group that shares the console associated with the calling process.&nbsp;

[GetAsyncKeyState](#win32api.GetAsyncKeyState)

Retrieves the asynch state of a virtual key code.&nbsp;

[GetCommandLine](#win32api.GetCommandLine)

Return the application's command line.&nbsp;

[GetComputerName](#win32api.GetComputerName)

Returns the local computer name&nbsp;

[GetComputerNameEx](#win32api.GetComputerNameEx)

Retrieves a NetBIOS or DNS name associated with the local computer&nbsp;

[GetComputerObjectName](#win32api.GetComputerObjectName)

Retrieves the local computer's name in a specified format&nbsp;

[GetMonitorInfo](#win32api.GetMonitorInfo)

Retrieves information for a monitor by handle&nbsp;

[GetUserName](#win32api.GetUserName)

Returns the current user name.&nbsp;

[GetUserNameEx](#win32api.GetUserNameEx)

Returns the current user name in format specified by Name* constants&nbsp;

[GetCursorPos](#win32api.GetCursorPos)

Returns the position of the cursor, in screen co-ordinates.&nbsp;

[GetCurrentThread](#win32api.GetCurrentThread)

Returns a pseudohandle for the current thread.&nbsp;

[GetCurrentThreadId](#win32api.GetCurrentThreadId)

Returns the thread ID for the current thread.&nbsp;

[GetCurrentProcessId](#win32api.GetCurrentProcessId)

Returns the thread ID for the current thread.&nbsp;

[GetCurrentProcess](#win32api.GetCurrentProcess)

Returns a pseudohandle for the current process.&nbsp;

[GetConsoleTitle](#win32api.GetConsoleTitle)

Return the application's console title.&nbsp;

[GetDateFormat](#win32api.GetDateFormat)

Formats a date as a date string for a specified locale.&nbsp;

[GetDiskFreeSpace](#win32api.GetDiskFreeSpace)

Retrieves information about a disk.&nbsp;

[GetDiskFreeSpaceEx](#win32api.GetDiskFreeSpaceEx)

Retrieves information about a disk.&nbsp;

[GetDllDirectory](#win32api.GetDllDirectory)

Retrieves the DLL search path&nbsp;

[GetDomainName](#win32api.GetDomainName)

Returns the current domain name&nbsp;

[GetEnvironmentVariable](#win32api.GetEnvironmentVariable)

Retrieves the value of an environment variable.&nbsp;

[GetEnvironmentVariableW](#win32api.GetEnvironmentVariableW)

Retrieves the value of an environment variable.&nbsp;

[GetFileAttributes](#win32api.GetFileAttributes)

Retrieves the attributes for the named file.&nbsp;

[GetFileVersionInfo](#win32api.GetFileVersionInfo)

Retrieves string version info&nbsp;

[GetFocus](#win32api.GetFocus)

Retrieves the handle of the keyboard focus window associated with the thread that called the method.&nbsp;

[GetFullPathName](#win32api.GetFullPathName)

Returns the full path of a (possibly relative) path&nbsp;

[GetHandleInformation](#win32api.GetHandleInformation)

Retrieves a handle's flags.&nbsp;

[GetKeyboardLayout](#win32api.GetKeyboardLayout)

Retrieves the active input locale identifier&nbsp;

[GetKeyboardLayoutList](#win32api.GetKeyboardLayoutList)

Returns a sequence of all locale ids in the system&nbsp;

[GetKeyboardLayoutName](#win32api.GetKeyboardLayoutName)

Retrieves the name of the active input locale identifier (formerly called the keyboard layout).&nbsp;

[GetKeyboardState](#win32api.GetKeyboardState)

Retrieves the status of the 256 virtual keys on the keyboard.&nbsp;

[GetKeyState](#win32api.GetKeyState)

Retrives the last known key state for a key.&nbsp;

[GetLastError](#win32api.GetLastError)

Retrieves the last error code known by the system.&nbsp;

[GetLastInputInfo](#win32api.GetLastInputInfo)

Returns time of last input event in tick count&nbsp;

[GetLocalTime](#win32api.GetLocalTime)

Returns the current local time.&nbsp;

[GetLongPathName](#win32api.GetLongPathName)

Converts the specified path to its long form.&nbsp;

[GetLongPathNameW](#win32api.GetLongPathNameW)

Converts the specified path to its long form.&nbsp;

[GetLogicalDrives](#win32api.GetLogicalDrives)

Returns a bitmask representing the currently available disk drives.&nbsp;

[GetLogicalDriveStrings](#win32api.GetLogicalDriveStrings)

Returns a list of strings for all the drives.&nbsp;

[GetModuleFileName](#win32api.GetModuleFileName)

Retrieves the filename of the specified module.&nbsp;

[GetModuleFileNameW](#win32api.GetModuleFileNameW)

Retrieves the unicode filename of the specified module.&nbsp;

[GetModuleHandle](#win32api.GetModuleHandle)

Returns the handle of an already loaded DLL.&nbsp;

[GetPwrCapabilities](#win32api.GetPwrCapabilities)

Retrieves system's power capabilities&nbsp;

[GetProfileSection](#win32api.GetProfileSection)

Returns a list of entries in an INI file.&nbsp;

[GetProcAddress](#win32api.GetProcAddress)

Returns the address of the specified exported dynamic-link library (DLL) function.&nbsp;

[GetProfileVal](#win32api.GetProfileVal)

Returns a value from an INI file.&nbsp;

[GetShortPathName](#win32api.GetShortPathName)

Returns the 8.3 version of a pathname.&nbsp;

[GetStdHandle](#win32api.GetStdHandle)

Returns a handle for the standard input, standard output, or standard error device&nbsp;

[GetSysColor](#win32api.GetSysColor)

Returns the system colors.&nbsp;

[GetSystemDefaultLangID](#win32api.GetSystemDefaultLangID)

Retrieves the system default language identifier.&nbsp;

[GetSystemDefaultLCID](#win32api.GetSystemDefaultLCID)

Retrieves the system default locale identifier.&nbsp;

[GetSystemDirectory](#win32api.GetSystemDirectory)

Returns the Windows system directory.&nbsp;

[GetSystemFileCacheSize](#win32api.GetSystemFileCacheSize)

Returns the amount of memory reserved for file cache&nbsp;

[SetSystemFileCacheSize](#win32api.SetSystemFileCacheSize)

Sets the amount of memory reserved for file cache&nbsp;

[GetSystemInfo](#win32api.GetSystemInfo)

Retrieves information about the current system.&nbsp;

[GetNativeSystemInfo](#win32api.GetNativeSystemInfo)

Retrieves information about the current system for a Wow64 process.&nbsp;

[GetSystemMetrics](#win32api.GetSystemMetrics)

Returns the specified system metrics.&nbsp;

[GetSystemTime](#win32api.GetSystemTime)

Returns the current system time.&nbsp;

[GetTempFileName](#win32api.GetTempFileName)

Creates a temporary file.&nbsp;

[GetTempPath](#win32api.GetTempPath)

Returns the path designated as holding temporary files.&nbsp;

[GetThreadLocale](#win32api.GetThreadLocale)

Returns the current thread's locale.&nbsp;

[GetTickCount](#win32api.GetTickCount)

Returns the milliseconds since windows started.&nbsp;

[GetTimeFormat](#win32api.GetTimeFormat)

Formats a time as a time string for a specified locale.&nbsp;

[GetTimeZoneInformation](#win32api.GetTimeZoneInformation)

Returns the system time-zone information.&nbsp;

[GetVersion](#win32api.GetVersion)

Returns Windows version information.&nbsp;

[GetVersionEx](#win32api.GetVersionEx)

Returns Windows version information as a tuple.&nbsp;

[GetVolumeInformation](#win32api.GetVolumeInformation)

Returns information about a volume and file system attached to the system.&nbsp;

[GetWindowsDirectory](#win32api.GetWindowsDirectory)

Returns the windows directory.&nbsp;

[GetWindowLong](#win32api.GetWindowLong)

Retrieves a long value at the specified offset into the extra window memory of the given window.&nbsp;

[GetUserDefaultLangID](#win32api.GetUserDefaultLangID)

Retrieves the user default language identifier.&nbsp;

[GetUserDefaultLCID](#win32api.GetUserDefaultLCID)

Retrieves the user default locale identifier.&nbsp;

[GlobalMemoryStatus](#win32api.GlobalMemoryStatus)

Returns systemwide memory usage&nbsp;

[GlobalMemoryStatusEx](#win32api.GlobalMemoryStatusEx)

Returns physical and virtual memory usage&nbsp;

[keybd_event](#win32api.keybd_event)

Simulate a keyboard event&nbsp;

[mouse_event](#win32api.mouse_event)

Simulate a mouse event&nbsp;

[LoadCursor](#win32api.LoadCursor)

Loads a cursor.&nbsp;

[LoadKeyboardLayout](#win32api.LoadKeyboardLayout)

Loads a new locale id&nbsp;

[LoadLibrary](#win32api.LoadLibrary)

Loads the specified DLL, and returns the handle.&nbsp;

[LoadLibraryEx](#win32api.LoadLibraryEx)

Loads the specified DLL, and returns the handle.&nbsp;

[LoadResource](#win32api.LoadResource)

Finds and loads a resource from a PE file.&nbsp;

[LoadString](#win32api.LoadString)

Loads a string from a resource file.&nbsp;

[MapVirtualKeyEx](#win32api.MapVirtualKeyEx)

Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code.&nbsp;

[MessageBeep](#win32api.MessageBeep)

Plays a predefined waveform sound.&nbsp;

[MessageBox](#win32api.MessageBox)

Display a message box.&nbsp;

[MonitorFromPoint](#win32api.MonitorFromPoint)

Finds monitor that contains a point&nbsp;

[MonitorFromRect](#win32api.MonitorFromRect)

Finds monitor that has largest intersection with a rectangle&nbsp;

[MonitorFromWindow](#win32api.MonitorFromWindow)

Finds monitor that contains a window&nbsp;

[MoveFile](#win32api.MoveFile)

Moves or renames a file.&nbsp;

[MoveFileEx](#win32api.MoveFileEx)

Moves or renames a file.&nbsp;

[OpenProcess](#win32api.OpenProcess)

Retrieves a handle to an existing process.&nbsp;

[OutputDebugString](#win32api.OutputDebugString)

Writes output to the Windows debugger.&nbsp;

[PostMessage](#win32api.PostMessage)

Post a message to a window.&nbsp;

[PostQuitMessage](#win32api.PostQuitMessage)

Posts a quit message.&nbsp;

[PostThreadMessage](#win32api.PostThreadMessage)

Post a message to a thread.&nbsp;

[RegCloseKey](#win32api.RegCloseKey)

Closes a registry key.&nbsp;

[RegConnectRegistry](#win32api.RegConnectRegistry)

Establishes a connection to a predefined registry handle on another computer.&nbsp;

[RegCopyTree](#win32api.RegCopyTree)

Copies an entire registry key to another location&nbsp;

[RegCreateKey](#win32api.RegCreateKey)

Creates the specified key, or opens the key if it already exists.&nbsp;

[RegCreateKeyEx](#win32api.RegCreateKeyEx)

Extended version of RegCreateKey&nbsp;

[RegDeleteKey](#win32api.RegDeleteKey)

Deletes the specified key.&nbsp;

[RegDeleteKeyEx](#win32api.RegDeleteKeyEx)

Deletes a registry key from 32 or 64 bit registry view&nbsp;

[RegDeleteTree](#win32api.RegDeleteTree)

Recursively deletes a key's subkeys and values&nbsp;

[RegDeleteValue](#win32api.RegDeleteValue)

Removes a named value from the specified registry key.&nbsp;

[RegEnumKey](#win32api.RegEnumKey)

Enumerates subkeys of the specified open registry key.&nbsp;

[RegEnumKeyEx](#win32api.RegEnumKeyEx)

Enumerates subkeys of the specified open registry key.&nbsp;

[RegEnumKeyExW](#win32api.RegEnumKeyExW)

Unicode version of RegEnumKeyEx&nbsp;

[RegEnumValue](#win32api.RegEnumValue)

Enumerates values of the specified open registry key.&nbsp;

[RegFlushKey](#win32api.RegFlushKey)

Writes all the attributes of the specified key to the registry.&nbsp;

[RegGetKeySecurity](#win32api.RegGetKeySecurity)

Retrieves the security on the specified registry key.&nbsp;

[RegLoadKey](#win32api.RegLoadKey)

Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and stores registration information from a specified file into that subkey.&nbsp;

[RegOpenCurrentUser](#win32api.RegOpenCurrentUser)

Opens HKEY_CURRENT_USER for impersonated user&nbsp;

[RegOpenKey](#win32api.RegOpenKey)

Alias for[win32api::RegOpenKeyEx](#win32api.RegOpenKeyEx)&nbsp;

[RegOpenKeyEx](#win32api.RegOpenKeyEx)

Opens the specified key.&nbsp;

[RegOpenKeyTransacted](#win32api.RegOpenKeyTransacted)

Opens a registry key as part of a transaction.&nbsp;

[RegOverridePredefKey](#win32api.RegOverridePredefKey)

Redirects one of the predefined keys to different key.&nbsp;

[RegQueryValue](#win32api.RegQueryValue)

Retrieves the value associated with the unnamed value for a specified key in the registry.&nbsp;

[RegQueryValueEx](#win32api.RegQueryValueEx)

Retrieves the type and data for a specified value name associated with an open registry key.&nbsp;

[RegQueryInfoKey](#win32api.RegQueryInfoKey)

Returns information about the specified key.&nbsp;

[RegQueryInfoKeyW](#win32api.RegQueryInfoKeyW)

Returns information about an open registry key&nbsp;

[RegRestoreKey](#win32api.RegRestoreKey)

Restores a key and subkeys from a saved registry file&nbsp;

[RegSaveKey](#win32api.RegSaveKey)

Saves the specified key, and all its subkeys to the specified file.&nbsp;

[RegSaveKeyEx](#win32api.RegSaveKeyEx)

Extended version of RegSaveKey&nbsp;

[RegSetKeySecurity](#win32api.RegSetKeySecurity)

Sets the security on the specified registry key.&nbsp;

[RegSetValue](#win32api.RegSetValue)

Associates a value with a specified key.  Currently, only strings are supported.&nbsp;

[RegSetValueEx](#win32api.RegSetValueEx)

Stores data in the value field of an open registry key.&nbsp;

[RegUnLoadKey](#win32api.RegUnLoadKey)

Unloads the specified registry key and its subkeys from the registry.  The keys must have been loaded previously by a call to RegLoadKey.&nbsp;

[RegisterWindowMessage](#win32api.RegisterWindowMessage)

Given a string, return a system wide unique message ID.&nbsp;

[RegNotifyChangeKeyValue](#win32api.RegNotifyChangeKeyValue)

Watch for registry changes&nbsp;

[SearchPath](#win32api.SearchPath)

Searches a path for a file.&nbsp;

[SendMessage](#win32api.SendMessage)

Send a message to a window.&nbsp;

[SetConsoleCtrlHandler](#win32api.SetConsoleCtrlHandler)

Adds or removes an application-defined HandlerRoutine function from the list of handler functions for the calling process.&nbsp;

[SetConsoleTitle](#win32api.SetConsoleTitle)

Sets the title for the current console.&nbsp;

[SetCursorPos](#win32api.SetCursorPos)

The SetCursorPos function moves the cursor to the specified screen coordinates.&nbsp;

[SetDllDirectory](#win32api.SetDllDirectory)

Modifies the application-specific DLL search path&nbsp;

[SetErrorMode](#win32api.SetErrorMode)

Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.&nbsp;

[SetFileAttributes](#win32api.SetFileAttributes)

Sets the named file's attributes.&nbsp;

[SetLastError](#win32api.SetLastError)

Sets the last error code known for the current thread.&nbsp;

[SetSysColors](#win32api.SetSysColors)

Changes color of various window elements&nbsp;

[SetLocalTime](#win32api.SetLocalTime)

Changes the system's local time.&nbsp;

[SetSystemTime](#win32api.SetSystemTime)

Sets the system time.&nbsp;

[SetClassLong](#win32api.SetClassLong)

Replaces the specified 32-bit (long) value at the specified offset into the extra class memory for the window.&nbsp;

[SetClassWord](#win32api.SetClassWord)

Replaces the specified 32-bit (long) value at the specified offset into the extra class memory for the window.&nbsp;

[SetWindowWord](#win32api.SetWindowWord)

&nbsp;

[SetCursor](#win32api.SetCursor)

Set the cursor to the HCURSOR object.&nbsp;

[SetEnvironmentVariable](#win32api.SetEnvironmentVariable)

Creates, deletes, or changes the value of an environment variable.&nbsp;

[SetEnvironmentVariable](#win32api.SetEnvironmentVariable)

Creates, deletes, or changes the value of an environment variable.&nbsp;

[SetEnvironmentVariableW](#win32api.SetEnvironmentVariableW)

Creates, deletes, or changes the value of an environment variable.&nbsp;

[SetHandleInformation](#win32api.SetHandleInformation)

Sets a handles's flags&nbsp;

[SetStdHandle](#win32api.SetStdHandle)

Sets a handle for the standard input, standard output, or standard error device&nbsp;

[SetSystemPowerState](#win32api.SetSystemPowerState)

Powers machine down to a suspended state&nbsp;

[SetThreadLocale](#win32api.SetThreadLocale)

Sets the current thread's locale.&nbsp;

[SetTimeZoneInformation](#win32api.SetTimeZoneInformation)

Sets the system time-zone information.&nbsp;

[SetWindowLong](#win32api.SetWindowLong)

Places a long value at the specified offset into the extra window memory of the given window.&nbsp;

[ShellExecute](#win32api.ShellExecute)

Executes an application.&nbsp;

[ShowCursor](#win32api.ShowCursor)

The ShowCursor method displays or hides the cursor.&nbsp;

[Sleep](#win32api.Sleep)

Suspends current application execution&nbsp;

[TerminateProcess](#win32api.TerminateProcess)

Terminates a process.&nbsp;

[ToAsciiEx](#win32api.ToAsciiEx)

Translates the specified virtual-key code and keyboard state to the corresponding character or characters.&nbsp;

[Unicode](#win32api.Unicode)

Creates a new[PyUnicode](#PyUnicode)object&nbsp;

[UpdateResource](#win32api.UpdateResource)

Updates a resource in a PE file.&nbsp;

[VkKeyScan](#win32api.VkKeyScan)

Translates a character to the corresponding virtual-key code and shift state.&nbsp;

[VkKeyScan](#win32api.VkKeyScan)

Translates a character to the corresponding virtual-key code and shift state.&nbsp;

[WinExec](#win32api.WinExec)

Execute a program.&nbsp;

[WinHelp](#win32api.WinHelp)

Invokes the Windows Help engine.&nbsp;

[WriteProfileSection](#win32api.WriteProfileSection)

Writes a complete section to an INI file or registry.&nbsp;

[WriteProfileVal](#win32api.WriteProfileVal)

Write a value to a Windows INI file.&nbsp;

[HIBYTE](#win32api.HIBYTE)

An interface to the win32api HIBYTE macro.&nbsp;

[LOBYTE](#win32api.LOBYTE)

An interface to the win32api LOBYTE macro.&nbsp;

[HIWORD](#win32api.HIWORD)

An interface to the win32api HIWORD macro.&nbsp;

[LOWORD](#win32api.LOWORD)

An interface to the win32api LOWORD macro.&nbsp;

[RGB](#win32api.RGB)

An interface to the win32api RGB macro.&nbsp;

[MAKELANGID](#win32api.MAKELANGID)

Creates a language identifier from a primary language identifier and a sublanguage identifier.&nbsp;

[MAKEWORD](#win32api.MAKEWORD)

creates a WORD value by concatenating the specified values.&nbsp;

[MAKELONG](#win32api.MAKELONG)

creates a LONG value by concatenating the specified values.&nbsp;

<span id="win32api.AbortSystemShutdown">win32api.AbortSystemShutdown</span>
===

## [win32api](#win32api).AbortSystemShutdown
 **AbortSystemShutdown(computerName** )
Aborts a system shutdown

### Parameters

computerName: string/[PyUnicode](#PyUnicode)

Specifies the name of the computer where the shutdown is to be stopped.

### Win32 API References

Search forAbortSystemShutdownat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown),[google](#http://www.google.com/search?q=AbortSystemShutdown)or[google groups](#http://groups.google.com/groups?q=AbortSystemShutdown).

<span id="win32api.Apply">win32api.Apply</span>
===

## [win32api](#win32api).Apply
object = **Apply(exceptionHandler, func, args** )
Calls a Python function, but traps Win32 exceptions.

### Parameters

exceptionHandler: object

An object which will be called when a win32 exception occurs.

func: object

The function call call under the protection of the Win32 exception handler.

args: tuple

Args for the function.

### CommentsCalls the specified function in a manner similar to 

the built-in function apply(), but allows Win32 exceptions 

to be handled by Python.  If a Win32 exception occurs calling 

the function, the specified exceptionHandler is called, and its 

return value determines the action taken.


<span id="win32api.Beep">win32api.Beep</span>
===

## [win32api](#win32api).Beep
 **Beep(freq, dur** )
Generates simple tones on the speaker.

### Parameters

freq: int

Specifies the frequency, in hertz, of the sound. This parameter must be in the range 37 through 32,767 (0x25 through 0x7FFF).

dur: int

Specifies the duration, in milliseconds, of the sound.~ 

One value has a special meaning: If dwDuration is  - 1, the function 

operates asynchronously and produces sound until called again.

### Win32 API References

Search forBeepat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=Beep),[google](#http://www.google.com/search?q=Beep)or[google groups](#http://groups.google.com/groups?q=Beep).

<span id="win32api.BeginUpdateResource">win32api.BeginUpdateResource</span>
===

## [win32api](#win32api).BeginUpdateResource
[PyHANDLE](#PyHANDLE)= **BeginUpdateResource(filename, delete** )
Begins an update cycle for a PE file.

### Parameters

filename: string

File in which to update resources.

delete: int

Flag to indicate that all existing resources should be deleted.

<span id="win32api.ChangeDisplaySettings">win32api.ChangeDisplaySettings</span>
===

## [win32api](#win32api).ChangeDisplaySettings
int = **ChangeDisplaySettings(DevMode, Flags** )
Changes video mode for default display

### Parameters

DevMode:[PyDEVMODE](#PyDEVMODE)

A PyDEVMODE object as returned from EnumDisplaySettings, or None to reset to default settings from registry

Flags: int

One of the win32con.CDS_* constants, or 0

### Return ValueReturns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

<span id="win32api.ChangeDisplaySettingsEx">win32api.ChangeDisplaySettingsEx</span>
===

## [win32api](#win32api).ChangeDisplaySettingsEx
int = **ChangeDisplaySettingsEx(DeviceName, DevMode, Flags** )
Changes video mode for specified display

### Parameters

DeviceName=None: str

Name of device as returned by[win32api::EnumDisplayDevices](#win32api.EnumDisplayDevices), use None for default display device

DevMode=None:[PyDEVMODE](#PyDEVMODE)

A PyDEVMODE object as returned from[win32api::EnumDisplaySettings](#win32api.EnumDisplaySettings), or None to reset to default settings from registry

Flags=0: int

One of the win32con.CDS_* constants, or 0

### CommentsAccepts keyword arguments

### Return ValueReturns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

<span id="win32api.ClipCursor">win32api.ClipCursor</span>
===

## [win32api](#win32api).ClipCursor
 **ClipCursor(left, top, right, bottom** )
Confines the cursor to a rectangular area on the screen.

### Parameters

left, top, right, bottom: (int, int, int, int)

contains the screen coordinates of the upper-left and lower-right corners of the confining rectangle. If this parameter is omitted or (0,0,0,0), the cursor is free to move anywhere on the screen.

### Win32 API References

Search forClipCursorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ClipCursor),[google](#http://www.google.com/search?q=ClipCursor)or[google groups](#http://groups.google.com/groups?q=ClipCursor).

<span id="win32api.CloseHandle">win32api.CloseHandle</span>
===

## [win32api](#win32api).CloseHandle
 **CloseHandle(handle** )
Closes an open handle.

### Parameters

handle:[PyHANDLE](#PyHANDLE)/int

A previously opened handle.

<span id="win32api.CopyFile">win32api.CopyFile</span>
===

## [win32api](#win32api).CopyFile
 **CopyFile(src, dest, bFailOnExist** )
Copies an existing file to a new file

### Parameters

src: string[PyUnicode](#PyUnicode)

Name of an existing file.

dest: string/[PyUnicode](#PyUnicode)

Name of file to copy to.

bFailOnExist=0: int

Indicates if the operation should fail if the file exists.

### Win32 API References

Search forCopyFileat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CopyFile),[google](#http://www.google.com/search?q=CopyFile)or[google groups](#http://groups.google.com/groups?q=CopyFile).

<span id="win32api.DebugBreak">win32api.DebugBreak</span>
===

## [win32api](#win32api).DebugBreak
 **DebugBreak(** )
Breaks into the C debugger

### Win32 API References

Search forDebugBreakat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DebugBreak),[google](#http://www.google.com/search?q=DebugBreak)or[google groups](#http://groups.google.com/groups?q=DebugBreak).

<span id="win32api.DeleteFile">win32api.DeleteFile</span>
===

## [win32api](#win32api).DeleteFile
 **DeleteFile(fileName** )
Deletes the specified file.

### Parameters

fileName: string/[PyUnicode](#PyUnicode)

File to delete.

### Win32 API References

Search forDeleteFileat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DeleteFile),[google](#http://www.google.com/search?q=DeleteFile)or[google groups](#http://groups.google.com/groups?q=DeleteFile).

<span id="win32api.DragFinish">win32api.DragFinish</span>
===

## [win32api](#win32api).DragFinish
 **DragFinish(hDrop** )
Releases the memory stored by Windows for the filenames.

### Parameters

hDrop: int

Handle identifying the structure containing the file names.

### Win32 API References

Search forDragFinishat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DragFinish),[google](#http://www.google.com/search?q=DragFinish)or[google groups](#http://groups.google.com/groups?q=DragFinish).

<span id="win32api.DragQueryFile">win32api.DragQueryFile</span>
===

## [win32api](#win32api).DragQueryFile
string/int = **DragQueryFile(hDrop, fileNum** )
Retrieves the file names of dropped files.

### Parameters

hDrop: int

Handle identifying the structure containing the file names.

fileNum=0xFFFFFFFF: int

Specifies the index of the file to query.

### Win32 API References

Search forDragQueryFileat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=DragQueryFile),[google](#http://www.google.com/search?q=DragQueryFile)or[google groups](#http://groups.google.com/groups?q=DragQueryFile).

### Return ValueIf the fileNum parameter is 0xFFFFFFFF (the default) then the return value 

is an integer with the count of files dropped.  If fileNum is between 0 and Count, 

the return value is a string containing the filename.
If an error occurs, and exception is raised.

<span id="win32api.DuplicateHandle">win32api.DuplicateHandle</span>
===

## [win32api](#win32api).DuplicateHandle
[PyHANDLE](#PyHANDLE)= **DuplicateHandle(hSourceProcess, hSource, hTargetProcessHandle, desiredAccess, bInheritHandle, options** )
Duplicates a handle.

### Parameters

hSourceProcess:[PyHANDLE](#PyHANDLE)

Identifies the process containing the handle to duplicate.

hSource:[PyHANDLE](#PyHANDLE)

Identifies the handle to duplicate. This is an open object handle that is valid in the context of the source process.

hTargetProcessHandle:[PyHANDLE](#PyHANDLE)

Identifies the process that is to receive the duplicated handle. The handle must have PROCESS_DUP_HANDLE access.

desiredAccess: int

Specifies the access requested for the new handle. This parameter is ignored if the dwOptions parameter specifies the DUPLICATE_SAME_ACCESS flag. Otherwise, the flags that can be specified depend on the type of object whose handle is being duplicated. For the flags that can be specified for each object type, see the following Remarks section. Note that the new handle can have more access than the original handle.

bInheritHandle: int

Indicates whether the handle is inheritable. If TRUE, the duplicate handle can be inherited by new processes created by the target process. If FALSE, the new handle cannot be inherited.

options: int

Specifies optional actions. This parameter can be zero, or any combination of the following flags
DUPLICATE_CLOSE_SOURCEloses the source handle. This occurs regardless of any error status returned.DUPLICATE_SAME_ACCESSIgnores the dwDesiredAccess parameter. The duplicate handle has the same access as the source handle.
### CommentsWhen duplicating a handle for a different process, you should either keep a 

reference to the returned PyHANDLE, or call .Detach() on it to prevent it 

from being closed prematurely.

<span id="win32api.EndUpdateResource">win32api.EndUpdateResource</span>
===

## [win32api](#win32api).EndUpdateResource
 **EndUpdateResource(handle, discard** )
Ends a resource update cycle of a PE file.

### Parameters

handle:[PyHANDLE](#PyHANDLE)

The update-file handle.

discard: int

Flag to discard all writes.

<span id="win32api.EnumDisplayDevices">win32api.EnumDisplayDevices</span>
===

## [win32api](#win32api).EnumDisplayDevices
[PyDISPLAY_DEVICE](#PyDISPLAY.DEVICE)= **EnumDisplayDevices(Device, DevNum, Flags** )
Obtain information about the display devices in a system

### Parameters

Device=None: string

Name of device, use None to obtain information for the display adapter(s) on the machine, based on DevNum

DevNum=0: int

Index of device of interest, starting with zero

Flags=0: int

Reserved, use 0 if passed in

### CommentsAccepts keyword arguments

<span id="win32api.EnumDisplayMonitors">win32api.EnumDisplayMonitors</span>
===

## [win32api](#win32api).EnumDisplayMonitors
list = **EnumDisplayMonitors(hdc, rcClip** )
Lists display monitors for a given device context and area

### Parameters

hdc=None:[PyHANDLE](#PyHANDLE)

Handle to device context, use None for virtual desktop

rcClip=None:[PyRECT](#PyRECT)

Clipping rectangle, can be None

### CommentsAccepts keyword arguments

### Return ValueReturns a sequence of tuples.  For each monitor found, returns a handle to the monitor, 

device context handle, and intersection rectangle: (hMonitor, hdcMonitor,[PyRECT](#PyRECT))

<span id="win32api.EnumDisplaySettings">win32api.EnumDisplaySettings</span>
===

## [win32api](#win32api).EnumDisplaySettings
[PyDEVMODE](#PyDEVMODE)= **EnumDisplaySettings(DeviceName, ModeNum** )
List available modes for specified display device

### Parameters

DeviceName=None: string

Name of device as returned by[win32api::EnumDisplayDevices](#win32api.EnumDisplayDevices), use None for default display device

ModeNum=0: int

Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS

### CommentsAccepts keyword arguments

<span id="win32api.EnumDisplaySettingsEx">win32api.EnumDisplaySettingsEx</span>
===

## [win32api](#win32api).EnumDisplaySettingsEx
[PyDEVMODE](#PyDEVMODE)= **EnumDisplaySettingsEx(DeviceName, ModeNum, Flags** )
Lists available modes for a display device, with optional flags

### Parameters

DeviceName=None: string

Name of device as returned by[win32api::EnumDisplayDevices](#win32api.EnumDisplayDevices). Can be None for default display

ModeNum: int

Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS

Flags=0: int

EDS_RAWMODE (2) is only defined flag

### CommentsAccepts keyword arguments

<span id="win32api.EnumResourceLanguages">win32api.EnumResourceLanguages</span>
===

## [win32api](#win32api).EnumResourceLanguages
[int,...] = **EnumResourceLanguages(hmodule, lpType, lpName** )
List languages for a resource

### Parameters

hmodule:[PyHANDLE](#PyHANDLE)

Handle to the module that contains resource

lpType:[PyResourceId](#PyResourceId)

Resource type, can be string or integer

lpName:[PyResourceId](#PyResourceId)

Resource name, can be string or integer

<span id="win32api.EnumResourceNames">win32api.EnumResourceNames</span>
===

## [win32api](#win32api).EnumResourceNames
[string, ...] = **EnumResourceNames(hmodule, resType** )
Enumerates all the resources of the specified type from the nominated file.

### Parameters

hmodule:[PyHANDLE](#PyHANDLE)

The handle to the module to enumerate.

resType:[PyResourceId](#PyResourceId)

The type of resource to enumerate. (win32con.RT_*). 

If passed as a string, form is '#' sign followed by decimal number. eg RT_ANICURSOR would be '#21'

### Return ValueThe result is a list of string or integers, one for each resource enumerated.

<span id="win32api.EnumResourceTypes">win32api.EnumResourceTypes</span>
===

## [win32api](#win32api).EnumResourceTypes
[[PyUnicode](#PyUnicode),...] = **EnumResourceTypes(hmodule** )
Return name or integer id of all resource types contained in module

### Parameters

hmodule:[PyHANDLE](#PyHANDLE)

The handle to the module to enumerate.

<span id="win32api.ExitWindows">win32api.ExitWindows</span>
===

## [win32api](#win32api).ExitWindows
 **ExitWindows(reserved1, reserved2** )
Logs off the current user

### Parameters

reserved1=0: int



reserved2=0: int



### Win32 API References

Search forAbortSystemShutdownat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown),[google](#http://www.google.com/search?q=AbortSystemShutdown)or[google groups](#http://groups.google.com/groups?q=AbortSystemShutdown).

<span id="win32api.ExitWindowsEx">win32api.ExitWindowsEx</span>
===

## [win32api](#win32api).ExitWindowsEx
 **ExitWindowsEx(flags, reserved** )
either logs off the current user, shuts down the system, or shuts down and restarts the system.

### Parameters

flags: int

The shutdown operation

reserved=0: int



### CommentsIt sends the WM_QUERYENDSESSION message to all applications to determine if they can be terminated.

### Win32 API References

Search forAbortSystemShutdownat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=AbortSystemShutdown),[google](#http://www.google.com/search?q=AbortSystemShutdown)or[google groups](#http://groups.google.com/groups?q=AbortSystemShutdown).

<span id="win32api.ExpandEnvironmentStrings">win32api.ExpandEnvironmentStrings</span>
===

## [win32api](#win32api).ExpandEnvironmentStrings
string = **ExpandEnvironmentStrings(in** )
Expands environment-variable strings and replaces them with their defined values.

### Parameters

in: string

String to expand

### Win32 API References

Search forExpandEnvironmentStringsat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ExpandEnvironmentStrings),[google](#http://www.google.com/search?q=ExpandEnvironmentStrings)or[google groups](#http://groups.google.com/groups?q=ExpandEnvironmentStrings).

<span id="win32api.FindCloseChangeNotification">win32api.FindCloseChangeNotification</span>
===

## [win32api](#win32api).FindCloseChangeNotification
 **FindCloseChangeNotification(handle** )
Closes the change notification handle.

### Parameters

handle: int

The handle returned from[win32api::FindFirstChangeNotification](#win32api.FindFirstChangeNotification)

<span id="win32api.FindExecutable">win32api.FindExecutable</span>
===

## [win32api](#win32api).FindExecutable
(int, string) = **FindExecutable(filename, dir** )
Retrieves the name and handle of the executable (.EXE) file associated with the specified filename.

### Parameters

filename: string

A file name.  This can be either a document or executable file.

dir: string

The default directory.

### CommentsThe function will raise an exception if it fails.

### Win32 API References

Search forFindExecutableat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindExecutable),[google](#http://www.google.com/search?q=FindExecutable)or[google groups](#http://groups.google.com/groups?q=FindExecutable).

### Return ValueThe return value is a tuple of (integer, string)
The integer is the instance handle of the executable file associated 

with the specified filename. (This handle could also be the handle of 

a dynamic data exchange [DDE] server application.)
The may contain the path to the DDE server started if no server responds to a request to initiate a DDE conversation.

<span id="win32api.FindFiles">win32api.FindFiles</span>
===

## [win32api](#win32api).FindFiles
list = **FindFiles(fileSpec** )
Retrieves a list of matching filenames.  An interface to the API FindFirstFile/FindNextFile/Find close functions.

### Parameters

fileSpec: string

A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).

### Win32 API References

Search forFindFirstFileat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindFirstFile),[google](#http://www.google.com/search?q=FindFirstFile)or[google groups](#http://groups.google.com/groups?q=FindFirstFile).

Search forFindNextFileat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindNextFile),[google](#http://www.google.com/search?q=FindNextFile)or[google groups](#http://groups.google.com/groups?q=FindNextFile).

Search forFindCloseat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FindClose),[google](#http://www.google.com/search?q=FindClose)or[google groups](#http://groups.google.com/groups?q=FindClose).

### Return ValueReturns a sequence of[WIN32_FIND_DATA](#WIN32.FIND_DATA)tuples

<span id="win32api.FindFirstChangeNotification">win32api.FindFirstChangeNotification</span>
===

## [win32api](#win32api).FindFirstChangeNotification
int = **FindFirstChangeNotification(pathName, bSubDirs, filter** )
Creates a change notification handle and sets up initial change notification filter conditions.

### Parameters

pathName: string

Specifies the path of the directory to watch.

bSubDirs: int

Specifies whether the function will monitor the directory or the directory tree. If this parameter is TRUE, the function monitors the directory tree rooted at the specified directory; if it is FALSE, it monitors only the specified directory

filter: int

Specifies the filter conditions that satisfy a change notification wait. This parameter can be one or more of the following values:

 **Value**  **Meaning** FILE_NOTIFY_CHANGE_FILE_NAMEAny file name change in the watched directory or subtree causes a change notification wait operation to return. Changes include renaming, creating, or deleting a file name.FILE_NOTIFY_CHANGE_DIR_NAMEAny directory-name change in the watched directory or subtree causes a change notification wait operation to return. Changes include creating or deleting a directory.FILE_NOTIFY_CHANGE_ATTRIBUTESAny attribute change in the watched directory or subtree causes a change notification wait operation to return.FILE_NOTIFY_CHANGE_SIZEAny file-size change in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change in file size only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.FILE_NOTIFY_CHANGE_LAST_WRITEAny change to the last write-time of files in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change to the last write-time only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.FILE_NOTIFY_CHANGE_SECURITYAny security-descriptor change in the watched directory or subtree causes a change notification wait operation to return
### Return ValueAlthough the result is a handle, the handle can not be closed via CloseHandle() - therefore a PyHandle object is not used.

<span id="win32api.FindNextChangeNotification">win32api.FindNextChangeNotification</span>
===

## [win32api](#win32api).FindNextChangeNotification
 **FindNextChangeNotification(handle** )
Requests that the operating system signal a change notification handle the next time it detects an appropriate change.

### Parameters

handle:[PyHANDLE](#PyHANDLE)

The handle returned from[win32api::FindFirstChangeNotification](#win32api.FindFirstChangeNotification)

<span id="win32api.FormatMessage">win32api.FormatMessage</span>
===

## [win32api](#win32api).FormatMessage
string = **FormatMessage(errCode** )
Returns an error message from the system error file.

### Parameters

errCode=0: int

The error code to return the message for,  If this value is 0, then GetLastError() is called to determine the error code.

### Alternative Parameters

flags

Flags for the call.  Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.

source

The source object.  If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int; 

if flags contain FORMAT_MESSAGE_FROM_STRING it should be a string containing the error msg; 

otherwise it is ignored.

messageId

The message ID.

languageID

The language ID.

inserts

The string inserts to insert.

### Win32 API References

Search forGetLastErrorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError),[google](#http://www.google.com/search?q=GetLastError)or[google groups](#http://groups.google.com/groups?q=GetLastError).

Search forFormatMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FormatMessage),[google](#http://www.google.com/search?q=FormatMessage)or[google groups](#http://groups.google.com/groups?q=FormatMessage).

<span id="win32api.FormatMessageW">win32api.FormatMessageW</span>
===

## [win32api](#win32api).FormatMessageW
[PyUnicode](#PyUnicode)= **FormatMessageW(errCode** )
Returns an error message from the system error file.

### Parameters

errCode=0: int

The error code to return the message for,  If this value is 0, 

then GetLastError() is called to determine the error code.

### Alternative Parameters

flags

Flags for the call.  Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.

source

The source object.  If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int or[PyHANDLE](#PyHANDLE); 

if flags contain FORMAT_MESSAGE_FROM_STRING it should be a unicode string; 

otherwise it is ignored.

messageId

The message ID.

languageID

The language ID.

inserts

The string inserts to insert.

### Win32 API References

Search forGetLastErrorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError),[google](#http://www.google.com/search?q=GetLastError)or[google groups](#http://groups.google.com/groups?q=GetLastError).

Search forFormatMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FormatMessage),[google](#http://www.google.com/search?q=FormatMessage)or[google groups](#http://groups.google.com/groups?q=FormatMessage).

<span id="win32api.FreeLibrary">win32api.FreeLibrary</span>
===

## [win32api](#win32api).FreeLibrary
 **FreeLibrary(hModule** )
Decrements the reference count of the loaded dynamic-link library (DLL) module.

### Parameters

hModule:[PyHANDLE](#PyHANDLE)

Specifies the handle to the module.

### Win32 API References

Search forFreeLibraryat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=FreeLibrary),[google](#http://www.google.com/search?q=FreeLibrary)or[google groups](#http://groups.google.com/groups?q=FreeLibrary).

<span id="win32api.GenerateConsoleCtrlEvent">win32api.GenerateConsoleCtrlEvent</span>
===

## [win32api](#win32api).GenerateConsoleCtrlEvent
int = **GenerateConsoleCtrlEvent(controlEvent, processGroupId** )
Send a specified signal to a console process group that shares the console associated with the calling process.

### Parameters

controlEvent: int

Signal to generate.

processGroupId: int

Process group to get signal.

### Win32 API References

Search forGenerateConsoleCtrlEventat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GenerateConsoleCtrlEvent),[google](#http://www.google.com/search?q=GenerateConsoleCtrlEvent)or[google groups](#http://groups.google.com/groups?q=GenerateConsoleCtrlEvent).

<span id="win32api.GetAsyncKeyState">win32api.GetAsyncKeyState</span>
===

## [win32api](#win32api).GetAsyncKeyState
int = **GetAsyncKeyState(key** )
Retrieves the status of the specified key.

### Parameters

key: int

Specifies one of 256 possible virtual-key codes.

### CommentsAn application can use the virtual-key code constants win32con.VK_SHIFT, 

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

### Win32 API References

Search forGetAsyncKeyStateat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetAsyncKeyState),[google](#http://www.google.com/search?q=GetAsyncKeyState)or[google groups](#http://groups.google.com/groups?q=GetAsyncKeyState).

### Return ValueThe return value specifies whether the key was pressed since the last 

call to GetAsyncKeyState, and whether the key is currently up or down. If 

the most significant bit is set, the key is down, and if the least significant 

bit is set, the key was pressed after the previous call to GetAsyncKeyState.
The return value is zero if a window in another thread or process currently has the 

keyboard focus.

<span id="win32api.GetCommandLine">win32api.GetCommandLine</span>
===

## [win32api](#win32api).GetCommandLine
string = **GetCommandLine(** )
Retrieves the current application's command line.

### Win32 API References

Search forGetCommandLineat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCommandLine),[google](#http://www.google.com/search?q=GetCommandLine)or[google groups](#http://groups.google.com/groups?q=GetCommandLine).

<span id="win32api.GetComputerName">win32api.GetComputerName</span>
===

## [win32api](#win32api).GetComputerName
string = **GetComputerName(** )
Returns the local computer name

### Win32 API References

Search forGetComputerNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerName),[google](#http://www.google.com/search?q=GetComputerName)or[google groups](#http://groups.google.com/groups?q=GetComputerName).

<span id="win32api.GetComputerNameEx">win32api.GetComputerNameEx</span>
===

## [win32api](#win32api).GetComputerNameEx
string = **GetComputerNameEx(NameType** )
Retrieves a NetBIOS or DNS name associated with the local computer

### Parameters

NameType: int

Value from COMPUTER_NAME_FORMAT enum, win32con.ComputerName*

### Win32 API References

Search forGetComputerNameExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerNameEx),[google](#http://www.google.com/search?q=GetComputerNameEx)or[google groups](#http://groups.google.com/groups?q=GetComputerNameEx).

<span id="win32api.GetComputerObjectName">win32api.GetComputerObjectName</span>
===

## [win32api](#win32api).GetComputerObjectName
string = **GetComputerObjectName(NameFormat** )
Retrieves the local computer's name in a specified format.

### Parameters

NameFormat: int

EXTENDED_NAME_FORMAT value, win32con.Name*

### Win32 API References

Search forGetComputerObjectNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetComputerObjectName),[google](#http://www.google.com/search?q=GetComputerObjectName)or[google groups](#http://groups.google.com/groups?q=GetComputerObjectName).

<span id="win32api.GetConsoleTitle">win32api.GetConsoleTitle</span>
===

## [win32api](#win32api).GetConsoleTitle
string = **GetConsoleTitle(** )
Returns the title for the current console.

<span id="win32api.GetCurrentProcess">win32api.GetCurrentProcess</span>
===

## [win32api](#win32api).GetCurrentProcess
int = **GetCurrentProcess(** )
Returns a pseudohandle for the current process.

### CommentsA pseudohandle is a special constant that is interpreted as the current thread handle. The calling thread can use this handle to specify itself whenever a thread handle is required. Pseudohandles are not inherited by child processes. 

The method[win32api::DuplicateHandle](#win32api.DuplicateHandle)can be used to create a handle that other threads and processes can use. 

As this handle can not be closed, and integer is returned rather than 

a[PyHANDLE](#PyHANDLE)object, which would attempt to automatically close the handle.

### Win32 API References

Search forGetCurrentProcessat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentProcess),[google](#http://www.google.com/search?q=GetCurrentProcess)or[google groups](#http://groups.google.com/groups?q=GetCurrentProcess).

<span id="win32api.GetCurrentProcessId">win32api.GetCurrentProcessId</span>
===

## [win32api](#win32api).GetCurrentProcessId
int = **GetCurrentProcessId(** )
Returns the thread ID for the current process.

### Win32 API References

Search forGetCurrentProcessIdat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentProcessId),[google](#http://www.google.com/search?q=GetCurrentProcessId)or[google groups](#http://groups.google.com/groups?q=GetCurrentProcessId).

<span id="win32api.GetCurrentThread">win32api.GetCurrentThread</span>
===

## [win32api](#win32api).GetCurrentThread
int = **GetCurrentThread(** )
Returns a pseudohandle for the current thread.

### CommentsA pseudohandle is a special constant that is interpreted as the current thread handle. The calling thread can use this handle to specify itself whenever a thread handle is required. Pseudohandles are not inherited by child processes. 

The method[win32api::DuplicateHandle](#win32api.DuplicateHandle)can be used to create a handle that other threads and processes can use. 

As this handle can not be closed, and integer is returned rather than 

a[PyHANDLE](#PyHANDLE)object, which would attempt to automatically close the handle.

### Win32 API References

Search forGetCurrentThreadat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentThread),[google](#http://www.google.com/search?q=GetCurrentThread)or[google groups](#http://groups.google.com/groups?q=GetCurrentThread).

<span id="win32api.GetCurrentThreadId">win32api.GetCurrentThreadId</span>
===

## [win32api](#win32api).GetCurrentThreadId
int = **GetCurrentThreadId(** )
Returns the thread ID for the current thread.

### Win32 API References

Search forGetCurrentThreadIdat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCurrentThreadId),[google](#http://www.google.com/search?q=GetCurrentThreadId)or[google groups](#http://groups.google.com/groups?q=GetCurrentThreadId).

<span id="win32api.GetCursorPos">win32api.GetCursorPos</span>
===

## [win32api](#win32api).GetCursorPos
int, int = **GetCursorPos(** )
Returns the position of the cursor, in screen co-ordinates.

### Win32 API References

Search forGetCursorPosat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCursorPos),[google](#http://www.google.com/search?q=GetCursorPos)or[google groups](#http://groups.google.com/groups?q=GetCursorPos).

<span id="win32api.GetDateFormat">win32api.GetDateFormat</span>
===

## [win32api](#win32api).GetDateFormat
string = **GetDateFormat(locale, flags, time, format** )
Formats a date as a date string for a specified locale. The function formats either a specified date or the local system date.

### Parameters

locale: int



flags: int



time:[PyTime](#PyTime)

The time to use, or None to use the current time.

format: string

May be None

<span id="win32api.GetDiskFreeSpace">win32api.GetDiskFreeSpace</span>
===

## [win32api](#win32api).GetDiskFreeSpace
tuple = **GetDiskFreeSpace(rootPath** )
Retrieves information about the specified disk, including the amount of free space available.

### Parameters

rootPath: string

Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.

### Win32 API References

Search forGetDiskFreeSpaceat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDiskFreeSpace),[google](#http://www.google.com/search?q=GetDiskFreeSpace)or[google groups](#http://groups.google.com/groups?q=GetDiskFreeSpace).

### Return ValueThe return value is a tuple of 4 integers, containing 

the number of sectors per cluster, the number of bytes per sector, 

the total number of free clusters on the disk and the total number of clusters on the disk.
If the function fails, an error is returned.

<span id="win32api.GetDiskFreeSpaceEx">win32api.GetDiskFreeSpaceEx</span>
===

## [win32api](#win32api).GetDiskFreeSpaceEx
tuple = **GetDiskFreeSpaceEx(rootPath** )
Retrieves information about the specified disk, including the amount of free space available.

### Parameters

rootPath: string

Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.

### Win32 API References

Search forGetDiskFreeSpaceExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDiskFreeSpaceEx),[google](#http://www.google.com/search?q=GetDiskFreeSpaceEx)or[google groups](#http://groups.google.com/groups?q=GetDiskFreeSpaceEx).

### Return ValueThe return value is a tuple of 3 integers, containing 

the number of free bytes available 

the total number of bytes available on disk 

the total number of free bytes on disk 

the above values may be less, if user-quotas are in effect
If the function fails, an error is returned.

<span id="win32api.GetDllDirectory">win32api.GetDllDirectory</span>
===

## [win32api](#win32api).GetDllDirectory
[PyUnicode](#PyUnicode)= **GetDllDirectory(** )
Returns the DLL search path

### Win32 API References

Search forGetDllDirectoryat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetDllDirectory),[google](#http://www.google.com/search?q=GetDllDirectory)or[google groups](#http://groups.google.com/groups?q=GetDllDirectory).

<span id="win32api.GetDomainName">win32api.GetDomainName</span>
===

## [win32api](#win32api).GetDomainName
string = **GetDomainName(** )
Returns the current domain name

### CommentsThis is a convenience wrapper of the Win32 function LookupAccountSid()

<span id="win32api.GetEnvironmentVariable">win32api.GetEnvironmentVariable</span>
===

## [win32api](#win32api).GetEnvironmentVariable
str = **GetEnvironmentVariable(variable** )
Retrieves the value of an environment variable.

### Parameters

variable: str

The variable to get

### Win32 API References

Search forGetEnvironmentVariableat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetEnvironmentVariable),[google](#http://www.google.com/search?q=GetEnvironmentVariable)or[google groups](#http://groups.google.com/groups?q=GetEnvironmentVariable).

### Return ValueReturns None if environment variable is not found

<span id="win32api.GetEnvironmentVariableW">win32api.GetEnvironmentVariableW</span>
===

## [win32api](#win32api).GetEnvironmentVariableW
[PyUnicode](#PyUnicode)= **GetEnvironmentVariableW(Name** )
Retrieves the unicode value of an environment variable.

### Parameters

Name: str

The variable to retrieve

### Win32 API References

Search forGetEnvironmentVariableWat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetEnvironmentVariableW),[google](#http://www.google.com/search?q=GetEnvironmentVariableW)or[google groups](#http://groups.google.com/groups?q=GetEnvironmentVariableW).

### Return ValueReturns None if environment variable is not found

<span id="win32api.GetFileAttributes">win32api.GetFileAttributes</span>
===

## [win32api](#win32api).GetFileAttributes
int = **GetFileAttributes(pathName** )
Retrieves the attributes for the named file.

### Parameters

pathName: string

The name of the file whose attributes are to be returned. 

If this param is a unicode object, GetFileAttributesW is called.

### Win32 API References

Search forGetFileAttributesat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributes),[google](#http://www.google.com/search?q=GetFileAttributes)or[google groups](#http://groups.google.com/groups?q=GetFileAttributes).

Search forGetFileAttributesWat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFileAttributesW),[google](#http://www.google.com/search?q=GetFileAttributesW)or[google groups](#http://groups.google.com/groups?q=GetFileAttributesW).

### Return ValueThe return value is a combination of the win32con.FILE_ATTRIBUTE_* constants.
An exception is raised on failure.

<span id="win32api.GetFileVersionInfo">win32api.GetFileVersionInfo</span>
===

## [win32api](#win32api).GetFileVersionInfo
 **GetFileVersionInfo(Filename, SubBlock** )
Retrieve version info for specified file

### Parameters

Filename: string/unicode

File to query for version info

SubBlock: string/unicode

Information to return: \\ for VS_FIXEDFILEINFO, \\VarFileInfo\\Translation for languages/codepages available

<span id="win32api.GetFocus">win32api.GetFocus</span>
===

## [win32api](#win32api).GetFocus
int = **GetFocus(** )
Retrieves the handle of the keyboard focus window associated with the thread that called the method.

### Win32 API References

Search forGetFocusat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetFocus),[google](#http://www.google.com/search?q=GetFocus)or[google groups](#http://groups.google.com/groups?q=GetFocus).

### Return ValueThe method raises an exception if no window with the focus exists.

<span id="win32api.GetFullPathName">win32api.GetFullPathName</span>
===

## [win32api](#win32api).GetFullPathName
string = **GetFullPathName(fileName** )
Returns the full path of a (possibly relative) path

### Parameters

fileName: string

The file name.

### CommentsPlease use[win32file::GetFullPathName](#win32file.GetFullPathName)instead - it has better Unicode semantics.

<span id="win32api.GetHandleInformation">win32api.GetHandleInformation</span>
===

## [win32api](#win32api).GetHandleInformation
int = **GetHandleInformation(Object** )
Retrieves a handle's flags.

### Parameters

Object:[PyHANDLE](#PyHANDLE)

Handle to an object

### CommentsNot available on Win98/Me

### Return ValueReturns a combination of HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE

<span id="win32api.GetKeyState">win32api.GetKeyState</span>
===

## [win32api](#win32api).GetKeyState
int = **GetKeyState(key** )
Retrieves the status of the specified key.

### Parameters

key: int

Specifies a virtual key. If the desired virtual key is a letter or digit (A through Z, a through z, or 0 through 9), key must be set to the ASCII value of that character. For other keys, it must be a virtual-key code.

### CommentsThe key status returned from this function changes as a given thread 

reads key messages from its message queue. The status does not reflect the 

interrupt-level state associated with the hardware. Use the[win32api::GetAsyncKeyState](#win32api.GetAsyncKeyState)method to retrieve that information.

### Win32 API References

Search forGetKeyStateat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetKeyState),[google](#http://www.google.com/search?q=GetKeyState)or[google groups](#http://groups.google.com/groups?q=GetKeyState).

### Return ValueThe return value specifies the status of 

the given virtual key. If the high-order bit is 1, the key is down; 

otherwise, it is up. If the low-order bit is 1, the key is toggled. 

A key, such as the CAPS LOCK key, is toggled if it is turned on. 

The key is off and untoggled if the low-order bit is 0. A toggle key's 

indicator light (if any) on the keyboard will be on when the key is 

toggled, and off when the key is untoggled.

<span id="win32api.GetKeyboardLayout">win32api.GetKeyboardLayout</span>
===

## [win32api](#win32api).GetKeyboardLayout
int = **GetKeyboardLayout(threadId** )
retrieves the active input locale identifier (formerly called the keyboard layout) for the specified thread.

### Parameters

threadId=0: int



### CommentsIf the idThread parameter is zero, the input locale identifier for the active thread is returned.

<span id="win32api.GetKeyboardLayoutList">win32api.GetKeyboardLayoutList</span>
===

## [win32api](#win32api).GetKeyboardLayoutList
(int,..) = **GetKeyboardLayoutList(** )
Returns a sequence of all locale ids currently loaded

<span id="win32api.GetKeyboardLayoutName">win32api.GetKeyboardLayoutName</span>
===

## [win32api](#win32api).GetKeyboardLayoutName
int = **GetKeyboardLayoutName(** )
Retrieves the name of the active input locale identifier (formerly called the keyboard layout).

<span id="win32api.GetKeyboardState">win32api.GetKeyboardState</span>
===

## [win32api](#win32api).GetKeyboardState
string = **GetKeyboardState(** )
Retrieves the status of the 256 virtual keys on the keyboard.

### Win32 API References

Search forGetKeyboardStateat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetKeyboardState),[google](#http://www.google.com/search?q=GetKeyboardState)or[google groups](#http://groups.google.com/groups?q=GetKeyboardState).

### Return ValueThe return value is a string of exactly 256 characters. 

Each character represents the bitmask for a key - see the Win32 

documentation for more details.

<span id="win32api.GetLastError">win32api.GetLastError</span>
===

## [win32api](#win32api).GetLastError
int = **GetLastError(** )
Retrieves the calling thread's last error code value.

### Win32 API References

Search forGetLastErrorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastError),[google](#http://www.google.com/search?q=GetLastError)or[google groups](#http://groups.google.com/groups?q=GetLastError).

<span id="win32api.GetLastInputInfo">win32api.GetLastInputInfo</span>
===

## [win32api](#win32api).GetLastInputInfo
int = **GetLastInputInfo(** )
Returns time of last input event in tick count

### Win32 API References

Search forGetLastInputInfoat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLastInputInfo),[google](#http://www.google.com/search?q=GetLastInputInfo)or[google groups](#http://groups.google.com/groups?q=GetLastInputInfo).

<span id="win32api.GetLocalTime">win32api.GetLocalTime</span>
===

## [win32api](#win32api).GetLocalTime
tuple = **GetLocalTime(** )
Returns the current local time

<span id="win32api.GetLogicalDriveStrings">win32api.GetLogicalDriveStrings</span>
===

## [win32api](#win32api).GetLogicalDriveStrings
string = **GetLogicalDriveStrings(** )
Returns a string with all logical drives currently mapped.

### Win32 API References

Search forGetLogicalDriveStringsat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLogicalDriveStrings),[google](#http://www.google.com/search?q=GetLogicalDriveStrings)or[google groups](#http://groups.google.com/groups?q=GetLogicalDriveStrings).

### Return ValueThe return value is a single string, with each drive 

letter NULL terminated.
Use "s.split('\\0')" to split into components.

<span id="win32api.GetLogicalDrives">win32api.GetLogicalDrives</span>
===

## [win32api](#win32api).GetLogicalDrives
int = **GetLogicalDrives(** )
Returns a bitmask representing the currently available disk drives.

### Win32 API References

Search forGetLogicalDrivesat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetLogicalDrives),[google](#http://www.google.com/search?q=GetLogicalDrives)or[google groups](#http://groups.google.com/groups?q=GetLogicalDrives).

<span id="win32api.GetLongPathName">win32api.GetLongPathName</span>
===

## [win32api](#win32api).GetLongPathName
string = **GetLongPathName(fileName** )
Converts the specified path to its long form.

### Parameters

fileName: string

The file name.

### CommentsThis function may raise a NotImplementedError exception if the version 

of Windows does not support this function.

<span id="win32api.GetLongPathNameW">win32api.GetLongPathNameW</span>
===

## [win32api](#win32api).GetLongPathNameW
[PyUnicode](#PyUnicode)= **GetLongPathNameW(fileName** )
Converts the specified path to its long form.

### Parameters

fileName:[PyUnicode](#PyUnicode)

The file name.

### CommentsThis function may raise a NotImplementedError exception if the version 

of Windows does not support this function.

<span id="win32api.GetModuleFileName">win32api.GetModuleFileName</span>
===

## [win32api](#win32api).GetModuleFileName
string = **GetModuleFileName(hModule** )
Retrieves the filename of the specified module.

### Parameters

hModule:[PyHANDLE](#PyHANDLE)

Specifies the handle to the module.

### Win32 API References

Search forGetModuleFileNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName),[google](#http://www.google.com/search?q=GetModuleFileName)or[google groups](#http://groups.google.com/groups?q=GetModuleFileName).

<span id="win32api.GetModuleFileNameW">win32api.GetModuleFileNameW</span>
===

## [win32api](#win32api).GetModuleFileNameW
[PyUnicode](#PyUnicode)= **GetModuleFileNameW(hModule** )
Retrieves the unicode filename of the specified module.

### Parameters

hModule:[PyHANDLE](#PyHANDLE)

Specifies the handle to the module.

### Win32 API References

Search forGetModuleFileNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName),[google](#http://www.google.com/search?q=GetModuleFileName)or[google groups](#http://groups.google.com/groups?q=GetModuleFileName).

<span id="win32api.GetModuleHandle">win32api.GetModuleHandle</span>
===

## [win32api](#win32api).GetModuleHandle
int = **GetModuleHandle(fileName** )
Returns the handle of an already loaded DLL.

### Parameters

fileName=None: string

Specifies the file name of the module to load.

### Win32 API References

Search forGetModuleHandleat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleHandle),[google](#http://www.google.com/search?q=GetModuleHandle)or[google groups](#http://groups.google.com/groups?q=GetModuleHandle).

<span id="win32api.GetMonitorInfo">win32api.GetMonitorInfo</span>
===

## [win32api](#win32api).GetMonitorInfo
dict = **GetMonitorInfo(hMonitor** )
Retrieves information for a monitor by handle

### Parameters

hMonitor:[PyHANDLE](#PyHANDLE)

Handle to a monitor

### CommentsAccepts keyword args

### Return ValueReturns a dictionary representing a MONITORINFOEX structure

<span id="win32api.GetNativeSystemInfo">win32api.GetNativeSystemInfo</span>
===

## [win32api](#win32api).GetNativeSystemInfo
tuple = **GetNativeSystemInfo(** )
Retrieves information about the current system for a Wow64 process.

### Win32 API References

Search forGetNativeSystemInfoat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetNativeSystemInfo),[google](#http://www.google.com/search?q=GetNativeSystemInfo)or[google groups](#http://groups.google.com/groups?q=GetNativeSystemInfo).

### Return ValueThe return value is a tuple of 9 values, which corresponds 

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

<span id="win32api.GetProcAddress">win32api.GetProcAddress</span>
===

## [win32api](#win32api).GetProcAddress
int = **GetProcAddress(hModule, functionName** )
Returns the address of the specified exported dynamic-link library (DLL) function.

### Parameters

hModule:[PyHANDLE](#PyHANDLE)

Specifies the handle to the module.

functionName:[PyResourceId](#PyResourceId)

Specifies the name of the procedure, or its ordinal value

### Win32 API References

Search forGetProcAddressat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProcAddress),[google](#http://www.google.com/search?q=GetProcAddress)or[google groups](#http://groups.google.com/groups?q=GetProcAddress).

<span id="win32api.GetProfileSection">win32api.GetProfileSection</span>
===

## [win32api](#win32api).GetProfileSection
list = **GetProfileSection(section, iniName** )
Retrieves all entries from a section in an INI file.

### Parameters

section: string

The section in the INI file to retrieve a entries for.

iniName=None: string

The name of the INI file.  If None, the system INI file is used.

### CommentsThis function is obsolete, applications should use the registry instead.

### Win32 API References

Search forGetProfileSectionat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileSection),[google](#http://www.google.com/search?q=GetProfileSection)or[google groups](#http://groups.google.com/groups?q=GetProfileSection).

### Return ValueThe return value is a list of strings.

<span id="win32api.GetProfileVal">win32api.GetProfileVal</span>
===

## [win32api](#win32api).GetProfileVal
int/string = **GetProfileVal(section, entry, defValue, iniName** )
Retrieves entries from a windows INI file.  This method encapsulates GetProfileString, GetProfileInt, GetPrivateProfileString and GetPrivateProfileInt.

### Parameters

section: string

The section in the INI file to retrieve a value for.

entry: string

The entry within the section in the INI file to retrieve a value for.

defValue: int/string

The default value.  The type of this parameter determines the methods return type.

iniName=None: string

The name of the INI file.  If None, the system INI file is used.

### CommentsThis function is obsolete, applications should use the registry instead.

### Win32 API References

Search forGetProfileStringat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileString),[google](#http://www.google.com/search?q=GetProfileString)or[google groups](#http://groups.google.com/groups?q=GetProfileString).

Search forGetProfileIntat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetProfileInt),[google](#http://www.google.com/search?q=GetProfileInt)or[google groups](#http://groups.google.com/groups?q=GetProfileInt).

Search forGetPrivateProfileStringat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPrivateProfileString),[google](#http://www.google.com/search?q=GetPrivateProfileString)or[google groups](#http://groups.google.com/groups?q=GetPrivateProfileString).

Search forGetPrivateProfileIntat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPrivateProfileInt),[google](#http://www.google.com/search?q=GetPrivateProfileInt)or[google groups](#http://groups.google.com/groups?q=GetPrivateProfileInt).

### Return ValueThe return value is the same type as the default parameter.

<span id="win32api.GetPwrCapabilities">win32api.GetPwrCapabilities</span>
===

## [win32api](#win32api).GetPwrCapabilities
dict = **GetPwrCapabilities(** )
Retrieves system's power capabilities

### CommentsRequires Win2k or later.

### Win32 API References

Search forGetPwrCapabilitiesat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetPwrCapabilities),[google](#http://www.google.com/search?q=GetPwrCapabilities)or[google groups](#http://groups.google.com/groups?q=GetPwrCapabilities).

### Return ValueReturns a dict representing a SYSTEM_POWER_CAPABILITIES struct

<span id="win32api.GetShortPathName">win32api.GetShortPathName</span>
===

## [win32api](#win32api).GetShortPathName
string = **GetShortPathName(path** )
Obtains the short path form of the specified path.

### Parameters

path: string/unicode

If a unicode object is passed, 

GetShortPathNameW will be called and a unicode object returned.

### CommentsThe short path name is an 8.3 compatible file name.  As the input path does 

not need to be absolute, the returned name may be longer than the input path.

### Win32 API References

Search forGetShortPathNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetShortPathName),[google](#http://www.google.com/search?q=GetShortPathName)or[google groups](#http://groups.google.com/groups?q=GetShortPathName).

<span id="win32api.GetStdHandle">win32api.GetStdHandle</span>
===

## [win32api](#win32api).GetStdHandle
 **GetStdHandle(handle** )
Returns a handle for the standard input, standard output, or standard error device

### Parameters

handle: int

input, output, or error device

<span id="win32api.GetSysColor">win32api.GetSysColor</span>
===

## [win32api](#win32api).GetSysColor
int = **GetSysColor(index** )
Returns the current system color for the specified element.

### Parameters

index: int

The Id of the element to return.  See the API for full details.

### Win32 API References

Search forGetSysColorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSysColor),[google](#http://www.google.com/search?q=GetSysColor)or[google groups](#http://groups.google.com/groups?q=GetSysColor).

### Return ValueThe return value is a windows RGB color representation.

<span id="win32api.GetSystemDefaultLCID">win32api.GetSystemDefaultLCID</span>
===

## [win32api](#win32api).GetSystemDefaultLCID
int = **GetSystemDefaultLCID(** )
Retrieves the system default locale identifier.

### Win32 API References

Search forGetSystemDefaultLCIDat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDefaultLCID),[google](#http://www.google.com/search?q=GetSystemDefaultLCID)or[google groups](#http://groups.google.com/groups?q=GetSystemDefaultLCID).

<span id="win32api.GetSystemDefaultLangID">win32api.GetSystemDefaultLangID</span>
===

## [win32api](#win32api).GetSystemDefaultLangID
int = **GetSystemDefaultLangID(** )
Retrieves the system default language identifier.

### Win32 API References

Search forGetSystemDefaultLangIDat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDefaultLangID),[google](#http://www.google.com/search?q=GetSystemDefaultLangID)or[google groups](#http://groups.google.com/groups?q=GetSystemDefaultLangID).

<span id="win32api.GetSystemDirectory">win32api.GetSystemDirectory</span>
===

## [win32api](#win32api).GetSystemDirectory
string = **GetSystemDirectory(** )
Returns the path of the Windows system directory.

### Win32 API References

Search forGetSystemDirectoryat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemDirectory),[google](#http://www.google.com/search?q=GetSystemDirectory)or[google groups](#http://groups.google.com/groups?q=GetSystemDirectory).

<span id="win32api.GetSystemFileCacheSize">win32api.GetSystemFileCacheSize</span>
===

## [win32api](#win32api).GetSystemFileCacheSize
tuple = **GetSystemFileCacheSize(** )
Returns the amount of memory reserved for file cache

### Return ValueReturns a tuple containing the minimum and maximum cache sizes, and flags (combination of win32con.MM_WORKING_SET_* flags)

<span id="win32api.GetSystemInfo">win32api.GetSystemInfo</span>
===

## [win32api](#win32api).GetSystemInfo
tuple = **GetSystemInfo(** )
Retrieves information about the current system.

### Win32 API References

Search forGetSystemInfoat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemInfo),[google](#http://www.google.com/search?q=GetSystemInfo)or[google groups](#http://groups.google.com/groups?q=GetSystemInfo).

### Return ValueThe return value is a tuple of 9 values, which corresponds 

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

<span id="win32api.GetSystemMetrics">win32api.GetSystemMetrics</span>
===

## [win32api](#win32api).GetSystemMetrics
int = **GetSystemMetrics(index** )
Retrieves various system metrics and system configuration settings.

### Parameters

index: int

Which metric is being requested.  See the API documentation for a full list.

### Win32 API References

Search forGetSystemMetricsat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetSystemMetrics),[google](#http://www.google.com/search?q=GetSystemMetrics)or[google groups](#http://groups.google.com/groups?q=GetSystemMetrics).

<span id="win32api.GetSystemTime">win32api.GetSystemTime</span>
===

## [win32api](#win32api).GetSystemTime
tuple = **GetSystemTime(** )
Returns the current system time

<span id="win32api.GetTempFileName">win32api.GetTempFileName</span>
===

## [win32api](#win32api).GetTempFileName
tuple = **GetTempFileName(path, prefix, nUnique** )
Returns creates a temporary filename of the following form: path\\preuuuu.tmp.

### Parameters

path: string

Specifies the path where the method creates the temporary filename. 

Applications typically specify a period (.) or the result of the GetTempPath function for this parameter.

prefix: string

Specifies the temporary filename prefix.

nUnique: int

Specifies an nteger used in creating the temporary filename. 

If this parameter is nonzero, it is appended to the temporary filename. 

If this parameter is zero, Windows uses the current system time to create a number to append to the filename.

### Win32 API References

Search forGetTempFileNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetTempFileName),[google](#http://www.google.com/search?q=GetTempFileName)or[google groups](#http://groups.google.com/groups?q=GetTempFileName).

### Return ValueThe return value is a tuple of (string, int), where string is the 

filename, and rc is the unique number used to generate the filename.

<span id="win32api.GetTempPath">win32api.GetTempPath</span>
===

## [win32api](#win32api).GetTempPath
string = **GetTempPath(** )
Retrieves the path of the directory designated for temporary files.

<span id="win32api.GetThreadLocale">win32api.GetThreadLocale</span>
===

## [win32api](#win32api).GetThreadLocale
int = **GetThreadLocale(** )
Returns the current thread's locale.

<span id="win32api.GetTickCount">win32api.GetTickCount</span>
===

## [win32api](#win32api).GetTickCount
int = **GetTickCount(** )
Returns the number of milliseconds since windows started.

<span id="win32api.GetTimeFormat">win32api.GetTimeFormat</span>
===

## [win32api](#win32api).GetTimeFormat
string = **GetTimeFormat(locale, flags, time, format** )
Formats a time as a time string for a specified locale. The function formats either a specified time or the local system time.

### Parameters

locale: int



flags: int



time:[PyTime](#PyTime)

The time to use, or None to use the current time.

format: string

May be None

<span id="win32api.GetTimeZoneInformation">win32api.GetTimeZoneInformation</span>
===

## [win32api](#win32api).GetTimeZoneInformation
tuple = **GetTimeZoneInformation(times_as_tuples** )
Retrieves the system time-zone information.

### Parameters

times_as_tuples=False: bool

If true, the SYSTEMTIME elements are returned as tuples instead of a time object.

### Return ValueThe return value is a tuple of (rc, tzinfo), where rc is 

the integer return code from ::GetTimezoneInformation(), which may be

 **value**  **description** TIME_ZONE_ID_STANDARDif in standard timeTIME_ZONE_ID_DAYLIGHTif in daylight savings timeTIME_ZONE_ID_UNKNOWNif the timezone in question doesn't use daylight savings time, (eg. indiana time).tzinfo is a tuple of:

### Items

[0]int: bias

Specifies the current bias, in minutes, for local time translation on this computer. The bias is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. All translations between UTC and local time are based on the following formula:

UTC = local time + bias



[1]unicode: standardName

Specifies a string associated with standard time on this operating system. For example, this member could contain "EST" to indicate Eastern Standard Time. This string is not used by the operating system, so anything stored there using the SetTimeZoneInformation function is returned unchanged by the GetTimeZoneInformation function. This string can be empty.

[2][PyTime](#PyTime)/tuple: standardTime

Specifies a SYSTEMTIME object that contains a date and local time when the transition from daylight saving time to standard time occurs on this operating system. If this date is not specified, the wMonth member in the SYSTEMTIME structure must be zero. If this date is specified, the DaylightDate value in the TIME_ZONE_INFORMATION structure must also be specified.
To select the correct day in the month, set the wYear member to zero, the wDayOfWeek member to an appropriate weekday, and the wDay member to a value in the range 1 through 5. Using this notation, the first Sunday in April can be specified, as can the last Thursday in October (5 is equal to "the last").

[3]int: standardBias

Specifies a bias value to be used during local time translations that occur during standard time. This member is ignored if a value for the StandardDate member is not supplied.
This value is added to the value of the Bias member to form the bias used during standard time. In most time zones, the value of this member is zero.

[4]unicode: daylightName



[5][PyTime](#PyTime)/tuple: daylightTime



[6]int: daylightBias

Specifies a bias value to be used during local time translations that occur during daylight saving time. This member is ignored if a value for the DaylightDate member is not supplied.
This value is added to the value of the Bias member to form the bias used during daylight saving time. In most time zones, the value of this member is &#150 60.

<span id="win32api.GetUserDefaultLCID">win32api.GetUserDefaultLCID</span>
===

## [win32api](#win32api).GetUserDefaultLCID
int = **GetUserDefaultLCID(** )
Retrieves the user default locale identifier.

### Win32 API References

Search forGetUserDefaultLCIDat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserDefaultLCID),[google](#http://www.google.com/search?q=GetUserDefaultLCID)or[google groups](#http://groups.google.com/groups?q=GetUserDefaultLCID).

<span id="win32api.GetUserDefaultLangID">win32api.GetUserDefaultLangID</span>
===

## [win32api](#win32api).GetUserDefaultLangID
int = **GetUserDefaultLangID(** )
Retrieves the user default language identifier.

### Win32 API References

Search forGetUserDefaultLangIDat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserDefaultLangID),[google](#http://www.google.com/search?q=GetUserDefaultLangID)or[google groups](#http://groups.google.com/groups?q=GetUserDefaultLangID).

<span id="win32api.GetUserName">win32api.GetUserName</span>
===

## [win32api](#win32api).GetUserName
string = **GetUserName(** )
Returns the current user name

### Win32 API References

Search forGetUserNameat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserName),[google](#http://www.google.com/search?q=GetUserName)or[google groups](#http://groups.google.com/groups?q=GetUserName).

<span id="win32api.GetUserNameEx">win32api.GetUserNameEx</span>
===

## [win32api](#win32api).GetUserNameEx
string = **GetUserNameEx(NameFormat** )
Returns the current user name in format from EXTENDED_NAME_FORMAT enum

### Parameters

NameFormat: int

EXTENDED_NAME_FORMAT value, win32con.Name*

### Win32 API References

Search forGetUserNameExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetUserNameEx),[google](#http://www.google.com/search?q=GetUserNameEx)or[google groups](#http://groups.google.com/groups?q=GetUserNameEx).

<span id="win32api.GetVersion">win32api.GetVersion</span>
===

## [win32api](#win32api).GetVersion
int = **GetVersion(** )
Returns the current version of Windows, and information about the environment.

### Return ValueThe return value's low word is the major/minor version of Windows.  The high 

word is 0 if the platform is Windows NT, or 1 if Win32s on Windows 3.1

<span id="win32api.GetVersionEx">win32api.GetVersionEx</span>
===

## [win32api](#win32api).GetVersionEx
tuple = **GetVersionEx(format** )
Returns the current version of Windows, and information about the environment.

### Parameters

format=0: int

The format of the version info to return. 

May be 0 (for OSVERSIONINFO) or 1 (for OSVERSIONINFOEX)

### Return ValueThe return value is a tuple with the following information.


### Items

[0]int: majorVersion

Identifies the major version number of the operating system.


[1]int: minorVersion

Identifies the minor version number of the operating system.


[2]int: buildNumber

Identifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)


[3]int: platformId

Identifies the platform supported by the operating system.  May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT


[4]string: version

Contains arbitrary additional information about the operating system.

### Return Valueor if the format param is 1, the return value is a tuple with:


### Items

[0]int: majorVersion

Identifies the major version number of the operating system.


[1]int: minorVersion

Identifies the minor version number of the operating system.


[2]int: buildNumber

Identifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)


[3]int: platformId

Identifies the platform supported by the operating system.  May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT


[4]string: version

Contains arbitrary additional information about the operating system.

[5]int: wServicePackMajor

Major version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the major version number is 3. If no Service Pack has been installed, the value is zero.

[6]int: wServicePackMinor

Minor version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the minor version number is 0.

[7]int: wSuiteMask

Bit flags that identify the product suites available on the system. This member can be a combination of the VER_SUITE_* values.

[8]int: wProductType

Additional information about the system. This member can be one of the VER_NT_* values.

[9]int: wReserved



<span id="win32api.GetVolumeInformation">win32api.GetVolumeInformation</span>
===

## [win32api](#win32api).GetVolumeInformation
tuple = **GetVolumeInformation(path** )
Returns information about a file system and colume whose root directory is specified.

### Parameters

path: string

The root path of the volume on which information is being requested.

### Return ValueThe return is a tuple of:
string - Volume Name
long - Volume serial number.
long - Maximum Component Length of a file name.
long - Sys Flags - other flags specific to the file system.  See the api for details.
string - File System Name

<span id="win32api.GetWindowLong">win32api.GetWindowLong</span>
===

## [win32api](#win32api).GetWindowLong
int = **GetWindowLong(hwnd, offset** )
Retrieves a long value at the specified offset into the extra window memory of the given window.

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The handle to the window.

offset: int

Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

### CommentsThis function calls the GetWindowLongPtr Api function

<span id="win32api.GetWindowsDirectory">win32api.GetWindowsDirectory</span>
===

## [win32api](#win32api).GetWindowsDirectory
string = **GetWindowsDirectory(** )
Returns the path of the Windows directory.

<span id="win32api.GlobalMemoryStatus">win32api.GlobalMemoryStatus</span>
===

## [win32api](#win32api).GlobalMemoryStatus
dict = **GlobalMemoryStatus(** )
Returns systemwide memory usage

### Return ValueReturns a dictionary representing a MEMORYSTATUS structure

<span id="win32api.GlobalMemoryStatusEx">win32api.GlobalMemoryStatusEx</span>
===

## [win32api](#win32api).GlobalMemoryStatusEx
dict = **GlobalMemoryStatusEx(** )
Returns physical and virtual memory usage

### CommentsOnly available on Win2k and later.

### Return ValueReturns a dictionary representing a MEMORYSTATUSEX structure

<span id="win32api.HIBYTE">win32api.HIBYTE</span>
===

## [win32api](#win32api).HIBYTE
int = **HIBYTE(val** )
An interface to the win32api HIBYTE macro.

### Parameters

val: int

The value to retrieve the HIBYTE from.

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.HIWORD">win32api.HIWORD</span>
===

## [win32api](#win32api).HIWORD
int = **HIWORD(val** )
An interface to the win32api HIWORD macro.

### Parameters

val: int

The value to retrieve the HIWORD from.

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.InitiateSystemShutdown">win32api.InitiateSystemShutdown</span>
===

## [win32api](#win32api).InitiateSystemShutdown
 **InitiateSystemShutdown(computerName, message, timeOut, bForceClose, bRebootAfterShutdown** )
Initiates a shutdown and optional restart of the specified computer.

### Parameters

computerName: string/[PyUnicode](#PyUnicode)

Specifies the name of the computer to shut-down, or None

message: string/[PyUnicode](#PyUnicode)

Message to display in a dialog box

timeOut: int

Specifies the time (in seconds) that the dialog box should be displayed. While this dialog box is displayed, the shutdown can be stopped by the AbortSystemShutdown function. 

If dwTimeout is zero, the computer shuts down without displaying the dialog box, and the shutdown cannot be stopped by AbortSystemShutdown.

bForceClose: int

Specifies whether applications with unsaved changes are to be forcibly closed. If this parameter is TRUE, such applications are closed. If this parameter is FALSE, a dialog box is displayed prompting the user to close the applications.

bRebootAfterShutdown: int

Specifies whether the computer is to restart immediately after shutting down. If this parameter is TRUE, the computer is to restart. If this parameter is FALSE, the system flushes all caches to disk, clears the screen, and displays a message indicating that it is safe to power down.

### Win32 API References

Search forInitiateSystemShutdownat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=InitiateSystemShutdown),[google](#http://www.google.com/search?q=InitiateSystemShutdown)or[google groups](#http://groups.google.com/groups?q=InitiateSystemShutdown).

<span id="win32api.LOBYTE">win32api.LOBYTE</span>
===

## [win32api](#win32api).LOBYTE
int = **LOBYTE(val** )
An interface to the win32api LOBYTE macro.

### Parameters

val: int

The value to retrieve the LOBYTE from.

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.LOWORD">win32api.LOWORD</span>
===

## [win32api](#win32api).LOWORD
int = **LOWORD(val** )
An interface to the win32api LOWORD macro.

### Parameters

val: int

The value to retrieve the LOWORD from.

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.LoadCursor">win32api.LoadCursor</span>
===

## [win32api](#win32api).LoadCursor
[PyHANDLE](#PyHANDLE)= **LoadCursor(hInstance, cursorid** )
Loads a cursor.

### Parameters

hInstance:[PyHANDLE](#PyHANDLE)

Handle to the instance to load the resource from, or None to load a standard system cursor

cursorid:[PyResourceId](#PyResourceId)

The ID of the cursor.  Can be a resource id or for system cursors, one of win32con.IDC_*

### Win32 API References

Search forLoadCursorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadCursor),[google](#http://www.google.com/search?q=LoadCursor)or[google groups](#http://groups.google.com/groups?q=LoadCursor).

<span id="win32api.LoadKeyboardLayout">win32api.LoadKeyboardLayout</span>
===

## [win32api](#win32api).LoadKeyboardLayout
int = **LoadKeyboardLayout(KLID, Flags** )
Loads a new locale id

### Parameters

KLID: string

Hex string containing a locale id, eg "00000409"

Flags=0: int

Combination of win32con.KLF_* constants

### Return ValueReturns the numeric locale id that was loaded

<span id="win32api.LoadLibrary">win32api.LoadLibrary</span>
===

## [win32api](#win32api).LoadLibrary
int = **LoadLibrary(fileName** )
Loads the specified DLL, and returns the handle.

### Parameters

fileName: string

Specifies the file name of the module to load.

### Win32 API References

Search forLoadLibraryat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadLibrary),[google](#http://www.google.com/search?q=LoadLibrary)or[google groups](#http://groups.google.com/groups?q=LoadLibrary).

<span id="win32api.LoadLibraryEx">win32api.LoadLibraryEx</span>
===

## [win32api](#win32api).LoadLibraryEx
[PyHANDLE](#PyHANDLE)= **LoadLibraryEx(fileName, handle, handle** )
Loads the specified DLL, and returns the handle.

### Parameters

fileName: string

Specifies the file name of the module to load.

handle:[PyHANDLE](#PyHANDLE)

Reserved - must be zero

handle: flags

Specifies the action to take when loading the module.

### Win32 API References

Search forLoadLibraryExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LoadLibraryEx),[google](#http://www.google.com/search?q=LoadLibraryEx)or[google groups](#http://groups.google.com/groups?q=LoadLibraryEx).

<span id="win32api.LoadResource">win32api.LoadResource</span>
===

## [win32api](#win32api).LoadResource
string = **LoadResource(handle, type, name, language** )
Finds and loads a resource from a PE file.

### Parameters

handle:[PyHANDLE](#PyHANDLE)

The handle of the module containing the resource.  Use None for currrent process executable.

type:[PyResourceId](#PyResourceId)

The type of resource to load.

name:[PyResourceId](#PyResourceId)

The name or Id of the resource to load.

language=NEUTRAL: int

Language to use, defaults to LANG_NEUTRAL.

<span id="win32api.LoadString">win32api.LoadString</span>
===

## [win32api](#win32api).LoadString
[PyUnicode](#PyUnicode)= **LoadString(handle, stringId, numChars** )
Loads a string from a resource file.

### Parameters

handle:[PyHANDLE](#PyHANDLE)

The handle of the module containing the resource.

stringId: int

The ID of the string to load.

numChars=1024: int

Number of characters to allocate for the return buffer.

<span id="win32api.MAKELANGID">win32api.MAKELANGID</span>
===

## [win32api](#win32api).MAKELANGID
int = **MAKELANGID(PrimaryLanguage, SubLanguage** )
Creates a language identifier from a primary language identifier and a sublanguage identifier.

### Parameters

PrimaryLanguage: int

Primary language identifier

SubLanguage: int

The sublanguage identifier

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.MAKELONG">win32api.MAKELONG</span>
===

## [win32api](#win32api).MAKELONG
int = **MAKELONG(low, high** )
creates a LONG value by concatenating the specified values.

### Parameters

low: int

Specifies the low-order byte of the new value.

high: int

Specifies the high-order byte of the new value.

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.MAKEWORD">win32api.MAKEWORD</span>
===

## [win32api](#win32api).MAKEWORD
int = **MAKEWORD(low, high** )
creates a WORD value by concatenating the specified values.

### Parameters

low: int

Specifies the low-order byte of the new value.

high: int

Specifies the high-order byte of the new value.

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.MapVirtualKey">win32api.MapVirtualKey</span>
===

## [win32api](#win32api).MapVirtualKey
int = **MapVirtualKey(vk, type, hlayout** )
Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code.

### Parameters

vk: int

The virtual key code.

type: int

The type of conversion to make - see the API

hlayout=None: handle

The keyboard layout to use.  If not 

specified, the API function MapVirtualKey will be called.  If it 

is specified MapVirtualKeyEx will be called.

### Commentsimplemented by calling the unicode versions of the API (MapVirtualKeyW/MapVirtualKeyExW)

<span id="win32api.MessageBeep">win32api.MessageBeep</span>
===

## [win32api](#win32api).MessageBeep
int = **MessageBeep(type** )
Plays a predefined waveform sound.

### Parameters

type=win32con.MB_OK: int

Specifies the sound type, as 

identified by an entry in the [sounds] section of the 

registry. This parameter can be one of MB_ICONASTERISK, 

MB_ICONEXCLAMATION, MB_ICONHAND, MB_ICONQUESTION or MB_OK.

### CommentsThe waveform sound for each sound type is identified by an entry in the [sounds] section of the registry.

<span id="win32api.MessageBox">win32api.MessageBox</span>
===

## [win32api](#win32api).MessageBox
int = **MessageBox(hwnd, message, title, style, language** )
Display a message box.

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The handle of the parent window.  See the comments section.

message: string

The message to be displayed in the message box.

title: string/None

The title for the message box.  If None, the applications title will be used.

style=win32con.MB_OK: int

The style of the message box.

language=win32api.MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT): int

The language ID to use.

### CommentsNormally, a program in a GUI environment will use one of the MessageBox 

methods supplied by the GUI (eg,[win32ui::MessageBox](#win32ui.MessageBox)or[PyCWnd::MessageBox](#PyCWnd.MessageBox))

### Return ValueAn integer identifying the button pressed to dismiss the dialog.

<span id="win32api.MonitorFromPoint">win32api.MonitorFromPoint</span>
===

## [win32api](#win32api).MonitorFromPoint
[PyHANDLE](#PyHANDLE)= **MonitorFromPoint(pt, Flags** )
Finds monitor that contains a point

### Parameters

pt: (int, int)

Tuple of 2 ints (x,y) specifying screen coordinates

Flags=0: int

Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

### CommentsAccepts keyword arguments

### Return ValueReturns None if no monitor was found

<span id="win32api.MonitorFromRect">win32api.MonitorFromRect</span>
===

## [win32api](#win32api).MonitorFromRect
[PyHANDLE](#PyHANDLE)= **MonitorFromRect(rc, Flags** )
Finds monitor that has largest intersection with a rectangle

### Parameters

rc:[PyRECT](#PyRECT)

Rectangle to be examined

Flags=0: int

Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

### CommentsAccepts keyword arguments

### Return ValueReturns None if no monitor was found

<span id="win32api.MonitorFromWindow">win32api.MonitorFromWindow</span>
===

## [win32api](#win32api).MonitorFromWindow
[PyHANDLE](#PyHANDLE)= **MonitorFromWindow(hwnd, Flags** )
Finds monitor that contains a window

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

Handle to a window

Flags=0: int

Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY

### CommentsAccepts keyword arguments

### Return ValueReturns None if no monitor was found

<span id="win32api.MoveFile">win32api.MoveFile</span>
===

## [win32api](#win32api).MoveFile
 **MoveFile(srcName, destName** )
Renames a file, or a directory (including its children).

### Parameters

srcName: string

The name of the source file.

destName: string

The name of the destination file.

### CommentsThis method can not move files across volumes.

### Win32 API References

Search forMoveFile.at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MoveFile.),[google](#http://www.google.com/search?q=MoveFile.)or[google groups](#http://groups.google.com/groups?q=MoveFile.).

<span id="win32api.MoveFileEx">win32api.MoveFileEx</span>
===

## [win32api](#win32api).MoveFileEx
 **MoveFileEx(srcName, destName, flag** )
Renames a file.

### Parameters

srcName: string

The name of the source file.

destName: string

The name of the destination file.  May be None.

flag: int

Flags indicating how the move is to be performed.  See the API for full details.

### CommentsThis method can move files across volumes.
If destName is None, and flags contains win32con.MOVEFILE_DELAY_UNTIL_REBOOT, the 

file will be deleted next reboot.

### Win32 API References

Search forMoveFileExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MoveFileEx),[google](#http://www.google.com/search?q=MoveFileEx)or[google groups](#http://groups.google.com/groups?q=MoveFileEx).

<span id="win32api.OpenProcess">win32api.OpenProcess</span>
===

## [win32api](#win32api).OpenProcess
[PyHANDLE](#PyHANDLE)= **OpenProcess(reqdAccess, bInherit, pid** )
Retrieves a handle to an existing process

### Parameters

reqdAccess: int

The required access.

bInherit: int

Specifies whether the returned handle can be inherited by a new process created by the current process. If TRUE, the handle is inheritable.

pid: int

The process ID

<span id="win32api.OutputDebugString">win32api.OutputDebugString</span>
===

## [win32api](#win32api).OutputDebugString
 **OutputDebugString(msg** )
Sends a string to the Windows debugging device.

### Parameters

msg: string

The string to write.

<span id="win32api.PostMessage">win32api.PostMessage</span>
===

## [win32api](#win32api).PostMessage
 **PostMessage(hwnd, idMessage, wParam, lParam** )
Post a message to a window.

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The hWnd of the window to receive the message.

idMessage: int

The ID of the message to post.

wParam=None: int

The wParam for the message

lParam=None: int

The lParam for the message

### Win32 API References

Search forPostMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostMessage),[google](#http://www.google.com/search?q=PostMessage)or[google groups](#http://groups.google.com/groups?q=PostMessage).

<span id="win32api.PostQuitMessage">win32api.PostQuitMessage</span>
===

## [win32api](#win32api).PostQuitMessage
 **PostQuitMessage(exitCode** )
Post a quit message to an app.

### Parameters

exitCode=0: int

The exit code

### Win32 API References

Search forPostQuitMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostQuitMessage),[google](#http://www.google.com/search?q=PostQuitMessage)or[google groups](#http://groups.google.com/groups?q=PostQuitMessage).

<span id="win32api.PostThreadMessage">win32api.PostThreadMessage</span>
===

## [win32api](#win32api).PostThreadMessage
 **PostThreadMessage(tid, idMessage, wParam, lParam** )
Post a message to the specified thread.

### Parameters

tid: int

Identifier of the thread to which the message will be posted.

idMessage: int

The ID of the message to post.

wParam=None: int/str

The wParam for the message

lParam=None: int/str

The lParam for the message

### Win32 API References

Search forPostThreadMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PostThreadMessage),[google](#http://www.google.com/search?q=PostThreadMessage)or[google groups](#http://groups.google.com/groups?q=PostThreadMessage).

<span id="win32api.RGB">win32api.RGB</span>
===

## [win32api](#win32api).RGB
int = **RGB(red, green, blue** )
An interface to the win32api RGB macro.

### Parameters

red: int

The red value

green: int

The green value

blue: int

The blue value

### CommentsThis is simply a wrapper to a C++ macro.

<span id="win32api.RegCloseKey">win32api.RegCloseKey</span>
===

## [win32api](#win32api).RegCloseKey
 **RegCloseKey(key** )
Closes a previously opened registry key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

The key to be closed.

### Win32 API References

Search forRegCloseKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCloseKey),[google](#http://www.google.com/search?q=RegCloseKey)or[google groups](#http://groups.google.com/groups?q=RegCloseKey).

<span id="win32api.RegConnectRegistry">win32api.RegConnectRegistry</span>
===

## [win32api](#win32api).RegConnectRegistry
int = **RegConnectRegistry(computerName, key** )
Establishes a connection to a predefined registry handle on another computer.

### Parameters

computerName: string

The name of the remote computer, of the form \\\\computername.  If None, the local computer is used.

key: int

The predefined handle.  May be win32con.HKEY_LOCAL_MACHINE or win32con.HKEY_USERS.

### Win32 API References

Search forRegConnectRegistryat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegConnectRegistry),[google](#http://www.google.com/search?q=RegConnectRegistry)or[google groups](#http://groups.google.com/groups?q=RegConnectRegistry).

### Return ValueThe return value is the handle of the opened key. 

If the function fails, an exception is raised.

<span id="win32api.RegCopyTree">win32api.RegCopyTree</span>
===

## [win32api](#win32api).RegCopyTree
 **RegCopyTree(KeySrc, SubKey, KeyDest** )
Copies an entire registry key to another location

### Parameters

KeySrc:[PyHKEY](#PyHKEY)

Registry key to be copied

SubKey:[PyUnicode](#PyUnicode)

Subkey to be copied, can be None

KeyDest:[PyHKEY](#PyHKEY)

The destination key

### CommentsAccepts keyword args.
Requires Vista or later.

<span id="win32api.RegCreateKey">win32api.RegCreateKey</span>
===

## [win32api](#win32api).RegCreateKey
[PyHKEY](#PyHKEY)= **RegCreateKey(key, subKey** )
Creates the specified key, or opens the key if it already exists.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

subKey: string

The name of a key that this method opens or creates. 

This key must be a subkey of the key identified by the key parameter. 

If key is one of the predefined keys, subKey may be None. In that case, 

the handle returned is the same hkey handle passed in to the function.

### Win32 API References

Search forRegCreateKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKey),[google](#http://www.google.com/search?q=RegCreateKey)or[google groups](#http://groups.google.com/groups?q=RegCreateKey).

### Return ValueThe return value is the handle of the opened key. 

If the function fails, an exception is raised.

<span id="win32api.RegCreateKeyEx">win32api.RegCreateKeyEx</span>
===

## [win32api](#win32api).RegCreateKeyEx
[PyHKEY](#PyHKEY), int = **RegCreateKeyEx(Key, SubKey, samDesired, Class, Options, SecurityAttributes, Transaction** )
Extended version of RegCreateKey

### Parameters

Key:[PyHKEY](#PyHKEY)/int

Registry key or one of win32con.HKEY_* values

SubKey:[PyUnicode](#PyUnicode)

Name of subkey to open or create.

samDesired: int

Access allowed to handle, combination of win32con.KEY_* constants.  Can also contain 

standard access rights such as DELETE, WRITE_OWNER, etc.

Class=None:[PyUnicode](#PyUnicode)

Name of registry key class

Options=REG_OPTION_NON_VOLATILE: int

One of the winnt.REG_OPTION_* values

SecurityAttributes=None:[PySECURITY_ATTRIBUTES](#PySECURITY.ATTRIBUTES)

Specifies security for key and handle inheritance

Transaction=None:[PyHANDLE](#PyHANDLE)

Handle to a transaction as returned by[win32transaction::CreateTransaction](#win32transaction.CreateTransaction)

### CommentsImplemented only as Unicode (RegCreateKeyExW).  Accepts keyword arguments.
If a transaction handle is passed in, RegCreateKeyTransacted will be called (requires Vista or later)

### Win32 API References

Search forRegCreateKeyExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKeyEx),[google](#http://www.google.com/search?q=RegCreateKeyEx)or[google groups](#http://groups.google.com/groups?q=RegCreateKeyEx).

Search forRegCreateKeyTransactedat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegCreateKeyTransacted),[google](#http://www.google.com/search?q=RegCreateKeyTransacted)or[google groups](#http://groups.google.com/groups?q=RegCreateKeyTransacted).

### Return ValueReturns registry handle and flag indicating if key was opened or created (REG_CREATED_NEW_KEY or REG_OPENED_EXISTING_KEY)

<span id="win32api.RegDeleteKey">win32api.RegDeleteKey</span>
===

## [win32api](#win32api).RegDeleteKey
 **RegDeleteKey(key, subKey** )
Deletes the specified key.  This method can not delete keys with subkeys.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

subKey: string

The name of the key to delete. 

This key must be a subkey of the key identified by the key parameter. 

This value must not be None, and the key may not have subkeys.

### CommentsIf the method succeeds, the entire key, including all of its values, is removed. 

If the method fails, and exception is raised.

### Win32 API References

Search forRegDeleteKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKey),[google](#http://www.google.com/search?q=RegDeleteKey)or[google groups](#http://groups.google.com/groups?q=RegDeleteKey).

<span id="win32api.RegDeleteKeyEx">win32api.RegDeleteKeyEx</span>
===

## [win32api](#win32api).RegDeleteKeyEx
 **RegDeleteKeyEx(Key, SubKey, samDesired, Transaction** )
Deletes a registry key from 32 or 64 bit registry view

### Parameters

Key:[PyHKEY](#PyHKEY)/int

Registry key or one of win32con.HKEY_* values

SubKey:[PyUnicode](#PyUnicode)

Name of subkey to be deleted.

samDesired=0: int

Can be KEY_WOW64_32KEY or KEY_WOW64_64KEY to specify alternate registry view

Transaction=None:[PyHANDLE](#PyHANDLE)

Handle to a transaction as returned by[win32transaction::CreateTransaction](#win32transaction.CreateTransaction)

### CommentsAccepts keyword args.
Requires 64-bit XP, Vista, or later.
Key to be deleted cannot contain subkeys
If a transaction handle is specified, RegDeleteKeyTransacted is called

### Win32 API References

Search forRegDeleteKeyExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKeyEx),[google](#http://www.google.com/search?q=RegDeleteKeyEx)or[google groups](#http://groups.google.com/groups?q=RegDeleteKeyEx).

Search forRegDeleteKeyTransactedat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteKeyTransacted),[google](#http://www.google.com/search?q=RegDeleteKeyTransacted)or[google groups](#http://groups.google.com/groups?q=RegDeleteKeyTransacted).

<span id="win32api.RegDeleteTree">win32api.RegDeleteTree</span>
===

## [win32api](#win32api).RegDeleteTree
 **RegDeleteTree(Key, SubKey** )
Recursively deletes a key's subkeys and values

### Parameters

Key:[PyHKEY](#PyHKEY)

Handle to a registry key

SubKey:[PyUnicode](#PyUnicode)

Name of subkey to be deleted, or None for all subkeys and values

### CommentsAccepts keyword args.
Requires Vista or later.

<span id="win32api.RegDeleteValue">win32api.RegDeleteValue</span>
===

## [win32api](#win32api).RegDeleteValue
 **RegDeleteValue(key, value** )
Removes a named value from the specified registry key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

value: string

The name of the value to remove.

### Win32 API References

Search forRegDeleteValueat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegDeleteValue),[google](#http://www.google.com/search?q=RegDeleteValue)or[google groups](#http://groups.google.com/groups?q=RegDeleteValue).

<span id="win32api.RegEnumKey">win32api.RegEnumKey</span>
===

## [win32api](#win32api).RegEnumKey
string = **RegEnumKey(key, index** )
Enumerates subkeys of the specified open registry key. The function retrieves the name of one subkey each time it is called.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

index: int

The index of the key to retrieve.

### Win32 API References

Search forRegEnumKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegEnumKey),[google](#http://www.google.com/search?q=RegEnumKey)or[google groups](#http://groups.google.com/groups?q=RegEnumKey).

<span id="win32api.RegEnumKeyEx">win32api.RegEnumKeyEx</span>
===

## [win32api](#win32api).RegEnumKeyEx
tuple = **RegEnumKeyEx(Key** )
Lists subkeys of a registry key

### Parameters

Key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS.

### Return ValueReturns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

<span id="win32api.RegEnumKeyExW">win32api.RegEnumKeyExW</span>
===

## [win32api](#win32api).RegEnumKeyExW
tuple = **RegEnumKeyExW(Key** )
Unicode version of RegEnumKeyEx

### Parameters

Key:[PyHKEY](#PyHKEY)

Registry handle opened with KEY_ENUMERATE_SUB_KEYS, or one of win32con.HKEY_* constants

### Return ValueReturns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

<span id="win32api.RegEnumValue">win32api.RegEnumValue</span>
===

## [win32api](#win32api).RegEnumValue
(string,object,type) = **RegEnumValue(key, index** )
Enumerates values of the specified open registry key. The function retrieves the name of one subkey each time it is called.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

index: int

The index of the key to retrieve.

### CommentsThis function is typically called repeatedly, until an exception is raised, indicating no more values.

### Win32 API References

Search forPyRegEnumValueat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PyRegEnumValue),[google](#http://www.google.com/search?q=PyRegEnumValue)or[google groups](#http://groups.google.com/groups?q=PyRegEnumValue).

<span id="win32api.RegFlushKey">win32api.RegFlushKey</span>
===

## [win32api](#win32api).RegFlushKey
 **RegFlushKey(key** )
Writes all the attributes of the specified key to the registry.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

### CommentsIt is not necessary to call RegFlushKey to change a key. 

Registry changes are flushed to disk by the registry using its lazy flusher. 

Registry changes are also flushed to disk at system shutdown.
Unlike[win32api::RegCloseKey](#win32api.RegCloseKey), the RegFlushKey method returns only when all the data has been written to the registry.
An application should only call RegFlushKey if it requires absolute certainty that registry changes are on disk. If you don't know whether a RegFlushKey call is required, it probably isn't.

### Win32 API References

Search forRegFlushKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegFlushKey),[google](#http://www.google.com/search?q=RegFlushKey)or[google groups](#http://groups.google.com/groups?q=RegFlushKey).

<span id="win32api.RegGetKeySecurity">win32api.RegGetKeySecurity</span>
===

## [win32api](#win32api).RegGetKeySecurity
[PySECURITY_DESCRIPTOR](#PySECURITY.DESCRIPTOR)= **RegGetKeySecurity(key, security_info** )
Retrieves the security on the specified registry key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

Handle to an open key for which the security descriptor is set.

security_info: int

Specifies the components of the security descriptor to retrieve. The value can be a combination of the *_SECURITY_INFORMATION constants.

### Win32 API References

Search forRegGetKeySecurityat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegGetKeySecurity),[google](#http://www.google.com/search?q=RegGetKeySecurity)or[google groups](#http://groups.google.com/groups?q=RegGetKeySecurity).

<span id="win32api.RegLoadKey">win32api.RegLoadKey</span>
===

## [win32api](#win32api).RegLoadKey
 **RegLoadKey(key, subKey, filename** )
The RegLoadKey method creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE 

and stores registration information from a specified file into that subkey.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

subKey: string

The name of the key to delete. 

This key must be a subkey of the key identified by the key parameter. 

This value must not be None, and the key may not have subkeys.

filename: string

The name of the file to load registry data from. 

This file must have been created with the[win32api::RegSaveKey](#win32api.RegSaveKey)function. 

Under the file allocation table (FAT) file system, the filename may not have an extension.

### CommentsA call to RegLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege.
If hkey is a handle returned by[win32api::RegConnectRegistry](#win32api.RegConnectRegistry), then the path specified in fileName is relative to the remote computer.

### Win32 API References

Search forRegLoadKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegLoadKey),[google](#http://www.google.com/search?q=RegLoadKey)or[google groups](#http://groups.google.com/groups?q=RegLoadKey).

<span id="win32api.RegNotifyChangeKeyValue">win32api.RegNotifyChangeKeyValue</span>
===

## [win32api](#win32api).RegNotifyChangeKeyValue
 **RegNotifyChangeKeyValue(key, bWatchSubTree, dwNotifyFilter, hKey, fAsynchronous** )
Receive notification of registry changes

### Parameters

key:[PyHKEY](#PyHKEY)/int

Handle to an open registry key

bWatchSubTree: int

Boolean, notify of changes to subkeys if True

dwNotifyFilter: int

Combination of REG_NOTIFY_CHANGE_* constants

hKey:[PyHANDLE](#PyHANDLE)

Event handle to be signalled, use None if fAsynchronous is False

fAsynchronous: int

Boolean, function returns immediately if True, waits for change if False

<span id="win32api.RegOpenCurrentUser">win32api.RegOpenCurrentUser</span>
===

## [win32api](#win32api).RegOpenCurrentUser
[PyHKEY](#PyHKEY)= **RegOpenCurrentUser(samDesired** )
Opens HKEY_CURRENT_USER for impersonated user

### Parameters

samDesired=MAXIMUM_ALLOWED: int

Desired access, combination of win32con.KEY_*

### Win32 API References

Search forRegOpenCurrentUserat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenCurrentUser),[google](#http://www.google.com/search?q=RegOpenCurrentUser)or[google groups](#http://groups.google.com/groups?q=RegOpenCurrentUser).

<span id="win32api.RegOpenKey">win32api.RegOpenKey</span>
===

## [win32api](#win32api).RegOpenKey
[PyHKEY](#PyHKEY)= **RegOpenKey(** )
Opens the specified key.

### CommentsThis funcion is implemented using[win32api::RegOpenKeyEx](#win32api.RegOpenKeyEx), by taking advantage 

of default parameters.  See[win32api::RegOpenKeyEx](#win32api.RegOpenKeyEx)for more details.

<span id="win32api.RegOpenKeyEx">win32api.RegOpenKeyEx</span>
===

## [win32api](#win32api).RegOpenKeyEx
[PyHKEY](#PyHKEY)= **RegOpenKeyEx(key, subKey, reserved, sam** )
Opens the specified key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

subKey: string

The name of a key that this method opens. 

This key must be a subkey of the key identified by the key parameter. 

If key is one of the predefined keys, subKey may be None. In that case, 

the handle returned is the same key handle passed in to the function.

reserved=0: int

Reserved.  Must be zero.

sam=KEY_READ: int

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


### Win32 API References

Search forRegOpenKeyExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenKeyEx),[google](#http://www.google.com/search?q=RegOpenKeyEx)or[google groups](#http://groups.google.com/groups?q=RegOpenKeyEx).

### Return ValueThe return value is the handle of the opened key. 

If the function fails, an exception is raised.

<span id="win32api.RegOpenKeyTransacted">win32api.RegOpenKeyTransacted</span>
===

## [win32api](#win32api).RegOpenKeyTransacted
[PyHKEY](#PyHKEY)= **RegOpenKeyTransacted(Key, SubKey, samDesired, Transaction, Options** )
Opens a registry key as part of a transaction

### Parameters

Key:[PyHKEY](#PyHKEY)/int

Registry key or one of win32con.HKEY_* values

SubKey:[PyUnicode](#PyUnicode)

Name of subkey to open.  Can be None to reopen an existing key.

samDesired: int

Access allowed to handle, combination of win32con.KEY_* constants.  Can also contain 

standard access rights such as DELETE, WRITE_OWNER, etc.

Transaction:[PyHANDLE](#PyHANDLE)

Handle to a transaction as returned by[win32transaction::CreateTransaction](#win32transaction.CreateTransaction)

Options=0: int

Reserved, use only 0

### CommentsAccepts keyword arguments.
Requires Vista or later.

### Win32 API References

Search forRegOpenKeyTransactedat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOpenKeyTransacted),[google](#http://www.google.com/search?q=RegOpenKeyTransacted)or[google groups](#http://groups.google.com/groups?q=RegOpenKeyTransacted).

### Return ValueReturns a transacted registry handle.  Note that operations on subkeys are not automatically transacted.

<span id="win32api.RegOverridePredefKey">win32api.RegOverridePredefKey</span>
===

## [win32api](#win32api).RegOverridePredefKey
 **RegOverridePredefKey(Key, NewKey** )
Redirects one of the predefined keys to different key

### Parameters

Key:[PyHKEY](#PyHKEY)

One of the predefined registry keys (win32con.HKEY_*)

NewKey:[PyHKEY](#PyHKEY)

Registry key to which it will be redirected.  Pass None to restore original key.

### CommentsRequires Windows 2000 or later.

### Win32 API References

Search forRegOverridePredefKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegOverridePredefKey),[google](#http://www.google.com/search?q=RegOverridePredefKey)or[google groups](#http://groups.google.com/groups?q=RegOverridePredefKey).

<span id="win32api.RegQueryInfoKey">win32api.RegQueryInfoKey</span>
===

## [win32api](#win32api).RegQueryInfoKey
(int, int, long) = **RegQueryInfoKey(key** )
Returns the number of 

subkeys, the number of values a key has, 

and if available the last time the key was modified as 

100's of nanoseconds since Jan 1, 1600.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or or any one of the following win32con 

constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

### Win32 API References

Search forRegQueryInfoKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryInfoKey),[google](#http://www.google.com/search?q=RegQueryInfoKey)or[google groups](#http://groups.google.com/groups?q=RegQueryInfoKey).

<span id="win32api.RegQueryInfoKeyW">win32api.RegQueryInfoKeyW</span>
===

## [win32api](#win32api).RegQueryInfoKeyW
dict = **RegQueryInfoKeyW(Key** )
Returns information about an open registry key

### Parameters

Key:[PyHKEY](#PyHKEY)

Handle to a registry key, or one of win32con.HKEY_* constants

### Win32 API References

Search forRegQueryInfoKeyWat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryInfoKeyW),[google](#http://www.google.com/search?q=RegQueryInfoKeyW)or[google groups](#http://groups.google.com/groups?q=RegQueryInfoKeyW).

<span id="win32api.RegQueryValue">win32api.RegQueryValue</span>
===

## [win32api](#win32api).RegQueryValue
string = **RegQueryValue(key, subKey** )
The RegQueryValue method retrieves the value associated with 

the unnamed value for a specified key in the registry.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

subKey: string

The name of the subkey with which the value is associated. 

If this parameter is None or empty, the function retrieves the value set by the[win32api::RegSetValue](#win32api.RegSetValue)method for the key identified by key.

### CommentsValues in the registry have name, type, and data components. This method 

retrieves the data for a key's first value that has a NULL name. 

But the underlying API call doesn't return the type, Lame Lame Lame, DONT USE THIS!!!

### Win32 API References

Search forRegQueryValueat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryValue),[google](#http://www.google.com/search?q=RegQueryValue)or[google groups](#http://groups.google.com/groups?q=RegQueryValue).

<span id="win32api.RegQueryValueEx">win32api.RegQueryValueEx</span>
===

## [win32api](#win32api).RegQueryValueEx
(object,type) = **RegQueryValueEx(key, valueName** )
Retrieves the type and data for a specified value name associated with an open registry key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

valueName: string

The name of the value to query.

### CommentsValues in the registry have name, type, and data components. This method 

retrieves the data for the given value.

### Win32 API References

Search forRegQueryValueExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegQueryValueEx),[google](#http://www.google.com/search?q=RegQueryValueEx)or[google groups](#http://groups.google.com/groups?q=RegQueryValueEx).

<span id="win32api.RegRestoreKey">win32api.RegRestoreKey</span>
===

## [win32api](#win32api).RegRestoreKey
 **RegRestoreKey(Key, File, Flags** )
Restores a key and subkeys from a saved registry file

### Parameters

Key:[PyHKEY](#PyHKEY)

Handle to registry key to be restored.  Can also be one of win32con.HKEY_* values.

File:[PyUnicode](#PyUnicode)

File from which to restore registry data

Flags=0: int

One of REG_FORCE_RESTORE,REG_NO_LAZY_FLUSH,REG_REFRESH_HIVE,REG_WHOLE_HIVE_VOLATILE (from winnt)

### CommentsImplemented only as Unicode (RegRestoreKeyW).  Accepts keyword arguments.
Requires SeBackupPrivilege and SeRestorePrivilege

### Win32 API References

Search forRegRestoreKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegRestoreKey),[google](#http://www.google.com/search?q=RegRestoreKey)or[google groups](#http://groups.google.com/groups?q=RegRestoreKey).

<span id="win32api.RegSaveKey">win32api.RegSaveKey</span>
===

## [win32api](#win32api).RegSaveKey
 **RegSaveKey(key, filename, sa** )
The RegSaveKey method saves the specified key, and all its subkeys to the specified file.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

filename: string

The name of the file to save registry data to. 

This file cannot already exist. If this filename includes an extension, it cannot be used on file allocation table (FAT) file systems by the[win32api::RegLoadKey](#win32api.RegLoadKey), **win32api::RegReplaceKey** , or[win32api::RegRestoreKey](#win32api.RegRestoreKey)methods.

sa=None:[PySECURITY_ATTRIBUTES](#PySECURITY.ATTRIBUTES)

The security attributes of the created file.

### CommentsIf key represents a key on a remote computer, the path described by fileName is relative to the remote computer.
The caller of this method must possess the SeBackupPrivilege security privilege.

### Win32 API References

Search forRegSaveKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSaveKey),[google](#http://www.google.com/search?q=RegSaveKey)or[google groups](#http://groups.google.com/groups?q=RegSaveKey).

<span id="win32api.RegSaveKeyEx">win32api.RegSaveKeyEx</span>
===

## [win32api](#win32api).RegSaveKeyEx
 **RegSaveKeyEx(Key, File, SecurityAttributes, Flags** )
Extended version of RegSaveKey

### Parameters

Key:[PyHKEY](#PyHKEY)

Handle to a registry key or one of HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER

File:[PyUnicode](#PyUnicode)

Name of file in which to save data.  File must not already exist.

SecurityAttributes=None:[PySECURITY_ATTRIBUTES](#PySECURITY.ATTRIBUTES)

Specifies security for the file to be created

Flags=REG_LATEST_FORMAT: int

One of REG_STANDARD_FORMAT,REG_LATEST_FORMAT,REG_NO_COMPRESSION (from winnt.py)

### CommentsImplemented only as Unicode (RegSaveKeyExW).  Accepts keyword arguments.
SE_BACKUP_NAME privilege must be enabled.

### Win32 API References

Search forRegSaveKeyExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSaveKeyEx),[google](#http://www.google.com/search?q=RegSaveKeyEx)or[google groups](#http://groups.google.com/groups?q=RegSaveKeyEx).

<span id="win32api.RegSetKeySecurity">win32api.RegSetKeySecurity</span>
===

## [win32api](#win32api).RegSetKeySecurity
 **RegSetKeySecurity(key, security_info, sd** )
Sets the security on the specified registry key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

Handle to an open key for which the security descriptor is set.

security_info: int

Specifies the components of the security descriptor to set. The value can be a combination of the *_SECURITY_INFORMATION constants.

sd:[PySECURITY_DESCRIPTOR](#PySECURITY.DESCRIPTOR)

The new security descriptor for the key

### CommentsIf key is one of the predefined keys, the predefined key should be closed with[win32api::RegCloseKey](#win32api.RegCloseKey). That ensures that the new security information is in effect the next time the predefined key is referenced.

### Win32 API References

Search forPyRegSetKeySecurityat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PyRegSetKeySecurity),[google](#http://www.google.com/search?q=PyRegSetKeySecurity)or[google groups](#http://groups.google.com/groups?q=PyRegSetKeySecurity).

<span id="win32api.RegSetValue">win32api.RegSetValue</span>
===

## [win32api](#win32api).RegSetValue
 **RegSetValue(key, subKey, type, value** )
Associates a value with a specified key.  Currently, only strings are supported.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

subKey: string

The name of the subkey with which the value is associated. 

This parameter can be None or empty, in which case the value will be added to the key identified by the key parameter.

type: int

Type of data. Must be win32con.REG_SZ

value: string

The value to associate with the key.

### CommentsIf the key specified by the lpszSubKey parameter does not exist, the RegSetValue function creates it.
Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access.

### Win32 API References

Search forRegSetValueat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSetValue),[google](#http://www.google.com/search?q=RegSetValue)or[google groups](#http://groups.google.com/groups?q=RegSetValue).

<span id="win32api.RegSetValueEx">win32api.RegSetValueEx</span>
===

## [win32api](#win32api).RegSetValueEx
 **RegSetValueEx(key, valueName, reserved, type, value** )
Stores data in the value field of an open registry key.

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_CLASSES_ROOT
HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE
HKEY_USERS

valueName: string

The name of the value to set. 

If a value with this name is not already present in the key, the method adds it to the key.
If this parameter is None or an empty string and the type parameter is the win32api.REG_SZ type, this function sets the same value the[win32api::RegSetValue](#win32api.RegSetValue)method would set.

reserved: any

Place holder for reserved argument.  Zero will always be passed to the API function.

type: int

Type of data.

 **Value**  **Meaning** REG_BINARYBinary data in any form.REG_DWORDA 32-bit number.REG_DWORD_LITTLE_ENDIANA 32-bit number in little-endian format. This is equivalent to REG_DWORD.
In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format.REG_QWORDA 64-bit number.REG_QWORD_LITTLE_ENDIANA 64-bit number in little-endian format. This is equivalent to REG_QWORD.
In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format. 

Windows NT and Windows 95 are designed to run on little-endian computer architectures. A user may connect to computers that have big-endian architectures, such as some UNIX systems.REG_DWORD_BIG_ENDIANA 32-bit number in big-endian format. 

In big-endian format, a multi-byte value is stored in memory from the highest byte (the big end) to the lowest byte. For example, the value 0x12345678 is stored as (0x12 0x34 0x56 0x78) in big-endian format.REG_EXPAND_SZA null-terminated string that contains unexpanded references to environment variables (for example, %PATH%). It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions.REG_LINKA Unicode symbolic link.REG_MULTI_SZAn array of null-terminated strings, terminated by two null characters.REG_NONENo defined value type.REG_RESOURCE_LISTA device-driver resource list.REG_SZA null-terminated string. It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions
value: registry data

The value to be stored with the specified value name.

### CommentsThis method can also set additional value and type information for the specified key.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access. 

To open the key, use the[win32api::RegCreateKeyEx](#win32api.RegCreateKeyEx)or[win32api::RegOpenKeyEx](#win32api.RegOpenKeyEx)methods.
Value lengths are limited by available memory. 

Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. 

This helps the registry perform efficiently.
The key identified by the key parameter must have been opened with KEY_SET_VALUE access.

### Win32 API References

Search forRegSetValueExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegSetValueEx),[google](#http://www.google.com/search?q=RegSetValueEx)or[google groups](#http://groups.google.com/groups?q=RegSetValueEx).

<span id="win32api.RegUnLoadKey">win32api.RegUnLoadKey</span>
===

## [win32api](#win32api).RegUnLoadKey
 **RegUnLoadKey(key, subKey** )
The RegUnLoadKey function unloads the specified registry key and its subkeys from the registry. 

The key should have been created by a previous call to[win32api::RegLoadKey](#win32api.RegLoadKey).

### Parameters

key:[PyHKEY](#PyHKEY)/int

An already open key, or any one of the following win32con constants:
HKEY_USERS
HKEY_LOCAL_MACHINE

subKey: string

The name of the key to unload. 

This key must be a subkey of the key identified by the key parameter. 

This value must not be None.

### CommentsA call to RegUnLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege.
If hkey is a handle returned by[win32api::RegConnectRegistry](#win32api.RegConnectRegistry), then the path specified in fileName is relative to the remote computer.

### Win32 API References

Search forRegUnLoadKeyat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegUnLoadKey),[google](#http://www.google.com/search?q=RegUnLoadKey)or[google groups](#http://groups.google.com/groups?q=RegUnLoadKey).

<span id="win32api.RegisterWindowMessage">win32api.RegisterWindowMessage</span>
===

## [win32api](#win32api).RegisterWindowMessage
 **RegisterWindowMessage(msgString** )
The RegisterWindowMessage method, given a string, returns a system wide unique 

message ID, suitable for sending messages between applications who both register the same string.

### Parameters

msgString: string

The name of the message to register. 

All applications that register this message string will get the same message. 

ID back.  It will be unique in the system and suitable for applications to 

use to exchange messages.

### CommentsOnly use RegisterWindowMessage when more than one application must process the
same message. For sending private messages within a window class, an application
can use any integer in the range WM_USER through 0x7FFF. (Messages in this range
are private to a window class, not to an application. For example, predefined
control classes such as BUTTON, EDIT, LISTBOX, and COMBOBOX may use values in
this range.)

### Win32 API References

Search forRegisterWindowMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=RegisterWindowMessage),[google](#http://www.google.com/search?q=RegisterWindowMessage)or[google groups](#http://groups.google.com/groups?q=RegisterWindowMessage).

<span id="win32api.SearchPath">win32api.SearchPath</span>
===

## [win32api](#win32api).SearchPath
int = **SearchPath(path, fileName, fileExt** )
Searches a path for the specified file.

### Parameters

path: string

The path to search.  If None, searches the standard paths.

fileName: string

The name of the file to search for.

fileExt=None: string

specifies an extension to be added to the filename when searching for the file. 

The first character of the filename extension must be a period (.). 

The extension is added only if the specified filename does not end with an extension. 

If a filename extension is not required or if the filename contains an extension, this parameter can be None.

### Win32 API References

Search forSearchPathat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SearchPath),[google](#http://www.google.com/search?q=SearchPath)or[google groups](#http://groups.google.com/groups?q=SearchPath).

### Return ValueThe return value is a tuple of (string, int).  string is the full 

path name located.  int is the offset in the string of the base name 

of the file.

<span id="win32api.SendMessage">win32api.SendMessage</span>
===

## [win32api](#win32api).SendMessage
 **SendMessage(hwnd, idMessage, wParam, lParam** )
Send a message to a window.

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The hWnd of the window to receive the message.

idMessage: int

The ID of the message to send.

wParam=None: int/string

The wParam for the message

lParam=None: int/string

The lParam for the message

### Win32 API References

Search forSendMessageat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SendMessage),[google](#http://www.google.com/search?q=SendMessage)or[google groups](#http://groups.google.com/groups?q=SendMessage).

<span id="win32api.SetClassLong">win32api.SetClassLong</span>
===

## [win32api](#win32api).SetClassLong
int = **SetClassLong(hwnd, offset, val** )
Replaces the specified 32 or 64 bit value at the specified offset into the extra class memory for the window.

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The handle to the window.

offset: int

Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

val: int

Specifies the long value to place in the window's reserved memory.

### CommentsThis function calls the SetClassLongPtr Api function

<span id="win32api.SetClassWord">win32api.SetClassWord</span>
===

## [win32api](#win32api).SetClassWord
int = **SetClassWord(hwnd, offset, val** )


### Parameters

hwnd: int

The handle to the window.

offset: int

Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

val: int

Specifies the long value to place in the window's reserved memory.

### CommentsThis function is obsolete, use[win32api::SetClassLong](#win32api.SetClassLong)instead

<span id="win32api.SetConsoleCtrlHandler">win32api.SetConsoleCtrlHandler</span>
===

## [win32api](#win32api).SetConsoleCtrlHandler
 **SetConsoleCtrlHandler(ctrlHandler, bAdd** )
Adds or removes an application-defined HandlerRoutine function from the list of handler functions for the calling process.

### Parameters

ctrlHandler: callable

The function to call.  This function 

should accept one param - the type of signal.

bAdd: int

True if the handler is being added, false if removed.

### CommentsNote that the implementation is a single CtrlHandler in C, which 

keeps a list of the handlers added by this function.  So although this 

function uses the same semantics as the Win32 function (ie, last 

registered first called, and first to return True stops the calls) the 

true order of all Python and C implemented CtrlHandlers may not match 

what would happen if all were implemented in C.
This handler must acquire the Python lock before it can call any 

of the registered handlers.  This means the handler may not be called 

until the current Python thread yields the lock.
A console process can use the[win32api::GenerateConsoleCtrlEvent](#win32api.GenerateConsoleCtrlEvent)function to send a CTRL+C or CTRL+BREAK signal to a console process 

group.
The system generates CTRL_CLOSE_EVENT, CTRL_LOGOFF_EVENT, and 

CTRL_SHUTDOWN_EVENT signals when the user closes the console, logs off, 

or shuts down the system so that the process has an opportunity to 

clean up before termination.

### Win32 API References

Search forSetConsoleCtrlHandlerat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetConsoleCtrlHandler),[google](#http://www.google.com/search?q=SetConsoleCtrlHandler)or[google groups](#http://groups.google.com/groups?q=SetConsoleCtrlHandler).

<span id="win32api.SetConsoleTitle">win32api.SetConsoleTitle</span>
===

## [win32api](#win32api).SetConsoleTitle
 **SetConsoleTitle(title** )
Sets the title for the current console.

### Parameters

title: string

The new title

### Win32 API References

Search forSetConsoleTitleat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetConsoleTitle),[google](#http://www.google.com/search?q=SetConsoleTitle)or[google groups](#http://groups.google.com/groups?q=SetConsoleTitle).

<span id="win32api.SetCursor">win32api.SetCursor</span>
===

## [win32api](#win32api).SetCursor
[PyHANDLE](#PyHANDLE)= **SetCursor(hCursor** )
Set the cursor to the HCURSOR object.

### Parameters

hCursor:[PyHANDLE](#PyHANDLE)

The new cursor. Can be None to remove cursor.

### Win32 API References

Search forSetCursorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetCursor),[google](#http://www.google.com/search?q=SetCursor)or[google groups](#http://groups.google.com/groups?q=SetCursor).

### Return ValueThe result is the previous cursor if there was one.

<span id="win32api.SetCursorPos">win32api.SetCursorPos</span>
===

## [win32api](#win32api).SetCursorPos
 **SetCursorPos(x,y** )
The SetCursorPos function moves the cursor to the specified screen coordinates.

### Parameters

x,y: (int, int)

The new position.

### Win32 API References

Search forSetCursorPosat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetCursorPos),[google](#http://www.google.com/search?q=SetCursorPos)or[google groups](#http://groups.google.com/groups?q=SetCursorPos).

<span id="win32api.SetDllDirectory">win32api.SetDllDirectory</span>
===

## [win32api](#win32api).SetDllDirectory
 **SetDllDirectory(PathName** )
Modifies the application-specific DLL search path

### Parameters

PathName:[PyUnicode](#PyUnicode)

Directory to be added to search path, can be None to restore defaults

### Win32 API References

Search forSetDllDirectoryat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetDllDirectory),[google](#http://www.google.com/search?q=SetDllDirectory)or[google groups](#http://groups.google.com/groups?q=SetDllDirectory).

<span id="win32api.SetEnvironmentVariable">win32api.SetEnvironmentVariable</span>
===

## [win32api](#win32api).SetEnvironmentVariable
 **SetEnvironmentVariable(Name, Value** )
Creates, deletes, or changes the value of an environment variable.

### Parameters

Name: str/unicode

Name of the environment variable

Value: str/unicode

Value to be set, use None to remove variable

### Win32 API References

Search forSetEnvironmentVariableat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetEnvironmentVariable),[google](#http://www.google.com/search?q=SetEnvironmentVariable)or[google groups](#http://groups.google.com/groups?q=SetEnvironmentVariable).

<span id="win32api.SetEnvironmentVariableW">win32api.SetEnvironmentVariableW</span>
===

## [win32api](#win32api).SetEnvironmentVariableW
 **SetEnvironmentVariableW(Name, Value** )
Creates, deletes, or changes the value of an environment variable.

### Parameters

Name: str

Name of the environment variable

Value: str

Value to be set, or None to remove variable

### Win32 API References

Search forSetEnvironmentVariableat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetEnvironmentVariable),[google](#http://www.google.com/search?q=SetEnvironmentVariable)or[google groups](#http://groups.google.com/groups?q=SetEnvironmentVariable).

<span id="win32api.SetErrorMode">win32api.SetErrorMode</span>
===

## [win32api](#win32api).SetErrorMode
int = **SetErrorMode(errorMode** )
Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.

### Parameters

errorMode: int

A set of bit flags that specify the process error mode

### Win32 API References

Search forSetErrorModeat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetErrorMode),[google](#http://www.google.com/search?q=SetErrorMode)or[google groups](#http://groups.google.com/groups?q=SetErrorMode).

### Return ValueThe result is an integer containing the old error flags.

<span id="win32api.SetFileAttributes">win32api.SetFileAttributes</span>
===

## [win32api](#win32api).SetFileAttributes
int = **SetFileAttributes(pathName, attrs** )
Sets the named file's attributes.

### Parameters

pathName: string

The name of the file.

attrs: int

The attributes to set.  Must be a combination of the win32con.FILE_ATTRIBUTE_* constants.

<span id="win32api.SetHandleInformation">win32api.SetHandleInformation</span>
===

## [win32api](#win32api).SetHandleInformation
 **SetHandleInformation(Object, Mask, Flags** )
Sets a handles's flags

### Parameters

Object:[PyHANDLE](#PyHANDLE)

Handle to an object

Mask: int

Bitmask specifying which flags should be set

Flags: int

Bitmask of flag values to be set. Valid Flags are HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE

### CommentsNot available on Win98/Me

<span id="win32api.SetLastError">win32api.SetLastError</span>
===

## [win32api](#win32api).SetLastError
int = **SetLastError(** )
Sets the calling thread's last error code value.

### Win32 API References

Search forSetLastErrorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetLastError),[google](#http://www.google.com/search?q=SetLastError)or[google groups](#http://groups.google.com/groups?q=SetLastError).

<span id="win32api.SetLocalTime">win32api.SetLocalTime</span>
===

## [win32api](#win32api).SetLocalTime
 **SetLocalTime(SystemTime** )
Changes the system's local time

### Parameters

SystemTime:[PyTime](#PyTime)

The local time to be set.  Can also be a time tuple.

<span id="win32api.SetStdHandle">win32api.SetStdHandle</span>
===

## [win32api](#win32api).SetStdHandle
 **SetStdHandle(handle, handle** )
Set the handle for the standard input, standard output, or standard error device

### Parameters

handle: int

input, output, or error device

handle:[PyHANDLE](#PyHANDLE)/int

A previously opened handle to be a standard handle

<span id="win32api.SetSysColors">win32api.SetSysColors</span>
===

## [win32api](#win32api).SetSysColors
 **SetSysColors(Elements, RgbValues** )
Changes color of various window elements

### Parameters

Elements: tuple

A tuple of ints, COLOR_* constants indicating which window element to change

RgbValues: tuple

An equal length tuple of ints representing RGB values (see[win32api::RGB](#win32api.RGB))

<span id="win32api.SetSystemFileCacheSize">win32api.SetSystemFileCacheSize</span>
===

## [win32api](#win32api).SetSystemFileCacheSize
 **SetSystemFileCacheSize(MinimumFileCacheSize, MaximumFileCacheSize, Flags** )
Sets the amount of memory reserved for file cache

### Parameters

MinimumFileCacheSize: long

Minimum size in bytes.

MaximumFileCacheSize: long

Maximum size in bytes.

Flags=0: int

Combination of win32con.MM_WORKING_SET_* flags

### CommentsRequires SE_INCREASE_QUOTA_NAME priv
Pass -1 for both min and max to flush file cache.
Accepts keyword args.

<span id="win32api.SetSystemPowerState">win32api.SetSystemPowerState</span>
===

## [win32api](#win32api).SetSystemPowerState
 **SetSystemPowerState(Suspend, Force** )
Initiates low power mode to make system sleep or hibernate

### Parameters

Suspend: boolean

True - system is suspended. False - initiates hibernation.

Force: boolean

True - power state occurs unconditionally. False - applications are queried for permission.

### CommentsRequires Win2k or later.
SE_SHUTDOWN_NAME privilege must be enabled.

### Win32 API References

Search forSetSystemPowerStateat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SetSystemPowerState),[google](#http://www.google.com/search?q=SetSystemPowerState)or[google groups](#http://groups.google.com/groups?q=SetSystemPowerState).

<span id="win32api.SetSystemTime">win32api.SetSystemTime</span>
===

## [win32api](#win32api).SetSystemTime
int = **SetSystemTime(year, month, dayOfWeek, day, hour, minute, second, millseconds** )
Returns the current system time

### Parameters

year: int



month: int



dayOfWeek: int



day: int



hour: int



minute: int



second: int



millseconds: int



<span id="win32api.SetThreadLocale">win32api.SetThreadLocale</span>
===

## [win32api](#win32api).SetThreadLocale
 **SetThreadLocale(lcid** )
Sets the current thread's locale.

### Parameters

lcid: int

The new LCID

<span id="win32api.SetTimeZoneInformation">win32api.SetTimeZoneInformation</span>
===

## [win32api](#win32api).SetTimeZoneInformation
tuple = **SetTimeZoneInformation(tzi** )
Sets the system time-zone information.

### Parameters

tzi: tuple

A tuple with the timezone info

### CommentsThe tuple is of form:

### Items

[0]int: Bias



[1]string: StandardName



[2]SYSTEMTIME tuple: StandardDate



[3]int: StandardBias



[4]string: DaylightName



[5]SYSTEMTIME tuple: DaylightDate



[6]int: DaylightBias



<span id="win32api.SetWindowLong">win32api.SetWindowLong</span>
===

## [win32api](#win32api).SetWindowLong
int = **SetWindowLong(hwnd, offset, val** )
Places a long value at the specified offset into the extra window memory of the given window.

### Parameters

hwnd: int

The handle to the window.

offset: int

Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

val: int

Specifies the long value to place in the window's reserved memory.

### CommentsThis function calls the SetWindowLongPtr Api function

<span id="win32api.SetWindowWord">win32api.SetWindowWord</span>
===

## [win32api](#win32api).SetWindowWord
int = **SetWindowWord(hwnd, offset, val** )


### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The handle to the window.

offset: int

Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.

val: int

Specifies the long value to place in the window's reserved memory.

### CommentsThis function is obsolete, use[win32api::SetWindowLong](#win32api.SetWindowLong)instead

<span id="win32api.ShellExecute">win32api.ShellExecute</span>
===

## [win32api](#win32api).ShellExecute
int = **ShellExecute(hwnd, op, file, params, dir, bShow** )
Opens or prints a file.

### Parameters

hwnd:[PyHANDLE](#PyHANDLE)

The handle of the parent window, or 0 for no parent.  This window receives any message boxes an application produces (for example, for error reporting).

op: string

The operation to perform.  May be "open", "print", or None, which defaults to "open".

file: string

The name of the file to open.

params: string

The parameters to pass, if the file name contains an executable.  Should be None for a document file.

dir: string

The initial directory for the application.

bShow: int

Specifies whether the application is shown when it is opened. If the lpszFile parameter specifies a document file, this parameter is zero.

### Win32 API References

Search forShellExecuteat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ShellExecute),[google](#http://www.google.com/search?q=ShellExecute)or[google groups](#http://groups.google.com/groups?q=ShellExecute).

### Return ValueThe instance handle of the application that was run. (This handle could also be the handle of a dynamic data exchange [DDE] server application.) 

If there is an error, the method raises an exception.

<span id="win32api.ShowCursor">win32api.ShowCursor</span>
===

## [win32api](#win32api).ShowCursor
int = **ShowCursor(show** )
The ShowCursor method displays or hides the cursor.

### Parameters

show: int

Visiblilty flag

### CommentsThis function sets an internal display counter that 

determines whether the cursor should be displayed. The 

cursor is displayed only if the display count is greater 

than or equal to 0. If a mouse is installed, the initial display 

count is 0. If no mouse is installed, the display count is -1.

### Win32 API References

Search forShowCursorat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=ShowCursor),[google](#http://www.google.com/search?q=ShowCursor)or[google groups](#http://groups.google.com/groups?q=ShowCursor).

### Return ValueThe return value specifies the new display counter

<span id="win32api.Sleep">win32api.Sleep</span>
===

## [win32api](#win32api).Sleep
int = **Sleep(time, bAlterable** )
Suspends execution of the current thread for the specified time.

### Parameters

time: int

The number of milli-seconds to sleep for,

bAlterable=0: int

Specifies whether the function may terminate early due to an I/O completion callback function.

### Win32 API References

Search forSleepat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=Sleep),[google](#http://www.google.com/search?q=Sleep)or[google groups](#http://groups.google.com/groups?q=Sleep).

Search forSleepExat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SleepEx),[google](#http://www.google.com/search?q=SleepEx)or[google groups](#http://groups.google.com/groups?q=SleepEx).

### Return ValueThe return value is zero if the specified time interval expired.

<span id="win32api.TerminateProcess">win32api.TerminateProcess</span>
===

## [win32api](#win32api).TerminateProcess
 **TerminateProcess(handle, exitCode** )
Kills a process

### Parameters

handle:[PyHANDLE](#PyHANDLE)

The handle of the process to terminate.

exitCode: int

The exit code for the process.

### CommentsSee also[win32api::OpenProcess](#win32api.OpenProcess)

<span id="win32api.ToAsciiEx">win32api.ToAsciiEx</span>
===

## [win32api](#win32api).ToAsciiEx
bytes = **ToAsciiEx(vk, scancode, keyboardstate, flags, hlayout** )
Translates the specified virtual-key code and keyboard state to the corresponding character or characters.

### Parameters

vk: int

The virtual key code.

scancode: int

The scan code.

keyboardstate: bytes

A string of exactly 256 characters.

flags=0: int



hlayout=None: handle

The keyboard layout to use

<span id="win32api.Unicode">win32api.Unicode</span>
===

## [win32api](#win32api).Unicode
[PyUnicode](#PyUnicode)= **Unicode(** )
Creates a new Unicode object

<span id="win32api.UpdateResource">win32api.UpdateResource</span>
===

## [win32api](#win32api).UpdateResource
 **UpdateResource(handle, type, name, data, language** )
Updates a resource in a PE file.

### Parameters

handle:[PyHANDLE](#PyHANDLE)

The update-file handle.

type:[PyResourceId](#PyResourceId)

The type of resource to update

name:[PyResourceId](#PyResourceId)

The id/name of the resource to update

data: string

The data to place into the resource.

language=NEUTRAL: int

Language to use, defaults to LANG_NEUTRAL.

<span id="win32api.VkKeyScan">win32api.VkKeyScan</span>
===

## [win32api](#win32api).VkKeyScan
int = **VkKeyScan(char, char** )
Translates a character to the corresponding virtual-key code and shift state.

### Parameters

char: string or unicode

A byte or unicode string of length 1.  If a byte string is passed 

VkKeyScanA will be called, otherwise VkKeyScanW will be called.

char: chr

Specifies a character

### Win32 API References

Search forVkKeyScanAat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanA),[google](#http://www.google.com/search?q=VkKeyScanA)or[google groups](#http://groups.google.com/groups?q=VkKeyScanA).

Search forVkKeyScanWat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanW),[google](#http://www.google.com/search?q=VkKeyScanW)or[google groups](#http://groups.google.com/groups?q=VkKeyScanW).

<span id="win32api.VkKeyScanEx">win32api.VkKeyScanEx</span>
===

## [win32api](#win32api).VkKeyScanEx
int = **VkKeyScanEx(char, hkl** )
Translates a character to the corresponding virtual-key code and shift state.

### Parameters

char: string or unicode

A byte or unicode string of length 1.  If a byte string is passed 

VkKeyScanExA will be called, otherwise VkKeyScanExW will be called.

hkl:[PyHANDLE](#PyHANDLE)

Handle to a keyboard layout at returned by[win32api::LoadKeyboardLayout](#win32api.LoadKeyboardLayout)

### Win32 API References

Search forVkKeyScanExAat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanExA),[google](#http://www.google.com/search?q=VkKeyScanExA)or[google groups](#http://groups.google.com/groups?q=VkKeyScanExA).

Search forVkKeyScanExWat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VkKeyScanExW),[google](#http://www.google.com/search?q=VkKeyScanExW)or[google groups](#http://groups.google.com/groups?q=VkKeyScanExW).

<span id="win32api.WinExec">win32api.WinExec</span>
===

## [win32api](#win32api).WinExec
 **WinExec(cmdLine, show** )
Runs the specified application.

### Parameters

cmdLine: string

The command line to execute.

show=win32con.SW_SHOWNORMAL: int

The initial state of the applications window.

### Win32 API References

Search forWinExecat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinExec),[google](#http://www.google.com/search?q=WinExec)or[google groups](#http://groups.google.com/groups?q=WinExec).

<span id="win32api.WinHelp">win32api.WinHelp</span>
===

## [win32api](#win32api).WinHelp
 **WinHelp(hwnd, hlpFile, cmd, data** )
Invokes the Windows Help system.

### Parameters

hwnd: int

The handle of the window requesting help.

hlpFile: string

The name of the help file.

cmd: int

The type of help.  See the api for full details.

data=0: int/string

Additional data specific to the help call.

### Win32 API References

Search forWinHelpat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WinHelp),[google](#http://www.google.com/search?q=WinHelp)or[google groups](#http://groups.google.com/groups?q=WinHelp).

### Return ValueThe method raises an exception if an error occurs.

<span id="win32api.WriteProfileSection">win32api.WriteProfileSection</span>
===

## [win32api](#win32api).WriteProfileSection
list = **WriteProfileSection(section, data, iniName** )
Writes a complete section to an INI file or registry.

### Parameters

section: string

The section in the INI file to be written.

data: string

The data to write.  Can be None to delete the section.  Otherwise, must be string, 

with each entry terminated with '\\0', followed by another terminating '\\0'

iniName=None: string

Name of INI file.  If specified, WritePrivateProfileSection will be called.

### CommentsThis function is obsolete, applications should use the registry instead.

### Win32 API References

Search forWriteProfileSectionat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WriteProfileSection),[google](#http://www.google.com/search?q=WriteProfileSection)or[google groups](#http://groups.google.com/groups?q=WriteProfileSection).

Search forWritePrivateProfileSectionat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WritePrivateProfileSection),[google](#http://www.google.com/search?q=WritePrivateProfileSection)or[google groups](#http://groups.google.com/groups?q=WritePrivateProfileSection).

<span id="win32api.WriteProfileVal">win32api.WriteProfileVal</span>
===

## [win32api](#win32api).WriteProfileVal
 **WriteProfileVal(section, entry, value, iniName** )
Writes a value to a Windows INI file.

### Parameters

section: string

The section in the INI file to write to.

entry: string

The entry within the section in the INI file to write to.

value: int/string

The value to write.

iniName=None: string

The name of the INI file.  If None, the system INI file is used.

### CommentsThis function is obsolete, applications should use the registry instead.

### Win32 API References

Search forWritePrivateProfileStringat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WritePrivateProfileString),[google](#http://www.google.com/search?q=WritePrivateProfileString)or[google groups](#http://groups.google.com/groups?q=WritePrivateProfileString).

Search forWriteProfileStringat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=WriteProfileString),[google](#http://www.google.com/search?q=WriteProfileString)or[google groups](#http://groups.google.com/groups?q=WriteProfileString).

<span id="win32api.keybd_event">win32api.keybd_event</span>
===

## [win32api](#win32api).keybd_event
 **keybd_event(bVk, bScan, dwFlags, dwExtraInfo** )
Simulate a keyboard event

### Parameters

bVk: BYTE

Virtual-key code

bScan: BYTE

Hardware scan code

dwFlags=0: DWORD

Flags specifying various function options

dwExtraInfo=0: DWORD

Additional data associated with keystroke

### Win32 API References

Search forkeybd_eventat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=keybd.event),[google](#http://www.google.com/search?q=keybd.event)or[google groups](#http://groups.google.com/groups?q=keybd.event).

<span id="win32api.mouse_event">win32api.mouse_event</span>
===

## [win32api](#win32api).mouse_event
 **mouse_event(dwFlags, dx, dy, dwData, dwExtraInfo** )
Simulate a mouse event

### Parameters

dwFlags=0: DWORD

Flags specifying various function options

dx: DWORD

Horizontal position of mouse

dy: DWORD

Vertical position of mouse

dwData: DWORD

Flag specific parameter

dwExtraInfo=0: DWORD

Additional data associated with mouse event

### Win32 API References

Search formouse_eventat[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=mouse.event),[google](#http://www.google.com/search?q=mouse.event)or[google groups](#http://groups.google.com/groups?q=mouse.event).