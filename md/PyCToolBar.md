# PyCToolBar

## PyCToolBar Object

A class which encapsulates an MFC __CToolBar__ .  Derived from a[PyCControlBar](#pyccontrolbar)object.

#### Methods


  - [GetButtonStyle](PyCToolBar.md#pyctoolbargetbuttonstyle)

    Retrieves the style for a button.&nbsp;

  - [GetButtonText](PyCToolBar.md#pyctoolbargetbuttontext)

    Gets the text for a button.&nbsp;

  - [GetItemID](PyCToolBar.md#pyctoolbargetitemid)

    Returns the command ID of a button or separator at the given index.&nbsp;

  - [SetButtonInfo](PyCToolBar.md#pyctoolbarsetbuttoninfo)

    Gets the associated tooltip control&nbsp;

  - [GetToolBarCtrl](PyCToolBar.md#pyctoolbargettoolbarctrl)

    Returns the tool bar control object associated with the tool bar&nbsp;

  - [LoadBitmap](PyCToolBar.md#pyctoolbarloadbitmap)

    Loads the bitmap containing bitmap-button images.&nbsp;

  - [LoadToolBar](PyCToolBar.md#pyctoolbarloadtoolbar)

    Loads a toolbar from a Toolbar resource.&nbsp;

  - [SetBarStyle](PyCToolBar.md#pyctoolbarsetbarstyle)

    Sets toolbar's (CBRS_xxx) part of style&nbsp;

  - [SetBitmap](PyCToolBar.md#pyctoolbarsetbitmap)

    Sets a bitmapped image.&nbsp;

  - [SetButtonInfo](PyCToolBar.md#pyctoolbarsetbuttoninfo)

    Sets the button's command ID, style, and image number.&nbsp;

  - [SetButtons](PyCToolBar.md#pyctoolbarsetbuttons)

    Sets button styles and an index of button images within the bitmap.&nbsp;

  - [SetButtonStyle](PyCToolBar.md#pyctoolbarsetbuttonstyle)

    Sets the style for a button&nbsp;

  - [SetHeight](PyCToolBar.md#pyctoolbarsetheight)

    Sets the height of the toolbar.&nbsp;

  - [SetSizes](PyCToolBar.md#pyctoolbarsetsizes)

    Sets the sizes for the toolbar items.&nbsp;

  - [SetButtonInfo](PyCToolBar.md#pyctoolbarsetbuttoninfo)

    Sets the tooltips control&nbsp;

## [PyCToolBar](#pyctoolbar).GetButtonStyle

 __GetButtonStyle( *index* __ )
Retrieves the style for a button.

#### Parameters


  -  *index* : int

    Index of the item whose style is to be retrieved.

## [PyCToolBar](#pyctoolbar).GetButtonText

string = __GetButtonText( *index* __ )
Gets the text for a button.

#### Parameters


  -  *index* : int

    Index of the item whose text is to be retrieved.

## [PyCToolBar](#pyctoolbar).GetItemID

 __GetItemID( *index* __ )
Returns the command ID of a button or separator at the given index.

#### Parameters


  -  *index* : int

    Index of the item whose ID is to be retrieved.

## [PyCToolBar](#pyctoolbar).GetToolBarCtrl

[PyCToolBarCtrl](#pyctoolbarctrl)= __GetToolBarCtrl(__ )
Gets the toolbar control object for the toolbar

## [PyCToolBar](#pyctoolbar).GetToolTips

 __GetToolTips(__ )
Returns the associated tooltips control

## [PyCToolBar](#pyctoolbar).LoadBitmap

 __LoadBitmap( *id* __ )
Loads the bitmap containing bitmap-button images.

#### Parameters


  -  *id* :[PyResourceId](#pyresourceid)

    Name or id of the resource that contains the bitmap.

#### Comments
The bitmap should contain one image for each toolbar button. If the 

images are not of the standard size (16 pixels wide and 15 pixels high), 

call[PyCToolBar::SetSizes](PyCToolBar.md#pyctoolbarsetsizes)to set the button sizes and their images.

## [PyCToolBar](#pyctoolbar).LoadToolBar

 __LoadToolBar( *id* __ )
Loads a toolbar from a toolbar resource.

#### Parameters


  -  *id* :[PyResourceId](#pyresourceid)

    Name or resource id of the resource

#### Comments
The bitmap should contain one image for each toolbar button. If the 

images are not of the standard size (16 pixels wide and 15 pixels high), 

call[PyCToolBar::SetSizes](PyCToolBar.md#pyctoolbarsetsizes)to set the button sizes and their images.

## [PyCToolBar](#pyctoolbar).SetBarStyle

 __SetBarStyle( *style* __ )
Sets the toolbar part of style

#### Parameters


  -  *style* : long

    The toolbar style to set.

## [PyCToolBar](#pyctoolbar).SetBitmap

 __SetBitmap( *hBitmap* __ )
Sets a bitmapped image.

#### Parameters


  -  *hBitmap* : int

    The handle to a bitmap resource.

#### Comments
Call this method to set the bitmap image for the toolbar. For example, 

call SetBitmap to change the bitmapped image after the user takes an action on 

a document that changes the action of a button.

## [PyCToolBar](#pyctoolbar).SetButtonInfo

 __SetButtonInfo( *index*  *, ID*  *, style*  *, imageIx* __ )
Sets the button's command ID, style, and image number.

#### Parameters


  -  *index* : int

    Index of the button or separator whose information is to be set.

  -  *ID* : int

    The value to which the button's command ID is set.

  -  *style* : int

    The new button style

  -  *imageIx* : int

    New index for the button's image within the bitmap

## [PyCToolBar](#pyctoolbar).SetButtonStyle

 __SetButtonStyle( *index*  *, style* __ )
Sets the style for a button.

#### Parameters


  -  *index* : int

    Index of the item whose style is to be set

  -  *style* : int

    The new style

## [PyCToolBar](#pyctoolbar).SetButtonText

 __SetButtonText( *index*  *, text* __ )
Sets the text for a button.

#### Parameters


  -  *index* : int

    Index of the item whose style is to be set

  -  *text* : string

    The new text

## [PyCToolBar](#pyctoolbar).SetButtons

 __SetButtons( *buttons* __ )
Sets button styles and an index of button images within the bitmap.

#### Parameters


  -  *buttons* : tuple

    A tuple containing the ID's of the buttons.

#### Alternative Parameters


  -  *numButtons* 

    The number of buttons to pre-allocate.  If this option is used, then __PyCToolBar::PySetButtonInfo__ must be used.

## [PyCToolBar](#pyctoolbar).SetHeight

 __SetHeight( *height* __ )
Sets the height of the toolbar.

#### Parameters


  -  *height* : int

    The height in pixels of the toolbar.

## [PyCToolBar](#pyctoolbar).SetSizes

 __SetSizes( *sizeButton*  *, sizeButton* __ )
Sets the size of each button.

#### Parameters


  -  *sizeButton* : (cx, cy)

    The size of each button.

  -  *sizeButton* : (cx, cy)

    The size of each bitmap.

## [PyCToolBar](#pyctoolbar).SetToolTips

 __SetToolTips( *obTTC* __ )
Sets the tooltips control

#### Parameters


  -  *obTTC* :[PyCToolTipCtrl](#pyctooltipctrl)

    The ToolTipCtrl ctrl to be set.