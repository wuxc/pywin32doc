# PyIDirectoryObject


## PyIDirectoryObject Object

A COM interface to ADSI's IDirectoryObject interface\. 

Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [GetObjectInformation](PyIDirectoryObject.md#pyidirectoryobjectgetobjectinformation)

    Retrieves an [PyADS\_OBJECT\_INFO](PyADS.md#pyadsobject_info) object that contains information about the identity and location of a directory service object\.&nbsp;

  - [GetObjectAttributes](PyIDirectoryObject.md#pyidirectoryobjectgetobjectattributes)

    Gets one or more specified attributes of the directory service object, as defined in the [PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info) structure\.&nbsp;

  - [SetObjectAttributes](PyIDirectoryObject.md#pyidirectoryobjectsetobjectattributes)

    Sets one or more specified attributes of the directory service object, as defined in the [PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info) structure\.&nbsp;

  - [CreateDSObject](PyIDirectoryObject.md#pyidirectoryobjectcreatedsobject)

    &nbsp;

  - [DeleteDSObject](PyIDirectoryObject.md#pyidirectoryobjectdeletedsobject)

    Deletes a leaf object in a directory tree&nbsp;


## [PyIDirectoryObject](PyIDirectoryObject.md#pyidirectoryobject)\.CreateDSObject

[PyIDispatch](PyIDispatch.md) = CreateDSObject\(rdn, attrs

\)

#### Parameters

  - rdn : [PyUnicode](PyUnicode.md)

    The relative distinguished name \(relative path\) of the object to be created\.

  - attrs : \([PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info), \.\.\.\)

    The attributes to set\.


## [PyIDirectoryObject](PyIDirectoryObject.md#pyidirectoryobject)\.DeleteDSObject

DeleteDSObject\(rdn\)
Deletes a leaf object in a directory tree

#### Parameters

  - rdn : string

    The relative distinguished name \(relative path\) of the object to be deleted\.


## [PyIDirectoryObject](PyIDirectoryObject.md#pyidirectoryobject)\.GetObjectAttributes

\([PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info), \.\.\.\) = GetObjectAttributes\(names\)
Gets one or more specified attributes of the directory service object, as defined in the [PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info) structure\.

#### Parameters

  - names : \([PyUnicode](PyUnicode.md), \.\.\.\)

    


## [PyIDirectoryObject](PyIDirectoryObject.md#pyidirectoryobject)\.GetObjectInformation

[PyADS\_OBJECT\_INFO](PyADS.md#pyadsobject_info) = GetObjectInformation\(\)
Retrieves an [PyADS\_OBJECT\_INFO](PyADS.md#pyadsobject_info) object that contains information about the identity and location of a directory service object\.


## [PyIDirectoryObject](PyIDirectoryObject.md#pyidirectoryobject)\.SetObjectAttributes

int = SetObjectAttributes\(attrs\)
Sets one or more specified attributes of the directory service object, as defined in the [PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info) structure\.

#### Parameters

  - attrs : \([PyADS\_ATTR\_INFO](PyADS.md#pyadsattr_info), \.\.\.\)

    The attributes to set