# PyIShellLink

## PyIShellLink Object

Interface used to access the properties of a shell link file (*.lnk)

#### Methods


  - [GetPath](PyIShellLink.md#pyishelllinkgetpath)

    Retrieves the path and file name of a shell link object.&nbsp;

  - [GetIDList](PyIShellLink.md#pyishelllinkgetidlist)

    Retrieves the item id list that identifies the target of the shell link.&nbsp;

  - [SetIDList](PyIShellLink.md#pyishelllinksetidlist)

    Sets the target of the link using an item id list&nbsp;

  - [GetDescription](PyIShellLink.md#pyishelllinkgetdescription)

    Retrieves the description of the link (displays as Comment in the UI)&nbsp;

  - [SetDescription](PyIShellLink.md#pyishelllinksetdescription)

    Sets the description of the link (displays as Comment in the UI)&nbsp;

  - [GetWorkingDirectory](PyIShellLink.md#pyishelllinkgetworkingdirectory)

    Retrieves the working directory for the link&nbsp;

  - [SetWorkingDirectory](PyIShellLink.md#pyishelllinksetworkingdirectory)

    Sets the working directory for the link&nbsp;

  - [GetArguments](PyIShellLink.md#pyishelllinkgetarguments)

    Retrieves the command-line arguments associated with a shell link object.&nbsp;

  - [SetArguments](PyIShellLink.md#pyishelllinksetarguments)

    Sets the command-line arguments associated with a shell link object.&nbsp;

  - [GetHotkey](PyIShellLink.md#pyishelllinkgethotkey)

    Retrieves the hot key for a shell link object.&nbsp;

  - [SetHotkey](PyIShellLink.md#pyishelllinksethotkey)

    Sets the hot key for a shell link object.&nbsp;

  - [GetShowCmd](PyIShellLink.md#pyishelllinkgetshowcmd)

    Retrieves the show (SW_) command for a shell link object.&nbsp;

  - [SetShowCmd](PyIShellLink.md#pyishelllinksetshowcmd)

    Sets the show (SW_) command for a shell link object.&nbsp;

  - [GetIconLocation](PyIShellLink.md#pyishelllinkgeticonlocation)

    Retrieves the location (path and index) of the icon for a shell link object.&nbsp;

  - [SetIconLocation](PyIShellLink.md#pyishelllinkseticonlocation)

    Sets the location (path and index) of the icon for a shell link object.&nbsp;

  - [SetRelativePath](PyIShellLink.md#pyishelllinksetrelativepath)

    Sets the relative path for a shell link object.&nbsp;

  - [Resolve](PyIShellLink.md#pyishelllinkresolve)

    Resolves a shell link&nbsp;

  - [SetPath](PyIShellLink.md#pyishelllinksetpath)

    Sets the path and file name of a shell link object.&nbsp;

## [PyIShellLink](#pyishelllink).GetArguments

str = __GetArguments( *cchMaxName* __ )
Retrieves the command-line arguments associated with a shell link object.

#### Parameters


  -  *cchMaxName=1024* : int

    Number of characters to fetch.

## [PyIShellLink](#pyishelllink).GetDescription

str = __GetDescription( *cchMaxName* __ )
Retrieves the description of the link (displays as Comment in the UI)

#### Parameters


  -  *cchMaxName=1024* : int

    Number of character to allocate for the retrieved text

## [PyIShellLink](#pyishelllink).GetHotkey

int = __GetHotkey(__ )
Retrieves the hot key for a shell link object.

#### Comments
Note: My tests do not seem to be working. at least, the values returned 

seem not to match what the documentation says should be returned. 

I would expect with a Hotkey of CTRL-ALT-T, to get an integer where 

integer & 256 == ord('T'), i.e. 116 or 84, instead I get 1620

## [PyIShellLink](#pyishelllink).GetIDList

[PyIDL](#pyidl)= __GetIDList(__ )
Retrieves the item id list that identifies the target of the shell link.

## [PyIShellLink](#pyishelllink).GetIconLocation

str = __GetIconLocation( *cchMaxPath* __ )
Retrieves the location (path and index) of the icon for a shell link object.

#### Parameters


  -  *cchMaxPath=_MAX_PATH* : int

    Number of characters to allocate for the result string.

## [PyIShellLink](#pyishelllink).GetPath

str,[WIN32_FIND_DATA](WIN32.md#win32find_data)= __GetPath( *fFlags*  *, cchMaxPath* __ )
Retrieves the target path and file name of a shell link object

#### Parameters


  -  *fFlags* : int

    One of the following values:

 __Value__  __Description__ SLGP_SHORTPATHRetrieves the standard short (8.3 format) file name.SLGP_UNCPRIORITYRetrieves the Universal Naming Convention (UNC) path name of the file.SLGP_RAWPATHRetrieves the raw path name. A raw path is something that might not exist and may include environment variables that need to be expanded.
  -  *cchMaxPath=_MAX_PATH* : int

    Number of characters to allocate for returned filename

#### Comments
The AlternateFileName (8.3) member of WIN32_FIND_DATA does not return information

## [PyIShellLink](#pyishelllink).GetShowCmd

int = __GetShowCmd(__ )
Retrieves the show (SW_) command for a shell link object.

## [PyIShellLink](#pyishelllink).GetWorkingDirectory

str = __GetWorkingDirectory( *cchMaxName* __ )
Retrieves the working directory for the link

#### Parameters


  -  *cchMaxName=1024* : int

    Number of characters to allocate for returned text

## [PyIShellLink](#pyishelllink).Resolve

 __Resolve( *hwnd*  *, fFlags* __ )
Resolves a shell link by searching for the shell link object and updating the 

shell link path and its list of identifiers (if necessary)

#### Parameters


  -  *hwnd* : HWND

    The parent window of a dialog which will pop up if resolution fails.

  -  *fFlags* : int

    One of the following constants:


## [PyIShellLink](#pyishelllink).SetArguments

 __SetArguments( *args* __ )
Sets the command-line arguments associated with a shell link object.

#### Parameters


  -  *args* : str

    The new arguments.

## [PyIShellLink](#pyishelllink).SetDescription

 __SetDescription( *Name* __ )
Sets the description of the link (displays as Comment in the UI)

#### Parameters


  -  *Name* : str

    The description for the link

## [PyIShellLink](#pyishelllink).SetHotkey

 __SetHotkey( *wHotkey* __ )
Sets the hot key for a shell link object.

#### Parameters


  -  *wHotkey* : int

    The virtual key code is in the low-order byte, and the modifier 

flags are in the high-order byte. The modifier flags can be a combination of the 

values specified in the description of the[PyIShellLink::GetHotkey](PyIShellLink.md#pyishelllinkgethotkey)method.

## [PyIShellLink](#pyishelllink).SetIDList

 __SetIDList( *pidl* __ )
Sets the target of the link using an item id list

#### Parameters


  -  *pidl* :[PyIDL](#pyidl)

    Absolute item id list that identifies the target

## [PyIShellLink](#pyishelllink).SetIconLocation

 __SetIconLocation( *iconPath*  *, iIcon* __ )
Sets the location (path and index) of the icon for a shell link object.

#### Parameters


  -  *iconPath* : string

    Path to the file with the icon.

  -  *iIcon* : int

    Index of the icon.

## [PyIShellLink](#pyishelllink).SetPath

 __SetPath( *path* __ )
Sets the path and file name of a shell link object.

#### Parameters


  -  *path* : string

    The path and filename of the link.

## [PyIShellLink](#pyishelllink).SetRelativePath

 __SetRelativePath( *relPath*  *, reserved* __ )
Sets the relative path for a shell link object.

#### Parameters


  -  *relPath* : string

    The relative path.

  -  *reserved=0* : int

    Reserved - must be zero.

#### Comments
This mechanism allows for moved link files 

to reestablish connection with relative files through 

similar-prefix comparisons

## [PyIShellLink](#pyishelllink).SetShowCmd

 __SetShowCmd( *iShowCmd* __ )
Sets the show (SW_) command for a shell link object.

#### Parameters


  -  *iShowCmd* : int

    The new show command value.

## [PyIShellLink](#pyishelllink).SetWorkingDirectory

 __SetWorkingDirectory( *Dir* __ )
Sets the working directory for the link.

#### Parameters


  -  *Dir* : str

    The working directory for the link