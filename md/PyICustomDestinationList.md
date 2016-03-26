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


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.AbortList

AbortList\(\)
Discards all changes


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.AddUserTasks

AddUserTasks\(Items\)
Sets the entries shown in the Tasks category

#### Parameters

  - Items : [PyIObjectArray](PyIObjectArray.md)

    Collection of [PyIShellItem](PyIShellItem.md) and/or [PyIShellLink](PyIShellLink.md) interfaces


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.AppendCategory

AppendCategory\(Category, Items\)
Adds a custom category to the jump list

#### Parameters

  - Category : str

    Display name of the category, can also be a dll and resource id for localization

  - Items : [PyIObjectArray](PyIObjectArray.md)

    Collection of IShellItem and/or IShellLink interfaces


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.AppendKnownCategory

AppendKnownCategory\(Category\)
Adds one of the predefined categories to the custom list

#### Parameters

  - Category : int

    shellcon\.KDC\_RECENT or KDC\_FREQUENT


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.BeginList

int, [PyIObjectArray](PyIObjectArray.md) = BeginList\(riid\)
Clears the jump list and prepares it to be repopulated

#### Parameters

  - riid=IID\_IObjectArray : [PyIID](PyIID.md)

    The interface to return

#### Return Value
Returns the number of slots and a collection of all destinations removed from the jump list


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.CommitList

CommitList\(\)
Finalizes changes\.


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.DeleteList

DeleteList\(AppID\)
Removes any customization, leaving only the system-maintained Recent and Frequent lists

#### Parameters

  - AppID=None : str

    The taskbar identifier of the application


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.GetRemovedDestinations

[PyIObjectArray](PyIObjectArray.md) = GetRemovedDestinations\(riid\)
Returns all the items removed from the jump list

#### Parameters

  - riid=IID\_IObjectArray : [PyIID](PyIID.md)

    The interface to return


## [PyICustomDestinationList](PyICustomDestinationList.md#pyicustomdestinationlist)\.SetAppID

SetAppID\(AppID\)
Specifies the taskbar identifier for the jump list

#### Parameters

  - AppID : str

    The taskbar identifier of the application

#### Comments

Only needed if the calling app doesn't use the system-assigned default