# PyCMINVOKECOMMANDINFO

## PyCMINVOKECOMMANDINFO Object

A tuple of parameters to be converted to a CMINVOKECOMMANDINFO struct

#### Items


  - \[0\] *int* : Mask

    Combination of shellcon\.CMIC\_MASK\_\* constants, can be 0

  - \[1\] *[PyHANDLE](#pyhandle)* : hwnd

    Window that owns the shortcut menu

  - \[2\] *int or str* : Verb

    Action to be carried out, specified as a string command or integer menu item id

  - \[3\] *str* : Parameters

    Extra parameters to be passed to the command line for the action, can be None

  - \[4\] *str* : Directory

    Working directory, can be None

  - \[5\] *int* : Show

    Combination of win32con\.SW\_\* constants for any windows that may be created

  - \[6\] *int* : HotKey

    Hot key for any application that may be started

  - \[7\] *[PyHANDLE](#pyhandle)* : Icon

    Handle to icon to use for application, can be None