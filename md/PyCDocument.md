# PyCDocument

## PyCDocument Object

A document class.  Encapsulates an MFC __CDocument__ class

#### Methods


  - [DeleteContents](PyCDocument.md#pycdocumentdeletecontents)

    Call the MFC DeleteContents method.&nbsp;

  - [DoSave](PyCDocument.md#pycdocumentdosave)

    Save the file.  If necessary, prompt for file name.&nbsp;

  - [DoFileSave](PyCDocument.md#pycdocumentdofilesave)

    Check file attributes, and save the file.&nbsp;

  - [GetDocTemplate](PyCDocument.md#pycdocumentgetdoctemplate)

    Returns the[PyCDocTemplate](#pycdoctemplate)for the document.&nbsp;

  - [GetAllViews](PyCDocument.md#pycdocumentgetallviews)

    Returns a list of all views for the current document.&nbsp;

  - [GetFirstView](PyCDocument.md#pycdocumentgetfirstview)

    Returns the first view object attached to this document.&nbsp;

  - [GetPathName](PyCDocument.md#pycdocumentgetpathname)

    Returns the full path name of the current document.&nbsp;

  - [GetTitle](PyCDocument.md#pycdocumentgettitle)

    Returns the title of the current document.&nbsp;

  - [IsModified](PyCDocument.md#pycdocumentismodified)

    Return a flag indicating if the document has been modified.&nbsp;

  - [OnChangedViewList](PyCDocument.md#pycdocumentonchangedviewlist)

    Informs the document when a view is added or removed.&nbsp;

  - [OnCloseDocument](PyCDocument.md#pycdocumentonclosedocument)

    Call the MFC OnCloseDocument handler.&nbsp;

  - [OnNewDocument](PyCDocument.md#pycdocumentonnewdocument)

    Call the MFC OnNewDocument handler.&nbsp;

  - [OnOpenDocument](PyCDocument.md#pycdocumentonopendocument)

    Call the MFC OnOpenDocument handler.&nbsp;

  - [OnSaveDocument](PyCDocument.md#pycdocumentonsavedocument)

    Call the MFC OnSaveDocument handler.&nbsp;

  - [SetModifiedFlag](PyCDocument.md#pycdocumentsetmodifiedflag)

    Set the "dirty" flag for the document.&nbsp;

  - [SaveModified](PyCDocument.md#pycdocumentsavemodified)

    Call the underlying MFC method.&nbsp;

  - [SetPathName](PyCDocument.md#pycdocumentsetpathname)

    Set the full path name for the document.&nbsp;

  - [SetTitle](PyCDocument.md#pycdocumentsettitle)

    Set the title of the document.&nbsp;

  - [UpdateAllViews](PyCDocument.md#pycdocumentupdateallviews)

    Informs each view when a document changes. 

sentinel&nbsp;


## [PyCDocument](#pycdocument).DeleteContents

 __DeleteContents(__ )
Call the MFC DeleteContents method. 

This routine is provided so a document object which overrides this method 

can call the original MFC version if required.

#### See Also


  - [PyCDocument.DeleteContents](PyCDocument.md#pycdocumentdeletecontents_virtual)virtual method

#### MFC References


  - CDocument::DeleteContents

## [PyCDocument.DeleteContents](#pycdocument)Virtual

 __DeleteContents(__ )
Called by the MFC architecture when a document is newly created or closed.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::DeleteContents](PyCDocument.md#pycdocumentdeletecontents)

## [PyCDocument](#pycdocument).DoFileSave

 __DoFileSave(__ )
Checks the file attributes. 

If the file is read only, a new name is prompted, else the 

file is saved (by calling DoSave)

#### See Also


  - [PyCDocument.DoFileSave](PyCDocument.md#pycdocumentdofilesave_virtual)virtual method

#### Undocumented MFC References

  - CDocument::DoFileSave

## [PyCDocument.DoFileSave](#pycdocument)Virtual

 __DoFileSave(__ )
Called by the MFC architecture.

#### Comments
If a handler is defined for this function, it must call the 

base class[PyCDocument::DoFileSave](PyCDocument.md#pycdocumentdofilesave)method.

#### See Also


  - [PyCDocument::DoFileSave](PyCDocument.md#pycdocumentdofilesave)

#### Return Value
TRUE if the document could be saved, else FALSE.

## [PyCDocument](#pycdocument).DoSave

 __DoSave( *fileName*  *, bReplace* __ )
Calls the underlying MFC DoSave method.

#### Parameters


  -  *fileName* : string

    The name of the file to save to.

  -  *bReplace=1* : int

    Should an existing file be silently replaced?.

#### Comments
If invalid or no filename, will prompt for a name, else 

will perform the actual saving of the document.

#### See Also


  - [PyCDocument.DoSave](PyCDocument.md#pycdocumentdosave_virtual)virtual method

#### Undocumented MFC References

  - CDocument::DoSave

## [PyCDocument.DoSave](#pycdocument)Virtual

 __DoSave( *fileName*  *, bReplace* __ )
Called by the MFC architecture to save a document.

#### Parameters


  -  *fileName* : string

    The name of the file being saved.

  -  *bReplace* : int

    TRUE if the file should be replaced.

#### Comments
If a handler is defined for this function, it must call the 

base class[PyCDocument::DoSave](PyCDocument.md#pycdocumentdosave)method.

#### See Also


  - [PyCDocument::DoSave](PyCDocument.md#pycdocumentdosave)

#### Return Value
TRUE if the document could be saved, else FALSE.

## [PyCDocument](#pycdocument).GetAllViews

[[PyCView](#pycview),...] = __GetAllViews(__ )
Returns a list of all views for the current document.

#### MFC References


  - CDocument::GetFirstViewPosition

  - CDocument::GetNextView

## [PyCDocument](#pycdocument).GetDocTemplate

[PyCDocTemplate](#pycdoctemplate)= __GetDocTemplate(__ )
Returns the template for the document.

#### MFC References


  - CDocument::GetDocTemplate

## [PyCDocument](#pycdocument).GetFirstView

[PyCView](#pycview)= __GetFirstView(__ )
Returns the first view object attached to this document.

#### Comments
For more info, see[PyCDocument::GetAllViews](PyCDocument.md#pycdocumentgetallviews)shouldnt be possible.

#### MFC References


  - CDocument::GetFirstViewPosition

  - CDocument::GetNextView

## [PyCDocument](#pycdocument).GetPathName

string = __GetPathName(__ )
Returns the full path name of the current document. 

The string will be empty if no path name has been set.

#### MFC References


  - CDocument::GetPathName

## [PyCDocument](#pycdocument).GetTitle

string = __GetTitle(__ )
Returns the title of the current document. 

This will often be the file name portion of the path name.

#### MFC References


  - CDocument::GetTitle

## [PyCDocument](#pycdocument).IsModified

int = __IsModified(__ )
Return a flag indicating if the document has been modified.

#### MFC References


  - CDocument::IsModified

## [PyCDocument](#pycdocument).OnChangedViewList

 __OnChangedViewList(__ )
Informs the document when a view is added or removed.

## [PyCDocument.OnChangedViewList](#pycdocument)Virtual

 __OnChangedViewList(__ )
Called by the MFC architecture when after a view is attached.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::OnChangedViewList](PyCDocument.md#pycdocumentonchangedviewlist)

## [PyCDocument](#pycdocument).OnCloseDocument

 __OnCloseDocument(__ )
Call the MFC OnCloseDocument handler. 

This routine is provided so a document object which overrides this method 

can call the original MFC version if required.

#### See Also


  - [PyCDocument.OnCloseDocument](PyCDocument.md#pycdocumentonclosedocument_virtual)virtual method

#### MFC References


  - CDocument::OnCloseDocument

## [PyCDocument.OnCloseDocument](#pycdocument)Virtual

 __OnCloseDocument(__ )
Called by the MFC architecture.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::OnCloseDocument](PyCDocument.md#pycdocumentonclosedocument)

## [PyCDocument](#pycdocument).OnNewDocument

 __OnNewDocument(__ )
Call the MFC OnNewDocument handler. 

This routine is provided so a document object which overrides this method 

can call the original MFC version if required.

#### See Also


  - [PyCDocument.OnNewDocument](PyCDocument.md#pycdocumentonnewdocument_virtual)virtual method

#### MFC References


  - CDocument::OnNewDocument

## [PyCDocument.OnNewDocument](#pycdocument)Virtual

 __OnNewDocument(__ )
Called by the MFC architecture.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::OnNewDocument](PyCDocument.md#pycdocumentonnewdocument)

#### Return Value
TRUE if a new document could be created, else FALSE.

## [PyCDocument](#pycdocument).OnOpenDocument

 __OnOpenDocument( *pathName* __ )
Call the MFC OnOpenDocument handler. 

This routine is provided so a document object which overrides this method 

can call the original MFC version if required.

#### Parameters


  -  *pathName* : string

    The full path of the file to open.

#### MFC References


  - CDocument::OnOpenDocument

## [PyCDocument.OnOpenDocument](#pycdocument)Virtual

 __OnOpenDocument( *fileName* __ )
Called by the MFC architecture.

#### Parameters


  -  *fileName* : string

    The name of the file being opened.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::OnOpenDocument](PyCDocument.md#pycdocumentonopendocument)

#### Return Value
TRUE if the document could be opened, else FALSE.

## [PyCDocument](#pycdocument).OnSaveDocument

 __OnSaveDocument( *pathName* __ )
Call the MFC OnSaveDocument handler. 

This routine is provided so a document object which overrides this method 

can call the original MFC version if required.

#### Parameters


  -  *pathName* : string

    The full path of the file to save.

#### MFC References


  - CDocument::OnSaveDocument

## [PyCDocument.OnSaveDocument](#pycdocument)Virtual

 __OnSaveDocument( *fileName* __ )
Called by the MFC architecture.

#### Parameters


  -  *fileName* : string

    The name of the file being saved.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::OnSaveDocument](PyCDocument.md#pycdocumentonsavedocument)

#### Return Value
TRUE if the document could be saved, else FALSE.

## [PyCDocument.PreCloseFrame](#pycdocument)Virtual

 __PreCloseFrame(__ )
Called before the frame window is closed.

#### Comments
The MFC base implementation is always called after the Python handler returns.

## [PyCDocument](#pycdocument).SaveModified

int = __SaveModified(__ )
Call the underlying MFC method.

#### See Also


  - [PyCDocument.SaveModified](PyCDocument.md#pycdocumentsavemodified_virtual)virtual method

#### MFC References


  - CDocument::SaveModified

#### Return Value
Nonzero if it is safe to continue and close the document; 0 if the document should not be closed.

## [PyCDocument.SaveModified](#pycdocument)Virtual

 __SaveModified(__ )
Called by the MFC architecture when a document is closed.

#### Comments
If a handler is defined for this function, the base (MFC) function will not 

be called.  If necessary, the handler must call this function explicitely.

#### See Also


  - [PyCDocument::SaveModified](PyCDocument.md#pycdocumentsavemodified)

#### Return Value
The handler should return TRUE if it is safe to continue and close 

the document; 0 if the document should not be closed.

## [PyCDocument](#pycdocument).SetModifiedFlag

 __SetModifiedFlag( *bModified* __ )
Set the "dirty" flag for the document.

#### Parameters


  -  *bModified=1* : int

    Set dirty flag

#### MFC References


  - CDocument::SetModifiedFlag

## [PyCDocument](#pycdocument).SetPathName

 __SetPathName( *path* __ )
Set the full path name for the document.

#### Parameters


  -  *path* : string

    The full path of the file.

#### MFC References


  - CDocument::SetPathName

## [PyCDocument](#pycdocument).SetTitle

 __SetTitle( *title* __ )
Set the title of the document (ie, the name 

to appear in the window caption for the document.

#### Parameters


  -  *title* : string

    The new title.

#### MFC References


  - CDocument::SetTitle

## [PyCDocument](#pycdocument).UpdateAllViews

 __UpdateAllViews( *sender*  *, hint* __ )
Informs each view when a document changes.

#### Parameters


  -  *sender* :[PyCView](#pycview)

    The view who initiated the update

  -  *hint=None* : object

    A hint for the update.

#### MFC References


  - CDocument::UpdateAllViews