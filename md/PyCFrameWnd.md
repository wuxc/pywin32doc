# PyCFrameWnd


## PyCFrameWnd Object

A windows frame window\.  Encapsulates an MFC CFrameWnd

 class\.  Derived from a [PyCWnd](PyCWnd.md) object\.

#### Methods

  - [BeginModalState](PyCFrameWnd.md#pycframewndbeginmodalstate)

    Sets the frame window to modal\.&nbsp;

  - [CreateWindow](PyCFrameWnd.md#pycframewndcreatewindow)

    Creates the underlying window for the object\.&nbsp;

  - [EndModalState](PyCFrameWnd.md#pycframewndendmodalstate)

    Ends the frame window's modal state\. Enables all of the windows disabled by [PyCFrameWnd::BeginModalState](PyCFrameWnd.md#pycframewndbeginmodalstate)\.&nbsp;

  - [DockControlBar](PyCFrameWnd.md#pycframewnddockcontrolbar)

    Docks a control bar\.&nbsp;

  - [EnableDocking](PyCFrameWnd.md#pycframewndenabledocking)

    Enable dockable control bars in a frame window&nbsp;

  - [FloatControlBar](PyCFrameWnd.md#pycframewndfloatcontrolbar)

    Floats a control bar\.&nbsp;

  - [GetActiveDocument](PyCFrameWnd.md#pycframewndgetactivedocument)

    Returns the currently active document&nbsp;

  - [GetControlBar](PyCFrameWnd.md#pycframewndgetcontrolbar)

    Retrieves the specified control bar\.&nbsp;

  - [GetMessageString](PyCFrameWnd.md#pycframewndgetmessagestring)

    Retrieves message corresponding to a command ID\.&nbsp;

  - [GetMessageBar](PyCFrameWnd.md#pycframewndgetmessagebar)

    Retrieves the message bar for the frame\.&nbsp;

  - [IsTracking](PyCFrameWnd.md#pycframewndistracking)

    Determines if splitter bar is currently being moved\.&nbsp;

  - [InModalState](PyCFrameWnd.md#pycframewndinmodalstate)

    Returns a value indicating whether or not a frame window is in a modal state\.&nbsp;

  - [LoadAccelTable](PyCFrameWnd.md#pycframewndloadacceltable)

    Loads an accelerator table\.&nbsp;

  - [LoadFrame](PyCFrameWnd.md#pycframewndloadframe)

    Creates the MDI Window's frame&nbsp;

  - [LoadBarState](PyCFrameWnd.md#pycframewndloadbarstate)

    Loads a control bars settings&nbsp;

  - [PreCreateWindow](PyCFrameWnd.md#pycframewndprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [SaveBarState](PyCFrameWnd.md#pycframewndsavebarstate)

    Saves a control bars settings&nbsp;

  - [ShowControlBar](PyCFrameWnd.md#pycframewndshowcontrolbar)

    Shows a control bar\.&nbsp;

  - [RecalcLayout](PyCFrameWnd.md#pycframewndrecalclayout)

    Called by the framework when the standard control bars are toggled on or off or when the frame window is resized\.&nbsp;

  - [GetActiveView](PyCFrameWnd.md#pycframewndgetactiveview)

    Retrieves the active view\.&nbsp;

  - [OnBarCheck](PyCFrameWnd.md#pycframewndonbarcheck)

    Changes the state of the specified controlbar\.&nbsp;

  - [OnUpdateControlBarMenu](PyCFrameWnd.md#pycframewndonupdatecontrolbarmenu)

    Checks the state of a menu item&nbsp;

  - [SetActiveView](PyCFrameWnd.md#pycframewndsetactiveview)

    Sets the active view for a frame\.&nbsp;




## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.BeginModalState

BeginModalState\(\)
Sets the frame window to modal\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.CreateWindow

tuple = CreateWindow\(wndClass, title

, style

, rect

, [PyCWnd](PyCWnd.md)

, createContext

, menuId

, styleEx

\)
Creates the actual window for the PyCFrameWnd object\.

#### Parameters

  - wndClass : string

    The window class name, or None

  - title : string

    The window title

  - style=WS\_VISIBLE | WS\_OVERLAPPEDWINDOW : int

    The window style

  - rect=None : int, int, int, int

    The default rectangle

  - [PyCWnd](PyCWnd.md)=None : parent

    The parent window

  - createContext=None : tuple

    A tuple representing a CREATECONTEXT structure\.

  - menuId : string or int

    The string or integer id for the menu\.

  - styleEx : int

    The extended style of the window being created\.

#### MFC References

  - CFrameWnd::Create


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.DockControlBar

DockControlBar\(controlBar, dockBarId, int, int, int, int\)
Docks a control bar\.

#### Parameters

  - controlBar : [PyCControlBar](PyCControlBar.md)

    The control bar to dock\.

  - dockBarId=0 : int

    Determines which sides of the frame window to consider for docking\.

  - int, int, int, int=0,0,0,0 : left, top, right, bottom

    Determines, in screen coordinates, where the control bar will be docked in the nonclient area of the destination frame window\.

#### MFC References

  - CFrameWnd::DockControlBar


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.EnableDocking

EnableDocking\(style\)
Enable dockable control bars in a frame window

#### Parameters

  - style : int

    Specifies which sides of the frame window can serve as docking sites for control bars\.

#### Comments

By default, control bars will be docked to a side of the frame window in the following order: top, bottom, left, right\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.EndModalState

EndModalState\(\)
Ends the frame window's modal state\. Enables all of the windows disabled by [PyCFrameWnd::BeginModalState](PyCFrameWnd.md#pycframewndbeginmodalstate)\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.FloatControlBar

FloatControlBar\(controlBar, int, int, style\)
Floats a control bar\.

#### Parameters

  - controlBar : [PyCControlBar](PyCControlBar.md)

    The control bar to dock\.

  - int, int : x,y

    The location, in screen coordinates, where the top left corner of the control bar will be placed\.

  - style=CBRS\_ALIGN\_TOP : int

    Determines which sides of the frame window to consider for docking\.

#### MFC References

  - CFrameWnd::FloatControlBar


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.GetActiveDocument

[PyCDocument](PyCDocument.md) = GetActiveDocument\(\)
Gets the currently active document, else None

#### MFC References

  - CFrameWnd::GetActiveDocument


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.GetActiveView

[PyCView](PyCView.md) = GetActiveView\(\)
Retrieves the active view\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.GetControlBar

[PyCControlBar](PyCControlBar.md) = GetControlBar\(id\)
Retrieves the specified control bar\.

#### Parameters

  - id : int

    The ID of the toolbar to be retrieved


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.GetMessageBar

[PyCWnd](PyCWnd.md) = GetMessageBar\(\)
Retrieves the message bar for the frame\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.GetMessageString

string = GetMessageString\(id\)
Retrieves message corresponding to a command ID\.

#### Parameters

  - id : int

    The ID to be retrieved

#### See Also

  - [PyCMDIChildWnd\.GetMessageString](PyCMDIChildWnd.md#pycmdichildwndgetmessagestring_virtual) virtual method


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.InModalState

int = InModalState\(\)
Returns a value indicating whether or not a frame window is in a modal state\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.IsTracking

int = IsTracking\(\)
Determines if splitter bar is currently being moved\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.LoadAccelTable

LoadAccelTable\(id\)
Loads an accelerator table\.

#### Parameters

  - id : [PyResourceId](PyResourceId.md)

    Name or id of the resource that contains the table


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.LoadBarState

LoadBarState\(profileName\)
Loads a control bars settings

#### Parameters

  - profileName : string

    Name of a section in the initialization file or a key in the Windows registry where state information is stored\.

#### MFC References

  - CFrameWnd::LoadBarState


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.LoadFrame

LoadFrame\(idResource, style, wndParent, context\)
Loads a Windows frame window and associated resources

#### Parameters

  - idResource=IDR\_PYTHONTYPE : int

    The Id of the resources \(menu, icon, etc\) for this window

  - style=-1 : long

    The window style\.  Note -1 implies win32con\.WS\_OVERLAPPEDWINDOW|win32con\.FWS\_ADDTOTITLE

  - wndParent=None : [PyCWnd](PyCWnd.md)

    The parent of the window, or None\.

  - context=None : object

    An object passed to the OnCreateClient for the frame,

#### MFC References

  - CFrameWnd::LoadFrame


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.OnBarCheck

int = OnBarCheck\(id\)
Changes the state of the specified controlbar\.

#### Parameters

  - id : int

    The control ID of the control bar\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.OnUpdateControlBarMenu

int = OnUpdateControlBarMenu\(cmdUI\)
Checks the state of a menu item

#### Parameters

  - cmdUI : [PyCCmdUI](PyCCmdUI.md)

    A cmdui object


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.PreCreateWindow

tuple = PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters

  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.

#### See Also

  - [PyCWnd\.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual) virtual method


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.RecalcLayout

RecalcLayout\(bNotify\)
Called by the framework when the standard control bars are toggled on or off or when the frame window is resized\.

#### Parameters

  - bNotify=1 : int

    Notify flag

#### MFC References

  - CFrameWnd::RecalcLayout


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.SaveBarState

SaveBarState\(profileName\)
Saves a control bars settings

#### Parameters

  - profileName : string

    Name of a section in the initialization file or a key in the Windows registry where state information is stored\.

#### MFC References

  - CFrameWnd::SaveBarState


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.SetActiveView

SetActiveView\(view, bNotify\)
Sets the active view for a frame\.

#### Parameters

  - view : [PyCView](PyCView.md)

    The view to set active\.

  - bNotify=1 : int

    Specifies whether the view is to be notified of activation\. If TRUE, OnActivateView is called for the new view; if FALSE, it is not\.


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.ShowControlBar

ShowControlBar\(controlBar, bShow, bDelay\)
Shows a control bar\.

#### Parameters

  - controlBar : [PyCControlBar](PyCControlBar.md)

    The control bar to dock\.

  - bShow : int

    Show or hide flag\.

  - bDelay : int

    If TRUE, delay showing the control bar\. If FALSE, show the control bar immediately\.

#### MFC References

  - CFrameWnd::ShowControlBar


## [PyCFrameWnd](PyCFrameWnd.md#pycframewnd)\.ShowOwnedWindows

string = ShowOwnedWindows\(bShow\)
Shows all windows that are descendants of the [PyCFrameWnd](PyCFrameWnd.md#pycframewnd) object\.

#### Parameters

  - bShow=1 : int

    Flag