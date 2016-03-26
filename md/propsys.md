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

    Serializes a[PyPROPVARIANT](#pypropvariant)&nbsp;

  - [StgDeserializePropVariant](propsys.md#propsysstgdeserializepropvariant)

    Creates a[PyPROPVARIANT](#pypropvariant)from a serialized buffer&nbsp;

  - [PSCreateMemoryPropertyStore](propsys.md#propsyspscreatememorypropertystore)

    Creates a temporary property store that is not connected to any backing storage&nbsp;

  - [PSCreatePropertyStoreFromPropertySetStorage](propsys.md#propsyspscreatepropertystorefrompropertysetstorage)

    Wraps a[PyIPropertySetStorage](#pyipropertysetstorage)interface in a[PyIPropertyStore](#pyipropertystore)object&nbsp;

  - [PSLookupPropertyHandlerCLSID](propsys.md#propsyspslookuppropertyhandlerclsid)

    Returns the GUID of the property handler for a file&nbsp;

  - [SHGetPropertyStoreForWindow](propsys.md#propsysshgetpropertystoreforwindow)

    Retrieves a collection of a window's properties&nbsp;

  - [PSGetPropertyFromPropertyStorage](propsys.md#propsyspsgetpropertyfrompropertystorage)

    Extracts a property from a serialized buffer by key&nbsp;

  - [PSGetNamedPropertyFromPropertyStorage](propsys.md#propsyspsgetnamedpropertyfrompropertystorage)

    Extracts a property from a serialized buffer by name&nbsp;

  - [PSCreateSimplePropertyChange](propsys.md#propsyspscreatesimplepropertychange)

    Creates a[PyIPropertyChange](#pyipropertychange)interface used to apply changes to a[PyPROPVARIANT](#pypropvariant)&nbsp;

  - [PSCreatePropertyChangeArray](propsys.md#propsyspscreatepropertychangearray)

    Creates a[PyIPropertyChangeArray](#pyipropertychangearray)interface to be used with[PyIFileOperation](#pyifileoperation)&nbsp;

  - [SHSetDefaultProperties](propsys.md#propsysshsetdefaultproperties)

    Sets the default properties for a file.&nbsp;

## [propsys](#propsys).PSCreateMemoryPropertyStore

[PyIPropertyStore](#pyipropertystore)= __PSCreateMemoryPropertyStore( *riid* __ )
Creates a temporary property store that is not connected to any backing storage

#### Parameters


  -  *riid=IID_IPropertyStore* :[PyIID](#pyiid)

    The interface to create

#### Comments
May also be used to create[PyINamedPropertyStore](#pyinamedpropertystore),[PyIPropertyStoreCache](#pyipropertystorecache),[PyIPersistStream](#pyipersiststream), or[PyIPropertyBag](#pyipropertybag)

## [propsys](#propsys).PSCreatePropertyChangeArray

[PyIPropertyChangeArray](#pyipropertychangearray)= __PSCreatePropertyChangeArray(__ )
Creates an IPropertyChangeArray interface to be used with[PyIFileOperation](#pyifileoperation)

#### Comments
Currently only creates an empty array to be filled in later

## [propsys](#propsys).PSCreatePropertyStoreFromPropertySetStorage

[PyIPropertyStore](#pyipropertystore)= __PSCreatePropertyStoreFromPropertySetStorage( *pss*  *, Mode*  *, riid* __ )
Wraps a[PyIPropertySetStorage](#pyipropertysetstorage)interface in a[PyIPropertyStore](#pyipropertystore)object

#### Parameters


  -  *pss* :[PyIPropertySetStorage](#pyipropertysetstorage)

    Property container to be adapted

  -  *Mode* : int

    Read or write mode, shellcon.STGM_*.  Must match mode used to open input interface.

  -  *riid=IID_IPropertyStore* :[PyIID](#pyiid)

    The interface to create

#### Comments
This function does not work for the NTFS property storage implementation based on 

alternate data streams.

## [propsys](#propsys).PSCreateSimplePropertyChange

[PyIPropertyChange](#pyipropertychange)= __PSCreateSimplePropertyChange( *flags*  *, key*  *, val*  *, riid* __ )
Creates an IPropertyChange interface used to apply changes to a[PyPROPVARIANT](#pypropvariant)

#### Parameters


  -  *flags* : int

    The change operation, pscon.PKA_*

  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    The property key

  -  *val* :[PyPROPVARIANT](#pypropvariant)

    The value that the change operation will apply

  -  *riid=IID_IPropertyChange* :[PyIID](#pyiid)

    The interface to return.

## [propsys](#propsys).PSGetItemPropertyHandler

[PyIPropertyStore](#pyipropertystore)= __PSGetItemPropertyHandler( *Item*  *, ReadWrite*  *, riid* __ )
Retrieves the property store for a shell item

#### Parameters


  -  *Item* :[PyIShellItem](#pyishellitem)

    A shell item

  -  *ReadWrite=False* : bool

    Pass True for a writeable property store

  -  *riid=IID_IPropertyStore* :[PyIID](#pyiid)

    Interface to return

## [propsys](#propsys).PSGetNameFromPropertyKey

string = __PSGetNameFromPropertyKey( *Key* __ )
Retrieves the canonical name of a property

#### Parameters


  -  *Key* :[PyPROPERTYKEY](#pypropertykey)

    A property key

## [propsys](#propsys).PSGetNamedPropertyFromPropertyStorage

[PyPROPVARIANT](#pypropvariant)= __PSGetNamedPropertyFromPropertyStorage( *ps*  *, name* __ )
Extracts a property value from a serialized buffer by name

#### Parameters


  -  *ps* : buffer

    Bytes or buffer (or str in python 2) containing a serialized property set (see[PyIPersistSerializedPropStorage::GetPropertyStorage](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragegetpropertystorage))

  -  *name* : str

    Property to return

## [propsys](#propsys).PSGetPropertyDescription

[PyIPropertyDescription](#pyipropertydescription)= __PSGetPropertyDescription( *Key*  *, riid* __ )
Gets a description interface for a property

#### Parameters


  -  *Key* :[PyPROPERTYKEY](#pypropertykey)

    A property key identifier

  -  *riid=IID_IPropertyDescription* :[PyIID](#pyiid)

    The interface to return

#### Comments
Possible interfaces include IPropertyDescription, IPropertyDescriptionAliasInfo, and IPropertyDescriptionSearchInfo

## [propsys](#propsys).PSGetPropertyFromPropertyStorage

[PyPROPVARIANT](#pypropvariant)= __PSGetPropertyFromPropertyStorage( *ps*  *, key* __ )
Extracts a property value from a serialized buffer by key

#### Parameters


  -  *ps* : buffer

    Bytes or buffer (or str in python 2) containing a serialized property set (see[PyIPersistSerializedPropStorage::GetPropertyStorage](PyIPersistSerializedPropStorage.md#pyipersistserializedpropstoragegetpropertystorage))

  -  *key* :[PyPROPERTYKEY](#pypropertykey)

    Property to return

## [propsys](#propsys).PSGetPropertyKeyFromName

[PyPROPERTYKEY](#pypropertykey)= __PSGetPropertyKeyFromName( *Name* __ )
Retrieves the property key by canonical name

#### Parameters


  -  *Name* : str

    The canonical name of a property (eg System.Author)

## [propsys](#propsys).PSGetPropertySystem

[PyIPropertySystem](#pyipropertysystem)= __PSGetPropertySystem( *riid* __ )
Creates an IPropertySystem interface

#### Parameters


  -  *riid=IID_IPropertySystem* :[PyIID](#pyiid)

    The interface to return

## [propsys](#propsys).PSLookupPropertyHandlerCLSID

[PyIID](#pyiid)= __PSLookupPropertyHandlerCLSID( *FilePath* __ )
Returns the GUID of the property handler for a file

#### Parameters


  -  *FilePath* : str

    Name of file

#### Comments
If no handler is found, the returned error code can be deceptive as it seems to indicate 

that the file itself was not found

## [propsys](#propsys).PSRegisterPropertySchema

 __PSRegisterPropertySchema( *filename* __ )
Registers a group of properties described in a schema file

#### Parameters


  -  *filename* : unicode

    An XML file that defines a property schema (*.propdesc)

## [propsys](#propsys).PSUnregisterPropertySchema

 __PSUnregisterPropertySchema( *filename* __ )
Removes a property schema definition

#### Parameters


  -  *filename* : unicode

    A previously registered schema definition file

## [propsys](#propsys).SHGetPropertyStoreForWindow

[PyIPropertyStore](#pyipropertystore)= __SHGetPropertyStoreForWindow( *hwnd*  *, riid* __ )
Retrieves a collection of a window's properties

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *riid=IID_IPropertyStore* :[PyIID](#pyiid)

    The interface to create

#### Comments
Requires Windows 7 or later.

#### Return Value
The returned store can be used to set the System.AppUserModel.ID property that determines how windows 

are grouped on the taskbar

## [propsys](#propsys).SHGetPropertyStoreFromParsingName

[PyIPropertyStore](#pyipropertystore)= __SHGetPropertyStoreFromParsingName( *Path*  *, BindCtx*  *, Flags*  *, riid* __ )
Retrieves the property store for an item by path

#### Parameters


  -  *Path* : string

    Path to file

  -  *BindCtx=None* :[PyIBindCtx](#pyibindctx)

    Bind context, or None

  -  *Flags=GPS_DEFAULT* : int

    Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)

  -  *riid=IID_IPropertyStore* :[PyIID](#pyiid)

    The interface to return

#### Comments
This function does not exist on XP, even with Desktop Search installed

## [propsys](#propsys).SHSetDefaultProperties

 __SHSetDefaultProperties( *hwnd*  *, Item*  *, FileOpFlags*  *, Sink* __ )
Sets the default properties for a file.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Parent window for any notifications, can be None

  -  *Item* :[PyIShellItem](#pyishellitem)

    Shell item whose defaults are to be set

  -  *FileOpFlags=0* : int

    File operation flags, as used with[PyIFileOperation::SetOperationFlags](PyIFileOperation.md#pyifileoperationsetoperationflags)

  -  *Sink=None* :[PyGFileOperationProgressSink](#pygfileoperationprogresssink)

    Event sink to receive notifications

#### Comments
Default properties are registered by filetype under SetDefaultsFor value.

## [propsys](#propsys).StgDeserializePropVariant

[PyPROPVARIANT](#pypropvariant)= __StgDeserializePropVariant( *prop* __ )
Creates a[PyPROPVARIANT](#pypropvariant)from a serialized buffer

#### Parameters


  -  *prop* : bytes

    Buffer or bytes object (or str in Python 2) containing a serialized value

## [propsys](#propsys).StgSerializePropVariant

bytes = __StgSerializePropVariant( *propvar* __ )
Serializes a[PyPROPVARIANT](#pypropvariant)

#### Parameters


  -  *propvar* :[PyPROPVARIANT](#pypropvariant)

    The value to serialize