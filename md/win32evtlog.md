# win32evtlog

## Module win32evtlog

A module, encapsulating the Windows Win32 event log API\.
The Evt\* functions are only available on Vista and later\.  Attempting to call 

them on XP will result in the process exiting, rather than a python exception\.

#### Methods


  - [ReadEventLog](win32evtlog.md#win32evtlogreadeventlog)

    Reads some event log records\.&nbsp;

  - [ClearEventLog](win32evtlog.md#win32evtlogcleareventlog)

    Clears the event log&nbsp;

  - [BackupEventLog](win32evtlog.md#win32evtlogbackupeventlog)

    Backs up the event log&nbsp;

  - [CloseEventLog](win32evtlog.md#win32evtlogcloseeventlog)

    Closes the eventlog&nbsp;

  - [DeregisterEventSource](win32evtlog.md#win32evtlogderegistereventsource)

    Deregisters an Event Source&nbsp;

  - [NotifyChangeEventLog](win32evtlog.md#win32evtlognotifychangeeventlog)

    Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter\. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled\.&nbsp;

  - [GetNumberOfEventLogRecords](win32evtlog.md#win32evtloggetnumberofeventlogrecords)

    Returns the number of event log records\.&nbsp;

  - [GetOldestEventLogRecord](win32evtlog.md#win32evtloggetoldesteventlogrecord)

    Returns the number of event log records\.&nbsp;

  - [OpenEventLog](win32evtlog.md#win32evtlogopeneventlog)

    Opens an event log\.&nbsp;

  - [RegisterEventSource](win32evtlog.md#win32evtlogregistereventsource)

    Registers an Event Source&nbsp;

  - [OpenBackupEventLog](win32evtlog.md#win32evtlogopenbackupeventlog)

    Opens a previously saved event log\.&nbsp;

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

    Returns additional error info from last Evt\* call&nbsp;

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

## [win32evtlog](#win32evtlog)\.BackupEventLog

 **BackupEventLog\( *handle*  *, eventLogName* ** \)
Backs up the event log

#### Parameters


  -  *handle* : int

    Handle to the event log to backup\.

  -  *eventLogName* :[PyUnicode](#pyunicode)

    The name of the event log to save to

## [win32evtlog](#win32evtlog)\.ClearEventLog

 **ClearEventLog\( *handle*  *, eventLogName* ** \)
Clears the event log

#### Parameters


  -  *handle* : int

    Handle to the event log to clear\.

  -  *eventLogName* :[PyUnicode](#pyunicode)

    The name of the event log to save to, or None

## [win32evtlog](#win32evtlog)\.CloseEventLog

 **CloseEventLog\( *handle* ** \)
Closes the eventlog

#### Parameters


  -  *handle* : int

    Handle to the event log to close

## [win32evtlog](#win32evtlog)\.DeregisterEventSource

 **DeregisterEventSource\( *handle* ** \)
Deregisters an Event Source

#### Parameters


  -  *handle* : int

    Identifies the event log whose handle was returned by[win32evtlog::RegisterEventSource](win32evtlog.md#win32evtlogregistereventsource)

## EVENTLOG\_AUDIT\_FAILURE
 **const win32evtlog\.EVENTLOG\_AUDIT\_FAILURE;** 


## EVENTLOG\_AUDIT\_SUCCESS
 **const win32evtlog\.EVENTLOG\_AUDIT\_SUCCESS;** 


## EVENTLOG\_BACKWARDS\_READ
 **const win32evtlog\.EVENTLOG\_BACKWARDS\_READ;** 


## EVENTLOG\_END\_ALL\_PAIRED\_EVENTS
 **const win32evtlog\.EVENTLOG\_END\_ALL\_PAIRED\_EVENTS;** 


## EVENTLOG\_END\_PAIRED\_EVENT
 **const win32evtlog\.EVENTLOG\_END\_PAIRED\_EVENT;** 


## EVENTLOG\_ERROR\_TYPE
 **const win32evtlog\.EVENTLOG\_ERROR\_TYPE;** 


## EVENTLOG\_FORWARDS\_READ
 **const win32evtlog\.EVENTLOG\_FORWARDS\_READ;** 


## EVENTLOG\_INFORMATION\_TYPE
 **const win32evtlog\.EVENTLOG\_INFORMATION\_TYPE;** 


## EVENTLOG\_PAIRED\_EVENT\_ACTIVE
 **const win32evtlog\.EVENTLOG\_PAIRED\_EVENT\_ACTIVE;** 


## EVENTLOG\_PAIRED\_EVENT\_INACTIVE
 **const win32evtlog\.EVENTLOG\_PAIRED\_EVENT\_INACTIVE;** 


## EVENTLOG\_SEEK\_READ
 **const win32evtlog\.EVENTLOG\_SEEK\_READ;** 


## EVENTLOG\_SEQUENTIAL\_READ
 **const win32evtlog\.EVENTLOG\_SEQUENTIAL\_READ;** 


## EVENTLOG\_START\_PAIRED\_EVENT
 **const win32evtlog\.EVENTLOG\_START\_PAIRED\_EVENT;** 


## EVENTLOG\_SUCCESS
 **const win32evtlog\.EVENTLOG\_SUCCESS;** 


## EVENTLOG\_WARNING\_TYPE
 **const win32evtlog\.EVENTLOG\_WARNING\_TYPE;** 


## EventMetadataEventChannel
 **const win32evtlog\.EventMetadataEventChannel;** 


## EventMetadataEventID
 **const win32evtlog\.EventMetadataEventID;** 


## EventMetadataEventKeyword
 **const win32evtlog\.EventMetadataEventKeyword;** 


## EventMetadataEventLevel
 **const win32evtlog\.EventMetadataEventLevel;** 


## EventMetadataEventMessageID
 **const win32evtlog\.EventMetadataEventMessageID;** 


## EventMetadataEventOpcode
 **const win32evtlog\.EventMetadataEventOpcode;** 


## EventMetadataEventTask
 **const win32evtlog\.EventMetadataEventTask;** 


## EventMetadataEventTemplate
 **const win32evtlog\.EventMetadataEventTemplate;** 


## EventMetadataEventVersion
 **const win32evtlog\.EventMetadataEventVersion;** 


## [win32evtlog](#win32evtlog)\.EvtArchiveExportedLog

 **EvtArchiveExportedLog\( *LogFilePath*  *, Locale*  *, Session*  *, Flags* ** \)
Localizes an exported event log file

#### Parameters


  -  *LogFilePath* : str

    Filename of an exported log file

  -  *Locale* : int

    Locale id

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

  -  *Flags\=0* : int

    Reserved

#### Comments
Accepts keyword args

## EvtChannelConfigAccess
 **const win32evtlog\.EvtChannelConfigAccess;** 


## EvtChannelConfigClassicEventlog
 **const win32evtlog\.EvtChannelConfigClassicEventlog;** 


## EvtChannelConfigEnabled
 **const win32evtlog\.EvtChannelConfigEnabled;** 


## EvtChannelConfigIsolation
 **const win32evtlog\.EvtChannelConfigIsolation;** 


## EvtChannelConfigOwningPublisher
 **const win32evtlog\.EvtChannelConfigOwningPublisher;** 


## EvtChannelConfigPropertyIdEND
 **const win32evtlog\.EvtChannelConfigPropertyIdEND;** 


## EvtChannelConfigType
 **const win32evtlog\.EvtChannelConfigType;** 


## EvtChannelLoggingConfigAutoBackup
 **const win32evtlog\.EvtChannelLoggingConfigAutoBackup;** 


## EvtChannelLoggingConfigLogFilePath
 **const win32evtlog\.EvtChannelLoggingConfigLogFilePath;** 


## EvtChannelLoggingConfigMaxSize
 **const win32evtlog\.EvtChannelLoggingConfigMaxSize;** 


## EvtChannelLoggingConfigRetention
 **const win32evtlog\.EvtChannelLoggingConfigRetention;** 


## EvtChannelPublisherList
 **const win32evtlog\.EvtChannelPublisherList;** 


## EvtChannelPublishingConfigBufferSize
 **const win32evtlog\.EvtChannelPublishingConfigBufferSize;** 


## EvtChannelPublishingConfigClockType
 **const win32evtlog\.EvtChannelPublishingConfigClockType;** 


## EvtChannelPublishingConfigControlGuid
 **const win32evtlog\.EvtChannelPublishingConfigControlGuid;** 


## EvtChannelPublishingConfigFileMax
 **const win32evtlog\.EvtChannelPublishingConfigFileMax;** 


## EvtChannelPublishingConfigKeywords
 **const win32evtlog\.EvtChannelPublishingConfigKeywords;** 


## EvtChannelPublishingConfigLatency
 **const win32evtlog\.EvtChannelPublishingConfigLatency;** 


## EvtChannelPublishingConfigLevel
 **const win32evtlog\.EvtChannelPublishingConfigLevel;** 


## EvtChannelPublishingConfigMaxBuffers
 **const win32evtlog\.EvtChannelPublishingConfigMaxBuffers;** 


## EvtChannelPublishingConfigMinBuffers
 **const win32evtlog\.EvtChannelPublishingConfigMinBuffers;** 


## EvtChannelPublishingConfigSidType
 **const win32evtlog\.EvtChannelPublishingConfigSidType;** 


## [win32evtlog](#win32evtlog)\.EvtClearLog

 **EvtClearLog\( *ChannelPath*  *, TargetFilePath*  *, Session*  *, Flags* ** \)
Clears an event log and optionally exports events to an archive

#### Parameters


  -  *ChannelPath* : str

    Name of event log to be cleared

  -  *TargetFilePath\=None* : str

    Name of file in which cleared events will be archived, or None

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtCreateBookmark

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtCreateBookmark\( *BookmarkXML* ** \)
Creates a bookmark

#### Parameters


  -  *BookmarkXML\=None* : str

    XML representation of a bookmark as returned by[win32evtlog::EvtRender](win32evtlog.md#win32evtlogevtrender), or None for a new bookmark

#### Comments
Accepts keyword args

## EvtEventMetadataPropertyIdEND
 **const win32evtlog\.EvtEventMetadataPropertyIdEND;** 


## EvtEventPath
 **const win32evtlog\.EvtEventPath;** 


## EvtEventPropertyIdEND
 **const win32evtlog\.EvtEventPropertyIdEND;** 


## EvtEventQueryIDs
 **const win32evtlog\.EvtEventQueryIDs;** 


## [win32evtlog](#win32evtlog)\.EvtExportLog

 **EvtExportLog\( *Path*  *, TargetFilePath*  *, Flags*  *, Query*  *, Session* ** \)
Exports events from a channel or log file

#### Parameters


  -  *Path* : str

    Path of a live event log channel or exported log file

  -  *TargetFilePath* : str

    File to create, cannot already exist

  -  *Flags* : int

    Combination of EvtExportLog\* flags specifying the type of path

  -  *Query\=None* : str

    Selects specific events to export

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

#### Comments
Accepts keyword args

## EvtExportLogChannelPath
 **const win32evtlog\.EvtExportLogChannelPath;** 


## EvtExportLogFilePath
 **const win32evtlog\.EvtExportLogFilePath;** 


## EvtExportLogTolerateQueryErrors
 **const win32evtlog\.EvtExportLogTolerateQueryErrors;** 


## [win32evtlog](#win32evtlog)\.EvtGetChannelConfigProperty

\(object, int\) \= **EvtGetChannelConfigProperty\( *ChannelConfig*  *, PropertyId*  *, Flags* ** \)
Retreives channel configuration information

#### Parameters


  -  *ChannelConfig* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Config handle as returned by[win32evtlog::EvtOpenChannelConfig](win32evtlog.md#win32evtlogevtopenchannelconfig)

  -  *PropertyId* : int

    Property to retreive, one of EvtChannel\* constants

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args
Returns the value and type of value \(EvtVarType\*\)

## [win32evtlog](#win32evtlog)\.EvtGetEventInfo

\(object, int\) \= **EvtGetEventInfo\( *Event*  *, PropertyId* ** \)
Retrieves information about the source of an event

#### Parameters


  -  *Event* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an event

  -  *PropertyId* : int

    Property to retreive, EvtEvent\*

#### Comments
Accepts keyword args
Returns the value and type of value \(EvtVarType\*\)

## [win32evtlog](#win32evtlog)\.EvtGetEventMetadataProperty

\(object, int\) \= **EvtGetEventMetadataProperty\( *EventMetadata*  *, PropertyId*  *, Flags* ** \)
Retrieves a property from an event publisher

#### Parameters


  -  *EventMetadata* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Event metadata handle as returned by[win32evtlog::EvtNextEventMetadata](win32evtlog.md#win32evtlogevtnexteventmetadata)

  -  *PropertyId* : int

    Property to retreive, EventMetadata\*

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value \(EvtVarType\*\)\.

## [win32evtlog](#win32evtlog)\.EvtGetExtendedStatus

str \= **EvtGetExtendedStatus\(** \)
Returns additional error info from last Evt\* call

## [win32evtlog](#win32evtlog)\.EvtGetLogInfo

\(object, int\) \= **EvtGetLogInfo\( *Log*  *, PropertyId* ** \)
Retrieves log file or channel information

#### Parameters


  -  *Log* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Event log handle as returned by[win32evtlog::EvtOpenLog](win32evtlog.md#win32evtlogevtopenlog)

  -  *PropertyId* : int

    Property to retreive, EvtLog\*

#### Comments
Accepts keyword args
Returns the value and type of value \(EvtVarType\*\)

## [win32evtlog](#win32evtlog)\.EvtGetObjectArrayProperty

\(object, int\) \= **EvtGetObjectArrayProperty\( *ObjectArray*  *, PropertyId*  *, ArrayIndex*  *, Flags* ** \)
Retrieves an item from an object array

#### Parameters


  -  *ObjectArray* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an array of objects as returned by[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)for some ProperyId's

  -  *PropertyId* : int

    Type of property contained in the array

  -  *ArrayIndex* : int

    Zero-based index of item to retrieve

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value \(EvtVarType\*\)

## [win32evtlog](#win32evtlog)\.EvtGetObjectArraySize

int \= **EvtGetObjectArraySize\( *ObjectArray* ** \)
Returns the size of an array of event objects

#### Parameters


  -  *ObjectArray* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an array of objects as returned by[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)for some ProperyId's

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtGetPublisherMetadataProperty

\(object, int\) \= **EvtGetPublisherMetadataProperty\( *PublisherMetadata*  *, PropertyId*  *, Flags* ** \)
Retrieves a property from an event publisher

#### Parameters


  -  *PublisherMetadata* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Publisher handle as returned by[win32evtlog::EvtOpenPublisherMetadata](win32evtlog.md#win32evtlogevtopenpublishermetadata)

  -  *PropertyId* : int

    Property to retreive, EvtPublisherMetadata\*

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns the value and type of value \(EvtVarType\*\) 

Some properties return a handle \(type EvtVarTypeEvtHandle\) which can be iterated using[win32evtlog::EvtGetObjectArraySize](win32evtlog.md#win32evtlogevtgetobjectarraysize)and[win32evtlog::EvtGetObjectArrayProperty](win32evtlog.md#win32evtlogevtgetobjectarrayproperty)\.

## EvtLogAttributes
 **const win32evtlog\.EvtLogAttributes;** 


## EvtLogCreationTime
 **const win32evtlog\.EvtLogCreationTime;** 


## EvtLogFileSize
 **const win32evtlog\.EvtLogFileSize;** 


## EvtLogFull
 **const win32evtlog\.EvtLogFull;** 


## EvtLogLastAccessTime
 **const win32evtlog\.EvtLogLastAccessTime;** 


## EvtLogLastWriteTime
 **const win32evtlog\.EvtLogLastWriteTime;** 


## EvtLogNumberOfLogRecords
 **const win32evtlog\.EvtLogNumberOfLogRecords;** 


## EvtLogOldestRecordNumber
 **const win32evtlog\.EvtLogOldestRecordNumber;** 


## [win32evtlog](#win32evtlog)\.EvtNext

\([PyEVT\_HANDLE](PyEVT.md#pyevthandle),\.\.\.\) \= **EvtNext\( *ResultSet*  *, Count*  *, Timeout*  *, Flags* ** \)
Returns events from a query

#### Parameters


  -  *ResultSet* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to event query or subscription

  -  *Count* : int

    Number of events to return

  -  *Timeout\=-1* : int

    Time to wait in milliseconds, use -1 for infinite

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

#### Return Value
Returns a tuple of handles to events\.  If no items are available, returns 

an empty tuple instead of raising an exception\.

## [win32evtlog](#win32evtlog)\.EvtNextChannelPath

str \= **EvtNextChannelPath\( *ChannelEnum* ** \)
Retrieves a channel path from an enumeration

#### Parameters


  -  *ChannelEnum* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an enumeration as returned by[win32evtlog::EvtOpenChannelEnum](win32evtlog.md#win32evtlogevtopenchannelenum)

#### Comments
Accepts keyword args

#### Return Value
Returns None at end of enumeration

## [win32evtlog](#win32evtlog)\.EvtNextEventMetadata

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtNextEventMetadata\( *EventMetadataEnum*  *, Flags* ** \)
Retrieves the next item from an event metadata enumeration

#### Parameters


  -  *EventMetadataEnum* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Enumeration handle as returned by[win32evtlog::EvtOpenEventMetadataEnum](win32evtlog.md#win32evtlogevtopeneventmetadataenum)

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtNextPublisherId

str \= **EvtNextPublisherId\( *PublisherEnum* ** \)
Returns the next publisher from an enumeration

#### Parameters


  -  *PublisherEnum* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an enumeration as returned by[win32evtlog::EvtOpenPublisherEnum](win32evtlog.md#win32evtlogevtopenpublisherenum)

#### Comments
Accepts keyword args

#### Return Value
Returns None at end of enumeration

## [win32evtlog](#win32evtlog)\.EvtOpenChannelConfig

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenChannelConfig\( *ChannelPath*  *, Session*  *, Flags* ** \)
Opens channel configuration

#### Parameters


  -  *ChannelPath* : str

    Channel to be opened

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Session handle as returned by[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession), or None for local machine

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtOpenChannelEnum

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenChannelEnum\( *Session*  *, Flags* ** \)
Begins an enumeration of event channels

#### Parameters


  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtOpenChannelPath
 **const win32evtlog\.EvtOpenChannelPath;** 


## [win32evtlog](#win32evtlog)\.EvtOpenEventMetadataEnum

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenEventMetadataEnum\( *PublisherMetadata*  *, Flags* ** \)
Enumerates the events that a publisher provides

#### Parameters


  -  *PublisherMetadata* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Publisher handle as returned by[win32evtlog::EvtOpenPublisherMetadata](win32evtlog.md#win32evtlogevtopenpublishermetadata)

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtOpenFilePath
 **const win32evtlog\.EvtOpenFilePath;** 


## [win32evtlog](#win32evtlog)\.EvtOpenLog

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenLog\( *Path*  *, Flags*  *, Session* ** \)
Opens an event log or exported log archive

#### Parameters


  -  *Path* : str

    Event log name or Path of an export file

  -  *Flags* : int

    EvtOpenChannelPath \(1\) or EvtOpenFilePath \(2\)

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtOpenPublisherEnum

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenPublisherEnum\( *Session*  *, Flags* ** \)
Begins an enumeration of event publishers

#### Parameters


  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtOpenPublisherMetadata

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenPublisherMetadata\( *PublisherIdentity*  *, Session*  *, LogFilePath*  *, Locale*  *, Flags* ** \)
Opens a publisher to retrieve properties using[win32evtlog::EvtGetPublisherMetadataProperty](win32evtlog.md#win32evtlogevtgetpublishermetadataproperty)

#### Parameters


  -  *PublisherIdentity* : str

    Publisher id as returned by[win32evtlog::EvtNextPublisherId](win32evtlog.md#win32evtlogevtnextpublisherid)

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to remote session, or None for local machine

  -  *LogFilePath\=None* : str

    Log file from which to retrieve publisher, or None for locally registered publisher

  -  *Locale\=0* : int

    Locale to use for retrieved properties, use 0 for current locale

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## [win32evtlog](#win32evtlog)\.EvtOpenSession

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtOpenSession\( *Login*  *, LoginClass*  *, Timeout*  *, Flags* ** \)
Creates a session used to access the Event Log on another machine

#### Parameters


  -  *Login* :[PyEVT\_RPC\_LOGIN](PyEVT.md#pyevtrpc_login)

    Credentials to be used to access remote machine

  -  *LoginClass\=EvtRpcLogin* : int

    Type of login to perform, EvtRpcLogin is only defined value

  -  *Timeout\=0* : int

    Reserved, use only 0

  -  *Flags\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtPublisherMetadataChannelReferenceFlags
 **const win32evtlog\.EvtPublisherMetadataChannelReferenceFlags;** 


## EvtPublisherMetadataChannelReferenceID
 **const win32evtlog\.EvtPublisherMetadataChannelReferenceID;** 


## EvtPublisherMetadataChannelReferenceIndex
 **const win32evtlog\.EvtPublisherMetadataChannelReferenceIndex;** 


## EvtPublisherMetadataChannelReferenceMessageID
 **const win32evtlog\.EvtPublisherMetadataChannelReferenceMessageID;** 


## EvtPublisherMetadataChannelReferencePath
 **const win32evtlog\.EvtPublisherMetadataChannelReferencePath;** 


## EvtPublisherMetadataChannelReferences
 **const win32evtlog\.EvtPublisherMetadataChannelReferences;** 


## EvtPublisherMetadataHelpLink
 **const win32evtlog\.EvtPublisherMetadataHelpLink;** 


## EvtPublisherMetadataKeywordMessageID
 **const win32evtlog\.EvtPublisherMetadataKeywordMessageID;** 


## EvtPublisherMetadataKeywordName
 **const win32evtlog\.EvtPublisherMetadataKeywordName;** 


## EvtPublisherMetadataKeywordValue
 **const win32evtlog\.EvtPublisherMetadataKeywordValue;** 


## EvtPublisherMetadataKeywords
 **const win32evtlog\.EvtPublisherMetadataKeywords;** 


## EvtPublisherMetadataLevelMessageID
 **const win32evtlog\.EvtPublisherMetadataLevelMessageID;** 


## EvtPublisherMetadataLevelName
 **const win32evtlog\.EvtPublisherMetadataLevelName;** 


## EvtPublisherMetadataLevelValue
 **const win32evtlog\.EvtPublisherMetadataLevelValue;** 


## EvtPublisherMetadataLevels
 **const win32evtlog\.EvtPublisherMetadataLevels;** 


## EvtPublisherMetadataMessageFilePath
 **const win32evtlog\.EvtPublisherMetadataMessageFilePath;** 


## EvtPublisherMetadataOpcodeMessageID
 **const win32evtlog\.EvtPublisherMetadataOpcodeMessageID;** 


## EvtPublisherMetadataOpcodeName
 **const win32evtlog\.EvtPublisherMetadataOpcodeName;** 


## EvtPublisherMetadataOpcodeValue
 **const win32evtlog\.EvtPublisherMetadataOpcodeValue;** 


## EvtPublisherMetadataOpcodes
 **const win32evtlog\.EvtPublisherMetadataOpcodes;** 


## EvtPublisherMetadataParameterFilePath
 **const win32evtlog\.EvtPublisherMetadataParameterFilePath;** 


## EvtPublisherMetadataPropertyIdEND
 **const win32evtlog\.EvtPublisherMetadataPropertyIdEND;** 


## EvtPublisherMetadataPublisherGuid
 **const win32evtlog\.EvtPublisherMetadataPublisherGuid;** 


## EvtPublisherMetadataPublisherMessageID
 **const win32evtlog\.EvtPublisherMetadataPublisherMessageID;** 


## EvtPublisherMetadataResourceFilePath
 **const win32evtlog\.EvtPublisherMetadataResourceFilePath;** 


## EvtPublisherMetadataTaskEventGuid
 **const win32evtlog\.EvtPublisherMetadataTaskEventGuid;** 


## EvtPublisherMetadataTaskMessageID
 **const win32evtlog\.EvtPublisherMetadataTaskMessageID;** 


## EvtPublisherMetadataTaskName
 **const win32evtlog\.EvtPublisherMetadataTaskName;** 


## EvtPublisherMetadataTaskValue
 **const win32evtlog\.EvtPublisherMetadataTaskValue;** 


## EvtPublisherMetadataTasks
 **const win32evtlog\.EvtPublisherMetadataTasks;** 


## [win32evtlog](#win32evtlog)\.EvtQuery

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtQuery\( *Path*  *, Flags*  *, Query*  *, Session* ** \)
Opens a query over a log channel or exported log file

#### Parameters


  -  *Path* : str

    Log channel or exported log file, depending on Flags

  -  *Flags* : int

    Combination of EVT\_QUERY\_FLAGS \(EvtQuery\*\)

  -  *Query\=None* : str

    Selects events to return, None or '\*' for all events

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a remote session \(see[win32evtlog::EvtOpenSession](win32evtlog.md#win32evtlogevtopensession)\), or None for local machine\.

#### Comments
Accepts keyword args

## EvtQueryChannelPath
 **const win32evtlog\.EvtQueryChannelPath;** 


## EvtQueryFilePath
 **const win32evtlog\.EvtQueryFilePath;** 


## EvtQueryForwardDirection
 **const win32evtlog\.EvtQueryForwardDirection;** 


## EvtQueryReverseDirection
 **const win32evtlog\.EvtQueryReverseDirection;** 


## EvtQueryTolerateQueryErrors
 **const win32evtlog\.EvtQueryTolerateQueryErrors;** 


## [win32evtlog](#win32evtlog)\.EvtRender

str \= **EvtRender\( *Event*  *, Flags* ** \)
Formats an event into XML text

#### Parameters


  -  *Event* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an event or bookmark

  -  *Flags* : int

    EvtRenderEventXml or EvtRenderBookmark indicating type of handle

#### Comments
Accepts keyword args
Rendering event values \(Flags\=EvtRenderEventValues\) is not currently supported

## EvtRenderBookmark
 **const win32evtlog\.EvtRenderBookmark;** 


## EvtRenderEventValues
 **const win32evtlog\.EvtRenderEventValues;** 


## EvtRenderEventXml
 **const win32evtlog\.EvtRenderEventXml;** 


## EvtRpcLogin
 **const win32evtlog\.EvtRpcLogin;** 


## EvtRpcLoginAuthDefault
 **const win32evtlog\.EvtRpcLoginAuthDefault;** 


## EvtRpcLoginAuthKerberos
 **const win32evtlog\.EvtRpcLoginAuthKerberos;** 


## EvtRpcLoginAuthNTLM
 **const win32evtlog\.EvtRpcLoginAuthNTLM;** 


## EvtRpcLoginAuthNegotiate
 **const win32evtlog\.EvtRpcLoginAuthNegotiate;** 


## [win32evtlog](#win32evtlog)\.EvtSeek

 **EvtSeek\( *ResultSet*  *, Position*  *, Flags*  *, Bookmark*  *, Timeout* ** \)
Changes the current position in a result set

#### Parameters


  -  *ResultSet* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to event query or subscription

  -  *Position* : int

    Offset \(base from which to seek is specified by Flags\)

  -  *Flags* : int

    EvtSeekRelative\* flag indicating seek origin

  -  *Bookmark\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Used as seek origin only if Flags contains EvtSeekRelativeToBookmark

  -  *Timeout\=0* : int

    Reserved, use only 0

#### Comments
Accepts keyword args

## EvtSeekOriginMask
 **const win32evtlog\.EvtSeekOriginMask;** 


## EvtSeekRelativeToBookmark
 **const win32evtlog\.EvtSeekRelativeToBookmark;** 


## EvtSeekRelativeToCurrent
 **const win32evtlog\.EvtSeekRelativeToCurrent;** 


## EvtSeekRelativeToFirst
 **const win32evtlog\.EvtSeekRelativeToFirst;** 


## EvtSeekRelativeToLast
 **const win32evtlog\.EvtSeekRelativeToLast;** 


## EvtSeekStrict
 **const win32evtlog\.EvtSeekStrict;** 


## [win32evtlog](#win32evtlog)\.EvtSubscribe

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtSubscribe\( *ChannelPath*  *, Flags*  *, SignalEvent*  *, Callback*  *, Context*  *, Query*  *, Session*  *, Bookmark* ** \)
Requests notification for events

#### Parameters


  -  *ChannelPath* : str

    Name of an event log channel

  -  *Flags* : int

    Combination of EvtSubscribe\* flags determining how subscription is initiated

  -  *SignalEvent\=None* : **Py\_HANDLE** 

    An event handle to be set when events are available \(see[win32event::CreateEvent](win32event.md#win32eventcreateevent)\)

  -  *Callback\=None* : function

    Python function to be called with each event

  -  *Context\=None* : object

    Arbitrary object to be passed to the callback function

  -  *Query\=None* : str

    XML query used to select specific events, use None or '\*' for all events

  -  *Session\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a session on another machine, or None for local

  -  *Bookmark\=None* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    If Flags contains EvtSubscribeStartAfterBookmark, used as starting point

#### Comments
Accepts keyword args
The method used to receive events is determined by the parameters passed in\. 

To create a push subscription, define a callback function that will be called with each event\. 

The function will receive 3 args: 

First is an integer specifying why the function was called \(EvtSubscribeActionError or EvtSubscribeActionDeliver\) 

Second is the context object passed to EvtSubscribe\. 

Third is the handle to an event log record \(if not called due to an error\) 

If an event handle is passed in, a pull subscription is created\.  The event handle will be 

signalled when events are available, and the subscription handle can be 

passed to[win32evtlog::EvtNext](win32evtlog.md#win32evtlogevtnext)to obtain the events\.

## EvtSubscribeActionDeliver
 **const win32evtlog\.EvtSubscribeActionDeliver;** 


## EvtSubscribeActionError
 **const win32evtlog\.EvtSubscribeActionError;** 


## EvtSubscribeOriginMask
 **const win32evtlog\.EvtSubscribeOriginMask;** 


## EvtSubscribeStartAfterBookmark
 **const win32evtlog\.EvtSubscribeStartAfterBookmark;** 


## EvtSubscribeStartAtOldestRecord
 **const win32evtlog\.EvtSubscribeStartAtOldestRecord;** 


## EvtSubscribeStrict
 **const win32evtlog\.EvtSubscribeStrict;** 


## EvtSubscribeToFutureEvents
 **const win32evtlog\.EvtSubscribeToFutureEvents;** 


## EvtSubscribeTolerateQueryErrors
 **const win32evtlog\.EvtSubscribeTolerateQueryErrors;** 


## [win32evtlog](#win32evtlog)\.EvtUpdateBookmark

[PyEVT\_HANDLE](PyEVT.md#pyevthandle)\= **EvtUpdateBookmark\( *Bookmark*  *, Event* ** \)
Repositions a bookmark to an event

#### Parameters


  -  *Bookmark* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to a bookmark

  -  *Event* :[PyEVT\_HANDLE](PyEVT.md#pyevthandle)

    Handle to an event

#### Comments
Accepts keyword args

## EvtVarTypeAnsiString
 **const win32evtlog\.EvtVarTypeAnsiString;** 


## EvtVarTypeBinary
 **const win32evtlog\.EvtVarTypeBinary;** 


## EvtVarTypeBoolean
 **const win32evtlog\.EvtVarTypeBoolean;** 


## EvtVarTypeByte
 **const win32evtlog\.EvtVarTypeByte;** 


## EvtVarTypeDouble
 **const win32evtlog\.EvtVarTypeDouble;** 


## EvtVarTypeEvtHandle
 **const win32evtlog\.EvtVarTypeEvtHandle;** 


## EvtVarTypeEvtXml
 **const win32evtlog\.EvtVarTypeEvtXml;** 


## EvtVarTypeFileTime
 **const win32evtlog\.EvtVarTypeFileTime;** 


## EvtVarTypeGuid
 **const win32evtlog\.EvtVarTypeGuid;** 


## EvtVarTypeHexInt32
 **const win32evtlog\.EvtVarTypeHexInt32;** 


## EvtVarTypeHexInt64
 **const win32evtlog\.EvtVarTypeHexInt64;** 


## EvtVarTypeInt16
 **const win32evtlog\.EvtVarTypeInt16;** 


## EvtVarTypeInt32
 **const win32evtlog\.EvtVarTypeInt32;** 


## EvtVarTypeInt64
 **const win32evtlog\.EvtVarTypeInt64;** 


## EvtVarTypeNull
 **const win32evtlog\.EvtVarTypeNull;** 


## EvtVarTypeSByte
 **const win32evtlog\.EvtVarTypeSByte;** 


## EvtVarTypeSid
 **const win32evtlog\.EvtVarTypeSid;** 


## EvtVarTypeSingle
 **const win32evtlog\.EvtVarTypeSingle;** 


## EvtVarTypeSizeT
 **const win32evtlog\.EvtVarTypeSizeT;** 


## EvtVarTypeString
 **const win32evtlog\.EvtVarTypeString;** 


## EvtVarTypeSysTime
 **const win32evtlog\.EvtVarTypeSysTime;** 


## EvtVarTypeUInt16
 **const win32evtlog\.EvtVarTypeUInt16;** 


## EvtVarTypeUInt32
 **const win32evtlog\.EvtVarTypeUInt32;** 


## EvtVarTypeUInt64
 **const win32evtlog\.EvtVarTypeUInt64;** 


## [win32evtlog](#win32evtlog)\.GetNumberOfEventLogRecords

int \= **GetNumberOfEventLogRecords\( *handle* ** \)
Returns the number of event log records\.

#### Parameters


  -  *handle* : int

    Handle to the event log to query\.

## [win32evtlog](#win32evtlog)\.GetOldestEventLogRecord

int \= **GetOldestEventLogRecord\(** \)
Returns the number of event log records\.

#### Return Value
The result is the absolute record number of the oldest record in the given event log\.

## [win32evtlog](#win32evtlog)\.NotifyChangeEventLog

 **NotifyChangeEventLog\( *handle*  *, handle* ** \)
Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter\. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled\.

#### Parameters


  -  *handle* : int

    Handle to an event log file, obtained by calling[win32evtlog::OpenEventLog](win32evtlog.md#win32evtlogopeneventlog)function\. When an event is written to this log file, the event specified by hEvent becomes signaled\.

  -  *handle* : int

    A handle to a Win32 event\. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter\.

## [win32evtlog](#win32evtlog)\.OpenBackupEventLog

[PyEVTLOG\_HANDLE](PyEVTLOG.md#pyevtloghandle)\= **OpenBackupEventLog\( *serverName*  *, fileName* ** \)
Opens a previously saved event log\.

#### Parameters


  -  *serverName* :[PyUnicode](#pyunicode)

    The server name, or None

  -  *fileName* :[PyUnicode](#pyunicode)

    The filename to open

## [win32evtlog](#win32evtlog)\.OpenEventLog

[PyEVTLOG\_HANDLE](PyEVTLOG.md#pyevtloghandle)\= **OpenEventLog\( *serverName*  *, sourceName* ** \)
Opens an event log\.

#### Parameters


  -  *serverName* :[PyUnicode](#pyunicode)

    The server name, or None

  -  *sourceName* :[PyUnicode](#pyunicode)

    specifies the name of the source that the returned handle will reference\. The source name must be a subkey of a logfile entry under the EventLog key in the registry\.

## [win32evtlog](#win32evtlog)\.ReadEventLog

\[object,\.\.\.\] \= **ReadEventLog\( *Handle*  *, Flags*  *, Offset*  *, Size* ** \)
Reads some event log records\.

#### Parameters


  -  *Handle* : **Py\_HANDLE** 

    Handle to a an opened event log \(see[win32evtlog::OpenEventLog](win32evtlog.md#win32evtlogopeneventlog)\)

  -  *Flags* : int

    Reading flags

  -  *Offset* : int

    Record offset to read \(in SEEK mode\)\.

  -  *Size\=4096* : int

    Output buffer size\.

#### Return Value
If there are no event log records available, then an empty list is returned\.

## [win32evtlog](#win32evtlog)\.RegisterEventSource

int \= **RegisterEventSource\( *serverName*  *, sourceName* ** \)
Registers an Event Source

#### Parameters


  -  *serverName* :[PyUnicode](#pyunicode)

    The server name, or None

  -  *sourceName* :[PyUnicode](#pyunicode)

    The source name

## [win32evtlog](#win32evtlog)\.ReportEvent

 **ReportEvent\( *EventLog*  *, Type*  *, Category*  *, EventID*  *, UserSid*  *, Strings*  *, RawData* ** \)
Reports an event

#### Parameters


  -  *EventLog* :[PyHANDLE](#pyhandle)

    Handle to an event log

  -  *Type* : int

    win32con\.EVENTLOG\_\* value

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