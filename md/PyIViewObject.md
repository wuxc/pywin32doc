# PyIViewObject

## PyIViewObject Object

Description of the interface

#### Methods


  - [Draw](PyIViewObject.md#pyiviewobjectdraw)

    Description of Draw&nbsp;

  - [GetColorSet](PyIViewObject.md#pyiviewobjectgetcolorset)

    Description of GetColorSet&nbsp;

  - [Freeze](PyIViewObject.md#pyiviewobjectfreeze)

    Description of Freeze&nbsp;

  - [Unfreeze](PyIViewObject.md#pyiviewobjectunfreeze)

    Description of Unfreeze&nbsp;

  - [SetAdvise](PyIViewObject.md#pyiviewobjectsetadvise)

    Description of SetAdvise&nbsp;

  - [GetAdvise](PyIViewObject.md#pyiviewobjectgetadvise)

    Description of GetAdvise&nbsp;

## [PyIViewObject](#pyiviewobject).Draw

 __Draw( *dwDrawAspect*  *, lindex*  *, aspectFlags*  *, hdcTargetDev*  *, hdcDraw*  *, left, top, right, bottom*  *, left, top, right, bottom*  *, funcContinue*  *, obContinue* __ )
Description of Draw.

#### Parameters


  -  *dwDrawAspect* : int

    Description for dwDrawAspect

  -  *lindex* : int

    Description for lindex

  -  *aspectFlags* : int

    Integer value for the dwFlags item of the DVASPECTINFO structure.

  -  *hdcTargetDev* : HDC

    Description for hdcTargetDev

  -  *hdcDraw* : HDC

    Description for hdcDraw

  -  *left, top, right, bottom* : int, int, int, int

    Bounds rectangle.

  -  *left, top, right, bottom* : int, int, int, int

    WBounds rectangle.

  -  *funcContinue* : object

    A continue function.

  -  *obContinue* : object

    Value passed to the function.

## [PyIViewObject](#pyiviewobject).Freeze

 __Freeze( *dwDrawAspect*  *, lindex*  *, aspectFlags* __ )
Description of Freeze.

#### Parameters


  -  *dwDrawAspect* : int

    Description for dwDrawAspect

  -  *lindex* : int

    Description for lindex

  -  *aspectFlags* : int

    Integer value for the dwFlags item of the DVASPECTINFO structure.

## [PyIViewObject](#pyiviewobject).GetAdvise

 __GetAdvise(__ )
Description of GetAdvise.

## [PyIViewObject](#pyiviewobject).GetColorSet

 __GetColorSet( *dwDrawAspect*  *, lindex*  *, aspectFlags*  *, hicTargetDev* __ )
Description of GetColorSet.

#### Parameters


  -  *dwDrawAspect* : int

    Description for dwDrawAspect

  -  *lindex* : int

    Description for lindex

  -  *aspectFlags* : int

    Integer value for the dwFlags item of the DVASPECTINFO structure.

  -  *hicTargetDev* : HDC

    Description for hicTargetDev

## [PyIViewObject](#pyiviewobject).SetAdvise

 __SetAdvise( *aspects*  *, advf*  *, pAdvSink* __ )
Description of SetAdvise.

#### Parameters


  -  *aspects* : int

    Description for aspects

  -  *advf* : int

    Description for advf

  -  *pAdvSink* : __PyIAdviseSink__ 

    Description for pAdvSink

## [PyIViewObject](#pyiviewobject).Unfreeze

 __Unfreeze( *dwFreeze* __ )
Description of Unfreeze.

#### Parameters


  -  *dwFreeze* : int

    Description for dwFreeze