# PyIDocHostUIHandler

## PyIDocHostUIHandler Object



Description of the interface

#### Methods


  - [ShowContextMenu](PyIDocHostUIHandler.md#pyidochostuihandlershowcontextmenu)

    Description of ShowContextMenu&nbsp;

  - [GetHostInfo](PyIDocHostUIHandler.md#pyidochostuihandlergethostinfo)

    Description of GetHostInfo&nbsp;

  - [ShowUI](PyIDocHostUIHandler.md#pyidochostuihandlershowui)

    Description of ShowUI&nbsp;

  - [HideUI](PyIDocHostUIHandler.md#pyidochostuihandlerhideui)

    Description of HideUI&nbsp;

  - [UpdateUI](PyIDocHostUIHandler.md#pyidochostuihandlerupdateui)

    Description of UpdateUI&nbsp;

  - [EnableModeless](PyIDocHostUIHandler.md#pyidochostuihandlerenablemodeless)

    Description of EnableModeless&nbsp;

  - [OnDocWindowActivate](PyIDocHostUIHandler.md#pyidochostuihandlerondocwindowactivate)

    Description of OnDocWindowActivate&nbsp;

  - [OnFrameWindowActivate](PyIDocHostUIHandler.md#pyidochostuihandleronframewindowactivate)

    Description of OnFrameWindowActivate&nbsp;

  - [ResizeBorder](PyIDocHostUIHandler.md#pyidochostuihandlerresizeborder)

    Description of ResizeBorder&nbsp;

  - [TranslateAccelerator](PyIDocHostUIHandler.md#pyidochostuihandlertranslateaccelerator)

    Description of TranslateAccelerator&nbsp;

  - [GetOptionKeyPath](PyIDocHostUIHandler.md#pyidochostuihandlergetoptionkeypath)

    Description of GetOptionKeyPath&nbsp;

  - [GetDropTarget](PyIDocHostUIHandler.md#pyidochostuihandlergetdroptarget)

    Description of GetDropTarget&nbsp;

  - [GetExternal](PyIDocHostUIHandler.md#pyidochostuihandlergetexternal)

    Description of GetExternal&nbsp;

  - [TranslateUrl](PyIDocHostUIHandler.md#pyidochostuihandlertranslateurl)

    Description of TranslateUrl&nbsp;

  - [FilterDataObject](PyIDocHostUIHandler.md#pyidochostuihandlerfilterdataobject)

    Description of FilterDataObject&nbsp;

## [PyIDocHostUIHandler](#pyidochostuihandler)\.EnableModeless

EnableModeless\(fEnable\)
Description of EnableModeless\.

#### Parameters


  - fEnable : int

    Description for fEnable

## [PyIDocHostUIHandler](#pyidochostuihandler)\.FilterDataObject

FilterDataObject\(pDO\)
Description of FilterDataObject\.

#### Parameters


  - pDO :[PyIDataObject](#pyidataobject)

    Description for pDO

## [PyIDocHostUIHandler](#pyidochostuihandler)\.GetDropTarget

GetDropTarget\(pDropTarget\)
Description of GetDropTarget\.

#### Parameters


  - pDropTarget :[PyIDropTarget](#pyidroptarget)

    Description for pDropTarget

## [PyIDocHostUIHandler](#pyidochostuihandler)\.GetExternal

GetExternal\(\)
Description of GetExternal\.

## [PyIDocHostUIHandler](#pyidochostuihandler)\.GetHostInfo

GetHostInfo\(\)
Description of GetHostInfo\.

## [PyIDocHostUIHandler](#pyidochostuihandler)\.GetOptionKeyPath

GetOptionKeyPath\(dw\)
Description of GetOptionKeyPath\.

#### Parameters


  - dw : int

    Description for dw

## [PyIDocHostUIHandler](#pyidochostuihandler)\.HideUI

HideUI\(\)
Description of HideUI\.

## [PyIDocHostUIHandler](#pyidochostuihandler)\.OnDocWindowActivate

OnDocWindowActivate\(fActivate\)
Description of OnDocWindowActivate\.

#### Parameters


  - fActivate : int

    Description for fActivate

## [PyIDocHostUIHandler](#pyidochostuihandler)\.OnFrameWindowActivate

OnFrameWindowActivate\(fActivate\)
Description of OnFrameWindowActivate\.

#### Parameters


  - fActivate : int

    Description for fActivate

## [PyIDocHostUIHandler](#pyidochostuihandler)\.ResizeBorder

ResizeBorder\(prcBorder, pUIWindow, fRameWindow\)
Description of ResizeBorder\.

#### Parameters


  - prcBorder : \(int, int, int, int\)

    Description for prcBorder

  - pUIWindow :[PyIOleInPlaceUIWindow](#pyioleinplaceuiwindow)

    Description for pUIWindow

  - fRameWindow : int

    Description for fRameWindow

## [PyIDocHostUIHandler](#pyidochostuihandler)\.ShowContextMenu

ShowContextMenu\(dwID, pt, pcmdtReserved, pdispReserved\)
Description of ShowContextMenu\.

#### Parameters


  - dwID : int

    Description for dwID

  - pt : \(int, int\)

    Description for ppt

  - pcmdtReserved :[PyIUnknown](#pyiunknown)

    Description for pcmdtReserved

  - pdispReserved :[PyIDispatch](#pyidispatch)

    Description for pdispReserved

## [PyIDocHostUIHandler](#pyidochostuihandler)\.ShowUI

ShowUI\(dwID, pActiveObject, pCommandTarget, pFrame, pDoc\)
Description of ShowUI\.

#### Parameters


  - dwID : int

    Description for dwID

  - pActiveObject :[PyIOleInPlaceActiveObject](#pyioleinplaceactiveobject)

    Description for pActiveObject

  - pCommandTarget :[PyIOleCommandTarget](#pyiolecommandtarget)

    Description for pCommandTarget

  - pFrame :[PyIOleInPlaceFrame](#pyioleinplaceframe)

    Description for pFrame

  - pDoc :[PyIOleInPlaceUIWindow](#pyioleinplaceuiwindow)

    Description for pDoc

## [PyIDocHostUIHandler](#pyidochostuihandler)\.TranslateAccelerator

TranslateAccelerator\(lpMsg, pguidCmdGroup, nCmdID\)
Description of TranslateAccelerator\.

#### Parameters


  - lpMsg :PyLPMSG

    Description for lpMsg

  - pguidCmdGroup :[PyIID](#pyiid)

    Description for pguidCmdGroup

  - nCmdID : int

    Description for nCmdID

## [PyIDocHostUIHandler](#pyidochostuihandler)\.TranslateUrl

TranslateUrl\(dwTranslate, pchURLIn\)
Description of TranslateUrl\.

#### Parameters


  - dwTranslate : int

    Description for dwTranslate

  - pchURLIn :unicode

    Description for pchURLIn

## [PyIDocHostUIHandler](#pyidochostuihandler)\.UpdateUI

UpdateUI\(\)
Description of UpdateUI\.