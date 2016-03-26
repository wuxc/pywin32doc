# PyCPrintDialog

## PyCPrintDialog Object

An object which encapsulates an MFC CPrintDialog object.


## [PyCPrintDialog.OnCancel](#pycprintdialog)Virtual

 __OnCancel(__ )
Called by the MFC architecture when the user selects the Cancel button.

#### Comments
The procedure is expected to dismiss the window with the __PyCPrintDialog::EndDialog__ method. 

The base implementation (which dismisses the dialog) is not called if a handler exists.  This can be 

done via __PyCPrintDialog::OnCancel__ .

#### See Also


  - [PyCDialog::OnCancel](PyCDialog.md#pycdialogoncancel)

## [PyCPrintDialog.OnOK](#pycprintdialog)Virtual

 __OnOK(__ )
Called by the MFC architecture when the user selects the OK button.

#### Comments
The procedure is expected to dismiss the window with the __PyCPrintDialog::EndDialog__ method. 

The base implementation (which dismisses the dialog) is not called if a handler exists.  This can be 

done via __PyCPrintDialog::OnOK__ .

#### See Also


  -  __PyCDialogDialog::OnOK__ 