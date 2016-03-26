# PyIKnownFolderManager


## PyIKnownFolderManager Object

Interface used to manage known folder definitions\.

#### Methods

  - [FolderIdFromCsidl](PyIKnownFolderManager.md#pyiknownfoldermanagerfolderidfromcsidl)

    Returns the folder id that corresponds to a CSIDL&nbsp;

  - [FolderIdToCsidl](PyIKnownFolderManager.md#pyiknownfoldermanagerfolderidtocsidl)

    Returns the CSIDL equivalent of a known folder&nbsp;

  - [GetFolderIds](PyIKnownFolderManager.md#pyiknownfoldermanagergetfolderids)

    Retrieves all known folder ids\.&nbsp;

  - [GetFolder](PyIKnownFolderManager.md#pyiknownfoldermanagergetfolder)

    Returns a folder by its id&nbsp;

  - [GetFolderByName](PyIKnownFolderManager.md#pyiknownfoldermanagergetfolderbyname)

    Returns a folder by its canonical name&nbsp;

  - [RegisterFolder](PyIKnownFolderManager.md#pyiknownfoldermanagerregisterfolder)

    Defines a new known folder&nbsp;

  - [UnregisterFolder](PyIKnownFolderManager.md#pyiknownfoldermanagerunregisterfolder)

    Removes the definition of a known folder&nbsp;

  - [FindFolderFromPath](PyIKnownFolderManager.md#pyiknownfoldermanagerfindfolderfrompath)

    Retrieves a known folder by path&nbsp;

  - [FindFolderFromIDList](PyIKnownFolderManager.md#pyiknownfoldermanagerfindfolderfromidlist)

    Retrieves a known folder using its item id list\.&nbsp;

  - [Redirect](PyIKnownFolderManager.md#pyiknownfoldermanagerredirect)

    Redirects a known folder to an alternate location&nbsp;


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.FindFolderFromIDList

[PyIKnownFolder](PyIKnownFolder.md) = FindFolderFromIDList\(pidl\)
Retrieves a known folder using its item id list\.

#### Parameters

  - pidl : [PyIDL](PyIDL.md)

    Item id list of the folder


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.FindFolderFromPath

[PyIKnownFolder](PyIKnownFolder.md) = FindFolderFromPath\(Path, Mode

\)
Retrieves a known folder by path

#### Parameters

  - Path : str

    Path of a folder

  - Mode : int

    FFFP\_EXACTMATCH or FFFP\_NEARESTPARENTMATCH


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.FolderIdFromCsidl

[PyIID](PyIID.md) = FolderIdFromCsidl\(Csidl\)
Returns the folder id that corresponds to a CSIDL

#### Parameters

  - Csidl : int

    The legacy CSIDL identifying a folder


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.FolderIdToCsidl

int = FolderIdToCsidl\(id\)
Returns the CSIDL equivalent of a known folder

#### Parameters

  - id : [PyIID](PyIID.md)

    A known folder id \(shell\.FOLDERID\_\*\)


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.GetFolder

[PyIKnownFolder](PyIKnownFolder.md) = GetFolder\(id\)
Returns a folder by its id\.

#### Parameters

  - id : [PyIID](PyIID.md)

    A known folder id \(shell\.FOLDERID\_\*\)


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.GetFolderByName

[PyIKnownFolder](PyIKnownFolder.md) = GetFolderByName\(Name\)
Returns a folder by canonical name

#### Parameters

  - Name : str

    The nonlocalized name of a known folder


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.GetFolderIds

\([PyIID](PyIID.md),\.\.\.\) = GetFolderIds\(\)
Retrieves all known folder ids\.


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.Redirect

Redirect\(id, hwnd, flags, TargetPath, Exclusion\)
Redirects a known folder to an alternate location

#### Parameters

  - id : [PyIID](PyIID.md)

    Id of the known folder to be redirected

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Handle of window to be used for user interaction

  - flags : int

    Combination of KF\_REDIRECT\_\* flags

  - TargetPath : str

    Path to which the known folder will be redirected

  - Exclusion : \([PyIID](PyIID.md),\.\.\.\)

    Sequence of known folder ids of subfolders to be excluded from redirection


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.RegisterFolder

RegisterFolder\(id, Definition\)
Defines a new known folder

#### Parameters

  - id : [PyIID](PyIID.md)

    GUID used to identify the new known folder

  - Definition : dict

    Dictionary containing info to be placed in a KNOWNFOLDER\_DEFINITION struct

#### Comments

[PyIKnownFolder::GetFolderDefinition](PyIKnownFolder.md#pyiknownfoldergetfolderdefinition) can be used to get a template dictionary


## [PyIKnownFolderManager](PyIKnownFolderManager.md#pyiknownfoldermanager)\.UnregisterFolder

UnregisterFolder\(id\)
Removes the definition of a known folder

#### Parameters

  - id : [PyIID](PyIID.md)

    GUID of a known folder to be unregistered