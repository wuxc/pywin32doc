# PyIOleObject

## PyIOleObject Object



Description of the interface

#### Methods


  - [SetClientSite](PyIOleObject.md#pyioleobjectsetclientsite)

    Description of SetClientSite&nbsp;

  - [GetClientSite](PyIOleObject.md#pyioleobjectgetclientsite)

    Description of GetClientSite&nbsp;

  - [SetHostNames](PyIOleObject.md#pyioleobjectsethostnames)

    Description of SetHostNames&nbsp;

  - [Close](PyIOleObject.md#pyioleobjectclose)

    Description of Close&nbsp;

  - [SetMoniker](PyIOleObject.md#pyioleobjectsetmoniker)

    Description of SetMoniker&nbsp;

  - [GetMoniker](PyIOleObject.md#pyioleobjectgetmoniker)

    Description of GetMoniker&nbsp;

  - [InitFromData](PyIOleObject.md#pyioleobjectinitfromdata)

    Description of InitFromData&nbsp;

  - [GetClipboardData](PyIOleObject.md#pyioleobjectgetclipboarddata)

    Description of GetClipboardData&nbsp;

  - [DoVerb](PyIOleObject.md#pyioleobjectdoverb)

    Description of DoVerb&nbsp;

  - [EnumVerbs](PyIOleObject.md#pyioleobjectenumverbs)

    Description of EnumVerbs&nbsp;

  - [Update](PyIOleObject.md#pyioleobjectupdate)

    Description of Update&nbsp;

  - [IsUpToDate](PyIOleObject.md#pyioleobjectisuptodate)

    Description of IsUpToDate&nbsp;

  - [GetUserClassID](PyIOleObject.md#pyioleobjectgetuserclassid)

    Description of GetUserClassID&nbsp;

  - [GetUserType](PyIOleObject.md#pyioleobjectgetusertype)

    Description of GetUserType&nbsp;

  - [SetExtent](PyIOleObject.md#pyioleobjectsetextent)

    Description of SetExtent&nbsp;

  - [GetExtent](PyIOleObject.md#pyioleobjectgetextent)

    Description of GetExtent&nbsp;

  - [Advise](PyIOleObject.md#pyioleobjectadvise)

    Description of Advise&nbsp;

  - [Unadvise](PyIOleObject.md#pyioleobjectunadvise)

    Description of Unadvise&nbsp;

  - [EnumAdvise](PyIOleObject.md#pyioleobjectenumadvise)

    Description of EnumAdvise&nbsp;

  - [GetMiscStatus](PyIOleObject.md#pyioleobjectgetmiscstatus)

    Description of GetMiscStatus&nbsp;

  - [SetColorScheme](PyIOleObject.md#pyioleobjectsetcolorscheme)

    Description of SetColorScheme&nbsp;

## [PyIOleObject](#pyioleobject)\.Advise

Advise\(pAdvSink\)
Description of Advise\.

#### Parameters


  - pAdvSink :PyIAdviseSink

    Description for pAdvSink

## [PyIOleObject](#pyioleobject)\.Close

Close\(dwSaveOption\)
Description of Close\.

#### Parameters


  - dwSaveOption : int

    Description for dwSaveOption

## [PyIOleObject](#pyioleobject)\.DoVerb

DoVerb\(iVerb, msg, pActiveSite, lindex, hwndParent, rect\)
Description of DoVerb\.

#### Parameters


  - iVerb : int

    Description for iVerb

  - msg :[PyMSG](#pymsg)

    MSG tuple, a-la win32gui etc\.

  - pActiveSite :[PyIOleClientSite](#pyioleclientsite)

    Description for pActiveSite

  - lindex : int

    Description for lindex

  - hwndParent : HWND

    Description for hwndParent

  - rect : \(int, int, int, int\)

    

## [PyIOleObject](#pyioleobject)\.EnumAdvise

EnumAdvise\(\)
Description of EnumAdvise\.

## [PyIOleObject](#pyioleobject)\.EnumVerbs

EnumVerbs\(\)
Description of EnumVerbs\.

## [PyIOleObject](#pyioleobject)\.GetClientSite

GetClientSite\(\)
Description of GetClientSite\.

## [PyIOleObject](#pyioleobject)\.GetClipboardData

GetClipboardData\(dwReserved\)
Description of GetClipboardData\.

#### Parameters


  - dwReserved : int

    Description for dwReserved

## [PyIOleObject](#pyioleobject)\.GetExtent

GetExtent\(dwDrawAspect, size\)
Description of GetExtent\.

#### Parameters


  - dwDrawAspect : int

    Description for dwDrawAspect

  - size : \(int, int\)

    Size limit for the object\.

## [PyIOleObject](#pyioleobject)\.GetMiscStatus

GetMiscStatus\(dwAspect\)
Description of GetMiscStatus\.

#### Parameters


  - dwAspect : int

    Description for dwAspect

## [PyIOleObject](#pyioleobject)\.GetMoniker

GetMoniker\(dwAssign, dwWhichMoniker\)
Description of GetMoniker\.

#### Parameters


  - dwAssign : int

    Description for dwAssign

  - dwWhichMoniker : int

    Description for dwWhichMoniker

## [PyIOleObject](#pyioleobject)\.GetUserClassID

GetUserClassID\(\)
Description of GetUserClassID\.

## [PyIOleObject](#pyioleobject)\.GetUserType

GetUserType\(dwFormOfType\)
Description of GetUserType\.

#### Parameters


  - dwFormOfType : int

    Description for dwFormOfType

## [PyIOleObject](#pyioleobject)\.InitFromData

InitFromData\(pDataObject, fCreation, dwReserved\)
Description of InitFromData\.

#### Parameters


  - pDataObject :[PyIDataObject](#pyidataobject)

    Description for pDataObject

  - fCreation : int

    Description for fCreation

  - dwReserved : int

    Description for dwReserved

## [PyIOleObject](#pyioleobject)\.IsUpToDate

IsUpToDate\(\)
Description of IsUpToDate\.

## [PyIOleObject](#pyioleobject)\.SetClientSite

SetClientSite\(pClientSite\)
Description of SetClientSite\.

#### Parameters


  - pClientSite :[PyIOleClientSite](#pyioleclientsite)

    Description for pClientSite

## [PyIOleObject](#pyioleobject)\.SetColorScheme

SetColorScheme\(\)
Description of SetColorScheme\.

## [PyIOleObject](#pyioleobject)\.SetExtent

SetExtent\(dwDrawAspect, size\)
Description of SetExtent\.

#### Parameters


  - dwDrawAspect : int

    Description for dwDrawAspect

  - size : \(int, int\)

    Size limit for the object\.

## [PyIOleObject](#pyioleobject)\.SetHostNames

SetHostNames\(szContainerApp, szContainerObj\)
Description of SetHostNames\.

#### Parameters


  - szContainerApp :unicode

    Description for szContainerApp

  - szContainerObj :unicode

    Description for szContainerObj

## [PyIOleObject](#pyioleobject)\.SetMoniker

SetMoniker\(dwWhichMoniker, pmk\)
Description of SetMoniker\.

#### Parameters


  - dwWhichMoniker : int

    Description for dwWhichMoniker

  - pmk :[PyIMoniker](#pyimoniker)

    Description for pmk

## [PyIOleObject](#pyioleobject)\.Unadvise

Unadvise\(dwConnection\)
Description of Unadvise\.

#### Parameters


  - dwConnection : int

    Description for dwConnection

## [PyIOleObject](#pyioleobject)\.Update

Update\(\)
Description of Update\.