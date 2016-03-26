
## AFX_IDW_PANE_FIRST
 **const win32ui.AFX_IDW_PANE_FIRST;** 
Id of the first splitter pane

## AFX_IDW_PANE_LAST
 **const win32ui.AFX_IDW_PANE_LAST;** 
Id of the last splitter pane

## AFX_WS_DEFAULT_VIEW
 **const win32ui.AFX_WS_DEFAULT_VIEW;** 


## [win32ui](#README.md#win32ui).AddToRecentFileList

 **AddToRecentFileList( *fileName* ** )
Adds an entry to the applications Recent File List.

#### Parameters


     *fileName* : string

    The file name to be added to the list.

#### MFC References


    CWinApp::AddToRecentFileList

## CDocTemplate_Confidence_maybeAttemptForeign
 **const win32ui.CDocTemplate_Confidence_maybeAttemptForeign;** 


## CDocTemplate_Confidence_maybeAttemptNative
 **const win32ui.CDocTemplate_Confidence_maybeAttemptNative;** 


## CDocTemplate_Confidence_noAttempt
 **const win32ui.CDocTemplate_Confidence_noAttempt;** 


## CDocTemplate_Confidence_yesAlreadyOpen
 **const win32ui.CDocTemplate_Confidence_yesAlreadyOpen;** 


## CDocTemplate_Confidence_yesAttemptForeign
 **const win32ui.CDocTemplate_Confidence_yesAttemptForeign;** 


## CDocTemplate_Confidence_yesAttemptNative
 **const win32ui.CDocTemplate_Confidence_yesAttemptNative;** 


## CDocTemplate_docName
 **const win32ui.CDocTemplate_docName;** 


## CDocTemplate_fileNewName
 **const win32ui.CDocTemplate_fileNewName;** 


## CDocTemplate_filterExt
 **const win32ui.CDocTemplate_filterExt;** 


## CDocTemplate_filterName
 **const win32ui.CDocTemplate_filterName;** 


## CDocTemplate_regFileTypeId
 **const win32ui.CDocTemplate_regFileTypeId;** 


## CDocTemplate_regFileTypeName
 **const win32ui.CDocTemplate_regFileTypeName;** 


## CDocTemplate_windowTitle
 **const win32ui.CDocTemplate_windowTitle;** 


## CRichEditView_WrapNone
 **const win32ui.CRichEditView_WrapNone;** 


## CRichEditView_WrapToTargetDevice
 **const win32ui.CRichEditView_WrapToTargetDevice;** 


## CRichEditView_WrapToWindow
 **const win32ui.CRichEditView_WrapToWindow;** 


## [win32ui](#README.md#win32ui).ComparePath

int = **ComparePath( *path1*  *, path2* ** )
Compares 2 paths.

#### Parameters


     *path1* : string

    The path name.

     *path2* : string

    The path name.

## [win32ui](#README.md#win32ui).CreateBitmap

