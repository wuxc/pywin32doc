# PyCStatusBarCtrl

## PyCStatusBarCtrl Object



A windows progress bar control\.  Encapsulates an MFCCStatusBarCtrl



 class\.  Derived from[PyCControl](#pyccontrol)\.

#### Methods


  - [CreateWindow](PyCStatusBarCtrl.md#pycstatusbarctrlcreatewindow)

    Creates the window for a new progress bar object\.&nbsp;

  - [GetBorders](PyCStatusBarCtrl.md#pycstatusbarctrlgetborders)

    Retrieve the status bar control's current widths of the horizontal and vertical borders and of the space between rectangles\.&nbsp;

  - [GetParts](PyCStatusBarCtrl.md#pycstatusbarctrlgetparts)

    Retrieve coordinates of the parts in a status bar control\.&nbsp;

  - [GetRect](PyCStatusBarCtrl.md#pycstatusbarctrlgetrect)

    Retrieves the bounding rectangle of a part in a status bar control\.&nbsp;

  - [GetText](PyCStatusBarCtrl.md#pycstatusbarctrlgettext)

    Retrieves the text of a part in a status bar control\.&nbsp;

  - [GetTextAttr](PyCStatusBarCtrl.md#pycstatusbarctrlgettextattr)

    Retrieves the text attributes of a part in a status bar control\.&nbsp;

  - [GetTextLength](PyCStatusBarCtrl.md#pycstatusbarctrlgettextlength)

    Retrieves the length of the text in a part in a status bar control\.&nbsp;

  - [SetMinHeight](PyCStatusBarCtrl.md#pycstatusbarctrlsetminheight)

    Set the minimum height of a status bar control's drawing area\.&nbsp;

  - [SetParts](PyCStatusBarCtrl.md#pycstatusbarctrlsetparts)

    Sets the number of parts in a status bar control and the coordinate of the right edge of each part\.&nbsp;

  - [SetText](PyCStatusBarCtrl.md#pycstatusbarctrlsettext)

    Set the text in the given part of a status bar control\.&nbsp;

  - [SetTipText](PyCStatusBarCtrl.md#pycstatusbarctrlsettiptext)

    Sets the tooltip text for a pane in a status bar\.&nbsp;

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.CreateWindow

CreateWindow\(style, rect, parent, id\)
Creates the actual control\.

#### Parameters


  - style : int

    The style for the control\.

  - rect : \(left, top, right, bottom\)

    The size and position of the control\.

  - parent :[PyCWnd](#pycwnd)

    The parent window of the control\.  Usually a[PyCDialog](#pycdialog)\.

  - id : int

    The control's ID\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.GetBorders



\(width, height, spacing\) =GetBorders\(\)
Retrieve the status bar control's current widths of the horizontal and vertical borders and of the space between rectangles\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.GetParts



\(int\) =GetParts\(nParts\)
Retrieve coordinates of the parts in a status bar control\.

#### Parameters


  - nParts : int

    The number of coordinates to retrieve

#### Comments


This function, as designed in MFC, returns both the \*number\* of parts, and, 

through an OUT parameter, an array of ints giving the coordinates of the 

parts\.  There is also an IN parameter saying how many coordinates to give 

back\.  Here, we're explicitly changing the semantics a bit\.

GetParts\(\) -&gt Tuple of all coordinates
GetParts\(n\) -&gt Tuple of the first n coordinates \(or all coordinates, if 

fewer than n\)


So, in Python, you can't simultaneously find out how many coordinates there 

are, and retrieve a subset of them\.  In a reasonable universe, there would 

have been GetParts\(\) -&gt int, and GetCoords\(\) -&gt List\.  This means that I 

need to call the MFC method twice; once to find out how many there are, and 

another time to get them\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.GetRect



\(left, top, right, bottom\) =GetRect\(nPane\)
Retrieves the bounding rectangle of a part in a status bar control\.

#### Parameters


  - nPane : int

    Zero-based index of the part whose bounding rectangle is to be retrieved\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.GetText



text =GetText\(nPane\)
Retrieve the text from the given part of a status bar control\.

#### Parameters


  - nPane : int

    Zero-based index of the part whose text is to be retrieved\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.GetTextAttr



int =GetTextAttr\(nPane\)
Retrieve the attributes of the text in the given part of a status bar control\.

#### Parameters


  - nPane : int

    Zero-based index of the part whose text is to be retrieved\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.GetTextLength



int =GetTextLength\(nPane\)
Retrieve the length the text in the given part of a status bar control\.

#### Parameters


  - nPane : int

    Zero-based index of the part whose text is to be retrieved\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.SetMinHeight

SetMinHeight\(nHeight\)
Set the minimum height of a status bar control's drawing area\.

#### Parameters


  - nHeight : int

    Minimum height

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.SetParts

SetParts\(coord\)
Sets the number of parts in a status bar control and the coordinate of the right edge of each part\.

#### Parameters


  - coord : int\.\.\.

    Coordinates of each part

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.SetSimple

SetSimple\(bSimple\)
Specify whether a status bar control displays simple text or displays all control parts set by a previous call to SetParts\.

#### Parameters


  - bSimple : int

    If non-zero, displays simple text\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.SetText

SetText\(text, nPane, nType\)
Set the text in the given part of a status bar control\.

#### Parameters


  - text : string

    The text to display

  - nPane : int

    Zero-based index of the part to set\.

  - nType : int

    Type of drawing operation\.

#### Comments


The drawing type can be set to one of:~ 

0 - The text is drawn with a border to appear lower than 

the plane of the status bar\.~ 

win32con\.SBT\_NOBORDERS - The text is drawn without borders\.~ 

win32con\.SBT\_OWNERDRAW - The text is drawn by the parent window\.~ 

win32con\.SBT\_POPOUT - The text is drawn with a border to appear 

higher than the plane of the status bar\.

## [PyCStatusBarCtrl](#pycstatusbarctrl)\.SetTipText

SetTipText\(nPane, text\)
Sets the tooltip text for a pane in a status bar\. The status bar must have been created with the afxres\.SBT\_TOOLTIPS control style to enable ToolTips\.

#### Parameters


  - nPane : int

    The zero-based index of status bar pane to receive the tooltip text\.

  - text : string

    The string containing the tooltip text\.

#### Comments


Pay attention, this tooltip text is ONLY displayed in two situations:
1\. When the corresponding pane in the status bar contains only an icon\.
2\. When the corresponding pane in the status bar contains text that is truncated due to the size of the pane\.
To make the tooltip appear even if the text is not truncated, you could add additional spaces to the end of the pane text\.

#### MFC References


  - CStatusBarCtrl::SetTipText