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

## [PyIDocHostUIHandler](#pyidochostuihandler).EnableModeless

 __EnableModeless( *fEnable* __ )
Description of EnableModeless.

#### Parameters


  -  *fEnable* : int

    Description for fEnable

## [PyIDocHostUIHandler](#pyidochostuihandler).FilterDataObject

 __FilterDataObject( *pDO* __ )
Description of FilterDataObject.

#### Parameters


  -  *pDO* :[PyIDataObject](#pyidataobject)

    Description for pDO

## [PyIDocHostUIHandler](#pyidochostuihandler).GetDropTarget

 __GetDropTarget( *pDropTarget* __ )
Description of GetDropTarget.

#### Parameters


  -  *pDropTarget* :[PyIDropTarget](#pyidroptarget)

    Description for pDropTarget

## [PyIDocHostUIHandler](#pyidochostuihandler).GetExternal

 __GetExternal(__ )
Description of GetExternal.

## [PyIDocHostUIHandler](#pyidochostuihandler).GetHostInfo

 __GetHostInfo(__ )
Description of GetHostInfo.

## [PyIDocHostUIHandler](#pyidochostuihandler).GetOptionKeyPath

 __GetOptionKeyPath( *dw* __ )
Description of GetOptionKeyPath.

#### Parameters


  -  *dw* : int

    Description for dw

## [PyIDocHostUIHandler](#pyidochostuihandler).HideUI

 __HideUI(__ )
Description of HideUI.

## [PyIDocHostUIHandler](#pyidochostuihandler).OnDocWindowActivate

 __OnDocWindowActivate( *fActivate* __ )
Description of OnDocWindowActivate.

#### Parameters


  -  *fActivate* : int

    Description for fActivate

## [PyIDocHostUIHandler](#pyidochostuihandler).OnFrameWindowActivate

 __OnFrameWindowActivate( *fActivate* __ )
Description of OnFrameWindowActivate.

#### Parameters


  -  *fActivate* : int

    Description for fActivate

## [PyIDocHostUIHandler](#pyidochostuihandler).ResizeBorder

 __ResizeBorder( *prcBorder*  *, pUIWindow*  *, fRameWindow* __ )
Description of ResizeBorder.

#### Parameters


  -  *prcBorder* : (int, int, int, int)

    Description for prcBorder

  -  *pUIWindow* :[PyIOleInPlaceUIWindow](#pyioleinplaceuiwindow)

    Description for pUIWindow

  -  *fRameWindow* : int

    Description for fRameWindow

## [PyIDocHostUIHandler](#pyidochostuihandler).ShowContextMenu

 __ShowContextMenu( *dwID*  *, pt*  *, pcmdtReserved*  *, pdispReserved* __ )
Description of ShowContextMenu.

#### Parameters


  -  *dwID* : int

    Description for dwID

  -  *pt* : (int, int)

    Description for ppt

  -  *pcmdtReserved* :[PyIUnknown](#pyiunknown)

    Description for pcmdtReserved

  -  *pdispReserved* :[PyIDispatch](#pyidispatch)

    Description for pdispReserved

## [PyIDocHostUIHandler](#pyidochostuihandler).ShowUI

 __ShowUI( *dwID*  *, pActiveObject*  *, pCommandTarget*  *, pFrame*  *, pDoc* __ )
Description of ShowUI.

#### Parameters


  -  *dwID* : int

    Description for dwID

  -  *pActiveObject* :[PyIOleInPlaceActiveObject](#pyioleinplaceactiveobject)

    Description for pActiveObject

  -  *pCommandTarget* :[PyIOleCommandTarget](#pyiolecommandtarget)

    Description for pCommandTarget

  -  *pFrame* :[PyIOleInPlaceFrame](#pyioleinplaceframe)

    Description for pFrame

  -  *pDoc* :[PyIOleInPlaceUIWindow](#pyioleinplaceuiwindow)

    Description for pDoc

## [PyIDocHostUIHandler](#pyidochostuihandler).TranslateAccelerator

 __TranslateAccelerator( *lpMsg*  *, pguidCmdGroup*  *, nCmdID* __ )
Description of TranslateAccelerator.

#### Parameters


  -  *lpMsg* : __PyLPMSG__ 

    Description for lpMsg

  -  *pguidCmdGroup* :[PyIID](#pyiid)

    Description for pguidCmdGroup

  -  *nCmdID* : int

    Description for nCmdID

## [PyIDocHostUIHandler](#pyidochostuihandler).TranslateUrl

 __TranslateUrl( *dwTranslate*  *, pchURLIn* __ )
Description of TranslateUrl.

#### Parameters


  -  *dwTranslate* : int

    Description for dwTranslate

  -  *pchURLIn* : __unicode__ 

    Description for pchURLIn

## [PyIDocHostUIHandler](#pyidochostuihandler).UpdateUI

 __UpdateUI(__ )
Description of UpdateUI.