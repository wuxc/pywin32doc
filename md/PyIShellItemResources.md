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

## [PyIShellItemResources](#pyishellitemresources).CreateResource

interface = __CreateResource( *sir*  *, riid* __ )
Description of CreateResource.

#### Parameters


  -  *sir* :[PySHELL_ITEM_RESOURCE](PySHELL.md#pyshellitem_resource)

    Resource identifier

  -  *riid* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemResources](#pyishellitemresources).EnumResources

[PyIEnumResources](#pyienumresources)= __EnumResources(__ )
Description of EnumResources.

## [PyIShellItemResources](#pyishellitemresources).GetAttributes

 __GetAttributes(__ )
Description of GetAttributes.

## [PyIShellItemResources](#pyishellitemresources).GetResourceDescription

 __GetResourceDescription( *pcsir* __ )
Description of GetResourceDescription.

#### Parameters


  -  *pcsir* :[PySHELL_ITEM_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir

## [PyIShellItemResources](#pyishellitemresources).GetSize

int = __GetSize(__ )
Description of GetSize.

## [PyIShellItemResources](#pyishellitemresources).GetTimes

 __GetTimes(__ )
Description of GetTimes.

## [PyIShellItemResources](#pyishellitemresources).MarkForDelete

 __MarkForDelete(__ )
Description of MarkForDelete.

## [PyIShellItemResources](#pyishellitemresources).OpenResource

[PyIUnknown](#pyiunknown)= __OpenResource( *pcsir*  *, riid* __ )
Description of OpenResource.

#### Parameters


  -  *pcsir* :[PySHELL_ITEM_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir

  -  *riid* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItemResources](#pyishellitemresources).SetTimes

 __SetTimes( *pftCreation*  *, pftWrite*  *, pftAccess* __ )
Description of SetTimes.

#### Parameters


  -  *pftCreation* :[PyTime](#pytime)

    Description for pftCreation

  -  *pftWrite* :[PyTime](#pytime)

    Description for pftWrite

  -  *pftAccess* :[PyTime](#pytime)

    Description for pftAccess

## [PyIShellItemResources](#pyishellitemresources).SupportsResource

boolean = __SupportsResource( *pcsir* __ )
Description of SupportsResource.

#### Parameters


  -  *pcsir* :[PySHELL_ITEM_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir