# PyIPropertyDescriptionAliasInfo

## PyIPropertyDescriptionAliasInfo Object

Interface that gives access to the sorting columns for a property

#### Methods


  - [GetSortByAlias](PyIPropertyDescriptionAliasInfo.md#pyipropertydescriptionaliasinfogetsortbyalias)

    Returns the primary column used for sorting&nbsp;

  - [GetAdditionalSortByAliases](PyIPropertyDescriptionAliasInfo.md#pyipropertydescriptionaliasinfogetadditionalsortbyaliases)

    Returns secondary sorting columns&nbsp;

## [PyIPropertyDescriptionAliasInfo](#pyipropertydescriptionaliasinfo).GetAdditionalSortByAliases

[PyIPropertyDescriptionList](#pyipropertydescriptionlist)= __GetAdditionalSortByAliases( *riid* __ )
Returns secondary sorting columns

#### Parameters


  -  *riid=IID_IPropertyDescriptionList* :[PyIID](#pyiid)

    The interface to return

## [PyIPropertyDescriptionAliasInfo](#pyipropertydescriptionaliasinfo).GetSortByAlias

[PyIPropertyDescription](#pyipropertydescription)= __GetSortByAlias( *riid* __ )
Returns the primary column used for sorting

#### Parameters


  -  *riid=IID_IPropertyDescription* :[PyIID](#pyiid)

    The interface to return