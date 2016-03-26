# PyICatRegister

## PyICatRegister Object

An interface to a COM ICatRegister interface.

#### Methods


  - [RegisterCategories](PyICatRegister.md#pyicatregisterregistercategories)

    Registers one or more component categories. Each component category consists of a CATID and a list of locale-dependent description strings.&nbsp;

  - [UnRegisterCategories](PyICatRegister.md#pyicatregisterunregistercategories)

    Unregister one or more previously registered categories.&nbsp;

  - [RegisterClassImplCategories](PyICatRegister.md#pyicatregisterregisterclassimplcategories)

    Registers the class as implementing one or more component categories.&nbsp;

  - [UnRegisterClassImplCategories](PyICatRegister.md#pyicatregisterunregisterclassimplcategories)

    Unregisters the class as implementing one or more component categories.&nbsp;

  - [RegisterClassReqCategories](PyICatRegister.md#pyicatregisterregisterclassreqcategories)

    Registers the class as requiring one or more component categories.&nbsp;

  - [UnRegisterClassReqCategories](PyICatRegister.md#pyicatregisterunregisterclassreqcategories)

    Unregisters the class as requiring one or more component categories.&nbsp;


## [PyICatRegister](#pyicatregister).RegisterCategories

 __RegisterCategories( *[ (catId, lcid, description), ...]* __ )
Registers one or more component categories. Each component category consists of a CATID and a list of locale-dependent description strings.

#### Parameters


  -  *[ (catId, lcid, description), ...]* : [ ([PyIID](#pyiid), int, string), ...]

    A sequence of category descriptions.

## [PyICatRegister](#pyicatregister).RegisterClassImplCategories

 __RegisterClassImplCategories( *clsid*  *, [catId, ...]* __ )
Registers the class as implementing one or more component categories.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    Class ID of the relevent class

  -  *[catId, ...]* : [[PyIID](#pyiid), ...]

    A sequence of category IDs to be associated with the class.

## [PyICatRegister](#pyicatregister).RegisterClassReqCategories

 __RegisterClassReqCategories( *clsid*  *, [catId, ...]* __ )
Registers the class as requiring one or more component categories.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    Class ID of the relevent class

  -  *[catId, ...]* : [[PyIID](#pyiid), ...]

    A sequence of category IDs to be associated with the class.

## [PyICatRegister](#pyicatregister).UnRegisterClassImplCategories

 __UnRegisterClassImplCategories( *clsid*  *, [catId, ...]* __ )
Unregisters the class as implementing one or more component categories.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    Class ID of the relevent class

  -  *[catId, ...]* : [[PyIID](#pyiid), ...]

    A sequence of category IDs to be unregistered from the class.

## [PyICatRegister](#pyicatregister).UnRegisterClassReqCategories

 __UnRegisterClassReqCategories( *clsid*  *, [catId, ...]* __ )
Unregisters the class as requiring one or more component categories.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    Class ID of the relevent class

  -  *[catId, ...]* : [[PyIID](#pyiid), ...]

    A sequence of category IDs to be unregistered for the class.

## [PyICatRegister](#pyicatregister).UnregisterCategories

 __UnregisterCategories( *[catId, ...]* __ )
Unregister one or more previously registered categories.

#### Parameters


  -  *[catId, ...]* : [[PyIID](#pyiid), ...]

    The list of category IDs to be unregistered.