
## [win32uiole](#README.md#win32uiole).AfxOleInit

 **AfxOleInit( *enabled* ** )


#### Parameters


     *enabled* : bool

    

## COleClientItem_activeState
 **const win32uiole.COleClientItem_activeState;** 


## COleClientItem_activeUIState
 **const win32uiole.COleClientItem_activeUIState;** 


## COleClientItem_emptyState
 **const win32uiole.COleClientItem_emptyState;** 


## COleClientItem_loadedState
 **const win32uiole.COleClientItem_loadedState;** 


## COleClientItem_openState
 **const win32uiole.COleClientItem_openState;** 


## [win32uiole](#README.md#win32uiole).CreateInsertDialog

[PyCOleInsertDialog](#README.md#PyCOleInsertDialog)= **CreateInsertDialog(** )
Creates a InsertObject dialog. 

self*/, PyObject *args )

## [win32uiole](#README.md#win32uiole).CreateOleClientItem

[PyCOleClientItem](#README.md#PyCOleClientItem)= **CreateOleClientItem(** )
Creates a[PyCOleClientItem](#README.md#PyCOleClientItem)object.

## [win32uiole](#README.md#win32uiole).CreateOleDocument

[PyCOleDocument](#README.md#PyCOleDocument)= **CreateOleDocument( *template*  *, fileName* ** )
Creates an OLE document.

#### Parameters


     *template* :[PyCDocTemplate](#README.md#PyCDocTemplate)

    The template to be attached to this document.

     *fileName=None* : string

    The filename for the document.

## [win32uiole](#README.md#win32uiole).DaoGetEngine

[PyIDispatch](#README.md#PyIDispatch)= **DaoGetEngine(** )


## [win32uiole](#README.md#win32uiole).EnableBusyDialog

 **EnableBusyDialog( *enabled* ** )


#### Parameters


     *enabled* : bool

    

## [win32uiole](#README.md#win32uiole).EnableNotRespondingDialog

 **EnableNotRespondingDialog( *enabled* ** )


#### Parameters


     *enabled* : bool

    

## [win32uiole](#README.md#win32uiole).GetIDispatchForWindow

[PyIDispatch](#README.md#PyIDispatch)= **GetIDispatchForWindow(** )
Gets an OCX IDispatch pointer, if the window has one!

## OLE_CHANGED
 **const win32uiole.OLE_CHANGED;** 
representation of a draw aspect has changed

## OLE_CHANGED_ASPECT
 **const win32uiole.OLE_CHANGED_ASPECT;** 
the item draw aspect has changed

## OLE_CHANGED_STATE
 **const win32uiole.OLE_CHANGED_STATE;** 
the item state (open, active, etc.) has changed

## OLE_CLOSED
 **const win32uiole.OLE_CLOSED;** 
the item has closed

## OLE_RENAMED
 **const win32uiole.OLE_RENAMED;** 
the item has changed its moniker

## OLE_SAVED
 **const win32uiole.OLE_SAVED;** 
the item has committed its storage

## [win32uiole](#README.md#win32uiole).OleGetUserCtrl

int = **OleGetUserCtrl(** )
Returns the application name.

## [win32uiole](#README.md#win32uiole).OleSetUserCtrl

int = **OleSetUserCtrl( *bUserCtrl* ** )
Sets or clears the user control flag.

#### Parameters


     *bUserCtrl* : int

    Specifies whether the user-control flag is to be set or cleared.

## [win32uiole](#README.md#win32uiole).SetMessagePendingDelay

 **SetMessagePendingDelay( *delay* ** )


#### Parameters


     *delay* : int

    