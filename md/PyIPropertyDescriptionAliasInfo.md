# PyIPropertyDescriptionAliasInfo


## PyIPropertyDescriptionAliasInfo Object

Interface that gives access to the sorting columns for a property

#### Methods

  - [GetSortByAlias](PyIPropertyDescriptionAliasInfo.md#pyipropertydescriptionaliasinfogetsortbyalias)

    Returns the primary column used for sorting&nbsp;

  - [GetAdditionalSortByAliases](PyIPropertyDescriptionAliasInfo.md#pyipropertydescriptionaliasinfogetadditionalsortbyaliases)

    Returns secondary sorting columns&nbsp;


## [PyIPropertyDescriptionAliasInfo](PyIPropertyDescriptionAliasInfo.md#pyipropertydescriptionaliasinfo)\.GetAdditionalSortByAliases

[PyIPropertyDescriptionList](PyIPropertyDescriptionList.md) = GetAdditionalSortByAliases\(riid\)
Returns secondary sorting columns

#### Parameters

  - riid=IID\_IPropertyDescriptionList : [PyIID](PyIID.md)

    The interface to return


## [PyIPropertyDescriptionAliasInfo](PyIPropertyDescriptionAliasInfo.md#pyipropertydescriptionaliasinfo)\.GetSortByAlias

[PyIPropertyDescription](PyIPropertyDescription.md) = GetSortByAlias\(riid\)
Returns the primary column used for sorting

#### Parameters

  - riid=IID\_IPropertyDescription : [PyIID](PyIID.md)

    The interface to return