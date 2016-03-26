
## [win32console](#README.md#win32console).AddConsoleAlias

 **AddConsoleAlias( *Source*  *, Target*  *, ExeName* ** )
Creates a new console alias

#### Parameters


     *Source* :[PyUNICODE](#README.md#PyUNICODE)

    The string to be mapped to the target string

     *Target* :[PyUNICODE](#README.md#PyUNICODE)

    String to be substituted for Source.  If None, alias is removed

     *ExeName* :[PyUNICODE](#README.md#PyUNICODE)

    Name of executable that will use alias

## [win32console](#README.md#win32console).AllocConsole

 **AllocConsole(** )
Creates a new console for the calling process

#### Comments
Calling process must not already be attached to another console

## [win32console](#README.md#win32console).AttachConsole

 **AttachConsole( *ProcessId* ** )
Attaches to console of another process

#### Parameters


     *ProcessId* : int

    Pid of another process, or ATTACH_PARENT_PROCESS

#### Comments
Calling process must not already be attached to another console

## [win32console](#README.md#win32console).CreateConsoleScreenBuffer

[PyConsoleScreenBuffer](#README.md#PyConsoleScreenBuffer)= **CreateConsoleScreenBuffer( *DesiredAccess*  *, ShareMode*  *, SecurityAttributes*  *, Flags* ** )
Creates a new console screen buffer

#### Parameters


     *DesiredAccess=GENERIC_READ and GENERIC_WRITE* : int

    GENERIC_READ and/or GENERIC_WRITE

     *ShareMode=FILE_SHARE_READ and FILE_SHARE_WRITE* : int

    FILE_SHARE_READ and/or FILE_SHARE_WRITE

     *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    Specifies security descriptor and inheritance for handle

     *Flags=CONSOLE_TEXTMODE_BUFFER* : int

    CONSOLE_TEXTMODE_BUFFER is currently only valid flag

## [win32console](#README.md#win32console).FreeConsole

 **FreeConsole(** )
Detaches process from its current console

## [win32console](#README.md#win32console).GenerateConsoleCtrlEvent

 **GenerateConsoleCtrlEvent( *CtrlEvent*  *, ProcessGroupId* ** )
Sends a control signal to a group of processes attached to a common console

#### Parameters


     *CtrlEvent* : int

    Signal to be sent to specified process group - CTRL_C_EVENT or CTRL_BREAK_EVENT

     *ProcessGroupId=0* : int

    Pid of a process group, use 0 for calling process

## [win32console](#README.md#win32console).GetConsoleAliasExes

[PyUNICODE](#README.md#PyUNICODE)= **GetConsoleAliasExes(** )
Lists all executables that have console aliases defined

#### Return Value
Returns a unicode string containing executable names separated by NULLS

## [win32console](#README.md#win32console).GetConsoleAliases

[PyUNICODE](#README.md#PyUNICODE)= **GetConsoleAliases( *ExeName* ** )
Retrieves aliases defined under specified executable

#### Parameters


     *ExeName* :[PyUNICODE](#README.md#PyUNICODE)

    Name of executable for which to return aliases

#### Return Value
Returns a unicode string containing null-terminated pairs of aliases and their target text 

of the form "alias1=replacementtext1\\0alias2=replacementtext2\\0"

## [win32console](#README.md#win32console).GetConsoleCP

int = **GetConsoleCP(** )
Returns the input code page for calling process's console

## [win32console](#README.md#win32console).GetConsoleDisplayMode

int = **GetConsoleDisplayMode(** )
Returns the current console's display mode

#### Comments
Only exists on Wix XP and later

#### Return Value
CONSOLE_FULLSCREEN,CONSOLE_FULLSCREEN_HARDWARE

## [win32console](#README.md#win32console).GetConsoleOutputCP

int = **GetConsoleOutputCP(** )
Returns the output code page for calling process's console

## [win32console](#README.md#win32console).GetConsoleProcessList

(int,...) = **GetConsoleProcessList(** )
Returns pids of all processes attached to current console

## [win32console](#README.md#win32console).GetConsoleSelectionInfo

dict = **GetConsoleSelectionInfo(** )
Returns info on text selection within the current console

#### Return Value
Returns a dictionary containing {Flags:int, SelectionAnchor:[PyCOORD](#README.md#PyCOORD), Selection:[PySMALL_RECT](#PySMALL.md#PySMALLRECT)} 

Flags will contain a combination of 

CONSOLE_NO_SELECTION,CONSOLE_SELECTION_IN_PROGRESS,CONSOLE_SELECTION_NOT_EMPTY,CONSOLE_MOUSE_SELECTION,CONSOLE_MOUSE_DOWN

## [win32console](#README.md#win32console).GetConsoleTitle

[PyUNICODE](#README.md#PyUNICODE)= **GetConsoleTitle(** )
Returns the title of the console window

## [win32console](#README.md#win32console).GetConsoleWindow

int = **GetConsoleWindow(** )
Returns a handle to the console's window, or 0 if none exists

#### Return Value
This function may raise NotImplementedError if it does not exist on 

the platform, or a[PyHANDLE](#README.md#PyHANDLE)object with a value of 0.  It will never 

raise a win32 exception.

## [win32console](#README.md#win32console).GetNumberOfConsoleFonts

int = **GetNumberOfConsoleFonts(** )
Returns the number of fonts available to the console

#### Comments
Function is not documented in MSDN

## [win32console](#README.md#win32console).GetStdHandle

[PyConsoleScreenBuffer](#README.md#PyConsoleScreenBuffer)= **GetStdHandle( *StdHandle* ** )
Returns one of calling process's standard handles

#### Parameters


     *StdHandle* : int

    Specifies the handle to return - STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE

#### Return Value
Returns a[PyConsoleScreenBuffer](#README.md#PyConsoleScreenBuffer)wrapping the handle, or None if specified handle does not exist

## [win32console](#README.md#win32console).SetConsoleCP

 **SetConsoleCP( *CodePageId* ** )
Sets the input code page for calling process's console

#### Parameters


     *CodePageId* : int

    The code page to set

## [win32console](#README.md#win32console).SetConsoleOutputCP

 **SetConsoleOutputCP( *CodePageID* ** )
Sets the output code page for calling process's console

#### Parameters


     *CodePageID* : int

    The code page to set

## [win32console](#README.md#win32console).SetConsoleTitle

 **SetConsoleTitle( *ConsoleTitle* ** )
Sets the title of the console window

#### Parameters


     *ConsoleTitle* :[PyUNICODE](#README.md#PyUNICODE)

    New title for the console