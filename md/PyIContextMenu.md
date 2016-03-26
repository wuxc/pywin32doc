# PyIContextMenu


## PyIContextMenu Object

Description of the interface

#### Methods

  - [QueryContextMenu](PyIContextMenu.md#pyicontextmenuquerycontextmenu)

    Adds options to a context menu&nbsp;

  - [InvokeCommand](PyIContextMenu.md#pyicontextmenuinvokecommand)

    Executes a context menu option&nbsp;

  - [GetCommandString](PyIContextMenu.md#pyicontextmenugetcommandstring)

    Retrieves verb or help text for a context menu option&nbsp;


## [PyIContextMenu](PyIContextMenu.md#pyicontextmenu)\.GetCommandString

str = GetCommandString\(idCmd, uType

, cchMax

\)
Retrieves verb or help text for a context menu option

#### Parameters

  - idCmd : int

    Id of the command

  - uType : int

    One of the shellcon\.GCS\_\* constants

  - cchMax=2048 : int

    Size of buffer to create for returned string


## [PyIContextMenu](PyIContextMenu.md#pyicontextmenu)\.InvokeCommand

InvokeCommand\(pici\)
Executes a context menu option

#### Parameters

  - pici : [PyCMINVOKECOMMANDINFO](PyCMINVOKECOMMANDINFO.md)

    Tuple of parameters representing a CMINVOKECOMMANDINFO struct


## [PyIContextMenu](PyIContextMenu.md#pyicontextmenu)\.QueryContextMenu

int = QueryContextMenu\(hmenu, indexMenu

, idCmdFirst

, idCmdLast

, uFlags

\)
Adds options to a context menu

#### Parameters

  - hmenu : [PyHANDLE](PyHANDLE.md)

    Handle to menu to which items should be added

  - indexMenu : int

    Zero-based index at which to add first item

  - idCmdFirst : int

    Minimum menu item Id

  - idCmdLast : int

    Max menu item Id

  - uFlags : int

    Combination of shellcon\.CMF\_\* flags, can be 0