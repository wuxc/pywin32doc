
## [win32job](#README.md#win32job).AssignProcessToJobObject

 **AssignProcessToJobObject( *hJob*  *, hProcess* ** )
Associates a process with an existing job object.

#### Parameters


     *hJob* :[PyHANDLE](#README.md#PyHANDLE)

    

     *hProcess* :[PyHANDLE](#README.md#PyHANDLE)

    

## [win32job](#README.md#win32job).CreateJobObject

 **CreateJobObject( *jobAttributes*  *, name* ** )
Creates or opens a job object.

#### Parameters


     *jobAttributes* :[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)

    

     *name* : unicode

    

## [win32job](#README.md#win32job).IsProcessInJob

boolean = **IsProcessInJob( *hProcess*  *, hJob* ** )
Determines if the process is running in the specified job.

#### Parameters


     *hProcess* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a process

     *hJob* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a job, use None to check if process is part of any job

#### Comments
Function is only available on WinXP and later

## JOB_OBJECT_ALL_ACCESS
 **const win32job.JOB_OBJECT_ALL_ACCESS;** 


## JOB_OBJECT_ASSIGN_PROCESS
 **const win32job.JOB_OBJECT_ASSIGN_PROCESS;** 


## JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS
 **const win32job.JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS;** 


## JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS
 **const win32job.JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS;** 


## JOB_OBJECT_LIMIT_ACTIVE_PROCESS
 **const win32job.JOB_OBJECT_LIMIT_ACTIVE_PROCESS;** 


## JOB_OBJECT_LIMIT_AFFINITY
 **const win32job.JOB_OBJECT_LIMIT_AFFINITY;** 


## JOB_OBJECT_LIMIT_BREAKAWAY_OK
 **const win32job.JOB_OBJECT_LIMIT_BREAKAWAY_OK;** 


## JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION
 **const win32job.JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION;** 


## JOB_OBJECT_LIMIT_JOB_MEMORY
 **const win32job.JOB_OBJECT_LIMIT_JOB_MEMORY;** 


## JOB_OBJECT_LIMIT_JOB_TIME
 **const win32job.JOB_OBJECT_LIMIT_JOB_TIME;** 


## JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
 **const win32job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;** 


## JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME
 **const win32job.JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME;** 


## JOB_OBJECT_LIMIT_PRIORITY_CLASS
 **const win32job.JOB_OBJECT_LIMIT_PRIORITY_CLASS;** 


## JOB_OBJECT_LIMIT_PROCESS_MEMORY
 **const win32job.JOB_OBJECT_LIMIT_PROCESS_MEMORY;** 


## JOB_OBJECT_LIMIT_PROCESS_TIME
 **const win32job.JOB_OBJECT_LIMIT_PROCESS_TIME;** 


## JOB_OBJECT_LIMIT_SCHEDULING_CLASS
 **const win32job.JOB_OBJECT_LIMIT_SCHEDULING_CLASS;** 


## JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK
 **const win32job.JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK;** 


## JOB_OBJECT_LIMIT_VALID_FLAGS
 **const win32job.JOB_OBJECT_LIMIT_VALID_FLAGS;** 


## JOB_OBJECT_LIMIT_WORKINGSET
 **const win32job.JOB_OBJECT_LIMIT_WORKINGSET;** 


## JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS
 **const win32job.JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS;** 


## JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT
 **const win32job.JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT;** 


## JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO
 **const win32job.JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO;** 


## JOB_OBJECT_MSG_END_OF_JOB_TIME
 **const win32job.JOB_OBJECT_MSG_END_OF_JOB_TIME;** 


## JOB_OBJECT_MSG_END_OF_PROCESS_TIME
 **const win32job.JOB_OBJECT_MSG_END_OF_PROCESS_TIME;** 


## JOB_OBJECT_MSG_EXIT_PROCESS
 **const win32job.JOB_OBJECT_MSG_EXIT_PROCESS;** 


## JOB_OBJECT_MSG_JOB_MEMORY_LIMIT
 **const win32job.JOB_OBJECT_MSG_JOB_MEMORY_LIMIT;** 


## JOB_OBJECT_MSG_NEW_PROCESS
 **const win32job.JOB_OBJECT_MSG_NEW_PROCESS;** 


## JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT
 **const win32job.JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT;** 


## JOB_OBJECT_POST_AT_END_OF_JOB
 **const win32job.JOB_OBJECT_POST_AT_END_OF_JOB;** 


## JOB_OBJECT_QUERY
 **const win32job.JOB_OBJECT_QUERY;** 


## JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS
 **const win32job.JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS;** 


## JOB_OBJECT_SECURITY_FILTER_TOKENS
 **const win32job.JOB_OBJECT_SECURITY_FILTER_TOKENS;** 


## JOB_OBJECT_SECURITY_NO_ADMIN
 **const win32job.JOB_OBJECT_SECURITY_NO_ADMIN;** 


## JOB_OBJECT_SECURITY_ONLY_TOKEN
 **const win32job.JOB_OBJECT_SECURITY_ONLY_TOKEN;** 


## JOB_OBJECT_SECURITY_RESTRICTED_TOKEN
 **const win32job.JOB_OBJECT_SECURITY_RESTRICTED_TOKEN;** 


## JOB_OBJECT_SECURITY_VALID_FLAGS
 **const win32job.JOB_OBJECT_SECURITY_VALID_FLAGS;** 


## JOB_OBJECT_SET_ATTRIBUTES
 **const win32job.JOB_OBJECT_SET_ATTRIBUTES;** 


## JOB_OBJECT_SET_SECURITY_ATTRIBUTES
 **const win32job.JOB_OBJECT_SET_SECURITY_ATTRIBUTES;** 


## JOB_OBJECT_TERMINATE
 **const win32job.JOB_OBJECT_TERMINATE;** 


## JOB_OBJECT_TERMINATE_AT_END_OF_JOB
 **const win32job.JOB_OBJECT_TERMINATE_AT_END_OF_JOB;** 


## JOB_OBJECT_UILIMIT_ALL
 **const win32job.JOB_OBJECT_UILIMIT_ALL;** 


## JOB_OBJECT_UILIMIT_DESKTOP
 **const win32job.JOB_OBJECT_UILIMIT_DESKTOP;** 


## JOB_OBJECT_UILIMIT_DISPLAYSETTINGS
 **const win32job.JOB_OBJECT_UILIMIT_DISPLAYSETTINGS;** 


## JOB_OBJECT_UILIMIT_EXITWINDOWS
 **const win32job.JOB_OBJECT_UILIMIT_EXITWINDOWS;** 


## JOB_OBJECT_UILIMIT_GLOBALATOMS
 **const win32job.JOB_OBJECT_UILIMIT_GLOBALATOMS;** 


## JOB_OBJECT_UILIMIT_HANDLES
 **const win32job.JOB_OBJECT_UILIMIT_HANDLES;** 


## JOB_OBJECT_UILIMIT_NONE
 **const win32job.JOB_OBJECT_UILIMIT_NONE;** 


## JOB_OBJECT_UILIMIT_READCLIPBOARD
 **const win32job.JOB_OBJECT_UILIMIT_READCLIPBOARD;** 


## JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS
 **const win32job.JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS;** 


## JOB_OBJECT_UILIMIT_WRITECLIPBOARD
 **const win32job.JOB_OBJECT_UILIMIT_WRITECLIPBOARD;** 


## JOB_OBJECT_UI_VALID_FLAGS
 **const win32job.JOB_OBJECT_UI_VALID_FLAGS;** 


## JobObjectAssociateCompletionPortInformation
 **const win32job.JobObjectAssociateCompletionPortInformation;** 


## JobObjectBasicAccountingInformation
 **const win32job.JobObjectBasicAccountingInformation;** 


## JobObjectBasicAndIoAccountingInformation
 **const win32job.JobObjectBasicAndIoAccountingInformation;** 


## JobObjectBasicLimitInformation
 **const win32job.JobObjectBasicLimitInformation;** 


## JobObjectBasicProcessIdList
 **const win32job.JobObjectBasicProcessIdList;** 


## JobObjectBasicUIRestrictions
 **const win32job.JobObjectBasicUIRestrictions;** 


## JobObjectEndOfJobTimeInformation
 **const win32job.JobObjectEndOfJobTimeInformation;** 


## JobObjectExtendedLimitInformation
 **const win32job.JobObjectExtendedLimitInformation;** 


## JobObjectJobSetInformation
 **const win32job.JobObjectJobSetInformation;** 


## JobObjectSecurityLimitInformation
 **const win32job.JobObjectSecurityLimitInformation;** 


## MaxJobObjectInfoClass
 **const win32job.MaxJobObjectInfoClass;** 


## [win32job](#README.md#win32job).OpenJobObject

 **OpenJobObject( *desiredAccess*  *, inheritHandles*  *, name* ** )
Opens an existing job object.

#### Parameters


     *desiredAccess* : int

    

     *inheritHandles* : bool

    

     *name* : unicode

    

## [win32job](#README.md#win32job).QueryInformationJobObject

dict = **QueryInformationJobObject( *Job*  *, JobObjectInfoClass* ** )
Retrieves limit and job state information from the job object.

#### Parameters


     *Job* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a job, use None for job that calling process is part of

     *JobObjectInfoClass* : int

    The type of data required, one of JobObject* values

 **JobObjectInfoClass**  **Type of information returned** JobObjectBasicAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_ACCOUNTING_INFORMATION structJobObjectBasicAndIoAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION structJobObjectBasicLimitInformationReturns a dict representing a JOBOBJECT_BASIC_LIMIT_INFORMATION structJobObjectExtendedLimitInformationReturns a dict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION structJobObjectEndOfJobTimeInformationReturns a dict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION structJobObjectBasicUIRestrictionsReturns a dict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS structJobObjectBasicProcessIdListReturns a sequence of pids of processes assigned to the jobJobObjectJobSetInformationReturns a dict representing a JOBOBJECT_JOBSET_INFORMATION struct (not documented on MSDN)JobObjectSecurityLimitInformationJOBOBJECT_SECURITY_LIMIT_INFORMATION Not implementedJobObjectAssociateCompletionPortInformationJOBOBJECT_ASSOCIATE_COMPLETION_PORT Not implemented
#### Return Value
The type of the returned information is dependent on the class requested

## [win32job](#README.md#win32job).SetInformationJobObject

 **SetInformationJobObject( *Job*  *, JobObjectInfoClass*  *, JobObjectInfo* ** )
Sets quotas and limits for a job

#### Parameters


     *Job* :[PyHANDLE](#README.md#PyHANDLE)

    Handle to a job

     *JobObjectInfoClass* : int

    The type of data required, one of JobObject* values

     *JobObjectInfo* : dict

    Dictionary containing info to be set, as returned by[win32job::QueryInformationJobObject](#win32job.md#win32jobQueryInformationJobObject)


## [win32job](#README.md#win32job).TerminateJobObject

 **TerminateJobObject( *hJob*  *, exitCode* ** )
Terminates all processes currently associated with the job.

#### Parameters


     *hJob* :[PyHANDLE](#README.md#PyHANDLE)

    

     *exitCode* : int

    

## [win32job](#README.md#win32job).UserHandleGrantAccess

 **UserHandleGrantAccess( *hUserHandle*  *, hJob*  *, grant* ** )
Grants or denies access to a handle to a User object to a job that has a user-interface restriction.

#### Parameters


     *hUserHandle* :[PyHANDLE](#README.md#PyHANDLE)

    

     *hJob* :[PyHANDLE](#README.md#PyHANDLE)

    

     *grant* : bool

    