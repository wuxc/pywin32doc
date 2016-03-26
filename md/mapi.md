# mapi

## Module mapi

A COM interface to MAPI

#### Methods


  - [HexFromBin](mapi.md#mapihexfrombin)

    converts a binary number into a string representation of a hexadecimal number.&nbsp;

  - [BinFromHex](mapi.md#mapibinfromhex)

    converts a hexadecimal number into a binary string&nbsp;

  - [MAPIUninitialize](mapi.md#mapimapiuninitialize)

    Decrements the reference count, cleans up, and deletes per-instance global data for the MAPI DLL.&nbsp;

  - [MAPIInitialize](mapi.md#mapimapiinitialize)

    Increments the MAPI subsystem reference count and initializes global data for the MAPI DLL.&nbsp;

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

    Builds a new IMessage object on top of an existing OLE IStorage object, to be used within a message session.&nbsp;

  - [RTFStreamToHTML](mapi.md#mapirtfstreamtohtml)

    &nbsp;

  - [OpenStreamOnFile](mapi.md#mapiopenstreamonfile)

    Allocates and initializes an OLE IStream object to access the contents of a file.&nbsp;

  - [HrGetOneProp](mapi.md#mapihrgetoneprop)

    Retrieves the value of a single property from an IMAPIProp object.&nbsp;

  - [HrSetOneProp](mapi.md#mapihrsetoneprop)

    Sets the value of a single property on a IMAPIProp object.&nbsp;

## AB_NO_DIALOG
 __const mapi.AB_NO_DIALOG;__ 


## ATTACH_BY_REFERENCE
 __const mapi.ATTACH_BY_REFERENCE;__ 
The PR_ATTACH_PATHNAME or PR_ATTACH_LONG_PATHNAME property contains a fully qualified path identifying the attachment to recipients with access to a common file server.

## ATTACH_BY_REF_ONLY
 __const mapi.ATTACH_BY_REF_ONLY;__ 
The PR_ATTACH_PATHNAME or PR_ATTACH_LONG_PATHNAME property contains a fully qualified path identifying the attachment.

## ATTACH_BY_REF_RESOLVE
 __const mapi.ATTACH_BY_REF_RESOLVE;__ 
The PR_ATTACH_PATHNAME or PR_ATTACH_LONG_PATHNAME property contains a fully qualified path identifying the attachment.

## ATTACH_BY_VALUE
 __const mapi.ATTACH_BY_VALUE;__ 
The PR_ATTACH_DATA_BIN property contains the attachment data.

## ATTACH_EMBEDDED_MSG
 __const mapi.ATTACH_EMBEDDED_MSG;__ 
The PR_ATTACH_DATA_OBJ property contains an embedded object that supports the IMessage interface.

## ATTACH_OLE
 __const mapi.ATTACH_OLE;__ 
The attachment is an embedded OLE object

## BMR_EQZ
 __const mapi.BMR_EQZ;__ 
Perform a bitwise AND operation of the mask in the ulMask member with the property represented by the ulPropTag member and test for being equal to zero.

## BMR_NEZ
 __const mapi.BMR_NEZ;__ 
Perform a bitwise AND operation of the mask in the ulMask member with the property represented by the ulPropTag member and test for being not equal to zero.

## BOOKMARK_BEGINNING
 __const mapi.BOOKMARK_BEGINNING;__ 
Starts the seek operation from the beginning of the table.

## BOOKMARK_CURRENT
 __const mapi.BOOKMARK_CURRENT;__ 
Starts the seek operation from the row in the table where the cursor is located.

## BOOKMARK_END
 __const mapi.BOOKMARK_END;__ 
Starts the seek operation from the end of the table.

## [mapi](#mapi).BinFromHex

[PyUnicode](#pyunicode)= __BinFromHex( *val* __ )
converts a hexadecimal number into a binary string

#### Parameters


  -  *val* : string/[PyUnicode](#pyunicode)

    The string to be converted.

## CCSF_8BITHEADERS
 __const mapi.CCSF_8BITHEADERS;__ 
the converter should allow 8 bit headers

## CCSF_EMBEDDED_MESSAGE
 __const mapi.CCSF_EMBEDDED_MESSAGE;__ 
sent/unsent information is persisted in X-Unsent

## CCSF_INCLUDE_BCC
 __const mapi.CCSF_INCLUDE_BCC;__ 
the converter should include Bcc recipients

## CCSF_NOHEADERS
 __const mapi.CCSF_NOHEADERS;__ 
the converter should ignore the headers on the outside message

## CCSF_NO_MSGID
 __const mapi.CCSF_NO_MSGID;__ 
don't include Message-Id field in outgoing messages

## CCSF_PLAIN_TEXT_ONLY
 __const mapi.CCSF_PLAIN_TEXT_ONLY;__ 
the converter should just send plain text

## CCSF_PRESERVE_SOURCE
 __const mapi.CCSF_PRESERVE_SOURCE;__ 
don't modify the source message

## CCSF_SMTP
 __const mapi.CCSF_SMTP;__ 
the converter is being passed an SMTP message

## CCSF_USE_RTF
 __const mapi.CCSF_USE_RTF;__ 
the converter should do HTML-&gtRTF conversion

## CCSF_USE_TNEF
 __const mapi.CCSF_USE_TNEF;__ 
the converter should embed TNEF in the MIME message

## CONVENIENT_DEPTH
 __const mapi.CONVENIENT_DEPTH;__ 
Fills the hierarchy table with containers from multiple levels. If CONVENIENT_DEPTH is not set, the hierarchy table contains only the container's immediate child containers.

## [mapi](#mapi).CloseIMsgSession

 __CloseIMsgSession(__ )


## DELETE_HARD_DELETE
 __const mapi.DELETE_HARD_DELETE;__ 
Permanently removes all messages, including soft-deleted ones.

## DEL_FOLDERS
 __const mapi.DEL_FOLDERS;__ 
All subfolders of the subfolder pointed to by lpEntryID should be deleted.

## DEL_MESSAGES
 __const mapi.DEL_MESSAGES;__ 
All messages in the subfolder pointed to by lpEntryID should be deleted.

## DIR_BACKWARD
 __const mapi.DIR_BACKWARD;__ 
Searches backward from the row identified by the bookmark.

## FLUSH_ASYNC_OK
 __const mapi.FLUSH_ASYNC_OK;__ 


## FLUSH_DOWNLOAD
 __const mapi.FLUSH_DOWNLOAD;__ 


## FLUSH_FORCE
 __const mapi.FLUSH_FORCE;__ 


## FLUSH_NO_UI
 __const mapi.FLUSH_NO_UI;__ 


## FLUSH_UPLOAD
 __const mapi.FLUSH_UPLOAD;__ 


## FL_FULLSTRING
 __const mapi.FL_FULLSTRING;__ 
To match, the lpProp search string must be completely contained in the property identified by ulPropTag.

## FL_IGNORECASE
 __const mapi.FL_IGNORECASE;__ 
The comparison should be made without considering case.

## FL_IGNORENONSPACE
 __const mapi.FL_IGNORENONSPACE;__ 
The comparison should ignore Unicode-defined nonspacing characters such as diacritical marks.

## FL_LOOSE
 __const mapi.FL_LOOSE;__ 
The comparison should result in a match whenever possible, ignoring case and nonspacing characters

## FL_PREFIX
 __const mapi.FL_PREFIX;__ 
To match, the lpProp search string must appear at the beginning of the property identified by ulPropTag. The two strings should be compared only up to the length of the search string indicated by lpProp.

## FL_SUBSTRING
 __const mapi.FL_SUBSTRING;__ 
To match, the lpProp search string must be contained anywhere within the property identified by ulPropTag.

## FOLDER_DIALOG
 __const mapi.FOLDER_DIALOG;__ 
A progress indicator should be displayed while the operation proceeds.

## FOLDER_GENERIC
 __const mapi.FOLDER_GENERIC;__ 
A generic folder should be created.

## FOLDER_SEARCH
 __const mapi.FOLDER_SEARCH;__ 
A search-results folder should be created.

## FORCE_SAVE
 __const mapi.FORCE_SAVE;__ 
Changes should be written to the object, overriding any previous changes made to the object, and the object closed. Read/write access must have been set for the operation to succeed. The FORCE_SAVE flag is used after a previous call to SaveChanges returned MAPI_E_OBJECT_CHANGED.

## [mapi](#mapi).HexFromBin

[PyUnicode](#pyunicode)= __HexFromBin( *val* __ )
converts a binary number into a string representation of a hexadecimal number.

#### Parameters


  -  *val* : string

    Converts an EntryID into a hex string representation.

#### Comments
Note: This function may not be supported in future versions of MAPI.

## [mapi](#mapi).HrGetOneProp

item = __HrGetOneProp( *prop*  *, propTag* __ )
Retrieves the value of a single property from an IMAPIProp object.

#### Parameters


  -  *prop* :[PyIMAPIProp](#pyimapiprop)

    Object to retrieve property value from.

  -  *propTag* : ULONG

    The property tag to open.

## [mapi](#mapi).HrQueryAllRows

 __SRowSet__ = __HrQueryAllRows( *table*  *, properties*  *, restrictions*  *, sortOrderSet*  *, rowsMax* __ )


#### Parameters


  -  *table* :[PyIMAPITable](#pyimapitable)

    

  -  *properties* :[PySPropTagArray](#pysproptagarray)

    A sequence of property tags indicating table columns. These tags are used to select the specific columns to be retrieved. If this parameter is None, HrQueryAllRows retrieves the entire column set of the current table view passed in the table parameter.

  -  *restrictions* :[PySRestriction](#pysrestriction)

    Defines the retrieval restrictions. If this parameter is None, HrQueryAllRows makes no restrictions.

  -  *sortOrderSet* :[PySSortOrderSet](#pyssortorderset)

    Identifies the sort order of the columns to be retrieved. If this parameter is None, the default sort order for the table is used.

  -  *rowsMax* : int

    Maximum number of rows to be retrieved. If the value of the rowsMax parameter is zero, no limit on the number of rows retrieved is set.

## [mapi](#mapi).HrSetOneProp

item = __HrSetOneProp( *prop*  *, propValue* __ )
Sets the value of a single property on a IMAPIProp object.

#### Parameters


  -  *prop* :[PyIMAPIProp](#pyimapiprop)

    Object to set property value on.

  -  *propValue* :[PySPropValue](#pyspropvalue)

    Property value to set.

## KEEP_OPEN_READONLY
 __const mapi.KEEP_OPEN_READONLY;__ 
Changes should be committed and the object should be kept open for reading. No further changes will be made.

## KEEP_OPEN_READWRITE
 __const mapi.KEEP_OPEN_READWRITE;__ 
Changes should be committed and the object should be kept open for read/write access. This flag is usually set when the object was initially opened for read/write access. Subsequent changes to the object are allowed.

## [mapi](#mapi).MAPIAdminProfiles

 __PyIProfAdmin__ = __MAPIAdminProfiles( *fFlags* __ )


#### Parameters


  -  *fFlags* : int

    

## [mapi](#mapi).MAPIInitialize

 __MAPIInitialize( *init* __ )
Increments the MAPI subsystem reference count and initializes global data for the MAPI DLL.

#### Parameters


  -  *init* :[MAPIINIT_0](MAPIINIT.md#mapiinit0)

    MAPI Initialization flags.

## [mapi](#mapi).MAPILogonEx

[PyIMAPISession](#pyimapisession)= __MAPILogonEx( *hWnd*  *, profileName*  *, password*  *, uiFlags* __ )


#### Parameters


  -  *hWnd* : int

    Handle to the window to which the logon dialog box is modal. If no dialog box is displayed during the call, the hWnd parameter is ignored. This parameter can be zero.

  -  *profileName* :[PyUnicode](#pyunicode)

    A string containing the name of the profile to use when logging on. This string is limited to 64 characters.

  -  *password* :[PyUnicode](#pyunicode)

    A string containing the password of the profile. This parameter can be None whether or not the profileName parameter is None. This string is limited to 64 characters.

  -  *uiFlags* : int

    Bitmask of flags used to control how logon is performed.  See the MAPI documentation for details.

## [mapi](#mapi).MAPIUninitialize

 __MAPIUninitialize(__ )
Decrements the reference count, cleans up, and deletes per-instance global data for the MAPI DLL.

## MAPI_ALLOW_OTHERS
 __const mapi.MAPI_ALLOW_OTHERS;__ 
The shared session should be returned, allowing subsequent clients to acquire the session without providing any user credentials.

## MAPI_ASSOCIATED
 __const mapi.MAPI_ASSOCIATED;__ 
The container's associated contents table should be returned rather than the standard contents table. This flag is used only with folders. The messages that are included in the associated contents table were created with the MAPI_ASSOCIATED flag set in the call to IMAPIFolder::CreateMessage. Clients typically use the associated contents table to retrieve forms and views.

## MAPI_BCC
 __const mapi.MAPI_BCC;__ 
The recipient is a blind carbon copy (BCC) recipient. Primary and carbon copy recipients are unaware of the existence of BCC recipients.

## MAPI_BEST_ACCESS
 __const mapi.MAPI_BEST_ACCESS;__ 


## MAPI_CC
 __const mapi.MAPI_CC;__ 
The recipient is a carbon copy (CC) recipient, a recipient that receives a message in addition to the primary recipients.

## MAPI_CREATE
 __const mapi.MAPI_CREATE;__ 
The object will be created if necessary.

## MAPI_DEFAULT_SERVICES
 __const mapi.MAPI_DEFAULT_SERVICES;__ 
MAPI should populate the new profile with the message services that are included in the [Default Services] section of the MAPISVC.INF file.

## MAPI_DEFERRED_ERRORS
 __const mapi.MAPI_DEFERRED_ERRORS;__ 
Allows a method to return successfully, possibly before the changes have been fully committed.

## MAPI_DIALOG
 __const mapi.MAPI_DIALOG;__ 


## MAPI_EXPLICIT_PROFILE
 __const mapi.MAPI_EXPLICIT_PROFILE;__ 
The default profile should not be used, and the user should be required to supply a profile.

## MAPI_EXTENDED
 __const mapi.MAPI_EXTENDED;__ 
Log on with extended capabilities. This flag should always be set. The older MAPILogon function is no longer available.

## MAPI_E_ACCOUNT_DISABLED
 __const mapi.MAPI_E_ACCOUNT_DISABLED;__ 


## MAPI_E_AMBIGUOUS_RECIP
 __const mapi.MAPI_E_AMBIGUOUS_RECIP;__ 


## MAPI_E_BAD_CHARWIDTH
 __const mapi.MAPI_E_BAD_CHARWIDTH;__ 


## MAPI_E_BAD_COLUMN
 __const mapi.MAPI_E_BAD_COLUMN;__ 


## MAPI_E_BAD_VALUE
 __const mapi.MAPI_E_BAD_VALUE;__ 


## MAPI_E_BUSY
 __const mapi.MAPI_E_BUSY;__ 


## MAPI_E_CALL_FAILED
 __const mapi.MAPI_E_CALL_FAILED;__ 


## MAPI_E_CANCEL
 __const mapi.MAPI_E_CANCEL;__ 


## MAPI_E_COLLISION
 __const mapi.MAPI_E_COLLISION;__ 


## MAPI_E_COMPUTED
 __const mapi.MAPI_E_COMPUTED;__ 


## MAPI_E_CORRUPT_DATA
 __const mapi.MAPI_E_CORRUPT_DATA;__ 


## MAPI_E_CORRUPT_STORE
 __const mapi.MAPI_E_CORRUPT_STORE;__ 


## MAPI_E_DECLINE_COPY
 __const mapi.MAPI_E_DECLINE_COPY;__ 


## MAPI_E_DISK_ERROR
 __const mapi.MAPI_E_DISK_ERROR;__ 


## MAPI_E_END_OF_SESSION
 __const mapi.MAPI_E_END_OF_SESSION;__ 


## MAPI_E_EXTENDED_ERROR
 __const mapi.MAPI_E_EXTENDED_ERROR;__ 


## MAPI_E_FAILONEPROVIDER
 __const mapi.MAPI_E_FAILONEPROVIDER;__ 


## MAPI_E_FOLDER_CYCLE
 __const mapi.MAPI_E_FOLDER_CYCLE;__ 


## MAPI_E_HAS_FOLDERS
 __const mapi.MAPI_E_HAS_FOLDERS;__ 


## MAPI_E_HAS_MESSAGES
 __const mapi.MAPI_E_HAS_MESSAGES;__ 


## MAPI_E_INTERFACE_NOT_SUPPORTED
 __const mapi.MAPI_E_INTERFACE_NOT_SUPPORTED;__ 


## MAPI_E_INVALID_ACCESS_TIME
 __const mapi.MAPI_E_INVALID_ACCESS_TIME;__ 


## MAPI_E_INVALID_BOOKMARK
 __const mapi.MAPI_E_INVALID_BOOKMARK;__ 


## MAPI_E_INVALID_ENTRYID
 __const mapi.MAPI_E_INVALID_ENTRYID;__ 


## MAPI_E_INVALID_OBJECT
 __const mapi.MAPI_E_INVALID_OBJECT;__ 


## MAPI_E_INVALID_PARAMETER
 __const mapi.MAPI_E_INVALID_PARAMETER;__ 


## MAPI_E_INVALID_TYPE
 __const mapi.MAPI_E_INVALID_TYPE;__ 


## MAPI_E_INVALID_WORKSTATION_ACCOUNT
 __const mapi.MAPI_E_INVALID_WORKSTATION_ACCOUNT;__ 


## MAPI_E_LOGON_FAILED
 __const mapi.MAPI_E_LOGON_FAILED;__ 


## MAPI_E_MISSING_REQUIRED_COLUMN
 __const mapi.MAPI_E_MISSING_REQUIRED_COLUMN;__ 


## MAPI_E_NETWORK_ERROR
 __const mapi.MAPI_E_NETWORK_ERROR;__ 


## MAPI_E_NON_STANDARD
 __const mapi.MAPI_E_NON_STANDARD;__ 


## MAPI_E_NOT_ENOUGH_DISK
 __const mapi.MAPI_E_NOT_ENOUGH_DISK;__ 


## MAPI_E_NOT_ENOUGH_MEMORY
 __const mapi.MAPI_E_NOT_ENOUGH_MEMORY;__ 


## MAPI_E_NOT_ENOUGH_RESOURCES
 __const mapi.MAPI_E_NOT_ENOUGH_RESOURCES;__ 


## MAPI_E_NOT_FOUND
 __const mapi.MAPI_E_NOT_FOUND;__ 


## MAPI_E_NOT_INITIALIZED
 __const mapi.MAPI_E_NOT_INITIALIZED;__ 


## MAPI_E_NOT_IN_QUEUE
 __const mapi.MAPI_E_NOT_IN_QUEUE;__ 


## MAPI_E_NOT_ME
 __const mapi.MAPI_E_NOT_ME;__ 


## MAPI_E_NO_ACCESS
 __const mapi.MAPI_E_NO_ACCESS;__ 


## MAPI_E_NO_RECIPIENTS
 __const mapi.MAPI_E_NO_RECIPIENTS;__ 


## MAPI_E_NO_SUPPORT
 __const mapi.MAPI_E_NO_SUPPORT;__ 


## MAPI_E_NO_SUPPRESS
 __const mapi.MAPI_E_NO_SUPPRESS;__ 


## MAPI_E_OBJECT_CHANGED
 __const mapi.MAPI_E_OBJECT_CHANGED;__ 


## MAPI_E_OBJECT_DELETED
 __const mapi.MAPI_E_OBJECT_DELETED;__ 


## MAPI_E_PASSWORD_CHANGE_REQUIRED
 __const mapi.MAPI_E_PASSWORD_CHANGE_REQUIRED;__ 


## MAPI_E_PASSWORD_EXPIRED
 __const mapi.MAPI_E_PASSWORD_EXPIRED;__ 


## MAPI_E_SESSION_LIMIT
 __const mapi.MAPI_E_SESSION_LIMIT;__ 


## MAPI_E_STRING_TOO_LONG
 __const mapi.MAPI_E_STRING_TOO_LONG;__ 


## MAPI_E_SUBMITTED
 __const mapi.MAPI_E_SUBMITTED;__ 


## MAPI_E_TABLE_EMPTY
 __const mapi.MAPI_E_TABLE_EMPTY;__ 


## MAPI_E_TABLE_TOO_BIG
 __const mapi.MAPI_E_TABLE_TOO_BIG;__ 


## MAPI_E_TIMEOUT
 __const mapi.MAPI_E_TIMEOUT;__ 


## MAPI_E_TOO_BIG
 __const mapi.MAPI_E_TOO_BIG;__ 


## MAPI_E_TOO_COMPLEX
 __const mapi.MAPI_E_TOO_COMPLEX;__ 


## MAPI_E_TYPE_NO_SUPPORT
 __const mapi.MAPI_E_TYPE_NO_SUPPORT;__ 


## MAPI_E_UNABLE_TO_ABORT
 __const mapi.MAPI_E_UNABLE_TO_ABORT;__ 


## MAPI_E_UNABLE_TO_COMPLETE
 __const mapi.MAPI_E_UNABLE_TO_COMPLETE;__ 


## MAPI_E_UNCONFIGURED
 __const mapi.MAPI_E_UNCONFIGURED;__ 


## MAPI_E_UNEXPECTED_ID
 __const mapi.MAPI_E_UNEXPECTED_ID;__ 


## MAPI_E_UNEXPECTED_TYPE
 __const mapi.MAPI_E_UNEXPECTED_TYPE;__ 


## MAPI_E_UNKNOWN_CPID
 __const mapi.MAPI_E_UNKNOWN_CPID;__ 


## MAPI_E_UNKNOWN_ENTRYID
 __const mapi.MAPI_E_UNKNOWN_ENTRYID;__ 


## MAPI_E_UNKNOWN_FLAGS
 __const mapi.MAPI_E_UNKNOWN_FLAGS;__ 


## MAPI_E_UNKNOWN_LCID
 __const mapi.MAPI_E_UNKNOWN_LCID;__ 


## MAPI_E_USER_CANCEL
 __const mapi.MAPI_E_USER_CANCEL;__ 


## MAPI_E_VERSION
 __const mapi.MAPI_E_VERSION;__ 


## MAPI_E_WAIT
 __const mapi.MAPI_E_WAIT;__ 


## MAPI_FORCE_DOWNLOAD
 __const mapi.MAPI_FORCE_DOWNLOAD;__ 
An attempt should be made to download all of the user's messages before returning. If the MAPI_FORCE_DOWNLOAD flag is not set, messages can be downloaded in the background after the call to MAPILogonEx returns.

## MAPI_INIT_VERSION
 __const mapi.MAPI_INIT_VERSION;__ 


## MAPI_LOGON_UI
 __const mapi.MAPI_LOGON_UI;__ 
A dialog box should be displayed to prompt the user for logon information if required. When the MAPI_LOGON_UI flag is not set, the calling client does not display a logon dialog box and returns an error value if the user is not logged on. MAPI_LOGON_UI and MAPI_PASSWORD_UI are mutually exclusive.

## MAPI_MODIFY
 __const mapi.MAPI_MODIFY;__ 


## MAPI_MULTITHREAD_NOTIFICATIONS
 __const mapi.MAPI_MULTITHREAD_NOTIFICATIONS;__ 
MAPI should generate notifications using a thread dedicated to notification handling rather than the first thread used to call[mapi::MAPIInitialize](mapi.md#mapimapiinitialize).

## MAPI_NEW_SESSION
 __const mapi.MAPI_NEW_SESSION;__ 
An attempt should be made to create a new MAPI session rather than acquire the shared session. If the MAPI_NEW_SESSION flag is not set, MAPILogonEx uses an existing shared session even if the lpszprofileName parameter is not NULL.

## MAPI_NO_IDS
 __const mapi.MAPI_NO_IDS;__ 
Requests that only names stored as Unicode strings be returned.

## MAPI_NO_MAIL
 __const mapi.MAPI_NO_MAIL;__ 
MAPI should not inform the MAPI spooler of the session's existence. The result is that no messages can be sent or received within the session except through a tightly coupled store and transport pair. A calling client sets this flag if it is acting as an agent, if configuration work must be done, or if the client is browsing the available message stores.

## MAPI_NO_STRINGS
 __const mapi.MAPI_NO_STRINGS;__ 
Requests that only names stored as numeric identifiers be returned.

## MAPI_NT_SERVICE
 __const mapi.MAPI_NT_SERVICE;__ 
The caller is running as a Windows NT service. Callers that are not running as a Windows NT service should not set this flag; callers that are running as a service must set this flag.

## MAPI_P1
 __const mapi.MAPI_P1;__ 
The recipient did not successfully receive the message on the previous attempt. This is a resend of an earlier transmission.

## MAPI_PASSWORD_UI
 __const mapi.MAPI_PASSWORD_UI;__ 
A dialog box should be displayed to prompt the user for the profile password. MAPI_PASSWORD_UI cannot be set if MAPI_LOGON_UI is set because the calling client can only present one of the two dialog boxes. This dialog box does not allow the profile name to be changed; the lpszProfileName parameter must be non-NULL.

## MAPI_SERVICE_UI_ALWAYS
 __const mapi.MAPI_SERVICE_UI_ALWAYS;__ 
MAPILogonEx should display a configuration dialog box for each message service in the profile. The dialog boxes are displayed after the profile has been chosen but before any message service is logged on. The MAPI common dialog box for logon also contains a check box that requests the same operation.

## MAPI_SUBMITTED
 __const mapi.MAPI_SUBMITTED;__ 
The recipient has already received the message and does not need to receive it again. This is a resend of an earlier transmission. This flag is set in conjunction with the MAPI_TO, MAPI_CC, and MAPI_BCC values.

## MAPI_TIMEOUT_SHORT
 __const mapi.MAPI_TIMEOUT_SHORT;__ 
The logon should fail if blocked for more than a few seconds.

## MAPI_TO
 __const mapi.MAPI_TO;__ 
The recipient is a primary (To) recipient. Clients are required to handle primary recipients; all other types are optional.

## MAPI_UNICODE
 __const mapi.MAPI_UNICODE;__ 
The passed-in strings are in Unicode format. If the MAPI_UNICODE flag is not set, the strings are in ANSI format.

## MAPI_USE_DEFAULT
 __const mapi.MAPI_USE_DEFAULT;__ 
The messaging subsystem should substitute the profile name of the default profile for the lpszProfileName parameter. The MAPI_EXPLICIT_PROFILE flag is ignored unless lpszProfileName is NULL or empty.

## MAPI_W_APPROX_COUNT
 __const mapi.MAPI_W_APPROX_COUNT;__ 


## MAPI_W_CANCEL_MESSAGE
 __const mapi.MAPI_W_CANCEL_MESSAGE;__ 


## MAPI_W_ERRORS_RETURNED
 __const mapi.MAPI_W_ERRORS_RETURNED;__ 


## MAPI_W_NO_SERVICE
 __const mapi.MAPI_W_NO_SERVICE;__ 


## MAPI_W_PARTIAL_COMPLETION
 __const mapi.MAPI_W_PARTIAL_COMPLETION;__ 


## MAPI_W_POSITION_CHANGED
 __const mapi.MAPI_W_POSITION_CHANGED;__ 


## MDB_NO_DIALOG
 __const mapi.MDB_NO_DIALOG;__ 
Prevents the display of logon dialog boxes. If this flag is set, and OpenMsgStore does not have enough configuration information to open the message store without the user's help, it returns MAPI_E_LOGON_FAILED. If this flag is not set, the message store provider can prompt the user to correct a name or password, to insert a disk, or to perform other actions necessary to establish connection to the message store.

## MDB_NO_MAIL
 __const mapi.MDB_NO_MAIL;__ 
The message store should not be used for sending or receiving mail. When this flag is set, MAPI does not notify the MAPI spooler that this message store is being opened.

## MDB_TEMPORARY
 __const mapi.MDB_TEMPORARY;__ 
Instructs MAPI that the message store is not permanent and should not be added to the message store table. This flag is used to log on the message store so that information can be retrieved programmatically from the profile section.

## MDB_WRITE
 __const mapi.MDB_WRITE;__ 
Requests read/write access to the message store.

## MESSAGE_DIALOG
 __const mapi.MESSAGE_DIALOG;__ 
Displays a progress indicator as the operation proceeds.

## MODRECIP_ADD
 __const mapi.MODRECIP_ADD;__ 
The recipients should be added to the recipient list.

## MODRECIP_MODIFY
 __const mapi.MODRECIP_MODIFY;__ 
The recipients should replace existing recipients. All of the existing properties are replaced by those in the corresponding ADRENTRY structure.

## MODRECIP_REMOVE
 __const mapi.MODRECIP_REMOVE;__ 
Existing recipients should be removed from the recipient list using as an index the PR_ROWID property included in the property value array of each recipient entry in the mods parameter.

## NO_ATTACHMENT
 __const mapi.NO_ATTACHMENT;__ 
The attachment has just been created.

## OPEN_IF_EXISTS
 __const mapi.OPEN_IF_EXISTS;__ 
Does not fail if the specified folder already exists.

## [mapi](#mapi).OpenIMsgOnIStg

[PyIMessage](#pyimessage)= __OpenIMsgOnIStg( *session*  *, support*  *, storage*  *, callback*  *, callbackData*  *, flags* __ )
Builds a new IMessage object on top of an existing OLE IStorage object, to be used within a message session.

#### Parameters


  -  *session* : object

    

  -  *support* : __PyIMAPISupport__ 

    May be None

  -  *storage* :[PyIStorage](#pyistorage)

    A[PyIStorage](#pyistorage)object that is open and has read-only or read/write access. Because IMessage does not support write-only access, OpenIMsgOnIStg does not accept a storage object opened in write-only mode.

  -  *callback=None* : object

    Only None is supported.

  -  *callbackData=0* : int

    

  -  *flags=0* : int

    

## [mapi](#mapi).OpenIMsgSession

object = __OpenIMsgSession(__ )


## [mapi](#mapi).OpenStreamOnFile

[PyIStream](#pyistream)= __OpenStreamOnFile( *filename*  *, flags*  *, prefix* __ )
Allocates and initializes an OLE IStream object to access the contents of a file.

#### Parameters


  -  *filename* : string

    

  -  *flags=0* : int

    

  -  *prefix=None* : string

    

## RELOP_EQ
 __const mapi.RELOP_EQ;__ 
The comparison is made based on equal values.

## RELOP_GE
 __const mapi.RELOP_GE;__ 
The comparison is made based on a greater or equal first value.

## RELOP_GT
 __const mapi.RELOP_GT;__ 
The comparison is made based on a greater first value.

## RELOP_LE
 __const mapi.RELOP_LE;__ 
The comparison is made based on a lesser or equal first value.

## RELOP_LT
 __const mapi.RELOP_LT;__ 
The comparison is made based on a lesser first value.

## RELOP_NE
 __const mapi.RELOP_NE;__ 
The comparison is made based on unequal values.

## RELOP_RE
 __const mapi.RELOP_RE;__ 
The comparison is made based on LIKE (regular expression) values.

## RES_AND
 __const mapi.RES_AND;__ 
SRestriction structure describes an AND restriction, which applies a bitwise AND operation to a restriction.

## RES_BITMASK
 __const mapi.RES_BITMASK;__ 
SRestriction structure describes a bitmask restriction, which applies a bitmask to a property value.

## RES_COMMENT
 __const mapi.RES_COMMENT;__ 
SRestriction structure describes a comment restriction, which associates a comment with a restriction.

## RES_COMPAREPROPS
 __const mapi.RES_COMPAREPROPS;__ 
SRestriction structure describes a compare properties restriction, which compares two property values.

## RES_CONTENT
 __const mapi.RES_CONTENT;__ 
SRestriction structure describes a content restriction, which searches a property value for specific content.

## RES_EXIST
 __const mapi.RES_EXIST;__ 
SRestriction structure describes an exist restriction, which determines if a property is supported.

## RES_NOT
 __const mapi.RES_NOT;__ 
SRestriction structure describes a NOT restriction, which applies a logical NOT operation to a restriction.

## RES_OR
 __const mapi.RES_OR;__ 
SRestriction structure describes an OR restriction, which applies a logical OR operation to a restriction.

## RES_PROPERTY
 __const mapi.RES_PROPERTY;__ 
SRestriction structure describes a property restriction, which determines if a property value matches a particular value.

## RES_SIZE
 __const mapi.RES_SIZE;__ 
SRestriction structure describes a size restriction, which determines if a property value is a particular size.

## RES_SUBRESTRICTION
 __const mapi.RES_SUBRESTRICTION;__ 
SRestriction structure describes a subobject restriction, which applies a restriction to a message's attachments or recipients.

## [mapi](#mapi).RTFStreamToHTML

 __RTFStreamToHTML( *The stream to read the uncompressed RTF from* __ )


#### Parameters


  -  *The stream to read the uncompressed RTF from* :[PyIStream](#pyistream)

    

## [mapi](#mapi).RTFSync

int = __RTFSync( *message*  *, flags* __ )


#### Parameters


  -  *message* :[PyIMessage](#pyimessage)

    The message.

  -  *flags* : int

    

## RTF_SYNC_BODY_CHANGED
 __const mapi.RTF_SYNC_BODY_CHANGED;__ 
The plain text version of the message has changed.

## RTF_SYNC_RTF_CHANGED
 __const mapi.RTF_SYNC_RTF_CHANGED;__ 
The RTF version of the message has changed.

## SERVICE_UI_ALLOWED
 __const mapi.SERVICE_UI_ALLOWED;__ 
The message service should display its configuration property sheet only if the service is not completely configured.

## SERVICE_UI_ALWAYS
 __const mapi.SERVICE_UI_ALWAYS;__ 
The message service must always display its configuration property sheet. If SERVICE_UI_ALWAYS is not set, a configuration property sheet can still be displayed if SERVICE_UI_ALLOWED is set and valid configuration information is not available from the property value array in the lpProps parameter. Either SERVICE_UI_ALLOWED or SERVICE_UI_ALWAYS must be set for a property sheet to be displayed.

## SHOW_SOFT_DELETES
 __const mapi.SHOW_SOFT_DELETES;__ 
Shows items that are currently marked as soft deleted.

## SOF_UNIQUEFILENAME
 __const mapi.SOF_UNIQUEFILENAME;__ 
A temporary file is to be created for the IStream object

## STATUS_DEFAULT_STORE
 __const mapi.STATUS_DEFAULT_STORE;__ 


## STATUS_FLUSH_QUEUES
 __const mapi.STATUS_FLUSH_QUEUES;__ 


## STATUS_INBOUND_FLUSH
 __const mapi.STATUS_INBOUND_FLUSH;__ 


## STATUS_OUTBOUND_FLUSH
 __const mapi.STATUS_OUTBOUND_FLUSH;__ 


## TABLE_SORT_ASCEND
 __const mapi.TABLE_SORT_ASCEND;__ 
The table should be sorted in ascending order.

## TABLE_SORT_COMBINE
 __const mapi.TABLE_SORT_COMBINE;__ 
The sort operation should create a category that combines the property identified as the sort key column in the ulPropTag member with the sort key column specified in the previous SSortOrder structure.
TABLE_SORT_COMBINE can only be used when the SSortOrder structure is being used as an entry in an SSortOrderSet structure to specify multiple sort orders for a categorized sort. TABLE_SORT_COMBINE cannot be used in the first SSortOrder structure in an SSortOrderSet structure.

## TABLE_SORT_DESCEND
 __const mapi.TABLE_SORT_DESCEND;__ 
The table should be sorted in descending order.

## TBL_ALL_COLUMNS
 __const mapi.TBL_ALL_COLUMNS;__ 
The table should return all available columns.

## TBL_ASYNC
 __const mapi.TBL_ASYNC;__ 
Starts the operation asynchronously and returns before the operation completes.

## TBL_BATCH
 __const mapi.TBL_BATCH;__ 
Defers evaluation of the filter until the data in the table is required.

## [mapi](#mapi).WrapCompressedRTFStream

[PyIStream](#pyistream)= __WrapCompressedRTFStream( *stream*  *, flags* __ )


#### Parameters


  -  *stream* :[PyIStream](#pyistream)

    Message stream

  -  *flags* : int

    