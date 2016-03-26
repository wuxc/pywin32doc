# PyIShellLibrary


## PyIShellLibrary Object

Interface used to access Libraries

#### Comments

Requires Windows 7 or later

#### Methods

  - [LoadLibraryFromItem](PyIShellLibrary.md#pyishelllibraryloadlibraryfromitem)

    Loads an existing library file&nbsp;

  - [LoadLibraryFromKnownFolder](PyIShellLibrary.md#pyishelllibraryloadlibraryfromknownfolder)

    Initializes library from a known folder&nbsp;

  - [AddFolder](PyIShellLibrary.md#pyishelllibraryaddfolder)

    Includes a folder in the library&nbsp;

  - [RemoveFolder](PyIShellLibrary.md#pyishelllibraryremovefolder)

    Removes a folder&nbsp;

  - [GetFolders](PyIShellLibrary.md#pyishelllibrarygetfolders)

    Retrieves a collection of folders in the library&nbsp;

  - [ResolveFolder](PyIShellLibrary.md#pyishelllibraryresolvefolder)

    Attempts to locate a folder that has been moved or renamed&nbsp;

  - [GetDefaultSaveFolder](PyIShellLibrary.md#pyishelllibrarygetdefaultsavefolder)

    Returns the default folder in which new items are saved&nbsp;

  - [SetDefaultSaveFolder](PyIShellLibrary.md#pyishelllibrarysetdefaultsavefolder)

    Sets the default save location&nbsp;

  - [GetOptions](PyIShellLibrary.md#pyishelllibrarygetoptions)

    Retrieves library option flags&nbsp;

  - [SetOptions](PyIShellLibrary.md#pyishelllibrarysetoptions)

    Sets library option flags&nbsp;

  - [GetFolderType](PyIShellLibrary.md#pyishelllibrarygetfoldertype)

    Retrieves the folder type of the library&nbsp;

  - [SetFolderType](PyIShellLibrary.md#pyishelllibrarysetfoldertype)

    Sets the folder type of the library&nbsp;

  - [GetIcon](PyIShellLibrary.md#pyishelllibrarygeticon)

    Returns the location of the library's icon&nbsp;

  - [SetIcon](PyIShellLibrary.md#pyishelllibraryseticon)

    Sets the library icon&nbsp;

  - [Commit](PyIShellLibrary.md#pyishelllibrarycommit)

    Saves changes \(only if loaded from an existing library\)&nbsp;

  - [Save](PyIShellLibrary.md#pyishelllibrarysave)

    Saves the library to a specific location&nbsp;

  - [SaveInKnownFolder](PyIShellLibrary.md#pyishelllibrarysaveinknownfolder)

    Saves the library in a known folder&nbsp;


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.AddFolder

AddFolder\(Location\)
Includes a folder

#### Parameters

  - Location : [PyIShellItem](PyIShellItem.md)

    Shell item interface representing the folder


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.Commit

Commit\(\)
Saves changes \(only if loaded from an existing library\)


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.GetDefaultSaveFolder

[PyIShellItem](PyIShellItem.md) = GetDefaultSaveFolder\(Type, riid

\)
Returns the default folder in which new items are saved

#### Parameters

  - Type=DSFT\_DETECT : int

    Specifies whether to return public or private save location, shellcon\.DSFT\_\*

  - riid=IID\_IShellItem : [PyIID](PyIID.md)

    The interface to return


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.GetFolderType

[PyIID](PyIID.md) = GetFolderType\(\)
Returns the library type, shell\.FOLDERTYPEID\_\*


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.GetFolders

[PyIShellItemArray](PyIShellItemArray.md) = GetFolders\(Filter, riid

\)
Retrieves a collection of folders in the library

#### Parameters

  - Filter=LFF\_ALLITEMS : int

    Specifies what types of folder to return \(shellcon\.LFF\_\*\)

  - riid=IID\_IShellItemArray : [PyIID](PyIID.md)

    The interface to return, IObjectCollection and IObjectArray also accepted\.


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.GetIcon

str = GetIcon\(\)
Returns the location of the library's icon

#### Return Value
Uses "module,resource" format


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.GetOptions

int = GetOptions\(\)
Retrieves library option flags

#### Return Value
Returns a combination of shellcon\.LOF\_\* flags


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.LoadLibraryFromItem

LoadLibraryFromItem\(Library, Mode\)
Loads an existing library file

#### Parameters

  - Library : [PyIShellItem](PyIShellItem.md)

    Shell item interface representing the library file

  - Mode : int

    Access mode, combination of storagecon\.STGM\_\* flags


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.LoadLibraryFromKnownFolder

LoadLibraryFromKnownFolder\(Library, Mode\)
Initializes library from a known folder

#### Parameters

  - Library : [PyIID](PyIID.md)

    Known folder id, shell\.FOLDERID\_\*

  - Mode : int

    Access mode, combination of storagecon\.STGM\_\* flags


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.RemoveFolder

RemoveFolder\(Location\)
Removes a folder

#### Parameters

  - Location : [PyIShellItem](PyIShellItem.md)

    Shell item interface representing the folder


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.ResolveFolder

[PyIShellItem](PyIShellItem.md) = ResolveFolder\(FolderToResolve, Timeout

, riid

\)
Attempts to locate a folder that has been moved or renamed

#### Parameters

  - FolderToResolve : [PyIShellItem](PyIShellItem.md)

    Library item whose location has changed

  - Timeout : int

    Max search time, specified in milliseconds

  - riid=IID\_IShellItem : [PyIID](PyIID.md)

    The interface to return


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.Save

[PyIShellItem](PyIShellItem.md) = Save\(FolderToSaveIn, LibraryName

, Flags

\)
Saves the library to a specific location

#### Parameters

  - FolderToSaveIn : [PyIShellItem](PyIShellItem.md)

    The destination folder, use None to save in current user's Libraries folder

  - LibraryName : str

    Filename for the new library, without file extension

  - Flags : int

    Determines behaviour if file already exists, shellcon\.LSF\_\*

#### Return Value
Returns a shell item for the saved file\.


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.SaveInKnownFolder

[PyIShellItem](PyIShellItem.md) = SaveInKnownFolder\(FolderToSaveIn, LibraryName

, Flags

\)
Saves the library in a known folder

#### Parameters

  - FolderToSaveIn : [PyIID](PyIID.md)

    The destination folder, shell\.FOLDERID\_\*

  - LibraryName : str

    Filename for the new library, without file extension

  - Flags : int

    Determines behaviour if file already exists, shellcon\.LSF\_\*


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.SetDefaultSaveFolder

SetDefaultSaveFolder\(Type, SaveFolder\)
Sets the default save location

#### Parameters

  - Type : int

    Specifies public or private save location, shellcon\.DSFT\_\*

  - SaveFolder : [PyIShellItem](PyIShellItem.md)

    New default location, must be in the library


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.SetFolderType

SetFolderType\(Type\)
Sets the folder type for the library

#### Parameters

  - Type : [PyIID](PyIID.md)

    New type, shell\.FOLDERTYPEID\_\*


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.SetIcon

SetIcon\(Icon\)
Sets the library icon

#### Parameters

  - Icon : str

    Icon location in "module,resource" syntax


## [PyIShellLibrary](PyIShellLibrary.md#pyishelllibrary)\.SetOptions

SetOptions\(Mask, Options\)
Sets library option flags

#### Parameters

  - Mask : int

    Bitmask of flags to be changed, combination of shellcon\.LOF\_\* values

  - Options : int

    New options, combination of shellcon\.LOF\_\* values