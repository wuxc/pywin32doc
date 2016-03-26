# PyConsoleScreenBuffer

## PyConsoleScreenBuffer Object

Handle to a console screen buffer 

Create using[win32console::CreateConsoleScreenBuffer](win32console.md#win32consolecreateconsolescreenbuffer)or[win32console::GetStdHandle](win32console.md#win32consolegetstdhandle)Use PyConsoleScreenBufferType(Handle) to wrap a pre-existing handle as returned by[win32api::GetStdHandle](win32api.md#win32apigetstdhandle). 

Will also accept a handle created by[win32file::CreateFile](win32file.md#win32filecreatefile)for CONIN$ or CONOUT$. 

When an existing handle is wrapped, a copy is made using DuplicateHandle, and caller is still responsible 

for any cleanup of original handle.

#### Methods


  - [Detach](PyConsoleScreenBuffer.md#pyconsolescreenbufferdetach)

    Releases reference to handle without closing it&nbsp;

  - [Close](PyConsoleScreenBuffer.md#pyconsolescreenbufferclose)

    Closes the handle&nbsp;

  - [SetConsoleActiveScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsoleactivescreenbuffer)

    Sets this handle as the currently display screen buffer&nbsp;

  - [GetConsoleCursorInfo](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetconsolecursorinfo)

    Retrieves size and visibility of console's cursor&nbsp;

  - [SetConsoleCursorInfo](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsolecursorinfo)

    Sets the size and visibility of console's cursor&nbsp;

  - [GetConsoleMode](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetconsolemode)

    Returns the input or output mode of the console buffer&nbsp;

  - [SetConsoleMode](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsolemode)

    Sets the input or output mode of the console buffer&nbsp;

  - [ReadConsole](PyConsoleScreenBuffer.md#pyconsolescreenbufferreadconsole)

    Reads characters from the console input buffer&nbsp;

  - [WriteConsole](PyConsoleScreenBuffer.md#pyconsolescreenbufferwriteconsole)

    Writes characters at current cursor position&nbsp;

  - [FlushConsoleInputBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbufferflushconsoleinputbuffer)

    Flush input buffer for console&nbsp;

  - [SetConsoleTextAttribute](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsoletextattribute)

    Sets character attributes for subsequent write operations&nbsp;

  - [SetConsoleCursorPosition](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsolecursorposition)

    Sets the console screen buffer's cursor position&nbsp;

  - [SetConsoleScreenBufferSize](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsolescreenbuffersize)

    Sets the size of the console screen buffer&nbsp;

  - [SetConsoleWindowInfo](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsolewindowinfo)

    Changes size and position of a console's window&nbsp;

  - [GetConsoleScreenBufferInfo](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetconsolescreenbufferinfo)

    Returns the state of the screen buffer&nbsp;

  - [GetLargestConsoleWindowSize](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetlargestconsolewindowsize)

    Returns the largest possible size for the console's window&nbsp;

  - [FillConsoleOutputAttribute](PyConsoleScreenBuffer.md#pyconsolescreenbufferfillconsoleoutputattribute)

    Set text attributes for a consecutive series of characters&nbsp;

  - [FillConsoleOutputCharacter](PyConsoleScreenBuffer.md#pyconsolescreenbufferfillconsoleoutputcharacter)

    Sets consecutive character positions to a specified character&nbsp;

  - [ReadConsoleOutputCharacter](PyConsoleScreenBuffer.md#pyconsolescreenbufferreadconsoleoutputcharacter)

    Reads consecutive characters from a starting position&nbsp;

  - [ReadConsoleOutputAttribute](PyConsoleScreenBuffer.md#pyconsolescreenbufferreadconsoleoutputattribute)

    Retrieves attributes from consecutive character cells&nbsp;

  - [WriteConsoleOutputCharacter](PyConsoleScreenBuffer.md#pyconsolescreenbufferwriteconsoleoutputcharacter)

    Writes a string of characters at a specified position&nbsp;

  - [WriteConsoleOutputAttribute](PyConsoleScreenBuffer.md#pyconsolescreenbufferwriteconsoleoutputattribute)

    Sets the attributes of a range of character cells&nbsp;

  - [ScrollConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbufferscrollconsolescreenbuffer)

    Scrolls a region of the display&nbsp;

  - [GetCurrentConsoleFont](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetcurrentconsolefont)

    Returns the currently displayed font&nbsp;

  - [GetConsoleFontSize](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetconsolefontsize)

    Returns size of specified font for the console&nbsp;

  - [SetConsoleFont](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsolefont)

    Changes the font used by the screen buffer&nbsp;

  - [SetStdHandle](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetstdhandle)

    Replaces one of calling process's standard handles with this handle&nbsp;

  - [SetConsoleDisplayMode](PyConsoleScreenBuffer.md#pyconsolescreenbuffersetconsoledisplaymode)

    Sets the display mode of the console buffer&nbsp;

  - [WriteConsoleInput](PyConsoleScreenBuffer.md#pyconsolescreenbufferwriteconsoleinput)

    Places input records in the console's input queue&nbsp;

  - [ReadConsoleInput](PyConsoleScreenBuffer.md#pyconsolescreenbufferreadconsoleinput)

    Reads input records and removes them from the input queue&nbsp;

  - [PeekConsoleInput](PyConsoleScreenBuffer.md#pyconsolescreenbufferpeekconsoleinput)

    Returns pending input records without removing them from the input queue&nbsp;

  - [GetNumberOfConsoleInputEvents](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetnumberofconsoleinputevents)

    Returns the number of unread records in the input queue&nbsp;

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).FillConsoleOutputAttribute

int = __FillConsoleOutputAttribute( *Attribute*  *, Length*  *, WriteCoord* __ )
Set text attributes for a consecutive series of characters

#### Parameters


  -  *Attribute* : int

    Text attributes to be set, combination of FOREGROUND_*, BACKGROUND_*, and COMMON_LVB_* constants

  -  *Length* : int

    The number of characters to set

  -  *WriteCoord* :[PyCOORD](#pycoord)

    The screen position to begin at

#### Return Value
Returns the number of character cells whose attributes were set

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).FillConsoleOutputCharacter

int = __FillConsoleOutputCharacter( *Character*  *, Length*  *, WriteCoord* __ )
Sets consecutive character positions to a specified character

#### Parameters


  -  *Character* :[PyUNICODE](#pyunicode)

    A single character to be used to fill the specified range

  -  *Length* : int

    The number of characters positions to fill

  -  *WriteCoord* :[PyCOORD](#pycoord)

    The screen position to begin at

#### Return Value
Returns the number of characters actually written

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).FlushConsoleInputBuffer

 __FlushConsoleInputBuffer(__ )
Flush input buffer

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetConsoleCursorInfo

(Size, bVisible) = __GetConsoleCursorInfo(__ )
Retrieves size and visibility of console's cursor

#### Return Value
Returns the size of the console's cursor expressed as a percentage of character size, and a boolen indicating if cursor is visible

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetConsoleFontSize

[PyCOORD](#pycoord)= __GetConsoleFontSize( *Font* __ )
Returns size of specified font for the console

#### Parameters


  -  *Font* : int

    Index of font as returned by GetCurrentConsoleFont

#### Comments
Only exists on XP or later.

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetConsoleMode

int = __GetConsoleMode(__ )
Returns the input or output mode of the console buffer

#### Return Value
Returns a combination of ENABLE_*_INPUT or ENABLE_*_OUTPUT constants

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetConsoleScreenBufferInfo

dict = __GetConsoleScreenBufferInfo(__ )
Returns the state of the screen buffer

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetCurrentConsoleFont

(int,[PyCOORD](#pycoord)) = __GetCurrentConsoleFont( *MaximumWindow* __ )
Returns currently displayed font

#### Parameters


  -  *MaximumWindow=False* : boolean

    If True, retrieves font size for maximum window size

#### Comments
Only exists on XP or later.
MSDN docs claim the returned COORD is the font size, but it's actually the window size.
Use[PyConsoleScreenBuffer::GetConsoleFontSize](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetconsolefontsize)for the font size.

#### Return Value
Returns the index of current font and window size

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetLargestConsoleWindowSize

[PyCOORD](#pycoord)= __GetLargestConsoleWindowSize(__ )
Returns the largest possible size for the console's window

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).GetNumberOfConsoleInputEvents

int = __GetNumberOfConsoleInputEvents(__ )
Returns the number of unread records in the input queue

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).PeekConsoleInput

([PyINPUT_RECORD](PyINPUT.md#pyinputrecord),...) = __PeekConsoleInput( *Length* __ )
Returns pending input records without removing them from the input queue

#### Parameters


  -  *Length* : int

    The number of input records to read

#### Comments
This function does not block as ReadConsoleInput does.
The number of records returned may be less than the nbr requested

#### Return Value
Returns a sequence of[PyINPUT_RECORD](PyINPUT.md#pyinputrecord)objects

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).ReadConsole

[PyUNICODE](#pyunicode)= __ReadConsole( *NumberOfCharsToRead* __ )
Reads characters from the console input buffer

#### Parameters


  -  *NumberOfCharsToRead* : int

    Characters to read

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).ReadConsoleInput

([PyINPUT_RECORD](PyINPUT.md#pyinputrecord),...) = __ReadConsoleInput( *Length* __ )
Reads input records and removes them from the input queue

#### Parameters


  -  *Length* : int

    The number of input records to read

#### Comments
This functions blocks until at least one record is read.
The number of records returned may be less than the nbr requested

#### Return Value
Returns a sequence of[PyINPUT_RECORD](PyINPUT.md#pyinputrecord)objects

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).ReadConsoleOutputAttribute

(int,...) = __ReadConsoleOutputAttribute( *Length*  *, ReadCoord* __ )
Retrieves attributes from consecutive character cells

#### Parameters


  -  *Length* : int

    The number of attributes to read

  -  *ReadCoord* :[PyCOORD](#pycoord)

    The screen position from which to start reading

#### Return Value
Returns a sequence of ints containing the attributes of a range of characters

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).ReadConsoleOutputCharacter

[PyUnicode](#pyunicode)= __ReadConsoleOutputCharacter( *Length*  *, ReadCoord* __ )
Reads consecutive characters from a starting position

#### Parameters


  -  *Length* : int

    The number of characters positions to read

  -  *ReadCoord* :[PyCOORD](#pycoord)

    The screen position start reading from

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).ScrollConsoleScreenBuffer

 __ScrollConsoleScreenBuffer( *ScrollRectangle*  *, ClipRectangle*  *, DestinationOrigin*  *, FillCharacter*  *, FillAttribute* __ )
Scrolls a region of the display

#### Parameters


  -  *ScrollRectangle* :[PySMALL_RECT](PySMALL.md#pysmallrect)

    The region to be scrolled

  -  *ClipRectangle* :[PySMALL_RECT](PySMALL.md#pysmallrect)

    Rectangle that limits display area affected, can be None

  -  *DestinationOrigin* :[PyCOORD](#pycoord)

    The position to which ScrollRectangle will be moved

  -  *FillCharacter* :[PyUNICODE](#pyunicode)

    Character to fill in the area left blank by scrolling operation

  -  *FillAttribute* : int

    Text attributes to apply to FillCharacter

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleActiveScreenBuffer

 __SetConsoleActiveScreenBuffer(__ )
Sets this handle as the currently displayed screen buffer

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleCursorInfo

 __SetConsoleCursorInfo( *Size*  *, Visible* __ )
Sets the size and visibility of console's cursor

#### Parameters


  -  *Size* : int

    Percentage of character size that cursor will occupy

  -  *Visible* : boolen

    Determines if cursor is visible

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleCursorPosition

 __SetConsoleCursorPosition( *CursorPosition* __ )
Sets the console screen buffer's cursor position

#### Parameters


  -  *CursorPosition* :[PyCOORD](#pycoord)

    A PyCOORD containing the new cursor position

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleDisplayMode

 __SetConsoleDisplayMode( *Flags*  *, NewScreenBufferDimensions* __ )
Sets the display mode of the console buffer

#### Parameters


  -  *Flags* : int

    CONSOLE_FULLSCREEN_MODE or CONSOLE_WINDOWED_MODE

  -  *NewScreenBufferDimensions* :[PyCOORD](#pycoord)

    New size of the screen buffer in characters

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleFont

 __SetConsoleFont( *Font* __ )
Changes the font used by the screen buffer

#### Parameters


  -  *Font* : int

    The number of the font to be set

#### Comments
Function is not documented on MSDN

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleMode

 __SetConsoleMode( *Mode* __ )
Sets the input or output mode of the console buffer

#### Parameters


  -  *Mode* : int

    Combination of ENABLE_*_INPUT or ENABLE_*_OUTPUT constants

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleScreenBufferSize

 __SetConsoleScreenBufferSize( *Size* __ )
Sets the size of the console screen buffer

#### Parameters


  -  *Size* :[PyCOORD](#pycoord)

    COORD object containing the new dimensions

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleTextAttribute

 __SetConsoleTextAttribute( *Attributes* __ )
Sets character attributes for subsequent write operations

#### Parameters


  -  *Attributes* : int

    Attributes to be set, combination of FOREGROUND_*, BACKGROUND_*, and COMMON_LVB_* constants

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetConsoleWindowInfo

 __SetConsoleWindowInfo( *Absolute*  *, ConsoleWindow* __ )
Changes size and position of a console's window

#### Parameters


  -  *Absolute* : boolean

    If False, coordinates are relative to current position

  -  *ConsoleWindow* :[PySMALL_RECT](PySMALL.md#pysmallrect)

    A SMALL_RECT containing the new window coordinates

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).SetStdHandle

 __SetStdHandle( *StdHandle* __ )
Replaces one of calling process's standard handles with this handle

#### Parameters


  -  *StdHandle* : int

    Specifies handle to be replaced - STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLE

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).WriteConsole

int = __WriteConsole( *Buffer* __ )
Writes characters at current cursor position

#### Parameters


  -  *Buffer* :[PyUNICODE](#pyunicode)

    String or Unicode to be written to console

#### Return Value
Returns the number of characters written

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).WriteConsoleInput

int = __WriteConsoleInput( *Buffer* __ )
Places input records in the console's input queue

#### Parameters


  -  *Buffer* : ([PyINPUT_RECORD](PyINPUT.md#pyinputrecord),...)

    A sequence of[PyINPUT_RECORD](PyINPUT.md#pyinputrecord)objects

#### Return Value
Returns the number of records written

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).WriteConsoleOutputAttribute

int = __WriteConsoleOutputAttribute( *Attributes*  *, WriteCoord* __ )
Sets the attributes of a range of character cells

#### Parameters


  -  *Attributes* : (int,...)

    A sequence of ints containing the attributes to be set

  -  *WriteCoord* :[PyCOORD](#pycoord)

    The screen position at which to start writing

#### Return Value
Returns the number of attributes set

## [PyConsoleScreenBuffer](#pyconsolescreenbuffer).WriteConsoleOutputCharacter

int = __WriteConsoleOutputCharacter( *Characters*  *, WriteCoord* __ )
Writes a string of characters at a specified position

#### Parameters


  -  *Characters* :[PyUNICODE](#pyunicode)

    Characters to be written

  -  *WriteCoord* :[PyCOORD](#pycoord)

    The screen position at which to start writing

#### Return Value
Returns the number of characters actually written