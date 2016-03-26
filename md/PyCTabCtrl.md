# PyCTabCtrl

## PyCTabCtrl Object

A class which encapsulates an MFC CTabCtrl object.  Derived from a[PyCWnd](#pycwnd)object.

#### Methods


  - [GetCurSel](PyCTabCtrl.md#pyctabctrlgetcursel)

    Gets the current selection of a tab control.&nbsp;

  - [GetItemCountl](PyCTabCtrl.md#pyctabctrlgetitemcountl)

    Returns the number of tabs in the control.&nbsp;

  - [SetCurSel](PyCTabCtrl.md#pyctabctrlsetcursel)

    Sets the current selection of a tab control.&nbsp;

## [PyCTabCtrl](#pyctabctrl).GetCurSel

int = __GetCurSel(__ )
Gets the current selection of a tab control.

#### Return Value
The zero-based index of the currently selected item, or -1 if no selection.

## [PyCTabCtrl](#pyctabctrl).GetItemCountl

int = __GetItemCountl(__ )
Returns the number of tabs in the control.

## [PyCTabCtrl](#pyctabctrl).SetCurSel

int = __SetCurSel( *index* __ )
Sets the current selection of a tab control.

#### Parameters


  -  *index* : int

    The index of the tab to set current.

#### Return Value
The zero-based index of the previously selected item.