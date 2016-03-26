# PyCView

## PyCView Object



A class which implements a generic CView\.  Derived from a[PyCWnd](#pycwnd) object\.

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


## [PyCView](#pycview)\.CreateWindow

CreateWindow\(parent, id, style, rect\)
Creates the window for a view\.

#### Parameters


  - parent :[PyCWnd](#pycwnd)

    The parent window \(usually a frame\)

  - id=win32ui\.AFX\_IDW\_PANE\_FIRST : int

    The child ID for the view

  - style=win32ui\.AFX\_WS\_DEFAULT\_VIEW : int

    The style for the view

  - rect=\(0,0,0,0\) : \(left, top, right, bottom\)

    The default position of the window\.

## [PyCView](#pycview)\.DoPreparePrinting



int =DoPreparePrinting\(\)
Invoke the Print dialog box and create a printer device context\.

#### Comments


This function is usually called from[PyCView\.OnPreparePrinting](PyCView.md#pycviewonprepareprinting_virtual) virtual method

## [PyCView](#pycview)\.GetDocument

[PyCDocument](#pycdocument) =GetDocument\(\)
Returns the document for a view\.

## [PyCView](#pycview)\.OnActivateView



int =OnActivateView\(activate, activateView, DeactivateView\)
Calls the underlying MFC OnActivateView method\.

#### Parameters


  - activate : int

    Indicates whether the view is being activated or deactivated\.

  - activateView :[PyCView](#pycview)

    The view object that is being activated\.

  - DeactivateView :[PyCView](#pycview)

    The view object that is being deactivated\.

#### See Also


  - [PyCView\.OnActivateView](PyCView.md#pycviewonactivateview_virtual) virtual method

## [PyCView\.OnActivateView](#pycview) Virtual

OnActivateView\(bActivate, activateView, DeactivateView\)
Called by the framework when a view is activated or deactivated\.

#### Parameters


  - bActivate : int

    Indicates whether the view is being activated or deactivated\.

  - activateView :[PyCWnd](#pycwnd)

    The view object that is being activated\.

  - DeactivateView :[PyCWnd](#pycwnd)

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

## [PyCView](#pycview)\.OnBeginPrinting

OnBeginPrinting\(\)
Calls the underlying MFC OnBeginPrinting method\.

#### See Also


  - [PyCView\.OnBeginPrinting](PyCView.md#pycviewonbeginprinting_virtual) virtual method

## [PyCView\.OnBeginPrinting](#pycview) Virtual

OnBeginPrinting\(dc, pInfo\)
Called by the framework at the beginning of a print or print preview job, after OnPreparePrinting has been called\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    The DC object\.

  - pInfo :[PyCPrintInfo](#pycprintinfo)

    The print info object\.

#### See Also


  - [PyCView::OnBeginPrinting](PyCView.md#pycviewonbeginprinting)

## [PyCView\.OnDraw](#pycview) Virtual

OnDraw\(dc\)
Called when the view should be drawn\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    The DC object\.

#### See Also


  - PyCView::OnDraw

## [PyCView](#pycview)\.OnEndPrinting

OnEndPrinting\(\)
Calls the underlying MFC OnEndPrinting method\.

#### See Also


  - [PyCView\.OnEndPrinting](PyCView.md#pycviewonendprinting_virtual) virtual method

## [PyCView\.OnEndPrinting](#pycview) Virtual

OnEndPrinting\(dc, pInfo\)
Called by the framework after a document has been printed or previewed\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    The DC object\.

  - pInfo :[PyCPrintInfo](#pycprintinfo)

    The print info object\.

#### See Also


  - [PyCView::OnEndPrinting](PyCView.md#pycviewonendprinting)

## [PyCView](#pycview)\.OnFilePrint

OnFilePrint\(\)
Calls the underlying MFC OnFilePrint method\.

## [PyCView](#pycview)\.OnFilePrintPreview

OnFilePrintPreview\(\)
Calls the underlying MFC OnFilePrintPreview method\.

## [PyCView](#pycview)\.OnInitialUpdate

OnInitialUpdate\(\)
Calls the underlying MFC OnInitialUpdate method\.

#### See Also


  - [PyCView\.OnInitialUpdate](PyCView.md#pycviewoninitialupdate_virtual) virtual method

## [PyCView\.OnInitialUpdate](#pycview) Virtual

OnInitialUpdate\(\)
Called before the first update for a view\.

#### Comments


The MFC base class is called only if no handler exists\.

#### See Also


  - [PyCView::OnInitialUpdate](PyCView.md#pycviewoninitialupdate)

## [PyCView](#pycview)\.OnMouseActivate



int =OnMouseActivate\(wnd, hittest, message\)
Calls the base MFC OnMouseActivate function\.

#### Parameters


  - wnd :[PyCWnd](#pycwnd)

    

  - hittest : int

    

  - message : int

    

#### See Also


  - [PyCWnd\.OnMouseActivate](PyCWnd.md#pycwndonmouseactivate_virtual) virtual method

## [PyCView](#pycview)\.OnPrepareDC

OnPrepareDC\(\)
Calls the underlying MFC OnPrepareDC method\.

#### See Also


  - [PyCView\.OnPrepareDC](PyCView.md#pycviewonpreparedc_virtual) virtual method

## [PyCView\.OnPrepareDC](#pycview) Virtual

OnPrepareDC\(dc, pInfo\)
Called to prepare the device context for a view\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    The DC object\.

  - pInfo :[PyCPrintInfo](#pycprintinfo)

    The print info object\.

#### See Also


  - PyCWnd::OnPrepareDC

## [PyCView](#pycview)\.OnPreparePrinting



int =OnPreparePrinting\(\)
Calls the underlying MFC OnPreparePrinting method\.

#### See Also


  - [PyCView\.OnPreparePrinting](PyCView.md#pycviewonprepareprinting_virtual) virtual method

## [PyCView\.OnPreparePrinting](#pycview) Virtual

OnPreparePrinting\(pInfo\)
Called by the framework before a document is printed or previewed

#### Parameters


  - pInfo :[PyCPrintInfo](#pycprintinfo)

    The print info object\.

#### See Also


  - [PyCView::OnPreparePrinting](PyCView.md#pycviewonprepareprinting)

## [PyCView\.OnPrint](#pycview) Virtual

OnPrint\(dc, pInfo\)
Called when the view should be printed\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    The DC object\.

  - pInfo :PyPrintInfo

    The PrintIfo object\.

#### See Also


  - PyCView::OnPrint

## [PyCView\.OnUpdate](#pycview) Virtual

OnUpdate\(sender, lHint, hint\)
Called by the framework when a view needs updating\.

#### Parameters


  - sender :[PyCView](#pycview)

    

  - lHint : int

    

  - hint : object

    

#### Comments


Typically you should not perform any drawing directly from OnUpdate\. 

Instead, determine the rectangle describing, in device coordinates, the 

area that requires updating; pass this rectangle to[PyCWnd::InvalidateRect](PyCWnd.md#pycwndinvalidaterect)\. 

You can then paint the update nextPyCView::OnDraw

#### See Also


  - PyCView::OnUpdate

## [PyCView](#pycview)\.PreCreateWindow



tuple =PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters


  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.

#### See Also


  - [PyCWnd\.PreCreateWindow](PyCWnd.md#pycwndprecreatewindow_virtual) virtual method