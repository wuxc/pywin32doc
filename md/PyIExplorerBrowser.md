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


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.Advise

int = Advise\(psbe\)
Description of Advise\.

#### Parameters

  - psbe : [PyIExplorerBrowserEvents](PyIExplorerBrowserEvents.md)

    Description for psbe


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.BrowseToIDList

BrowseToIDList\(pidl, uFlags\)
Description of BrowseToIDList\.

#### Parameters

  - pidl : PyPCUIDLIST\_RELATIVE

    Description for pidl

  - uFlags : int

    Description for uFlags


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.BrowseToObject

BrowseToObject\(punk, uFlags\)
Description of BrowseToObject\.

#### Parameters

  - punk : [PyIUnknown](PyIUnknown.md)

    Description for punk

  - uFlags : int

    Description for uFlags


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.Destroy

Destroy\(\)
Description of Destroy\.


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.FillFromObject

FillFromObject\(punk, dwFlags\)
Description of FillFromObject\.

#### Parameters

  - punk : [PyIUnknown](PyIUnknown.md)

    Description for punk

  - dwFlags : PyEXPLORER\_BROWSER\_FILL\_FLAGS

    Description for dwFlags


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.GetCurrentView

[PyIUnknown](PyIUnknown.md) = GetCurrentView\(riid\)
Description of GetCurrentView\.

#### Parameters

  - riid : [PyIID](PyIID.md)

    Description for riid


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.GetOptions

int = GetOptions\(\)
Description of GetOptions\.


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.Initialize

Initialize\(hwndParent, prc, pfs\)
Description of Initialize\.

#### Parameters

  - hwndParent : HWND

    Description for hwndParent

  - prc : [PyRECT](PyRECT.md)

    Description for prc

  - pfs : PyFOLDERSETTINGS

    Description for pfs


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.RemoveAll

RemoveAll\(\)
Description of RemoveAll\.


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.SetEmptyText

SetEmptyText\(EmptyText\)
Description of SetEmptyText\.

#### Parameters

  - EmptyText : str

    Description for pszEmptyText


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.SetFolderSettings

SetFolderSettings\(pfs\)
Description of SetFolderSettings\.

#### Parameters

  - pfs : PyFOLDERSETTINGS

    Description for pfs


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.SetOptions

SetOptions\(dwFlag\)
Description of SetOptions\.

#### Parameters

  - dwFlag : PyEXPLORER\_BROWSER\_OPTIONS

    Description for dwFlag


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.SetPropertyBag

SetPropertyBag\(PropertyBag\)
Description of SetPropertyBag\.

#### Parameters

  - PropertyBag : str

    Description for pszPropertyBag


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.SetRect

[PyHANDLE](PyHANDLE.md) = SetRect\(hdwp, rcBrowser

\)
Description of SetRect\.

#### Parameters

  - hdwp : PyHDWP

    Description for phdwp

  - rcBrowser : [PyRECT](PyRECT.md)

    Description for rcBrowser


## [PyIExplorerBrowser](PyIExplorerBrowser.md#pyiexplorerbrowser)\.Unadvise

Unadvise\(dwCookie\)
Description of Unadvise\.

#### Parameters

  - dwCookie : int

    Description for dwCookie