# adsi

## Module adsi

A COM interface to ADSI

#### Methods


  - [ADsOpenObject](adsi.md#adsiadsopenobject)

    Binds to an ADSI object using explicit username and password credentials\.&nbsp;

  - [ADsGetObject](adsi.md#adsiadsgetobject)

    Binds to an object given its path and a specified interface identifier \(IID\)\.&nbsp;

  - [ADsBuildEnumerator](adsi.md#adsiadsbuildenumerator)

    Builds an enumerator object for the specified ADSI container object\.&nbsp;

  - [ADsEnumerateNext](adsi.md#adsiadsenumeratenext)

    &nbsp;

  - [ADsGetLastError](adsi.md#adsiadsgetlasterror)

    &nbsp;

  - [StringAsDS\_SELECTION\_LIST](adsi.md#adsistringasds_selection_list)

    Unpacks a string \(generally fetched via[PyIDataObject::GetData](PyIDataObject.md#pyidataobjectgetdata)\) into a **PyDS\_SELECTION\_LIST** list\.&nbsp;

  - [DSOP\_SCOPE\_INIT\_INFOs](adsi.md#adsidsop_scope_init_infos)

    The type object for[PyDSOP\_SCOPE\_INIT\_INFOs](PyDSOP.md#pydsopscope_init_infos)objects\.&nbsp;

## [adsi](#adsi)\.ADsBuildEnumerator

 **PyIEnumerator** \= **ADsBuildEnumerator\( *container* ** \)
Builds an enumerator object for the specified ADSI container object\.

#### Parameters


  -  *container* :[PyIADsContainer](#pyiadscontainer)

    

## [adsi](#adsi)\.ADsEnumerateNext

 **PyIEnumerator** \= **ADsEnumerateNext\( *enum*  *, num* ** \)


#### Parameters


  -  *enum* : **PyIEnumVARIANT** 

    The enumerator\.

  -  *num\=1* : int

    Number of items to retrieve\.

#### Return Value
The result is a tuple of Python objects converted from Variants, 

one for each element returned\.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned\.

## [adsi](#adsi)\.ADsGetLastError

\(int, unicode, unicode\) \= **ADsGetLastError\(** \)


## [adsi](#adsi)\.ADsGetObject

com\_object \= **ADsGetObject\( *path*  *, iid* ** \)
Binds to an object given its path and a specified interface identifier \(IID\)\.

#### Parameters


  -  *path* : unicode

    

  -  *iid\=IID\_IDispatch* :[PyIID](#pyiid)

    The requested interface

## [adsi](#adsi)\.ADsOpenObject

com\_object \= **ADsOpenObject\( *path*  *, username*  *, password*  *, reserved*  *, iid* ** \)
Binds to an ADSI object using explicit username and password credentials\.

#### Parameters


  -  *path* : unicode

    

  -  *username* : unicode

    

  -  *password* : unicode

    

  -  *reserved\=0* : int

    

  -  *iid\=IID\_IDispatch* :[PyIID](#pyiid)

    The requested interface

## [adsi](#adsi)\.DSOP\_SCOPE\_INIT\_INFOs

 **DSOP\_SCOPE\_INIT\_INFOs** \= **DSOP\_SCOPE\_INIT\_INFOs\( *size* ** \)
The type object for[PyDSOP\_SCOPE\_INIT\_INFOs](PyDSOP.md#pydsopscope_init_infos)objects\.

#### Parameters


  -  *size* : int

    The number of[PyDSOP\_SCOPE\_INIT\_INFO](PyDSOP.md#pydsopscope_init_info)objects to create in the array\.

## [adsi](#adsi)\.StringAsDS\_SELECTION\_LIST

 **PyDS\_SELECTION\_LIST** \= **StringAsDS\_SELECTION\_LIST\( *buf* ** \)
Unpacks a string \(generally fetched via[PyIDataObject::GetData](PyIDataObject.md#pyidataobjectgetdata)\) into a **PyDS\_SELECTION\_LIST** list\.

#### Parameters


  -  *buf* : str

    The raw buffer