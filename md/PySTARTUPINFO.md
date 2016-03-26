# PySTARTUPINFO


## PySTARTUPINFO Object

A Python object, representing an STARTUPINFO structure

#### Comments

Typically you create a PySTARTUPINFO \(via [win32process::STARTUPINFO](win32process.md#win32processstartupinfo)\) object, and set its properties\. 

The object can then be passed to any function which takes an STARTUPINFO object\.

#### Properties

  - integer dwX

    Specifies the x offset, in pixels, of the upper left corner of a window if a new window is created\. The offset is from the upper left corner of the screen\.

  - integer dwY

    Specifies the y offset, in pixels, of the upper left corner of a window if a new window is created\. The offset is from the upper left corner of the screen\.

  - integer dwXSize

    Specifies the width, in pixels, of the window if a new window is created\.

  - integer dwYSize

    Specifies the height, in pixels, of the window if a new window is created\.

  - integer dwXCountChars

    For console processes, if a new console window is created, specifies the screen buffer width in character columns\. This value is ignored in a GUI process\.

  - integer dwYCountChars

    For console processes, if a new console window is created, specifies the screen buffer height in character rows\.

  - integer dwFillAttribute

    Specifies the initial text and background colors if a new console window is created in a console application\. These values are ignored in GUI applications

  - integer dwFlags

    This is a bit field that determines whether certain STARTUPINFO attributes are used when the process creates a window\. To use many of the additional attributes, you typically must set the appropriate mask in this attribute, and also set the attributes themselves\. Any combination of the win32con\.STARTF\_\* flags can be specified\.

  - integer wShowWindow

    Can be any of the SW\_ constants defined in win32con\. For GUI processes, this specifies the default value the first time ShowWindow is called\.

  - integer/[PyHANDLE](PyHANDLE.md) hStdInput

    

  - integer/[PyHANDLE](PyHANDLE.md) hStdOutput

    

  - integer/[PyHANDLE](PyHANDLE.md) hStdError

    

  - string/None lpDesktop

    

  - string/None lpTitle

    