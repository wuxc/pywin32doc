# PyCControlBar

## PyCControlBar Object

A class which encapsulates an MFC __CControlBar__ .  Derived from a[PyCWnd](#pycwnd)object.

#### Methods


  - [CalcDynamicLayout](PyCControlBar.md#pyccontrolbarcalcdynamiclayout)

    The framework calls this member function to calculate the dimensions of a dynamic toolbar.&nbsp;

  - [CalcFixedLayout](PyCControlBar.md#pyccontrolbarcalcfixedlayout)

    Calculates the horizontal size of a control bar&nbsp;

  - [EnableDocking](PyCControlBar.md#pyccontrolbarenabledocking)

    Specifies whether the control bar supports docking and the sides of its parent window.&nbsp;

  - [EraseNonClient](PyCControlBar.md#pyccontrolbarerasenonclient)

    &nbsp;

  - [GetBarStyle](PyCControlBar.md#pyccontrolbargetbarstyle)

    Retrieves the control bar style settings.&nbsp;

  - [GetCount](PyCControlBar.md#pyccontrolbargetcount)

    Returns the number of non-HWND elements in the control bar.&nbsp;

  - [GetDockingFrame](PyCControlBar.md#pyccontrolbargetdockingframe)

    Returns the frame window to which a control bar is docked.&nbsp;

  - [IsFloating](PyCControlBar.md#pyccontrolbarisfloating)

    Returns a nonzero value if the control bar in question is a floating control bar.&nbsp;

  - [SetBarStyle](PyCControlBar.md#pyccontrolbarsetbarstyle)

    Modifies the control bar style settings.&nbsp;

  - [ShowWindow](PyCControlBar.md#pyccontrolbarshowwindow)

    Shows the window, and recalculates the toolbar layout.&nbsp;

#### Properties

  -  __[PyCFrameWnd](#pycframewnd)dockSite__ 
    Current dock site, if dockable

  -  __[PyCWnd](#pycwnd)dockBar__ 
    Current dock bar, if dockable

  -  __[PyCDockContext](#pycdockcontext)dockContext__ 
    Used during dragging

  -  __int dwStyle__ 
    creation style (used for layout)

  -  __int dwDockStyle__ 
    indicates how bar can be docked

## [PyCControlBar](#pyccontrolbar).CalcDynamicLayout

int = __CalcDynamicLayout( *length*  *, dwMode* __ )
The framework calls this member function to calculate the dimensions of a dynamic toolbar.

#### Parameters


  -  *length* : int

    The requested dimension of the control bar, either horizontal or vertical, depending on dwMode.

  -  *dwMode* : int

    A combination of flags.

## [PyCControlBar.CalcDynamicLayout](#pyccontrolbar)Virtual

 __CalcDynamicLayout(__ )
Override to augment control-bar size calculations.

#### Comments
The base implementation is not called if a handler exists.  This can be 

done via __CPythonControlBar::CalcDynamicLayout__ .

#### See Also


  -  __CPythonControlBar::CalcDynamicLayout__ 

## [PyCControlBar](#pyccontrolbar).CalcFixedLayout

int = __CalcFixedLayout( *bStretch*  *, bHorz* __ )
Calculates the horizontal size of a control bar

#### Parameters


  -  *bStretch* : int

    Indicates whether the bar should be stretched to the size of the frame. The bStretch parameter is nonzero when the bar is not a docking bar (not available for docking) and is 0 when it is docked or floating (available for docking).

  -  *bHorz* : int

    Indicates that the bar is horizontally or vertically oriented.

## [PyCControlBar.CalcFixedLayout](#pyccontrolbar)Virtual

 __CalcFixedLayout(__ )
Override to augment control-bar size calculations.

#### Comments
The base implementation is not called if a handler exists.  This can be 

done via __CPythonControlBar::CalcFixedLayout__ .

#### See Also


  -  __CPythonControlBar::CalcFixedLayout__ 

## [PyCControlBar](#pyccontrolbar).EnableDocking

 __EnableDocking( *style* __ )
pecifies whether the control bar supports docking and the sides of its parent window.

#### Parameters


  -  *style* : int

    Enables a control bar to be docked.

## [PyCControlBar](#pyccontrolbar).EraseNonClient

 __EraseNonClient(__ )


## [PyCControlBar](#pyccontrolbar).GetBarStyle

int = __GetBarStyle(__ )
Retrieves the control bar style settings.

## [PyCControlBar](#pyccontrolbar).GetCount

int = __GetCount(__ )
Returns the number of non-HWND elements in the control bar.

## [PyCControlBar](#pyccontrolbar).GetDockingFrame

[PyCFrameWnd](#pycframewnd)= __GetDockingFrame(__ )
Returns the frame window to which a control bar is docked.

## [PyCControlBar](#pyccontrolbar).IsFloating

int = __IsFloating(__ )
Returns a nonzero value if the control bar in question is a floating control bar.

## [PyCControlBar.OnBarStyleChange](#pyccontrolbar)Virtual

 __OnBarStyleChange(__ )
Override to augment control-bar size calculations.

#### Comments
The base implementation is not called if a handler exists.  This can be 

done via __CPythonControlBar::OnBarStyleChange__ .

## [PyCControlBar.OnUpdateCmdUI](#pyccontrolbar)Virtual

 __OnUpdateCmdUI( *frame*  *, bDisableIsNoHandler* __ )


#### Parameters


  -  *frame* :[PyCFrameWnd](#pycframewnd)

    

  -  *bDisableIsNoHandler* : int

    

## [PyCControlBar](#pyccontrolbar).SetBarStyle

 __SetBarStyle( *style* __ )
Modifies the control bar style settings.

#### Parameters


  -  *style* : int

    The new style

## [PyCControlBar](#pyccontrolbar).ShowWindow

int = __ShowWindow(__ )
Shows the toolbar, and recalculates the button layout.

#### Comments
This method is provided for convenience.  For further details, see[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow)and[PyCFrameWnd::RecalcLayout](PyCFrameWnd.md#pycframewndrecalclayout)

#### Return Value
The return value is that returned from[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow)