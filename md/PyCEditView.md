# PyCEditView


## PyCEditView Object

A class which implementes a CView of a text file\.  Derived from [PyCView](PyCView.md) and [PyCEdit](PyCEdit.md) objects\.

#### Methods

  - [IsModified](PyCEditView.md#pyceditviewismodified)

    Indicates if the view's document is modified\.&nbsp;

  - [LoadFile](PyCEditView.md#pyceditviewloadfile)

    Loads a named file into the view\.&nbsp;

  - [SetModifiedFlag](PyCEditView.md#pyceditviewsetmodifiedflag)

    Sets the view's document modified flag\.&nbsp;

  - [GetEditCtrl](PyCEditView.md#pyceditviewgeteditctrl)

    Returns the underlying [PyCEdit](PyCEdit.md) object&nbsp;

  - [PreCreateWindow](PyCEditView.md#pyceditviewprecreatewindow)

    Calls the underlying MFC PreCreateWindow method\.&nbsp;

  - [SaveFile](PyCEditView.md#pyceditviewsavefile)

    Saves the view to a named file\.&nbsp;

  - [OnCommand](PyCEditView.md#pyceditviewoncommand)

    Calls the standard Python framework OnCommand handler&nbsp;




## [PyCEditView](PyCEditView.md#pyceditview)\.GetEditCtrl

PyCEditCtrl

 = GetEditCtrl\(\)
returns the underlying edit control object\.


## [PyCEditView](PyCEditView.md#pyceditview)\.IsModified

int = IsModified\(\)
Indicates if the view's document has the modified flag set\.


## [PyCEditView](PyCEditView.md#pyceditview)\.LoadFile

LoadFile\(fileName\)
Loads a file into the view\.

#### Parameters

  - fileName : string

    The name of the file to be loaded\.


## [PyCEditView](PyCEditView.md#pyceditview)\.OnCommand

OnCommand\(wparam, lparam\)
Calls the standard Python framework OnCommand handler

#### Parameters

  - wparam : int

    

  - lparam : int

    

#### See Also

  - [PyCWnd\.OnCommand](PyCWnd.md#pycwndoncommand_virtual) virtual method


## [PyCEditView](PyCEditView.md#pyceditview)\.PreCreateWindow

tuple = PreCreateWindow\(createStruct\)
Calls the underlying MFC PreCreateWindow method\.

#### Parameters

  - createStruct : tuple

    A tuple representing a CREATESTRUCT structure\.


## [PyCEditView](PyCEditView.md#pyceditview)\.SaveFile

SaveFile\(fileName\)
Saves the view to a file\.

#### Parameters

  - fileName : string

    The name of the file to be written\.


## [PyCEditView](PyCEditView.md#pyceditview)\.SetModifiedFlag

SetModifiedFlag\(bModified\)
Sets the modified flag for the view's document\.

#### Parameters

  - bModified=1 : int

    The modified state to set\.