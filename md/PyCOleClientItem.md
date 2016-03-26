# PyCOleClientItem

## PyCOleClientItem Object

An OLE client item class.  Encapsulates an MFC __COleClientItem__ class

#### Methods


  - [CreateNewItem](PyCOleClientItem.md#pycoleclientitemcreatenewitem)

    Creates an embedded item.&nbsp;

  - [Close](PyCOleClientItem.md#pycoleclientitemclose)

    Closes the item.&nbsp;

  - [DoVerb](PyCOleClientItem.md#pycoleclientitemdoverb)

    Executes the specified verb.&nbsp;

  - [Draw](PyCOleClientItem.md#pycoleclientitemdraw)

    Draws the OLE item into the specified bounding rectangle using the specified device context.&nbsp;

  - [GetActiveView](PyCOleClientItem.md#pycoleclientitemgetactiveview)

    Obtains the active view for the item&nbsp;

  - [GetDocument](PyCOleClientItem.md#pycoleclientitemgetdocument)

    Obtains the current document for the item&nbsp;

  - [GetInPlaceWindow](PyCOleClientItem.md#pycoleclientitemgetinplacewindow)

    Obtains the window in which the item has been opened for in-place editing.&nbsp;

  - [GetItemState](PyCOleClientItem.md#pycoleclientitemgetitemstate)

    Obtains the OLE item's current state&nbsp;

  - [GetObject](PyCOleClientItem.md#pycoleclientitemgetobject)

    Returns the COM object to the item.  This is the m_lpObject variable in MFC.&nbsp;

  - [GetStorage](PyCOleClientItem.md#pycoleclientitemgetstorage)

    Returns the COM object used for storage&nbsp;

  - [OnActivate](PyCOleClientItem.md#pycoleclientitemonactivate)

    Calls the underlying MFC handler.&nbsp;

  - [OnChange](PyCOleClientItem.md#pycoleclientitemonchange)

    Calls the underlying MFC handler.&nbsp;

  - [OnChangeItemPosition](PyCOleClientItem.md#pycoleclientitemonchangeitemposition)

    Calls the underlying MFC method.&nbsp;

  - [OnDeactivateUI](PyCOleClientItem.md#pycoleclientitemondeactivateui)

    Calls the underlying MFC method.&nbsp;

  - [Run](PyCOleClientItem.md#pycoleclientitemrun)

    Runs the application associated with this item.&nbsp;

  - [SetItemRects](PyCOleClientItem.md#pycoleclientitemsetitemrects)

    Sets the bounding rectangle or the visible rectangle of the OLE item.&nbsp;

## [PyCOleClientItem](#pycoleclientitem).Close

 __Close(__ )
Closes the item

## [PyCOleClientItem](#pycoleclientitem).CreateNewItem

 __CreateNewItem(__ )
Creates an embedded item.

## [PyCOleClientItem](#pycoleclientitem).DoVerb

 __DoVerb(__ )
Executes the specified verb.

## [PyCOleClientItem](#pycoleclientitem).Draw

 __Draw(__ )
Draws the OLE item into the specified bounding rectangle using the specified device context.

## [PyCOleClientItem](#pycoleclientitem).GetActiveView

[PyCView](#pycview)= __GetActiveView(__ )
Obtains the active view for the item

## [PyCOleClientItem](#pycoleclientitem).GetDocument

[PyCDocument](#pycdocument)= __GetDocument(__ )
Obtains the current document for the item

## [PyCOleClientItem](#pycoleclientitem).GetInPlaceWindow

[PyCWnd](#pycwnd)= __GetInPlaceWindow(__ )
Obtains the window in which the item has been opened for in-place editing.

## [PyCOleClientItem](#pycoleclientitem).GetItemState

 __GetItemState(__ )
Obtains the OLE item's current state

## [PyCOleClientItem](#pycoleclientitem).GetObject

[PyIUnknown](#pyiunknown)= __GetObject(__ )
Returns the COM object to the item.  This is the m_lpObject variable in MFC.

## [PyCOleClientItem](#pycoleclientitem).GetStorage

 __GetStorage(__ )
Returns the COM object used for storage

## [PyCOleClientItem](#pycoleclientitem).OnActivate

 __OnActivate(__ )
Calls the underlying MFC method.

## [PyCOleClientItem.OnActivate](#pycoleclientitem)Virtual

 __OnActivate(__ )


## [PyCOleClientItem](#pycoleclientitem).OnChange

 __OnChange(__ )
Calls the underlying MFC method.

## [PyCOleClientItem](#pycoleclientitem).OnChangeItemPosition

int = __OnChangeItemPosition(__ )
Calls the underlying MFC method.

#### Return Value
The result is a BOOL indicating if the function succeeded.  No exception is thrown.

## [PyCOleClientItem.OnChangeItemPosition](#pycoleclientitem)Virtual

 __OnChangeItemPosition( *(left, top, right, bottom)* __ )


#### Parameters


  -  *(left, top, right, bottom)* : (int, int, int, int)

    The new position

## [PyCOleClientItem.OnChange](#pycoleclientitem)Virtual

 __OnChange( *wNotification*  *, dwParam* __ )


#### Parameters


  -  *wNotification* : int

    

  -  *dwParam* : int

    

## [PyCOleClientItem](#pycoleclientitem).OnDeactivateUI

int = __OnDeactivateUI(__ )
Calls the underlying MFC method.

## [PyCOleClientItem.OnDeactivateUI](#pycoleclientitem)Virtual

 __OnDeactivateUI( *bUndoable* __ )


#### Parameters


  -  *bUndoable* : int

    

## [PyCOleClientItem.OnGetItemPosition](#pycoleclientitem)Virtual

 __OnGetItemPosition(__ )


## [PyCOleClientItem](#pycoleclientitem).Run

 __Run(__ )
Runs the application associated with this item.

## [PyCOleClientItem](#pycoleclientitem).SetItemRects

 __SetItemRects(__ )
Sets the bounding rectangle or the visible rectangle of the OLE item.