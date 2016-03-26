# PyCColorDialog


## PyCColorDialog Object

A class which encapsulates an MFC CColorDialog object\.  Derived from a [PyCDialog](PyCDialog.md) object\.

#### Methods

  - [GetColor](PyCColorDialog.md#pyccolordialoggetcolor)

    Determines the selected color\.&nbsp;

  - [DoModal](PyCColorDialog.md#pyccolordialogdomodal)

    Displays a dialog and allows the user to make a selection\.&nbsp;

  - [GetSavedCustomColors](PyCColorDialog.md#pyccolordialoggetsavedcustomcolors)

    Returns the saved custom colors\.&nbsp;

  - [SetCurrentColor](PyCColorDialog.md#pyccolordialogsetcurrentcolor)

    Sets the currently selected color\.&nbsp;

  - [SetCustomColors](PyCColorDialog.md#pyccolordialogsetcustomcolors)

    Sets one or more custom colors&nbsp;

  - [GetCustomColors](PyCColorDialog.md#pyccolordialoggetcustomcolors)

    Gets the currently defined custom colors\.&nbsp;




## [PyCColorDialog](PyCColorDialog.md#pyccolordialog)\.DoModal

int = DoModal\(\)
Displays a dialog and allows the user to make a selection\.

#### MFC References

  - CColorDialog::DoModal


## [PyCColorDialog](PyCColorDialog.md#pyccolordialog)\.GetColor

int = GetColor\(\)
Determines the selected color\.

#### MFC References

  - CColorDialog::GetColor


## [PyCColorDialog](PyCColorDialog.md#pyccolordialog)\.GetCustomColors

\(int,\.\.\.\) = GetCustomColors\(\)
Gets the 16 currently defined custom colors


## [PyCColorDialog](PyCColorDialog.md#pyccolordialog)\.GetSavedCustomColors

int = GetSavedCustomColors\(\)
Returns the saved custom colors\.

#### MFC References

  - CColorDialog::GetSavedCustomColors


## [PyCColorDialog](PyCColorDialog.md#pyccolordialog)\.SetCurrentColor

SetCurrentColor\(color\)
Sets the currently selected color\.

#### Parameters

  - color : int

    The color to set\.

#### MFC References

  - CColorDialog::SetCurrentColor


## [PyCColorDialog](PyCColorDialog.md#pyccolordialog)\.SetCustomColors

SetCustomColors\(\)
Sets one or more custom colors