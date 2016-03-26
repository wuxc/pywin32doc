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


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.EnableModeless

EnableModeless\(fEnable\)
Description of EnableModeless\.

#### Parameters

  - fEnable : int

    Description for fEnable


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.FilterDataObject

FilterDataObject\(pDO\)
Description of FilterDataObject\.

#### Parameters

  - pDO : [PyIDataObject](PyIDataObject.md)

    Description for pDO


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.GetDropTarget

GetDropTarget\(pDropTarget\)
Description of GetDropTarget\.

#### Parameters

  - pDropTarget : [PyIDropTarget](PyIDropTarget.md)

    Description for pDropTarget


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.GetExternal

GetExternal\(\)
Description of GetExternal\.


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.GetHostInfo

GetHostInfo\(\)
Description of GetHostInfo\.


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.GetOptionKeyPath

GetOptionKeyPath\(dw\)
Description of GetOptionKeyPath\.

#### Parameters

  - dw : int

    Description for dw


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.HideUI

HideUI\(\)
Description of HideUI\.


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.OnDocWindowActivate

OnDocWindowActivate\(fActivate\)
Description of OnDocWindowActivate\.

#### Parameters

  - fActivate : int

    Description for fActivate


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.OnFrameWindowActivate

OnFrameWindowActivate\(fActivate\)
Description of OnFrameWindowActivate\.

#### Parameters

  - fActivate : int

    Description for fActivate


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.ResizeBorder

ResizeBorder\(prcBorder, pUIWindow, fRameWindow\)
Description of ResizeBorder\.

#### Parameters

  - prcBorder : \(int, int, int, int\)

    Description for prcBorder

  - pUIWindow : [PyIOleInPlaceUIWindow](PyIOleInPlaceUIWindow.md)

    Description for pUIWindow

  - fRameWindow : int

    Description for fRameWindow


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.ShowContextMenu

ShowContextMenu\(dwID, pt, pcmdtReserved, pdispReserved\)
Description of ShowContextMenu\.

#### Parameters

  - dwID : int

    Description for dwID

  - pt : \(int, int\)

    Description for ppt

  - pcmdtReserved : [PyIUnknown](PyIUnknown.md)

    Description for pcmdtReserved

  - pdispReserved : [PyIDispatch](PyIDispatch.md)

    Description for pdispReserved


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.ShowUI

ShowUI\(dwID, pActiveObject, pCommandTarget, pFrame, pDoc\)
Description of ShowUI\.

#### Parameters

  - dwID : int

    Description for dwID

  - pActiveObject : [PyIOleInPlaceActiveObject](PyIOleInPlaceActiveObject.md)

    Description for pActiveObject

  - pCommandTarget : [PyIOleCommandTarget](PyIOleCommandTarget.md)

    Description for pCommandTarget

  - pFrame : [PyIOleInPlaceFrame](PyIOleInPlaceFrame.md)

    Description for pFrame

  - pDoc : [PyIOleInPlaceUIWindow](PyIOleInPlaceUIWindow.md)

    Description for pDoc


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.TranslateAccelerator

TranslateAccelerator\(lpMsg, pguidCmdGroup, nCmdID\)
Description of TranslateAccelerator\.

#### Parameters

  - lpMsg : PyLPMSG

    Description for lpMsg

  - pguidCmdGroup : [PyIID](PyIID.md)

    Description for pguidCmdGroup

  - nCmdID : int

    Description for nCmdID


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.TranslateUrl

TranslateUrl\(dwTranslate, pchURLIn\)
Description of TranslateUrl\.

#### Parameters

  - dwTranslate : int

    Description for dwTranslate

  - pchURLIn : unicode

    Description for pchURLIn


## [PyIDocHostUIHandler](PyIDocHostUIHandler.md#pyidochostuihandler)\.UpdateUI

UpdateUI\(\)
Description of UpdateUI\.