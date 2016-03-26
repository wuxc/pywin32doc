# NT


## NT\_CONSOLE\_PROPS Object

Dictionary containing information for a NT\_CONSOLE\_PROPS struct

#### Properties

  - int Signature

    The type of data block, one of shellcon\.\*\_SIG values

  - int FillAttribute

    Character attributes for fill operations

  - int PopupFillAttribute

    Fill attributes for popups

  - \(int,int\) ScreenBufferSize

    Size of console screen buffer, in character cells

  - \(int,int\) WindowSize

    Size of console window in character cells

  - \(int,int\) WindowOrigin

    Window position, in screen coordinates

  - int nFont

    Number of font to be displayed\.  See [win32console::GetNumberOfConsoleFonts](win32console.md#win32consolegetnumberofconsolefonts)

  - int InputBufferSize

    Size of console's input buffer

  - \(int,int\) FontSize

    Size of font

  - int FontFamily

    Font family

  - int FontWeight

    Controls thickness of displayed font

  - str FaceName

    Name of font face, 31 characters at most

  - int CursorSize

    Relative size of cursor, expressed as percent of character size

  - bool FullScreen

    Causes console to run in full screen mode

  - bool QuickEdit

    

  - bool InsertMode

    

  - bool AutoPosition

    Lets system determine window placement

  - int HistoryBufferSize

    Size of command line history buffer

  - int NumberOfHistoryBuffers

    

  - bool HistoryNoDup

    

  - tuple ColorTable

    Tuple of 16 ints containing console's color attributes

  - int Size

    Size of structure, ignored on input


## NT\_FE\_CONSOLE\_PROPS Object

Dictionary containing information for a NT\_FE\_CONSOLE\_PROPS struct

#### Properties

  - int Signature

    The type of data block, one of shellcon\.\*\_SIG values

  - int CodePage

    The codepage to be used for console text

  - int Size

    Size of structure, ignored on input