# PyCToolBar


## PyCToolBar Object

A class which encapsulates an MFC CToolBar

\.  Derived from a [PyCControlBar](PyCControlBar.md) object\.

#### Methods

  - [GetButtonStyle](PyCToolBar.md#pyctoolbargetbuttonstyle)

    Retrieves the style for a button\.&nbsp;

  - [GetButtonText](PyCToolBar.md#pyctoolbargetbuttontext)

    Gets the text for a button\.&nbsp;

  - [GetItemID](PyCToolBar.md#pyctoolbargetitemid)

    Returns the command ID of a button or separator at the given index\.&nbsp;

  - [SetButtonInfo](PyCToolBar.md#pyctoolbarsetbuttoninfo)

    Gets the associated tooltip control&nbsp;

  - [GetToolBarCtrl](PyCToolBar.md#pyctoolbargettoolbarctrl)

    Returns the tool bar control object associated with the tool bar&nbsp;

  - [LoadBitmap](PyCToolBar.md#pyctoolbarloadbitmap)

    Loads the bitmap containing bitmap-button images\.&nbsp;

  - [LoadToolBar](PyCToolBar.md#pyctoolbarloadtoolbar)

    Loads a toolbar from a Toolbar resource\.&nbsp;

  - [SetBarStyle](PyCToolBar.md#pyctoolbarsetbarstyle)

    Sets toolbar's \(CBRS\_xxx\) part of style&nbsp;

  - [SetBitmap](PyCToolBar.md#pyctoolbarsetbitmap)

    Sets a bitmapped image\.&nbsp;

  - [SetButtonInfo](PyCToolBar.md#pyctoolbarsetbuttoninfo)

    Sets the button's command ID, style, and image number\.&nbsp;

  - [SetButtons](PyCToolBar.md#pyctoolbarsetbuttons)

    Sets button styles and an index of button images within the bitmap\.&nbsp;

  - [SetButtonStyle](PyCToolBar.md#pyctoolbarsetbuttonstyle)

    Sets the style for a button&nbsp;

  - [SetHeight](PyCToolBar.md#pyctoolbarsetheight)

    Sets the height of the toolbar\.&nbsp;

  - [SetSizes](PyCToolBar.md#pyctoolbarsetsizes)

    Sets the sizes for the toolbar items\.&nbsp;

  - [SetButtonInfo](PyCToolBar.md#pyctoolbarsetbuttoninfo)

    Sets the tooltips control&nbsp;


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.GetButtonStyle

GetButtonStyle\(index\)
Retrieves the style for a button\.

#### Parameters

  - index : int

    Index of the item whose style is to be retrieved\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.GetButtonText

string = GetButtonText\(index\)
Gets the text for a button\.

#### Parameters

  - index : int

    Index of the item whose text is to be retrieved\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.GetItemID

GetItemID\(index\)
Returns the command ID of a button or separator at the given index\.

#### Parameters

  - index : int

    Index of the item whose ID is to be retrieved\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.GetToolBarCtrl

[PyCToolBarCtrl](PyCToolBarCtrl.md) = GetToolBarCtrl\(\)
Gets the toolbar control object for the toolbar


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.GetToolTips

GetToolTips\(\)
Returns the associated tooltips control


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.LoadBitmap

LoadBitmap\(id\)
Loads the bitmap containing bitmap-button images\.

#### Parameters

  - id : [PyResourceId](PyResourceId.md)

    Name or id of the resource that contains the bitmap\.

#### Comments

The bitmap should contain one image for each toolbar button\. If the 

images are not of the standard size \(16 pixels wide and 15 pixels high\), 

call [PyCToolBar::SetSizes](PyCToolBar.md#pyctoolbarsetsizes) to set the button sizes and their images\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.LoadToolBar

LoadToolBar\(id\)
Loads a toolbar from a toolbar resource\.

#### Parameters

  - id : [PyResourceId](PyResourceId.md)

    Name or resource id of the resource

#### Comments

The bitmap should contain one image for each toolbar button\. If the 

images are not of the standard size \(16 pixels wide and 15 pixels high\), 

call [PyCToolBar::SetSizes](PyCToolBar.md#pyctoolbarsetsizes) to set the button sizes and their images\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetBarStyle

SetBarStyle\(style\)
Sets the toolbar part of style

#### Parameters

  - style : long

    The toolbar style to set\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetBitmap

SetBitmap\(hBitmap\)
Sets a bitmapped image\.

#### Parameters

  - hBitmap : int

    The handle to a bitmap resource\.

#### Comments

Call this method to set the bitmap image for the toolbar\. For example, 

call SetBitmap to change the bitmapped image after the user takes an action on 

a document that changes the action of a button\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetButtonInfo

SetButtonInfo\(index, ID, style, imageIx\)
Sets the button's command ID, style, and image number\.

#### Parameters

  - index : int

    Index of the button or separator whose information is to be set\.

  - ID : int

    The value to which the button's command ID is set\.

  - style : int

    The new button style

  - imageIx : int

    New index for the button's image within the bitmap


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetButtonStyle

SetButtonStyle\(index, style\)
Sets the style for a button\.

#### Parameters

  - index : int

    Index of the item whose style is to be set

  - style : int

    The new style


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetButtonText

SetButtonText\(index, text\)
Sets the text for a button\.

#### Parameters

  - index : int

    Index of the item whose style is to be set

  - text : string

    The new text


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetButtons

SetButtons\(buttons\)
Sets button styles and an index of button images within the bitmap\.

#### Parameters

  - buttons : tuple

    A tuple containing the ID's of the buttons\.

#### Alternative Parameters

  - numButtons

    The number of buttons to pre-allocate\.  If this option is used, then PyCToolBar::PySetButtonInfo

 must be used\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetHeight

SetHeight\(height\)
Sets the height of the toolbar\.

#### Parameters

  - height : int

    The height in pixels of the toolbar\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetSizes

SetSizes\(sizeButton, sizeButton\)
Sets the size of each button\.

#### Parameters

  - sizeButton : \(cx, cy\)

    The size of each button\.

  - sizeButton : \(cx, cy\)

    The size of each bitmap\.


## [PyCToolBar](PyCToolBar.md#pyctoolbar)\.SetToolTips

SetToolTips\(obTTC\)
Sets the tooltips control

#### Parameters

  - obTTC : [PyCToolTipCtrl](PyCToolTipCtrl.md)

    The ToolTipCtrl ctrl to be set\.