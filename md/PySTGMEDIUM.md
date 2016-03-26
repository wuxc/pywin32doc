# PySTGMEDIUM

## PySTGMEDIUM Object

A STGMEDIUM object represents a COM STGMEDIUM structure.

#### Methods


  - [set](PySTGMEDIUM.md#pystgmediumset)

    Sets the type and data of the object&nbsp;

#### Properties

  -  __int tymed__ 
    An integer indicating the type of data in the stgmedium

  -  __object data__ 
    The data in the stgmedium. 

The result depends on the value of the 'tymed' property of the __PySTGMEDIUM__ object.

 __tymed__  __Result Type__ TYMED_GDIAn integer GDI handleTYMED_MFPICTAn integer METAFILE handleTYMED_ENHMFAn integer ENHMETAFILE handleTYMED_HGLOBALA string with the bytes of the global memory object.TYMED_FILEA string/unicode filenameTYMED_ISTREAMA[PyIStream](#pyistream)objectTYMED_ISTORAGEA[PyIStorage](#pyistorage)object
  -  __int data_handle__ 
    The raw 'integer' representation of the data. 

For TYMED_HGLOBAL, this is the handle rather than the string data. 

For the string and interface types, this is an integer holding the pointer.

## [PySTGMEDIUM](#pystgmedium).set

 __set( *tymed*  *, data* __ )
Sets the type and data of the object.

#### Parameters


  -  *tymed* : int

    The type of the data

  -  *data* : object

    