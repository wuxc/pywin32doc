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

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.FindFolderFromIDList

[PyIKnownFolder](#pyiknownfolder)\= **FindFolderFromIDList\( *pidl* ** \)
Retrieves a known folder using its item id list\.

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    Item id list of the folder

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.FindFolderFromPath

[PyIKnownFolder](#pyiknownfolder)\= **FindFolderFromPath\( *Path*  *, Mode* ** \)
Retrieves a known folder by path

#### Parameters


  -  *Path* : str

    Path of a folder

  -  *Mode* : int

    FFFP\_EXACTMATCH or FFFP\_NEARESTPARENTMATCH

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.FolderIdFromCsidl

[PyIID](#pyiid)\= **FolderIdFromCsidl\( *Csidl* ** \)
Returns the folder id that corresponds to a CSIDL

#### Parameters


  -  *Csidl* : int

    The legacy CSIDL identifying a folder

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.FolderIdToCsidl

int \= **FolderIdToCsidl\( *id* ** \)
Returns the CSIDL equivalent of a known folder

#### Parameters


  -  *id* :[PyIID](#pyiid)

    A known folder id \(shell\.FOLDERID\_\*\)

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.GetFolder

[PyIKnownFolder](#pyiknownfolder)\= **GetFolder\( *id* ** \)
Returns a folder by its id\.

#### Parameters


  -  *id* :[PyIID](#pyiid)

    A known folder id \(shell\.FOLDERID\_\*\)

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.GetFolderByName

[PyIKnownFolder](#pyiknownfolder)\= **GetFolderByName\( *Name* ** \)
Returns a folder by canonical name

#### Parameters


  -  *Name* : str

    The nonlocalized name of a known folder

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.GetFolderIds

\([PyIID](#pyiid),\.\.\.\) \= **GetFolderIds\(** \)
Retrieves all known folder ids\.

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.Redirect

 **Redirect\( *id*  *, hwnd*  *, flags*  *, TargetPath*  *, Exclusion* ** \)
Redirects a known folder to an alternate location

#### Parameters


  -  *id* :[PyIID](#pyiid)

    Id of the known folder to be redirected

  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle of window to be used for user interaction

  -  *flags* : int

    Combination of KF\_REDIRECT\_\* flags

  -  *TargetPath* : str

    Path to which the known folder will be redirected

  -  *Exclusion* : \([PyIID](#pyiid),\.\.\.\)

    Sequence of known folder ids of subfolders to be excluded from redirection

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.RegisterFolder

 **RegisterFolder\( *id*  *, Definition* ** \)
Defines a new known folder

#### Parameters


  -  *id* :[PyIID](#pyiid)

    GUID used to identify the new known folder

  -  *Definition* : dict

    Dictionary containing info to be placed in a KNOWNFOLDER\_DEFINITION struct

#### Comments
[PyIKnownFolder::GetFolderDefinition](PyIKnownFolder.md#pyiknownfoldergetfolderdefinition)can be used to get a template dictionary

## [PyIKnownFolderManager](#pyiknownfoldermanager)\.UnregisterFolder

 **UnregisterFolder\( *id* ** \)
Removes the definition of a known folder

#### Parameters


  -  *id* :[PyIID](#pyiid)

    GUID of a known folder to be unregistered