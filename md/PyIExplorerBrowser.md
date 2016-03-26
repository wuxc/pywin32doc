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

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.Advise

int \= **Advise\( *psbe* ** \)
Description of Advise\.

#### Parameters


  -  *psbe* :[PyIExplorerBrowserEvents](#pyiexplorerbrowserevents)

    Description for psbe

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.BrowseToIDList

 **BrowseToIDList\( *pidl*  *, uFlags* ** \)
Description of BrowseToIDList\.

#### Parameters


  -  *pidl* : **PyPCUIDLIST\_RELATIVE** 

    Description for pidl

  -  *uFlags* : int

    Description for uFlags

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.BrowseToObject

 **BrowseToObject\( *punk*  *, uFlags* ** \)
Description of BrowseToObject\.

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Description for punk

  -  *uFlags* : int

    Description for uFlags

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.Destroy

 **Destroy\(** \)
Description of Destroy\.

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.FillFromObject

 **FillFromObject\( *punk*  *, dwFlags* ** \)
Description of FillFromObject\.

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Description for punk

  -  *dwFlags* : **PyEXPLORER\_BROWSER\_FILL\_FLAGS** 

    Description for dwFlags

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.GetCurrentView

[PyIUnknown](#pyiunknown)\= **GetCurrentView\( *riid* ** \)
Description of GetCurrentView\.

#### Parameters


  -  *riid* :[PyIID](#pyiid)

    Description for riid

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.GetOptions

int \= **GetOptions\(** \)
Description of GetOptions\.

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.Initialize

 **Initialize\( *hwndParent*  *, prc*  *, pfs* ** \)
Description of Initialize\.

#### Parameters


  -  *hwndParent* : HWND

    Description for hwndParent

  -  *prc* :[PyRECT](#pyrect)

    Description for prc

  -  *pfs* : **PyFOLDERSETTINGS** 

    Description for pfs

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.RemoveAll

 **RemoveAll\(** \)
Description of RemoveAll\.

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.SetEmptyText

 **SetEmptyText\( *EmptyText* ** \)
Description of SetEmptyText\.

#### Parameters


  -  *EmptyText* : str

    Description for pszEmptyText

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.SetFolderSettings

 **SetFolderSettings\( *pfs* ** \)
Description of SetFolderSettings\.

#### Parameters


  -  *pfs* : **PyFOLDERSETTINGS** 

    Description for pfs

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.SetOptions

 **SetOptions\( *dwFlag* ** \)
Description of SetOptions\.

#### Parameters


  -  *dwFlag* : **PyEXPLORER\_BROWSER\_OPTIONS** 

    Description for dwFlag

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.SetPropertyBag

 **SetPropertyBag\( *PropertyBag* ** \)
Description of SetPropertyBag\.

#### Parameters


  -  *PropertyBag* : str

    Description for pszPropertyBag

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.SetRect

[PyHANDLE](#pyhandle)\= **SetRect\( *hdwp*  *, rcBrowser* ** \)
Description of SetRect\.

#### Parameters


  -  *hdwp* : **PyHDWP** 

    Description for phdwp

  -  *rcBrowser* :[PyRECT](#pyrect)

    Description for rcBrowser

## [PyIExplorerBrowser](#pyiexplorerbrowser)\.Unadvise

 **Unadvise\( *dwCookie* ** \)
Description of Unadvise\.

#### Parameters


  -  *dwCookie* : int

    Description for dwCookie