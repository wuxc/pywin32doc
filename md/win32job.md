# win32job

## Module win32job



An interface to the win32 Process and Thread API's, 

available in Windows 2000 and later\.

#### Methods


  - [AssignProcessToJobObject](win32job.md#win32jobassignprocesstojobobject)

    Associates a process with an existing job object\.&nbsp;

  - [CreateJobObject](win32job.md#win32jobcreatejobobject)

    Creates or opens a job object\.&nbsp;

  - [OpenJobObject](win32job.md#win32jobopenjobobject)

    Opens an existing job object\.&nbsp;

  - [TerminateJobObject](win32job.md#win32jobterminatejobobject)

    Terminates all processes currently associated with the job\.&nbsp;

  - [UserHandleGrantAccess](win32job.md#win32jobuserhandlegrantaccess)

    Grants or denies access to a handle to a User object to a job that has a user-interface restriction\.&nbsp;

  - [IsProcessInJob](win32job.md#win32jobisprocessinjob)

    Determines if the process is running in the specified job\.&nbsp;

  - [QueryInformationJobObject](win32job.md#win32jobqueryinformationjobobject)

    Retrieves limit and job state information from the job object\.&nbsp;

  - [SetInformationJobObject](win32job.md#win32jobsetinformationjobobject)

    Sets quotas and limits for a job&nbsp;

## [win32job](#win32job)\.AssignProcessToJobObject

AssignProcessToJobObject\(hJob, hProcess\)
Associates a process with an existing job object\.

#### Parameters


  - hJob :[PyHANDLE](#pyhandle)

    

  - hProcess :[PyHANDLE](#pyhandle)

    

## [win32job](#win32job)\.CreateJobObject

CreateJobObject\(jobAttributes, name\)
Creates or opens a job object\.

#### Parameters


  - jobAttributes :[PySECURITY\_ATTRIBUTES](PySECURITY.md#pysecurityattributes)

    

  - name : unicode

    

## [win32job](#win32job)\.IsProcessInJob



boolean =IsProcessInJob\(hProcess, hJob\)
Determines if the process is running in the specified job\.

#### Parameters


  - hProcess :[PyHANDLE](#pyhandle)

    Handle to a process

  - hJob :[PyHANDLE](#pyhandle)

    Handle to a job, use None to check if process is part of any job

#### Comments


Function is only available on WinXP and later

## JOB\_OBJECT\_ALL\_ACCESS
const win32job\.JOB\_OBJECT\_ALL\_ACCESS;


## JOB\_OBJECT\_ASSIGN\_PROCESS
const win32job\.JOB\_OBJECT\_ASSIGN\_PROCESS;


## JOB\_OBJECT\_BASIC\_LIMIT\_VALID\_FLAGS
const win32job\.JOB\_OBJECT\_BASIC\_LIMIT\_VALID\_FLAGS;


## JOB\_OBJECT\_EXTENDED\_LIMIT\_VALID\_FLAGS
const win32job\.JOB\_OBJECT\_EXTENDED\_LIMIT\_VALID\_FLAGS;


## JOB\_OBJECT\_LIMIT\_ACTIVE\_PROCESS
const win32job\.JOB\_OBJECT\_LIMIT\_ACTIVE\_PROCESS;


## JOB\_OBJECT\_LIMIT\_AFFINITY
const win32job\.JOB\_OBJECT\_LIMIT\_AFFINITY;


## JOB\_OBJECT\_LIMIT\_BREAKAWAY\_OK
const win32job\.JOB\_OBJECT\_LIMIT\_BREAKAWAY\_OK;


## JOB\_OBJECT\_LIMIT\_DIE\_ON\_UNHANDLED\_EXCEPTION
const win32job\.JOB\_OBJECT\_LIMIT\_DIE\_ON\_UNHANDLED\_EXCEPTION;


## JOB\_OBJECT\_LIMIT\_JOB\_MEMORY
const win32job\.JOB\_OBJECT\_LIMIT\_JOB\_MEMORY;


## JOB\_OBJECT\_LIMIT\_JOB\_TIME
const win32job\.JOB\_OBJECT\_LIMIT\_JOB\_TIME;


## JOB\_OBJECT\_LIMIT\_KILL\_ON\_JOB\_CLOSE
const win32job\.JOB\_OBJECT\_LIMIT\_KILL\_ON\_JOB\_CLOSE;


## JOB\_OBJECT\_LIMIT\_PRESERVE\_JOB\_TIME
const win32job\.JOB\_OBJECT\_LIMIT\_PRESERVE\_JOB\_TIME;


## JOB\_OBJECT\_LIMIT\_PRIORITY\_CLASS
const win32job\.JOB\_OBJECT\_LIMIT\_PRIORITY\_CLASS;


## JOB\_OBJECT\_LIMIT\_PROCESS\_MEMORY
const win32job\.JOB\_OBJECT\_LIMIT\_PROCESS\_MEMORY;


## JOB\_OBJECT\_LIMIT\_PROCESS\_TIME
const win32job\.JOB\_OBJECT\_LIMIT\_PROCESS\_TIME;


## JOB\_OBJECT\_LIMIT\_SCHEDULING\_CLASS
const win32job\.JOB\_OBJECT\_LIMIT\_SCHEDULING\_CLASS;


## JOB\_OBJECT\_LIMIT\_SILENT\_BREAKAWAY\_OK
const win32job\.JOB\_OBJECT\_LIMIT\_SILENT\_BREAKAWAY\_OK;


## JOB\_OBJECT\_LIMIT\_VALID\_FLAGS
const win32job\.JOB\_OBJECT\_LIMIT\_VALID\_FLAGS;


## JOB\_OBJECT\_LIMIT\_WORKINGSET
const win32job\.JOB\_OBJECT\_LIMIT\_WORKINGSET;


## JOB\_OBJECT\_MSG\_ABNORMAL\_EXIT\_PROCESS
const win32job\.JOB\_OBJECT\_MSG\_ABNORMAL\_EXIT\_PROCESS;


## JOB\_OBJECT\_MSG\_ACTIVE\_PROCESS\_LIMIT
const win32job\.JOB\_OBJECT\_MSG\_ACTIVE\_PROCESS\_LIMIT;


## JOB\_OBJECT\_MSG\_ACTIVE\_PROCESS\_ZERO
const win32job\.JOB\_OBJECT\_MSG\_ACTIVE\_PROCESS\_ZERO;


## JOB\_OBJECT\_MSG\_END\_OF\_JOB\_TIME
const win32job\.JOB\_OBJECT\_MSG\_END\_OF\_JOB\_TIME;


## JOB\_OBJECT\_MSG\_END\_OF\_PROCESS\_TIME
const win32job\.JOB\_OBJECT\_MSG\_END\_OF\_PROCESS\_TIME;


## JOB\_OBJECT\_MSG\_EXIT\_PROCESS
const win32job\.JOB\_OBJECT\_MSG\_EXIT\_PROCESS;


## JOB\_OBJECT\_MSG\_JOB\_MEMORY\_LIMIT
const win32job\.JOB\_OBJECT\_MSG\_JOB\_MEMORY\_LIMIT;


## JOB\_OBJECT\_MSG\_NEW\_PROCESS
const win32job\.JOB\_OBJECT\_MSG\_NEW\_PROCESS;


## JOB\_OBJECT\_MSG\_PROCESS\_MEMORY\_LIMIT
const win32job\.JOB\_OBJECT\_MSG\_PROCESS\_MEMORY\_LIMIT;


## JOB\_OBJECT\_POST\_AT\_END\_OF\_JOB
const win32job\.JOB\_OBJECT\_POST\_AT\_END\_OF\_JOB;


## JOB\_OBJECT\_QUERY
const win32job\.JOB\_OBJECT\_QUERY;


## JOB\_OBJECT\_RESERVED\_LIMIT\_VALID\_FLAGS
const win32job\.JOB\_OBJECT\_RESERVED\_LIMIT\_VALID\_FLAGS;


## JOB\_OBJECT\_SECURITY\_FILTER\_TOKENS
const win32job\.JOB\_OBJECT\_SECURITY\_FILTER\_TOKENS;


## JOB\_OBJECT\_SECURITY\_NO\_ADMIN
const win32job\.JOB\_OBJECT\_SECURITY\_NO\_ADMIN;


## JOB\_OBJECT\_SECURITY\_ONLY\_TOKEN
const win32job\.JOB\_OBJECT\_SECURITY\_ONLY\_TOKEN;


## JOB\_OBJECT\_SECURITY\_RESTRICTED\_TOKEN
const win32job\.JOB\_OBJECT\_SECURITY\_RESTRICTED\_TOKEN;


## JOB\_OBJECT\_SECURITY\_VALID\_FLAGS
const win32job\.JOB\_OBJECT\_SECURITY\_VALID\_FLAGS;


## JOB\_OBJECT\_SET\_ATTRIBUTES
const win32job\.JOB\_OBJECT\_SET\_ATTRIBUTES;


## JOB\_OBJECT\_SET\_SECURITY\_ATTRIBUTES
const win32job\.JOB\_OBJECT\_SET\_SECURITY\_ATTRIBUTES;


## JOB\_OBJECT\_TERMINATE
const win32job\.JOB\_OBJECT\_TERMINATE;


## JOB\_OBJECT\_TERMINATE\_AT\_END\_OF\_JOB
const win32job\.JOB\_OBJECT\_TERMINATE\_AT\_END\_OF\_JOB;


## JOB\_OBJECT\_UILIMIT\_ALL
const win32job\.JOB\_OBJECT\_UILIMIT\_ALL;


## JOB\_OBJECT\_UILIMIT\_DESKTOP
const win32job\.JOB\_OBJECT\_UILIMIT\_DESKTOP;


## JOB\_OBJECT\_UILIMIT\_DISPLAYSETTINGS
const win32job\.JOB\_OBJECT\_UILIMIT\_DISPLAYSETTINGS;


## JOB\_OBJECT\_UILIMIT\_EXITWINDOWS
const win32job\.JOB\_OBJECT\_UILIMIT\_EXITWINDOWS;


## JOB\_OBJECT\_UILIMIT\_GLOBALATOMS
const win32job\.JOB\_OBJECT\_UILIMIT\_GLOBALATOMS;


## JOB\_OBJECT\_UILIMIT\_HANDLES
const win32job\.JOB\_OBJECT\_UILIMIT\_HANDLES;


## JOB\_OBJECT\_UILIMIT\_NONE
const win32job\.JOB\_OBJECT\_UILIMIT\_NONE;


## JOB\_OBJECT\_UILIMIT\_READCLIPBOARD
const win32job\.JOB\_OBJECT\_UILIMIT\_READCLIPBOARD;


## JOB\_OBJECT\_UILIMIT\_SYSTEMPARAMETERS
const win32job\.JOB\_OBJECT\_UILIMIT\_SYSTEMPARAMETERS;


## JOB\_OBJECT\_UILIMIT\_WRITECLIPBOARD
const win32job\.JOB\_OBJECT\_UILIMIT\_WRITECLIPBOARD;


## JOB\_OBJECT\_UI\_VALID\_FLAGS
const win32job\.JOB\_OBJECT\_UI\_VALID\_FLAGS;


## JobObjectAssociateCompletionPortInformation
const win32job\.JobObjectAssociateCompletionPortInformation;


## JobObjectBasicAccountingInformation
const win32job\.JobObjectBasicAccountingInformation;


## JobObjectBasicAndIoAccountingInformation
const win32job\.JobObjectBasicAndIoAccountingInformation;


## JobObjectBasicLimitInformation
const win32job\.JobObjectBasicLimitInformation;


## JobObjectBasicProcessIdList
const win32job\.JobObjectBasicProcessIdList;


## JobObjectBasicUIRestrictions
const win32job\.JobObjectBasicUIRestrictions;


## JobObjectEndOfJobTimeInformation
const win32job\.JobObjectEndOfJobTimeInformation;


## JobObjectExtendedLimitInformation
const win32job\.JobObjectExtendedLimitInformation;


## JobObjectJobSetInformation
const win32job\.JobObjectJobSetInformation;


## JobObjectSecurityLimitInformation
const win32job\.JobObjectSecurityLimitInformation;


## MaxJobObjectInfoClass
const win32job\.MaxJobObjectInfoClass;


## [win32job](#win32job)\.OpenJobObject

OpenJobObject\(desiredAccess, inheritHandles, name\)
Opens an existing job object\.

#### Parameters


  - desiredAccess : int

    

  - inheritHandles : bool

    

  - name : unicode

    

## [win32job](#win32job)\.QueryInformationJobObject



dict =QueryInformationJobObject\(Job, JobObjectInfoClass\)
Retrieves limit and job state information from the job object\.

#### Parameters


  - Job :[PyHANDLE](#pyhandle)

    Handle to a job, use None for job that calling process is part of

  - JobObjectInfoClass : int

    The type of data required, one of JobObject\* values

JobObjectInfoClassType of information returnedJobObjectBasicAccountingInformationReturns a dict representing a JOBOBJECT\_BASIC\_ACCOUNTING\_INFORMATION structJobObjectBasicAndIoAccountingInformationReturns a dict representing a JOBOBJECT\_BASIC\_AND\_IO\_ACCOUNTING\_INFORMATION structJobObjectBasicLimitInformationReturns a dict representing a JOBOBJECT\_BASIC\_LIMIT\_INFORMATION structJobObjectExtendedLimitInformationReturns a dict representing a JOBOBJECT\_EXTENDED\_LIMIT\_INFORMATION structJobObjectEndOfJobTimeInformationReturns a dict representing a JOBOBJECT\_END\_OF\_JOB\_TIME\_INFORMATION structJobObjectBasicUIRestrictionsReturns a dict representing a JOBOBJECT\_BASIC\_UI\_RESTRICTIONS structJobObjectBasicProcessIdListReturns a sequence of pids of processes assigned to the jobJobObjectJobSetInformationReturns a dict representing a JOBOBJECT\_JOBSET\_INFORMATION struct \(not documented on MSDN\)JobObjectSecurityLimitInformationJOBOBJECT\_SECURITY\_LIMIT\_INFORMATION Not implementedJobObjectAssociateCompletionPortInformationJOBOBJECT\_ASSOCIATE\_COMPLETION\_PORT Not implemented
#### Return Value
The type of the returned information is dependent on the class requested

## [win32job](#win32job)\.SetInformationJobObject

SetInformationJobObject\(Job, JobObjectInfoClass, JobObjectInfo\)
Sets quotas and limits for a job

#### Parameters


  - Job :[PyHANDLE](#pyhandle)

    Handle to a job

  - JobObjectInfoClass : int

    The type of data required, one of JobObject\* values

  - JobObjectInfo : dict

    Dictionary containing info to be set, as returned by[win32job::QueryInformationJobObject](win32job.md#win32jobqueryinformationjobobject)


## [win32job](#win32job)\.TerminateJobObject

TerminateJobObject\(hJob, exitCode\)
Terminates all processes currently associated with the job\.

#### Parameters


  - hJob :[PyHANDLE](#pyhandle)

    

  - exitCode : int

    

## [win32job](#win32job)\.UserHandleGrantAccess

UserHandleGrantAccess\(hUserHandle, hJob, grant\)
Grants or denies access to a handle to a User object to a job that has a user-interface restriction\.

#### Parameters


  - hUserHandle :[PyHANDLE](#pyhandle)

    

  - hJob :[PyHANDLE](#pyhandle)

    

  - grant : bool

    