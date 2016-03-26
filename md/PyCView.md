# PyCView

## PyCView Object

A class which implements a generic CView.  Derived from a[PyCWnd](#pycwnd)object.

#### Methods


  - [CreateWindow](PyCView.md#pycviewcreatewindow)

    Create the window for a view.&nbsp;

  - [GetDocument](PyCView.md#pycviewgetdocument)

    Returns the document for a view.&nbsp;

  - [OnActivateView](PyCView.md#pycviewonactivateview)

    Calls the underlying MFC OnActivateView method.&nbsp;

  - [OnInitialUpdate](PyCView.md#pycviewoninitialupdate)

    Calls the underlying MFC OnInitialUpdate method.&nbsp;

  - [OnMouseActivate](PyCView.md#pycviewonmouseactivate)

    Calls the underlying MFC OnMouseActivate method.&nbsp;

  - [PreCreateWindow](PyCView.md#pycviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method.&nbsp;

  - [OnFilePrint](PyCView.md#pycviewonfileprint)

    Calls the underlying MFC OnFilePrint method.&nbsp;

  - [OnFilePrint](PyCView.md#pycviewonfileprint)

    Calls the underlying MFC OnFilePrintPreview method.&nbsp;

  - [DoPreparePrinting](PyCView.md#pycviewdoprepareprinting)

    Calls the underlying MFC DoPreparePrinting method.&nbsp;

  - [OnBeginPrinting](PyCView.md#pycviewonbeginprinting)

    Calls the underlying MFC OnBeginPrinting method.&nbsp;

  - [OnEndPrinting](PyCView.md#pycviewonendprinting)

    Calls the underlying MFC OnEndPrinting method.&nbsp;


## [PyCView](#pycview).CreateWindow

 __CreateWindow( *parent*  *, id*  *, style*  *, rect* __ )
Creates the window for a view.

#### Parameters


  -  *parent* :[PyCWnd](#pycwnd)

    The parent window (usually a frame)

  -  *id=win32ui.AFX_IDW_PANE_FIRST* : int

    The child ID for the view

  -  *style=win32ui.AFX_WS_DEFAULT_VIEW* : int

    The style for the view

  -  *rect=(0,0,0,0)* : (left, top, right, bottom)

    The default position of the window.

## [PyCView](#pycview).DoPreparePrinting

int = __DoPreparePrinting(__ )
Invoke the Print dialog box and create a printer device context.

#### Comments
This function is usually called from[PyCView.OnPreparePrinting](PyCView.md#pycviewonprepareprinting_virtual)virtual method

## [PyCView](#pycview).GetDocument

[PyCDocument](#pycdocument)= __GetDocument(__ )
Returns the document for a view.

## [PyCView](#pycview).OnActivateView

int = __OnActivateView( *activate*  *, activateView*  *, DeactivateView* __ )
Calls the underlying MFC OnActivateView method.

#### Parameters


  -  *activate* : int

    Indicates whether the view is being activated or deactivated.

  -  *activateView* :[PyCView](#pycview)

    The view object that is being activated.

  -  *DeactivateView* :[PyCView](#pycview)

    The view object that is being deactivated.

#### See Also


  - [PyCView.OnActivateView](PyCView.md#pycviewonactivateview_virtual)virtual method

## [PyCView.OnActivateView](#pycview)Virtual

 __OnActivateView( *bActivate*  *, activateView*  *, DeactivateView* __ )
Called by the framework when a view is activated or deactivated.

#### Parameters


  -  *bActivate* : int

    Indicates whether the view is being activated or deactivated.

  -  *activateView* :[PyCWnd](#pycwnd)

    The view object that is being activated.

  -  *DeactivateView* :[PyCWnd](#pycwnd)

    The view object that is being deactivated.

#### Comments
If a handler exists, the base MFC implementation is not called.
The activateView and deactiveView parameters are the same objects if the 

application's main frame window is activated with no change in the 

active view for example, if the focus is being transferred from 

another application to this one, rather than from one view to 

another within the application. 

This allows a view to re-realize its palette, if needed.

#### See Also


  - [PyCView::OnActivateView](PyCView.md#pycviewonactivateview)

## [PyCView](#pycview).OnBeginPrinting

 __OnBeginPrinting(__ )
Calls the underlying MFC OnBeginPrinting method.

#### See Also


  - [PyCView.OnBeginPrinting](PyCView.md#pycviewonbeginprinting_virtual)virtual method

## [PyCView.OnBeginPrinting](#pycview)Virtual

 __OnBeginPrinting( *dc*  *, pInfo* __ )
Called by the framework at the beginning of a print or print preview job, after OnPreparePrinting has been called.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The DC object.

  -  *pInfo* :[PyCPrintInfo](#pycprintinfo)

    The print info object.

#### See Also


  - [PyCView::OnBeginPrinting](PyCView.md#pycviewonbeginprinting)

## [PyCView.OnDraw](#pycview)Virtual

 __OnDraw( *dc* __ )
Called when the view should be drawn.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The DC object.

#### See Also


  -  __PyCView::OnDraw__ 

## [PyCView](#pycview).OnEndPrinting

 __OnEndPrinting(__ )
Calls the underlying MFC OnEndPrinting method.

#### See Also


  - [PyCView.OnEndPrinting](PyCView.md#pycviewonendprinting_virtual)virtual method

## [PyCView.OnEndPrinting](#pycview)Virtual

 __OnEndPrinting( *dc*  *, pInfo* __ )
Called by the framework after a document has been printed or previewed.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The DC object.

  -  *pInfo* :[PyCPrintInfo](#pycprintinfo)

    The print info object.

#### See Also


  - [PyCView::OnEndPrinting](PyCView.md#pycviewonendprinting)

## [PyCView](#pycview).OnFilePrint

 __OnFilePrint(__ )
Calls the underlying MFC OnFilePrint method.

## [PyCView](#pycview).OnFilePrintPreview

 __OnFilePrintPreview(__ )
Calls the underlying MFC OnFilePrintPreview method.

## [PyCView](#pycview).OnInitialUpdate

 __OnInitialUpdate(__ )
Calls the underlying MFC OnInitialUpdate method.

#### See Also


  - [PyCView.OnInitialUpdate](PyCView.md#pycviewoninitialupdate_virtual)virtual method

## [PyCView.OnInitialUpdate](#pycview)Virtual

 __OnInitialUpdate(__ )
Called before the first update for a view.

#### Comments
The MFC base class is called only if no handler exists.

#### See Also


  - [PyCView::OnInitialUpdate](PyCView.md#pycviewoninitialupdate)

## [PyCView](#pycview).OnMouseActivate

int = __OnMouseActivate( *wnd*  *, hittest*  *, message* __ )
Calls the base MFC OnMouseActivate function.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    

  -  *hittest* : int

    

  -  *message* : int

    

#### See Also


  - [PyCWnd.OnMouseActivate](PyCWnd.md#pycwndonmouseactivate_virtual)virtual method

## [PyCView](#pycview).OnPrepareDC

 __OnPrepareDC(__ )
Calls the underlying MFC OnPrepareDC method.

#### See Also


  - [PyCView.OnPrepareDC](PyCView.md#pycviewonpreparedc_virtual)virtual method

## [PyCView.OnPrepareDC](#pycview)Virtual

 __OnPrepareDC( *dc*  *, pInfo* __ )
Called to prepare the device context for a view.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The DC object.

  -  *pInfo* :[PyCPrintInfo](#pycprintinfo)

    The print info object.

#### See Also


  -  __PyCWnd::OnPrepareDC__ 

## [PyCView](#pycview).OnPreparePrinting

int = __OnPreparePrinting(__ )
Calls the underlying MFC OnPreparePrinting method.

#### See Also


  - [PyCView.OnPreparePrinting](PyCView.md#pycviewonprepareprinting_virtual)virtual method

## [PyCView.OnPreparePrinting](#pycview)Virtual

 __OnPreparePrinting( *pInfo* __ )
Called by the framework before a document is printed or previewed

#### Parameters


  -  *pInfo* :[PyCPrintInfo](#pycprintinfo)

    The print info object.

#### See Also


  - [PyCView::OnPreparePrinting](PyCView.md#pycviewonprepareprinting)

## [PyCView.OnPrint](#pycview)Virtual

 __OnPrint( *dc*  *, pInfo* __ )
Called when the view should be printed.

#### Parameters


  -  *dc* :[PyCDC](#pycdc)

    The DC object.

  -  *pInfo* : __PyPrintInfo__ 

    The PrintIfo object.

#### See Also


  -  __PyCView::OnPrint__ 

## [PyCView.OnUpdate](#pycview)Virtual

 __OnUpdate( *sender*  *, lHint*  *, hint* __ )
Called by the framework when a view needs updating.

#### Parameters


  -  *sender* :[PyCView](#pycview)

    

  -  *lHint* : int

    

  -  *hint* : object

    

#### Comments
Typically you should not perform any drawing directly from OnUpdate. 

Instead, determine the rectangle describing, in device coordinates, the 

area that requires updating; pass this rectangle to[PyCWnd::InvalidateRect](PyCWnd.md#pycwndinvalidaterect). 

You can then paint the update next __PyCView::OnDraw__ 

#### See Also


  -  __PyCView::OnUpdate__ 

## [PyCView](#pycview).PreCreateWindow

tuple = __PreCreateWindow( *createStruct* __ )
Calls the underlying MFC PreCreateWindow method.

#### Parameters


  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure.

#### See Also


  - [PyCWnd.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual)virtual method