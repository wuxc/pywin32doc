# win32job

## Module win32job

An interface to the win32 Process and Thread API's, 

available in Windows 2000 and later.

#### Methods


  - [AssignProcessToJobObject](win32job.md#win32jobassignprocesstojobobject)

    Associates a process with an existing job object.&nbsp;

  - [CreateJobObject](win32job.md#win32jobcreatejobobject)

    Creates or opens a job object.&nbsp;

  - [OpenJobObject](win32job.md#win32jobopenjobobject)

    Opens an existing job object.&nbsp;

  - [TerminateJobObject](win32job.md#win32jobterminatejobobject)

    Terminates all processes currently associated with the job.&nbsp;

  - [UserHandleGrantAccess](win32job.md#win32jobuserhandlegrantaccess)

    Grants or denies access to a handle to a User object to a job that has a user-interface restriction.&nbsp;

  - [IsProcessInJob](win32job.md#win32jobisprocessinjob)

    Determines if the process is running in the specified job.&nbsp;

  - [QueryInformationJobObject](win32job.md#win32jobqueryinformationjobobject)

    Retrieves limit and job state information from the job object.&nbsp;

  - [SetInformationJobObject](win32job.md#win32jobsetinformationjobobject)

    Sets quotas and limits for a job&nbsp;

## [win32job](#win32job).AssignProcessToJobObject

 __AssignProcessToJobObject( *hJob*  *, hProcess* __ )
Associates a process with an existing job object.

#### Parameters


  -  *hJob* :[PyHANDLE](#pyhandle)

    

  -  *hProcess* :[PyHANDLE](#pyhandle)

    

## [win32job](#win32job).CreateJobObject

 __CreateJobObject( *jobAttributes*  *, name* __ )
Creates or opens a job object.

#### Parameters


  -  *jobAttributes* :[PySECURITY_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    

  -  *name* : unicode

    

## [win32job](#win32job).IsProcessInJob

boolean = __IsProcessInJob( *hProcess*  *, hJob* __ )
Determines if the process is running in the specified job.

#### Parameters


  -  *hProcess* :[PyHANDLE](#pyhandle)

    Handle to a process

  -  *hJob* :[PyHANDLE](#pyhandle)

    Handle to a job, use None to check if process is part of any job

#### Comments
Function is only available on WinXP and later

## JOB_OBJECT_ALL_ACCESS
 __const win32job.JOB_OBJECT_ALL_ACCESS;__ 


## JOB_OBJECT_ASSIGN_PROCESS
 __const win32job.JOB_OBJECT_ASSIGN_PROCESS;__ 


## JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS
 __const win32job.JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS;__ 


## JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS
 __const win32job.JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS;__ 


## JOB_OBJECT_LIMIT_ACTIVE_PROCESS
 __const win32job.JOB_OBJECT_LIMIT_ACTIVE_PROCESS;__ 


## JOB_OBJECT_LIMIT_AFFINITY
 __const win32job.JOB_OBJECT_LIMIT_AFFINITY;__ 


## JOB_OBJECT_LIMIT_BREAKAWAY_OK
 __const win32job.JOB_OBJECT_LIMIT_BREAKAWAY_OK;__ 


## JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION
 __const win32job.JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION;__ 


## JOB_OBJECT_LIMIT_JOB_MEMORY
 __const win32job.JOB_OBJECT_LIMIT_JOB_MEMORY;__ 


## JOB_OBJECT_LIMIT_JOB_TIME
 __const win32job.JOB_OBJECT_LIMIT_JOB_TIME;__ 


## JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
 __const win32job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;__ 


## JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME
 __const win32job.JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME;__ 


## JOB_OBJECT_LIMIT_PRIORITY_CLASS
 __const win32job.JOB_OBJECT_LIMIT_PRIORITY_CLASS;__ 


## JOB_OBJECT_LIMIT_PROCESS_MEMORY
 __const win32job.JOB_OBJECT_LIMIT_PROCESS_MEMORY;__ 


## JOB_OBJECT_LIMIT_PROCESS_TIME
 __const win32job.JOB_OBJECT_LIMIT_PROCESS_TIME;__ 


## JOB_OBJECT_LIMIT_SCHEDULING_CLASS
 __const win32job.JOB_OBJECT_LIMIT_SCHEDULING_CLASS;__ 


## JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK
 __const win32job.JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK;__ 


## JOB_OBJECT_LIMIT_VALID_FLAGS
 __const win32job.JOB_OBJECT_LIMIT_VALID_FLAGS;__ 


## JOB_OBJECT_LIMIT_WORKINGSET
 __const win32job.JOB_OBJECT_LIMIT_WORKINGSET;__ 


## JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS
 __const win32job.JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS;__ 


## JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT
 __const win32job.JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT;__ 


## JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO
 __const win32job.JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO;__ 


## JOB_OBJECT_MSG_END_OF_JOB_TIME
 __const win32job.JOB_OBJECT_MSG_END_OF_JOB_TIME;__ 


## JOB_OBJECT_MSG_END_OF_PROCESS_TIME
 __const win32job.JOB_OBJECT_MSG_END_OF_PROCESS_TIME;__ 


## JOB_OBJECT_MSG_EXIT_PROCESS
 __const win32job.JOB_OBJECT_MSG_EXIT_PROCESS;__ 


## JOB_OBJECT_MSG_JOB_MEMORY_LIMIT
 __const win32job.JOB_OBJECT_MSG_JOB_MEMORY_LIMIT;__ 


## JOB_OBJECT_MSG_NEW_PROCESS
 __const win32job.JOB_OBJECT_MSG_NEW_PROCESS;__ 


## JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT
 __const win32job.JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT;__ 


## JOB_OBJECT_POST_AT_END_OF_JOB
 __const win32job.JOB_OBJECT_POST_AT_END_OF_JOB;__ 


## JOB_OBJECT_QUERY
 __const win32job.JOB_OBJECT_QUERY;__ 


## JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS
 __const win32job.JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS;__ 


## JOB_OBJECT_SECURITY_FILTER_TOKENS
 __const win32job.JOB_OBJECT_SECURITY_FILTER_TOKENS;__ 


## JOB_OBJECT_SECURITY_NO_ADMIN
 __const win32job.JOB_OBJECT_SECURITY_NO_ADMIN;__ 


## JOB_OBJECT_SECURITY_ONLY_TOKEN
 __const win32job.JOB_OBJECT_SECURITY_ONLY_TOKEN;__ 


## JOB_OBJECT_SECURITY_RESTRICTED_TOKEN
 __const win32job.JOB_OBJECT_SECURITY_RESTRICTED_TOKEN;__ 


## JOB_OBJECT_SECURITY_VALID_FLAGS
 __const win32job.JOB_OBJECT_SECURITY_VALID_FLAGS;__ 


## JOB_OBJECT_SET_ATTRIBUTES
 __const win32job.JOB_OBJECT_SET_ATTRIBUTES;__ 


## JOB_OBJECT_SET_SECURITY_ATTRIBUTES
 __const win32job.JOB_OBJECT_SET_SECURITY_ATTRIBUTES;__ 


## JOB_OBJECT_TERMINATE
 __const win32job.JOB_OBJECT_TERMINATE;__ 


## JOB_OBJECT_TERMINATE_AT_END_OF_JOB
 __const win32job.JOB_OBJECT_TERMINATE_AT_END_OF_JOB;__ 


## JOB_OBJECT_UILIMIT_ALL
 __const win32job.JOB_OBJECT_UILIMIT_ALL;__ 


## JOB_OBJECT_UILIMIT_DESKTOP
 __const win32job.JOB_OBJECT_UILIMIT_DESKTOP;__ 


## JOB_OBJECT_UILIMIT_DISPLAYSETTINGS
 __const win32job.JOB_OBJECT_UILIMIT_DISPLAYSETTINGS;__ 


## JOB_OBJECT_UILIMIT_EXITWINDOWS
 __const win32job.JOB_OBJECT_UILIMIT_EXITWINDOWS;__ 


## JOB_OBJECT_UILIMIT_GLOBALATOMS
 __const win32job.JOB_OBJECT_UILIMIT_GLOBALATOMS;__ 


## JOB_OBJECT_UILIMIT_HANDLES
 __const win32job.JOB_OBJECT_UILIMIT_HANDLES;__ 


## JOB_OBJECT_UILIMIT_NONE
 __const win32job.JOB_OBJECT_UILIMIT_NONE;__ 


## JOB_OBJECT_UILIMIT_READCLIPBOARD
 __const win32job.JOB_OBJECT_UILIMIT_READCLIPBOARD;__ 


## JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS
 __const win32job.JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS;__ 


## JOB_OBJECT_UILIMIT_WRITECLIPBOARD
 __const win32job.JOB_OBJECT_UILIMIT_WRITECLIPBOARD;__ 


## JOB_OBJECT_UI_VALID_FLAGS
 __const win32job.JOB_OBJECT_UI_VALID_FLAGS;__ 


## JobObjectAssociateCompletionPortInformation
 __const win32job.JobObjectAssociateCompletionPortInformation;__ 


## JobObjectBasicAccountingInformation
 __const win32job.JobObjectBasicAccountingInformation;__ 


## JobObjectBasicAndIoAccountingInformation
 __const win32job.JobObjectBasicAndIoAccountingInformation;__ 


## JobObjectBasicLimitInformation
 __const win32job.JobObjectBasicLimitInformation;__ 


## JobObjectBasicProcessIdList
 __const win32job.JobObjectBasicProcessIdList;__ 


## JobObjectBasicUIRestrictions
 __const win32job.JobObjectBasicUIRestrictions;__ 


## JobObjectEndOfJobTimeInformation
 __const win32job.JobObjectEndOfJobTimeInformation;__ 


## JobObjectExtendedLimitInformation
 __const win32job.JobObjectExtendedLimitInformation;__ 


## JobObjectJobSetInformation
 __const win32job.JobObjectJobSetInformation;__ 


## JobObjectSecurityLimitInformation
 __const win32job.JobObjectSecurityLimitInformation;__ 


## MaxJobObjectInfoClass
 __const win32job.MaxJobObjectInfoClass;__ 


## [win32job](#win32job).OpenJobObject

 __OpenJobObject( *desiredAccess*  *, inheritHandles*  *, name* __ )
Opens an existing job object.

#### Parameters


  -  *desiredAccess* : int

    

  -  *inheritHandles* : bool

    

  -  *name* : unicode

    

## [win32job](#win32job).QueryInformationJobObject

dict = __QueryInformationJobObject( *Job*  *, JobObjectInfoClass* __ )
Retrieves limit and job state information from the job object.

#### Parameters


  -  *Job* :[PyHANDLE](#pyhandle)

    Handle to a job, use None for job that calling process is part of

  -  *JobObjectInfoClass* : int

    The type of data required, one of JobObject* values

 __JobObjectInfoClass__  __Type of information returned__ JobObjectBasicAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_ACCOUNTING_INFORMATION structJobObjectBasicAndIoAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION structJobObjectBasicLimitInformationReturns a dict representing a JOBOBJECT_BASIC_LIMIT_INFORMATION structJobObjectExtendedLimitInformationReturns a dict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION structJobObjectEndOfJobTimeInformationReturns a dict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION structJobObjectBasicUIRestrictionsReturns a dict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS structJobObjectBasicProcessIdListReturns a sequence of pids of processes assigned to the jobJobObjectJobSetInformationReturns a dict representing a JOBOBJECT_JOBSET_INFORMATION struct (not documented on MSDN)JobObjectSecurityLimitInformationJOBOBJECT_SECURITY_LIMIT_INFORMATION Not implementedJobObjectAssociateCompletionPortInformationJOBOBJECT_ASSOCIATE_COMPLETION_PORT Not implemented
#### Return Value
The type of the returned information is dependent on the class requested

## [win32job](#win32job).SetInformationJobObject

 __SetInformationJobObject( *Job*  *, JobObjectInfoClass*  *, JobObjectInfo* __ )
Sets quotas and limits for a job

#### Parameters


  -  *Job* :[PyHANDLE](#pyhandle)

    Handle to a job

  -  *JobObjectInfoClass* : int

    The type of data required, one of JobObject* values

  -  *JobObjectInfo* : dict

    Dictionary containing info to be set, as returned by[win32job::QueryInformationJobObject](win32job.md#win32jobqueryinformationjobobject)


## [win32job](#win32job).TerminateJobObject

 __TerminateJobObject( *hJob*  *, exitCode* __ )
Terminates all processes currently associated with the job.

#### Parameters


  -  *hJob* :[PyHANDLE](#pyhandle)

    

  -  *exitCode* : int

    

## [win32job](#win32job).UserHandleGrantAccess

 __UserHandleGrantAccess( *hUserHandle*  *, hJob*  *, grant* __ )
Grants or denies access to a handle to a User object to a job that has a user-interface restriction.

#### Parameters


  -  *hUserHandle* :[PyHANDLE](#pyhandle)

    

  -  *hJob* :[PyHANDLE](#pyhandle)

    

  -  *grant* : bool

    