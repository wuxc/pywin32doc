# PyCControlBar


## PyCControlBar Object

A class which encapsulates an MFC CControlBar

\.  Derived from a [PyCWnd](PyCWnd.md) object\.

#### Methods

  - [CalcDynamicLayout](PyCControlBar.md#pyccontrolbarcalcdynamiclayout)

    The framework calls this member function to calculate the dimensions of a dynamic toolbar\.&nbsp;

  - [CalcFixedLayout](PyCControlBar.md#pyccontrolbarcalcfixedlayout)

    Calculates the horizontal size of a control bar&nbsp;

  - [EnableDocking](PyCControlBar.md#pyccontrolbarenabledocking)

    Specifies whether the control bar supports docking and the sides of its parent window\.&nbsp;

  - [EraseNonClient](PyCControlBar.md#pyccontrolbarerasenonclient)

    &nbsp;

  - [GetBarStyle](PyCControlBar.md#pyccontrolbargetbarstyle)

    Retrieves the control bar style settings\.&nbsp;

  - [GetCount](PyCControlBar.md#pyccontrolbargetcount)

    Returns the number of non-HWND elements in the control bar\.&nbsp;

  - [GetDockingFrame](PyCControlBar.md#pyccontrolbargetdockingframe)

    Returns the frame window to which a control bar is docked\.&nbsp;

  - [IsFloating](PyCControlBar.md#pyccontrolbarisfloating)

    Returns a nonzero value if the control bar in question is a floating control bar\.&nbsp;

  - [SetBarStyle](PyCControlBar.md#pyccontrolbarsetbarstyle)

    Modifies the control bar style settings\.&nbsp;

  - [ShowWindow](PyCControlBar.md#pyccontrolbarshowwindow)

    Shows the window, and recalculates the toolbar layout\.&nbsp;

#### Properties

  - [PyCFrameWnd](PyCFrameWnd.md) dockSite

    Current dock site, if dockable

  - [PyCWnd](PyCWnd.md) dockBar

    Current dock bar, if dockable

  - [PyCDockContext](PyCDockContext.md) dockContext

    Used during dragging

  - int dwStyle

    creation style \(used for layout\)

  - int dwDockStyle

    indicates how bar can be docked


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.CalcDynamicLayout

int = CalcDynamicLayout\(length, dwMode

\)
The framework calls this member function to calculate the dimensions of a dynamic toolbar\.

#### Parameters

  - length : int

    The requested dimension of the control bar, either horizontal or vertical, depending on dwMode\.

  - dwMode : int

    A combination of flags\.


## [PyCControlBar\.CalcDynamicLayout](PyCControlBar.md#pyccontrolbar) Virtual

CalcDynamicLayout\(\)
Override to augment control-bar size calculations\.

#### Comments

The base implementation is not called if a handler exists\.  This can be 

done via CPythonControlBar::CalcDynamicLayout

\.

#### See Also

  - CPythonControlBar::CalcDynamicLayout




## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.CalcFixedLayout

int = CalcFixedLayout\(bStretch, bHorz

\)
Calculates the horizontal size of a control bar

#### Parameters

  - bStretch : int

    Indicates whether the bar should be stretched to the size of the frame\. The bStretch parameter is nonzero when the bar is not a docking bar \(not available for docking\) and is 0 when it is docked or floating \(available for docking\)\.

  - bHorz : int

    Indicates that the bar is horizontally or vertically oriented\.


## [PyCControlBar\.CalcFixedLayout](PyCControlBar.md#pyccontrolbar) Virtual

CalcFixedLayout\(\)
Override to augment control-bar size calculations\.

#### Comments

The base implementation is not called if a handler exists\.  This can be 

done via CPythonControlBar::CalcFixedLayout

\.

#### See Also

  - CPythonControlBar::CalcFixedLayout




## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.EnableDocking

EnableDocking\(style\)
pecifies whether the control bar supports docking and the sides of its parent window\.

#### Parameters

  - style : int

    Enables a control bar to be docked\.


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.EraseNonClient

EraseNonClient\(\)



## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.GetBarStyle

int = GetBarStyle\(\)
Retrieves the control bar style settings\.


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.GetCount

int = GetCount\(\)
Returns the number of non-HWND elements in the control bar\.


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.GetDockingFrame

[PyCFrameWnd](PyCFrameWnd.md) = GetDockingFrame\(\)
Returns the frame window to which a control bar is docked\.


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.IsFloating

int = IsFloating\(\)
Returns a nonzero value if the control bar in question is a floating control bar\.


## [PyCControlBar\.OnBarStyleChange](PyCControlBar.md#pyccontrolbar) Virtual

OnBarStyleChange\(\)
Override to augment control-bar size calculations\.

#### Comments

The base implementation is not called if a handler exists\.  This can be 

done via CPythonControlBar::OnBarStyleChange

\.


## [PyCControlBar\.OnUpdateCmdUI](PyCControlBar.md#pyccontrolbar) Virtual

OnUpdateCmdUI\(frame, bDisableIsNoHandler

\)

#### Parameters

  - frame : [PyCFrameWnd](PyCFrameWnd.md)

    

  - bDisableIsNoHandler : int

    


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.SetBarStyle

SetBarStyle\(style\)
Modifies the control bar style settings\.

#### Parameters

  - style : int

    The new style


## [PyCControlBar](PyCControlBar.md#pyccontrolbar)\.ShowWindow

int = ShowWindow\(\)
Shows the toolbar, and recalculates the button layout\.

#### Comments

This method is provided for convenience\.  For further details, see 

[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow) and [PyCFrameWnd::RecalcLayout](PyCFrameWnd.md#pycframewndrecalclayout)

#### Return Value
The return value is that returned from [PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow)