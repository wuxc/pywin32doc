# PyIApplicationDestinations

## PyIApplicationDestinations Object

Allows an application to removed items from its jump lists

#### Comments
Available on Windows 7 and later

#### Methods


  - [SetAppID](PyIApplicationDestinations.md#pyiapplicationdestinationssetappid)

    Specifies the application whose jump list is to be accessed&nbsp;

  - [RemoveDestination](PyIApplicationDestinations.md#pyiapplicationdestinationsremovedestination)

    Removes a single entry from the jump list&nbsp;

  - [RemoveAllDestinations](PyIApplicationDestinations.md#pyiapplicationdestinationsremovealldestinations)

    Removes all Recent and Frequent jump list entries&nbsp;

## [PyIApplicationDestinations](#pyiapplicationdestinations)\.RemoveAllDestinations

 **RemoveAllDestinations\(** \)
Removes all Recent and Frequent jump list entries

## [PyIApplicationDestinations](#pyiapplicationdestinations)\.RemoveDestination

 **RemoveDestination\( *punk* ** \)
Removes a single entry from the jump lists

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    IShellItem or IShellLink representing an item in the application's jump list

#### Comments
Does not remove pinned items

## [PyIApplicationDestinations](#pyiapplicationdestinations)\.SetAppID

 **SetAppID\( *AppID* ** \)
Specifies the application whose jump list is to be accessed

#### Parameters


  -  *AppID* : str

    Taskbar identifier for the application

#### Comments
This method is only needed if the application sets its own taskbar identifier