# PyCListBox

## PyCListBox Object



A windows listbox control\.  Encapsulates an MFCCListBox



 class\.  Derived from a[PyCControl](#pyccontrol) object\.

#### Methods


  - [AddString](PyCListBox.md#pyclistboxaddstring)

    Add a string to the listbox\.&nbsp;

  - [DeleteString](PyCListBox.md#pyclistboxdeletestring)

    Delete a string from the listbox\.&nbsp;

  - [Dir](PyCListBox.md#pyclistboxdir)

    Fill a listbox with a file specification\.&nbsp;

  - [GetCaretIndex](PyCListBox.md#pyclistboxgetcaretindex)

    Get the index of the item with the focus rectangle\.&nbsp;

  - [GetCount](PyCListBox.md#pyclistboxgetcount)

    Get the count of items in the listbox\.&nbsp;

  - [GetCurSel](PyCListBox.md#pyclistboxgetcursel)

    Get the current selection in a single selection listbox\.&nbsp;

  - [GetItemData](PyCListBox.md#pyclistboxgetitemdata)

    Retrieves the application-specific object associated with a listbox entry&nbsp;

  - [GetItemValue](PyCListBox.md#pyclistboxgetitemvalue)

    Retrieves the application-specific value associated with a listbox entry&nbsp;

  - [GetSel](PyCListBox.md#pyclistboxgetsel)

    Get the selected items in a multiple selection listbox\.&nbsp;

  - [GetSelCount](PyCListBox.md#pyclistboxgetselcount)

    Get the number of selected items in a multtiple selection listbox\.&nbsp;

  - [GetSelItems](PyCListBox.md#pyclistboxgetselitems)

    Get the index of the selected items in a multiple selection listbox\.&nbsp;

  - [GetSelTextItems](PyCListBox.md#pyclistboxgetseltextitems)

    Get the text of the selected items in a multiple selection listbox\.&nbsp;

  - [GetTopIndex](PyCListBox.md#pyclistboxgettopindex)

    Get the index of the topmost item\.&nbsp;

  - [GetText](PyCListBox.md#pyclistboxgettext)

    Get the text associated with an item\.&nbsp;

  - [GetTextLen](PyCListBox.md#pyclistboxgettextlen)

    Get the length of an item&nbsp;

  - [InsertString](PyCListBox.md#pyclistboxinsertstring)

    Insert a string into the listbox\.&nbsp;

  - [ResetContent](PyCListBox.md#pyclistboxresetcontent)

    Remove all items from a listbox\.&nbsp;

  - [SetCaretIndex](PyCListBox.md#pyclistboxsetcaretindex)

    Set the focus rectange to a specified item\.&nbsp;

  - [SelectString](PyCListBox.md#pyclistboxselectstring)

    Select an item, based on a string\.&nbsp;

  - [SelItemRange](PyCListBox.md#pyclistboxselitemrange)

    Select a range of items in a multiple selection listbox\.&nbsp;

  - [SetCurSel](PyCListBox.md#pyclistboxsetcursel)

    Set the current selection in a single selection listbox\.&nbsp;

  - [SetItemData](PyCListBox.md#pyclistboxsetitemdata)

    Sets the application-specific object associated with a listbox entry&nbsp;

  - [SetItemValue](PyCListBox.md#pyclistboxsetitemvalue)

    Sets the application-specific value associated with a listbox entry&nbsp;

  - [SetSel](PyCListBox.md#pyclistboxsetsel)

    Set the selection\.&nbsp;

  - [SetTabStops](PyCListBox.md#pyclistboxsettabstops)

    Set the tab stops for a listbox\.&nbsp;

  - [SetTopIndex](PyCListBox.md#pyclistboxsettopindex)

    Set the top most visible item in a listbox\.&nbsp;

## [PyCListBox](#pyclistbox)\.AddString



int =AddString\(object\)
Adds a string to a listbox\.

#### Parameters


  - object : any

    Any object\.  If not a string, \_\_str\_\_, \_\_repr\_\_ or a default repr\(\) will be used

#### MFC References


  - CListBox::AddString

#### Return Value
The zero based index of the new string\.

## [PyCListBox](#pyclistbox)\.DeleteString



int =DeleteString\(pos\)
Deletes an item from a listbox\.

#### Parameters


  - pos : int

    The zero based index of the item to delete\.

#### MFC References


  - CListBox::DeleteString

#### Return Value
The count of the items remaining in the list\.

## [PyCListBox](#pyclistbox)\.Dir



int =Dir\(attr, wild\)
Fills a listbox with a directory listing\.

#### Parameters


  - attr : int

    The attributes of the files to locate

  - wild : string

    A file specification string - eg, \*\.\*

#### MFC References


  - CListBox::Dir

#### Return Value
The index of the last file name added to the list\.

## [PyCListBox](#pyclistbox)\.GetCaretIndex



int =GetCaretIndex\(\)
Returns the index of the item which has focus\.

#### Return Value
The zero-based index of the item that has the focus rectangle in a list box\. 

If the list box is a single-selection list box, the return value is the index of the item that is selected, if any\.

## [PyCListBox](#pyclistbox)\.GetCount



int =GetCount\(\)
Returns the count of items in the listbox\.

#### MFC References


  - CListBox::GetCount

#### Return Value
Returns the number of items currently in the listbox\.

## [PyCListBox](#pyclistbox)\.GetCurSel



int =GetCurSel\(\)
Returns the index of the currently selected item\.

#### Comments


Should not be called for a multiple selection listbox\.

#### MFC References


  - CListBox::GetCurSel

## [PyCListBox](#pyclistbox)\.GetItemData



object =GetItemData\(item\)
Retrieves the application-specific object associated with an item\.

#### Parameters


  - item : int

    The index of the item whose data is to be retrieved\.

## [PyCListBox](#pyclistbox)\.GetItemValue



int =GetItemValue\(item\)
Retrieves the application-specific value associated with an item\.

#### Parameters


  - item : int

    The index of the item whose data is to be retrieved\.

## [PyCListBox](#pyclistbox)\.GetSel



int =GetSel\(index\)
Returns the selection state of a specified item\.

#### Parameters


  - index : int

    The index of the item to return the state for\.

#### MFC References


  - CListBox::GetSel

#### Return Value
A \+ve number if the item is selected, else zero\.

## [PyCListBox](#pyclistbox)\.GetSelCount



int =GetSelCount\(\)
Returns the number of selected items in a multiple selection listbox\.

#### MFC References


  - CListBox::GetSelCount

## [PyCListBox](#pyclistbox)\.GetSelItems



list =GetSelItems\(\)
Returns a list of the indexes of the currently selected items in a multiple selection listbox\.

#### MFC References


  - CListBox::GetSelCount

  - CListBox::GetSelItems

## [PyCListBox](#pyclistbox)\.GetSelTextItems



list =GetSelTextItems\(\)
Returns a list of the strings of the currently selected items in a multiple selection listbox\.

#### MFC References


  - CListBox::GetSelCount

  - CListBox::GetSelItems

  - CListBox::GetText

## [PyCListBox](#pyclistbox)\.GetText



string =GetText\(index\)
Returns the string for a specified item\.

#### Parameters


  - index : int

    The index of the item to retrieve the text of

## [PyCListBox](#pyclistbox)\.GetTextLen



int =GetTextLen\(index\)
Returns the length of the string for a specified item\.

#### Parameters


  - index : int

    The index of the item to retrieve the length of the text\.

#### MFC References


  - CListBox::GetTextLen

## [PyCListBox](#pyclistbox)\.GetTopIndex



int =GetTopIndex\(\)
Returns the index of the top most visible item\.

#### MFC References


  - CListBox::GetTopIndex

#### Return Value
The zero based index of the top most visible item\.

## [PyCListBox](#pyclistbox)\.InsertString



int =InsertString\(pos, object\)
Insert a string into a listbox\.

#### Parameters


  - pos : int

    The zero based index in the listbox to insert the new string

  - object : any

    The object to be added to the listbox

#### MFC References


  - CListBox::InsertString

#### Return Value
The zero based index of the new string added\.

## [PyCListBox](#pyclistbox)\.ResetContent

ResetContent\(\)
Clear all the items from a listbox\.

#### MFC References


  - CListBox::ResetContent

## [PyCListBox](#pyclistbox)\.SelItemRange

SelItemRange\(bSel, start, end\)
Selects an item range\.

#### Parameters


  - bSel : int

    Should the selection specified be set or cleared?

  - start : int

    The zero based index of the first item to select\.

  - end : int

    The zero based index of the last item to select\.

## [PyCListBox](#pyclistbox)\.SelectString

SelectString\(after, string\)
Searches for a list-box item that matches the specified string, and selects it\.

#### Parameters


  - after : int

    Contains the zero-based index of the item before the first item to be searched, or -1 for the entire listbox\.

  - string : string

    The string to search for\.

#### MFC References


  - CListBox::SelectString

#### Return Value
The return value is always None - an exception is raised if the string can not be located\.

## [PyCListBox](#pyclistbox)\.SetCaretIndex

SetCaretIndex\(index, bScroll\)
Sets the focus rectange to a specified item\.

#### Parameters


  - index : int

    The zero based index of the item\.

  - bScroll=1 : int

    Should the listbox scroll to the item?

#### MFC References


  - CListBox::SetCaretIndex

## [PyCListBox](#pyclistbox)\.SetCurSel

SetCurSel\(index\)
Selects an item in a single selection listbox\.

#### Parameters


  - index : int

    The zero based index of the item to select\.

#### MFC References


  - CListBox::SetCurSel

## [PyCListBox](#pyclistbox)\.SetItemData



int =SetItemData\(item, Data\)
Sets the item's application-specific object value\.

#### Parameters


  - item : int

    Index of the item whose Data is to be set\.

  - Data : object

    New value for the data\.

#### Comments


Note that a reference count is not added to the object\.  This it is your 

responsibility to make sure the object remains alive while in the list\.

## [PyCListBox](#pyclistbox)\.SetItemValue



int =SetItemValue\(item, data\)
Sets the item's application-specific value\.

#### Parameters


  - item : int

    Index of the item whose Data is to be set\.

  - data : int

    New value for the data\.

## [PyCListBox](#pyclistbox)\.SetSel

SetSel\(index, bSel\)
Selects an item in a multiple selection listbox\.

#### Parameters


  - index : int

    The zero based index of the item to select\.

  - bSel=1 : int

    Should the item be selected or deselected?

#### MFC References


  - CListBox::SetSel

## [PyCListBox](#pyclistbox)\.SetTabStops

SetTabStops\(eachTabStop\)
Sets the tab stops for a listbox\.

#### Parameters


  - eachTabStop : int

    The position for each tab stop\.

#### Alternative Parameters


  - tabStops

    Each individual tab stop\.

## [PyCListBox](#pyclistbox)\.SetTopIndex

SetTopIndex\(index\)
Sets the top index \(top most visible item\) of the listbox\.

#### Parameters


  - index : int

    The zero based index of the item to place at the top of the list\.

#### MFC References


  - CListBox::SetTopIndex