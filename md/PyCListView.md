# PyCListView

## PyCListView Object

A class which implementes a CListView\.  Derived from[PyCView](#pycview)and[PyCListCtrl](#pyclistctrl)objects\.

#### Methods


  - [PreCreateWindow](PyCListView.md#pyclistviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [GetListCtrl](PyCListView.md#pyclistviewgetlistctrl)

    Returns the underlying list control object\.&nbsp;

  - [OnCommand](PyCListView.md#pyclistviewoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;


## [PyCListView](#pyclistview)\.GetListCtrl

[PyCListCtrl](#pyclistctrl)\= **GetListCtrl\(** \)
Returns the underlying list control object\.

## [PyCListView](#pyclistview)\.OnCommand

 **OnCommand\( *wparam*  *, lparam* ** \)
Calls the standard Python framework OnCommand handler

#### Parameters


  -  *wparam* : int

    

  -  *lparam* : int

    

#### See Also


  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual)virtual method

## [PyCListView](#pyclistview)\.PreCreateWindow

tuple \= **PreCreateWindow\( *createStruct* ** \)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters


  -  *createStruct* : tuple

    A tuple representing a CREATESTRUCT structure\.