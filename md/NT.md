# NT

## NT_CONSOLE_PROPS Object

Dictionary containing information for a NT_CONSOLE_PROPS struct

#### Properties

  -  __int Signature__ 
    The type of data block, one of shellcon.*_SIG values

  -  __int FillAttribute__ 
    Character attributes for fill operations

  -  __int PopupFillAttribute__ 
    Fill attributes for popups

  -  __(int,int) ScreenBufferSize__ 
    Size of console screen buffer, in character cells

  -  __(int,int) WindowSize__ 
    Size of console window in character cells

  -  __(int,int) WindowOrigin__ 
    Window position, in screen coordinates

  -  __int nFont__ 
    Number of font to be displayed.  See[win32console::GetNumberOfConsoleFonts](win32console.md#win32consolegetnumberofconsolefonts)

  -  __int InputBufferSize__ 
    Size of console's input buffer

  -  __(int,int) FontSize__ 
    Size of font

  -  __int FontFamily__ 
    Font family

  -  __int FontWeight__ 
    Controls thickness of displayed font

  -  __str FaceName__ 
    Name of font face, 31 characters at most

  -  __int CursorSize__ 
    Relative size of cursor, expressed as percent of character size

  -  __bool FullScreen__ 
    Causes console to run in full screen mode

  -  __bool QuickEdit__ 
    

  -  __bool InsertMode__ 
    

  -  __bool AutoPosition__ 
    Lets system determine window placement

  -  __int HistoryBufferSize__ 
    Size of command line history buffer

  -  __int NumberOfHistoryBuffers__ 
    

  -  __bool HistoryNoDup__ 
    

  -  __tuple ColorTable__ 
    Tuple of 16 ints containing console's color attributes

  -  __int Size__ 
    Size of structure, ignored on input

## NT_FE_CONSOLE_PROPS Object

Dictionary containing information for a NT_FE_CONSOLE_PROPS struct

#### Properties

  -  __int Signature__ 
    The type of data block, one of shellcon.*_SIG values

  -  __int CodePage__ 
    The codepage to be used for console text

  -  __int Size__ 
    Size of structure, ignored on input