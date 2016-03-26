# PyIShellBrowser

## PyIShellBrowser Object



Exposed by Windows Explorer and the Open File common dialog box to provide services for namespace extensions\.

#### Methods


  - [InsertMenusSB](PyIShellBrowser.md#pyishellbrowserinsertmenussb)

    Updates a composite menu with container's options&nbsp;

  - [SetMenuSB](PyIShellBrowser.md#pyishellbrowsersetmenusb)

    Attaches a shared menu to a shell view window&nbsp;

  - [RemoveMenusSB](PyIShellBrowser.md#pyishellbrowserremovemenussb)

    Asks container to remove any items it added to a composite menu&nbsp;

  - [SetStatusTextSB](PyIShellBrowser.md#pyishellbrowsersetstatustextsb)

    Sets the status text in view's status bar&nbsp;

  - [EnableModelessSB](PyIShellBrowser.md#pyishellbrowserenablemodelesssb)

    Enables or disables modeless dialogs&nbsp;

  - [TranslateAcceleratorSB](PyIShellBrowser.md#pyishellbrowsertranslateacceleratorsb)

    Translates keystrokes used as menu item activators&nbsp;

  - [BrowseObject](PyIShellBrowser.md#pyishellbrowserbrowseobject)

    Navigates to a different location&nbsp;

  - [GetViewStateStream](PyIShellBrowser.md#pyishellbrowsergetviewstatestream)

    Returns a stream that can be used to access view state information&nbsp;

  - [GetControlWindow](PyIShellBrowser.md#pyishellbrowsergetcontrolwindow)

    Returns a handle to one of the browser's control elements&nbsp;

  - [SendControlMsg](PyIShellBrowser.md#pyishellbrowsersendcontrolmsg)

    Sends a control msg to browser's toolbar or status bar&nbsp;

  - [QueryActiveShellView](PyIShellBrowser.md#pyishellbrowserqueryactiveshellview)

    Returns the currently displayed view&nbsp;

  - [OnViewWindowActive](PyIShellBrowser.md#pyishellbrowseronviewwindowactive)

    Callback triggered when a view window is activated&nbsp;

  - [SetToolbarItems](PyIShellBrowser.md#pyishellbrowsersettoolbaritems)

    Adds toolbar buttons to the browser's toolbar&nbsp;

## [PyIShellBrowser](#pyishellbrowser)\.BrowseObject

BrowseObject\(pidl, wFlags\)
Navigates to a different location

#### Parameters


  - pidl :[PyIDL](#pyidl)

    Item id list that specifies the new browse location, can be None

  - wFlags : int

    Combination of shellcon\.SBSP\_\* flags

## [PyIShellBrowser](#pyishellbrowser)\.EnableModelessSB

EnableModelessSB\(fEnable\)
Enables or disables modeless dialogs

#### Parameters


  - fEnable : boolean

    Use True to enable or False to disable modeless dialog boxes

## [PyIShellBrowser](#pyishellbrowser)\.GetControlWindow

GetControlWindow\(id\)
Returns a handle to one of the browser's control elements

#### Parameters


  - id : int

    One of shellcon\.FCW\_\* values

## [PyIShellBrowser](#pyishellbrowser)\.GetViewStateStream

[PyIStream](#pyistream) =GetViewStateStream\(grfMode\)
Returns a stream that can be used to access view state information

#### Parameters


  - grfMode : int

    Read/write mode, one of STGM\_READ,STGM\_WRITE,STGM\_READWRITE

## [PyIShellBrowser](#pyishellbrowser)\.InsertMenusSB

[PyOLEMENUGROUPWIDTHS](#pyolemenugroupwidths) =InsertMenusSB\(hmenuShared, lpMenuWidths\)
Updates a composite menu with container's options

#### Parameters


  - hmenuShared :[PyHANDLE](#pyhandle)

    Newly created menu that contains no items

  - lpMenuWidths :[PyOLEMENUGROUPWIDTHS](#pyolemenugroupwidths)

    Tuple of 6 ints\.  Items 0,2,and 4 are updated when the tuple is returned\.

## [PyIShellBrowser](#pyishellbrowser)\.OnViewWindowActive

OnViewWindowActive\(pshv\)
Callback triggered when a view window is activated

#### Parameters


  - pshv :[PyIShellView](#pyishellview)

    The activated view object

## [PyIShellBrowser](#pyishellbrowser)\.QueryActiveShellView

[PyIShellView](#pyishellview) =QueryActiveShellView\(\)
Returns the currently displayed view

## [PyIShellBrowser](#pyishellbrowser)\.RemoveMenusSB

RemoveMenusSB\(hmenuShared\)
Asks container to remove any items it added to a composite menu

#### Parameters


  - hmenuShared :[PyHANDLE](#pyhandle)

    Handle to the composite menu

## [PyIShellBrowser](#pyishellbrowser)\.SendControlMsg



int =SendControlMsg\(id, uMsg, wParam, lParam\)
Sends a control msg to browser's toolbar or status bar

#### Parameters


  - id : int

    shellcon\.FCW\_TOOLBAR or FCW\_STATUS

  - uMsg : int

    The message to send

  - wParam : int

    Value is dependent on the message

  - lParam : long

    Value is dependent on the message

## [PyIShellBrowser](#pyishellbrowser)\.SetMenuSB

SetMenuSB\(hmenuShared, holemenuRes, hwndActiveObject\)
Attaches a shared menu to a shell view window

#### Parameters


  - hmenuShared :[PyHANDLE](#pyhandle)

    Handle to the shared menu

  - holemenuRes :[PyHANDLE](#pyhandle)

    Reserved, use only None \(or 0\)

  - hwndActiveObject :[PyHANDLE](#pyhandle)

    Handle to the shell window

## [PyIShellBrowser](#pyishellbrowser)\.SetStatusTextSB

SetStatusTextSB\(pszStatusText\)
Sets the status text in view's status bar

#### Parameters


  - pszStatusText : str

    New status to be displayed

## [PyIShellBrowser](#pyishellbrowser)\.SetToolbarItems

SetToolbarItems\(lpButtons, uFlags\)
Adds toolbar buttons to the browser's toolbar

#### Parameters


  - lpButtons :PyLPTBBUTTONSB

    Sequence of tuples describing the buttons to be added

  - uFlags : int

    Indicates button positions, combination of shellcon\.FCT\_\*

## [PyIShellBrowser](#pyishellbrowser)\.TranslateAcceleratorSB

TranslateAcceleratorSB\(pmsg, wID\)
Translates keystrokes used as menu item activators

#### Parameters


  - pmsg :[PyMSG](#pymsg)

    Keystroke message to be translated

  - wID : int

    Menu command id for the keystroke