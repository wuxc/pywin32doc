# PyCView


## PyCView Object

A class which implements a generic CView\.  Derived from a [PyCWnd](PyCWnd.md) object\.

#### Methods

  - [CreateWindow](PyCView.md#pycviewcreatewindow)

    Create the window for a view\.&nbsp;

  - [GetDocument](PyCView.md#pycviewgetdocument)

    Returns the document for a view\.&nbsp;

  - [OnActivateView](PyCView.md#pycviewonactivateview)

    Calls the underlying MFC OnActivateView method\.&nbsp;

  - [OnInitialUpdate](PyCView.md#pycviewoninitialupdate)

    Calls the underlying MFC OnInitialUpdate method\.&nbsp;

  - [OnMouseActivate](PyCView.md#pycviewonmouseactivate)

    Calls the underlying MFC OnMouseActivate method\.&nbsp;

  - [PreCreateWindow](PyCView.md#pycviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [OnFilePrint](PyCView.md#pycviewonfileprint)

    Calls the underlying MFC OnFilePrint method\.&nbsp;

  - [OnFilePrint](PyCView.md#pycviewonfileprint)

    Calls the underlying MFC OnFilePrintPreview method\.&nbsp;

  - [DoPreparePrinting](PyCView.md#pycviewdoprepareprinting)

    Calls the underlying MFC DoPreparePrinting method\.&nbsp;

  - [OnBeginPrinting](PyCView.md#pycviewonbeginprinting)

    Calls the underlying MFC OnBeginPrinting method\.&nbsp;

  - [OnEndPrinting](PyCView.md#pycviewonendprinting)

    Calls the underlying MFC OnEndPrinting method\.&nbsp;




## [PyCView](PyCView.md#pycview)\.CreateWindow

CreateWindow\(parent, id, style, rect\)
Creates the window for a view\.

#### Parameters

  - parent : [PyCWnd](PyCWnd.md)

    The parent window \(usually a frame\)

  - id=win32ui\.AFX\_IDW\_PANE\_FIRST : int

    The child ID for the view

  - style=win32ui\.AFX\_WS\_DEFAULT\_VIEW : int

    The style for the view

  - rect=\(0,0,0,0\) : \(left, top, right, bottom\)

    The default position of the window\.


## [PyCView](PyCView.md#pycview)\.DoPreparePrinting

int = DoPreparePrinting\(\)
Invoke the Print dialog box and create a printer device context\.

#### Comments

This function is usually called from [PyCView\.OnPreparePrinting](PyCView.md#pycviewonprepareprinting_virtual) virtual method


## [PyCView](PyCView.md#pycview)\.GetDocument

[PyCDocument](PyCDocument.md) = GetDocument\(\)
Returns the document for a view\.


## [PyCView](PyCView.md#pycview)\.OnActivateView

int = OnActivateView\(activate, activateView

, DeactivateView

\)
Calls the underlying MFC OnActivateView method\.

#### Parameters

  - activate : int

    Indicates whether the view is being activated or deactivated\.

  - activateView : [PyCView](PyCView.md#pycview)

    The view object that is being activated\.

  - DeactivateView : [PyCView](PyCView.md#pycview)

    The view object that is being deactivated\.

#### See Also

  - [PyCView\.OnActivateView](PyCView.md#pycviewonactivateview_virtual) virtual method


## [PyCView\.OnActivateView](PyCView.md#pycview) Virtual

OnActivateView\(bActivate, activateView

, DeactivateView

\)
Called by the framework when a view is activated or deactivated\.

#### Parameters

  - bActivate : int

    Indicates whether the view is being activated or deactivated\.

  - activateView : [PyCWnd](PyCWnd.md)

    The view object that is being activated\.

  - DeactivateView : [PyCWnd](PyCWnd.md)

    The view object that is being deactivated\.

#### Comments

If a handler exists, the base MFC implementation is not called\. 

The activateView and deactiveView parameters are the same objects if the 

application's main frame window is activated with no change in the 

active view for example, if the focus is being transferred from 

another application to this one, rather than from one view to 

another within the application\. 

This allows a view to re-realize its palette, if needed\.

#### See Also

  - [PyCView::OnActivateView](PyCView.md#pycviewonactivateview)


## [PyCView](PyCView.md#pycview)\.OnBeginPrinting

OnBeginPrinting\(\)
Calls the underlying MFC OnBeginPrinting method\.

#### See Also

  - [PyCView\.OnBeginPrinting](PyCView.md#pycviewonbeginprinting_virtual) virtual method


## [PyCView\.OnBeginPrinting](PyCView.md#pycview) Virtual

OnBeginPrinting\(dc, pInfo

\)
Called by the framework at the beginning of a print or print preview job, after OnPreparePrinting has been called\.

#### Parameters

  - dc : [PyCDC](PyCDC.md)

    The DC object\.

  - pInfo : [PyCPrintInfo](PyCPrintInfo.md)

    The print info object\.

#### See Also

  - [PyCView::OnBeginPrinting](PyCView.md#pycviewonbeginprinting)


## [PyCView\.OnDraw](PyCView.md#pycview) Virtual

OnDraw\(dc\)
Called when the view should be drawn\.

#### Parameters

  - dc : [PyCDC](PyCDC.md)

    The DC object\.

#### See Also

  - PyCView::OnDraw




## [PyCView](PyCView.md#pycview)\.OnEndPrinting

OnEndPrinting\(\)
Calls the underlying MFC OnEndPrinting method\.

#### See Also

  - [PyCView\.OnEndPrinting](PyCView.md#pycviewonendprinting_virtual) virtual method


## [PyCView\.OnEndPrinting](PyCView.md#pycview) Virtual

OnEndPrinting\(dc, pInfo

\)
Called by the framework after a document has been printed or previewed\.

#### Parameters

  - dc : [PyCDC](PyCDC.md)

    The DC object\.

  - pInfo : [PyCPrintInfo](PyCPrintInfo.md)

    The print info object\.

#### See Also

  - [PyCView::OnEndPrinting](PyCView.md#pycviewonendprinting)


## [PyCView](PyCView.md#pycview)\.OnFilePrint

OnFilePrint\(\)
Calls the underlying MFC OnFilePrint method\.


## [PyCView](PyCView.md#pycview)\.OnFilePrintPreview

OnFilePrintPreview\(\)
Calls the underlying MFC OnFilePrintPreview method\.


## [PyCView](PyCView.md#pycview)\.OnInitialUpdate

OnInitialUpdate\(\)
Calls the underlying MFC OnInitialUpdate method\.

#### See Also

  - [PyCView\.OnInitialUpdate](PyCView.md#pycviewoninitialupdate_virtual) virtual method


## [PyCView\.OnInitialUpdate](PyCView.md#pycview) Virtual

OnInitialUpdate\(\)
Called before the first update for a view\.

#### Comments

The MFC base class is called only if no handler exists\.

#### See Also

  - [PyCView::OnInitialUpdate](PyCView.md#pycviewoninitialupdate)


## [PyCView](PyCView.md#pycview)\.OnMouseActivate

int = OnMouseActivate\(wnd, hittest

, message

\)
Calls the base MFC OnMouseActivate function\.

#### Parameters

  - wnd : [PyCWnd](PyCWnd.md)

    

  - hittest : int

    

  - message : int

    

#### See Also

  - [PyCWnd\.OnMouseActivate](PyCWnd.md#pycwndonmouseactivate_virtual) virtual method


## [PyCView](PyCView.md#pycview)\.OnPrepareDC

OnPrepareDC\(\)
Calls the underlying MFC OnPrepareDC method\.

#### See Also

  - [PyCView\.OnPrepareDC](PyCView.md#pycviewonpreparedc_virtual) virtual method


## [PyCView\.OnPrepareDC](PyCView.md#pycview) Virtual

OnPrepareDC\(dc, pInfo

\)
Called to prepare the device context for a view\.

#### Parameters

  - dc : [PyCDC](PyCDC.md)

    The DC object\.

  - pInfo : [PyCPrintInfo](PyCPrintInfo.md)

    The print info object\.

#### See Also

  - PyCWnd::OnPrepareDC




## [PyCView](PyCView.md#pycview)\.OnPreparePrinting

int = OnPreparePrinting\(\)
Calls the underlying MFC OnPreparePrinting method\.

#### See Also

  - [PyCView\.OnPreparePrinting](PyCView.md#pycviewonprepareprinting_virtual) virtual method


## [PyCView\.OnPreparePrinting](PyCView.md#pycview) Virtual

OnPreparePrinting\(pInfo\)
Called by the framework before a document is printed or previewed

#### Parameters

  - pInfo : [PyCPrintInfo](PyCPrintInfo.md)

    The print info object\.

#### See Also

  - [PyCView::OnPreparePrinting](PyCView.md#pycviewonprepareprinting)


## [PyCView\.OnPrint](PyCView.md#pycview) Virtual

OnPrint\(dc, pInfo

\)
Called when the view should be printed\.

#### Parameters

  - dc : [PyCDC](PyCDC.md)

    The DC object\.

  - pInfo : PyPrintInfo

    The PrintIfo object\.

#### See Also

  - PyCView::OnPrint




## [PyCView\.OnUpdate](PyCView.md#pycview) Virtual

OnUpdate\(sender, lHint

, hint

\)
Called by the framework when a view needs updating\.

#### Parameters

  - sender : [PyCView](PyCView.md#pycview)

    

  - lHint : int

    

  - hint : object

    

#### Comments

Typically you should not perform any drawing directly from OnUpdate\. 

Instead, determine the rectangle describing, in device coordinates, the 

area that requires updating; pass this rectangle to [PyCWnd::InvalidateRect](PyCWnd.md#pycwndinvalidaterect)\. 

You can then paint the update next PyCView::OnDraw

#### See Also

  - PyCView::OnUpdate




## [PyCView](PyCView.md#pycview)\.PreCreateWindow

tuple = PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters

  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.

#### See Also

  - [PyCWnd\.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual) virtual method