
## [win32evtlog](#README.md#win32evtlog).BackupEventLog

 **BackupEventLog( *handle*  *, eventLogName* ** )
Backs up the event log

#### Parameters


     *handle* : int

    Handle to the event log to backup.

     *eventLogName* :[PyUnicode](#README.md#PyUnicode)

    The name of the event log to save to

## [win32evtlog](#README.md#win32evtlog).ClearEventLog

 **ClearEventLog( *handle*  *, eventLogName* ** )
Clears the event log

#### Parameters


     *handle* : int

    Handle to the event log to clear.

     *eventLogName* :[PyUnicode](#README.md#PyUnicode)

    The name of the event log to save to, or None

## [win32evtlog](#README.md#win32evtlog).CloseEventLog

 **CloseEventLog( *handle* ** )
Closes the eventlog

#### Parameters


     *handle* : int

    Handle to the event log to close

## [win32evtlog](#README.md#win32evtlog).DeregisterEventSource

 **DeregisterEventSource( *handle* ** )
Deregisters an Event Source

#### Parameters


     *handle* : int

    Identifies the event log whose handle was returned by[win32evtlog::RegisterEventSource](#win32evtlog.md#win32evtlogRegisterEventSource)

## EVENTLOG_AUDIT_FAILURE
 **const win32evtlog.EVENTLOG_AUDIT_FAILURE;** 


## EVENTLOG_AUDIT_SUCCESS
 **const win32evtlog.EVENTLOG_AUDIT_SUCCESS;** 


## EVENTLOG_BACKWARDS_READ
 **const win32evtlog.EVENTLOG_BACKWARDS_READ;** 


## EVENTLOG_END_ALL_PAIRED_EVENTS
 **const win32evtlog.EVENTLOG_END_ALL_PAIRED_EVENTS;** 


## EVENTLOG_END_PAIRED_EVENT
 **const win32evtlog.EVENTLOG_END_PAIRED_EVENT;** 


## EVENTLOG_ERROR_TYPE
 **const win32evtlog.EVENTLOG_ERROR_TYPE;** 


## EVENTLOG_FORWARDS_READ
 **const win32evtlog.EVENTLOG_FORWARDS_READ;** 


## EVENTLOG_INFORMATION_TYPE
 **const win32evtlog.EVENTLOG_INFORMATION_TYPE;** 


## EVENTLOG_PAIRED_EVENT_ACTIVE
 **const win32evtlog.EVENTLOG_PAIRED_EVENT_ACTIVE;** 


## EVENTLOG_PAIRED_EVENT_INACTIVE
 **const win32evtlog.EVENTLOG_PAIRED_EVENT_INACTIVE;** 


## EVENTLOG_SEEK_READ
 **const win32evtlog.EVENTLOG_SEEK_READ;** 


## EVENTLOG_SEQUENTIAL_READ
 **const win32evtlog.EVENTLOG_SEQUENTIAL_READ;** 


## EVENTLOG_START_PAIRED_EVENT
 **const win32evtlog.EVENTLOG_START_PAIRED_EVENT;** 


## EVENTLOG_SUCCESS
 **const win32evtlog.EVENTLOG_SUCCESS;** 


## EVENTLOG_WARNING_TYPE
 **const win32evtlog.EVENTLOG_WARNING_TYPE;** 


## EventMetadataEventChannel
 **const win32evtlog.EventMetadataEventChannel;** 


## EventMetadataEventID
 **const win32evtlog.EventMetadataEventID;** 


## EventMetadataEventKeyword
 **const win32evtlog.EventMetadataEventKeyword;** 


## EventMetadataEventLevel
 **const win32evtlog.EventMetadataEventLevel;** 


## EventMetadataEventMessageID
 **const win32evtlog.EventMetadataEventMessageID;** 


## EventMetadataEventOpcode
 **const win32evtlog.EventMetadataEventOpcode;** 


## EventMetadataEventTask
 **const win32evtlog.EventMetadataEventTask;** 


## EventMetadataEventTemplate
 **const win32evtlog.EventMetadataEventTemplate;** 


## EventMetadataEventVersion
 **const win32evtlog.EventMetadataEventVersion;** 


## [win32evtlog](#README.md#win32evtlog).EvtArchiveExportedLog

 **EvtArchiveExportedLog( *LogFilePath*  *, Locale*  *, Session*  *, Flags* ** )
Localizes an exported event log file

#### Parameters


     *LogFilePath* : str

    Filename of an exported log file

     *Locale* : int

    Locale id

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

     *Flags=0* : int

    Reserved

#### Comments
Accepts keyword args

## EvtChannelConfigAccess
 **const win32evtlog.EvtChannelConfigAccess;** 


## EvtChannelConfigClassicEventlog
 **const win32evtlog.EvtChannelConfigClassicEventlog;** 


## EvtChannelConfigEnabled
 **const win32evtlog.EvtChannelConfigEnabled;** 


## EvtChannelConfigIsolation
 **const win32evtlog.EvtChannelConfigIsolation;** 


## EvtChannelConfigOwningPublisher
 **const win32evtlog.EvtChannelConfigOwningPublisher;** 


## EvtChannelConfigPropertyIdEND
 **const win32evtlog.EvtChannelConfigPropertyIdEND;** 


## EvtChannelConfigType
 **const win32evtlog.EvtChannelConfigType;** 


## EvtChannelLoggingConfigAutoBackup
 **const win32evtlog.EvtChannelLoggingConfigAutoBackup;** 


## EvtChannelLoggingConfigLogFilePath
 **const win32evtlog.EvtChannelLoggingConfigLogFilePath;** 


## EvtChannelLoggingConfigMaxSize
 **const win32evtlog.EvtChannelLoggingConfigMaxSize;** 


## EvtChannelLoggingConfigRetention
 **const win32evtlog.EvtChannelLoggingConfigRetention;** 


## EvtChannelPublisherList
 **const win32evtlog.EvtChannelPublisherList;** 


## EvtChannelPublishingConfigBufferSize
 **const win32evtlog.EvtChannelPublishingConfigBufferSize;** 


## EvtChannelPublishingConfigClockType
 **const win32evtlog.EvtChannelPublishingConfigClockType;** 


## EvtChannelPublishingConfigControlGuid
 **const win32evtlog.EvtChannelPublishingConfigControlGuid;** 


## EvtChannelPublishingConfigFileMax
 **const win32evtlog.EvtChannelPublishingConfigFileMax;** 


## EvtChannelPublishingConfigKeywords
 **const win32evtlog.EvtChannelPublishingConfigKeywords;** 


## EvtChannelPublishingConfigLatency
 **const win32evtlog.EvtChannelPublishingConfigLatency;** 


## EvtChannelPublishingConfigLevel
 **const win32evtlog.EvtChannelPublishingConfigLevel;** 


## EvtChannelPublishingConfigMaxBuffers
 **const win32evtlog.EvtChannelPublishingConfigMaxBuffers;** 


## EvtChannelPublishingConfigMinBuffers
 **const win32evtlog.EvtChannelPublishingConfigMinBuffers;** 


## EvtChannelPublishingConfigSidType
 **const win32evtlog.EvtChannelPublishingConfigSidType;** 


## [win32evtlog](#README.md#win32evtlog).EvtClearLog

 **EvtClearLog( *ChannelPath*  *, TargetFilePath*  *, Session*  *, Flags* ** )
Clears an event log and optionally exports events to an archive

#### Parameters


     *ChannelPath* : str

    Name of event log to be cleared

     *TargetFilePath=None* : str

    Name of file in which cleared events will be archived, or None

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtCreateBookmark

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtCreateBookmark( *BookmarkXML* ** )
Creates a bookmark

#### Parameters


     *BookmarkXML=None* : str

    XML representation of a bookmark as returned by[win32evtlog::EvtRender](#win32evtlog.md#win32evtlogEvtRender), or None for a new bookmark

#### Comments
Accepts keyword args

## EvtEventMetadataPropertyIdEND
 **const win32evtlog.EvtEventMetadataPropertyIdEND;** 


## EvtEventPath
 **const win32evtlog.EvtEventPath;** 


## EvtEventPropertyIdEND
 **const win32evtlog.EvtEventPropertyIdEND;** 


## EvtEventQueryIDs
 **const win32evtlog.EvtEventQueryIDs;** 


## [win32evtlog](#README.md#win32evtlog).EvtExportLog

 **EvtExportLog( *Path*  *, TargetFilePath*  *, Flags*  *, Query*  *, Session* ** )
Exports events from a channel or log file

#### Parameters


     *Path* : str

    Path of a live event log channel or exported log file

     *TargetFilePath* : str

    File to create, cannot already exist

     *Flags* : int

    Combination of EvtExportLog* flags specifying the type of path

     *Query=None* : str

    Selects specific events to export

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

#### Comments
Accepts keyword args

## EvtExportLogChannelPath
 **const win32evtlog.EvtExportLogChannelPath;** 


## EvtExportLogFilePath
 **const win32evtlog.EvtExportLogFilePath;** 


## EvtExportLogTolerateQueryErrors
 **const win32evtlog.EvtExportLogTolerateQueryErrors;** 


## [win32evtlog](#README.md#win32evtlog).EvtGetChannelConfigProperty

(object, int) = **EvtGetChannelConfigProperty( *ChannelConfig*  *, PropertyId*  *, Flags* ** )
Retreives channel configuration information

#### Parameters


     *ChannelConfig* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Config handle as returned by[win32evtlog::EvtOpenChannelConfig](#win32evtlog.md#win32evtlogEvtOpenChannelConfig)

     *PropertyId* : int

    Property to retreive, one of EvtChannel* constants

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#README.md#win32evtlog).EvtGetEventInfo

(object, int) = **EvtGetEventInfo( *Event*  *, PropertyId* ** )
Retrieves information about the source of an event

#### Parameters


     *Event* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an event

     *PropertyId* : int

    Property to retreive, EvtEvent*

#### Comments
Accepts keyword args
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#README.md#win32evtlog).EvtGetEventMetadataProperty

(object, int) = **EvtGetEventMetadataProperty( *EventMetadata*  *, PropertyId*  *, Flags* ** )
Retrieves a property from an event publisher

#### Parameters


     *EventMetadata* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Event metadata handle as returned by[win32evtlog::EvtNextEventMetadata](#win32evtlog.md#win32evtlogEvtNextEventMetadata)

     *PropertyId* : int

    Property to retreive, EventMetadata*

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value (EvtVarType*).

## [win32evtlog](#README.md#win32evtlog).EvtGetExtendedStatus

str = **EvtGetExtendedStatus(** )
Returns additional error info from last Evt* call

## [win32evtlog](#README.md#win32evtlog).EvtGetLogInfo

(object, int) = **EvtGetLogInfo( *Log*  *, PropertyId* ** )
Retrieves log file or channel information

#### Parameters


     *Log* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Event log handle as returned by[win32evtlog::EvtOpenLog](#win32evtlog.md#win32evtlogEvtOpenLog)

     *PropertyId* : int

    Property to retreive, EvtLog*

#### Comments
Accepts keyword args
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#README.md#win32evtlog).EvtGetObjectArrayProperty

(object, int) = **EvtGetObjectArrayProperty( *ObjectArray*  *, PropertyId*  *, ArrayIndex*  *, Flags* ** )
Retrieves an item from an object array

#### Parameters


     *ObjectArray* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an array of objects as returned by[win32evtlog::EvtGetPublisherMetadataProperty](#win32evtlog.md#win32evtlogEvtGetPublisherMetadataProperty)for some ProperyId's

     *PropertyId* : int

    Type of property contained in the array

     *ArrayIndex* : int

    Zero-based index of item to retrieve

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#README.md#win32evtlog).EvtGetObjectArraySize

int = **EvtGetObjectArraySize( *ObjectArray* ** )
Returns the size of an array of event objects

#### Parameters


     *ObjectArray* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an array of objects as returned by[win32evtlog::EvtGetPublisherMetadataProperty](#win32evtlog.md#win32evtlogEvtGetPublisherMetadataProperty)for some ProperyId's

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtGetPublisherMetadataProperty

(object, int) = **EvtGetPublisherMetadataProperty( *PublisherMetadata*  *, PropertyId*  *, Flags* ** )
Retrieves a property from an event publisher

#### Parameters


     *PublisherMetadata* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Publisher handle as returned by[win32evtlog::EvtOpenPublisherMetadata](#win32evtlog.md#win32evtlogEvtOpenPublisherMetadata)

     *PropertyId* : int

    Property to retreive, EvtPublisherMetadata*

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value (EvtVarType*) 

Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using[win32evtlog::EvtGetObjectArraySize](#win32evtlog.md#win32evtlogEvtGetObjectArraySize)and[win32evtlog::EvtGetObjectArrayProperty](#win32evtlog.md#win32evtlogEvtGetObjectArrayProperty).

## EvtLogAttributes
 **const win32evtlog.EvtLogAttributes;** 


## EvtLogCreationTime
 **const win32evtlog.EvtLogCreationTime;** 


## EvtLogFileSize
 **const win32evtlog.EvtLogFileSize;** 


## EvtLogFull
 **const win32evtlog.EvtLogFull;** 


## EvtLogLastAccessTime
 **const win32evtlog.EvtLogLastAccessTime;** 


## EvtLogLastWriteTime
 **const win32evtlog.EvtLogLastWriteTime;** 


## EvtLogNumberOfLogRecords
 **const win32evtlog.EvtLogNumberOfLogRecords;** 


## EvtLogOldestRecordNumber
 **const win32evtlog.EvtLogOldestRecordNumber;** 


## [win32evtlog](#README.md#win32evtlog).EvtNext

([PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE),...) = **EvtNext( *ResultSet*  *, Count*  *, Timeout*  *, Flags* ** )
Returns events from a query

#### Parameters


     *ResultSet* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to event query or subscription

     *Count* : int

    Number of events to return

     *Timeout=-1* : int

    Time to wait in milliseconds, use -1 for infinite

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns a tuple of handles to events.  If no items are available, returns 

an empty tuple instead of raising an exception.

## [win32evtlog](#README.md#win32evtlog).EvtNextChannelPath

str = **EvtNextChannelPath( *ChannelEnum* ** )
Retrieves a channel path from an enumeration

#### Parameters


     *ChannelEnum* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an enumeration as returned by[win32evtlog::EvtOpenChannelEnum](#win32evtlog.md#win32evtlogEvtOpenChannelEnum)

#### Comments
Accepts keyword args

#### Return Value
Returns None at end of enumeration

## [win32evtlog](#README.md#win32evtlog).EvtNextEventMetadata

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtNextEventMetadata( *EventMetadataEnum*  *, Flags* ** )
Retrieves the next item from an event metadata enumeration

#### Parameters


     *EventMetadataEnum* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Enumeration handle as returned by[win32evtlog::EvtOpenEventMetadataEnum](#win32evtlog.md#win32evtlogEvtOpenEventMetadataEnum)

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtNextPublisherId

str = **EvtNextPublisherId( *PublisherEnum* ** )
Returns the next publisher from an enumeration

#### Parameters


     *PublisherEnum* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an enumeration as returned by[win32evtlog::EvtOpenPublisherEnum](#win32evtlog.md#win32evtlogEvtOpenPublisherEnum)

#### Comments
Accepts keyword args

#### Return Value
Returns None at end of enumeration

## [win32evtlog](#README.md#win32evtlog).EvtOpenChannelConfig

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenChannelConfig( *ChannelPath*  *, Session*  *, Flags* ** )
Opens channel configuration

#### Parameters


     *ChannelPath* : str

    Channel to be opened

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Session handle as returned by[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession), or None for local machine

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtOpenChannelEnum

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenChannelEnum( *Session*  *, Flags* ** )
Begins an enumeration of event channels

#### Parameters


     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtOpenChannelPath
 **const win32evtlog.EvtOpenChannelPath;** 


## [win32evtlog](#README.md#win32evtlog).EvtOpenEventMetadataEnum

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenEventMetadataEnum( *PublisherMetadata*  *, Flags* ** )
Enumerates the events that a publisher provides

#### Parameters


     *PublisherMetadata* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Publisher handle as returned by[win32evtlog::EvtOpenPublisherMetadata](#win32evtlog.md#win32evtlogEvtOpenPublisherMetadata)

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtOpenFilePath
 **const win32evtlog.EvtOpenFilePath;** 


## [win32evtlog](#README.md#win32evtlog).EvtOpenLog

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenLog( *Path*  *, Flags*  *, Session* ** )
Opens an event log or exported log archive

#### Parameters


     *Path* : str

    Event log name or Path of an export file

     *Flags* : int

    EvtOpenChannelPath (1) or EvtOpenFilePath (2)

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtOpenPublisherEnum

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenPublisherEnum( *Session*  *, Flags* ** )
Begins an enumeration of event publishers

#### Parameters


     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtOpenPublisherMetadata

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenPublisherMetadata( *PublisherIdentity*  *, Session*  *, LogFilePath*  *, Locale*  *, Flags* ** )
Opens a publisher to retrieve properties using[win32evtlog::EvtGetPublisherMetadataProperty](#win32evtlog.md#win32evtlogEvtGetPublisherMetadataProperty)

#### Parameters


     *PublisherIdentity* : str

    Publisher id as returned by[win32evtlog::EvtNextPublisherId](#win32evtlog.md#win32evtlogEvtNextPublisherId)

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to remote session, or None for local machine

     *LogFilePath=None* : str

    Log file from which to retrieve publisher, or None for locally registered publisher

     *Locale=0* : int

    Locale to use for retrieved properties, use 0 for current locale

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#README.md#win32evtlog).EvtOpenSession

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtOpenSession( *Login*  *, LoginClass*  *, Timeout*  *, Flags* ** )
Creates a session used to access the Event Log on another machine

#### Parameters


     *Login* :[PyEVT_RPC_LOGIN](#PyEVT.md#PyEVTRPC_LOGIN)

    Credentials to be used to access remote machine

     *LoginClass=EvtRpcLogin* : int

    Type of login to perform, EvtRpcLogin is only defined value

     *Timeout=0* : int

    Reserved, use only 0

     *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtPublisherMetadataChannelReferenceFlags
 **const win32evtlog.EvtPublisherMetadataChannelReferenceFlags;** 


## EvtPublisherMetadataChannelReferenceID
 **const win32evtlog.EvtPublisherMetadataChannelReferenceID;** 


## EvtPublisherMetadataChannelReferenceIndex
 **const win32evtlog.EvtPublisherMetadataChannelReferenceIndex;** 


## EvtPublisherMetadataChannelReferenceMessageID
 **const win32evtlog.EvtPublisherMetadataChannelReferenceMessageID;** 


## EvtPublisherMetadataChannelReferencePath
 **const win32evtlog.EvtPublisherMetadataChannelReferencePath;** 


## EvtPublisherMetadataChannelReferences
 **const win32evtlog.EvtPublisherMetadataChannelReferences;** 


## EvtPublisherMetadataHelpLink
 **const win32evtlog.EvtPublisherMetadataHelpLink;** 


## EvtPublisherMetadataKeywordMessageID
 **const win32evtlog.EvtPublisherMetadataKeywordMessageID;** 


## EvtPublisherMetadataKeywordName
 **const win32evtlog.EvtPublisherMetadataKeywordName;** 


## EvtPublisherMetadataKeywordValue
 **const win32evtlog.EvtPublisherMetadataKeywordValue;** 


## EvtPublisherMetadataKeywords
 **const win32evtlog.EvtPublisherMetadataKeywords;** 


## EvtPublisherMetadataLevelMessageID
 **const win32evtlog.EvtPublisherMetadataLevelMessageID;** 


## EvtPublisherMetadataLevelName
 **const win32evtlog.EvtPublisherMetadataLevelName;** 


## EvtPublisherMetadataLevelValue
 **const win32evtlog.EvtPublisherMetadataLevelValue;** 


## EvtPublisherMetadataLevels
 **const win32evtlog.EvtPublisherMetadataLevels;** 


## EvtPublisherMetadataMessageFilePath
 **const win32evtlog.EvtPublisherMetadataMessageFilePath;** 


## EvtPublisherMetadataOpcodeMessageID
 **const win32evtlog.EvtPublisherMetadataOpcodeMessageID;** 


## EvtPublisherMetadataOpcodeName
 **const win32evtlog.EvtPublisherMetadataOpcodeName;** 


## EvtPublisherMetadataOpcodeValue
 **const win32evtlog.EvtPublisherMetadataOpcodeValue;** 


## EvtPublisherMetadataOpcodes
 **const win32evtlog.EvtPublisherMetadataOpcodes;** 


## EvtPublisherMetadataParameterFilePath
 **const win32evtlog.EvtPublisherMetadataParameterFilePath;** 


## EvtPublisherMetadataPropertyIdEND
 **const win32evtlog.EvtPublisherMetadataPropertyIdEND;** 


## EvtPublisherMetadataPublisherGuid
 **const win32evtlog.EvtPublisherMetadataPublisherGuid;** 


## EvtPublisherMetadataPublisherMessageID
 **const win32evtlog.EvtPublisherMetadataPublisherMessageID;** 


## EvtPublisherMetadataResourceFilePath
 **const win32evtlog.EvtPublisherMetadataResourceFilePath;** 


## EvtPublisherMetadataTaskEventGuid
 **const win32evtlog.EvtPublisherMetadataTaskEventGuid;** 


## EvtPublisherMetadataTaskMessageID
 **const win32evtlog.EvtPublisherMetadataTaskMessageID;** 


## EvtPublisherMetadataTaskName
 **const win32evtlog.EvtPublisherMetadataTaskName;** 


## EvtPublisherMetadataTaskValue
 **const win32evtlog.EvtPublisherMetadataTaskValue;** 


## EvtPublisherMetadataTasks
 **const win32evtlog.EvtPublisherMetadataTasks;** 


## [win32evtlog](#README.md#win32evtlog).EvtQuery

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtQuery( *Path*  *, Flags*  *, Query*  *, Session* ** )
Opens a query over a log channel or exported log file

#### Parameters


     *Path* : str

    Log channel or exported log file, depending on Flags

     *Flags* : int

    Combination of EVT_QUERY_FLAGS (EvtQuery*)

     *Query=None* : str

    Selects events to return, None or '*' for all events

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)), or None for local machine.

#### Comments
Accepts keyword args

## EvtQueryChannelPath
 **const win32evtlog.EvtQueryChannelPath;** 


## EvtQueryFilePath
 **const win32evtlog.EvtQueryFilePath;** 


## EvtQueryForwardDirection
 **const win32evtlog.EvtQueryForwardDirection;** 


## EvtQueryReverseDirection
 **const win32evtlog.EvtQueryReverseDirection;** 


## EvtQueryTolerateQueryErrors
 **const win32evtlog.EvtQueryTolerateQueryErrors;** 


## [win32evtlog](#README.md#win32evtlog).EvtRender

str = **EvtRender( *Event*  *, Flags* ** )
Formats an event into XML text

#### Parameters


     *Event* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an event or bookmark

     *Flags* : int

    EvtRenderEventXml or EvtRenderBookmark indicating type of handle

#### Comments
Accepts keyword args
Rendering event values (Flags=EvtRenderEventValues) is not currently supported

## EvtRenderBookmark
 **const win32evtlog.EvtRenderBookmark;** 


## EvtRenderEventValues
 **const win32evtlog.EvtRenderEventValues;** 


## EvtRenderEventXml
 **const win32evtlog.EvtRenderEventXml;** 


## EvtRpcLogin
 **const win32evtlog.EvtRpcLogin;** 


## EvtRpcLoginAuthDefault
 **const win32evtlog.EvtRpcLoginAuthDefault;** 


## EvtRpcLoginAuthKerberos
 **const win32evtlog.EvtRpcLoginAuthKerberos;** 


## EvtRpcLoginAuthNTLM
 **const win32evtlog.EvtRpcLoginAuthNTLM;** 


## EvtRpcLoginAuthNegotiate
 **const win32evtlog.EvtRpcLoginAuthNegotiate;** 


## [win32evtlog](#README.md#win32evtlog).EvtSeek

 **EvtSeek( *ResultSet*  *, Position*  *, Flags*  *, Bookmark*  *, Timeout* ** )
Changes the current position in a result set

#### Parameters


     *ResultSet* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to event query or subscription

     *Position* : int

    Offset (base from which to seek is specified by Flags)

     *Flags* : int

    EvtSeekRelative* flag indicating seek origin

     *Bookmark=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Used as seek origin only if Flags contains EvtSeekRelativeToBookmark

     *Timeout=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtSeekOriginMask
 **const win32evtlog.EvtSeekOriginMask;** 


## EvtSeekRelativeToBookmark
 **const win32evtlog.EvtSeekRelativeToBookmark;** 


## EvtSeekRelativeToCurrent
 **const win32evtlog.EvtSeekRelativeToCurrent;** 


## EvtSeekRelativeToFirst
 **const win32evtlog.EvtSeekRelativeToFirst;** 


## EvtSeekRelativeToLast
 **const win32evtlog.EvtSeekRelativeToLast;** 


## EvtSeekStrict
 **const win32evtlog.EvtSeekStrict;** 


## [win32evtlog](#README.md#win32evtlog).EvtSubscribe

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtSubscribe( *ChannelPath*  *, Flags*  *, SignalEvent*  *, Callback*  *, Context*  *, Query*  *, Session*  *, Bookmark* ** )
Requests notification for events

#### Parameters


     *ChannelPath* : str

    Name of an event log channel

     *Flags* : int

    Combination of EvtSubscribe* flags determining how subscription is initiated

     *SignalEvent=None* : **Py_HANDLE** 

    An event handle to be set when events are available (see[win32event::CreateEvent](#win32event.md#win32eventCreateEvent))

     *Callback=None* : function

    Python function to be called with each event

     *Context=None* : object

    Arbitrary object to be passed to the callback function

     *Query=None* : str

    XML query used to select specific events, use None or '*' for all events

     *Session=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a session on another machine, or None for local

     *Bookmark=None* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    If Flags contains EvtSubscribeStartAfterBookmark, used as starting point

#### Comments
Accepts keyword args
The method used to receive events is determined by the parameters passed in. 

To create a push subscription, define a callback function that will be called with each event. 

The function will receive 3 args: 

First is an integer specifying why the function was called (EvtSubscribeActionError or EvtSubscribeActionDeliver) 

Second is the context object passed to EvtSubscribe. 

Third is the handle to an event log record (if not called due to an error) 

If an event handle is passed in, a pull subscription is created.  The event handle will be 

signalled when events are available, and the subscription handle can be 

passed to[win32evtlog::EvtNext](#win32evtlog.md#win32evtlogEvtNext)to obtain the events.

## EvtSubscribeActionDeliver
 **const win32evtlog.EvtSubscribeActionDeliver;** 


## EvtSubscribeActionError
 **const win32evtlog.EvtSubscribeActionError;** 


## EvtSubscribeOriginMask
 **const win32evtlog.EvtSubscribeOriginMask;** 


## EvtSubscribeStartAfterBookmark
 **const win32evtlog.EvtSubscribeStartAfterBookmark;** 


## EvtSubscribeStartAtOldestRecord
 **const win32evtlog.EvtSubscribeStartAtOldestRecord;** 


## EvtSubscribeStrict
 **const win32evtlog.EvtSubscribeStrict;** 


## EvtSubscribeToFutureEvents
 **const win32evtlog.EvtSubscribeToFutureEvents;** 


## EvtSubscribeTolerateQueryErrors
 **const win32evtlog.EvtSubscribeTolerateQueryErrors;** 


## [win32evtlog](#README.md#win32evtlog).EvtUpdateBookmark

[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)= **EvtUpdateBookmark( *Bookmark*  *, Event* ** )
Repositions a bookmark to an event

#### Parameters


     *Bookmark* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to a bookmark

     *Event* :[PyEVT_HANDLE](#PyEVT.md#PyEVTHANDLE)

    Handle to an event

#### Comments
Accepts keyword args

## EvtVarTypeAnsiString
 **const win32evtlog.EvtVarTypeAnsiString;** 


## EvtVarTypeBinary
 **const win32evtlog.EvtVarTypeBinary;** 


## EvtVarTypeBoolean
 **const win32evtlog.EvtVarTypeBoolean;** 


## EvtVarTypeByte
 **const win32evtlog.EvtVarTypeByte;** 


## EvtVarTypeDouble
 **const win32evtlog.EvtVarTypeDouble;** 


## EvtVarTypeEvtHandle
 **const win32evtlog.EvtVarTypeEvtHandle;** 


## EvtVarTypeEvtXml
 **const win32evtlog.EvtVarTypeEvtXml;** 


## EvtVarTypeFileTime
 **const win32evtlog.EvtVarTypeFileTime;** 


## EvtVarTypeGuid
 **const win32evtlog.EvtVarTypeGuid;** 


## EvtVarTypeHexInt32
 **const win32evtlog.EvtVarTypeHexInt32;** 


## EvtVarTypeHexInt64
 **const win32evtlog.EvtVarTypeHexInt64;** 


## EvtVarTypeInt16
 **const win32evtlog.EvtVarTypeInt16;** 


## EvtVarTypeInt32
 **const win32evtlog.EvtVarTypeInt32;** 


## EvtVarTypeInt64
 **const win32evtlog.EvtVarTypeInt64;** 


## EvtVarTypeNull
 **const win32evtlog.EvtVarTypeNull;** 


## EvtVarTypeSByte
 **const win32evtlog.EvtVarTypeSByte;** 


## EvtVarTypeSid
 **const win32evtlog.EvtVarTypeSid;** 


## EvtVarTypeSingle
 **const win32evtlog.EvtVarTypeSingle;** 


## EvtVarTypeSizeT
 **const win32evtlog.EvtVarTypeSizeT;** 


## EvtVarTypeString
 **const win32evtlog.EvtVarTypeString;** 


## EvtVarTypeSysTime
 **const win32evtlog.EvtVarTypeSysTime;** 


## EvtVarTypeUInt16
 **const win32evtlog.EvtVarTypeUInt16;** 


## EvtVarTypeUInt32
 **const win32evtlog.EvtVarTypeUInt32;** 


## EvtVarTypeUInt64
 **const win32evtlog.EvtVarTypeUInt64;** 


## [win32evtlog](#README.md#win32evtlog).GetNumberOfEventLogRecords

int = **GetNumberOfEventLogRecords( *handle* ** )
Returns the number of event log records.

#### Parameters


     *handle* : int

    Handle to the event log to query.

## [win32evtlog](#README.md#win32evtlog).GetOldestEventLogRecord

int = **GetOldestEventLogRecord(** )
Returns the number of event log records.

#### Return Value
The result is the absolute record number of the oldest record in the given event log.

## [win32evtlog](#README.md#win32evtlog).NotifyChangeEventLog

 **NotifyChangeEventLog( *handle*  *, handle* ** )
Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.

#### Parameters


     *handle* : int

    Handle to an event log file, obtained by calling[win32evtlog::OpenEventLog](#win32evtlog.md#win32evtlogOpenEventLog)function. When an event is written to this log file, the event specified by hEvent becomes signaled.

     *handle* : int

    A handle to a Win32 event. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter.

## [win32evtlog](#README.md#win32evtlog).OpenBackupEventLog

[PyEVTLOG_HANDLE](#PyEVTLOG.md#PyEVTLOGHANDLE)= **OpenBackupEventLog( *serverName*  *, fileName* ** )
Opens a previously saved event log.

#### Parameters


     *serverName* :[PyUnicode](#README.md#PyUnicode)

    The server name, or None

     *fileName* :[PyUnicode](#README.md#PyUnicode)

    The filename to open

## [win32evtlog](#README.md#win32evtlog).OpenEventLog

[PyEVTLOG_HANDLE](#PyEVTLOG.md#PyEVTLOGHANDLE)= **OpenEventLog( *serverName*  *, sourceName* ** )
Opens an event log.

#### Parameters


     *serverName* :[PyUnicode](#README.md#PyUnicode)

    The server name, or None

     *sourceName* :[PyUnicode](#README.md#PyUnicode)

    specifies the name of the source that the returned handle will reference. The source name must be a subkey of a logfile entry under the EventLog key in the registry.

## [win32evtlog](#README.md#win32evtlog).ReadEventLog

[object,...] = **ReadEventLog( *Handle*  *, Flags*  *, Offset*  *, Size* ** )
Reads some event log records.

#### Parameters


     *Handle* : **Py_HANDLE** 

    Handle to a an opened event log (see[win32evtlog::OpenEventLog](#win32evtlog.md#win32evtlogOpenEventLog))

     *Flags* : int

    Reading flags

     *Offset* : int

    Record offset to read (in SEEK mode).

     *Size=4096* : int

    Output buffer size.

#### Return Value
If there are no event log records available, then an empty list is returned.

## [win32evtlog](#README.md#win32evtlog).RegisterEventSource

int = **RegisterEventSource( *serverName*  *, sourceName* ** )
Registers an Event Source

#### Parameters


     *serverName* :[PyUnicode](#README.md#PyUnicode)

    The server name, or None

     *sourceName* :[PyUnicode](#README.md#PyUnicode)

    The source name

## [win32evtlog](#README.md#win32evtlog).ReportEvent

 **ReportEvent( *EventLog*  *, Type*  *, Category*  *, EventID*  *, UserSid*  *, Strings*  *, RawData* ** )
Reports an event

#### Parameters


     *EventLog* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to an event log

     *Type* : int

    win32con.EVENTLOG_* value

     *Category* : int

    Source-specific event category

     *EventID* : int

    Source-specific event identifier

     *UserSid* :[PySID](#README.md#PySID)

    Sid of current user, can be None

     *Strings* : sequence

    Sequence of unicode strings to be inserted in message

     *RawData* : str

    Binary data for event, can be None