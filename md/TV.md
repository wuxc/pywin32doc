# TV


## TV\_ITEM Object

Describes a TV\_ITEM tuple, used by the [PyCListCtrl](PyCListCtrl.md) object\. 

A tuple of 8 items: 

When returned from a win32ui function, will always be a tuple of size 8, and items may be None if not available\. 

When passed to a win32ui function, the tuple may be any length up to 8, and any item may be None\.

#### Items

  - \[0\] int : hItem

    Item handle

  - \[1\] int : state

    Item state\.  If specified, the stateMask must also be specified\.

  - \[2\] int : stateMask

    Item state mask

  - \[3\] string : text

    Item text

  - \[4\] int : iImage

    Image list index of icon for non-seleted state\.

  - \[5\] int : iSelectedImage

    Offset of items selected image\.

  - \[6\] int : cChildren

    Number of child items\.

  - \[7\] int : lParam

    User defined integer param\.