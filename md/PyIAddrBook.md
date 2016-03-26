# PyIAddrBook

## PyIAddrBook Object

An COM interface to MAPI's IAddrBook interface.
Derived from[PyIMAPIProp](#pyimapiprop)

#### Methods


  - [ResolveName](PyIAddrBook.md#pyiaddrbookresolvename)

    Performs name resolution, assigning entry identifiers to recipients in a recipient list.&nbsp;

  - [OpenEntry](PyIAddrBook.md#pyiaddrbookopenentry)

    Opens a folder or message and returns an interface object for further access.&nbsp;

  - [CompareEntryIDs](PyIAddrBook.md#pyiaddrbookcompareentryids)

    Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object&nbsp;

## [PyIAddrBook](#pyiaddrbook).CompareEntryIDs

int = __CompareEntryIDs( *entryId*  *, entryId*  *, flags* __ )
Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

#### Parameters


  -  *entryId* : string

    The first entry ID to be compared

  -  *entryId* : string

    The second entry ID to be compared

  -  *flags=0* : int

    Reserved - must be zero.

#### Return Value
The result is set to TRUE if the two entry identifiers refer to the same object, and FALSE otherwise.

## [PyIAddrBook](#pyiaddrbook).OpenEntry

 __PyIInterface__ = __OpenEntry( *entryId*  *, iid*  *, flags* __ )
Opens a folder or message and returns an interface object for further access.

#### Parameters


  -  *entryId* : string

    The entryID of the object

  -  *iid* :[PyIID](#pyiid)

    The IID of the object to return, or None for the default IID

  -  *flags* : int

    Bitmask of flags that controls how the object is opened.

## [PyIAddrBook](#pyiaddrbook).ResolveName

 __ResolveName( *uiParm*  *, flags*  *, entryTitle*  *, ADRLIST* __ )
Performs name resolution, assigning entry identifiers to recipients in a recipient list.

#### Parameters


  -  *uiParm* : int

    hwnd of a dialogs parent.

  -  *flags* : int

    Bitmask of flags that controls whether a dialog box can be displayed.

  -  *entryTitle* : string

    

  -  *ADRLIST* : __PyADRLIST__ 

    Partial addresses to resolve.