# PySTGMEDIUM


## PySTGMEDIUM Object

A STGMEDIUM object represents a COM STGMEDIUM structure\.

#### Methods

  - [set](PySTGMEDIUM.md#pystgmediumset)

    Sets the type and data of the object&nbsp;

#### Properties

  - int tymed

    An integer indicating the type of data in the stgmedium

  - object data

    The data in the stgmedium\. 

The result depends on the value of the 'tymed' property of the PySTGMEDIUM object\.

   

       tymed

   

   

       Result Type

   

TYMED\_GDIAn integer GDI handle

TYMED\_MFPICTAn integer METAFILE handle

TYMED\_ENHMFAn integer ENHMETAFILE handle

TYMED\_HGLOBALA string with the bytes of the global memory object\.

TYMED\_FILEA string/unicode filename

TYMED\_ISTREAMA [PyIStream](PyIStream.md) object

TYMED\_ISTORAGEA [PyIStorage](PyIStorage.md) object

  - int data\_handle

    The raw 'integer' representation of the data\. 

For TYMED\_HGLOBAL, this is the handle rather than the string data\. 

For the string and interface types, this is an integer holding the pointer\.


## [PySTGMEDIUM](PySTGMEDIUM.md#pystgmedium)\.set

set\(tymed, data\)
Sets the type and data of the object\.

#### Parameters

  - tymed : int

    The type of the data

  - data : object

    