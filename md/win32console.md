# win32console

## Module win32console

Interface to the Windows Console functions for dealing with character-mode applications

#### Methods


  - [CreateConsoleScreenBuffer](win32console.md#win32consolecreateconsolescreenbuffer)

    Creates a new console handle&nbsp;

  - [GetConsoleDisplayMode](win32console.md#win32consolegetconsoledisplaymode)

    Returns the current console's display mode&nbsp;

  - [AttachConsole](win32console.md#win32consoleattachconsole)

    Attaches calling process to console of another process&nbsp;

  - [AllocConsole](win32console.md#win32consoleallocconsole)

    Creates a new console for the calling process&nbsp;

  - [FreeConsole](win32console.md#win32consolefreeconsole)

    Detaches process from its console&nbsp;

  - [GetConsoleProcessList](win32console.md#win32consolegetconsoleprocesslist)

    Returns pids of all processes attached to current console&nbsp;

  - [GetConsoleCP](win32console.md#win32consolegetconsolecp)

    Returns the input code page for calling process's console&nbsp;

  - [GetConsoleOutputCP](win32console.md#win32consolegetconsoleoutputcp)

    Returns the output code page for calling process's console&nbsp;

  - [SetConsoleCP](win32console.md#win32consolesetconsolecp)

    Sets the input code page for calling process's console&nbsp;

  - [SetConsoleOutputCP](win32console.md#win32consolesetconsoleoutputcp)

    Sets the output code page for calling process's console&nbsp;

  - [GetConsoleSelectionInfo](win32console.md#win32consolegetconsoleselectioninfo)

    Returns info on text selection within the current console&nbsp;

  - [AddConsoleAlias](win32console.md#win32consoleaddconsolealias)

    Creates a new console alias&nbsp;

  - [GetConsoleAliases](win32console.md#win32consolegetconsolealiases)

    Retrieves aliases defined under specified executable&nbsp;

  - [GetConsoleAliasExes](win32console.md#win32consolegetconsolealiasexes)

    Lists all executables that have console aliases defined&nbsp;

  - [GetConsoleWindow](win32console.md#win32consolegetconsolewindow)

    Returns a handle to the console's window, or 0 if none exists&nbsp;

  - [GetNumberOfConsoleFonts](win32console.md#win32consolegetnumberofconsolefonts)

    Returns the number of fonts available to the console&nbsp;

  - [SetConsoleTitle](win32console.md#win32consolesetconsoletitle)

    Sets the title of calling process's console&nbsp;

  - [GetConsoleTitle](win32console.md#win32consolegetconsoletitle)

    Returns the title of console to which calling process is attached&nbsp;

  - [GenerateConsoleCtrlEvent](win32console.md#win32consolegenerateconsolectrlevent)

    Sends a control signal to a group of processes attached to a common console&nbsp;

  - [GetStdHandle](win32console.md#win32consolegetstdhandle)

    Returns one of calling process's standard handles&nbsp;

## [win32console](#win32console).AddConsoleAlias

 __AddConsoleAlias( *Source*  *, Target*  *, ExeName* __ )
Creates a new console alias

#### Parameters


  -  *Source* :[PyUNICODE](#pyunicode)

    The string to be mapped to the target string

  -  *Target* :[PyUNICODE](#pyunicode)

    String to be substituted for Source.  If None, alias is removed

  -  *ExeName* :[PyUNICODE](#pyunicode)

    Name of executable that will use alias

## [win32console](#win32console).AllocConsole

 __AllocConsole(__ )
Creates a new console for the calling process

#### Comments
Calling process must not already be attached to another console

## [win32console](#win32console).AttachConsole

 __AttachConsole( *ProcessId* __ )
Attaches to console of another process

#### Parameters


  -  *ProcessId* : int

    Pid of another process, or ATTACH_PARENT_PROCESS

#### Comments
Calling process must not already be attached to another console

## [win32console](#win32console).CreateConsoleScreenBuffer

[PyConsoleScreenBuffer](#pyconsolescreenbuffer)= __CreateConsoleScreenBuffer( *DesiredAccess*  *, ShareMode*  *, SecurityAttributes*  *, Flags* __ )
Creates a new console screen buffer

#### Parameters


  -  *DesiredAccess=GENERIC_READ and GENERIC_WRITE* : int

    GENERIC_READ and/or GENERIC_WRITE

  -  *ShareMode=FILE_SHARE_READ and FILE_SHARE_WRITE* : int

    FILE_SHARE_READ and/or FILE_SHARE_WRITE

  -  *SecurityAttributes=None* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    Specifies security descriptor and inheritance for handle

  -  *Flags=CONSOLE_TEXTMODE_BUFFER* : int

    CONSOLE_TEXTMODE_BUFFER is currently only valid flag

## [win32console](#win32console).FreeConsole

 __FreeConsole(__ )
Detaches process from its current console

## [win32console](#win32console).GenerateConsoleCtrlEvent

 __GenerateConsoleCtrlEvent( *CtrlEvent*  *, ProcessGroupId* __ )
Sends a control signal to a group of processes attached to a common console

#### Parameters


  -  *CtrlEvent* : int

    Signal to be sent to specified process group - CTRL_C_EVENT or CTRL_BREAK_EVENT

  -  *ProcessGroupId=0* : int

    Pid of a process group, use 0 for calling process

## [win32console](#win32console).GetConsoleAliasExes

[PyUNICODE](#pyunicode)= __GetConsoleAliasExes(__ )
Lists all executables that have console aliases defined

#### Return Value
Returns a unicode string containing executable names separated by NULLS

## [win32console](#win32console).GetConsoleAliases

[PyUNICODE](#pyunicode)= __GetConsoleAliases( *ExeName* __ )
Retrieves aliases defined under specified executable

#### Parameters


  -  *ExeName* :[PyUNICODE](#pyunicode)

    Name of executable for which to return aliases

#### Return Value
Returns a unicode string containing null-terminated pairs of aliases and their target text 

of the form "alias1=replacementtext1\\0alias2=replacementtext2\\0"

## [win32console](#win32console).GetConsoleCP

int = __GetConsoleCP(__ )
Returns the input code page for calling process's console

## [win32console](#win32console).GetConsoleDisplayMode

int = __GetConsoleDisplayMode(__ )
Returns the current console's display mode

#### Comments
Only exists on Wix XP and later

#### Return Value
CONSOLE_FULLSCREEN,CONSOLE_FULLSCREEN_HARDWARE

## [win32console](#win32console).GetConsoleOutputCP

int = __GetConsoleOutputCP(__ )
Returns the output code page for calling process's console

## [win32console](#win32console).GetConsoleProcessList

(int,...) = __GetConsoleProcessList(__ )
Returns pids of all processes attached to current console

## [win32console](#win32console).GetConsoleSelectionInfo

dict = __GetConsoleSelectionInfo(__ )
Returns info on text selection within the current console

#### Return Value
Returns a dictionary containing {Flags:int, SelectionAnchor:[PyCOORD](#pycoord), Selection:[PySMALL_RECT](PySMALL.md#pysmallrect)} 

Flags will contain a combination of 

CONSOLE_NO_SELECTION,CONSOLE_SELECTION_IN_PROGRESS,CONSOLE_SELECTION_NOT_EMPTY,CONSOLE_MOUSE_SELECTION,CONSOLE_MOUSE_DOWN

## [win32console](#win32console).GetConsoleTitle

[PyUNICODE](#pyunicode)= __GetConsoleTitle(__ )
Returns the title of the console window

## [win32console](#win32console).GetConsoleWindow

int = __GetConsoleWindow(__ )
Returns a handle to the console's window, or 0 if none exists

#### Return Value
This function may raise NotImplementedError if it does not exist on 

the platform, or a[PyHANDLE](#pyhandle)object with a value of 0.  It will never 

raise a win32 exception.

## [win32console](#win32console).GetNumberOfConsoleFonts

int = __GetNumberOfConsoleFonts(__ )
Returns the number of fonts available to the console

#### Comments
Function is not documented in MSDN

## [win32console](#win32console).GetStdHandle

[PyConsoleScreenBuffer](#pyconsolescreenbuffer)= __GetStdHandle( *StdHandle* __ )
Returns one of calling process's standard handles

#### Parameters


  -  *StdHandle* : int

    Specifies the handle to return - STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE

#### Return Value
Returns a[PyConsoleScreenBuffer](#pyconsolescreenbuffer)wrapping the handle, or None if specified handle does not exist

## [win32console](#win32console).SetConsoleCP

 __SetConsoleCP( *CodePageId* __ )
Sets the input code page for calling process's console

#### Parameters


  -  *CodePageId* : int

    The code page to set

## [win32console](#win32console).SetConsoleOutputCP

 __SetConsoleOutputCP( *CodePageID* __ )
Sets the output code page for calling process's console

#### Parameters


  -  *CodePageID* : int

    The code page to set

## [win32console](#win32console).SetConsoleTitle

 __SetConsoleTitle( *ConsoleTitle* __ )
Sets the title of the console window

#### Parameters


  -  *ConsoleTitle* :[PyUNICODE](#pyunicode)

    New title for the console