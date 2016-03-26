# PyCOleDocument


## PyCOleDocument Object

An OLE document class\.  Encapsulates an MFC COleDocument

 class

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


## [PyCOleDocument](PyCOleDocument.md#pycoledocument)\.EnableCompoundFile

EnableCompoundFile\(bEnable\)
Call this function if you want to store the document using the compound-file format\.

#### Parameters

  - bEnable=1 : int

    Specifies whether compound file support is enabled or disabled\.


## [PyCOleDocument](PyCOleDocument.md#pycoledocument)\.GetInPlaceActiveItem

[PyCOleClientItem](PyCOleClientItem.md) = GetInPlaceActiveItem\(wnd\)
Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd\.

#### Parameters

  - wnd : [PyCWnd](PyCWnd.md)

    The window\.


## [PyCOleDocument](PyCOleDocument.md#pycoledocument)\.GetNextItem

\(POSITION, [PyCOleClientItem](PyCOleClientItem.md)\) = GetNextItem\(pos\)
Call this function repeatedly to access each of the items in your document\.

#### Parameters

  - pos : POSITION

    The position to iterate from\.


## [PyCOleDocument](PyCOleDocument.md#pycoledocument)\.GetStartPosition

POSITION = GetStartPosition\(\)
Obtains the position of the first item in the document\.