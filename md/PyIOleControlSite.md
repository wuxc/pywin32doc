# PyIOleControlSite

## PyIOleControlSite Object

Description of the interface

#### Methods


  - [OnControlInfoChanged](PyIOleControlSite.md#pyiolecontrolsiteoncontrolinfochanged)

    Description of OnControlInfoChanged&nbsp;

  - [LockInPlaceActive](PyIOleControlSite.md#pyiolecontrolsitelockinplaceactive)

    Description of LockInPlaceActive&nbsp;

  - [GetExtendedControl](PyIOleControlSite.md#pyiolecontrolsitegetextendedcontrol)

    Description of GetExtendedControl&nbsp;

  - [TransformCoords](PyIOleControlSite.md#pyiolecontrolsitetransformcoords)

    Description of TransformCoords&nbsp;

  - [TranslateAccelerator](PyIOleControlSite.md#pyiolecontrolsitetranslateaccelerator)

    Description of TranslateAccelerator&nbsp;

  - [OnFocus](PyIOleControlSite.md#pyiolecontrolsiteonfocus)

    Description of OnFocus&nbsp;

  - [ShowPropertyFrame](PyIOleControlSite.md#pyiolecontrolsiteshowpropertyframe)

    Description of ShowPropertyFrame&nbsp;

## [PyIOleControlSite](#pyiolecontrolsite)\.GetExtendedControl

 **GetExtendedControl\(** \)
Description of GetExtendedControl\.

## [PyIOleControlSite](#pyiolecontrolsite)\.LockInPlaceActive

 **LockInPlaceActive\( *fLock* ** \)
Description of LockInPlaceActive\.

#### Parameters


  -  *fLock* : int

    Description for fLock

## [PyIOleControlSite](#pyiolecontrolsite)\.OnControlInfoChanged

 **OnControlInfoChanged\(** \)
Description of OnControlInfoChanged\.

## [PyIOleControlSite](#pyiolecontrolsite)\.OnFocus

 **OnFocus\( *fGotFocus* ** \)
Description of OnFocus\.

#### Parameters


  -  *fGotFocus* : int

    Description for fGotFocus

## [PyIOleControlSite](#pyiolecontrolsite)\.ShowPropertyFrame

 **ShowPropertyFrame\(** \)
Description of ShowPropertyFrame\.

## [PyIOleControlSite](#pyiolecontrolsite)\.TransformCoords

 **TransformCoords\( *PtlHimetric*  *, pPtfContainer*  *, dwFlags* ** \)
Description of TransformCoords\.

#### Parameters


  -  *PtlHimetric* : \(int, int\)

    Description for pPtlHimetric

  -  *pPtfContainer* : \(float, float\)\)

    Description for pPtfContainer

  -  *dwFlags* : int

    Description for dwFlags

#### Return Value
The result is a tuple of the transformed input points - ie, 

a tuple of \(\(int, int\), \(float, float\)\)

## [PyIOleControlSite](#pyiolecontrolsite)\.TranslateAccelerator

 **TranslateAccelerator\( *pMsg*  *, grfModifiers* ** \)
Description of TranslateAccelerator\.

#### Parameters


  -  *pMsg* :[PyMSG](#pymsg)

    Description for pMsg

  -  *grfModifiers* : int

    Description for grfModifiers