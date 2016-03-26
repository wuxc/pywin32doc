# PyCDialog

## PyCDialog Object

A class which encapsulates an MFC CDialog object\.  Derived from a[PyCWnd](#pycwnd)object\.

#### Methods


  - [CreateWindow](PyCDialog.md#pycdialogcreatewindow)

    Creates a modless window for the dialog\.&nbsp;

  - [DoModal](PyCDialog.md#pycdialogdomodal)

    Creates a modal window for the dialog\.&nbsp;

  - [EndDialog](PyCDialog.md#pycdialogenddialog)

    Closes a modal dialog\.&nbsp;

  - [GotoDlgCtrl](PyCDialog.md#pycdialoggotodlgctrl)

    Sets focus to a specific control\.&nbsp;

  - [MapDialogRect](PyCDialog.md#pycdialogmapdialogrect)

    Converts the dialog-box units of a rectangle to screen units\.&nbsp;

  - [OnCancel](PyCDialog.md#pycdialogoncancel)

    Calls the default MFC OnCancel handler\.&nbsp;

  - [OnOK](PyCDialog.md#pycdialogonok)

    Calls the default MFC OnOK handler\.&nbsp;

  - [OnInitDialog](PyCDialog.md#pycdialogoninitdialog)

    Calls the default MFC OnInitDialog handler\. 

sentinel&nbsp;


## [PyCDialog](#pycdialog)\.CreateWindow

 **CreateWindow\( *obParent* ** \)
Create a modeless window for the dialog box\.

#### Parameters


  -  *obParent\=None* :[PyCWnd](#pycwnd)

    The parent window for the new window

#### MFC References


  - CDialog::CreateIndirect

## [PyCDialog](#pycdialog)\.DoModal

int \= **DoModal\(** \)
Create a modal window for the dialog box\.

#### MFC References


  - CDialog::DoModal

#### Return Value
The return value from the dialog\.  This is the value passed to[PyCDialog::EndDialog](PyCDialog.md#pycdialogenddialog)\.

## [PyCDialog](#pycdialog)\.EndDialog

 **EndDialog\( *result* ** \)
Ends a modal dialog box\.

#### Parameters


  -  *result* : int

    The value to be returned by the[PyCDialog::DoModal](PyCDialog.md#pycdialogdomodal)method\.

#### MFC References


  - CDialog::EndDialog

## [PyCDialog](#pycdialog)\.GotoDlgCtrl

 **GotoDlgCtrl\( *control* ** \)
Moves the focus to the specified control in the dialog box\.

#### Parameters


  -  *control* :[PyCWnd](#pycwnd)

    The control to get the focus\.

## [PyCDialog](#pycdialog)\.MapDialogRect

\(left, top, right, bottom\) \= **MapDialogRect\( *rect* ** \)
Converts the dialog-box units of a rectangle to screen units\.

#### Parameters


  -  *rect* : \(left, top, right, bottom\)

    The rect to be converted

## [PyCDialog](#pycdialog)\.OnCancel

 **OnCancel\(** \)
Calls the default MFC OnCancel handler\.

#### See Also


  - [PyCDialog\.OnCancel](PyCDialog.md#pycdialogoncancel_virtual)virtual method

## [PyCDialog\.OnCancel](#pycdialog)Virtual

 **OnCancel\(** \)
Called by the MFC architecture when the user selects the Cancel button\.

#### Comments
The procedure is expected to dismiss the window with the[PyCDialog::EndDialog](PyCDialog.md#pycdialogenddialog)method\. 

The base implementation \(which dismisses the dialog\) is not called if a handler exists\.  This can be 

done via[PyCDialog::OnCancel](PyCDialog.md#pycdialogoncancel)\.

#### See Also


  - [PyCDialog::OnCancel](PyCDialog.md#pycdialogoncancel)

## [PyCDialog](#pycdialog)\.OnInitDialog

int \= **OnInitDialog\(** \)
Calls the default MFC OnInitDialog handler\.

#### See Also


  - [PyCDialog\.OnInitDialog](PyCDialog.md#pycdialogoninitdialog_virtual)virtual method

## [PyCDialog\.OnInitDialog](#pycdialog)Virtual

 **OnInitDialog\(** \)
Override to augment dialog-box initialization\.

#### Comments
The base implementation is not called if a handler exists\.  This can be 

done via[PyCDialog::OnInitDialog](PyCDialog.md#pycdialogoninitdialog)\.

#### See Also


  - [PyCDialog::OnInitDialog](PyCDialog.md#pycdialogoninitdialog)

#### Return Value
Specifies whether the application has set the input focus to 

one of the controls in the dialog box\. If OnInitDialog returns 

nonzero, Windows sets the input focus to the first control 

in the dialog box\. The application can return 0/None only if 

it has explicitly set the input focus to one of the controls in the 

dialog box\.

## [PyCDialog](#pycdialog)\.OnOK

 **OnOK\(** \)
Calls the default MFC OnOK handler\.

#### See Also


  - [PyCDialog\.OnOK](PyCDialog.md#pycdialogonok_virtual)virtual method

## [PyCDialog\.OnOK](#pycdialog)Virtual

 **OnOK\(** \)
Called by the MFC architecture when the user selects the OK button\.

#### Comments
The procedure is expected to dismiss the window with the[PyCDialog::EndDialog](PyCDialog.md#pycdialogenddialog)method\. 

The base implementation \(which dismisses the dialog\) is not called if a handler exists\.  This can be 

done via[PyCDialog::OnOK](PyCDialog.md#pycdialogonok)\.

#### See Also


  - [PyCDialog::OnOK](PyCDialog.md#pycdialogonok)