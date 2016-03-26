# PyIShellView

## PyIShellView Object

Description of the interface

#### Methods


  - [TranslateAccelerator](PyIShellView.md#pyishellviewtranslateaccelerator)

    Description of TranslateAccelerator&nbsp;

  - [EnableModeless](PyIShellView.md#pyishellviewenablemodeless)

    Description of EnableModeless&nbsp;

  - [UIActivate](PyIShellView.md#pyishellviewuiactivate)

    Description of UIActivate&nbsp;

  - [Refresh](PyIShellView.md#pyishellviewrefresh)

    Description of Refresh&nbsp;

  - [CreateViewWindow](PyIShellView.md#pyishellviewcreateviewwindow)

    Description of CreateViewWindow&nbsp;

  - [DestroyViewWindow](PyIShellView.md#pyishellviewdestroyviewwindow)

    Description of DestroyViewWindow&nbsp;

  - [GetCurrentInfo](PyIShellView.md#pyishellviewgetcurrentinfo)

    Description of GetCurrentInfo&nbsp;

  - [SaveViewState](PyIShellView.md#pyishellviewsaveviewstate)

    Description of SaveViewState&nbsp;

  - [SelectItem](PyIShellView.md#pyishellviewselectitem)

    Description of SelectItem&nbsp;

  - [GetItemObject](PyIShellView.md#pyishellviewgetitemobject)

    Description of GetItemObject&nbsp;

## [PyIShellView](#pyishellview)\.CreateViewWindow

int \= **CreateViewWindow\( *psvPrevious*  *, pfs*  *, psb*  *, prcView* ** \)
Description of CreateViewWindow\.

#### Parameters


  -  *psvPrevious* :[PyIShellView](#pyishellview)

    Description for psvPrevious

  -  *pfs* : \(int, int\)

    Description for pfs

  -  *psb* :[PyIShellBrowser](#pyishellbrowser)

    Description for psb

  -  *prcView* : \(int, int, int, int\)

    Description for prcView

#### Return Value
The result is an integer handle to the new window\.

## [PyIShellView](#pyishellview)\.DestroyViewWindow

 **DestroyViewWindow\(** \)
Description of DestroyViewWindow\.

## [PyIShellView](#pyishellview)\.EnableModeless

 **EnableModeless\( *fEnable* ** \)
Description of EnableModeless\.

#### Parameters


  -  *fEnable* : int

    Description for fEnable

## [PyIShellView](#pyishellview)\.GetCurrentInfo

 **PyFOLDERSETTINGS** \= **GetCurrentInfo\(** \)
Description of GetCurrentInfo\.

## [PyIShellView](#pyishellview)\.GetItemObject

[PyIUnknown](#pyiunknown)\= **GetItemObject\( *uItem*  *, riid* ** \)
Description of GetItemObject\.

#### Parameters


  -  *uItem* : int

    Description for uItem

  -  *riid* :[PyIID](#pyiid)

    Description for riid

## [PyIShellView](#pyishellview)\.Refresh

 **Refresh\(** \)
Description of Refresh\.

## [PyIShellView](#pyishellview)\.SaveViewState

 **SaveViewState\(** \)
Description of SaveViewState\.

## [PyIShellView](#pyishellview)\.SelectItem

 **SelectItem\( *pidlItem*  *, uFlags* ** \)
Description of SelectItem\.

#### Parameters


  -  *pidlItem* :[PyIDL](#pyidl)

    Description for pidlItem

  -  *uFlags* : int

    Description for uFlags

## [PyIShellView](#pyishellview)\.TranslateAccelerator

int \= **TranslateAccelerator\( *pmsg* ** \)
Description of TranslateAccelerator\.

#### Parameters


  -  *pmsg* : tuple

    Description for pmsg

#### Return Value
The result is the HRESULT from the underlying TranslateAccelerator call

## [PyIShellView](#pyishellview)\.UIActivate

 **UIActivate\( *uState* ** \)
Description of UIActivate\.

#### Parameters


  -  *uState* : int

    Description for uState