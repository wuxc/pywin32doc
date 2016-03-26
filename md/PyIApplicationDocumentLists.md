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

## [PyIApplicationDocumentLists](#pyiapplicationdocumentlists).GetList

[PyIEnumObjects](#pyienumobjects)= __GetList( *ListType*  *, ItemsDesired*  *, riid* __ )
Retrieves a list of items in a jump list

#### Parameters


  -  *ListType* : int

    Type of document list to return, shellcon.ADLT_RECENT or ADLT_FREQUENT

  -  *ItemsDesired=0* : int

    Number of items to return, use 0 for all available

  -  *riid=IID_IEnumObjects* :[PyIID](#pyiid)

    The interface to return, IID_IEnumObjects or IID_IObjectArray

## [PyIApplicationDocumentLists](#pyiapplicationdocumentlists).SetAppID

 __SetAppID( *AppID* __ )
Specifies the application whose jump list is to be accessed

#### Parameters


  -  *AppID* : str

    Taskbar identifier for the application

#### Comments
This method is only needed if the application sets its own taskbar identifier