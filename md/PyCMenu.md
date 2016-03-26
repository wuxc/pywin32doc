# PyCMenu


## PyCMenu Object

A windows menu\.  Encapsulates an MFC CMenu

 class

#### Methods

  - [AppendMenu](PyCMenu.md#pycmenuappendmenu)

    Appends a new item to the end of a menu\. Python can specify the state of the menu item by setting values in nFlags\.&nbsp;

  - [DeleteMenu](PyCMenu.md#pycmenudeletemenu)

    Deletes the specified menu item\.&nbsp;

  - [EnableMenuItem](PyCMenu.md#pycmenuenablemenuitem)

    Enables, disables, or dims a menu item\.&nbsp;

  - [GetHandle](PyCMenu.md#pycmenugethandle)

    Returns the menu object's underlying hMenu\.&nbsp;

  - [GetMenuItemCount](PyCMenu.md#pycmenugetmenuitemcount)

    Determines the number of items in a menu\.&nbsp;

  - [GetMenuItemID](PyCMenu.md#pycmenugetmenuitemid)

    Returns the item ID for the specified item in a pop-up menu\.&nbsp;

  - [GetMenuString](PyCMenu.md#pycmenugetmenustring)

    Returns the string for a specified menu item\.&nbsp;

  - [GetSubMenu](PyCMenu.md#pycmenugetsubmenu)

    Returns a submenu\.&nbsp;

  - [InsertMenu](PyCMenu.md#pycmenuinsertmenu)

    Inserts an item into a menu\.&nbsp;

  - [ModifyMenu](PyCMenu.md#pycmenumodifymenu)

    Modify an item in a menu\.&nbsp;

  - [TrackPopupMenu](PyCMenu.md#pycmenutrackpopupmenu)

    Creates a popup menu anywhere on the screen\.&nbsp;


## [PyCMenu](PyCMenu.md#pycmenu)\.AppendMenu

AppendMenu\(flags, id, value\)
Appends a new item to the end of a menu\. Python can specify the state of the menu item by setting values in nFlags\.

#### Parameters

  - flags : int

    Specifies information about the state of the new menu item when it is added to the menu\.  May be a combination of the win32con\.MF\_\* values\.

  - id=0 : int

    Specifies either the command ID of the new menu item\.

  - value=None : string/None

    Specifies the content of the new menu item\.  If used, flags must contain win32con\.MF\_STRING\.


## [PyCMenu](PyCMenu.md#pycmenu)\.DeleteMenu

string = DeleteMenu\(id, flags

\)
Deletes the specified menu item\.

#### Parameters

  - id : int

    The id of the item being deleted\.

  - flags : int

    Specifies how the id parameter is interpreted\. It must be one of win32con\.MF\_BYCOMMAND or win32con\.MF\_BYPOSITION\.


## [PyCMenu](PyCMenu.md#pycmenu)\.EnableMenuItem

int = EnableMenuItem\(id, flags

\)
Enables, disables, or dims a menu item\.

#### Parameters

  - id : int

    Specifies the command ID of the menu item\. This parameter can specify pop-up menu items as well as standard menu items\.

  - flags : int

    Specifies the action to take\. It can be a combination of MF\_DISABLED, MF\_ENABLED, or MF\_GRAYED, with MF\_BYCOMMAND or MF\_BYPOSITION

#### Comments

The PyCMenu::CreateMenu

, [PyCMenu::InsertMenu](PyCMenu.md#pycmenuinsertmenu), [PyCMenu::ModifyMenu](PyCMenu.md#pycmenumodifymenu), 

and PyCMenu::LoadMenuIndirect

 member functions can also set the state 

\(enabled, disabled, or dimmed\) of a menu item\.


## [PyCMenu](PyCMenu.md#pycmenu)\.GetHandle

int = GetHandle\(\)
Returns the menu object's underlying hMenu\.


## [PyCMenu](PyCMenu.md#pycmenu)\.GetMenuItemCount

int = GetMenuItemCount\(\)
Determines the number of items in a menu\.

#### Return Value
The number of items in the menu if the function is successful; otherwise -1\.


## [PyCMenu](PyCMenu.md#pycmenu)\.GetMenuItemID

int = GetMenuItemID\(pos\)
Returns the item ID for the specified item in a pop-up menu\.

#### Parameters

  - pos : int

    The position \(zero-based\) of the menu item whose ID is being retrieved\.

#### Comments

If the specified item is a pop-up menu \(as opposed to an item within the pop-up menu\), 

the return value is -1\. If nPos corresponds to a SEPARATOR menu item, 

the return value is 0\.


## [PyCMenu](PyCMenu.md#pycmenu)\.GetMenuString

string = GetMenuString\(id, flags

\)
Returns the string for a specified menu item\.

#### Parameters

  - id : int

    The id of the item being requested\.

  - flags=win32con\.MF\_BYCOMMAND : int

    Specifies how the id parameter is interpreted\. It must be one of win32con\.MF\_BYCOMMAND or win32con\.MF\_BYPOSITION\.


## [PyCMenu](PyCMenu.md#pycmenu)\.GetSubMenu

[PyCMenu](PyCMenu.md#pycmenu) = GetSubMenu\(pos\)
Returns a submenu\.

#### Parameters

  - pos : int

    The position \(zero-based\) of the menu item being retrieved\.


## [PyCMenu](PyCMenu.md#pycmenu)\.InsertMenu

InsertMenu\(pos, flags, id, value\)
Inserts an item into a menu\.

#### Parameters

  - pos : int

    The position \(zero-based\) the item should be inserted\.

  - flags : int

    Flags for the new item\.

  - id=0 : int/[PyCMenu](PyCMenu.md#pycmenu)

    The ID for a new menu item, or handle to a submenu

  - value=None : string/None

    A string for the menu item\.


## [PyCMenu](PyCMenu.md#pycmenu)\.ModifyMenu

ModifyMenu\(pos, flags, id, value\)
Modify an item in a menu\.

#### Parameters

  - pos : int

    The position \(zero-based\) the item to be changed\.

  - flags : int

    Flags for the item\.

  - id=0 : int

    The ID for the item\.

  - value=None : string/None

    A string for the menu item\.


## [PyCMenu](PyCMenu.md#pycmenu)\.TrackPopupMenu

TrackPopupMenu\(\(x,y\), flags, owner\)
Creates a popup menu anywhere on the screen\.

#### Parameters

  - \(x,y\) : \(int, int\)

    The position for the menu\.\.

  - flags=win32con\.TPM\_LEFTALIGN|win32con\.TPM\_LEFTBUTTON|win32con\.TPM\_RIGHTBUTTON : int

    Flags for the menu\.

  - owner=\(main application frame\) : [PyCWnd](PyCWnd.md)

    The owner of the menu\.

#### Comments

The TrackPopupMenu function displays a floating pop-up menu at the 

specified location and tracks the selection of items on the pop-up menu\. 

The floating pop-up menu can appear anywhere on the screen\.

#### Return Value
If the underlying MFC function fails, but TPM\_RETURNCMD is set in the flags parameter, then None is returned instead of the normal exception\.