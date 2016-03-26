# PyCPropertySheet

## PyCPropertySheet Object

A class which encapsulates an MFC CPropertySheet object.  Derived from a[PyCWnd](#pycwnd)object.

#### Methods


  - [AddPage](PyCPropertySheet.md#pycpropertysheetaddpage)

    Adds the supplied page with the rightmost tab in the property sheet.&nbsp;

  - [CreateWindow](PyCPropertySheet.md#pycpropertysheetcreatewindow)

    Displays the property sheet as a modeless dialog.&nbsp;

  - [DoModal](PyCPropertySheet.md#pycpropertysheetdomodal)

    Displays the property sheet as a modal dialog.&nbsp;

  - [EnableStackedTabs](PyCPropertySheet.md#pycpropertysheetenablestackedtabs)

    Enables or disables stacked tabs.&nbsp;

  - [EndDialog](PyCPropertySheet.md#pycpropertysheetenddialog)

    Closes the dialog, with the specified result.&nbsp;

  - [GetActiveIndex](PyCPropertySheet.md#pycpropertysheetgetactiveindex)

    Retrieves the index of the active page of the property sheet.&nbsp;

  - [GetActivePage](PyCPropertySheet.md#pycpropertysheetgetactivepage)

    Returns the currently active property page.&nbsp;

  - [GetPage](PyCPropertySheet.md#pycpropertysheetgetpage)

    Returns the specified property page.&nbsp;

  - [GetPageIndex](PyCPropertySheet.md#pycpropertysheetgetpageindex)

    Retrieves the index of the specified page of the property sheet.&nbsp;

  - [GetPageCount](PyCPropertySheet.md#pycpropertysheetgetpagecount)

    Returns the number of pages.&nbsp;

  - [GetTabCtrl](PyCPropertySheet.md#pycpropertysheetgettabctrl)

    Returns the tab control used by the sheet.&nbsp;

  - [OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog)

    Calls the default MFC OnInitDialog handler.&nbsp;

  - [PressButton](PyCPropertySheet.md#pycpropertysheetpressbutton)

    Simulates the choice of the specified button in a property sheet.&nbsp;

  - [RemovePage](PyCPropertySheet.md#pycpropertysheetremovepage)

    Removes the specified page from the sheet.&nbsp;

  - [SetActivePage](PyCPropertySheet.md#pycpropertysheetsetactivepage)

    Programmatically sets the active page object.&nbsp;

  - [SetTitle](PyCPropertySheet.md#pycpropertysheetsettitle)

    Sets the caption for the property sheet.&nbsp;

  - [SetFinishText](PyCPropertySheet.md#pycpropertysheetsetfinishtext)

    Sets the text for the Finish button&nbsp;

  - [SetWizardMode](PyCPropertySheet.md#pycpropertysheetsetwizardmode)

    Enables the wizard mode&nbsp;

  - [SetWizardButtons](PyCPropertySheet.md#pycpropertysheetsetwizardbuttons)

    Enables the wizard buttons&nbsp;

  - [SetPSHBit](PyCPropertySheet.md#pycpropertysheetsetpshbit)

    Sets (or clears) a bit in m_psh.dwFlags.&nbsp;

## [PyCPropertySheet](#pycpropertysheet).AddPage

 __AddPage( *page* __ )
Adds the supplied page with the rightmost tab in the property sheet.

#### Parameters


  -  *page* :[PyCPropertyPage](#pycpropertypage)

    The page to be added.

#### Comments
Add pages to the property sheet in the left-to-right order you want them to appear.

#### MFC References


  - PyCPropertySheet::AddPage

## [PyCPropertySheet](#pycpropertysheet).CreateWindow

 __CreateWindow( *parent*  *, style*  *, exStyle* __ )
Displays the property sheet as a modeless dialog.

#### Parameters


  -  *parent=None* :[PyCWnd](#pycwnd)

    The parent of the dialog.

  -  *style=WS_SYSMENU|WS_POPUP|WS_CAPTION|DS_MODALFRAME|WS_VISIBLE* : int

    The style for the window.

  -  *exStyle=WS_EX_DLGMODALFRAME* : int

    The extended style for the window.

## [PyCPropertySheet](#pycpropertysheet).DoModal

int = __DoModal(__ )
Displays the property sheet as a modal dialog.

## [PyCPropertySheet](#pycpropertysheet).EnableStackedTabs

[PyCPropertyPage](#pycpropertypage)= __EnableStackedTabs( *stacked* __ )
Enables or disables stacked tabs.

#### Parameters


  -  *stacked* : int

    A boolean flag

## [PyCPropertySheet](#pycpropertysheet).EndDialog

 __EndDialog( *result* __ )
Closes the dialog, with the specified result.

#### Parameters


  -  *result* : int

    The result to be returned by DoModal.

## [PyCPropertySheet](#pycpropertysheet).GetActiveIndex

int = __GetActiveIndex(__ )
Retrieves the index of the active page of the property sheet.

## [PyCPropertySheet](#pycpropertysheet).GetActivePage

[PyCPropertyPage](#pycpropertypage)= __GetActivePage(__ )
Returns the currently active property page.

#### MFC References


  - PyCPropertySheet::GetActivePage

## [PyCPropertySheet](#pycpropertysheet).GetPage

[PyCPropertyPage](#pycpropertypage)= __GetPage( *pageNo* __ )
Returns the specified property page.

#### Parameters


  -  *pageNo* : int

    The index of the page toretrieve.

#### MFC References


  - PyCPropertySheet::GetPage

## [PyCPropertySheet](#pycpropertysheet).GetPageCount

int = __GetPageCount(__ )
Returns the number of pages.

## [PyCPropertySheet](#pycpropertysheet).GetPageIndex

int = __GetPageIndex( *page* __ )
Retrieves the index of the specified page of the property sheet.

#### Parameters


  -  *page* :[PyCPropertyPage](#pycpropertypage)

    The page.

## [PyCPropertySheet](#pycpropertysheet).GetTabCtrl

[PyCTabCtrl](#pyctabctrl)= __GetTabCtrl(__ )
Returns the tab control used by the sheet.

## [PyCPropertySheet](#pycpropertysheet).OnInitDialog

int = __OnInitDialog(__ )
Calls the default MFC OnInitDialog handler.

#### See Also


  - [PyCPropertySheet.OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog_virtual)virtual method

## [PyCPropertySheet.OnInitDialog](#pycpropertysheet)Virtual

 __OnInitDialog(__ )
Override to augment dialog-box initialization.

#### Comments
The base implementation is not called if a handler exists.  This can be 

done via[PyCDialog::OnInitDialog](PyCDialog.md#pycdialogoninitdialog).

#### See Also


  - [PyCDialog::OnInitDialog](PyCDialog.md#pycdialogoninitdialog)

#### Return Value
Specifies whether the application has set the input focus to 

one of the controls in the dialog box. If OnInitDialog returns 

nonzero, Windows sets the input focus to the first control 

in the dialog box. The application can return 0/None only if 

it has explicitly set the input focus to one of the controls in the 

dialog box.

## [PyCPropertySheet.OnInitDialog](#pycpropertysheet)Virtual

 __OnInitDialog(__ )
Override to augment dialog-box initialization.

#### Comments
The base implementation is not called if a handler exists.  This can be 

done via[PyCPropertySheet::OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog).

#### See Also


  - [PyCPropertySheet::OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog)

#### Return Value
Specifies whether the application has set the input focus to 

one of the controls in the dialog box. If OnInitDialog returns 

nonzero, Windows sets the input focus to the first control 

in the dialog box. The application can return 0/None only if 

it has explicitly set the input focus to one of the controls in the 

dialog box.

## [PyCPropertySheet](#pycpropertysheet).PressButton

 __PressButton( *button* __ )
Simulates the choice of the specified button in a property sheet.

#### Parameters


  -  *button* : int

    The button to press

## [PyCPropertySheet](#pycpropertysheet).RemovePage

 __RemovePage( *offset* __ )
Removes the specified page from the sheet.

#### Parameters


  -  *offset* : int

    The page number to remove

#### Alternative Parameters


  -  *page* 

    The page to remove

## [PyCPropertySheet](#pycpropertysheet).SetActivePage

 __SetActivePage( *page* __ )
Programmatically sets the active page object.

#### Parameters


  -  *page* :[PyCPropertyPage](#pycpropertypage)

    The page.

## [PyCPropertySheet](#pycpropertysheet).SetFinishText

 __SetFinishText( *text* __ )
Sets the text for the Finish button

#### Parameters


  -  *text* : string

    The next for the button

## [PyCPropertySheet](#pycpropertysheet).SetPSHBit

 __SetPSHBit( *bitMask*  *, bitValue* __ )
Sets or clears a bit in m_psh.dwFlags

#### Parameters


  -  *bitMask* : int

    The PSH_* bit mask constant

  -  *bitValue* : int

    1 to set, 0 to clear

## [PyCPropertySheet](#pycpropertysheet).SetTitle

 __SetTitle( *title* __ )
Sets the caption for the property sheet.

#### Parameters


  -  *title* : string

    The new caption

## [PyCPropertySheet](#pycpropertysheet).SetWizardButtons

 __SetWizardButtons( *flags* __ )
Enables the wizard buttons

#### Parameters


  -  *flags* : int

    The wizard flags

## [PyCPropertySheet](#pycpropertysheet).SetWizardMode

 __SetWizardMode(__ )
Enables the wizard mode

## [PyCPropertySheet.WindowProc](#pycpropertysheet)Virtual

 __WindowProc(__ )
Default message handler.