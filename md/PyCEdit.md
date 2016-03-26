# PyCEdit

## PyCEdit Object



A windows edit control\.  Encapsulates an MFCCEdit



 class\.  Derived from a[PyCControl](#pyccontrol) object\.

#### Methods


  - [CreateWindow](PyCEdit.md#pyceditcreatewindow)

    Creates the window for a new edit object\.&nbsp;

  - [Clear](PyCEdit.md#pyceditclear)

    Clears all text from an edit control\.&nbsp;

  - [Copy](PyCEdit.md#pyceditcopy)

    Copy the selection to the clipboard\.&nbsp;

  - [Cut](PyCEdit.md#pyceditcut)

    Cut the selection, and place it in the clipboard\.&nbsp;

  - [FmtLines](PyCEdit.md#pyceditfmtlines)

    Change the formatting options for the edit control&nbsp;

  - [GetFirstVisibleLine](PyCEdit.md#pyceditgetfirstvisibleline)

    Returns zero-based index of the topmost visible line\.&nbsp;

  - [GetSel](PyCEdit.md#pyceditgetsel)

    Returns the selection\.&nbsp;

  - [GetLine](PyCEdit.md#pyceditgetline)

    Returns a specified line\.&nbsp;

  - [GetLineCount](PyCEdit.md#pyceditgetlinecount)

    Returns the number of lines in an edit control\.&nbsp;

  - [LimitText](PyCEdit.md#pyceditlimittext)

    Sets max length of text that user can enter&nbsp;

  - [LineFromChar](PyCEdit.md#pyceditlinefromchar)

    Returns the line number of a given character\.&nbsp;

  - [LineIndex](PyCEdit.md#pyceditlineindex)

    Returns the line index&nbsp;

  - [LineScroll](PyCEdit.md#pyceditlinescroll)

    Scroll the control vertically and horizontally&nbsp;

  - [Paste](PyCEdit.md#pyceditpaste)

    Pastes the contents of the clipboard into the edit control\.&nbsp;

  - [ReplaceSel](PyCEdit.md#pyceditreplacesel)

    Replace the selection with the specified text\.&nbsp;

  - [SetReadOnly](PyCEdit.md#pyceditsetreadonly)

    Set the read only status of an edit control\.&nbsp;

  - [SetSel](PyCEdit.md#pyceditsetsel)

    Changes the selection in an edit control\. 

sentinel&nbsp;

## [PyCEdit](#pycedit)\.Clear



int =Clear\(\)
Clears all text in an edit control\.

#### MFC References


  - CEdit::Clear

## [PyCEdit](#pycedit)\.Copy

Copy\(\)
Copys the current selection to the clipboard\.

#### MFC References


  - CEdit::Copy

## [PyCEdit](#pycedit)\.CreateWindow

CreateWindow\(style, rect, parent, id\)
Creates the window for a new Edit object\.

#### Parameters


  - style : int

    The style for the Edit\.  Use any of the win32con\.BS\_\* constants\.

  - rect : \(left, top, right, bottom\)

    The size and position of the Edit\.

  - parent :[PyCWnd](#pycwnd)

    The parent window of the Edit\.  Usually a[PyCDialog](#pycdialog)\.

  - id : int

    The Edits control ID\.

## [PyCEdit](#pycedit)\.Cut

Cut\(\)
Cuts the current selection to the clipboard\.

#### MFC References


  - CEdit::Cut

## [PyCEdit](#pycedit)\.FmtLines



int =FmtLines\(bAddEOL\)
Sets the formatting options for the control\.

#### Parameters


  - bAddEOL : int

    Specifies whether soft line-break characters are to be inserted\. 

A value of TRUE inserts the characters; a value of FALSE removes them\.

#### MFC References


  - CEdit::FmtLines

#### Return Value
Nonzero if any formatting occurs; otherwise 0\.

## [PyCEdit](#pycedit)\.GetFirstVisibleLine



int =GetFirstVisibleLine\(\)
Returns zero-based index of the topmost visible line\.

#### MFC References


  - CEdit::GetFirstVisibleLine

#### Return Value
The zero-based index of the topmost visible line\. For single-line edit controls, the return value is 0\.

## [PyCEdit](#pycedit)\.GetLine



int =GetLine\(lineNo\)
Returns the text in a specified line\.

#### Parameters


  - lineNo=current : int

    Contains the zero-based index value for the desired line\.

#### Comments


This function is not an MFC wrapper\.

## [PyCEdit](#pycedit)\.GetLineCount



int =GetLineCount\(\)
Gets the number of lines in an edit control\.

#### MFC References


  - CEdit::GetLineCount

#### Return Value
The number of lines in the buffer\.  If the control is empty, the return value is 1\.

## [PyCEdit](#pycedit)\.GetSel



\(start, end\) =GetSel\(\)
Returns the start and end of the current selection\.

#### MFC References


  - CEdit::GetSel

#### Return Value
The return tuple is \(the first character in the current selection, first nonselected character past the end of the current selection\)

## [PyCEdit](#pycedit)\.LimitText

LimitText\(nChars\)
Sets max length of text that user can enter

#### Parameters


  - nChars=0 : int

    Specifies the length \(in bytes\) of the text that the user can enter\. If this parameter is 0, the text length is set to 

UINT\_MAX bytes\. This is the default behavior\.

#### MFC References


  - CEdit::LimitText

## [PyCEdit](#pycedit)\.LineFromChar



int =LineFromChar\(charNo\)
Returns the line number of the specified character\.

#### Parameters


  - charNo=-1 : int

    Contains the zero-based index value for the desired character in the text of the edit 

control, or -1\.  If -1, then it specifies the current line\.

#### MFC References


  - CEdit::LineFromChar

#### Return Value
The zero-based line number of the line containing the character index specified by charNo\. 

If charNo is -1, the number of the line that contains the first character of the selection is returned\. 

If there is no selection, the current line number is returned\.

## [PyCEdit](#pycedit)\.LineIndex



int =LineIndex\(lineNo\)
Retrieves the character index of a line within a multiple-line edit control\.

#### Parameters


  - lineNo=-1 : int

    Contains the index value for the desired line in the text 

of the edit control, or contains -1\.  If -1, then it specifies the current line\.

#### Comments


This method only works on multi-linr edit controls\.

#### MFC References


  - CEdit::LineIndex

#### Return Value
The character index of the line specified in lineNo, or -1 if 

the specified line number is greater then the number of lines in 

the edit control\.

## [PyCEdit](#pycedit)\.LineScroll



int =LineScroll\(nLines, nChars\)
Scroll the control vertically and horizontally

#### Parameters


  - nLines : int

    Specifies the number of lines to scroll vertically\.

  - nChars=0 : int

    Specifies the number of character positions to scroll horizontally\. This value is ignored if the edit control has either the 

ES\_RIGHT or ES\_CENTER style\.

#### Comments


This method only works on multi-linr edit controls\.

#### MFC References


  - CEdit::LineScroll

## [PyCEdit](#pycedit)\.Paste

Paste\(\)
Pastes the contents of the clipboard into the control\.

#### MFC References


  - CEdit::Paste

## [PyCEdit](#pycedit)\.ReplaceSel

ReplaceSel\(text\)
Replaces the selection with the specified text\.

#### Parameters


  - text : string

    The text to replace the selection with\.

#### MFC References


  - CEdit::ReplaceSel

## [PyCEdit](#pycedit)\.SetReadOnly

SetReadOnly\(bReadOnly\)
Sets or clears the read-only status of the listbox\.

#### Parameters


  - bReadOnly=1 : int

    The read-only state to set\.

#### MFC References


  - CEdit::SetReadOnly

## [PyCEdit](#pycedit)\.SetSel

SetSel\(start, end, bNoScroll\)
Sets the selection in the edit control\.

#### Parameters


  - start : int

    Specifies the starting position\. 

If start is 0 and end is -1, all the text in the edit control is selected\. 

If start is -1, any current selection is removed\.

  - end=start : int

    Specifies the ending position\.

  - bNoScroll=0 : int

    Indicates whether the caret should be scrolled into view\. If 0, the caret is scrolled into view\. If 1, the caret is not scrolled into view\.

#### Alternative Parameters


  - start,end\)

    As for normal start, end args\.

  - bNoScroll

    Indicates whether the caret should be scrolled into view\. If 0, the caret is scrolled into view\. If 1, the caret is not scrolled into view\.

#### MFC References


  - CEdit::SetSel