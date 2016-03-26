# PyCPrintInfo

## PyCPrintInfo Object

Encapsulates an MFC CPrintInfo class, its member __CPrintDialog__ class, and the __PRINTDLG__ structure member of the CPrintDialog.

#### Methods


  - [DocObject](PyCPrintInfo.md#pycprintinfodocobject)

    A flag indicating whether the document being printed is a DocObject.&nbsp;

  - [GetDwFlags](PyCPrintInfo.md#pycprintinfogetdwflags)

    A flags specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.&nbsp;

  - [SetDwFlags](PyCPrintInfo.md#pycprintinfosetdwflags)

    Set a flag specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.&nbsp;

  - [GetDocOffsetPage](PyCPrintInfo.md#pycprintinfogetdocoffsetpage)

    Get the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.&nbsp;

  - [SetDocOffsetPage](PyCPrintInfo.md#pycprintinfosetdocoffsetpage)

    Set the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.&nbsp;

  - [SetPrintDialog](PyCPrintInfo.md#pycprintinfosetprintdialog)

    Set a pointer to the CPrintDialog object used to display the Print dialog box for the print job.&nbsp;

  - [GetDirect](PyCPrintInfo.md#pycprintinfogetdirect)

    TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.&nbsp;

  - [SetDirect](PyCPrintInfo.md#pycprintinfosetdirect)

    Sets to TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.&nbsp;

  - [GetPreview](PyCPrintInfo.md#pycprintinfogetpreview)

    A flag indicating whether the document is being previewed.&nbsp;

  - [SetPreview](PyCPrintInfo.md#pycprintinfosetpreview)

    Set whether the document is being previewed.&nbsp;

  - [GetContinuePrinting](PyCPrintInfo.md#pycprintinfogetcontinueprinting)

    A flag indicating whether the framework should continue the print loop.&nbsp;

  - [SetContinuePrinting](PyCPrintInfo.md#pycprintinfosetcontinueprinting)

    Set whether the framework should continue the print loop.&nbsp;

  - [GetCurPage](PyCPrintInfo.md#pycprintinfogetcurpage)

    Get the number of the current page.&nbsp;

  - [SetCurPage](PyCPrintInfo.md#pycprintinfosetcurpage)

    Set the number of the current page.&nbsp;

  - [GetNumPreviewPages](PyCPrintInfo.md#pycprintinfogetnumpreviewpages)

    Get the number of pages displayed in preview mode.&nbsp;

  - [SetNumPreviewPages](PyCPrintInfo.md#pycprintinfosetnumpreviewpages)

    Set the number of pages displayed in preview mode.&nbsp;

  - [GetUserData](PyCPrintInfo.md#pycprintinfogetuserdata)

    Get a user-created structure.&nbsp;

  - [SetUserData](PyCPrintInfo.md#pycprintinfosetuserdata)

    Set a user-created structure.&nbsp;

  - [GetDraw](PyCPrintInfo.md#pycprintinfogetdraw)

    Get the usable drawing area of the page in logical coordinates.&nbsp;

  - [SetDraw](PyCPrintInfo.md#pycprintinfosetdraw)

    Set the usable drawing area of the page in logical coordinates.&nbsp;

  - [GetPageDesc](PyCPrintInfo.md#pycprintinfogetpagedesc)

    Get the format string used to display the page numbers during print preview&nbsp;

  - [SetPageDesc](PyCPrintInfo.md#pycprintinfosetpagedesc)

    Set the format string used to display the page numbers during print preview&nbsp;

  - [GetMinPage](PyCPrintInfo.md#pycprintinfogetminpage)

    Get the number of the first page of the document.&nbsp;

  - [SetMinPage](PyCPrintInfo.md#pycprintinfosetminpage)

    Set the number of the first page of the document.&nbsp;

  - [GetMaxPage](PyCPrintInfo.md#pycprintinfogetmaxpage)

    Get the number of the last page of the document.&nbsp;

  - [SetMaxPage](PyCPrintInfo.md#pycprintinfosetmaxpage)

    Set the number of the last page of the document.&nbsp;

  - [GetOffsetPage](PyCPrintInfo.md#pycprintinfogetoffsetpage)

    Get the number of pages preceding the first page of a DocObject item being printed in a combined DocObject print job.&nbsp;

  - [GetFromPage](PyCPrintInfo.md#pycprintinfogetfrompage)

    The number of the first page to be printed.&nbsp;

  - [GetToPage](PyCPrintInfo.md#pycprintinfogettopage)

    The number of the last page to be printed.&nbsp;

  - [SetHDC](PyCPrintInfo.md#pycprintinfosethdc)

    Sets the printer DC compatible with the users choices, call after the print dialog DoModal finishes.&nbsp;

  - [CreatePrinterDC](PyCPrintInfo.md#pycprintinfocreateprinterdc)

    Handle to the newly created printer device context, call only after DoModal finishes.&nbsp;

  - [DoModal](PyCPrintInfo.md#pycprintinfodomodal)

    Call DoModal on the dialog.&nbsp;

  - [GetCopies](PyCPrintInfo.md#pycprintinfogetcopies)

    The number of copies requested, call only after DoModal finishes.&nbsp;

  - [GetDefaults](PyCPrintInfo.md#pycprintinfogetdefaults)

    Retrieves device defaults without displaying a dialog box.&nbsp;

  - [FreeDefaults](PyCPrintInfo.md#pycprintinfofreedefaults)

    After a call to GetDefaults, and you are through with the CPrintDialog object, this call deletes the printer DC and calls GlobalFree function on the handles.&nbsp;

  - [GetDeviceName](PyCPrintInfo.md#pycprintinfogetdevicename)

    The name of the currently selected printer, call only after DoModal finishes.&nbsp;

  - [GetDriverName](PyCPrintInfo.md#pycprintinfogetdrivername)

    The name of the currently selected printer device driver, call only after DoModal finishes.&nbsp;

  - [GetDlgFromPage](PyCPrintInfo.md#pycprintinfogetdlgfrompage)

    Retrieves the starting page of the print range.&nbsp;

  - [GetDlgToPage](PyCPrintInfo.md#pycprintinfogetdlgtopage)

    Retrieves the ending page of the print range.&nbsp;

  - [GetPortName](PyCPrintInfo.md#pycprintinfogetportname)

    The name of the currently selected printer port, call only after DoModal finishes.&nbsp;

  - [GetPrinterDC](PyCPrintInfo.md#pycprintinfogetprinterdc)

    A handle to the printer device context if successful; otherwise NULL.  If the bPrintSetupOnly parameter of the CPrintDialog constructor was FALSE (indicating that the Print dialog box is displayed), then GetPrinterDC returns a handle to the printer device context. You must call the WindowsDeleteDC function to delete the device context when you are done using it.&nbsp;

  - [PrintAll](PyCPrintInfo.md#pycprintinfoprintall)

    Nonzero if all pages in the document are to be printed; otherwise 0, call only after DoModal finishes.&nbsp;

  - [PrintCollate](PyCPrintInfo.md#pycprintinfoprintcollate)

    Nonzero if the user selects the collate check box in the dialog box; otherwise 0, call only after DoModal finishes.&nbsp;

  - [PrintRange](PyCPrintInfo.md#pycprintinfoprintrange)

    Nonzero if only a range of pages in the document are to be printed; otherwise 0, call only after DoModal finishes.&nbsp;

  - [PrintSelection](PyCPrintInfo.md#pycprintinfoprintselection)

    Nonzero if only the selected items are to be printed; otherwise 0., call only after DoModal finishes&nbsp;

  - [GetHDC](PyCPrintInfo.md#pycprintinfogethdc)

    Identifies a device context or an information context, depending on whether the Flags member specifies the PD_RETURNDC or PC_RETURNIC flag. If neither flag is specified, the value of this member is undefined. If both flags are specified, PD_RETURNDC has priority.&nbsp;

  - [GetFlags](PyCPrintInfo.md#pycprintinfogetflags)

    A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input.&nbsp;

  - [SetFlags](PyCPrintInfo.md#pycprintinfosetflags)

    A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input.&nbsp;

  - [SetFromPage](PyCPrintInfo.md#pycprintinfosetfrompage)

    The number of the first page to be printed.&nbsp;

  - [SetToPage](PyCPrintInfo.md#pycprintinfosettopage)

    The number of the first page to be printed.&nbsp;

  - [GetPRINTDLGMinPage](PyCPrintInfo.md#pycprintinfogetprintdlgminpage)

    Get the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.&nbsp;

  - [SetPRINTDLGMinPage](PyCPrintInfo.md#pycprintinfosetprintdlgminpage)

    Set the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.&nbsp;

  - [GetPRINTDLGCopies](PyCPrintInfo.md#pycprintinfogetprintdlgcopies)

    Gets the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of the DEVMODE structure contains the initial value.&nbsp;

  - [SetPRINTDLGCopies](PyCPrintInfo.md#pycprintinfosetprintdlgcopies)

    Sets the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of the DEVMODE structure contains the initial value.&nbsp;

## [PyCPrintInfo](#pycprintinfo).CreatePrinterDC

 __CreatePrinterDC(__ )
Handle to the newly created printer device context, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::CreatePrinterDC

## [PyCPrintInfo](#pycprintinfo).DoModal

 __DoModal(__ )
Call DoModal on the dialog.

#### MFC References


  - CPrintDialog::DoModal

## [PyCPrintInfo](#pycprintinfo).DocObject

 __DocObject(__ )
Return true if the document being printed is a DocObject.

#### MFC References


  - CPrintInfo::m_bDocObject

## [PyCPrintInfo](#pycprintinfo).FreeDefaults

 __FreeDefaults(__ )
After a call to GetDefaults, and you are through with the CPrintDialog object, this call deletes the printer DC and calls GlobalFree function on the handles.

#### MFC References


  - CPrintDialog::GetDefaults

## [PyCPrintInfo](#pycprintinfo).GetContinuePrinting

 __GetContinuePrinting(__ )
A flag indicating whether the framework should continue the print loop.

#### MFC References


  - CPrintInfo::m_bContinuePrinting

## [PyCPrintInfo](#pycprintinfo).GetCopies

 __GetCopies(__ )
The number of copies requested, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::GetCopies

## [PyCPrintInfo](#pycprintinfo).GetCurPage

 __GetCurPage(__ )
Get the number of the current page.

#### MFC References


  - CPrintInfo::m_nCurPage

## [PyCPrintInfo](#pycprintinfo).GetDefaults

 __GetDefaults(__ )
Nonzero if the function was successful; otherwise 0.  Call this function to retrieve the device defaults of the default printer without displaying a dialog box. The retrieved values are placed in the m_pd structure.  In some cases, a call to this function will call the constructor for CPrintDialog with bPrintSetupOnly set to FALSE. In these cases, a printer DC and hDevNames and hDevMode (two handles located in the m_pd data member) are automatically allocated.  If the constructor for CPrintDialog was called with bPrintSetupOnly set to FALSE, this function will not only return hDevNames and hDevMode (located in m_pd.hDevNames and m_pd.hDevMode) to the caller, but will also return a printer DC in m_pd.hDC. It is the responsibility of the caller to delete the printer DC and call the WindowsGlobalFree function on the handles when you are finished with the CPrintDialog object.

#### MFC References


  - CPrintDialog::GetDefaults

## [PyCPrintInfo](#pycprintinfo).GetDeviceName

 __GetDeviceName(__ )
The name of the currently selected printer, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::GetDeviceName

## [PyCPrintInfo](#pycprintinfo).GetDirect

 __GetDirect(__ )
TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.

#### MFC References


  - CPrintInfo::m_bDirect

## [PyCPrintInfo](#pycprintinfo).GetDlgFromPage

 __GetDlgFromPage(__ )
Retrieves the starting page of the print range.

#### MFC References


  - CPrintDialog::GetDlgFromPage

## [PyCPrintInfo](#pycprintinfo).GetDlgToPage

 __GetDlgToPage(__ )
Retrieves the ending page of the print range.

#### MFC References


  - CPrintDialog::GetDlgToPage

## [PyCPrintInfo](#pycprintinfo).GetDocOffsetPage

 __GetDocOffsetPage(__ )
Get the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.

#### MFC References


  - CPrintInfo::m_nOffsetPage

## [PyCPrintInfo](#pycprintinfo).GetDraw

 __GetDraw(__ )
Get the usable drawing area of the page in logical coordinates.

#### MFC References


  - CPrintInfo::m_rectDraw

## [PyCPrintInfo](#pycprintinfo).GetDriverName

 __GetDriverName(__ )
The name of the currently selected printer device driver, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::GetDriverName

## [PyCPrintInfo](#pycprintinfo).GetDwFlags

 __GetDwFlags(__ )
A flags specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.

#### MFC References


  - CPrintInfo::m_dwFlags

## [PyCPrintInfo](#pycprintinfo).GetFlags

 __GetFlags(__ )
A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input. This member can be a combination of the following flags: PD_ALLPAGES, PD_COLLATE, PD_DISABLEPRINTTOFILE, PD_ENABLEPRINTHOOK, PD_ENABLEPRINTTEMPLATE, PD_ENABLEPRINTTEMPLATEHANDLE, PD_ENABLESETUPHOOK, PD_ENABLESETUPTEMPLATE, PD_ENABLESETUPTEMPLATEHANDLE, PD_HIDEPRINTTOFILE, PD_NONETWORKBUTTON, PD_NOPAGENUMS, PD_NOSELECTION, PD_NOWARNING, PD_PAGENUMS, PD_PRINTSETUP, PD_PRINTTOFILE, PD_RETURNDC, PD_RETURNDEFAULT, PD_RETURNIC, PD_SELECTION, PD_SHOWHELP, PD_USEDEVMODECOPIES, PD_USEDEVMODECOPIESANDCOLLATE.

#### MFC References


  - PRINTDLG::Flags

## [PyCPrintInfo](#pycprintinfo).GetFromPage

 __GetFromPage(__ )
The number of the first page to be printed.

#### MFC References


  - CPrintInfo::GetFromPage

## [PyCPrintInfo](#pycprintinfo).GetHDC

 __GetHDC(__ )
Identifies a device context or an information context, depending on whether the Flags member specifies the PD_RETURNDC or PC_RETURNIC flag. If neither flag is specified, the value of this member is undefined. If both flags are specified, PD_RETURNDC has priority.

#### MFC References


  - PRINTDLG::hDC

## [PyCPrintInfo](#pycprintinfo).GetMaxPage

 __GetMaxPage(__ )
Get the number of the last page of the document.

#### MFC References


  - CPrintInfo::GetMaxPage

## [PyCPrintInfo](#pycprintinfo).GetMinPage

 __GetMinPage(__ )
Get the number of the first page of the document.

#### MFC References


  - CPrintInfo::GetMinPage

## [PyCPrintInfo](#pycprintinfo).GetNumPreviewPages

 __GetNumPreviewPages(__ )
Get the number of pages displayed in preview mode.

#### MFC References


  - CPrintInfo::m_nNumPreviewPages

## [PyCPrintInfo](#pycprintinfo).GetOffsetPage

 __GetOffsetPage(__ )
Get the number of pages preceding the first page of a DocObject item being printed in a combined DocObject print job.  This currently does NOT work, as, if I include the symbol pInfo-&gtGetOffsetPage(), the link fails to find its definition.  Allways returns 0.

#### MFC References


  - CPrintInfo::GetOffsetPage

## [PyCPrintInfo](#pycprintinfo).GetPRINTDLGCopies

 __GetPRINTDLGCopies(__ )
Get the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of theDEVMODE structure contains the initial value. When PrintDlg returns, nCopies contains the actual number of copies to print. This value depends on whether the application or the printer driver is responsible for printing multiple copies. If the PD_USEDEVMODECOPIESANDCOLLATE flag is set in the Flags member, nCopies is always 1 on return, and the printer driver is responsible for printing multiple copies. If the flag is not set, the application is responsible for printing the number of copies specified by nCopies. For more information, see the description of the PD_USEDEVMODECOPIESANDCOLLATE flag.

#### MFC References


  - PRINTDLG::nCopies

## [PyCPrintInfo](#pycprintinfo).GetPRINTDLGMinPage

 __GetPRINTDLGMinPage(__ )
Get the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.

#### MFC References


  - PRINTDLG::nMinPage

## [PyCPrintInfo](#pycprintinfo).GetPageDesc

 __GetPageDesc(__ )
Get the format string used to display the page numbers during print preview

#### MFC References


  - CPrintInfo::m_strPageDesc

## [PyCPrintInfo](#pycprintinfo).GetPortName

 __GetPortName(__ )
The name of the currently selected printer port, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::GetPortName

## [PyCPrintInfo](#pycprintinfo).GetPreview

 __GetPreview(__ )
A flag indicating whether the document is being previewed.

#### MFC References


  - CPrintInfo::m_bPreview

## [PyCPrintInfo](#pycprintinfo).GetPrinterDC

 __GetPrinterDC(__ )
A handle to the printer device context if successful; otherwise NULL.  If the bPrintSetupOnly parameter of the CPrintDialog constructor was FALSE (indicating that the Print dialog box is displayed), then GetPrinterDC returns a handle to the printer device context. You must call the WindowsDeleteDC function to delete the device context when you are done using it.

#### MFC References


  - CPrintDialog::GetPrinterDC

## [PyCPrintInfo](#pycprintinfo).GetToPage

 __GetToPage(__ )
The number of the last page to be printed.

#### MFC References


  - CPrintInfo::GetToPage

## [PyCPrintInfo](#pycprintinfo).GetUserData

 __GetUserData(__ )
Get a user-created structure.

#### MFC References


  - CPrintInfo::m_lpUserData

## [PyCPrintInfo](#pycprintinfo).PrintAll

 __PrintAll(__ )
Nonzero if all pages in the document are to be printed; otherwise 0, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::PrintAll

## [PyCPrintInfo](#pycprintinfo).PrintCollate

 __PrintCollate(__ )
Nonzero if the user selects the collate check box in the dialog box; otherwise 0, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::PrintCollate

## [PyCPrintInfo](#pycprintinfo).PrintRange

 __PrintRange(__ )
Nonzero if only a range of pages in the document are to be printed; otherwise 0, call only after DoModal finishes.

#### MFC References


  - CPrintDialog::PrintRange

## [PyCPrintInfo](#pycprintinfo).PrintSelection

 __PrintSelection(__ )
Nonzero if only the selected items are to be printed; otherwise 0., call only after DoModal finishes

#### MFC References


  - CPrintDialog::PrintSelection

## [PyCPrintInfo](#pycprintinfo).SetContinuePrinting

 __SetContinuePrinting(__ )
Set whether the framework should continue the print loop.

#### MFC References


  - CPrintInfo::m_bContinuePrinting

## [PyCPrintInfo](#pycprintinfo).SetCurPage

 __SetCurPage(__ )
Set the number of the current page.

#### MFC References


  - CPrintInfo::m_nCurPage

## [PyCPrintInfo](#pycprintinfo).SetDirect

 __SetDirect(__ )
Sets to TRUE if the Print dialog box will be bypassed for direct printing; FALSE otherwise.

#### MFC References


  - CPrintInfo::m_bDirect

## [PyCPrintInfo](#pycprintinfo).SetDocOffsetPage

 __SetDocOffsetPage(__ )
Set the number of pages preceding the first page of a particular DocObject in a combined DocObject print job.

#### MFC References


  - CPrintInfo::m_nOffsetPage

## [PyCPrintInfo](#pycprintinfo).SetDraw

 __SetDraw(__ )
Set the usable drawing area of the page in logical coordinates.

#### MFC References


  - CPrintInfo::m_rectDraw

## [PyCPrintInfo](#pycprintinfo).SetDwFlags

 __SetDwFlags(__ )
Set a flag specifying DocObject printing operations. Valid only if data member m_bDocObject is TRUE.

#### MFC References


  - CPrintInfo::m_dwFlags

## [PyCPrintInfo](#pycprintinfo).SetFlags

 __SetFlags(__ )
A set of bit flags that you can use to initialize the Print common dialog box. When the dialog box returns, it sets these flags to indicate the user's input. This member can be a combination of the following flags: PD_ALLPAGES, PD_COLLATE, PD_DISABLEPRINTTOFILE, PD_ENABLEPRINTHOOK, PD_ENABLEPRINTTEMPLATE, PD_ENABLEPRINTTEMPLATEHANDLE, PD_ENABLESETUPHOOK, PD_ENABLESETUPTEMPLATE, PD_ENABLESETUPTEMPLATEHANDLE, PD_HIDEPRINTTOFILE, PD_NONETWORKBUTTON, PD_NOPAGENUMS, PD_NOSELECTION, PD_NOWARNING, PD_PAGENUMS, PD_PRINTSETUP, PD_PRINTTOFILE, PD_RETURNDC, PD_RETURNDEFAULT, PD_RETURNIC, PD_SELECTION, PD_SHOWHELP, PD_USEDEVMODECOPIES, PD_USEDEVMODECOPIESANDCOLLATE.

#### MFC References


  - PRINTDLG::Flags

## [PyCPrintInfo](#pycprintinfo).SetFromPage

 __SetFromPage(__ )
The number of the first page to be printed.

#### MFC References


  - PRINTDLG::nFromPage

## [PyCPrintInfo](#pycprintinfo).SetHDC

 __SetHDC( *hdc* __ )
Sets the printer DC compatible with the users choices, call after the print dialog DoModal finishes.

#### Parameters


  -  *hdc* : int

    The DC.

#### MFC References


  - CPrintInfo::m_pPD

  - CPrintDialog::m_pd.hDC

## [PyCPrintInfo](#pycprintinfo).SetMaxPage

 __SetMaxPage(__ )
Set the number of the last page of the document.

#### MFC References


  - CPrintInfo::SetMaxPage

## [PyCPrintInfo](#pycprintinfo).SetMinPage

 __SetMinPage(__ )
Set the number of the first page of the document.

#### MFC References


  - CPrintInfo::SetMinPage

## [PyCPrintInfo](#pycprintinfo).SetNumPreviewPages

 __SetNumPreviewPages(__ )
Set the number of pages displayed in preview mode.

#### MFC References


  - CPrintInfo::m_nNumPreviewPages

## [PyCPrintInfo](#pycprintinfo).SetPRINTDLGCopies

 __SetPRINTDLGCopies(__ )
Set the initial number of copies for the Copies edit control if hDevMode is NULL; otherwise, the dmCopies member of theDEVMODE structure contains the initial value. When PrintDlg returns, nCopies contains the actual number of copies to print. This value depends on whether the application or the printer driver is responsible for printing multiple copies. If the PD_USEDEVMODECOPIESANDCOLLATE flag is set in the Flags member, nCopies is always 1 on return, and the printer driver is responsible for printing multiple copies. If the flag is not set, the application is responsible for printing the number of copies specified by nCopies. For more information, see the description of the PD_USEDEVMODECOPIESANDCOLLATE flag.

#### MFC References


  - PRINTDLG::nCopies

## [PyCPrintInfo](#pycprintinfo).SetPRINTDLGMinPage

 __SetPRINTDLGMinPage(__ )
Set the minimum value for the page range specified in the From and To page edit controls. If nMinPage equals nMaxPage, the Pages radio button and the starting and ending page edit controls are disabled.

#### MFC References


  - PRINTDLG::nMinPage

## [PyCPrintInfo](#pycprintinfo).SetPageDesc

 __SetPageDesc(__ )
Set the format string used to display the page numbers during print preview

#### MFC References


  - CPrintInfo::m_strPageDesc

## [PyCPrintInfo](#pycprintinfo).SetPreview

 __SetPreview(__ )
Set whether the document is being previewed.

#### MFC References


  - CPrintInfo::m_bPreview

## [PyCPrintInfo](#pycprintinfo).SetPrintDialog

 __SetPrintDialog(__ )
Set a pointer to the CPrintDialog object used to display the Print dialog box for the print job.

#### MFC References


  - CPrintInfo::m_pPD

## [PyCPrintInfo](#pycprintinfo).SetToPage

 __SetToPage(__ )
The number of the last page to be printed.

#### MFC References


  - PRINTDLG::nToPage

## [PyCPrintInfo](#pycprintinfo).SetUserData

 __SetUserData(__ )
Set a user-created structure.

#### MFC References


  - CPrintInfo::m_lpUserData