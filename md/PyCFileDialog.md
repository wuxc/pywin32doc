# PyCFileDialog

## PyCFileDialog Object

A class which encapsulates an MFC CFileDialog object.  Derived from a[PyCDialog](#pycdialog)object.

#### Methods


  - [GetPathName](PyCFileDialog.md#pycfiledialoggetpathname)

    Retrieves the path name.&nbsp;

  - [GetFileName](PyCFileDialog.md#pycfiledialoggetfilename)

    Retrieves the file name.&nbsp;

  - [GetFileExt](PyCFileDialog.md#pycfiledialoggetfileext)

    Retrieves the file extension.&nbsp;

  - [GetFileTitle](PyCFileDialog.md#pycfiledialoggetfiletitle)

    Retrieves the file title.&nbsp;

  - [GetPathNames](PyCFileDialog.md#pycfiledialoggetpathnames)

    Retrieves the list of path names from the file dialog.&nbsp;

  - [GetReadOnlyPref](PyCFileDialog.md#pycfiledialoggetreadonlypref)

    Retrieves the read-only preference.&nbsp;

  - [SetOFNTitle](PyCFileDialog.md#pycfiledialogsetofntitle)

    Sets the title for the dialog.&nbsp;

  - [SetOFNInitialDir](PyCFileDialog.md#pycfiledialogsetofninitialdir)

    Sets the initial directory for the dialog.&nbsp;


## [PyCFileDialog](#pycfiledialog).GetFileExt

string = __GetFileExt(__ )
Retrives the file extension from the file dialog.

#### MFC References


  - CFileDialog::GetFileExt

## [PyCFileDialog](#pycfiledialog).GetFileName

string = __GetFileName(__ )
Retrives the file name from the file dialog.

#### MFC References


  - CFileDialog::GetFileName

## [PyCFileDialog](#pycfiledialog).GetFileTitle

string = __GetFileTitle(__ )
Retrives the file title from the file dialog.

#### MFC References


  - CFileDialog::GetFileTitle

## [PyCFileDialog](#pycfiledialog).GetPathName

string = __GetPathName(__ )
Retrives the path name from the file dialog.

#### MFC References


  - CFileDialog::GetPathName

## [PyCFileDialog](#pycfiledialog).GetPathNames

string = __GetPathNames(__ )
Retrieves the list of path names from the file dialog.

#### Comments
This method is useful when a multi-select dialog is used.

#### MFC References


  - CFileDialog::GetPathNames

## [PyCFileDialog](#pycfiledialog).GetReadOnlyPref

int = __GetReadOnlyPref(__ )
Retrives the value of the "Read Only" checkbox on the file dialog.

#### MFC References


  - CFileDialog::GetReadOnlyPref

## [PyCFileDialog](#pycfiledialog).SetOFNInitialDir

 __SetOFNInitialDir( *title* __ )
Sets the initial directory for the dialog.

#### Parameters


  -  *title* : string

    The initial directory for the dialog box.  May be None.

## [PyCFileDialog](#pycfiledialog).SetOFNTitle

 __SetOFNTitle( *title* __ )
Sets the Title for the dialog.

#### Parameters


  -  *title* : string

    The title for the dialog box.  May be None.