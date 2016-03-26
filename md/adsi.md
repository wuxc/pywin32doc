# adsi

## Module adsi

A COM interface to ADSI

#### Methods


  - [ADsOpenObject](adsi.md#adsiadsopenobject)

    Binds to an ADSI object using explicit username and password credentials.&nbsp;

  - [ADsGetObject](adsi.md#adsiadsgetobject)

    Binds to an object given its path and a specified interface identifier (IID).&nbsp;

  - [ADsBuildEnumerator](adsi.md#adsiadsbuildenumerator)

    Builds an enumerator object for the specified ADSI container object.&nbsp;

  - [ADsEnumerateNext](adsi.md#adsiadsenumeratenext)

    &nbsp;

  - [ADsGetLastError](adsi.md#adsiadsgetlasterror)

    &nbsp;

  - [StringAsDS_SELECTION_LIST](adsi.md#adsistringasds_selection_list)

    Unpacks a string (generally fetched via[PyIDataObject::GetData](PyIDataObject.md#pyidataobjectgetdata)) into a __PyDS_SELECTION_LIST__ list.&nbsp;

  - [DSOP_SCOPE_INIT_INFOs](adsi.md#adsidsop_scope_init_infos)

    The type object for[PyDSOP_SCOPE_INIT_INFOs](PyDSOP.md#pydsopscope_init_infos)objects.&nbsp;

## [adsi](#adsi).ADsBuildEnumerator

 __PyIEnumerator__ = __ADsBuildEnumerator( *container* __ )
Builds an enumerator object for the specified ADSI container object.

#### Parameters


  -  *container* :[PyIADsContainer](#pyiadscontainer)

    

## [adsi](#adsi).ADsEnumerateNext

 __PyIEnumerator__ = __ADsEnumerateNext( *enum*  *, num* __ )


#### Parameters


  -  *enum* : __PyIEnumVARIANT__ 

    The enumerator.

  -  *num=1* : int

    Number of items to retrieve.

#### Return Value
The result is a tuple of Python objects converted from Variants, 

one for each element returned.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned.

## [adsi](#adsi).ADsGetLastError

(int, unicode, unicode) = __ADsGetLastError(__ )


## [adsi](#adsi).ADsGetObject

com_object = __ADsGetObject( *path*  *, iid* __ )
Binds to an object given its path and a specified interface identifier (IID).

#### Parameters


  -  *path* : unicode

    

  -  *iid=IID_IDispatch* :[PyIID](#pyiid)

    The requested interface

## [adsi](#adsi).ADsOpenObject

com_object = __ADsOpenObject( *path*  *, username*  *, password*  *, reserved*  *, iid* __ )
Binds to an ADSI object using explicit username and password credentials.

#### Parameters


  -  *path* : unicode

    

  -  *username* : unicode

    

  -  *password* : unicode

    

  -  *reserved=0* : int

    

  -  *iid=IID_IDispatch* :[PyIID](#pyiid)

    The requested interface

## [adsi](#adsi).DSOP_SCOPE_INIT_INFOs

 __DSOP_SCOPE_INIT_INFOs__ = __DSOP_SCOPE_INIT_INFOs( *size* __ )
The type object for[PyDSOP_SCOPE_INIT_INFOs](PyDSOP.md#pydsopscope_init_infos)objects.

#### Parameters


  -  *size* : int

    The number of[PyDSOP_SCOPE_INIT_INFO](PyDSOP.md#pydsopscope_init_info)objects to create in the array.

## [adsi](#adsi).StringAsDS_SELECTION_LIST

 __PyDS_SELECTION_LIST__ = __StringAsDS_SELECTION_LIST( *buf* __ )
Unpacks a string (generally fetched via[PyIDataObject::GetData](PyIDataObject.md#pyidataobjectgetdata)) into a __PyDS_SELECTION_LIST__ list.

#### Parameters


  -  *buf* : str

    The raw buffer