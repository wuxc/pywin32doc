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

    Creates a view object for a shell folder.&nbsp;

  - [GetAttributesOf](PyIShellFolder.md#pyishellfoldergetattributesof)

    Queries attributes of items within the shell folder&nbsp;

  - [GetUIObjectOf](PyIShellFolder.md#pyishellfoldergetuiobjectof)

    Creates an interface to one or more items in a shell folder&nbsp;

  - [GetDisplayNameOf](PyIShellFolder.md#pyishellfoldergetdisplaynameof)

    Returns the display name of an item within this shell folder&nbsp;

  - [SetNameOf](PyIShellFolder.md#pyishellfoldersetnameof)

    Sets the display name of an item and changes its PIDL&nbsp;

  - [__iter__](PyIShellFolder.md#pyishellfolder__iter__)

    Enumerates all objects in this folder.&nbsp;

## [PyIShellFolder](#pyishellfolder).BindToObject

[PyIShellFolder](#pyishellfolder)= __BindToObject( *pidl*  *, pbc*  *, riid* __ )
Returns an IShellFolder interface for a subfolder

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    Relative item id list that identifies the subfolder, can be multi-level

  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Bind context to be used, can be None

  -  *riid* :[PyIID](#pyiid)

    IID of the desired interface, usually IID_IShellFolder

## [PyIShellFolder](#pyishellfolder).BindToStorage

interface = __BindToStorage( *pidl*  *, pbc*  *, riid* __ )
Returns an interface to a storage object in a shell folder

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    Relative pidl for the folder item, must be a single item id

  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Bind context that affects how binding is performed, can be None

  -  *riid* :[PyIID](#pyiid)

    IID of the desired interface, one of IID_IStream, IID_IStorage, IID_IPropertySetStorage

#### Return Value
Returns[PyIStream](#pyistream),[PyIStorage](#pyistorage)or[PyIPropertySetStorage](#pyipropertysetstorage)depending on the riid passed in

## [PyIShellFolder](#pyishellfolder).CompareIDs

int = __CompareIDs( *lparam*  *, pidl1*  *, pidl2* __ )
Determines the sorting order of 2 items in shell folder

#### Parameters


  -  *lparam* : int

    Lower 16 bits specify folder-dependent sorting rules, 0 means to sort by display name. 

System folder view uses these as a column number.
Upper sixteen bits is used for flags SHCIDS_ALLFIELDS or SHCIDS_CANONICALONLY

  -  *pidl1* :[PyIDL](#pyidl)

    Item id list that idenfies an object relative to the folder

  -  *pidl2* :[PyIDL](#pyidl)

    Item id list that idenfies an object relative to the folder

#### Return Value
Returns 0 if items compare equal, -1 if the pidl1 comes first, or 1 if pidl2 comes first

## [PyIShellFolder](#pyishellfolder).CreateViewObject

[PyIShellView](#pyishellview)= __CreateViewObject( *hwndOwner*  *, riid* __ )
Creates a view object for a shell folder.

#### Parameters


  -  *hwndOwner* : HWND

    Parent window for a custom folder view, or 0

  -  *riid* :[PyIID](#pyiid)

    IID of the desired interface, usually IID_IShellView

## [PyIShellFolder](#pyishellfolder).EnumObjects

[PyIEnumIDList](#pyienumidlist)= __EnumObjects( *hwndOwner*  *, grfFlags* __ )
Creates an enumerator to list the contents of the shell folder

#### Parameters


  -  *hwndOwner=None* :[PyHANDLE](#pyhandle)

    Window to use if any user interaction is required

  -  *grfFlags=SHCONTF_FOLDERS|SHCONTF_NONFOLDERS|SHCONTF_INCLUDEHIDDEN* : int

    Combination of shellcon.SHCONTF_* constants

## [PyIShellFolder](#pyishellfolder).GetAttributesOf

int = __GetAttributesOf( *pidl*  *, rgfInOut* __ )
Queries attributes of items within the shell folder

#### Parameters


  -  *pidl* : ([PyIDL](#pyidl),...)

    A sequence of single-level pidls identifying items directly contained by the folder

  -  *rgfInOut* : int

    Combination of shellcon.SFGAO_* constants

#### Return Value
The requested attributes are only returned if they are common to all of the specified items

## [PyIShellFolder](#pyishellfolder).GetDisplayNameOf

str = __GetDisplayNameOf( *pidl*  *, uFlags* __ )
Returns the display name of an item within this shell folder

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    PIDL that identifies the item relative to the parent folder

  -  *uFlags* : int

    Combination of shellcon.SHGDN_* flags

## [PyIShellFolder](#pyishellfolder).GetUIObjectOf

int,[PyIUnknown](#pyiunknown)= __GetUIObjectOf( *hwndOwner*  *, pidl*  *, riid*  *, Reserved*  *, iidout* __ )
Creates an interface to one or more items in a shell folder

#### Parameters


  -  *hwndOwner* :[PyHANDLE](#pyhandle)

    Specifies a window in which to display any required dialogs or errors, can be 0

  -  *pidl* : ([PyIDL](#pyidl),...)

    A sequence of single-level pidls identifying items in the folder

  -  *riid* :[PyIID](#pyiid)

    The interface to create, one of IID_IContextMenu, IID_IContextMenu2, IID_IDataObject, IID_IDropTarget, IID_IExtractIcon, IID_IQueryInfo

  -  *Reserved=0* : int

    Reserved, use 0 if passed in

  -  *iidout=riid* :[PyIID](#pyiid)

    The interface to return.  Can be used in the case where there is not a 

python wrapper for the desired interface.  You must make certain that the interface identified by riid 

actually supports the iidout interface, or Bad Things Will Happen. 

It should always be safe to return[PyIUnknown](#pyiunknown), which is the base for all interfaces.

#### Return Value
Returns the Reserved parameter and the requested interface

## [PyIShellFolder](#pyishellfolder).ParseDisplayName

tuple = __ParseDisplayName( *hwndOwner*  *, pbc*  *, DisplayName*  *, Attributes* __ )
Returns the PIDL of an item in a shell folder

#### Parameters


  -  *hwndOwner* :[PyHANDLE](#pyhandle)

    Window in which to display any dialogs or message boxes, can be 0

  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Bind context that affects how parsing is performed, can be None

  -  *DisplayName* : str

    Display name to parse, format is dependent on the shell folder. 

Desktop folder will accept a file path, as well as guids of the form ::{guid} 

Example: '::%s\\::%s' %(shell.CLSID_MyComputer,shell.CLSID_ControlPanel)

  -  *Attributes=0* : int

    Combination of shellcon.SFGAO_* constants specifying which attributes should be returned

#### Return Value
The result is a tuple of cchEaten, pidl, attr

#### Items


  - [0] *int* : cchEaten

    the number of characters of the input name that were parsed

  - [1] *[PyIDL](#pyidl)* : pidl

    specifies the relative path from the parsing folder to the object

  - [2] *int* : Attributes

    returns any requested attributes

## [PyIShellFolder](#pyishellfolder).SetNameOf

[PyIDL](#pyidl)= __SetNameOf( *hwndOwner*  *, pidl*  *, Name*  *, Flags* __ )
Sets the display name of an item and changes its PIDL

#### Parameters


  -  *hwndOwner* : HWND

    Window in which to display any message boxes or dialogs, can be 0

  -  *pidl* :[PyIDL](#pyidl)

    PIDL that identifies the item relative to the parent folder

  -  *Name* : str

    New name for the item

  -  *Flags* : int

    Combination of shellcon.SHGDM_* values

#### Return Value
Returns the new PIDL for item