# PyIKnownFolder

## PyIKnownFolder Object

Interface representing a known folder that serves 

as a replacement for the numeric CSIDL definitions and API functions. 

Requires Vista or later.

#### Methods


  - [GetId](PyIKnownFolder.md#pyiknownfoldergetid)

    Returns the id of the folder&nbsp;

  - [GetCategory](PyIKnownFolder.md#pyiknownfoldergetcategory)

    Returns the category for a folder (shellcon.KF_CATEGORY_*)&nbsp;

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

## [PyIKnownFolder](#pyiknownfolder).GetCategory

int = __GetCategory(__ )
Returns the category for a folder (shellcon.KF_CATEGORY_*)

## [PyIKnownFolder](#pyiknownfolder).GetFolderDefinition

dict = __GetFolderDefinition(__ )
Retrieves detailed information about a known folder

#### Return Value
Returns a dict containing info from a KNOWNFOLDER_DEFINITION struct

## [PyIKnownFolder](#pyiknownfolder).GetFolderType

[PyIID](#pyiid)= __GetFolderType(__ )
Returns the type of the folder

#### Return Value
Returns a folder type guid (shell.FOLDERTYPEID_*)

## [PyIKnownFolder](#pyiknownfolder).GetIDList

[PyIDL](#pyidl)= __GetIDList( *Flags* __ )
Returns the folder's location as an item id list.

#### Parameters


  -  *Flags* : int

    Combination of shellcon.KF_FLAG_* values that affect how the operation is performed

## [PyIKnownFolder](#pyiknownfolder).GetId

[PyIID](#pyiid)= __GetId(__ )
Returns the id of the folder

## [PyIKnownFolder](#pyiknownfolder).GetPath

str = __GetPath( *Flags* __ )
Returns the path to the folder

#### Parameters


  -  *Flags=0* : int

    Combination of shellcon.KF_FLAG_* flags controlling how the path is returned

## [PyIKnownFolder](#pyiknownfolder).GetRedirectionCapabilities

int = __GetRedirectionCapabilities(__ )
Returns flags indicating how the folder can be redirected

#### Return Value
Combination of shellcon.KF_REDIRECTION_CAPABILITIES_* flags

## [PyIKnownFolder](#pyiknownfolder).GetShellItem

[PyIShellItem](#pyishellitem)= __GetShellItem( *Flags*  *, riid* __ )
Returns a shell interface for the folder

#### Parameters


  -  *Flags=0* : int

    Combination of shellcon.KF_FLAG_* values

  -  *riid=IID_IShellItem* :[PyIID](#pyiid)

    The interface to return (IShellItem or IShellItem2)

## [PyIKnownFolder](#pyiknownfolder).SetPath

 __SetPath( *Flags*  *, Path* __ )
Changes the location of the folder

#### Parameters


  -  *Flags* : int

    KF_FLAG_DONT_UNEXPAND, or 0

  -  *Path* : str

    New path for known folder