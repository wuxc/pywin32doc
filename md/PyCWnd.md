# PyCWnd

## PyCWnd Object

A base window class.  Encapsulates an MFC __CWnd__ class

#### Methods


  - [ActivateFrame](PyCWnd.md#pycwndactivateframe)

    Searches upwards for a parent window which has a frame, and activates it.&nbsp;

  - [BringWindowToTop](PyCWnd.md#pycwndbringwindowtotop)

    Brings the window to the top of a stack of overlapping windows.&nbsp;

  - [BeginPaint](PyCWnd.md#pycwndbeginpaint)

    Prepares the window for painting.&nbsp;

  - [CalcWindowRect](PyCWnd.md#pycwndcalcwindowrect)

    Computes the size of the window rectangle based on the desired client rectangle size.&nbsp;

  - [CenterWindow](PyCWnd.md#pycwndcenterwindow)

    Centers a window relative to its parent.&nbsp;

  - [CheckRadioButton](PyCWnd.md#pycwndcheckradiobutton)

    Selects a specified radio button&nbsp;

  - [ChildWindowFromPoint](PyCWnd.md#pycwndchildwindowfrompoint)

    Identifies the child window that contains the point&nbsp;

  - [ClientToScreen](PyCWnd.md#pycwndclienttoscreen)

    Convert coordinates from Client to Screen&nbsp;

  - [CreateWindow](PyCWnd.md#pycwndcreatewindow)

    Create the underlying window object&nbsp;

  - [CreateWindowEx](PyCWnd.md#pycwndcreatewindowex)

    Creates the actual window for the PyCWnd object using extended attributes.&nbsp;

  - [DefWindowProc](PyCWnd.md#pycwnddefwindowproc)

    Calls the default message handler.&nbsp;

  - [DestroyWindow](PyCWnd.md#pycwnddestroywindow)

    Destroys the window attached to the object.&nbsp;

  - [DlgDirList](PyCWnd.md#pycwnddlgdirlist)

    Fill a listbox control with a file specification.&nbsp;

  - [DlgDirListComboBox](PyCWnd.md#pycwnddlgdirlistcombobox)

    Fill a combobox control with a file specification.&nbsp;

  - [DlgDirSelect](PyCWnd.md#pycwnddlgdirselect)

    Retrieves the current selection from a list box.&nbsp;

  - [DlgDirSelectComboBox](PyCWnd.md#pycwnddlgdirselectcombobox)

    Retrieves the current selection from a combo box.&nbsp;

  - [DragAcceptFiles](PyCWnd.md#pycwnddragacceptfiles)

    Indicate the window can accept files dragges from file manager.&nbsp;

  - [DrawMenuBar](PyCWnd.md#pycwnddrawmenubar)

    Redraw the windows menu bar.&nbsp;

  - [EnableWindow](PyCWnd.md#pycwndenablewindow)

    Enable or disable the window.&nbsp;

  - [EndModalLoop](PyCWnd.md#pycwndendmodalloop)

    Ends a modal loop.&nbsp;

  - [EndPaint](PyCWnd.md#pycwndendpaint)

    Ends painting in a window&nbsp;

  - [GetCheckedRadioButton](PyCWnd.md#pycwndgetcheckedradiobutton)

    Get the ID of the checked a radio button in a group.&nbsp;

  - [GetClientRect](PyCWnd.md#pycwndgetclientrect)

    Gets the client rectangle for thewindow.&nbsp;

  - [GetDC](PyCWnd.md#pycwndgetdc)

    Gets the window's current device context.&nbsp;

  - [GetDCEx](PyCWnd.md#pycwndgetdcex)

    Gets the window's current device context.&nbsp;

  - [GetDlgCtrlID](PyCWnd.md#pycwndgetdlgctrlid)

    Get the current window's control id.&nbsp;

  - [GetDlgItem](PyCWnd.md#pycwndgetdlgitem)

    Get a child control by Id&nbsp;

  - [GetDlgItemInt](PyCWnd.md#pycwndgetdlgitemint)

    Returns the integer value of a child window or control with the specified ID.&nbsp;

  - [GetDlgItemText](PyCWnd.md#pycwndgetdlgitemtext)

    Returns the text of child window or control with the specified ID.&nbsp;

  - [GetLastActivePopup](PyCWnd.md#pycwndgetlastactivepopup)

    Identifies the most recently active pop-up window&nbsp;

  - [GetMenu](PyCWnd.md#pycwndgetmenu)

    Get the current menu for a window.&nbsp;

  - [GetParent](PyCWnd.md#pycwndgetparent)

    Get the parent window.&nbsp;

  - [GetParentFrame](PyCWnd.md#pycwndgetparentframe)

    Returns the window's frame.&nbsp;

  - [GetParent](PyCWnd.md#pycwndgetparent)

    Returns the child window's parent window or owner window.&nbsp;

  - [GetSafeHwnd](PyCWnd.md#pycwndgetsafehwnd)

    Returns the HWnd of this window.&nbsp;

  - [GetScrollInfo](PyCWnd.md#pycwndgetscrollinfo)

    Retrieve information about a scroll bar&nbsp;

  - [GetScrollPos](PyCWnd.md#pycwndgetscrollpos)

    Retrieves the current position of the scroll box of a scroll bar.&nbsp;

  - [GetStyle](PyCWnd.md#pycwndgetstyle)

    Retrieves the window style&nbsp;

  - [GetExStyle](PyCWnd.md#pycwndgetexstyle)

    Retrieves the window extended style&nbsp;

  - [GetSystemMenu](PyCWnd.md#pycwndgetsystemmenu)

    Get the system menu for the window.&nbsp;

  - [GetTopLevelFrame](PyCWnd.md#pycwndgettoplevelframe)

    Get the top-level frame window.&nbsp;

  - [GetTopLevelOwner](PyCWnd.md#pycwndgettoplevelowner)

    Get the top-level owner window.&nbsp;

  - [GetTopLevelParent](PyCWnd.md#pycwndgettoplevelparent)

    Get the top-level parent window.&nbsp;

  - [GetTopWindow](PyCWnd.md#pycwndgettopwindow)

    Get the top level window attached to this window.&nbsp;

  - [GetWindow](PyCWnd.md#pycwndgetwindow)

    Get a specified window (eg, parent, child, etc).&nbsp;

  - [GetWindowDC](PyCWnd.md#pycwndgetwindowdc)

    Obtains the __PyDC__ for a window.&nbsp;

  - [GetWindowPlacement](PyCWnd.md#pycwndgetwindowplacement)

    Gets the window's current placement information.&nbsp;

  - [GetWindowRect](PyCWnd.md#pycwndgetwindowrect)

    Get the windows rectangle.&nbsp;

  - [GetWindowText](PyCWnd.md#pycwndgetwindowtext)

    Get the window's current text.&nbsp;

  - [HideCaret](PyCWnd.md#pycwndhidecaret)

    Hides the caret&nbsp;

  - [HookAllKeyStrokes](PyCWnd.md#pycwndhookallkeystrokes)

    Hook a handler for all keystroke messages.&nbsp;

  - [HookKeyStroke](PyCWnd.md#pycwndhookkeystroke)

    Hook a keystroke handler.&nbsp;

  - [HookMessage](PyCWnd.md#pycwndhookmessage)

    Hook a message notification handler.&nbsp;

  - [InvalidateRect](PyCWnd.md#pycwndinvalidaterect)

    Invalidate a specified rectangle in a window.&nbsp;

  - [InvalidateRgn](PyCWnd.md#pycwndinvalidatergn)

    Invalidate a specified region of a window.&nbsp;

  - [IsChild](PyCWnd.md#pycwndischild)

    Indicates if a window is a child.&nbsp;

  - [IsDlgButtonChecked](PyCWnd.md#pycwndisdlgbuttonchecked)

    Indicates if a dialog botton is checked.&nbsp;

  - [IsIconic](PyCWnd.md#pycwndisiconic)

    Indicates if the window is currently minimised.&nbsp;

  - [IsZoomed](PyCWnd.md#pycwndiszoomed)

    Indicates if the window is currently maximised.&nbsp;

  - [IsWindow](PyCWnd.md#pycwndiswindow)

    determines whether the specified window handle identifies an existing window.&nbsp;

  - [IsWindowVisible](PyCWnd.md#pycwndiswindowvisible)

    Determines if the window is currently visible.&nbsp;

  - [IsWindowVisible](PyCWnd.md#pycwndiswindowvisible)

    Determines if the window is currently enabled.&nbsp;

  - [KillTimer](PyCWnd.md#pycwndkilltimer)

    Destroys a system timer&nbsp;

  - [LockWindowUpdate](PyCWnd.md#pycwndlockwindowupdate)

    Disables drawing in the given window&nbsp;

  - [MapWindowPoints](PyCWnd.md#pycwndmapwindowpoints)

    Converts (maps) a set of points from the coordinate space of the CWnd to the coordinate space of another window.&nbsp;

  - [MouseCaptured](PyCWnd.md#pycwndmousecaptured)

    Indicates if the window currently has the mouse captured.&nbsp;

  - [MessageBox](PyCWnd.md#pycwndmessagebox)

    Displays a message box.&nbsp;

  - [ModifyStyle](PyCWnd.md#pycwndmodifystyle)

    Modifies the style of a window.&nbsp;

  - [ModifyStyleEx](PyCWnd.md#pycwndmodifystyleex)

    Modifies the style of a window.&nbsp;

  - [MoveWindow](PyCWnd.md#pycwndmovewindow)

    Moves the window to a new location.&nbsp;

  - [OnClose](PyCWnd.md#pycwndonclose)

    Calls the default MFC OnClose handler.&nbsp;

  - [OnCtlColor](PyCWnd.md#pycwndonctlcolor)

    Calls the default MFC OnCtlColor handler.&nbsp;

  - [OnEraseBkgnd](PyCWnd.md#pycwndonerasebkgnd)

    Calls the default MFC OnEraseBkgnd handler.&nbsp;

  - [OnNcHitTest](PyCWnd.md#pycwndonnchittest)

    Calls the base MFC OnNcHitTest function.&nbsp;

  - [OnPaint](PyCWnd.md#pycwndonpaint)

    Calls the default MFC OnPaint handler.&nbsp;

  - [OnQueryDragIcon](PyCWnd.md#pycwndonquerydragicon)

    Calls the default MFC OnQueryDragIcon handler.&nbsp;

  - [OnQueryNewPalette](PyCWnd.md#pycwndonquerynewpalette)

    Calls the underlying MFC OnQueryNewPalette method.&nbsp;

  - [OnSetCursor](PyCWnd.md#pycwndonsetcursor)

    Calls the default MFC OnSetCursor message&nbsp;

  - [OnMouseActivate](PyCWnd.md#pycwndonmouseactivate)

    Calls the default MFC OnMouseActicate message&nbsp;

  - [OnWndMsg](PyCWnd.md#pycwndonwndmsg)

    Calls the default MFC Window Message handler.&nbsp;

  - [PreCreateWindow](PyCWnd.md#pycwndprecreatewindow)

    Calls the underlying MFC PreCreateWindow method.&nbsp;

  - [PumpWaitingMessages](PyCWnd.md#pycwndpumpwaitingmessages)

    Calls the Peek/Dispatch loop on the wnd.&nbsp;

  - [RedrawWindow](PyCWnd.md#pycwndredrawwindow)

    Updates the specified rectangle or region in the given window's client area.&nbsp;

  - [ReleaseCapture](PyCWnd.md#pycwndreleasecapture)

    Releases the mouse capture for the window.&nbsp;

  - [ReleaseDC](PyCWnd.md#pycwndreleasedc)

    Releases a device context, freeing it for use by other applications.&nbsp;

  - [RepositionBars](PyCWnd.md#pycwndrepositionbars)

    Repositions the control bars for the window.&nbsp;

  - [RunModalLoop](PyCWnd.md#pycwndrunmodalloop)

    Starts a modal loop for the window.&nbsp;

  - [PostMessage](PyCWnd.md#pycwndpostmessage)

    Post a message to the window.&nbsp;

  - [SendMessageToDescendants](PyCWnd.md#pycwndsendmessagetodescendants)

    Send a message to a window's children.&nbsp;

  - [SendMessage](PyCWnd.md#pycwndsendmessage)

    Send a message to the window.&nbsp;

  - [SetActiveWindow](PyCWnd.md#pycwndsetactivewindow)

    Sets the window active.&nbsp;

  - [SetForegroundWindow](PyCWnd.md#pycwndsetforegroundwindow)

    Puts the window into the foreground and activates the window.&nbsp;

  - [SetWindowPos](PyCWnd.md#pycwndsetwindowpos)

    Sets the windows position information.&nbsp;

  - [ScreenToClient](PyCWnd.md#pycwndscreentoclient)

    Converts from screen coordinates to client coordinates.&nbsp;

  - [SetCapture](PyCWnd.md#pycwndsetcapture)

    Captures the mouse input for thw window.&nbsp;

  - [SetDlgItemText](PyCWnd.md#pycwndsetdlgitemtext)

    Sets the text for the child window or control with the specified ID.&nbsp;

  - [SetFocus](PyCWnd.md#pycwndsetfocus)

    Sets focus to the window.&nbsp;

  - [SetFont](PyCWnd.md#pycwndsetfont)

    Sets the window's current font to the specified font.&nbsp;

  - [SetIcon](PyCWnd.md#pycwndseticon)

    Sets the handle to a specific icon.&nbsp;

  - [SetMenu](PyCWnd.md#pycwndsetmenu)

    Sets the menu for a window.&nbsp;

  - [SetRedraw](PyCWnd.md#pycwndsetredraw)

    Sets the redraw flag for the window.&nbsp;

  - [SetScrollPos](PyCWnd.md#pycwndsetscrollpos)

    Sets the current position of the scroll box of a scroll bar.&nbsp;

  - [SetScrollInfo](PyCWnd.md#pycwndsetscrollinfo)

    Set information about a scroll bar&nbsp;

  - [SetTimer](PyCWnd.md#pycwndsettimer)

    Installs a system timer&nbsp;

  - [SetWindowPlacement](PyCWnd.md#pycwndsetwindowplacement)

    Sets the window's placement options.&nbsp;

  - [SetWindowText](PyCWnd.md#pycwndsetwindowtext)

    Sets the window's text.&nbsp;

  - [ShowCaret](PyCWnd.md#pycwndshowcaret)

    Shows the caret&nbsp;

  - [ShowScrollBar](PyCWnd.md#pycwndshowscrollbar)

    Shows/Hides the window's scroll bars.&nbsp;

  - [ShowWindow](PyCWnd.md#pycwndshowwindow)

    Shows the window.&nbsp;

  - [UnLockWindowUpdate](PyCWnd.md#pycwndunlockwindowupdate)

    Unlocks a window that was locked with LockWindowUpdate&nbsp;

  - [UpdateData](PyCWnd.md#pycwndupdatedata)

    Updates a windows dialog data.&nbsp;

  - [UpdateDialogControls](PyCWnd.md#pycwndupdatedialogcontrols)

    Updates the state of dialog buttons and other controls in a dialog box or window that uses the __PyCCmdUI::HookCommandUpdate__ callback mechanism.&nbsp;

  - [UpdateWindow](PyCWnd.md#pycwndupdatewindow)

    Updates a window.&nbsp;


## [PyCWnd](#pycwnd).ActivateFrame

 __ActivateFrame( *cmdShow* __ )
Searches upwards for a parent window which has 

a frame, and activates it.

#### Parameters


  -  *cmdShow=SW_SHOW* : int

    The param passed to __CFrameWnd::ShowWindow__ .  See also[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow).

#### MFC References


  - CFrameWnd::ActivateFrame

## [PyCWnd](#pycwnd).BeginPaint

[PyCDC](#pycdc), __PAINTSTRUCT__ = __BeginPaint(__ )
Prepares a window for painting

#### Return Value
You must pass the PAINTSTRUCT param to the[PyCWnd::EndPaint](PyCWnd.md#pycwndendpaint)method.

## [PyCWnd](#pycwnd).BringWindowToTop

 __BringWindowToTop(__ )
Brings the window to the top of a stack of overlapping windows.

#### Comments
This method activates pop-up, top-level, and MDI child windows. 

The BringWindowToTop member function should be used to uncover any window that is partially or 

completely obscured by any overlapping windows.
Calling this method is similar to calling the[PyCWnd::SetWindowPos](PyCWnd.md#pycwndsetwindowpos)method to 

change a window's position in the Z order. The BringWindowToTop method 

does not change the window style to make it a top-level window of the desktop.

#### MFC References


  - CWnd::BringWindowToTop

## [PyCWnd](#pycwnd).CalcWindowRect

(left, top, right, bottom) = __CalcWindowRect( *rect*  *, nAdjustType* __ )
Computes the size of the window rectangle based on the desired client 

rectangle size.  The resulting size can then be used as the initial 

size for the window object.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    The size to calculate from

  -  *nAdjustType=adjustBorder* : int

    An enumerated type used for in-place editing. It can have the following values: CWnd::adjustBorder = 0, which 

means that scrollbar sizes are ignored in calculation; and CWnd::adjustOutside = 1, which means that they are added into the final 

measurements of the rectangle.

#### MFC References


  - CWnd::CalcWindowRect

## [PyCWnd](#pycwnd).CenterWindow

 __CenterWindow( *altwin* __ )
Centers a window relative to its parent.

#### Parameters


  -  *altwin=None* :[PyCWnd](#pycwnd)

    alternate window relative to which it will be centered (other than the parent window).

#### MFC References


  - CWnd::CenterWindow

## [PyCWnd](#pycwnd).CheckRadioButton

 __CheckRadioButton( *idFirst*  *, idLast*  *, idCheck* __ )
Selects the specified radio button, and clears 

all others in the group.

#### Parameters


  -  *idFirst* : int

    The identifier of the first radio button in the group.

  -  *idLast* : int

    The identifier of the last radio button in the group.

  -  *idCheck* : int

    The identifier of the radio button to be checked.

#### MFC References


  - CWnd::CheckRadioButton

## [PyCWnd](#pycwnd).ChildWindowFromPoint

PyCWnd = __ChildWindowFromPoint( *x*  *, y*  *, flag* __ )
Returns the child window that contains the point

#### Parameters


  -  *x* : int

    x coordinate of point

  -  *y* : int

    y coordinate of point

  -  *flag=0* : int

    Specifies which child windows to skip

#### MFC References


  - CWnd::ChildWindowFromPoint

## [PyCWnd](#pycwnd).ClientToScreen

(x,y) or (l, t, r, b) = __ClientToScreen( *point* __ )
Converts the client coordinates of a given point on the display to screen coordinates.

#### Parameters


  -  *point* : (x,y)

    The client coordinates.

#### Alternative Parameters


  -  *rect* 

    The client coordinates.

#### Comments
The new screen coordinates are relative to the upper-left corner of the system display. 

This function assumes that the given pointis in client coordinates.

#### MFC References


  - CWnd::ClientToScreen

## [PyCWnd](#pycwnd).CreateWindow

 __CreateWindow( *classId*  *, windowName*  *, style*  *, rect*  *, parent*  *, id*  *, context* __ )
Creates the actual window

#### Parameters


  -  *classId* : string

    The class ID for the window, or None

  -  *windowName* : string

    The title for the window, or None

  -  *style* : int

    The style for the window.

  -  *rect* : (left, top, right, bottom)

    The size and position of the window.

  -  *parent* :[PyCWnd](#pycwnd)

    The parent window of the new window..

  -  *id* : int

    The control's ID.

  -  *context=None* : object

    A CreateContext object.

#### MFC References


  - CWnd::Create

## [PyCWnd](#pycwnd).CreateWindowEx

 __CreateWindowEx( *styleEx*  *, classId*  *, windowName*  *, style*  *, rect*  *, parent*  *, id*  *, createStruct*  *, createStruct* __ )
Creates the actual window using extended capabilities.

#### Parameters


  -  *styleEx* : int

    The extended style of the window being created.

  -  *classId* : string

    The class ID for the window.  May not be None.

  -  *windowName* : string

    The title for the window, or None

  -  *style* : int

    The style for the window.

  -  *rect* : (left, top, right, bottom)

    The size and position of the window.

  -  *parent* :[PyCWnd](#pycwnd)

    The parent window of the new window..

  -  *id* : int

    The control's ID.

  -  *createStruct=None* :[CREATESTRUCT](#createstruct)

    A CreateStruct object (ie, a tuple)

  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure.

#### MFC References


  - CWnd::CreateEx

## [PyCWnd](#pycwnd).DefWindowProc

int = __DefWindowProc( *message*  *, idLast*  *, idCheck* __ )
Calls the default message handler.

#### Parameters


  -  *message* : int

    The Windows message.

  -  *idLast* : int

    The lParam for the message.

  -  *idCheck* : int

    The wParam for the message.

#### MFC References


  - CWnd::DefWindowProc

## [PyCWnd](#pycwnd).DestroyWindow

 __DestroyWindow(__ )
Destroy the window attached to the object.

#### Comments
The DestroyWindow member function sends appropriate messages 

to the window to deactivate it and remove the input focus. 

It also destroys the window's menu, flushes the application queue, 

destroys outstanding timers, removes Clipboard ownership, and breaks the 

Clipboard-viewer chain if CWnd is at the top of the viewer chain. 

It sends WM_DESTROY and WM_NCDESTROY messages to the window.

## [PyCWnd](#pycwnd).DlgDirList

 __DlgDirList( *defPath*  *, idListbox*  *, idStaticPath*  *, fileType* __ )
Fill a list box with a file or directory listing.

#### Parameters


  -  *defPath* : string

    The file spec to fill the list box with

  -  *idListbox* : int

    The Id of the listbox control to fill.

  -  *idStaticPath* : int

    The Id of the static control used to display the current drive and directory. If idStaticPath is 0, it is assumed that no such control exists.

  -  *fileType* : int

    Specifies the attributes of the files to be displayed. 

It can be any combination of DDL_READWRITE, DDL_READONLY, DDL_HIDDEN, DDL_SYSTEM, DDL_DIRECTORY, DDL_ARCHIVE, DDL_POSTMSGS, DDL_DRIVES or DDL_EXCLUSIVE

#### MFC References


  - CWnd::DlgDirList

## [PyCWnd](#pycwnd).DlgDirListComboBox

 __DlgDirListComboBox(__ )
Fill a combo with a file or directory listing.  See[PyCWnd::DlgDirList](PyCWnd.md#pycwnddlgdirlist)for details.

#### MFC References


  - CWnd::DlgDirListComboBox

## [PyCWnd](#pycwnd).DlgDirSelect

string = __DlgDirSelect( *idListbox* __ )
Retrieves the current selection from a list box. It assumes that the list box has been filled by the[PyCWnd::DlgDirList](PyCWnd.md#pycwnddlgdirlist)member function and that the selection is a drive letter, a file, or a directory name.

#### Parameters


  -  *idListbox* : int

    The Id of the listbox.

#### MFC References


  - CWnd::DlgDirSelect

## [PyCWnd](#pycwnd).DlgDirSelectComboBox

string = __DlgDirSelectComboBox( *idListbox* __ )
Retrieves the current selection from the list box of a combo box. It assumes that the list box has been filled by the[PyCWnd::DlgDirListComboBox](PyCWnd.md#pycwnddlgdirlistcombobox)member function and that the selection is a drive letter, a file, or a directory name.

#### Parameters


  -  *idListbox* : int

    The Id of the combobox.

#### MFC References


  - CWnd::DlgDirSelectComboBox

## [PyCWnd](#pycwnd).DragAcceptFiles

 __DragAcceptFiles( *bAccept* __ )
Indicates that the window and children supports files dropped from file manager

#### Parameters


  -  *bAccept=1* : int

    A flag indicating if files are accepted.

#### MFC References


  - CWnd::DragAcceptFiles

## [PyCWnd](#pycwnd).DrawMenuBar

 __DrawMenuBar(__ )
Redraws the menu bar.  Can be called if the menu changes.

## [PyCWnd](#pycwnd).EnableWindow

int = __EnableWindow( *bEnable* __ )
Enables or disables the window.  Typically used for dialog controls.

#### Parameters


  -  *bEnable=1* : int

    A flag indicating if the window is to be enabled or disabled.

#### MFC References


  - CWnd::EnableWindow

#### Return Value
Returns the state before the EnableWindow member function was called

## [PyCWnd](#pycwnd).EndModalLoop

 __EndModalLoop( *result* __ )
Ends a modal loop.

#### Parameters


  -  *result* : int

    The result as returned to RunModalLoop

## [PyCWnd](#pycwnd).EndPaint

 __EndPaint( *paintStruct* __ )
Ends painting

#### Parameters


  -  *paintStruct* : __PAINTSTRUCT__ 

    The object returned from[PyCWnd::BeginPaint](PyCWnd.md#pycwndbeginpaint)

## [PyCWnd](#pycwnd).GetCheckedRadioButton

int = __GetCheckedRadioButton( *idFirst*  *, idLast* __ )
Returns the ID of the checked radio button, or 0 if none is selected.

#### Parameters


  -  *idFirst* : int

    The Id of the first radio button in the group.

  -  *idLast* : int

    The Id of the last radio button in the group.

#### MFC References


  - CWnd::GetCheckedRadioButton

## [PyCWnd](#pycwnd).GetClientRect

(left, top, right, bottom) = __GetClientRect(__ )
Returns the client coordinates of the window.  left and top will be zero.

## [PyCWnd](#pycwnd).GetDC

[PyCDC](#pycdc)= __GetDC(__ )
Gets the windows current DC object.

#### Return Value
The result is a[PyCDC](#pycdc), or a win32ui.error exception is raised.

## [PyCWnd](#pycwnd).GetDCEx

[PyCDC](#pycdc)= __GetDCEx(__ )
Gets the windows current DC object with extended caps.

## [PyCWnd](#pycwnd).GetDlgCtrlID

int = __GetDlgCtrlID(__ )
Returns the ID of this child window.

#### MFC References


  - CWnd::GetDlgCtrlId

## [PyCWnd](#pycwnd).GetDlgItem

[PyCWnd](#pycwnd)= __GetDlgItem( *idControl* __ )
Returns a window object for the child window or control with the specified ID. 

The type of the return object will be as specific as possible, but will always 

be derived from an[PyCWnd](#pycwnd)object.

#### Parameters


  -  *idControl* : int

    The Id of the control to be retrieved.

#### MFC References


  - CWnd::GetDlgItem

#### Return Value
The result is a[PyCWnd](#pycwnd)(or derived) object, or a win32ui.error exception is raised.

## [PyCWnd](#pycwnd).GetDlgItemInt

int = __GetDlgItemInt( *idControl*  *, bUnsigned* __ )
Returns the integer value of a child window or control with the specified ID.

#### Parameters


  -  *idControl* : int

    The Id of the control to be retrieved.

  -  *bUnsigned=1* : int

    Should the function check for a minus sign

#### MFC References


  - CWnd::GetDlgItemInt

#### Return Value
If the value can not be converted, a ValueError is raised.

## [PyCWnd](#pycwnd).GetDlgItemText

string = __GetDlgItemText( *idControl* __ )
Returns the text of child window or control with the specified ID.

#### Parameters


  -  *idControl* : int

    The Id of the control to be retrieved.

#### MFC References


  - CWnd::GetDlgItemText

## [PyCWnd](#pycwnd).GetExStyle

int = __GetExStyle(__ )
Retrieves the window's extended style

## [PyCWnd](#pycwnd).GetLastActivePopup

[PyCWnd](#pycwnd)= __GetLastActivePopup(__ )
Returns the last active popup Window, or the Window itself.

#### MFC References


  - CWnd::GetLastActivePopup

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetMenu

[PyCMenu](#pycmenu)= __GetMenu(__ )
Returns the menu object for the window's menu.

#### MFC References


  - CWnd::GetMenu

#### Return Value
The result is a __PyMenu__ object, or an exception is thrown.

## [PyCWnd](#pycwnd).GetParent

[PyCWnd](#pycwnd)= __GetParent(__ )
Returns the window's parent.

#### MFC References


  - CWnd::GetParent

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetParentFrame

[PyCWnd](#pycwnd)= __GetParentFrame(__ )
Returns the window's frame.

#### MFC References


  - CWnd::GetParentFrame

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetParentOwner

[PyCWnd](#pycwnd)= __GetParentOwner(__ )
Returns the child window's parent window or owner window.

#### MFC References


  - CWnd::GetParentOwner

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetSafeHwnd

int = __GetSafeHwnd(__ )
Returns the HWnd of this window.

#### MFC References


  - CWnd::GetSafeHwnd

## [PyCWnd](#pycwnd).GetScrollInfo

[SCROLLINFO tuple](SCROLLINFO.md#scrollinfotuple)= __GetScrollInfo( *nBar*  *, mask* __ )
Returns information about a scroll bar

#### Parameters


  -  *nBar* : int

    The scroll bar to examine.  Can be one of win32con.SB_BOTH, win32con.SB_VERT or win32con.SB_HORZ

  -  *mask=SIF_ALL* : int

    The mask for attributes to retrieve.

## [PyCWnd](#pycwnd).GetScrollPos

int = __GetScrollPos( *nBar* __ )
Retrieves the current position of the scroll box of a scroll bar.

#### Parameters


  -  *nBar* : int

    The scroll bar to examine.  Can be one of win32con.SB_VERT or win32con.SB_HORZ

## [PyCWnd](#pycwnd).GetStyle

int = __GetStyle(__ )
Retrieves the window style

## [PyCWnd](#pycwnd).GetSystemMenu

[PyCMenu](#pycmenu)= __GetSystemMenu(__ )
Returns the menu object for the window's system menu.

#### MFC References


  - CWnd::GetSystemMenu

## [PyCWnd](#pycwnd).GetTopLevelFrame

[PyCWnd](#pycwnd)= __GetTopLevelFrame(__ )
Returns the top-level frame of the window.

#### MFC References


  - CWnd::GetTopLevelFrame

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetTopLevelOwner

[PyCWnd](#pycwnd)= __GetTopLevelOwner(__ )
Returns the top-level owner of the window.

#### MFC References


  - CWnd::GetTopLevelOwner

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetTopLevelParent

[PyCWnd](#pycwnd)= __GetTopLevelParent(__ )
Returns the top-level parent of the window.

#### MFC References


  - CWnd::GetTopLevelParent

#### Return Value
The result is a[PyCWnd](#pycwnd)object, or None if no Window can be found.

## [PyCWnd](#pycwnd).GetTopWindow

[PyCWnd](#pycwnd)= __GetTopWindow(__ )
Identifies the top-level child window in a linked list of child windows.

#### Comments
Searches for the top-level child window that belongs to this window. If this window has no children, this function returns None

#### MFC References


  - CWnd::GetTopWindow

#### Return Value
If no child windows exist, the value is None.

## [PyCWnd](#pycwnd).GetWindow

[PyCWnd](#pycwnd)= __GetWindow( *type* __ )
Returns a window, with the specified relationship to this window.

#### Parameters


  -  *type* : int

    Specifies the relationship between the current and the returned window. It can take one of the following values: 

GW_CHILD, GW_HWNDFIRST, GW_HWNDLAST, GW_HWNDNEXT, GW_HWNDPREV or GW_OWNER

#### MFC References


  - CWnd::GetWindow

#### Return Value
The result is a[PyCWnd](#pycwnd)or None if no Window can be found.

## [PyCWnd](#pycwnd).GetWindowDC

[PyCDC](#pycdc)= __GetWindowDC(__ )
Gets the windows current DC object.

## [PyCWnd](#pycwnd).GetWindowPlacement

tuple = __GetWindowPlacement(__ )
Returns placement information about the current window.

#### MFC References


  - CWnd::GetWindowPlacement

#### Return Value
The result is a tuple of 

(flags, showCmd, (minposX, minposY), (maxposX, maxposY), (normalposX, normalposY))


## [PyCWnd](#pycwnd).GetWindowRect

(left, top, right, bottom) = __GetWindowRect(__ )
Returns the screen coordinates of the windows upper left corner

#### MFC References


  - CWnd::GetWindowRect

## [PyCWnd](#pycwnd).GetWindowText

string = __GetWindowText(__ )
Returns the windows text.

#### MFC References


  - CWnd::Py_BuildValue

## [PyCWnd](#pycwnd).HideCaret

 __HideCaret(__ )
Hides the caret

#### Comments
See also[PyCWnd::ShowCaret](PyCWnd.md#pycwndshowcaret)

## [PyCWnd](#pycwnd).HookAllKeyStrokes

 __HookAllKeyStrokes( *obHandler* __ )
Hook a key stroke handler for all key strokes.

#### Parameters


  -  *obHandler* : object

    The handler for the keystrokes.  This must be a callable object.

#### Comments
The handler object passed will be called as the application receives WM_CHAR messages. 

The handler will be called with 2 arguments
The handler object (as per all hook functions).
The keystroke being handled.
If the handler returns TRUE, then the keystroke will be passed on to the 

default handler, otherwise it will be consumed.
Note: This handler will prevent any[PyCWnd::HookKeyStroke](PyCWnd.md#pycwndhookkeystroke)hooks from being called.

## [PyCWnd](#pycwnd).HookKeyStroke

object = __HookKeyStroke( *obHandler*  *, ch* __ )
Hook a key stroke handler

#### Parameters


  -  *obHandler* : object

    The handler of the keystroke.  This must be a callable object.

  -  *ch* : int

    The ID for the keystroke to be handled. 

This may be an ascii code, or a virtual key code.

#### Comments
The handler object passed will be called as the application receives WM_CHAR message for the specified character code. 

The handler will be called with 2 arguments
The handler object (as per all hook functions)
The keystroke being handled.
If the handler returns TRUE, then the keystroke will be passed on to the 

default handler, otherwise the keystroke will be consumed.
Note: This handler will not be called if a[PyCWnd::HookAllKeyStrokes](PyCWnd.md#pycwndhookallkeystrokes)hook is in place.

#### Return Value
The return value is the previous handler, or None.

## [PyCWnd](#pycwnd).HookMessage

object = __HookMessage( *obHandler*  *, message* __ )
Hook a message notification handler

#### Parameters


  -  *obHandler* : object

    The handler for the message notification.  This must be a callable object.

  -  *message* : int

    The ID of the message to be handled.

#### Comments
The handler object passed will be called as the application receives messages with the specified ID. 

Note that it is not possible for PythonWin to consume a message - it is always passed on to the default handler. 

The handler will be called with 2 arguments
The handler object (as per all hook functions).
A tuple representing the message.
The message tuple is in the following format:

#### Items


  - [0] *int* : hwnd

    The hwnd of the window.

  - [1] *int* : message

    The message.

  - [2] *int* : wParam

    The wParam sent with the message.

  - [3] *int* : lParam

    The lParam sent with the message.

  - [4] *int* : time

    The time the message was posted.

  - [5] *int, int* : point

    The point where the mouse was when the message was posted.

#### Return Value
The return value is the previous handler, or None.

## [PyCWnd](#pycwnd).InvalidateRect

 __InvalidateRect( *rect*  *, bErase* __ )
Invalidates an area of a window.

#### Parameters


  -  *rect=(0,0,0,0)* : (left, top, right, bottom)

    Rectangle to be 

updated.  If default param is used, the entire window is invalidated.

  -  *bErase=1* : int

    Specifies whether the background within the update region is to be erased.

#### MFC References


  - CWnd::InvalidateRect

## [PyCWnd](#pycwnd).InvalidateRgn

 __InvalidateRgn( *region*  *, bErase* __ )
Invalidates a region of the window

#### Parameters


  -  *region* :[PyCRgn](#pycrgn)

    The region to erase.

  -  *bErase=1* : int

    Indicates if the region should be erased.

## [PyCWnd](#pycwnd).IsChild

int = __IsChild( *obWnd* __ )
Determines if a given window is a child of this window.

#### Parameters


  -  *obWnd* :[PyCWnd](#pycwnd)

    The window to be checked

#### MFC References


  - CWnd::IsChild

## [PyCWnd](#pycwnd).IsDlgButtonChecked

int = __IsDlgButtonChecked( *idCtl* __ )
Determines if a dialog button is checked.

#### Parameters


  -  *idCtl* : int

    The ID of the button to check.

#### MFC References


  - CWnd::IsDlgButtonChecked

## [PyCWnd](#pycwnd).IsIconic

int = __IsIconic(__ )
Determines if the window is currently displayed as an icon.

## [PyCWnd](#pycwnd).IsWindow

int = __IsWindow(__ )
determines whether the specified window handle identifies an existing window

## [PyCWnd](#pycwnd).IsWindowEnabled

int = __IsWindowEnabled(__ )
Determines if the window is currently enabled.

## [PyCWnd](#pycwnd).IsWindowVisible

int = __IsWindowVisible(__ )
Determines if the window is currently visible.

## [PyCWnd](#pycwnd).IsZoomed

int = __IsZoomed(__ )
Determines if the window is currently maximised.

## [PyCWnd](#pycwnd).KillTimer

int = __KillTimer(__ )
Kills a system timer

#### MFC References


  - CWnd::KillTimer

## [PyCWnd](#pycwnd).LockWindowUpdate

 __LockWindowUpdate(__ )
Disables drawing in the given window

#### MFC References


  - CWnd::LockWindowUpdate

## [PyCWnd](#pycwnd).MapWindowPoints

 __MapWindowPoints( *wnd*  *, points* __ )
Converts (maps) a set of points from the coordinate space of a window to the coordinate space of another window.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    

  -  *points* : [ (x,y), ...]

    The points to map

#### Return Value
A list of the mapped points from the coordinate space of the CWnd to the coordinate space of another window.

## [PyCWnd](#pycwnd).MessageBox

 __MessageBox( *message*  *, title*  *, style* __ )
Display a message box.

#### Parameters


  -  *message* : string

    The message to be displayed in the message box.

  -  *title=None* : string/None

    The title for the message box.  If None, the applications title will be used.

  -  *style=win32con.MB_OK* : int

    The style of the message box.

#### MFC References


  - CWnd::MessageBox

#### Return Value
An integer identifying the button pressed to dismiss the dialog.

## [PyCWnd](#pycwnd).ModifyStyle

int = __ModifyStyle( *remove*  *, add*  *, flags* __ )
Modifies the style of a window.

#### Parameters


  -  *remove* : int

    Specifies window styles to be removed during style modification.

  -  *add* : int

    Specifies window styles to be added during style modification.

  -  *flags=0* : int

    Flags to be passed to SetWindowPos, or zero if SetWindowPos should not be called. The default is zero.

#### Comments
If nFlags is nonzero, ModifyStyle calls the Windows API function ::SetWindowPos and redraws the window by combining nFlags with the following four preset flags:
* SWP_NOSIZE&#09Retains the current size.
* SWP_NOMOVE&#09Retains the current position.
* SWP_NOZORDER&#09Retains the current Z order.
* SWP_NOACTIVATE&#09Does not activate the window.
See also[PyCWnd::ModifyStyleEx](PyCWnd.md#pycwndmodifystyleex)

#### MFC References


  - CWnd::ModifyStyle

#### Return Value
The result is true if the style was changed, or false if the style 

is already the same as requested and no change was made.

## [PyCWnd](#pycwnd).ModifyStyleEx

int = __ModifyStyleEx( *remove*  *, add*  *, flags* __ )
Modifies the extended style of a window.

#### Parameters


  -  *remove* : int

    Specifies extended window styles to be removed during style modification.

  -  *add* : int

    Specifies extended extended window styles to be added during style modification.

  -  *flags=0* : int

    Flags to be passed to SetWindowPos, or zero if SetWindowPos should not be called. The default is zero.

#### Comments
If nFlags is nonzero, ModifyStyleEx calls the Windows API function ::SetWindowPos and redraws the window by combining nFlags with the following four preset flags:
* SWP_NOSIZE&#09Retains the current size.
* SWP_NOMOVE&#09Retains the current position.
* SWP_NOZORDER&#09Retains the current Z order.
* SWP_NOACTIVATE&#09Does not activate the window.
See also[PyCWnd::ModifyStyle](PyCWnd.md#pycwndmodifystyle)

#### MFC References


  - CWnd::ModifyStyleEx

#### Return Value
The result is true if the style was changed, or false if the style 

is already the same as requested and no change was made.

## [PyCWnd](#pycwnd).MouseCaptured

int = __MouseCaptured(__ )
Returns 1 if the window has the mouse capture, else 0

## [PyCWnd](#pycwnd).MoveWindow

 __MoveWindow( *rect*  *, bRepaint* __ )
Move a window to a new location.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    The new location of the window, relative to the parent.

  -  *bRepaint=1* : int

    Indicates if the window should be repainted after the move.

#### MFC References


  - CWnd::MoveWindow

## [PyCWnd](#pycwnd).OnClose

int = __OnClose(__ )
Calls the default MFC OnClose handler.

#### See Also


  - [PyCWnd.OnClose](PyCWnd.md#pycwndonclose_virtual)virtual method

#### MFC References


  - CWnd::OnClose

## [PyCWnd.OnClose](#pycwnd)Virtual

 __OnClose(__ )
Called for the WM_CLOSE message.

#### Comments
The default calls DestroyWindow().  If you supply a handler, the default is not called.
The MFC base class is always called before the Python method.

#### See Also


  - [PyCWnd::OnClose](PyCWnd.md#pycwndonclose)

## [PyCWnd.OnCommand](#pycwnd)Virtual

 __OnCommand( *wparam*  *, lparam* __ )
Allows a Window to override the OnCommand handling.

#### Parameters


  -  *wparam* : int

    

  -  *lparam* : int

    

#### Comments
The base class method must be called manually via __PyCWnd::OnCommand__ . 

Failure to call the base implementation will prevent all Python command 

handlers (hooked via __PyCWnd::HookCommand__ ).

## [PyCWnd.OnCreate](#pycwnd)Virtual

 __OnCreate(__ )
Called for the WM_CREATE message.

#### Comments
The MFC implementation is always called before Python.

#### Return Value
The result is an integer indicating if the window should be created.

## [PyCWnd](#pycwnd).OnCtlColor

int = __OnCtlColor( *dc*  *, control*  *, type* __ )
Calls the default MFC OnCtlColor handler.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The dc

  -  *control* : __PyCWin__ 

    The control that want's it's color changed

  -  *type* : int

    Type of control

#### See Also


  - [PyCWnd.OnCtlColor](PyCWnd.md#pycwndonctlcolor_virtual)virtual method

#### MFC References


  - CWnd::OnCtlColor

## [PyCWnd.OnCtlColor](#pycwnd)Virtual

 __OnCtlColor(__ )
Called for the WM_CTLCOLOR message.

#### Comments
Setup dc to paint the control pWnd of type nCtlColor.
The default calls OnCtlColor().  If you supply a handler, the default is not called.

#### See Also


  - [PyCWnd::OnCtlColor](PyCWnd.md#pycwndonctlcolor)

#### Return Value
Handle of the brush to paint the control's background.

## [PyCWnd](#pycwnd).OnEraseBkgnd

int = __OnEraseBkgnd( *dc* __ )
Calls the default MFC OnEraseBkgnd handler.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The dc

#### See Also


  - [PyCWnd.OnEraseBkgnd](PyCWnd.md#pycwndonerasebkgnd_virtual)virtual method

#### MFC References


  - CWnd::OnEraseBkgnd

## [PyCWnd.OnEraseBkgnd](#pycwnd)Virtual

 __OnEraseBkgnd( *dc* __ )
Called for the WN_ERASEBACKGROUND message.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The device context.

#### See Also


  - [PyCWnd::OnEraseBkgnd](PyCWnd.md#pycwndonerasebkgnd)

#### Return Value
Nonzero if it erases the background; otherwise 0.

## [PyCWnd.OnMDIActivate](#pycwnd)Virtual

 __OnMDIActivate( *bActivate*  *, wndActivate*  *, wndDeactivate* __ )


#### Parameters


  -  *bActivate* : int

    

  -  *wndActivate* :[PyCWnd](#pycwnd)

    

  -  *wndDeactivate* :[PyCWnd](#pycwnd)

    

#### Comments
The MFC implementation is always called before this.

## [PyCWnd](#pycwnd).OnMouseActivate

int = __OnMouseActivate( *wnd*  *, hittest*  *, message* __ )
Calls the base MFC OnMouseActivate function.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    

  -  *hittest* : int

    

  -  *message* : int

    

#### See Also


  - [PyCWnd.OnMouseActivate](PyCWnd.md#pycwndonmouseactivate_virtual)virtual method

## [PyCWnd.OnMouseActivate](#pycwnd)Virtual

 __OnMouseActivate( *wndDesktop*  *, hitTest*  *, msg* __ )
Called when the mouse is used to activate a window.

#### Parameters


  -  *wndDesktop* :[PyCWnd](#pycwnd)

    

  -  *hitTest* : int

    

  -  *msg* : int

    

#### See Also


  - [PyCWnd::OnMouseActivate](PyCWnd.md#pycwndonmouseactivate)

## [PyCWnd.OnNcCalcSize](#pycwnd)Virtual

 __OnNcCalcSize(__ )
Called for the WM_NCCALCSIZE message.

## [PyCWnd](#pycwnd).OnNcHitTest

int = __OnNcHitTest( *x, y* __ )
Calls the base MFC OnNcHitTest function.

#### Parameters


  -  *x, y* : int, int

    The point

#### See Also


  - [PyCWnd.OnNcHitTest](PyCWnd.md#pycwndonnchittest_virtual)virtual method

## [PyCWnd.OnNcHitTest](#pycwnd)Virtual

 __OnNcHitTest( *x,y* __ )
Called for the WM_NCHITTEST message.

#### Parameters


  -  *x,y* : int, int

    The point to test.

#### See Also


  - [PyCWnd::OnNcHitTest](PyCWnd.md#pycwndonnchittest)

## [PyCWnd](#pycwnd).OnPaint

int = __OnPaint(__ )
Calls the default MFC OnPaint handler.

#### See Also


  - [PyCWnd.OnPaint](PyCWnd.md#pycwndonpaint_virtual)virtual method

#### MFC References


  - CWnd::OnEraseBkgnd

## [PyCWnd.OnPaint](#pycwnd)Virtual

 __OnPaint(__ )
Default message handler.

#### See Also


  -  __Wnd::OnPaint__ 

## [PyCWnd.OnPaletteChanged](#pycwnd)Virtual

 __OnPaletteChanged( *focusWnd* __ )
Called to allow windows that use a color palette to realize their logical palettes and update their client areas.

#### Parameters


  -  *focusWnd* :[PyCWnd](#pycwnd)

    The window that caused the system palette to change.

## [PyCWnd.OnPaletteIsChanging](#pycwnd)Virtual

 __OnPaletteIsChanging( *realizeWnd* __ )
Informs other applications when an application is going to realize its logical palette.

#### Parameters


  -  *realizeWnd* :[PyCWnd](#pycwnd)

    Specifies the window that is about to realize its logical palette.

#### Comments
The MFC base class is always called before the Python method.

## [PyCWnd](#pycwnd).OnQueryDragIcon

int = __OnQueryDragIcon(__ )
Calls the default MFC OnQueryDragIcon handler.

#### See Also


  - [PyCWnd.OnQueryDragIcon](PyCWnd.md#pycwndonquerydragicon_virtual)virtual method

## [PyCWnd.OnQueryDragIcon](#pycwnd)Virtual

 __OnQueryDragIcon(__ )
Called for the WM_QUERYDRAGICON message.

#### See Also


  - [PyCWnd::OnQueryDragIcon](PyCWnd.md#pycwndonquerydragicon)

#### Return Value
The result is an integer containing a HCURSOR for the icon.

## [PyCWnd](#pycwnd).OnQueryNewPalette

int = __OnQueryNewPalette(__ )
Calls the underlying MFC OnQueryNewPalette method.

#### See Also


  - [PyCWnd.OnQueryNewPalette](PyCWnd.md#pycwndonquerynewpalette_virtual)virtual method

## [PyCWnd.OnQueryNewPalette](#pycwnd)Virtual

 __OnQueryNewPalette(__ )
Informs the window it is about to receive input focus, and shoudl realize its logical palette.

#### Comments
The base class method must be called manually via __PyCScrollView::OnQueryNewPalette__ 

#### See Also


  - [PyCWnd::OnQueryNewPalette](PyCWnd.md#pycwndonquerynewpalette)

## [PyCWnd](#pycwnd).OnSetCursor

int = __OnSetCursor( *wnd*  *, hittest*  *, message* __ )
Calls the base MFC OnSetCursor function.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    

  -  *hittest* : int

    

  -  *message* : int

    

#### See Also


  - [PyCWnd.OnSetCursor](PyCWnd.md#pycwndonsetcursor_virtual)virtual method

## [PyCWnd.OnSetCursor](#pycwnd)Virtual

 __OnSetCursor( *wnd*  *, hitTest*  *, msg* __ )
Called for the WM_SETCURSOR message.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    

  -  *hitTest* : int

    

  -  *msg* : int

    

#### See Also


  - [PyCWnd::OnSetCursor](PyCWnd.md#pycwndonsetcursor)

## [PyCWnd.OnSysColorChange](#pycwnd)Virtual

 __OnSysColorChange(__ )
Called for all top-level windows when a change is made in the system color setting.

#### Comments
The MFC base class is always called before the Python method.

## [PyCWnd.OnTimer](#pycwnd)Virtual

 __OnTimer( *nIDEvent* __ )
Called for the WM_TIMER message.

#### Parameters


  -  *nIDEvent* : int

    Specifies the identifier of the timer.

## [PyCWnd.OnWinIniChange](#pycwnd)Virtual

 __OnWinIniChange( *section* __ )
Called when the system configuration changes.

#### Parameters


  -  *section* : string

    The section which changed.

#### Comments
The MFC base class is always called before the Python method.

## [PyCWnd](#pycwnd).OnWndMsg

(int,int) = __OnWndMsg( *msg*  *, wParam*  *, lParam* __ )
Calls the default MFC Window Message handler.

#### Parameters


  -  *msg* : int

    The message

  -  *wParam* : int

    The wParam for the message

  -  *lParam* : int

    The lParam for the message

#### MFC References


  - CWnd::OnWndMsg

#### Return Value
The return value is a tuple of (int, int), being the 

return value from the MFC function call, and the value of the 

lResult param.  Please see the MFC documentation for more details.

## [PyCWnd](#pycwnd).PostMessage

 __PostMessage( *idMessage*  *, wParam*  *, lParam* __ )
Post a message to the window.

#### Parameters


  -  *idMessage* : int

    The ID of the message to post.

  -  *wParam=0* : int

    The wParam for the message

  -  *lParam=0* : int

    The lParam for the message

#### MFC References


  - CWnd::PostMessage

## [PyCWnd](#pycwnd).PreCreateWindow

tuple = __PreCreateWindow( *createStruct* __ )
Calls the underlying MFC PreCreateWindow method.

#### Parameters


  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure.

#### See Also


  - [PyCWnd.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual)virtual method

## [PyCWnd.PreCreateWindow](#pycwnd)Virtual

 __PreCreateWindow( *CREATESTRUCT* __ )
Called by the framework before the creation of the Windows window attached to this View object.

#### Parameters


  -  *CREATESTRUCT* : tuple

    A tuple describing a CREATESTRUCT structure.

#### See Also


  - [PyCWnd::PreCreateWindow](PyCWnd.md#pycwndprecreatewindow)

## [PyCWnd.PreTranslateMessage](#pycwnd)Virtual

 __PreTranslateMessage( *msg* __ )
Allows a Window to override the PreTranslateMessage handling.

#### Parameters


  -  *msg* : tuple

    Built from a MSG structure using format "iiiii(ii)"

#### Return Value
The result should be a tuple of the same format as the msg param, 

in which case the MSG structure will be updated and TRUE returned 

from the C++ function.  If None is returned, the default handler 

is called.

## [PyCWnd](#pycwnd).PumpWaitingMessages

 __PumpWaitingMessages( *firstMsg*  *, lastMsg* __ )
Pump messages associate with a window.

#### Parameters


  -  *firstMsg* : int

    First message ID to process

  -  *lastMsg* : int

    First message ID to process

#### MFC References


  - CWnd::PeekMessage and DispatchMessage

## [PyCWnd](#pycwnd).RedrawWindow

 __RedrawWindow( *rect*  *, object*  *, flags* __ )
Updates the specified rectangle or region in the given window's client area.

#### Parameters


  -  *rect=None* : (left, top, right, bottom)

    A rect, or None

  -  *object=PyCRgn or None* : PyCRgn

    A region

  -  *flags=RDW_INVALIDATE | RDW_UPDATENOW | RDW_ERASE* : int

    

#### MFC References


  - CWnd::RedrawWindow

## [PyCWnd](#pycwnd).ReleaseCapture

 __ReleaseCapture(__ )
Releases the mouse capture for this window.  See[PyCWnd::SetCapture](PyCWnd.md#pycwndsetcapture).

## [PyCWnd](#pycwnd).ReleaseDC

 __ReleaseDC( *dc* __ )
Releases a device context, freeing it for use by other applications.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The DC to be released.

## [PyCWnd](#pycwnd).RepositionBars

 __RepositionBars( *idFirst*  *, idLast*  *, idLeftOver* __ )
Repositions the windows control bars.( UINT nIDFirst, UINT nIDLast, UINT nIDLeftOver, UINT nFlag = CWnd::reposDefault, LPRECT lpRectParam = NULL, LPCRECT lpRectClient = NULL, BOOL bStretch = TRUE );

#### Parameters


  -  *idFirst* : int

    The ID of the first control to reposition.

  -  *idLast* : int

    The ID of the last control to reposition.

  -  *idLeftOver* : int

    

## [PyCWnd](#pycwnd).RunModalLoop

int = __RunModalLoop( *flags* __ )
Begins a modal loop for the window.

#### Parameters


  -  *flags* : int

    

## [PyCWnd](#pycwnd).ScreenToClient

(left, top, right, bottom) or (x, y) = __ScreenToClient( *rect* __ )
Converts the screen coordinates of a given point or rectangle on the display to client coordinates.

#### Parameters


  -  *rect* : (left, top, right, bottom) or (x,y)

    The coordinates to convert.

#### Alternative Parameters


  -  *pnt* 

    The coordinates to convert.

#### MFC References


  - CWnd::ScreenToClient

#### Return Value
The result is the same size as the input argument.

## [PyCWnd](#pycwnd).SendMessage

 __SendMessage( *idMessage*  *, wParam*  *, lParam* __ )
Send a message to the window.

#### Parameters


  -  *idMessage* : int

    The ID of the message to send.

  -  *wParam=0* : int

    The wParam for the message

  -  *lParam=0* : int

    The lParam for the message

#### Alternative Parameters


  -  *idMessage* 

    The ID of the message to send.

  -  *ob* 

    A buffer whose size is passed in wParam, and address is passed in lParam

#### MFC References


  - CWnd::SendMessage

## [PyCWnd](#pycwnd).SendMessageToDescendants

 __SendMessageToDescendants( *idMessage*  *, wParam*  *, lParam*  *, bDeep* __ )
Send a message to all descendant windows.

#### Parameters


  -  *idMessage* : int

    The ID of the message to send.

  -  *wParam=0* : int

    The wParam for the message

  -  *lParam=0* : int

    The lParam for the message

  -  *bDeep=1* : int

    Indicates if the message should be recursively sent to all children

#### MFC References


  - CWnd::SendMessageToDescendants

## [PyCWnd](#pycwnd).SetActiveWindow

[PyCWnd](#pycwnd)= __SetActiveWindow(__ )
Sets the window active.  Returns the previously active window, or None.

#### Return Value
The result is the previous window with focus, or None.

## [PyCWnd](#pycwnd).SetCapture

 __SetCapture(__ )
Causes all subsequent mouse input to be sent to the window object regardless of the position of the cursor.

## [PyCWnd](#pycwnd).SetDlgItemText

 __SetDlgItemText( *idControl*  *, text* __ )
Sets the text for the child window or control with the specified ID.

#### Parameters


  -  *idControl* : int

    The Id of the control

  -  *text* : string

    The new text

#### MFC References


  - CWnd::SetDlgItemText

## [PyCWnd](#pycwnd).SetFocus

 __SetFocus(__ )
Claims the input focus.  The object that previously had the focus loses it.

## [PyCWnd](#pycwnd).SetFont

 __SetFont( *font*  *, bRedraw* __ )
Sets the window's current font to the specified font.

#### Parameters


  -  *font* :[PyCFont](#pycfont)

    The new font to use.

  -  *bRedraw=1* : int

    If TRUE, redraw the window.

## [PyCWnd](#pycwnd).SetForegroundWindow

 __SetForegroundWindow(__ )
Puts the window into the foreground and activates the window.

## [PyCWnd](#pycwnd).SetIcon

HICON = __SetIcon(__ )
Calls the underlying MFC SetIcon method.

## [PyCWnd](#pycwnd).SetMenu

 __SetMenu( *menuObj* __ )
Sets the menu for a window.

#### Parameters


  -  *menuObj* : PyCMenu

    The menu object to set, or None to remove the window.

## [PyCWnd](#pycwnd).SetRedraw

 __SetRedraw( *bState* __ )
Allows changes to be redrawn or to prevent changes from being redrawn.

#### Parameters


  -  *bState=1* : int

    Specifies the state of the redraw flag.

#### MFC References


  - CWnd::SetRedraw

## [PyCWnd](#pycwnd).SetScrollInfo

int = __SetScrollInfo( *nBar*  *, ScrollInfo*  *, redraw* __ )
Set information about a scroll bar

#### Parameters


  -  *nBar* : int

    The scroll bar to examine.  Can be one of win32con.SB_BOTH, win32con.SB_VERT or win32con.SB_HORZ

  -  *ScrollInfo* :[SCROLLINFO tuple](SCROLLINFO.md#scrollinfotuple)

    The information to set

  -  *redraw=1* : int

    A flag indicating if the scrollbar should be re-drawn.

## [PyCWnd](#pycwnd).SetScrollPos

int = __SetScrollPos( *nBar*  *, nPos*  *, redraw* __ )
Sets the current position of the scroll box of a scroll bar.

#### Parameters


  -  *nBar* : int

    The scroll bar to set.  Can be one of win32con.SB_VERT or win32con.SB_HORZ

  -  *nPos* : int

    The new position

  -  *redraw=1* : int

    A flag indicating if the scrollbar should be redrawn.

## [PyCWnd](#pycwnd).SetTimer

int = __SetTimer( *idEvent*  *, elapse* __ )
Installs a system timer

#### Parameters


  -  *idEvent* : int

    The ID of the event

  -  *elapse* : int

    How often the timer should fire.

#### MFC References


  - CWnd::SetTimer

## [PyCWnd](#pycwnd).SetWindowPlacement

 __SetWindowPlacement( *placement* __ )
Sets the windows placement

#### Parameters


  -  *placement* : (tuple)

    A tuple representing the WINDOWPLACEMENT structure.

#### MFC References


  - CWnd::SetWindowPlacement

## [PyCWnd](#pycwnd).SetWindowPos

 __SetWindowPos( *hWndInsertAfter*  *, position*  *, flags* __ )
Sets the windows position information

#### Parameters


  -  *hWndInsertAfter* : int

    A hwnd, else one of the win32con.HWND_* constants.

  -  *position* : (x,y,cx,cy)

    The new position of the window.

  -  *flags* : int

    Window positioning flags.

#### MFC References


  - CWnd::SetWindowPos

## [PyCWnd](#pycwnd).SetWindowText

 __SetWindowText( *text* __ )
Sets the window's text.

#### Parameters


  -  *text* : string

    The windows text.

#### MFC References


  - CWnd::SetWindowText

## [PyCWnd](#pycwnd).ShowCaret

 __ShowCaret(__ )
Shows the caret

#### Comments
See also[PyCWnd::HideCaret](PyCWnd.md#pycwndhidecaret)

## [PyCWnd](#pycwnd).ShowScrollBar

 __ShowScrollBar( *nBar*  *, bShow* __ )
Shows or hides a scroll bar. 

An application should not call ShowScrollBar to hide a scroll bar while processing a scroll-bar notification message.

#### Parameters


  -  *nBar* : int

    Specifies whether the scroll bar is a control or part of a window's nonclient area. 

If it is part of the nonclient area, nBar also indicates whether the scroll bar is positioned horizontally, vertically, or both. 

It must be one of win32con.SB_BOTH, win32con.SB_HORZ or win32con.SB_VERT.

  -  *bShow=1* : int

    Indicates if the scroll bar should be shown or hidden.

#### MFC References


  - CWnd::ShowScrollBar

## [PyCWnd](#pycwnd).ShowWindow

int = __ShowWindow( *style* __ )
Sets the visibility state of the window.

#### Parameters


  -  *style=win32con.SW_SHOWNORMAL* : int

    Specifies how the window is to be shown. 

It must be one of win32con.SW_HIDE, win32con.SW_MINIMIZE, win32con.SW_RESTORE, win32con.SW_SHOW, win32con.SW_SHOWMAXIMIZED 

win32con.SW_SHOWMINIMIZED, win32con.SW_SHOWMINNOACTIVE, win32con.SW_SHOWNA, win32con.SW_SHOWNOACTIVATE,  or win32con.SW_SHOWNORMAL

#### MFC References


  - CWnd::ShowWindow

#### Return Value
Returns TRUE is the window was previously visible.

## [PyCWnd](#pycwnd).UnlockWindowUpdate

 __UnlockWindowUpdate(__ )
Unlocks a window that was locked with LockWindowUpdate

#### MFC References


  - CWnd::UnLockWindowUpdate

## [PyCWnd](#pycwnd).UpdateData

int = __UpdateData( *bSaveAndValidate* __ )
Initialises data in a dialog box, or to retrieves and validates dialog data. 

Returns nonzero if the operation is successful; otherwise 0. If bSaveAndValidate is TRUE, then a return value of nonzero means that the data is successfully validated.

#### Parameters


  -  *bSaveAndValidate=1* : int

    Flag that indicates whether dialog box is being initialized (FALSE) or data is being retrieved (TRUE).

#### MFC References


  - CWnd::UpdateData

## [PyCWnd](#pycwnd).UpdateDialogControls

int = __UpdateDialogControls( *pTarget*  *, disableIfNoHandler* __ )
Updates the state of dialog buttons and other controls in a dialog box or window that uses the __PyCCmdUI::HookCommandUpdate__ callback mechanism.

#### Parameters


  -  *pTarget* :[PyCCmdTarget](#pyccmdtarget)

    The main frame window of the application, and is used for routing update messages.

  -  *disableIfNoHandler* : int

    Flag that indicates whether a control that has no update handler should be automatically displayed as disabled.

## [PyCWnd](#pycwnd).UpdateWindow

 __UpdateWindow(__ )
Updates a window.  This forces a paint message to be sent to the window, if any part of the window is marked as invalid.