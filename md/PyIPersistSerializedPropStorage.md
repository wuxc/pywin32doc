# PyIPersistSerializedPropStorage

## PyIPersistSerializedPropStorage Object

Allows a property store to be marshalled into a single buffer\. 

Primarily used with property stores created using[propsys::PSCreateMemoryPropertyStore](propsys.md#propsyspscreatememorypropertystore)\.

#### Methods


  - [SetFlags](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragesetflags)

    Sets flags for the store&nbsp;

  - [SetPropertyStorage](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragesetpropertystorage)

    Initializes the store with a serialized buffer&nbsp;

  - [GetPropertyStorage](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragegetpropertystorage)

    Retrieves the current contents of the property store&nbsp;

## [PyIPersistSerializedPropStorage](#pyipersistserializedpropstorage)\.GetPropertyStorage

buffer \= **GetPropertyStorage\(** \)
Retrieves the current contents of the property store

## [PyIPersistSerializedPropStorage](#pyipersistserializedpropstorage)\.SetFlags

 **SetFlags\( *flags* ** \)
Sets flags for the store

#### Parameters


  -  *flags* : int

    Combination of pscon\.FPSPS\_\* values

## [PyIPersistSerializedPropStorage](#pyipersistserializedpropstorage)\.SetPropertyStorage

 **SetPropertyStorage\( *ps* ** \)
Initializes the store with a serialized buffer

#### Parameters


  -  *ps* : buffer

    Bytes or buffer object containing a serialized property store