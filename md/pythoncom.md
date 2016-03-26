# pythoncom

## Module pythoncom

A module, encapsulating the OLE automation API

#### Methods


  - [_GetInterfaceCount](pythoncom.md#pythoncom_getinterfacecount)

    Retrieves the number of interface objects currently in existance&nbsp;

  - [_GetInterfaceCount](pythoncom.md#pythoncom_getinterfacecount)

    Retrieves the number of gateway objects currently in existance&nbsp;

  - [CoCreateFreeThreadedMarshaler](pythoncom.md#pythoncomcocreatefreethreadedmarshaler)

    Creates an aggregatable object capable of context-dependent marshaling.&nbsp;

  - [CoCreateInstanceEx](pythoncom.md#pythoncomcocreateinstanceex)

    Create a new instance of an OLE automation server possibly on a remote machine. 

MS_WINCE&nbsp;

  - [CoCreateInstance](pythoncom.md#pythoncomcocreateinstance)

    Create a new instance of an OLE automation server.&nbsp;

  - [CoFreeUnusedLibraries](pythoncom.md#pythoncomcofreeunusedlibraries)

    Unloads any DLLs that are no longer in use and that, when loaded, were specified to be freed automatically.&nbsp;

  - [CoInitialize](pythoncom.md#pythoncomcoinitialize)

    Initialize the COM libraries for the calling thread.&nbsp;

  - [CoInitializeEx](pythoncom.md#pythoncomcoinitializeex)

    Initialize the COM libraries for the calling thread.&nbsp;

  - [CoInitializeSecurity](pythoncom.md#pythoncomcoinitializesecurity)

    Registers security and sets the default security values.&nbsp;

  - [CoGetInterfaceAndReleaseStream](pythoncom.md#pythoncomcogetinterfaceandreleasestream)

    Unmarshals a buffer containing an interface pointer and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.&nbsp;

  - [CoMarshalInterThreadInterfaceInStream](pythoncom.md#pythoncomcomarshalinterthreadinterfaceinstream)

    Marshals an interface pointer from one thread to another thread in the same process.&nbsp;

  - [CoMarshalInterface](pythoncom.md#pythoncomcomarshalinterface)

    Marshals an interface into a stream&nbsp;

  - [CoUnmarshalInterface](pythoncom.md#pythoncomcounmarshalinterface)

    Unmarshals an interface&nbsp;

  - [CoReleaseMarshalData](pythoncom.md#pythoncomcoreleasemarshaldata)

    Frees resources used by a marshalled interface 

MS_WINCE&nbsp;

  - [CoGetObject](pythoncom.md#pythoncomcogetobject)

    Converts a display name into a moniker that identifies the object named, and then binds to the object identified by the moniker.&nbsp;

  - [CoUninitialize](pythoncom.md#pythoncomcouninitialize)

    Uninitialize the COM libraries.&nbsp;

  - [CoRegisterClassObject](pythoncom.md#pythoncomcoregisterclassobject)

    Registers an EXE class object with OLE so other applications can connect to it.&nbsp;

  - [CoResumeClassObjects](pythoncom.md#pythoncomcoresumeclassobjects)

    Called by a server that can register multiple class objects to inform the OLE SCM about all registered classes, and permits activation requests for those class objects.&nbsp;

  - [CoRevokeClassObject](pythoncom.md#pythoncomcorevokeclassobject)

    Informs OLE that a class object, previously registered with the[pythoncom::CoRegisterClassObject](pythoncom.md#pythoncomcoregisterclassobject)method, is no longer available for use.&nbsp;

  - [CoTreatAsClass](pythoncom.md#pythoncomcotreatasclass)

    Establishes or removes an emulation, in which objects of one class are treated as objects of a different class.&nbsp;

  - [CoWaitForMultipleHandles](pythoncom.md#pythoncomcowaitformultiplehandles)

    Waits for specified handles to be signaled or for a specified timeout period to elapse.&nbsp;

  - [Connect](pythoncom.md#pythoncomconnect)

    Connects to a running instance of an OLE automation server.&nbsp;

  - [CreateGuid](pythoncom.md#pythoncomcreateguid)

    Creates a new, unique GUIID.&nbsp;

  - [CreateBindCtx](pythoncom.md#pythoncomcreatebindctx)

    Obtains a[PyIBindCtx](#pyibindctx)object.&nbsp;

  - [CreateFileMoniker](pythoncom.md#pythoncomcreatefilemoniker)

    Creates a file moniker given a file name.&nbsp;

  - [CreateItemMoniker](pythoncom.md#pythoncomcreateitemmoniker)

    Creates an item moniker that identifies an object within a containing object (typically a compound document).&nbsp;

  - [CreatePointerMoniker](pythoncom.md#pythoncomcreatepointermoniker)

    Creates a pointer moniker based on a pointer to an object.&nbsp;

  - [CreateURLMoniker](pythoncom.md#pythoncomcreateurlmoniker)

    Create a URL moniker from a full url or partial url and base moniker&nbsp;

  - [CreateTypeLib](pythoncom.md#pythoncomcreatetypelib)

    Provides access to a new object instance that supports the ICreateTypeLib interface.&nbsp;

  - [CreateTypeLib2](pythoncom.md#pythoncomcreatetypelib2)

    Provides access to a new object instance that supports the ICreateTypeLib2 interface. 

MS_WINCE&nbsp;

  - [CreateStreamOnHGlobal](pythoncom.md#pythoncomcreatestreamonhglobal)

    Creates an in-memory stream storage object&nbsp;

  - [CreateILockBytesOnHGlobal](pythoncom.md#pythoncomcreateilockbytesonhglobal)

    Creates an ILockBytes interface based on global memory&nbsp;

  - [EnableQuitMessage](pythoncom.md#pythoncomenablequitmessage)

    Indicates the thread PythonCOM should post a WM_QUIT message to.&nbsp;

  - [FUNCDESC](pythoncom.md#pythoncomfuncdesc)

    Returns a new[FUNCDESC](#funcdesc)object.&nbsp;

  - [GetActiveObject](pythoncom.md#pythoncomgetactiveobject)

    Retrieves an object representing a running object registered with OLE&nbsp;

  - [GetClassFile](pythoncom.md#pythoncomgetclassfile)

    Supplies the CLSID associated with the given filename. 

MS_WINCE&nbsp;

  - [GetFacilityString](pythoncom.md#pythoncomgetfacilitystring)

    Returns the facility string, given an OLE scode.&nbsp;

  - [GetRecordFromGuids](pythoncom.md#pythoncomgetrecordfromguids)

    Creates a new record object from the given GUIDs&nbsp;

  - [GetRecordFromTypeInfo](pythoncom.md#pythoncomgetrecordfromtypeinfo)

    Creates a __PyRecord__ object from a[PyITypeInfo](#pyitypeinfo)interface&nbsp;

  - [GetRunningObjectTable](pythoncom.md#pythoncomgetrunningobjecttable)

    Obtains a[PyIRunningObjectTable](#pyirunningobjecttable)object. 

MS_WINCE&nbsp;

  - [GetScodeString](pythoncom.md#pythoncomgetscodestring)

    Returns the string for an OLE scode.&nbsp;

  - [GetScodeRangeString](pythoncom.md#pythoncomgetscoderangestring)

    Returns the scode range string, given an OLE scode.&nbsp;

  - [GetSeverityString](pythoncom.md#pythoncomgetseveritystring)

    Returns the severity string, given an OLE scode.&nbsp;

  - [IsGatewayRegistered](pythoncom.md#pythoncomisgatewayregistered)

    Returns 1 if the given IID has a registered gateway object.&nbsp;

  - [LoadRegTypeLib](pythoncom.md#pythoncomloadregtypelib)

    Loads a registered type library by CLSID&nbsp;

  - [LoadTypeLib](pythoncom.md#pythoncomloadtypelib)

    Loads a type library by name&nbsp;

  - [MakePyFactory](pythoncom.md#pythoncommakepyfactory)

    Creates a new[PyIClassFactory](#pyiclassfactory)object wrapping a PythonCOM Class Factory object.&nbsp;

  - [MkParseDisplayName](pythoncom.md#pythoncommkparsedisplayname)

    Parses a moniker display name into a moniker object. The inverse of IMoniker::GetDisplayName. 

MS_WINCE&nbsp;

  - [New](pythoncom.md#pythoncomnew)

    Create a new instance of an OLE automation server.&nbsp;

  - [ObjectFromAddress](pythoncom.md#pythoncomobjectfromaddress)

    Returns a COM object given its address in memory.&nbsp;

  - [ObjectFromLresult](pythoncom.md#pythoncomobjectfromlresult)

    Retrieves a requested interface pointer for an object based on a previously generated object reference.&nbsp;

  - [OleInitialize](pythoncom.md#pythoncomoleinitialize)

    &nbsp;

  - [OleGetClipboard](pythoncom.md#pythoncomolegetclipboard)

    Retrieves a data object that you can use to access the contents of the clipboard.&nbsp;

  - [OleFlushClipboard](pythoncom.md#pythoncomoleflushclipboard)

    Carries out the clipboard shutdown sequence. It also releases the IDataObject pointer that was placed on the clipboard by the[pythoncom::OleSetClipboard](pythoncom.md#pythoncomolesetclipboard)function.&nbsp;

  - [OleIsCurrentClipboard](pythoncom.md#pythoncomoleiscurrentclipboard)

    Determines whether the data object pointer previously placed on the clipboard by the OleSetClipboard function is still on the clipboard.&nbsp;

  - [OleSetClipboard](pythoncom.md#pythoncomolesetclipboard)

    Places a pointer to a specific data object onto the clipboard. This makes the data object accessible to the OleGetClipboard function.&nbsp;

  - [OleLoadFromStream](pythoncom.md#pythoncomoleloadfromstream)

    Load an object from an IStream.&nbsp;

  - [OleSaveToStream](pythoncom.md#pythoncomolesavetostream)

    Save an object to an IStream.&nbsp;

  - [OleLoad](pythoncom.md#pythoncomoleload)

    Loads into memory an object nested within a specified storage object.&nbsp;

  - [ProgIDFromCLSID](pythoncom.md#pythoncomprogidfromclsid)

    Converts a CLSID string to a progID. 

MS_WINCE&nbsp;

  - [PumpWaitingMessages](pythoncom.md#pythoncompumpwaitingmessages)

    Pumps all waiting messages for the current thread.&nbsp;

  - [PumpMessages](pythoncom.md#pythoncompumpmessages)

    Pumps all messages for the current thread until a WM_QUIT message.&nbsp;

  - [QueryPathOfRegTypeLib](pythoncom.md#pythoncomquerypathofregtypelib)

    Retrieves the path of a registered type library 

MS_WINCE&nbsp;

  - [ReadClassStg](pythoncom.md#pythoncomreadclassstg)

    Reads a CLSID from a storage object&nbsp;

  - [ReadClassStm](pythoncom.md#pythoncomreadclassstm)

    Reads a CLSID from a[PyIStream](#pyistream)object&nbsp;

  - [RegisterTypeLib](pythoncom.md#pythoncomregistertypelib)

    Adds information about a type library to the system registry.&nbsp;

  - [UnRegisterTypeLib](pythoncom.md#pythoncomunregistertypelib)

    Removes a type library from the system registry.&nbsp;

  - [RegisterActiveObject](pythoncom.md#pythoncomregisteractiveobject)

    Register an object as the active object for its class&nbsp;

  - [RevokeActiveObject](pythoncom.md#pythoncomrevokeactiveobject)

    Ends an object&#146s status as active.&nbsp;

  - [RegisterDragDrop](pythoncom.md#pythoncomregisterdragdrop)

    Registers the specified window as one that can be the target of an OLE drag-and-drop operation.&nbsp;

  - [RevokeDragDrop](pythoncom.md#pythoncomrevokedragdrop)

    Revokes the specified window as the target of an OLE drag-and-drop operation.&nbsp;

  - [DoDragDrop](pythoncom.md#pythoncomdodragdrop)

    Carries out an OLE drag and drop operation. 

MS_WINCE&nbsp;

  - [StgCreateDocfile](pythoncom.md#pythoncomstgcreatedocfile)

    Creates a new compound file storage object using the OLE-provided compound file implementation for the[PyIStorage](#pyistorage)interface.&nbsp;

  - [StgCreateDocfileOnILockBytes](pythoncom.md#pythoncomstgcreatedocfileonilockbytes)

    Creates a new compound file storage object using the OLE-provided compound file implementation for the[PyIStorage](#pyistorage)interface.&nbsp;

  - [StgIsStorageFile](pythoncom.md#pythoncomstgisstoragefile)

    Indicates whether a particular disk file contains a storage object. 

MS_WINCE&nbsp;

  - [STGMEDIUM](pythoncom.md#pythoncomstgmedium)

    Creates a new[PySTGMEDIUM](#pystgmedium)object suitable for the[PyIDataObject](#pyidataobject)interface.&nbsp;

  - [StgOpenStorage](pythoncom.md#pythoncomstgopenstorage)

    Opens an existing root storage object in the file system.&nbsp;

  - [StgOpenStorageEx](pythoncom.md#pythoncomstgopenstorageex)

    Access IStorage and IPropertySetStorage interfaces for normal files&nbsp;

  - [StgCreateStorageEx](pythoncom.md#pythoncomstgcreatestorageex)

    Creates a new structured storage file or property set&nbsp;

  - [TYPEATTR](pythoncom.md#pythoncomtypeattr)

    Returns a new[TYPEATTR](#typeattr)object.&nbsp;

  - [VARDESC](pythoncom.md#pythoncomvardesc)

    Returns a new[VARDESC](#vardesc)object.&nbsp;

  - [WrapObject](pythoncom.md#pythoncomwrapobject)

    Wraps an object in a gateway.&nbsp;

  - [WriteClassStg](pythoncom.md#pythoncomwriteclassstg)

    Stores a CLSID from a storage object&nbsp;

  - [WriteClassStm](pythoncom.md#pythoncomwriteclassstm)

    Sets the CLSID of a stream&nbsp;

  - [UnwrapObject](pythoncom.md#pythoncomunwrapobject)

    Unwraps a Python instance in a gateway object.&nbsp;

  - [FmtIdToPropStgName](pythoncom.md#pythoncomfmtidtopropstgname)

    Convert a FMTID to its stream name&nbsp;

  - [PropStgNameToFmtId](pythoncom.md#pythoncompropstgnametofmtid)

    Convert property set name to FMTID&nbsp;

  - [CoGetCallContext](pythoncom.md#pythoncomcogetcallcontext)

    Creates interfaces used to access client security settings and perform impersonation&nbsp;

  - [CoGetObjectContext](pythoncom.md#pythoncomcogetobjectcontext)

    Creates an interface to interact with the context of the current object&nbsp;

  - [CoGetCancelObject](pythoncom.md#pythoncomcogetcancelobject)

    Retrieves an interface used to cancel a pending call&nbsp;

  - [CoSetCancelObject](pythoncom.md#pythoncomcosetcancelobject)

    Sets or removes a[PyICancelMethodCalls](#pyicancelmethodcalls)interface to be used on the current thread&nbsp;

  - [CoEnableCallCancellation](pythoncom.md#pythoncomcoenablecallcancellation)

    Enables call cancellation for synchronous calls on the current thread&nbsp;

  - [CoDisableCallCancellation](pythoncom.md#pythoncomcodisablecallcancellation)

    Disables call cancellation for synchronous calls on the current thread&nbsp;

#### Properties

  -  __int frozen__ 
    1 if the host is a frozen program, else 0

  -  __int dcom__ 
    1 if the system is DCOM aware, else 0.  Only Win95 without DCOM extensions should return 0

## [pythoncom](#pythoncom).CoCreateFreeThreadedMarshaler

[PyIUnknown](#pyiunknown)= __CoCreateFreeThreadedMarshaler( *unk* __ )
Creates an aggregatable object capable of context-dependent marshaling.

#### Parameters


  -  *unk* :[PyIUnknown](#pyiunknown)

    The unknown object to marshal.

## [pythoncom](#pythoncom).CoCreateInstance

[PyIUnknown](#pyiunknown)= __CoCreateInstance( *clsid*  *, unkOuter*  *, context*  *, iid* __ )
Create a new instance of an OLE automation server.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    Class identifier (CLSID) of the object

  -  *unkOuter* :[PyIUnknown](#pyiunknown)

    The outer unknown, or None

  -  *context* : int

    The create context for the object, combination of pythoncom.CLSCTX_* flags

  -  *iid* :[PyIID](#pyiid)

    The IID required from the object

## [pythoncom](#pythoncom).CoCreateInstanceEx

[PyIUnknown](#pyiunknown)= __CoCreateInstanceEx( *clsid*  *, unkOuter*  *, context*  *, serverInfo*  *, iids* __ )
Create a new instance of an OLE automation server possibly on a remote machine.

#### Parameters


  -  *clsid* :[PyIID](#pyiid)

    Class identifier (CLSID) of the object

  -  *unkOuter* :[PyIUnknown](#pyiunknown)

    The outer unknown, or None

  -  *context* : int

    The create context for the object, combination of pythoncom.CLSCTX_* flags

  -  *serverInfo* : (server, authino=None, reserved1=0,reserved2=0)

    May be None, or describes the remote server to execute on.

  -  *iids* : [[PyIID](#pyiid), ...]

    A list of IIDs required from the object

## [pythoncom](#pythoncom).CoDisableCallCancellation

 __CoDisableCallCancellation(__ )
Disables call cancellation for synchronous calls on the current thread

## [pythoncom](#pythoncom).CoEnableCallCancellation

 __CoEnableCallCancellation(__ )
Enables call cancellation for synchronous calls on the current thread

## [pythoncom](#pythoncom).CoFreeUnusedLibraries

 __CoFreeUnusedLibraries(__ )
Unloads any DLLs that are no longer in use and that, when loaded, were specified to be freed automatically.

## [pythoncom](#pythoncom).CoGetCallContext

[PyIServerSecurity](#pyiserversecurity)= __CoGetCallContext( *riid* __ )
Creates interfaces used to access client security requirements and perform impersonation

#### Parameters


  -  *riid=IID_IServerSecurity* :[PyIID](#pyiid)

    The interface to create, 

IID_IServerSecurity or IID_ISecurityCallContext

#### Comments
ISecurityCallContext will only be available for a server that uses role-based security

## [pythoncom](#pythoncom).CoGetCancelObject

[PyICancelMethodCalls](#pyicancelmethodcalls)= __CoGetCancelObject( *ThreadID*  *, riid* __ )
Retrieves an interface used to cancel a pending call

#### Parameters


  -  *ThreadID=0* : int

    Id of thread with pending call, or 0 for current thread

  -  *riid=IID_ICancelMethodCalls* :[PyIID](#pyiid)

    The interface to return

#### Comments
Requires Win2k or later

## [pythoncom](#pythoncom).CoGetInterfaceAndReleaseStream

[PyIUnknown](#pyiunknown)= __CoGetInterfaceAndReleaseStream( *stream*  *, iid* __ )
Unmarshals a buffer containing an interface pointer and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    The stream to unmarshal the object from.

  -  *iid* :[PyIID](#pyiid)

    The IID if the interface to unmarshal.

## [pythoncom](#pythoncom).CoGetObject

[PyIUnknown](#pyiunknown)= __CoGetObject( *name*  *, bindOpts*  *, iid* __ )
Converts a display name into a moniker that identifies the object named, and then binds to the object identified by the moniker.

#### Parameters


  -  *name* : string

    

  -  *bindOpts=None* : None

    Must be None

  -  *iid=IID_IUnknown* :[PyIID](#pyiid)

    The IID of the interface to return.

## [pythoncom](#pythoncom).CoGetObjectContext

[PyIContext](#pyicontext)= __CoGetObjectContext( *riid* __ )
Creates an interface to interact with the context of the current object

#### Parameters


  -  *riid=IID_IContext* :[PyIID](#pyiid)

    The interface to return

#### Comments
Requires Win2k or later
COM applications can use this function to create IComThreadingInfo, IContext, or IContextCallback 

COM+ applications may also create IObjectContext, IObjectContextInfo, IObjectContextActivity, or IContextState

## [pythoncom](#pythoncom).CoInitialize

 __CoInitialize(__ )
Initialize the COM libraries for the calling thread.

#### Comments
Apart from the error handling semantics, this is equivalent 

to[pythoncom::CoInitializeEx](pythoncom.md#pythoncomcoinitializeex)(pythoncom.COINIT_APARTMENTTHREADED). 

See[pythoncom::CoInitializeEx](pythoncom.md#pythoncomcoinitializeex)for a description.

#### Return Value
This function will ignore the RPC_E_CHANGED_MODE error, as 

that error indicates someone else beat you to the initialization, and 

did so with a different threading model.  This error is ignored as it 

still means COM is ready for use on this thread, and as this function 

does not explicitly specify a threading model the caller probably 

doesn't care what model it is.
All other COM errors will raise pythoncom.error as usual.  Use[pythoncom::CoInitializeEx](pythoncom.md#pythoncomcoinitializeex)if you also want to handle the RPC_E_CHANGED_MODE 

error.

## [pythoncom](#pythoncom).CoInitializeEx

 __CoInitializeEx( *flags* __ )
Initialize the COM libraries for the calling thread.

#### Parameters


  -  *flags* : int

    Flags for the initialization.

#### Comments
There is no need to call this for the main Python thread, as it is called 

automatically by pythoncom (using sys.coinit_flags as the param, or COINIT_APARTMENTTHREADED 

if sys.coinit_flags does not exist).
You must call this manually if you create a thread which wishes to use COM.

#### Return Value
This function will raise pythoncom.error for all error 

return values, including RPC_E_CHANGED_MODE error.  This is 

in contrast to[pythoncom::CoInitialize](pythoncom.md#pythoncomcoinitialize)which will hide that 

specific error.  If your code is happy to work in a threading model 

other than the one you specified, you must explicitly handle 

(and presumably ignore) this exception.

## [pythoncom](#pythoncom).CoInitializeSecurity

 __CoInitializeSecurity( *sd*  *, authSvc*  *, reserved1*  *, authnLevel*  *, impLevel*  *, authInfo*  *, capabilities*  *, reserved2* __ )
Registers security and sets the default security values.

#### Parameters


  -  *sd* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    Security descriptor containing access permissions for process' objects, can be None.
If Capabilities contains EOAC_APPID, sd should be an AppId (guid), or None to use server executable.
If Capabilities contains EOAC_ACCESS_CONTROL, sd parameter should be an IAccessControl interface.

  -  *authSvc* : object

    A value of None tells COM to choose which authentication services to use.  An empty list means use no services.

  -  *reserved1* : object

    Must be None

  -  *authnLevel* : int

    One of pythoncom.RPC_C_AUTHN_LEVEL_* values. The default authentication level for proxies. On the server side, COM will fail calls that arrive at a lower level. All calls to AddRef&#160and Release are made at this level.

  -  *impLevel* : int

    One of pythoncom.RPC_C_IMP_LEVEL_* values.  The default impersonation level for proxies. This value is not checked on the server side. AddRef&#160and Release&#160calls are made with this impersonation level so even security aware apps should set this carefully. Setting IUnknown&#160security only affects calls to QueryInterface, not AddRef&#160or Release.

  -  *authInfo* : object

    Must be None

  -  *capabilities* : int

    Authentication capabilities, combination of pythoncom.EOAC_* flags.

  -  *reserved2* : object

    Must be None

## [pythoncom](#pythoncom).CoMarshalInterThreadInterfaceInStream

[PyIStream](#pyistream)= __CoMarshalInterThreadInterfaceInStream( *iid*  *, unk* __ )
Marshals an interface pointer from one thread to another thread in the same process.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the interface to marshal.

  -  *unk* :[PyIUnknown](#pyiunknown)

    The interface to marshal.

## [pythoncom](#pythoncom).CoMarshalInterface

 __CoMarshalInterface( *Stm*  *, riid*  *, Unk*  *, DestContext*  *, flags* __ )
Marshals an interface into a stream

#### Parameters


  -  *Stm* :[PyIStream](#pyistream)

    An IStream interface into which marshalled interface will be written

  -  *riid* :[PyIID](#pyiid)

    IID of interface to be marshalled

  -  *Unk* :[PyIUnknown](#pyiunknown)

    Base IUnknown of the object to be marshalled

  -  *DestContext* : int

    MSHCTX_* flag indicating where object will be unmarshalled

  -  *flags=MSHLFLAGS_NORMAL* : int

    MSHLFLAGS_* flag indicating marshalling options

## [pythoncom](#pythoncom).CoRegisterClassObject

int = __CoRegisterClassObject( *iid*  *, factory*  *, context*  *, flags* __ )
Registers an EXE class object with OLE so other applications can connect to it.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the object to register

  -  *factory* :[PyIUnknown](#pyiunknown)

    The class factory object.  It is the Python programmers responsibility to ensure this object remains alive until the class is unregistered.

  -  *context* : int

    The create context for the server.  Must be a combination of the CLSCTX_* flags.

  -  *flags* : int

    Create flags.

#### Comments
The class factory object should be[PyIClassFactory](#pyiclassfactory)object, but as per the COM documentation, only[PyIUnknown](#pyiunknown)is checked.

#### Return Value
The result is a handle which should be revoked using[pythoncom::CoRevokeClassObject](pythoncom.md#pythoncomcorevokeclassobject)

## [pythoncom](#pythoncom).CoReleaseMarshalData

 __CoReleaseMarshalData( *Stm* __ )
Frees resources used by a marshalled interface

#### Parameters


  -  *Stm* :[PyIStream](#pyistream)

    Stream containing marshalled interface

#### Comments
This is usually only needed when the interface could not be successfully unmarshalled

## [pythoncom](#pythoncom).CoResumeClassObjects

 __CoResumeClassObjects(__ )
Called by a server that can register multiple class objects to inform the OLE SCM about all registered classes, and permits activation requests for those class objects.

## [pythoncom](#pythoncom).CoRevokeClassObject

 __CoRevokeClassObject( *reg* __ )
Informs OLE that a class object, previously registered with the[pythoncom::CoRegisterClassObject](pythoncom.md#pythoncomcoregisterclassobject)method, is no longer available for use.

#### Parameters


  -  *reg* : int

    The value returned from[pythoncom::CoRegisterClassObject](pythoncom.md#pythoncomcoregisterclassobject)

## [pythoncom](#pythoncom).CoSetCancelObject

 __CoSetCancelObject( *Unk* __ )
Sets or removes a[PyICancelMethodCalls](#pyicancelmethodcalls)interface to be used on the current thread

#### Parameters


  -  *Unk* :[PyIUnknown](#pyiunknown)

    An interface that support ICancelMethodCalls, can be None to unregister current cancel object

#### Comments
Requires Win2k or later

## [pythoncom](#pythoncom).CoTreatAsClass

 __CoTreatAsClass( *clsidold*  *, clsidnew* __ )
Establishes or removes an emulation, in which objects of one class are treated as objects of a different class.

#### Parameters


  -  *clsidold* :[PyIID](#pyiid)

    CLSID of the object to be emulated.

  -  *clsidnew=CLSID_NULL* :[PyIID](#pyiid)

    CLSID of the object that should emulate the original object. This replaces any existing emulation for clsidOld. Can be ommitted or CLSID_NULL, in which case any existing emulation for clsidOld is removed.

## [pythoncom](#pythoncom).CoUninitialize

 __CoUninitialize(__ )
Uninitialize the COM libraries for the calling thread.

## [pythoncom](#pythoncom).CoUnmarshalInterface

interface = __CoUnmarshalInterface( *Stm*  *, riid* __ )
Unmarshals an interface

#### Parameters


  -  *Stm* :[PyIStream](#pyistream)

    Stream containing marshalled interface

  -  *riid* :[PyIID](#pyiid)

    IID of interface to be unmarshalled

## [pythoncom](#pythoncom).CoWaitForMultipleHandles

int = __CoWaitForMultipleHandles( *Flags*  *, Timeout*  *, Handles* __ )
Waits for specified handles to be signaled or for a specified timeout period to elapse.

#### Parameters


  -  *Flags* : int

    Combination of pythoncom.COWAIT_* values

  -  *Timeout* : int

    Timeout in milliseconds

  -  *Handles* : [[PyHANDLE](#pyhandle), ...]

    Sequence of handles

## [pythoncom](#pythoncom).Connect

[PyIDispatch](#pyidispatch)= __Connect( *cls* __ )
Connect to an already running OLE automation server.

#### Parameters


  -  *cls* : CLSID

    An identifier for the program.  Usually "program.item"

#### Comments
This function is equivalent to[pythoncom::GetActiveObject](pythoncom.md#pythoncomgetactiveobject)(clsid). __pythoncom::QueryInterace__ (pythoncom.IID_IDispatch)

## [pythoncom](#pythoncom).CreateBindCtx

[PyIBindCtx](#pyibindctx)= __CreateBindCtx(__ )
Creates a new[PyIBindCtx](#pyibindctx)object.

## [pythoncom](#pythoncom).CreateFileMoniker

[PyIMoniker](#pyimoniker)= __CreateFileMoniker( *filename* __ )
Creates a new[PyIMoniker](#pyimoniker)object.

#### Parameters


  -  *filename* : string

    The name of the file.

## [pythoncom](#pythoncom).CreateGuid

[PyIID](#pyiid)= __CreateGuid(__ )
Creates a new, unique GUIID.

#### Comments
Use the CreateGuid function when you need an absolutely unique number that you will use as a persistent identifier in a distributed environment.To a very high degree of certainty, this function returns a unique value &#150 no other invocation, on the same or any other system (networked or not), should return the same value.

## [pythoncom](#pythoncom).CreateILockBytesOnHGlobal

[PyILockBytes](#pyilockbytes)= __CreateILockBytesOnHGlobal( *hGlobal*  *, DeleteOnRelease* __ )
Creates an ILockBytes interface based on global memory

#### Parameters


  -  *hGlobal=None* :[PyHANDLE](#pyhandle)

    Global memory handle.  If None, a new global memory object is allocated.

  -  *DeleteOnRelease=True* : bool

    Indicates if global memory should be freed when interface is released.

## [pythoncom](#pythoncom).CreateItemMoniker

[PyIMoniker](#pyimoniker)= __CreateItemMoniker( *delim*  *, item* __ )
Creates an item moniker 

that identifies an object within a containing object (typically a compound document).

#### Parameters


  -  *delim* : string

    String containing the delimiter (typically "!") used to separate this item's display name from the display name of its containing object.

  -  *item* : string

    String indicating the containing object's name for the object being identified.

## [pythoncom](#pythoncom).CreatePointerMoniker

[PyIMoniker](#pyimoniker)= __CreatePointerMoniker( *IUnknown* __ )
Creates a new[PyIMoniker](#pyimoniker)object.

#### Parameters


  -  *IUnknown* :[PyIUnknown](#pyiunknown)

    The interface for the moniker.

## [pythoncom](#pythoncom).CreateStreamOnHGlobal

[PyIStream](#pyistream)= __CreateStreamOnHGlobal( *hGlobal*  *, DeleteOnRelease* __ )
Creates an in-memory stream storage object

#### Parameters


  -  *hGlobal=None* :[PyHANDLE](#pyhandle)

    Global memory handle.  If None, a new global memory object is allocated.

  -  *DeleteOnRelease=True* : bool

    Indicates if global memory should be freed when IStream object is destroyed.

## [pythoncom](#pythoncom).CreateTypeLib

 __ICreateTypeLib__ = __CreateTypeLib(__ )
Provides access to a new object instance that supports the ICreateTypeLib interface.

## [pythoncom](#pythoncom).CreateTypeLib2

 __ICreateTypeLib2__ = __CreateTypeLib2(__ )
Provides access to a new object instance that supports the ICreateTypeLib2 interface.

## [pythoncom](#pythoncom).CreateURLMonikerEx

[PyIMoniker](#pyimoniker)= __CreateURLMonikerEx( *Context*  *, URL*  *, Flags* __ )
Create a URL moniker from a full url or partial url and base moniker

#### Parameters


  -  *Context* :[PyIMoniker](#pyimoniker)

    An IMoniker interface to be used as a base with a partial URL, can be None

  -  *URL* :[PyUNICODE](#pyunicode)

    Full or partial url for which to create a moniker

  -  *Flags=URL_MK_UNIFORM* : int

    URL_MK_UNIFORM or URL_MK_LEGACY

#### Win32 API References


  - Search for *CreateURLMonikerEx* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=createurlmonikerex),[google](#http://www.google.com/search?q=createurlmonikerex)or[google groups](#http://groups.google.com/groups?q=createurlmonikerex).

## [pythoncom](#pythoncom).DoDragDrop

 __DoDragDrop(__ )
Carries out an OLE drag and drop operation.

## [pythoncom](#pythoncom).EnableQuitMessage

 __EnableQuitMessage( *threadId* __ )
Indicates the thread PythonCOM should post a WM_QUIT message to.

#### Parameters


  -  *threadId* : int

    The thread ID.

## [pythoncom](#pythoncom).FUNCDESC

[FUNCDESC](#funcdesc)= __FUNCDESC(__ )
Creates a new FUNCDESC object

## [pythoncom](#pythoncom).FmtIdToPropStgName

[PyUNICODE](#pyunicode)= __FmtIdToPropStgName( *fmtid* __ )
Converts a FMTID to its stream name

#### Parameters


  -  *fmtid* :[PyIID](#pyiid)

    Format id - a property storage GUID (FMTID_* IIDs)

## [pythoncom](#pythoncom).GetActiveObject

[PyIUnknown](#pyiunknown)= __GetActiveObject( *cls* __ )
Retrieves an object representing a running object registered with OLE

#### Parameters


  -  *cls* : CLSID

    The IID for the program.  As for all CLSID's in Python, a "program.name" or IID format string may be used, or a real[PyIID](#pyiid)object.

## [pythoncom](#pythoncom).GetClassFile

[PyIID](#pyiid)= __GetClassFile( *fileName* __ )
Supplies the CLSID associated with the given filename.

#### Parameters


  -  *fileName* : str

    The filename for which you are requesting the associated CLSID.

## [pythoncom](#pythoncom).GetFacilityString

string = __GetFacilityString( *scode* __ )
Returns the facility string, given an OLE scode.

#### Parameters


  -  *scode* : int

    The OLE error code for the facility string requested.

## [pythoncom](#pythoncom).GetRecordFromGuids

 __PyRecord__ = __GetRecordFromGuids( *iid*  *, verMajor*  *, verMinor*  *, lcid*  *, infoIID*  *, data* __ )
Creates a new record object from the given GUIDs

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The GUID of the type library

  -  *verMajor* : int

    The major version number of the type lib.

  -  *verMinor* : int

    The minor version number of the type lib.

  -  *lcid* : int

    The LCID of the type lib.

  -  *infoIID* :[PyIID](#pyiid)

    The GUID of the record info in the library

  -  *data=None* : string or buffer

    The raw data to initialize the record with.

## [pythoncom](#pythoncom).GetRecordFromTypeInfo

 __PyRecord__ = __GetRecordFromTypeInfo( *TypeInfo* __ )
Creates a new record object from a[PyITypeInfo](#pyitypeinfo)interface

#### Parameters


  -  *TypeInfo* :[PyITypeInfo](#pyitypeinfo)

    The type information to be converted into a PyRecord object

#### Comments
This function will fail if the specified type info does not have a guid defined

## [pythoncom](#pythoncom).GetRunningObjectTable

[PyIRunningObjectTable](#pyirunningobjecttable)= __GetRunningObjectTable( *reserved* __ )
Creates a new[PyIRunningObjectTable](#pyirunningobjecttable)object.

#### Parameters


  -  *reserved=0* : int

    A reserved parameter.  Should be zero unless you have inside information that I don't!

## [pythoncom](#pythoncom).GetScodeRangeString

string = __GetScodeRangeString( *scode* __ )
Returns the scode range string, given an OLE scode.

#### Parameters


  -  *scode* : int

    An OLE error code to return the scode range string for.

## [pythoncom](#pythoncom).GetScodeString

string = __GetScodeString( *scode* __ )
Returns the string for an OLE scode (HRESULT)

#### Parameters


  -  *scode* : int

    The OLE error code for the scode string requested.

#### Comments
This will obtain the COM Error message for a given HRESULT. 

Internally, PythonCOM uses this function to obtain the description 

when a[com_error](com.md#comerror)COM Exception is raised.

## [pythoncom](#pythoncom).GetSeverityString

string = __GetSeverityString( *scode* __ )
Returns the severity string, given an OLE scode.

#### Parameters


  -  *scode* : int

    The OLE error code for the severity string requested.

## [pythoncom](#pythoncom).IsGatewayRegistered

int = __IsGatewayRegistered( *iid* __ )
Returns true if a gateway has been registered for the given IID

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    IID of the interface.

## [pythoncom](#pythoncom).LoadRegTypeLib

[PyITypeLib](#pyitypelib)= __LoadRegTypeLib( *iid*  *, versionMajor*  *, versionMinor*  *, lcid* __ )
Loads a registered type library.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the type library.

  -  *versionMajor* : int

    The major version number of the library

  -  *versionMinor* : int

    The minor version number of the library

  -  *lcid=LOCALE_USER_DEFAULT* : int

    The locale ID to use.

#### Comments
LoadRegTypeLib compares the requested version numbers against those found in the system registry, and takes one of the following actions:
If one of the registered libraries exactly matches both the requested major and minor version numbers, then that type library is loaded.
If one or more registered type libraries exactly match the requested major version number, and has a greater minor version number than that requested, the one with the greatest minor version number is loaded.
If none of the registered type libraries exactly match the requested major version number (or if none of those that do exactly match the major version number also have a minor version number greater than or equal to the requested minor version number), then LoadRegTypeLib returns an error.

## [pythoncom](#pythoncom).LoadTypeLib

[PyITypeLib](#pyitypelib)= __LoadTypeLib( *libFileName* __ )
Loads a registered type library.

#### Parameters


  -  *libFileName* : string

    The path to the file containing the type information.

## [pythoncom](#pythoncom).MakePyFactory

[PyIClassFactory](#pyiclassfactory)= __MakePyFactory( *iid* __ )
Creates a new[PyIClassFactory](#pyiclassfactory)object wrapping a PythonCOM Class Factory object.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the object the class factory provides.

## [pythoncom](#pythoncom).MkParseDisplayName

[PyIMoniker](#pyimoniker),int,[PyIBindCtx](#pyibindctx)= __MkParseDisplayName( *displayName*  *, bindCtx* __ )
Parses a moniker display name into a moniker object. The inverse of[PyIMoniker::GetDisplayName](PyIMoniker.md#pyimonikergetdisplayname)

#### Parameters


  -  *displayName* : string

    The display name to parse

  -  *bindCtx=None* :[PyIBindCtx](#pyibindctx)

    The bind context object to use.

#### Comments
If a binding context is not provided, then one will be created. 

Any binding context created or passed in will be returned to the 

caller.

## [pythoncom](#pythoncom).ObjectFromAddress

[PyIUnknown](#pyiunknown)= __ObjectFromAddress( *address*  *, iid* __ )
Returns a COM object given its address in memory.

#### Parameters


  -  *address* : int

    The address which holds a COM object

  -  *iid=IUnknown* :[PyIID](#pyiid)

    The IID to query

#### Return Value
This method is useful for applications which return objects via non-standard 

mechanisms - eg, Windows Explorer allows you to send a specific message to the 

explorer window and the result will be the address of an object Explorer implements. 

This method allows you to recover the object from that address.

## [pythoncom](#pythoncom).ObjectFromLresult

[PyIUnknown](#pyiunknown)= __ObjectFromLresult( *lresult*  *, iid*  *, wparm* __ )
Retrieves a requested 

interface pointer for an object based on a previously generated object reference.

#### Parameters


  -  *lresult* : int

    

  -  *iid* :[PyIID](#pyiid)

    The IID to query

  -  *wparm* : int

    

## [pythoncom](#pythoncom).OleFlushClipboard

 __OleFlushClipboard(__ )
Carries out the clipboard shutdown sequence. It also releases the IDataObject pointer that was placed on the clipboard by the[pythoncom::OleSetClipboard](pythoncom.md#pythoncomolesetclipboard)function.

## [pythoncom](#pythoncom).OleGetClipboard

[PyIDataObject](#pyidataobject)= __OleGetClipboard(__ )
Retrieves a data object that you can use to access the contents of the clipboard.

## [pythoncom](#pythoncom).OleInitialize

 __OleInitialize(__ )
Calls OleInitialized - this should rarely 

be needed, although some clipboard operations insist this is called rather 

than[pythoncom::CoInitialize](pythoncom.md#pythoncomcoinitialize)

## [pythoncom](#pythoncom).OleIsCurrentClipboard

true/false = __OleIsCurrentClipboard( *dataObj* __ )
Determines whether the data object pointer previously placed on the clipboard by the OleSetClipboard function is still on the clipboard.

#### Parameters


  -  *dataObj* :[PyIDataObject](#pyidataobject)

    The data object to check

## [pythoncom](#pythoncom).OleLoad

 __OleLoad( *storage*  *, iid*  *, site* __ )
Loads into memory an object nested within a specified storage object.

#### Parameters


  -  *storage* :[PyIStorage](#pyistorage)

    The storage object from which to load

  -  *iid* :[PyIID](#pyiid)

    The IID if the interface to load.

  -  *site* :[PyIOleClientSite](#pyioleclientsite)

    The client site for the object.

## [pythoncom](#pythoncom).OleLoadFromStream

 __OleLoadFromStream( *stream*  *, iid* __ )
Load an object from an IStream.

#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    The stream to load the object from.

  -  *iid* :[PyIID](#pyiid)

    The IID if the interface to load.

## [pythoncom](#pythoncom).OleSaveToStream

 __OleSaveToStream( *persist*  *, stream* __ )
Save an object to an IStream.

#### Parameters


  -  *persist* :[PyIPersistStream](#pyipersiststream)

    The object to save

  -  *stream* :[PyIStream](#pyistream)

    The stream to save the object to.

## [pythoncom](#pythoncom).OleSetClipboard

 __OleSetClipboard( *dataObj* __ )
Places a pointer to a specific data object onto the clipboard. This makes the data object accessible to the OleGetClipboard function.

#### Parameters


  -  *dataObj* :[PyIDataObject](#pyidataobject)

    The data object to place on the clipboard. 

This parameter can be None in which case the clipboard is emptied.

## [pythoncom](#pythoncom).ProgIDFromCLSID

string = __ProgIDFromCLSID( *clsid* __ )
Converts a CLSID to a progID.

#### Parameters


  -  *clsid* : IID

    A CLSID (either in a string, or in an[PyIID](#pyiid)object)

## [pythoncom](#pythoncom).PropStgNameToFmtId

[PyIID](#pyiid)= __PropStgNameToFmtId( *Name* __ )
Converts a property set name to its format id (GUID)

#### Parameters


  -  *Name* : string/unicode

    Storage stream name

## [pythoncom](#pythoncom).PumpMessages

 __PumpMessages(__ )
Pumps all messages for the current thread until a WM_QUIT message.

## [pythoncom](#pythoncom).PumpWaitingMessages

int = __PumpWaitingMessages(__ )
Pumps all waiting messages for the current thread.

#### Comments
It is sometimes necessary for a COM thread to have a message loop.  This function 

can be used with[win32event::MsgWaitForMultipleObjects](win32event.md#win32eventmsgwaitformultipleobjects)to pump all messages 

when necessary.  Please see the COM documentation for more details.

#### Win32 API References


  - Search for *PeekMessage and DispatchMessage* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=peekmessage and dispatchmessage),[google](#http://www.google.com/search?q=peekmessage and dispatchmessage)or[google groups](#http://groups.google.com/groups?q=peekmessage and dispatchmessage).

#### Return Value
Returns 1 if a WM_QUIT message was received, else 0

## [pythoncom](#pythoncom).QueryPathOfRegTypeLib

[PyUnicode](#pyunicode)= __QueryPathOfRegTypeLib( *iid*  *, versionMajor*  *, versionMinor*  *, lcid* __ )
Retrieves the path of a registered type library.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the type library.

  -  *versionMajor* : int

    The major version number of the library

  -  *versionMinor* : int

    The minor version number of the library

  -  *lcid=LOCALE_USER_DEFAULT* : int

    The locale ID to use.

## [pythoncom](#pythoncom).ReadClassStg

[PyIID](#pyiid)= __ReadClassStg( *storage* __ )
Reads a CLSID from a storage object.

#### Parameters


  -  *storage* :[PyIStorage](#pyistorage)

    The storage to read the CLSID from.

## [pythoncom](#pythoncom).ReadClassStm

[PyIID](#pyiid)= __ReadClassStm( *Stm* __ )
Retrieves the CLSID from a stream

#### Parameters


  -  *Stm* :[PyIStream](#pyistream)

    An IStream interface

## [pythoncom](#pythoncom).RegisterActiveObject

int = __RegisterActiveObject( *obUnknown*  *, clsid*  *, flags* __ )
Register an object as the active object for its class

#### Parameters


  -  *obUnknown* :[PyIUnknown](#pyiunknown)

    The object to register.

  -  *clsid* :[PyIID](#pyiid)

    The CLSID for the object

  -  *flags* : int

    Flags to use.

#### Return Value
The result is a handle which should be pass to[pythoncom::RevokeActiveObject](pythoncom.md#pythoncomrevokeactiveobject)

## [pythoncom](#pythoncom).RegisterDragDrop

 __RegisterDragDrop( *hwnd*  *, dropTarget* __ )
Registers the specified window as 

one that can be the target of an OLE drag-and-drop operation and 

specifies the[PyIDropTarget](#pyidroptarget)instance to use for drop operations.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *dropTarget* :[PyIDropTarget](#pyidroptarget)

    Object that implements the IDropTarget interface

## [pythoncom](#pythoncom).RegisterTypeLib

 __RegisterTypeLib( *typelib*  *, fullPath*  *, helpDir*  *, lcid* __ )
Adds information about a type library to the system registry.

#### Parameters


  -  *typelib* :[PyITypeLib](#pyitypelib)

    The type library being registered.

  -  *fullPath* : string

    Fully qualified path specification for the type library being registered

  -  *helpDir=None* : string

    Directory in which the Help file for the library being registered can be found. Can be None.

  -  *lcid=LOCALE_USER_DEFAULT* : int

    The locale ID to use.

#### Comments
This function can be used during application initialization to register the application's type 

library correctly. When RegisterTypeLib is called to register a type library, 

both the minor and major version numbers are registered in hexadecimal.
In addition to filling in a complete registry entry under the type library key, 

RegisterTypeLib adds entries for each of the dispinterfaces and Automation-compatible 

interfaces, including dual interfaces. This information is required to create 

instances of these interfaces. Coclasses are not registered (that is, 

RegisterTypeLib does not write any values to the CLSID key of the coclass).

## [pythoncom](#pythoncom).RevokeActiveObject

 __RevokeActiveObject( *handle* __ )
Ends an object&#146s status as active.

#### Parameters


  -  *handle* : int

    A handle obtained from[pythoncom::RegisterActiveObject](pythoncom.md#pythoncomregisteractiveobject)

## [pythoncom](#pythoncom).RevokeDragDrop

 __RevokeDragDrop( *hwnd* __ )
Revokes the registration of the 

specified application window as a potential target for OLE drag-and-drop 

operations.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to a window registered as an OLE drop target.

## [pythoncom](#pythoncom).STGMEDIUM

[PySTGMEDIUM](#pystgmedium)= __STGMEDIUM(__ )
Creates a new STGMEDIUM object

## [pythoncom](#pythoncom).StgCreateDocfile

[PyIStorage](#pyistorage)= __StgCreateDocfile( *name*  *, mode*  *, reserved* __ )
Creates a new compound file storage object using the OLE-provided compound file implementation for the[PyIStorage](#pyistorage)interface.

#### Parameters


  -  *name* : string

    the path of the compound file to create. It is passed uninterpreted to the file system. This can be a relative name or None.  If None, a temporary stream is created.

  -  *mode* : int

    Specifies the access mode used to open the storage.

  -  *reserved=0* : int

    A reserved value

## [pythoncom](#pythoncom).StgCreateDocfileOnILockBytes

[PyIStorage](#pyistorage)= __StgCreateDocfileOnILockBytes( *lockBytes*  *, mode*  *, reserved* __ )
Creates a new compound file storage object using the OLE-provided compound file implementation for the[PyIStorage](#pyistorage)interface.

#### Parameters


  -  *lockBytes* :[PyILockBytes](#pyilockbytes)

    The[PyILockBytes](#pyilockbytes)interface on the underlying byte array object on which to create a compound file.

  -  *mode* : int

    Specifies the access mode used to open the storage.

  -  *reserved=0* : int

    A reserved value

## [pythoncom](#pythoncom).StgCreateStorageEx

[PyIStorage](#pyistorage)= __StgCreateStorageEx( *Name*  *, Mode*  *, stgfmt*  *, Attrs*  *, riid*  *, StgOptions*  *, SecurityDescriptor* __ )
Creates a new structured storage file or property set

#### Parameters


  -  *Name* : string

    Name of the stream or file to open

  -  *Mode* : int

    Access mode, combination of storagecon.STGM_* flags

  -  *stgfmt* : int

    Storage format, storagecon.STGFMT_*

  -  *Attrs* : int

    File flags and attributes, only used with STGFMT_DOCFILE

  -  *riid* :[PyIID](#pyiid)

    Interface id to return, IStorage or IPropertySetStorage

  -  *StgOptions=None* : dict

    Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)

  -  *SecurityDescriptor=None* :[PySECURITY_DESCRIPTOR](PySECURITY.md#pysecuritydescriptor)

    Specifies security for the new file.  Must be None on Windows XP.

#### Comments
Requires Win2k or later
Accepts keyword args

## [pythoncom](#pythoncom).StgIsStorageFile

int = __StgIsStorageFile( *name* __ )
Indicates whether a particular disk file contains a storage object.

#### Parameters


  -  *name* : string

    The path to the file to check.

#### Return Value
The return value is 1 if a storage file, else 0.  This 

method will also raise com_error if the StgIsStorageFile function 

returns a failure HRESULT.

## [pythoncom](#pythoncom).StgOpenStorage

[PyIStorage](#pyistorage)= __StgOpenStorage( *name*  *, other*  *, mode*  *, snbExclude*  *, reserved* __ )
Opens an existing root storage object in the file system.

#### Parameters


  -  *name* : string

    Name of the stream, or possibly None if storageOther is non None.

  -  *other* :[PyIStorage](#pyistorage)

    Usually None, or another parent storage.

  -  *mode* : int

    Specifies the access mode used to open the storage.  A combination of the storagecon.STGM_* constants.

  -  *snbExclude=None* : object

    Not yet supported - must be None

  -  *reserved=0* : int

    A reserved value

## [pythoncom](#pythoncom).StgOpenStorageEx

[PyIStorage](#pyistorage)= __StgOpenStorageEx( *Name*  *, Mode*  *, stgfmt*  *, Attrs*  *, riid*  *, StgOptions* __ )
Advanced version of StgOpenStorage, win2k or better

#### Parameters


  -  *Name* : string

    Name of the stream or file to open

  -  *Mode* : int

    Access mode, combination of storagecon.STGM_* flags

  -  *stgfmt* : int

    Storage format (STGFMT_STORAGE,STGFMT_FILE,STGFMT_ANY, or STGFMT_DOCFILE)

  -  *Attrs* : int

    File flags and attributes, only used with STGFMT_DOCFILE

  -  *riid* :[PyIID](#pyiid)

    Interface id to return, IStorage or IPropertySetStorage

  -  *StgOptions=None* : dict

    Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)

#### Comments
Requires Win2k or later
Accepts keyword args

## [pythoncom](#pythoncom).TYPEATTR

[TYPEATTR](#typeattr)= __TYPEATTR(__ )
Creates a new TYPEATTR object

## [pythoncom](#pythoncom).UnRegisterTypeLib

[PyUnicode](#pyunicode)= __UnRegisterTypeLib( *iid*  *, versionMajor*  *, versionMinor*  *, lcid*  *, syskind* __ )
Unregister a Type Library.

#### Parameters


  -  *iid* :[PyIID](#pyiid)

    The IID of the type library.

  -  *versionMajor* : int

    The major version number of the library

  -  *versionMinor* : int

    The minor version number of the library

  -  *lcid=LOCALE_USER_DEFAULT* : int

    The locale ID to use.

  -  *syskind=SYS_WIN32* : int

    The target operating system.

#### Comments
Removes type library information from the system registry. 

Use this API to allow applications to properly uninstall themselves. 

In-process objects typically call this API from DllUnregisterServer.

## [pythoncom](#pythoncom).UnwrapObject

[PyIDispatch](#pyidispatch)= __UnwrapObject( *ob* __ )
Unwraps a Python instance in a gateway object.

#### Parameters


  -  *ob* :[PyIUnknown](#pyiunknown)

    The object to unwrap.

#### Comments
If the object is not a PythonCOM object, then ValueError is raised.

## [pythoncom](#pythoncom).VARDESC

[VARDESC](#vardesc)= __VARDESC(__ )
Creates a new VARDESC object

## [pythoncom](#pythoncom).WrapObject

[PyIUnknown](#pyiunknown)= __WrapObject( *ob*  *, gatewayIID*  *, interfaceIID* __ )
Wraps a Python instance in a gateway object.

#### Parameters


  -  *ob* : object

    The object to wrap.

  -  *gatewayIID=IID_IDispatch* :[PyIID](#pyiid)

    The IID of the gateway object to create (ie, the interface of the server object wrapped by the return value)

  -  *interfaceIID=IID_IDispatch* :[PyIID](#pyiid)

    The IID of the interface object to create (ie, the interface of the returned object)

#### Return Value
Note that there are 2 objects created by this call - a gateway (server) object, suitable for 

use by other external COM clients/hosts, as well as the returned Python interface (client) object, which 

maps to the new gateway.
There are some unusual cases where the 2 IID parameters will not be identical. 

If you need to do this, you should know exactly what you are doing, and why!

## [pythoncom](#pythoncom).WriteClassStg

 __WriteClassStg( *storage*  *, iid* __ )
Writes a CLSID to a storage object

#### Parameters


  -  *storage* :[PyIStorage](#pyistorage)

    Storage object into which CLSID will be written.

  -  *iid* :[PyIID](#pyiid)

    The IID to write

## [pythoncom](#pythoncom).WriteClassStm

 __WriteClassStm( *Stm*  *, clsid* __ )
Writes a CLSID to a stream.

#### Parameters


  -  *Stm* :[PyIStream](#pyistream)

    An IStream interface

  -  *clsid* :[PyIID](#pyiid)

    The IID to write

## [pythoncom](#pythoncom)._GetGatewayCount

int = ___GetGatewayCount(__ )
Retrieves the number of gateway objects currently in existance

#### Comments
This is the number of Python object that implement COM servers which 

are still alive (ie, serving a client).  The only way to reduce this count 

is to have the process which uses these PythonCOM servers release its references.

## [pythoncom](#pythoncom)._GetInterfaceCount

int = ___GetInterfaceCount(__ )
Retrieves the number of interface objects currently in existance

#### Comments
If is occasionally a good idea to call this function before your Python program 

terminates.  If this function returns non-zero, then you still have PythonCOM objects 

alive in your program (possibly in global variables).

## pythoncom.dcom property

#### Data Type
 __int__ 

#### Description
1 if the system is DCOM aware, else 0.  Only Win95 without DCOM extensions should return 0
Defined in: O:/SRC/PYWIN32/COM/WIN32COM/SRC/PYTHONCOM.CPP

## pythoncom.frozen property

#### Data Type
 __int__ 

#### Description
1 if the host is a frozen program, else 0
Defined in: O:/SRC/PYWIN32/COM/WIN32COM/SRC/PYTHONCOM.CPP

## [pythoncom](#pythoncom).new

[PyIDispatch](#pyidispatch)= __new( *cls* __ )
Create a new instance of an OLE automation server.

#### Parameters


  -  *cls* : CLSID

    An identifier for the program.  Usually "program.item"

#### Comments
This is just a wrapper for the CoCreateInstance method. 

Specifically, this call is identical to:
pythoncom.CoCreateInstance(cls, None, pythoncom.CLSCTX_SERVER, pythoncom.IID_IDispatch)