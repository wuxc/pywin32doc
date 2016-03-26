# PyIApplicationDocumentLists


## PyIApplicationDocumentLists Object

Interface used to retrieve the jump lists for an application

#### Comments

Available on Windows 7 and later

#### Methods

  - [SetAppID](PyIApplicationDocumentLists.md#pyiapplicationdocumentlistssetappid)

    Specifies the application whose jump list is to be accessed&nbsp;

  - [GetList](PyIApplicationDocumentLists.md#pyiapplicationdocumentlistsgetlist)

    Retrieves a list of items in a jump list&nbsp;


## [PyIApplicationDocumentLists](PyIApplicationDocumentLists.md#pyiapplicationdocumentlists)\.GetList

[PyIEnumObjects](PyIEnumObjects.md) = GetList\(ListType, ItemsDesired

, riid

\)
Retrieves a list of items in a jump list

#### Parameters

  - ListType : int

    Type of document list to return, shellcon\.ADLT\_RECENT or ADLT\_FREQUENT

  - ItemsDesired=0 : int

    Number of items to return, use 0 for all available

  - riid=IID\_IEnumObjects : [PyIID](PyIID.md)

    The interface to return, IID\_IEnumObjects or IID\_IObjectArray


## [PyIApplicationDocumentLists](PyIApplicationDocumentLists.md#pyiapplicationdocumentlists)\.SetAppID

SetAppID\(AppID\)
Specifies the application whose jump list is to be accessed

#### Parameters

  - AppID : str

    Taskbar identifier for the application

#### Comments

This method is only needed if the application sets its own taskbar identifier