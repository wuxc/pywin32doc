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


## [PyIViewObject](PyIViewObject.md#pyiviewobject)\.Draw

Draw\(dwDrawAspect, lindex, aspectFlags, hdcTargetDev, hdcDraw, left, top, right, bottom, left, top, right, bottom, funcContinue, obContinue\)
Description of Draw\.

#### Parameters

  - dwDrawAspect : int

    Description for dwDrawAspect

  - lindex : int

    Description for lindex

  - aspectFlags : int

    Integer value for the dwFlags item of the DVASPECTINFO structure\.

  - hdcTargetDev : HDC

    Description for hdcTargetDev

  - hdcDraw : HDC

    Description for hdcDraw

  - left, top, right, bottom : int, int, int, int

    Bounds rectangle\.

  - left, top, right, bottom : int, int, int, int

    WBounds rectangle\.

  - funcContinue : object

    A continue function\.

  - obContinue : object

    Value passed to the function\.


## [PyIViewObject](PyIViewObject.md#pyiviewobject)\.Freeze

Freeze\(dwDrawAspect, lindex, aspectFlags\)
Description of Freeze\.

#### Parameters

  - dwDrawAspect : int

    Description for dwDrawAspect

  - lindex : int

    Description for lindex

  - aspectFlags : int

    Integer value for the dwFlags item of the DVASPECTINFO structure\.


## [PyIViewObject](PyIViewObject.md#pyiviewobject)\.GetAdvise

GetAdvise\(\)
Description of GetAdvise\.


## [PyIViewObject](PyIViewObject.md#pyiviewobject)\.GetColorSet

GetColorSet\(dwDrawAspect, lindex, aspectFlags, hicTargetDev\)
Description of GetColorSet\.

#### Parameters

  - dwDrawAspect : int

    Description for dwDrawAspect

  - lindex : int

    Description for lindex

  - aspectFlags : int

    Integer value for the dwFlags item of the DVASPECTINFO structure\.

  - hicTargetDev : HDC

    Description for hicTargetDev


## [PyIViewObject](PyIViewObject.md#pyiviewobject)\.SetAdvise

SetAdvise\(aspects, advf, pAdvSink\)
Description of SetAdvise\.

#### Parameters

  - aspects : int

    Description for aspects

  - advf : int

    Description for advf

  - pAdvSink : PyIAdviseSink

    Description for pAdvSink


## [PyIViewObject](PyIViewObject.md#pyiviewobject)\.Unfreeze

Unfreeze\(dwFreeze\)
Description of Unfreeze\.

#### Parameters

  - dwFreeze : int

    Description for dwFreeze