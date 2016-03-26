# PyConsoleScreenBuffer


## PyConsoleScreenBuffer Object

Handle to a console screen buffer 

Create using [win32console::CreateConsoleScreenBuffer](win32console.md#win32consolecreateconsolescreenbuffer) or [win32console::GetStdHandle](win32console.md#win32consolegetstdhandle) 

Use PyConsoleScreenBufferType\(Handle\) to wrap a pre-existing handle as returned by [win32api::GetStdHandle](win32api.md#win32apigetstdhandle)\. 

Will also accept a handle created by [win32file::CreateFile](win32file.md#win32filecreatefile) for CONIN$ or CONOUT$\. 

When an existing handle is wrapped, a copy is made using DuplicateHandle, and caller is still responsible 

for any cleanup of original handle\.

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


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.FillConsoleOutputAttribute

int = FillConsoleOutputAttribute\(Attribute, Length

, WriteCoord

\)
Set text attributes for a consecutive series of characters

#### Parameters

  - Attribute : int

    Text attributes to be set, combination of FOREGROUND\_\*, BACKGROUND\_\*, and COMMON\_LVB\_\* constants

  - Length : int

    The number of characters to set

  - WriteCoord : [PyCOORD](PyCOORD.md)

    The screen position to begin at

#### Return Value
Returns the number of character cells whose attributes were set


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.FillConsoleOutputCharacter

int = FillConsoleOutputCharacter\(Character, Length

, WriteCoord

\)
Sets consecutive character positions to a specified character

#### Parameters

  - Character : [PyUNICODE](PyUNICODE.md)

    A single character to be used to fill the specified range

  - Length : int

    The number of characters positions to fill

  - WriteCoord : [PyCOORD](PyCOORD.md)

    The screen position to begin at

#### Return Value
Returns the number of characters actually written


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.FlushConsoleInputBuffer

FlushConsoleInputBuffer\(\)
Flush input buffer


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetConsoleCursorInfo

\(Size, bVisible\) = GetConsoleCursorInfo\(\)
Retrieves size and visibility of console's cursor

#### Return Value
Returns the size of the console's cursor expressed as a percentage of character size, and a boolen indicating if cursor is visible


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetConsoleFontSize

[PyCOORD](PyCOORD.md) = GetConsoleFontSize\(Font\)
Returns size of specified font for the console

#### Parameters

  - Font : int

    Index of font as returned by GetCurrentConsoleFont

#### Comments

Only exists on XP or later\.


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetConsoleMode

int = GetConsoleMode\(\)
Returns the input or output mode of the console buffer

#### Return Value
Returns a combination of ENABLE\_\*\_INPUT or ENABLE\_\*\_OUTPUT constants


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetConsoleScreenBufferInfo

dict = GetConsoleScreenBufferInfo\(\)
Returns the state of the screen buffer


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetCurrentConsoleFont

\(int, [PyCOORD](PyCOORD.md)\) = GetCurrentConsoleFont\(MaximumWindow\)
Returns currently displayed font

#### Parameters

  - MaximumWindow=False : boolean

    If True, retrieves font size for maximum window size

#### Comments

Only exists on XP or later\.
 

MSDN docs claim the returned COORD is the font size, but it's actually the window size\.
 

Use [PyConsoleScreenBuffer::GetConsoleFontSize](PyConsoleScreenBuffer.md#pyconsolescreenbuffergetconsolefontsize) for the font size\.

#### Return Value
Returns the index of current font and window size


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetLargestConsoleWindowSize

[PyCOORD](PyCOORD.md) = GetLargestConsoleWindowSize\(\)
Returns the largest possible size for the console's window


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.GetNumberOfConsoleInputEvents

int = GetNumberOfConsoleInputEvents\(\)
Returns the number of unread records in the input queue


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.PeekConsoleInput

\([PyINPUT\_RECORD](PyINPUT.md#pyinputrecord),\.\.\.\) = PeekConsoleInput\(Length\)
Returns pending input records without removing them from the input queue

#### Parameters

  - Length : int

    The number of input records to read

#### Comments

This function does not block as ReadConsoleInput does\.
 

The number of records returned may be less than the nbr requested

#### Return Value
Returns a sequence of [PyINPUT\_RECORD](PyINPUT.md#pyinputrecord) objects


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.ReadConsole

[PyUNICODE](PyUNICODE.md) = ReadConsole\(NumberOfCharsToRead\)
Reads characters from the console input buffer

#### Parameters

  - NumberOfCharsToRead : int

    Characters to read


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.ReadConsoleInput

\([PyINPUT\_RECORD](PyINPUT.md#pyinputrecord),\.\.\.\) = ReadConsoleInput\(Length\)
Reads input records and removes them from the input queue

#### Parameters

  - Length : int

    The number of input records to read

#### Comments

This functions blocks until at least one record is read\.
 

The number of records returned may be less than the nbr requested

#### Return Value
Returns a sequence of [PyINPUT\_RECORD](PyINPUT.md#pyinputrecord) objects


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.ReadConsoleOutputAttribute

\(int,\.\.\.\) = ReadConsoleOutputAttribute\(Length, ReadCoord

\)
Retrieves attributes from consecutive character cells

#### Parameters

  - Length : int

    The number of attributes to read

  - ReadCoord : [PyCOORD](PyCOORD.md)

    The screen position from which to start reading

#### Return Value
Returns a sequence of ints containing the attributes of a range of characters


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.ReadConsoleOutputCharacter

[PyUnicode](PyUnicode.md) = ReadConsoleOutputCharacter\(Length, ReadCoord

\)
Reads consecutive characters from a starting position

#### Parameters

  - Length : int

    The number of characters positions to read

  - ReadCoord : [PyCOORD](PyCOORD.md)

    The screen position start reading from


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.ScrollConsoleScreenBuffer

ScrollConsoleScreenBuffer\(ScrollRectangle, ClipRectangle, DestinationOrigin, FillCharacter, FillAttribute\)
Scrolls a region of the display

#### Parameters

  - ScrollRectangle : [PySMALL\_RECT](PySMALL.md#pysmallrect)

    The region to be scrolled

  - ClipRectangle : [PySMALL\_RECT](PySMALL.md#pysmallrect)

    Rectangle that limits display area affected, can be None

  - DestinationOrigin : [PyCOORD](PyCOORD.md)

    The position to which ScrollRectangle will be moved

  - FillCharacter : [PyUNICODE](PyUNICODE.md)

    Character to fill in the area left blank by scrolling operation

  - FillAttribute : int

    Text attributes to apply to FillCharacter


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleActiveScreenBuffer

SetConsoleActiveScreenBuffer\(\)
Sets this handle as the currently displayed screen buffer


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleCursorInfo

SetConsoleCursorInfo\(Size, Visible\)
Sets the size and visibility of console's cursor

#### Parameters

  - Size : int

    Percentage of character size that cursor will occupy

  - Visible : boolen

    Determines if cursor is visible


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleCursorPosition

SetConsoleCursorPosition\(CursorPosition\)
Sets the console screen buffer's cursor position

#### Parameters

  - CursorPosition : [PyCOORD](PyCOORD.md)

    A PyCOORD containing the new cursor position


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleDisplayMode

SetConsoleDisplayMode\(Flags, NewScreenBufferDimensions\)
Sets the display mode of the console buffer

#### Parameters

  - Flags : int

    CONSOLE\_FULLSCREEN\_MODE or CONSOLE\_WINDOWED\_MODE

  - NewScreenBufferDimensions : [PyCOORD](PyCOORD.md)

    New size of the screen buffer in characters


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleFont

SetConsoleFont\(Font\)
Changes the font used by the screen buffer

#### Parameters

  - Font : int

    The number of the font to be set

#### Comments

Function is not documented on MSDN


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleMode

SetConsoleMode\(Mode\)
Sets the input or output mode of the console buffer

#### Parameters

  - Mode : int

    Combination of ENABLE\_\*\_INPUT or ENABLE\_\*\_OUTPUT constants


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleScreenBufferSize

SetConsoleScreenBufferSize\(Size\)
Sets the size of the console screen buffer

#### Parameters

  - Size : [PyCOORD](PyCOORD.md)

    COORD object containing the new dimensions


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleTextAttribute

SetConsoleTextAttribute\(Attributes\)
Sets character attributes for subsequent write operations

#### Parameters

  - Attributes : int

    Attributes to be set, combination of FOREGROUND\_\*, BACKGROUND\_\*, and COMMON\_LVB\_\* constants


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetConsoleWindowInfo

SetConsoleWindowInfo\(Absolute, ConsoleWindow\)
Changes size and position of a console's window

#### Parameters

  - Absolute : boolean

    If False, coordinates are relative to current position

  - ConsoleWindow : [PySMALL\_RECT](PySMALL.md#pysmallrect)

    A SMALL\_RECT containing the new window coordinates


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.SetStdHandle

SetStdHandle\(StdHandle\)
Replaces one of calling process's standard handles with this handle

#### Parameters

  - StdHandle : int

    Specifies handle to be replaced - STD\_INPUT\_HANDLE, STD\_OUTPUT\_HANDLE, or STD\_ERROR\_HANDLE


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.WriteConsole

int = WriteConsole\(Buffer\)
Writes characters at current cursor position

#### Parameters

  - Buffer : [PyUNICODE](PyUNICODE.md)

    String or Unicode to be written to console

#### Return Value
Returns the number of characters written


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.WriteConsoleInput

int = WriteConsoleInput\(Buffer\)
Places input records in the console's input queue

#### Parameters

  - Buffer : \([PyINPUT\_RECORD](PyINPUT.md#pyinputrecord),\.\.\.\)

    A sequence of [PyINPUT\_RECORD](PyINPUT.md#pyinputrecord) objects

#### Return Value
Returns the number of records written


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.WriteConsoleOutputAttribute

int = WriteConsoleOutputAttribute\(Attributes, WriteCoord

\)
Sets the attributes of a range of character cells

#### Parameters

  - Attributes : \(int,\.\.\.\)

    A sequence of ints containing the attributes to be set

  - WriteCoord : [PyCOORD](PyCOORD.md)

    The screen position at which to start writing

#### Return Value
Returns the number of attributes set


## [PyConsoleScreenBuffer](PyConsoleScreenBuffer.md#pyconsolescreenbuffer)\.WriteConsoleOutputCharacter

int = WriteConsoleOutputCharacter\(Characters, WriteCoord

\)
Writes a string of characters at a specified position

#### Parameters

  - Characters : [PyUNICODE](PyUNICODE.md)

    Characters to be written

  - WriteCoord : [PyCOORD](PyCOORD.md)

    The screen position at which to start writing

#### Return Value
Returns the number of characters actually written