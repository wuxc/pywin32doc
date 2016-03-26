# PyIShellItemResources

## PyIShellItemResources Object



Description of the interface

#### Methods


  - [GetAttributes](PyIShellItemResources.md#pyishellitemresourcesgetattributes)

    Description of GetAttributes&nbsp;

  - [GetSize](PyIShellItemResources.md#pyishellitemresourcesgetsize)

    Description of GetSize&nbsp;

  - [GetTimes](PyIShellItemResources.md#pyishellitemresourcesgettimes)

    Description of GetTimes&nbsp;

  - [SetTimes](PyIShellItemResources.md#pyishellitemresourcessettimes)

    Description of SetTimes&nbsp;

  - [GetResourceDescription](PyIShellItemResources.md#pyishellitemresourcesgetresourcedescription)

    Description of GetResourceDescription&nbsp;

  - [EnumResources](PyIShellItemResources.md#pyishellitemresourcesenumresources)

    Description of EnumResources&nbsp;

  - [SupportsResource](PyIShellItemResources.md#pyishellitemresourcessupportsresource)

    Description of SupportsResource&nbsp;

  - [OpenResource](PyIShellItemResources.md#pyishellitemresourcesopenresource)

    Description of OpenResource&nbsp;

  - [CreateResource](PyIShellItemResources.md#pyishellitemresourcescreateresource)

    Description of CreateResource&nbsp;

  - [MarkForDelete](PyIShellItemResources.md#pyishellitemresourcesmarkfordelete)

    Description of MarkForDelete&nbsp;

## [PyIShellItemResources](#pyishellitemresources)\.CreateResource



interface =CreateResource\(sir, riid\)
Description of CreateResource\.

#### Parameters


  - sir :[PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Resource identifier

  - riid :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemResources](#pyishellitemresources)\.EnumResources

[PyIEnumResources](#pyienumresources) =EnumResources\(\)
Description of EnumResources\.

## [PyIShellItemResources](#pyishellitemresources)\.GetAttributes

GetAttributes\(\)
Description of GetAttributes\.

## [PyIShellItemResources](#pyishellitemresources)\.GetResourceDescription

GetResourceDescription\(pcsir\)
Description of GetResourceDescription\.

#### Parameters


  - pcsir :[PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir

## [PyIShellItemResources](#pyishellitemresources)\.GetSize



int =GetSize\(\)
Description of GetSize\.

## [PyIShellItemResources](#pyishellitemresources)\.GetTimes

GetTimes\(\)
Description of GetTimes\.

## [PyIShellItemResources](#pyishellitemresources)\.MarkForDelete

MarkForDelete\(\)
Description of MarkForDelete\.

## [PyIShellItemResources](#pyishellitemresources)\.OpenResource

[PyIUnknown](#pyiunknown) =OpenResource\(pcsir, riid\)
Description of OpenResource\.

#### Parameters


  - pcsir :[PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir

  - riid :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemResources](#pyishellitemresources)\.SetTimes

SetTimes\(pftCreation, pftWrite, pftAccess\)
Description of SetTimes\.

#### Parameters


  - pftCreation :[PyTime](#pytime)

    Description for pftCreation

  - pftWrite :[PyTime](#pytime)

    Description for pftWrite

  - pftAccess :[PyTime](#pytime)

    Description for pftAccess

## [PyIShellItemResources](#pyishellitemresources)\.SupportsResource



boolean =SupportsResource\(pcsir\)
Description of SupportsResource\.

#### Parameters


  - pcsir :[PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir