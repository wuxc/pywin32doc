# PyCToolBarCtrl

## PyCToolBarCtrl Object

A class which encapsulates an MFC __CToolBarCtrl__ .  Derived from a[PyCWnd](#pycwnd)object. Created using[PyCToolBar::GetToolBarCtrl](PyCToolBar.md#pyctoolbargettoolbarctrl)

#### Methods


  - [AddBitmap](PyCToolBarCtrl.md#pyctoolbarctrladdbitmap)

    Add one or more button images to the list of button images&nbsp;

  - [AddButtons](PyCToolBarCtrl.md#pyctoolbarctrladdbuttons)

    Add one or more buttons&nbsp;

  - [AddStrings](PyCToolBarCtrl.md#pyctoolbarctrladdstrings)

    Add one or more strings&nbsp;

  - [AutoSize](PyCToolBarCtrl.md#pyctoolbarctrlautosize)

    Resize the entire toolbar&nbsp;

  - [CheckButton](PyCToolBarCtrl.md#pyctoolbarctrlcheckbutton)

    Check or clear a button&nbsp;

  - [CommandToIndex](PyCToolBarCtrl.md#pyctoolbarctrlcommandtoindex)

    Retrieve the zero-based index for the button associated with the specified command identifier.&nbsp;

  - [CreateWindow](PyCToolBarCtrl.md#pyctoolbarctrlcreatewindow)

    Create the actual control&nbsp;

  - [Customize](PyCToolBarCtrl.md#pyctoolbarctrlcustomize)

    Display the customize toolbar dialog box&nbsp;

  - [DeleteButton](PyCToolBarCtrl.md#pyctoolbarctrldeletebutton)

    Delete a button from the toolbar control&nbsp;

  - [EnableButton](PyCToolBarCtrl.md#pyctoolbarctrlenablebutton)

    Enable or disable a toolbar control button.&nbsp;

  - [GetBitmapFlags](PyCToolBarCtrl.md#pyctoolbarctrlgetbitmapflags)

    Retrieve the bitmap flags from the toolbar.&nbsp;

  - [GetButton](PyCToolBarCtrl.md#pyctoolbarctrlgetbutton)

    Retrieve information about the specified button in a toolbar control.&nbsp;

  - [GetButtonCount](PyCToolBarCtrl.md#pyctoolbarctrlgetbuttoncount)

    Retrieve a count of the buttons currently in the toolbar control.&nbsp;

  - [GetItemRect](PyCToolBarCtrl.md#pyctoolbarctrlgetitemrect)

    Retrieve the bounding rectangle of a button in a toolbar control.&nbsp;

  - [GetRows](PyCToolBarCtrl.md#pyctoolbarctrlgetrows)

    Retrieve the number of rows of buttons currently displayed&nbsp;

  - [HideButton](PyCToolBarCtrl.md#pyctoolbarctrlhidebutton)

    Hide or show the specified button in a toolbar control.&nbsp;

  - [Indeterminate](PyCToolBarCtrl.md#pyctoolbarctrlindeterminate)

    Hide or show the specified button in a toolbar control.&nbsp;

  - [InsertButton](PyCToolBarCtrl.md#pyctoolbarctrlinsertbutton)

    Insert a button into a toolbar control.&nbsp;

  - [IsButtonChecked](PyCToolBarCtrl.md#pyctoolbarctrlisbuttonchecked)

    See if a button is checked.&nbsp;

  - [IsButtonEnabled](PyCToolBarCtrl.md#pyctoolbarctrlisbuttonenabled)

    See if a button is enabled.&nbsp;

  - [IsButtonHidden](PyCToolBarCtrl.md#pyctoolbarctrlisbuttonhidden)

    See if a button is checked.&nbsp;

  - [IsButtonIndeterminate](PyCToolBarCtrl.md#pyctoolbarctrlisbuttonindeterminate)

    See if a button is Indeterminate.&nbsp;

  - [IsButtonPressed](PyCToolBarCtrl.md#pyctoolbarctrlisbuttonpressed)

    See if a button is pressed.&nbsp;

  - [PressButton](PyCToolBarCtrl.md#pyctoolbarctrlpressbutton)

    Mark or unmark the specified button as pressed.&nbsp;

  - [SetBitmapSize](PyCToolBarCtrl.md#pyctoolbarctrlsetbitmapsize)

    Set the size of the actual bitmapped images to be added to a toolbar control.&nbsp;

  - [SetButtonSize](PyCToolBarCtrl.md#pyctoolbarctrlsetbuttonsize)

    Set the size of the actual buttons to be added to a toolbar control.&nbsp;

  - [SetCmdID](PyCToolBarCtrl.md#pyctoolbarctrlsetcmdid)

    Set the command identifier which will be sent to the owner window when the specified button is pressed.&nbsp;

  - [SetRows](PyCToolBarCtrl.md#pyctoolbarctrlsetrows)

    Ask the toolbar control to resize itself to the requested number of rows.&nbsp;

## [PyCToolBarCtrl](#pyctoolbarctrl).AddBitmap

int = __AddBitmap( *numButtons*  *, bitmap* __ )
Add one or more button images to the list of button images

#### Parameters


  -  *numButtons* : int

    Number of button images in the bitmap.

  -  *bitmap* :[PyBitmap](#pybitmap)

    Bitmap containing button or buttons to be added

#### MFC References


  - CToolBarCtrl::AddBitmap

## [PyCToolBarCtrl](#pyctoolbarctrl).AddButtons

int = __AddButtons(__ )
Add one or more buttons to the toolbar

#### MFC References


  - CToolBarCtrl::AddButtons

## [PyCToolBarCtrl](#pyctoolbarctrl).AddStrings

int = __AddStrings( *strings* __ )
Add one or more strings to the toolbar

#### Parameters


  -  *strings* : string...

    Strings to add. Can give more than one string.

## [PyCToolBarCtrl](#pyctoolbarctrl).AutoSize

 __AutoSize(__ )
Resize the entire toolbar control

#### MFC References


  - CToolBarCtrl::AutoSize

## [PyCToolBarCtrl](#pyctoolbarctrl).CheckButton

int = __CheckButton( *nID*  *, bCheck* __ )
Check or clear a given button in a toolbar control

#### Parameters


  -  *nID* : int

    Command identifier of the button to check or clear.

  -  *bCheck=1* : int

    1 to check, 0 to clear the button

#### MFC References


  - CToolBarCtrl::CheckButton

## [PyCToolBarCtrl](#pyctoolbarctrl).CommandToIndex

int = __CommandToIndex( *nID* __ )
Retrieve the zero-based index for the button associated with the specified command identifier.

#### Parameters


  -  *nID* : int

    Command identifier of the button you want to find.

#### MFC References


  - CToolBarCtrl::CommandToIndex

## [PyCToolBarCtrl](#pyctoolbarctrl).CreateWindow

 __CreateWindow( *style*  *, rect*  *, parent*  *, id* __ )
Creates the window for a new toolbar object

#### Parameters


  -  *style* : int

    The style for the button.  Use any of the win32con.BS_* constants.

  -  *rect* : (left, top, right, bottom)

    The size and position of the button.

  -  *parent* :[PyCWnd](#pycwnd)

    The parent window of the button.  Usually a[PyCDialog](#pycdialog).

  -  *id* : int

    The buttons control ID.

#### MFC References


  - CToolBarCtrl::Create

## [PyCToolBarCtrl](#pyctoolbarctrl).Customize

 __Customize(__ )
Display the Customize Toolbar dialog box.

#### MFC References


  - CToolBarCtrl::Customize

## [PyCToolBarCtrl](#pyctoolbarctrl).DeleteButton

 __DeleteButton( *nID* __ )
Delete a button from the toolbar control.

#### Parameters


  -  *nID* : int

    ID of the button to delete.

#### MFC References


  - CToolBarCtrl::DeleteButton

## [PyCToolBarCtrl](#pyctoolbarctrl).EnableButton

 __EnableButton( *nID*  *, bEnable* __ )
Enable or disable a toolbar control button.

#### Parameters


  -  *nID* : int

    ID of the button to enable or disable.

  -  *bEnable=1* : int

    1 to enable, 0 to disable

#### MFC References


  - CToolBarCtrl::EnableButton

## [PyCToolBarCtrl](#pyctoolbarctrl).GetBitmapFlags

int = __GetBitmapFlags(__ )
retrieve the bitmap flags from the toolbar.

#### MFC References


  - CToolBarCtrl::GetBitmapFlags

## [PyCToolBarCtrl](#pyctoolbarctrl).GetButton

 __PyCToolBarCtrl::TBBUTTON__ = __GetButton( *nID* __ )
Retrieve information about the specified button in a toolbar control.

#### Parameters


  -  *nID* : int

    ID of the button to retrieve.

#### MFC References


  - CToolBarCtrl::GetButton

## [PyCToolBarCtrl](#pyctoolbarctrl).GetButtonCount

int = __GetButtonCount(__ )
Retrieve a count of the buttons currently in the toolbar control.

#### MFC References


  - CToolBarCtrl::GetButtonCount

## [PyCToolBarCtrl](#pyctoolbarctrl).GetItemRect

left, top, right, bottom = __GetItemRect( *nID* __ )
Retrieve the bounding rectangle of a button in a toolbar control.

#### Parameters


  -  *nID* : int

    ID of the button.

#### MFC References


  - CToolBarCtrl::GetItemRect

## [PyCToolBarCtrl](#pyctoolbarctrl).GetRows

left, top, right, bottom = __GetRows(__ )
Retrieve the number of rows of buttons currently displayed

#### MFC References


  - CToolBarCtrl::GetRows

## [PyCToolBarCtrl](#pyctoolbarctrl).HideButton

 __HideButton( *nID*  *, bEnable* __ )
Hide or show the specified button in a toolbar control.

#### Parameters


  -  *nID* : int

    ID of the button to hide.

  -  *bEnable=1* : int

    1 to hide, 0 to show.

#### MFC References


  - CToolBarCtrl::HideButton

## [PyCToolBarCtrl](#pyctoolbarctrl).Indeterminate

 __Indeterminate( *nID*  *, bEnable* __ )
Mark or unmark the specified button as indeterminate

#### Parameters


  -  *nID* : int

    ID of the button to mark.

  -  *bEnable=1* : int

    1 to hide, 0 to show.

#### MFC References


  - CToolBarCtrl::Indeterminate

## [PyCToolBarCtrl](#pyctoolbarctrl).InsertButton

int = __InsertButton( *nID*  *, button* __ )
Insert a button in a toolbar control.

#### Parameters


  -  *nID* : int

    Zero-based index of a button. This function inserts the new button to the left of this button.

  -  *button* : __PyCToolBarCtrl::TBBUTTON__ 

    Bitmap containing button to be inserted

#### Comments
The image and/or string whose index you provide must have 

previously been added to the toolbar control's list using[PyCToolBarCtrl::AddBitmap](PyCToolBarCtrl.md#pyctoolbarctrladdbitmap), __PyCToolBarCtrl::AddString__ , 

and/or[PyCToolBarCtrl::AddStrings](PyCToolBarCtrl.md#pyctoolbarctrladdstrings).

#### MFC References


  - CToolBarCtrl::InsertButton

## [PyCToolBarCtrl](#pyctoolbarctrl).IsButtonChecked

int = __IsButtonChecked( *nID* __ )
Determine whether the specified button in a toolbar control is checked.

#### Parameters


  -  *nID* : int

    ID of the button to check.

#### MFC References


  - CToolBarCtrl::IsButtonChecked

## [PyCToolBarCtrl](#pyctoolbarctrl).IsButtonEnabled

int = __IsButtonEnabled( *nID* __ )
Determine whether the specified button in a toolbar control is enabled.

#### Parameters


  -  *nID* : int

    ID of the button to check.

#### MFC References


  - CToolBarCtrl::IsButtonEnabled

## [PyCToolBarCtrl](#pyctoolbarctrl).IsButtonHidden

int = __IsButtonHidden( *nID* __ )
Determine whether the specified button in a toolbar control is hidden.

#### Parameters


  -  *nID* : int

    ID of the button to check.

#### MFC References


  - CToolBarCtrl::IsButtonHidden

## [PyCToolBarCtrl](#pyctoolbarctrl).IsButtonIndeterminate

int = __IsButtonIndeterminate( *nID* __ )
Determine whether the specified button in a toolbar control is indeterminate.

#### Parameters


  -  *nID* : int

    ID of the button to check.

#### MFC References


  - CToolBarCtrl::IsButtonIndeterminate

## [PyCToolBarCtrl](#pyctoolbarctrl).IsButtonPressed

int = __IsButtonPressed( *nID* __ )
Determine whether the specified button in a toolbar control is pressed.

#### Parameters


  -  *nID* : int

    ID of the button to check.

#### MFC References


  - CToolBarCtrl::IsButtonPressed

## [PyCToolBarCtrl](#pyctoolbarctrl).PressButton

 __PressButton( *nID*  *, bEnable* __ )
Mark or unmark the specified button as pressed.

#### Parameters


  -  *nID* : int

    ID of the button to mark.

  -  *bEnable=1* : int

    1 to mark, 0 to unmark.

#### MFC References


  - CToolBarCtrl::PressButton

## [PyCToolBarCtrl](#pyctoolbarctrl).SetBitmapSize

 __SetBitmapSize( *width*  *, height* __ )
Set the size of the actual bitmapped images to be added to a toolbar control.

#### Parameters


  -  *width=16* : int

    Width of bitmap images.

  -  *height=15* : int

    Height of bitmap images.

#### Alternative Parameters


  -  *width* 

    Width of bitmap images.

  -  *height* 

    Height of bitmap images.

#### MFC References


  - CToolBarCtrl::SetBitmapSize

## [PyCToolBarCtrl](#pyctoolbarctrl).SetButtonSize

 __SetButtonSize( *width*  *, height* __ )
Set the size of the buttons to be added to a toolbar control.

#### Parameters


  -  *width=16* : int

    Width of buttons

  -  *height=15* : int

    Height of buttons

#### Alternative Parameters


  -  *width* 

    Width of bitmap images.

  -  *height* 

    Height of bitmap images.

#### MFC References


  - CToolBarCtrl::SetButtonSize

## [PyCToolBarCtrl](#pyctoolbarctrl).SetCmdID

 __SetCmdID( *nIndex*  *, nID* __ )
Set the command identifier which will be sent to the owner window when the specified button is pressed.

#### Parameters


  -  *nIndex* : int

    The zero-based index of the button whose command ID is to be set.

  -  *nID* : int

    The command ID to set the selected button to.

#### MFC References


  - CToolBarCtrl::SetCmdID

## [PyCToolBarCtrl](#pyctoolbarctrl).SetRows

left, top, right, bottom = __SetRows( *nRows*  *, bLarger* __ )
Ask the toolbar control to resize itself to the requested number of rows.

#### Parameters


  -  *nRows* : int

    Requested number of rows.

  -  *bLarger* : int

    Tells whether to use more rows or fewer rows if the toolbar cannot be resized to the requested number of rows.

#### MFC References


  - CToolBarCtrl::SetRows

## [PyCToolBarCtrl](#pyctoolbarctrl).TBUTTON tuple

 __TBUTTON tuple( *iBitmap*  *, idCommand*  *, fsState*  *, fsStyle*  *, userob*  *, iString* __ )
Describes a TBUTTON tuple, used by the PyCToolBarCtrl AddButtons method

#### Parameters


  -  *iBitmap* : int

    Zero-based index of button image

  -  *idCommand* : int

    Command to be sent when button pressed

  -  *fsState* : int

    Button state. Can be any of the TBSTATE values defined in win32con

  -  *fsStyle* : int

    Button style. Can be any of the TBSTYLE values defined in win32con

  -  *userob* : object

    Arbitrary Python object

  -  *iString* : int

    Zero-based index of button label string

#### Comments
Userob is any Python object at all, but no reference count is kept, so you must ensure the object remains referenced throughout.