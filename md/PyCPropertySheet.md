# PyCPropertySheet


## PyCPropertySheet Object

A class which encapsulates an MFC CPropertySheet object\.  Derived from a [PyCWnd](PyCWnd.md) object\.

#### Methods

  - [AddPage](PyCPropertySheet.md#pycpropertysheetaddpage)

    Adds the supplied page with the rightmost tab in the property sheet\.&nbsp;

  - [CreateWindow](PyCPropertySheet.md#pycpropertysheetcreatewindow)

    Displays the property sheet as a modeless dialog\.&nbsp;

  - [DoModal](PyCPropertySheet.md#pycpropertysheetdomodal)

    Displays the property sheet as a modal dialog\.&nbsp;

  - [EnableStackedTabs](PyCPropertySheet.md#pycpropertysheetenablestackedtabs)

    Enables or disables stacked tabs\.&nbsp;

  - [EndDialog](PyCPropertySheet.md#pycpropertysheetenddialog)

    Closes the dialog, with the specified result\.&nbsp;

  - [GetActiveIndex](PyCPropertySheet.md#pycpropertysheetgetactiveindex)

    Retrieves the index of the active page of the property sheet\.&nbsp;

  - [GetActivePage](PyCPropertySheet.md#pycpropertysheetgetactivepage)

    Returns the currently active property page\.&nbsp;

  - [GetPage](PyCPropertySheet.md#pycpropertysheetgetpage)

    Returns the specified property page\.&nbsp;

  - [GetPageIndex](PyCPropertySheet.md#pycpropertysheetgetpageindex)

    Retrieves the index of the specified page of the property sheet\.&nbsp;

  - [GetPageCount](PyCPropertySheet.md#pycpropertysheetgetpagecount)

    Returns the number of pages\.&nbsp;

  - [GetTabCtrl](PyCPropertySheet.md#pycpropertysheetgettabctrl)

    Returns the tab control used by the sheet\.&nbsp;

  - [OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog)

    Calls the default MFC OnInitDialog handler\.&nbsp;

  - [PressButton](PyCPropertySheet.md#pycpropertysheetpressbutton)

    Simulates the choice of the specified button in a property sheet\.&nbsp;

  - [RemovePage](PyCPropertySheet.md#pycpropertysheetremovepage)

    Removes the specified page from the sheet\.&nbsp;

  - [SetActivePage](PyCPropertySheet.md#pycpropertysheetsetactivepage)

    Programmatically sets the active page object\.&nbsp;

  - [SetTitle](PyCPropertySheet.md#pycpropertysheetsettitle)

    Sets the caption for the property sheet\.&nbsp;

  - [SetFinishText](PyCPropertySheet.md#pycpropertysheetsetfinishtext)

    Sets the text for the Finish button&nbsp;

  - [SetWizardMode](PyCPropertySheet.md#pycpropertysheetsetwizardmode)

    Enables the wizard mode&nbsp;

  - [SetWizardButtons](PyCPropertySheet.md#pycpropertysheetsetwizardbuttons)

    Enables the wizard buttons&nbsp;

  - [SetPSHBit](PyCPropertySheet.md#pycpropertysheetsetpshbit)

    Sets \(or clears\) a bit in m\_psh\.dwFlags\.&nbsp;


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.AddPage

AddPage\(page\)
Adds the supplied page with the rightmost tab in the property sheet\.

#### Parameters

  - page : [PyCPropertyPage](PyCPropertyPage.md)

    The page to be added\.

#### Comments

Add pages to the property sheet in the left-to-right order you want them to appear\.

#### MFC References

  - PyCPropertySheet::AddPage


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.CreateWindow

CreateWindow\(parent, style, exStyle\)
Displays the property sheet as a modeless dialog\.

#### Parameters

  - parent=None : [PyCWnd](PyCWnd.md)

    The parent of the dialog\.

  - style=WS\_SYSMENU|WS\_POPUP|WS\_CAPTION|DS\_MODALFRAME|WS\_VISIBLE : int

    The style for the window\.

  - exStyle=WS\_EX\_DLGMODALFRAME : int

    The extended style for the window\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.DoModal

int = DoModal\(\)
Displays the property sheet as a modal dialog\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.EnableStackedTabs

[PyCPropertyPage](PyCPropertyPage.md) = EnableStackedTabs\(stacked\)
Enables or disables stacked tabs\.

#### Parameters

  - stacked : int

    A boolean flag


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.EndDialog

EndDialog\(result\)
Closes the dialog, with the specified result\.

#### Parameters

  - result : int

    The result to be returned by DoModal\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.GetActiveIndex

int = GetActiveIndex\(\)
Retrieves the index of the active page of the property sheet\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.GetActivePage

[PyCPropertyPage](PyCPropertyPage.md) = GetActivePage\(\)
Returns the currently active property page\.

#### MFC References

  - PyCPropertySheet::GetActivePage


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.GetPage

[PyCPropertyPage](PyCPropertyPage.md) = GetPage\(pageNo\)
Returns the specified property page\.

#### Parameters

  - pageNo : int

    The index of the page toretrieve\.

#### MFC References

  - PyCPropertySheet::GetPage


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.GetPageCount

int = GetPageCount\(\)
Returns the number of pages\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.GetPageIndex

int = GetPageIndex\(page\)
Retrieves the index of the specified page of the property sheet\.

#### Parameters

  - page : [PyCPropertyPage](PyCPropertyPage.md)

    The page\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.GetTabCtrl

[PyCTabCtrl](PyCTabCtrl.md) = GetTabCtrl\(\)
Returns the tab control used by the sheet\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.OnInitDialog

int = OnInitDialog\(\)
Calls the default MFC OnInitDialog handler\.

#### See Also

  - [PyCPropertySheet\.OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog_virtual) virtual method


## [PyCPropertySheet\.OnInitDialog](PyCPropertySheet.md#pycpropertysheet) Virtual

OnInitDialog\(\)
Override to augment dialog-box initialization\.

#### Comments

The base implementation is not called if a handler exists\.  This can be 

done via [PyCDialog::OnInitDialog](PyCDialog.md#pycdialogoninitdialog)\.

#### See Also

  - [PyCDialog::OnInitDialog](PyCDialog.md#pycdialogoninitdialog)

#### Return Value
Specifies whether the application has set the input focus to 

one of the controls in the dialog box\. If OnInitDialog returns 

nonzero, Windows sets the input focus to the first control 

in the dialog box\. The application can return 0/None only if 

it has explicitly set the input focus to one of the controls in the 

dialog box\.


## [PyCPropertySheet\.OnInitDialog](PyCPropertySheet.md#pycpropertysheet) Virtual

OnInitDialog\(\)
Override to augment dialog-box initialization\.

#### Comments

The base implementation is not called if a handler exists\.  This can be 

done via [PyCPropertySheet::OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog)\.

#### See Also

  - [PyCPropertySheet::OnInitDialog](PyCPropertySheet.md#pycpropertysheetoninitdialog)

#### Return Value
Specifies whether the application has set the input focus to 

one of the controls in the dialog box\. If OnInitDialog returns 

nonzero, Windows sets the input focus to the first control 

in the dialog box\. The application can return 0/None only if 

it has explicitly set the input focus to one of the controls in the 

dialog box\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.PressButton

PressButton\(button\)
Simulates the choice of the specified button in a property sheet\.

#### Parameters

  - button : int

    The button to press


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.RemovePage

RemovePage\(offset\)
Removes the specified page from the sheet\.

#### Parameters

  - offset : int

    The page number to remove

#### Alternative Parameters

  - page

    The page to remove


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.SetActivePage

SetActivePage\(page\)
Programmatically sets the active page object\.

#### Parameters

  - page : [PyCPropertyPage](PyCPropertyPage.md)

    The page\.


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.SetFinishText

SetFinishText\(text\)
Sets the text for the Finish button

#### Parameters

  - text : string

    The next for the button


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.SetPSHBit

SetPSHBit\(bitMask, bitValue\)
Sets or clears a bit in m\_psh\.dwFlags

#### Parameters

  - bitMask : int

    The PSH\_\* bit mask constant

  - bitValue : int

    1 to set, 0 to clear


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.SetTitle

SetTitle\(title\)
Sets the caption for the property sheet\.

#### Parameters

  - title : string

    The new caption


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.SetWizardButtons

SetWizardButtons\(flags\)
Enables the wizard buttons

#### Parameters

  - flags : int

    The wizard flags


## [PyCPropertySheet](PyCPropertySheet.md#pycpropertysheet)\.SetWizardMode

SetWizardMode\(\)
Enables the wizard mode


## [PyCPropertySheet\.WindowProc](PyCPropertySheet.md#pycpropertysheet) Virtual

WindowProc\(\)
Default message handler\.