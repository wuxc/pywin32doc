# PyIExplorerBrowser

## PyIExplorerBrowser Object

Description of the interface

#### Methods


  - [Initialize](PyIExplorerBrowser.md#pyiexplorerbrowserinitialize)

    Description of Initialize&nbsp;

  - [Destroy](PyIExplorerBrowser.md#pyiexplorerbrowserdestroy)

    Description of Destroy&nbsp;

  - [SetRect](PyIExplorerBrowser.md#pyiexplorerbrowsersetrect)

    Description of SetRect&nbsp;

  - [SetPropertyBag](PyIExplorerBrowser.md#pyiexplorerbrowsersetpropertybag)

    Description of SetPropertyBag&nbsp;

  - [SetEmptyText](PyIExplorerBrowser.md#pyiexplorerbrowsersetemptytext)

    Description of SetEmptyText&nbsp;

  - [SetFolderSettings](PyIExplorerBrowser.md#pyiexplorerbrowsersetfoldersettings)

    Description of SetFolderSettings&nbsp;

  - [Advise](PyIExplorerBrowser.md#pyiexplorerbrowseradvise)

    Description of Advise&nbsp;

  - [Unadvise](PyIExplorerBrowser.md#pyiexplorerbrowserunadvise)

    Description of Unadvise&nbsp;

  - [SetOptions](PyIExplorerBrowser.md#pyiexplorerbrowsersetoptions)

    Description of SetOptions&nbsp;

  - [GetOptions](PyIExplorerBrowser.md#pyiexplorerbrowsergetoptions)

    Description of GetOptions&nbsp;

  - [BrowseToIDList](PyIExplorerBrowser.md#pyiexplorerbrowserbrowsetoidlist)

    Description of BrowseToIDList&nbsp;

  - [BrowseToObject](PyIExplorerBrowser.md#pyiexplorerbrowserbrowsetoobject)

    Description of BrowseToObject&nbsp;

  - [FillFromObject](PyIExplorerBrowser.md#pyiexplorerbrowserfillfromobject)

    Description of FillFromObject&nbsp;

  - [RemoveAll](PyIExplorerBrowser.md#pyiexplorerbrowserremoveall)

    Description of RemoveAll&nbsp;

  - [GetCurrentView](PyIExplorerBrowser.md#pyiexplorerbrowsergetcurrentview)

    Description of GetCurrentView&nbsp;

## [PyIExplorerBrowser](#pyiexplorerbrowser).Advise

int = __Advise( *psbe* __ )
Description of Advise.

#### Parameters


  -  *psbe* :[PyIExplorerBrowserEvents](#pyiexplorerbrowserevents)

    Description for psbe

## [PyIExplorerBrowser](#pyiexplorerbrowser).BrowseToIDList

 __BrowseToIDList( *pidl*  *, uFlags* __ )
Description of BrowseToIDList.

#### Parameters


  -  *pidl* : __PyPCUIDLIST_RELATIVE__ 

    Description for pidl

  -  *uFlags* : int

    Description for uFlags

## [PyIExplorerBrowser](#pyiexplorerbrowser).BrowseToObject

 __BrowseToObject( *punk*  *, uFlags* __ )
Description of BrowseToObject.

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Description for punk

  -  *uFlags* : int

    Description for uFlags

## [PyIExplorerBrowser](#pyiexplorerbrowser).Destroy

 __Destroy(__ )
Description of Destroy.

## [PyIExplorerBrowser](#pyiexplorerbrowser).FillFromObject

 __FillFromObject( *punk*  *, dwFlags* __ )
Description of FillFromObject.

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Description for punk

  -  *dwFlags* : __PyEXPLORER_BROWSER_FILL_FLAGS__ 

    Description for dwFlags

## [PyIExplorerBrowser](#pyiexplorerbrowser).GetCurrentView

[PyIUnknown](#pyiunknown)= __GetCurrentView( *riid* __ )
Description of GetCurrentView.

#### Parameters


  -  *riid* :[PyIID](#pyiid)

    Description for riid

## [PyIExplorerBrowser](#pyiexplorerbrowser).GetOptions

int = __GetOptions(__ )
Description of GetOptions.

## [PyIExplorerBrowser](#pyiexplorerbrowser).Initialize

 __Initialize( *hwndParent*  *, prc*  *, pfs* __ )
Description of Initialize.

#### Parameters


  -  *hwndParent* : HWND

    Description for hwndParent

  -  *prc* :[PyRECT](#pyrect)

    Description for prc

  -  *pfs* : __PyFOLDERSETTINGS__ 

    Description for pfs

## [PyIExplorerBrowser](#pyiexplorerbrowser).RemoveAll

 __RemoveAll(__ )
Description of RemoveAll.

## [PyIExplorerBrowser](#pyiexplorerbrowser).SetEmptyText

 __SetEmptyText( *EmptyText* __ )
Description of SetEmptyText.

#### Parameters


  -  *EmptyText* : str

    Description for pszEmptyText

## [PyIExplorerBrowser](#pyiexplorerbrowser).SetFolderSettings

 __SetFolderSettings( *pfs* __ )
Description of SetFolderSettings.

#### Parameters


  -  *pfs* : __PyFOLDERSETTINGS__ 

    Description for pfs

## [PyIExplorerBrowser](#pyiexplorerbrowser).SetOptions

 __SetOptions( *dwFlag* __ )
Description of SetOptions.

#### Parameters


  -  *dwFlag* : __PyEXPLORER_BROWSER_OPTIONS__ 

    Description for dwFlag

## [PyIExplorerBrowser](#pyiexplorerbrowser).SetPropertyBag

 __SetPropertyBag( *PropertyBag* __ )
Description of SetPropertyBag.

#### Parameters


  -  *PropertyBag* : str

    Description for pszPropertyBag

## [PyIExplorerBrowser](#pyiexplorerbrowser).SetRect

[PyHANDLE](#pyhandle)= __SetRect( *hdwp*  *, rcBrowser* __ )
Description of SetRect.

#### Parameters


  -  *hdwp* : __PyHDWP__ 

    Description for phdwp

  -  *rcBrowser* :[PyRECT](#pyrect)

    Description for rcBrowser

## [PyIExplorerBrowser](#pyiexplorerbrowser).Unadvise

 __Unadvise( *dwCookie* __ )
Description of Unadvise.

#### Parameters


  -  *dwCookie* : int

    Description for dwCookie