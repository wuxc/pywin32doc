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

## [PyIOleControlSite](#pyiolecontrolsite).GetExtendedControl

 __GetExtendedControl(__ )
Description of GetExtendedControl.

## [PyIOleControlSite](#pyiolecontrolsite).LockInPlaceActive

 __LockInPlaceActive( *fLock* __ )
Description of LockInPlaceActive.

#### Parameters


  -  *fLock* : int

    Description for fLock

## [PyIOleControlSite](#pyiolecontrolsite).OnControlInfoChanged

 __OnControlInfoChanged(__ )
Description of OnControlInfoChanged.

## [PyIOleControlSite](#pyiolecontrolsite).OnFocus

 __OnFocus( *fGotFocus* __ )
Description of OnFocus.

#### Parameters


  -  *fGotFocus* : int

    Description for fGotFocus

## [PyIOleControlSite](#pyiolecontrolsite).ShowPropertyFrame

 __ShowPropertyFrame(__ )
Description of ShowPropertyFrame.

## [PyIOleControlSite](#pyiolecontrolsite).TransformCoords

 __TransformCoords( *PtlHimetric*  *, pPtfContainer*  *, dwFlags* __ )
Description of TransformCoords.

#### Parameters


  -  *PtlHimetric* : (int, int)

    Description for pPtlHimetric

  -  *pPtfContainer* : (float, float))

    Description for pPtfContainer

  -  *dwFlags* : int

    Description for dwFlags

#### Return Value
The result is a tuple of the transformed input points - ie, 

a tuple of ((int, int), (float, float))

## [PyIOleControlSite](#pyiolecontrolsite).TranslateAccelerator

 __TranslateAccelerator( *pMsg*  *, grfModifiers* __ )
Description of TranslateAccelerator.

#### Parameters


  -  *pMsg* :[PyMSG](#pymsg)

    Description for pMsg

  -  *grfModifiers* : int

    Description for grfModifiers