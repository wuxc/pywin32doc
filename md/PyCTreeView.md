# PyCTreeView

## PyCTreeView Object

A class which implementes a CTreeView\.  Derived from[PyCView](#pycview)and[PyCTreeCtrl](#pyctreectrl)objects\.

#### Methods


  - [PreCreateWindow](PyCTreeView.md#pyctreeviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [GetTreeCtrl](PyCTreeView.md#pyctreeviewgettreectrl)

    Returns the underlying tree control object\.&nbsp;

  - [OnCommand](PyCTreeView.md#pyctreeviewoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;


## [PyCTreeView](#pyctreeview)\.GetTreeCtrl

[PyCTreeCtrl](#pyctreectrl)\= **GetTreeCtrl\(** \)
Returns the underlying tree control object\.

## [PyCTreeView](#pyctreeview)\.OnCommand

 **OnCommand\( *wparam*  *, lparam* ** \)
Calls the standard Python framework OnCommand handler

#### Parameters


  -  *wparam* : int

    

  -  *lparam* : int

    

#### See Also


  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual)virtual method

## [PyCTreeView](#pyctreeview)\.PreCreateWindow

tuple \= **PreCreateWindow\( *createStruct* ** \)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters


  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure\.