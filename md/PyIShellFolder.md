# PyIShellFolder

## PyIShellFolder Object



Interface that represents an Explorer folder

#### Methods


  - [ParseDisplayName](PyIShellFolder.md#pyishellfolderparsedisplayname)

    Returns the PIDL of an item in a shell folder&nbsp;

  - [EnumObjects](PyIShellFolder.md#pyishellfolderenumobjects)

    Creates an enumerator to list the contents of the shell folder&nbsp;

  - [BindToObject](PyIShellFolder.md#pyishellfolderbindtoobject)

    Returns an IShellFolder interface for a subfolder&nbsp;

  - [BindToStorage](PyIShellFolder.md#pyishellfolderbindtostorage)

    Returns an interface to a storage object in a shell folder&nbsp;

  - [CompareIDs](PyIShellFolder.md#pyishellfoldercompareids)

    Determines the sorting order of 2 items in shell folder&nbsp;

  - [CreateViewObject](PyIShellFolder.md#pyishellfoldercreateviewobject)

    Creates a view object for a shell folder\.&nbsp;

  - [GetAttributesOf](PyIShellFolder.md#pyishellfoldergetattributesof)

    Queries attributes of items within the shell folder&nbsp;

  - [GetUIObjectOf](PyIShellFolder.md#pyishellfoldergetuiobjectof)

    Creates an interface to one or more items in a shell folder&nbsp;

  - [GetDisplayNameOf](PyIShellFolder.md#pyishellfoldergetdisplaynameof)

    Returns the display name of an item within this shell folder&nbsp;

  - [SetNameOf](PyIShellFolder.md#pyishellfoldersetnameof)

    Sets the display name of an item and changes its PIDL&nbsp;

  - [\_\_iter\_\_](PyIShellFolder.md#pyishellfolder__iter__)

    Enumerates all objects in this folder\.&nbsp;

## [PyIShellFolder](#pyishellfolder)\.BindToObject

[PyIShellFolder](#pyishellfolder) =BindToObject\(pidl, pbc, riid\)
Returns an IShellFolder interface for a subfolder

#### Parameters


  - pidl :[PyIDL](#pyidl)

    Relative item id list that identifies the subfolder, can be multi-level

  - pbc :[PyIBindCtx](#pyibindctx)

    Bind context to be used, can be None

  - riid :[PyIID](#pyiid)

    IID of the desired interface, usually IID\_IShellFolder

## [PyIShellFolder](#pyishellfolder)\.BindToStorage



interface =BindToStorage\(pidl, pbc, riid\)
Returns an interface to a storage object in a shell folder

#### Parameters


  - pidl :[PyIDL](#pyidl)

    Relative pidl for the folder item, must be a single item id

  - pbc :[PyIBindCtx](#pyibindctx)

    Bind context that affects how binding is performed, can be None

  - riid :[PyIID](#pyiid)

    IID of the desired interface, one of IID\_IStream, IID\_IStorage, IID\_IPropertySetStorage

#### Return Value
Returns[PyIStream](#pyistream),[PyIStorage](#pyistorage) or[PyIPropertySetStorage](#pyipropertysetstorage) depending on the riid passed in

## [PyIShellFolder](#pyishellfolder)\.CompareIDs



int =CompareIDs\(lparam, pidl1, pidl2\)
Determines the sorting order of 2 items in shell folder

#### Parameters


  - lparam : int

    Lower 16 bits specify folder-dependent sorting rules, 0 means to sort by display name\. 

System folder view uses these as a column number\.
 

Upper sixteen bits is used for flags SHCIDS\_ALLFIELDS or SHCIDS\_CANONICALONLY

  - pidl1 :[PyIDL](#pyidl)

    Item id list that idenfies an object relative to the folder

  - pidl2 :[PyIDL](#pyidl)

    Item id list that idenfies an object relative to the folder

#### Return Value
Returns 0 if items compare equal, -1 if the pidl1 comes first, or 1 if pidl2 comes first

## [PyIShellFolder](#pyishellfolder)\.CreateViewObject

[PyIShellView](#pyishellview) =CreateViewObject\(hwndOwner, riid\)
Creates a view object for a shell folder\.

#### Parameters


  - hwndOwner : HWND

    Parent window for a custom folder view, or 0

  - riid :[PyIID](#pyiid)

    IID of the desired interface, usually IID\_IShellView

## [PyIShellFolder](#pyishellfolder)\.EnumObjects

[PyIEnumIDList](#pyienumidlist) =EnumObjects\(hwndOwner, grfFlags\)
Creates an enumerator to list the contents of the shell folder

#### Parameters


  - hwndOwner=None :[PyHANDLE](#pyhandle)

    Window to use if any user interaction is required

  - grfFlags=SHCONTF\_FOLDERS|SHCONTF\_NONFOLDERS|SHCONTF\_INCLUDEHIDDEN : int

    Combination of shellcon\.SHCONTF\_\* constants

## [PyIShellFolder](#pyishellfolder)\.GetAttributesOf



int =GetAttributesOf\(pidl, rgfInOut\)
Queries attributes of items within the shell folder

#### Parameters


  - pidl : \([PyIDL](#pyidl),\.\.\.\)

    A sequence of single-level pidls identifying items directly contained by the folder

  - rgfInOut : int

    Combination of shellcon\.SFGAO\_\* constants

#### Return Value
The requested attributes are only returned if they are common to all of the specified items

## [PyIShellFolder](#pyishellfolder)\.GetDisplayNameOf



str =GetDisplayNameOf\(pidl, uFlags\)
Returns the display name of an item within this shell folder

#### Parameters


  - pidl :[PyIDL](#pyidl)

    PIDL that identifies the item relative to the parent folder

  - uFlags : int

    Combination of shellcon\.SHGDN\_\* flags

## [PyIShellFolder](#pyishellfolder)\.GetUIObjectOf



int,[PyIUnknown](#pyiunknown) =GetUIObjectOf\(hwndOwner, pidl, riid, Reserved, iidout\)
Creates an interface to one or more items in a shell folder

#### Parameters


  - hwndOwner :[PyHANDLE](#pyhandle)

    Specifies a window in which to display any required dialogs or errors, can be 0

  - pidl : \([PyIDL](#pyidl),\.\.\.\)

    A sequence of single-level pidls identifying items in the folder

  - riid :[PyIID](#pyiid)

    The interface to create, one of IID\_IContextMenu, IID\_IContextMenu2, IID\_IDataObject, IID\_IDropTarget, IID\_IExtractIcon, IID\_IQueryInfo

  - Reserved=0 : int

    Reserved, use 0 if passed in

  - iidout=riid :[PyIID](#pyiid)

    The interface to return\.  Can be used in the case where there is not a 

python wrapper for the desired interface\.  You must make certain that the interface identified by riid 

actually supports the iidout interface, or Bad Things Will Happen\. 

It should always be safe to return[PyIUnknown](#pyiunknown), which is the base for all interfaces\.

#### Return Value
Returns the Reserved parameter and the requested interface

## [PyIShellFolder](#pyishellfolder)\.ParseDisplayName



tuple =ParseDisplayName\(hwndOwner, pbc, DisplayName, Attributes\)
Returns the PIDL of an item in a shell folder

#### Parameters


  - hwndOwner :[PyHANDLE](#pyhandle)

    Window in which to display any dialogs or message boxes, can be 0

  - pbc :[PyIBindCtx](#pyibindctx)

    Bind context that affects how parsing is performed, can be None

  - DisplayName : str

    Display name to parse, format is dependent on the shell folder\. 

Desktop folder will accept a file path, as well as guids of the form ::\{guid\} 

Example: '::%s\\\\::%s' %\(shell\.CLSID\_MyComputer,shell\.CLSID\_ControlPanel\)

  - Attributes=0 : int

    Combination of shellcon\.SFGAO\_\* constants specifying which attributes should be returned

#### Return Value
The result is a tuple of cchEaten, pidl, attr

#### Items


  - \[0\]int : cchEaten

    the number of characters of the input name that were parsed

  - \[1\][PyIDL](#pyidl) : pidl

    specifies the relative path from the parsing folder to the object

  - \[2\]int : Attributes

    returns any requested attributes

## [PyIShellFolder](#pyishellfolder)\.SetNameOf

[PyIDL](#pyidl) =SetNameOf\(hwndOwner, pidl, Name, Flags\)
Sets the display name of an item and changes its PIDL

#### Parameters


  - hwndOwner : HWND

    Window in which to display any message boxes or dialogs, can be 0

  - pidl :[PyIDL](#pyidl)

    PIDL that identifies the item relative to the parent folder

  - Name : str

    New name for the item

  - Flags : int

    Combination of shellcon\.SHGDM\_\* values

#### Return Value
Returns the new PIDL for item