# PyCTreeView


## PyCTreeView Object

A class which implementes a CTreeView\.  Derived from [PyCView](PyCView.md) and [PyCTreeCtrl](PyCTreeCtrl.md) objects\.

#### Methods

  - [PreCreateWindow](PyCTreeView.md#pyctreeviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [GetTreeCtrl](PyCTreeView.md#pyctreeviewgettreectrl)

    Returns the underlying tree control object\.&nbsp;

  - [OnCommand](PyCTreeView.md#pyctreeviewoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;




## [PyCTreeView](PyCTreeView.md#pyctreeview)\.GetTreeCtrl

[PyCTreeCtrl](PyCTreeCtrl.md) = GetTreeCtrl\(\)
Returns the underlying tree control object\.


## [PyCTreeView](PyCTreeView.md#pyctreeview)\.OnCommand

OnCommand\(wparam, lparam\)
Calls the standard Python framework OnCommand handler

#### Parameters

  - wparam : int

    

  - lparam : int

    

#### See Also

  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual) virtual method


## [PyCTreeView](PyCTreeView.md#pyctreeview)\.PreCreateWindow

tuple = PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters

  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.