# PyCMDIFrameWnd

## PyCMDIFrameWnd Object

A main application frame window.  Encapsulates an MFC __CMDIFrameWnd__ class

#### Methods


  - [GetMDIClient](PyCMDIFrameWnd.md#pycmdiframewndgetmdiclient)

    Returns the MDI client window&nbsp;

  - [MDIGetActive](PyCMDIFrameWnd.md#pycmdiframewndmdigetactive)

    Retrieves the current active MDI child window, along with a flag indicating whether the child window is maximized.&nbsp;

  - [MDIActivate](PyCMDIFrameWnd.md#pycmdiframewndmdiactivate)

    Activate an MDI child window&nbsp;

  - [MDINext](PyCMDIFrameWnd.md#pycmdiframewndmdinext)

    Activates the next MDI window&nbsp;

  - [PreCreateWindow](PyCMDIFrameWnd.md#pycmdiframewndprecreatewindow)

    Calls the underlying MFC PreCreateWindow method.&nbsp;

  - [PreTranslateMessage](PyCMDIFrameWnd.md#pycmdiframewndpretranslatemessage)

    Calls the underlying MFC PreTranslateMessage method.&nbsp;

  - [OnCommand](PyCMDIFrameWnd.md#pycmdiframewndoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;

  - [OnContextHelp](PyCMDIFrameWnd.md#pycmdiframewndoncontexthelp)

    Calls the underlying MFC OnContextHelp method.&nbsp;

  - [OnClose](PyCMDIFrameWnd.md#pycmdiframewndonclose)

    Calls the standard Python framework OnClose handler&nbsp;


## [PyCMDIFrameWnd](#pycmdiframewnd).GetMDIClient

[PyCMDIFrameWnd](#pycmdiframewnd)= __GetMDIClient(__ )
Returns the MDI client window

## [PyCMDIFrameWnd](#pycmdiframewnd).MDIActivate

[PyCMDIFrameWnd](#pycmdiframewnd)= __MDIActivate( *window* __ )
Activate an MDI child window

#### Parameters


  -  *window* :[PyCWnd](#pycwnd)

    The window to activate.

## [PyCMDIFrameWnd](#pycmdiframewnd).MDIGetActive

([PyCMDIChildWnd](#pycmdichildwnd), int) = __MDIGetActive(__ )
Retrieves the current active MDI child window, along with a flag indicating whether the child window is maximized.

## [PyCMDIFrameWnd](#pycmdiframewnd).MDINext

 __MDINext( *fNext* __ )
Activates the next MDI window

#### Parameters


  -  *fNext=0* : int

    Indicates if the next (0) or previous (non-zero) window is requested.

#### Comments
Unlike MFC, this version supports the fNext param in the WM_MDINEXT message.

## [PyCMDIFrameWnd](#pycmdiframewnd).OnClose

 __OnClose(__ )
Calls the standard Python framework OnClose handler

## [PyCMDIFrameWnd](#pycmdiframewnd).OnCommand

 __OnCommand( *wparam*  *, lparam* __ )
Calls the standard Python framework OnCommand handler

#### Parameters


  -  *wparam* : int

    

  -  *lparam* : int

    

#### See Also


  - [PyCWnd.OnCommand](PyCWnd.md#pycwndoncommand_virtual)virtual method

## [PyCMDIFrameWnd](#pycmdiframewnd).OnContextHelp

None = __OnContextHelp(__ )
Calls the underlying MFC OnContextHelp method.

## [PyCMDIFrameWnd](#pycmdiframewnd).PreCreateWindow

tuple = __PreCreateWindow( *createStruct* __ )
Calls the underlying MFC PreCreateWindow method.

#### Parameters


  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure.

#### See Also


  - [PyCWnd.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual)virtual method

## [PyCMDIFrameWnd](#pycmdiframewnd).PreTranslateMessage

 __PreTranslateMessage(__ )
Calls the base PreTranslateMessage handler

#### See Also


  - [PyCWnd.PreTranslateMessage](PyCWnd.md#pycwndpretranslatemessage_virtual)virtual method