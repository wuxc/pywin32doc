# PyCMDIChildWnd

## PyCMDIChildWnd Object

A windows frame window.  Encapsulates an MFC __CMDIChildWindow__ class

#### Methods


  - [ActivateFrame](PyCMDIChildWnd.md#pycmdichildwndactivateframe)

    Calls the underlying MFC ActivateFrame method.&nbsp;

  - [CreateWindow](PyCMDIChildWnd.md#pycmdichildwndcreatewindow)

    Creates the actual window for the PyCWnd object.&nbsp;

  - [GetMDIFrame](PyCMDIChildWnd.md#pycmdichildwndgetmdiframe)

    Returns the MDI parent frame&nbsp;

  - [MDIActivate](PyCMDIChildWnd.md#pycmdichildwndmdiactivate)

    Activates the MDI frame independent of the main frame.&nbsp;

  - [PreCreateWindow](PyCMDIChildWnd.md#pycmdichildwndprecreatewindow)

    Calls the underlying MFC PreCreateWindow method.&nbsp;

  - [PreTranslateMessage](PyCMDIChildWnd.md#pycmdichildwndpretranslatemessage)

    Calls the underlying MFC PreTranslateMessage method.&nbsp;

  - [OnCommand](PyCMDIChildWnd.md#pycmdichildwndoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;

  - [OnClose](PyCMDIChildWnd.md#pycmdichildwndonclose)

    Calls the standard Python framework OnClose handler&nbsp;


## [PyCMDIChildWnd](#pycmdichildwnd).ActivateFrame

 __ActivateFrame( *cmdShow* __ )
Calls the underlying MFC ActivateFrame method.

#### Parameters


  -  *cmdShow=-1* : int

    The status of the window.

#### See Also


  - [PyCMDIChildWnd.ActivateFrame](PyCMDIChildWnd.md#pycmdichildwndactivateframe_virtual)virtual method

## [PyCMDIChildWnd.ActivateFrame](#pycmdichildwnd)Virtual

 __ActivateFrame( *cmdShow* __ )
Called to activate the frame window.

#### Parameters


  -  *cmdShow* : int

    The parameter to be passed to[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow)

#### Comments
If a handler for this function exists, then the base MFC implementation will not be called. 

If you wish to use the default functionality, __PyCMDIFrameWnd::ActivateFrame__ can be called.
If there is no handler, the base MFC implementation will be called.

#### See Also


  - [PyCMDIChildWnd::ActivateFrame](PyCMDIChildWnd.md#pycmdichildwndactivateframe)

## [PyCMDIChildWnd](#pycmdichildwnd).CreateWindow

tuple = __CreateWindow( *wndClass*  *, title*  *, style*  *, rect*  *,[PyCWnd](#pycwnd)*  *, createContext* __ )
Creates the actual window for the PyCWnd object.

#### Parameters


  -  *wndClass* : string

    The window class name, or None

  -  *title* : string

    The window title

  -  *style=WS_CHILD | WS_VISIBLE | WS_OVERLAPPEDWINDOW* : int

    The window style

  -  *rect=None* : int, int, int, int

    The default rectangle

  -  *[PyCWnd](#pycwnd)=None* : parent

    The parent window

  -  *createContext=None* : tuple

    A tuple representing a CREATECONTEXT structure.

#### Comments
You do not need to call this method if you use the MFC Document/View framework.

## [PyCMDIChildWnd](#pycmdichildwnd).GetMDIFrame

 __GetMDIFrame(__ )
Returns the MDI parent frame

## [PyCMDIChildWnd.GetMessageString](#pycmdichildwnd)Virtual

 __GetMessageString( *id* __ )
Gets the message string to use for a control specific ID.

#### Parameters


  -  *id* : int

    The command ID to retrieve the string for.

#### See Also


  -  __PyCMDIChildWnd::GetMessageString__ 

## [PyCMDIChildWnd](#pycmdichildwnd).MDIActivate

 __MDIActivate( *cmdShow* __ )
Activates the MDI frame independent of the main frame.

#### Parameters


  -  *cmdShow=-1* : int

    The status of the window.

#### See Also


  - [PyCWnd.OnMDIActivate](PyCWnd.md#pycwndonmdiactivate_virtual)virtual method

## [PyCMDIChildWnd](#pycmdichildwnd).OnClose

 __OnClose(__ )
Calls the standard Python framework OnClose handler

#### See Also


  - [PyCWnd.OnClose](PyCWnd.md#pycwndonclose_virtual)virtual method

## [PyCMDIChildWnd](#pycmdichildwnd).OnCommand

 __OnCommand( *wparam*  *, lparam* __ )
Calls the standard Python framework OnCommand handler

#### Parameters


  -  *wparam* : int

    

  -  *lparam* : int

    

#### See Also


  - [PyCWnd.OnCommand](PyCWnd.md#pycwndoncommand_virtual)virtual method

## [PyCMDIChildWnd.OnCreateClient](#pycmdichildwnd)Virtual

 __OnCreateClient( *CREATESTRUCT*  *, object* __ )
Called by the framework during the execution of OnCreate.

#### Parameters


  -  *CREATESTRUCT* : tuple

    A tuple describing a CREATESTRUCT structure.

  -  *object* : object

    A Python object initially passed to LoadFrame

#### Return Value
The return value from this method is ignored, but an exception will prevent window creation.

## [PyCMDIChildWnd](#pycmdichildwnd).PreCreateWindow

tuple = __PreCreateWindow( *createStruct* __ )
Calls the underlying MFC PreCreateWindow method.

#### Parameters


  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure.

#### See Also


  - [PyCWnd.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual)virtual method

## [PyCMDIChildWnd](#pycmdichildwnd).PreTranslateMessage

 __PreTranslateMessage(__ )
Calls the base PreTranslateMessage handler

#### See Also


  - [PyCWnd.PreTranslateMessage](PyCWnd.md#pycwndpretranslatemessage_virtual)virtual method