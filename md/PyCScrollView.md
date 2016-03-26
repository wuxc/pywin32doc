# PyCScrollView

## PyCScrollView Object



A class which implements a generic CScrollView\.  Derived from a[PyCView](#pycview) object\.

#### Methods


  - [GetDeviceScrollPosition](PyCScrollView.md#pycscrollviewgetdevicescrollposition)

    Return the position of the scroll bars \(device units\)\.&nbsp;

  - [GetDC](PyCScrollView.md#pycscrollviewgetdc)

    Get the views current[PyCDC](#pycdc)&nbsp;

  - [GetScrollPosition](PyCScrollView.md#pycscrollviewgetscrollposition)

    Return the position of the scroll bars \(logical units\)\.&nbsp;

  - [GetTotalSize](PyCScrollView.md#pycscrollviewgettotalsize)

    Return the total size of the views\.&nbsp;

  - [OnCommand](PyCScrollView.md#pycscrollviewoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;

  - [ResizeParentToFit](PyCScrollView.md#pycscrollviewresizeparenttofit)

    Call ResizeParentToFit to let the size of your view dictate the size of its frame window\.&nbsp;

  - [SetScaleToFitSize](PyCScrollView.md#pycscrollviewsetscaletofitsize)

    Scales the viewport size to the current window size automatically\.&nbsp;

  - [ScrollToPosition](PyCScrollView.md#pycscrollviewscrolltoposition)

    Scroll to a specified point\.&nbsp;

  - [SetScrollSizes](PyCScrollView.md#pycscrollviewsetscrollsizes)

    Set the scrolling sizes\.&nbsp;

  - [UpdateBars](PyCScrollView.md#pycscrollviewupdatebars)

    Update the scroll bar state\.&nbsp;


## [PyCScrollView](#pycscrollview)\.GetDC

[PyCDC](#pycdc) =GetDC\(\)
Gets the view's current DC\.

## [PyCScrollView](#pycscrollview)\.GetDeviceScrollPosition



\(x,y\) =GetDeviceScrollPosition\(\)
Returns the positon of the scroll bars in device units\.

## [PyCScrollView](#pycscrollview)\.GetScrollPosition



\(x,y\) =GetScrollPosition\(\)
Returns the current position of the scroll bars \(in logical units\)\.

## [PyCScrollView](#pycscrollview)\.GetTotalSize



\(x,y\) =GetTotalSize\(\)
Returns the total size of the view in logical units\.

## [PyCScrollView](#pycscrollview)\.OnCommand

OnCommand\(wparam, lparam\)
Calls the standard Python framework OnCommand handler

#### Parameters


  - wparam : int

    

  - lparam : int

    

#### See Also


  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual) virtual method

## [PyCScrollView\.OnPrepareDC](#pycscrollview) Virtual

OnPrepareDC\(dc\)
Called to prepare the device context for a view\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    The DC object\.

#### See Also


  - [PyCView::OnPrepareDC](PyCView.md#pycviewonpreparedc)

## [PyCScrollView](#pycscrollview)\.ResizeParentToFit



tuple =ResizeParentToFit\(bShrinkOnly\)
Lets the size of a view dictate the size of its frame window\.

#### Parameters


  - bShrinkOnly=1 : int

    The kind of resizing to perform\. The default value, TRUE, shrinks the frame window if appropriate\.

#### Comments


This is recommended only for views in MDI child frame windows\.
Use ResizeParentToFit in the OnInitialUpdate handler function of your View class\.
You must ensure the parent's[PyCFrameWnd::RecalcLayout](PyCFrameWnd.md#pycframewndrecalclayout) is called before using this method\.

## [PyCScrollView](#pycscrollview)\.ScrollToPosition

ScrollToPosition\(position\)
Scrolls to a given point in the view\.

#### Parameters


  - position : \(x,y\)

    The position to scroll to\.

## [PyCScrollView](#pycscrollview)\.SetScaleToFitSize

SetScaleToFitSize\(size\)
Scales the viewport size to the current window size automatically\.

#### Parameters


  - size : \(x,y\)

    The horizontal and vertical sizes to which the view is to be scaled\. The scroll view's size is measured in logical units\.

## [PyCScrollView](#pycscrollview)\.SetScrollSizes

SetScrollSizes\(mapMode, sizeTotal, sizePage, sizePage\)
Sets the sizes of the scroll bars

#### Parameters


  - mapMode : int

    The mapping mode for this view\.

  - sizeTotal : \(x,y\)

    The total size of the view\.  Sizes are in logical units\.  Both x and y must be greater than zero\.

  - sizePage=win32ui\.rectDefault : \(x,y\)

    The number of untils to scroll in response to a page-down command\.

  - sizePage=win32ui\.rectDefault : \(x,y\)

    The number of untils to scroll in response to a line-down command\.

## [PyCScrollView](#pycscrollview)\.UpdateBars

UpdateBars\(\)
Update the scroll bars state