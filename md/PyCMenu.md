# PyCMenu

## PyCMenu Object

A windows menu.  Encapsulates an MFC __CMenu__ class

#### Methods


  - [AppendMenu](PyCMenu.md#pycmenuappendmenu)

    Appends a new item to the end of a menu. Python can specify the state of the menu item by setting values in nFlags.&nbsp;

  - [DeleteMenu](PyCMenu.md#pycmenudeletemenu)

    Deletes the specified menu item.&nbsp;

  - [EnableMenuItem](PyCMenu.md#pycmenuenablemenuitem)

    Enables, disables, or dims a menu item.&nbsp;

  - [GetHandle](PyCMenu.md#pycmenugethandle)

    Returns the menu object's underlying hMenu.&nbsp;

  - [GetMenuItemCount](PyCMenu.md#pycmenugetmenuitemcount)

    Determines the number of items in a menu.&nbsp;

  - [GetMenuItemID](PyCMenu.md#pycmenugetmenuitemid)

    Returns the item ID for the specified item in a pop-up menu.&nbsp;

  - [GetMenuString](PyCMenu.md#pycmenugetmenustring)

    Returns the string for a specified menu item.&nbsp;

  - [GetSubMenu](PyCMenu.md#pycmenugetsubmenu)

    Returns a submenu.&nbsp;

  - [InsertMenu](PyCMenu.md#pycmenuinsertmenu)

    Inserts an item into a menu.&nbsp;

  - [ModifyMenu](PyCMenu.md#pycmenumodifymenu)

    Modify an item in a menu.&nbsp;

  - [TrackPopupMenu](PyCMenu.md#pycmenutrackpopupmenu)

    Creates a popup menu anywhere on the screen.&nbsp;

## [PyCMenu](#pycmenu).AppendMenu

 __AppendMenu( *flags*  *, id*  *, value* __ )
Appends a new item to the end of a menu. Python can specify the state of the menu item by setting values in nFlags.

#### Parameters


  -  *flags* : int

    Specifies information about the state of the new menu item when it is added to the menu.  May be a combination of the win32con.MF_* values.

  -  *id=0* : int

    Specifies either the command ID of the new menu item.

  -  *value=None* : string/None

    Specifies the content of the new menu item.  If used, flags must contain win32con.MF_STRING.

## [PyCMenu](#pycmenu).DeleteMenu

string = __DeleteMenu( *id*  *, flags* __ )
Deletes the specified menu item.

#### Parameters


  -  *id* : int

    The id of the item being deleted.

  -  *flags* : int

    Specifies how the id parameter is interpreted. It must be one of win32con.MF_BYCOMMAND or win32con.MF_BYPOSITION.

## [PyCMenu](#pycmenu).EnableMenuItem

int = __EnableMenuItem( *id*  *, flags* __ )
Enables, disables, or dims a menu item.

#### Parameters


  -  *id* : int

    Specifies the command ID of the menu item. This parameter can specify pop-up menu items as well as standard menu items.

  -  *flags* : int

    Specifies the action to take. It can be a combination of MF_DISABLED, MF_ENABLED, or MF_GRAYED, with MF_BYCOMMAND or MF_BYPOSITION

#### Comments
The __PyCMenu::CreateMenu__ ,[PyCMenu::InsertMenu](PyCMenu.md#pycmenuinsertmenu),[PyCMenu::ModifyMenu](PyCMenu.md#pycmenumodifymenu), 

and __PyCMenu::LoadMenuIndirect__ member functions can also set the state 

(enabled, disabled, or dimmed) of a menu item.

## [PyCMenu](#pycmenu).GetHandle

int = __GetHandle(__ )
Returns the menu object's underlying hMenu.

## [PyCMenu](#pycmenu).GetMenuItemCount

int = __GetMenuItemCount(__ )
Determines the number of items in a menu.

#### Return Value
The number of items in the menu if the function is successful; otherwise -1.

## [PyCMenu](#pycmenu).GetMenuItemID

int = __GetMenuItemID( *pos* __ )
Returns the item ID for the specified item in a pop-up menu.

#### Parameters


  -  *pos* : int

    The position (zero-based) of the menu item whose ID is being retrieved.

#### Comments
If the specified item is a pop-up menu (as opposed to an item within the pop-up menu), 

the return value is -1. If nPos corresponds to a SEPARATOR menu item, 

the return value is 0.

## [PyCMenu](#pycmenu).GetMenuString

string = __GetMenuString( *id*  *, flags* __ )
Returns the string for a specified menu item.

#### Parameters


  -  *id* : int

    The id of the item being requested.

  -  *flags=win32con.MF_BYCOMMAND* : int

    Specifies how the id parameter is interpreted. It must be one of win32con.MF_BYCOMMAND or win32con.MF_BYPOSITION.

## [PyCMenu](#pycmenu).GetSubMenu

[PyCMenu](#pycmenu)= __GetSubMenu( *pos* __ )
Returns a submenu.

#### Parameters


  -  *pos* : int

    The position (zero-based) of the menu item being retrieved.

## [PyCMenu](#pycmenu).InsertMenu

 __InsertMenu( *pos*  *, flags*  *, id*  *, value* __ )
Inserts an item into a menu.

#### Parameters


  -  *pos* : int

    The position (zero-based) the item should be inserted.

  -  *flags* : int

    Flags for the new item.

  -  *id=0* : int/[PyCMenu](#pycmenu)

    The ID for a new menu item, or handle to a submenu

  -  *value=None* : string/None

    A string for the menu item.

## [PyCMenu](#pycmenu).ModifyMenu

 __ModifyMenu( *pos*  *, flags*  *, id*  *, value* __ )
Modify an item in a menu.

#### Parameters


  -  *pos* : int

    The position (zero-based) the item to be changed.

  -  *flags* : int

    Flags for the item.

  -  *id=0* : int

    The ID for the item.

  -  *value=None* : string/None

    A string for the menu item.

## [PyCMenu](#pycmenu).TrackPopupMenu

 __TrackPopupMenu( *(x,y)*  *, flags*  *, owner* __ )
Creates a popup menu anywhere on the screen.

#### Parameters


  -  *(x,y)* : (int, int)

    The position for the menu..

  -  *flags=win32con.TPM_LEFTALIGN|win32con.TPM_LEFTBUTTON|win32con.TPM_RIGHTBUTTON* : int

    Flags for the menu.

  -  *owner=(main application frame)* :[PyCWnd](#pycwnd)

    The owner of the menu.

#### Comments
The TrackPopupMenu function displays a floating pop-up menu at the 

specified location and tracks the selection of items on the pop-up menu. 

The floating pop-up menu can appear anywhere on the screen.

#### Return Value
If the underlying MFC function fails, but TPM_RETURNCMD is set in the flags parameter, then None is returned instead of the normal exception.