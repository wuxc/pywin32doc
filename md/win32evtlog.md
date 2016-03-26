# win32evtlog

## Module win32evtlog

A module, encapsulating the Windows Win32 event log API.
The Evt* functions are only available on Vista and later.  Attempting to call 

them on XP will result in the process exiting, rather than a python exception.

#### Methods


  - [ReadEventLog](win32evtlog.md#win32evtlogreadeventlog)

    Reads some event log records.&nbsp;

  - [ClearEventLog](win32evtlog.md#win32evtlogcleareventlog)

    Clears the event log&nbsp;

  - [BackupEventLog](win32evtlog.md#win32evtlogbackupeventlog)

    Backs up the event log&nbsp;

  - [CloseEventLog](win32evtlog.md#win32evtlogcloseeventlog)

    Closes the eventlog&nbsp;

  - [DeregisterEventSource](win32evtlog.md#win32evtlogderegistereventsource)

    Deregisters an Event Source&nbsp;

  - [NotifyChangeEventLog](win32evtlog.md#win32evtlognotifychangeeventlog)

    Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.&nbsp;

  - [GetNumberOfEventLogRecords](win32evtlog.md#win32evtloggetnumberofeventlogrecords)

    Returns the number of event log records.&nbsp;

  - [GetOldestEventLogRecord](win32evtlog.md#win32evtloggetoldesteventlogrecord)

    Returns the number of event log records.&nbsp;

  - [OpenEventLog](win32evtlog.md#win32evtlogopeneventlog)

    Opens an event log.&nbsp;

  - [RegisterEventSource](win32evtlog.md#win32evtlogregistereventsource)

    Registers an Event Source&nbsp;

  - [OpenBackupEventLog](win32evtlog.md#win32evtlogopenbackupeventlog)

    Opens a previously saved event log.&nbsp;

  - [ReportEvent](win32evtlog.md#win32evtlogreportevent)

    Reports an event&nbsp;

  - [EvtOpenChannelEnum](win32evtlog.md#win32evtlogevtopenchannelenum)

    Begins an enumeration of event channels&nbsp;

  - [EvtNextChannelPath](win32evtlog.md#win32evtlogevtnextchannelpath)

    Retrieves a channel path from an enumeration&nbsp;

  - [EvtOpenLog](win32evtlog.md#win32evtlogevtopenlog)

    Opens an event log or exported log archive&nbsp;

  - [EvtClearLog](win32evtlog.md#win32evtlogevtclearlog)

    Clears an event log and optionally exports events to an archive&nbsp;

  - [EvtExportLog](win32evtlog.md#win32evtlogevtexportlog)

    Exports events from a channel or log file&nbsp;

  - [EvtArchiveExportedLog](win32evtlog.md#win32evtlogevtarchiveexportedlog)

    Localizes an exported event log file&nbsp;

  - [EvtGetExtendedStatus](win32evtlog.md#win32evtlogevtgetextendedstatus)

    Returns additional error info from last Evt* call&nbsp;

  - [EvtQuery](win32evtlog.md#win32evtlogevtquery)

    Opens a query over a log channel or exported log file&nbsp;

  - [EvtNext](win32evtlog.md#win32evtlogevtnext)

    Returns events from a query&nbsp;

  - [EvtSeek](win32evtlog.md#win32evtlogevtseek)

    Changes the current position in a result set&nbsp;

  - [EvtRender](win32evtlog.md#win32evtlogevtrender)

    Formats an event into XML text&nbsp;

  - [EvtSubscribe](win32evtlog.md#win32evtlogevtsubscribe)

    Requests notification for events&nbsp;

  - [EvtCreateBookmark](win32evtlog.md#win32evtlogevtcreatebookmark)

    Creates a bookmark&nbsp;

  - [EvtUpdateBookmark](win32evtlog.md#win32evtlogevtupdatebookmark)

    Repositions a bookmark to an event&nbsp;

  - [EvtGetChannelConfigProperty](win32evtlog.md#win32evtlogevtgetchannelconfigproperty)

    Retreives channel configuration information&nbsp;

  - [EvtOpenChannelConfig](win32evtlog.md#win32evtlogevtopenchannelconfig)

    Opens channel configuration&nbsp;

  - [EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)

    Creates a session used to access the Event Log on another machine&nbsp;

  - [EvtOpenPublisherEnum](win32evtlog.md#win32evtlogevtopenpublisherenum)

    Begins an enumeration of event publishers&nbsp;

  - [EvtNextPublisherId](win32evtlog.md#win32evtlogevtnextpublisherid)

    Returns the next publisher from an enumeration&nbsp;

  - [EvtOpenPublisherMetadata](win32evtlog.md#win32evtlogevtopenpublishermetadata)

    Opens a publisher to retrieve properties using[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)&nbsp;

  - [EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)

    Retrieves a property from an event publisher&nbsp;

  - [EvtOpenEventMetadataEnum](win32evtlog.md#win32evtlogevtopeneventmetadataenum)

    Enumerates the events that a publisher provides&nbsp;

  - [EvtNextEventMetadata](win32evtlog.md#win32evtlogevtnexteventmetadata)

    Retrieves the next item from an event metadata enumeration&nbsp;

  - [EvtGetEventMetadataProperty](win32evtlog.md#win32evtlogevtgeteventmetadataproperty)

    Retrieves a property from an event publisher&nbsp;

  - [EvtGetLogInfo](win32evtlog.md#win32evtlogevtgetloginfo)

    Retrieves log file or channel information&nbsp;

  - [EvtGetEventInfo](win32evtlog.md#win32evtlogevtgeteventinfo)

    Retrieves information about the source of an event&nbsp;

  - [EvtGetObjectArraySize](win32evtlog.md#win32evtlogevtgetobjectarraysize)

    Returns the size of an array of event objects&nbsp;

  - [EvtGetObjectArrayProperty](win32evtlog.md#win32evtlogevtgetobjectarrayproperty)

    Retrieves an item from an object array&nbsp;

## [win32evtlog](#win32evtlog).BackupEventLog

 __BackupEventLog( *handle*  *, eventLogName* __ )
Backs up the event log

#### Parameters


  -  *handle* : int

    Handle to the event log to backup.

  -  *eventLogName* :[PyUnicode](#pyunicode)

    The name of the event log to save to

## [win32evtlog](#win32evtlog).ClearEventLog

 __ClearEventLog( *handle*  *, eventLogName* __ )
Clears the event log

#### Parameters


  -  *handle* : int

    Handle to the event log to clear.

  -  *eventLogName* :[PyUnicode](#pyunicode)

    The name of the event log to save to, or None

## [win32evtlog](#win32evtlog).CloseEventLog

 __CloseEventLog( *handle* __ )
Closes the eventlog

#### Parameters


  -  *handle* : int

    Handle to the event log to close

## [win32evtlog](#win32evtlog).DeregisterEventSource

 __DeregisterEventSource( *handle* __ )
Deregisters an Event Source

#### Parameters


  -  *handle* : int

    Identifies the event log whose handle was returned by[win32evtlog::RegisterEventSource](win32evtlog.md#win32evtlogregistereventsource)

## EVENTLOG_AUDIT_FAILURE
 __const win32evtlog.EVENTLOG_AUDIT_FAILURE;__ 


## EVENTLOG_AUDIT_SUCCESS
 __const win32evtlog.EVENTLOG_AUDIT_SUCCESS;__ 


## EVENTLOG_BACKWARDS_READ
 __const win32evtlog.EVENTLOG_BACKWARDS_READ;__ 


## EVENTLOG_END_ALL_PAIRED_EVENTS
 __const win32evtlog.EVENTLOG_END_ALL_PAIRED_EVENTS;__ 


## EVENTLOG_END_PAIRED_EVENT
 __const win32evtlog.EVENTLOG_END_PAIRED_EVENT;__ 


## EVENTLOG_ERROR_TYPE
 __const win32evtlog.EVENTLOG_ERROR_TYPE;__ 


## EVENTLOG_FORWARDS_READ
 __const win32evtlog.EVENTLOG_FORWARDS_READ;__ 


## EVENTLOG_INFORMATION_TYPE
 __const win32evtlog.EVENTLOG_INFORMATION_TYPE;__ 


## EVENTLOG_PAIRED_EVENT_ACTIVE
 __const win32evtlog.EVENTLOG_PAIRED_EVENT_ACTIVE;__ 


## EVENTLOG_PAIRED_EVENT_INACTIVE
 __const win32evtlog.EVENTLOG_PAIRED_EVENT_INACTIVE;__ 


## EVENTLOG_SEEK_READ
 __const win32evtlog.EVENTLOG_SEEK_READ;__ 


## EVENTLOG_SEQUENTIAL_READ
 __const win32evtlog.EVENTLOG_SEQUENTIAL_READ;__ 


## EVENTLOG_START_PAIRED_EVENT
 __const win32evtlog.EVENTLOG_START_PAIRED_EVENT;__ 


## EVENTLOG_SUCCESS
 __const win32evtlog.EVENTLOG_SUCCESS;__ 


## EVENTLOG_WARNING_TYPE
 __const win32evtlog.EVENTLOG_WARNING_TYPE;__ 


## EventMetadataEventChannel
 __const win32evtlog.EventMetadataEventChannel;__ 


## EventMetadataEventID
 __const win32evtlog.EventMetadataEventID;__ 


## EventMetadataEventKeyword
 __const win32evtlog.EventMetadataEventKeyword;__ 


## EventMetadataEventLevel
 __const win32evtlog.EventMetadataEventLevel;__ 


## EventMetadataEventMessageID
 __const win32evtlog.EventMetadataEventMessageID;__ 


## EventMetadataEventOpcode
 __const win32evtlog.EventMetadataEventOpcode;__ 


## EventMetadataEventTask
 __const win32evtlog.EventMetadataEventTask;__ 


## EventMetadataEventTemplate
 __const win32evtlog.EventMetadataEventTemplate;__ 


## EventMetadataEventVersion
 __const win32evtlog.EventMetadataEventVersion;__ 


## [win32evtlog](#win32evtlog).EvtArchiveExportedLog

 __EvtArchiveExportedLog( *LogFilePath*  *, Locale*  *, Session*  *, Flags* __ )
Localizes an exported event log file

#### Parameters


  -  *LogFilePath* : str

    Filename of an exported log file

  -  *Locale* : int

    Locale id

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

  -  *Flags=0* : int

    Reserved

#### Comments
Accepts keyword args

## EvtChannelConfigAccess
 __const win32evtlog.EvtChannelConfigAccess;__ 


## EvtChannelConfigClassicEventlog
 __const win32evtlog.EvtChannelConfigClassicEventlog;__ 


## EvtChannelConfigEnabled
 __const win32evtlog.EvtChannelConfigEnabled;__ 


## EvtChannelConfigIsolation
 __const win32evtlog.EvtChannelConfigIsolation;__ 


## EvtChannelConfigOwningPublisher
 __const win32evtlog.EvtChannelConfigOwningPublisher;__ 


## EvtChannelConfigPropertyIdEND
 __const win32evtlog.EvtChannelConfigPropertyIdEND;__ 


## EvtChannelConfigType
 __const win32evtlog.EvtChannelConfigType;__ 


## EvtChannelLoggingConfigAutoBackup
 __const win32evtlog.EvtChannelLoggingConfigAutoBackup;__ 


## EvtChannelLoggingConfigLogFilePath
 __const win32evtlog.EvtChannelLoggingConfigLogFilePath;__ 


## EvtChannelLoggingConfigMaxSize
 __const win32evtlog.EvtChannelLoggingConfigMaxSize;__ 


## EvtChannelLoggingConfigRetention
 __const win32evtlog.EvtChannelLoggingConfigRetention;__ 


## EvtChannelPublisherList
 __const win32evtlog.EvtChannelPublisherList;__ 


## EvtChannelPublishingConfigBufferSize
 __const win32evtlog.EvtChannelPublishingConfigBufferSize;__ 


## EvtChannelPublishingConfigClockType
 __const win32evtlog.EvtChannelPublishingConfigClockType;__ 


## EvtChannelPublishingConfigControlGuid
 __const win32evtlog.EvtChannelPublishingConfigControlGuid;__ 


## EvtChannelPublishingConfigFileMax
 __const win32evtlog.EvtChannelPublishingConfigFileMax;__ 


## EvtChannelPublishingConfigKeywords
 __const win32evtlog.EvtChannelPublishingConfigKeywords;__ 


## EvtChannelPublishingConfigLatency
 __const win32evtlog.EvtChannelPublishingConfigLatency;__ 


## EvtChannelPublishingConfigLevel
 __const win32evtlog.EvtChannelPublishingConfigLevel;__ 


## EvtChannelPublishingConfigMaxBuffers
 __const win32evtlog.EvtChannelPublishingConfigMaxBuffers;__ 


## EvtChannelPublishingConfigMinBuffers
 __const win32evtlog.EvtChannelPublishingConfigMinBuffers;__ 


## EvtChannelPublishingConfigSidType
 __const win32evtlog.EvtChannelPublishingConfigSidType;__ 


## [win32evtlog](#win32evtlog).EvtClearLog

 __EvtClearLog( *ChannelPath*  *, TargetFilePath*  *, Session*  *, Flags* __ )
Clears an event log and optionally exports events to an archive

#### Parameters


  -  *ChannelPath* : str

    Name of event log to be cleared

  -  *TargetFilePath=None* : str

    Name of file in which cleared events will be archived, or None

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtCreateBookmark

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtCreateBookmark( *BookmarkXML* __ )
Creates a bookmark

#### Parameters


  -  *BookmarkXML=None* : str

    XML representation of a bookmark as returned by[win32evtlog::EvtRender](win32evtlog.md#win32evtlogevtrender), or None for a new bookmark

#### Comments
Accepts keyword args

## EvtEventMetadataPropertyIdEND
 __const win32evtlog.EvtEventMetadataPropertyIdEND;__ 


## EvtEventPath
 __const win32evtlog.EvtEventPath;__ 


## EvtEventPropertyIdEND
 __const win32evtlog.EvtEventPropertyIdEND;__ 


## EvtEventQueryIDs
 __const win32evtlog.EvtEventQueryIDs;__ 


## [win32evtlog](#win32evtlog).EvtExportLog

 __EvtExportLog( *Path*  *, TargetFilePath*  *, Flags*  *, Query*  *, Session* __ )
Exports events from a channel or log file

#### Parameters


  -  *Path* : str

    Path of a live event log channel or exported log file

  -  *TargetFilePath* : str

    File to create, cannot already exist

  -  *Flags* : int

    Combination of EvtExportLog* flags specifying the type of path

  -  *Query=None* : str

    Selects specific events to export

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

#### Comments
Accepts keyword args

## EvtExportLogChannelPath
 __const win32evtlog.EvtExportLogChannelPath;__ 


## EvtExportLogFilePath
 __const win32evtlog.EvtExportLogFilePath;__ 


## EvtExportLogTolerateQueryErrors
 __const win32evtlog.EvtExportLogTolerateQueryErrors;__ 


## [win32evtlog](#win32evtlog).EvtGetChannelConfigProperty

(object, int) = __EvtGetChannelConfigProperty( *ChannelConfig*  *, PropertyId*  *, Flags* __ )
Retreives channel configuration information

#### Parameters


  -  *ChannelConfig* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Config handle as returned by[win32evtlog::EvtOpenChannelConfig](win32evtlog.md#win32evtlogevtopenchannelconfig)

  -  *PropertyId* : int

    Property to retreive, one of EvtChannel* constants

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#win32evtlog).EvtGetEventInfo

(object, int) = __EvtGetEventInfo( *Event*  *, PropertyId* __ )
Retrieves information about the source of an event

#### Parameters


  -  *Event* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an event

  -  *PropertyId* : int

    Property to retreive, EvtEvent*

#### Comments
Accepts keyword args
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#win32evtlog).EvtGetEventMetadataProperty

(object, int) = __EvtGetEventMetadataProperty( *EventMetadata*  *, PropertyId*  *, Flags* __ )
Retrieves a property from an event publisher

#### Parameters


  -  *EventMetadata* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Event metadata handle as returned by[win32evtlog::EvtNextEventMetadata](win32evtlog.md#win32evtlogevtnexteventmetadata)

  -  *PropertyId* : int

    Property to retreive, EventMetadata*

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value (EvtVarType*).

## [win32evtlog](#win32evtlog).EvtGetExtendedStatus

str = __EvtGetExtendedStatus(__ )
Returns additional error info from last Evt* call

## [win32evtlog](#win32evtlog).EvtGetLogInfo

(object, int) = __EvtGetLogInfo( *Log*  *, PropertyId* __ )
Retrieves log file or channel information

#### Parameters


  -  *Log* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Event log handle as returned by[win32evtlog::EvtOpenLog](win32evtlog.md#win32evtlogevtopenlog)

  -  *PropertyId* : int

    Property to retreive, EvtLog*

#### Comments
Accepts keyword args
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#win32evtlog).EvtGetObjectArrayProperty

(object, int) = __EvtGetObjectArrayProperty( *ObjectArray*  *, PropertyId*  *, ArrayIndex*  *, Flags* __ )
Retrieves an item from an object array

#### Parameters


  -  *ObjectArray* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an array of objects as returned by[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)for some ProperyId's

  -  *PropertyId* : int

    Type of property contained in the array

  -  *ArrayIndex* : int

    Zero-based index of item to retrieve

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value (EvtVarType*)

## [win32evtlog](#win32evtlog).EvtGetObjectArraySize

int = __EvtGetObjectArraySize( *ObjectArray* __ )
Returns the size of an array of event objects

#### Parameters


  -  *ObjectArray* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an array of objects as returned by[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)for some ProperyId's

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtGetPublisherMetadataProperty

(object, int) = __EvtGetPublisherMetadataProperty( *PublisherMetadata*  *, PropertyId*  *, Flags* __ )
Retrieves a property from an event publisher

#### Parameters


  -  *PublisherMetadata* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Publisher handle as returned by[win32evtlog::EvtOpenPublisherMetadata](win32evtlog.md#win32evtlogevtopenpublishermetadata)

  -  *PropertyId* : int

    Property to retreive, EvtPublisherMetadata*

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value (EvtVarType*) 

Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using[win32evtlog::EvtGetObjectArraySize](win32evtlog.md#win32evtlogevtgetobjectarraysize)and[win32evtlog::EvtGetObjectArrayProperty](win32evtlog.md#win32evtlogevtgetobjectarrayproperty).

## EvtLogAttributes
 __const win32evtlog.EvtLogAttributes;__ 


## EvtLogCreationTime
 __const win32evtlog.EvtLogCreationTime;__ 


## EvtLogFileSize
 __const win32evtlog.EvtLogFileSize;__ 


## EvtLogFull
 __const win32evtlog.EvtLogFull;__ 


## EvtLogLastAccessTime
 __const win32evtlog.EvtLogLastAccessTime;__ 


## EvtLogLastWriteTime
 __const win32evtlog.EvtLogLastWriteTime;__ 


## EvtLogNumberOfLogRecords
 __const win32evtlog.EvtLogNumberOfLogRecords;__ 


## EvtLogOldestRecordNumber
 __const win32evtlog.EvtLogOldestRecordNumber;__ 


## [win32evtlog](#win32evtlog).EvtNext

([PyEVT_HANDLE](PyEVT.md#pyevthandle),...) = __EvtNext( *ResultSet*  *, Count*  *, Timeout*  *, Flags* __ )
Returns events from a query

#### Parameters


  -  *ResultSet* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to event query or subscription

  -  *Count* : int

    Number of events to return

  -  *Timeout=-1* : int

    Time to wait in milliseconds, use -1 for infinite

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns a tuple of handles to events.  If no items are available, returns 

an empty tuple instead of raising an exception.

## [win32evtlog](#win32evtlog).EvtNextChannelPath

str = __EvtNextChannelPath( *ChannelEnum* __ )
Retrieves a channel path from an enumeration

#### Parameters


  -  *ChannelEnum* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an enumeration as returned by[win32evtlog::EvtOpenChannelEnum](win32evtlog.md#win32evtlogevtopenchannelenum)

#### Comments
Accepts keyword args

#### Return Value
Returns None at end of enumeration

## [win32evtlog](#win32evtlog).EvtNextEventMetadata

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtNextEventMetadata( *EventMetadataEnum*  *, Flags* __ )
Retrieves the next item from an event metadata enumeration

#### Parameters


  -  *EventMetadataEnum* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Enumeration handle as returned by[win32evtlog::EvtOpenEventMetadataEnum](win32evtlog.md#win32evtlogevtopeneventmetadataenum)

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtNextPublisherId

str = __EvtNextPublisherId( *PublisherEnum* __ )
Returns the next publisher from an enumeration

#### Parameters


  -  *PublisherEnum* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an enumeration as returned by[win32evtlog::EvtOpenPublisherEnum](win32evtlog.md#win32evtlogevtopenpublisherenum)

#### Comments
Accepts keyword args

#### Return Value
Returns None at end of enumeration

## [win32evtlog](#win32evtlog).EvtOpenChannelConfig

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenChannelConfig( *ChannelPath*  *, Session*  *, Flags* __ )
Opens channel configuration

#### Parameters


  -  *ChannelPath* : str

    Channel to be opened

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Session handle as returned by[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession), or None for local machine

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtOpenChannelEnum

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenChannelEnum( *Session*  *, Flags* __ )
Begins an enumeration of event channels

#### Parameters


  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtOpenChannelPath
 __const win32evtlog.EvtOpenChannelPath;__ 


## [win32evtlog](#win32evtlog).EvtOpenEventMetadataEnum

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenEventMetadataEnum( *PublisherMetadata*  *, Flags* __ )
Enumerates the events that a publisher provides

#### Parameters


  -  *PublisherMetadata* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Publisher handle as returned by[win32evtlog::EvtOpenPublisherMetadata](win32evtlog.md#win32evtlogevtopenpublishermetadata)

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtOpenFilePath
 __const win32evtlog.EvtOpenFilePath;__ 


## [win32evtlog](#win32evtlog).EvtOpenLog

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenLog( *Path*  *, Flags*  *, Session* __ )
Opens an event log or exported log archive

#### Parameters


  -  *Path* : str

    Event log name or Path of an export file

  -  *Flags* : int

    EvtOpenChannelPath (1) or EvtOpenFilePath (2)

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtOpenPublisherEnum

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenPublisherEnum( *Session*  *, Flags* __ )
Begins an enumeration of event publishers

#### Parameters


  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtOpenPublisherMetadata

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenPublisherMetadata( *PublisherIdentity*  *, Session*  *, LogFilePath*  *, Locale*  *, Flags* __ )
Opens a publisher to retrieve properties using[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)

#### Parameters


  -  *PublisherIdentity* : str

    Publisher id as returned by[win32evtlog::EvtNextPublisherId](win32evtlog.md#win32evtlogevtnextpublisherid)

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to remote session, or None for local machine

  -  *LogFilePath=None* : str

    Log file from which to retrieve publisher, or None for locally registered publisher

  -  *Locale=0* : int

    Locale to use for retrieved properties, use 0 for current locale

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog).EvtOpenSession

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtOpenSession( *Login*  *, LoginClass*  *, Timeout*  *, Flags* __ )
Creates a session used to access the Event Log on another machine

#### Parameters


  -  *Login* :[PyEVT_RPC_LOGIN](PyEVT.md#pyevtrpc_login)

    Credentials to be used to access remote machine

  -  *LoginClass=EvtRpcLogin* : int

    Type of login to perform, EvtRpcLogin is only defined value

  -  *Timeout=0* : int

    Reserved, use only 0

  -  *Flags=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtPublisherMetadataChannelReferenceFlags
 __const win32evtlog.EvtPublisherMetadataChannelReferenceFlags;__ 


## EvtPublisherMetadataChannelReferenceID
 __const win32evtlog.EvtPublisherMetadataChannelReferenceID;__ 


## EvtPublisherMetadataChannelReferenceIndex
 __const win32evtlog.EvtPublisherMetadataChannelReferenceIndex;__ 


## EvtPublisherMetadataChannelReferenceMessageID
 __const win32evtlog.EvtPublisherMetadataChannelReferenceMessageID;__ 


## EvtPublisherMetadataChannelReferencePath
 __const win32evtlog.EvtPublisherMetadataChannelReferencePath;__ 


## EvtPublisherMetadataChannelReferences
 __const win32evtlog.EvtPublisherMetadataChannelReferences;__ 


## EvtPublisherMetadataHelpLink
 __const win32evtlog.EvtPublisherMetadataHelpLink;__ 


## EvtPublisherMetadataKeywordMessageID
 __const win32evtlog.EvtPublisherMetadataKeywordMessageID;__ 


## EvtPublisherMetadataKeywordName
 __const win32evtlog.EvtPublisherMetadataKeywordName;__ 


## EvtPublisherMetadataKeywordValue
 __const win32evtlog.EvtPublisherMetadataKeywordValue;__ 


## EvtPublisherMetadataKeywords
 __const win32evtlog.EvtPublisherMetadataKeywords;__ 


## EvtPublisherMetadataLevelMessageID
 __const win32evtlog.EvtPublisherMetadataLevelMessageID;__ 


## EvtPublisherMetadataLevelName
 __const win32evtlog.EvtPublisherMetadataLevelName;__ 


## EvtPublisherMetadataLevelValue
 __const win32evtlog.EvtPublisherMetadataLevelValue;__ 


## EvtPublisherMetadataLevels
 __const win32evtlog.EvtPublisherMetadataLevels;__ 


## EvtPublisherMetadataMessageFilePath
 __const win32evtlog.EvtPublisherMetadataMessageFilePath;__ 


## EvtPublisherMetadataOpcodeMessageID
 __const win32evtlog.EvtPublisherMetadataOpcodeMessageID;__ 


## EvtPublisherMetadataOpcodeName
 __const win32evtlog.EvtPublisherMetadataOpcodeName;__ 


## EvtPublisherMetadataOpcodeValue
 __const win32evtlog.EvtPublisherMetadataOpcodeValue;__ 


## EvtPublisherMetadataOpcodes
 __const win32evtlog.EvtPublisherMetadataOpcodes;__ 


## EvtPublisherMetadataParameterFilePath
 __const win32evtlog.EvtPublisherMetadataParameterFilePath;__ 


## EvtPublisherMetadataPropertyIdEND
 __const win32evtlog.EvtPublisherMetadataPropertyIdEND;__ 


## EvtPublisherMetadataPublisherGuid
 __const win32evtlog.EvtPublisherMetadataPublisherGuid;__ 


## EvtPublisherMetadataPublisherMessageID
 __const win32evtlog.EvtPublisherMetadataPublisherMessageID;__ 


## EvtPublisherMetadataResourceFilePath
 __const win32evtlog.EvtPublisherMetadataResourceFilePath;__ 


## EvtPublisherMetadataTaskEventGuid
 __const win32evtlog.EvtPublisherMetadataTaskEventGuid;__ 


## EvtPublisherMetadataTaskMessageID
 __const win32evtlog.EvtPublisherMetadataTaskMessageID;__ 


## EvtPublisherMetadataTaskName
 __const win32evtlog.EvtPublisherMetadataTaskName;__ 


## EvtPublisherMetadataTaskValue
 __const win32evtlog.EvtPublisherMetadataTaskValue;__ 


## EvtPublisherMetadataTasks
 __const win32evtlog.EvtPublisherMetadataTasks;__ 


## [win32evtlog](#win32evtlog).EvtQuery

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtQuery( *Path*  *, Flags*  *, Query*  *, Session* __ )
Opens a query over a log channel or exported log file

#### Parameters


  -  *Path* : str

    Log channel or exported log file, depending on Flags

  -  *Flags* : int

    Combination of EVT_QUERY_FLAGS (EvtQuery*)

  -  *Query=None* : str

    Selects events to return, None or '*' for all events

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session (see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)), or None for local machine.

#### Comments
Accepts keyword args

## EvtQueryChannelPath
 __const win32evtlog.EvtQueryChannelPath;__ 


## EvtQueryFilePath
 __const win32evtlog.EvtQueryFilePath;__ 


## EvtQueryForwardDirection
 __const win32evtlog.EvtQueryForwardDirection;__ 


## EvtQueryReverseDirection
 __const win32evtlog.EvtQueryReverseDirection;__ 


## EvtQueryTolerateQueryErrors
 __const win32evtlog.EvtQueryTolerateQueryErrors;__ 


## [win32evtlog](#win32evtlog).EvtRender

str = __EvtRender( *Event*  *, Flags* __ )
Formats an event into XML text

#### Parameters


  -  *Event* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an event or bookmark

  -  *Flags* : int

    EvtRenderEventXml or EvtRenderBookmark indicating type of handle

#### Comments
Accepts keyword args
Rendering event values (Flags=EvtRenderEventValues) is not currently supported

## EvtRenderBookmark
 __const win32evtlog.EvtRenderBookmark;__ 


## EvtRenderEventValues
 __const win32evtlog.EvtRenderEventValues;__ 


## EvtRenderEventXml
 __const win32evtlog.EvtRenderEventXml;__ 


## EvtRpcLogin
 __const win32evtlog.EvtRpcLogin;__ 


## EvtRpcLoginAuthDefault
 __const win32evtlog.EvtRpcLoginAuthDefault;__ 


## EvtRpcLoginAuthKerberos
 __const win32evtlog.EvtRpcLoginAuthKerberos;__ 


## EvtRpcLoginAuthNTLM
 __const win32evtlog.EvtRpcLoginAuthNTLM;__ 


## EvtRpcLoginAuthNegotiate
 __const win32evtlog.EvtRpcLoginAuthNegotiate;__ 


## [win32evtlog](#win32evtlog).EvtSeek

 __EvtSeek( *ResultSet*  *, Position*  *, Flags*  *, Bookmark*  *, Timeout* __ )
Changes the current position in a result set

#### Parameters


  -  *ResultSet* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to event query or subscription

  -  *Position* : int

    Offset (base from which to seek is specified by Flags)

  -  *Flags* : int

    EvtSeekRelative* flag indicating seek origin

  -  *Bookmark=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Used as seek origin only if Flags contains EvtSeekRelativeToBookmark

  -  *Timeout=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtSeekOriginMask
 __const win32evtlog.EvtSeekOriginMask;__ 


## EvtSeekRelativeToBookmark
 __const win32evtlog.EvtSeekRelativeToBookmark;__ 


## EvtSeekRelativeToCurrent
 __const win32evtlog.EvtSeekRelativeToCurrent;__ 


## EvtSeekRelativeToFirst
 __const win32evtlog.EvtSeekRelativeToFirst;__ 


## EvtSeekRelativeToLast
 __const win32evtlog.EvtSeekRelativeToLast;__ 


## EvtSeekStrict
 __const win32evtlog.EvtSeekStrict;__ 


## [win32evtlog](#win32evtlog).EvtSubscribe

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtSubscribe( *ChannelPath*  *, Flags*  *, SignalEvent*  *, Callback*  *, Context*  *, Query*  *, Session*  *, Bookmark* __ )
Requests notification for events

#### Parameters


  -  *ChannelPath* : str

    Name of an event log channel

  -  *Flags* : int

    Combination of EvtSubscribe* flags determining how subscription is initiated

  -  *SignalEvent=None* : __Py_HANDLE__ 

    An event handle to be set when events are available (see[win32event::CreateEvent](win32event.md#win32eventcreateevent))

  -  *Callback=None* : function

    Python function to be called with each event

  -  *Context=None* : object

    Arbitrary object to be passed to the callback function

  -  *Query=None* : str

    XML query used to select specific events, use None or '*' for all events

  -  *Session=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a session on another machine, or None for local

  -  *Bookmark=None* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

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

passed to[win32evtlog::EvtNext](win32evtlog.md#win32evtlogevtnext)to obtain the events.

## EvtSubscribeActionDeliver
 __const win32evtlog.EvtSubscribeActionDeliver;__ 


## EvtSubscribeActionError
 __const win32evtlog.EvtSubscribeActionError;__ 


## EvtSubscribeOriginMask
 __const win32evtlog.EvtSubscribeOriginMask;__ 


## EvtSubscribeStartAfterBookmark
 __const win32evtlog.EvtSubscribeStartAfterBookmark;__ 


## EvtSubscribeStartAtOldestRecord
 __const win32evtlog.EvtSubscribeStartAtOldestRecord;__ 


## EvtSubscribeStrict
 __const win32evtlog.EvtSubscribeStrict;__ 


## EvtSubscribeToFutureEvents
 __const win32evtlog.EvtSubscribeToFutureEvents;__ 


## EvtSubscribeTolerateQueryErrors
 __const win32evtlog.EvtSubscribeTolerateQueryErrors;__ 


## [win32evtlog](#win32evtlog).EvtUpdateBookmark

[PyEVT_HANDLE](PyEVT.md#pyevthandle)= __EvtUpdateBookmark( *Bookmark*  *, Event* __ )
Repositions a bookmark to an event

#### Parameters


  -  *Bookmark* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to a bookmark

  -  *Event* :[PyEVT_HANDLE](PyEVT.md#pyevthandle)

    Handle to an event

#### Comments
Accepts keyword args

## EvtVarTypeAnsiString
 __const win32evtlog.EvtVarTypeAnsiString;__ 


## EvtVarTypeBinary
 __const win32evtlog.EvtVarTypeBinary;__ 


## EvtVarTypeBoolean
 __const win32evtlog.EvtVarTypeBoolean;__ 


## EvtVarTypeByte
 __const win32evtlog.EvtVarTypeByte;__ 


## EvtVarTypeDouble
 __const win32evtlog.EvtVarTypeDouble;__ 


## EvtVarTypeEvtHandle
 __const win32evtlog.EvtVarTypeEvtHandle;__ 


## EvtVarTypeEvtXml
 __const win32evtlog.EvtVarTypeEvtXml;__ 


## EvtVarTypeFileTime
 __const win32evtlog.EvtVarTypeFileTime;__ 


## EvtVarTypeGuid
 __const win32evtlog.EvtVarTypeGuid;__ 


## EvtVarTypeHexInt32
 __const win32evtlog.EvtVarTypeHexInt32;__ 


## EvtVarTypeHexInt64
 __const win32evtlog.EvtVarTypeHexInt64;__ 


## EvtVarTypeInt16
 __const win32evtlog.EvtVarTypeInt16;__ 


## EvtVarTypeInt32
 __const win32evtlog.EvtVarTypeInt32;__ 


## EvtVarTypeInt64
 __const win32evtlog.EvtVarTypeInt64;__ 


## EvtVarTypeNull
 __const win32evtlog.EvtVarTypeNull;__ 


## EvtVarTypeSByte
 __const win32evtlog.EvtVarTypeSByte;__ 


## EvtVarTypeSid
 __const win32evtlog.EvtVarTypeSid;__ 


## EvtVarTypeSingle
 __const win32evtlog.EvtVarTypeSingle;__ 


## EvtVarTypeSizeT
 __const win32evtlog.EvtVarTypeSizeT;__ 


## EvtVarTypeString
 __const win32evtlog.EvtVarTypeString;__ 


## EvtVarTypeSysTime
 __const win32evtlog.EvtVarTypeSysTime;__ 


## EvtVarTypeUInt16
 __const win32evtlog.EvtVarTypeUInt16;__ 


## EvtVarTypeUInt32
 __const win32evtlog.EvtVarTypeUInt32;__ 


## EvtVarTypeUInt64
 __const win32evtlog.EvtVarTypeUInt64;__ 


## [win32evtlog](#win32evtlog).GetNumberOfEventLogRecords

int = __GetNumberOfEventLogRecords( *handle* __ )
Returns the number of event log records.

#### Parameters


  -  *handle* : int

    Handle to the event log to query.

## [win32evtlog](#win32evtlog).GetOldestEventLogRecord

int = __GetOldestEventLogRecord(__ )
Returns the number of event log records.

#### Return Value
The result is the absolute record number of the oldest record in the given event log.

## [win32evtlog](#win32evtlog).NotifyChangeEventLog

 __NotifyChangeEventLog( *handle*  *, handle* __ )
Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.

#### Parameters


  -  *handle* : int

    Handle to an event log file, obtained by calling[win32evtlog::OpenEventLog](win32evtlog.md#win32evtlogopeneventlog)function. When an event is written to this log file, the event specified by hEvent becomes signaled.

  -  *handle* : int

    A handle to a Win32 event. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter.

## [win32evtlog](#win32evtlog).OpenBackupEventLog

[PyEVTLOG_HANDLE](PyEVTLOG.md#pyevtloghandle)= __OpenBackupEventLog( *serverName*  *, fileName* __ )
Opens a previously saved event log.

#### Parameters


  -  *serverName* :[PyUnicode](#pyunicode)

    The server name, or None

  -  *fileName* :[PyUnicode](#pyunicode)

    The filename to open

## [win32evtlog](#win32evtlog).OpenEventLog

[PyEVTLOG_HANDLE](PyEVTLOG.md#pyevtloghandle)= __OpenEventLog( *serverName*  *, sourceName* __ )
Opens an event log.

#### Parameters


  -  *serverName* :[PyUnicode](#pyunicode)

    The server name, or None

  -  *sourceName* :[PyUnicode](#pyunicode)

    specifies the name of the source that the returned handle will reference. The source name must be a subkey of a logfile entry under the EventLog key in the registry.

## [win32evtlog](#win32evtlog).ReadEventLog

[object,...] = __ReadEventLog( *Handle*  *, Flags*  *, Offset*  *, Size* __ )
Reads some event log records.

#### Parameters


  -  *Handle* : __Py_HANDLE__ 

    Handle to a an opened event log (see[win32evtlog::OpenEventLog](win32evtlog.md#win32evtlogopeneventlog))

  -  *Flags* : int

    Reading flags

  -  *Offset* : int

    Record offset to read (in SEEK mode).

  -  *Size=4096* : int

    Output buffer size.

#### Return Value
If there are no event log records available, then an empty list is returned.

## [win32evtlog](#win32evtlog).RegisterEventSource

int = __RegisterEventSource( *serverName*  *, sourceName* __ )
Registers an Event Source

#### Parameters


  -  *serverName* :[PyUnicode](#pyunicode)

    The server name, or None

  -  *sourceName* :[PyUnicode](#pyunicode)

    The source name

## [win32evtlog](#win32evtlog).ReportEvent

 __ReportEvent( *EventLog*  *, Type*  *, Category*  *, EventID*  *, UserSid*  *, Strings*  *, RawData* __ )
Reports an event

#### Parameters


  -  *EventLog* :[PyHANDLE](#pyhandle)

    Handle to an event log

  -  *Type* : int

    win32con.EVENTLOG_* value

  -  *Category* : int

    Source-specific event category

  -  *EventID* : int

    Source-specific event identifier

  -  *UserSid* :[PySID](#pysid)

    Sid of current user, can be None

  -  *Strings* : sequence

    Sequence of unicode strings to be inserted in message

  -  *RawData* : str

    Binary data for event, can be None