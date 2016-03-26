# SCROLLINFO

## SCROLLINFO tuple Object



Tuple representing a SCROLLINFO struct

#### Items


  - \[0\]int : addnMask

    Additional mask information\.  Python automatically fills the mask for valid items, so currently the only valid values are zero, and win32con\.SIF\_DISABLENOSCROLL\.

  - \[1\]int : min

    The minimum scrolling position\.  Both min and max, or neither, must be provided\.

  - \[2\]int : max

    The maximum scrolling position\.  Both min and max, or neither, must be provided\.

  - \[3\]int : page

    Specifies the page size\. A scroll bar uses this value to determine the appropriate size of the proportional scroll box\.

  - \[4\]int : pos

    Specifies the position of the scroll box\.

  - \[5\]int : trackPos

    Specifies the immediate position of a scroll box that the user 

is dragging\. An application can retrieve this value while processing 

the SB\_THUMBTRACK notification message\. An application cannot set 

the immediate scroll position; the[PyCWnd::SetScrollInfo](PyCWnd.md#pycwndsetscrollinfo) function ignores 

this member\.

#### Comments


When returned from a method, will always be a tuple of size 6, and items may be None if not available\.


When passed as an arg, it must have the addn mask attribute, but all other items may be None, or not exist\.