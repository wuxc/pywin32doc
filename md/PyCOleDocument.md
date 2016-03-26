# PyCOleDocument

## PyCOleDocument Object

An OLE document class\.  Encapsulates an MFC **COleDocument** class

#### Methods


  - [EnableCompoundFile](PyCOleDocument.md#pycoledocumentenablecompoundfile)

    Call this function if you want to store the document using the compound-file format&nbsp;

  - [GetStartPosition](PyCOleDocument.md#pycoledocumentgetstartposition)

    Obtains the position of the first item in the document\.&nbsp;

  - [GetNextItem](PyCOleDocument.md#pycoledocumentgetnextitem)

    Call this function repeatedly to access each of the items in your document\.&nbsp;

  - [GetInPlaceActiveItem](PyCOleDocument.md#pycoledocumentgetinplaceactiveitem)

    Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd\. 

sentinel&nbsp;

## [PyCOleDocument](#pycoledocument)\.EnableCompoundFile

 **EnableCompoundFile\( *bEnable* ** \)
Call this function if you want to store the document using the compound-file format\.

#### Parameters


  -  *bEnable\=1* : int

    Specifies whether compound file support is enabled or disabled\.

## [PyCOleDocument](#pycoledocument)\.GetInPlaceActiveItem

[PyCOleClientItem](#pycoleclientitem)\= **GetInPlaceActiveItem\( *wnd* ** \)
Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd\.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    The window\.

## [PyCOleDocument](#pycoledocument)\.GetNextItem

\(POSITION,[PyCOleClientItem](#pycoleclientitem)\) \= **GetNextItem\( *pos* ** \)
Call this function repeatedly to access each of the items in your document\.

#### Parameters


  -  *pos* : POSITION

    The position to iterate from\.

## [PyCOleDocument](#pycoledocument)\.GetStartPosition

POSITION \= **GetStartPosition\(** \)
Obtains the position of the first item in the document\.