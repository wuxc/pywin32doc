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

## [PyICategoryProvider](#pyicategoryprovider).CanCategorizeOnSCID

 __CanCategorizeOnSCID( *pscid* __ )
Description of CanCategorizeOnSCID.

#### Parameters


  -  *pscid* : __SHCOLUMNID__ 

    Description for pscid

## [PyICategoryProvider](#pyicategoryprovider).CreateCategory

 __CreateCategory( *guid*  *, riid* __ )
Description of CreateCategory.

#### Parameters


  -  *guid* :[PyIID](#pyiid)

    Description for pguid

  -  *riid* :[PyIID](#pyiid)

    Description for riid

## [PyICategoryProvider](#pyicategoryprovider).EnumCategories

 __EnumCategories(__ )
Description of EnumCategories.

## [PyICategoryProvider](#pyicategoryprovider).GetCategoryForSCID

 __GetCategoryForSCID( *pscid* __ )
Description of GetCategoryForSCID.

#### Parameters


  -  *pscid* : __SHCOLUMNID__ 

    Description for pscid

## [PyICategoryProvider](#pyicategoryprovider).GetCategoryName

 __GetCategoryName( *guid* __ )
Description of GetCategoryName.

#### Parameters


  -  *guid* :[PyIID](#pyiid)

    Description for pguid

#### Comments
The buffer is always 1024 chars long

## [PyICategoryProvider](#pyicategoryprovider).GetDefaultCategory

 __GetDefaultCategory(__ )
Description of GetDefaultCategory.