# PyICustomDestinationList

## PyICustomDestinationList Object

Interface used to customize an application's jump list

#### Comments
Requires Windows 7 or later

#### Methods


  - [SetAppID](PyICustomDestinationList.md#pyicustomdestinationlistsetappid)

    Specifies the taskbar identifier for the jump list&nbsp;

  - [BeginList](PyICustomDestinationList.md#pyicustomdestinationlistbeginlist)

    Clears the jump list and prepares it to be repopulated&nbsp;

  - [AppendCategory](PyICustomDestinationList.md#pyicustomdestinationlistappendcategory)

    Adds a custom category to the jump list&nbsp;

  - [AppendKnownCategory](PyICustomDestinationList.md#pyicustomdestinationlistappendknowncategory)

    Adds one of the predefined categories to the custom list&nbsp;

  - [AddUserTasks](PyICustomDestinationList.md#pyicustomdestinationlistaddusertasks)

    Sets the entries shown in the Tasks category&nbsp;

  - [CommitList](PyICustomDestinationList.md#pyicustomdestinationlistcommitlist)

    Finalizes changes&nbsp;

  - [GetRemovedDestinations](PyICustomDestinationList.md#pyicustomdestinationlistgetremoveddestinations)

    Returns all the items removed from the jump list&nbsp;

  - [DeleteList](PyICustomDestinationList.md#pyicustomdestinationlistdeletelist)

    Removes any customization, leaving only the system-maintained Recent and Frequent lists&nbsp;

  - [AbortList](PyICustomDestinationList.md#pyicustomdestinationlistabortlist)

    Discards all changes&nbsp;

## [PyICustomDestinationList](#pyicustomdestinationlist)\.AbortList

 **AbortList\(** \)
Discards all changes

## [PyICustomDestinationList](#pyicustomdestinationlist)\.AddUserTasks

 **AddUserTasks\( *Items* ** \)
Sets the entries shown in the Tasks category

#### Parameters


  -  *Items* :[PyIObjectArray](#pyiobjectarray)

    Collection of[PyIShellItem](#pyishellitem)and/or[PyIShellLink](#pyishelllink)interfaces

## [PyICustomDestinationList](#pyicustomdestinationlist)\.AppendCategory

 **AppendCategory\( *Category*  *, Items* ** \)
Adds a custom category to the jump list

#### Parameters


  -  *Category* : str

    Display name of the category, can also be a dll and resource id for localization

  -  *Items* :[PyIObjectArray](#pyiobjectarray)

    Collection of IShellItem and/or IShellLink interfaces

## [PyICustomDestinationList](#pyicustomdestinationlist)\.AppendKnownCategory

 **AppendKnownCategory\( *Category* ** \)
Adds one of the predefined categories to the custom list

#### Parameters


  -  *Category* : int

    shellcon\.KDC\_RECENT or KDC\_FREQUENT

## [PyICustomDestinationList](#pyicustomdestinationlist)\.BeginList

int,[PyIObjectArray](#pyiobjectarray)\= **BeginList\( *riid* ** \)
Clears the jump list and prepares it to be repopulated

#### Parameters


  -  *riid\=IID\_IObjectArray* :[PyIID](#pyiid)

    The interface to return

#### Return Value
Returns the number of slots and a collection of all destinations removed from the jump list

## [PyICustomDestinationList](#pyicustomdestinationlist)\.CommitList

 **CommitList\(** \)
Finalizes changes\.

## [PyICustomDestinationList](#pyicustomdestinationlist)\.DeleteList

 **DeleteList\( *AppID* ** \)
Removes any customization, leaving only the system-maintained Recent and Frequent lists

#### Parameters


  -  *AppID\=None* : str

    The taskbar identifier of the application

## [PyICustomDestinationList](#pyicustomdestinationlist)\.GetRemovedDestinations

[PyIObjectArray](#pyiobjectarray)\= **GetRemovedDestinations\( *riid* ** \)
Returns all the items removed from the jump list

#### Parameters


  -  *riid\=IID\_IObjectArray* :[PyIID](#pyiid)

    The interface to return

## [PyICustomDestinationList](#pyicustomdestinationlist)\.SetAppID

 **SetAppID\( *AppID* ** \)
Specifies the taskbar identifier for the jump list

#### Parameters


  -  *AppID* : str

    The taskbar identifier of the application

#### Comments
Only needed if the calling app doesn't use the system-assigned default