# PyMSG


## PyMSG Object

A tuple representing a win32 MSG structure\.

#### Items

  - \[0\] [PyHANDLE](PyHANDLE.md) : hwnd

    Handle to the window whose window procedure receives the message\.

  - \[1\] int : message

    Specifies the message identifier\.

  - \[2\] int : wParam

    Specifies additional information about the message\.

  - \[3\] int : lParam

    Specifies additional information about the message\.

  - \[4\] int : time

    Specifies the time at which the message was posted \(retrieved via GetTickCount\(\)\)\.

  - \[5\] \(int, int\) : point

    Specifies the cursor position, in screen coordinates, when the message was posted\.