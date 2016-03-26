# PyCDocTemplate


## PyCDocTemplate Object

A document template class\.  Encapsulates an MFC CDocTemplate

 class

#### Methods

  - [DoCreateDoc](PyCDocTemplate.md#pycdoctemplatedocreatedoc)

    Creates an underlying document object\.&nbsp;

  - [FindOpenDocument](PyCDocTemplate.md#pycdoctemplatefindopendocument)

    Returns an existing document with the specified file name\.&nbsp;

  - [GetDocString](PyCDocTemplate.md#pycdoctemplategetdocstring)

    Retrieves a specific substring describing the document type\.&nbsp;

  - [GetDocumentList](PyCDocTemplate.md#pycdoctemplategetdocumentlist)

    Return a list of all open documents\.&nbsp;

  - [GetResourceID](PyCDocTemplate.md#pycdoctemplategetresourceid)

    Returns the resource ID in use\.&nbsp;

  - [GetSharedMenu](PyCDocTemplate.md#pycdoctemplategetsharedmenu)

    Returns the shared menu object for all frames using this template\.&nbsp;

  - [InitialUpdateFrame](PyCDocTemplate.md#pycdoctemplateinitialupdateframe)

    Calls the default OnInitialFrame handler\.&nbsp;

  - [SetContainerInfo](PyCDocTemplate.md#pycdoctemplatesetcontainerinfo)

    Sets the resources to be used when an OLE 2 object is in-place activated\.&nbsp;

  - [SetDocStrings](PyCDocTemplate.md#pycdoctemplatesetdocstrings)

    Assigns the document strings for the template\.&nbsp;

  - [OpenDocumentFile](PyCDocTemplate.md#pycdoctemplateopendocumentfile)

    Opens a document file, creating a view and frame\.&nbsp;


## [PyCDocTemplate\.CreateNewDocument](PyCDocTemplate.md#pycdoctemplate) Virtual

CreateNewDocument\(\)
Called to create a new document object\.


## [PyCDocTemplate\.CreateNewFrame](PyCDocTemplate.md#pycdoctemplate) Virtual

CreateNewFrame\(\)
Called to create a new frame window\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.DoCreateDoc

[PyCDocument](PyCDocument.md) = DoCreateDoc\(fileName\)
Creates an underlying document object\.

#### Parameters

  - fileName=None : string

    The name of the file to load\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.FindOpenDocument

[PyCDocument](PyCDocument.md) = FindOpenDocument\(fileName\)
Returns an existing document with the specified file name\.

#### Parameters

  - fileName : string

    The fully qualified filename to search for\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.GetDocString

string = GetDocString\(docIndex\)
Retrieves a specific substring describing the document type\.

#### Parameters

  - docIndex : int

    The document index\.  Must be one of the win32ui\.CDocTemplate\_\* constants\.

#### Comments

For more information on the doc strings, please see [PyCDocTemplate::SetDocStrings](PyCDocTemplate.md#pycdoctemplatesetdocstrings)


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.GetDocumentList

list = GetDocumentList\(\)
Return a list of all open documents\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.GetResourceID

GetResourceID\(\)
Returns the resource ID in use\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.GetSharedMenu

[PyCMenu](PyCMenu.md) = GetSharedMenu\(\)
Returns the shared menu object for all frames using this template\.

#### MFC References

  - CWnd::m\_hMenuShared


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.InitialUpdateFrame

InitialUpdateFrame\(frame, doc, bMakeVisible\)
Calls the default OnInitialFrame handler\.

#### Parameters

  - frame=None : [PyCFrameWnd](PyCFrameWnd.md)

    The frame window\.

  - doc=None : [PyCDocument](PyCDocument.md)

    A document for the frame\.

  - bMakeVisible=1 : int

    Indicates of the frame should be shown\.

#### See Also

  - [PyCDocTemplate\.InitialUpdateFrame](PyCDocTemplate.md#pycdoctemplateinitialupdateframe_virtual) virtual method


## [PyCDocTemplate\.InitialUpdateFrame](PyCDocTemplate.md#pycdoctemplate) Virtual

InitialUpdateFrame\(frame, frame

, bMakeVisible

\)
Called to perform the initial frame update\. 

The default behaviour is to call OnInitialUpdate on all views\.

#### Parameters

  - frame : [PyCFrameWnd](PyCFrameWnd.md)

    The frame window\.

  - frame : [PyCDocument](PyCDocument.md)

    The document attached to the frame\.

  - bMakeVisible : int

    Indicates if the frame should be made visible\.


## [PyCDocTemplate\.MatchDocType](PyCDocTemplate.md#pycdoctemplate) Virtual

MatchDocType\(fileName, fileType

\)
Queries if the template can open the specified file name\.

#### Parameters

  - fileName : string

    The name of the file to open\.

  - fileType : int

    Only used on the mac\.

#### Comments

This method should call PyCDocTemplate\.FindOpenDocument to return an already open 

document if one exists, else it should return one of the win32ui\.CDocTemplate\_Confidence\_\* constants\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.OpenDocumentFile

OpenDocumentFile\(filename, bMakeVisible\)
Opens a document file, creating a view and frame\.

#### Parameters

  - filename : string

    Name of file to open, or None

  - bMakeVisible=1 : int

    Indicates if the document should be created visible\.


## [PyCDocTemplate\.OpenDocumentFile](PyCDocTemplate.md#pycdoctemplate) Virtual

OpenDocumentFile\(\)
Called when a document file is to be opened\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.SetContainerInfo

SetContainerInfo\(id\)
Sets the resources to be used when an OLE 2 object is in-place activated\.

#### Parameters

  - id : int

    The resource ID\.


## [PyCDocTemplate](PyCDocTemplate.md#pycdoctemplate)\.SetDocStrings

SetDocStrings\(docStrings\)
Assigns the document strings for the template\.

#### Parameters

  - docStrings : string

    The document strings\.

#### Comments

The string must be a \\\\n seperated list of docstrings\. 

The elements are:

