# PyIDataObject

## PyIDataObject Object

Used to transfer data in various formats throughout the shell

#### Comments
Can be enumerated to return a series of[PyFORMATETC](#pyformatetc)describing the formats 

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

## [PyIDataObject](#pyidataobject)\.DAdvise

int \= **DAdvise\( *pformatetc*  *, advf*  *, pAdvSink* ** \)
Connects the object to an interface that will receive notifications when its data changes

#### Parameters


  -  *pformatetc* :[PyFORMATETC](#pyformatetc)

    Defines the type of data for which the sink will receive notifications\.

  -  *advf* : int

    Combination of values from ADVF enum\. \(which currently do not appear in any of the constants modules\!\)

  -  *pAdvSink* : **PyIAdviseSink** 

    Currently this interface is not wrapped\.

#### Return Value
Returns a unique number that is used to identify the connection

## [PyIDataObject](#pyidataobject)\.DUnadvise

 **DUnadvise\( *dwConnection* ** \)
Disconnects a notification sink\.

#### Parameters


  -  *dwConnection* : int

    Identifier of the connection as returned by DAdvise\.

## [PyIDataObject](#pyidataobject)\.EnumDAdvise

 **PyIEnumSTATDATA** \= **EnumDAdvise\(** \)
Creates an enumerator to list connected notification sinks\.

## [PyIDataObject](#pyidataobject)\.EnumFormatEtc

[PyIEnumFORMATETC](#pyienumformatetc)\= **EnumFormatEtc\( *dwDirection* ** \)
Returns an enumerator to list the data formats that the object supports\.

#### Parameters


  -  *dwDirection\=DATADIR\_GET* : int

    Indicates whether to return formats that can be queried or set \(pythoncom\.DATADIR\_GET or DATADIR\_SET\)

## [PyIDataObject](#pyidataobject)\.GetCanonicalFormatEtc

[PyFORMATETC](#pyformatetc)\= **GetCanonicalFormatEtc\( *pformatectIn* ** \)
Transforms a FORMATECT data description into a general format that the object supports

#### Parameters


  -  *pformatectIn* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

## [PyIDataObject](#pyidataobject)\.GetData

[PySTGMEDIUM](#pystgmedium)\= **GetData\( *pformatetcIn* ** \)
Retrieves data from the object in specified format

#### Parameters


  -  *pformatetcIn* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

## [PyIDataObject](#pyidataobject)\.GetDataHere

[PySTGMEDIUM](#pystgmedium)\= **GetDataHere\( *pformatetcIn* ** \)
Retunrs a copy of the object's data in specified format

#### Parameters


  -  *pformatetcIn* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

## [PyIDataObject](#pyidataobject)\.QueryGetData

 **QueryGetData\( *pformatetc* ** \)
Checks if the objects supports returning data in a particular format\.

#### Parameters


  -  *pformatetc* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing how the data should be returned

#### Return Value
Returns None if the object supports the specified format, otherwise an error is raised\.

## [PyIDataObject](#pyidataobject)\.SetData

 **SetData\( *pformatetc*  *, pmedium*  *, fRelease* ** \)
Sets the data that the object will return\.

#### Parameters


  -  *pformatetc* :[PyFORMATETC](#pyformatetc)

    Tuple representing a FORMATETC struct describing the type of data to be set

  -  *pmedium* :[PySTGMEDIUM](#pystgmedium)

    The data to be placed in the object

  -  *fRelease* : boolean

    If True, transfers ownership of the data to the object\.  If False, caller is responsible for releasing the STGMEDIUM\.