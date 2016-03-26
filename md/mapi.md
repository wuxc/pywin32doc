# mapi

## Module mapi

A COM interface to MAPI

#### Methods


  - [HexFromBin](mapi.md#mapihexfrombin)

    converts a binary number into a string representation of a hexadecimal number\.&nbsp;

  - [BinFromHex](mapi.md#mapibinfromhex)

    converts a hexadecimal number into a binary string&nbsp;

  - [MAPIUninitialize](mapi.md#mapimapiuninitialize)

    Decrements the reference count, cleans up, and deletes per-instance global data for the MAPI DLL\.&nbsp;

  - [MAPIInitialize](mapi.md#mapimapiinitialize)

    Increments the MAPI subsystem reference count and initializes global data for the MAPI DLL\.&nbsp;

  - [MAPILogonEx](mapi.md#mapimapilogonex)

    &nbsp;

  - [MAPIAdminProfiles](mapi.md#mapimapiadminprofiles)

    &nbsp;

  - [HrQueryAllRows](mapi.md#mapihrqueryallrows)

    &nbsp;

  - [RTFSync](mapi.md#mapirtfsync)

    &nbsp;

  - [WrapCompressedRTFStream](mapi.md#mapiwrapcompressedrtfstream)

    &nbsp;

  - [OpenIMsgSession](mapi.md#mapiopenimsgsession)

    &nbsp;

  - [CloseIMsgSession](mapi.md#mapicloseimsgsession)

    &nbsp;

  - [OpenIMsgOnIStg](mapi.md#mapiopenimsgonistg)

    Builds a new IMessage object on top of an existing OLE IStorage object, to be used within a message session\.&nbsp;

  - [RTFStreamToHTML](mapi.md#mapirtfstreamtohtml)

    &nbsp;

  - [OpenStreamOnFile](mapi.md#mapiopenstreamonfile)

    Allocates and initializes an OLE IStream object to access the contents of a file\.&nbsp;

  - [HrGetOneProp](mapi.md#mapihrgetoneprop)

    Retrieves the value of a single property from an IMAPIProp object\.&nbsp;

  - [HrSetOneProp](mapi.md#mapihrsetoneprop)

    Sets the value of a single property on a IMAPIProp object\.&nbsp;

## AB\_NO\_DIALOG
 **const mapi\.AB\_NO\_DIALOG;** 


## ATTACH\_BY\_REFERENCE
 **const mapi\.ATTACH\_BY\_REFERENCE;** 
The PR\_ATTACH\_PATHNAME or PR\_ATTACH\_LONG\_PATHNAME property contains a fully qualified path identifying the attachment to recipients with access to a common file server\.

## ATTACH\_BY\_REF\_ONLY
 **const mapi\.ATTACH\_BY\_REF\_ONLY;** 
The PR\_ATTACH\_PATHNAME or PR\_ATTACH\_LONG\_PATHNAME property contains a fully qualified path identifying the attachment\.

## ATTACH\_BY\_REF\_RESOLVE
 **const mapi\.ATTACH\_BY\_REF\_RESOLVE;** 
The PR\_ATTACH\_PATHNAME or PR\_ATTACH\_LONG\_PATHNAME property contains a fully qualified path identifying the attachment\.

## ATTACH\_BY\_VALUE
 **const mapi\.ATTACH\_BY\_VALUE;** 
The PR\_ATTACH\_DATA\_BIN property contains the attachment data\.

## ATTACH\_EMBEDDED\_MSG
 **const mapi\.ATTACH\_EMBEDDED\_MSG;** 
The PR\_ATTACH\_DATA\_OBJ property contains an embedded object that supports the IMessage interface\.

## ATTACH\_OLE
 **const mapi\.ATTACH\_OLE;** 
The attachment is an embedded OLE object

## BMR\_EQZ
 **const mapi\.BMR\_EQZ;** 
Perform a bitwise AND operation of the mask in the ulMask member with the property represented by the ulPropTag member and test for being equal to zero\.

## BMR\_NEZ
 **const mapi\.BMR\_NEZ;** 
Perform a bitwise AND operation of the mask in the ulMask member with the property represented by the ulPropTag member and test for being not equal to zero\.

## BOOKMARK\_BEGINNING
 **const mapi\.BOOKMARK\_BEGINNING;** 
Starts the seek operation from the beginning of the table\.

## BOOKMARK\_CURRENT
 **const mapi\.BOOKMARK\_CURRENT;** 
Starts the seek operation from the row in the table where the cursor is located\.

## BOOKMARK\_END
 **const mapi\.BOOKMARK\_END;** 
Starts the seek operation from the end of the table\.

## [mapi](#mapi)\.BinFromHex

[PyUnicode](#pyunicode)\= **BinFromHex\( *val* ** \)
converts a hexadecimal number into a binary string

#### Parameters


  -  *val* : string/[PyUnicode](#pyunicode)

    The string to be converted\.

## CCSF\_8BITHEADERS
 **const mapi\.CCSF\_8BITHEADERS;** 
the converter should allow 8 bit headers

## CCSF\_EMBEDDED\_MESSAGE
 **const mapi\.CCSF\_EMBEDDED\_MESSAGE;** 
sent/unsent information is persisted in X-Unsent

## CCSF\_INCLUDE\_BCC
 **const mapi\.CCSF\_INCLUDE\_BCC;** 
the converter should include Bcc recipients

## CCSF\_NOHEADERS
 **const mapi\.CCSF\_NOHEADERS;** 
the converter should ignore the headers on the outside message

## CCSF\_NO\_MSGID
 **const mapi\.CCSF\_NO\_MSGID;** 
don't include Message-Id field in outgoing messages

## CCSF\_PLAIN\_TEXT\_ONLY
 **const mapi\.CCSF\_PLAIN\_TEXT\_ONLY;** 
the converter should just send plain text

## CCSF\_PRESERVE\_SOURCE
 **const mapi\.CCSF\_PRESERVE\_SOURCE;** 
don't modify the source message

## CCSF\_SMTP
 **const mapi\.CCSF\_SMTP;** 
the converter is being passed an SMTP message

## CCSF\_USE\_RTF
 **const mapi\.CCSF\_USE\_RTF;** 
the converter should do HTML-&gtRTF conversion

## CCSF\_USE\_TNEF
 **const mapi\.CCSF\_USE\_TNEF;** 
the converter should embed TNEF in the MIME message

## CONVENIENT\_DEPTH
 **const mapi\.CONVENIENT\_DEPTH;** 
Fills the hierarchy table with containers from multiple levels\. If CONVENIENT\_DEPTH is not set, the hierarchy table contains only the container's immediate child containers\.

## [mapi](#mapi)\.CloseIMsgSession

 **CloseIMsgSession\(** \)


## DELETE\_HARD\_DELETE
 **const mapi\.DELETE\_HARD\_DELETE;** 
Permanently removes all messages, including soft-deleted ones\.

## DEL\_FOLDERS
 **const mapi\.DEL\_FOLDERS;** 
All subfolders of the subfolder pointed to by lpEntryID should be deleted\.

## DEL\_MESSAGES
 **const mapi\.DEL\_MESSAGES;** 
All messages in the subfolder pointed to by lpEntryID should be deleted\.

## DIR\_BACKWARD
 **const mapi\.DIR\_BACKWARD;** 
Searches backward from the row identified by the bookmark\.

## FLUSH\_ASYNC\_OK
 **const mapi\.FLUSH\_ASYNC\_OK;** 


## FLUSH\_DOWNLOAD
 **const mapi\.FLUSH\_DOWNLOAD;** 


## FLUSH\_FORCE
 **const mapi\.FLUSH\_FORCE;** 


## FLUSH\_NO\_UI
 **const mapi\.FLUSH\_NO\_UI;** 


## FLUSH\_UPLOAD
 **const mapi\.FLUSH\_UPLOAD;** 


## FL\_FULLSTRING
 **const mapi\.FL\_FULLSTRING;** 
To match, the lpProp search string must be completely contained in the property identified by ulPropTag\.

## FL\_IGNORECASE
 **const mapi\.FL\_IGNORECASE;** 
The comparison should be made without considering case\.

## FL\_IGNORENONSPACE
 **const mapi\.FL\_IGNORENONSPACE;** 
The comparison should ignore Unicode-defined nonspacing characters such as diacritical marks\.

## FL\_LOOSE
 **const mapi\.FL\_LOOSE;** 
The comparison should result in a match whenever possible, ignoring case and nonspacing characters

## FL\_PREFIX
 **const mapi\.FL\_PREFIX;** 
To match, the lpProp search string must appear at the beginning of the property identified by ulPropTag\. The two strings should be compared only up to the length of the search string indicated by lpProp\.

## FL\_SUBSTRING
 **const mapi\.FL\_SUBSTRING;** 
To match, the lpProp search string must be contained anywhere within the property identified by ulPropTag\.

## FOLDER\_DIALOG
 **const mapi\.FOLDER\_DIALOG;** 
A progress indicator should be displayed while the operation proceeds\.

## FOLDER\_GENERIC
 **const mapi\.FOLDER\_GENERIC;** 
A generic folder should be created\.

## FOLDER\_SEARCH
 **const mapi\.FOLDER\_SEARCH;** 
A search-results folder should be created\.

## FORCE\_SAVE
 **const mapi\.FORCE\_SAVE;** 
Changes should be written to the object, overriding any previous changes made to the object, and the object closed\. Read/write access must have been set for the operation to succeed\. The FORCE\_SAVE flag is used after a previous call to SaveChanges returned MAPI\_E\_OBJECT\_CHANGED\.

## [mapi](#mapi)\.HexFromBin

[PyUnicode](#pyunicode)\= **HexFromBin\( *val* ** \)
converts a binary number into a string representation of a hexadecimal number\.

#### Parameters


  -  *val* : string

    Converts an EntryID into a hex string representation\.

#### Comments
Note: This function may not be supported in future versions of MAPI\.

## [mapi](#mapi)\.HrGetOneProp

item \= **HrGetOneProp\( *prop*  *, propTag* ** \)
Retrieves the value of a single property from an IMAPIProp object\.

#### Parameters


  -  *prop* :[PyIMAPIProp](#pyimapiprop)

    Object to retrieve property value from\.

  -  *propTag* : ULONG

    The property tag to open\.

## [mapi](#mapi)\.HrQueryAllRows

 **SRowSet** \= **HrQueryAllRows\( *table*  *, properties*  *, restrictions*  *, sortOrderSet*  *, rowsMax* ** \)


#### Parameters


  -  *table* :[PyIMAPITable](#pyimapitable)

    

  -  *properties* :[PySPropTagArray](#pysproptagarray)

    A sequence of property tags indicating table columns\. These tags are used to select the specific columns to be retrieved\. If this parameter is None, HrQueryAllRows retrieves the entire column set of the current table view passed in the table parameter\.

  -  *restrictions* :[PySRestriction](#pysrestriction)

    Defines the retrieval restrictions\. If this parameter is None, HrQueryAllRows makes no restrictions\.

  -  *sortOrderSet* :[PySSortOrderSet](#pyssortorderset)

    Identifies the sort order of the columns to be retrieved\. If this parameter is None, the default sort order for the table is used\.

  -  *rowsMax* : int

    Maximum number of rows to be retrieved\. If the value of the rowsMax parameter is zero, no limit on the number of rows retrieved is set\.

## [mapi](#mapi)\.HrSetOneProp

item \= **HrSetOneProp\( *prop*  *, propValue* ** \)
Sets the value of a single property on a IMAPIProp object\.

#### Parameters


  -  *prop* :[PyIMAPIProp](#pyimapiprop)

    Object to set property value on\.

  -  *propValue* :[PySPropValue](#pyspropvalue)

    Property value to set\.

## KEEP\_OPEN\_READONLY
 **const mapi\.KEEP\_OPEN\_READONLY;** 
Changes should be committed and the object should be kept open for reading\. No further changes will be made\.

## KEEP\_OPEN\_READWRITE
 **const mapi\.KEEP\_OPEN\_READWRITE;** 
Changes should be committed and the object should be kept open for read/write access\. This flag is usually set when the object was initially opened for read/write access\. Subsequent changes to the object are allowed\.

## [mapi](#mapi)\.MAPIAdminProfiles

 **PyIProfAdmin** \= **MAPIAdminProfiles\( *fFlags* ** \)


#### Parameters


  -  *fFlags* : int

    

## [mapi](#mapi)\.MAPIInitialize

 **MAPIInitialize\( *init* ** \)
Increments the MAPI subsystem reference count and initializes global data for the MAPI DLL\.

#### Parameters


  -  *init* :[MAPIINIT\_0](MAPIINIT.md#mapiinit0)

    MAPI Initialization flags\.

## [mapi](#mapi)\.MAPILogonEx

[PyIMAPISession](#pyimapisession)\= **MAPILogonEx\( *hWnd*  *, profileName*  *, password*  *, uiFlags* ** \)


#### Parameters


  -  *hWnd* : int

    Handle to the window to which the logon dialog box is modal\. If no dialog box is displayed during the call, the hWnd parameter is ignored\. This parameter can be zero\.

  -  *profileName* :[PyUnicode](#pyunicode)

    A string containing the name of the profile to use when logging on\. This string is limited to 64 characters\.

  -  *password* :[PyUnicode](#pyunicode)

    A string containing the password of the profile\. This parameter can be None whether or not the profileName parameter is None\. This string is limited to 64 characters\.

  -  *uiFlags* : int

    Bitmask of flags used to control how logon is performed\.  See the MAPI documentation for details\.

## [mapi](#mapi)\.MAPIUninitialize

 **MAPIUninitialize\(** \)
Decrements the reference count, cleans up, and deletes per-instance global data for the MAPI DLL\.

## MAPI\_ALLOW\_OTHERS
 **const mapi\.MAPI\_ALLOW\_OTHERS;** 
The shared session should be returned, allowing subsequent clients to acquire the session without providing any user credentials\.

## MAPI\_ASSOCIATED
 **const mapi\.MAPI\_ASSOCIATED;** 
The container's associated contents table should be returned rather than the standard contents table\. This flag is used only with folders\. The messages that are included in the associated contents table were created with the MAPI\_ASSOCIATED flag set in the call to IMAPIFolder::CreateMessage\. Clients typically use the associated contents table to retrieve forms and views\.

## MAPI\_BCC
 **const mapi\.MAPI\_BCC;** 
The recipient is a blind carbon copy \(BCC\) recipient\. Primary and carbon copy recipients are unaware of the existence of BCC recipients\.

## MAPI\_BEST\_ACCESS
 **const mapi\.MAPI\_BEST\_ACCESS;** 


## MAPI\_CC
 **const mapi\.MAPI\_CC;** 
The recipient is a carbon copy \(CC\) recipient, a recipient that receives a message in addition to the primary recipients\.

## MAPI\_CREATE
 **const mapi\.MAPI\_CREATE;** 
The object will be created if necessary\.

## MAPI\_DEFAULT\_SERVICES
 **const mapi\.MAPI\_DEFAULT\_SERVICES;** 
MAPI should populate the new profile with the message services that are included in the \[Default Services\] section of the MAPISVC\.INF file\.

## MAPI\_DEFERRED\_ERRORS
 **const mapi\.MAPI\_DEFERRED\_ERRORS;** 
Allows a method to return successfully, possibly before the changes have been fully committed\.

## MAPI\_DIALOG
 **const mapi\.MAPI\_DIALOG;** 


## MAPI\_EXPLICIT\_PROFILE
 **const mapi\.MAPI\_EXPLICIT\_PROFILE;** 
The default profile should not be used, and the user should be required to supply a profile\.

## MAPI\_EXTENDED
 **const mapi\.MAPI\_EXTENDED;** 
Log on with extended capabilities\. This flag should always be set\. The older MAPILogon function is no longer available\.

## MAPI\_E\_ACCOUNT\_DISABLED
 **const mapi\.MAPI\_E\_ACCOUNT\_DISABLED;** 


## MAPI\_E\_AMBIGUOUS\_RECIP
 **const mapi\.MAPI\_E\_AMBIGUOUS\_RECIP;** 


## MAPI\_E\_BAD\_CHARWIDTH
 **const mapi\.MAPI\_E\_BAD\_CHARWIDTH;** 


## MAPI\_E\_BAD\_COLUMN
 **const mapi\.MAPI\_E\_BAD\_COLUMN;** 


## MAPI\_E\_BAD\_VALUE
 **const mapi\.MAPI\_E\_BAD\_VALUE;** 


## MAPI\_E\_BUSY
 **const mapi\.MAPI\_E\_BUSY;** 


## MAPI\_E\_CALL\_FAILED
 **const mapi\.MAPI\_E\_CALL\_FAILED;** 


## MAPI\_E\_CANCEL
 **const mapi\.MAPI\_E\_CANCEL;** 


## MAPI\_E\_COLLISION
 **const mapi\.MAPI\_E\_COLLISION;** 


## MAPI\_E\_COMPUTED
 **const mapi\.MAPI\_E\_COMPUTED;** 


## MAPI\_E\_CORRUPT\_DATA
 **const mapi\.MAPI\_E\_CORRUPT\_DATA;** 


## MAPI\_E\_CORRUPT\_STORE
 **const mapi\.MAPI\_E\_CORRUPT\_STORE;** 


## MAPI\_E\_DECLINE\_COPY
 **const mapi\.MAPI\_E\_DECLINE\_COPY;** 


## MAPI\_E\_DISK\_ERROR
 **const mapi\.MAPI\_E\_DISK\_ERROR;** 


## MAPI\_E\_END\_OF\_SESSION
 **const mapi\.MAPI\_E\_END\_OF\_SESSION;** 


## MAPI\_E\_EXTENDED\_ERROR
 **const mapi\.MAPI\_E\_EXTENDED\_ERROR;** 


## MAPI\_E\_FAILONEPROVIDER
 **const mapi\.MAPI\_E\_FAILONEPROVIDER;** 


## MAPI\_E\_FOLDER\_CYCLE
 **const mapi\.MAPI\_E\_FOLDER\_CYCLE;** 


## MAPI\_E\_HAS\_FOLDERS
 **const mapi\.MAPI\_E\_HAS\_FOLDERS;** 


## MAPI\_E\_HAS\_MESSAGES
 **const mapi\.MAPI\_E\_HAS\_MESSAGES;** 


## MAPI\_E\_INTERFACE\_NOT\_SUPPORTED
 **const mapi\.MAPI\_E\_INTERFACE\_NOT\_SUPPORTED;** 


## MAPI\_E\_INVALID\_ACCESS\_TIME
 **const mapi\.MAPI\_E\_INVALID\_ACCESS\_TIME;** 


## MAPI\_E\_INVALID\_BOOKMARK
 **const mapi\.MAPI\_E\_INVALID\_BOOKMARK;** 


## MAPI\_E\_INVALID\_ENTRYID
 **const mapi\.MAPI\_E\_INVALID\_ENTRYID;** 


## MAPI\_E\_INVALID\_OBJECT
 **const mapi\.MAPI\_E\_INVALID\_OBJECT;** 


## MAPI\_E\_INVALID\_PARAMETER
 **const mapi\.MAPI\_E\_INVALID\_PARAMETER;** 


## MAPI\_E\_INVALID\_TYPE
 **const mapi\.MAPI\_E\_INVALID\_TYPE;** 


## MAPI\_E\_INVALID\_WORKSTATION\_ACCOUNT
 **const mapi\.MAPI\_E\_INVALID\_WORKSTATION\_ACCOUNT;** 


## MAPI\_E\_LOGON\_FAILED
 **const mapi\.MAPI\_E\_LOGON\_FAILED;** 


## MAPI\_E\_MISSING\_REQUIRED\_COLUMN
 **const mapi\.MAPI\_E\_MISSING\_REQUIRED\_COLUMN;** 


## MAPI\_E\_NETWORK\_ERROR
 **const mapi\.MAPI\_E\_NETWORK\_ERROR;** 


## MAPI\_E\_NON\_STANDARD
 **const mapi\.MAPI\_E\_NON\_STANDARD;** 


## MAPI\_E\_NOT\_ENOUGH\_DISK
 **const mapi\.MAPI\_E\_NOT\_ENOUGH\_DISK;** 


## MAPI\_E\_NOT\_ENOUGH\_MEMORY
 **const mapi\.MAPI\_E\_NOT\_ENOUGH\_MEMORY;** 


## MAPI\_E\_NOT\_ENOUGH\_RESOURCES
 **const mapi\.MAPI\_E\_NOT\_ENOUGH\_RESOURCES;** 


## MAPI\_E\_NOT\_FOUND
 **const mapi\.MAPI\_E\_NOT\_FOUND;** 


## MAPI\_E\_NOT\_INITIALIZED
 **const mapi\.MAPI\_E\_NOT\_INITIALIZED;** 


## MAPI\_E\_NOT\_IN\_QUEUE
 **const mapi\.MAPI\_E\_NOT\_IN\_QUEUE;** 


## MAPI\_E\_NOT\_ME
 **const mapi\.MAPI\_E\_NOT\_ME;** 


## MAPI\_E\_NO\_ACCESS
 **const mapi\.MAPI\_E\_NO\_ACCESS;** 


## MAPI\_E\_NO\_RECIPIENTS
 **const mapi\.MAPI\_E\_NO\_RECIPIENTS;** 


## MAPI\_E\_NO\_SUPPORT
 **const mapi\.MAPI\_E\_NO\_SUPPORT;** 


## MAPI\_E\_NO\_SUPPRESS
 **const mapi\.MAPI\_E\_NO\_SUPPRESS;** 


## MAPI\_E\_OBJECT\_CHANGED
 **const mapi\.MAPI\_E\_OBJECT\_CHANGED;** 


## MAPI\_E\_OBJECT\_DELETED
 **const mapi\.MAPI\_E\_OBJECT\_DELETED;** 


## MAPI\_E\_PASSWORD\_CHANGE\_REQUIRED
 **const mapi\.MAPI\_E\_PASSWORD\_CHANGE\_REQUIRED;** 


## MAPI\_E\_PASSWORD\_EXPIRED
 **const mapi\.MAPI\_E\_PASSWORD\_EXPIRED;** 


## MAPI\_E\_SESSION\_LIMIT
 **const mapi\.MAPI\_E\_SESSION\_LIMIT;** 


## MAPI\_E\_STRING\_TOO\_LONG
 **const mapi\.MAPI\_E\_STRING\_TOO\_LONG;** 


## MAPI\_E\_SUBMITTED
 **const mapi\.MAPI\_E\_SUBMITTED;** 


## MAPI\_E\_TABLE\_EMPTY
 **const mapi\.MAPI\_E\_TABLE\_EMPTY;** 


## MAPI\_E\_TABLE\_TOO\_BIG
 **const mapi\.MAPI\_E\_TABLE\_TOO\_BIG;** 


## MAPI\_E\_TIMEOUT
 **const mapi\.MAPI\_E\_TIMEOUT;** 


## MAPI\_E\_TOO\_BIG
 **const mapi\.MAPI\_E\_TOO\_BIG;** 


## MAPI\_E\_TOO\_COMPLEX
 **const mapi\.MAPI\_E\_TOO\_COMPLEX;** 


## MAPI\_E\_TYPE\_NO\_SUPPORT
 **const mapi\.MAPI\_E\_TYPE\_NO\_SUPPORT;** 


## MAPI\_E\_UNABLE\_TO\_ABORT
 **const mapi\.MAPI\_E\_UNABLE\_TO\_ABORT;** 


## MAPI\_E\_UNABLE\_TO\_COMPLETE
 **const mapi\.MAPI\_E\_UNABLE\_TO\_COMPLETE;** 


## MAPI\_E\_UNCONFIGURED
 **const mapi\.MAPI\_E\_UNCONFIGURED;** 


## MAPI\_E\_UNEXPECTED\_ID
 **const mapi\.MAPI\_E\_UNEXPECTED\_ID;** 


## MAPI\_E\_UNEXPECTED\_TYPE
 **const mapi\.MAPI\_E\_UNEXPECTED\_TYPE;** 


## MAPI\_E\_UNKNOWN\_CPID
 **const mapi\.MAPI\_E\_UNKNOWN\_CPID;** 


## MAPI\_E\_UNKNOWN\_ENTRYID
 **const mapi\.MAPI\_E\_UNKNOWN\_ENTRYID;** 


## MAPI\_E\_UNKNOWN\_FLAGS
 **const mapi\.MAPI\_E\_UNKNOWN\_FLAGS;** 


## MAPI\_E\_UNKNOWN\_LCID
 **const mapi\.MAPI\_E\_UNKNOWN\_LCID;** 


## MAPI\_E\_USER\_CANCEL
 **const mapi\.MAPI\_E\_USER\_CANCEL;** 


## MAPI\_E\_VERSION
 **const mapi\.MAPI\_E\_VERSION;** 


## MAPI\_E\_WAIT
 **const mapi\.MAPI\_E\_WAIT;** 


## MAPI\_FORCE\_DOWNLOAD
 **const mapi\.MAPI\_FORCE\_DOWNLOAD;** 
An attempt should be made to download all of the user's messages before returning\. If the MAPI\_FORCE\_DOWNLOAD flag is not set, messages can be downloaded in the background after the call to MAPILogonEx returns\.

## MAPI\_INIT\_VERSION
 **const mapi\.MAPI\_INIT\_VERSION;** 


## MAPI\_LOGON\_UI
 **const mapi\.MAPI\_LOGON\_UI;** 
A dialog box should be displayed to prompt the user for logon information if required\. When the MAPI\_LOGON\_UI flag is not set, the calling client does not display a logon dialog box and returns an error value if the user is not logged on\. MAPI\_LOGON\_UI and MAPI\_PASSWORD\_UI are mutually exclusive\.

## MAPI\_MODIFY
 **const mapi\.MAPI\_MODIFY;** 


## MAPI\_MULTITHREAD\_NOTIFICATIONS
 **const mapi\.MAPI\_MULTITHREAD\_NOTIFICATIONS;** 
MAPI should generate notifications using a thread dedicated to notification handling rather than the first thread used to call[mapi::MAPIInitialize](mapi.md#mapimapiinitialize)\.

## MAPI\_NEW\_SESSION
 **const mapi\.MAPI\_NEW\_SESSION;** 
An attempt should be made to create a new MAPI session rather than acquire the shared session\. If the MAPI\_NEW\_SESSION flag is not set, MAPILogonEx uses an existing shared session even if the lpszprofileName parameter is not NULL\.

## MAPI\_NO\_IDS
 **const mapi\.MAPI\_NO\_IDS;** 
Requests that only names stored as Unicode strings be returned\.

## MAPI\_NO\_MAIL
 **const mapi\.MAPI\_NO\_MAIL;** 
MAPI should not inform the MAPI spooler of the session's existence\. The result is that no messages can be sent or received within the session except through a tightly coupled store and transport pair\. A calling client sets this flag if it is acting as an agent, if configuration work must be done, or if the client is browsing the available message stores\.

## MAPI\_NO\_STRINGS
 **const mapi\.MAPI\_NO\_STRINGS;** 
Requests that only names stored as numeric identifiers be returned\.

## MAPI\_NT\_SERVICE
 **const mapi\.MAPI\_NT\_SERVICE;** 
The caller is running as a Windows NT service\. Callers that are not running as a Windows NT service should not set this flag; callers that are running as a service must set this flag\.

## MAPI\_P1
 **const mapi\.MAPI\_P1;** 
The recipient did not successfully receive the message on the previous attempt\. This is a resend of an earlier transmission\.

## MAPI\_PASSWORD\_UI
 **const mapi\.MAPI\_PASSWORD\_UI;** 
A dialog box should be displayed to prompt the user for the profile password\. MAPI\_PASSWORD\_UI cannot be set if MAPI\_LOGON\_UI is set because the calling client can only present one of the two dialog boxes\. This dialog box does not allow the profile name to be changed; the lpszProfileName parameter must be non-NULL\.

## MAPI\_SERVICE\_UI\_ALWAYS
 **const mapi\.MAPI\_SERVICE\_UI\_ALWAYS;** 
MAPILogonEx should display a configuration dialog box for each message service in the profile\. The dialog boxes are displayed after the profile has been chosen but before any message service is logged on\. The MAPI common dialog box for logon also contains a check box that requests the same operation\.

## MAPI\_SUBMITTED
 **const mapi\.MAPI\_SUBMITTED;** 
The recipient has already received the message and does not need to receive it again\. This is a resend of an earlier transmission\. This flag is set in conjunction with the MAPI\_TO, MAPI\_CC, and MAPI\_BCC values\.

## MAPI\_TIMEOUT\_SHORT
 **const mapi\.MAPI\_TIMEOUT\_SHORT;** 
The logon should fail if blocked for more than a few seconds\.

## MAPI\_TO
 **const mapi\.MAPI\_TO;** 
The recipient is a primary \(To\) recipient\. Clients are required to handle primary recipients; all other types are optional\.

## MAPI\_UNICODE
 **const mapi\.MAPI\_UNICODE;** 
The passed-in strings are in Unicode format\. If the MAPI\_UNICODE flag is not set, the strings are in ANSI format\.

## MAPI\_USE\_DEFAULT
 **const mapi\.MAPI\_USE\_DEFAULT;** 
The messaging subsystem should substitute the profile name of the default profile for the lpszProfileName parameter\. The MAPI\_EXPLICIT\_PROFILE flag is ignored unless lpszProfileName is NULL or empty\.

## MAPI\_W\_APPROX\_COUNT
 **const mapi\.MAPI\_W\_APPROX\_COUNT;** 


## MAPI\_W\_CANCEL\_MESSAGE
 **const mapi\.MAPI\_W\_CANCEL\_MESSAGE;** 


## MAPI\_W\_ERRORS\_RETURNED
 **const mapi\.MAPI\_W\_ERRORS\_RETURNED;** 


## MAPI\_W\_NO\_SERVICE
 **const mapi\.MAPI\_W\_NO\_SERVICE;** 


## MAPI\_W\_PARTIAL\_COMPLETION
 **const mapi\.MAPI\_W\_PARTIAL\_COMPLETION;** 


## MAPI\_W\_POSITION\_CHANGED
 **const mapi\.MAPI\_W\_POSITION\_CHANGED;** 


## MDB\_NO\_DIALOG
 **const mapi\.MDB\_NO\_DIALOG;** 
Prevents the display of logon dialog boxes\. If this flag is set, and OpenMsgStore does not have enough configuration information to open the message store without the user's help, it returns MAPI\_E\_LOGON\_FAILED\. If this flag is not set, the message store provider can prompt the user to correct a name or password, to insert a disk, or to perform other actions necessary to establish connection to the message store\.

## MDB\_NO\_MAIL
 **const mapi\.MDB\_NO\_MAIL;** 
The message store should not be used for sending or receiving mail\. When this flag is set, MAPI does not notify the MAPI spooler that this message store is being opened\.

## MDB\_TEMPORARY
 **const mapi\.MDB\_TEMPORARY;** 
Instructs MAPI that the message store is not permanent and should not be added to the message store table\. This flag is used to log on the message store so that information can be retrieved programmatically from the profile section\.

## MDB\_WRITE
 **const mapi\.MDB\_WRITE;** 
Requests read/write access to the message store\.

## MESSAGE\_DIALOG
 **const mapi\.MESSAGE\_DIALOG;** 
Displays a progress indicator as the operation proceeds\.

## MODRECIP\_ADD
 **const mapi\.MODRECIP\_ADD;** 
The recipients should be added to the recipient list\.

## MODRECIP\_MODIFY
 **const mapi\.MODRECIP\_MODIFY;** 
The recipients should replace existing recipients\. All of the existing properties are replaced by those in the corresponding ADRENTRY structure\.

## MODRECIP\_REMOVE
 **const mapi\.MODRECIP\_REMOVE;** 
Existing recipients should be removed from the recipient list using as an index the PR\_ROWID property included in the property value array of each recipient entry in the mods parameter\.

## NO\_ATTACHMENT
 **const mapi\.NO\_ATTACHMENT;** 
The attachment has just been created\.

## OPEN\_IF\_EXISTS
 **const mapi\.OPEN\_IF\_EXISTS;** 
Does not fail if the specified folder already exists\.

## [mapi](#mapi)\.OpenIMsgOnIStg

[PyIMessage](#pyimessage)\= **OpenIMsgOnIStg\( *session*  *, support*  *, storage*  *, callback*  *, callbackData*  *, flags* ** \)
Builds a new IMessage object on top of an existing OLE IStorage object, to be used within a message session\.

#### Parameters


  -  *session* : object

    

  -  *support* : **PyIMAPISupport** 

    May be None

  -  *storage* :[PyIStorage](#pyistorage)

    A[PyIStorage](#pyistorage)object that is open and has read-only or read/write access\. Because IMessage does not support write-only access, OpenIMsgOnIStg does not accept a storage object opened in write-only mode\.

  -  *callback\=None* : object

    Only None is supported\.

  -  *callbackData\=0* : int

    

  -  *flags\=0* : int

    

## [mapi](#mapi)\.OpenIMsgSession

object \= **OpenIMsgSession\(** \)


## [mapi](#mapi)\.OpenStreamOnFile

[PyIStream](#pyistream)\= **OpenStreamOnFile\( *filename*  *, flags*  *, prefix* ** \)
Allocates and initializes an OLE IStream object to access the contents of a file\.

#### Parameters


  -  *filename* : string

    

  -  *flags\=0* : int

    

  -  *prefix\=None* : string

    

## RELOP\_EQ
 **const mapi\.RELOP\_EQ;** 
The comparison is made based on equal values\.

## RELOP\_GE
 **const mapi\.RELOP\_GE;** 
The comparison is made based on a greater or equal first value\.

## RELOP\_GT
 **const mapi\.RELOP\_GT;** 
The comparison is made based on a greater first value\.

## RELOP\_LE
 **const mapi\.RELOP\_LE;** 
The comparison is made based on a lesser or equal first value\.

## RELOP\_LT
 **const mapi\.RELOP\_LT;** 
The comparison is made based on a lesser first value\.

## RELOP\_NE
 **const mapi\.RELOP\_NE;** 
The comparison is made based on unequal values\.

## RELOP\_RE
 **const mapi\.RELOP\_RE;** 
The comparison is made based on LIKE \(regular expression\) values\.

## RES\_AND
 **const mapi\.RES\_AND;** 
SRestriction structure describes an AND restriction, which applies a bitwise AND operation to a restriction\.

## RES\_BITMASK
 **const mapi\.RES\_BITMASK;** 
SRestriction structure describes a bitmask restriction, which applies a bitmask to a property value\.

## RES\_COMMENT
 **const mapi\.RES\_COMMENT;** 
SRestriction structure describes a comment restriction, which associates a comment with a restriction\.

## RES\_COMPAREPROPS
 **const mapi\.RES\_COMPAREPROPS;** 
SRestriction structure describes a compare properties restriction, which compares two property values\.

## RES\_CONTENT
 **const mapi\.RES\_CONTENT;** 
SRestriction structure describes a content restriction, which searches a property value for specific content\.

## RES\_EXIST
 **const mapi\.RES\_EXIST;** 
SRestriction structure describes an exist restriction, which determines if a property is supported\.

## RES\_NOT
 **const mapi\.RES\_NOT;** 
SRestriction structure describes a NOT restriction, which applies a logical NOT operation to a restriction\.

## RES\_OR
 **const mapi\.RES\_OR;** 
SRestriction structure describes an OR restriction, which applies a logical OR operation to a restriction\.

## RES\_PROPERTY
 **const mapi\.RES\_PROPERTY;** 
SRestriction structure describes a property restriction, which determines if a property value matches a particular value\.

## RES\_SIZE
 **const mapi\.RES\_SIZE;** 
SRestriction structure describes a size restriction, which determines if a property value is a particular size\.

## RES\_SUBRESTRICTION
 **const mapi\.RES\_SUBRESTRICTION;** 
SRestriction structure describes a subobject restriction, which applies a restriction to a message's attachments or recipients\.

## [mapi](#mapi)\.RTFStreamToHTML

 **RTFStreamToHTML\( *The stream to read the uncompressed RTF from* ** \)


#### Parameters


  -  *The stream to read the uncompressed RTF from* :[PyIStream](#pyistream)

    

## [mapi](#mapi)\.RTFSync

int \= **RTFSync\( *message*  *, flags* ** \)


#### Parameters


  -  *message* :[PyIMessage](#pyimessage)

    The message\.

  -  *flags* : int

    

## RTF\_SYNC\_BODY\_CHANGED
 **const mapi\.RTF\_SYNC\_BODY\_CHANGED;** 
The plain text version of the message has changed\.

## RTF\_SYNC\_RTF\_CHANGED
 **const mapi\.RTF\_SYNC\_RTF\_CHANGED;** 
The RTF version of the message has changed\.

## SERVICE\_UI\_ALLOWED
 **const mapi\.SERVICE\_UI\_ALLOWED;** 
The message service should display its configuration property sheet only if the service is not completely configured\.

## SERVICE\_UI\_ALWAYS
 **const mapi\.SERVICE\_UI\_ALWAYS;** 
The message service must always display its configuration property sheet\. If SERVICE\_UI\_ALWAYS is not set, a configuration property sheet can still be displayed if SERVICE\_UI\_ALLOWED is set and valid configuration information is not available from the property value array in the lpProps parameter\. Either SERVICE\_UI\_ALLOWED or SERVICE\_UI\_ALWAYS must be set for a property sheet to be displayed\.

## SHOW\_SOFT\_DELETES
 **const mapi\.SHOW\_SOFT\_DELETES;** 
Shows items that are currently marked as soft deleted\.

## SOF\_UNIQUEFILENAME
 **const mapi\.SOF\_UNIQUEFILENAME;** 
A temporary file is to be created for the IStream object

## STATUS\_DEFAULT\_STORE
 **const mapi\.STATUS\_DEFAULT\_STORE;** 


## STATUS\_FLUSH\_QUEUES
 **const mapi\.STATUS\_FLUSH\_QUEUES;** 


## STATUS\_INBOUND\_FLUSH
 **const mapi\.STATUS\_INBOUND\_FLUSH;** 


## STATUS\_OUTBOUND\_FLUSH
 **const mapi\.STATUS\_OUTBOUND\_FLUSH;** 


## TABLE\_SORT\_ASCEND
 **const mapi\.TABLE\_SORT\_ASCEND;** 
The table should be sorted in ascending order\.

## TABLE\_SORT\_COMBINE
 **const mapi\.TABLE\_SORT\_COMBINE;** 
The sort operation should create a category that combines the property identified as the sort key column in the ulPropTag member with the sort key column specified in the previous SSortOrder structure\.
TABLE\_SORT\_COMBINE can only be used when the SSortOrder structure is being used as an entry in an SSortOrderSet structure to specify multiple sort orders for a categorized sort\. TABLE\_SORT\_COMBINE cannot be used in the first SSortOrder structure in an SSortOrderSet structure\.

## TABLE\_SORT\_DESCEND
 **const mapi\.TABLE\_SORT\_DESCEND;** 
The table should be sorted in descending order\.

## TBL\_ALL\_COLUMNS
 **const mapi\.TBL\_ALL\_COLUMNS;** 
The table should return all available columns\.

## TBL\_ASYNC
 **const mapi\.TBL\_ASYNC;** 
Starts the operation asynchronously and returns before the operation completes\.

## TBL\_BATCH
 **const mapi\.TBL\_BATCH;** 
Defers evaluation of the filter until the data in the table is required\.

## [mapi](#mapi)\.WrapCompressedRTFStream

[PyIStream](#pyistream)\= **WrapCompressedRTFStream\( *stream*  *, flags* ** \)


#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    Message stream

  -  *flags* : int

    