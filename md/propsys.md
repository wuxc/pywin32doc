# propsys


## Module propsys

A module, encapsulating the Vista Property System interfaces

#### Methods

  - [PSGetItemPropertyHandler](propsys.md#propsyspsgetitempropertyhandler)

    Retrieves the property store for a shell item&nbsp;

  - [PSGetPropertyDescription](propsys.md#propsyspsgetpropertydescription)

    Gets a description interface for a property&nbsp;

  - [PSGetPropertySystem](propsys.md#propsyspsgetpropertysystem)

    Creates an IPropertySystem interface&nbsp;

  - [PSGetNameFromPropertyKey](propsys.md#propsyspsgetnamefrompropertykey)

    Retrieves the canonical name for a property key&nbsp;

  - [PSGetPropertyKeyFromName](propsys.md#propsyspsgetpropertykeyfromname)

    Retrieves the property key by canonical name&nbsp;

  - [PSRegisterPropertySchema](propsys.md#propsyspsregisterpropertyschema)

    Registers a group of properties described in a schema file&nbsp;

  - [PSUnregisterPropertySchema](propsys.md#propsyspsunregisterpropertyschema)

    Removes a property schema definition&nbsp;

  - [SHGetPropertyStoreFromParsingName](propsys.md#propsysshgetpropertystorefromparsingname)

    Retrieves the property store for an item by path&nbsp;

  - [StgSerializePropVariant](propsys.md#propsysstgserializepropvariant)

    Serializes a [PyPROPVARIANT](PyPROPVARIANT.md)&nbsp;

  - [StgDeserializePropVariant](propsys.md#propsysstgdeserializepropvariant)

    Creates a [PyPROPVARIANT](PyPROPVARIANT.md) from a serialized buffer&nbsp;

  - [PSCreateMemoryPropertyStore](propsys.md#propsyspscreatememorypropertystore)

    Creates a temporary property store that is not connected to any backing storage&nbsp;

  - [PSCreatePropertyStoreFromPropertySetStorage](propsys.md#propsyspscreatepropertystorefrompropertysetstorage)

    Wraps a [PyIPropertySetStorage](PyIPropertySetStorage.md) interface in a [PyIPropertyStore](PyIPropertyStore.md) object&nbsp;

  - [PSLookupPropertyHandlerCLSID](propsys.md#propsyspslookuppropertyhandlerclsid)

    Returns the GUID of the property handler for a file&nbsp;

  - [SHGetPropertyStoreForWindow](propsys.md#propsysshgetpropertystoreforwindow)

    Retrieves a collection of a window's properties&nbsp;

  - [PSGetPropertyFromPropertyStorage](propsys.md#propsyspsgetpropertyfrompropertystorage)

    Extracts a property from a serialized buffer by key&nbsp;

  - [PSGetNamedPropertyFromPropertyStorage](propsys.md#propsyspsgetnamedpropertyfrompropertystorage)

    Extracts a property from a serialized buffer by name&nbsp;

  - [PSCreateSimplePropertyChange](propsys.md#propsyspscreatesimplepropertychange)

    Creates a [PyIPropertyChange](PyIPropertyChange.md) interface used to apply changes to a [PyPROPVARIANT](PyPROPVARIANT.md)&nbsp;

  - [PSCreatePropertyChangeArray](propsys.md#propsyspscreatepropertychangearray)

    Creates a [PyIPropertyChangeArray](PyIPropertyChangeArray.md) interface to be used with [PyIFileOperation](PyIFileOperation.md)&nbsp;

  - [SHSetDefaultProperties](propsys.md#propsysshsetdefaultproperties)

    Sets the default properties for a file\.&nbsp;


## [propsys](propsys.md#propsys)\.PSCreateMemoryPropertyStore

[PyIPropertyStore](PyIPropertyStore.md) = PSCreateMemoryPropertyStore\(riid\)
Creates a temporary property store that is not connected to any backing storage

#### Parameters

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to create

#### Comments

May also be used to create [PyINamedPropertyStore](PyINamedPropertyStore.md), [PyIPropertyStoreCache](PyIPropertyStoreCache.md), [PyIPersistStream](PyIPersistStream.md), or [PyIPropertyBag](PyIPropertyBag.md)


## [propsys](propsys.md#propsys)\.PSCreatePropertyChangeArray

[PyIPropertyChangeArray](PyIPropertyChangeArray.md) = PSCreatePropertyChangeArray\(\)
Creates an IPropertyChangeArray interface to be used with [PyIFileOperation](PyIFileOperation.md)

#### Comments

Currently only creates an empty array to be filled in later


## [propsys](propsys.md#propsys)\.PSCreatePropertyStoreFromPropertySetStorage

[PyIPropertyStore](PyIPropertyStore.md) = PSCreatePropertyStoreFromPropertySetStorage\(pss, Mode

, riid

\)
Wraps a [PyIPropertySetStorage](PyIPropertySetStorage.md) interface in a [PyIPropertyStore](PyIPropertyStore.md) object

#### Parameters

  - pss : [PyIPropertySetStorage](PyIPropertySetStorage.md)

    Property container to be adapted

  - Mode : int

    Read or write mode, shellcon\.STGM\_\*\.  Must match mode used to open input interface\.

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to create

#### Comments

This function does not work for the NTFS property storage implementation based on 

alternate data streams\.


## [propsys](propsys.md#propsys)\.PSCreateSimplePropertyChange

[PyIPropertyChange](PyIPropertyChange.md) = PSCreateSimplePropertyChange\(flags, key

, val

, riid

\)
Creates an IPropertyChange interface used to apply changes to a [PyPROPVARIANT](PyPROPVARIANT.md)

#### Parameters

  - flags : int

    The change operation, pscon\.PKA\_\*

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    The property key

  - val : [PyPROPVARIANT](PyPROPVARIANT.md)

    The value that the change operation will apply

  - riid=IID\_IPropertyChange : [PyIID](PyIID.md)

    The interface to return\.


## [propsys](propsys.md#propsys)\.PSGetItemPropertyHandler

[PyIPropertyStore](PyIPropertyStore.md) = PSGetItemPropertyHandler\(Item, ReadWrite

, riid

\)
Retrieves the property store for a shell item

#### Parameters

  - Item : [PyIShellItem](PyIShellItem.md)

    A shell item

  - ReadWrite=False : bool

    Pass True for a writeable property store

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    Interface to return


## [propsys](propsys.md#propsys)\.PSGetNameFromPropertyKey

string = PSGetNameFromPropertyKey\(Key\)
Retrieves the canonical name of a property

#### Parameters

  - Key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    A property key


## [propsys](propsys.md#propsys)\.PSGetNamedPropertyFromPropertyStorage

[PyPROPVARIANT](PyPROPVARIANT.md) = PSGetNamedPropertyFromPropertyStorage\(ps, name

\)
Extracts a property value from a serialized buffer by name

#### Parameters

  - ps : buffer

    Bytes or buffer \(or str in python 2\) containing a serialized property set \(see [PyIPersistSerializedPropStorage::GetPropertyStorage](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragegetpropertystorage)\)

  - name : str

    Property to return


## [propsys](propsys.md#propsys)\.PSGetPropertyDescription

[PyIPropertyDescription](PyIPropertyDescription.md) = PSGetPropertyDescription\(Key, riid

\)
Gets a description interface for a property

#### Parameters

  - Key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    A property key identifier

  - riid=IID\_IPropertyDescription : [PyIID](PyIID.md)

    The interface to return

#### Comments

Possible interfaces include IPropertyDescription, IPropertyDescriptionAliasInfo, and IPropertyDescriptionSearchInfo


## [propsys](propsys.md#propsys)\.PSGetPropertyFromPropertyStorage

[PyPROPVARIANT](PyPROPVARIANT.md) = PSGetPropertyFromPropertyStorage\(ps, key

\)
Extracts a property value from a serialized buffer by key

#### Parameters

  - ps : buffer

    Bytes or buffer \(or str in python 2\) containing a serialized property set \(see [PyIPersistSerializedPropStorage::GetPropertyStorage](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragegetpropertystorage)\)

  - key : [PyPROPERTYKEY](PyPROPERTYKEY.md)

    Property to return


## [propsys](propsys.md#propsys)\.PSGetPropertyKeyFromName

[PyPROPERTYKEY](PyPROPERTYKEY.md) = PSGetPropertyKeyFromName\(Name\)
Retrieves the property key by canonical name

#### Parameters

  - Name : str

    The canonical name of a property \(eg System\.Author\)


## [propsys](propsys.md#propsys)\.PSGetPropertySystem

[PyIPropertySystem](PyIPropertySystem.md) = PSGetPropertySystem\(riid\)
Creates an IPropertySystem interface

#### Parameters

  - riid=IID\_IPropertySystem : [PyIID](PyIID.md)

    The interface to return


## [propsys](propsys.md#propsys)\.PSLookupPropertyHandlerCLSID

[PyIID](PyIID.md) = PSLookupPropertyHandlerCLSID\(FilePath\)
Returns the GUID of the property handler for a file

#### Parameters

  - FilePath : str

    Name of file

#### Comments

If no handler is found, the returned error code can be deceptive as it seems to indicate 

that the file itself was not found


## [propsys](propsys.md#propsys)\.PSRegisterPropertySchema

PSRegisterPropertySchema\(filename\)
Registers a group of properties described in a schema file

#### Parameters

  - filename : unicode

    An XML file that defines a property schema \(\*\.propdesc\)


## [propsys](propsys.md#propsys)\.PSUnregisterPropertySchema

PSUnregisterPropertySchema\(filename\)
Removes a property schema definition

#### Parameters

  - filename : unicode

    A previously registered schema definition file


## [propsys](propsys.md#propsys)\.SHGetPropertyStoreForWindow

[PyIPropertyStore](PyIPropertyStore.md) = SHGetPropertyStoreForWindow\(hwnd, riid

\)
Retrieves a collection of a window's properties

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Handle to a window

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to create

#### Comments

Requires Windows 7 or later\.

#### Return Value
The returned store can be used to set the System\.AppUserModel\.ID property that determines how windows 

are grouped on the taskbar


## [propsys](propsys.md#propsys)\.SHGetPropertyStoreFromParsingName

[PyIPropertyStore](PyIPropertyStore.md) = SHGetPropertyStoreFromParsingName\(Path, BindCtx

, Flags

, riid

\)
Retrieves the property store for an item by path

#### Parameters

  - Path : string

    Path to file

  - BindCtx=None : [PyIBindCtx](PyIBindCtx.md)

    Bind context, or None

  - Flags=GPS\_DEFAULT : int

    Combination of GETPROPERTYSTOREFLAGS values \(shellcon\.GPS\_\*\)

  - riid=IID\_IPropertyStore : [PyIID](PyIID.md)

    The interface to return

#### Comments

This function does not exist on XP, even with Desktop Search installed


## [propsys](propsys.md#propsys)\.SHSetDefaultProperties

SHSetDefaultProperties\(hwnd, Item, FileOpFlags, Sink\)
Sets the default properties for a file\.

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Parent window for any notifications, can be None

  - Item : [PyIShellItem](PyIShellItem.md)

    Shell item whose defaults are to be set

  - FileOpFlags=0 : int

    File operation flags, as used with [PyIFileOperation::SetOperationFlags](PyIFileOperation.md#pyifileoperationsetoperationflags)

  - Sink=None : [PyGFileOperationProgressSink](PyGFileOperationProgressSink.md)

    Event sink to receive notifications

#### Comments

Default properties are registered by filetype under SetDefaultsFor value\.


## [propsys](propsys.md#propsys)\.StgDeserializePropVariant

[PyPROPVARIANT](PyPROPVARIANT.md) = StgDeserializePropVariant\(prop\)
Creates a [PyPROPVARIANT](PyPROPVARIANT.md) from a serialized buffer

#### Parameters

  - prop : bytes

    Buffer or bytes object \(or str in Python 2\) containing a serialized value


## [propsys](propsys.md#propsys)\.StgSerializePropVariant

bytes = StgSerializePropVariant\(propvar\)
Serializes a [PyPROPVARIANT](PyPROPVARIANT.md)

#### Parameters

  - propvar : [PyPROPVARIANT](PyPROPVARIANT.md)

    The value to serialize