[PyCBitMap](#README.md#PyCBitMap)= **CreateBitmap(** )
Creates a bitmap object.

## [win32ui](#README.md#win32ui).CreateBitmapFromHandle

[PyCBitMap](#README.md#PyCBitMap)= **CreateBitmapFromHandle(** )
Creates a bitmap object from a HBITMAP.

## [win32ui](#README.md#win32ui).CreateBrush

[PyCBrush](#README.md#PyCBrush)= **CreateBrush(** )
Creates a new brush object.

#### Alternative Parameters


     *style* 

    The brush style.

     *color* 

    The brush color.

     *hatch* 

    The brush hatching.

#### Comments
If called with no arguments, an uninitialized brush is created.

## [win32ui](#README.md#win32ui).CreateButton

[PyCButton](#README.md#PyCButton)= **CreateButton(** )
Creates a button object.[PyCButton::CreateWindow](#PyCButton.md#PyCButtonCreateWindow)creates the actual control.

## [win32ui](#README.md#win32ui).CreateColorDialog

[PyCColorDialog](#README.md#PyCColorDialog)= **CreateColorDialog( *initColor*  *, flags*  *, parent* ** )
Creates a color selection dialog box. 

self*/, PyObject *args )

#### Parameters


     *initColor=0* : int

    The initial color.

     *flags=0* : int

    The choose-color flags to use.

     *parent=None* :[PyCWnd](#README.md#PyCWnd)

    The parent or owner window of the dialog.

## [win32ui](#README.md#win32ui).CreateControl

[PyCWnd](#README.md#PyCWnd)= **CreateControl( *classId*  *, windowName*  *, style*  *, rect*  *, parent*  *, id*  *, obPersist*  *, bStorage*  *, licKey* ** )
Creates an OLE control.

#### Parameters


     *classId* : string

    The class ID for the window.

     *windowName* : string

    The title for the window.

     *style* : int

    The style for the control.

     *rect* : (left, top, right, bottom)

    The default position of the window.

     *parent* :[PyCWnd](#README.md#PyCWnd)

    The parent window

     *id* : int

    The child ID for the view

     *obPersist=None* : object

    Place holder for future support.

     *bStorage=FALSE* : int

    Not used.

     *licKey=None* : string

    The licence key for the control.

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).CreateControlBar

[PyCControlBar](#README.md#PyCControlBar)= **CreateControlBar(** )
Creates a control bar object.

## [win32ui](#README.md#win32ui).CreateCtrlView

[PyCCtrlView](#README.md#PyCCtrlView)= **CreateCtrlView( *doc*  *, className*  *, style* ** )
Creates a control view object.

#### Parameters


     *doc* :[PyCDocument](#README.md#PyCDocument)

    The document.

     *className* : string

    The class name of the control

     *style=0* : int

    Additional style bits

## [win32ui](#README.md#win32ui).CreateDC

 **CreateDC(** )
Creates an uninitialised device context.

## [win32ui](#README.md#win32ui).CreateDCFromHandle

 **CreateDCFromHandle(** )
Creates a DC object from an integer handle.

## [win32ui](#README.md#win32ui).CreateDebuggerThread

 **CreateDebuggerThread(** )
Starts a debugging thread (ie, creates the "break" button).

#### Comments
This allows an application which is performing a long operation to dispatch paint messages during the operation.

## [win32ui](#README.md#win32ui).CreateDialog

[PyCDialog](#README.md#PyCDialog)= **CreateDialog( *idRes*  *, dll* ** )
Creates a dialog object.

#### Parameters


     *idRes* : int

    The ID of the dialog resource to load.

     *dll=None* :[PyDLL](#README.md#PyDLL)

    The DLL object to load the dialog from.

## [win32ui](#README.md#win32ui).CreateDialogBar

[PyCDialogBar](#README.md#PyCDialogBar)= **CreateDialogBar(** )
Creates a[PyCDialogBar](#README.md#PyCDialogBar)object.

## [win32ui](#README.md#win32ui).CreateDialogIndirect

[PyCDialog](#README.md#PyCDialog)= **CreateDialogIndirect( *obList* ** )
Creates a dialog object from a template.

#### Parameters


     *obList* : list

    A list of [[PyDLGTEMPLATE](#README.md#PyDLGTEMPLATE),[PyDLGITEMTEMPLATE](#README.md#PyDLGITEMTEMPLATE), ...], which describe the dialog to be created.

## [win32ui](#README.md#win32ui).CreateDocTemplate

[PyCDocTemplate](#README.md#PyCDocTemplate)= **CreateDocTemplate( *idRes* ** )
Creates a document template object.

#### Parameters


     *idRes* : int

    The ID for resources for documents of this type.

## [win32ui](#README.md#win32ui).CreateEdit

[PyCEdit](#README.md#PyCEdit)= **CreateEdit(** )
Creates an Edit object.[PyCEdit::CreateWindow](#PyCEdit.md#PyCEditCreateWindow)creates the actual control.

## [win32ui](#README.md#win32ui).CreateEditView

[PyCEditView](#README.md#PyCEditView)= **CreateEditView( *doc* ** )
Creates a PyEditView object.

#### Parameters


     *doc* :[PyCDocument](#README.md#PyCDocument)

    The document to use with the view.

## [win32ui](#README.md#win32ui).CreateFileDialog

[PyCFileDialog](#README.md#PyCFileDialog)= **CreateFileDialog( *bFileOpen*  *, defExt*  *, fileName*  *, flags*  *, filter*  *, parent* ** )
Creates a File Open/Save/etc Common Dialog. 

self*/, PyObject *args )

#### Parameters


     *bFileOpen* : int

    A flag indicating if the Dialog is a FileOpen or FileSave dialog.

     *defExt=None* : string

    The default file extension for saved files. If None, no extension is supplied.

     *fileName=None* : string

    The initial filename that appears in the filename edit box. If None, no filename initially appears.

     *flags=win32con.OFN_HIDEREADONLY|win32con.OFN_OVERWRITEPROMPT* : int

    The flags for the dialog.  See the API documentation for full details.

     *filter=None* : string

    A series of string pairs that specify filters you can apply to the file. 

If you specify file filters, only selected files will appear 

in the Files list box. The first string in the string pair describes 

the filter; the second string indicates the file extension to use. 

Multiple extensions may be specified using ';' as the delimiter. 

The string ends with two '|' characters.  May be None.

     *parent=None* :[PyCWnd](#README.md#PyCWnd)

    The parent or owner window of the dialog.

## [win32ui](#README.md#win32ui).CreateFont

[PyCFont](#README.md#PyCFont)= **CreateFont( *properties* ** )
Creates a[PyCFont](#README.md#PyCFont)object.

#### Parameters


     *properties* : dict

    A dictionary containing the font 

properties.  Valid dictionary keys are:
height
width
escapement
orientation
weight
italic
underline
strike out
charset
out precision
clip precision
quality
pitch and family
name

#### Comments
The code for the PyCFont was contributed by Dave Brennan 

(Last known address is brennan@hal.com, but I hear he is now at Microsoft) 

args contains a dict of font properties

## [win32ui](#README.md#win32ui).CreateFontDialog

[PyCFontDialog](#README.md#PyCFontDialog)= **CreateFontDialog( *font*  *, flags*  *, dcPrinter*  *, parent* ** )
Creates a font selection dialog box. 

self*/, PyObject *args )

#### Parameters


     *font=None* : dict/tuple

    A dictionary describing a LOGFONT, or a tuple describing a CHARFORMAT.

     *flags=win32con.CF_EFFECTS|win32con.CF_SCREENFONTS* : int

    The choose-font flags to use.

     *dcPrinter=None* :[PyCDC](#README.md#PyCDC)

    Show fonts available for the specified device.

     *parent=None* :[PyCWnd](#README.md#PyCWnd)

    The parent or owner window of the dialog.

## [win32ui](#README.md#win32ui).CreateFormView

[PyCFormView](#README.md#PyCFormView)= **CreateFormView( *doc*  *, Template* ** )
Creates a form view object.

#### Parameters


     *doc* :[PyCDocument](#README.md#PyCDocument)

    The document to use with the view.

     *Template* : int/str

    Name or ID of the dialog template resource

## [win32ui](#README.md#win32ui).CreateFrame

 **PyFrameWnd** = **CreateFrame(** )
Creates a Frame window.

#### Return Value
The window object (not the OS window) created.  An exception is raised if an error occurs.

## [win32ui](#README.md#win32ui).CreateImageList

int = **CreateImageList( *cx*  *, cy*  *, mask*  *, initial*  *, grow* ** )
Creates an image list.

#### Parameters


     *cx* : int

    Dimension of each image, in pixels.

     *cy* : int

    Dimension of each image, in pixels.

     *mask* : int

    TRUE if the image contains a mask; otherwise FALSE.

     *initial* : int

    Number of images that the image list initially contains.

     *grow* : int

    Number of images by which the image list can grow when the system needs to resize the list to make room for new images. This parameter represents the number of new images the resized image list can contain.

#### Alternative Parameters


     *bitmapId* 

    Resource name or ID of the bitmap to be associated with the image list.

     *cx* 

    Dimension of each image, in pixels.

     *grow* 

    Number of images by which the image list can grow when the system needs to resize the list to make room for new images. This parameter represents the number of new images the resized image list can contain.

     *crMask* 

    Color used to generate a mask. Each pixel of this color in the specified bitmap is changed to black, and the corresponding bit in the mask is set to one.

## [win32ui](#README.md#win32ui).CreateListCtrl

[PyCListCtrl](#README.md#PyCListCtrl)= **CreateListCtrl(** )
Creates a list control.

## [win32ui](#README.md#win32ui).CreateListView

[PyCListView](#README.md#PyCListView)= **CreateListView( *doc* ** )
Creates a PyCListView object.

#### Parameters


     *doc* :[PyCDocument](#README.md#PyCDocument)

    The document to use with the view.

## [win32ui](#README.md#win32ui).CreateMDIChild

[PyCMDIChildWnd](#README.md#PyCMDIChildWnd)= **CreateMDIChild(** )
Creates an MDI Child window.

#### Return Value
The window object created.  An exception is raised if an error occurs.

## [win32ui](#README.md#win32ui).CreateMDIFrame

[PyCMDIFrameWnd](#README.md#PyCMDIFrameWnd)= **CreateMDIFrame(** )
Creates an MDI Frame window.

#### Comments
An MDI Frame Window is usually the main application window. 

Therefore there is uaually only one of these windows per application.
An application can only hae one main window.  This method will fail if the application 

window already exists.

#### Return Value
The window object created.  An exception is raised if an error occurs.

## [win32ui](#README.md#win32ui).CreateMenu

[PyCMenu](#README.md#PyCMenu)= **CreateMenu(** )
Creates a menu object.

## [win32ui](#README.md#win32ui).CreatePalette

int = **CreatePalette( *lp* ** )
Creates a HPALETTE

#### Parameters


     *lp* : **LOGPALETTE** 

    The entries for the palette.

## [win32ui](#README.md#win32ui).CreatePen

 **PyCPen** = **CreatePen( *style*  *, width*  *, color* ** )
Creates a **PyCPen** object. 

static*/ PyObject *

#### Parameters


     *style* : int

    The pen style.

     *width* : int

    The pen width.

     *color* : long

    The pen color.

## [win32ui](#README.md#win32ui).CreatePopupMenu

[PyCMenu](#README.md#PyCMenu)= **CreatePopupMenu(** )
Creates a popup menu object.

## [win32ui](#README.md#win32ui).CreatePrintDialog

[PyCPrintDialog](#README.md#PyCPrintDialog)= **CreatePrintDialog( *idRes*  *, bPrintSetupOnly*  *, dwFlags*  *, parent*  *, dll* ** )
Creates a print dialog object.

#### Parameters


     *idRes* : int

    The ID of the dialog resource to load.

     *bPrintSetupOnly=FALSE* : int

    Specifies whether the standard Windows Print dialog box or Print Setup dialog box is displayed.

     *dwFlags=PD_ALLPAGES|PD_USEDEVMODECOPIES|PD_NOPAGENUMS|PD_HIDEPRINTTOFILE|PD_NOSELECTION* : int

    One or more flags you can use to customize the settings of the dialog box, combined using the bitwise OR operator.

     *parent=None* :[PyCWnd](#README.md#PyCWnd)

    A pointer to the dialog box parent or owner window.

     *dll=None* :[PyDLL](#README.md#PyDLL)

    The DLL object to load the dialog from.

## [win32ui](#README.md#win32ui).CreateProgressCtrl

[PyCProgressCtrl](#README.md#PyCProgressCtrl)= **CreateProgressCtrl(** )
Creates a progress control object. **PyProgressCtrl::Create** creates the actual control.

## [win32ui](#README.md#win32ui).CreatePropertyPage

[PyCPropertyPage](#README.md#PyCPropertyPage)= **CreatePropertyPage( *resource*  *, caption* ** )
Creates a property page object.

#### Parameters


     *resource* :[PyResourceId](#README.md#PyResourceId)

    String template name or inteter resource ID to use for the page.

     *caption=0* : int

    The ID if the string resource to use for the caption.

## [win32ui](#README.md#win32ui).CreatePropertyPageIndirect

[PyCPropertyPage](#README.md#PyCPropertyPage)= **CreatePropertyPageIndirect( *resourceList*  *, caption* ** )
Creates a property page object from a template.

#### Parameters


     *resourceList* :[PyDialogTemplate](#README.md#PyDialogTemplate)

    Definition of the page to be created.

     *caption=0* : int

    The ID if the string resource to use for the caption.

## [win32ui](#README.md#win32ui).CreatePropertySheet

[PyCPropertySheet](#README.md#PyCPropertySheet)= **CreatePropertySheet( *caption*  *, parent*  *, select* ** )
Creates a property sheet object.

#### Parameters


     *caption* :[PyResourceId](#README.md#PyResourceId)

    The caption for the property sheet, or id of the caption

     *parent=None* :[PyCWnd](#README.md#PyCWnd)

    The parent window of the property sheet.

     *select=0* : int

    The index of the first page to be selected.

## [win32ui](#README.md#win32ui).CreateRgn

[PyCRgn](#README.md#PyCRgn)= **CreateRgn(** )
Creates a new rgn object. 

Return Values: a PyCRgn object

## [win32ui](#README.md#win32ui).CreateRichEditCtrl

[PyCRichEditCtrl](#README.md#PyCRichEditCtrl)= **CreateRichEditCtrl(** )
Creates a rich edit control.

#### Comments
This method only creates the RichEdit object. To create the window, (ie, the control itself), call **PyCRichEdit::CreateWindow** 

## [win32ui](#README.md#win32ui).CreateRichEditDocTemplate

[PyCRichEditDocTemplate](#README.md#PyCRichEditDocTemplate)= **CreateRichEditDocTemplate( *idRes* ** )
Creates a document template object.

#### Parameters


     *idRes* : int

    The ID for resources for documents of this type.

## [win32ui](#README.md#win32ui).CreateRichEditView

[PyCRichEditView](#README.md#PyCRichEditView)= **CreateRichEditView( *doc* ** )
Creates a PyRichEditView object.

#### Parameters


     *doc=None* :[PyCDocument](#README.md#PyCDocument)

    The document to use with the view, or None for NULL.

## [win32ui](#README.md#win32ui).CreateSliderCtrl

[PyCSliderCtrl](#README.md#PyCSliderCtrl)= **CreateSliderCtrl(** )
Creates a Slider control object.

#### Comments
The method **PySliderCtrl::CreateWindow** is used to 

create the actual control.

## [win32ui](#README.md#win32ui).CreateSplitter

[PyCSplitterWnd](#README.md#PyCSplitterWnd)= **CreateSplitter(** )
Creates a splitter window object.

## [win32ui](#README.md#win32ui).CreateStatusBar

[PyCStatusBar](#README.md#PyCStatusBar)= **CreateStatusBar( *parent*  *, style*  *, windowId*  *, ctrlStype* ** )
Creates a statusbar object.

#### Parameters


     *parent* :[PyCWnd](#README.md#PyCWnd)

    The parent window for the status bar.

     *style=afxres.WS_CHILD | afxres.WS_VISIBLE | afxres.CBRS_BOTTOM* : int

    The style for the status bar.

     *windowId=afxres.AFX_IDW_STATUS_BAR* : int

    The child window ID.

     *ctrlStype=0* : int

    Additional styles for the creation of the embedded[PyCStatusBarCtrl](#README.md#PyCStatusBarCtrl)object.
Status bar styles supported are:
commctrl.SBARS_SIZEGRIP - The status bar control includes a 

sizing grip at the right end of the status bar. A sizing grip is similar to a sizing border; 

it is a rectangular area that the user can click and drag to resize the parent window.
commctrl.SBT_TOOLTIPS - The status bar supports tooltips.

#### Comments
You must ensure no 2 status bars share the same ID.

#### MFC References


    CStatusBar::CreateEx

## [win32ui](#README.md#win32ui).CreateStatusBarCtrl

[PyCStatusBarCtrl](#README.md#PyCStatusBarCtrl)= **CreateStatusBarCtrl(** )
Creates a progress control object. **PyStatusBarCtrl::Create** creates the actual control.

## [win32ui](#README.md#win32ui).CreateThread

[PyCWinThread](#README.md#PyCWinThread)= **CreateThread(** )
Creates a new[PyCWinThread](#README.md#PyCWinThread)object

## [win32ui](#README.md#win32ui).CreateToolBar

[PyCToolBar](#README.md#PyCToolBar)= **CreateToolBar( *parent*  *, style*  *, windowId* ** )
Creates a toolbar object.

#### Parameters


     *parent* :[PyCWnd](#README.md#PyCWnd)

    The parent window for the toolbar.

     *style* : int

    The style for the toolbar.

     *windowId=afxres.AFX_IDW_TOOLBAR* : int

    The child window ID.

#### Comments
You must ensure no 2 toolbars share the same ID.

## [win32ui](#README.md#win32ui).CreateToolBarCtrl

[PyCToolBarCtrl](#README.md#PyCToolBarCtrl)= **CreateToolBarCtrl(** )
Creates a toolbar control object.[PyCToolBarCtrl::CreateWindow](#PyCToolBarCtrl.md#PyCToolBarCtrlCreateWindow)creates the actual control.

## [win32ui](#README.md#win32ui).CreateToolTipCtrl

[PyCToolTipCtrl](#README.md#PyCToolTipCtrl)= **CreateToolTipCtrl(** )
Creates a progress control object. **PyToolTipCtrl::Create** creates the actual control.

## [win32ui](#README.md#win32ui).CreateTreeCtrl

[PyCTreeCtrl](#README.md#PyCTreeCtrl)= **CreateTreeCtrl(** )
Creates a tree control.

## [win32ui](#README.md#win32ui).CreateTreeView

[PyCTreeView](#README.md#PyCTreeView)= **CreateTreeView( *doc* ** )
Creates a PyCTreeView object.

#### Parameters


     *doc* :[PyCDocument](#README.md#PyCDocument)

    The document to use with the view.

## [win32ui](#README.md#win32ui).CreateView

[PyCScrollView](#README.md#PyCScrollView)= **CreateView( *doc* ** )
Creates a generic view object.

#### Parameters


     *doc* :[PyCDocument](#README.md#PyCDocument)

    The document to use with the view.

## [win32ui](#README.md#win32ui).CreateWindowFromHandle

[PyCWnd](#README.md#PyCWnd)= **CreateWindowFromHandle( *hwnd* ** )
Creates a[PyCWnd](#README.md#PyCWnd)from an integer containing a HWND

#### Parameters


     *hwnd* : int

    The window handle.

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).CreateWnd

[PyCWnd](#README.md#PyCWnd)= **CreateWnd(** )
Creates an unitialized[PyCWnd](#README.md#PyCWnd)

## [win32ui](#README.md#win32ui).DestroyDebuggerThread

 **DestroyDebuggerThread(** )
Cleans up the debugger thread.  See[win32ui::CreateDebuggerThread](#win32ui.md#win32uiCreateDebuggerThread).

## [win32ui](#README.md#win32ui).DisplayTraceback

 **DisplayTraceback(** )
Displays a traceback in a dialog box.

## [win32ui](#README.md#win32ui).DoWaitCursor

 **DoWaitCursor( *code* ** )
Dispay a wait cursor.

#### Parameters


     *code* : int

    If this parameter is 0, the original cursor is restored. If 1, a wait cursor appears. If -1, the wait cursor ends.

## [win32ui](#README.md#win32ui).Enable3dControls

int = **Enable3dControls(** )
Enables 3d controls for the application.

#### Return Value
True if 3d controls could be enabled, false otherwise.

## [win32ui](#README.md#win32ui).EnableControlContainer

int = **EnableControlContainer(** )
Enables support for containment of OLE controls.

## FWS_ADDTOTITLE
 **const win32ui.FWS_ADDTOTITLE;** 
MFC Frame Window style extension.  Add document title to window title.

## FWS_PREFIXTITLE
 **const win32ui.FWS_PREFIXTITLE;** 
MFC Frame Window style extension.

## FWS_SNAPTOBARS
 **const win32ui.FWS_SNAPTOBARS;** 
MFC Frame Window style extension.

## [win32ui](#README.md#win32ui).FindWindow

[PyCWnd](#README.md#PyCWnd)= **FindWindow( *className*  *, windowName* ** )
Searches for the specified top-level window

#### Parameters


     *className* : string

    The window class name to find, else None

     *windowName* : string

    The window name (ie, title) to find, else None

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).FindWindowEx

[PyCWnd](#README.md#PyCWnd)= **FindWindowEx( *parentWindow*  *, childAfter*  *, className*  *, windowName* ** )
Searches for the specified top-level or child window

#### Parameters


     *parentWindow* :[PyCWnd](#README.md#PyCWnd)

    The parent whose children will be searched.  If None, the desktops window will be used.

     *childAfter* :[PyCWnd](#README.md#PyCWnd)

    The search begins with the next window in the Z order.  If None, all children are searched.

     *className* : string

    The window class name to find, else None

     *windowName* : string

    The window name (ie, title) to find, else None

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).FullPath

string = **FullPath( *path* ** )
Return the fully qualified path of a file name.

#### Parameters


     *path* : string

    The path name.

## [win32ui](#README.md#win32ui).GetActiveWindow

[PyCWnd](#README.md#PyCWnd)= **GetActiveWindow(** )
Retrieves the active window.

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).GetApp

[PyCWinApp](#README.md#PyCWinApp)= **GetApp(** )
Retrieves the application object.

#### Comments
There will only ever be one application object per application.

## [win32ui](#README.md#win32ui).GetAppName

int = **GetAppName(** )
Returns the application name.

## [win32ui](#README.md#win32ui).GetAppRegistryKey

 **GetAppRegistryKey(** )
Returns the registry key for the application.

## [win32ui](#README.md#win32ui).GetBytes

string = **GetBytes( *address*  *, size* ** )
Gets raw bytes from memory

#### Parameters


     *address* : int

    The memory address

     *size* : int

    The size to get.

#### Comments
This method is useful to help decode unknown notify messages. 

You must be very carefull when using this method.

#### Return Value
The result is a string with a length of size.

## [win32ui](#README.md#win32ui).GetCommandLine

string = **GetCommandLine(** )
Returns the application's command line.

#### Win32 API References


    Search for *GetCommandLine* at[msdn](#README.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetCommandLine),[google](#README.md#http://www.google.com/search?q=GetCommandLine)or[google groups](#README.md#http://groups.google.com/groups?q=GetCommandLine).

## [win32ui](#README.md#win32ui).GetDeviceCaps

int = **GetDeviceCaps( *hdc*  *, index* ** )
Calls the API version of GetDeviceCaps.  See also[PyCDC::GetDeviceCaps](#PyCDC.md#PyCDCGetDeviceCaps)

#### Parameters


     *hdc* : int

    

     *index* : int

    

## [win32ui](#README.md#win32ui).GetFileTitle

string = **GetFileTitle( *fileName* ** )
Given a file name, return its title

#### Parameters


     *fileName* : string

    The file name.

## [win32ui](#README.md#win32ui).GetFocus

[PyCWnd](#README.md#PyCWnd)= **GetFocus(** )
Retrieves the window with the focus.

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).GetForegroundWindow

[PyCWnd](#README.md#PyCWnd)= **GetForegroundWindow(** )
Retrieves the foreground window.

#### Return Value
The result is a[PyCWnd](#README.md#PyCWnd)(or derived) object, or a win32ui.error exception is raised.

## [win32ui](#README.md#win32ui).GetHalftoneBrush

[PyCBrush](#README.md#PyCBrush)= **GetHalftoneBrush(** )
Creates a new halftone brush object.

## [win32ui](#README.md#win32ui).GetInitialStateRequest

int = **GetInitialStateRequest(** )
Returns the requested state that the application start in.  This is the same as the parameter available to[PyCWnd::ShowWindow](#PyCWnd.md#PyCWndShowWindow)

#### Comments
In some cases, it may not be possible to start in the requested mode.  An application 

may start in its default mode, then set its mode to match the value returned from this method.

## [win32ui](#README.md#win32ui).GetMainFrame

[PyCWnd](#README.md#PyCWnd)= **GetMainFrame(** )
Returns a window object for the main application frame.

## [win32ui](#README.md#win32ui).GetName

string = **GetName(** )
Returns the name of the current executable.

## [win32ui](#README.md#win32ui).GetProfileFileName

string = **GetProfileFileName(** )
Returns the name of the INI file used by the application.

## [win32ui](#README.md#win32ui).GetProfileVal

int/string = **GetProfileVal( *section*  *, entry*  *, defValue* ** )
Returns a value from the application's INI file.

#### Parameters


     *section* : string

    The section in the INI file to read from.

     *entry* : string

    The entry within the section in the INI file to read.

     *defValue* : int/string

    The default value.  The type of this parameter determines the method's return type.

## [win32ui](#README.md#win32ui).GetRecentFileList

list = **GetRecentFileList(** )
Returns the entries in the applications Recent File List.

#### Return Value
A list of strings containing the fully qualified file names.

## [win32ui](#README.md#win32ui).GetRect

tuple = **GetRect(** )
Returns the rectangle of the main application frame.  See **PyCWnd::GetWindowRecr** for further details.

#### Return Value
A tuple of integers with (left, top, right, bottom)

## [win32ui](#README.md#win32ui).GetResource

[PyDLL](#README.md#PyDLL)= **GetResource(** )
Retrieve the object associated with the applications resources.

## [win32ui](#README.md#win32ui).GetThread

[PyCWinApp](#README.md#PyCWinApp)= **GetThread(** )
Retrieves the current thread object.

## [win32ui](#README.md#win32ui).GetType

object = **GetType(** )
Retrieves a Python Type object given its name

## IDB_BROWSER_HIER
 **const win32ui.IDB_BROWSER_HIER;** 
Id of built in bitmap for the browser

## IDB_DEBUGGER_HIER
 **const win32ui.IDB_DEBUGGER_HIER;** 


## IDB_HIERFOLDERS
 **const win32ui.IDB_HIERFOLDERS;** 
Id of built in bitmap for default hierarchical list

## IDC_ABOUT_VERSION
 **const win32ui.IDC_ABOUT_VERSION;** 
Id of 'Version' control

## IDC_AUTOCOMPLETE
 **const win32ui.IDC_AUTOCOMPLETE;** 


## IDC_AUTO_RELOAD
 **const win32ui.IDC_AUTO_RELOAD;** 


## IDC_BUTTON1
 **const win32ui.IDC_BUTTON1;** 


## IDC_BUTTON2
 **const win32ui.IDC_BUTTON2;** 


## IDC_BUTTON3
 **const win32ui.IDC_BUTTON3;** 


## IDC_BUTTON4
 **const win32ui.IDC_BUTTON4;** 


## IDC_CALLTIPS
 **const win32ui.IDC_CALLTIPS;** 


## IDC_CHECK1
 **const win32ui.IDC_CHECK1;** 


## IDC_CHECK2
 **const win32ui.IDC_CHECK2;** 


## IDC_CHECK3
 **const win32ui.IDC_CHECK3;** 


## IDC_COMBO1
 **const win32ui.IDC_COMBO1;** 


## IDC_COMBO2
 **const win32ui.IDC_COMBO2;** 


## IDC_EDIT1
 **const win32ui.IDC_EDIT1;** 


## IDC_EDIT2
 **const win32ui.IDC_EDIT2;** 


## IDC_EDIT3
 **const win32ui.IDC_EDIT3;** 


## IDC_EDIT4
 **const win32ui.IDC_EDIT4;** 


## IDC_EDIT_COLOE
 **const win32ui.IDC_EDIT_COLOE;** 


## IDC_EDIT_TABS
 **const win32ui.IDC_EDIT_TABS;** 


## IDC_INDENT_SIZE
 **const win32ui.IDC_INDENT_SIZE;** 


## IDC_KEYBOARD_CONFIG
 **const win32ui.IDC_KEYBOARD_CONFIG;** 


## IDC_LIST1
 **const win32ui.IDC_LIST1;** 


## IDC_PROMPT1
 **const win32ui.IDC_PROMPT1;** 


## IDC_PROMPT2
 **const win32ui.IDC_PROMPT2;** 


## IDC_PROMPT3
 **const win32ui.IDC_PROMPT3;** 


## IDC_PROMPT4
 **const win32ui.IDC_PROMPT4;** 


## IDC_PROMPT_TABS
 **const win32ui.IDC_PROMPT_TABS;** 


## IDC_RADIO1
 **const win32ui.IDC_RADIO1;** 


## IDC_RADIO2
 **const win32ui.IDC_RADIO2;** 


## IDC_RIGHTEDGE_COLUMN
 **const win32ui.IDC_RIGHTEDGE_COLUMN;** 


## IDC_RIGHTEDGE_DEFINE
 **const win32ui.IDC_RIGHTEDGE_DEFINE;** 


## IDC_RIGHTEDGE_ENABLE
 **const win32ui.IDC_RIGHTEDGE_ENABLE;** 


## IDC_RIGHTEDGE_SAMPLE
 **const win32ui.IDC_RIGHTEDGE_SAMPLE;** 


## IDC_SPIN1
 **const win32ui.IDC_SPIN1;** 


## IDC_SPIN2
 **const win32ui.IDC_SPIN2;** 


## IDC_SPIN3
 **const win32ui.IDC_SPIN3;** 


## IDC_TAB_SIZE
 **const win32ui.IDC_TAB_SIZE;** 


## IDC_USE_SMART_TABS
 **const win32ui.IDC_USE_SMART_TABS;** 


## IDC_USE_TABS
 **const win32ui.IDC_USE_TABS;** 


## IDC_VIEW_WHITESPACE
 **const win32ui.IDC_VIEW_WHITESPACE;** 


## IDC_VSS_INTEGRATE
 **const win32ui.IDC_VSS_INTEGRATE;** 


## IDD_ABOUTBOX
 **const win32ui.IDD_ABOUTBOX;** 
Id of built in 'About Box' dialog

## IDD_DUMMYPROPPAGE
 **const win32ui.IDD_DUMMYPROPPAGE;** 
Id of built in dummy property page

## IDD_GENERAL_STATUS
 **const win32ui.IDD_GENERAL_STATUS;** 
Id of a general status dialog box (fairly small, 3 static controls, minimize box)

## IDD_LARGE_EDIT
 **const win32ui.IDD_LARGE_EDIT;** 
Id of built in 'Large Edit' dialog (dialog box with a large edit control)

## IDD_PP_DEBUGGER
 **const win32ui.IDD_PP_DEBUGGER;** 


## IDD_PP_EDITOR
 **const win32ui.IDD_PP_EDITOR;** 
Id of built in 'Editor' property page

## IDD_PP_FORMAT
 **const win32ui.IDD_PP_FORMAT;** 
Id of built in 'Format' property page

## IDD_PP_IDE
 **const win32ui.IDD_PP_IDE;** 
Id of built in 'IDE' property page

## IDD_PP_TABS
 **const win32ui.IDD_PP_TABS;** 
Id of built in 'Tabs and Whitespace' property page

## IDD_PP_TOOLMENU
 **const win32ui.IDD_PP_TOOLMENU;** 
Id of built in 'ToolsMenu' property page

## IDD_PROPDEMO1
 **const win32ui.IDD_PROPDEMO1;** 
Id of built in Property Page demo dialog 1

## IDD_PROPDEMO2
 **const win32ui.IDD_PROPDEMO2;** 
Id of built in Property Page demo dialog 2

## IDD_RUN_SCRIPT
 **const win32ui.IDD_RUN_SCRIPT;** 
Id of built in 'Run Script' dialog

## IDD_SET_TABSTOPS
 **const win32ui.IDD_SET_TABSTOPS;** 
Id of built in 'Set Tab Stops' dialog

## IDD_SIMPLE_INPUT
 **const win32ui.IDD_SIMPLE_INPUT;** 
Id of built in 'Simple Input' property page.

## IDD_TREE
 **const win32ui.IDD_TREE;** 
Id of built in dialog with a tree control.

## IDD_TREE_MB
 **const win32ui.IDD_TREE_MB;** 
Id of built in dialog with a tree control with multiple buttons.

## IDR_CNTR_INPLACE
 **const win32ui.IDR_CNTR_INPLACE;** 


## IDR_DEBUGGER
 **const win32ui.IDR_DEBUGGER;** 


## IDR_MAINFRAME
 **const win32ui.IDR_MAINFRAME;** 


## IDR_PYTHONCONTYPE
 **const win32ui.IDR_PYTHONCONTYPE;** 


## IDR_PYTHONTYPE
 **const win32ui.IDR_PYTHONTYPE;** 


## IDR_PYTHONTYPE_CNTR_IP
 **const win32ui.IDR_PYTHONTYPE_CNTR_IP;** 


## IDR_TEXTTYPE
 **const win32ui.IDR_TEXTTYPE;** 


## ID_APP_ABOUT
 **const win32ui.ID_APP_ABOUT;** 


## ID_APP_EXIT
 **const win32ui.ID_APP_EXIT;** 


## ID_EDIT_CLEAR
 **const win32ui.ID_EDIT_CLEAR;** 


## ID_EDIT_CLEAR_ALL
 **const win32ui.ID_EDIT_CLEAR_ALL;** 


## ID_EDIT_COPY
 **const win32ui.ID_EDIT_COPY;** 


## ID_EDIT_CUT
 **const win32ui.ID_EDIT_CUT;** 


## ID_EDIT_FIND
 **const win32ui.ID_EDIT_FIND;** 


## ID_EDIT_GOTO_LINE
 **const win32ui.ID_EDIT_GOTO_LINE;** 


## ID_EDIT_PASTE
 **const win32ui.ID_EDIT_PASTE;** 


## ID_EDIT_REDO
 **const win32ui.ID_EDIT_REDO;** 


## ID_EDIT_REPEAT
 **const win32ui.ID_EDIT_REPEAT;** 


## ID_EDIT_REPLACE
 **const win32ui.ID_EDIT_REPLACE;** 


## ID_EDIT_SELECT_ALL
 **const win32ui.ID_EDIT_SELECT_ALL;** 


## ID_EDIT_SELECT_BLOCK
 **const win32ui.ID_EDIT_SELECT_BLOCK;** 


## ID_EDIT_UNDO
 **const win32ui.ID_EDIT_UNDO;** 


## ID_FILE_CHECK
 **const win32ui.ID_FILE_CHECK;** 


## ID_FILE_CLOSE
 **const win32ui.ID_FILE_CLOSE;** 


## ID_FILE_IMPORT
 **const win32ui.ID_FILE_IMPORT;** 


## ID_FILE_LOCATE
 **const win32ui.ID_FILE_LOCATE;** 


## ID_FILE_MRU_FILE1
 **const win32ui.ID_FILE_MRU_FILE1;** 


## ID_FILE_MRU_FILE2
 **const win32ui.ID_FILE_MRU_FILE2;** 


## ID_FILE_MRU_FILE3
 **const win32ui.ID_FILE_MRU_FILE3;** 


## ID_FILE_MRU_FILE4
 **const win32ui.ID_FILE_MRU_FILE4;** 


## ID_FILE_NEW
 **const win32ui.ID_FILE_NEW;** 


## ID_FILE_OPEN
 **const win32ui.ID_FILE_OPEN;** 


## ID_FILE_PAGE_SETUP
 **const win32ui.ID_FILE_PAGE_SETUP;** 


## ID_FILE_PRINT
 **const win32ui.ID_FILE_PRINT;** 


## ID_FILE_PRINT_PREVIEW
 **const win32ui.ID_FILE_PRINT_PREVIEW;** 


## ID_FILE_PRINT_SETUP
 **const win32ui.ID_FILE_PRINT_SETUP;** 


## ID_FILE_RUN
 **const win32ui.ID_FILE_RUN;** 


## ID_FILE_SAVE
 **const win32ui.ID_FILE_SAVE;** 


## ID_FILE_SAVE_ALL
 **const win32ui.ID_FILE_SAVE_ALL;** 


## ID_FILE_SAVE_AS
 **const win32ui.ID_FILE_SAVE_AS;** 


## ID_HELP_GUI_REF
 **const win32ui.ID_HELP_GUI_REF;** 


## ID_HELP_OTHER
 **const win32ui.ID_HELP_OTHER;** 


## ID_HELP_PYTHON
 **const win32ui.ID_HELP_PYTHON;** 


## ID_INDICATOR_COLNUM
 **const win32ui.ID_INDICATOR_COLNUM;** 


## ID_INDICATOR_LINENUM
 **const win32ui.ID_INDICATOR_LINENUM;** 


## ID_NEXT_PANE
 **const win32ui.ID_NEXT_PANE;** 


## ID_PREV_PANE
 **const win32ui.ID_PREV_PANE;** 


## ID_SEPARATOR
 **const win32ui.ID_SEPARATOR;** 


## ID_VIEW_BROWSE
 **const win32ui.ID_VIEW_BROWSE;** 


## ID_VIEW_EOL
 **const win32ui.ID_VIEW_EOL;** 


## ID_VIEW_FIXED_FONT
 **const win32ui.ID_VIEW_FIXED_FONT;** 


## ID_VIEW_FOLD_COLLAPSE
 **const win32ui.ID_VIEW_FOLD_COLLAPSE;** 


## ID_VIEW_FOLD_COLLAPSE_ALL
 **const win32ui.ID_VIEW_FOLD_COLLAPSE_ALL;** 


## ID_VIEW_FOLD_EXPAND
 **const win32ui.ID_VIEW_FOLD_EXPAND;** 


## ID_VIEW_FOLD_EXPAND_ALL
 **const win32ui.ID_VIEW_FOLD_EXPAND_ALL;** 


## ID_VIEW_FOLD_TOGGLE
 **const win32ui.ID_VIEW_FOLD_TOGGLE;** 


## ID_VIEW_INDENTATIONGUIDES
 **const win32ui.ID_VIEW_INDENTATIONGUIDES;** 


## ID_VIEW_INTERACTIVE
 **const win32ui.ID_VIEW_INTERACTIVE;** 


## ID_VIEW_OPTIONS
 **const win32ui.ID_VIEW_OPTIONS;** 


## ID_VIEW_RIGHT_EDGE
 **const win32ui.ID_VIEW_RIGHT_EDGE;** 


## ID_VIEW_STATUS_BAR
 **const win32ui.ID_VIEW_STATUS_BAR;** 


## ID_VIEW_TOOLBAR
 **const win32ui.ID_VIEW_TOOLBAR;** 


## ID_VIEW_TOOLBAR_DBG
 **const win32ui.ID_VIEW_TOOLBAR_DBG;** 


## ID_VIEW_WHITESPACE
 **const win32ui.ID_VIEW_WHITESPACE;** 


## ID_WINDOW_ARRANGE
 **const win32ui.ID_WINDOW_ARRANGE;** 


## ID_WINDOW_CASCADE
 **const win32ui.ID_WINDOW_CASCADE;** 


## ID_WINDOW_NEW
 **const win32ui.ID_WINDOW_NEW;** 


## ID_WINDOW_SPLIT
 **const win32ui.ID_WINDOW_SPLIT;** 


## ID_WINDOW_TILE_HORZ
 **const win32ui.ID_WINDOW_TILE_HORZ;** 


## ID_WINDOW_TILE_VERT
 **const win32ui.ID_WINDOW_TILE_VERT;** 


## [win32ui](#README.md#win32ui).InitRichEdit

string = **InitRichEdit(** )
Initializes the rich edit framework.

## [win32ui](#README.md#win32ui).InstallCallBackCaller

object = **InstallCallBackCaller(** )
Install a Python method which will dispatch all callbacks into Python.

#### Return Value
The previous callback caller.

## [win32ui](#README.md#win32ui).IsDebug

int = **IsDebug(** )
Returns a flag indicating if the current win32ui build is a DEBUG build.

#### Comments
This should not normally be of relevance to the Python 

programmer.  However, under certain circumstances Python code may 

wish to detect this.

## [win32ui](#README.md#win32ui).IsObject

int = **IsObject( *o* ** )
Determines if the passed object is a win32ui object.

#### Parameters


     *o* : object

    The object to check.

## [win32ui](#README.md#win32ui).IsWin32s

int = **IsWin32s(** )
Determines if the application is running under Win32s.

## LM_COMMIT
 **const win32ui.LM_COMMIT;** 
Remember MRUWidth

## LM_HORZ
 **const win32ui.LM_HORZ;** 
same as bHorz in CalcFixedLayout

## LM_HORZDOCK
 **const win32ui.LM_HORZDOCK;** 
Horizontal Docked Dimensions

## LM_LENGTHY
 **const win32ui.LM_LENGTHY;** 
Set if nLength is a Height instead of a Width

## LM_MRUWIDTH
 **const win32ui.LM_MRUWIDTH;** 
Most Recently Used Dynamic Width

## LM_STRETCH
 **const win32ui.LM_STRETCH;** 
same meaning as bStretch in CalcFixedLayout.  If set, ignores nLength and returns dimensions based on LM_HORZ state, otherwise LM_HORZ is used to determine if nLength is the desired horizontal or vertical length and dimensions are returned based on nLength

## LM_VERTDOCK
 **const win32ui.LM_VERTDOCK;** 
Vertical Docked Dimensions

## [win32ui](#README.md#win32ui).LoadDialogResource

list = **LoadDialogResource( *idRes*  *, dll* ** )
Loads a dialog resource, and returns a list detailing the objects.

#### Parameters


     *idRes* : int

    The ID of the dialog resource to load.

     *dll=None* :[PyDLL](#README.md#PyDLL)

    The DLL object to load the dialog from.

## [win32ui](#README.md#win32ui).LoadLibrary

[PyDLL](#README.md#PyDLL)= **LoadLibrary( *fileName* ** )
Creates a DLL object, and loads a Windows DLL into the object.

#### Parameters


     *fileName* : string

    The name of the DLL file to load.

## [win32ui](#README.md#win32ui).LoadMenu

[PyCMenu](#README.md#PyCMenu)= **LoadMenu( *id*  *, dll* ** )
Creates and loads a menu resource from a DLL.

#### Parameters


     *id* : int

    The Id of the menu to load.

     *dll=None* :[PyDLL](#README.md#PyDLL)

    The DLL to load from.

## [win32ui](#README.md#win32ui).LoadStdProfileSettings

 **LoadStdProfileSettings( *maxFiles* ** )
Loads MFC standard settings from the applications INI file.  This includes the Recent File List, etc.

#### Parameters


     *maxFiles=_AFX_MRU_COUNT* : int

    The maximum number of files to maintain on the Recently Used File list.

#### Comments
This function can only be called once in an applications lifetime, else an exception is raised.

## [win32ui](#README.md#win32ui).LoadString

[PyUnicode](#README.md#PyUnicode)= **LoadString( *stringId* ** )
Loads a string from a resource file.

#### Parameters


     *stringId* : int

    The ID of the string to load.

## MFS_4THICKFRAME
 **const win32ui.MFS_4THICKFRAME;** 
thick frame all around (no tiles)

## MFS_BLOCKSYSMENU
 **const win32ui.MFS_BLOCKSYSMENU;** 
block hit testing on system menu

## MFS_MOVEFRAME
 **const win32ui.MFS_MOVEFRAME;** 
no sizing, just moving

## MFS_SYNCACTIVE
 **const win32ui.MFS_SYNCACTIVE;** 
syncronize activation w/ parent

## MFS_THICKFRAME
 **const win32ui.MFS_THICKFRAME;** 
use instead of WS_THICKFRAME

## [win32ui](#README.md#win32ui).MessageBox

int = **MessageBox( *message*  *, title*  *, style* ** )
Display a message box.

#### Parameters


     *message* : string

    The message to be displayed in the message box.

     *title=None* : string/None

    The title for the message box.  If None, the applications title will be used.

     *style=win32con.MB_OK* : int

    The style of the message box.

#### Return Value
An integer identifying the button pressed to dismiss the dialog.

## [win32ui](#README.md#win32ui).OutputDebugString

 **OutputDebugString( *msg* ** )
Sends a string to the Windows debugging device.

#### Parameters


     *msg* : string

    The string to write.

## PD_ALLPAGES
 **const win32ui.PD_ALLPAGES;** 
The default flag that indicates that the All radio button is initially selected. This flag is used as a placeholder to indicate that the PD_PAGENUMS and PD_SELECTION flags are not specified.

## PD_COLLATE
 **const win32ui.PD_COLLATE;** 
If this flag is set, the Collate check box is checked. If this flag is set when the PrintDlg function returns, the application must simulate collation of multiple copies. For more information, see the description of the PD_USEDEVMODECOPIESANDCOLLATE flag.

## PD_DISABLEPRINTTOFILE
 **const win32ui.PD_DISABLEPRINTTOFILE;** 
Disables the Print to File check box.

## PD_ENABLEPRINTHOOK
 **const win32ui.PD_ENABLEPRINTHOOK;** 
Enables the hook procedure specified in the lpfnPrintHook member. This enables the hook procedure for the Print dialog box.

## PD_ENABLEPRINTTEMPLATE
 **const win32ui.PD_ENABLEPRINTTEMPLATE;** 
PD_ENABLEPRINTTEMPLATE

## PD_ENABLEPRINTTEMPLATEHANDLE
 **const win32ui.PD_ENABLEPRINTTEMPLATEHANDLE;** 
Indicates that the hPrintTemplate member identifies a data block that contains a preloaded dialog box template. This template replaces the default template for the Print dialog box. The system ignores the lpPrintTemplateName member if this flag is specified.

## PD_ENABLESETUPHOOK
 **const win32ui.PD_ENABLESETUPHOOK;** 
Enables the hook procedure specified in the lpfnSetupHook member. This enables the hook procedure for the Print Setup dialog box.

## PD_ENABLESETUPTEMPLATE
 **const win32ui.PD_ENABLESETUPTEMPLATE;** 
Indicates that the hInstance and lpSetupTemplateName members specify a replacement for the default Print Setup dialog box template.

## PD_ENABLESETUPTEMPLATEHANDLE
 **const win32ui.PD_ENABLESETUPTEMPLATEHANDLE;** 
Indicates that the hSetupTemplate member identifies a data block that contains a preloaded dialog box template. This template replaces the default template for the Print Setup dialog box. The system ignores the lpSetupTemplateName member if this flag is specified.

## PD_HIDEPRINTTOFILE
 **const win32ui.PD_HIDEPRINTTOFILE;** 
Hides the Print to File check box.

## PD_NONETWORKBUTTON
 **const win32ui.PD_NONETWORKBUTTON;** 
Hides and disables the Network button.

## PD_NOPAGENUMS
 **const win32ui.PD_NOPAGENUMS;** 
Disables the Pages radio button and the associated edit controls.

## PD_NOSELECTION
 **const win32ui.PD_NOSELECTION;** 
Disables the Selection radio button.

## PD_NOWARNING
 **const win32ui.PD_NOWARNING;** 
Prevents the warning message from being displayed when there is no default printer.

## PD_PAGENUMS
 **const win32ui.PD_PAGENUMS;** 
If this flag is set, the Pages radio button is selected. If this flag is set when the PrintDlg function returns, the nFromPage and nFromPage members indicate the starting and ending pages specified by the user.

## PD_PRINTSETUP
 **const win32ui.PD_PRINTSETUP;** 
Causes the system to display the Print Setup dialog box rather than the Print dialog box.

## PD_PRINTTOFILE
 **const win32ui.PD_PRINTTOFILE;** 
If this flag is set, the Print to File check box is selected. If this flag is set when the PrintDlg function returns, the offset indicated by the wOutputOffset member of the DEVNAMES structure contains the string "FILE:". When you call theStartDoc function to start the printing operation, specify this "FILE:" string in the lpszOutput member of theDOCINFO structure. Specifying this string causes the print subsystem to query the user for the name of the output file.

## PD_RETURNDC
 **const win32ui.PD_RETURNDC;** 
Causes PrintDlg to return a device context matching the selections the user made in the dialog box. The device context is returned in hDC.

## PD_RETURNDEFAULT
 **const win32ui.PD_RETURNDEFAULT;** 
If this flag is set, the PrintDlg function does not display the dialog box. Instead, it sets the hDevNames and hDevMode members to handles toDEVMODE and DEVNAMES structures that are initialized for the system default printer. Both hDevNames and hDevMode must be NULL, or PrintDlg returns an error. If the system default printer is supported by an old printer driver (earlier than Windows version 3.0), only hDevNames is returned; hDevMode is NULL.

## PD_RETURNIC
 **const win32ui.PD_RETURNIC;** 
Similar to the PD_RETURNDC flag, except this flag returns an information context rather than a device context. If neither PD_RETURNDC nor PD_RETURNIC is specified, hDC is undefined on output.

## PD_SELECTION
 **const win32ui.PD_SELECTION;** 
If this flag is set, the Selection radio button is selected. If neither PD_PAGENUMS nor PD_SELECTION is set, the All radio button is selected.

## PD_SHOWHELP
 **const win32ui.PD_SHOWHELP;** 
Causes the dialog box to display the Help button. The hwndOwner member must specify the window to receive the HELPMSGSTRING registered messages that the dialog box sends when the user clicks the Help button.

## PD_USEDEVMODECOPIES
 **const win32ui.PD_USEDEVMODECOPIES;** 
Same as PD_USEDEVMODECOPIESANDCOLLATE

## PD_USEDEVMODECOPIESANDCOLLATE
 **const win32ui.PD_USEDEVMODECOPIESANDCOLLATE;** 
This flag indicates whether your application supports multiple copies and collation. Set this flag on input to indicate that your application does not support multiple copies and collation. In this case, the nCopies member of the PRINTDLG structure always returns 1, and PD_COLLATE is never set in the Flags member. If this flag is not set, the application is responsible for printing and collating multiple copies. In this case, the nCopies member of the PRINTDLG structure indicates the number of copies the user wants to print, and the PD_COLLATE flag in the Flags member indicates whether the user wants collation. Regardless of whether this flag is set, an application can determine from nCopies and PD_COLLATE how many copies to render and whether to print them collated.  If this flag is set and the printer driver does not support multiple copies, the Copies edit control is disabled. Similarly, if this flag is set and

## PSWIZB_BACK
 **const win32ui.PSWIZB_BACK;** 
Enable/Disable the Property sheet Back button

## PSWIZB_DISABLEDFINISH
 **const win32ui.PSWIZB_DISABLEDFINISH;** 
Enable/Disable the Property sheet disabled Finish button

## PSWIZB_FINISH
 **const win32ui.PSWIZB_FINISH;** 
Enable/Disable the Property sheet Finish button

## PSWIZB_NEXT
 **const win32ui.PSWIZB_NEXT;** 
Enable/Disable the Property sheet Next button

## [win32ui](#README.md#win32ui).PrintTraceback

 **PrintTraceback( *tb*  *, output* ** )
Prints a traceback using the internal Python mechanism.

#### Parameters


     *tb* : object

    The traceback to print.

     *output* : object

    The object to write the traceback to.

## [win32ui](#README.md#win32ui).PumpWaitingMessages

int = **PumpWaitingMessages( *firstMessage*  *, lastMessage* ** )
Recursively start a new message dispatching loop while any message remain in the queue.

#### Parameters


     *firstMessage=WM_PAINT* : int

    The lowest message ID to retrieve

     *lastMessage=WM_PAINT* : int

    The highest message ID to retrieve

#### Comments
This allows an application which is performing a long operation to dispatch paint messages during the operation.

#### Return Value
The result is 1 if a WM_QUIT message was processed, otherwise 0.

## [win32ui](#README.md#win32ui).RegisterWndClass

string = **RegisterWndClass( *style*  *, hCursor*  *, hBrush*  *, hIcon* ** )
Registers a window class

#### Parameters


     *style* : int

    Specifies the Windows class style or combination of styles

     *hCursor=0* : int

    

     *hBrush=0* : int

    

     *hIcon=0* : int

    

#### Comments
The Microsoft Foundation Class Library automatically registers several standard window classes for you. Call this function if you want to register your own window classes.

## [win32ui](#README.md#win32ui).RemoveRecentFile

 **RemoveRecentFile( *index* ** )
Removes the entry in the applications Recent File List at index.

#### Parameters


     *index=0* : int

    Zero-based index of the file to be removed from the MRU (most recently used) file list.

## [win32ui](#README.md#win32ui).SetAppHelpPath

int = **SetAppHelpPath(** )
Set the pApp-&gtm_pszHelpFilePath variable.

## [win32ui](#README.md#win32ui).SetAppName

int = **SetAppName( *appName* ** )
Sets the name of the application.

#### Parameters


     *appName* : string

    The new name for the application.  This is used for the default registry key, and the title bar of the application.

#### MFC References


    CWinApp::m_pszAppName

## [win32ui](#README.md#win32ui).SetCurrentInstanceHandle

int = **SetCurrentInstanceHandle( *newVal* ** )
Sets the MFC variable afxCurrentInstanceHandle

#### Parameters


     *newVal* : int

    The new value for afxCurrentInstanceHandle

#### Return Value
The result is the previous value of afxCurrentInstanceHandle

## [win32ui](#README.md#win32ui).SetCurrentResourceHandle

int = **SetCurrentResourceHandle( *newVal* ** )
Sets the MFC variable afxCurrentResourceHandle

#### Parameters


     *newVal* : int

    The new value for afxCurrentResourceHandle

#### Return Value
The result is the previous value of afxCurrentResourceHandle

## [win32ui](#README.md#win32ui).SetDialogBkColor

int = **SetDialogBkColor( *clrCtlBk*  *, clrCtlText* ** )
Sets the default background and text color for dialog boxes and message boxes within the application.

#### Parameters


     *clrCtlBk=win32ui.RGB(192, 192, 192)* : int

    The color for the controls background.

     *clrCtlText=win32ui.RGB(0, 0, 0)* : int

    The color for the controls text.

#### MFC References


    CWinApp::SetDialogBkColor

## [win32ui](#README.md#win32ui).SetProfileFileName

 **SetProfileFileName( *filename* ** )
Sets the name of the INI file used by the application.

#### Parameters


     *filename* : string

    The name of the ini file.

## [win32ui](#README.md#win32ui).SetRegistryKey

 **SetRegistryKey( *key* ** )
Causes application settings to be stored in the registry instead of INI files.

#### Parameters


     *key* : string

    A string containing the name of the key.

#### Comments
Causes application settings to be stored in the registry instead of INI files. This function sets m_pszRegistryKey, which 

is then used by the GetProfileXXX and WriteProfileXXX member functions of CWinApp. If this function has been 

called, the list of most recently-used (MRU) files is also stored in the registry. The registry key is usually the name of a 

company. It is stored in a key of the following form: 

HKEY_CURRENT_USER\\Software\\&ltcompany name&gt\\&ltapplication name&gt\\&ltsection name&gt\\&ltvalue name&gt.

## [win32ui](#README.md#win32ui).SetResource

[PyDLL](#README.md#PyDLL)= **SetResource( *dll* ** )
Specifies the default DLL object for application resources.

#### Parameters


     *dll* :[PyDll](#README.md#PyDll)

    The dll object to use for default resources.

#### Return Value
The previous default DLL object.

## [win32ui](#README.md#win32ui).SetStatusText

 **SetStatusText( *msg*  *, bForce* ** )
Sets the text in the status bar of the application.

#### Parameters


     *msg* : string

    The message to write to the status bar.

     *bForce=0* : int

    A flag indicating if the message should be forced to the status bar, or written in idle time.

## [win32ui](#README.md#win32ui).StartDebuggerPump

 **StartDebuggerPump(** )
Starts a recursive message loop, waiting for an application close message.

#### Comments
This function is used by the debugger.  It allows the debugger to 

interact with the user, even while the Python code is stopped. 

As the Python code may be responding to a Windows Event, this function 

works around the inherent message queue problems.

## [win32ui](#README.md#win32ui).StopDebuggerPump

 **StopDebuggerPump(** )
Stops the debugger pump.  See[win32ui::StartDebuggerPump](#win32ui.md#win32uiStartDebuggerPump).

## [win32ui](#README.md#win32ui).TranslateMessage

int = **TranslateMessage(** )
Calls the API version of TranslateMessage.

## [win32ui](#README.md#win32ui).TranslateVirtualKey

string/None = **TranslateVirtualKey( *vk* ** )


#### Parameters


     *vk* : int

    The key to translate

## [win32ui](#README.md#win32ui).WinHelp

 **WinHelp( *cmd*  *, data* ** )
Invokes the Windows Help system.

#### Parameters


     *cmd=win32con.HELP_CONTEXT* : int

    The type of help.  See the api for full details.

     *data* : int/string

    Additional data specific to the help call.

## [win32ui](#README.md#win32ui).WriteProfileVal

 **WriteProfileVal( *section*  *, entry*  *, value* ** )
Writes a value to the application's INI file.

#### Parameters


     *section* : string

    The section in the INI file to write to.

     *entry* : string

    The entry within the section in the INI file to write to.

     *value* : int/string

    The value to write. The type of this parameter determines the method's return type.

## debug
 **const win32ui.debug;** 
1 if we are current using a _DEBUG build of win32ui, else 0.