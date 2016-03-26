# PyCOleInsertDialog

## PyCOleInsertDialog Object

An OLE 'Insert Object' dialog.  Encapsulates an MFC __COleInsertDialog__ class

#### Methods


  - [GetClassID](PyCOleInsertDialog.md#pycoleinsertdialoggetclassid)

    Returns the CLSID associated with the selected item&nbsp;

  - [GetSelectionType](PyCOleInsertDialog.md#pycoleinsertdialoggetselectiontype)

    Returns the type of selection made&nbsp;

  - [GetPathName](PyCOleInsertDialog.md#pycoleinsertdialoggetpathname)

    Returns the full path to the file selected in the dialog box&nbsp;

## [PyCOleInsertDialog](#pycoleinsertdialog).GetClassID

CLSID = __GetClassID(__ )
Returns the CLSID associated with the selected item

## [PyCOleInsertDialog](#pycoleinsertdialog).GetPathName

CLSID = __GetPathName(__ )
Returns the full path to the file selected in the dialog box

#### Comments
Do not call this if the selection type is createNewItem,

## [PyCOleInsertDialog](#pycoleinsertdialog).GetSelectionType

CLSID = __GetSelectionType(__ )
Returns the type of selection made