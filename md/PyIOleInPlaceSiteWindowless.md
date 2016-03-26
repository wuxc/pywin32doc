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

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.AdjustRect

 **AdjustRect\(** \)
Description of AdjustRect\.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.CanWindowlessActivate

 **CanWindowlessActivate\(** \)
Description of CanWindowlessActivate\.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.GetCapture

 **GetCapture\(** \)
Description of GetCapture\.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.GetDC

 **GetDC\( *grfFlags*  *, rect* ** \)
Description of GetDC\.

#### Parameters


  -  *grfFlags* : int

    Description for grfFlags

  -  *rect* : \(int, int, int, int\)

    

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.GetFocus

 **GetFocus\(** \)
Description of GetFocus\.

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.InvalidateRect

 **InvalidateRect\( *rect*  *, fErase* ** \)
Description of InvalidateRect\.

#### Parameters


  -  *rect* : \(int, int, int, int\)

    

  -  *fErase* : int

    Description for fErase

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.InvalidateRgn

 **InvalidateRgn\( *hRgn*  *, fErase* ** \)
Description of InvalidateRgn\.

#### Parameters


  -  *hRgn* : int

    Handle to a region

  -  *fErase* : int

    Description for fErase

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.OnDefWindowMessage

 **OnDefWindowMessage\( *msg*  *, wParam*  *, lParam* ** \)
Description of OnDefWindowMessage\.

#### Parameters


  -  *msg* : int

    Description for msg

  -  *wParam* : int

    Description for wParam

  -  *lParam* : long

    Description for lParam

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.ReleaseDC

 **ReleaseDC\( *hDC* ** \)
Description of ReleaseDC\.

#### Parameters


  -  *hDC* : HDC

    Description for hDC

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.ScrollRect

 **ScrollRect\( *dx*  *, dy* ** \)
Description of ScrollRect\.

#### Parameters


  -  *dx* : int

    Description for dx

  -  *dy* : int

    Description for dy

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.SetCapture

 **SetCapture\( *fCapture* ** \)
Description of SetCapture\.

#### Parameters


  -  *fCapture* : int

    Description for fCapture

## [PyIOleInPlaceSiteWindowless](#pyioleinplacesitewindowless)\.SetFocus

 **SetFocus\( *fFocus* ** \)
Description of SetFocus\.

#### Parameters


  -  *fFocus* : int

    Description for fFocus