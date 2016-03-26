# PyICatInformation

## PyICatInformation Object

A Python interface to ICatInformation

#### Methods


  - [EnumCategories](PyICatInformation.md#pyicatinformationenumcategories)

    Returns an enumerator for the component categories registered on the system.&nbsp;

  - [GetCategoryDesc](PyICatInformation.md#pyicatinformationgetcategorydesc)

    Retrieves the localized description string for a specific category ID.&nbsp;

  - [EnumClassesOfCategories](PyICatInformation.md#pyicatinformationenumclassesofcategories)

    Returns an enumerator over the classes that implement one or more interfaces.&nbsp;


## [PyICatInformation](#pyicatinformation).EnumCategories

[PyIEnumCATEGORYINFO](#pyienumcategoryinfo)= __EnumCategories( *lcid* __ )
Returns an enumerator for the component categories registered on the system.

#### Parameters


  -  *lcid=0* : int

    lcid

## [PyICatInformation](#pyicatinformation).EnumClassesOfCategories

[PyIEnumGUID](#pyienumguid)= __EnumClassesOfCategories( *listIIdImplemented*  *, listIIdRequired* __ )
Returns an enumerator over the classes that implement one or more interfaces.

#### Parameters


  -  *listIIdImplemented=None* : [[PyIID](#pyiid), ...]

    A sequence of[PyIID](#pyiid)objects, or None.

  -  *listIIdRequired=None* : list iid

    A sequence of[PyIID](#pyiid)objects, or None.

## [PyICatInformation](#pyicatinformation).GetCategoryDesc

string = __GetCategoryDesc( *lcid* __ )
Retrieves the localized description string for a specific category ID.

#### Parameters


  -  *lcid=0* : int

    lcid

#### Comments
The return type is a unicode object.