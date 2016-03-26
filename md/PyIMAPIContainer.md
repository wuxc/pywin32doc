# PyIMAPIContainer

## PyIMAPIContainer Object

An COM interface to MAPI's IMAPIContainer interface.
Derived from[PyIMAPIProp](#pyimapiprop)

#### Methods


  - [OpenEntry](PyIMAPIContainer.md#pyimapicontaineropenentry)

    Opens an object and returns an interface object for further access.&nbsp;

  - [GetContentsTable](PyIMAPIContainer.md#pyimapicontainergetcontentstable)

    Returns an object representing the container's contents table.&nbsp;

  - [GetHierarchyTable](PyIMAPIContainer.md#pyimapicontainergethierarchytable)

    Returns an object representing the container's hierarchy table.&nbsp;

## [PyIMAPIContainer](#pyimapicontainer).GetContentsTable

[PyIMAPITable](#pyimapitable)= __GetContentsTable( *flags* __ )
Returns an object representing the container's contents table.

#### Parameters


  -  *flags* : int

    The flags to use.

## [PyIMAPIContainer](#pyimapicontainer).GetHierarchyTable

[PyIMAPITable](#pyimapitable)= __GetHierarchyTable( *flags* __ )
Returns an object representing the container's hierarchy table.

#### Parameters


  -  *flags* : int

    The flags to use.

## [PyIMAPIContainer](#pyimapicontainer).OpenEntry

 __PyIInterface__ = __OpenEntry( *entryId*  *, iid*  *, flags* __ )
Opens an object and returns an interface object for further access.

#### Parameters


  -  *entryId* : string

    The EntryID to open.

  -  *iid* :[PyIID](#pyiid)

    The IID of the returned interface, or None for the default interface.

  -  *flags* : int

    Flags for the call.  May include MAPI_BEST_ACCESS, MAPI_DEFERRED_ERRORS, MAPI_MODIFY and possibly others (see the MAPI documentation)