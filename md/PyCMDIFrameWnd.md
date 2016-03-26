# PyCMDIFrameWnd


## PyCMDIFrameWnd Object

A main application frame window\.  Encapsulates an MFC CMDIFrameWnd

 class

#### Methods

  - [GetMDIClient](PyCMDIFrameWnd.md#pycmdiframewndgetmdiclient)

    Returns the MDI client window&nbsp;

  - [MDIGetActive](PyCMDIFrameWnd.md#pycmdiframewndmdigetactive)

    Retrieves the current active MDI child window, along with a flag indicating whether the child window is maximized\.&nbsp;

  - [MDIActivate](PyCMDIFrameWnd.md#pycmdiframewndmdiactivate)

    Activate an MDI child window&nbsp;

  - [MDINext](PyCMDIFrameWnd.md#pycmdiframewndmdinext)

    Activates the next MDI window&nbsp;

  - [PreCreateWindow](PyCMDIFrameWnd.md#pycmdiframewndprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [PreTranslateMessage](PyCMDIFrameWnd.md#pycmdiframewndpretranslatemessage)

    Calls the underlying MFC PreTranslateMessage method\.&nbsp;

  - [OnCommand](PyCMDIFrameWnd.md#pycmdiframewndoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;

  - [OnContextHelp](PyCMDIFrameWnd.md#pycmdiframewndoncontexthelp)

    Calls the underlying MFC OnContextHelp method\.&nbsp;

  - [OnClose](PyCMDIFrameWnd.md#pycmdiframewndonclose)

    Calls the standard Python framework OnClose handler&nbsp;




## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.GetMDIClient

[PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd) = GetMDIClient\(\)
Returns the MDI client window


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.MDIActivate

[PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd) = MDIActivate\(window\)
Activate an MDI child window

#### Parameters

  - window : [PyCWnd](PyCWnd.md)

    The window to activate\.


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.MDIGetActive

\([PyCMDIChildWnd](PyCMDIChildWnd.md), int\) = MDIGetActive\(\)
Retrieves the current active MDI child window, along with a flag indicating whether the child window is maximized\.


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.MDINext

MDINext\(fNext\)
Activates the next MDI window

#### Parameters

  - fNext=0 : int

    Indicates if the next \(0\) or previous \(non-zero\) window is requested\.

#### Comments

Unlike MFC, this version supports the fNext param in the WM\_MDINEXT message\.


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.OnClose

OnClose\(\)
Calls the standard Python framework OnClose handler


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.OnCommand

OnCommand\(wparam, lparam\)
Calls the standard Python framework OnCommand handler

#### Parameters

  - wparam : int

    

  - lparam : int

    

#### See Also

  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual) virtual method


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.OnContextHelp

None = OnContextHelp\(\)
Calls the underlying MFC OnContextHelp method\.


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.PreCreateWindow

tuple = PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters

  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.

#### See Also

  - [PyCWnd\.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual) virtual method


## [PyCMDIFrameWnd](PyCMDIFrameWnd.md#pycmdiframewnd)\.PreTranslateMessage

PreTranslateMessage\(\)
Calls the base PreTranslateMessage handler

#### See Also

  - [PyCWnd\.PreTranslateMessage](PyCWnd.md#pycwndpretranslatemessage_virtual) virtual method