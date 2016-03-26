# PyHWINSTA

## PyHWINSTA Object

Wrapper for a handle to a window station - returned by CreateWindowStation, OpenWindowStation, or GetProcessWindowStation

#### Methods


  - [EnumDesktops](PyHWINSTA.md#pyhwinstaenumdesktops)

    List desktop names within the window station&nbsp;

  - [SetProcessWindowStation](PyHWINSTA.md#pyhwinstasetprocesswindowstation)

    Associates the calling process with the window station&nbsp;

  - [CloseWindowStation](PyHWINSTA.md#pyhwinstaclosewindowstation)

    Closes the window station handle&nbsp;

  - [Detach](PyHWINSTA.md#pyhwinstadetach)

    Releases reference to handle without closing it&nbsp;

## [PyHWINSTA](#pyhwinsta).CloseWindowStation

 __CloseWindowStation(__ )
Closes the window station handle

#### Comments
This function cannot close the handle to current process's window station

## [PyHWINSTA](#pyhwinsta).EnumDesktops

(PyUNICODE,...) = __EnumDesktops(__ )
Lists names of desktops in the window station

## [PyHWINSTA](#pyhwinsta).SetProcessWindowStation

 __SetProcessWindowStation(__ )
Associates the calling process with the window station