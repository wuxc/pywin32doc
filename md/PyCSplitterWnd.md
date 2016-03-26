# PyCSplitterWnd


## PyCSplitterWnd Object

A class which encapsulates an MFC CSplitterWnd

\. Derived from a [PyCWnd](PyCWnd.md) object\.

#### Methods

  - [GetPane](PyCSplitterWnd.md#pycsplitterwndgetpane)

    Returns the [PyCWnd](PyCWnd.md) object associated with a splitter window pane\.&nbsp;

  - [CreateView](PyCSplitterWnd.md#pycsplitterwndcreateview)

    Creates a view in a splitter window&nbsp;

  - [CreateStatic](PyCSplitterWnd.md#pycsplitterwndcreatestatic)

    Creates a static splitter window\.&nbsp;

  - [SetColumnInfo](PyCSplitterWnd.md#pycsplitterwndsetcolumninfo)

    Sets a new minimum height and ideal height for a column&nbsp;

  - [SetRowInfo](PyCSplitterWnd.md#pycsplitterwndsetrowinfo)

    Sets a new minimum height and ideal height for a row\.&nbsp;

  - [IdFromRowCol](PyCSplitterWnd.md#pycsplitterwndidfromrowcol)

    Gets the child window ID for the specified child\.&nbsp;

  - [DoKeyboardSplit](PyCSplitterWnd.md#pycsplitterwnddokeyboardsplit)

    &nbsp;


## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.CreateStatic

CreateStatic\(parent, rows, cols, style, id\)
Creates a static splitter window\.

#### Parameters

  - parent : [PyCFrameWnd](PyCFrameWnd.md) or PyCSplitter

    The parent window\.

  - rows : int

    The number of rows in the splitter\.

  - cols : int

    The number of columns in the splitter\.

  - style=WS\_CHILD | WS\_VISIBLE : int

    Specifies the window style

  - id=AFX\_IDW\_PANE\_FIRST : int

    The child window ID of the window\. The ID can be AFX\_IDW\_PANE\_FIRST unless the splitter window is nested inside another splitter window\.

#### Comments

A static splitter window is a splitter where the number of panes are 

fixed at window creation time\.  Currently this is the only splitter window 

supported by win32ui\.

#### MFC References

  - CSplitterWnd::CreateStatic


## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.CreateView

CreateView\(view, row, col, width, height\)
Creates a view in a splitter window

#### Parameters

  - view : [PyCView](PyCView.md)

    The view to place in the splitter pane\.

  - row : int

    The row in the splitter to place the view\.

  - col : int

    The column in the splitter to place the view\.

  - width, height : \(int, int\)

    The initial size of the new view\.

#### MFC References

  - CSplitterWnd::CreateView 

exception set\.


## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.DoKeyboardSplit

int = DoKeyboardSplit\(\)



## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.GetPane

[PyCWnd](PyCWnd.md) = GetPane\(row, col

\)
Returns the [PyCView](PyCView.md) associated with the specified pane\.

#### Parameters

  - row : int

    The row in the splitter\.

  - col : int

    The column in the splitter\.

#### Comments

Theoretically the return value can be a [PyCWnd](PyCWnd.md) object, but currently it 

will always be a [PyCView](PyCView.md) or derived object\.


## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.IdFromRowCol

IdFromRowCol\(row, col\)
Gets the child window ID for the specified child\.

#### Parameters

  - row : int

    The row in the splitter\.

  - col : int

    The col in the splitter


## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.SetColumnInfo

SetColumnInfo\(column, ideal, min\)
Sets a new minimum height and ideal height for a column

#### Parameters

  - column : int

    The column in the splitter\.

  - ideal : int

    Specifies an ideal height for the splitter window column in pixels\.

  - min : int

    Specifies a minimum height for the splitter window column in pixels\.


## [PyCSplitterWnd](PyCSplitterWnd.md#pycsplitterwnd)\.SetRowInfo

SetRowInfo\(row, ideal, min\)
Sets a new minimum height and ideal height for a row\.

#### Parameters

  - row : int

    The row in the splitter\.

  - ideal : int

    Specifies an ideal height for the splitter window row in pixels\.

  - min : int

    Specifies a minimum height for the splitter window row in pixels\.