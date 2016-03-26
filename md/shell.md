# shell


## Module shell

A module wrapping Windows Shell functions and interfaces

#### Methods

  - [AssocCreate](shell.md#shellassoccreate)

    Creates a [PyIQueryAssociations](PyIQueryAssociations.md) object&nbsp;

  - [AssocCreateForClasses](shell.md#shellassoccreateforclasses)

    Retrieves an object that implements an IQueryAssociations interface\."\}&nbsp;

  - [DragQueryFile](shell.md#shelldragqueryfile)

    Retrieves the file names of dropped files that have resulted from a successful drag-and-drop operation\.&nbsp;

  - [DragQueryFileW](shell.md#shelldragqueryfilew)

    Retrieves the file names of dropped files that have resulted from a successful drag-and-drop operation\.&nbsp;

  - [DragQueryPoint](shell.md#shelldragquerypoint)

    Retrieves the position of the mouse pointer at the time a file was dropped during a drag-and-drop operation\.&nbsp;

  - [IsUserAnAdmin](shell.md#shellisuseranadmin)

    Tests whether the current user is a member of the Administrator's group\.&nbsp;

  - [SHCreateDataObject](shell.md#shellshcreatedataobject)

    Creates a data object in a parent folder\.&nbsp;

  - [SHCreateDefaultContextMenu](shell.md#shellshcreatedefaultcontextmenu)

    &nbsp;

  - [SHCreateDefaultExtractIcon](shell.md#shellshcreatedefaultextracticon)

    Creates a standard icon extractor, whose defaults can be further configured via the IDefaultExtractIconInit interface\.&nbsp;

  - [SHCreateShellFolderView](shell.md#shellshcreateshellfolderview)

    Creates a new instance of the default Shell folder view object\.&nbsp;

  - [SHCreateShellItemArray](shell.md#shellshcreateshellitemarray)

    Creates a Shell item array object\.&nbsp;

  - [SHCreateShellItemArrayFromDataObject](shell.md#shellshcreateshellitemarrayfromdataobject)

    Creates a shell item array from an IDataObject interface&nbsp;

  - [SHCreateShellItemArrayFromIDLists](shell.md#shellshcreateshellitemarrayfromidlists)

    Creates a shell item array from a number of item identifiers&nbsp;

  - [SHCreateShellItemArrayFromShellItem](shell.md#shellshcreateshellitemarrayfromshellitem)

    &nbsp;

  - [SHGetPathFromIDList](shell.md#shellshgetpathfromidlist)

    Converts an [PyIDL](PyIDL.md) to a path\.&nbsp;

  - [SHGetPathFromIDListW](shell.md#shellshgetpathfromidlistw)

    Converts an [PyIDL](PyIDL.md) to a unicode path\.&nbsp;

  - [SHBrowseForFolder](shell.md#shellshbrowseforfolder)

    Displays a dialog box that enables the user to select a shell folder\.&nbsp;

  - [SHGetFileInfo](shell.md#shellshgetfileinfo)

    Retrieves information about an object in the file system, such as a file, a folder, a directory, or a drive root\.&nbsp;

  - [SHGetFolderPath](shell.md#shellshgetfolderpath)

    Retrieves the path of a folder\.&nbsp;

  - [SHSetFolderPath](shell.md#shellshsetfolderpath)

    Sets the location of a special folder&nbsp;

  - [SHGetFolderLocation](shell.md#shellshgetfolderlocation)

    Retrieves the [PyIDL](PyIDL.md) of a folder\.&nbsp;

  - [SHGetNameFromIDList](shell.md#shellshgetnamefromidlist)

    Retrieves the display name of an item from an ID list\.&nbsp;

  - [SHGetSpecialFolderPath](shell.md#shellshgetspecialfolderpath)

    Retrieves the path of a special folder\.&nbsp;

  - [SHGetSpecialFolderLocation](shell.md#shellshgetspecialfolderlocation)

    Retrieves the [PyIDL](PyIDL.md) of a special folder\.&nbsp;

  - [SHAddToRecentDocs](shell.md#shellshaddtorecentdocs)

    Adds a document to the shell's list of recently used documents or clears all documents from the list\. The user gains access to the list through the Start menu of the Windows taskbar\.&nbsp;

  - [SHChangeNotify](shell.md#shellshchangenotify)

    Notifies the system of an event that an application has performed\. An application should use this function if it performs an action that may affect the shell\.&nbsp;

  - [SHEmptyRecycleBin](shell.md#shellshemptyrecyclebin)

    Empties the recycle bin on the specified drive\.&nbsp;

  - [SHQueryRecycleBin](shell.md#shellshqueryrecyclebin)

    Returns the number of items and total size of recycle bin&nbsp;

  - [SHGetDesktopFolder](shell.md#shellshgetdesktopfolder)

    Retrieves the [PyIShellFolder](PyIShellFolder.md) interface for the desktop folder, which is the root of the shell's namespace\.&nbsp;

  - [SHUpdateImage](shell.md#shellshupdateimage)

    Notifies the shell that an image in the system image list has changed\.&nbsp;

  - [SHChangeNotify](shell.md#shellshchangenotify)

    Notifies the system of an event that an application has performed\.&nbsp;

  - [SHChangeNotifyRegister](shell.md#shellshchangenotifyregister)

    Registers a window that receives notifications from the file system or shell\.&nbsp;

  - [SHChangeNotifyDeregister](shell.md#shellshchangenotifyderegister)

    Unregisters the client's window process from receiving notification events&nbsp;

  - [SHCreateItemFromIDList](shell.md#shellshcreateitemfromidlist)

    Creates and initializes a Shell item object\.&nbsp;

  - [SHCreateItemFromParsingName](shell.md#shellshcreateitemfromparsingname)

    Creates and initializes a Shell item object from a parsing name\.&nbsp;

  - [SHCreateItemFromRelativeName](shell.md#shellshcreateitemfromrelativename)

    Creates and initializes a Shell item object from a relative parsing name\.&nbsp;

  - [SHCreateItemInKnownFolder](shell.md#shellshcreateiteminknownfolder)

    Creates a Shell item object for a single file that exists inside a known folder\.&nbsp;

  - [SHCreateItemWithParent](shell.md#shellshcreateitemwithparent)

    Create a Shell item, given a parent folder and a child item ID\.&nbsp;

  - [SHGetIDListFromObject](shell.md#shellshgetidlistfromobject)

    Retrieves the PIDL of an object\.&nbsp;

  - [SHGetInstanceExplorer](shell.md#shellshgetinstanceexplorer)

    Allows components that run in a Web browser \(Iexplore\.exe\) or a nondefault Windows&\#174 Explorer \(Explorer\.exe\) process to hold a reference to the process\. The components can use the reference to prevent the process from closing prematurely\.&nbsp;

  - [SHFileOperation](shell.md#shellshfileoperation)

    Copies, moves, renames, or deletes a file system object\.&nbsp;

  - [StringAsCIDA](shell.md#shellstringascida)

    Given a CIDA as a raw string, return pidl\_folder, \[pidl\_children, \.\.\.\]&nbsp;

  - [CIDAAsString](shell.md#shellcidaasstring)

    Given a \(pidl, child\_pidls\) object, return a CIDA as a string&nbsp;

  - [StringAsPIDL](shell.md#shellstringaspidl)

    Given a PIDL as a raw string, return a PIDL object \(ie, a list of strings\)&nbsp;

  - [AddressAsPIDL](shell.md#shelladdressaspidl)

    Given the address of a PIDL, return a PIDL object \(ie, a list of strings\)&nbsp;

  - [PIDLAsString](shell.md#shellpidlasstring)

    Given a PIDL object, return the raw PIDL bytes as a string&nbsp;

  - [SHGetSettings](shell.md#shellshgetsettings)

    Retrieves the current shell option settings\.&nbsp;

  - [FILEGROUPDESCRIPTORAsString](shell.md#shellfilegroupdescriptorasstring)

    Creates a FILEGROUPDESCRIPTOR from a sequence of mapping objects, each with FILEDESCRIPTOR attributes&nbsp;

  - [StringAsFILEGROUPDESCRIPTOR](shell.md#shellstringasfilegroupdescriptor)

    Decodes a FILEGROUPDESCRIPTOR packed in a string&nbsp;

  - [ShellExecuteEx](shell.md#shellshellexecuteex)

    Performs an action on a file\.&nbsp;

  - [SHGetViewStatePropertyBag](shell.md#shellshgetviewstatepropertybag)

    Retrieves an interface for a folder's view state&nbsp;

  - [SHILCreateFromPath](shell.md#shellshilcreatefrompath)

    Returns the PIDL and attributes of a path&nbsp;

  - [SHCreateShellItem](shell.md#shellshcreateshellitem)

    Creates an IShellItem interface from a PIDL&nbsp;

  - [SHOpenFolderAndSelectItems](shell.md#shellshopenfolderandselectitems)

    Displays a shell folder with items pre-selected&nbsp;

  - [SHCreateStreamOnFileEx](shell.md#shellshcreatestreamonfileex)

    Creates a [PyIStream](PyIStream.md) that reads and writes to a file&nbsp;

  - [SetCurrentProcessExplicitAppUserModelID](shell.md#shellsetcurrentprocessexplicitappusermodelid)

    Sets the taskbar identifier&nbsp;

  - [GetCurrentProcessExplicitAppUserModelID](shell.md#shellgetcurrentprocessexplicitappusermodelid)

    Retrieves the current taskbar identifier&nbsp;

  - [SHParseDisplayName](shell.md#shellshparsedisplayname)

    Translates a display name into a shell item identifier&nbsp;


## [shell](shell.md#shell)\.AddressAsPIDL

[PyIDL](PyIDL.md) = AddressAsPIDL\(address\)
Given the address of a PIDL in memory, return a PIDL object \(ie, a list of strings\)

#### Parameters

  - address : int

    The address of the PIDL


## [shell](shell.md#shell)\.AssocCreate

[PyIQueryAssociations](PyIQueryAssociations.md) = AssocCreate\(\)
Creates a [PyIQueryAssociations](PyIQueryAssociations.md) object


## [shell](shell.md#shell)\.AssocCreateForClasses

[PyIUnknown](PyIUnknown.md) = AssocCreateForClasses\(\)
Retrieves an object that implements an IQueryAssociations interface\.

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.CIDAAsString

string = CIDAAsString\(pidl\)
Given a \(pidl, child\_pidls\) object, return a CIDA as a string

#### Parameters

  - pidl : string

    The PIDL as a raw string\.

#### Return Value
The result is a string with the CIDA bytes\.


## [shell](shell.md#shell)\.DragQueryFile

int/string = DragQueryFile\(hglobal, index

\)
Retrieves the names \(or count\) of dropped files

#### Parameters

  - hglobal : [PyHANDLE](PyHANDLE.md)

    The HGLOBAL object - generally obtained via the 'data\_handle' property of a [PySTGMEDIUM](PySTGMEDIUM.md) object\.

  - index : int

    The index to retrieve\.  If -1, the result if an integer representing the valid index values\.


## [shell](shell.md#shell)\.DragQueryFileW

int/[PyUnicode](PyUnicode.md) = DragQueryFileW\(hglobal, index

\)
Retrieves the names \(or count\) of dropped files

#### Parameters

  - hglobal : [PyHANDLE](PyHANDLE.md)

    The HGLOBAL object - generally obtained via the 'data\_handle' property of a [PySTGMEDIUM](PySTGMEDIUM.md) object\.

  - index : int

    The index to retrieve\.  If -1, the result if an integer representing the valid index values\.


## [shell](shell.md#shell)\.DragQueryPoint

int, \(int,int\) = DragQueryPoint\(hglobal\)
Retrieves the position of the mouse pointer at the time a file was dropped during a drag-and-drop operation\.

#### Parameters

  - hglobal : [PyHANDLE](PyHANDLE.md)

    The HGLOBAL object - generally obtained the 'data\_handle' property of a [PySTGMEDIUM](PySTGMEDIUM.md)

#### Comments

The window for which coordinates are returned is the window that received the WM\_DROPFILES message

#### Return Value
The first item of the return tuple is True if the drop occurred in the client area of the window, or False if the drop did not occur in the client area of the window\.


## [shell](shell.md#shell)\.FILEGROUPDESCRIPTORAsString

string = FILEGROUPDESCRIPTORAsString\(descriptors, make\_unicode

\)
Creates a FILEGROUPDESCRIPTOR from a sequence of mapping objects, each with FILEDESCRIPTOR attributes

#### Parameters

  - descriptors : \[FILEDESCRIPTOR, \.\.\.\]

    A sequence of FILEDESCRIPTOR objects\. 

Each filedescriptor object must be a mapping/dictionary, with the following 

optional attributes: dwFlags, clsid, sizel, pointl, dwFileAttributes, 

ftCreationTime, ftLastAccessTime, ftLastWriteTime, nFileSize 

If these attributes do not exist, or are None, they will be ignored - hence 

you only need specify attributes you care about\. 

In general, you can omit dwFlags - it will be set correctly based 

on what other attributes exist\.

  - make\_unicode=False on py2k, True on py3k : bool

    If true, a FILEDESCRIPTORW object is created


## [shell](shell.md#shell)\.GetCurrentProcessExplicitAppUserModelID

str = GetCurrentProcessExplicitAppUserModelID\(\)
Retrieves the current taskbar identifier

#### Comments

Will only retrieve an identifier if set by the application, not a system-assigned default\.

Requires Windows 7 or later


## [shell](shell.md#shell)\.IsUserAnAdmin

bool = IsUserAnAdmin\(\)
Tests whether the current user is a member of the Administrator's group\.

#### Comments

This method is only available with version 5 or later of the shell controls

#### Return Value
The result is true or false, or a com\_error with E\_NOTIMPL is raised\.


## [shell](shell.md#shell)\.PIDLAsString

string = PIDLAsString\(pidl\)
Given a PIDL object, return the raw PIDL bytes as a string

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    The PIDL object \(ie, a list of strings\)


## [shell](shell.md#shell)\.SHAddToRecentDocs

SHAddToRecentDocs\(Flags, data\)
Adds a document to the shell's list of recently used documents or clears all documents from the list\. The user gains access to the list through the Start menu of the Windows taskbar\.

#### Parameters

  - Flags : int

    Value from SHARD enum indicating how the item is identified\.

  - data : object

    Type of input is determined by the SHARD\_\* flag\.  Use None to clear recent items list\.

   

       Flags

   

   

       Type of input

   

SHARD\_PATHAString containing a file path

SHARD\_PATHWString containing a file path

SHARD\_PIDL[PyIDL](PyIDL.md), or a buffer containing a PIDL \(see [shell::PIDLAsString](shell.md#shellpidlasstring)\)

SHARD\_APPIDINFOTuple of \([PyIShellItem](PyIShellItem.md), str\), where str is an AppID

SHARD\_APPIDINFOIDLISTTuple of \([PyIDL](PyIDL.md), str\), where str is an AppID

SHARD\_LINK[PyIShellLink](PyIShellLink.md)

SHARD\_APPIDINFOLINKTuple of \([PyIShellLink](PyIShellLink.md), str\) where str is an AppID

SHARD\_SHELLITEM[PyIShellItem](PyIShellItem.md)

#### Comments

On Windows 7, the entry is also added to the application's jump list\.

The underlying API function has no return value, and therefore no way to indicate failure\.

#### Win32 API References

  - Search for SHAddToRecentDocs at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=SHAddToRecentDocs.md), [google](http://www.google.com/search?q=SHAddToRecentDocs.md) or [google groups](http://groups.google.com/groups?q=SHAddToRecentDocs.md)\.


## [shell](shell.md#shell)\.SHBrowseForFolder

\([PyIDL](PyIDL.md), string displayName, iImage\) = SHBrowseForFolder\(hwndOwner, pidlRoot

, title

, flags

, callback

, callback\_data

\)
Displays a dialog box that enables the user to select a shell folder\.

#### Parameters

  - hwndOwner=None : [PyHANDLE](PyHANDLE.md)

    Parent window for the dialog box, can be None

  - pidlRoot=None : [PyIDL](PyIDL.md)

    PIDL identifying the place to start browsing\. Desktop is used if not specified

  - title=None : Unicode

/string

    Title to be displayed with the directory tree

  - flags=0 : int

    Combination of shellcon\.BIF\_\* flags

  - callback=None : object

    A callable object to be used as the callback, or None

  - callback\_data=None : object

    An object passed to the callback function

#### Comments

If you provide a callback function, it should take 4 args: 

hwnd, msg, lp, data\.  Data will be whatever you passed as callback\_data, 

and the rest are integers\.  See the Microsoft documentation for 

SHBrowseForFolder, or the browse\_for\_folder\.py shell sample for more 

information\.

#### Return Value
The result is ALWAYS a tuple of 3 items\.  If the user cancels the 

dialog, all items are None\.  If the dialog is closed normally, the result is 

a tuple of \(PIDL, DisplayName, iImageList\)


## [shell](shell.md#shell)\.SHChangeNotify

SHChangeNotify\(EventId, Flags, Item1, Item2\)
Notifies the system of an event that an application has performed\. An application should use this function if it performs an action that may affect the shell\.

#### Parameters

  - EventId : int

    Combination of shellcon\.SHCNE\_\* constants

  - Flags : int

    Combination of shellcon\.SHCNF\_\* constants that specify type of last 2 parameters 

Only one of the type flags may be specified, combined with one of the SHCNF\_FLUSH\* flags

  - Item1 : object

    Type is dependent on the event to be signalled

  - Item2 : object

    Type is dependent on the event to be signalled


## [shell](shell.md#shell)\.SHChangeNotifyDeregister

SHChangeNotifyDeregister\(id\)
Unregisters the client's window process from receiving notification events

#### Parameters

  - id : int

    The registration identifier \(ID\) returned by [shell::SHChangeNotifyRegister](shell.md#shellshchangenotifyregister)\.


## [shell](shell.md#shell)\.SHChangeNotifyRegister

int = SHChangeNotifyRegister\(hwnd, sources

, events

, msg

\)
Registers a window that receives notifications from the file system or shell\.

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Handle to the window that receives the change or notification messages\.

  - sources : int

    One or more values that indicate the type of events for which to receive notifications\.

  - events : int

    Change notification events for which to receive notification\.

  - msg : int

    Message to be posted to the window procedure\.


## [shell](shell.md#shell)\.SHCreateDataObject

[PyIUnknown](PyIUnknown.md) = SHCreateDataObject\(parent, children

, do\_inner

, iid

\)

#### Parameters

  - parent : PIDL

    

  - children : \[PIDL, \.\.\.\]

    

  - do\_inner : [PyIDataObject](PyIDataObject.md)

    The inner data object, or None 

bNoneOK \*/\)\)

  - iid=IID\_IDataObject : [PyIID](PyIID.md)

    The IID to query for

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateDefaultContextMenu

[PyIUnknown](PyIUnknown.md) = SHCreateDefaultContextMenu\(dcm, iid

\)

#### Parameters

  - dcm : DEFAULTCONTEXTMENU

    

  - iid=IID\_IContextMenu : [PyIID](PyIID.md)

    The IID to query for

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateDefaultExtractIcon

[PyIDefaultExtractIconInit](PyIDefaultExtractIconInit.md) = SHCreateDefaultExtractIcon\(\)
Creates a standard icon extractor, whose defaults can be further configured via the IDefaultExtractIconInit interface\.

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateItemFromIDList

[PyIShellItem](PyIShellItem.md) = SHCreateItemFromIDList\(pidl, riid

\)
Creates and initializes a Shell item 

object from a PIDL\.  Can also create [PyIShellItem2](PyIShellItem2.md) objects\.

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    An absolute item identifier list

  - riid=IID\_IShellItem : [PyIID](PyIID.md)

    The interface to create

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateItemFromParsingName

[PyIShellItem](PyIShellItem.md) = SHCreateItemFromParsingName\(name, ctx

, riid

\)
Creates and initializes a Shell item object from a parsing name\.

#### Parameters

  - name : str

    The display name of the item to create, eg a file path

  - ctx : [PyIBindCtx](PyIBindCtx.md)

    Bind context, can be None

  - riid : [PyIID](PyIID.md)

    The interface to create, IID\_IShellItem or IID\_IShellItem2

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateItemFromRelativeName

[PyIShellItem](PyIShellItem.md) = SHCreateItemFromRelativeName\(Parent, Name

, ctx

, riid

\)
Creates and initializes a Shell item object from a relative parsing name\.

#### Parameters

  - Parent : [PyIShellItem](PyIShellItem.md)

    Shell item interface on the parent folder

  - Name : str

    Relative name of an item within the parent folder

  - ctx : [PyIBindCtx](PyIBindCtx.md)

    Bind context for parsing, can be None

  - riid : [PyIID](PyIID.md)

    The interface to return, IID\_IShellItem or IID\_IShellItem2

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateItemInKnownFolder

[PyIShellItem](PyIShellItem.md) = SHCreateItemInKnownFolder\(FolderId, Flags

, Name

, riid

\)
Creates a Shell item object for a single file that exists inside a known folder\.

#### Parameters

  - FolderId : [PyIID](PyIID.md)

    The GUID of a known folder \(shell\.FOLDERID\_\*\)

  - Flags : int

    Combination of shellcon\.KF\_FLAG\_\* flags controlling how folder is handled

  - Name : str

    Name of an item in the folder\.  Pass None to bind to the known folder itself\.

  - riid=IID\_IShellItem : [PyIID](PyIID.md)

    The interface to return, usually IID\_IShellItem or IID\_IShellItem2

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateItemWithParent

[PyIShellItem](PyIShellItem.md) = SHCreateItemWithParent\(Parent, sfParent

, child

, riid

\)
Create a Shell item, given a parent folder and a child item ID\.

#### Parameters

  - Parent : [PyIDL](PyIDL.md)

    Absolute item id list of the parent folder\.  Pass None if the below shell folder is used\.

  - sfParent : [PyIShellFolder](PyIShellFolder.md)

    Parent folder object\.  Can be None if parent id list is specified\.

  - child : [PyIDL](PyIDL.md)

    Relative item id list for an object in the parent folder

  - riid=IID\_IShellItem : [PyIID](PyIID.md)

    The interface to return, usually IID\_IShellItem or IID\_IShellItem2

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateShellFolderView

[PyIShellView](PyIShellView.md) = SHCreateShellFolderView\(sf, viewOuter

, callbacks

\)
Creates a new instance of the default Shell folder view object\.

#### Parameters

  - sf : [PyIShellFolder](PyIShellFolder.md)

    

  - viewOuter=None : [PyIShellView](PyIShellView.md)

    

  - callbacks=None : PyIShellFolderViewCB

    


## [shell](shell.md#shell)\.SHCreateShellItem

[PyIShellItem](PyIShellItem.md) = SHCreateShellItem\(pidlParent, sfParent

, Child

\)
Creates an IShellItem interface from a PIDL

#### Parameters

  - pidlParent : [PyIDL](PyIDL.md)

    PIDL of parent folder, can be None

  - sfParent : [PyIShellFolder](PyIShellFolder.md)

    IShellFolder interface of parent folder, can be None

  - Child : [PyIDL](PyIDL.md)

    PIDL identifying desired item\.  Must be an absolute PIDL if parent is not specified\.

#### Comments

This function is only available on XP and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateShellItemArray

[PyIShellItemArray](PyIShellItemArray.md) = SHCreateShellItemArray\(parent, sf

, children

\)
Creates a Shell item array object\.

#### Parameters

  - parent : [PyIDL](PyIDL.md)

    Absolute ID list of parent folder, or None if sf is specified

  - sf : [PyIShellFolder](PyIShellFolder.md)

    The Shell data source object that is the parent of the child items specified in children\. If parent is specified, this parameter can be NULL\. 

bNoneOK \*/\)\)

  - children : \[[PyIDL](PyIDL.md), \.\.\.\]

    Sequence of relative IDLs for items in the parent folder

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateShellItemArrayFromDataObject

[PyIShellItemArray](PyIShellItemArray.md) = SHCreateShellItemArrayFromDataObject\(do, iid

\)
Creates a shell item array from an IDataObject 

interface that contains a list of items \(eg CF\_HDROP\)

#### Parameters

  - do : [PyIDataObject](PyIDataObject.md)

    A data object that can be rendered as a list of items

  - iid=IID\_IShellItemArray : [PyIID](PyIID.md)

    The interface to create

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateShellItemArrayFromIDLists

[PyIShellItemArray](PyIShellItemArray.md) = SHCreateShellItemArrayFromIDLists\(pidls\)
Creates a shell item array from a number of item identifiers

#### Parameters

  - pidls : \[[PyIDL](PyIDL.md), \.\.\.\]

    A sequence of absolute IDLs\.

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateShellItemArrayFromShellItem

[PyIShellItemArray](PyIShellItemArray.md) = SHCreateShellItemArrayFromShellItem\(si, riid

\)
Creates an item array containing a single item

#### Parameters

  - si : [PyIShellItem](PyIShellItem.md)

    A shell item 

bNoneOK \*/\)\)

  - riid=IID\_IShellItemArray : [PyIID](PyIID.md)

    The interface to return

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHCreateStreamOnFileEx

[PyIStream](PyIStream.md) = SHCreateStreamOnFileEx\(File, Mode

, Attributes

, Create

, Template

\)
Creates an IStream interface that reads and writes to a file

#### Parameters

  - File : str

    Name of file to be connected to the stream

  - Mode : int

    Combination of storagecon\.STGM\_\* flags specifying the access mode

  - Attributes : int

    Combination of win32con\.FILE\_ATTRIBUTE\_\* flags

  - Create : bool

    Determines if function should fail when file exists \(see MSDN docs for full explanation\)

  - Template=None : None

    Reserved, use only None

#### Comments

Accepts keyword args\.

This function is only available on WinXP and later\. 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHEmptyRecycleBin

SHEmptyRecycleBin\(hwnd, path, flags\)
Empties the recycle bin on the specified drive\.

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Handle to parent window, can be None

  - path : string

    A NULL-terminated string that contains the path of the root drive on which the recycle bin is located\. This parameter can contain the address of a string formatted with the drive, folder, and subfolder names \(c:\\\\windows\\\\system \. \. \.\)\. It can also contain an empty string or NULL\. If this value is an empty string or NULL, all recycle bins on all drives will be emptied\.

  - flags : int

    One of the SHERB\_\* values\.

#### Comments

This method is only available in shell version 4\.71\.  If the function is not available, a COM Exception with HRESULT=E\_NOTIMPL will be raised\.


## [shell](shell.md#shell)\.SHFileOperation

int, int = SHFileOperation\(operation\)
Copies, moves, renames, or deletes a file system object\.

#### Parameters

  - operation : [SHFILEOPSTRUCT](SHFILEOPSTRUCT.md)

    Defines the operation to perform\.

#### Return Value
The result is a tuple containing int result of the function itself, and the result of the 

fAnyOperationsAborted member after the operation\.  If Flags contains FOF\_WANTMAPPINGHANDLE, 

returned tuple will have a 3rd member containing a sequence of 2-tuples with the old and new file names 

of renamed files\.  This will only have any content if FOF\_RENAMEONCOLLISION was specified, and some 

filename conflicts actually occurred\.


## [shell](shell.md#shell)\.SHGetDesktopFolder

[PyIShellFolder](PyIShellFolder.md) = SHGetDesktopFolder\(\)
Retrieves the [PyIShellFolder](PyIShellFolder.md) interface for the desktop folder, which is the root of the shell's namespace\.


## [shell](shell.md#shell)\.SHGetFileInfo

int, [SHFILEINFO](SHFILEINFO.md) = SHGetFileInfo\(name, dwFileAttributes

, uFlags

, infoAttrs

\)
Retrieves information about an object in the file system, such as a file, a folder, a directory, or a drive root\.

#### Parameters

  - name : string/[PyIDL](PyIDL.md)

    The path and file name\. Both absolute 

and relative paths are valid\. 

If the uFlags parameter includes the SHGFI\_PIDL flag, this parameter 

must be a valid [PyIDL](PyIDL.md) object that uniquely identifies the file within 

the shell's namespace\. The PIDL must be a fully qualified PIDL\. 

Relative PIDLs are not allowed\. 

If the uFlags parameter includes the SHGFI\_USEFILEATTRIBUTES flag, this parameter does not have to be a valid file name\. 

The function will proceed as if the file exists with the specified name 

and with the file attributes passed in the dwFileAttributes parameter\. 

This allows you to obtain information about a file type by passing 

just the extension for pszPath and passing FILE\_ATTRIBUTE\_NORMAL 

in dwFileAttributes\. 

This string can use either short \(the 8\.3 form\) or long file names\.

  - dwFileAttributes : int

    Combination of one or more file attribute flags \(FILE\_ATTRIBUTE\_ values\)\. If uFlags does not include the SHGFI\_USEFILEATTRIBUTES flag, this parameter is ignored\.

  - uFlags : int

    Combination of shellcon\.SHGFI\_\* flags that specify the file information to retrieve\.  See MSDN for details

  - infoAttrs=0 : int

    Flags copied to the SHFILEINFO\.dwAttributes member - useful when flags contains SHGFI\_ATTR\_SPECIFIED


## [shell](shell.md#shell)\.SHGetFolderLocation

[PyIDL](PyIDL.md) = SHGetFolderLocation\(hwndOwner, nFolder

, hToken

, reserved

\)
Retrieves the PIDL of a folder\.

#### Parameters

  - hwndOwner : int

    Window in which to display any neccessary dialogs

  - nFolder : int

    One of the CSIDL\_\* constants specifying the path\.

  - hToken=None : [PyHANDLE](PyHANDLE.md)

    An access token that can be used to represent a particular user, or None

  - reserved=0 : int

    Must be 0

#### Comments

This method is only available with version 5 or later of the shell controls


## [shell](shell.md#shell)\.SHGetFolderPath

string/[PyUnicode](PyUnicode.md) = SHGetFolderPath\(hwndOwner, nFolder

, handle

, flags

\)
Retrieves the path of a folder\.

#### Parameters

  - hwndOwner : [PyHANDLE](PyHANDLE.md)

    Parent window, can be None \(or 0\)

  - nFolder : int

    One of the CSIDL\_\* constants specifying the path\.

  - handle : [PyHANDLE](PyHANDLE.md)

    An access token that can be used to represent a particular user, or None

  - flags : int

    Controls which path is returned\.  May be SHGFP\_TYPE\_CURRENT or SHGFP\_TYPE\_DEFAULT

#### Comments

This method is only available with later versions of shell32\.dll, or if you have shfolder\.dll installed on earlier systems


## [shell](shell.md#shell)\.SHGetIDListFromObject

[PyIDL](PyIDL.md) = SHGetIDListFromObject\(unk\)
Retrieves the PIDL of an object\.

#### Parameters

  - unk : [PyIUnknown](PyIUnknown.md)

    

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHGetInstanceExplorer

[PyIUnknown](PyIUnknown.md) = SHGetInstanceExplorer\(\)
Allows components that run in a Web browser \(Iexplore\.exe\) or a nondefault Windows Explorer \(Explorer\.exe\) process to hold a reference to the process\. The components can use the reference to prevent the process from closing prematurely\.

#### Comments

SHGetInstanceExplorer succeeds only if it is called from within 

an Explorer\.exe or Iexplorer\.exe process\. It is typically used by 

components that run in the context of the Web browser \(Iexplore\.exe\)\. 

However, it is also useful when Explorer\.exe has been configured to 

run all folders in a second process\. SHGetInstanceExplorer fails if 

the component is running in the default Explorer\.exe process\. There 

is no need to hold a reference to this process, as it is shut down 

only when the user logs out\.


## [shell](shell.md#shell)\.SHGetNameFromIDList

str = SHGetNameFromIDList\(pidl, flags

\)
Retrieves the display name of an item from an ID list\.

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    Absolute ID list of the item

  - flags : int

    Type of name to return, shellcon\.SIGDN\_\*

#### Comments

This function is only available on Vista and later; a 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHGetPathFromIDList

string = SHGetPathFromIDList\(idl\)
Converts an IDLIST to a path\.

#### Parameters

  - idl : [PyIDL](PyIDL.md)

    The ITEMIDLIST


## [shell](shell.md#shell)\.SHGetPathFromIDListW

[PyUnicode](PyUnicode.md) = SHGetPathFromIDListW\(idl\)
Converts an IDLIST to a path\.

#### Parameters

  - idl : [PyIDL](PyIDL.md)

    The ITEMIDLIST


## [shell](shell.md#shell)\.SHGetSettings

dict = SHGetSettings\(mask\)
Retrieves the current shell option settings\.

#### Parameters

  - mask=-1 : int

    The values being requested - one of the shellcon\.SSF\_\* constants

#### Comments

This method is only available in shell version 4\.71\.  If the 

function is not available, a COM Exception with HRESULT=E\_NOTIMPL 

will be raised\.

#### Return Value
The result is a dictionary, the contents of which depend on 

the mask param\.  Key names are the same as the SHELLFLAGSTATE 

structure members - 'fShowExtensions', 'fNoConfirmRecycle', etc


## [shell](shell.md#shell)\.SHGetSpecialFolderLocation

[PyIDL](PyIDL.md) = SHGetSpecialFolderLocation\(hwndOwner, nFolder

\)
Retrieves the PIDL of a special folder\.

#### Parameters

  - hwndOwner : [PyHANDLE](PyHANDLE.md)

    Parent window, can be None \(or 0\)

  - nFolder : int

    One of the CSIDL\_\* constants specifying the path\.


## [shell](shell.md#shell)\.SHGetSpecialFolderPath

[PyUnicode](PyUnicode.md) = SHGetSpecialFolderPath\(hwndOwner, nFolder

, bCreate

\)
Retrieves the path of a special folder\.

#### Parameters

  - hwndOwner : [PyHANDLE](PyHANDLE.md)

    Parent window, can be None \(or 0\)

  - nFolder : int

    One of the CSIDL\_\* constants specifying the path\.

  - bCreate=0 : int

    Should the path be created\.

#### Comments

This method is only available in shell version 4\.71\.  If the 

function is not available, a COM Exception with HRESULT=E\_NOTIMPL 

will be raised\.  If the function fails, a COM Exception with 

HRESULT=E\_FAIL will be raised\.


## [shell](shell.md#shell)\.SHGetViewStatePropertyBag

[PyIPropertyBag](PyIPropertyBag.md) = SHGetViewStatePropertyBag\(pidl, BagName

, Flags

, riid

\)
Retrieves an interface for the view state of a folder

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    An item id list that identifies the folder

  - BagName : [PyUnicode](PyUnicode.md)

    Name of the property bag to retrieve

  - Flags : int

    Combination of SHGVSPB\_\* flags

  - riid : [PyIID](PyIID.md)

    The interface to return, usually IID\_IPropertyBag

#### Comments

This function will also return IPropertyBag2, but we don't have a python implementation of this interface yet


## [shell](shell.md#shell)\.SHILCreateFromPath

\([PyIDL](PyIDL.md), int\) = SHILCreateFromPath\(Path, Flags

\)
Retrieves the PIDL and attributes for a path

#### Parameters

  - Path : [PyUnicode](PyUnicode.md)

    The path whose PIDL will be returned

  - Flags : int

    A combination of SFGAO\_\* constants as used with GetAttributesOf

#### Return Value
Returns the PIDL for the given path and any requested attributes


## [shell](shell.md#shell)\.SHOpenFolderAndSelectItems

SHOpenFolderAndSelectItems\(Folder, Items, Flags\)
Displays a shell folder with items pre-selected

#### Parameters

  - Folder : [PyIDL](PyIDL.md)

    An absolute item id list identifying a shell folder

  - Items : \([PyIDL](PyIDL.md),\.\.\.\)

    A sequence of relative item ids identifying items in the folder

  - Flags=0 : int

    Combination of OFASI\_\* flags \(not used on XP\)

#### Comments

This function is only available on XP and later\. 

COM exception with E\_NOTIMPL will be thrown if the function can't be located\.


## [shell](shell.md#shell)\.SHParseDisplayName

\([PyIDL](PyIDL.md), int\) = SHParseDisplayName\(Name, Attributes

, BindCtx

\)
Translates a display name into a shell item identifier

#### Parameters

  - Name : str

    Display name of a shell item, such as a file path

  - Attributes : int

    Bitmask of shell attributes to retrieve, combination of shellcon\.SFGAO\_\*

  - BindCtx=None : [PyIBindCtx](PyIBindCtx.md)

    Bind context, can be None

#### Comments

Accepts keyword args

Requires XP or later

#### Return Value
Returns the item id list and any requested attribute flags


## [shell](shell.md#shell)\.SHQueryRecycleBin

long,long = SHQueryRecycleBin\(RootPath\)
Retrieves the total size and number of items in the Recycle Bin for a specified drive

#### Parameters

  - RootPath=None : [PyUnicode](PyUnicode.md)

    A path containing the drive whose recycle bin will be queried, or None for all drives


## [shell](shell.md#shell)\.SHSetFolderPath

SHSetFolderPath\(csidl, Path, hToken\)
Sets the location of one of the special folders

#### Parameters

  - csidl : int

    One of the shellcon\.CSIDL\_\* values

  - Path : str/unicode

    The full path to be set

  - hToken=None : [PyHANDLE](PyHANDLE.md)

    Handle to an access token, can be None

#### Comments

This function is only available on Windows 2000 or later


## [shell](shell.md#shell)\.SHUpdateImage

SHUpdateImage\(HashItem, Index, Flags, ImageIndex\)
Notifies the shell that an image in the system image list has changed\.

#### Parameters

  - HashItem : string

    Full path of file containing the icon as returned by [PyIExtractIcon::GetIconLocation](PyIExtractIcon.md#pyiextracticongeticonlocation)

  - Index : int

    Index of the icon in the above file

  - Flags : int

    GIL\_NOTFILENAME or GIL\_SIMULATEDOC

  - ImageIndex : int

    Index of the icon in the system image list


## [shell](shell.md#shell)\.SetCurrentProcessExplicitAppUserModelID

SetCurrentProcessExplicitAppUserModelID\(AppID\)
Sets the taskbar identifier

#### Parameters

  - AppID : str

    The Application User Model ID used to group taskbar buttons

#### Comments

Should be used early in process startup before creating any windows

Requires Windows 7 or later


## [shell](shell.md#shell)\.ShellExecuteEx

dict = ShellExecuteEx\(fMask, hwnd

, lpVerb

, lpFile

, lpParameters

, lpDirectory

, nShow

, lpIDList

, obClass

, hkeyClass

, dwHotKey

, hIcon

, hMonitor

\)
Performs an operation on a file\.

#### Parameters

  - fMask=0 : int

    The default mask for the structure\.  Other 

masks may be added based on what paramaters are supplied\.

  - hwnd=0 : [PyHANDLE](PyHANDLE.md)

    

  - lpVerb : string

    

  - lpFile : string

    

  - lpParameters : string

    

  - lpDirectory : string

    

  - nShow=0 : int

    

  - lpIDList : [PyIDL](PyIDL.md)

    

  - obClass : string

    

  - hkeyClass : int

    

  - dwHotKey : int

    

  - hIcon : [PyHANDLE](PyHANDLE.md)

    

  - hMonitor : [PyHANDLE](PyHANDLE.md)

    

#### Return Value
The result is a dictionary based on documented result values 

in the structure\.  Currently this is "hInstApp" and "hProcess"


## [shell](shell.md#shell)\.StringAsCIDA

[PyIDL](PyIDL.md), list = StringAsCIDA\(pidl\)
Given a CIDA as a raw string, return the folder PIDL and list of children

#### Parameters

  - pidl : string

    The PIDL as a raw string\.

#### Return Value
The result is the PIDL of the folder, and a list of child PIDLs\.


## [shell](shell.md#shell)\.StringAsFILEGROUPDESCRIPTOR

\[dict, \.\.\.\] = StringAsFILEGROUPDESCRIPTOR\(buf, make\_unicode

\)
Decodes a FILEGROUPDESCRIPTOR packed in a string

#### Parameters

  - buf : buffer

    A string packed as either FILEGROUPDESCRIPTORW or FILEGROUPDESCRIPTORW

  - make\_unicode=-1 : bool

    Should this be treated as a FILEDESCRIPTORW?  If -1 

the size of the buffer will be used to make that determination\.  Thus, if 

the buffer is not the exact size of a correct FILEDESCRIPTORW or FILEDESCRIPTORA, 

you will need to specify this parameter\.


## [shell](shell.md#shell)\.StringAsPIDL

[PyIDL](PyIDL.md) = StringAsPIDL\(pidl\)
Given a PIDL as a raw string, return a PIDL object \(ie, a list of strings\)

#### Parameters

  - pidl : string

    The PIDL as a raw string\.