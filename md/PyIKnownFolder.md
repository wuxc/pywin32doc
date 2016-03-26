# PyIKnownFolder

## PyIKnownFolder Object

Interface representing a known folder that serves 

as a replacement for the numeric CSIDL definitions and API functions\. 

Requires Vista or later\.

#### Methods


  - [GetId](PyIKnownFolder.md#pyiknownfoldergetid)

    Returns the id of the folder&nbsp;

  - [GetCategory](PyIKnownFolder.md#pyiknownfoldergetcategory)

    Returns the category for a folder \(shellcon\.KF\_CATEGORY\_\*\)&nbsp;

  - [GetShellItem](PyIKnownFolder.md#pyiknownfoldergetshellitem)

    Returns a shell interface for the folder&nbsp;

  - [GetPath](PyIKnownFolder.md#pyiknownfoldergetpath)

    Returns the path to the folder&nbsp;

  - [SetPath](PyIKnownFolder.md#pyiknownfoldersetpath)

    Changes the location of the folder&nbsp;

  - [GetIDList](PyIKnownFolder.md#pyiknownfoldergetidlist)

    Returns the folder's location as an item id list&nbsp;

  - [GetFolderType](PyIKnownFolder.md#pyiknownfoldergetfoldertype)

    Returns the type of the folder&nbsp;

  - [GetRedirectionCapabilities](PyIKnownFolder.md#pyiknownfoldergetredirectioncapabilities)

    Returns flags indicating how the folder can be redirected&nbsp;

  - [GetFolderDefinition](PyIKnownFolder.md#pyiknownfoldergetfolderdefinition)

    Retrieves detailed information about a known folder&nbsp;

## [PyIKnownFolder](#pyiknownfolder)\.GetCategory

int \= **GetCategory\(** \)
Returns the category for a folder \(shellcon\.KF\_CATEGORY\_\*\)

## [PyIKnownFolder](#pyiknownfolder)\.GetFolderDefinition

dict \= **GetFolderDefinition\(** \)
Retrieves detailed information about a known folder

#### Return Value
Returns a dict containing info from a KNOWNFOLDER\_DEFINITION struct

## [PyIKnownFolder](#pyiknownfolder)\.GetFolderType

[PyIID](#pyiid)\= **GetFolderType\(** \)
Returns the type of the folder

#### Return Value
Returns a folder type guid \(shell\.FOLDERTYPEID\_\*\)

## [PyIKnownFolder](#pyiknownfolder)\.GetIDList

[PyIDL](#pyidl)\= **GetIDList\( *Flags* ** \)
Returns the folder's location as an item id list\.

#### Parameters


  -  *Flags* : int

    Combination of shellcon\.KF\_FLAG\_\* values that affect how the operation is performed

## [PyIKnownFolder](#pyiknownfolder)\.GetId

[PyIID](#pyiid)\= **GetId\(** \)
Returns the id of the folder

## [PyIKnownFolder](#pyiknownfolder)\.GetPath

str \= **GetPath\( *Flags* ** \)
Returns the path to the folder

#### Parameters


  -  *Flags\=0* : int

    Combination of shellcon\.KF\_FLAG\_\* flags controlling how the path is returned

## [PyIKnownFolder](#pyiknownfolder)\.GetRedirectionCapabilities

int \= **GetRedirectionCapabilities\(** \)
Returns flags indicating how the folder can be redirected

#### Return Value
Combination of shellcon\.KF\_REDIRECTION\_CAPABILITIES\_\* flags

## [PyIKnownFolder](#pyiknownfolder)\.GetShellItem

[PyIShellItem](#pyishellitem)\= **GetShellItem\( *Flags*  *, riid* ** \)
Returns a shell interface for the folder

#### Parameters


  -  *Flags\=0* : int

    Combination of shellcon\.KF\_FLAG\_\* values

  -  *riid\=IID\_IShellItem* :[PyIID](#pyiid)

    The interface to return \(IShellItem or IShellItem2\)

## [PyIKnownFolder](#pyiknownfolder)\.SetPath

 **SetPath\( *Flags*  *, Path* ** \)
Changes the location of the folder

#### Parameters


  -  *Flags* : int

    KF\_FLAG\_DONT\_UNEXPAND, or 0

  -  *Path* : str

    New path for known folder