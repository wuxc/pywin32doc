# PyIDataObject

## PyIDataObject Object

Used to transfer data in various formats throughout the shell

#### Comments
Can be enumerated to return a series of[PyFORMATETC](#pyformatetc)describing the formats 

that the object can render.

#### Methods


  - [GetData](PyIDataObject.md#pyidataobjectgetdata)

    Retrieves data from the object in specified format&nbsp;

  - [GetDataHere](PyIDataObject.md#pyidataobjectgetdatahere)

    Returns a copy of the object's data in specified format&nbsp;

  - [QueryGetData](PyIDataObject.md#pyidataobjectquerygetdata)

    Checks if the object supports returning data in a particular format&nbsp;

  - [GetCanonicalFormatEtc](PyIDataObject.md#pyidataobjectgetcanonicalformatetc)

    Transforms a FORMATECT data description into a general format that the object supports&nbsp;

  - [SetData](PyIDataObject.md#pyidataobjectsetdata)

    Sets the data that the object will return.&nbsp;

  - [EnumFormatEtc](PyIDataObject.md#pyidataobjectenumformatetc)

    Returns an enumerator to list the data formats that the object supports.&nbsp;

  - [DAdvise](PyIDataObject.md#pyidataobjectdadvise)

    Connects the object to an interface that will receive notifications when its data changes&nbsp;

  - [DUnadvise](PyIDataObject.md#pyidataobjectdunadvise)

    Disconnects a notification sink.&nbsp;

  - [EnumDAdvise](PyIDataObject.md#pyidataobjectenumdadvise)

    Creates an enumerator to list connected notification sinks.&nbsp;

## [PyIDataObject](#pyidataobject).DAdvise

int = __DAdvise( *pformatetc*  *, advf*  *, pAdvSink* __ )
Connects the object to an interface that will receive notifications when its data changes

#### Parameters


  -  *pformatetc* :[PyFORMATETC](#pyformatetc)

    Defines the type of data for which the sink will receive notifications.

  -  *advf* : int

    Combination of values from ADVF enum. (which currently do not appear in any of the constants modules!)

  -  *pAdvSink* : __PyIAdviseSink__ 

    Currently this interface is not wrapped.

#### Return Value
Returns a unique number that is used to identify the connection

## [PyIDataObject](#pyidataobject).DUnadvise

 __DUnadvise( *dwConnection* __ )
Disconnects a notification sink.

#### Parameters


  -  *dwConnection* : int

    Identifier of the connection as returned by DAdvise.

## [PyIDataObject](#pyidataobject).EnumDAdvise

 __PyIEnumSTATDATA__ = __EnumDAdvise(__ )
Creates an enumerator to list connected notification sinks.

## [PyIDataObject](#pyidataobject).EnumFormatEtc

[PyIEnumFORMATETC](#pyienumformatetc)= __EnumFormatEtc( *dwDirection* __ )
Returns an enumerator to list the data formats that the object supports.

#### Parameters


  -  *dwDirection=DATADIR_GET* : int

    Indicates whether to return formats that can be queried or set (pythoncom.DATADIR_GET or DATADIR_SET)

## [PyIDataObject](#pyidataobject).GetCanonicalFormatEtc

[PyFORMATETC](#pyformatetc)= __GetCanonicalFormatEtc( *pformatectIn* __ )
Transforms a FORMATECT data description into a general format that the object supports

#### Parameters


  -  *pformatectIn* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

## [PyIDataObject](#pyidataobject).GetData

[PySTGMEDIUM](#pystgmedium)= __GetData( *pformatetcIn* __ )
Retrieves data from the object in specified format

#### Parameters


  -  *pformatetcIn* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

## [PyIDataObject](#pyidataobject).GetDataHere

[PySTGMEDIUM](#pystgmedium)= __GetDataHere( *pformatetcIn* __ )
Retunrs a copy of the object's data in specified format

#### Parameters


  -  *pformatetcIn* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

## [PyIDataObject](#pyidataobject).QueryGetData

 __QueryGetData( *pformatetc* __ )
Checks if the objects supports returning data in a particular format.

#### Parameters


  -  *pformatetc* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

#### Return Value
Returns None if the object supports the specified format, otherwise an error is raised.

## [PyIDataObject](#pyidataobject).SetData

 __SetData( *pformatetc*  *, pmedium*  *, fRelease* __ )
Sets the data that the object will return.

#### Parameters


  -  *pformatetc* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing the type of data to be set

  -  *pmedium* :[PySTGMEDIUM](#pystgmedium)

    The data to be placed in the object

  -  *fRelease* : boolean

    If True, transfers ownership of the data to the object.  If False, caller is responsible for releasing the STGMEDIUM.