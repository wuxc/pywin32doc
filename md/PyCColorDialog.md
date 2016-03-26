# PyCColorDialog

## PyCColorDialog Object

A class which encapsulates an MFC CColorDialog object.  Derived from a[PyCDialog](#pycdialog)object.

#### Methods


  - [GetColor](PyCColorDialog.md#pyccolordialoggetcolor)

    Determines the selected color.&nbsp;

  - [DoModal](PyCColorDialog.md#pyccolordialogdomodal)

    Displays a dialog and allows the user to make a selection.&nbsp;

  - [GetSavedCustomColors](PyCColorDialog.md#pyccolordialoggetsavedcustomcolors)

    Returns the saved custom colors.&nbsp;

  - [SetCurrentColor](PyCColorDialog.md#pyccolordialogsetcurrentcolor)

    Sets the currently selected color.&nbsp;

  - [SetCustomColors](PyCColorDialog.md#pyccolordialogsetcustomcolors)

    Sets one or more custom colors&nbsp;

  - [GetCustomColors](PyCColorDialog.md#pyccolordialoggetcustomcolors)

    Gets the currently defined custom colors.&nbsp;


## [PyCColorDialog](#pyccolordialog).DoModal

int = __DoModal(__ )
Displays a dialog and allows the user to make a selection.

#### MFC References


  - CColorDialog::DoModal

## [PyCColorDialog](#pyccolordialog).GetColor

int = __GetColor(__ )
Determines the selected color.

#### MFC References


  - CColorDialog::GetColor

## [PyCColorDialog](#pyccolordialog).GetCustomColors

(int,...) = __GetCustomColors(__ )
Gets the 16 currently defined custom colors

## [PyCColorDialog](#pyccolordialog).GetSavedCustomColors

int = __GetSavedCustomColors(__ )
Returns the saved custom colors.

#### MFC References


  - CColorDialog::GetSavedCustomColors

## [PyCColorDialog](#pyccolordialog).SetCurrentColor

 __SetCurrentColor( *color* __ )
Sets the currently selected color.

#### Parameters


  -  *color* : int

    The color to set.

#### MFC References


  - CColorDialog::SetCurrentColor

## [PyCColorDialog](#pyccolordialog).SetCustomColors

 __SetCustomColors(__ )
Sets one or more custom colors