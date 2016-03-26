# PyCToolTipCtrl

## PyCToolTipCtrl Object

A windows tooltip control.  Encapsulates an MFC __CToolTipCtrl__ class.  Derived from[PyCControl](#pyccontrol).

#### Methods


  - [CreateWindow](PyCToolTipCtrl.md#pyctooltipctrlcreatewindow)

    Creates the window for a new progress bar object.&nbsp;

  - [UpdateTipText](PyCToolTipCtrl.md#pyctooltipctrlupdatetiptext)

    Update the tool tip text for a control's tools&nbsp;

  - [AddTool](PyCToolTipCtrl.md#pyctooltipctrladdtool)

    Adds a tool to tooltip control.&nbsp;

  - [SetMaxTipWidth](PyCToolTipCtrl.md#pyctooltipctrlsetmaxtipwidth)

    &nbsp;

## [PyCToolTipCtrl](#pyctooltipctrl).AddTool

 __AddTool( *wnd*  *, text*  *, rect*  *, id* __ )
Adds a tool to tooltip control.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    The window of the tool.

  -  *text* : string

    The text for the tool.

  -  *rect=None* : int, int, int, int

    The default rectangle

  -  *id* : int

    The id of the tool

## [PyCToolTipCtrl](#pyctooltipctrl).CreateWindow

 __CreateWindow( *parent*  *, style* __ )
Creates the actual control.

#### Parameters


  -  *parent* :[PyCWnd](#pycwnd)

    The parent window of the control.

  -  *style* : int

    The style for the control.

## [PyCToolTipCtrl](#pyctooltipctrl).SetMaxTipWidth

int = __SetMaxTipWidth( *width* __ )


#### Parameters


  -  *width* : int

    The new width

## [PyCToolTipCtrl](#pyctooltipctrl).UpdateTipText

 __UpdateTipText( *text*  *, wnd*  *, id* __ )
Update the tool tip text for a control's tools

#### Parameters


  -  *text* : string

    The text for the tool.

  -  *wnd* :[PyCWnd](#pycwnd)

    The window of the tool.

  -  *id* : int

    The id of the tool