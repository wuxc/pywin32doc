# PyCOleDocument

## PyCOleDocument Object

An OLE document class.  Encapsulates an MFC __COleDocument__ class

#### Methods


  - [EnableCompoundFile](PyCOleDocument.md#pycoledocumentenablecompoundfile)

    Call this function if you want to store the document using the compound-file format&nbsp;

  - [GetStartPosition](PyCOleDocument.md#pycoledocumentgetstartposition)

    Obtains the position of the first item in the document.&nbsp;

  - [GetNextItem](PyCOleDocument.md#pycoledocumentgetnextitem)

    Call this function repeatedly to access each of the items in your document.&nbsp;

  - [GetInPlaceActiveItem](PyCOleDocument.md#pycoledocumentgetinplaceactiveitem)

    Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd. 

sentinel&nbsp;

## [PyCOleDocument](#pycoledocument).EnableCompoundFile

 __EnableCompoundFile( *bEnable* __ )
Call this function if you want to store the document using the compound-file format.

#### Parameters


  -  *bEnable=1* : int

    Specifies whether compound file support is enabled or disabled.

## [PyCOleDocument](#pycoledocument).GetInPlaceActiveItem

[PyCOleClientItem](#pycoleclientitem)= __GetInPlaceActiveItem( *wnd* __ )
Obtains the OLE item that is currently activated in place in the frame window containing the view identified by obWnd.

#### Parameters


  -  *wnd* :[PyCWnd](#pycwnd)

    The window.

## [PyCOleDocument](#pycoledocument).GetNextItem

(POSITION,[PyCOleClientItem](#pycoleclientitem)) = __GetNextItem( *pos* __ )
Call this function repeatedly to access each of the items in your document.

#### Parameters


  -  *pos* : POSITION

    The position to iterate from.

## [PyCOleDocument](#pycoledocument).GetStartPosition

POSITION = __GetStartPosition(__ )
Obtains the position of the first item in the document.