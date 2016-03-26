# PyIMAPISession

## PyIMAPISession Object

An COM interface to MAPI's ISession interface\.
Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [OpenEntry](PyIMAPISession.md#pyimapisessionopenentry)

    Opens an object and returns an interface object for further access\.&nbsp;

  - [OpenMsgStore](PyIMAPISession.md#pyimapisessionopenmsgstore)

    Opens a message store\.&nbsp;

  - [QueryIdentity](PyIMAPISession.md#pyimapisessionqueryidentity)

    Returns the entry identifier of the object that provides the primary identity for the session\.&nbsp;

  - [Advise](PyIMAPISession.md#pyimapisessionadvise)

    &nbsp;

  - [Unadvise](PyIMAPISession.md#pyimapisessionunadvise)

    &nbsp;

  - [CompareEntryIDs](PyIMAPISession.md#pyimapisessioncompareentryids)

    Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object&nbsp;

  - [GetMsgStoresTable](PyIMAPISession.md#pyimapisessiongetmsgstorestable)

    Provides access to the message store table - a table with information about all of the message stores in the session profile\.&nbsp;

  - [GetStatusTable](PyIMAPISession.md#pyimapisessiongetstatustable)

    Provides access to the status table - a table with information about all of the MAPI resources in the session\.&nbsp;

  - [Logoff](PyIMAPISession.md#pyimapisessionlogoff)

    Ends a MAPI session\.&nbsp;

  - [OpenAddressBook](PyIMAPISession.md#pyimapisessionopenaddressbook)

    Opens the integrated address book\.&nbsp;

  - [OpenProfileSection](PyIMAPISession.md#pyimapisessionopenprofilesection)

    Opens a section of the current profile and returns an object for futher access&nbsp;

## [PyIMAPISession](#pyimapisession)\.Advise

int \= **Advise\( *entryId*  *, mask*  *, sink* ** \)


#### Parameters


  -  *entryId* : string

    The entryID of the object

  -  *mask* : int

    

  -  *sink* : **PyIMAPIAdviseSink** 

    

#### Return Value
The result is an integer which should be passed to[PyIMAPISession::Unadvise](PyIMAPISession.md#pyimapisessionunadvise)

## [PyIMAPISession](#pyimapisession)\.CompareEntryIDs

int \= **CompareEntryIDs\( *entryId*  *, entryId*  *, flags* ** \)
Compares two entry identifiers belonging to a particular address book provider to determine if they refer to the same address book object

#### Parameters


  -  *entryId* : string

    The first entry ID to be compared

  -  *entryId* : string

    The second entry ID to be compared

  -  *flags\=0* : int

    Reserved - must be zero\.

#### Return Value
The result is set to TRUE if the two entry identifiers refer to the same object, and FALSE otherwise\.

## [PyIMAPISession](#pyimapisession)\.GetMsgStoresTable

[PyIMAPITable](#pyimapitable)\= **GetMsgStoresTable\( *flags* ** \)
Provides access to the message store table - a table with information about all of the message stores in the session profile\.

#### Parameters


  -  *flags* : int

    Flags that control the opening\.

## [PyIMAPISession](#pyimapisession)\.GetStatusTable

[PyIMAPITable](#pyimapitable)\= **GetStatusTable\( *flags* ** \)
Provides access to the status table - a table with information about all of the MAPI resources in the session\.

#### Parameters


  -  *flags* : int

    Flags that control the opening\.

## [PyIMAPISession](#pyimapisession)\.Logoff

 **Logoff\( *uiParm*  *, flags*  *, reserved* ** \)
Ends a MAPI session\.

#### Parameters


  -  *uiParm* : int

    hwnd of a dialog is to be displayed\.

  -  *flags* : int

    Bitmask of flags that control the logoff operation\.

  -  *reserved* : int

    Reserved; must be zero\.

## [PyIMAPISession](#pyimapisession)\.OpenAddressBook

[PyIAddrBook](#pyiaddrbook)\= **OpenAddressBook\( *uiParm*  *, iid*  *, flags* ** \)
Opens the integrated address book\.

#### Parameters


  -  *uiParm* : int

    hwnd of a dialog is to be displayed\.

  -  *iid* :[PyIID](#pyiid)

    The IID of the interface, or None\.

  -  *flags* : int

    Flags that control the opening - AB\_NO\_DIALOG\.

## [PyIMAPISession](#pyimapisession)\.OpenEntry

 **PyIInterface** \= **OpenEntry\( *entryId*  *, iid*  *, flags* ** \)
Opens an object and returns an interface object for further access\.

#### Parameters


  -  *entryId* : string

    The EntryID to open\.

  -  *iid* :[PyIID](#pyiid)

    The IID of the returned interface, or None for the default interface\.

  -  *flags* : int

    Flags for the call\.  May include MAPI\_BEST\_ACCESS, MAPI\_DEFERRED\_ERRORS, MAPI\_MODIFY and possibly others \(see the MAPI documentation\)

## [PyIMAPISession](#pyimapisession)\.OpenMsgStore

[PyIUnknown](#pyiunknown)\= **OpenMsgStore\( *uiParam*  *, entryId*  *, iid*  *, flags* ** \)
Opens a message store\.

#### Parameters


  -  *uiParam* : int

    Handle to the parent window for dialogs\.

  -  *entryId* : string

    The entry ID of the message store to open\.

  -  *iid* :[PyIID](#pyiid)

    The IID of the interface returned, or None

  -  *flags* : int

    Options for the call\.

#### Comments
The result is the interface specified by the IID, or IID\_IMsgStore if None is used\.

## [PyIMAPISession](#pyimapisession)\.OpenProfileSection

 **PyIProfSection** \= **OpenProfileSection\( *iidSection*  *, iid*  *, flags* ** \)
Opens a section of the current profile and returns an object for futher access

#### Parameters


  -  *iidSection* :[PyIID](#pyiid)

    The MAPIIID of the profile section

  -  *iid* :[PyIID](#pyiid)

    The IID of the interface, or None\.

  -  *flags* : int

    Flags that control the opening\.

## [PyIMAPISession](#pyimapisession)\.QueryIdentity

string \= **QueryIdentity\(** \)
Returns the entry identifier of the object that provides the primary identity for the session\.

## [PyIMAPISession](#pyimapisession)\.Unadvise

 **Unadvise\( *connection* ** \)


#### Parameters


  -  *connection* : int

    Value returned from[PyIMAPISession::Advise](PyIMAPISession.md#pyimapisessionadvise)