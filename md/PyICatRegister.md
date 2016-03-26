# PyICatRegister

## PyICatRegister Object



An interface to a COM ICatRegister interface\.

#### Methods


  - [RegisterCategories](PyICatRegister.md#pyicatregisterregistercategories)

    Registers one or more component categories\. Each component category consists of a CATID and a list of locale-dependent description strings\.&nbsp;

  - [UnRegisterCategories](PyICatRegister.md#pyicatregisterunregistercategories)

    Unregister one or more previously registered categories\.&nbsp;

  - [RegisterClassImplCategories](PyICatRegister.md#pyicatregisterregisterclassimplcategories)

    Registers the class as implementing one or more component categories\.&nbsp;

  - [UnRegisterClassImplCategories](PyICatRegister.md#pyicatregisterunregisterclassimplcategories)

    Unregisters the class as implementing one or more component categories\.&nbsp;

  - [RegisterClassReqCategories](PyICatRegister.md#pyicatregisterregisterclassreqcategories)

    Registers the class as requiring one or more component categories\.&nbsp;

  - [UnRegisterClassReqCategories](PyICatRegister.md#pyicatregisterunregisterclassreqcategories)

    Unregisters the class as requiring one or more component categories\.&nbsp;


## [PyICatRegister](#pyicatregister)\.RegisterCategories

RegisterCategories\(\[ \(catId, lcid, description\), \.\.\.\]\)
Registers one or more component categories\. Each component category consists of a CATID and a list of locale-dependent description strings\.

#### Parameters


  - \[ \(catId, lcid, description\), \.\.\.\] : \[ \([PyIID](#pyiid), int, string\), \.\.\.\]

    A sequence of category descriptions\.

## [PyICatRegister](#pyicatregister)\.RegisterClassImplCategories

RegisterClassImplCategories\(clsid, \[catId, \.\.\.\]\)
Registers the class as implementing one or more component categories\.

#### Parameters


  - clsid :[PyIID](#pyiid)

    Class ID of the relevent class

  - \[catId, \.\.\.\] : \[[PyIID](#pyiid), \.\.\.\]

    A sequence of category IDs to be associated with the class\.

## [PyICatRegister](#pyicatregister)\.RegisterClassReqCategories

RegisterClassReqCategories\(clsid, \[catId, \.\.\.\]\)
Registers the class as requiring one or more component categories\.

#### Parameters


  - clsid :[PyIID](#pyiid)

    Class ID of the relevent class

  - \[catId, \.\.\.\] : \[[PyIID](#pyiid), \.\.\.\]

    A sequence of category IDs to be associated with the class\.

## [PyICatRegister](#pyicatregister)\.UnRegisterClassImplCategories

UnRegisterClassImplCategories\(clsid, \[catId, \.\.\.\]\)
Unregisters the class as implementing one or more component categories\.

#### Parameters


  - clsid :[PyIID](#pyiid)

    Class ID of the relevent class

  - \[catId, \.\.\.\] : \[[PyIID](#pyiid), \.\.\.\]

    A sequence of category IDs to be unregistered from the class\.

## [PyICatRegister](#pyicatregister)\.UnRegisterClassReqCategories

UnRegisterClassReqCategories\(clsid, \[catId, \.\.\.\]\)
Unregisters the class as requiring one or more component categories\.

#### Parameters


  - clsid :[PyIID](#pyiid)

    Class ID of the relevent class

  - \[catId, \.\.\.\] : \[[PyIID](#pyiid), \.\.\.\]

    A sequence of category IDs to be unregistered for the class\.

## [PyICatRegister](#pyicatregister)\.UnregisterCategories

UnregisterCategories\(\[catId, \.\.\.\]\)
Unregister one or more previously registered categories\.

#### Parameters


  - \[catId, \.\.\.\] : \[[PyIID](#pyiid), \.\.\.\]

    The list of category IDs to be unregistered\.