# PyICatInformation


## PyICatInformation Object

A Python interface to ICatInformation

#### Methods

  - [EnumCategories](PyICatInformation.md#pyicatinformationenumcategories)

    Returns an enumerator for the component categories registered on the system\.&nbsp;

  - [GetCategoryDesc](PyICatInformation.md#pyicatinformationgetcategorydesc)

    Retrieves the localized description string for a specific category ID\.&nbsp;

  - [EnumClassesOfCategories](PyICatInformation.md#pyicatinformationenumclassesofcategories)

    Returns an enumerator over the classes that implement one or more interfaces\.&nbsp;




## [PyICatInformation](PyICatInformation.md#pyicatinformation)\.EnumCategories

[PyIEnumCATEGORYINFO](PyIEnumCATEGORYINFO.md) = EnumCategories\(lcid\)
Returns an enumerator for the component categories registered on the system\.

#### Parameters

  - lcid=0 : int

    lcid


## [PyICatInformation](PyICatInformation.md#pyicatinformation)\.EnumClassesOfCategories

[PyIEnumGUID](PyIEnumGUID.md) = EnumClassesOfCategories\(listIIdImplemented, listIIdRequired

\)
Returns an enumerator over the classes that implement one or more interfaces\.

#### Parameters

  - listIIdImplemented=None : \[[PyIID](PyIID.md), \.\.\.\]

    A sequence of [PyIID](PyIID.md) objects, or None\.

  - listIIdRequired=None : list iid

    A sequence of [PyIID](PyIID.md) objects, or None\.


## [PyICatInformation](PyICatInformation.md#pyicatinformation)\.GetCategoryDesc

string = GetCategoryDesc\(lcid\)
Retrieves the localized description string for a specific category ID\.

#### Parameters

  - lcid=0 : int

    lcid

#### Comments

The return type is a unicode object\.