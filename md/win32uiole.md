# win32uiole


## Module win32uiole

A module, encapsulating the Microsoft Foundation Classes OLE functionality\.

#### Methods

  - [AfxOleInit](win32uiole.md#win32uioleafxoleinit)

    &nbsp;

  - [CreateInsertDialog](win32uiole.md#win32uiolecreateinsertdialog)

    Creates a InsertObject dialog\.&nbsp;

  - [CreateOleClientItem](win32uiole.md#win32uiolecreateoleclientitem)

    Creates a [PyCOleClientItem](PyCOleClientItem.md) object\.&nbsp;

  - [CreateOleDocument](win32uiole.md#win32uiolecreateoledocument)

    Creates a [PyCOleDocument](PyCOleDocument.md) object\.&nbsp;

  - [DaoGetEngine](win32uiole.md#win32uioledaogetengine)

    &nbsp;

  - [GetIDispatchForWindow](win32uiole.md#win32uiolegetidispatchforwindow)

    Gets an OCX IDispatch pointer, if the window has one\!&nbsp;

  - [OleGetUserCtrl](win32uiole.md#win32uioleolegetuserctrl)

    Retrieves the current user-control flag\.&nbsp;

  - [OleSetUserCtrl](win32uiole.md#win32uioleolesetuserctrl)

    Sets the current user-control flag\.&nbsp;

  - [SetMessagePendingDelay](win32uiole.md#win32uiolesetmessagependingdelay)

    &nbsp;

  - [EnableNotRespondingDialog](win32uiole.md#win32uioleenablenotrespondingdialog)

    &nbsp;

  - [EnableNotRespondingDialog](win32uiole.md#win32uioleenablenotrespondingdialog)

    &nbsp;


## [win32uiole](win32uiole.md#win32uiole)\.AfxOleInit

AfxOleInit\(enabled\)

#### Parameters

  - enabled : bool

    


## COleClientItem\_activeState

const win32uiole\.COleClientItem\_activeState;




## COleClientItem\_activeUIState

const win32uiole\.COleClientItem\_activeUIState;




## COleClientItem\_emptyState

const win32uiole\.COleClientItem\_emptyState;




## COleClientItem\_loadedState

const win32uiole\.COleClientItem\_loadedState;




## COleClientItem\_openState

const win32uiole\.COleClientItem\_openState;




## [win32uiole](win32uiole.md#win32uiole)\.CreateInsertDialog

[PyCOleInsertDialog](PyCOleInsertDialog.md) = CreateInsertDialog\(\)
Creates a InsertObject dialog\. 

self\*/, PyObject \*args \)


## [win32uiole](win32uiole.md#win32uiole)\.CreateOleClientItem

[PyCOleClientItem](PyCOleClientItem.md) = CreateOleClientItem\(\)
Creates a [PyCOleClientItem](PyCOleClientItem.md) object\.


## [win32uiole](win32uiole.md#win32uiole)\.CreateOleDocument

[PyCOleDocument](PyCOleDocument.md) = CreateOleDocument\(template, fileName

\)
Creates an OLE document\.

#### Parameters

  - template : [PyCDocTemplate](PyCDocTemplate.md)

    The template to be attached to this document\.

  - fileName=None : string

    The filename for the document\.


## [win32uiole](win32uiole.md#win32uiole)\.DaoGetEngine

[PyIDispatch](PyIDispatch.md) = DaoGetEngine\(\)



## [win32uiole](win32uiole.md#win32uiole)\.EnableBusyDialog

EnableBusyDialog\(enabled\)

#### Parameters

  - enabled : bool

    


## [win32uiole](win32uiole.md#win32uiole)\.EnableNotRespondingDialog

EnableNotRespondingDialog\(enabled\)

#### Parameters

  - enabled : bool

    


## [win32uiole](win32uiole.md#win32uiole)\.GetIDispatchForWindow

[PyIDispatch](PyIDispatch.md) = GetIDispatchForWindow\(\)
Gets an OCX IDispatch pointer, if the window has one\!


## OLE\_CHANGED

const win32uiole\.OLE\_CHANGED;

representation of a draw aspect has changed


## OLE\_CHANGED\_ASPECT

const win32uiole\.OLE\_CHANGED\_ASPECT;

the item draw aspect has changed


## OLE\_CHANGED\_STATE

const win32uiole\.OLE\_CHANGED\_STATE;

the item state \(open, active, etc\.\) has changed


## OLE\_CLOSED

const win32uiole\.OLE\_CLOSED;

the item has closed


## OLE\_RENAMED

const win32uiole\.OLE\_RENAMED;

the item has changed its moniker


## OLE\_SAVED

const win32uiole\.OLE\_SAVED;

the item has committed its storage


## [win32uiole](win32uiole.md#win32uiole)\.OleGetUserCtrl

int = OleGetUserCtrl\(\)
Returns the application name\.


## [win32uiole](win32uiole.md#win32uiole)\.OleSetUserCtrl

int = OleSetUserCtrl\(bUserCtrl\)
Sets or clears the user control flag\.

#### Parameters

  - bUserCtrl : int

    Specifies whether the user-control flag is to be set or cleared\.


## [win32uiole](win32uiole.md#win32uiole)\.SetMessagePendingDelay

SetMessagePendingDelay\(delay\)

#### Parameters

  - delay : int

    