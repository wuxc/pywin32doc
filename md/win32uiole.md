# win32uiole

## Module win32uiole

A module, encapsulating the Microsoft Foundation Classes OLE functionality.

#### Methods


  - [AfxOleInit](win32uiole.md#win32uioleafxoleinit)

    &nbsp;

  - [CreateInsertDialog](win32uiole.md#win32uiolecreateinsertdialog)

    Creates a InsertObject dialog.&nbsp;

  - [CreateOleClientItem](win32uiole.md#win32uiolecreateoleclientitem)

    Creates a[PyCOleClientItem](#pycoleclientitem)object.&nbsp;

  - [CreateOleDocument](win32uiole.md#win32uiolecreateoledocument)

    Creates a[PyCOleDocument](#pycoledocument)object.&nbsp;

  - [DaoGetEngine](win32uiole.md#win32uioledaogetengine)

    &nbsp;

  - [GetIDispatchForWindow](win32uiole.md#win32uiolegetidispatchforwindow)

    Gets an OCX IDispatch pointer, if the window has one!&nbsp;

  - [OleGetUserCtrl](win32uiole.md#win32uioleolegetuserctrl)

    Retrieves the current user-control flag.&nbsp;

  - [OleSetUserCtrl](win32uiole.md#win32uioleolesetuserctrl)

    Sets the current user-control flag.&nbsp;

  - [SetMessagePendingDelay](win32uiole.md#win32uiolesetmessagependingdelay)

    &nbsp;

  - [EnableNotRespondingDialog](win32uiole.md#win32uioleenablenotrespondingdialog)

    &nbsp;

  - [EnableNotRespondingDialog](win32uiole.md#win32uioleenablenotrespondingdialog)

    &nbsp;

## [win32uiole](#win32uiole).AfxOleInit

 __AfxOleInit( *enabled* __ )


#### Parameters


  -  *enabled* : bool

    

## COleClientItem_activeState
 __const win32uiole.COleClientItem_activeState;__ 


## COleClientItem_activeUIState
 __const win32uiole.COleClientItem_activeUIState;__ 


## COleClientItem_emptyState
 __const win32uiole.COleClientItem_emptyState;__ 


## COleClientItem_loadedState
 __const win32uiole.COleClientItem_loadedState;__ 


## COleClientItem_openState
 __const win32uiole.COleClientItem_openState;__ 


## [win32uiole](#win32uiole).CreateInsertDialog

[PyCOleInsertDialog](#pycoleinsertdialog)= __CreateInsertDialog(__ )
Creates a InsertObject dialog. 

self*/, PyObject *args )

## [win32uiole](#win32uiole).CreateOleClientItem

[PyCOleClientItem](#pycoleclientitem)= __CreateOleClientItem(__ )
Creates a[PyCOleClientItem](#pycoleclientitem)object.

## [win32uiole](#win32uiole).CreateOleDocument

[PyCOleDocument](#pycoledocument)= __CreateOleDocument( *template*  *, fileName* __ )
Creates an OLE document.

#### Parameters


  -  *template* :[PyCDocTemplate](#pycdoctemplate)

    The template to be attached to this document.

  -  *fileName=None* : string

    The filename for the document.

## [win32uiole](#win32uiole).DaoGetEngine

[PyIDispatch](#pyidispatch)= __DaoGetEngine(__ )


## [win32uiole](#win32uiole).EnableBusyDialog

 __EnableBusyDialog( *enabled* __ )


#### Parameters


  -  *enabled* : bool

    

## [win32uiole](#win32uiole).EnableNotRespondingDialog

 __EnableNotRespondingDialog( *enabled* __ )


#### Parameters


  -  *enabled* : bool

    

## [win32uiole](#win32uiole).GetIDispatchForWindow

[PyIDispatch](#pyidispatch)= __GetIDispatchForWindow(__ )
Gets an OCX IDispatch pointer, if the window has one!

## OLE_CHANGED
 __const win32uiole.OLE_CHANGED;__ 
representation of a draw aspect has changed

## OLE_CHANGED_ASPECT
 __const win32uiole.OLE_CHANGED_ASPECT;__ 
the item draw aspect has changed

## OLE_CHANGED_STATE
 __const win32uiole.OLE_CHANGED_STATE;__ 
the item state (open, active, etc.) has changed

## OLE_CLOSED
 __const win32uiole.OLE_CLOSED;__ 
the item has closed

## OLE_RENAMED
 __const win32uiole.OLE_RENAMED;__ 
the item has changed its moniker

## OLE_SAVED
 __const win32uiole.OLE_SAVED;__ 
the item has committed its storage

## [win32uiole](#win32uiole).OleGetUserCtrl

int = __OleGetUserCtrl(__ )
Returns the application name.

## [win32uiole](#win32uiole).OleSetUserCtrl

int = __OleSetUserCtrl( *bUserCtrl* __ )
Sets or clears the user control flag.

#### Parameters


  -  *bUserCtrl* : int

    Specifies whether the user-control flag is to be set or cleared.

## [win32uiole](#win32uiole).SetMessagePendingDelay

 __SetMessagePendingDelay( *delay* __ )


#### Parameters


  -  *delay* : int

    