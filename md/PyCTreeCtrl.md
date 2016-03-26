# PyCTreeCtrl

## PyCTreeCtrl Object



A class which encapsulates an MFC CTreeCtrl object\.  Derived from a[PyCWnd](#pycwnd) object\.

#### Methods


  - [CreateWindow](PyCTreeCtrl.md#pyctreectrlcreatewindow)

    Creates the actual window for the object\.&nbsp;

  - [GetCount](PyCTreeCtrl.md#pyctreectrlgetcount)

    Retrieves the number of tree items associated with a tree view control\.&nbsp;

  - [GetIndent](PyCTreeCtrl.md#pyctreectrlgetindent)

    Retrieves the offset \(in pixels\) of a tree view item from its parent\.&nbsp;

  - [SetIndent](PyCTreeCtrl.md#pyctreectrlsetindent)

    Sets the offset \(in pixels\) of a tree view item from its parent\.&nbsp;

  - [GetImageList](PyCTreeCtrl.md#pyctreectrlgetimagelist)

    Retrieves the current image list\.&nbsp;

  - [SetImageList](PyCTreeCtrl.md#pyctreectrlsetimagelist)

    Assigns an image list to a list view control\.&nbsp;

  - [GetNextItem](PyCTreeCtrl.md#pyctreectrlgetnextitem)

    Retrieves the next item\.&nbsp;

  - [ItemHasChildren](PyCTreeCtrl.md#pyctreectrlitemhaschildren)

    Returns nonzero if the specified item has child items\.&nbsp;

  - [GetChildItem](PyCTreeCtrl.md#pyctreectrlgetchilditem)

    Retrieves the child item of the specified tree view item\.&nbsp;

  - [GetNextSiblingItem](PyCTreeCtrl.md#pyctreectrlgetnextsiblingitem)

    Retrieves the next sibling of the specified tree view item\.&nbsp;

  - [GetPrevSiblingItem](PyCTreeCtrl.md#pyctreectrlgetprevsiblingitem)

    Retrieves the previous sibling of the specified tree view item\.&nbsp;

  - [GetParentItem](PyCTreeCtrl.md#pyctreectrlgetparentitem)

    Retrieves the parent item of the specified tree view item\.&nbsp;

  - [GetFirstVisibleItem](PyCTreeCtrl.md#pyctreectrlgetfirstvisibleitem)

    Retrieves the first visible item of the specified tree view item\.&nbsp;

  - [GetNextVisibleItem](PyCTreeCtrl.md#pyctreectrlgetnextvisibleitem)

    Retrieves the next visible item of the specified tree view item\.&nbsp;

  - [GetNextVisibleItem](PyCTreeCtrl.md#pyctreectrlgetnextvisibleitem)

    Retrieves the previous visible item of the specified tree view item\.&nbsp;

  - [GetSelectedItem](PyCTreeCtrl.md#pyctreectrlgetselecteditem)

    Retrieves the currently selected tree view item\.&nbsp;

  - [GetDropHilightItem](PyCTreeCtrl.md#pyctreectrlgetdrophilightitem)

    Retrieves the target of a drag-and-drop operation\.&nbsp;

  - [GetRootItem](PyCTreeCtrl.md#pyctreectrlgetrootitem)

    Retrieves the root of the specified tree view item\.&nbsp;

  - [GetToolTips](PyCTreeCtrl.md#pyctreectrlgettooltips)

    Returns the tooltip control&nbsp;

  - [GetItem](PyCTreeCtrl.md#pyctreectrlgetitem)

    Retrieves the details of an items attributes\.&nbsp;

  - [SetItem](PyCTreeCtrl.md#pyctreectrlsetitem)

    Sets some of all of an items attributes\.&nbsp;

  - [GetItemState](PyCTreeCtrl.md#pyctreectrlgetitemstate)

    Retrieves the state of an item\.&nbsp;

  - [SetItemState](PyCTreeCtrl.md#pyctreectrlsetitemstate)

    Sets the state of an item\.&nbsp;

  - [GetItemImage](PyCTreeCtrl.md#pyctreectrlgetitemimage)

    Retrieves the index of an items images\.&nbsp;

  - [SetItemImage](PyCTreeCtrl.md#pyctreectrlsetitemimage)

    Sets the index of an items images\.&nbsp;

  - [SetItemText](PyCTreeCtrl.md#pyctreectrlsetitemtext)

    Changes the text of a list view item or subitem\.&nbsp;

  - [GetItemText](PyCTreeCtrl.md#pyctreectrlgetitemtext)

    Retrieves the text of a list view item or subitem\.&nbsp;

  - [GetItemData](PyCTreeCtrl.md#pyctreectrlgetitemdata)

    Retrieves the application-specific value associated with an item\.&nbsp;

  - [SetItemData](PyCTreeCtrl.md#pyctreectrlsetitemdata)

    Sets the item's application-specific value&nbsp;

  - [GetItemRect](PyCTreeCtrl.md#pyctreectrlgetitemrect)

    Retrieves the bounding rectangle of a tree view item\.&nbsp;

  - [GetEditControl](PyCTreeCtrl.md#pyctreectrlgeteditcontrol)

    Retrieves the handle of the edit control used to edit the specified tree view item\.&nbsp;

  - [GetVisibleCount](PyCTreeCtrl.md#pyctreectrlgetvisiblecount)

    Retrieves the number of visible tree items associated with a tree view control\.&nbsp;

  - [InsertItem](PyCTreeCtrl.md#pyctreectrlinsertitem)

    Inserts an item into the list\.&nbsp;

  - [DeleteItem](PyCTreeCtrl.md#pyctreectrldeleteitem)

    Deletes an item from the list\.&nbsp;

  - [DeleteAllItems](PyCTreeCtrl.md#pyctreectrldeleteallitems)

    Deletes all items from the list\.&nbsp;

  - [Expand](PyCTreeCtrl.md#pyctreectrlexpand)

    Expands, or collapses, the child items of the specified tree view item\.&nbsp;

  - [Select](PyCTreeCtrl.md#pyctreectrlselect)

    Selects, scrolls into view, or redraws a specified tree view item\.&nbsp;

  - [SelectItem](PyCTreeCtrl.md#pyctreectrlselectitem)

    Selects a specified tree view item\.&nbsp;

  - [SelectDropTarget](PyCTreeCtrl.md#pyctreectrlselectdroptarget)

    Redraws the tree item as the target of a drag-and-drop operation\.&nbsp;

  - [SelectSetFirstVisible](PyCTreeCtrl.md#pyctreectrlselectsetfirstvisible)

    Selects a specified tree view item as the first visible item\.&nbsp;

  - [EditLabel](PyCTreeCtrl.md#pyctreectrleditlabel)

    Edits a specified tree view item in-place\.&nbsp;

  - [CreateDragImage](PyCTreeCtrl.md#pyctreectrlcreatedragimage)

    Creates a dragging bitmap for the specified tree view item\.&nbsp;

  - [SortChildren](PyCTreeCtrl.md#pyctreectrlsortchildren)

    Sorts the children of a given parent item\.&nbsp;

  - [EnsureVisible](PyCTreeCtrl.md#pyctreectrlensurevisible)

    Ensures that a tree view item is visible in its tree view control\.&nbsp;

  - [HitTest](PyCTreeCtrl.md#pyctreectrlhittest)

    Determines which tree view item, if any, is at a specified position\.&nbsp;

#### Comments


Sam Rushing has found the following tidbits:
 

You can implement dynamic collapsing and expanding of events for large 

collections yourself - see KB Q130697
 

The MFC docs tell you to use TVE\_COLLAPSERESET in order to 

throw away the child items when collapsing a node\.  They neglect to 

tell you a very important tidbit: that you need to combine the flag 

with TVE\_COLLAPSE\.  This is pointed out in the docs for 

TreeView\_Expand\(\), but not in those for CTreeCtrl::Expand\.

## [PyCTreeCtrl](#pyctreectrl)\.CreateDragImage

[PyCImageList](#pycimagelist) =CreateDragImage\(item\)
Creates a dragging bitmap for the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The item to edit\.

## [PyCTreeCtrl](#pyctreectrl)\.CreateWindow

CreateWindow\(style, rect,[PyCWnd](#pycwnd), id\)
Creates the actual window for the object\.

#### Parameters


  - style : int

    The window style

  - rect : int, int, int, int

    The default rectangle

  - [PyCWnd](#pycwnd) : parent

    The parent window

  - id : int

    The control ID

#### MFC References


  - CTreeCtrl::Create

## [PyCTreeCtrl](#pyctreectrl)\.DeleteAllItems



object =DeleteAllItems\(\)
Deletes all items in the control

## [PyCTreeCtrl](#pyctreectrl)\.DeleteItem

DeleteItem\(item\)
Deletes the specified item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.EditLabel

[PyCEdit](#pycedit) =EditLabel\(item\)
Edits a specified tree view item in-place\.

#### Parameters


  - item : HTREEITEM

    The item to edit\.

## [PyCTreeCtrl](#pyctreectrl)\.EnsureVisible



int =EnsureVisible\(item\)
Ensures that a tree view item is visible in its tree view control\.

#### Parameters


  - item : HTREEITEM

    The item to edit\.

## [PyCTreeCtrl](#pyctreectrl)\.Expand

Expand\(item, code\)
Expands, or collapses, the child items of the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

  - code : int

    The action to take

## [PyCTreeCtrl](#pyctreectrl)\.GetChildItem



HTREEITEM =GetChildItem\(item\)
Retrieves the first child item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetCount



int =GetCount\(\)
Retrieves the number of tree items associated with a tree view control\.

## [PyCTreeCtrl](#pyctreectrl)\.GetDropHilightItem



HTREEITEM =GetDropHilightItem\(\)
Retrieves the target of a drag-and-drop operation\.

## [PyCTreeCtrl](#pyctreectrl)\.GetEditControl

[PyCEdit](#pycedit) =GetEditControl\(\)
Retrieves the handle of the edit control used to edit the specified tree view item\.

## [PyCTreeCtrl](#pyctreectrl)\.GetFirstVisibleItem



HTREEITEM =GetFirstVisibleItem\(\)
Retrieves the first visible item of the tree view control\.

## [PyCTreeCtrl](#pyctreectrl)\.GetImageList

[PyCImageList](#pycimagelist) =GetImageList\(nImageList\)
Retrieves the current image list\.

#### Parameters


  - nImageList : int

    Value specifying which image list to retrieve\. It can be one of:
-&\#09commctrl\.LVSIL\_NORMAL   Image list with large icons\.
-&\#09commctrl\.LVSIL\_SMALL   Image list with small icons\.
-&\#09commctrl\.LVSIL\_STATE   Image list with state images\.

## [PyCTreeCtrl](#pyctreectrl)\.GetIndent



int =GetIndent\(\)
Retrieves the offset \(in pixels\) of a tree view item from its parent\.

## [PyCTreeCtrl](#pyctreectrl)\.GetItem

[TV\_ITEM](TV.md#tvitem) =GetItem\(item, mask\)
Retrieves the details of an items attributes\.

#### Parameters


  - item : HTREEITEM

    The item whose attributes are to be retrieved\.

  - mask=\(all flags set\) : int

    The requested attributes\.

## [PyCTreeCtrl](#pyctreectrl)\.GetItemData



object =GetItemData\(item\)
Retrieves the application-specific value associated with an item\.

#### Parameters


  - item : HTREEITEM

    The index of the item whose data is to be retrieved\.

## [PyCTreeCtrl](#pyctreectrl)\.GetItemImage



\(int,int\) =GetItemImage\(item\)
Retrieves the index of an items images\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetItemRect



\(int, int, int, int\) =GetItemRect\(item, bTextOnly\)
Retrieves the bounding rectangle of a tree view item\.

#### Parameters


  - item : HTREEITEM

    The item whose Data is to be set\.

  - bTextOnly : int

    f this parameter is nonzero, the bounding rectangle includes only the text of the item\. Otherwise it includes the entire line that the item occupies in the tree view control\.

## [PyCTreeCtrl](#pyctreectrl)\.GetItemState



\(int,int\) =GetItemState\(item, stateMask\)
Retrieves the state and mask of an item\.

#### Parameters


  - item : HTREEITEM

    The specified item

  - stateMask : int

    The mask for the result\.

## [PyCTreeCtrl](#pyctreectrl)\.GetItemText



int =GetItemText\(item\)
Retrieves the text of a list view item or subitem\.

#### Parameters


  - item : HTREEITEM

    The item whose text is to be retrieved\.

## [PyCTreeCtrl](#pyctreectrl)\.GetNextItem



HTREEITEM =GetNextItem\(item, code\)
Retrieves the next item\.

#### Parameters


  - item : HTREEITEM

    The specified item

  - code : int

    Specifies the relationship of the item to fetch\.

## [PyCTreeCtrl](#pyctreectrl)\.GetNextSiblingItem



HTREEITEM =GetNextSiblingItem\(item\)
Retrieves the next sibling of the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetNextVisibleItem



HTREEITEM =GetNextVisibleItem\(item\)
Retrieves the next visible item of the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetParentItem



HTREEITEM =GetParentItem\(item\)
Retrieves the parent item of the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetPrevSiblingItem



HTREEITEM =GetPrevSiblingItem\(item\)
Retrieves the previous sibling of the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetPrevVisibleItem



HTREEITEM =GetPrevVisibleItem\(item\)
Retrieves the previous visible item of the specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.GetRootItem



HTREEITEM =GetRootItem\(\)
Retrieves the root of the specified tree view item\.

## [PyCTreeCtrl](#pyctreectrl)\.GetSelectedItem



HTREEITEM =GetSelectedItem\(\)
Retrieves the currently selected tree view item\.

## [PyCTreeCtrl](#pyctreectrl)\.GetToolTips

PyCToolTopCtrl

 =GetToolTips\(\)
Returns the tooltip control

## [PyCTreeCtrl](#pyctreectrl)\.GetVisibleCount



int =GetVisibleCount\(\)
Retrieves the number of visible tree items associated with a tree view control\.

## [PyCTreeCtrl](#pyctreectrl)\.HitTest



\(int, int\) =HitTest\(x,y\)
Determines which tree view item, if any, is at a specified position\.

#### Parameters


  - x,y : point

    The point to test\.

#### Return Value
The result is a tuple of \(flags, hItem\)\. 

flags may be a combination of the following values:


## [PyCTreeCtrl](#pyctreectrl)\.InsertItem



int =InsertItem\(hParent, hInsertAfter, item\)
Inserts an item into the list\.

#### Parameters


  - hParent : HTREEITEM

    The parent item\.  If commctrl\.TVI\_ROOT or 0, it is added to the root\.

  - hInsertAfter : HTREEITEM

    The item to insert after\.  Can be an item or TVI\_FIRST, TVI\_LAST or TVI\_SORT

  - item :[TV\_ITEM](TV.md#tvitem)

    A tuple describing the new item\.

#### Alternative Parameters


  - mask

    Integer specifying which attributes to set

  - text

    The text of the item\.

  - image

    The index of the image to use\.

  - selectedImage

    The index of the items selected image\.

  - state

    The initial state of the item\.

  - stateMask

    Specifies which bits of the state are valid\.

  - lParam

    A user defined object for the item\.

  - parent

    The parent of the item\.

  - parent

    The parent of the item\.

#### Alternative Parameters


  - text

    The text for the item\.

  - image

    The index of the image to use\.

  - selectedImage

    The index of the items selected image\.

  - parent

    The parent of the item\.

  - insertAfter

    The item to insert the new item after, or TVI\_FIRST, TVI\_LAST or TVI\_SORT

#### Alternative Parameters


  - text

    The text for the item\.

  - parent

    The parent of the item\.

  - parent

    The parent of the item\.

## [PyCTreeCtrl](#pyctreectrl)\.ItemHasChildren



int =ItemHasChildren\(item\)
Returns nonzero if the specified item has child items\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.Select

Select\(item, code\)
Selects, scrolls into view, or redraws a specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

  - code : int

    The action to take

## [PyCTreeCtrl](#pyctreectrl)\.SelectDropTarget

SelectDropTarget\(item\)
Redraws the tree item as the target of a drag-and-drop operation\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.SelectItem

SelectItem\(item\)
Selects a specified tree view item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.SelectSetFirstVisible

SelectSetFirstVisible\(item\)
Selects a specified tree view item as the first visible item\.

#### Parameters


  - item : HTREEITEM

    The specified item

## [PyCTreeCtrl](#pyctreectrl)\.SetImageList



int =SetImageList\(imageList, imageType\)
Assigns an image list to a list view control\.

#### Parameters


  - imageList :[PyCImageList](#pycimagelist)

    The Image List to use\.

  - imageType : int

    Type of image list\. It can be one of \(COMMCTRL\.\) LVSIL\_NORMAL, LVSIL\_SMALL or LVSIL\_STATE

## [PyCTreeCtrl](#pyctreectrl)\.SetIndent

SetIndent\(indent\)
Sets the offset \(in pixels\) of a tree view item from its parent\.

#### Parameters


  - indent : int

    The new indent\.

## [PyCTreeCtrl](#pyctreectrl)\.SetItem



int =SetItem\(item\)
Sets some of all of an items attributes\.

#### Parameters


  - item :[TV\_ITEM](TV.md#tvitem)

    A tuple describing the new item\.

## [PyCTreeCtrl](#pyctreectrl)\.SetItemData



int =SetItemData\(item, Data\)
Sets the item's application-specific value\.

#### Parameters


  - item : HTREEITEM

    The item whose Data is to be set\.

  - Data : int

    New value for the data\.

#### Comments


Note that a reference count is not added to the object\.  This it is your 

responsibility to make sure the object remains alive while in the list\.

## [PyCTreeCtrl](#pyctreectrl)\.SetItemImage

SetItemImage\(item, iImage, iSelectedImage\)
Sets the index of an items images\.

#### Parameters


  - item : HTREEITEM

    The specified item

  - iImage : int

    The offset of the image\.

  - iSelectedImage : int

    The offset of the selected image\.

## [PyCTreeCtrl](#pyctreectrl)\.SetItemState

SetItemState\(item, state, stateMask\)
Sets the state of item\.

#### Parameters


  - item : HTREEITEM

    The specified item

  - state : int

    The new state

  - stateMask : int

    The mask for the new state

## [PyCTreeCtrl](#pyctreectrl)\.SetItemText



int =SetItemText\(item, text\)
Changes the text of a list view item or subitem\.

#### Parameters


  - item : HTREEITEM

    The item whose text is to be retrieved\.

  - text : string

    String that contains the new item text\.

## [PyCTreeCtrl](#pyctreectrl)\.SortChildren

SortChildren\(item\)
Sorts the children of a given parent item\.

#### Parameters


  - item : HTREEITEM

    The specified parent item