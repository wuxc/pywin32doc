
## Module win32process

An interface to the win32 Process and Thread API's

#### Methods


  - [STARTUPINFO](win32process.md#win32processstartupinfo)

    Creates a new STARTUPINFO object.&nbsp;

  - [beginthreadex](win32process.md#win32processbeginthreadex)

    Creates a new thread&nbsp;

  - [CreateRemoteThread](win32process.md#win32processcreateremotethread)

    creates a thread that runs in 

the virtual address space of another process.&nbsp;

  - [CreateProcess](win32process.md#win32processcreateprocess)

    Creates a new process and its primary thread. The new process executes the specified executable file.&nbsp;

  - [CreateProcessAsUser](win32process.md#win32processcreateprocessasuser)

    Creates a new process in the context of the specified user.&nbsp;

  - [GetCurrentProcess](win32process.md#win32processgetcurrentprocess)

    Retrieves a pseudo handle for the current process.&nbsp;

  - [GetProcessVersion](win32process.md#win32processgetprocessversion)

    Obtains the major and minor version numbers of the system on which a specified process expects to run.&nbsp;

  - [GetCurrentProcessId](win32process.md#win32processgetcurrentprocessid)

    Retrieves the process identifier of the calling process.&nbsp;

  - [GetStartupInfo](win32process.md#win32processgetstartupinfo)

    Retrieves the contents of the STARTUPINFO structure that was specified when the calling process was created.&nbsp;

  - [GetPriorityClass](win32process.md#win32processgetpriorityclass)

    &nbsp;

  - [GetExitCodeThread](win32process.md#win32processgetexitcodethread)

    &nbsp;

  - [GetExitCodeProcess](win32process.md#win32processgetexitcodeprocess)

    &nbsp;

  - [GetWindowThreadProcessId](win32process.md#win32processgetwindowthreadprocessid)

    Retrieves the identifier of the thread and process that created the specified window.&nbsp;

  - [SetThreadPriority](win32process.md#win32processsetthreadpriority)

    &nbsp;

  - [GetThreadPriority](win32process.md#win32processgetthreadpriority)

    &nbsp;

  - [GetProcessPriorityBoost](win32process.md#win32processgetprocesspriorityboost)

    Determines if dynamic priority adjustment is enabled for a process&nbsp;

  - [SetProcessPriorityBoost](win32process.md#win32processsetprocesspriorityboost)

    Enables or disables dynamic priority adjustment for a process&nbsp;

  - [GetThreadPriorityBoost](win32process.md#win32processgetthreadpriorityboost)

    Determines if dynamic priority adjustment is enabled for a thread&nbsp;

  - [SetThreadPriorityBoost](win32process.md#win32processsetthreadpriorityboost)

    Enables or disables dynamic priority adjustment for a thread&nbsp;

  - [GetThreadIOPendingFlag](win32process.md#win32processgetthreadiopendingflag)

    Determines if thread has any outstanding IO requests&nbsp;

  - [GetThreadTimes](win32process.md#win32processgetthreadtimes)

    Returns a thread's time statistics&nbsp;

  - [GetProcessId](win32process.md#win32processgetprocessid)

    Returns the Pid for a process handle&nbsp;

  - [SetPriorityClass](win32process.md#win32processsetpriorityclass)

    &nbsp;

  - [AttachThreadInput](win32process.md#win32processattachthreadinput)

    Attaches or detaches the input of two threads&nbsp;

  - [SetThreadIdealProcessor](win32process.md#win32processsetthreadidealprocessor)

    Used to specify a preferred processor for a thread. The system schedules threads on their preferred processors whenever possible.&nbsp;

  - [GetProcessAffinityMask](win32process.md#win32processgetprocessaffinitymask)

    Gets a processor affinity mask for a specified process&nbsp;

  - [SetProcessAffinityMask](win32process.md#win32processsetprocessaffinitymask)

    Sets a processor affinity mask for a specified process.&nbsp;

  - [SetThreadAffinityMask](win32process.md#win32processsetthreadaffinitymask)

    Sets a processor affinity mask for a specified thread.&nbsp;

  - [SuspendThread](win32process.md#win32processsuspendthread)

    Suspends the specified thread.&nbsp;

  - [ResumeThread](win32process.md#win32processresumethread)

    Resumes the specified thread. When the suspend count is decremented to zero, the execution of the thread is resumed.&nbsp;

  - [TerminateProcess](win32process.md#win32processterminateprocess)

    Terminates the specified process and all of its threads.&nbsp;

  - [ExitProcess](win32process.md#win32processexitprocess)

    Ends a process and all its threads&nbsp;

  - [EnumProcesses](win32process.md#win32processenumprocesses)

    Returns Pids for currently running processes&nbsp;

  - [EnumProcessModules](win32process.md#win32processenumprocessmodules)

    Lists loaded modules for a process handle&nbsp;

  - [EnumProcessModulesEx](win32process.md#win32processenumprocessmodulesex)

    Lists 32 or 64-bit modules load by a process&nbsp;

  - [GetModuleFileNameEx](win32process.md#win32processgetmodulefilenameex)

    Return name of module loaded by another process (uses process handle, not pid)&nbsp;

  - [GetProcessMemoryInfo](win32process.md#win32processgetprocessmemoryinfo)

    Returns process memory statistics as a dict representing a PROCESS_MEMORY_COUNTERS struct&nbsp;

  - [GetProcessTimes](win32process.md#win32processgetprocesstimes)

    Retrieve time statics for a process by handle.  (KernelTime and UserTime in 100 nanosecond units)&nbsp;

  - [GetProcessIoCounters](win32process.md#win32processgetprocessiocounters)

    Return I/O statistics for a process as a dictionary representing an IO_COUNTERS struct.&nbsp;

  - [GetProcessWindowStation](win32process.md#win32processgetprocesswindowstation)

    Returns a handle to the window station for the calling process&nbsp;

  - [GetProcessWorkingSetSize](win32process.md#win32processgetprocessworkingsetsize)

    Returns min and max working set sizes for a process by handle&nbsp;

  - [SetProcessWorkingSetSize](win32process.md#win32processsetprocessworkingsetsize)

    Sets minimum and maximum working set sizes for a process&nbsp;

  - [GetProcessShutdownParameters](win32process.md#win32processgetprocessshutdownparameters)

    Retrieves shutdown priority and flags for current process&nbsp;

  - [SetProcessShutdownParameters](win32process.md#win32processsetprocessshutdownparameters)

    Sets shutdown priority and flags for current process&nbsp;

  - [GetGuiResources](win32process.md#win32processgetguiresources)

    Returns the number of GDI or user object handles held by a process&nbsp;

  - [IsWow64Process](win32process.md#win32processiswow64process)

    Determines whether the specified process is running under WOW64.&nbsp;

## ABOVE_NORMAL_PRIORITY_CLASS
 **const win32process.ABOVE_NORMAL_PRIORITY_CLASS;** 
Windows 2000: Indicates a process that has priority above NORMAL_PRIORITY_CLASS but below HIGH_PRIORITY_CLASS.

## [win32process](README.md#win32process).AttachThreadInput

 **AttachThreadInput( *idAttach*  *, idAttachTo*  *, Attach* ** )
Attaches or detaches the input of two threads

#### Parameters


  -  *idAttach* : int

    The id of a thread

  -  *idAttachTo* : int

    The id of the thread to which it will be attached

  -  *Attach* : bool

    Indicates whether thread should be attached or detached

## BELOW_NORMAL_PRIORITY_CLASS
 **const win32process.BELOW_NORMAL_PRIORITY_CLASS;** 
Windows 2000: Indicates a process that has priority above IDLE_PRIORITY_CLASS but below NORMAL_PRIORITY_CLASS.

## CREATE_BREAKAWAY_FROM_JOB
 **const win32process.CREATE_BREAKAWAY_FROM_JOB;** 


## CREATE_DEFAULT_ERROR_MODE
 **const win32process.CREATE_DEFAULT_ERROR_MODE;** 
The new process does not inherit the error mode of the calling process. Instead, CreateProcess gives the new process the current default error mode. An application sets the current default error mode by calling SetErrorMode. 

This flag is particularly useful for multi-threaded shell applications that run with hard errors disabled.

## CREATE_NEW_CONSOLE
 **const win32process.CREATE_NEW_CONSOLE;** 
The new process has a new console, instead of inheriting the parent's console. This flag cannot be used with the DETACHED_PROCESS flag.

## CREATE_NEW_PROCESS_GROUP
 **const win32process.CREATE_NEW_PROCESS_GROUP;** 
The new process is the root process of a new process group. The process group includes all processes that are descendants of this root process. The process identifier of the new process group is the same as the process identifier, which is returned in the lpProcessInformation parameter. Process groups are used by the GenerateConsoleCtrlEvent function to enable sending a ctrl+c or ctrl+break signal to a group of console processes.

## CREATE_NO_WINDOW
 **const win32process.CREATE_NO_WINDOW;** 


## CREATE_PRESERVE_CODE_AUTHZ_LEVEL
 **const win32process.CREATE_PRESERVE_CODE_AUTHZ_LEVEL;** 


## CREATE_SEPARATE_WOW_VDM
 **const win32process.CREATE_SEPARATE_WOW_VDM;** 
Windows NT: This flag is valid only when starting a 16-bit Windows-based application. If set, the new process is run in a private Virtual DOS Machine (VDM). By default, all 16-bit Windows-based applications are run as threads in a single, shared VDM. The advantage of running separately is that a crash only kills the single VDM; any other programs running in distinct VDMs continue to function normally. Also, 16-bit Windows-based applications that are run in separate VDMs have separate input queues. That means that if one application hangs momentarily, applications in separate VDMs continue to receive input. The disadvantage of running separately is that it takes significantly more memory to do so. You should use this flag only if the user requests that 16-bit applications should run in them own VDM.

## CREATE_SHARED_WOW_VDM
 **const win32process.CREATE_SHARED_WOW_VDM;** 
Windows NT: The flag is valid only when starting a 16-bit Windows-based application. If the DefaultSeparateVDM switch in the Windows section of WIN.INI is TRUE, this flag causes the CreateProcess function to override the switch and run the new process in the shared Virtual DOS Machine.

## CREATE_SUSPENDED
 **const win32process.CREATE_SUSPENDED;** 


## CREATE_UNICODE_ENVIRONMENT
 **const win32process.CREATE_UNICODE_ENVIRONMENT;** 
If set, the environment block pointed to by lpEnvironment uses Unicode characters. If clear, the environment block uses ANSI characters.

## [win32process](README.md#win32process).CreateProcess

[PyHANDLE](README.md#pyhandle),[PyHANDLE](README.md#pyhandle), int, int = **CreateProcess( *appName*  *, commandLine*  *, processAttributes*  *, threadAttributes*  *, bInheritHandles*  *, dwCreationFlags*  *, newEnvironment*  *, currentDirectory*  *, startupinfo* ** )
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

    creation flags.  May be a combination of the following values from the win32con module:

 **Value**  **Meaning** CREATE_BREAKAWAY_FROM_JOBWindows 2000: The child processes of a process associated with a job are not associated with the job. 

If the calling process is not associated with a job, this flag has no effect. If the calling process is associated with a job, the job must set the JOB_OBJECT_LIMIT_BREAKAWAY_OK limit or CreateProcess will fail.CREATE_DEFAULT_ERROR_MODEThe new process does not inherit the error mode of the calling process. Instead, CreateProcess gives the new process the current default error mode. An application sets the current default error mode by calling SetErrorMode. 

This flag is particularly useful for multi-threaded shell applications that run with hard errors disabled. 

The default behavior for CreateProcess is for the new process to inherit the error mode of the caller. Setting this flag changes that default behavior.CREATE_FORCE_DOSWindows NT/2000: This flag is valid only when starting a 16-bit bound application. If set, the system will force the application to run as an MS-DOS-based application rather than as an OS/2-based application.CREATE_NEW_CONSOLEThe new process has a new console, instead of inheriting the parent's console. This flag cannot be used with the DETACHED_PROCESS flag.CREATE_NEW_PROCESS_GROUPThe new process is the root process of a new process group. The process group includes all processes that are descendants of this root process. The process identifier of the new process group is the same as the process identifier, which is returned in the lpProcessInformation parameter. Process groups are used by the GenerateConsoleCtrlEvent function to enable sending a CTRL+C or CTRL+BREAK signal to a group of console processes.CREATE_NO_WINDOWWindows NT/2000: This flag is valid only when starting a console application. If set, the console application is run without a console window.CREATE_SEPARATE_WOW_VDMWindows NT/2000: This flag is valid only when starting a 16-bit Windows-based application. If set, the new process runs in a private Virtual DOS Machine (VDM). By default, all 16-bit Windows-based applications run as threads in a single, shared VDM. The advantage of running separately is that a crash only terminates the single VDM; any other programs running in distinct VDMs continue to function normally. Also, 16-bit Windows-based applications that are run in separate VDMs have separate input queues. That means that if one application stops responding momentarily, applications in separate VDMs continue to receive input. The disadvantage of running separately is that it takes significantly more memory to do so. You should use this flag only if the user requests that 16-bit applications should run in them own VDM.CREATE_SHARED_WOW_VDMWindows NT/2000: The flag is valid only when starting a 16-bit Windows-based application. If the DefaultSeparateVDM switch in the Windows section of WIN.INI is TRUE, this flag causes the CreateProcess function to override the switch and run the new process in the shared Virtual DOS Machine.CREATE_SUSPENDEDThe primary thread of the new process is created in a suspended state, and does not run until the ResumeThread function is called.CREATE_UNICODE_ENVIRONMENTIndicates the format of the lpEnvironment parameter. If this flag is set, the environment block pointed to by lpEnvironment uses Unicode characters. Otherwise, the environment block uses ANSI characters.DEBUG_PROCESSIf this flag is set, the calling process is treated as a debugger, and the new process is debugged. The system notifies the debugger of all debug events that occur in the process being debugged. 

If you create a process with this flag set, only the calling thread (the thread that called CreateProcess) can call the WaitForDebugEvent function. 

Windows 95/98: This flag is not valid if the new process is a 16-bit application.DEBUG_ONLY_THIS_PROCESSIf this flag is not set and the calling process is being debugged, the new process becomes another process being debugged by the calling process's debugger. If the calling process is not a process being debugged, no debugging-related actions occur.DETACHED_PROCESSFor console processes, the new process does not have access to the console of the parent process. The new process can call the AllocConsole function at a later time to create a new console. This flag cannot be used with the CREATE_NEW_CONSOLE flag.ABOVE_NORMAL_PRIORITY_CLASSWindows 2000: Indicates a process that has priority higher than NORMAL_PRIORITY_CLASS but lower than HIGH_PRIORITY_CLASS.BELOW_NORMAL_PRIORITY_CLASSWindows 2000: Indicates a process that has priority higher than IDLE_PRIORITY_CLASS but lower than NORMAL_PRIORITY_CLASS.HIGH_PRIORITY_CLASSIndicates a process that performs time-critical tasks. The threads of a high-priority class process preempt the threads of normal-priority or idle-priority class processes. An example is the Task List, which must respond quickly when called by the user, regardless of the load on the system. Use extreme care when using the high-priority class, because a CPU-bound application with a high-priority class can use nearly all available cycles.IDLE_PRIORITY_CLASSIndicates a process whose threads run only when the system is idle and are preempted by the threads of any process running in a higher priority class. An example is a screen saver. The idle priority class is inherited by child processes.NORMAL_PRIORITY_CLASSIndicates a normal process with no special scheduling needs.REALTIME_PRIORITY_CLASSIndicates a process that has the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes, including operating system processes performing important tasks. For example, a real-time process that executes for more than a very brief interval can cause disk caches not to flush or cause the mouse to be unresponsive.
  -  *newEnvironment* : dictionary/None

    A dictionary of string or Unicode pairs to define the environment for the process, or None to inherit the current environment.

  -  *currentDirectory* : string

    current directory name, or None

  -  *startupinfo* :[PySTARTUPINFO](README.md#pystartupinfo)

    a STARTUPINFO object that specifies how the main window for the new process should appear.

#### Comments
The result is a tuple of (hProcess, hThread, dwProcessId, dwThreadId)

## [win32process](README.md#win32process).CreateProcessAsUser

[PyHANDLE](README.md#pyhandle),[PyHANDLE](README.md#pyhandle), int, int = **CreateProcessAsUser( *hToken*  *, appName*  *, commandLine*  *, processAttributes*  *, threadAttributes*  *, bInheritHandles*  *, dwCreationFlags*  *, newEnvironment*  *, currentDirectory*  *, startupinfo* ** )
Creates a new process in the context of the specified user.

#### Parameters


  -  *hToken* :[PyHANDLE](README.md#pyhandle)

    Handle to a token that represents a logged-on user

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

  -  *startupinfo* :[PySTARTUPINFO](README.md#pystartupinfo)

    a STARTUPINFO object that specifies how the main window for the new process should appear.

#### Comments
The result is a tuple of (hProcess, hThread, dwProcessId, dwThreadId)

## [win32process](README.md#win32process).CreateRemoteThread

[PyHANDLE](README.md#pyhandle), int = **CreateRemoteThread( *hprocess*  *, sa*  *, stackSize*  *, entryPoint*  *, Parameter*  *, flags* ** )
creates a thread that runs in 

the virtual address space of another process.

#### Parameters


  -  *hprocess* :[PyHANDLE](README.md#pyhandle)

    The handle to the remote process.

  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *stackSize* : int

    Stack size for the new thread, or zero for the default size.

  -  *entryPoint* : function

    The thread function's address.

  -  *Parameter* : int

    Arg passed to the function in the form of a void pointer

  -  *flags* : int

    

#### Return Value
The result is a tuple of the thread handle and thread ID.

## DEBUG_ONLY_THIS_PROCESS
 **const win32process.DEBUG_ONLY_THIS_PROCESS;** 
If not set and the calling process is being debugged, the new process becomes another process being debugged by the calling process's debugger. If the calling process is not a process being debugged, no debugging-related actions occur.

## DEBUG_PROCESS
 **const win32process.DEBUG_PROCESS;** 
If this flag is set, the calling process is treated as a debugger, and the new process is a process being debugged. The system notifies the debugger of all debug events that occur in the process being debugged. 

If you create a process with this flag set, only the calling thread (the thread that called CreateProcess) can call the WaitForDebugEvent function. 

Windows 95 and Windows 98: This flag is not valid if the new process is a 16-bit application.

## DETACHED_PROCESS
 **const win32process.DETACHED_PROCESS;** 
For console processes, the new process does not have access to the console of the parent process. The new process can call the AllocConsole function at a later time to create a new console. This flag cannot be used with the CREATE_NEW_CONSOLE flag.

## [win32process](README.md#win32process).EnumProcessModules

(long,....) = **EnumProcessModules( *hProcess* ** )
Lists loaded modules for a process handle

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

## [win32process](README.md#win32process).EnumProcessModulesEx

(long,....) = **EnumProcessModulesEx( *hProcess*  *, FilterFlag* ** )
Lists 32 or 64-bit modules load by a process

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

  -  *FilterFlag=LIST_MODULES_DEFAULT* : int

    Controls whether 32 or 64-bit modules are returned

#### Comments
Requires Vista or later

## [win32process](README.md#win32process).EnumProcesses

(long,....) = **EnumProcesses(** )
Returns Pids for currently running processes

## [win32process](README.md#win32process).ExitProcess

 **ExitProcess( *exitCode* ** )
Ends a process and all its threads

#### Parameters


  -  *exitCode* : int

    Specifies the exit code for the process, and for all threads that are terminated as a result of this call

#### Comments
ExitProcess is the preferred method of ending a process. This function provides 

a clean process shutdown. This includes calling the entry-point function of all 

attached dynamic-link libraries (DLLs) with a value indicating that the process 

is detaching from the DLL. If a process terminates by calling[win32process::TerminateProcess](win32process.md#win32processterminateprocess), the DLLs that the process is attached to are 

not notified of the process termination.

## [win32process](README.md#win32process).GetCurrentProcess

int = **GetCurrentProcess(** )
Retrieves a pseudo handle for the current process.

## [win32process](README.md#win32process).GetCurrentProcessId

int = **GetCurrentProcessId(** )
Retrieves the process identifier of the calling process.

## [win32process](README.md#win32process).GetExitCodeProcess

int = **GetExitCodeProcess( *handle* ** )


#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the process

## [win32process](README.md#win32process).GetExitCodeThread

int = **GetExitCodeThread( *handle* ** )


#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread

## [win32process](README.md#win32process).GetGuiResources

int = **GetGuiResources( *Process*  *, Flags* ** )
Returns the number of GDI or user object handles held by a process

#### Parameters


  -  *Process* :[PyHANDLE](README.md#pyhandle)

    Handle to a process as returned by[win32api::OpenProcess](win32api.md#win32apiopenprocess)

  -  *Flags* : int

    GR_GDIOBJECTS or GR_USEROBJECTS (from win32con)

#### Comments
Available on Win2k and up

## [win32process](README.md#win32process).GetModuleFileNameEx

[PyUNICODE](README.md#pyunicode)= **GetModuleFileNameEx( *hProcess*  *, hModule* ** )
Return name of module loaded by another process (uses process handle, not pid)

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

  -  *hModule* :[PyHANDLE](README.md#pyhandle)

    Module handle

## [win32process](README.md#win32process).GetPriorityClass

int = **GetPriorityClass( *handle* ** )


#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread

## [win32process](README.md#win32process).GetProcessAffinityMask

int, int = **GetProcessAffinityMask( *hProcess* ** )
Gets a processor affinity mask for a specified process

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    handle to the process of interest

#### Return Value
The result is a tuple of (process affinity mask, system affinity mask)

## [win32process](README.md#win32process).GetProcessId

int = **GetProcessId( *Process* ** )
Returns the Pid for a process handle

#### Parameters


  -  *Process* :[PyHANDLE](README.md#pyhandle)

    Handle to a process

## [win32process](README.md#win32process).GetProcessIoCounters

 **dict** = **GetProcessIoCounters( *hProcess* ** )
Return I/O statistics for a process as a dictionary representing an IO_COUNTERS struct.

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

## [win32process](README.md#win32process).GetProcessMemoryInfo

 **dict** = **GetProcessMemoryInfo( *hProcess* ** )
Returns process memory statistics as a dict representing a PROCESS_MEMORY_COUNTERS struct

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

## [win32process](README.md#win32process).GetProcessPriorityBoost

bool = **GetProcessPriorityBoost( *Process* ** )
Determines if dynamic priority adjustment is enabled for a process

#### Parameters


  -  *Process* :[PyHANDLE](README.md#pyhandle)

    Handle to a process

## [win32process](README.md#win32process).GetProcessShutdownParameters

int,int = **GetProcessShutdownParameters(** )
Retrieves shutdown priority and flags for current process

#### Comments
Ranges are 000-0FF Reserved by windows, 100-1FF Last, 200-2FF Middle, 300-3FF First, 400-4FF Reserved by Windows

## [win32process](README.md#win32process).GetProcessTimes

 **dict** = **GetProcessTimes( *hProcess* ** )
Retrieve time statics for a process by handle.  (KernelTime and UserTime in 100 nanosecond units)

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

## [win32process](README.md#win32process).GetProcessVersion

int = **GetProcessVersion( *processId* ** )
Obtains the major and minor version numbers of the system on which a specified process expects to run.

#### Parameters


  -  *processId* : int

    identifier specifying the process of interest.

## [win32process](README.md#win32process).GetProcessWindowStation

 **GetProcessWindowStation(** )
Returns a handle to the window station for the calling process

## [win32process](README.md#win32process).GetProcessWorkingSetSize

int,int = **GetProcessWorkingSetSize( *hProcess* ** )
Returns min and max working set sizes for a process by handle

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by[win32api::OpenProcess](win32api.md#win32apiopenprocess)

## [win32process](README.md#win32process).GetStartupInfo

[PySTARTUPINFO](README.md#pystartupinfo)= **GetStartupInfo(** )
Retrieves the contents of the STARTUPINFO structure that was specified when the calling process was created.

## [win32process](README.md#win32process).GetThreadIOPendingFlag

bool = **GetThreadIOPendingFlag( *Thread* ** )
Determines if thread has any outstanding IO requests

#### Parameters


  -  *Thread* :[PyHANDLE](README.md#pyhandle)

    Handle to a thread

## [win32process](README.md#win32process).GetThreadPriority

int = **GetThreadPriority( *handle* ** )


#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread

## [win32process](README.md#win32process).GetThreadPriorityBoost

bool = **GetThreadPriorityBoost( *Thread* ** )
Determines if dynamic priority adjustment is enabled for a thread

#### Parameters


  -  *Thread* :[PyHANDLE](README.md#pyhandle)

    Handle to a thread

## [win32process](README.md#win32process).GetThreadTimes

dict = **GetThreadTimes( *Thread* ** )
Returns a thread's time statistics

#### Parameters


  -  *Thread* :[PyHANDLE](README.md#pyhandle)

    Handle to a thread

## [win32process](README.md#win32process).GetWindowThreadProcessId

int, int = **GetWindowThreadProcessId( *hwnd* ** )
Retrieves the identifier of the thread and process that created the specified window.

#### Parameters


  -  *hwnd* : int

    handle to the window

#### Return Value
The result is a tuple of (threadId, processId)

## HIGH_PRIORITY_CLASS
 **const win32process.HIGH_PRIORITY_CLASS;** 
Indicates a process that performs time-critical tasks that must be executed immediately for it to run correctly. The threads of a high-priority class process preempt the threads of normal-priority or idle-priority class processes. An example is the Task List, which must respond quickly when called by the user, regardless of the load on the system. Use extreme care when using the high-priority class, because a high-priority class CPU-bound application can use nearly all available cycles.

## IDLE_PRIORITY_CLASS
 **const win32process.IDLE_PRIORITY_CLASS;** 
Indicates a process whose threads run only when the system is idle and are preempted by the threads of any process running in a higher priority class. An example is a screen saver. The idle priority class is inherited by child processes.

## [win32process](README.md#win32process).IsWow64Process

bool = **IsWow64Process( *Process* ** )
Determines whether the specified process is running under WOW64.

#### Parameters


  -  *Process=None* :[PyHANDLE](README.md#pyhandle)

    Handle to a process as returned by[win32api::OpenProcess](win32api.md#win32apiopenprocess),[win32api::GetCurrentProcess](win32api.md#win32apigetcurrentprocess), etc, or 

will use the current process handle if None (the default) is passed.

#### Return Value
If this function is not provided by the operating system, the 

return value is False (ie, a NotImplemented exception will never be thrown). 

However, if the function exists but fails, a win32process.error exception 

is thrown as normal.

## LIST_MODULES_32BIT
 **const win32process.LIST_MODULES_32BIT;** 


## LIST_MODULES_64BIT
 **const win32process.LIST_MODULES_64BIT;** 


## LIST_MODULES_ALL
 **const win32process.LIST_MODULES_ALL;** 


## LIST_MODULES_DEFAULT
 **const win32process.LIST_MODULES_DEFAULT;** 


## MAXIMUM_PROCESSORS
 **const win32process.MAXIMUM_PROCESSORS;** 


## NORMAL_PRIORITY_CLASS
 **const win32process.NORMAL_PRIORITY_CLASS;** 
Indicates a normal process with no special scheduling needs.

## REALTIME_PRIORITY_CLASS
 **const win32process.REALTIME_PRIORITY_CLASS;** 
Indicates a process that has the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes, including operating system processes performing important tasks. For example, a real-time process that executes for more than a very brief interval can cause disk caches not to flush or cause the mouse to be unresponsive.

## [win32process](README.md#win32process).ResumeThread

int = **ResumeThread( *handle* ** )
Resumes the specified thread. When the suspend count is decremented to zero, the execution of the thread is resumed.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread

#### Return Value
The return value is the thread's previous suspend count

## STARTF_FORCEOFFFEEDBACK
 **const win32process.STARTF_FORCEOFFFEEDBACK;** 
Indicates that the feedback cursor is forced off while the process is starting. The normal cursor is displayed.

## STARTF_FORCEONFEEDBACK
 **const win32process.STARTF_FORCEONFEEDBACK;** 
Indicates that the cursor is in feedback mode for two seconds after CreateProcess is called. If during those two seconds the process makes the first GUI call, the system gives five more seconds to the process. If during those five seconds the process shows a window, the system gives five more seconds to the process to finish drawing the window. 

The system turns the feedback cursor off after the first call to GetMessage, regardless of whether the process is drawing.

## STARTF_RUNFULLSCREEN
 **const win32process.STARTF_RUNFULLSCREEN;** 
Indicates that the process should be run in full-screen mode, rather than in windowed mode. 

This flag is only valid for console applications running on an x86 computer.

## STARTF_USECOUNTCHARS
 **const win32process.STARTF_USECOUNTCHARS;** 
If this value is not specified, the dwXCountChars and dwYCountChars members are ignored.

## STARTF_USEFILLATTRIBUTE
 **const win32process.STARTF_USEFILLATTRIBUTE;** 
If this value is not specified, the dwFillAttribute member is ignored.

## STARTF_USEPOSITION
 **const win32process.STARTF_USEPOSITION;** 
If this value is not specified, the dwX and dwY members are ignored.

## STARTF_USESHOWWINDOW
 **const win32process.STARTF_USESHOWWINDOW;** 
If this value is not specified, the wShowWindow member is ignored.

## STARTF_USESIZE
 **const win32process.STARTF_USESIZE;** 
If this value is not specified, the dwXSize and dwYSize members are ignored.

## STARTF_USESTDHANDLES
 **const win32process.STARTF_USESTDHANDLES;** 
Sets the standard input, standard output, and standard error handles for the process to the handles specified in the hStdInput, hStdOutput, and hStdError members of the STARTUPINFO structure. The CreateProcess function's fInheritHandles parameter must be set to TRUE for this to work properly. 

If this value is not specified, the hStdInput, hStdOutput, and hStdError members of the STARTUPINFO structure are ignored.

## [win32process](README.md#win32process).STARTUPINFO

[PySTARTUPINFO](README.md#pystartupinfo)= **STARTUPINFO(** )
Creates a new STARTUPINFO object.

## [win32process](README.md#win32process).SetPriorityClass

 **SetPriorityClass( *handle*  *, dwPriorityClass* ** )


#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the process

  -  *dwPriorityClass* : int

    priority class value

## [win32process](README.md#win32process).SetProcessAffinityMask

 **SetProcessAffinityMask( *hProcess*  *, mask* ** )
Sets a processor affinity mask for a specified process.

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    handle to the process of interest

  -  *mask* : int

    a processor affinity mask

#### Comments
This function does not exist on all platforms.

## [win32process](README.md#win32process).SetProcessPriorityBoost

 **SetProcessPriorityBoost( *Process*  *, DisablePriorityBoost* ** )
Enables or disables dynamic priority adjustment for a process

#### Parameters


  -  *Process* :[PyHANDLE](README.md#pyhandle)

    Handle to a process

  -  *DisablePriorityBoost* : boolean

    True to disable or False to enable

## [win32process](README.md#win32process).SetProcessShutdownParameters

 **SetProcessShutdownParameters( *Level*  *, Flags* ** )
Sets shutdown priority and flags for current process

#### Parameters


  -  *Level* : int

    Priority, higher means earlier

  -  *Flags* : int

    Currently only SHUTDOWN_NORETRY valid

#### Comments
Ranges are 000-0FF Reserved by windows, 100-1FF Last, 200-2FF Middle, 300-3FF First, 400-4FF Reserved by windows

## [win32process](README.md#win32process).SetProcessWorkingSetSize

 **SetProcessWorkingSetSize( *hProcess*  *, MinimumWorkingSetSize*  *, MaximumWorkingSetSize* ** )
Sets minimum and maximum working set sizes for a process

#### Parameters


  -  *hProcess* :[PyHANDLE](README.md#pyhandle)

    Process handle as returned by OpenProcess

  -  *MinimumWorkingSetSize* : int

    Minimum number of bytes to keep in physical memory

  -  *MaximumWorkingSetSize* : int

    Maximum number of bytes to keep in physical memory

#### Comments
Set both min and max to -1 to have process swapped out completely

## [win32process](README.md#win32process).SetThreadAffinityMask

int = **SetThreadAffinityMask( *hThread*  *, ThreadAffinityMask* ** )
Sets a processor affinity mask for a specified thread.

#### Parameters


  -  *hThread* :[PyHANDLE](README.md#pyhandle)

    handle to the thread of interest

  -  *ThreadAffinityMask* : int

    a processor affinity mask

## [win32process](README.md#win32process).SetThreadIdealProcessor

int = **SetThreadIdealProcessor( *handle*  *, dwIdealProcessor* ** )
Used to specify a preferred processor for a thread. The system schedules threads on their preferred processors whenever possible.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread of interest

  -  *dwIdealProcessor* : int

    ideal processor number

## [win32process](README.md#win32process).SetThreadPriority

 **SetThreadPriority( *handle*  *, nPriority* ** )


#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread

  -  *nPriority* : int

    thread priority level

## [win32process](README.md#win32process).SetThreadPriorityBoost

 **SetThreadPriorityBoost( *Thread*  *, DisablePriorityBoost* ** )
Enables or disables dynamic priority adjustment for a thread

#### Parameters


  -  *Thread* :[PyHANDLE](README.md#pyhandle)

    Handle to a thread

  -  *DisablePriorityBoost* : boolean

    True to disable or False to enable

## [win32process](README.md#win32process).SuspendThread

int = **SuspendThread( *handle* ** )
Suspends the specified thread.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the thread

#### Return Value
The return value is the thread's previous suspend count

## THREAD_MODE_BACKGROUND_BEGIN
 **const win32process.THREAD_MODE_BACKGROUND_BEGIN;** 


## THREAD_MODE_BACKGROUND_BEGIN
 **const win32process.THREAD_MODE_BACKGROUND_BEGIN;** 


## THREAD_MODE_BACKGROUND_END
 **const win32process.THREAD_MODE_BACKGROUND_END;** 


## THREAD_MODE_BACKGROUND_END
 **const win32process.THREAD_MODE_BACKGROUND_END;** 


## THREAD_PRIORITY_ABOVE_NORMAL
 **const win32process.THREAD_PRIORITY_ABOVE_NORMAL;** 
Indicates 1 point above normal priority for the priority class.

## THREAD_PRIORITY_BELOW_NORMAL
 **const win32process.THREAD_PRIORITY_BELOW_NORMAL;** 
Indicates 1 point below normal priority for the priority class.

## THREAD_PRIORITY_HIGHEST
 **const win32process.THREAD_PRIORITY_HIGHEST;** 
Indicates 2 points above normal priority for the priority class.

## THREAD_PRIORITY_IDLE
 **const win32process.THREAD_PRIORITY_IDLE;** 
Indicates a base priority level of 1 for IDLE_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, or HIGH_PRIORITY_CLASS processes, and a base priority level of 16 for REALTIME_PRIORITY_CLASS processes.

## THREAD_PRIORITY_LOWEST
 **const win32process.THREAD_PRIORITY_LOWEST;** 
Indicates 2 points below normal priority for the priority class.

## THREAD_PRIORITY_NORMAL
 **const win32process.THREAD_PRIORITY_NORMAL;** 
Indicates normal priority for the priority class.

## THREAD_PRIORITY_TIME_CRITICAL
 **const win32process.THREAD_PRIORITY_TIME_CRITICAL;** 
Indicates a base priority level of 15 for IDLE_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, or HIGH_PRIORITY_CLASS processes, and a base priority level of 31 for REALTIME_PRIORITY_CLASS processes.

## [win32process](README.md#win32process).TerminateProcess

 **TerminateProcess( *handle*  *, exitCode* ** )
Terminates the specified process and all of its threads.

#### Parameters


  -  *handle* :[PyHANDLE](README.md#pyhandle)

    handle to the process

  -  *exitCode* : int

    The exit code for the process.

## [win32process](README.md#win32process).beginthreadex

[PyHANDLE](README.md#pyhandle), int = **beginthreadex( *sa*  *, stackSize*  *, entryPoint*  *, args*  *, flags* ** )
Creates a new thread

#### Parameters


  -  *sa* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    The security attributes, or None

  -  *stackSize* : int

    Stack size for the new thread, or zero for the default size.

  -  *entryPoint* : function

    The thread function.

  -  *args* : tuple

    Args passed to the function.

  -  *flags* : int

    Can be CREATE_SUSPENDED so thread doesn't run immediately

#### Return Value
The result is a tuple of the thread handle and thread ID.