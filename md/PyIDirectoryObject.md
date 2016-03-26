# PyIDirectoryObject

## PyIDirectoryObject Object

A COM interface to ADSI's IDirectoryObject interface.
Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [GetObjectInformation](PyIDirectoryObject.md#pyidirectoryobjectgetobjectinformation)

    Retrieves an[PyADS_OBJECT_INFO](PyADS.md#pyadsobject_info)object that contains information about the identity and location of a directory service object.&nbsp;

  - [GetObjectAttributes](PyIDirectoryObject.md#pyidirectoryobjectgetobjectattributes)

    Gets one or more specified attributes of the directory service object, as defined in the[PyADS_ATTR_INFO](PyADS.md#pyadsattr_info)structure.&nbsp;

  - [SetObjectAttributes](PyIDirectoryObject.md#pyidirectoryobjectsetobjectattributes)

    Sets one or more specified attributes of the directory service object, as defined in the[PyADS_ATTR_INFO](PyADS.md#pyadsattr_info)structure.&nbsp;

  - [CreateDSObject](PyIDirectoryObject.md#pyidirectoryobjectcreatedsobject)

    &nbsp;

  - [DeleteDSObject](PyIDirectoryObject.md#pyidirectoryobjectdeletedsobject)

    Deletes a leaf object in a directory tree&nbsp;

## [PyIDirectoryObject](#pyidirectoryobject).CreateDSObject

[PyIDispatch](#pyidispatch)= __CreateDSObject( *rdn*  *, attrs* __ )


#### Parameters


  -  *rdn* :[PyUnicode](#pyunicode)

    The relative distinguished name (relative path) of the object to be created.

  -  *attrs* : ([PyADS_ATTR_INFO](PyADS.md#pyadsattr_info), ...)

    The attributes to set.

## [PyIDirectoryObject](#pyidirectoryobject).DeleteDSObject

 __DeleteDSObject( *rdn* __ )
Deletes a leaf object in a directory tree

#### Parameters


  -  *rdn* : string

    The relative distinguished name (relative path) of the object to be deleted.

## [PyIDirectoryObject](#pyidirectoryobject).GetObjectAttributes

([PyADS_ATTR_INFO](PyADS.md#pyadsattr_info), ...) = __GetObjectAttributes( *names* __ )
Gets one or more specified attributes of the directory service object, as defined in the[PyADS_ATTR_INFO](PyADS.md#pyadsattr_info)structure.

#### Parameters


  -  *names* : ([PyUnicode](#pyunicode), ...)

    

## [PyIDirectoryObject](#pyidirectoryobject).GetObjectInformation

[PyADS_OBJECT_INFO](PyADS.md#pyadsobject_info)= __GetObjectInformation(__ )
Retrieves an[PyADS_OBJECT_INFO](PyADS.md#pyadsobject_info)object that contains information about the identity and location of a directory service object.

## [PyIDirectoryObject](#pyidirectoryobject).SetObjectAttributes

int = __SetObjectAttributes( *attrs* __ )
Sets one or more specified attributes of the directory service object, as defined in the[PyADS_ATTR_INFO](PyADS.md#pyadsattr_info)structure.

#### Parameters


  -  *attrs* : ([PyADS_ATTR_INFO](PyADS.md#pyadsattr_info), ...)

    The attributes to set