# PyCControlBar

## PyCControlBar Object

A class which encapsulates an MFC **CControlBar** \.  Derived from a[PyCWnd](#pycwnd)object\.

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

  -  **[PyCFrameWnd](#pycframewnd)dockSite** 
    Current dock site, if dockable

  -  **[PyCWnd](#pycwnd)dockBar** 
    Current dock bar, if dockable

  -  **[PyCDockContext](#pycdockcontext)dockContext** 
    Used during dragging

  -  **int dwStyle** 
    creation style \(used for layout\)

  -  **int dwDockStyle** 
    indicates how bar can be docked

## [PyCControlBar](#pyccontrolbar)\.CalcDynamicLayout

int \= **CalcDynamicLayout\( *length*  *, dwMode* ** \)
The framework calls this member function to calculate the dimensions of a dynamic toolbar\.

#### Parameters


  -  *length* : int

    The requested dimension of the control bar, either horizontal or vertical, depending on dwMode\.

  -  *dwMode* : int

    A combination of flags\.

## [PyCControlBar\.CalcDynamicLayout](#pyccontrolbar)Virtual

 **CalcDynamicLayout\(** \)
Override to augment control-bar size calculations\.

#### Comments
The base implementation is not called if a handler exists\.  This can be 

done via **CPythonControlBar::CalcDynamicLayout** \.

#### See Also


  -  **CPythonControlBar::CalcDynamicLayout** 

## [PyCControlBar](#pyccontrolbar)\.CalcFixedLayout

int \= **CalcFixedLayout\( *bStretch*  *, bHorz* ** \)
Calculates the horizontal size of a control bar

#### Parameters


  -  *bStretch* : int

    Indicates whether the bar should be stretched to the size of the frame\. The bStretch parameter is nonzero when the bar is not a docking bar \(not available for docking\) and is 0 when it is docked or floating \(available for docking\)\.

  -  *bHorz* : int

    Indicates that the bar is horizontally or vertically oriented\.

## [PyCControlBar\.CalcFixedLayout](#pyccontrolbar)Virtual

 **CalcFixedLayout\(** \)
Override to augment control-bar size calculations\.

#### Comments
The base implementation is not called if a handler exists\.  This can be 

done via **CPythonControlBar::CalcFixedLayout** \.

#### See Also


  -  **CPythonControlBar::CalcFixedLayout** 

## [PyCControlBar](#pyccontrolbar)\.EnableDocking

 **EnableDocking\( *style* ** \)
pecifies whether the control bar supports docking and the sides of its parent window\.

#### Parameters


  -  *style* : int

    Enables a control bar to be docked\.

## [PyCControlBar](#pyccontrolbar)\.EraseNonClient

 **EraseNonClient\(** \)


## [PyCControlBar](#pyccontrolbar)\.GetBarStyle

int \= **GetBarStyle\(** \)
Retrieves the control bar style settings\.

## [PyCControlBar](#pyccontrolbar)\.GetCount

int \= **GetCount\(** \)
Returns the number of non-HWND elements in the control bar\.

## [PyCControlBar](#pyccontrolbar)\.GetDockingFrame

[PyCFrameWnd](#pycframewnd)\= **GetDockingFrame\(** \)
Returns the frame window to which a control bar is docked\.

## [PyCControlBar](#pyccontrolbar)\.IsFloating

int \= **IsFloating\(** \)
Returns a nonzero value if the control bar in question is a floating control bar\.

## [PyCControlBar\.OnBarStyleChange](#pyccontrolbar)Virtual

 **OnBarStyleChange\(** \)
Override to augment control-bar size calculations\.

#### Comments
The base implementation is not called if a handler exists\.  This can be 

done via **CPythonControlBar::OnBarStyleChange** \.

## [PyCControlBar\.OnUpdateCmdUI](#pyccontrolbar)Virtual

 **OnUpdateCmdUI\( *frame*  *, bDisableIsNoHandler* ** \)


#### Parameters


  -  *frame* :[PyCFrameWnd](#pycframewnd)

    

  -  *bDisableIsNoHandler* : int

    

## [PyCControlBar](#pyccontrolbar)\.SetBarStyle

 **SetBarStyle\( *style* ** \)
Modifies the control bar style settings\.

#### Parameters


  -  *style* : int

    The new style

## [PyCControlBar](#pyccontrolbar)\.ShowWindow

int \= **ShowWindow\(** \)
Shows the toolbar, and recalculates the button layout\.

#### Comments
This method is provided for convenience\.  For further details, see[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow)and[PyCFrameWnd::RecalcLayout](PyCFrameWnd.md#pycframewndrecalclayout)

#### Return Value
The return value is that returned from[PyCWnd::ShowWindow](PyCWnd.md#pycwndshowwindow)