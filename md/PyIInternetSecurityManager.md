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

\{ "QueryCustomPolicy", PyIInternetSecurityManager::QueryCustomPolicy, 1 \},&nbsp;

  - [SetZoneMapping](PyIInternetSecurityManager.md#pyiinternetsecuritymanagersetzonemapping)

    Description of SetZoneMapping&nbsp;

  - [GetZoneMappings](PyIInternetSecurityManager.md#pyiinternetsecuritymanagergetzonemappings)

    Description of GetZoneMappings&nbsp;

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.GetSecurityId

GetSecurityId\(pwszUrl, pcbSecurityId\)
Description of GetSecurityId\.

#### Parameters


  - pwszUrl :unicode

    Description for pwszUrl

  - pcbSecurityId : int

    Description for pcbSecurityId

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.GetSecuritySite

GetSecuritySite\(\)
Description of GetSecuritySite\.

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.GetZoneMappings

GetZoneMappings\(dwZone, dwFlags\)
Description of GetZoneMappings\.

#### Parameters


  - dwZone : int

    Description for dwZone

  - dwFlags : int

    Description for dwFlags

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.MapUrlToZone

MapUrlToZone\(pwszUrl, dwFlags\)
Description of MapUrlToZone\.

#### Parameters


  - pwszUrl :unicode

    Description for pwszUrl

  - dwFlags : int

    Description for dwFlags

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.ProcessUrlAction

ProcessUrlAction\(pwszUrl, dwAction, context, dwFlags\)
Description of ProcessUrlAction\.

#### Parameters


  - pwszUrl :unicode

    Description for pwszUrl

  - dwAction : int

    Description for dwAction

  - context : bytes

    

  - dwFlags : int

    Description for dwFlags

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.SetSecuritySite

SetSecuritySite\(pSite\)
Description of SetSecuritySite\.

#### Parameters


  - pSite :PyIInternetSecurityMgrSite

    Description for pSite

## [PyIInternetSecurityManager](#pyiinternetsecuritymanager)\.SetZoneMapping

SetZoneMapping\(dwZone, lpszPattern, dwFlags\)
Description of SetZoneMapping\.

#### Parameters


  - dwZone : int

    Description for dwZone

  - lpszPattern :unicode

    Description for lpszPattern

  - dwFlags : int

    Description for dwFlags