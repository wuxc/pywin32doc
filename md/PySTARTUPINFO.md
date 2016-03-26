# PySTARTUPINFO

## PySTARTUPINFO Object

A Python object, representing an STARTUPINFO structure

#### Comments
Typically you create a PySTARTUPINFO (via[win32process::STARTUPINFO](win32process.md#win32processstartupinfo)) object, and set its properties. 

The object can then be passed to any function which takes an STARTUPINFO object.

#### Properties

  -  __integer dwX__ 
    Specifies the x offset, in pixels, of the upper left corner of a window if a new window is created. The offset is from the upper left corner of the screen.

  -  __integer dwY__ 
    Specifies the y offset, in pixels, of the upper left corner of a window if a new window is created. The offset is from the upper left corner of the screen.

  -  __integer dwXSize__ 
    Specifies the width, in pixels, of the window if a new window is created.

  -  __integer dwYSize__ 
    Specifies the height, in pixels, of the window if a new window is created.

  -  __integer dwXCountChars__ 
    For console processes, if a new console window is created, specifies the screen buffer width in character columns. This value is ignored in a GUI process.

  -  __integer dwYCountChars__ 
    For console processes, if a new console window is created, specifies the screen buffer height in character rows.

  -  __integer dwFillAttribute__ 
    Specifies the initial text and background colors if a new console window is created in a console application. These values are ignored in GUI applications

  -  __integer dwFlags__ 
    This is a bit field that determines whether certain STARTUPINFO attributes are used when the process creates a window. To use many of the additional attributes, you typically must set the appropriate mask in this attribute, and also set the attributes themselves. Any combination of the win32con.STARTF_* flags can be specified.

  -  __integer wShowWindow__ 
    Can be any of the SW_ constants defined in win32con. For GUI processes, this specifies the default value the first time ShowWindow is called.

  -  __integer/[PyHANDLE](#pyhandle)hStdInput__ 
    

  -  __integer/[PyHANDLE](#pyhandle)hStdOutput__ 
    

  -  __integer/[PyHANDLE](#pyhandle)hStdError__ 
    

  -  __string/None lpDesktop__ 
    

  -  __string/None lpTitle__ 
    