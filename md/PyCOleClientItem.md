# PyCOleClientItem


## PyCOleClientItem Object

An OLE client item class\.  Encapsulates an MFC COleClientItem

 class

#### Methods

  - [CreateNewItem](PyCOleClientItem.md#pycoleclientitemcreatenewitem)

    Creates an embedded item\.&nbsp;

  - [Close](PyCOleClientItem.md#pycoleclientitemclose)

    Closes the item\.&nbsp;

  - [DoVerb](PyCOleClientItem.md#pycoleclientitemdoverb)

    Executes the specified verb\.&nbsp;

  - [Draw](PyCOleClientItem.md#pycoleclientitemdraw)

    Draws the OLE item into the specified bounding rectangle using the specified device context\.&nbsp;

  - [GetActiveView](PyCOleClientItem.md#pycoleclientitemgetactiveview)

    Obtains the active view for the item&nbsp;

  - [GetDocument](PyCOleClientItem.md#pycoleclientitemgetdocument)

    Obtains the current document for the item&nbsp;

  - [GetInPlaceWindow](PyCOleClientItem.md#pycoleclientitemgetinplacewindow)

    Obtains the window in which the item has been opened for in-place editing\.&nbsp;

  - [GetItemState](PyCOleClientItem.md#pycoleclientitemgetitemstate)

    Obtains the OLE item's current state&nbsp;

  - [GetObject](PyCOleClientItem.md#pycoleclientitemgetobject)

    Returns the COM object to the item\.  This is the m\_lpObject variable in MFC\.&nbsp;

  - [GetStorage](PyCOleClientItem.md#pycoleclientitemgetstorage)

    Returns the COM object used for storage&nbsp;

  - [OnActivate](PyCOleClientItem.md#pycoleclientitemonactivate)

    Calls the underlying MFC handler\.&nbsp;

  - [OnChange](PyCOleClientItem.md#pycoleclientitemonchange)

    Calls the underlying MFC handler\.&nbsp;

  - [OnChangeItemPosition](PyCOleClientItem.md#pycoleclientitemonchangeitemposition)

    Calls the underlying MFC method\.&nbsp;

  - [OnDeactivateUI](PyCOleClientItem.md#pycoleclientitemondeactivateui)

    Calls the underlying MFC method\.&nbsp;

  - [Run](PyCOleClientItem.md#pycoleclientitemrun)

    Runs the application associated with this item\.&nbsp;

  - [SetItemRects](PyCOleClientItem.md#pycoleclientitemsetitemrects)

    Sets the bounding rectangle or the visible rectangle of the OLE item\.&nbsp;


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.Close

Close\(\)
Closes the item


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.CreateNewItem

CreateNewItem\(\)
Creates an embedded item\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.DoVerb

DoVerb\(\)
Executes the specified verb\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.Draw

Draw\(\)
Draws the OLE item into the specified bounding rectangle using the specified device context\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.GetActiveView

[PyCView](PyCView.md) = GetActiveView\(\)
Obtains the active view for the item


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.GetDocument

[PyCDocument](PyCDocument.md) = GetDocument\(\)
Obtains the current document for the item


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.GetInPlaceWindow

[PyCWnd](PyCWnd.md) = GetInPlaceWindow\(\)
Obtains the window in which the item has been opened for in-place editing\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.GetItemState

GetItemState\(\)
Obtains the OLE item's current state


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.GetObject

[PyIUnknown](PyIUnknown.md) = GetObject\(\)
Returns the COM object to the item\.  This is the m\_lpObject variable in MFC\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.GetStorage

GetStorage\(\)
Returns the COM object used for storage


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.OnActivate

OnActivate\(\)
Calls the underlying MFC method\.


## [PyCOleClientItem\.OnActivate](PyCOleClientItem.md#pycoleclientitem) Virtual

OnActivate\(\)



## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.OnChange

OnChange\(\)
Calls the underlying MFC method\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.OnChangeItemPosition

int = OnChangeItemPosition\(\)
Calls the underlying MFC method\.

#### Return Value
The result is a BOOL indicating if the function succeeded\.  No exception is thrown\.


## [PyCOleClientItem\.OnChangeItemPosition](PyCOleClientItem.md#pycoleclientitem) Virtual

OnChangeItemPosition\(\(left, top, right, bottom\)\)

#### Parameters

  - \(left, top, right, bottom\) : \(int, int, int, int\)

    The new position


## [PyCOleClientItem\.OnChange](PyCOleClientItem.md#pycoleclientitem) Virtual

OnChange\(wNotification, dwParam

\)

#### Parameters

  - wNotification : int

    

  - dwParam : int

    


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.OnDeactivateUI

int = OnDeactivateUI\(\)
Calls the underlying MFC method\.


## [PyCOleClientItem\.OnDeactivateUI](PyCOleClientItem.md#pycoleclientitem) Virtual

OnDeactivateUI\(bUndoable\)

#### Parameters

  - bUndoable : int

    


## [PyCOleClientItem\.OnGetItemPosition](PyCOleClientItem.md#pycoleclientitem) Virtual

OnGetItemPosition\(\)



## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.Run

Run\(\)
Runs the application associated with this item\.


## [PyCOleClientItem](PyCOleClientItem.md#pycoleclientitem)\.SetItemRects

SetItemRects\(\)
Sets the bounding rectangle or the visible rectangle of the OLE item\.