# PyCSplitterWnd

## PyCSplitterWnd Object

A class which encapsulates an MFC __CSplitterWnd__ . Derived from a[PyCWnd](#pycwnd)object.

#### Methods


  - [GetPane](PyCSplitterWnd.md#pycsplitterwndgetpane)

    Returns the[PyCWnd](#pycwnd)object associated with a splitter window pane.&nbsp;

  - [CreateView](PyCSplitterWnd.md#pycsplitterwndcreateview)

    Creates a view in a splitter window&nbsp;

  - [CreateStatic](PyCSplitterWnd.md#pycsplitterwndcreatestatic)

    Creates a static splitter window.&nbsp;

  - [SetColumnInfo](PyCSplitterWnd.md#pycsplitterwndsetcolumninfo)

    Sets a new minimum height and ideal height for a column&nbsp;

  - [SetRowInfo](PyCSplitterWnd.md#pycsplitterwndsetrowinfo)

    Sets a new minimum height and ideal height for a row.&nbsp;

  - [IdFromRowCol](PyCSplitterWnd.md#pycsplitterwndidfromrowcol)

    Gets the child window ID for the specified child.&nbsp;

  - [DoKeyboardSplit](PyCSplitterWnd.md#pycsplitterwnddokeyboardsplit)

    &nbsp;

## [PyCSplitterWnd](#pycsplitterwnd).CreateStatic

 __CreateStatic( *parent*  *, rows*  *, cols*  *, style*  *, id* __ )
Creates a static splitter window.

#### Parameters


  -  *parent* :[PyCFrameWnd](#pycframewnd)or __PyCSplitter__ 

    The parent window.

  -  *rows* : int

    The number of rows in the splitter.

  -  *cols* : int

    The number of columns in the splitter.

  -  *style=WS_CHILD | WS_VISIBLE* : int

    Specifies the window style

  -  *id=AFX_IDW_PANE_FIRST* : int

    The child window ID of the window. The ID can be AFX_IDW_PANE_FIRST unless the splitter window is nested inside another splitter window.

#### Comments
A static splitter window is a splitter where the number of panes are 

fixed at window creation time.  Currently this is the only splitter window 

supported by win32ui.

#### MFC References


  - CSplitterWnd::CreateStatic

## [PyCSplitterWnd](#pycsplitterwnd).CreateView

 __CreateView( *view*  *, row*  *, col*  *, width, height* __ )
Creates a view in a splitter window

#### Parameters


  -  *view* :[PyCView](#pycview)

    The view to place in the splitter pane.

  -  *row* : int

    The row in the splitter to place the view.

  -  *col* : int

    The column in the splitter to place the view.

  -  *width, height* : (int, int)

    The initial size of the new view.

#### MFC References


  - CSplitterWnd::CreateView 

exception set.

## [PyCSplitterWnd](#pycsplitterwnd).DoKeyboardSplit

int = __DoKeyboardSplit(__ )


## [PyCSplitterWnd](#pycsplitterwnd).GetPane

[PyCWnd](#pycwnd)= __GetPane( *row*  *, col* __ )
Returns the[PyCView](#pycview)associated with the specified pane.

#### Parameters


  -  *row* : int

    The row in the splitter.

  -  *col* : int

    The column in the splitter.

#### Comments
Theoretically the return value can be a[PyCWnd](#pycwnd)object, but currently it 

will always be a[PyCView](#pycview)or derived object.

## [PyCSplitterWnd](#pycsplitterwnd).IdFromRowCol

 __IdFromRowCol( *row*  *, col* __ )
Gets the child window ID for the specified child.

#### Parameters


  -  *row* : int

    The row in the splitter.

  -  *col* : int

    The col in the splitter

## [PyCSplitterWnd](#pycsplitterwnd).SetColumnInfo

 __SetColumnInfo( *column*  *, ideal*  *, min* __ )
Sets a new minimum height and ideal height for a column

#### Parameters


  -  *column* : int

    The column in the splitter.

  -  *ideal* : int

    Specifies an ideal height for the splitter window column in pixels.

  -  *min* : int

    Specifies a minimum height for the splitter window column in pixels.

## [PyCSplitterWnd](#pycsplitterwnd).SetRowInfo

 __SetRowInfo( *row*  *, ideal*  *, min* __ )
Sets a new minimum height and ideal height for a row.

#### Parameters


  -  *row* : int

    The row in the splitter.

  -  *ideal* : int

    Specifies an ideal height for the splitter window row in pixels.

  -  *min* : int

    Specifies a minimum height for the splitter window row in pixels.