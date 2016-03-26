# PyIShellBrowser

## PyIShellBrowser Object

Exposed by Windows Explorer and the Open File common dialog box to provide services for namespace extensions.

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

## [PyIShellBrowser](#pyishellbrowser).BrowseObject

 __BrowseObject( *pidl*  *, wFlags* __ )
Navigates to a different location

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    Item id list that specifies the new browse location, can be None

  -  *wFlags* : int

    Combination of shellcon.SBSP_* flags

## [PyIShellBrowser](#pyishellbrowser).EnableModelessSB

 __EnableModelessSB( *fEnable* __ )
Enables or disables modeless dialogs

#### Parameters


  -  *fEnable* : boolean

    Use True to enable or False to disable modeless dialog boxes

## [PyIShellBrowser](#pyishellbrowser).GetControlWindow

 __GetControlWindow( *id* __ )
Returns a handle to one of the browser's control elements

#### Parameters


  -  *id* : int

    One of shellcon.FCW_* values

## [PyIShellBrowser](#pyishellbrowser).GetViewStateStream

[PyIStream](#pyistream)= __GetViewStateStream( *grfMode* __ )
Returns a stream that can be used to access view state information

#### Parameters


  -  *grfMode* : int

    Read/write mode, one of STGM_READ,STGM_WRITE,STGM_READWRITE

## [PyIShellBrowser](#pyishellbrowser).InsertMenusSB

[PyOLEMENUGROUPWIDTHS](#pyolemenugroupwidths)= __InsertMenusSB( *hmenuShared*  *, lpMenuWidths* __ )
Updates a composite menu with container's options

#### Parameters


  -  *hmenuShared* :[PyHANDLE](#pyhandle)

    Newly created menu that contains no items

  -  *lpMenuWidths* :[PyOLEMENUGROUPWIDTHS](#pyolemenugroupwidths)

    Tuple of 6 ints.  Items 0,2,and 4 are updated when the tuple is returned.

## [PyIShellBrowser](#pyishellbrowser).OnViewWindowActive

 __OnViewWindowActive( *pshv* __ )
Callback triggered when a view window is activated

#### Parameters


  -  *pshv* :[PyIShellView](#pyishellview)

    The activated view object

## [PyIShellBrowser](#pyishellbrowser).QueryActiveShellView

[PyIShellView](#pyishellview)= __QueryActiveShellView(__ )
Returns the currently displayed view

## [PyIShellBrowser](#pyishellbrowser).RemoveMenusSB

 __RemoveMenusSB( *hmenuShared* __ )
Asks container to remove any items it added to a composite menu

#### Parameters


  -  *hmenuShared* :[PyHANDLE](#pyhandle)

    Handle to the composite menu

## [PyIShellBrowser](#pyishellbrowser).SendControlMsg

int = __SendControlMsg( *id*  *, uMsg*  *, wParam*  *, lParam* __ )
Sends a control msg to browser's toolbar or status bar

#### Parameters


  -  *id* : int

    shellcon.FCW_TOOLBAR or FCW_STATUS

  -  *uMsg* : int

    The message to send

  -  *wParam* : int

    Value is dependent on the message

  -  *lParam* : long

    Value is dependent on the message

## [PyIShellBrowser](#pyishellbrowser).SetMenuSB

 __SetMenuSB( *hmenuShared*  *, holemenuRes*  *, hwndActiveObject* __ )
Attaches a shared menu to a shell view window

#### Parameters


  -  *hmenuShared* :[PyHANDLE](#pyhandle)

    Handle to the shared menu

  -  *holemenuRes* :[PyHANDLE](#pyhandle)

    Reserved, use only None (or 0)

  -  *hwndActiveObject* :[PyHANDLE](#pyhandle)

    Handle to the shell window

## [PyIShellBrowser](#pyishellbrowser).SetStatusTextSB

 __SetStatusTextSB( *pszStatusText* __ )
Sets the status text in view's status bar

#### Parameters


  -  *pszStatusText* : str

    New status to be displayed

## [PyIShellBrowser](#pyishellbrowser).SetToolbarItems

 __SetToolbarItems( *lpButtons*  *, uFlags* __ )
Adds toolbar buttons to the browser's toolbar

#### Parameters


  -  *lpButtons* : __PyLPTBBUTTONSB__ 

    Sequence of tuples describing the buttons to be added

  -  *uFlags* : int

    Indicates button positions, combination of shellcon.FCT_*

## [PyIShellBrowser](#pyishellbrowser).TranslateAcceleratorSB

 __TranslateAcceleratorSB( *pmsg*  *, wID* __ )
Translates keystrokes used as menu item activators

#### Parameters


  -  *pmsg* :[PyMSG](#pymsg)

    Keystroke message to be translated

  -  *wID* : int

    Menu command id for the keystroke