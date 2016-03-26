# PyCWinApp


## PyCWinApp Object

An application class\.  Encapsulates an MFC CWinApp

 class

#### Methods

  - [AddDocTemplate](PyCWinApp.md#pycwinappadddoctemplate)

    Adds a template to the application list\.&nbsp;

  - [FindOpenDocument](PyCWinApp.md#pycwinappfindopendocument)

    Returns an existing document with the specified file name\.&nbsp;

  - [GetDocTemplateList](PyCWinApp.md#pycwinappgetdoctemplatelist)

    Returns a list of all document templates in use\.&nbsp;

  - [InitDlgInstance](PyCWinApp.md#pycwinappinitdlginstance)

    Calls critical InitInstance processing for a dialog based application\.&nbsp;

  - [LoadCursor](PyCWinApp.md#pycwinapploadcursor)

    Loads a cursor\.&nbsp;

  - [LoadStandardCursor](PyCWinApp.md#pycwinapploadstandardcursor)

    Loads a standard cursor\.&nbsp;

  - [LoadOEMCursor](PyCWinApp.md#pycwinapploadoemcursor)

    Loads an OEM cursor\.&nbsp;

  - [LoadIcon](PyCWinApp.md#pycwinapploadicon)

    Loads an icon resource\.&nbsp;

  - [LoadStandardIcon](PyCWinApp.md#pycwinapploadstandardicon)

    Loads an icon resource\.&nbsp;

  - [OpenDocumentFile](PyCWinApp.md#pycwinappopendocumentfile)

    Opens a document file by name\.&nbsp;

  - [OnFileNew](PyCWinApp.md#pycwinapponfilenew)

    Calls the underlying OnFileNew MFC method\.&nbsp;

  - [OnFileOpen](PyCWinApp.md#pycwinapponfileopen)

    Calls the underlying OnFileOpen MFC method\.&nbsp;

  - [RemoveDocTemplate](PyCWinApp.md#pycwinappremovedoctemplate)

    Removes a template to the application list\.&nbsp;

  - [Run](PyCWinApp.md#pycwinapprun)

    Starts the main application message pump\.&nbsp;

  - [IsInproc](PyCWinApp.md#pycwinappisinproc)

    Returns a flag to indicate if the created CWinApp was in the DLL, or an external EXE\.&nbsp;


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.AddDocTemplate

AddDocTemplate\(template\)
Adds a template to the application list\.

#### Parameters

  - template : [PyCDocTemplate](PyCDocTemplate.md)

    The template to be added\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.FindOpenDocument

[PyCDocument](PyCDocument.md) = FindOpenDocument\(fileName\)
Returns an existing document with the specified file name\.

#### Parameters

  - fileName : string

    The fully qualified filename to search for\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.GetDocTemplateList

\[[PyCDocTemplate](PyCDocTemplate.md),\.\.\.\] = GetDocTemplateList\(\)
Returns a list of all document templates\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.InitDlgInstance

InitDlgInstance\(dialog\)
Calls critical InitInstance processing for a dialog based application\.

#### Parameters

  - dialog : [PyCDialog](PyCDialog.md)

    The dialog object to be used as the main window for the application\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.IsInproc

int = IsInproc\(\)
Returns a flag to indicate if the created CWinApp was in the DLL, or an external EXE\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.LoadCursor

int = LoadCursor\(cursorId\)
Loads a cursor\.

#### Parameters

  - cursorId : [PyResourceId](PyResourceId.md)

    The resource id or name of the cursor to load\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.LoadIcon

int = LoadIcon\(idResource\)
Loads an icon resource\.

#### Parameters

  - idResource : int

    The ID of the icon to load\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.LoadOEMCursor

int = LoadOEMCursor\(cursorId\)
Loads an OEM cursor\.

#### Parameters

  - cursorId : int

    The ID of the cursor to load\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.LoadStandardCursor

int = LoadStandardCursor\(cursorId\)
Loads a standard cursor\.

#### Parameters

  - cursorId : [PyResourceId](PyResourceId.md)

    The resource ID or name of the cursor to load\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.LoadStandardIcon

int = LoadStandardIcon\(resourceName\)
Loads an icon resource\.

#### Parameters

  - resourceName : [PyResourceId](PyResourceId.md)

    The resource name or id of the standard icon to load\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.OnFileNew

OnFileNew\(\)
Calls the underlying OnFileNew MFC method\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.OnFileOpen

OnFileOpen\(\)
Calls the underlying OnFileOpen MFC method\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.OpenDocumentFile

OpenDocumentFile\(fileName\)
Opens a document file by name\.

#### Parameters

  - fileName : string

    The name of the document to open\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.RemoveDocTemplate

RemoveDocTemplate\(template\)
Removes a template to the application list\.

#### Parameters

  - template : [PyCDocTemplate](PyCDocTemplate.md)

    The template to be removed\.  Must have previously been added by [PyCWinApp::AddDocTemplate](PyCWinApp.md#pycwinappadddoctemplate)\.

#### Comments

Note that MFC does not provide an equivilent function\.


## [PyCWinApp](PyCWinApp.md#pycwinapp)\.Run

int = Run\(\)
Starts the message pump\.  Advanced users only