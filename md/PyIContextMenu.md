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

## [PyIContextMenu](#pyicontextmenu).GetCommandString

str = __GetCommandString( *idCmd*  *, uType*  *, cchMax* __ )
Retrieves verb or help text for a context menu option

#### Parameters


  -  *idCmd* : int

    Id of the command

  -  *uType* : int

    One of the shellcon.GCS_* constants

  -  *cchMax=2048* : int

    Size of buffer to create for returned string

## [PyIContextMenu](#pyicontextmenu).InvokeCommand

 __InvokeCommand( *pici* __ )
Executes a context menu option

#### Parameters


  -  *pici* :[PyCMINVOKECOMMANDINFO](#pycminvokecommandinfo)

    Tuple of parameters representing a CMINVOKECOMMANDINFO struct

## [PyIContextMenu](#pyicontextmenu).QueryContextMenu

int = __QueryContextMenu( *hmenu*  *, indexMenu*  *, idCmdFirst*  *, idCmdLast*  *, uFlags* __ )
Adds options to a context menu

#### Parameters


  -  *hmenu* :[PyHANDLE](#pyhandle)

    Handle to menu to which items should be added

  -  *indexMenu* : int

    Zero-based index at which to add first item

  -  *idCmdFirst* : int

    Minimum menu item Id

  -  *idCmdLast* : int

    Max menu item Id

  -  *uFlags* : int

    Combination of shellcon.CMF_* flags, can be 0