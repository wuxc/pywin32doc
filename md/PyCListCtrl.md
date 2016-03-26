# PyCListCtrl

## PyCListCtrl Object

A class which encapsulates an MFC CListCtrl object.  Derived from a[PyCWnd](#pycwnd)object.

#### Methods


  - [Arrange](PyCListCtrl.md#pyclistctrlarrange)

    Aligns items on a grid.&nbsp;

  - [CreateWindow](PyCListCtrl.md#pyclistctrlcreatewindow)

    Creates the actual window for the object.&nbsp;

  - [DeleteAllItems](PyCListCtrl.md#pyclistctrldeleteallitems)

    Deletes all items from the list.&nbsp;

  - [DeleteItem](PyCListCtrl.md#pyclistctrldeleteitem)

    Deletes the specified item.&nbsp;

  - [GetTextColor](PyCListCtrl.md#pyclistctrlgettextcolor)

    Retrieves the text color of a list view control.&nbsp;

  - [SetTextColor](PyCListCtrl.md#pyclistctrlsettextcolor)

    Sets the text color of a list view control.&nbsp;

  - [GetBkColor](PyCListCtrl.md#pyclistctrlgetbkcolor)

    Retrieves the background color of the control.&nbsp;

  - [SetBkColor](PyCListCtrl.md#pyclistctrlsetbkcolor)

    Sets the background color of the control.&nbsp;

  - [GetItem](PyCListCtrl.md#pyclistctrlgetitem)

    Retrieves the details of an items attributes.&nbsp;

  - [GetItemCount](PyCListCtrl.md#pyclistctrlgetitemcount)

    Retrieves the number of items in a list view control.&nbsp;

  - [GetItemRect](PyCListCtrl.md#pyclistctrlgetitemrect)

    Retrieves the bounding rectangle of a list view item.&nbsp;

  - [GetEditControl](PyCListCtrl.md#pyclistctrlgeteditcontrol)

    Retrieves the handle of the edit control used to edit the specified list view item.&nbsp;

  - [EditLabel](PyCListCtrl.md#pyclistctrleditlabel)

    Edits a specified list view item in-place.&nbsp;

  - [EnsureVisible](PyCListCtrl.md#pyclistctrlensurevisible)

    Ensures that a list view item is visible in its list view control.&nbsp;

  - [CreateDragImage](PyCListCtrl.md#pyclistctrlcreatedragimage)

    Creates a dragging bitmap for the specified list view item.&nbsp;

  - [GetImageList](PyCListCtrl.md#pyclistctrlgetimagelist)

    Retrieves the current image list.&nbsp;

  - [GetNextItem](PyCListCtrl.md#pyclistctrlgetnextitem)

    Searches for a list view item with specified properties and with specified relationship to a given item.&nbsp;

  - [InsertColumn](PyCListCtrl.md#pyclistctrlinsertcolumn)

    Inserts a column into a list control when in report view.&nbsp;

  - [InsertItem](PyCListCtrl.md#pyclistctrlinsertitem)

    Inserts an item into the list.&nbsp;

  - [SetImageList](PyCListCtrl.md#pyclistctrlsetimagelist)

    Assigns an image list to a list view control.&nbsp;

  - [GetColumn](PyCListCtrl.md#pyclistctrlgetcolumn)

    Retrieves the details of a column in the control.&nbsp;

  - [GetTextBkColor](PyCListCtrl.md#pyclistctrlgettextbkcolor)

    Retrieves the text background color of a list view control.&nbsp;

  - [SetTextBkColor](PyCListCtrl.md#pyclistctrlsettextbkcolor)

    Sets the text background color of a list view control.&nbsp;

  - [GetTopIndex](PyCListCtrl.md#pyclistctrlgettopindex)

    Retrieves the index of the topmost visible item.&nbsp;

  - [GetCountPerPage](PyCListCtrl.md#pyclistctrlgetcountperpage)

    Calculates the number of items that can fit vertically in a list view control.&nbsp;

  - [GetSelectedCount](PyCListCtrl.md#pyclistctrlgetselectedcount)

    Retrieves the number of selected items in the list view control.&nbsp;

  - [SetItem](PyCListCtrl.md#pyclistctrlsetitem)

    Sets some of all of an items attributes.&nbsp;

  - [SetItemState](PyCListCtrl.md#pyclistctrlsetitemstate)

    Changes the state of an item in a list view control.&nbsp;

  - [GetItemState](PyCListCtrl.md#pyclistctrlgetitemstate)

    Retrieves the state of a list view item.&nbsp;

  - [SetItemData](PyCListCtrl.md#pyclistctrlsetitemdata)

    Sets the item's application-specific value.&nbsp;

  - [GetItemData](PyCListCtrl.md#pyclistctrlgetitemdata)

    Retrieves the application-specific value associated with an item.&nbsp;

  - [SetItemCount](PyCListCtrl.md#pyclistctrlsetitemcount)

    Prepares a list view control for adding a large number of items.&nbsp;

  - [GetItemCount](PyCListCtrl.md#pyclistctrlgetitemcount)

    Retrieves the number of items in a list view control.&nbsp;

  - [SetItemText](PyCListCtrl.md#pyclistctrlsetitemtext)

    Changes the text of a list view item or subitem.&nbsp;

  - [GetItemText](PyCListCtrl.md#pyclistctrlgetitemtext)

    Retrieves the text of a list view item or subitem.&nbsp;

  - [RedrawItems](PyCListCtrl.md#pyclistctrlredrawitems)

    Redraws a range of items&nbsp;

  - [Update](PyCListCtrl.md#pyclistctrlupdate)

    Forces the control to repaint a specified item.&nbsp;

  - [SetColumn](PyCListCtrl.md#pyclistctrlsetcolumn)

    Sets the state of a column in a list control when in report view.&nbsp;

  - [DeleteColumn](PyCListCtrl.md#pyclistctrldeletecolumn)

    Deletes the specified column from the list control.&nbsp;

  - [GetColumnWidth](PyCListCtrl.md#pyclistctrlgetcolumnwidth)

    Gets the width of the specified column in the list control.&nbsp;

  - [SetColumnWidth](PyCListCtrl.md#pyclistctrlsetcolumnwidth)

    Sets the width of the specified column in the list control.&nbsp;

  - [GetStringWidth](PyCListCtrl.md#pyclistctrlgetstringwidth)

    Gets the necessary column width to fully display this text in a column.&nbsp;

  - [HitTest](PyCListCtrl.md#pyclistctrlhittest)

    Determines which list view item, if any, is at a specified position.&nbsp;

  - [GetItemPosition](PyCListCtrl.md#pyclistctrlgetitemposition)

    Determines the position of the specified item.&nbsp;

## [PyCListCtrl](#pyclistctrl).Arrange

 __Arrange( *code* __ )
Aligns items on a grid.

#### Parameters


  -  *code* : int

    Specifies the alignment style for the items

## [PyCListCtrl](#pyclistctrl).CreateDragImage

[PyCImageList](#pycimagelist),(x,y) = __CreateDragImage( *item* __ )
Creates a dragging bitmap for the specified list view item.

#### Parameters


  -  *item* : int

    The index of the item to edit.

## [PyCListCtrl](#pyclistctrl).CreateWindow

 __CreateWindow( *style*  *, rect*  *,[PyCWnd](#pycwnd)*  *, id* __ )
Creates the actual window for the object.

#### Parameters


  -  *style* : int

    The window style

  -  *rect* : int, int, int, int

    The default rectangle

  -  *[PyCWnd](#pycwnd)* : parent

    The parent window

  -  *id* : int

    The control ID

#### MFC References


  - CListCtrl::Create

## [PyCListCtrl](#pyclistctrl).DeleteAllItems

 __DeleteAllItems(__ )
Deletes all items from the list.

## [PyCListCtrl](#pyclistctrl).DeleteColumn

int = __DeleteColumn( *first* __ )
Deletes the specified column from the list control.

#### Parameters


  -  *first* : int

    Index of the column to be removed.

## [PyCListCtrl](#pyclistctrl).DeleteItem

 __DeleteItem( *item* __ )
Deletes the specified item.

#### Parameters


  -  *item* : int

    The item to delete.

## [PyCListCtrl](#pyclistctrl).EditLabel

[PyCEdit](#pycedit)= __EditLabel( *item* __ )
Edits a specified list view item in-place.

#### Parameters


  -  *item* : int

    The index of item to edit.

## [PyCListCtrl](#pyclistctrl).EnsureVisible

int = __EnsureVisible( *item*  *, bPartialOK* __ )
Ensures that a list view item is visible in its list view control.

#### Parameters


  -  *item* : int

    The index of item to edit.

  -  *bPartialOK* : int

    Specifies whether partial visibility is acceptable.

## [PyCListCtrl](#pyclistctrl).GetBkColor

int = __GetBkColor(__ )
Retrieves the background color of the control.

## [PyCListCtrl](#pyclistctrl).GetColumn

[LV_COLUMN](LV.md#lvcolumn)= __GetColumn( *column* __ )
Retrieves the details of a column in the control.

#### Parameters


  -  *column* : int

    The index of the column whose attributes are to be retrieved.

## [PyCListCtrl](#pyclistctrl).GetColumnWidth

int = __GetColumnWidth( *first* __ )
Gets the width of the specified column in the list control.

#### Parameters


  -  *first* : int

    Index of the column whose width is to be retrieved.

## [PyCListCtrl](#pyclistctrl).GetCountPerPage

int = __GetCountPerPage(__ )
Calculates the number of items that can fit vertically in a list view control.

## [PyCListCtrl](#pyclistctrl).GetEditControl

[PyCEdit](#pycedit)= __GetEditControl(__ )
Retrieves the handle of the edit control used to edit the specified list view item.

## [PyCListCtrl](#pyclistctrl).GetImageList

[PyCImageList](#pycimagelist)= __GetImageList( *nImageList* __ )
Retrieves the current image list.

#### Parameters


  -  *nImageList* : int

    Value specifying which image list to retrieve. It can be one of:
-&#09commctrl.LVSIL_NORMAL   Image list with large icons.
-&#09commctrl.LVSIL_SMALL   Image list with small icons.
-&#09commctrl.LVSIL_STATE   Image list with state images.

## [PyCListCtrl](#pyclistctrl).GetItem

[LV_ITEM](LV.md#lvitem)= __GetItem( *item*  *, sub* __ )
Retrieves the details of an items attributes.

#### Parameters


  -  *item* : int

    The index of the item whose attributes are to be retrieved.

  -  *sub* : int

    Specifies the subitem whose text is to be retrieved.

## [PyCListCtrl](#pyclistctrl).GetItemCount

int = __GetItemCount(__ )
Retrieves the number of items in a list view control.

## [PyCListCtrl](#pyclistctrl).GetItemData

object = __GetItemData( *item* __ )
Retrieves the application-specific value associated with an item.

#### Parameters


  -  *item* : int

    The index of the item whose data is to be retrieved.

## [PyCListCtrl](#pyclistctrl).GetItemPosition

(int, int) = __GetItemPosition( *item* __ )
Determines the position of the specified item.

#### Parameters


  -  *item* : int

    The item to determine the position for.

## [PyCListCtrl](#pyclistctrl).GetItemRect

(int, int, int, int) = __GetItemRect( *item*  *, bTextOnly* __ )
Retrieves the bounding rectangle of a list view item.

#### Parameters


  -  *item* : int

    Index of the item whose Data is to be set.

  -  *bTextOnly* : int

    f this parameter is nonzero, the bounding rectangle includes only the text of the item. Otherwise it includes the entire line that the item occupies in the list view control.

## [PyCListCtrl](#pyclistctrl).GetItemState

int = __GetItemState( *item*  *, mask* __ )
Retrieves the state of a list view item.

#### Parameters


  -  *item* : int

    The index of the item whose position is to be retrieved.

  -  *mask* : int

    Mask specifying which of the item's state flags to return.

## [PyCListCtrl](#pyclistctrl).GetItemText

int = __GetItemText( *item*  *, sub* __ )
Retrieves the text of a list view item or subitem.

#### Parameters


  -  *item* : int

    The index of the item whose text is to be retrieved.

  -  *sub* : int

    Specifies the subitem whose text is to be retrieved.

## [PyCListCtrl](#pyclistctrl).GetNextItem

int = __GetNextItem( *item*  *, flags* __ )
Searches for a list view item with specified properties and with specified relationship to a given item.

#### Parameters


  -  *item* : int

    Index of the item to begin the searching with, or -1 to find the first item that matches the specified flags. The specified item itself is excluded from the search.

  -  *flags* : int

    Geometric relation of the requested item to the specified item, 

and the state of the requested item. The geometric relation can be one of these values:
LVNI_ABOVE
LVNI_ALL
LVNI_BELOW
LVNI_TOLEFT
LVNI_TORIGHT
The state can be zero, or it can be one or more of these values:
LVNI_DROPHILITED
LVNI_FOCUSED
LVNI_HIDDEN
LVNI_MARKED
LVNI_SELECTED
If an item does not have all of the specified state flags set, the search continues with the next item.

#### Return Value
Returns an integer index, or raises a win32ui.error exception if not item can be found.

## [PyCListCtrl](#pyclistctrl).GetSelectedCount

int = __GetSelectedCount(__ )
Retrieves the number of selected items in the list view control.

## [PyCListCtrl](#pyclistctrl).GetStringWidth

int = __GetStringWidth( *first* __ )
Gets the necessary column width to fully display this text in a column.

#### Parameters


  -  *first* : int

    String that contains the text whose width is to be determined.

#### Comments
Doesn't take the size of an included Image in account, only the size of the text is determined.

## [PyCListCtrl](#pyclistctrl).GetTextBkColor

int = __GetTextBkColor(__ )
Retrieves the text background color of a list view control.

## [PyCListCtrl](#pyclistctrl).GetTextColor

int = __GetTextColor(__ )
Retrieves the text color of a list view control.

## [PyCListCtrl](#pyclistctrl).GetTopIndex

int = __GetTopIndex(__ )
Retrieves the index of the topmost visible item.

## [PyCListCtrl](#pyclistctrl).HitTest

(int, int, int) = __HitTest( *x,y* __ )
Determines which list view item, if any, is at a specified position.

#### Parameters


  -  *x,y* : point

    The point to test.

#### Return Value
The result is a tuple of (flags, item, subItem). 

flags may be a combination of the following values:


## [PyCListCtrl](#pyclistctrl).InsertColumn

int = __InsertColumn( *colNo*  *, item* __ )
Inserts a column into a list control when in report view.

#### Parameters


  -  *colNo* : int

    The new column number

  -  *item* :[LV_COLUMN](LV.md#lvcolumn)

    A tuple describing the new column.

## [PyCListCtrl](#pyclistctrl).InsertItem

int = __InsertItem( *item* __ )
Inserts an item into the list.

#### Parameters


  -  *item* :[LV_ITEM](LV.md#lvitem)

    A tuple describing the new item.

#### Alternative Parameters


  -  *item* 

    The index of the item.

  -  *text* 

    The text of the item.

  -  *image* 

    The index of the image to use.

#### Alternative Parameters


  -  *item* 

    The index of the item.

  -  *text* 

    The text of the item.

## [PyCListCtrl](#pyclistctrl).RedrawItems

int = __RedrawItems( *first*  *, first* __ )
Forces a listview to repaint a range of items.

#### Parameters


  -  *first* : int

    Index of the first item to be repainted.

  -  *first* : int

    Index of the last item to be repainted.

#### Comments
The specified items are not actually repainted until the list view window receives a WM_PAINT message. 

To repaint immediately, call the Windows UpdateWindow function after using this function.

## [PyCListCtrl](#pyclistctrl).SetBkColor

 __SetBkColor( *color* __ )
Sets the background color of the control.

#### Parameters


  -  *color* : int

    The new background color.

## [PyCListCtrl](#pyclistctrl).SetColumn

int = __SetColumn( *colNo*  *, item* __ )
Changes column state in a list control when in report view.

#### Parameters


  -  *colNo* : int

    The to be modified column number

  -  *item* :[LV_COLUMN](LV.md#lvcolumn)

    A tuple describing the modified column.

## [PyCListCtrl](#pyclistctrl).SetColumnWidth

int = __SetColumnWidth( *first*  *, first* __ )
Sets the width of the specified column in the list control.

#### Parameters


  -  *first* : int

    Index of the column to be changed.

  -  *first* : int

    New width of the column.

## [PyCListCtrl](#pyclistctrl).SetImageList

int = __SetImageList( *imageList*  *, imageType* __ )
Assigns an image list to a list view control.

#### Parameters


  -  *imageList* :[PyCImageList](#pycimagelist)

    The Image List to use.

  -  *imageType* : int

    Type of image list. It can be one of (COMMCTRL.) LVSIL_NORMAL, LVSIL_SMALL or LVSIL_STATE

## [PyCListCtrl](#pyclistctrl).SetItem

int = __SetItem( *item* __ )
Sets some of all of an items attributes.

#### Parameters


  -  *item* :[LV_ITEM](LV.md#lvitem)

    A tuple describing the new item.

## [PyCListCtrl](#pyclistctrl).SetItemCount

 __SetItemCount( *count* __ )
Prepares a list view control for adding a large number of items.

#### Parameters


  -  *count* : int

    Number of items that the control will ultimately contain.

#### Comments
By calling this function before adding a large number of items, 

you enable a list view control to reallocate its internal data structures 

only once rather than every time you add an item.

## [PyCListCtrl](#pyclistctrl).SetItemData

int = __SetItemData( *item*  *, Data* __ )
Sets the item's application-specific value.

#### Parameters


  -  *item* : int

    Index of the item whose Data is to be set.

  -  *Data* : object

    New value for the data.

#### Comments
Note that a reference count is not added to the object.  This it is your 

responsibility to make sure the object remains alive while in the list.

## [PyCListCtrl](#pyclistctrl).SetItemState

int = __SetItemState( *item*  *, state*  *, mask* __ )
Changes the state of an item in a list view control.

#### Parameters


  -  *item* : int

    Index of the item whose state is to be set.

  -  *state* : int

    New values for the state bits.

  -  *mask* : int

    Mask specifying which state bits to change.

## [PyCListCtrl](#pyclistctrl).SetItemText

int = __SetItemText( *item*  *, sub*  *, text* __ )
Changes the text of a list view item or subitem.

#### Parameters


  -  *item* : int

    Index of the item whose text is to be set.

  -  *sub* : int

    Index of the subitem, or zero to set the item label.

  -  *text* : string

    String that contains the new item text.

## [PyCListCtrl](#pyclistctrl).SetTextBkColor

 __SetTextBkColor( *color* __ )
Sets the text background color of a list view control.

#### Parameters


  -  *color* : int

    The new background color.

## [PyCListCtrl](#pyclistctrl).SetTextColor

 __SetTextColor( *color* __ )
Sets the text color of a list view control.

#### Parameters


  -  *color* : int

    The new color.

## [PyCListCtrl](#pyclistctrl).Update

 __Update( *item* __ )
Forces the control to repaint a specified item.

#### Parameters


  -  *item* : int

    The new color.