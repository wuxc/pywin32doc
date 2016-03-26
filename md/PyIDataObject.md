# PyIDataObject


## PyIDataObject Object

Used to transfer data in various formats throughout the shell

#### Comments

Can be enumerated to return a series of [PyFORMATETC](PyFORMATETC.md) describing the formats 

that the object can render\.

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

    Sets the data that the object will return\.&nbsp;

  - [EnumFormatEtc](PyIDataObject.md#pyidataobjectenumformatetc)

    Returns an enumerator to list the data formats that the object supports\.&nbsp;

  - [DAdvise](PyIDataObject.md#pyidataobjectdadvise)

    Connects the object to an interface that will receive notifications when its data changes&nbsp;

  - [DUnadvise](PyIDataObject.md#pyidataobjectdunadvise)

    Disconnects a notification sink\.&nbsp;

  - [EnumDAdvise](PyIDataObject.md#pyidataobjectenumdadvise)

    Creates an enumerator to list connected notification sinks\.&nbsp;


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.DAdvise

int = DAdvise\(pformatetc, advf

, pAdvSink

\)
Connects the object to an interface that will receive notifications when its data changes

#### Parameters

  - pformatetc : [PyFORMATETC](PyFORMATETC.md)

    Defines the type of data for which the sink will receive notifications\.

  - advf : int

    Combination of values from ADVF enum\. \(which currently do not appear in any of the constants modules\!\)

  - pAdvSink : PyIAdviseSink

    Currently this interface is not wrapped\.

#### Return Value
Returns a unique number that is used to identify the connection


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.DUnadvise

DUnadvise\(dwConnection\)
Disconnects a notification sink\.

#### Parameters

  - dwConnection : int

    Identifier of the connection as returned by DAdvise\.


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.EnumDAdvise

PyIEnumSTATDATA

 = EnumDAdvise\(\)
Creates an enumerator to list connected notification sinks\.


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.EnumFormatEtc

[PyIEnumFORMATETC](PyIEnumFORMATETC.md) = EnumFormatEtc\(dwDirection\)
Returns an enumerator to list the data formats that the object supports\.

#### Parameters

  - dwDirection=DATADIR\_GET : int

    Indicates whether to return formats that can be queried or set \(pythoncom\.DATADIR\_GET or DATADIR\_SET\)


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.GetCanonicalFormatEtc

[PyFORMATETC](PyFORMATETC.md) = GetCanonicalFormatEtc\(pformatectIn\)
Transforms a FORMATECT data description into a general format that the object supports

#### Parameters

  - pformatectIn : [PyFORMATETC](PyFORMATETC.md)

    Tuple representing a FORMATETC struct describing how the data should be returned


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.GetData

[PySTGMEDIUM](PySTGMEDIUM.md) = GetData\(pformatetcIn\)
Retrieves data from the object in specified format

#### Parameters

  - pformatetcIn : [PyFORMATETC](PyFORMATETC.md)

    Tuple representing a FORMATETC struct describing how the data should be returned


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.GetDataHere

[PySTGMEDIUM](PySTGMEDIUM.md) = GetDataHere\(pformatetcIn\)
Retunrs a copy of the object's data in specified format

#### Parameters

  - pformatetcIn : [PyFORMATETC](PyFORMATETC.md)

    Tuple representing a FORMATETC struct describing how the data should be returned


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.QueryGetData

QueryGetData\(pformatetc\)
Checks if the objects supports returning data in a particular format\.

#### Parameters

  - pformatetc : [PyFORMATETC](PyFORMATETC.md)

    Tuple representing a FORMATETC struct describing how the data should be returned

#### Return Value
Returns None if the object supports the specified format, otherwise an error is raised\.


## [PyIDataObject](PyIDataObject.md#pyidataobject)\.SetData

SetData\(pformatetc, pmedium, fRelease\)
Sets the data that the object will return\.

#### Parameters

  - pformatetc : [PyFORMATETC](PyFORMATETC.md)

    Tuple representing a FORMATETC struct describing the type of data to be set

  - pmedium : [PySTGMEDIUM](PySTGMEDIUM.md)

    The data to be placed in the object

  - fRelease : boolean

    If True, transfers ownership of the data to the object\.  If False, caller is responsible for releasing the STGMEDIUM\.