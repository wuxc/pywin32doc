# PyCSliderCtrl

## PyCSliderCtrl Object

A windows Slider bar control\.  Encapsulates an MFC **CSliderCtrl** class\.  Derived from[PyCControl](#pyccontrol)\.

#### Methods


  - [CreateWindow](PyCSliderCtrl.md#pycsliderctrlcreatewindow)

    Creates the window for a new Slider bar object\.&nbsp;

  - [GetLineSize](PyCSliderCtrl.md#pycsliderctrlgetlinesize)

    Get the control's line size&nbsp;

  - [SetLineSize](PyCSliderCtrl.md#pycsliderctrlsetlinesize)

    Set the control's line size&nbsp;

  - [GetPageSize](PyCSliderCtrl.md#pycsliderctrlgetpagesize)

    Get the control's Page size&nbsp;

  - [SetPageSize](PyCSliderCtrl.md#pycsliderctrlsetpagesize)

    Set the control's Page size&nbsp;

  - [GetRangeMax](PyCSliderCtrl.md#pycsliderctrlgetrangemax)

    Get the control's maximum&nbsp;

  - [GetRangeMin](PyCSliderCtrl.md#pycsliderctrlgetrangemin)

    Get the control's minimum&nbsp;

  - [GetRange](PyCSliderCtrl.md#pycsliderctrlgetrange)

    Get the control's minimum and maximum&nbsp;

  - [GetRangeMax](PyCSliderCtrl.md#pycsliderctrlgetrangemax)

    Set the control's maximum&nbsp;

  - [GetRangeMin](PyCSliderCtrl.md#pycsliderctrlgetrangemin)

    Set the control's minimum&nbsp;

  - [SetRange](PyCSliderCtrl.md#pycsliderctrlsetrange)

    Set the control's minimum and maximum&nbsp;

  - [GetSelection](PyCSliderCtrl.md#pycsliderctrlgetselection)

    Get the selection start and end positions&nbsp;

  - [SetSelection](PyCSliderCtrl.md#pycsliderctrlsetselection)

    Set the selection start and end positions&nbsp;

  - [GetChannelRect](PyCSliderCtrl.md#pycsliderctrlgetchannelrect)

    Get the control's channel rect&nbsp;

  - [GetThumbRect](PyCSliderCtrl.md#pycsliderctrlgetthumbrect)

    Get the control's thumb rect&nbsp;

  - [GetPos](PyCSliderCtrl.md#pycsliderctrlgetpos)

    Get the control's position&nbsp;

  - [SetPos](PyCSliderCtrl.md#pycsliderctrlsetpos)

    Set the control's position&nbsp;

  - [GetNumTics](PyCSliderCtrl.md#pycsliderctrlgetnumtics)

    Get the number of tics in the control&nbsp;

  - [GetTicArray](PyCSliderCtrl.md#pycsliderctrlgetticarray)

    Get the array of tic positions&nbsp;

  - [GetTic](PyCSliderCtrl.md#pycsliderctrlgettic)

    Get the position of the specified tic&nbsp;

  - [GetTicPos](PyCSliderCtrl.md#pycsliderctrlgetticpos)

    Get the position of the specified tic in client coordinates&nbsp;

  - [SetTic](PyCSliderCtrl.md#pycsliderctrlsettic)

    Set a tick at the position&nbsp;

  - [SetTicFreq](PyCSliderCtrl.md#pycsliderctrlsetticfreq)

    Set the tic mark frequency&nbsp;

  - [ClearSel](PyCSliderCtrl.md#pycsliderctrlclearsel)

    Clear any control selection&nbsp;

  - [VerifyPos](PyCSliderCtrl.md#pycsliderctrlverifypos)

    Verify the positon between min and max&nbsp;

  - [ClearTics](PyCSliderCtrl.md#pycsliderctrlcleartics)

    Clear any tic marks from the control&nbsp;

## [PyCSliderCtrl](#pycsliderctrl)\.ClearSel

int \= **ClearSel\( *bRedraw* ** \)
Clear the selection

#### Parameters


  -  *bRedraw\=1* : int

    Redraw the control?

## [PyCSliderCtrl](#pycsliderctrl)\.ClearTics

int \= **ClearTics\( *bRedraw* ** \)
Clear the control's tic marks

#### Parameters


  -  *bRedraw\=1* : int

    Redraw the control?

## [PyCSliderCtrl](#pycsliderctrl)\.CreateWindow

 **CreateWindow\( *style*  *, rect*  *, parent*  *, id* ** \)
Creates the actual control\.

#### Parameters


  -  *style* : int

    The style for the control\.

  -  *rect* : \(left, top, right, bottom\)

    The size and position of the control\.

  -  *parent* :[PyCWnd](#pycwnd)

    The parent window of the control\.  Usually a[PyCDialog](#pycdialog)\.

  -  *id* : int

    The control's ID\.

## [PyCSliderCtrl](#pycsliderctrl)\.GetChannelRect

int \= **GetChannelRect\(** \)
Get the control's channel rectangle

## [PyCSliderCtrl](#pycsliderctrl)\.GetLineSize

int \= **GetLineSize\(** \)
Get the control's position

## [PyCSliderCtrl](#pycsliderctrl)\.GetNumTics

int \= **GetNumTics\(** \)
Get number of tics in the slider

## [PyCSliderCtrl](#pycsliderctrl)\.GetPageSize

int \= **GetPageSize\(** \)
Get the control's position

## [PyCSliderCtrl](#pycsliderctrl)\.GetPos

int \= **GetPos\(** \)
Get the control's position

## [PyCSliderCtrl](#pycsliderctrl)\.GetRange

int \= **GetRange\(** \)
Get the control's min and max

## [PyCSliderCtrl](#pycsliderctrl)\.GetRangeMax

int \= **GetRangeMax\(** \)
Get the control's Maximum

## [PyCSliderCtrl](#pycsliderctrl)\.GetRangeMin

int \= **GetRangeMin\(** \)
Get the control's Minimum

## [PyCSliderCtrl](#pycsliderctrl)\.GetSelection

int \= **GetSelection\(** \)
Get the control's selection start and end positions

## [PyCSliderCtrl](#pycsliderctrl)\.GetThumbRect

int \= **GetThumbRect\(** \)
Get the control's thumb rectangle

## [PyCSliderCtrl](#pycsliderctrl)\.GetTic

int \= **GetTic\( *nTic* ** \)
Get the position of the specified tic number

#### Parameters


  -  *nTic\=1* : int

    Zero based index of the tic mark

## [PyCSliderCtrl](#pycsliderctrl)\.GetTicArray

int \= **GetTicArray\(** \)
Get a tuple of slider tic positions

## [PyCSliderCtrl](#pycsliderctrl)\.GetTicPos

int \= **GetTicPos\( *nTic* ** \)
Get the position of the specified tic number in client coordinates

#### Parameters


  -  *nTic\=1* : int

    Zero based index of the tic mark

## [PyCSliderCtrl](#pycsliderctrl)\.SetLineSize

int \= **SetLineSize\( *nLineSize* ** \)
Set the control's line size\.  Returns the previous line size\.

#### Parameters


  -  *nLineSize\=1* : int

    New line size of the Slider bar control

## [PyCSliderCtrl](#pycsliderctrl)\.SetPageSize

int \= **SetPageSize\( *nPageSize* ** \)
Set the control's page size  Returns the previous page size\.

#### Parameters


  -  *nPageSize\=1* : int

    New page size of the Slider bar control\.

## [PyCSliderCtrl](#pycsliderctrl)\.SetPos

int \= **SetPos\( *nPos* ** \)
Set the control's position

#### Parameters


  -  *nPos\=1* : int

    New position of the Slider bar control\.

## [PyCSliderCtrl](#pycsliderctrl)\.SetRange

int \= **SetRange\( *nRangeMin*  *, nRangeMax*  *, bRedraw* ** \)
Set the control's min and max

#### Parameters


  -  *nRangeMin\=1* : int

    New minimum of the Slider bar control\.

  -  *nRangeMax\=1* : int

    New maximum of the Slider bar control\.

  -  *bRedraw\=1* : int

    Should slider be redrawn?

## [PyCSliderCtrl](#pycsliderctrl)\.SetRangeMax

int \= **SetRangeMax\( *nRangeMax*  *, bRedraw* ** \)
Set the control's maximum

#### Parameters


  -  *nRangeMax\=1* : int

    New maximum of the Slider bar control\.

  -  *bRedraw\=1* : int

    Should slider be redrawn?

## [PyCSliderCtrl](#pycsliderctrl)\.SetRangeMin

int \= **SetRangeMin\( *nRangeMin*  *, bRedraw* ** \)
Set the control's minimum

#### Parameters


  -  *nRangeMin\=1* : int

    New minimum of the Slider bar control\.

  -  *bRedraw\=1* : int

    Should slider be redrawn?

## [PyCSliderCtrl](#pycsliderctrl)\.SetSelection

int \= **SetSelection\( *nRangeMin*  *, nRangeMax* ** \)
Set the control's selection start and end positions

#### Parameters


  -  *nRangeMin\=1* : int

    New start of the Slider's selection\.

  -  *nRangeMax\=1* : int

    New end of the Slider's selection\.

## [PyCSliderCtrl](#pycsliderctrl)\.SetTic

int \= **SetTic\( *nTic* ** \)
Set a tic at the specified position

#### Parameters


  -  *nTic\=1* : int

    Position of the desired tic mark

## [PyCSliderCtrl](#pycsliderctrl)\.SetTicFreq

int \= **SetTicFreq\( *nFreq* ** \)
Set the tic frequency

#### Parameters


  -  *nFreq\=1* : int

    Frequency of tic marks

## [PyCSliderCtrl](#pycsliderctrl)\.VerifyPos

int \= **VerifyPos\(** \)
Verify the position is between configured min and max