# PyIOleInPlaceSiteWindowless

## PyIOleInPlaceSiteWindowless Object

Description of the interface

#### Methods


  - [CanWindowlessActivate](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlesscanwindowlessactivate)

    Description of CanWindowlessActivate&nbsp;

  - [GetCapture](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessgetcapture)

    Description of GetCapture&nbsp;

  - [SetCapture](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlesssetcapture)

    Description of SetCapture&nbsp;

  - [GetFocus](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessgetfocus)

    Description of GetFocus&nbsp;

  - [SetFocus](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlesssetfocus)

    Description of SetFocus&nbsp;

  - [GetDC](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessgetdc)

    Description of GetDC&nbsp;

  - [ReleaseDC](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessreleasedc)

    Description of ReleaseDC&nbsp;

  - [InvalidateRect](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessinvalidaterect)

    Description of InvalidateRect&nbsp;

  - [InvalidateRgn](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessinvalidatergn)

    Description of InvalidateRgn&nbsp;

  - [ScrollRect](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessscrollrect)

    Description of ScrollRect&nbsp;

  - [AdjustRect](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessadjustrect)

    Description of AdjustRect&nbsp;

  - [OnDefWindowMessage](PyIOleInPlaceSiteWindowless.md#pyioleinplacesitewindowlessondefwindowmessage)

    Description of OnDefWindowMessage&nbsp;

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).AdjustRect

 __AdjustRect(__ )
Description of AdjustRect.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).CanWindowlessActivate

 __CanWindowlessActivate(__ )
Description of CanWindowlessActivate.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).GetCapture

 __GetCapture(__ )
Description of GetCapture.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).GetDC

 __GetDC( *grfFlags*  *, rect* __ )
Description of GetDC.

#### Parameters


  -  *grfFlags* : int

    Description for grfFlags

  -  *rect* : (int, int, int, int)

    

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).GetFocus

 __GetFocus(__ )
Description of GetFocus.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).InvalidateRect

 __InvalidateRect( *rect*  *, fErase* __ )
Description of InvalidateRect.

#### Parameters


  -  *rect* : (int, int, int, int)

    

  -  *fErase* : int

    Description for fErase

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).InvalidateRgn

 __InvalidateRgn( *hRgn*  *, fErase* __ )
Description of InvalidateRgn.

#### Parameters


  -  *hRgn* : int

    Handle to a region

  -  *fErase* : int

    Description for fErase

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).OnDefWindowMessage

 __OnDefWindowMessage( *msg*  *, wParam*  *, lParam* __ )
Description of OnDefWindowMessage.

#### Parameters


  -  *msg* : int

    Description for msg

  -  *wParam* : int

    Description for wParam

  -  *lParam* : long

    Description for lParam

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).ReleaseDC

 __ReleaseDC( *hDC* __ )
Description of ReleaseDC.

#### Parameters


  -  *hDC* : HDC

    Description for hDC

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).ScrollRect

 __ScrollRect( *dx*  *, dy* __ )
Description of ScrollRect.

#### Parameters


  -  *dx* : int

    Description for dx

  -  *dy* : int

    Description for dy

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).SetCapture

 __SetCapture( *fCapture* __ )
Description of SetCapture.

#### Parameters


  -  *fCapture* : int

    Description for fCapture

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless).SetFocus

 __SetFocus( *fFocus* __ )
Description of SetFocus.

#### Parameters


  -  *fFocus* : int

    Description for fFocus