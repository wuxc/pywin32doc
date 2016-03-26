# PyIInternetSecurityManager

## PyIInternetSecurityManager Object

Description of the interface

#### Methods


  - [SetSecuritySite](PyIInternetSecurityManager.md#pyiinternetsecuritymanagersetsecuritysite)

    Description of SetSecuritySite&nbsp;

  - [GetSecuritySite](PyIInternetSecurityManager.md#pyiinternetsecuritymanagergetsecuritysite)

    Description of GetSecuritySite&nbsp;

  - [MapUrlToZone](PyIInternetSecurityManager.md#pyiinternetsecuritymanagermapurltozone)

    Description of MapUrlToZone&nbsp;

  - [GetSecurityId](PyIInternetSecurityManager.md#pyiinternetsecuritymanagergetsecurityid)

    Description of GetSecurityId&nbsp;

  - [ProcessUrlAction](PyIInternetSecurityManager.md#pyiinternetsecuritymanagerprocessurlaction)

    Description of ProcessUrlAction 

{ "QueryCustomPolicy", PyIInternetSecurityManager::QueryCustomPolicy, 1 },&nbsp;

  - [SetZoneMapping](PyIInternetSecurityManager.md#pyiinternetsecuritymanagersetzonemapping)

    Description of SetZoneMapping&nbsp;

  - [GetZoneMappings](PyIInternetSecurityManager.md#pyiinternetsecuritymanagergetzonemappings)

    Description of GetZoneMappings&nbsp;

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).GetSecurityId

 __GetSecurityId( *pwszUrl*  *, pcbSecurityId* __ )
Description of GetSecurityId.

#### Parameters


  -  *pwszUrl* : __unicode__ 

    Description for pwszUrl

  -  *pcbSecurityId* : int

    Description for pcbSecurityId

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).GetSecuritySite

 __GetSecuritySite(__ )
Description of GetSecuritySite.

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).GetZoneMappings

 __GetZoneMappings( *dwZone*  *, dwFlags* __ )
Description of GetZoneMappings.

#### Parameters


  -  *dwZone* : int

    Description for dwZone

  -  *dwFlags* : int

    Description for dwFlags

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).MapUrlToZone

 __MapUrlToZone( *pwszUrl*  *, dwFlags* __ )
Description of MapUrlToZone.

#### Parameters


  -  *pwszUrl* : __unicode__ 

    Description for pwszUrl

  -  *dwFlags* : int

    Description for dwFlags

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).ProcessUrlAction

 __ProcessUrlAction( *pwszUrl*  *, dwAction*  *, context*  *, dwFlags* __ )
Description of ProcessUrlAction.

#### Parameters


  -  *pwszUrl* : __unicode__ 

    Description for pwszUrl

  -  *dwAction* : int

    Description for dwAction

  -  *context* : bytes

    

  -  *dwFlags* : int

    Description for dwFlags

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).SetSecuritySite

 __SetSecuritySite( *pSite* __ )
Description of SetSecuritySite.

#### Parameters


  -  *pSite* : __PyIInternetSecurityMgrSite__ 

    Description for pSite

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager).SetZoneMapping

 __SetZoneMapping( *dwZone*  *, lpszPattern*  *, dwFlags* __ )
Description of SetZoneMapping.

#### Parameters


  -  *dwZone* : int

    Description for dwZone

  -  *lpszPattern* : __unicode__ 

    Description for lpszPattern

  -  *dwFlags* : int

    Description for dwFlags