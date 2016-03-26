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


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.CreateResource

interface = CreateResource\(sir, riid

\)
Description of CreateResource\.

#### Parameters

  - sir : [PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Resource identifier

  - riid : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.EnumResources

[PyIEnumResources](PyIEnumResources.md) = EnumResources\(\)
Description of EnumResources\.


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.GetAttributes

GetAttributes\(\)
Description of GetAttributes\.


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.GetResourceDescription

GetResourceDescription\(pcsir\)
Description of GetResourceDescription\.

#### Parameters

  - pcsir : [PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.GetSize

int = GetSize\(\)
Description of GetSize\.


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.GetTimes

GetTimes\(\)
Description of GetTimes\.


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.MarkForDelete

MarkForDelete\(\)
Description of MarkForDelete\.


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.OpenResource

[PyIUnknown](PyIUnknown.md) = OpenResource\(pcsir, riid

\)
Description of OpenResource\.

#### Parameters

  - pcsir : [PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir

  - riid : [PyIID](PyIID.md)

    The interface to return


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.SetTimes

SetTimes\(pftCreation, pftWrite, pftAccess\)
Description of SetTimes\.

#### Parameters

  - pftCreation : [PyTime](PyTime.md)

    Description for pftCreation

  - pftWrite : [PyTime](PyTime.md)

    Description for pftWrite

  - pftAccess : [PyTime](PyTime.md)

    Description for pftAccess


## [PyIShellItemResources](PyIShellItemResources.md#pyishellitemresources)\.SupportsResource

boolean = SupportsResource\(pcsir\)
Description of SupportsResource\.

#### Parameters

  - pcsir : [PySHELL\_ITEM\_RESOURCE](PySHELL.md#pyshellitem_resource)

    Description for pcsir