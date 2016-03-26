# LV

## LV\_COLUMN Object



A tuple that describes a Win32 LV\_COLUMN tuple\. Used by the[PyCListCtrl](#pyclistctrl) object\. 

A tuple of 4 items, being fmt, cx, pszText, iSubItem

#### Items


  - \[0\]int : fmt

    Alignment of the column header and the subitem text in the column\.

  - \[1\]int : cx

    Width of the column\.

  - \[2\]string : text

    Column header text\.

  - \[3\]int : subItem

    Index of subitem associated with the column\.
When passed to Python, will always be a tuple of size 4, and items may be None if not available\.
When passed from Python, the tuple may be any length up to 4, and any item may be None\.

## LV\_ITEM Object



Describes an LV\_ITEM tuple, used by the[PyCListCtrl](#pyclistctrl) object\.

#### Items


  - \[0\]int : item

    The item number\.

  - \[1\]int : subItem

    The sub-item number\.

  - \[2\]int : state

    The items state\.  If specified, the stateMask must also be specified\.

  - \[3\]int : stateMask

    A mask indicating which of the state bits are valid\.\.

  - \[4\]string : text

    The text for the item

  - \[5\]int : iImage

    The image offset for the item

  - \[6\]int : userObject

    Any integer to be associated with the item\.

#### Comments


When passed to Python, will always be a tuple of size 7, and items may be None if not available\.
When passed from Python, the tuple must be at least 2 items long, and any item may be None\.
userob is any Python object at all, but no reference count is kept, so you must ensure the object remains referenced throught the lists life\.