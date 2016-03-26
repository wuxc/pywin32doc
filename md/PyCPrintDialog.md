# PyCPrintDialog

## PyCPrintDialog Object

An object which encapsulates an MFC CPrintDialog object\.


## [PyCPrintDialog\.OnCancel](#pycprintdialog)Virtual

 **OnCancel\(** \)
Called by the MFC architecture when the user selects the Cancel button\.

#### Comments
The procedure is expected to dismiss the window with the **PyCPrintDialog::EndDialog** method\. 

The base implementation \(which dismisses the dialog\) is not called if a handler exists\.  This can be 

done via **PyCPrintDialog::OnCancel** \.

#### See Also


  - [PyCDialog::OnCancel](PyCDialog.md#pycdialogoncancel)

## [PyCPrintDialog\.OnOK](#pycprintdialog)Virtual

 **OnOK\(** \)
Called by the MFC architecture when the user selects the OK button\.

#### Comments
The procedure is expected to dismiss the window with the **PyCPrintDialog::EndDialog** method\. 

The base implementation \(which dismisses the dialog\) is not called if a handler exists\.  This can be 

done via **PyCPrintDialog::OnOK** \.

#### See Also


  -  **PyCDialogDialog::OnOK** 