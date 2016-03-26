# PyICategoryProvider

## PyICategoryProvider Object



Description of the interface

#### Methods


  - [CanCategorizeOnSCID](PyICategoryProvider.md#pyicategoryprovidercancategorizeonscid)

    Description of CanCategorizeOnSCID&nbsp;

  - [GetDefaultCategory](PyICategoryProvider.md#pyicategoryprovidergetdefaultcategory)

    Description of GetDefaultCategory&nbsp;

  - [GetCategoryForSCID](PyICategoryProvider.md#pyicategoryprovidergetcategoryforscid)

    Description of GetCategoryForSCID&nbsp;

  - [EnumCategories](PyICategoryProvider.md#pyicategoryproviderenumcategories)

    Description of EnumCategories&nbsp;

  - [GetCategoryName](PyICategoryProvider.md#pyicategoryprovidergetcategoryname)

    Description of GetCategoryName&nbsp;

  - [CreateCategory](PyICategoryProvider.md#pyicategoryprovidercreatecategory)

    Description of CreateCategory&nbsp;

## [PyICategoryProvider](#pyicategoryprovider)\.CanCategorizeOnSCID

CanCategorizeOnSCID\(pscid\)
Description of CanCategorizeOnSCID\.

#### Parameters


  - pscid :SHCOLUMNID

    Description for pscid

## [PyICategoryProvider](#pyicategoryprovider)\.CreateCategory

CreateCategory\(guid, riid\)
Description of CreateCategory\.

#### Parameters


  - guid :[PyIID](#pyiid)

    Description for pguid

  - riid :[PyIID](#pyiid)

    Description for riid

## [PyICategoryProvider](#pyicategoryprovider)\.EnumCategories

EnumCategories\(\)
Description of EnumCategories\.

## [PyICategoryProvider](#pyicategoryprovider)\.GetCategoryForSCID

GetCategoryForSCID\(pscid\)
Description of GetCategoryForSCID\.

#### Parameters


  - pscid :SHCOLUMNID

    Description for pscid

## [PyICategoryProvider](#pyicategoryprovider)\.GetCategoryName

GetCategoryName\(guid\)
Description of GetCategoryName\.

#### Parameters


  - guid :[PyIID](#pyiid)

    Description for pguid

#### Comments


The buffer is always 1024 chars long

## [PyICategoryProvider](#pyicategoryprovider)\.GetDefaultCategory

GetDefaultCategory\(\)
Description of GetDefaultCategory\.