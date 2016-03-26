# PyCPrintInfo


## PyCPrintInfo Object

Encapsulates an MFC CPrintInfo class, its member CPrintDialog

 class, and the PRINTDLG

 structure member of the CPrintDialog\.

#### Methods

  - [DocObject](PyCPrintInfo.md#pycprintinfodocobject)

    A flag indicating whether the document being printed is a DocObject\.&nbsp;

  - [GetDwFlags](PyCPrintInfo.md#pycprintinfogetdwflags)

    A flags specifying DocObject printing operations\. Valid only if data member m\_bDocObject is TRUE\.&nbsp;

  - [SetDwFlags](PyCPrintInfo.md#pycprintinfosetdwflags)

    Set a flag specifying DocObject printing operations\. Valid only if data member m\_bDocObject is TRUE\.&nbsp;

  - [GetDocOffsetPage](PyCPrintInfo.md#pycprintinfogetdocoffsetpage)

    Get the number of pages preceding the first page of a particular DocObject in a combined DocObject print job\.&nbsp;

  - [SetDocOffsetPage](PyCPrintInfo.md#pycprintinfosetdocoffsetpage)

    Set the number of pages preceding the first page of a particular DocObject in a combined DocObject print job\.&nbsp;

  - [SetPrintDialog](PyCPrintInfo.md#pycprintinfosetprintdialog)

    Set a pointer to the CPrintDialog object used to display the Print dialog box for the print job\.&nbsp;

  - [GetDirect](PyCPrintInfo.md#pycprintinfogetdirect)

    TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise\.&nbsp;

  - [SetDirect](PyCPrintInfo.md#pycprintinfosetdirect)

    Sets to TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise\.&nbsp;

  - [GetPreview](PyCPrintInfo.md#pycprintinfogetpreview)

    A flag indicating whether the document is being previewed\.&nbsp;

  - [SetPreview](PyCPrintInfo.md#pycprintinfosetpreview)

    Set whether the document is being previewed\.&nbsp;

  - [GetContinuePrinting](PyCPrintInfo.md#pycprintinfogetcontinueprinting)

    A flag indicating whether the framework should continue the print loop\.&nbsp;

  - [SetContinuePrinting](PyCPrintInfo.md#pycprintinfosetcontinueprinting)

    Set whether the framework should continue the print loop\.&nbsp;

  - [GetCurPage](PyCPrintInfo.md#pycprintinfogetcurpage)

    Get the number of the current page\.&nbsp;

  - [SetCurPage](PyCPrintInfo.md#pycprintinfosetcurpage)

    Set the number of the current page\.&nbsp;

  - [GetNumPreviewPages](PyCPrintInfo.md#pycprintinfogetnumpreviewpages)

    Get the number of pages displayed in preview mode\.&nbsp;

  - [SetNumPreviewPages](PyCPrintInfo.md#pycprintinfosetnumpreviewpages)

    Set the number of pages displayed in preview mode\.&nbsp;

  - [GetUserData](PyCPrintInfo.md#pycprintinfogetuserdata)

    Get a user-created structure\.&nbsp;

  - [SetUserData](PyCPrintInfo.md#pycprintinfosetuserdata)

    Set a user-created structure\.&nbsp;

  - [GetDraw](PyCPrintInfo.md#pycprintinfogetdraw)

    Get the usable drawing area of the page in logical coordinates\.&nbsp;

  - [SetDraw](PyCPrintInfo.md#pycprintinfosetdraw)

    Set the usable drawing area of the page in logical coordinates\.&nbsp;

  - [GetPageDesc](PyCPrintInfo.md#pycprintinfogetpagedesc)

    Get the format string used to display the page numbers during print preview&nbsp;

  - [SetPageDesc](PyCPrintInfo.md#pycprintinfosetpagedesc)

    Set the format string used to display the page numbers during print preview&nbsp;

  - [GetMinPage](PyCPrintInfo.md#pycprintinfogetminpage)

    Get the number of the first page of the document\.&nbsp;

  - [SetMinPage](PyCPrintInfo.md#pycprintinfosetminpage)

    Set the number of the first page of the document\.&nbsp;

  - [GetMaxPage](PyCPrintInfo.md#pycprintinfogetmaxpage)

    Get the number of the last page of the document\.&nbsp;

  - [SetMaxPage](PyCPrintInfo.md#pycprintinfosetmaxpage)

    Set the number of the last page of the document\.&nbsp;

  - [GetOffsetPage](PyCPrintInfo.md#pycprintinfogetoffsetpage)

    Get the number of pages preceding the first page of a DocObject item being printed in a combined DocObject print job\.&nbsp;

  - [GetFromPage](PyCPrintInfo.md#pycprintinfogetfrompage)

    The number of the first page to be printed\.&nbsp;

  - [GetToPage](PyCPrintInfo.md#pycprintinfogettopage)

    The number of the last page to be printed\.&nbsp;

  - [SetHDC](PyCPrintInfo.md#pycprintinfosethdc)

    Sets the printer DC compatible with the users choices, call after the print dialog DoModal finishes\.&nbsp;

  - [CreatePrinterDC](PyCPrintInfo.md#pycprintinfocreateprinterdc)

    Handle to the newly created printer device context, call only after DoModal finishes\.&nbsp;

  - [DoModal](PyCPrintInfo.md#pycprintinfodomodal)

    Call DoModal on the dialog\.&nbsp;

  - [GetCopies](PyCPrintInfo.md#pycprintinfogetcopies)

    The number of copies requested, call only after DoModal finishes\.&nbsp;

  - [GetDefaults](PyCPrintInfo.md#pycprintinfogetdefaults)

    Retrieves device defaults without displaying a dialog box\.&nbsp;

  - [FreeDefaults](PyCPrintInfo.md#pycprintinfofreedefaults)

    After a call to GetDefaults, and you are through with the CPrintDialog object, this call deletes the printer DC and calls GlobalFree function on the handles\.&nbsp;

  - [GetDeviceName](PyCPrintInfo.md#pycprintinfogetdevicename)

    The name of the currently selected printer, call only after DoModal finishes\.&nbsp;

  - [GetDriverName](PyCPrintInfo.md#pycprintinfogetdrivername)

    The name of the currently selected printer device driver, call only after DoModal finishes\.&nbsp;

  - [GetDlgFromPage](PyCPrintInfo.md#pycprintinfogetdlgfrompage)

    Retrieves the starting page of the print range\.&nbsp;

  - [GetDlgToPage](PyCPrintInfo.md#pycprintinfogetdlgtopage)

    Retrieves the ending page of the print range\.&nbsp;

  - [GetPortName](PyCPrintInfo.md#pycprintinfogetportname)

    The name of the currently selected printer port, call only after DoModal finishes\.&nbsp;

  - [GetPrinterDC](PyCPrintInfo.md#pycprintinfogetprinterdc)

    A handle to the printer device context if successful; otherwise NULL\.  If the bPrintSetupOnly parameter of the CPrintDialog constructor was FALSE \(indicating that the Print dialog box is displayed\), then GetPrinterDC returns a handle to the printer device context\. You must call the WindowsDeleteDC function to delete the device context when you are done using it\.&nbsp;

  - [PrintAll](PyCPrintInfo.md#pycprintinfoprintall)

    Nonzero if all pages in the document are to be printed; otherwise 0, call only after DoModal finishes\.&nbsp;

  - [PrintCollate](PyCPrintInfo.md#pycprintinfoprintcollate)

    Nonzero if the user selects the collate check box in the dialog box; otherwise 0, call only after DoModal finishes\.&nbsp;

  - [PrintRange](PyCPrintInfo.md#pycprintinfoprintrange)

    Nonzero if only a range of pages in the document are to be printed; otherwise 0, call only after DoModal finishes\.&nbsp;

  - [PrintSelection](PyCPrintInfo.md#pycprintinfoprintselection)

    Nonzero if only the selected items are to be printed; otherwise 0\., call only after DoModal finishes&nbsp;

  - [GetHDC](PyCPrintInfo.md#pycprintinfogethdc)

    Identifies a device context or an information context, depending on whether the Flags member specifies the PD\_RETURNDC or PC\_RETURNIC flag\. If neither flag is specified, the value of this member is undefined\. If both flags are specified, PD\_RETURNDC has priority\.&nbsp;

  - [GetFlags](PyCPrintInfo.md#pycprintinfogetflags)

    A set of bit flags that you can use to initialize the Print common dialog box\. When the dialog box returns, it sets these flags to indicate the user's input\.&nbsp;

  - [SetFlags](PyCPrintInfo.md#pycprintinfosetflags)

    A set of bit flags that you can use to initialize the Print common dialog box\. When the dialog box returns, it sets these flags to indicate the user's input\.&nbsp;

  - [SetFromPage](PyCPrintInfo.md#pycprintinfosetfrompage)

    The number of the first page to be printed\.&nbsp;

  - [SetToPage](PyCPrintInfo.md#pycprintinfosettopage)

    The number of the first page to be printed\.&nbsp;

  - [GetPRINTDLGMinPage](PyCPrintInfo.md#pycprintinfogetprintdlgminpage)

    Get the minimum value for the page range specified in the From and To page edit controls\. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled\.&nbsp;

  - [SetPRINTDLGMinPage](PyCPrintInfo.md#pycprintinfosetprintdlgminpage)

    Set the minimum value for the page range specified in the From and To page edit controls\. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled\.&nbsp;

  - [GetPRINTDLGCopies](PyCPrintInfo.md#pycprintinfogetprintdlgcopies)

    Gets the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of the DEVMODE structure contains the initial value\.&nbsp;

  - [SetPRINTDLGCopies](PyCPrintInfo.md#pycprintinfosetprintdlgcopies)

    Sets the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of the DEVMODE structure contains the initial value\.&nbsp;


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.CreatePrinterDC

CreatePrinterDC\(\)
Handle to the newly created printer device context, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::CreatePrinterDC


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.DoModal

DoModal\(\)
Call DoModal on the dialog\.

#### MFC References

  - CPrintDialog::DoModal


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.DocObject

DocObject\(\)
Return true if the document being printed is a DocObject\.

#### MFC References

  - CPrintInfo::m\_bDocObject


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.FreeDefaults

FreeDefaults\(\)
After a call to GetDefaults, and you are through with the CPrintDialog object, this call deletes the printer DC and calls GlobalFree function on the handles\.

#### MFC References

  - CPrintDialog::GetDefaults


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetContinuePrinting

GetContinuePrinting\(\)
A flag indicating whether the framework should continue the print loop\.

#### MFC References

  - CPrintInfo::m\_bContinuePrinting


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetCopies

GetCopies\(\)
The number of copies requested, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::GetCopies


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetCurPage

GetCurPage\(\)
Get the number of the current page\.

#### MFC References

  - CPrintInfo::m\_nCurPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDefaults

GetDefaults\(\)
Nonzero if the function was successful; otherwise 0\.  Call this function to retrieve the device defaults of the default printer without displaying a dialog box\. The retrieved values are placed in the m\_pd structure\.  In some cases, a call to this function will call the constructor for CPrintDialog with bPrintSetupOnly set to FALSE\. In these cases, a printer DC and hDevNames and hDevMode \(two handles located in the m\_pd data member\) are automatically allocated\.  If the constructor for CPrintDialog was called with bPrintSetupOnly set to FALSE, this function will not only return hDevNames and hDevMode \(located in m\_pd\.hDevNames and m\_pd\.hDevMode\) to the caller, but will also return a printer DC in m\_pd\.hDC\. It is the responsibility of the caller to delete the printer DC and call the WindowsGlobalFree function on the handles when you are finished with the CPrintDialog object\.

#### MFC References

  - CPrintDialog::GetDefaults


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDeviceName

GetDeviceName\(\)
The name of the currently selected printer, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::GetDeviceName


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDirect

GetDirect\(\)
TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise\.

#### MFC References

  - CPrintInfo::m\_bDirect


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDlgFromPage

GetDlgFromPage\(\)
Retrieves the starting page of the print range\.

#### MFC References

  - CPrintDialog::GetDlgFromPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDlgToPage

GetDlgToPage\(\)
Retrieves the ending page of the print range\.

#### MFC References

  - CPrintDialog::GetDlgToPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDocOffsetPage

GetDocOffsetPage\(\)
Get the number of pages preceding the first page of a particular DocObject in a combined DocObject print job\.

#### MFC References

  - CPrintInfo::m\_nOffsetPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDraw

GetDraw\(\)
Get the usable drawing area of the page in logical coordinates\.

#### MFC References

  - CPrintInfo::m\_rectDraw


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDriverName

GetDriverName\(\)
The name of the currently selected printer device driver, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::GetDriverName


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetDwFlags

GetDwFlags\(\)
A flags specifying DocObject printing operations\. Valid only if data member m\_bDocObject is TRUE\.

#### MFC References

  - CPrintInfo::m\_dwFlags


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetFlags

GetFlags\(\)
A set of bit flags that you can use to initialize the Print common dialog box\. When the dialog box returns, it sets these flags to indicate the user's input\. This member can be a combination of the following flags: PD\_ALLPAGES, PD\_COLLATE, PD\_DISABLEPRINTTOFILE, PD\_ENABLEPRINTHOOK, PD\_ENABLEPRINTTEMPLATE, PD\_ENABLEPRINTTEMPLATEHANDLE, PD\_ENABLESETUPHOOK, PD\_ENABLESETUPTEMPLATE, PD\_ENABLESETUPTEMPLATEHANDLE, PD\_HIDEPRINTTOFILE, PD\_NONETWORKBUTTON, PD\_NOPAGENUMS, PD\_NOSELECTION, PD\_NOWARNING, PD\_PAGENUMS, PD\_PRINTSETUP, PD\_PRINTTOFILE, PD\_RETURNDC, PD\_RETURNDEFAULT, PD\_RETURNIC, PD\_SELECTION, PD\_SHOWHELP, PD\_USEDEVMODECOPIES, PD\_USEDEVMODECOPIESANDCOLLATE\.

#### MFC References

  - PRINTDLG::Flags


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetFromPage

GetFromPage\(\)
The number of the first page to be printed\.

#### MFC References

  - CPrintInfo::GetFromPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetHDC

GetHDC\(\)
Identifies a device context or an information context, depending on whether the Flags member specifies the PD\_RETURNDC or PC\_RETURNIC flag\. If neither flag is specified, the value of this member is undefined\. If both flags are specified, PD\_RETURNDC has priority\.

#### MFC References

  - PRINTDLG::hDC


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetMaxPage

GetMaxPage\(\)
Get the number of the last page of the document\.

#### MFC References

  - CPrintInfo::GetMaxPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetMinPage

GetMinPage\(\)
Get the number of the first page of the document\.

#### MFC References

  - CPrintInfo::GetMinPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetNumPreviewPages

GetNumPreviewPages\(\)
Get the number of pages displayed in preview mode\.

#### MFC References

  - CPrintInfo::m\_nNumPreviewPages


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetOffsetPage

GetOffsetPage\(\)
Get the number of pages preceding the first page of a DocObject item being printed in a combined DocObject print job\.  This currently does NOT work, as, if I include the symbol pInfo-&gtGetOffsetPage\(\), the link fails to find its definition\.  Allways returns 0\.

#### MFC References

  - CPrintInfo::GetOffsetPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetPRINTDLGCopies

GetPRINTDLGCopies\(\)
Get the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of theDEVMODE structure contains the initial value\. When PrintDlg returns, nCopies contains the actual number of copies to print\. This value depends on whether the application or the printer driver is responsible for printing multiple copies\. If the PD\_USEDEVMODECOPIESANDCOLLATE flag is set in the Flags member, nCopies is always 1 on return, and the printer driver is responsible for printing multiple copies\. If the flag is not set, the application is responsible for printing the number of copies specified by nCopies\. For more information, see the description of the PD\_USEDEVMODECOPIESANDCOLLATE flag\.

#### MFC References

  - PRINTDLG::nCopies


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetPRINTDLGMinPage

GetPRINTDLGMinPage\(\)
Get the minimum value for the page range specified in the From and To page edit controls\. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled\.

#### MFC References

  - PRINTDLG::nMinPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetPageDesc

GetPageDesc\(\)
Get the format string used to display the page numbers during print preview

#### MFC References

  - CPrintInfo::m\_strPageDesc


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetPortName

GetPortName\(\)
The name of the currently selected printer port, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::GetPortName


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetPreview

GetPreview\(\)
A flag indicating whether the document is being previewed\.

#### MFC References

  - CPrintInfo::m\_bPreview


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetPrinterDC

GetPrinterDC\(\)
A handle to the printer device context if successful; otherwise NULL\.  If the bPrintSetupOnly parameter of the CPrintDialog constructor was FALSE \(indicating that the Print dialog box is displayed\), then GetPrinterDC returns a handle to the printer device context\. You must call the WindowsDeleteDC function to delete the device context when you are done using it\.

#### MFC References

  - CPrintDialog::GetPrinterDC


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetToPage

GetToPage\(\)
The number of the last page to be printed\.

#### MFC References

  - CPrintInfo::GetToPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.GetUserData

GetUserData\(\)
Get a user-created structure\.

#### MFC References

  - CPrintInfo::m\_lpUserData


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.PrintAll

PrintAll\(\)
Nonzero if all pages in the document are to be printed; otherwise 0, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::PrintAll


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.PrintCollate

PrintCollate\(\)
Nonzero if the user selects the collate check box in the dialog box; otherwise 0, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::PrintCollate


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.PrintRange

PrintRange\(\)
Nonzero if only a range of pages in the document are to be printed; otherwise 0, call only after DoModal finishes\.

#### MFC References

  - CPrintDialog::PrintRange


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.PrintSelection

PrintSelection\(\)
Nonzero if only the selected items are to be printed; otherwise 0\., call only after DoModal finishes

#### MFC References

  - CPrintDialog::PrintSelection


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetContinuePrinting

SetContinuePrinting\(\)
Set whether the framework should continue the print loop\.

#### MFC References

  - CPrintInfo::m\_bContinuePrinting


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetCurPage

SetCurPage\(\)
Set the number of the current page\.

#### MFC References

  - CPrintInfo::m\_nCurPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetDirect

SetDirect\(\)
Sets to TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise\.

#### MFC References

  - CPrintInfo::m\_bDirect


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetDocOffsetPage

SetDocOffsetPage\(\)
Set the number of pages preceding the first page of a particular DocObject in a combined DocObject print job\.

#### MFC References

  - CPrintInfo::m\_nOffsetPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetDraw

SetDraw\(\)
Set the usable drawing area of the page in logical coordinates\.

#### MFC References

  - CPrintInfo::m\_rectDraw


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetDwFlags

SetDwFlags\(\)
Set a flag specifying DocObject printing operations\. Valid only if data member m\_bDocObject is TRUE\.

#### MFC References

  - CPrintInfo::m\_dwFlags


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetFlags

SetFlags\(\)
A set of bit flags that you can use to initialize the Print common dialog box\. When the dialog box returns, it sets these flags to indicate the user's input\. This member can be a combination of the following flags: PD\_ALLPAGES, PD\_COLLATE, PD\_DISABLEPRINTTOFILE, PD\_ENABLEPRINTHOOK, PD\_ENABLEPRINTTEMPLATE, PD\_ENABLEPRINTTEMPLATEHANDLE, PD\_ENABLESETUPHOOK, PD\_ENABLESETUPTEMPLATE, PD\_ENABLESETUPTEMPLATEHANDLE, PD\_HIDEPRINTTOFILE, PD\_NONETWORKBUTTON, PD\_NOPAGENUMS, PD\_NOSELECTION, PD\_NOWARNING, PD\_PAGENUMS, PD\_PRINTSETUP, PD\_PRINTTOFILE, PD\_RETURNDC, PD\_RETURNDEFAULT, PD\_RETURNIC, PD\_SELECTION, PD\_SHOWHELP, PD\_USEDEVMODECOPIES, PD\_USEDEVMODECOPIESANDCOLLATE\.

#### MFC References

  - PRINTDLG::Flags


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetFromPage

SetFromPage\(\)
The number of the first page to be printed\.

#### MFC References

  - PRINTDLG::nFromPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetHDC

SetHDC\(hdc\)
Sets the printer DC compatible with the users choices, call after the print dialog DoModal finishes\.

#### Parameters

  - hdc : int

    The DC\.

#### MFC References

  - CPrintInfo::m\_pPD

  - CPrintDialog::m\_pd\.hDC


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetMaxPage

SetMaxPage\(\)
Set the number of the last page of the document\.

#### MFC References

  - CPrintInfo::SetMaxPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetMinPage

SetMinPage\(\)
Set the number of the first page of the document\.

#### MFC References

  - CPrintInfo::SetMinPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetNumPreviewPages

SetNumPreviewPages\(\)
Set the number of pages displayed in preview mode\.

#### MFC References

  - CPrintInfo::m\_nNumPreviewPages


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetPRINTDLGCopies

SetPRINTDLGCopies\(\)
Set the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of theDEVMODE structure contains the initial value\. When PrintDlg returns, nCopies contains the actual number of copies to print\. This value depends on whether the application or the printer driver is responsible for printing multiple copies\. If the PD\_USEDEVMODECOPIESANDCOLLATE flag is set in the Flags member, nCopies is always 1 on return, and the printer driver is responsible for printing multiple copies\. If the flag is not set, the application is responsible for printing the number of copies specified by nCopies\. For more information, see the description of the PD\_USEDEVMODECOPIESANDCOLLATE flag\.

#### MFC References

  - PRINTDLG::nCopies


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetPRINTDLGMinPage

SetPRINTDLGMinPage\(\)
Set the minimum value for the page range specified in the From and To page edit controls\. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled\.

#### MFC References

  - PRINTDLG::nMinPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetPageDesc

SetPageDesc\(\)
Set the format string used to display the page numbers during print preview

#### MFC References

  - CPrintInfo::m\_strPageDesc


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetPreview

SetPreview\(\)
Set whether the document is being previewed\.

#### MFC References

  - CPrintInfo::m\_bPreview


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetPrintDialog

SetPrintDialog\(\)
Set a pointer to the CPrintDialog object used to display the Print dialog box for the print job\.

#### MFC References

  - CPrintInfo::m\_pPD


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetToPage

SetToPage\(\)
The number of the last page to be printed\.

#### MFC References

  - PRINTDLG::nToPage


## [PyCPrintInfo](PyCPrintInfo.md#pycprintinfo)\.SetUserData

SetUserData\(\)
Set a user-created structure\.

#### MFC References

  - CPrintInfo::m\_lpUserData