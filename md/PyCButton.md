# PyCButton


## PyCButton Object

A windows button\.  Encapsulates an MFC CButton

 class\.  Derived from [PyCControl](PyCControl.md)\.

#### Methods

  - [CreateWindow](PyCButton.md#pycbuttoncreatewindow)

    Creates the window for a new button object\.&nbsp;

  - [GetBitmap](PyCButton.md#pycbuttongetbitmap)

    Retrieves the bitmap associated with the button\.&nbsp;

  - [SetBitmap](PyCButton.md#pycbuttonsetbitmap)

    Sets the bitmap of a button\.&nbsp;

  - [GetCheck](PyCButton.md#pycbuttongetcheck)

    Retrieves the check state of a radio button or check box\.&nbsp;

  - [SetCheck](PyCButton.md#pycbuttonsetcheck)

    Sets the check state of a radio button or check box\.&nbsp;

  - [GetState](PyCButton.md#pycbuttongetstate)

    Retrieves the state of a radio button or check box\.&nbsp;

  - [SetState](PyCButton.md#pycbuttonsetstate)

    Sets the state of a radio button or check box\.&nbsp;

  - [GetButtonStyle](PyCButton.md#pycbuttongetbuttonstyle)

    Retrieves the style of a radio button or check box\.&nbsp;

  - [SetButtonStyle](PyCButton.md#pycbuttonsetbuttonstyle)

    Sets the state of a radio button or check box\.&nbsp;


## [PyCButton](PyCButton.md#pycbutton)\.CreateWindow

CreateWindow\(caption, style, rect, parent, id\)
Creates the window for a new button object\.

#### Parameters

  - caption : string

    The caption \(text\) for the button\.

  - style : int

    The style for the button\.  Use any of the win32con\.BS\_\* constants\.

  - rect : \(left, top, right, bottom\)

    The size and position of the button\.

  - parent : [PyCWnd](PyCWnd.md)

    The parent window of the button\.  Usually a [PyCDialog](PyCDialog.md)\.

  - id : int

    The buttons control ID\.


## [PyCButton](PyCButton.md#pycbutton)\.GetBitmap

int = GetBitmap\(\)
Get the button's bitmap


## [PyCButton](PyCButton.md#pycbutton)\.GetButtonStyle

int = GetButtonStyle\(\)
Gets the style of the button\.


## [PyCButton](PyCButton.md#pycbutton)\.GetCheck

int = GetCheck\(\)
Retrieves the check state of a radio button or check box\.


## [PyCButton](PyCButton.md#pycbutton)\.GetState

int = GetState\(\)
Returns the state of the button\.


## [PyCButton](PyCButton.md#pycbutton)\.SetBitmap

int = SetBitmap\(hBitmap\)
Set the button's bitmap

#### Parameters

  - hBitmap=1 : int

    Handle of the new bitmap


## [PyCButton](PyCButton.md#pycbutton)\.SetButtonStyle

int = SetButtonStyle\(style, bRedraw

\)
Sets the style of the button\.

#### Parameters

  - style : int

    The new style for the button\.

  - bRedraw=1 : int

    Should the button be redrawn?


## [PyCButton](PyCButton.md#pycbutton)\.SetCheck

SetCheck\(idCheck\)
Sets or resets the state of a radio button or check box\.

#### Parameters

  - idCheck : int

    The ID of the button\.


## [PyCButton](PyCButton.md#pycbutton)\.SetState

int = SetState\(bHighlight\)
Sets the state of the button\.

#### Parameters

  - bHighlight : int

    The new state for the button\.

#### Comments

Highlighting affects the exterior of a button control\. It has no effect on the check state of a radio button or check box\.