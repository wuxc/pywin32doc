# PyCListView


## PyCListView Object

A class which implementes a CListView\.  Derived from [PyCView](PyCView.md) and [PyCListCtrl](PyCListCtrl.md) objects\.

#### Methods

  - [PreCreateWindow](PyCListView.md#pyclistviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [GetListCtrl](PyCListView.md#pyclistviewgetlistctrl)

    Returns the underlying list control object\.&nbsp;

  - [OnCommand](PyCListView.md#pyclistviewoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;




## [PyCListView](PyCListView.md#pyclistview)\.GetListCtrl

[PyCListCtrl](PyCListCtrl.md) = GetListCtrl\(\)
Returns the underlying list control object\.


## [PyCListView](PyCListView.md#pyclistview)\.OnCommand

OnCommand\(wparam, lparam\)
Calls the standard Python framework OnCommand handler

#### Parameters

  - wparam : int

    

  - lparam : int

    

#### See Also

  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual) virtual method


## [PyCListView](PyCListView.md#pyclistview)\.PreCreateWindow

tuple = PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters

  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.