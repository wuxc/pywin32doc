# pywin32doc

##[win32process](md/win32process.md)

## Module win32process

An interface to the win32 Process and Thread API's

#### Methods


    [STARTUPINFO](#win32process.md#win32processSTARTUPINFO)

    Creates a new STARTUPINFO object.&nbsp;

    [beginthreadex](#win32process.md#win32processbeginthreadex)

    Creates a new thread&nbsp;

    [CreateRemoteThread](#win32process.md#win32processCreateRemoteThread)

    creates a thread that runs in 

the virtual address space of another process.&nbsp;

    [CreateProcess](#win32process.md#win32processCreateProcess)

    Creates a new process and its primary thread. The new process executes the specified executable file.&nbsp;

    [CreateProcessAsUser](#win32process.md#win32processCreateProcessAsUser)

    Creates a new process in the context of the specified user.&nbsp;

    [GetCurrentProcess](#win32process.md#win32processGetCurrentProcess)

    Retrieves a pseudo handle for the current process.&nbsp;

    [GetProcessVersion](#win32process.md#win32processGetProcessVersion)

    Obtains the major and minor version numbers of the system on which a specified process expects to run.&nbsp;

    [GetCurrentProcessId](#win32process.md#win32processGetCurrentProcessId)

    Retrieves the process identifier of the calling process.&nbsp;

    [GetStartupInfo](#win32process.md#win32processGetStartupInfo)

    Retrieves the contents of the STARTUPINFO structure that was specified when the calling process was created.&nbsp;

    [GetPriorityClass](#win32process.md#win32processGetPriorityClass)

    &nbsp;

    [GetExitCodeThread](#win32process.md#win32processGetExitCodeThread)

    &nbsp;

    [GetExitCodeProcess](#win32process.md#win32processGetExitCodeProcess)

    &nbsp;

    [GetWindowThreadProcessId](#win32process.md#win32processGetWindowThreadProcessId)

    Retrieves the identifier of the thread and process that created the specified window.&nbsp;

    [SetThreadPriority](#win32process.md#win32processSetThreadPriority)

    &nbsp;

    [GetThreadPriority](#win32process.md#win32processGetThreadPriority)

    &nbsp;

    [GetProcessPriorityBoost](#win32process.md#win32processGetProcessPriorityBoost)

    Determines if dynamic priority adjustment is enabled for a process&nbsp;

    [SetProcessPriorityBoost](#win32process.md#win32processSetProcessPriorityBoost)

    Enables or disables dynamic priority adjustment for a process&nbsp;

    [GetThreadPriorityBoost](#win32process.md#win32processGetThreadPriorityBoost)

    Determines if dynamic priority adjustment is enabled for a thread&nbsp;

    [SetThreadPriorityBoost](#win32process.md#win32processSetThreadPriorityBoost)

    Enables or disables dynamic priority adjustment for a thread&nbsp;

    [GetThreadIOPendingFlag](#win32process.md#win32processGetThreadIOPendingFlag)

    Determines if thread has any outstanding IO requests&nbsp;

    [GetThreadTimes](#win32process.md#win32processGetThreadTimes)

    Returns a thread's time statistics&nbsp;

    [GetProcessId](#win32process.md#win32processGetProcessId)

    Returns the Pid for a process handle&nbsp;

    [SetPriorityClass](#win32process.md#win32processSetPriorityClass)

    &nbsp;

    [AttachThreadInput](#win32process.md#win32processAttachThreadInput)

    Attaches or detaches the input of two threads&nbsp;

    [SetThreadIdealProcessor](#win32process.md#win32processSetThreadIdealProcessor)

    Used to specify a preferred processor for a thread. The system schedules threads on their preferred processors whenever possible.&nbsp;

    [GetProcessAffinityMask](#win32process.md#win32processGetProcessAffinityMask)

    Gets a processor affinity mask for a specified process&nbsp;

    [SetProcessAffinityMask](#win32process.md#win32processSetProcessAffinityMask)

    Sets a processor affinity mask for a specified process.&nbsp;

    [SetThreadAffinityMask](#win32process.md#win32processSetThreadAffinityMask)

    Sets a processor affinity mask for a specified thread.&nbsp;

    [SuspendThread](#win32process.md#win32processSuspendThread)

    Suspends the specified thread.&nbsp;

    [ResumeThread](#win32process.md#win32processResumeThread)

    Resumes the specified thread. When the suspend count is decremented to zero, the execution of the thread is resumed.&nbsp;

    [TerminateProcess](#win32process.md#win32processTerminateProcess)

    Terminates the specified process and all of its threads.&nbsp;

    [ExitProcess](#win32process.md#win32processExitProcess)

    Ends a process and all its threads&nbsp;

    [EnumProcesses](#win32process.md#win32processEnumProcesses)

    Returns Pids for currently running processes&nbsp;

    [EnumProcessModules](#win32process.md#win32processEnumProcessModules)

    Lists loaded modules for a process handle&nbsp;

    [EnumProcessModulesEx](#win32process.md#win32processEnumProcessModulesEx)

    Lists 32 or 64-bit modules load by a process&nbsp;

    [GetModuleFileNameEx](#win32process.md#win32processGetModuleFileNameEx)

    Return name of module loaded by another process (uses process handle, not pid)&nbsp;

    [GetProcessMemoryInfo](#win32process.md#win32processGetProcessMemoryInfo)

    Returns process memory statistics as a dict representing a PROCESS_MEMORY_COUNTERS struct&nbsp;

    [GetProcessTimes](#win32process.md#win32processGetProcessTimes)

    Retrieve time statics for a process by handle.  (KernelTime and UserTime in 100 nanosecond units)&nbsp;

    [GetProcessIoCounters](#win32process.md#win32processGetProcessIoCounters)

    Return I/O statistics for a process as a dictionary representing an IO_COUNTERS struct.&nbsp;

    [GetProcessWindowStation](#win32process.md#win32processGetProcessWindowStation)

    Returns a handle to the window station for the calling process&nbsp;

    [GetProcessWorkingSetSize](#win32process.md#win32processGetProcessWorkingSetSize)

    Returns min and max working set sizes for a process by handle&nbsp;

    [SetProcessWorkingSetSize](#win32process.md#win32processSetProcessWorkingSetSize)

    Sets minimum and maximum working set sizes for a process&nbsp;

    [GetProcessShutdownParameters](#win32process.md#win32processGetProcessShutdownParameters)

    Retrieves shutdown priority and flags for current process&nbsp;

    [SetProcessShutdownParameters](#win32process.md#win32processSetProcessShutdownParameters)

    Sets shutdown priority and flags for current process&nbsp;

    [GetGuiResources](#win32process.md#win32processGetGuiResources)

    Returns the number of GDI or user object handles held by a process&nbsp;

    [IsWow64Process](#win32process.md#win32processIsWow64Process)

    Determines whether the specified process is running under WOW64.&nbsp;
------

##[win32timezone](md/win32timezone.md)

## Module win32timezone

win32timezone: 

Module for handling datetime.tzinfo time zones using the windows 

registry for time zone information.  The time zone names are dependent 

on the registry entries defined by the operating system.

#### Comments
This module may be tested using the doctest module.
Written by Jason R. Coombs (jaraco@jaraco.com). 

Copyright &#194&#169 2003-2012. 

All Rights Reserved.
This module is licenced for use in Mark Hammond's pywin32 

library under the same terms as the pywin32 library.
To use this time zone module with the datetime module, simply pass 

the TimeZoneInfo object to the datetime constructor.  For example,
&gt&gt&gt import win32timezone, datetime

&gt&gt&gt assert 'Mountain Standard Time' in win32timezone.TimeZoneInfo.get_sorted_time_zone_names()

&gt&gt&gt MST = win32timezone.TimeZoneInfo('Mountain Standard Time')

&gt&gt&gt now = datetime.datetime.now(MST)
The now object is now a time-zone aware object, and daylight savings- 

aware methods may be called on it.
&gt&gt&gt now.utcoffset() in (datetime.timedelta(-1, 61200), datetime.timedelta(-1, 64800))

True
(note that the result of utcoffset call will be different based on when now was 

generated, unless standard time is always used)
&gt&gt&gt now = datetime.datetime.now(TimeZoneInfo('Mountain Standard Time', True))

&gt&gt&gt now.utcoffset()

datetime.timedelta(-1, 61200)
&gt&gt&gt aug2 = datetime.datetime(2003, 8, 2, tzinfo = MST)

&gt&gt&gt tuple(aug2.utctimetuple())

(2003, 8, 2, 6, 0, 0, 5, 214, 0)

&gt&gt&gt nov2 = datetime.datetime(2003, 11, 25, tzinfo = MST)

&gt&gt&gt tuple(nov2.utctimetuple())

(2003, 11, 25, 7, 0, 0, 1, 329, 0)
To convert from one timezone to another, just use the astimezone method.
&gt&gt&gt aug2.isoformat()

'2003-08-02T00:00:00-06:00'

&gt&gt&gt aug2est = aug2.astimezone(win32timezone.TimeZoneInfo('Eastern Standard Time'))

&gt&gt&gt aug2est.isoformat()

'2003-08-02T02:00:00-04:00'
calling the displayName member will return the display name as set in the 

registry.
&gt&gt&gt est = win32timezone.TimeZoneInfo('Eastern Standard Time')

&gt&gt&gt str(est.displayName)

'(UTC-05:00) Eastern Time (US & Canada)'
&gt&gt&gt gmt = win32timezone.TimeZoneInfo('GMT Standard Time', True)

&gt&gt&gt str(gmt.displayName)

'(UTC) Dublin, Edinburgh, Lisbon, London'
To get the complete list of available time zone keys,
&gt&gt&gt zones = win32timezone.TimeZoneInfo.get_all_time_zones()
If you want to get them in an order that's sorted longitudinally
&gt&gt&gt zones = win32timezone.TimeZoneInfo.get_sorted_time_zones()
TimeZoneInfo now supports being pickled and comparison
&gt&gt&gt import pickle

&gt&gt&gt tz = win32timezone.TimeZoneInfo('China Standard Time')

&gt&gt&gt tz == pickle.loads(pickle.dumps(tz))

True
It's possible to construct a TimeZoneInfo from a TimeZoneDescription 

including the currently-defined zone.
&gt&gt&gt tz = win32timezone.TimeZoneInfo(TimeZoneDefinition.current())

&gt&gt&gt tz == pickle.loads(pickle.dumps(tz))

True
&gt&gt&gt aest = win32timezone.TimeZoneInfo('AUS Eastern Standard Time')

&gt&gt&gt est = win32timezone.TimeZoneInfo('E. Australia Standard Time')

&gt&gt&gt dt = datetime.datetime(2006, 11, 11, 1, 0, 0, tzinfo = aest)

&gt&gt&gt estdt = dt.astimezone(est)

&gt&gt&gt estdt.strftime('%Y-%m-%d %H:%M:%S')

'2006-11-11 00:00:00'
&gt&gt&gt dt = datetime.datetime(2007, 1, 12, 1, 0, 0, tzinfo = aest)

&gt&gt&gt estdt = dt.astimezone(est)

&gt&gt&gt estdt.strftime('%Y-%m-%d %H:%M:%S')

'2007-01-12 00:00:00'
&gt&gt&gt dt = datetime.datetime(2007, 6, 13, 1, 0, 0, tzinfo = aest)

&gt&gt&gt estdt = dt.astimezone(est)

&gt&gt&gt estdt.strftime('%Y-%m-%d %H:%M:%S')

'2007-06-13 01:00:00'
Microsoft now has a patch for handling time zones in 2007 (see 

http://support.microsoft.com/gp/cp_dst)
As a result, patched systems will give an incorrect result for 

dates prior to the designated year except for Vista and its 

successors, which have dynamic time zone support.
&gt&gt&gt nov2_pre_change = datetime.datetime(2003, 11, 2, tzinfo = MST)

&gt&gt&gt old_response = (2003, 11, 2, 7, 0, 0, 6, 306, 0)

&gt&gt&gt incorrect_patch_response = (2003, 11, 2, 6, 0, 0, 6, 306, 0)

&gt&gt&gt pre_response = nov2_pre_change.utctimetuple()

&gt&gt&gt pre_response in (old_response, incorrect_patch_response)

True
Furthermore, unpatched systems pre-Vista will give an incorrect 

result for dates after 2007.
&gt&gt&gt nov2_post_change = datetime.datetime(2007, 11, 2, tzinfo = MST)

&gt&gt&gt incorrect_unpatched_response = (2007, 11, 2, 7, 0, 0, 4, 306, 0)

&gt&gt&gt new_response = (2007, 11, 2, 6, 0, 0, 4, 306, 0)

&gt&gt&gt post_response = nov2_post_change.utctimetuple()

&gt&gt&gt post_response in (new_response, incorrect_unpatched_response)

True
There is a function you can call to get some capabilities of the time 

zone data.
&gt&gt&gt caps = GetTZCapabilities()

&gt&gt&gt isinstance(caps, dict)

True

&gt&gt&gt 'MissingTZPatch' in caps

True

&gt&gt&gt 'DynamicTZSupport' in caps

True
&gt&gt&gt both_dates_correct = (pre_response == old_response and post_response == new_response)

&gt&gt&gt old_dates_wrong = (pre_response == incorrect_patch_response)

&gt&gt&gt new_dates_wrong = (post_response == incorrect_unpatched_response)
&gt&gt&gt caps['DynamicTZSupport'] == both_dates_correct

True
&gt&gt&gt (not caps['DynamicTZSupport'] and caps['MissingTZPatch']) == new_dates_wrong

True
&gt&gt&gt (not caps['DynamicTZSupport'] and not caps['MissingTZPatch']) == old_dates_wrong

True
This test helps ensure language support for unicode characters
&gt&gt&gt x = TIME_ZONE_INFORMATION(0, u'fran&#195&#167ais')
Test conversion from one time zone to another at a DST boundary
&gt&gt&gt tz_hi = TimeZoneInfo('Hawaiian Standard Time')

&gt&gt&gt tz_pac = TimeZoneInfo('Pacific Standard Time')

&gt&gt&gt time_before = datetime.datetime(2011, 11, 5, 15, 59, 59, tzinfo=tz_hi)

&gt&gt&gt tz_hi.utcoffset(time_before)

datetime.timedelta(-1, 50400)

&gt&gt&gt tz_hi.dst(time_before)

datetime.timedelta(0)
Hawaii doesn't need dynamic TZ info
&gt&gt&gt getattr(tz_hi, 'dynamicInfo', None)
Here's a time that gave some trouble as reported in #3523104 

because one minute later, the equivalent UTC time changes from DST 

in the U.S.
&gt&gt&gt dt_hi = datetime.datetime(2011, 11, 5, 15, 59, 59, 0, tzinfo=tz_hi)

&gt&gt&gt dt_hi.timetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=5, tm_hour=15, tm_min=59, tm_sec=59, tm_wday=5, tm_yday=309, tm_isdst=0)

&gt&gt&gt dt_hi.utctimetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=6, tm_hour=1, tm_min=59, tm_sec=59, tm_wday=6, tm_yday=310, tm_isdst=0)
Convert the time to pacific time.
&gt&gt&gt dt_pac = dt_hi.astimezone(tz_pac)

&gt&gt&gt dt_pac.timetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=5, tm_hour=18, tm_min=59, tm_sec=59, tm_wday=5, tm_yday=309, tm_isdst=1)
Notice that the UTC time is almost 2am.
&gt&gt&gt dt_pac.utctimetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=6, tm_hour=1, tm_min=59, tm_sec=59, tm_wday=6, tm_yday=310, tm_isdst=0)
Now do the same tests one minute later in Hawaii.
&gt&gt&gt time_after = datetime.datetime(2011, 11, 5, 16, 0, 0, 0, tzinfo=tz_hi)

&gt&gt&gt tz_hi.utcoffset(time_after)

datetime.timedelta(-1, 50400)

&gt&gt&gt tz_hi.dst(time_before)

datetime.timedelta(0)
&gt&gt&gt dt_hi = datetime.datetime(2011, 11, 5, 16, 0, 0, 0, tzinfo=tz_hi)

&gt&gt&gt print dt_hi.timetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=5, tm_hour=16, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=309, tm_isdst=0)

&gt&gt&gt print dt_hi.utctimetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=6, tm_hour=2, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=310, tm_isdst=0)
According to the docs, this is what astimezone does.
&gt&gt&gt utc = (dt_hi - dt_hi.utcoffset()).replace(tzinfo=tz_pac)

&gt&gt&gt utc

datetime.datetime(2011, 11, 6, 2, 0, tzinfo=TimeZoneInfo('Pacific Standard Time'))

&gt&gt&gt tz_pac.fromutc(utc) == dt_hi.astimezone(tz_pac)

True

&gt&gt&gt tz_pac.fromutc(utc)

datetime.datetime(2011, 11, 5, 19, 0, tzinfo=TimeZoneInfo('Pacific Standard Time'))
Make sure the converted time is correct.
&gt&gt&gt dt_pac = dt_hi.astimezone(tz_pac)

&gt&gt&gt dt_pac.timetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=5, tm_hour=19, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=309, tm_isdst=1)

&gt&gt&gt dt_pac.utctimetuple()

time.struct_time(tm_year=2011, tm_mon=11, tm_mday=6, tm_hour=2, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=310, tm_isdst=0)
Check some internal methods
&gt&gt&gt tz_pac._getStandardBias(datetime.datetime(2011, 1, 1))

datetime.timedelta(0, 28800)

&gt&gt&gt tz_pac._getDaylightBias(datetime.datetime(2011, 1, 1))

datetime.timedelta(0, 25200)
Test the offsets
&gt&gt&gt offset = tz_pac.utcoffset(datetime.datetime(2011, 11, 6, 2, 0))

&gt&gt&gt offset == datetime.timedelta(hours=-8)

True

&gt&gt&gt dst_offset = tz_pac.dst(datetime.datetime(2011, 11, 6, 2, 0) + offset)

&gt&gt&gt dst_offset == datetime.timedelta(hours=1)

True

&gt&gt&gt (offset + dst_offset) == datetime.timedelta(hours=-7)

True
Test offsets that occur right at the DST changeover
&gt&gt&gt datetime.datetime.utcfromtimestamp(1320570000).replace(

...     tzinfo=TimeZoneInfo.utc()).astimezone(tz_pac)

datetime.datetime(2011, 11, 6, 1, 0, tzinfo=TimeZoneInfo('Pacific Standard Time'))

#### Methods


    [GetTZCapabilities](#win32timezone.md#win32timezoneGetTZCapabilities)

    Run a few known tests to determine the capabilities of the time zone database&nbsp;

    [GetSortedTimeZoneNames](#win32timezone.md#win32timezoneGetSortedTimeZoneNames)

    Return a list of time zone names that can be used to initialize TimeZoneInfo instances&nbsp;

    [now](#win32timezone.md#win32timezonenow)

    Return the local time now with timezone awareness as enabled&nbsp;

    [resolveMUITimeZone](#win32timezone.md#win32timezoneresolveMUITimeZone)

    Resolve a multilingual user interface resource for the time zone name&nbsp;

    [deprecated](#win32timezone.md#win32timezonedeprecated)

    This is a decorator which can be used to mark functions&nbsp;

    [utcnow](#win32timezone.md#win32timezoneutcnow)

    Return the UTC time now with timezone awareness as enabled&nbsp;

#### Classes


    [TimeZoneInfo](#README.md#win32timezone.TimeZoneInfo)

    Main class for handling Windows time zones.&nbsp;

    [TimeZoneDefinition](#README.md#win32timezone.TimeZoneDefinition)

    A time zone definition class based on the win32&nbsp;

    [RangeMap](#README.md#win32timezone.RangeMap)

    A dictionary-like object that uses the keys as bounds for a range.&nbsp;
------

##[win32security](md/win32security.md)

## Module win32security

An interface to the win32 security API's

#### Methods


    [DsGetSpn](#win32security.md#win32securityDsGetSpn)

    Compose one or more service principal names to be registered using[win32security::DsWriteAccountSpn](#win32security.md#win32securityDsWriteAccountSpn)&nbsp;

    [DsWriteAccountSpn](#win32security.md#win32securityDsWriteAccountSpn)

    Associates a set of service principal names with an account&nbsp;

    [DsBind](#win32security.md#win32securityDsBind)

    Creates a connection to a directory service&nbsp;

    [DsUnBind](#win32security.md#win32securityDsUnBind)

    Closes a directory services handle created by[win32security::DsBind](#win32security.md#win32securityDsBind)&nbsp;

    [DsGetDcName](#win32security.md#win32securityDsGetDcName)

    Returns the name of a domain controller (DC) in a specified domain. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.&nbsp;

    [DsCrackNames](#win32security.md#win32securityDsCrackNames)

    Converts an array of directory service object names from one format to another.&nbsp;

    [DsListInfoForServer](#win32security.md#win32securityDsListInfoForServer)

    Lists miscellaneous information for a server.&nbsp;

    [DsListServersInSite](#win32security.md#win32securityDsListServersInSite)

    &nbsp;

    [DsListServersInSite](#win32security.md#win32securityDsListServersInSite)

    &nbsp;

    [DsListServersInSite](#win32security.md#win32securityDsListServersInSite)

    &nbsp;

    [DsListRoles](#win32security.md#win32securityDsListRoles)

    &nbsp;

    [DsListDomainsInSite](#win32security.md#win32securityDsListDomainsInSite)

    &nbsp;

    [ACL](#win32security.md#win32securityACL)

    Creates a new[PyACL](#README.md#PyACL)object.&nbsp;

    [SID](#win32security.md#win32securitySID)

    Creates a new[PySID](#README.md#PySID)object.&nbsp;

    [SECURITY_ATTRIBUTES](#win32security.md#win32securitySECURITY_ATTRIBUTES)

    Creates a new[PySECURITY_ATTRIBUTES](#PySECURITY.md#PySECURITYATTRIBUTES)object.&nbsp;

    [SECURITY_DESCRIPTOR](#win32security.md#win32securitySECURITY_DESCRIPTOR)

    Creates a new[PySECURITY_DESCRIPTOR](#PySECURITY.md#PySECURITYDESCRIPTOR)object.&nbsp;

    [ImpersonateNamedPipeClient](#win32security.md#win32securityImpersonateNamedPipeClient)

    Impersonates a named-pipe client application.&nbsp;

    [ImpersonateLoggedOnUser](#win32security.md#win32securityImpersonateLoggedOnUser)

    Impersonates a logged on user.&nbsp;

    [ImpersonateAnonymousToken](#win32security.md#win32securityImpersonateAnonymousToken)

    Cause a thread to act in the security context of an anonymous token&nbsp;

    [IsTokenRestricted](#win32security.md#win32securityIsTokenRestricted)

    Checks if a token contains restricted sids&nbsp;

    [RevertToSelf](#win32security.md#win32securityRevertToSelf)

    Terminates the impersonation of a client application.&nbsp;

    [LogonUser](#win32security.md#win32securityLogonUser)

    Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.&nbsp;

    [LogonUserEx](#win32security.md#win32securityLogonUserEx)

    Log a user onto the local machine,&nbsp;

    [LookupAccountName](#win32security.md#win32securityLookupAccountName)

    Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.&nbsp;

    [LookupAccountSid](#win32security.md#win32securityLookupAccountSid)

    Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.&nbsp;

    [GetBinarySid](#win32security.md#win32securityGetBinarySid)

    Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.&nbsp;

    [SetSecurityInfo](#win32security.md#win32securitySetSecurityInfo)

    Sets security info for an object by handle&nbsp;

    [GetSecurityInfo](#win32security.md#win32securityGetSecurityInfo)

    Retrieve security info for an object by handle&nbsp;

    [SetNamedSecurityInfo](#win32security.md#win32securitySetNamedSecurityInfo)

    Sets security info for an object by name&nbsp;

    [GetNamedSecurityInfo](#win32security.md#win32securityGetNamedSecurityInfo)

    Retrieve security info for an object by name&nbsp;

    [OpenProcessToken](#win32security.md#win32securityOpenProcessToken)

    Opens the access token associated with a process.&nbsp;

    [LookupPrivilegeValue](#win32security.md#win32securityLookupPrivilegeValue)

    Retrieves the locally unique id for a privilege name&nbsp;

    [LookupPrivilegeName](#win32security.md#win32securityLookupPrivilegeName)

    return the text name for a privilege LUID&nbsp;

    [LookupPrivilegeDisplayName](#win32security.md#win32securityLookupPrivilegeDisplayName)

    Returns long description for a privilege name&nbsp;

    [AdjustTokenPrivileges](#win32security.md#win32securityAdjustTokenPrivileges)

    Enables or disables privileges for an access token.&nbsp;

    [AdjustTokenGroups](#win32security.md#win32securityAdjustTokenGroups)

    Sets the groups associated to an access token.&nbsp;

    [GetTokenInformation](#win32security.md#win32securityGetTokenInformation)

    Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.&nbsp;

    [OpenThreadToken](#win32security.md#win32securityOpenThreadToken)

    Opens the access token associated with a thread.&nbsp;

    [SetThreadToken](#win32security.md#win32securitySetThreadToken)

    Assigns an impersonation token to a thread. The function 

can also cause a thread to stop using an impersonation token.&nbsp;

    [GetFileSecurity](#win32security.md#win32securityGetFileSecurity)

    Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

    [SetFileSecurity](#win32security.md#win32securitySetFileSecurity)

    Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

    [GetUserObjectSecurity](#win32security.md#win32securityGetUserObjectSecurity)

    Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

    [SetUserObjectSecurity](#win32security.md#win32securitySetUserObjectSecurity)

    Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

    [GetKernelObjectSecurity](#win32security.md#win32securityGetKernelObjectSecurity)

    Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

    [SetKernelObjectSecurity](#win32security.md#win32securitySetKernelObjectSecurity)

    Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.&nbsp;

    [SetTokenInformation](#win32security.md#win32securitySetTokenInformation)

    Set a specified type of information in an access token&nbsp;

    [LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)

    Opens a policy handle for the specified system&nbsp;

    [LsaClose](#win32security.md#win32securityLsaClose)

    Closes a policy handle created by[win32security::LsaOpenPolicy](#win32security.md#win32securityLsaOpenPolicy)&nbsp;

    [LsaQueryInformationPolicy](#win32security.md#win32securityLsaQueryInformationPolicy)

    Retrieves information from the policy handle&nbsp;

    [LsaSetInformationPolicy](#win32security.md#win32securityLsaSetInformationPolicy)

    Sets policy options&nbsp;

    [LsaAddAccountRights](#win32security.md#win32securityLsaAddAccountRights)

    Adds a list of privileges to an account&nbsp;

    [LsaRemoveAccountRights](#win32security.md#win32securityLsaRemoveAccountRights)

    Removes privs from an account&nbsp;

    [LsaEnumerateAccountRights](#win32security.md#win32securityLsaEnumerateAccountRights)

    Lists privileges held by SID&nbsp;

    [LsaEnumerateAccountsWithUserRight](#win32security.md#win32securityLsaEnumerateAccountsWithUserRight)

    Return SIDs that hold specified priv&nbsp;

    [ConvertSidToStringSid](#win32security.md#win32securityConvertSidToStringSid)

    Return string representation of a SID&nbsp;

    [ConvertStringSidToSid](#win32security.md#win32securityConvertStringSidToSid)

    Creates a SID from a string representation&nbsp;

    [ConvertSecurityDescriptorToStringSecurityDescriptor](#win32security.md#win32securityConvertSecurityDescriptorToStringSecurityDescriptor)

    Return string representation of a SECURITY_DESCRIPTOR&nbsp;

    [ConvertStringSecurityDescriptorToSecurityDescriptor](#win32security.md#win32securityConvertStringSecurityDescriptorToSecurityDescriptor)

    Turns string representation of a SECURITY_DESCRIPTOR into the real thing&nbsp;

    [LsaStorePrivateData](#win32security.md#win32securityLsaStorePrivateData)

    Stores encrypted unicode data under specified Lsa registry key. Returns None on success&nbsp;

    [LsaRetrievePrivateData](#win32security.md#win32securityLsaRetrievePrivateData)

    Retreives encrypted unicode data from Lsa registry key.&nbsp;

    [LsaRegisterPolicyChangeNotification](#win32security.md#win32securityLsaRegisterPolicyChangeNotification)

    Register an event handle to receive policy change events&nbsp;

    [LsaUnregisterPolicyChangeNotification](#win32security.md#win32securityLsaUnregisterPolicyChangeNotification)

    Stop receiving policy change notification&nbsp;

    [CryptEnumProviders](#win32security.md#win32securityCryptEnumProviders)

    List cryptography providers&nbsp;

    [EnumerateSecurityPackages](#win32security.md#win32securityEnumerateSecurityPackages)

    List available security packages as a sequence of dictionaries representing SecPkgInfo structures&nbsp;

    [AllocateLocallyUniqueId](#win32security.md#win32securityAllocateLocallyUniqueId)

    Creates a new LUID&nbsp;

    [ImpersonateSelf](#win32security.md#win32securityImpersonateSelf)

    Assigns an impersonation token for current security context to current process&nbsp;

    [DuplicateToken](#win32security.md#win32securityDuplicateToken)

    Creates a copy of an access token with specified impersonation level&nbsp;

    [DuplicateTokenEx](#win32security.md#win32securityDuplicateTokenEx)

    Extended version of DuplicateToken.&nbsp;

    [CheckTokenMembership](#win32security.md#win32securityCheckTokenMembership)

    Checks if a SID is enabled in a token&nbsp;

    [CreateRestrictedToken](#win32security.md#win32securityCreateRestrictedToken)

    Creates a restricted copy of an access token with reduced privs - requires win2K or higher&nbsp;

    [LsaRegisterLogonProcess](#win32security.md#win32securityLsaRegisterLogonProcess)

    Creates a trusted connection to LSA&nbsp;

    [LsaConnectUntrusted](#win32security.md#win32securityLsaConnectUntrusted)

    Creates untrusted connection to LSA&nbsp;

    [LsaDeregisterLogonProcess](#win32security.md#win32securityLsaDeregisterLogonProcess)

    Closes connection to LSA server&nbsp;

    [LsaLookupAuthenticationPackage](#win32security.md#win32securityLsaLookupAuthenticationPackage)

    Retrieves the unique id for an authentication package&nbsp;

    [LsaEnumerateLogonSessions](#win32security.md#win32securityLsaEnumerateLogonSessions)

    Lists all current logon ids&nbsp;

    [LsaGetLogonSessionData](#win32security.md#win32securityLsaGetLogonSessionData)

    Returns information about a logon session&nbsp;

    [AcquireCredentialsHandle](#win32security.md#win32securityAcquireCredentialsHandle)

    Creates a handle to credentials for use with SSPI&nbsp;

    [InitializeSecurityContext](#win32security.md#win32securityInitializeSecurityContext)

    Creates a security context based on credentials created by AcquireCredentialsHandle&nbsp;

    [AcceptSecurityContext](#win32security.md#win32securityAcceptSecurityContext)

    Builds security context between server and client&nbsp;

    [QuerySecurityPackageInfo](#win32security.md#win32securityQuerySecurityPackageInfo)

    Retrieves parameters for a security package&nbsp;

    [LsaCallAuthenticationPackage](#win32security.md#win32securityLsaCallAuthenticationPackage)

    Requests the services of an authentication package&nbsp;

    [TranslateName](#win32security.md#win32securityTranslateName)

    Converts a directory service object name from one format to another.&nbsp;

    [CreateWellKnownSid](#win32security.md#win32securityCreateWellKnownSid)

    Returns one of the predefined well known sids&nbsp;

    [MapGenericMask](#win32security.md#win32securityMapGenericMask)

    Translates generic access rights into specific rights&nbsp;
------

##[win32file](md/win32file.md)

## Module win32file

An interface to the win32 File API's
This module includes the tranactional NTFS operations introduced with 

Vista.  The transacted functions are not wrapped separately, but are invoked by 

passing a transaction handle to the corresponding Unicode API function. 

This makes it simple to convert a set of file operations into a transaction by 

simply adding Transaction=[PyHANDLE](#README.md#PyHANDLE)to the passed arguments. 

If Transaction is None, 0, or not specified, the non-transacted API function will 

be called.
Functions combined in this manner:
CreateFile / CreateFileTransacted
DeleteFile / DeleteFileTransacted
CreateDirectoryEx / CreateDirectoryTransacted
MoveFileWithProgress / MoveFileTransacted
CopyFileEx / CopyFileTransacted
GetFileAttributes / GetFileAttributesTransacted
SetFileAttributes / SetFileAttributesTransacted
CreateHardLink / CreateHardLinkTransacted
CreateSymbolicLink / CreateSymbolicLinkTransacted
RemoveDirectory / RemoveDirectoryTransacted

#### Methods


    [AreFileApisANSI](#win32file.md#win32fileAreFileApisANSI)

    Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

    [CancelIo](#win32file.md#win32fileCancelIo)

    Cancels pending IO requests for the object.&nbsp;

    [CopyFile](#win32file.md#win32fileCopyFile)

    Copies a file&nbsp;

    [CopyFileW](#win32file.md#win32fileCopyFileW)

    Copies a file (NT/2000 Unicode specific version)&nbsp;

    [CreateDirectory](#win32file.md#win32fileCreateDirectory)

    Creates a directory&nbsp;

    [CreateDirectoryW](#win32file.md#win32fileCreateDirectoryW)

    Creates a directory (NT/2000 Unicode specific version)&nbsp;

    [CreateDirectoryEx](#win32file.md#win32fileCreateDirectoryEx)

    Creates a directory&nbsp;

    [CreateFile](#win32file.md#win32fileCreateFile)

    Creates or opens the a file or other object and returns a handle that can be used to access the object.&nbsp;

    [CreateIoCompletionPort](#win32file.md#win32fileCreateIoCompletionPort)

    Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.&nbsp;

    [CreateMailslot](#win32file.md#win32fileCreateMailslot)

    Creates a mailslot on the local machine&nbsp;

    [GetMailslotInfo](#win32file.md#win32fileGetMailslotInfo)

    Retrieves information about a mailslot&nbsp;

    [SetMailslotInfo](#win32file.md#win32fileSetMailslotInfo)

    Sets a mailslot's timeout&nbsp;

    [DefineDosDevice](#win32file.md#win32fileDefineDosDevice)

    Lets an application define, redefine, or delete MS-DOS device names.&nbsp;

    [DefineDosDeviceW](#win32file.md#win32fileDefineDosDeviceW)

    Lets an application define, redefine, or delete MS-DOS device names. (NT/2000 Unicode specific version)&nbsp;

    [DeleteFile](#win32file.md#win32fileDeleteFile)

    Deletes a file.&nbsp;

    [DeviceIoControl](#win32file.md#win32fileDeviceIoControl)

    Sends a control code to a device or file system driver&nbsp;

    [FindClose](#win32file.md#win32fileFindClose)

    Closes a find handle.&nbsp;

    [FindCloseChangeNotification](#win32file.md#win32fileFindCloseChangeNotification)

    Closes a handle.&nbsp;

    [FindFirstChangeNotification](#win32file.md#win32fileFindFirstChangeNotification)

    Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.&nbsp;

    [FindNextChangeNotification](#win32file.md#win32fileFindNextChangeNotification)

    Requests that the operating system signal a change notification handle the next time it detects an appropriate change,&nbsp;

    [FlushFileBuffers](#win32file.md#win32fileFlushFileBuffers)

    Clears the buffers for the specified file and causes all buffered data to be written to the file.&nbsp;

    [GetBinaryType](#win32file.md#win32fileGetBinaryType)

    Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.&nbsp;

    [GetDiskFreeSpace](#win32file.md#win32fileGetDiskFreeSpace)

    Determines the free space on a device.&nbsp;

    [GetDiskFreeSpaceEx](#win32file.md#win32fileGetDiskFreeSpaceEx)

    Determines the free space on a device.&nbsp;

    [GetDriveType](#win32file.md#win32fileGetDriveType)

    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.&nbsp;

    [GetDriveTypeW](#win32file.md#win32fileGetDriveTypeW)

    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive. (NT/2000 Unicode specific version).&nbsp;

    [GetFileAttributes](#win32file.md#win32fileGetFileAttributes)

    Determines a files attributes.&nbsp;

    [GetFileAttributesW](#win32file.md#win32fileGetFileAttributesW)

    Determines a files attributes (NT/2000 Unicode specific version).&nbsp;

    [GetFileTime](#win32file.md#win32fileGetFileTime)

    Returns a file's creation, last access, and modification times.&nbsp;

    [SetFileTime](#win32file.md#win32fileSetFileTime)

    Sets the date and time that a file was created, last accessed, or last modified.&nbsp;

    [GetFileInformationByHandle](#win32file.md#win32fileGetFileInformationByHandle)

    Retrieves file information for a specified file.&nbsp;

    [GetCompressedFileSize](#win32file.md#win32fileGetCompressedFileSize)

    Determines the compressed size of a file.&nbsp;

    [GetFileSize](#win32file.md#win32fileGetFileSize)

    Determines the size of a file.&nbsp;

    [AllocateReadBuffer](#win32file.md#win32fileAllocateReadBuffer)

    Allocates a buffer which can be used with an overlapped Read operation using[win32file::ReadFile](#win32file.md#win32fileReadFile)&nbsp;

    [ReadFile](#win32file.md#win32fileReadFile)

    Reads a string from a file&nbsp;

    [WriteFile](#win32file.md#win32fileWriteFile)

    Writes a string to a file&nbsp;

    [CloseHandle](#win32file.md#win32fileCloseHandle)

    Closes an open handle.&nbsp;

    [LockFileEx](#win32file.md#win32fileLockFileEx)

    Locks a file. Wrapper for LockFileEx win32 API.&nbsp;

    [UnlockFileEx](#win32file.md#win32fileUnlockFileEx)

    Unlocks a file. Wrapper for UnlockFileEx win32 API.&nbsp;

    [GetQueuedCompletionStatus](#win32file.md#win32fileGetQueuedCompletionStatus)

    Attempts to dequeue an I/O completion packet from a specified input/output completion port.&nbsp;

    [PostQueuedCompletionStatus](#win32file.md#win32filePostQueuedCompletionStatus)

    lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.&nbsp;

    [GetFileType](#win32file.md#win32fileGetFileType)

    Determines the type of a file.&nbsp;

    [GetLogicalDrives](#win32file.md#win32fileGetLogicalDrives)

    Returns a bitmaks of the logical drives installed.&nbsp;

    [GetOverlappedResult](#win32file.md#win32fileGetOverlappedResult)

    Determines the result of the most recent call with an OVERLAPPED object.&nbsp;

    [LockFile](#win32file.md#win32fileLockFile)

    Locks a specified file for exclusive access by the calling process.&nbsp;

    [MoveFile](#win32file.md#win32fileMoveFile)

    Renames an existing file or a directory (including all its children).&nbsp;

    [MoveFileW](#win32file.md#win32fileMoveFileW)

    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).&nbsp;

    [MoveFileEx](#win32file.md#win32fileMoveFileEx)

    Renames an existing file or a directory (including all its children).&nbsp;

    [MoveFileExW](#win32file.md#win32fileMoveFileExW)

    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).&nbsp;

    [QueryDosDevice](#win32file.md#win32fileQueryDosDevice)

    Returns the mapping for a device name, or all device names&nbsp;

    [ReadDirectoryChangesW](#win32file.md#win32fileReadDirectoryChangesW)

    retrieves information describing the changes occurring within a directory.&nbsp;

    [FILE_NOTIFY_INFORMATION](#win32file.md#win32fileFILE_NOTIFY_INFORMATION)

    Decodes a PyFILE_NOTIFY_INFORMATION buffer.&nbsp;

    [SetCurrentDirectory](#win32file.md#win32fileSetCurrentDirectory)

    Sets the current directory.&nbsp;

    [SetEndOfFile](#win32file.md#win32fileSetEndOfFile)

    Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.&nbsp;

    [SetFileApisToANSI](#win32file.md#win32fileSetFileApisToANSI)

    Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

    [SetFileApisToOEM](#win32file.md#win32fileSetFileApisToOEM)

    Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.&nbsp;

    [SetFileAttributes](#win32file.md#win32fileSetFileAttributes)

    Changes a file's attributes.&nbsp;

    [SetFilePointer](#win32file.md#win32fileSetFilePointer)

    Moves the file pointer of an open file.&nbsp;

    [SetVolumeLabel](#win32file.md#win32fileSetVolumeLabel)

    Sets a volume label for a disk drive.&nbsp;

    [UnlockFile](#win32file.md#win32fileUnlockFile)

    Unlocks a region of a file locked by[win32file::LockFile](#win32file.md#win32fileLockFile)or[win32file::LockFileEx](#win32file.md#win32fileLockFileEx)&nbsp;

    [_get_osfhandle](#win32file.md#win32file_get_osfhandle)

    Gets operating-system file handle associated with existing stream&nbsp;

    [_open_osfhandle](#win32file.md#win32file_open_osfhandle)

    Associates a C run-time file handle with a existing operating-system file handle.&nbsp;

    [_setmaxstdio](#win32file.md#win32file_setmaxstdio)

    Set the maximum allowed number of open stdio handles&nbsp;

    [_getmaxstdio](#win32file.md#win32file_getmaxstdio)

    Returns the maximum number of CRT io streams.&nbsp;

    [TransmitFile](#win32file.md#win32fileTransmitFile)

    Transmits a file over a socket 

TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])&nbsp;

    [ConnectEx](#win32file.md#win32fileConnectEx)

    Version of connect that uses Overlapped I/O 

ConnectEx(sock, (addr, port), buf, overlap)&nbsp;

    [AcceptEx](#win32file.md#win32fileAcceptEx)

    Version of accept that uses Overlapped I/O&nbsp;

    [CalculateSocketEndPointSize](#win32file.md#win32fileCalculateSocketEndPointSize)

    Calculate how many bytes are needed for the connection endpoints data for a socket.&nbsp;

    [GetAcceptExSockaddrs](#win32file.md#win32fileGetAcceptExSockaddrs)

    Parses the connection endpoints from the buffer passed into AcceptEx&nbsp;

    [WSAEventSelect](#win32file.md#win32fileWSAEventSelect)

    Specifies an event object to be associated with the supplied set of FD_XXXX network events.&nbsp;

    [WSAEnumNetworkEvents](#win32file.md#win32fileWSAEnumNetworkEvents)

    Return network events that caused the event associated with the socket to be signaled.&nbsp;

    [WSAAsyncSelect](#win32file.md#win32fileWSAAsyncSelect)

    Request windows message notification for the supplied set of FD_XXXX network events.&nbsp;

    [WSASend](#win32file.md#win32fileWSASend)

    Winsock send() equivalent function for Overlapped I/O.&nbsp;

    [WSARecv](#win32file.md#win32fileWSARecv)

    Winsock recv() equivalent function for Overlapped I/O.&nbsp;

    [BuildCommDCB](#win32file.md#win32fileBuildCommDCB)

    Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command&nbsp;

    [ClearCommError](#win32file.md#win32fileClearCommError)

    retrieves information about a communications error and reports the current status of a communications device.&nbsp;

    [EscapeCommFunction](#win32file.md#win32fileEscapeCommFunction)

    directs a specified communications device to perform an extended function.&nbsp;

    [GetCommState](#win32file.md#win32fileGetCommState)

    Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.&nbsp;

    [SetCommState](#win32file.md#win32fileSetCommState)

    Configures a communications device according to the specifications in a device-control block. 

The function reinitializes all hardware and control settings, but it does not empty output or input queues.&nbsp;

    [ClearCommBreak](#win32file.md#win32fileClearCommBreak)

    Restores character transmission for a specified communications device and places the transmission line in a nonbreak state&nbsp;

    [GetCommMask](#win32file.md#win32fileGetCommMask)

    Retrieves the value of the event mask for a specified communications device.&nbsp;

    [SetCommMask](#win32file.md#win32fileSetCommMask)

    Sets the value of the event mask for a specified communications device.&nbsp;

    [GetCommModemStatus](#win32file.md#win32fileGetCommModemStatus)

    Retrieves modem control-register values.&nbsp;

    [GetCommTimeouts](#win32file.md#win32fileGetCommTimeouts)

    Retrieves the time-out parameters for all read and write operations on a specified communications device.&nbsp;

    [SetCommTimeouts](#win32file.md#win32fileSetCommTimeouts)

    Sets the time-out parameters for all read and write operations on a specified communications device.&nbsp;

    [PurgeComm](#win32file.md#win32filePurgeComm)

    Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.&nbsp;

    [SetCommBreak](#win32file.md#win32fileSetCommBreak)

    Suspends character transmission for a specified communications device and places the transmission line in a break state until the[win32file::ClearCommBreak](#win32file.md#win32fileClearCommBreak)function is called.&nbsp;

    [SetupComm](#win32file.md#win32fileSetupComm)

    Initializes the communications parameters for a specified communications device.&nbsp;

    [TransmitCommChar](#win32file.md#win32fileTransmitCommChar)

    Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.&nbsp;

    [WaitCommEvent](#win32file.md#win32fileWaitCommEvent)

    Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.&nbsp;

    [SetVolumeMountPoint](#win32file.md#win32fileSetVolumeMountPoint)

    Mounts the specified volume at the specified volume mount point.&nbsp;

    [DeleteVolumeMountPoint](#win32file.md#win32fileDeleteVolumeMountPoint)

    Unmounts the volume from the specified volume mount point.&nbsp;

    [GetVolumeNameForVolumeMountPoint](#win32file.md#win32fileGetVolumeNameForVolumeMountPoint)

    Returns unique volume name.&nbsp;

    [GetVolumePathName](#win32file.md#win32fileGetVolumePathName)

    Returns volume mount point for a path&nbsp;

    [GetVolumePathNamesForVolumeName](#win32file.md#win32fileGetVolumePathNamesForVolumeName)

    Returns mounted paths for a volume&nbsp;

    [CreateHardLink](#win32file.md#win32fileCreateHardLink)

    Establishes an NTFS hard link between an existing file and a new file.&nbsp;

    [CreateSymbolicLink](#win32file.md#win32fileCreateSymbolicLink)

    Creates a symbolic link (reparse point)&nbsp;

    [EncryptFile](#win32file.md#win32fileEncryptFile)

    Encrypts specified file (requires Win2k or higher and NTFS)&nbsp;

    [DecryptFile](#win32file.md#win32fileDecryptFile)

    Decrypts specified file (requires Win2k or higher and NTFS)&nbsp;

    [EncryptionDisable](#win32file.md#win32fileEncryptionDisable)

    Enables/disables encryption for a directory (requires Win2k or higher and NTFS)&nbsp;

    [FileEncryptionStatus](#win32file.md#win32fileFileEncryptionStatus)

    retrieves the encryption status of the specified file.&nbsp;

    [QueryUsersOnEncryptedFile](#win32file.md#win32fileQueryUsersOnEncryptedFile)

    Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)&nbsp;

    [QueryRecoveryAgentsOnEncryptedFile](#win32file.md#win32fileQueryRecoveryAgentsOnEncryptedFile)

    Lists recovery agents for file as a tuple of tuples.&nbsp;

    [RemoveUsersFromEncryptedFile](#win32file.md#win32fileRemoveUsersFromEncryptedFile)

    Removes specified certificates from file - if certificate is not found, it is ignored&nbsp;

    [AddUsersToEncryptedFile](#win32file.md#win32fileAddUsersToEncryptedFile)

    Allows user identified by SID and EFS certificate access to decrypt specified file&nbsp;

    [DuplicateEncryptionInfoFile](#win32file.md#win32fileDuplicateEncryptionInfoFile)

    Duplicates EFS encryption from one file to another&nbsp;

    [BackupRead](#win32file.md#win32fileBackupRead)

    Reads streams of data from a file&nbsp;

    [BackupSeek](#win32file.md#win32fileBackupSeek)

    Seeks forward in a file stream&nbsp;

    [BackupWrite](#win32file.md#win32fileBackupWrite)

    Restores file data&nbsp;

    [SetFileShortName](#win32file.md#win32fileSetFileShortName)

    Set the 8.3 name of a file&nbsp;

    [CopyFileEx](#win32file.md#win32fileCopyFileEx)

    Restartable file copy with optional progress routine&nbsp;

    [MoveFileWithProgress](#win32file.md#win32fileMoveFileWithProgress)

    Moves a file, and reports progress to a callback function&nbsp;

    [ReplaceFile](#win32file.md#win32fileReplaceFile)

    Replaces one file with another&nbsp;

    [OpenEncryptedFileRaw](#win32file.md#win32fileOpenEncryptedFileRaw)

    Initiates a backup or restore operation on an encrypted file&nbsp;

    [ReadEncryptedFileRaw](#win32file.md#win32fileReadEncryptedFileRaw)

    Reads the encrypted bytes of a file for backup and restore purposes&nbsp;

    [WriteEncryptedFileRaw](#win32file.md#win32fileWriteEncryptedFileRaw)

    Writes raw bytes to an encrypted file&nbsp;

    [CloseEncryptedFileRaw](#win32file.md#win32fileCloseEncryptedFileRaw)

    Frees a context created by[win32file::OpenEncryptedFileRaw](#win32file.md#win32fileOpenEncryptedFileRaw)&nbsp;

    [CreateFileW](#win32file.md#win32fileCreateFileW)

    Unicode version of CreateFile - see[win32file::CreateFile](#win32file.md#win32fileCreateFile)for more information.&nbsp;

    [DeleteFileW](#win32file.md#win32fileDeleteFileW)

    Deletes a file (Unicode version)&nbsp;

    [GetFileAttributesEx](#win32file.md#win32fileGetFileAttributesEx)

    Retrieves attributes for a specified file or directory.&nbsp;

    [SetFileAttributesW](#win32file.md#win32fileSetFileAttributesW)

    Sets a file's attributes&nbsp;

    [CreateDirectoryExW](#win32file.md#win32fileCreateDirectoryExW)

    Creates a directory (Unicode version)&nbsp;

    [RemoveDirectory](#win32file.md#win32fileRemoveDirectory)

    Removes an existing directory&nbsp;

    [FindFilesW](#win32file.md#win32fileFindFilesW)

    Retrieves a list of matching filenames, using the Windows Unicode API.  An interface to the API FindFirstFileW/FindNextFileW/Find close functions.&nbsp;

    [FindFilesIterator](#win32file.md#win32fileFindFilesIterator)

    Returns an interator based on 

FindFirstFile/FindNextFile. Similar to **win32file::FindFiles** , but 

avoids the creation of the list for huge directories.&nbsp;

    [FindStreams](#win32file.md#win32fileFindStreams)

    List the data streams for a file&nbsp;

    [FindFileNames](#win32file.md#win32fileFindFileNames)

    Enumerates hard links that point to specified file&nbsp;

    [GetFinalPathNameByHandle](#win32file.md#win32fileGetFinalPathNameByHandle)

    Returns the file name for an open file handle&nbsp;

    [SfcGetNextProtectedFile](#win32file.md#win32fileSfcGetNextProtectedFile)

    Returns list of protected operating system files&nbsp;

    [SfcIsFileProtected](#win32file.md#win32fileSfcIsFileProtected)

    Checks if a file is protected&nbsp;

    [GetLongPathName](#win32file.md#win32fileGetLongPathName)

    Retrieves the long path for a short path (8.3 filename)&nbsp;

    [GetFullPathName](#win32file.md#win32fileGetFullPathName)

    Returns full path for path passed in&nbsp;

    [Wow64DisableWow64FsRedirection](#win32file.md#win32fileWow64DisableWow64FsRedirection)

    Disables file system redirection for 32-bit processes running on a 64-bit system&nbsp;

    [Wow64RevertWow64FsRedirection](#win32file.md#win32fileWow64RevertWow64FsRedirection)

    Reenables file system redirection for 32-bit processes running on a 64-bit system&nbsp;

    [GetFileInformationByHandleEx](#win32file.md#win32fileGetFileInformationByHandleEx)

    Retrieves extended file information for an open file handle.&nbsp;

    [SetFileInformationByHandle](#win32file.md#win32fileSetFileInformationByHandle)

    Changes file characteristics by file handle&nbsp;

    [ReOpenFile](#win32file.md#win32fileReOpenFile)

    Creates a new handle to an open file&nbsp;

    [OpenFileById](#win32file.md#win32fileOpenFileById)

    Opens a file by File Id or Object Id&nbsp;
------

##[win32com.authorization.authorization](md/win32com.authorization.authorization.md)

## Module win32com.authorization.authorization

Module containing support for authorization COM interfaces

#### Methods


    [EditSecurity](#win32com.authorization.authorization.md#win32com.authorization.authorizationEditSecurity)

    Creates a security descriptor editor dialog&nbsp;
------

##[win32evtlog](md/win32evtlog.md)

## Module win32evtlog

A module, encapsulating the Windows Win32 event log API.
The Evt* functions are only available on Vista and later.  Attempting to call 

them on XP will result in the process exiting, rather than a python exception.

#### Methods


    [ReadEventLog](#win32evtlog.md#win32evtlogReadEventLog)

    Reads some event log records.&nbsp;

    [ClearEventLog](#win32evtlog.md#win32evtlogClearEventLog)

    Clears the event log&nbsp;

    [BackupEventLog](#win32evtlog.md#win32evtlogBackupEventLog)

    Backs up the event log&nbsp;

    [CloseEventLog](#win32evtlog.md#win32evtlogCloseEventLog)

    Closes the eventlog&nbsp;

    [DeregisterEventSource](#win32evtlog.md#win32evtlogDeregisterEventSource)

    Deregisters an Event Source&nbsp;

    [NotifyChangeEventLog](#win32evtlog.md#win32evtlogNotifyChangeEventLog)

    Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.&nbsp;

    [GetNumberOfEventLogRecords](#win32evtlog.md#win32evtlogGetNumberOfEventLogRecords)

    Returns the number of event log records.&nbsp;

    [GetOldestEventLogRecord](#win32evtlog.md#win32evtlogGetOldestEventLogRecord)

    Returns the number of event log records.&nbsp;

    [OpenEventLog](#win32evtlog.md#win32evtlogOpenEventLog)

    Opens an event log.&nbsp;

    [RegisterEventSource](#win32evtlog.md#win32evtlogRegisterEventSource)

    Registers an Event Source&nbsp;

    [OpenBackupEventLog](#win32evtlog.md#win32evtlogOpenBackupEventLog)

    Opens a previously saved event log.&nbsp;

    [ReportEvent](#win32evtlog.md#win32evtlogReportEvent)

    Reports an event&nbsp;

    [EvtOpenChannelEnum](#win32evtlog.md#win32evtlogEvtOpenChannelEnum)

    Begins an enumeration of event channels&nbsp;

    [EvtNextChannelPath](#win32evtlog.md#win32evtlogEvtNextChannelPath)

    Retrieves a channel path from an enumeration&nbsp;

    [EvtOpenLog](#win32evtlog.md#win32evtlogEvtOpenLog)

    Opens an event log or exported log archive&nbsp;

    [EvtClearLog](#win32evtlog.md#win32evtlogEvtClearLog)

    Clears an event log and optionally exports events to an archive&nbsp;

    [EvtExportLog](#win32evtlog.md#win32evtlogEvtExportLog)

    Exports events from a channel or log file&nbsp;

    [EvtArchiveExportedLog](#win32evtlog.md#win32evtlogEvtArchiveExportedLog)

    Localizes an exported event log file&nbsp;

    [EvtGetExtendedStatus](#win32evtlog.md#win32evtlogEvtGetExtendedStatus)

    Returns additional error info from last Evt* call&nbsp;

    [EvtQuery](#win32evtlog.md#win32evtlogEvtQuery)

    Opens a query over a log channel or exported log file&nbsp;

    [EvtNext](#win32evtlog.md#win32evtlogEvtNext)

    Returns events from a query&nbsp;

    [EvtSeek](#win32evtlog.md#win32evtlogEvtSeek)

    Changes the current position in a result set&nbsp;

    [EvtRender](#win32evtlog.md#win32evtlogEvtRender)

    Formats an event into XML text&nbsp;

    [EvtSubscribe](#win32evtlog.md#win32evtlogEvtSubscribe)

    Requests notification for events&nbsp;

    [EvtCreateBookmark](#win32evtlog.md#win32evtlogEvtCreateBookmark)

    Creates a bookmark&nbsp;

    [EvtUpdateBookmark](#win32evtlog.md#win32evtlogEvtUpdateBookmark)

    Repositions a bookmark to an event&nbsp;

    [EvtGetChannelConfigProperty](#win32evtlog.md#win32evtlogEvtGetChannelConfigProperty)

    Retreives channel configuration information&nbsp;

    [EvtOpenChannelConfig](#win32evtlog.md#win32evtlogEvtOpenChannelConfig)

    Opens channel configuration&nbsp;

    [EvtOpenSession](#win32evtlog.md#win32evtlogEvtOpenSession)

    Creates a session used to access the Event Log on another machine&nbsp;

    [EvtOpenPublisherEnum](#win32evtlog.md#win32evtlogEvtOpenPublisherEnum)

    Begins an enumeration of event publishers&nbsp;

    [EvtNextPublisherId](#win32evtlog.md#win32evtlogEvtNextPublisherId)

    Returns the next publisher from an enumeration&nbsp;

    [EvtOpenPublisherMetadata](#win32evtlog.md#win32evtlogEvtOpenPublisherMetadata)

    Opens a publisher to retrieve properties using[win32evtlog::EvtGetPublisherMetadataProperty](#win32evtlog.md#win32evtlogEvtGetPublisherMetadataProperty)&nbsp;

    [EvtGetPublisherMetadataProperty](#win32evtlog.md#win32evtlogEvtGetPublisherMetadataProperty)

    Retrieves a property from an event publisher&nbsp;

    [EvtOpenEventMetadataEnum](#win32evtlog.md#win32evtlogEvtOpenEventMetadataEnum)

    Enumerates the events that a publisher provides&nbsp;

    [EvtNextEventMetadata](#win32evtlog.md#win32evtlogEvtNextEventMetadata)

    Retrieves the next item from an event metadata enumeration&nbsp;

    [EvtGetEventMetadataProperty](#win32evtlog.md#win32evtlogEvtGetEventMetadataProperty)

    Retrieves a property from an event publisher&nbsp;

    [EvtGetLogInfo](#win32evtlog.md#win32evtlogEvtGetLogInfo)

    Retrieves log file or channel information&nbsp;

    [EvtGetEventInfo](#win32evtlog.md#win32evtlogEvtGetEventInfo)

    Retrieves information about the source of an event&nbsp;

    [EvtGetObjectArraySize](#win32evtlog.md#win32evtlogEvtGetObjectArraySize)

    Returns the size of an array of event objects&nbsp;

    [EvtGetObjectArrayProperty](#win32evtlog.md#win32evtlogEvtGetObjectArrayProperty)

    Retrieves an item from an object array&nbsp;
------

##[win32pdh](md/win32pdh.md)

## Module win32pdh

A module, encapsulating the Windows Performance Data Helpers API

#### Methods


    [AddCounter](#win32pdh.md#win32pdhAddCounter)

    Adds a new counter&nbsp;

    [AddEnglishCounter](#win32pdh.md#win32pdhAddEnglishCounter)

    Adds a counter to a query by its English name&nbsp;

    [RemoveCounter](#win32pdh.md#win32pdhRemoveCounter)

    Removes an open counter.&nbsp;

    [EnumObjectItems](#win32pdh.md#win32pdhEnumObjectItems)

    Enumerates an object's items&nbsp;

    [EnumObjects](#win32pdh.md#win32pdhEnumObjects)

    Enumerates objects&nbsp;

    [OpenQuery](#win32pdh.md#win32pdhOpenQuery)

    Opens a new query&nbsp;

    [CloseQuery](#win32pdh.md#win32pdhCloseQuery)

    Closes an open query.&nbsp;

    [MakeCounterPath](#win32pdh.md#win32pdhMakeCounterPath)

    Makes a fully resolved counter path&nbsp;

    [GetCounterInfo](#win32pdh.md#win32pdhGetCounterInfo)

    Retrieves information about a counter, such as data size, counter type, path, and user-supplied data values.&nbsp;

    [GetFormattedCounterValue](#win32pdh.md#win32pdhGetFormattedCounterValue)

    Retrieves a formatted counter value&nbsp;

    [CollectQueryData](#win32pdh.md#win32pdhCollectQueryData)

    Collects the current raw data value for all counters in the specified query and updates the status code of each counter.&nbsp;

    [ValidatePath](#win32pdh.md#win32pdhValidatePath)

    Validates that the specified counter is present on the machine specified in the counter path.&nbsp;

    [ExpandCounterPath](#win32pdh.md#win32pdhExpandCounterPath)

    Examines the specified machine (or local machine if none is specified) for counters and instances of counters that match the wild card strings in the counter path.&nbsp;

    [ParseCounterPath](#win32pdh.md#win32pdhParseCounterPath)

    Parses the elements of the counter path.&nbsp;

    [ParseInstanceName](#win32pdh.md#win32pdhParseInstanceName)

    Parses the elements of the instance name&nbsp;

    [SetCounterScaleFactor](#win32pdh.md#win32pdhSetCounterScaleFactor)

    Sets the scale factor that is applied to the calculated value of the specified counter when you request the formatted counter value.&nbsp;

    [BrowseCounters](#win32pdh.md#win32pdhBrowseCounters)

    Displays the counter browsing dialog box so that the user can select the counters to be returned to the caller.&nbsp;

    [ConnectMachine](#win32pdh.md#win32pdhConnectMachine)

    connects to the specified machine, and creates and initializes a machine entry in the PDH DLL.&nbsp;

    [LookupPerfIndexByName](#win32pdh.md#win32pdhLookupPerfIndexByName)

    Returns the counter index corresponding to the specified counter name.&nbsp;

    [LookupPerfNameByIndex](#win32pdh.md#win32pdhLookupPerfNameByIndex)

    Returns the performance object name corresponding to the specified index.&nbsp;
------

##[win32net](md/win32net.md)

## Module win32net

A module encapsulating the Windows Network API.

#### Methods


    [NetGetJoinInformation](#win32net.md#win32netNetGetJoinInformation)

    Retrieves join status information for the specified computer.&nbsp;

    [NetGroupGetInfo](#win32net.md#win32netNetGroupGetInfo)

    Retrieves information about a particular group on a server.&nbsp;

    [NetGroupGetUsers](#win32net.md#win32netNetGroupGetUsers)

    Enumerates the users in a group.&nbsp;

    [NetGroupSetUsers](#win32net.md#win32netNetGroupSetUsers)

    Sets the users in a group on server.&nbsp;

    [NetGroupSetInfo](#win32net.md#win32netNetGroupSetInfo)

    Sets information about a particular group account on a server.&nbsp;

    [NetGroupAdd](#win32net.md#win32netNetGroupAdd)

    Creates a new group.&nbsp;

    [NetGroupAddUser](#win32net.md#win32netNetGroupAddUser)

    Adds a user to a group&nbsp;

    [NetGroupDel](#win32net.md#win32netNetGroupDel)

    Deletes a group.&nbsp;

    [NetGroupDelUser](#win32net.md#win32netNetGroupDelUser)

    Deletes a user from the group&nbsp;

    [NetGroupEnum](#win32net.md#win32netNetGroupEnum)

    Enumerates the groups.&nbsp;

    [NetGroupAdd](#win32net.md#win32netNetGroupAdd)

    Creates a new group.&nbsp;

    [NetLocalGroupAddMembers](#win32net.md#win32netNetLocalGroupAddMembers)

    Adds users to a local group.&nbsp;

    [NetLocalGroupDelMembers](#win32net.md#win32netNetLocalGroupDelMembers)

    Deletes users from a local group.&nbsp;

    [NetGroupDel](#win32net.md#win32netNetGroupDel)

    Deletes a group.&nbsp;

    [NetGroupEnum](#win32net.md#win32netNetGroupEnum)

    Enumerates the groups.&nbsp;

    [NetGroupGetInfo](#win32net.md#win32netNetGroupGetInfo)

    Retrieves information about a particular group on a server.&nbsp;

    [NetLocalGroupGetMembers](#win32net.md#win32netNetLocalGroupGetMembers)

    Enumerates the members in a local group.&nbsp;

    [NetGroupSetInfo](#win32net.md#win32netNetGroupSetInfo)

    Sets information about a particular group account on a server.&nbsp;

    [NetLocalGroupSetMembers](#win32net.md#win32netNetLocalGroupSetMembers)

    Sets the members of a local group.  Any existing members not listed are removed.&nbsp;

    [NetMessageBufferSend](#win32net.md#win32netNetMessageBufferSend)

    sends a string to a registered message alias.&nbsp;

    [NetMessageNameAdd](#win32net.md#win32netNetMessageNameAdd)

    Add a message alias for a computer&nbsp;

    [NetMessageNameDel](#win32net.md#win32netNetMessageNameDel)

    Removes a message alias&nbsp;

    [NetMessageNameEnum](#win32net.md#win32netNetMessageNameEnum)

    List message aliases for a computer&nbsp;

    [NetServerEnum](#win32net.md#win32netNetServerEnum)

    Retrieves information about all servers of a specific type&nbsp;

    [NetServerGetInfo](#win32net.md#win32netNetServerGetInfo)

    Retrieves information about a particular server.&nbsp;

    [NetServerSetInfo](#win32net.md#win32netNetServerSetInfo)

    Sets information about a particular server.&nbsp;

    [NetShareAdd](#win32net.md#win32netNetShareAdd)

    Creates a new share.&nbsp;

    [NetShareDel](#win32net.md#win32netNetShareDel)

    Deletes a share&nbsp;

    [NetShareCheck](#win32net.md#win32netNetShareCheck)

    Checks if server is sharing a device&nbsp;

    [NetShareEnum](#win32net.md#win32netNetShareEnum)

    Retrieves information about each shared resource on a server.&nbsp;

    [NetShareGetInfo](#win32net.md#win32netNetShareGetInfo)

    Retrieves information about a particular share on a server.&nbsp;

    [NetShareSetInfo](#win32net.md#win32netNetShareSetInfo)

    Sets information about a particular share on a server.&nbsp;

    [NetUserAdd](#win32net.md#win32netNetUserAdd)

    Creates a new user.&nbsp;

    [NetUserChangePassword](#win32net.md#win32netNetUserChangePassword)

    Changes a users password on the specified domain.&nbsp;

    [NetUserEnum](#win32net.md#win32netNetUserEnum)

    Enumerates all users.&nbsp;

    [NetUserGetGroups](#win32net.md#win32netNetUserGetGroups)

    Returns a list of groups,attributes for all groups for the user.&nbsp;

    [NetUserGetInfo](#win32net.md#win32netNetUserGetInfo)

    Retrieves information about a particular user account on a server.&nbsp;

    [NetUserGetLocalGroups](#win32net.md#win32netNetUserGetLocalGroups)

    Retrieves a list of local groups to which a specified user belongs.&nbsp;

    [NetUserSetInfo](#win32net.md#win32netNetUserSetInfo)

    Sets information about a particular user account on a server.&nbsp;

    [NetUserDel](#win32net.md#win32netNetUserDel)

    Deletes a user.&nbsp;

    [NetUserModalsGet](#win32net.md#win32netNetUserModalsGet)

    Retrieves global user information on a server.&nbsp;

    [NetUserModalsSet](#win32net.md#win32netNetUserModalsSet)

    Sets global user information on a server.&nbsp;

    [NetWkstaUserEnum](#win32net.md#win32netNetWkstaUserEnum)

    Retrieves information about all users currently logged on to the workstation.&nbsp;

    [NetWkstaGetInfo](#win32net.md#win32netNetWkstaGetInfo)

    returns information about the configuration elements for a workstation.&nbsp;

    [NetWkstaSetInfo](#win32net.md#win32netNetWkstaSetInfo)

    Sets information about the configuration elements for a workstation.&nbsp;

    [NetWkstaTransportEnum](#win32net.md#win32netNetWkstaTransportEnum)

    Retrieves information about transport protocols that are currently managed by the redirector.&nbsp;

    [NetWkstaTransportAdd](#win32net.md#win32netNetWkstaTransportAdd)

    binds the redirector to a transport.&nbsp;

    [NetWkstaTransportDel](#win32net.md#win32netNetWkstaTransportDel)

    unbinds transport protocol from the redirector.&nbsp;

    [NetServerDiskEnum](#win32net.md#win32netNetServerDiskEnum)

    Retrieves the list of disk drives on a server.&nbsp;

    [NetUseAdd](#win32net.md#win32netNetUseAdd)

    Establishes connection between local or NULL device name and a shared resource through redirector.&nbsp;

    [NetUseDel](#win32net.md#win32netNetUseDel)

    Ends connection to a shared resource.&nbsp;

    [NetUseEnum](#win32net.md#win32netNetUseEnum)

    Enumerates connection between local machine and shared resources on remote computers.&nbsp;

    [NetUseGetInfo](#win32net.md#win32netNetUseGetInfo)

    Get information about locally mapped shared resource on remote computer.&nbsp;

    [NetGetAnyDCName](#win32net.md#win32netNetGetAnyDCName)

    Returns the name of any domain controller trusted by the specified server.&nbsp;

    [NetGetDCName](#win32net.md#win32netNetGetDCName)

    Returns the name of the primary domain controller (PDC).&nbsp;

    [NetSessionEnum](#win32net.md#win32netNetSessionEnum)

    Returns network session for the server, limited to single client and/or user if specified.&nbsp;

    [NetSessionDel](#win32net.md#win32netNetSessionDel)

    Delete network session for specified server, client computer and user. Returns None on success.&nbsp;

    [NetSessionGetInfo](#win32net.md#win32netNetSessionGetInfo)

    Get network session information.&nbsp;

    [NetFileEnum](#win32net.md#win32netNetFileEnum)

    Returns open file resources for server (single client and/or user may also be passed as criteria).&nbsp;

    [NetFileClose](#win32net.md#win32netNetFileClose)

    Closes file for specified server and file id.&nbsp;

    [NetFileGetInfo](#win32net.md#win32netNetFileGetInfo)

    Get info about files open on the server.&nbsp;

    [NetStatisticsGet](#win32net.md#win32netNetStatisticsGet)

    Return server or workstation stats&nbsp;

    [NetServerComputerNameAdd](#win32net.md#win32netNetServerComputerNameAdd)

    Adds an extra network name for a server&nbsp;

    [NetServerComputerNameDel](#win32net.md#win32netNetServerComputerNameDel)

    Deletes an emulated computer name created by **win32net::PyNetServerComputerNameAdd** &nbsp;

    [NetValidateName](#win32net.md#win32netNetValidateName)

    Verify that computer/domain name is valid for given context&nbsp;

    [NetValidatePasswordPolicy](#win32net.md#win32netNetValidatePasswordPolicy)

    Allows an application to check password compliance against an application-provided account database.&nbsp;
------

##[win32transaction](md/win32transaction.md)

## Module win32transaction

Module wrapping Kernal Transaction Manager functions, as used with 

transacted NTFS and transacted registry functions.

#### Comments
These functions are only available on Vista and later.
All functions accept keyword arguments.

#### Methods


    [CreateTransaction](#win32transaction.md#win32transactionCreateTransaction)

    Creates a transaction&nbsp;

    [RollbackTransaction](#win32transaction.md#win32transactionRollbackTransaction)

    Rolls back a transaction&nbsp;

    [RollbackTransactionAsync](#win32transaction.md#win32transactionRollbackTransactionAsync)

    Rolls back a transaction asynchronously&nbsp;

    [CommitTransaction](#win32transaction.md#win32transactionCommitTransaction)

    Commits a transaction&nbsp;

    [CommitTransactionAsync](#win32transaction.md#win32transactionCommitTransactionAsync)

    Commits a transaction asynchronously&nbsp;

    [GetTransactionId](#win32transaction.md#win32transactionGetTransactionId)

    Returns the transaction's GUID&nbsp;

    [OpenTransaction](#win32transaction.md#win32transactionOpenTransaction)

    Creates a handle to an existing transaction&nbsp;
------

##[win32timezone.TimeZoneDefinition](md/win32timezone.TimeZoneDefinition.md)

## win32timezone.TimeZoneDefinition Object

A time zone definition class based on the win32 

DYNAMIC_TIME_ZONE_INFORMATION structure.

#### Comments
Describes a bias against UTC (bias), and two dates at which a separate 

additional bias applies (standard_bias and daylight_bias).

#### Methods


    [current](#win32timezone.TimeZoneDefinition.md#win32timezone.TimeZoneDefinitioncurrent)

    Windows Platform SDK GetTimeZoneInformation&nbsp;
------

##[win32wnet](md/win32wnet.md)

## Module win32wnet

A module that exposes the Windows Networking API.

#### Methods


    [NETRESOURCE](#win32wnet.md#win32wnetNETRESOURCE)

    The[PyNETRESOURCE](#README.md#PyNETRESOURCE)type - can be used to create a new[PyNETRESOURCE](#README.md#PyNETRESOURCE)object.&nbsp;

    [NCB](#win32wnet.md#win32wnetNCB)

    The **PyNCB** type - can be used to create a new **PyNCB** object.&nbsp;

    [NCBBuffer](#win32wnet.md#win32wnetNCBBuffer)

    Creates a new buffer&nbsp;

    [Netbios](#win32wnet.md#win32wnetNetbios)

    Executes a Netbios call.&nbsp;

    [WNetAddConnection2](#win32wnet.md#win32wnetWNetAddConnection2)

    Creates a connection to a network resource.&nbsp;

    [WNetAddConnection3](#win32wnet.md#win32wnetWNetAddConnection3)

    Creates a connection to a network resource.&nbsp;

    [WNetCancelConnection2](#win32wnet.md#win32wnetWNetCancelConnection2)

    Closes network connections made by WNetAddConnection2 or 3&nbsp;

    [WNetOpenEnum](#win32wnet.md#win32wnetWNetOpenEnum)

    Opens an Enumeration Handle for Enumerating Resources with[win32wnet::WNetEnumResource](#win32wnet.md#win32wnetWNetEnumResource)&nbsp;

    [WNetCloseEnum](#win32wnet.md#win32wnetWNetCloseEnum)

    Closes a PyHANDLE that represents an Open Enumeration (from[win32wnet::WNetOpenEnum](#win32wnet.md#win32wnetWNetOpenEnum))&nbsp;

    [WNetEnumResource](#win32wnet.md#win32wnetWNetEnumResource)

    Enumerates a list of resources&nbsp;

    [WNetGetUser](#win32wnet.md#win32wnetWNetGetUser)

    Retrieves the current default user name, or the user name used to establish a network connection.&nbsp;

    [WNetGetUniversalName](#win32wnet.md#win32wnetWNetGetUniversalName)

    Takes a drive-based path for a network resource and returns an information structure that contains a more universal form of the name.&nbsp;

    [WNetGetResourceInformation](#win32wnet.md#win32wnetWNetGetResourceInformation)

    Finds the type and provider of a network resource&nbsp;

    [WNetGetLastError](#win32wnet.md#win32wnetWNetGetLastError)

    Retrieves extended error information set by a network provider when one of the WNet* functions fails&nbsp;

    [WNetGetResourceParent](#win32wnet.md#win32wnetWNetGetResourceParent)

    Finds the parent resource of a network resource&nbsp;

    [WNetGetConnection](#win32wnet.md#win32wnetWNetGetConnection)

    Retrieves the name of the network resource associated with a local device.&nbsp;
------

##[win32timezone.TimeZoneInfo](md/win32timezone.TimeZoneInfo.md)

## win32timezone.TimeZoneInfo Object

Main class for handling Windows time zones. 

Usage: 

TimeZoneInfo(&ltTime Zone Standard Name&gt, [&ltFix Standard Time&gt])

#### Comments
If &ltFix Standard Time&gt evaluates to True, daylight savings time is 

calculated in the same way as standard time.
&gt&gt&gt tzi = TimeZoneInfo('Pacific Standard Time')

&gt&gt&gt march31 = datetime.datetime(2000,3,31)
We know that time zone definitions haven't changed from 2007 

to 2012, so regardless of whether dynamic info is available, 

there should be consistent results for these years.
&gt&gt&gt subsequent_years = [march31.replace(year=year)

...     for year in range(2007, 2013)]

&gt&gt&gt offsets = set(tzi.utcoffset(year) for year in subsequent_years)

&gt&gt&gt len(offsets)

1

#### Methods


    [GetDSTStartTime](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfoGetDSTStartTime)

    Given a year, determines the time when daylight savings time starts&nbsp;

    [get_sorted_time_zones](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfoget_sorted_time_zones)

    Return the time zones sorted by some key.&nbsp;

    [utc](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfoutc)

    Returns a time-zone representing UTC.&nbsp;

    [GetDSTEndTime](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfoGetDSTEndTime)

    Given a year, determines the time when daylight savings ends.&nbsp;

    [dst](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfodst)

    Calculates the daylight savings offset according to the datetime.tzinfo spec&nbsp;

    [get_sorted_time_zone_names](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfoget_sorted_time_zone_names)

    Return a list of time zone names that can be used to initialize TimeZoneInfo instances&nbsp;

    [utcoffset](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfoutcoffset)

    Calculates the utcoffset according to the datetime.tzinfo spec&nbsp;

    [getWinInfo](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfogetWinInfo)

    Return the most relevant "info" for this time zone&nbsp;

    [local](#win32timezone.TimeZoneInfo.md#win32timezone.TimeZoneInfolocal)

    Returns the local time zone as defined by the operating system in the&nbsp;
------

##[win32job](md/win32job.md)

## Module win32job

An interface to the win32 Process and Thread API's, 

available in Windows 2000 and later.

#### Methods


    [AssignProcessToJobObject](#win32job.md#win32jobAssignProcessToJobObject)

    Associates a process with an existing job object.&nbsp;

    [CreateJobObject](#win32job.md#win32jobCreateJobObject)

    Creates or opens a job object.&nbsp;

    [OpenJobObject](#win32job.md#win32jobOpenJobObject)

    Opens an existing job object.&nbsp;

    [TerminateJobObject](#win32job.md#win32jobTerminateJobObject)

    Terminates all processes currently associated with the job.&nbsp;

    [UserHandleGrantAccess](#win32job.md#win32jobUserHandleGrantAccess)

    Grants or denies access to a handle to a User object to a job that has a user-interface restriction.&nbsp;

    [IsProcessInJob](#win32job.md#win32jobIsProcessInJob)

    Determines if the process is running in the specified job.&nbsp;

    [QueryInformationJobObject](#win32job.md#win32jobQueryInformationJobObject)

    Retrieves limit and job state information from the job object.&nbsp;

    [SetInformationJobObject](#win32job.md#win32jobSetInformationJobObject)

    Sets quotas and limits for a job&nbsp;
------

##[win32console](md/win32console.md)

## Module win32console

Interface to the Windows Console functions for dealing with character-mode applications

#### Methods


    [CreateConsoleScreenBuffer](#win32console.md#win32consoleCreateConsoleScreenBuffer)

    Creates a new console handle&nbsp;

    [GetConsoleDisplayMode](#win32console.md#win32consoleGetConsoleDisplayMode)

    Returns the current console's display mode&nbsp;

    [AttachConsole](#win32console.md#win32consoleAttachConsole)

    Attaches calling process to console of another process&nbsp;

    [AllocConsole](#win32console.md#win32consoleAllocConsole)

    Creates a new console for the calling process&nbsp;

    [FreeConsole](#win32console.md#win32consoleFreeConsole)

    Detaches process from its console&nbsp;

    [GetConsoleProcessList](#win32console.md#win32consoleGetConsoleProcessList)

    Returns pids of all processes attached to current console&nbsp;

    [GetConsoleCP](#win32console.md#win32consoleGetConsoleCP)

    Returns the input code page for calling process's console&nbsp;

    [GetConsoleOutputCP](#win32console.md#win32consoleGetConsoleOutputCP)

    Returns the output code page for calling process's console&nbsp;

    [SetConsoleCP](#win32console.md#win32consoleSetConsoleCP)

    Sets the input code page for calling process's console&nbsp;

    [SetConsoleOutputCP](#win32console.md#win32consoleSetConsoleOutputCP)

    Sets the output code page for calling process's console&nbsp;

    [GetConsoleSelectionInfo](#win32console.md#win32consoleGetConsoleSelectionInfo)

    Returns info on text selection within the current console&nbsp;

    [AddConsoleAlias](#win32console.md#win32consoleAddConsoleAlias)

    Creates a new console alias&nbsp;

    [GetConsoleAliases](#win32console.md#win32consoleGetConsoleAliases)

    Retrieves aliases defined under specified executable&nbsp;

    [GetConsoleAliasExes](#win32console.md#win32consoleGetConsoleAliasExes)

    Lists all executables that have console aliases defined&nbsp;

    [GetConsoleWindow](#win32console.md#win32consoleGetConsoleWindow)

    Returns a handle to the console's window, or 0 if none exists&nbsp;

    [GetNumberOfConsoleFonts](#win32console.md#win32consoleGetNumberOfConsoleFonts)

    Returns the number of fonts available to the console&nbsp;

    [SetConsoleTitle](#win32console.md#win32consoleSetConsoleTitle)

    Sets the title of calling process's console&nbsp;

    [GetConsoleTitle](#win32console.md#win32consoleGetConsoleTitle)

    Returns the title of console to which calling process is attached&nbsp;

    [GenerateConsoleCtrlEvent](#win32console.md#win32consoleGenerateConsoleCtrlEvent)

    Sends a control signal to a group of processes attached to a common console&nbsp;

    [GetStdHandle](#win32console.md#win32consoleGetStdHandle)

    Returns one of calling process's standard handles&nbsp;
------

##[win32clipboard](md/win32clipboard.md)

## Module win32clipboard

A module which supports the Windows Clipboard API.

#### Methods


    [ChangeClipboardChain](#win32clipboard.md#win32clipboardChangeClipboardChain)

    Removes a specified window from the chain 

of clipboard viewers.&nbsp;

    [CloseClipboard](#win32clipboard.md#win32clipboardCloseClipboard)

    Closes the clipboard.&nbsp;

    [CountClipboardFormats](#win32clipboard.md#win32clipboardCountClipboardFormats)

    Retrieves the number of different data 

formats currently on the clipboard.&nbsp;

    [EmptyClipboard](#win32clipboard.md#win32clipboardEmptyClipboard)

    Empties the clipboard and frees handles to data 

in the clipboard.&nbsp;

    [EnumClipboardFormats](#win32clipboard.md#win32clipboardEnumClipboardFormats)

    Lets you enumerate the data formats that 

are currently available on the clipboard.&nbsp;

    [GetClipboardData](#win32clipboard.md#win32clipboardGetClipboardData)

    Retrieves data from the clipboard in a 

specified format.&nbsp;

    [GetClipboardDataHandle](#win32clipboard.md#win32clipboardGetClipboardDataHandle)

    Retrieves data from the clipboard in a 

specified format, returning the underlying integer handle.&nbsp;

    [GetClipboardFormatName](#win32clipboard.md#win32clipboardGetClipboardFormatName)

    Retrieves from the clipboard the name 

of the specified registered format.&nbsp;

    [GetClipboardOwner](#win32clipboard.md#win32clipboardGetClipboardOwner)

    Retrieves the window handle of the current 

owner of the clipboard.&nbsp;

    [GetClipboardSequenceNumber](#win32clipboard.md#win32clipboardGetClipboardSequenceNumber)

    Returns the clipboard sequence number 

for the current window station.&nbsp;

    [GetClipboardViewer](#win32clipboard.md#win32clipboardGetClipboardViewer)

    Retrieves the handle of the first window in 

the clipboard viewer chain.&nbsp;

    [GetGlobalMemory](#win32clipboard.md#win32clipboardGetGlobalMemory)

    Returns the contents of the specified global 

memory object.&nbsp;

    [GetOpenClipboardWindow](#win32clipboard.md#win32clipboardGetOpenClipboardWindow)

    Retrieves the handle of the window that 

currently has the clipboard open.&nbsp;

    [GetPriorityClipboardFormat](#win32clipboard.md#win32clipboardGetPriorityClipboardFormat)

    Returns the first available clipboard 

format in the specified list.&nbsp;

    [IsClipboardFormatAvailable](#win32clipboard.md#win32clipboardIsClipboardFormatAvailable)

    Determines whether the clipboard 

contains data in the specified format.&nbsp;

    [OpenClipboard](#win32clipboard.md#win32clipboardOpenClipboard)

    Opens the clipboard for examination.&nbsp;

    [RegisterClipboardFormat](#win32clipboard.md#win32clipboardRegisterClipboardFormat)

    Registers a new clipboard format.&nbsp;

    [SetClipboardData](#win32clipboard.md#win32clipboardSetClipboardData)

    Places data on the clipboard in a specified 

clipboard format.&nbsp;

    [SetClipboardText](#win32clipboard.md#win32clipboardSetClipboardText)

    Places text on the clipboard .&nbsp;

    [SetClipboardViewer](#win32clipboard.md#win32clipboardSetClipboardViewer)

    Adds the specified window to the chain of 

clipboard viewers&nbsp;
------

##[win32event](md/win32event.md)

## Module win32event

A module which provides an interface to the win32 event/wait API

#### Methods


    [CancelWaitableTimer](#win32event.md#win32eventCancelWaitableTimer)

    Cancels a waiting timer.&nbsp;

    [CreateEvent](#win32event.md#win32eventCreateEvent)

    Creates a waitable event&nbsp;

    [CreateMutex](#win32event.md#win32eventCreateMutex)

    Creates a mutex&nbsp;

    [CreateSemaphore](#win32event.md#win32eventCreateSemaphore)

    Creates a semaphore, or opens an existing one&nbsp;

    [CreateWaitableTimer](#win32event.md#win32eventCreateWaitableTimer)

    Creates a waitable timer, or opens an existing one&nbsp;

    [MsgWaitForMultipleObjects](#win32event.md#win32eventMsgWaitForMultipleObjects)

    Returns when a message arrives of an event is signalled&nbsp;

    [MsgWaitForMultipleObjectsEx](#win32event.md#win32eventMsgWaitForMultipleObjectsEx)

    Returns when a message arrives of an event is signalled&nbsp;

    [OpenEvent](#win32event.md#win32eventOpenEvent)

    Returns a handle of an existing named event object.&nbsp;

    [OpenMutex](#win32event.md#win32eventOpenMutex)

    Returns a handle of an existing named mutex object.&nbsp;

    [OpenSemaphore](#win32event.md#win32eventOpenSemaphore)

    Returns a handle of an existing named semaphore object.&nbsp;

    [OpenWaitableTimer](#win32event.md#win32eventOpenWaitableTimer)

    Opens an existing named waitable timer object&nbsp;

    [PulseEvent](#win32event.md#win32eventPulseEvent)

    Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.&nbsp;

    [ReleaseMutex](#win32event.md#win32eventReleaseMutex)

    Releases a mutex.&nbsp;

    [ReleaseSemaphore](#win32event.md#win32eventReleaseSemaphore)

    Releases a semaphore.&nbsp;

    [ResetEvent](#win32event.md#win32eventResetEvent)

    Resets an event&nbsp;

    [SetEvent](#win32event.md#win32eventSetEvent)

    Sets an event&nbsp;

    [SetWaitableTimer](#win32event.md#win32eventSetWaitableTimer)

    Sets a waitable timer.&nbsp;

    [WaitForMultipleObjects](#win32event.md#win32eventWaitForMultipleObjects)

    Returns when an event is signalled&nbsp;

    [WaitForMultipleObjectsEx](#win32event.md#win32eventWaitForMultipleObjectsEx)

    Returns when an event is signalled&nbsp;

    [WaitForSingleObject](#win32event.md#win32eventWaitForSingleObject)

    Returns when an event is signalled&nbsp;

    [WaitForSingleObjectEx](#win32event.md#win32eventWaitForSingleObjectEx)

    Returns when an event is signalled&nbsp;

    [WaitForInputIdle](#win32event.md#win32eventWaitForInputIdle)

    Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed&nbsp;
------

##[win32cred](md/win32cred.md)

## Module win32cred

Interface to credentials management functions. 

The functions in this module are only available on Windows XP and later.
Functions operate only on the credential set of the calling user.
User's profile must be loaded for stored credentials to be accessible.
Each credential is uniquely identified by its TargetName and Type.
All functions accept keyword arguments.

#### Methods


    [CredMarshalCredential](#win32cred.md#win32credCredMarshalCredential)

    Marshals a credential into a unicode string&nbsp;

    [CredUnmarshalCredential](#win32cred.md#win32credCredUnmarshalCredential)

    Unmarshals credentials formatted using[win32cred::CredMarshalCredential](#win32cred.md#win32credCredMarshalCredential)&nbsp;

    [CredIsMarshaledCredential](#win32cred.md#win32credCredIsMarshaledCredential)

    Checks if a string matches the form of a marshaled credential&nbsp;

    [CredEnumerate](#win32cred.md#win32credCredEnumerate)

    Lists stored credentials for current logon session&nbsp;

    [CredGetTargetInfo](#win32cred.md#win32credCredGetTargetInfo)

    Determines type and location of credential target&nbsp;

    [CredWriteDomainCredentials](#win32cred.md#win32credCredWriteDomainCredentials)

    Creates or updates credential for a domain or server&nbsp;

    [CredReadDomainCredentials](#win32cred.md#win32credCredReadDomainCredentials)

    Retrieves a user's credentials for a domain or server&nbsp;

    [CredDelete](#win32cred.md#win32credCredDelete)

    Deletes a stored credential&nbsp;

    [CredWrite](#win32cred.md#win32credCredWrite)

    Creates or updates a stored credential&nbsp;

    [CredRead](#win32cred.md#win32credCredRead)

    Retrieves a stored credential&nbsp;

    [CredRename](#win32cred.md#win32credCredRename)

    Changes the target name of stored credentials&nbsp;

    [CredUICmdLinePromptForCredentials](#win32cred.md#win32credCredUICmdLinePromptForCredentials)

    Prompt for username/passwd from a console app&nbsp;

    [CredUIPromptForCredentials](#win32cred.md#win32credCredUIPromptForCredentials)

    Initiates dialog to request user credentials&nbsp;

    [CredUIConfirmCredentials](#win32cred.md#win32credCredUIConfirmCredentials)

    Confirms whether credentials entered by user are valid or not&nbsp;

    [CredUIReadSSOCredW](#win32cred.md#win32credCredUIReadSSOCredW)

    Retrieves single sign on username&nbsp;

    [CredUIStoreSSOCredW](#win32cred.md#win32credCredUIStoreSSOCredW)

    Creates a single sign on credential&nbsp;

    [CredUIParseUserName](#win32cred.md#win32credCredUIParseUserName)

    Parses a full username into domain and username&nbsp;
------

##[win32ras](md/win32ras.md)

## Module win32ras

A module encapsulating the Windows Remote Access Service (RAS) API.

#### Methods


    [CreatePhonebookEntry](#win32ras.md#win32rasCreatePhonebookEntry)

    Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry.&nbsp;

    [Dial](#win32ras.md#win32rasDial)

    Establishes a RAS connection to a RAS server.&nbsp;

    [EditPhonebookEntry](#win32ras.md#win32rasEditPhonebookEntry)

    Creates a new phonebook entry.  The function displays a dialog box into which the user can enter information about the entry&nbsp;

    [EnumConnections](#win32ras.md#win32rasEnumConnections)

    Returns a list of tuples, one for each active connection.&nbsp;

    [EnumEntries](#win32ras.md#win32rasEnumEntries)

    Returns a list of tuples, one for each phonebook entry.&nbsp;

    [GetConnectStatus](#win32ras.md#win32rasGetConnectStatus)

    Returns a tuple with connection information.&nbsp;

    [GetEntryDialParams](#win32ras.md#win32rasGetEntryDialParams)

    Returns a tuple with the most recently set dial parameters for the specified entry.&nbsp;

    [GetErrorString](#win32ras.md#win32rasGetErrorString)

    Returns an error string for a RAS error code.&nbsp;

    [HangUp](#win32ras.md#win32rasHangUp)

    Terminates a remote access session.&nbsp;

    [IsHandleValid](#win32ras.md#win32rasIsHandleValid)

    Indicates if the given RAS handle is valid.&nbsp;

    [SetEntryDialParams](#win32ras.md#win32rasSetEntryDialParams)

    Sets the dial parameters for the specified entry.&nbsp;

    [RASDIALEXTENSIONS](#win32ras.md#win32rasRASDIALEXTENSIONS)

    Creates a new[RASDIALEXTENSIONS](#README.md#RASDIALEXTENSIONS)object&nbsp;
------

##[win32ui](md/win32ui.md)

## Module win32ui

A module, encapsulating the Microsoft Foundation Classes.

#### Methods


    [AddToRecentFileList](#win32ui.md#win32uiAddToRecentFileList)

    Add a file name to the Recent File List.&nbsp;

    [ComparePath](#win32ui.md#win32uiComparePath)

    Compares 2 paths.&nbsp;

    [CreateMDIFrame](#win32ui.md#win32uiCreateMDIFrame)

    Creates an MDI Frame window.&nbsp;

    [CreateMDIChild](#win32ui.md#win32uiCreateMDIChild)

    Creates an MDI Child window.&nbsp;

    [CreateBitmap](#win32ui.md#win32uiCreateBitmap)

    Create a bitmap object.&nbsp;

    [CreateBitmapFromHandle](#win32ui.md#win32uiCreateBitmapFromHandle)

    Creates a bitmap object from a HBITMAP.&nbsp;

    [CreateBrush](#win32ui.md#win32uiCreateBrush)

    Creates a new GDI brush object.  Returns a[PyCBrush](#README.md#PyCBrush)object.&nbsp;

    [CreateButton](#win32ui.md#win32uiCreateButton)

    Creates a button object.[PyCButton::CreateWindow](#PyCButton.md#PyCButtonCreateWindow)creates the actual control.&nbsp;

    [CreateColorDialog](#win32ui.md#win32uiCreateColorDialog)

    Creates a color selection dialog box.&nbsp;

    [CreateControl](#win32ui.md#win32uiCreateControl)

    Creates an OLE control.&nbsp;

    [CreateControlBar](#win32ui.md#win32uiCreateControlBar)

    Creates an ControlBar&nbsp;

    [CreateCtrlView](#win32ui.md#win32uiCreateCtrlView)

    Creates a control view object.&nbsp;

    [CreateDC](#win32ui.md#win32uiCreateDC)

    Creates a[PyCDC](#README.md#PyCDC)object.&nbsp;

    [CreateDCFromHandle](#win32ui.md#win32uiCreateDCFromHandle)

    Creates a[PyCDC](#README.md#PyCDC)object from an integer handle.&nbsp;

    [CreateDialog](#win32ui.md#win32uiCreateDialog)

    Creates a[PyCDialog](#README.md#PyCDialog)object.&nbsp;

    [CreateDialogBar](#win32ui.md#win32uiCreateDialogBar)

    Creates a[PyCDialogBar](#README.md#PyCDialogBar)object.&nbsp;

    [CreateDialogIndirect](#win32ui.md#win32uiCreateDialogIndirect)

    Creates a[PyCDialog](#README.md#PyCDialog)object from a template.&nbsp;

    [CreatePrintDialog](#win32ui.md#win32uiCreatePrintDialog)

    Creates a[PyCPrintDialog](#README.md#PyCPrintDialog)object.&nbsp;

    [CreateDocTemplate](#win32ui.md#win32uiCreateDocTemplate)

    Create a[PyCDocTemplate](#README.md#PyCDocTemplate)object.&nbsp;

    [CreateEdit](#win32ui.md#win32uiCreateEdit)

    Creates an edit object.[PyCEdit::CreateWindow](#PyCEdit.md#PyCEditCreateWindow)creates the actual control.&nbsp;

    [CreateFileDialog](#win32ui.md#win32uiCreateFileDialog)

    Creates a FileOpen common dialog.&nbsp;

    [CreateFontDialog](#win32ui.md#win32uiCreateFontDialog)

    Creates a font selection dialog box.&nbsp;

    [CreateFormView](#win32ui.md#win32uiCreateFormView)

    Creates a form view object.&nbsp;

    [CreateFrame](#win32ui.md#win32uiCreateFrame)

    Creates a frame window.&nbsp;

    [CreateImageList](#win32ui.md#win32uiCreateImageList)

    Creates an[PyCImageList](#README.md#PyCImageList)object.&nbsp;

    [CreateListCtrl](#win32ui.md#win32uiCreateListCtrl)

    Creates a list control.&nbsp;

    [CreateListView](#win32ui.md#win32uiCreateListView)

    Creates a[PyCListView](#README.md#PyCListView)object.&nbsp;

    [CreateTreeCtrl](#win32ui.md#win32uiCreateTreeCtrl)

    Creates a tree control.&nbsp;

    [CreateTreeView](#win32ui.md#win32uiCreateTreeView)

    Creates a[PyCTreeView](#README.md#PyCTreeView)object.&nbsp;

    [CreatePalette](#win32ui.md#win32uiCreatePalette)

    Returns a HPALETTE&nbsp;

    [CreatePopupMenu](#win32ui.md#win32uiCreatePopupMenu)

    Creates a popup menu.&nbsp;

    [CreateMenu](#win32ui.md#win32uiCreateMenu)

    Creates a menu&nbsp;

    [CreatePen](#win32ui.md#win32uiCreatePen)

    Creates a **PyCPen** object.&nbsp;

    [CreateProgressCtrl](#win32ui.md#win32uiCreateProgressCtrl)

    Creates a progress bar object.[PyCProgressCtrl::CreateWindow](#PyCProgressCtrl.md#PyCProgressCtrlCreateWindow)creates the actual control.&nbsp;

    [CreatePropertyPage](#win32ui.md#win32uiCreatePropertyPage)

    Creates a[PyCPropertyPage](#README.md#PyCPropertyPage)object.&nbsp;

    [CreatePropertyPageIndirect](#win32ui.md#win32uiCreatePropertyPageIndirect)

    Creates a[PyCPropertyPage](#README.md#PyCPropertyPage)object from a template.&nbsp;

    [CreatePropertySheet](#win32ui.md#win32uiCreatePropertySheet)

    Creates a[PyCPropertySheet](#README.md#PyCPropertySheet)object&nbsp;

    [CreateRectRgn](#win32ui.md#win32uiCreateRectRgn)

    Initializes a[PyCRgn](#README.md#PyCRgn)to a rectangle&nbsp;

    [CreateRgn](#win32ui.md#win32uiCreateRgn)

    Creates a new[PyCRgn](#README.md#PyCRgn)object.&nbsp;

    [CreateRichEditCtrl](#win32ui.md#win32uiCreateRichEditCtrl)

    Creates a rich edit control.&nbsp;

    [CreateRichEditDocTemplate](#win32ui.md#win32uiCreateRichEditDocTemplate)

    Create a[PyCRichEditDocTemplate](#README.md#PyCRichEditDocTemplate)object.&nbsp;

    [CreateRichEditView](#win32ui.md#win32uiCreateRichEditView)

    Creates a[PyCRichEditView](#README.md#PyCRichEditView)object.&nbsp;

    [CreateSliderCtrl](#win32ui.md#win32uiCreateSliderCtrl)

    Creates a slider control object.[PyCSliderCtrl::CreateWindow](#PyCSliderCtrl.md#PyCSliderCtrlCreateWindow)creates the actual control.&nbsp;

    [CreateSplitter](#win32ui.md#win32uiCreateSplitter)

    Creates a splitter window.&nbsp;

    [CreateStatusBar](#win32ui.md#win32uiCreateStatusBar)

    Creates a status bar object.&nbsp;

    [CreateStatusBarCtrl](#win32ui.md#win32uiCreateStatusBarCtrl)

    Creates a new status bar control object.[PyCStatusBarCtrl::CreateWindow](#PyCStatusBarCtrl.md#PyCStatusBarCtrlCreateWindow)creates the actual control.&nbsp;

    [CreateFont](#win32ui.md#win32uiCreateFont)

    Creates a[PyCFont](#README.md#PyCFont)object.&nbsp;

    [CreateToolBar](#win32ui.md#win32uiCreateToolBar)

    Creates a toolbar object.&nbsp;

    [CreateToolBarCtrl](#win32ui.md#win32uiCreateToolBarCtrl)

    Creates a toolbar object.&nbsp;

    [CreateToolTipCtrl](#win32ui.md#win32uiCreateToolTipCtrl)

    Creates a tooltip control object.&nbsp;

    [CreateThread](#win32ui.md#win32uiCreateThread)

    Creates a[PyCWinThread](#README.md#PyCWinThread)object.&nbsp;

    [CreateView](#win32ui.md#win32uiCreateView)

    Creates a[PyCView](#README.md#PyCView)object.&nbsp;

    [CreateEditView](#win32ui.md#win32uiCreateEditView)

    Creates an[PyCEditView](#README.md#PyCEditView)object.&nbsp;

    [CreateDebuggerThread](#win32ui.md#win32uiCreateDebuggerThread)

    Starts a debugging thread.&nbsp;

    [CreateWindowFromHandle](#win32ui.md#win32uiCreateWindowFromHandle)

    Creates a[PyCWnd](#README.md#PyCWnd)from an integer containing a HWND&nbsp;

    [CreateWnd](#win32ui.md#win32uiCreateWnd)

    Create a new unitialized[PyCWnd](#README.md#PyCWnd)object&nbsp;

    [DestroyDebuggerThread](#win32ui.md#win32uiDestroyDebuggerThread)

    Cleans up the debugger thread.&nbsp;

    [DoWaitCursor](#win32ui.md#win32uiDoWaitCursor)

    Changes the cursor to/from a wait cursor.&nbsp;

    [DisplayTraceback](#win32ui.md#win32uiDisplayTraceback)

    Displays a traceback in a dialog box.&nbsp;

    [Enable3dControls](#win32ui.md#win32uiEnable3dControls)

    Enables 3d controls for the application.&nbsp;

    [FindWindow](#win32ui.md#win32uiFindWindow)

    Searches for the specified top-level window&nbsp;

    [FindWindowEx](#win32ui.md#win32uiFindWindowEx)

    Searches for the specified top-level or child window&nbsp;

    [FullPath](#win32ui.md#win32uiFullPath)

    Returns the full path name of the file.&nbsp;

    [GetActiveWindow](#win32ui.md#win32uiGetActiveWindow)

    Retrieves the active window.&nbsp;

    [GetApp](#win32ui.md#win32uiGetApp)

    Retrieves the application object.&nbsp;

    [GetAppName](#win32ui.md#win32uiGetAppName)

    Retrieves the name of the current application.&nbsp;

    [GetAppRegistryKey](#win32ui.md#win32uiGetAppRegistryKey)

    Returns the registry key for the application.&nbsp;

    [GetBytes](#win32ui.md#win32uiGetBytes)

    Gets raw bytes from memory&nbsp;

    [GetCommandLine](#win32ui.md#win32uiGetCommandLine)

    Returns the command line for hte application.&nbsp;

    [GetDeviceCaps](#win32ui.md#win32uiGetDeviceCaps)

    Calls the API version of GetDeviceCaps.  See also[PyCDC::GetDeviceCaps](#PyCDC.md#PyCDCGetDeviceCaps)&nbsp;

    [GetFileTitle](#win32ui.md#win32uiGetFileTitle)

    Given a file name, return its title&nbsp;

    [GetFocus](#win32ui.md#win32uiGetFocus)

    Retrieves the window with the focus.&nbsp;

    [GetForegroundWindow](#win32ui.md#win32uiGetForegroundWindow)

    Retrieves the foreground window.&nbsp;

    [GetHalftoneBrush](#win32ui.md#win32uiGetHalftoneBrush)

    Returns a halftone brush.&nbsp;

    [GetInitialStateRequest](#win32ui.md#win32uiGetInitialStateRequest)

    Returns the requested state that the application start in.  This is the same as the parameter available to[PyCWnd::ShowWindow](#PyCWnd.md#PyCWndShowWindow)&nbsp;

    [GetMainFrame](#win32ui.md#win32uiGetMainFrame)

    Returns a window object for the main application frame.&nbsp;

    [GetName](#win32ui.md#win32uiGetName)

    Returns the name of the current application.&nbsp;

    [GetProfileFileName](#win32ui.md#win32uiGetProfileFileName)

    Returns the name of the INI file used by the application.&nbsp;

    [GetProfileVal](#win32ui.md#win32uiGetProfileVal)

    Returns a value from the applications INI file.&nbsp;

    [GetRecentFileList](#win32ui.md#win32uiGetRecentFileList)

    Returns the recent file list.&nbsp;

    [GetResource](#win32ui.md#win32uiGetResource)

    Gets a resource.&nbsp;

    [GetThread](#win32ui.md#win32uiGetThread)

    Retrieves the current thread object.&nbsp;

    [GetType](#win32ui.md#win32uiGetType)

    Retrieves a Python Type object given its name&nbsp;

    [InitRichEdit](#win32ui.md#win32uiInitRichEdit)

    Initializes the rich edit framework.&nbsp;

    [InstallCallbackCaller](#win32ui.md#win32uiInstallCallbackCaller)

    Installs a callback caller.&nbsp;

    [IsDebug](#win32ui.md#win32uiIsDebug)

    Returns a flag indicating if the current win32ui build is a DEBUG build.&nbsp;

    [IsWin32s](#win32ui.md#win32uiIsWin32s)

    Determines if the application is running under Win32s.&nbsp;

    [IsObject](#win32ui.md#win32uiIsObject)

    Determines if the passed object is a win32ui object.&nbsp;

    [LoadDialogResource](#win32ui.md#win32uiLoadDialogResource)

    Loads a dialog resource, and returns a list detailing the objects.&nbsp;

    [LoadLibrary](#win32ui.md#win32uiLoadLibrary)

    Creates a[PyDLL](#README.md#PyDLL)object.&nbsp;

    [LoadMenu](#win32ui.md#win32uiLoadMenu)

    Loads a menu.&nbsp;

    [LoadStdProfileSettings](#win32ui.md#win32uiLoadStdProfileSettings)

    Loads standard application profile settings.&nbsp;

    [LoadString](#win32ui.md#win32uiLoadString)

    Loads a string from a resource file.&nbsp;

    [MessageBox](#win32ui.md#win32uiMessageBox)

    Displays a message box.&nbsp;

    [OutputDebugString](#win32ui.md#win32uiOutputDebugString)

    Writes output to the Windows debugger.&nbsp;

    [EnableControlContainer](#win32ui.md#win32uiEnableControlContainer)

    Call this function in your application object's InitInstance function to enable support for containment of OLE controls.&nbsp;

    [PrintTraceback](#win32ui.md#win32uiPrintTraceback)

    Prints a Traceback using the default Python traceback printer.&nbsp;

    [PumpWaitingMessages](#win32ui.md#win32uiPumpWaitingMessages)

    Pumps all waiting messages to the application.&nbsp;

    [RegisterWndClass](#win32ui.md#win32uiRegisterWndClass)

    Registers a window class&nbsp;

    [RemoveRecentFile](#win32ui.md#win32uiRemoveRecentFile)

    Removes the recent file at list index.&nbsp;

    [SetAppHelpPath](#win32ui.md#win32uiSetAppHelpPath)

    Sets the application help file path, i.e. the pApp-&gtm_pszHelpFilePath member variable.&nbsp;

    [SetAppName](#win32ui.md#win32uiSetAppName)

    Sets the application name.&nbsp;

    [SetCurrentInstanceHandle](#win32ui.md#win32uiSetCurrentInstanceHandle)

    Sets the MFC variable afxCurrentInstanceHandle.&nbsp;

    [SetCurrentResourceHandle](#win32ui.md#win32uiSetCurrentResourceHandle)

    Sets the MFC variable afxCurrentResourceHandle.&nbsp;

    [SetDialogBkColor](#win32ui.md#win32uiSetDialogBkColor)

    Sets the default background and text color for dialog boxes and message boxes within the application.&nbsp;

    [SetProfileFileName](#win32ui.md#win32uiSetProfileFileName)

    Sets the INI file name used by the application.&nbsp;

    [SetRegistryKey](#win32ui.md#win32uiSetRegistryKey)

    Causes application settings to be stored in the registry instead of INI files.&nbsp;

    [SetResource](#win32ui.md#win32uiSetResource)

    Specifies the default DLL object for application resources.&nbsp;

    [SetStatusText](#win32ui.md#win32uiSetStatusText)

    Sets the text in the status bar.&nbsp;

    [StartDebuggerPump](#win32ui.md#win32uiStartDebuggerPump)

    Starts the debugger message pump.&nbsp;

    [StopDebuggerPump](#win32ui.md#win32uiStopDebuggerPump)

    Stops the debugger message pump.&nbsp;

    [TranslateMessage](#win32ui.md#win32uiTranslateMessage)

    Calls ::TranslateMessage.&nbsp;

    [TranslateVirtualKey](#win32ui.md#win32uiTranslateVirtualKey)

    Translates a virtual key.&nbsp;

    [WinHelp](#win32ui.md#win32uiWinHelp)

    Invokes the Window Help engine.&nbsp;

    [WriteProfileVal](#win32ui.md#win32uiWriteProfileVal)

    Writes a value to the INI file.&nbsp;
------

##[win32uiole](md/win32uiole.md)

## Module win32uiole

A module, encapsulating the Microsoft Foundation Classes OLE functionality.

#### Methods


    [AfxOleInit](#win32uiole.md#win32uioleAfxOleInit)

    &nbsp;

    [CreateInsertDialog](#win32uiole.md#win32uioleCreateInsertDialog)

    Creates a InsertObject dialog.&nbsp;

    [CreateOleClientItem](#win32uiole.md#win32uioleCreateOleClientItem)

    Creates a[PyCOleClientItem](#README.md#PyCOleClientItem)object.&nbsp;

    [CreateOleDocument](#win32uiole.md#win32uioleCreateOleDocument)

    Creates a[PyCOleDocument](#README.md#PyCOleDocument)object.&nbsp;

    [DaoGetEngine](#win32uiole.md#win32uioleDaoGetEngine)

    &nbsp;

    [GetIDispatchForWindow](#win32uiole.md#win32uioleGetIDispatchForWindow)

    Gets an OCX IDispatch pointer, if the window has one!&nbsp;

    [OleGetUserCtrl](#win32uiole.md#win32uioleOleGetUserCtrl)

    Retrieves the current user-control flag.&nbsp;

    [OleSetUserCtrl](#win32uiole.md#win32uioleOleSetUserCtrl)

    Sets the current user-control flag.&nbsp;

    [SetMessagePendingDelay](#win32uiole.md#win32uioleSetMessagePendingDelay)

    &nbsp;

    [EnableNotRespondingDialog](#win32uiole.md#win32uioleEnableNotRespondingDialog)

    &nbsp;

    [EnableNotRespondingDialog](#win32uiole.md#win32uioleEnableNotRespondingDialog)

    &nbsp;
------

##[win32service](md/win32service.md)

## Module win32service

An interface to the Windows NT Service API

#### Methods


    [GetThreadDesktop](#win32service.md#win32serviceGetThreadDesktop)

    Retrieves a handle to the desktop for a thread&nbsp;

    [EnumWindowStations](#win32service.md#win32serviceEnumWindowStations)

    Lists names of window stations&nbsp;

    [GetUserObjectInformation](#win32service.md#win32serviceGetUserObjectInformation)

    Returns specified type of info about a window station or desktop&nbsp;

    [SetUserObjectInformation](#win32service.md#win32serviceSetUserObjectInformation)

    Set specified type of info for a window station or desktop object&nbsp;

    [OpenWindowStation](#win32service.md#win32serviceOpenWindowStation)

    Returns a handle to the specified window station&nbsp;

    [OpenDesktop](#win32service.md#win32serviceOpenDesktop)

    Opens a handle to a desktop&nbsp;

    [CreateDesktop](#win32service.md#win32serviceCreateDesktop)

    Creates a new desktop in calling process's current window station&nbsp;

    [OpenInputDesktop](#win32service.md#win32serviceOpenInputDesktop)

    Returns a handle to desktop for logged-in user&nbsp;

    [GetProcessWindowStation](#win32service.md#win32serviceGetProcessWindowStation)

    Returns a handle to calling process's current window station&nbsp;

    [CreateWindowStation](#win32service.md#win32serviceCreateWindowStation)

    Creates a new window station&nbsp;

    [EnumServicesStatus](#win32service.md#win32serviceEnumServicesStatus)

    Returns a tuple of status info for each service that meets specified criteria&nbsp;

    [EnumServicesStatusEx](#win32service.md#win32serviceEnumServicesStatusEx)

    Lists the status of services that meet the specified criteria&nbsp;

    [EnumDependentServices](#win32service.md#win32serviceEnumDependentServices)

    Lists services that depend on a service&nbsp;

    [QueryServiceConfig](#win32service.md#win32serviceQueryServiceConfig)

    Retrieves configuration parameters for a service&nbsp;

    [StartService](#win32service.md#win32serviceStartService)

    Starts the specified service&nbsp;

    [OpenService](#win32service.md#win32serviceOpenService)

    Returns a handle to the specified service.&nbsp;

    [OpenSCManager](#win32service.md#win32serviceOpenSCManager)

    Returns a handle to the service control manager&nbsp;

    [CloseServiceHandle](#win32service.md#win32serviceCloseServiceHandle)

    Closes a service or SCM handle&nbsp;

    [QueryServiceStatus](#win32service.md#win32serviceQueryServiceStatus)

    Queries a service status&nbsp;

    [QueryServiceStatusEx](#win32service.md#win32serviceQueryServiceStatusEx)

    Queries a service status&nbsp;

    [SetServiceObjectSecurity](#win32service.md#win32serviceSetServiceObjectSecurity)

    Set the security descriptor for a service&nbsp;

    [QueryServiceObjectSecurity](#win32service.md#win32serviceQueryServiceObjectSecurity)

    Retrieves information from the security descriptor for a service&nbsp;

    [GetServiceKeyName](#win32service.md#win32serviceGetServiceKeyName)

    Translates a service display name into its registry key name&nbsp;

    [GetServiceDisplayName](#win32service.md#win32serviceGetServiceDisplayName)

    Translates an internal service name into its display name&nbsp;

    [SetServiceStatus](#win32service.md#win32serviceSetServiceStatus)

    Sets a service status&nbsp;

    [ControlService](#win32service.md#win32serviceControlService)

    Sends a control message to a service.&nbsp;

    [DeleteService](#win32service.md#win32serviceDeleteService)

    Deletes the specified service&nbsp;

    [CreateService](#win32service.md#win32serviceCreateService)

    Creates a new service.&nbsp;

    [ChangeServiceConfig](#win32service.md#win32serviceChangeServiceConfig)

    Changes the configuration of an existing service.&nbsp;

    [LockServiceDatabase](#win32service.md#win32serviceLockServiceDatabase)

    Locks the service database.&nbsp;

    [UnlockServiceDatabase](#win32service.md#win32serviceUnlockServiceDatabase)

    Unlocks the service database.&nbsp;

    [QueryServiceLockStatus](#win32service.md#win32serviceQueryServiceLockStatus)

    Retrieves the lock status of the specified service control manager database.&nbsp;

    [ChangeServiceConfig2](#win32service.md#win32serviceChangeServiceConfig2)

    Modifies advanced service parameters&nbsp;

    [QueryServiceConfig2](#win32service.md#win32serviceQueryServiceConfig2)

    Retrieves advanced service configuration options&nbsp;
------

##[win32timezone.RangeMap](md/win32timezone.RangeMap.md)

## win32timezone.RangeMap Object

A dictionary-like object that uses the keys as bounds for a range. 

Inclusion of the value for that range is determined by the 

key_match_comparator, which defaults to less-than-or-equal. 

A value is returned for a key if it is the first key that matches in 

the sorted list of keys.

#### Comments
One may supply keyword parameters to be passed to the sort function used 

to sort keys (i.e. cmp [python 2 only], keys, reverse) as sort_params.
Let's create a map that maps 1-3 -&gt 'a', 4-6 -&gt 'b'
&gt&gt&gt r = RangeMap({3: 'a', 6: 'b'})  # boy, that was easy

&gt&gt&gt r[1], r[2], r[3], r[4], r[5], r[6]

('a', 'a', 'a', 'b', 'b', 'b')
Even float values should work so long as the comparison operator 

supports it.
&gt&gt&gt r[4.5]

'b'
But you'll notice that the way rangemap is defined, it must be open-ended on one side.
&gt&gt&gt r[0]

'a'

&gt&gt&gt r[-1]

'a'
One can close the open-end of the RangeMap by using undefined_value
&gt&gt&gt r = RangeMap({0: RangeMap.undefined_value, 3: 'a', 6: 'b'})

&gt&gt&gt r[0]

Traceback (most recent call last):

...

KeyError: 0
One can get the first or last elements in the range by using RangeMap.Item
&gt&gt&gt last_item = RangeMap.Item(-1)

&gt&gt&gt r[last_item]

'b'
.last_item is a shortcut for Item(-1)
&gt&gt&gt r[RangeMap.last_item]

'b'
Sometimes it's useful to find the bounds for a RangeMap
&gt&gt&gt r.bounds()

(0, 6)
RangeMap supports .get(key, default)
&gt&gt&gt r.get(0, 'not found')

'not found'
&gt&gt&gt r.get(7, 'not found')

'not found'

#### Methods


    [get](#win32timezone.RangeMap.md#win32timezone.RangeMapget)

    Return the value for key if key is in the dictionary, else default.&nbsp;
------

##[win32profile](md/win32profile.md)

## Module win32profile

Wraps functions for dealing with user profiles

#### Methods


    [CreateEnvironmentBlock](#win32profile.md#win32profileCreateEnvironmentBlock)

    Retrieves environment variables for a user&nbsp;

    [DeleteProfile](#win32profile.md#win32profileDeleteProfile)

    Removes a user's profile&nbsp;

    [ExpandEnvironmentStringsForUser](#win32profile.md#win32profileExpandEnvironmentStringsForUser)

    Replaces environment variables in a string with per-user values&nbsp;

    [GetAllUsersProfileDirectory](#win32profile.md#win32profileGetAllUsersProfileDirectory)

    Retrieve All Users profile directory&nbsp;

    [GetDefaultUserProfileDirectory](#win32profile.md#win32profileGetDefaultUserProfileDirectory)

    Retrieve profile path for Default user&nbsp;

    [GetEnvironmentStrings](#win32profile.md#win32profileGetEnvironmentStrings)

    Retrieves environment variables for current process&nbsp;

    [GetProfilesDirectory](#win32profile.md#win32profileGetProfilesDirectory)

    Retrieves directory where user profiles are stored&nbsp;

    [GetProfileType](#win32profile.md#win32profileGetProfileType)

    Returns type of current user's profile&nbsp;

    [GetUserProfileDirectory](#win32profile.md#win32profileGetUserProfileDirectory)

    Returns profile directory for a logon token&nbsp;

    [LoadUserProfile](#win32profile.md#win32profileLoadUserProfile)

    Load user settings for a login token&nbsp;

    [UnloadUserProfile](#win32profile.md#win32profileUnloadUserProfile)

    Unload profile loaded by LoadUserProfile&nbsp;
------

##[win32lz](md/win32lz.md)

## Module win32lz

A module encapsulating the Windows LZ compression routines.

#### Methods


    [GetExpandedName](#win32lz.md#win32lzGetExpandedName)

    Retrieves the original name of an expanded file,&nbsp;

    [Close](#win32lz.md#win32lzClose)

    Closes a handle to an LZ file.&nbsp;

    [Copy](#win32lz.md#win32lzCopy)

    Copies a source file to a destination file.&nbsp;

    [Init](#win32lz.md#win32lzInit)

    Allocates memory for the internal data structures required to decompress files, and then creates and initializes them.&nbsp;

    [OpenFile](#win32lz.md#win32lzOpenFile)

    Creates, opens, reopens, or deletes the specified file.&nbsp;
------

##[win32crypt](md/win32crypt.md)

## Module win32crypt

An interface to the win32 Cryptography API

#### Methods


    [CryptProtectData](#win32crypt.md#win32cryptCryptProtectData)

    Encrypts data using a session key derived from current user's logon credentials&nbsp;

    [CryptUnprotectData](#win32crypt.md#win32cryptCryptUnprotectData)

    Decrypts data that was encrypted using[win32crypt::CryptProtectData](#win32crypt.md#win32cryptCryptProtectData)&nbsp;

    [CryptEnumProviders](#win32crypt.md#win32cryptCryptEnumProviders)

    Lists available cryptographic providers&nbsp;

    [CryptEnumProviderTypes](#win32crypt.md#win32cryptCryptEnumProviderTypes)

    Lists available local cryptographic provider types&nbsp;

    [CryptGetDefaultProvider](#win32crypt.md#win32cryptCryptGetDefaultProvider)

    Returns default provider for local machine or current user&nbsp;

    [CryptSetProviderEx](#win32crypt.md#win32cryptCryptSetProviderEx)

    Sets default provider (for machine or user) for specified type&nbsp;

    [CryptAcquireContext](#win32crypt.md#win32cryptCryptAcquireContext)

    Retrieve handle to a cryptographic service provider&nbsp;

    [CryptFindLocalizedName](#win32crypt.md#win32cryptCryptFindLocalizedName)

    Return localized name for predefined system stores (Root, My, .Default, .LocalMachine)&nbsp;

    [CertEnumSystemStore](#win32crypt.md#win32cryptCertEnumSystemStore)

    Lists system stores&nbsp;

    [CertEnumSystemStoreLocation](#win32crypt.md#win32cryptCertEnumSystemStoreLocation)

    Lists system store locations&nbsp;

    [CertEnumPhysicalStore](#win32crypt.md#win32cryptCertEnumPhysicalStore)

    Lists physical stores on computer&nbsp;

    [CertRegisterSystemStore](#win32crypt.md#win32cryptCertRegisterSystemStore)

    Creates a new system certificate store&nbsp;

    [CertUnregisterSystemStore](#win32crypt.md#win32cryptCertUnregisterSystemStore)

    Unregister specified store, optionally deleting it&nbsp;

    [CertOpenStore](#win32crypt.md#win32cryptCertOpenStore)

    Opens a certificate store&nbsp;

    [CertOpenSystemStore](#win32crypt.md#win32cryptCertOpenSystemStore)

    Opens most commonly used Certificate Stores&nbsp;

    [CryptFindOIDInfo](#win32crypt.md#win32cryptCryptFindOIDInfo)

    Retreives information about an object identifier or alorithm identifier&nbsp;

    [CertAlgIdToOID](#win32crypt.md#win32cryptCertAlgIdToOID)

    Converts an integer ALG_ID to it's szOID_ string representation&nbsp;

    [CertOIDToAlgId](#win32crypt.md#win32cryptCertOIDToAlgId)

    Converts a string object identfier to a numeric algorith identifier&nbsp;

    [CryptGetKeyIdentifierProperty](#win32crypt.md#win32cryptCryptGetKeyIdentifierProperty)

    Retrieves a property from a certificate by it's key indentifier&nbsp;

    [CryptEnumKeyIdentifierProperties](#win32crypt.md#win32cryptCryptEnumKeyIdentifierProperties)

    Lists private keys for user or machine&nbsp;

    [CryptEnumOIDInfo](#win32crypt.md#win32cryptCryptEnumOIDInfo)

    Lists registered object identfiers&nbsp;

    [CertAddSerializedElementToStore](#win32crypt.md#win32cryptCertAddSerializedElementToStore)

    Creates a new Certificate, CRL, or CTL context from serialized data&nbsp;

    [CryptQueryObject](#win32crypt.md#win32cryptCryptQueryObject)

    Determines the type of serialized or encoded data&nbsp;

    [CryptDecodeMessage](#win32crypt.md#win32cryptCryptDecodeMessage)

    Decrypts an encoded message and verifies a signature&nbsp;

    [CryptEncryptMessage](#win32crypt.md#win32cryptCryptEncryptMessage)

    Encrypts and encodes a message&nbsp;

    [CryptDecryptMessage](#win32crypt.md#win32cryptCryptDecryptMessage)

    Decrypts an encrypted and encoded message&nbsp;

    [CryptSignAndEncryptMessage](#win32crypt.md#win32cryptCryptSignAndEncryptMessage)

    Decrypts an encrypted and encoded message&nbsp;

    [CryptVerifyMessageSignature](#win32crypt.md#win32cryptCryptVerifyMessageSignature)

    Verifies a message signature&nbsp;

    [CryptGetMessageCertificates](#win32crypt.md#win32cryptCryptGetMessageCertificates)

    Extracts certificates encoded in a message&nbsp;

    [CryptGetMessageSignerCount](#win32crypt.md#win32cryptCryptGetMessageSignerCount)

    Finds the number of signers of an encoded message&nbsp;

    [CryptSignMessage](#win32crypt.md#win32cryptCryptSignMessage)

    Signs and encodes a message&nbsp;

    [CryptVerifyDetachedMessageSignature](#win32crypt.md#win32cryptCryptVerifyDetachedMessageSignature)

    Verifies a signature that is encoded separately from the data&nbsp;

    [CryptDecryptAndVerifyMessageSignature](#win32crypt.md#win32cryptCryptDecryptAndVerifyMessageSignature)

    Decrypts and decodes a signed message, and verifies its signatures&nbsp;

    [CryptEncodeObjectEx](#win32crypt.md#win32cryptCryptEncodeObjectEx)

    Serializes and ASN encodes cryptographic structures&nbsp;

    [CryptDecodeObjectEx](#win32crypt.md#win32cryptCryptDecodeObjectEx)

    Decodes ASN encodes data&nbsp;

    [CertNameToStr](#win32crypt.md#win32cryptCertNameToStr)

    Converts an encoded CERT_NAME_INFO into a formatted string&nbsp;

    [CryptFormatObject](#win32crypt.md#win32cryptCryptFormatObject)

    Formats an encoded buffer into a readable string&nbsp;

    [PFXImportCertStore](#win32crypt.md#win32cryptPFXImportCertStore)

    Creates a certificate store from PKCS#12 data (*.PFX files)&nbsp;

    [PFXVerifyPassword](#win32crypt.md#win32cryptPFXVerifyPassword)

    Checks if a PFX blob can be decrypted with given password&nbsp;

    [PFXIsPFXBlob](#win32crypt.md#win32cryptPFXIsPFXBlob)

    Checks if data buffer contains a PFX blob&nbsp;

    [CryptBinaryToString](#win32crypt.md#win32cryptCryptBinaryToString)

    Formats a binary buffer into the specified type of string&nbsp;

    [CryptStringToBinary](#win32crypt.md#win32cryptCryptStringToBinary)

    Converts a formatted string back into raw bytes&nbsp;
------

##[win32](md/win32.md)

------

##[win32print](md/win32print.md)

## Module win32print

A module encapsulating the Windows printing API.

#### Methods


    [OpenPrinter](#win32print.md#win32printOpenPrinter)

    Retrieves a handle to a printer.&nbsp;

    [GetPrinter](#win32print.md#win32printGetPrinter)

    Retrieves information about a printer&nbsp;

    [SetPrinter](#win32print.md#win32printSetPrinter)

    Changes printer configuration and status&nbsp;

    [ClosePrinter](#win32print.md#win32printClosePrinter)

    Closes a handle to a printer.&nbsp;

    [AddPrinterConnection](#win32print.md#win32printAddPrinterConnection)

    Connects to a network printer.&nbsp;

    [DeletePrinterConnection](#win32print.md#win32printDeletePrinterConnection)

    Disconnects from a network printer.&nbsp;

    [EnumPrinters](#win32print.md#win32printEnumPrinters)

    Enumerates printers, print servers, domains and print providers.&nbsp;

    [GetDefaultPrinter](#win32print.md#win32printGetDefaultPrinter)

    Returns the default printer.&nbsp;

    [GetDefaultPrinterW](#win32print.md#win32printGetDefaultPrinterW)

    Returns the default printer.&nbsp;

    [SetDefaultPrinter](#win32print.md#win32printSetDefaultPrinter)

    Sets the default printer.&nbsp;

    [SetDefaultPrinterW](#win32print.md#win32printSetDefaultPrinterW)

    Sets the default printer.&nbsp;

    [StartDocPrinter](#win32print.md#win32printStartDocPrinter)

    Notifies the print spooler that a document is to be spooled for printing. Returns the Jobid of the started job.&nbsp;

    [EndDocPrinter](#win32print.md#win32printEndDocPrinter)

    The EndDocPrinter function ends a print job for the specified printer.&nbsp;

    [AbortPrinter](#win32print.md#win32printAbortPrinter)

    Deletes spool file for printer&nbsp;

    [StartPagePrinter](#win32print.md#win32printStartPagePrinter)

    Notifies the print spooler that a page is to be printed on specified printer&nbsp;

    [EndPagePrinter](#win32print.md#win32printEndPagePrinter)

    Ends a page in a print job&nbsp;

    [StartDoc](#win32print.md#win32printStartDoc)

    Starts spooling a print job on a printer device context&nbsp;

    [EndDoc](#win32print.md#win32printEndDoc)

    Stops spooling a print job on a printer device context&nbsp;

    [AbortDoc](#win32print.md#win32printAbortDoc)

    Cancels print job on a printer device context&nbsp;

    [StartPage](#win32print.md#win32printStartPage)

    Starts a page on a printer device context&nbsp;

    [EndPage](#win32print.md#win32printEndPage)

    Ends a page on a printer device context&nbsp;

    [WritePrinter](#win32print.md#win32printWritePrinter)

    Copies the specified bytes to the specified printer. StartDocPrinter and EndDocPrinter should be called before and after. Returns number of bytes written to printer.&nbsp;

    [EnumJobs](#win32print.md#win32printEnumJobs)

    Enumerates print jobs on specified printer.&nbsp;

    [GetJob](#win32print.md#win32printGetJob)

    Returns dictionary of information about a specified print job.&nbsp;

    [SetJob](#win32print.md#win32printSetJob)

    Pause, cancel, resume, set priority levels on a print job.&nbsp;

    [DocumentProperties](#win32print.md#win32printDocumentProperties)

    Changes printer configuration&nbsp;

    [EnumPrintProcessors](#win32print.md#win32printEnumPrintProcessors)

    List printer providers for specified server and environment&nbsp;

    [EnumPrintProcessorDatatypes](#win32print.md#win32printEnumPrintProcessorDatatypes)

    Lists data types that specified print provider supports&nbsp;

    [EnumPrinterDrivers](#win32print.md#win32printEnumPrinterDrivers)

    Lists installed printer drivers&nbsp;

    [EnumForms](#win32print.md#win32printEnumForms)

    Lists forms for a printer&nbsp;

    [AddForm](#win32print.md#win32printAddForm)

    Adds a form for a printer&nbsp;

    [DeleteForm](#win32print.md#win32printDeleteForm)

    Deletes a form defined for a printer&nbsp;

    [GetForm](#win32print.md#win32printGetForm)

    Retrieves information about a defined form&nbsp;

    [SetForm](#win32print.md#win32printSetForm)

    Change information for a form&nbsp;

    [AddJob](#win32print.md#win32printAddJob)

    Adds a job to be spooled to a printer queue&nbsp;

    [ScheduleJob](#win32print.md#win32printScheduleJob)

    Schedules a spooled job to be printed&nbsp;

    [DeviceCapabilities](#win32print.md#win32printDeviceCapabilities)

    Queries a printer for its capabilities&nbsp;

    [GetDeviceCaps](#win32print.md#win32printGetDeviceCaps)

    Retrieves device-specific parameters and settings&nbsp;

    [EnumMonitors](#win32print.md#win32printEnumMonitors)

    Lists installed printer port monitors&nbsp;

    [EnumPorts](#win32print.md#win32printEnumPorts)

    Lists printer ports on a server&nbsp;

    [GetPrintProcessorDirectory](#win32print.md#win32printGetPrintProcessorDirectory)

    Returns the directory where print processor files reside&nbsp;

    [GetPrinterDriverDirectory](#win32print.md#win32printGetPrinterDriverDirectory)

    Returns the directory where printer drivers are installed&nbsp;

    [AddPrinter](#win32print.md#win32printAddPrinter)

    Adds a new printer on a server&nbsp;

    [DeletePrinter](#win32print.md#win32printDeletePrinter)

    Deletes an existing printer&nbsp;

    [DeletePrinterDriver](#win32print.md#win32printDeletePrinterDriver)

    Deletes the specified driver from a server&nbsp;

    [DeletePrinterDriverEx](#win32print.md#win32printDeletePrinterDriverEx)

    Deletes a printer driver and associated files&nbsp;

    [FlushPrinter](#win32print.md#win32printFlushPrinter)

    Clears printer from error state if WritePrinter fails&nbsp;
------

##[win32ts](md/win32ts.md)

## Module win32ts

Interface to the Terminal Services Api 

All functions in this module accept keyword arguments

#### Methods


    [WTSOpenServer](#win32ts.md#win32tsWTSOpenServer)

    Opens a handle to a terminal server&nbsp;

    [WTSCloseServer](#win32ts.md#win32tsWTSCloseServer)

    Closes a terminal server handle&nbsp;

    [WTSQueryUserConfig](#win32ts.md#win32tsWTSQueryUserConfig)

    Returns user configuration&nbsp;

    [WTSSetUserConfig](#win32ts.md#win32tsWTSSetUserConfig)

    Changes user configuration&nbsp;

    [WTSEnumerateServers](#win32ts.md#win32tsWTSEnumerateServers)

    Lists terminal servers in a domain&nbsp;

    [WTSEnumerateSessions](#win32ts.md#win32tsWTSEnumerateSessions)

    Lists sessions on a server&nbsp;

    [WTSLogoffSession](#win32ts.md#win32tsWTSLogoffSession)

    Logs off a user logged in through Terminal Services&nbsp;

    [WTSDisconnectSession](#win32ts.md#win32tsWTSDisconnectSession)

    Disconnects a session without logging it off&nbsp;

    [WTSQuerySessionInformation](#win32ts.md#win32tsWTSQuerySessionInformation)

    Retrieve information about a session&nbsp;

    [WTSEnumerateProcesses](#win32ts.md#win32tsWTSEnumerateProcesses)

    Lists processes on a terminal server&nbsp;

    [WTSQueryUserToken](#win32ts.md#win32tsWTSQueryUserToken)

    Retrieves the access token for a session&nbsp;

    [WTSShutdownSystem](#win32ts.md#win32tsWTSShutdownSystem)

    Issues a shutdown request to a terminal server&nbsp;

    [WTSTerminateProcess](#win32ts.md#win32tsWTSTerminateProcess)

    Kills a process on a terminal server&nbsp;

    [ProcessIdToSessionId](#win32ts.md#win32tsProcessIdToSessionId)

    Finds the session under which a process is running&nbsp;

    [WTSGetActiveConsoleSessionId](#win32ts.md#win32tsWTSGetActiveConsoleSessionId)

    Returns the id of the console session&nbsp;

    [WTSRegisterSessionNotification](#win32ts.md#win32tsWTSRegisterSessionNotification)

    Registers a window to receive terminal service notifications&nbsp;

    [WTSUnRegisterSessionNotification](#win32ts.md#win32tsWTSUnRegisterSessionNotification)

    Disables terminal service window messages&nbsp;

    [WTSWaitSystemEvent](#win32ts.md#win32tsWTSWaitSystemEvent)

    Waits for an event to occur&nbsp;

    [WTSSendMessage](#win32ts.md#win32tsWTSSendMessage)

    Sends a popup message to a terminal services session&nbsp;
------

##[win32gui](md/win32gui.md)

## Module win32gui

A module which provides an interface to the native win32 

GUI API.
Note that a module[winxpgui](#README.md#winxpgui)also exists, 

which has the same methods as win32gui, but has an XP 

manifest and is setup for side-by-side sharing support for 

certain system DLLs, notably commctl32.

#### Methods


    [EnumFontFamilies](#win32gui.md#win32guiEnumFontFamilies)

    Enumerates the available font families.&nbsp;

    [set_logger](#win32gui.md#win32guiset_logger)

    Sets a logger object for exceptions and error information&nbsp;

    [LOGFONT](#win32gui.md#win32guiLOGFONT)

    Creates a LOGFONT object.&nbsp;

    [CreateFontIndirect](#win32gui.md#win32guiCreateFontIndirect)

    function creates a logical font that has the specified characteristics. 

The font can subsequently be selected as the current font for any device context.&nbsp;

    [GetObject](#win32gui.md#win32guiGetObject)

    Returns a struct containing the parameters used to create a GDI object&nbsp;

    [GetObjectType](#win32gui.md#win32guiGetObjectType)

    Returns the type (OBJ_* constant) of a GDI handle&nbsp;

    [PyGetMemory](#win32gui.md#win32guiPyGetMemory)

    Returns a buffer object from and address and length&nbsp;

    [PyGetString](#win32gui.md#win32guiPyGetString)

    Returns a string from an address.&nbsp;

    [PySetString](#win32gui.md#win32guiPySetString)

    Copies a string to an address (null terminated). 

You almost certainly should use[win32gui::PySetMemory](#win32gui.md#win32guiPySetMemory)instead.&nbsp;

    [PySetMemory](#win32gui.md#win32guiPySetMemory)

    Copies bytes to an address.&nbsp;

    [PyGetArraySignedLong](#win32gui.md#win32guiPyGetArraySignedLong)

    Returns a signed long from an array object at specified index&nbsp;

    [PyGetBufferAddressAndLen](#win32gui.md#win32guiPyGetBufferAddressAndLen)

    Returns a buffer object address and len&nbsp;

    [FlashWindow](#win32gui.md#win32guiFlashWindow)

    The FlashWindow function flashes the specified window one time. It does not change the active state of the window.&nbsp;

    [FlashWindowEx](#win32gui.md#win32guiFlashWindowEx)

    The FlashWindowEx function flashes the specified window a specified number of times.&nbsp;

    [GetWindowLong](#win32gui.md#win32guiGetWindowLong)

    &nbsp;

    [GetClassLong](#win32gui.md#win32guiGetClassLong)

    &nbsp;

    [SetWindowLong](#win32gui.md#win32guiSetWindowLong)

    Places a long value at the specified offset into the extra window memory of the given window.&nbsp;

    [CallWindowProc](#win32gui.md#win32guiCallWindowProc)

    &nbsp;

    [SendMessage](#win32gui.md#win32guiSendMessage)

    Sends a message to the window.&nbsp;

    [SendMessageTimeout](#win32gui.md#win32guiSendMessageTimeout)

    Sends a message to the window.&nbsp;

    [PostMessage](#win32gui.md#win32guiPostMessage)

    &nbsp;

    [PostThreadMessage](#win32gui.md#win32guiPostThreadMessage)

    &nbsp;

    [ReplyMessage](#win32gui.md#win32guiReplyMessage)

    Used to reply to a message sent through the SendMessage function without returning control to the function that called SendMessage.&nbsp;

    [RegisterWindowMessage](#win32gui.md#win32guiRegisterWindowMessage)

    Defines a new window message that is guaranteed to be unique throughout the system. The message value can be used when sending or posting messages.&nbsp;

    [DefWindowProc](#win32gui.md#win32guiDefWindowProc)

    &nbsp;

    [EnumWindows](#win32gui.md#win32guiEnumWindows)

    Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.&nbsp;

    [EnumThreadWindows](#win32gui.md#win32guiEnumThreadWindows)

    Enumerates all top-level windows associated with a thread on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE&nbsp;

    [EnumChildWindows](#win32gui.md#win32guiEnumChildWindows)

    Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE.&nbsp;

    [DialogBox](#win32gui.md#win32guiDialogBox)

    Creates a modal dialog box.&nbsp;

    [DialogBoxParam](#win32gui.md#win32guiDialogBoxParam)

    See[win32gui::DialogBox](#win32gui.md#win32guiDialogBox)&nbsp;

    [DialogBoxIndirect](#win32gui.md#win32guiDialogBoxIndirect)

    Creates a modal dialog box from a template, see[win32ui::CreateDialogIndirect](#win32ui.md#win32uiCreateDialogIndirect)&nbsp;

    [DialogBoxIndirectParam](#win32gui.md#win32guiDialogBoxIndirectParam)

    See[win32gui::DialogBoxIndirect](#win32gui.md#win32guiDialogBoxIndirect)&nbsp;

    [CreateDialogIndirect](#win32gui.md#win32guiCreateDialogIndirect)

    Creates a modeless dialog box from a template, see[win32ui::CreateDialogIndirect](#win32ui.md#win32uiCreateDialogIndirect)&nbsp;

    [DialogBoxIndirectParam](#win32gui.md#win32guiDialogBoxIndirectParam)

    See[win32gui::CreateDialogIndirect](#win32gui.md#win32guiCreateDialogIndirect)&nbsp;

    [EndDialog](#win32gui.md#win32guiEndDialog)

    Ends a dialog box.&nbsp;

    [GetDlgItem](#win32gui.md#win32guiGetDlgItem)

    Retrieves the handle to a control in the specified dialog box.&nbsp;

    [GetDlgItemInt](#win32gui.md#win32guiGetDlgItemInt)

    Returns the integer value of a dialog control&nbsp;

    [SetDlgItemInt](#win32gui.md#win32guiSetDlgItemInt)

    Places an integer value in a dialog control&nbsp;

    [GetDlgCtrlID](#win32gui.md#win32guiGetDlgCtrlID)

    Retrieves the identifier of the specified control.&nbsp;

    [GetDlgItemText](#win32gui.md#win32guiGetDlgItemText)

    Returns the text of a dialog control&nbsp;

    [SetDlgItemText](#win32gui.md#win32guiSetDlgItemText)

    Sets the text for a window or control&nbsp;

    [GetNextDlgTabItem](#win32gui.md#win32guiGetNextDlgTabItem)

    Retrieves a handle to the first control that has the WS_TABSTOP style that precedes (or follows) the specified control.&nbsp;

    [GetNextDlgGroupItem](#win32gui.md#win32guiGetNextDlgGroupItem)

    Retrieves a handle to the first control in a group of controls that precedes (or follows) the specified control in a dialog box.&nbsp;

    [SetWindowText](#win32gui.md#win32guiSetWindowText)

    Sets the window text.&nbsp;

    [GetWindowText](#win32gui.md#win32guiGetWindowText)

    Get the window text.&nbsp;

    [InitCommonControls](#win32gui.md#win32guiInitCommonControls)

    Initializes the common controls.&nbsp;

    [InitCommonControlsEx](#win32gui.md#win32guiInitCommonControlsEx)

    Initializes specific common controls.&nbsp;

    [LoadCursor](#win32gui.md#win32guiLoadCursor)

    Loads a cursor.&nbsp;

    [SetCursor](#win32gui.md#win32guiSetCursor)

    &nbsp;

    [GetCursor](#win32gui.md#win32guiGetCursor)

    &nbsp;

    [GetCursorInfo](#win32gui.md#win32guiGetCursorInfo)

    Retrieves information about the global cursor.&nbsp;

    [CreateAcceleratorTable](#win32gui.md#win32guiCreateAcceleratorTable)

    Creates an accelerator table&nbsp;

    [DestroyAccleratorTable](#win32gui.md#win32guiDestroyAccleratorTable)

    Destroys an accelerator table&nbsp;

    [LoadMenu](#win32gui.md#win32guiLoadMenu)

    Loads a menu&nbsp;

    [DestroyMenu](#win32gui.md#win32guiDestroyMenu)

    Destroys a previously loaded menu.&nbsp;

    [SetMenu](#win32gui.md#win32guiSetMenu)

    Sets the menu for the specified window.&nbsp;

    [GetMenu](#win32gui.md#win32guiGetMenu)

    Gets the menu for the specified window.&nbsp;

    [LoadIcon](#win32gui.md#win32guiLoadIcon)

    Loads an icon&nbsp;

    [CopyIcon](#win32gui.md#win32guiCopyIcon)

    Copies an icon&nbsp;

    [DrawIcon](#win32gui.md#win32guiDrawIcon)

    Draws an icon or cursor into the specified device context. 

To specify additional drawing options, use the[win32gui::DrawIconEx](#win32gui.md#win32guiDrawIconEx)function.&nbsp;

    [DrawIconEx](#win32gui.md#win32guiDrawIconEx)

    Draws an icon or cursor into the specified device context, 

performing the specified raster operations, and stretching or compressing the 

icon or cursor as specified.&nbsp;

    [CreateIconIndirect](#win32gui.md#win32guiCreateIconIndirect)

    Creates an icon or cursor from an ICONINFO structure.&nbsp;

    [CreateIconFromResource](#win32gui.md#win32guiCreateIconFromResource)

    Creates an icon or cursor from resource bits describing the icon.&nbsp;

    [LoadImage](#win32gui.md#win32guiLoadImage)

    Loads a bitmap, cursor or icon&nbsp;

    [DeleteObject](#win32gui.md#win32guiDeleteObject)

    Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.&nbsp;

    [BitBlt](#win32gui.md#win32guiBitBlt)

    Performs a bit-block transfer of the color data corresponding 

to a rectangle of pixels from the specified source device context into a 

destination device context.&nbsp;

    [StretchBlt](#win32gui.md#win32guiStretchBlt)

    Copies a bitmap from a source rectangle into a destination 

rectangle, stretching or compressing the bitmap to fit the dimensions of the 

destination rectangle, if necessary&nbsp;

    [PatBlt](#win32gui.md#win32guiPatBlt)

    Paints a rectangle by combining the current brush with existing colors&nbsp;

    [SetStretchBltMode](#win32gui.md#win32guiSetStretchBltMode)

    Sets the stretching mode used by[win32gui::StretchBlt](#win32gui.md#win32guiStretchBlt)&nbsp;

    [GetStretchBltMode](#win32gui.md#win32guiGetStretchBltMode)

    Returns the stretching mode used by[win32gui::StretchBlt](#win32gui.md#win32guiStretchBlt)&nbsp;

    [TransparentBlt](#win32gui.md#win32guiTransparentBlt)

    Transfers color from one DC to another, with one color treated as transparent&nbsp;

    [MaskBlt](#win32gui.md#win32guiMaskBlt)

    Combines the color data for the source and destination 

bitmaps using the specified mask and raster operation.&nbsp;

    [AlphaBlend](#win32gui.md#win32guiAlphaBlend)

    Transfers color information using alpha blending&nbsp;

    [ImageList_Add](#win32gui.md#win32guiImageList_Add)

    Adds an image or images to an image list.&nbsp;

    [ImageList_Create](#win32gui.md#win32guiImageList_Create)

    Create an image list&nbsp;

    [ImageList_Destroy](#win32gui.md#win32guiImageList_Destroy)

    Destroy an imagelist&nbsp;

    [ImageList_Draw](#win32gui.md#win32guiImageList_Draw)

    Draw an image on an HDC&nbsp;

    [ImageList_DrawEx](#win32gui.md#win32guiImageList_DrawEx)

    Draw an image on an HDC&nbsp;

    [ImageList_GetIcon](#win32gui.md#win32guiImageList_GetIcon)

    Extract an icon from an imagelist&nbsp;

    [ImageList_GetImageCount](#win32gui.md#win32guiImageList_GetImageCount)

    Return count of images in imagelist&nbsp;

    [ImageList_LoadImage](#win32gui.md#win32guiImageList_LoadImage)

    Loads bitmaps, cursors or icons, creates imagelist&nbsp;

    [ImageList_LoadBitmap](#win32gui.md#win32guiImageList_LoadBitmap)

    Creates an image list from the specified bitmap resource.&nbsp;

    [ImageList_Remove](#win32gui.md#win32guiImageList_Remove)

    Remove an image from an imagelist&nbsp;

    [ImageList_Replace](#win32gui.md#win32guiImageList_Replace)

    Replace an image in an imagelist with a bitmap image&nbsp;

    [ImageList_ReplaceIcon](#win32gui.md#win32guiImageList_ReplaceIcon)

    Replace an image in an imagelist with an icon image&nbsp;

    [ImageList_SetBkColor](#win32gui.md#win32guiImageList_SetBkColor)

    Set the background color for the imagelist&nbsp;

    [ImageList_SetOverlayImage](#win32gui.md#win32guiImageList_SetOverlayImage)

    Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image.&nbsp;

    [MessageBox](#win32gui.md#win32guiMessageBox)

    Displays a message box&nbsp;

    [MessageBeep](#win32gui.md#win32guiMessageBeep)

    Plays a waveform sound.&nbsp;

    [CreateWindow](#win32gui.md#win32guiCreateWindow)

    Creates a new window.&nbsp;

    [DestroyWindow](#win32gui.md#win32guiDestroyWindow)

    &nbsp;

    [EnableWindow](#win32gui.md#win32guiEnableWindow)

    Enables and disables keyboard and mouse input to a window&nbsp;

    [FindWindow](#win32gui.md#win32guiFindWindow)

    Retrieves a handle to the top-level window whose class name and window name match the specified strings.&nbsp;

    [FindWindowEx](#win32gui.md#win32guiFindWindowEx)

    Retrieves a handle to the top-level window whose class name and window name match the specified strings.&nbsp;

    [DragAcceptFiles](#win32gui.md#win32guiDragAcceptFiles)

    Registers whether a window accepts dropped files.&nbsp;

    [DragDetect](#win32gui.md#win32guiDragDetect)

    captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point.&nbsp;

    [SetDoubleClickTime](#win32gui.md#win32guiSetDoubleClickTime)

    &nbsp;

    [GetDoubleClickTime](#win32gui.md#win32guiGetDoubleClickTime)

    &nbsp;

    [HideCaret](#win32gui.md#win32guiHideCaret)

    Hides the caret&nbsp;

    [SetCaretPos](#win32gui.md#win32guiSetCaretPos)

    Changes the position of the caret&nbsp;

    [GetCaretPos](#win32gui.md#win32guiGetCaretPos)

    Returns the current caret position&nbsp;

    [ShowCaret](#win32gui.md#win32guiShowCaret)

    Shows the caret at its current position&nbsp;

    [ShowWindow](#win32gui.md#win32guiShowWindow)

    Shows or hides a window and changes its state&nbsp;

    [IsWindowVisible](#win32gui.md#win32guiIsWindowVisible)

    Indicates if the window has the WS_VISIBLE style.&nbsp;

    [IsWindowEnabled](#win32gui.md#win32guiIsWindowEnabled)

    Indicates if the window is enabled.&nbsp;

    [SetFocus](#win32gui.md#win32guiSetFocus)

    Sets focus to the specified window.&nbsp;

    [GetFocus](#win32gui.md#win32guiGetFocus)

    Returns the HWND of the window with focus.&nbsp;

    [UpdateWindow](#win32gui.md#win32guiUpdateWindow)

    &nbsp;

    [BringWindowToTop](#win32gui.md#win32guiBringWindowToTop)

    &nbsp;

    [SetActiveWindow](#win32gui.md#win32guiSetActiveWindow)

    &nbsp;

    [GetActiveWindow](#win32gui.md#win32guiGetActiveWindow)

    &nbsp;

    [SetForegroundWindow](#win32gui.md#win32guiSetForegroundWindow)

    &nbsp;

    [GetForegroundWindow](#win32gui.md#win32guiGetForegroundWindow)

    &nbsp;

    [GetClientRect](#win32gui.md#win32guiGetClientRect)

    Returns the rectangle of the client area of a window, in client coordinates&nbsp;

    [GetDC](#win32gui.md#win32guiGetDC)

    Gets the device context for the window.&nbsp;

    [SaveDC](#win32gui.md#win32guiSaveDC)

    Save the state of a device context&nbsp;

    [RestoreDC](#win32gui.md#win32guiRestoreDC)

    Restores a device context state&nbsp;

    [DeleteDC](#win32gui.md#win32guiDeleteDC)

    Deletes a DC&nbsp;

    [CreateCompatibleDC](#win32gui.md#win32guiCreateCompatibleDC)

    Creates a memory device context (DC) compatible with the specified device.&nbsp;

    [CreateCompatibleBitmap](#win32gui.md#win32guiCreateCompatibleBitmap)

    Creates a bitmap compatible with the device that is associated with the specified device context.&nbsp;

    [CreateBitmap](#win32gui.md#win32guiCreateBitmap)

    Creates a bitmap&nbsp;

    [SelectObject](#win32gui.md#win32guiSelectObject)

    Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.&nbsp;

    [GetCurrentObject](#win32gui.md#win32guiGetCurrentObject)

    Retrieves currently selected object from a DC&nbsp;

    [GetWindowRect](#win32gui.md#win32guiGetWindowRect)

    Returns the rectangle for a window in screen coordinates&nbsp;

    [GetStockObject](#win32gui.md#win32guiGetStockObject)

    Creates a handle to one of the standard system Gdi objects&nbsp;

    [PostQuitMessage](#win32gui.md#win32guiPostQuitMessage)

    &nbsp;

    [WaitMessage](#win32gui.md#win32guiWaitMessage)

    Waits for a message&nbsp;

    [SetWindowPos](#win32gui.md#win32guiSetWindowPos)

    Sets the position and size of a window&nbsp;

    [GetWindowPlacement](#win32gui.md#win32guiGetWindowPlacement)

    Returns placement information about the current window.&nbsp;

    [SetWindowPlacement](#win32gui.md#win32guiSetWindowPlacement)

    Sets the windows placement&nbsp;

    [RegisterClass](#win32gui.md#win32guiRegisterClass)

    Registers a window class.&nbsp;

    [UnregisterClass](#win32gui.md#win32guiUnregisterClass)

    Unregisters a window class created by[win32gui::RegisterClass](#win32gui.md#win32guiRegisterClass)&nbsp;

    [PumpMessages](#win32gui.md#win32guiPumpMessages)

    Runs a message loop until a WM_QUIT message is received.&nbsp;

    [PumpWaitingMessages](#win32gui.md#win32guiPumpWaitingMessages)

    Pumps all waiting messages for the current thread.&nbsp;

    [GetMessage](#win32gui.md#win32guiGetMessage)

    &nbsp;

    [TranslateMessage](#win32gui.md#win32guiTranslateMessage)

    &nbsp;

    [DispatchMessage](#win32gui.md#win32guiDispatchMessage)

    &nbsp;

    [TranslateAccelerator](#win32gui.md#win32guiTranslateAccelerator)

    &nbsp;

    [PeekMessage](#win32gui.md#win32guiPeekMessage)

    &nbsp;

    [Shell_NotifyIcon](#win32gui.md#win32guiShell_NotifyIcon)

    Adds, removes or modifies a taskbar icon.&nbsp;

    [GetSystemMenu](#win32gui.md#win32guiGetSystemMenu)

    &nbsp;

    [DrawMenuBar](#win32gui.md#win32guiDrawMenuBar)

    &nbsp;

    [MoveWindow](#win32gui.md#win32guiMoveWindow)

    &nbsp;

    [CloseWindow](#win32gui.md#win32guiCloseWindow)

    &nbsp;

    [DeleteMenu](#win32gui.md#win32guiDeleteMenu)

    &nbsp;

    [RemoveMenu](#win32gui.md#win32guiRemoveMenu)

    &nbsp;

    [CreateMenu](#win32gui.md#win32guiCreateMenu)

    &nbsp;

    [CreatePopupMenu](#win32gui.md#win32guiCreatePopupMenu)

    &nbsp;

    [TrackPopupMenu](#win32gui.md#win32guiTrackPopupMenu)

    Display popup shortcut menu&nbsp;

    [CommDlgExtendedError](#win32gui.md#win32guiCommDlgExtendedError)

    &nbsp;

    [ExtractIcon](#win32gui.md#win32guiExtractIcon)

    &nbsp;

    [ExtractIconEx](#win32gui.md#win32guiExtractIconEx)

    &nbsp;

    [DestroyIcon](#win32gui.md#win32guiDestroyIcon)

    &nbsp;

    [GetIconInfo](#win32gui.md#win32guiGetIconInfo)

    Returns parameters for an icon or cursor&nbsp;

    [ScreenToClient](#win32gui.md#win32guiScreenToClient)

    Convert screen coordinates to client coords&nbsp;

    [ClientToScreen](#win32gui.md#win32guiClientToScreen)

    Convert client coordinates to screen coords&nbsp;

    [PaintDesktop](#win32gui.md#win32guiPaintDesktop)

    Fills a DC with the destop background&nbsp;

    [RedrawWindow](#win32gui.md#win32guiRedrawWindow)

    Causes a portion of a window to be redrawn&nbsp;

    [GetTextExtentPoint32](#win32gui.md#win32guiGetTextExtentPoint32)

    Computes the width and height of the specified string of text.&nbsp;

    [GetTextMetrics](#win32gui.md#win32guiGetTextMetrics)

    Returns info for the font selected into a DC&nbsp;

    [GetTextCharacterExtra](#win32gui.md#win32guiGetTextCharacterExtra)

    Returns the space between characters&nbsp;

    [SetTextCharacterExtra](#win32gui.md#win32guiSetTextCharacterExtra)

    Sets the spacing between characters&nbsp;

    [GetTextAlign](#win32gui.md#win32guiGetTextAlign)

    Returns horizontal and vertical alignment for text in a device context&nbsp;

    [SetTextAlign](#win32gui.md#win32guiSetTextAlign)

    Sets horizontal and vertical alignment for text in a device context&nbsp;

    [GetTextFace](#win32gui.md#win32guiGetTextFace)

    Retrieves the name of the font currently selected in a DC&nbsp;

    [GetMapMode](#win32gui.md#win32guiGetMapMode)

    Returns the method a device context uses to translate logical units to physical units&nbsp;

    [SetMapMode](#win32gui.md#win32guiSetMapMode)

    Sets the method used for translating logical units to device units&nbsp;

    [GetGraphicsMode](#win32gui.md#win32guiGetGraphicsMode)

    Determines if advanced GDI features are enabled for a device context&nbsp;

    [SetGraphicsMode](#win32gui.md#win32guiSetGraphicsMode)

    Enables or disables advanced graphics features for a DC&nbsp;

    [GetLayout](#win32gui.md#win32guiGetLayout)

    Retrieves the layout mode of a device context&nbsp;

    [SetLayout](#win32gui.md#win32guiSetLayout)

    Sets the layout for a device context&nbsp;

    [GetPolyFillMode](#win32gui.md#win32guiGetPolyFillMode)

    Returns the polygon filling mode for a device context&nbsp;

    [SetPolyFillMode](#win32gui.md#win32guiSetPolyFillMode)

    Sets the polygon filling mode for a device context&nbsp;

    [GetWorldTransform](#win32gui.md#win32guiGetWorldTransform)

    Retrieves a device context's coordinate space translation matrix&nbsp;

    [SetWorldTransform](#win32gui.md#win32guiSetWorldTransform)

    Transforms a device context's coordinate space&nbsp;

    [ModifyWorldTransform](#win32gui.md#win32guiModifyWorldTransform)

    Combines a coordinate tranformation with device context's current transformation&nbsp;

    [CombineTransform](#win32gui.md#win32guiCombineTransform)

    Combines two coordinate space transformations&nbsp;

    [GetWindowOrgEx](#win32gui.md#win32guiGetWindowOrgEx)

    Retrievs the window origin for a DC&nbsp;

    [SetWindowOrgEx](#win32gui.md#win32guiSetWindowOrgEx)

    Changes the window origin for a DC&nbsp;

    [GetViewportOrgEx](#win32gui.md#win32guiGetViewportOrgEx)

    Retrievs the origin for a DC's viewport&nbsp;

    [SetViewportOrgEx](#win32gui.md#win32guiSetViewportOrgEx)

    Changes the viewport origin for a DC&nbsp;

    [GetWindowExtEx](#win32gui.md#win32guiGetWindowExtEx)

    Retrieves the window extents for a DC&nbsp;

    [SetWindowExtEx](#win32gui.md#win32guiSetWindowExtEx)

    Changes the window extents for a DC&nbsp;

    [GetViewportExtEx](#win32gui.md#win32guiGetViewportExtEx)

    Retrieves the viewport extents for a DC&nbsp;

    [SetViewportExtEx](#win32gui.md#win32guiSetViewportExtEx)

    Changes the viewport extents for a DC&nbsp;

    [GradientFill](#win32gui.md#win32guiGradientFill)

    Shades triangles or rectangles by interpolating between vertex colors&nbsp;

    [GetOpenFileName](#win32gui.md#win32guiGetOpenFileName)

    Creates an Open dialog box that lets the user specify the drive, directory, and the name of a file or set of files to open.&nbsp;

    [InsertMenuItem](#win32gui.md#win32guiInsertMenuItem)

    Inserts a menu item&nbsp;

    [SetMenuItemInfo](#win32gui.md#win32guiSetMenuItemInfo)

    Sets menu information&nbsp;

    [GetMenuItemInfo](#win32gui.md#win32guiGetMenuItemInfo)

    Gets menu information&nbsp;

    [GetMenuItemCount](#win32gui.md#win32guiGetMenuItemCount)

    &nbsp;

    [GetMenuItemRect](#win32gui.md#win32guiGetMenuItemRect)

    &nbsp;

    [GetMenuState](#win32gui.md#win32guiGetMenuState)

    &nbsp;

    [SetMenuDefaultItem](#win32gui.md#win32guiSetMenuDefaultItem)

    &nbsp;

    [GetMenuDefaultItem](#win32gui.md#win32guiGetMenuDefaultItem)

    &nbsp;

    [AppendMenu](#win32gui.md#win32guiAppendMenu)

    &nbsp;

    [InsertMenu](#win32gui.md#win32guiInsertMenu)

    &nbsp;

    [EnableMenuItem](#win32gui.md#win32guiEnableMenuItem)

    &nbsp;

    [CheckMenuItem](#win32gui.md#win32guiCheckMenuItem)

    &nbsp;

    [GetSubMenu](#win32gui.md#win32guiGetSubMenu)

    &nbsp;

    [ModifyMenu](#win32gui.md#win32guiModifyMenu)

    Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item.&nbsp;

    [GetMenuItemID](#win32gui.md#win32guiGetMenuItemID)

    Retrieves the menu item identifier of a menu item located at the specified position in a menu.&nbsp;

    [SetMenuItemBitmaps](#win32gui.md#win32guiSetMenuItemBitmaps)

    Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item.&nbsp;

    [CheckMenuRadioItem](#win32gui.md#win32guiCheckMenuRadioItem)

    Checks a specified menu item and makes it a 

radio item. At the same time, the function clears all other menu items in 

the associated group and clears the radio-item type flag for those items.&nbsp;

    [SetMenuInfo](#win32gui.md#win32guiSetMenuInfo)

    Sets information for a specified menu.&nbsp;

    [GetMenuInfo](#win32gui.md#win32guiGetMenuInfo)

    Gets information about a specified menu.&nbsp;

    [DrawFocusRect](#win32gui.md#win32guiDrawFocusRect)

    Draws a standard focus outline around a rectangle&nbsp;

    [DrawText](#win32gui.md#win32guiDrawText)

    Draws formatted text on a device context&nbsp;

    [LineTo](#win32gui.md#win32guiLineTo)

    Draw a line from current position to specified point&nbsp;

    [Ellipse](#win32gui.md#win32guiEllipse)

    Draws a filled ellipse on a device context&nbsp;

    [Pie](#win32gui.md#win32guiPie)

    Draws a section of an ellipse cut by 2 radials&nbsp;

    [Arc](#win32gui.md#win32guiArc)

    Draws an arc defined by an ellipse and 2 radials&nbsp;

    [ArcTo](#win32gui.md#win32guiArcTo)

    Draws an arc defined by an ellipse and 2 radials&nbsp;

    [AngleArc](#win32gui.md#win32guiAngleArc)

    Draws a line from current pos and a section of a circle's arc&nbsp;

    [Chord](#win32gui.md#win32guiChord)

    Draws a chord defined by an ellipse and 2 radials&nbsp;

    [ExtFloodFill](#win32gui.md#win32guiExtFloodFill)

    Fills an area with current brush&nbsp;

    [SetPixel](#win32gui.md#win32guiSetPixel)

    Set the color of a single pixel&nbsp;

    [GetPixel](#win32gui.md#win32guiGetPixel)

    Returns the RGB color of a single pixel&nbsp;

    [GetROP2](#win32gui.md#win32guiGetROP2)

    Returns the foreground mixing mode of a DC&nbsp;

    [SetROP2](#win32gui.md#win32guiSetROP2)

    Sets the foreground mixing mode of a DC&nbsp;

    [SetPixelV](#win32gui.md#win32guiSetPixelV)

    Sets the color of a single pixel to an approximation of specified color&nbsp;

    [MoveToEx](#win32gui.md#win32guiMoveToEx)

    Changes the current drawing position&nbsp;

    [GetCurrentPositionEx](#win32gui.md#win32guiGetCurrentPositionEx)

    Returns a device context's current drawing position&nbsp;

    [GetArcDirection](#win32gui.md#win32guiGetArcDirection)

    Returns the direction in which rectangles and arcs are drawn&nbsp;

    [SetArcDirection](#win32gui.md#win32guiSetArcDirection)

    Sets the drawing direction for arcs and rectangles&nbsp;

    [Polygon](#win32gui.md#win32guiPolygon)

    Draws a closed filled polygon defined by a sequence of points&nbsp;

    [Polyline](#win32gui.md#win32guiPolyline)

    Connects a sequence of points using currently selected pen&nbsp;

    [PolylineTo](#win32gui.md#win32guiPolylineTo)

    Draws a series of lines starting from current position.  Updates current position with end point.&nbsp;

    [PolyBezier](#win32gui.md#win32guiPolyBezier)

    Draws a series of Bezier curves starting from first point specified.&nbsp;

    [PolyBezierTo](#win32gui.md#win32guiPolyBezierTo)

    Draws a series of Bezier curves starting from current drawing position.&nbsp;

    [PlgBlt](#win32gui.md#win32guiPlgBlt)

    Copies color from a rectangle into a parallelogram&nbsp;

    [CreatePolygonRgn](#win32gui.md#win32guiCreatePolygonRgn)

    Creates a region from a sequence of vertices&nbsp;

    [ExtTextOut](#win32gui.md#win32guiExtTextOut)

    Writes text to a DC.&nbsp;

    [GetTextColor](#win32gui.md#win32guiGetTextColor)

    Returns the text color for a DC&nbsp;

    [SetTextColor](#win32gui.md#win32guiSetTextColor)

    Changes the text color for a device context&nbsp;

    [GetBkMode](#win32gui.md#win32guiGetBkMode)

    Returns the background mode for a device context&nbsp;

    [SetBkMode](#win32gui.md#win32guiSetBkMode)

    Sets the background mode for a device context&nbsp;

    [GetBkColor](#win32gui.md#win32guiGetBkColor)

    Returns the background color for a device context&nbsp;

    [SetBkColor](#win32gui.md#win32guiSetBkColor)

    Sets the background color for a device context&nbsp;

    [DrawEdge](#win32gui.md#win32guiDrawEdge)

    Draws edge(s) of a rectangle&nbsp;

    [FillRect](#win32gui.md#win32guiFillRect)

    Fills a rectangular area with specified brush&nbsp;

    [FillRgn](#win32gui.md#win32guiFillRgn)

    Fills a region with specified brush&nbsp;

    [PaintRgn](#win32gui.md#win32guiPaintRgn)

    Paints a region with current brush&nbsp;

    [FrameRgn](#win32gui.md#win32guiFrameRgn)

    Draws a frame around a region&nbsp;

    [InvertRgn](#win32gui.md#win32guiInvertRgn)

    Inverts the colors in a region&nbsp;

    [EqualRgn](#win32gui.md#win32guiEqualRgn)

    Determines if 2 regions are equal&nbsp;

    [PtInRegion](#win32gui.md#win32guiPtInRegion)

    Determines if a region contains a point&nbsp;

    [PtInRect](#win32gui.md#win32guiPtInRect)

    Determines if a rectangle contains a point&nbsp;

    [RectInRegion](#win32gui.md#win32guiRectInRegion)

    Determines if a region and rectangle overlap at any point&nbsp;

    [SetRectRgn](#win32gui.md#win32guiSetRectRgn)

    Makes an existing region rectangular&nbsp;

    [CombineRgn](#win32gui.md#win32guiCombineRgn)

    Combines two regions&nbsp;

    [DrawAnimatedRects](#win32gui.md#win32guiDrawAnimatedRects)

    Animates a rectangle in the manner of minimizing, mazimizing, or opening&nbsp;

    [CreateSolidBrush](#win32gui.md#win32guiCreateSolidBrush)

    Creates a solid brush of specified color&nbsp;

    [CreatePatternBrush](#win32gui.md#win32guiCreatePatternBrush)

    Creates a brush using a bitmap as a pattern&nbsp;

    [CreateHatchBrush](#win32gui.md#win32guiCreateHatchBrush)

    Creates a hatch brush with specified style and color&nbsp;

    [CreatePen](#win32gui.md#win32guiCreatePen)

    Create a GDI pen&nbsp;

    [GetSysColor](#win32gui.md#win32guiGetSysColor)

    Returns the color of a window element&nbsp;

    [GetSysColorBrush](#win32gui.md#win32guiGetSysColorBrush)

    Creates a handle to a system color brush&nbsp;

    [InvalidateRect](#win32gui.md#win32guiInvalidateRect)

    Invalidates a rectangular area of a window and adds it to the window's update region&nbsp;

    [FrameRect](#win32gui.md#win32guiFrameRect)

    Draws an outline around a rectangle&nbsp;

    [InvertRect](#win32gui.md#win32guiInvertRect)

    Inverts the colors in a regtangular region&nbsp;

    [WindowFromDC](#win32gui.md#win32guiWindowFromDC)

    Finds the window associated with a device context&nbsp;

    [GetUpdateRgn](#win32gui.md#win32guiGetUpdateRgn)

    Copies the update region of a window into an existing region&nbsp;

    [GetWindowRgn](#win32gui.md#win32guiGetWindowRgn)

    Copies the window region of a window into an existing region&nbsp;

    [SetWindowRgn](#win32gui.md#win32guiSetWindowRgn)

    Sets the visible region of a window&nbsp;

    [GetWindowRgnBox](#win32gui.md#win32guiGetWindowRgnBox)

    Returns the bounding box for a window's region&nbsp;

    [ValidateRgn](#win32gui.md#win32guiValidateRgn)

    Removes a region from a window's update region&nbsp;

    [InvalidateRgn](#win32gui.md#win32guiInvalidateRgn)

    Adds a region to a window's update region&nbsp;

    [GetRgnBox](#win32gui.md#win32guiGetRgnBox)

    Calculates the bounding box of a region&nbsp;

    [OffsetRgn](#win32gui.md#win32guiOffsetRgn)

    Relocates a region&nbsp;

    [Rectangle](#win32gui.md#win32guiRectangle)

    Creates a solid rectangle using currently selected pen and brush&nbsp;

    [RoundRect](#win32gui.md#win32guiRoundRect)

    Draws a rectangle with elliptically rounded corners, filled using using current brush&nbsp;

    [BeginPaint](#win32gui.md#win32guiBeginPaint)

    &nbsp;

    [EndPaint](#win32gui.md#win32guiEndPaint)

    &nbsp;

    [BeginPath](#win32gui.md#win32guiBeginPath)

    Initializes a path in a DC&nbsp;

    [EndPath](#win32gui.md#win32guiEndPath)

    Finalizes a path begun by[win32gui::BeginPath](#win32gui.md#win32guiBeginPath)&nbsp;

    [AbortPath](#win32gui.md#win32guiAbortPath)

    Cancels a path begun by[win32gui::BeginPath](#win32gui.md#win32guiBeginPath)&nbsp;

    [CloseFigure](#win32gui.md#win32guiCloseFigure)

    Closes a section of a path by connecting the beginning pos with the current pos&nbsp;

    [FlattenPath](#win32gui.md#win32guiFlattenPath)

    Flattens any curves in current path into a series of lines&nbsp;

    [FillPath](#win32gui.md#win32guiFillPath)

    Fills a path with currently selected brush&nbsp;

    [WidenPath](#win32gui.md#win32guiWidenPath)

    Widens current path by amount it would increase by if drawn with currently selected pen&nbsp;

    [StrokePath](#win32gui.md#win32guiStrokePath)

    Draws current path with currently selected pen&nbsp;

    [StrokeAndFillPath](#win32gui.md#win32guiStrokeAndFillPath)

    Combines operations of StrokePath and FillPath with no overlap&nbsp;

    [GetMiterLimit](#win32gui.md#win32guiGetMiterLimit)

    Retrieves the limit of miter joins for a DC&nbsp;

    [SetMiterLimit](#win32gui.md#win32guiSetMiterLimit)

    Set the limit of miter joins for a DC&nbsp;

    [PathToRegion](#win32gui.md#win32guiPathToRegion)

    Converts a closed path in a DC to a region&nbsp;

    [GetPath](#win32gui.md#win32guiGetPath)

    Returns a sequence of points that describe the current path&nbsp;

    [CreateRoundRectRgn](#win32gui.md#win32guiCreateRoundRectRgn)

    Create a rectangular region with elliptically rounded corners,&nbsp;

    [CreateRectRgnIndirect](#win32gui.md#win32guiCreateRectRgnIndirect)

    Creates a rectangular region,&nbsp;

    [CreateEllipticRgnIndirect](#win32gui.md#win32guiCreateEllipticRgnIndirect)

    Creates an ellipse region,&nbsp;

    [CreateWindowEx](#win32gui.md#win32guiCreateWindowEx)

    Creates a new window with Extended Style.&nbsp;

    [GetParent](#win32gui.md#win32guiGetParent)

    Retrieves a handle to the specified child window's parent window.&nbsp;

    [SetParent](#win32gui.md#win32guiSetParent)

    changes the parent window of the specified child window.&nbsp;

    [GetCursorPos](#win32gui.md#win32guiGetCursorPos)

    retrieves the cursor's position, in screen coordinates.&nbsp;

    [GetDesktopWindow](#win32gui.md#win32guiGetDesktopWindow)

    returns the desktop window&nbsp;

    [GetWindow](#win32gui.md#win32guiGetWindow)

    returns a window that has the specified relationship (Z order or owner) to the specified window.&nbsp;

    [GetWindowDC](#win32gui.md#win32guiGetWindowDC)

    returns the device context (DC) for the entire window, including title bar, menus, and scroll bars.&nbsp;

    [IsIconic](#win32gui.md#win32guiIsIconic)

    determines whether the specified window is minimized (iconic).&nbsp;

    [IsWindow](#win32gui.md#win32guiIsWindow)

    determines whether the specified window handle identifies an existing window.&nbsp;

    [IsChild](#win32gui.md#win32guiIsChild)

    Tests whether a window is a child window or descendant window of a specified parent window&nbsp;

    [ReleaseCapture](#win32gui.md#win32guiReleaseCapture)

    Releases the moust capture for a window.&nbsp;

    [GetCapture](#win32gui.md#win32guiGetCapture)

    Returns the window with the mouse capture.&nbsp;

    [SetCapture](#win32gui.md#win32guiSetCapture)

    Captures the mouse for the specified window.&nbsp;

    [_TrackMouseEvent](#win32gui.md#win32gui_TrackMouseEvent)

    Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.&nbsp;

    [ReleaseDC](#win32gui.md#win32guiReleaseDC)

    Releases a device context.&nbsp;

    [CreateCaret](#win32gui.md#win32guiCreateCaret)

    Creates a new caret for a window&nbsp;

    [DestroyCaret](#win32gui.md#win32guiDestroyCaret)

    Destroys caret for current task&nbsp;

    [ScrollWindowEx](#win32gui.md#win32guiScrollWindowEx)

    scrolls the content of the specified window's client area.&nbsp;

    [SetScrollInfo](#win32gui.md#win32guiSetScrollInfo)

    Sets information about a scroll-bar&nbsp;

    [GetScrollInfo](#win32gui.md#win32guiGetScrollInfo)

    Returns information about a scroll bar&nbsp;

    [GetClassName](#win32gui.md#win32guiGetClassName)

    Retrieves the name of the class to which the specified window belongs.&nbsp;

    [WindowFromPoint](#win32gui.md#win32guiWindowFromPoint)

    Retrieves a handle to the window that contains the specified point.&nbsp;

    [ChildWindowFromPoint](#win32gui.md#win32guiChildWindowFromPoint)

    Determines which, if any, of the child windows belonging to a parent window contains the specified point.&nbsp;

    [ChildWindowFromPoint](#win32gui.md#win32guiChildWindowFromPoint)

    Determines which, if any, of the child windows belonging to a parent window contains the specified point.&nbsp;

    [ListView_SortItems](#win32gui.md#win32guiListView_SortItems)

    Uses an application-defined comparison function to sort the items of a list view control.&nbsp;

    [ListView_SortItemsEx](#win32gui.md#win32guiListView_SortItemsEx)

    Uses an application-defined comparison function to sort the items of a list view control.&nbsp;

    [CreateDC](#win32gui.md#win32guiCreateDC)

    Creates a device context for a printer or display device&nbsp;

    [GetSaveFileNameW](#win32gui.md#win32guiGetSaveFileNameW)

    Creates a dialog for user to specify location to save a file or files&nbsp;

    [GetOpenFileNameW](#win32gui.md#win32guiGetOpenFileNameW)

    Creates a dialog to allow user to select file(s) to open&nbsp;

    [SystemParametersInfo](#win32gui.md#win32guiSystemParametersInfo)

    Queries or sets system-wide parameters. This function can also update the user profile while setting a parameter.&nbsp;

    [SetLayeredWindowAttributes](#win32gui.md#win32guiSetLayeredWindowAttributes)

    Sets the opacity and transparency color key of a layered window.&nbsp;

    [GetLayeredWindowAttributes](#win32gui.md#win32guiGetLayeredWindowAttributes)

    Retrieves the layering parameters of a window with the WS_EX_LAYERED extended style&nbsp;

    [UpdateLayeredWindow](#win32gui.md#win32guiUpdateLayeredWindow)

    Updates the position, size, shape, content, and translucency of a layered window.&nbsp;

    [AnimateWindow](#win32gui.md#win32guiAnimateWindow)

    Enables you to produce special effects when showing or hiding windows. There are three types of animation: roll, slide, and alpha-blended fade.&nbsp;

    [CreateBrushIndirect](#win32gui.md#win32guiCreateBrushIndirect)

    Creates a GDI brush from a LOGBRUSH struct&nbsp;

    [ExtCreatePen](#win32gui.md#win32guiExtCreatePen)

    Creates a GDI pen object&nbsp;

    [DrawTextW](#win32gui.md#win32guiDrawTextW)

    Draws Unicode text on a device context.&nbsp;

    [EnumPropsEx](#win32gui.md#win32guiEnumPropsEx)

    Enumerates properties attached to a window. 

Each property is passed to a callback function, which receives 4 arguments:
Handle to the window, name of the property, handle to the property data, and Param object passed to this function&nbsp;

    [RegisterDeviceNotification](#win32gui.md#win32guiRegisterDeviceNotification)

    Registers the device or type of device for which a window will receive notifications.&nbsp;

    [UnregisterDeviceNotification](#win32gui.md#win32guiUnregisterDeviceNotification)

    Unregisters a Device Notification handle. 

It is generally not necessary to call this function manually, but in some cases, 

handle values may be extracted via the struct module and need to be closed explicitly.&nbsp;

    [RegisterHotKey](#win32gui.md#win32guiRegisterHotKey)

    Registers a hotkey for a window&nbsp;
------

##[win32pipe](md/win32pipe.md)

## Module win32pipe

An interface to the win32 pipe API's

#### Methods


    [GetNamedPipeHandleState](#win32pipe.md#win32pipeGetNamedPipeHandleState)

    Determines the state of the named pipe.&nbsp;

    [SetNamedPipeHandleState](#win32pipe.md#win32pipeSetNamedPipeHandleState)

    Sets the state of the named pipe.&nbsp;

    [ConnectNamedPipe](#win32pipe.md#win32pipeConnectNamedPipe)

    Connects to a named pipe&nbsp;

    [TransactNamedPipe](#win32pipe.md#win32pipeTransactNamedPipe)

    Combines the functions that write a 

message to and read a message from the specified named pipe into a single 

network operation.&nbsp;

    [CallNamedPipe](#win32pipe.md#win32pipeCallNamedPipe)

    Opens and performs a transaction on a named pipe.&nbsp;

    [CreatePipe](#win32pipe.md#win32pipeCreatePipe)

    Creates an anonymous pipe, and returns handles to the read and write ends of the pipe&nbsp;

    [FdCreatePipe](#win32pipe.md#win32pipeFdCreatePipe)

    As CreatePipe but returns file descriptors&nbsp;

    [CreateNamedPipe](#win32pipe.md#win32pipeCreateNamedPipe)

    Creates an instance of a named pipe and returns a handle for subsequent pipe operations&nbsp;

    [DisconnectNamedPipe](#win32pipe.md#win32pipeDisconnectNamedPipe)

    Disconnects the server end of a named pipe instance from a client process.&nbsp;

    [GetOverlappedResult](#win32pipe.md#win32pipeGetOverlappedResult)

    Determines the result of the most recent call with an OVERLAPPED object.&nbsp;

    [WaitNamedPipe](#win32pipe.md#win32pipeWaitNamedPipe)

    Waits until either a time-out interval elapses or an instance of the specified named pipe is available to be connected to (that is, the pipe's server process has a pending[win32pipe::ConnectNamedPipe](#win32pipe.md#win32pipeConnectNamedPipe)operation on the pipe).&nbsp;

    [GetNamedPipeInfo](#win32pipe.md#win32pipeGetNamedPipeInfo)

    Returns pipe's flags, buffer sizes, and max instances&nbsp;

    [PeekNamedPipe](#win32pipe.md#win32pipePeekNamedPipe)

    Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.&nbsp;

    [GetNamedPipeClientProcessId](#win32pipe.md#win32pipeGetNamedPipeClientProcessId)

    Returns the process id of client that is connected to a named pipe&nbsp;

    [GetNamedPipeServerProcessId](#win32pipe.md#win32pipeGetNamedPipeServerProcessId)

    Returns pid of server process that created a named pipe&nbsp;

    [GetNamedPipeClientSessionId](#win32pipe.md#win32pipeGetNamedPipeClientSessionId)

    Returns the session id of client that is connected to a named pipe&nbsp;

    [GetNamedPipeServerSessionId](#win32pipe.md#win32pipeGetNamedPipeServerSessionId)

    Returns session id of server process that created a named pipe&nbsp;

    [popen](#win32pipe.md#win32pipepopen)

    Version of popen that works in a GUI&nbsp;

#### Comments
Not implemented in py3k.

#### Methods


    [popen2](#win32pipe.md#win32pipepopen2)

    Variation on popen - returns 2 pipes&nbsp;
Not implemented in py3k.

#### Methods


    [popen3](#win32pipe.md#win32pipepopen3)

    Variation on popen - returns 3 pipes&nbsp;
Not implemented in py3k.

#### Methods


    [popen4](#win32pipe.md#win32pipepopen4)

    Like popen2, but stdout/err are combined.&nbsp;
Not implemented in py3k.
------

##[win32help](md/win32help.md)

## Module win32help

A module, encapsulating the Win32 help API's.

#### Methods


    [WinHelp](#win32help.md#win32helpWinHelp)

    Invokes the Windows Help system.&nbsp;

    [HH_AKLINK](#win32help.md#win32helpHH_AKLINK)

    Create and returns an HH_AKLINK structure&nbsp;

    [HH_FTS_QUERY](#win32help.md#win32helpHH_FTS_QUERY)

    Create and returns an HH_FTS_QUERY structure&nbsp;

    [HH_POPUP](#win32help.md#win32helpHH_POPUP)

    Create and returns an HH_POPUP structure&nbsp;

    [HH_WINTYPE](#win32help.md#win32helpHH_WINTYPE)

    Create and returns an HH_WINTYPE structure&nbsp;

    [NMHDR](#win32help.md#win32helpNMHDR)

    Create and returns an NMHDR structure&nbsp;

    [HHN_NOTIFY](#win32help.md#win32helpHHN_NOTIFY)

    Create and returns an HHN_NOTIFY structure&nbsp;

    [HHNTRACK](#win32help.md#win32helpHHNTRACK)

    Create and returns an HHNTRACK structure&nbsp;

    [HtmlHelp](#win32help.md#win32helpHtmlHelp)

    Invokes the Windows HTML Help system.&nbsp;
------

##[win32inet](md/win32inet.md)

## Module win32inet

An interface to the Windows internet (wininet) API

#### Methods


    [InternetSetCookie](#win32inet.md#win32inetInternetSetCookie)

    Creates a cookie associated with the specified URL.&nbsp;

    [InternetGetCookie](#win32inet.md#win32inetInternetGetCookie)

    Retrieves the cookie for the specified URL&nbsp;

    [InternetAttemptConnect](#win32inet.md#win32inetInternetAttemptConnect)

    Attempts to make a connection to the Internet.&nbsp;

    [InternetCheckConnection](#win32inet.md#win32inetInternetCheckConnection)

    Allows an application to check if a connection to the Internet can be established&nbsp;

    [InternetGoOnline](#win32inet.md#win32inetInternetGoOnline)

    Prompts the user for permission to initiate connection to a URL.&nbsp;

    [InternetCloseHandle](#win32inet.md#win32inetInternetCloseHandle)

    &nbsp;

    [InternetConnect](#win32inet.md#win32inetInternetConnect)

    Opens an FTP, Gopher, or HTTP session for a given site.&nbsp;

    [InternetOpen](#win32inet.md#win32inetInternetOpen)

    Initializes an application's use of the Microsoft&#174 Win32&#174 Internet functions.&nbsp;

    [InternetOpenUrl](#win32inet.md#win32inetInternetOpenUrl)

    Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL.&nbsp;

    [InternetCanonicalizeUrl](#win32inet.md#win32inetInternetCanonicalizeUrl)

    Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences.&nbsp;

    [InternetGetLastResponseInfo](#win32inet.md#win32inetInternetGetLastResponseInfo)

    Retrieves the last Win32&#174 Internet function error description or server response on the thread calling this function.&nbsp;

    [InternetReadFile](#win32inet.md#win32inetInternetReadFile)

    Reads data from a handle opened by the[win32inet::InternetOpenUrl](#win32inet.md#win32inetInternetOpenUrl),[win32inet::FtpOpenFile](#win32inet.md#win32inetFtpOpenFile), **win32inet::GopherOpenFile** , or **win32inet::HttpOpenRequest** function.&nbsp;

    [InternetWriteFile](#win32inet.md#win32inetInternetWriteFile)

    Writes data to a handle opened by[win32inet::FtpOpenFile](#win32inet.md#win32inetFtpOpenFile).&nbsp;

    [FtpOpenFile](#win32inet.md#win32inetFtpOpenFile)

    Initiates access to a remote file on an FTP server for reading or writing.&nbsp;

    [FtpCommand](#win32inet.md#win32inetFtpCommand)

    Allows an application to send commands directly to an FTP server.&nbsp;

    [InternetQueryOption](#win32inet.md#win32inetInternetQueryOption)

    Retrieves an option for an internet handle&nbsp;

    [InternetSetOption](#win32inet.md#win32inetInternetSetOption)

    Sets an option for an internet handle&nbsp;

    [FindFirstUrlCacheEntry](#win32inet.md#win32inetFindFirstUrlCacheEntry)

    Initiates an enumeration of the browser cache&nbsp;

    [FindNextUrlCacheEntry](#win32inet.md#win32inetFindNextUrlCacheEntry)

    Continues enumeration of cached files&nbsp;

    [FindFirstUrlCacheEntryEx](#win32inet.md#win32inetFindFirstUrlCacheEntryEx)

    Initiates an enumeration of the browser cache&nbsp;

    [FindNextUrlCacheEntryEx](#win32inet.md#win32inetFindNextUrlCacheEntryEx)

    Continues enumeration of cached files&nbsp;

    [FindCloseUrlCache](#win32inet.md#win32inetFindCloseUrlCache)

    Closes a cache enumeration handle&nbsp;

    [FindFirstUrlCacheGroup](#win32inet.md#win32inetFindFirstUrlCacheGroup)

    Initiates enumeration of Url cache groups&nbsp;

    [FindNextUrlCacheGroup](#win32inet.md#win32inetFindNextUrlCacheGroup)

    Continues enumeration of cache groups&nbsp;

    [GetUrlCacheEntryInfo](#win32inet.md#win32inetGetUrlCacheEntryInfo)

    Retrieves cache info for a URL&nbsp;

    [DeleteUrlCacheGroup](#win32inet.md#win32inetDeleteUrlCacheGroup)

    Deletes a cache group&nbsp;

    [CreateUrlCacheGroup](#win32inet.md#win32inetCreateUrlCacheGroup)

    Creates a new cache group&nbsp;

    [CreateUrlCacheEntry](#win32inet.md#win32inetCreateUrlCacheEntry)

    Creates a cache entry for a URL&nbsp;

    [CommitUrlCacheEntry](#win32inet.md#win32inetCommitUrlCacheEntry)

    Commits a cache entry&nbsp;

    [SetUrlCacheEntryGroup](#win32inet.md#win32inetSetUrlCacheEntryGroup)

    Associates a cache entry with a group&nbsp;

    [GetUrlCacheGroupAttribute](#win32inet.md#win32inetGetUrlCacheGroupAttribute)

    Retrieves attributes for a cache group&nbsp;

    [SetUrlCacheGroupAttribute](#win32inet.md#win32inetSetUrlCacheGroupAttribute)

    Changes the attributes of a cache group&nbsp;

    [DeleteUrlCacheEntry](#win32inet.md#win32inetDeleteUrlCacheEntry)

    Deletes the cache entry for a URL&nbsp;
------

##[win32api](md/win32api.md)

## Module win32api

A module, encapsulating the Windows Win32 API.

#### Methods


    [AbortSystemShutdown](#win32api.md#win32apiAbortSystemShutdown)

    Aborts a system shutdown&nbsp;

    [InitiateSystemShutdown](#win32api.md#win32apiInitiateSystemShutdown)

    Initiates a shutdown and optional restart of the specified computer.&nbsp;

    [Apply](#win32api.md#win32apiApply)

    Calls a Python function, but traps Win32 exceptions.&nbsp;

    [Beep](#win32api.md#win32apiBeep)

    Generates a simple tone on the speaker.&nbsp;

    [BeginUpdateResource](#win32api.md#win32apiBeginUpdateResource)

    Begins an update cycle for a PE file.&nbsp;

    [ChangeDisplaySettings](#win32api.md#win32apiChangeDisplaySettings)

    Changes video mode for default display&nbsp;

    [ChangeDisplaySettingsEx](#win32api.md#win32apiChangeDisplaySettingsEx)

    Changes video mode for specified display&nbsp;

    [ClipCursor](#win32api.md#win32apiClipCursor)

    Confines the cursor to a rectangular area on the screen.&nbsp;

    [CloseHandle](#win32api.md#win32apiCloseHandle)

    Closes an open handle.&nbsp;

    [CopyFile](#win32api.md#win32apiCopyFile)

    Copy a file.&nbsp;

    [DebugBreak](#win32api.md#win32apiDebugBreak)

    Breaks into the C debugger.&nbsp;

    [DeleteFile](#win32api.md#win32apiDeleteFile)

    Deletes the specified file.&nbsp;

    [DragQueryFile](#win32api.md#win32apiDragQueryFile)

    Retrieve the file names for dropped files.&nbsp;

    [DragFinish](#win32api.md#win32apiDragFinish)

    Free memory associated with dropped files.&nbsp;

    [DuplicateHandle](#win32api.md#win32apiDuplicateHandle)

    Duplicates a handle.&nbsp;

    [EndUpdateResource](#win32api.md#win32apiEndUpdateResource)

    Ends a resource update cycle of a PE file.&nbsp;

    [EnumDisplayDevices](#win32api.md#win32apiEnumDisplayDevices)

    Obtain information about the display devices in a system&nbsp;

    [EnumDisplayMonitors](#win32api.md#win32apiEnumDisplayMonitors)

    Lists monitors for a device context&nbsp;

    [EnumDisplaySettings](#win32api.md#win32apiEnumDisplaySettings)

    Lists available modes for specified device&nbsp;

    [EnumDisplaySettingsEx](#win32api.md#win32apiEnumDisplaySettingsEx)

    Lists available modes for a display device, with optional flags&nbsp;

    [EnumResourceLanguages](#win32api.md#win32apiEnumResourceLanguages)

    List languages for specified resource&nbsp;

    [EnumResourceNames](#win32api.md#win32apiEnumResourceNames)

    Enumerates all the resources of the specified type from the nominated file.&nbsp;

    [EnumResourceTypes](#win32api.md#win32apiEnumResourceTypes)

    Return list of all resource types contained in module&nbsp;

    [ExpandEnvironmentStrings](#win32api.md#win32apiExpandEnvironmentStrings)

    Expands environment-variable strings and replaces them with their defined values.&nbsp;

    [ExitWindows](#win32api.md#win32apiExitWindows)

    Logs off the current user&nbsp;

    [ExitWindowsEx](#win32api.md#win32apiExitWindowsEx)

    either logs off the current user, shuts down the system, or shuts down and restarts the system.&nbsp;

    [FindFiles](#win32api.md#win32apiFindFiles)

    Find files matching a file spec.&nbsp;

    [FindFirstChangeNotification](#win32api.md#win32apiFindFirstChangeNotification)

    Creates a change notification handle and sets up initial change notification filter conditions.&nbsp;

    [FindNextChangeNotification](#win32api.md#win32apiFindNextChangeNotification)

    Requests that the operating system signal a change notification handle the next time it detects an appropriate change.&nbsp;

    [FindCloseChangeNotification](#win32api.md#win32apiFindCloseChangeNotification)

    Closes the change notification handle.&nbsp;

    [FindExecutable](#win32api.md#win32apiFindExecutable)

    Find an executable associated with a document.&nbsp;

    [FormatMessage](#win32api.md#win32apiFormatMessage)

    Return an error message string.&nbsp;

    [FormatMessageW](#win32api.md#win32apiFormatMessageW)

    Return an error message string (as a Unicode object).&nbsp;

    [FreeLibrary](#win32api.md#win32apiFreeLibrary)

    Decrements the reference count of the loaded dynamic-link library (DLL) module.&nbsp;

    [GenerateConsoleCtrlEvent](#win32api.md#win32apiGenerateConsoleCtrlEvent)

    Send a specified signal to a console process group that shares the console associated with the calling process.&nbsp;

    [GetAsyncKeyState](#win32api.md#win32apiGetAsyncKeyState)

    Retrieves the asynch state of a virtual key code.&nbsp;

    [GetCommandLine](#win32api.md#win32apiGetCommandLine)

    Return the application's command line.&nbsp;

    [GetComputerName](#win32api.md#win32apiGetComputerName)

    Returns the local computer name&nbsp;

    [GetComputerNameEx](#win32api.md#win32apiGetComputerNameEx)

    Retrieves a NetBIOS or DNS name associated with the local computer&nbsp;

    [GetComputerObjectName](#win32api.md#win32apiGetComputerObjectName)

    Retrieves the local computer's name in a specified format&nbsp;

    [GetMonitorInfo](#win32api.md#win32apiGetMonitorInfo)

    Retrieves information for a monitor by handle&nbsp;

    [GetUserName](#win32api.md#win32apiGetUserName)

    Returns the current user name.&nbsp;

    [GetUserNameEx](#win32api.md#win32apiGetUserNameEx)

    Returns the current user name in format specified by Name* constants&nbsp;

    [GetCursorPos](#win32api.md#win32apiGetCursorPos)

    Returns the position of the cursor, in screen co-ordinates.&nbsp;

    [GetCurrentThread](#win32api.md#win32apiGetCurrentThread)

    Returns a pseudohandle for the current thread.&nbsp;

    [GetCurrentThreadId](#win32api.md#win32apiGetCurrentThreadId)

    Returns the thread ID for the current thread.&nbsp;

    [GetCurrentProcessId](#win32api.md#win32apiGetCurrentProcessId)

    Returns the thread ID for the current thread.&nbsp;

    [GetCurrentProcess](#win32api.md#win32apiGetCurrentProcess)

    Returns a pseudohandle for the current process.&nbsp;

    [GetConsoleTitle](#win32api.md#win32apiGetConsoleTitle)

    Return the application's console title.&nbsp;

    [GetDateFormat](#win32api.md#win32apiGetDateFormat)

    Formats a date as a date string for a specified locale.&nbsp;

    [GetDiskFreeSpace](#win32api.md#win32apiGetDiskFreeSpace)

    Retrieves information about a disk.&nbsp;

    [GetDiskFreeSpaceEx](#win32api.md#win32apiGetDiskFreeSpaceEx)

    Retrieves information about a disk.&nbsp;

    [GetDllDirectory](#win32api.md#win32apiGetDllDirectory)

    Retrieves the DLL search path&nbsp;

    [GetDomainName](#win32api.md#win32apiGetDomainName)

    Returns the current domain name&nbsp;

    [GetEnvironmentVariable](#win32api.md#win32apiGetEnvironmentVariable)

    Retrieves the value of an environment variable.&nbsp;

    [GetEnvironmentVariableW](#win32api.md#win32apiGetEnvironmentVariableW)

    Retrieves the value of an environment variable.&nbsp;

    [GetFileAttributes](#win32api.md#win32apiGetFileAttributes)

    Retrieves the attributes for the named file.&nbsp;

    [GetFileVersionInfo](#win32api.md#win32apiGetFileVersionInfo)

    Retrieves string version info&nbsp;

    [GetFocus](#win32api.md#win32apiGetFocus)

    Retrieves the handle of the keyboard focus window associated with the thread that called the method.&nbsp;

    [GetFullPathName](#win32api.md#win32apiGetFullPathName)

    Returns the full path of a (possibly relative) path&nbsp;

    [GetHandleInformation](#win32api.md#win32apiGetHandleInformation)

    Retrieves a handle's flags.&nbsp;

    [GetKeyboardLayout](#win32api.md#win32apiGetKeyboardLayout)

    Retrieves the active input locale identifier&nbsp;

    [GetKeyboardLayoutList](#win32api.md#win32apiGetKeyboardLayoutList)

    Returns a sequence of all locale ids in the system&nbsp;

    [GetKeyboardLayoutName](#win32api.md#win32apiGetKeyboardLayoutName)

    Retrieves the name of the active input locale identifier (formerly called the keyboard layout).&nbsp;

    [GetKeyboardState](#win32api.md#win32apiGetKeyboardState)

    Retrieves the status of the 256 virtual keys on the keyboard.&nbsp;

    [GetKeyState](#win32api.md#win32apiGetKeyState)

    Retrives the last known key state for a key.&nbsp;

    [GetLastError](#win32api.md#win32apiGetLastError)

    Retrieves the last error code known by the system.&nbsp;

    [GetLastInputInfo](#win32api.md#win32apiGetLastInputInfo)

    Returns time of last input event in tick count&nbsp;

    [GetLocalTime](#win32api.md#win32apiGetLocalTime)

    Returns the current local time.&nbsp;

    [GetLongPathName](#win32api.md#win32apiGetLongPathName)

    Converts the specified path to its long form.&nbsp;

    [GetLongPathNameW](#win32api.md#win32apiGetLongPathNameW)

    Converts the specified path to its long form.&nbsp;

    [GetLogicalDrives](#win32api.md#win32apiGetLogicalDrives)

    Returns a bitmask representing the currently available disk drives.&nbsp;

    [GetLogicalDriveStrings](#win32api.md#win32apiGetLogicalDriveStrings)

    Returns a list of strings for all the drives.&nbsp;

    [GetModuleFileName](#win32api.md#win32apiGetModuleFileName)

    Retrieves the filename of the specified module.&nbsp;

    [GetModuleFileNameW](#win32api.md#win32apiGetModuleFileNameW)

    Retrieves the unicode filename of the specified module.&nbsp;

    [GetModuleHandle](#win32api.md#win32apiGetModuleHandle)

    Returns the handle of an already loaded DLL.&nbsp;

    [GetPwrCapabilities](#win32api.md#win32apiGetPwrCapabilities)

    Retrieves system's power capabilities&nbsp;

    [GetProfileSection](#win32api.md#win32apiGetProfileSection)

    Returns a list of entries in an INI file.&nbsp;

    [GetProcAddress](#win32api.md#win32apiGetProcAddress)

    Returns the address of the specified exported dynamic-link library (DLL) function.&nbsp;

    [GetProfileVal](#win32api.md#win32apiGetProfileVal)

    Returns a value from an INI file.&nbsp;

    [GetShortPathName](#win32api.md#win32apiGetShortPathName)

    Returns the 8.3 version of a pathname.&nbsp;

    [GetStdHandle](#win32api.md#win32apiGetStdHandle)

    Returns a handle for the standard input, standard output, or standard error device&nbsp;

    [GetSysColor](#win32api.md#win32apiGetSysColor)

    Returns the system colors.&nbsp;

    [GetSystemDefaultLangID](#win32api.md#win32apiGetSystemDefaultLangID)

    Retrieves the system default language identifier.&nbsp;

    [GetSystemDefaultLCID](#win32api.md#win32apiGetSystemDefaultLCID)

    Retrieves the system default locale identifier.&nbsp;

    [GetSystemDirectory](#win32api.md#win32apiGetSystemDirectory)

    Returns the Windows system directory.&nbsp;

    [GetSystemFileCacheSize](#win32api.md#win32apiGetSystemFileCacheSize)

    Returns the amount of memory reserved for file cache&nbsp;

    [SetSystemFileCacheSize](#win32api.md#win32apiSetSystemFileCacheSize)

    Sets the amount of memory reserved for file cache&nbsp;

    [GetSystemInfo](#win32api.md#win32apiGetSystemInfo)

    Retrieves information about the current system.&nbsp;

    [GetNativeSystemInfo](#win32api.md#win32apiGetNativeSystemInfo)

    Retrieves information about the current system for a Wow64 process.&nbsp;

    [GetSystemMetrics](#win32api.md#win32apiGetSystemMetrics)

    Returns the specified system metrics.&nbsp;

    [GetSystemTime](#win32api.md#win32apiGetSystemTime)

    Returns the current system time.&nbsp;

    [GetTempFileName](#win32api.md#win32apiGetTempFileName)

    Creates a temporary file.&nbsp;

    [GetTempPath](#win32api.md#win32apiGetTempPath)

    Returns the path designated as holding temporary files.&nbsp;

    [GetThreadLocale](#win32api.md#win32apiGetThreadLocale)

    Returns the current thread's locale.&nbsp;

    [GetTickCount](#win32api.md#win32apiGetTickCount)

    Returns the milliseconds since windows started.&nbsp;

    [GetTimeFormat](#win32api.md#win32apiGetTimeFormat)

    Formats a time as a time string for a specified locale.&nbsp;

    [GetTimeZoneInformation](#win32api.md#win32apiGetTimeZoneInformation)

    Returns the system time-zone information.&nbsp;

    [GetVersion](#win32api.md#win32apiGetVersion)

    Returns Windows version information.&nbsp;

    [GetVersionEx](#win32api.md#win32apiGetVersionEx)

    Returns Windows version information as a tuple.&nbsp;

    [GetVolumeInformation](#win32api.md#win32apiGetVolumeInformation)

    Returns information about a volume and file system attached to the system.&nbsp;

    [GetWindowsDirectory](#win32api.md#win32apiGetWindowsDirectory)

    Returns the windows directory.&nbsp;

    [GetWindowLong](#win32api.md#win32apiGetWindowLong)

    Retrieves a long value at the specified offset into the extra window memory of the given window.&nbsp;

    [GetUserDefaultLangID](#win32api.md#win32apiGetUserDefaultLangID)

    Retrieves the user default language identifier.&nbsp;

    [GetUserDefaultLCID](#win32api.md#win32apiGetUserDefaultLCID)

    Retrieves the user default locale identifier.&nbsp;

    [GlobalMemoryStatus](#win32api.md#win32apiGlobalMemoryStatus)

    Returns systemwide memory usage&nbsp;

    [GlobalMemoryStatusEx](#win32api.md#win32apiGlobalMemoryStatusEx)

    Returns physical and virtual memory usage&nbsp;

    [keybd_event](#win32api.md#win32apikeybd_event)

    Simulate a keyboard event&nbsp;

    [mouse_event](#win32api.md#win32apimouse_event)

    Simulate a mouse event&nbsp;

    [LoadCursor](#win32api.md#win32apiLoadCursor)

    Loads a cursor.&nbsp;

    [LoadKeyboardLayout](#win32api.md#win32apiLoadKeyboardLayout)

    Loads a new locale id&nbsp;

    [LoadLibrary](#win32api.md#win32apiLoadLibrary)

    Loads the specified DLL, and returns the handle.&nbsp;

    [LoadLibraryEx](#win32api.md#win32apiLoadLibraryEx)

    Loads the specified DLL, and returns the handle.&nbsp;

    [LoadResource](#win32api.md#win32apiLoadResource)

    Finds and loads a resource from a PE file.&nbsp;

    [LoadString](#win32api.md#win32apiLoadString)

    Loads a string from a resource file.&nbsp;

    [MapVirtualKeyEx](#win32api.md#win32apiMapVirtualKeyEx)

    Translates (maps) a virtual-key code into a scan code or character value, or translates a scan code into a virtual-key code.&nbsp;

    [MessageBeep](#win32api.md#win32apiMessageBeep)

    Plays a predefined waveform sound.&nbsp;

    [MessageBox](#win32api.md#win32apiMessageBox)

    Display a message box.&nbsp;

    [MonitorFromPoint](#win32api.md#win32apiMonitorFromPoint)

    Finds monitor that contains a point&nbsp;

    [MonitorFromRect](#win32api.md#win32apiMonitorFromRect)

    Finds monitor that has largest intersection with a rectangle&nbsp;

    [MonitorFromWindow](#win32api.md#win32apiMonitorFromWindow)

    Finds monitor that contains a window&nbsp;

    [MoveFile](#win32api.md#win32apiMoveFile)

    Moves or renames a file.&nbsp;

    [MoveFileEx](#win32api.md#win32apiMoveFileEx)

    Moves or renames a file.&nbsp;

    [OpenProcess](#win32api.md#win32apiOpenProcess)

    Retrieves a handle to an existing process.&nbsp;

    [OutputDebugString](#win32api.md#win32apiOutputDebugString)

    Writes output to the Windows debugger.&nbsp;

    [PostMessage](#win32api.md#win32apiPostMessage)

    Post a message to a window.&nbsp;

    [PostQuitMessage](#win32api.md#win32apiPostQuitMessage)

    Posts a quit message.&nbsp;

    [PostThreadMessage](#win32api.md#win32apiPostThreadMessage)

    Post a message to a thread.&nbsp;

    [RegCloseKey](#win32api.md#win32apiRegCloseKey)

    Closes a registry key.&nbsp;

    [RegConnectRegistry](#win32api.md#win32apiRegConnectRegistry)

    Establishes a connection to a predefined registry handle on another computer.&nbsp;

    [RegCopyTree](#win32api.md#win32apiRegCopyTree)

    Copies an entire registry key to another location&nbsp;

    [RegCreateKey](#win32api.md#win32apiRegCreateKey)

    Creates the specified key, or opens the key if it already exists.&nbsp;

    [RegCreateKeyEx](#win32api.md#win32apiRegCreateKeyEx)

    Extended version of RegCreateKey&nbsp;

    [RegDeleteKey](#win32api.md#win32apiRegDeleteKey)

    Deletes the specified key.&nbsp;

    [RegDeleteKeyEx](#win32api.md#win32apiRegDeleteKeyEx)

    Deletes a registry key from 32 or 64 bit registry view&nbsp;

    [RegDeleteTree](#win32api.md#win32apiRegDeleteTree)

    Recursively deletes a key's subkeys and values&nbsp;

    [RegDeleteValue](#win32api.md#win32apiRegDeleteValue)

    Removes a named value from the specified registry key.&nbsp;

    [RegEnumKey](#win32api.md#win32apiRegEnumKey)

    Enumerates subkeys of the specified open registry key.&nbsp;

    [RegEnumKeyEx](#win32api.md#win32apiRegEnumKeyEx)

    Enumerates subkeys of the specified open registry key.&nbsp;

    [RegEnumKeyExW](#win32api.md#win32apiRegEnumKeyExW)

    Unicode version of RegEnumKeyEx&nbsp;

    [RegEnumValue](#win32api.md#win32apiRegEnumValue)

    Enumerates values of the specified open registry key.&nbsp;

    [RegFlushKey](#win32api.md#win32apiRegFlushKey)

    Writes all the attributes of the specified key to the registry.&nbsp;

    [RegGetKeySecurity](#win32api.md#win32apiRegGetKeySecurity)

    Retrieves the security on the specified registry key.&nbsp;

    [RegLoadKey](#win32api.md#win32apiRegLoadKey)

    Creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE and stores registration information from a specified file into that subkey.&nbsp;

    [RegOpenCurrentUser](#win32api.md#win32apiRegOpenCurrentUser)

    Opens HKEY_CURRENT_USER for impersonated user&nbsp;

    [RegOpenKey](#win32api.md#win32apiRegOpenKey)

    Alias for[win32api::RegOpenKeyEx](#win32api.md#win32apiRegOpenKeyEx)&nbsp;

    [RegOpenKeyEx](#win32api.md#win32apiRegOpenKeyEx)

    Opens the specified key.&nbsp;

    [RegOpenKeyTransacted](#win32api.md#win32apiRegOpenKeyTransacted)

    Opens a registry key as part of a transaction.&nbsp;

    [RegOverridePredefKey](#win32api.md#win32apiRegOverridePredefKey)

    Redirects one of the predefined keys to different key.&nbsp;

    [RegQueryValue](#win32api.md#win32apiRegQueryValue)

    Retrieves the value associated with the unnamed value for a specified key in the registry.&nbsp;

    [RegQueryValueEx](#win32api.md#win32apiRegQueryValueEx)

    Retrieves the type and data for a specified value name associated with an open registry key.&nbsp;

    [RegQueryInfoKey](#win32api.md#win32apiRegQueryInfoKey)

    Returns information about the specified key.&nbsp;

    [RegQueryInfoKeyW](#win32api.md#win32apiRegQueryInfoKeyW)

    Returns information about an open registry key&nbsp;

    [RegRestoreKey](#win32api.md#win32apiRegRestoreKey)

    Restores a key and subkeys from a saved registry file&nbsp;

    [RegSaveKey](#win32api.md#win32apiRegSaveKey)

    Saves the specified key, and all its subkeys to the specified file.&nbsp;

    [RegSaveKeyEx](#win32api.md#win32apiRegSaveKeyEx)

    Extended version of RegSaveKey&nbsp;

    [RegSetKeySecurity](#win32api.md#win32apiRegSetKeySecurity)

    Sets the security on the specified registry key.&nbsp;

    [RegSetValue](#win32api.md#win32apiRegSetValue)

    Associates a value with a specified key.  Currently, only strings are supported.&nbsp;

    [RegSetValueEx](#win32api.md#win32apiRegSetValueEx)

    Stores data in the value field of an open registry key.&nbsp;

    [RegUnLoadKey](#win32api.md#win32apiRegUnLoadKey)

    Unloads the specified registry key and its subkeys from the registry.  The keys must have been loaded previously by a call to RegLoadKey.&nbsp;

    [RegisterWindowMessage](#win32api.md#win32apiRegisterWindowMessage)

    Given a string, return a system wide unique message ID.&nbsp;

    [RegNotifyChangeKeyValue](#win32api.md#win32apiRegNotifyChangeKeyValue)

    Watch for registry changes&nbsp;

    [SearchPath](#win32api.md#win32apiSearchPath)

    Searches a path for a file.&nbsp;

    [SendMessage](#win32api.md#win32apiSendMessage)

    Send a message to a window.&nbsp;

    [SetConsoleCtrlHandler](#win32api.md#win32apiSetConsoleCtrlHandler)

    Adds or removes an application-defined HandlerRoutine function from the list of handler functions for the calling process.&nbsp;

    [SetConsoleTitle](#win32api.md#win32apiSetConsoleTitle)

    Sets the title for the current console.&nbsp;

    [SetCursorPos](#win32api.md#win32apiSetCursorPos)

    The SetCursorPos function moves the cursor to the specified screen coordinates.&nbsp;

    [SetDllDirectory](#win32api.md#win32apiSetDllDirectory)

    Modifies the application-specific DLL search path&nbsp;

    [SetErrorMode](#win32api.md#win32apiSetErrorMode)

    Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.&nbsp;

    [SetFileAttributes](#win32api.md#win32apiSetFileAttributes)

    Sets the named file's attributes.&nbsp;

    [SetLastError](#win32api.md#win32apiSetLastError)

    Sets the last error code known for the current thread.&nbsp;

    [SetSysColors](#win32api.md#win32apiSetSysColors)

    Changes color of various window elements&nbsp;

    [SetLocalTime](#win32api.md#win32apiSetLocalTime)

    Changes the system's local time.&nbsp;

    [SetSystemTime](#win32api.md#win32apiSetSystemTime)

    Sets the system time.&nbsp;

    [SetClassLong](#win32api.md#win32apiSetClassLong)

    Replaces the specified 32-bit (long) value at the specified offset into the extra class memory for the window.&nbsp;

    [SetClassWord](#win32api.md#win32apiSetClassWord)

    Replaces the specified 32-bit (long) value at the specified offset into the extra class memory for the window.&nbsp;

    [SetWindowWord](#win32api.md#win32apiSetWindowWord)

    &nbsp;

    [SetCursor](#win32api.md#win32apiSetCursor)

    Set the cursor to the HCURSOR object.&nbsp;

    [SetEnvironmentVariable](#win32api.md#win32apiSetEnvironmentVariable)

    Creates, deletes, or changes the value of an environment variable.&nbsp;

    [SetEnvironmentVariable](#win32api.md#win32apiSetEnvironmentVariable)

    Creates, deletes, or changes the value of an environment variable.&nbsp;

    [SetEnvironmentVariableW](#win32api.md#win32apiSetEnvironmentVariableW)

    Creates, deletes, or changes the value of an environment variable.&nbsp;

    [SetHandleInformation](#win32api.md#win32apiSetHandleInformation)

    Sets a handles's flags&nbsp;

    [SetStdHandle](#win32api.md#win32apiSetStdHandle)

    Sets a handle for the standard input, standard output, or standard error device&nbsp;

    [SetSystemPowerState](#win32api.md#win32apiSetSystemPowerState)

    Powers machine down to a suspended state&nbsp;

    [SetThreadLocale](#win32api.md#win32apiSetThreadLocale)

    Sets the current thread's locale.&nbsp;

    [SetTimeZoneInformation](#win32api.md#win32apiSetTimeZoneInformation)

    Sets the system time-zone information.&nbsp;

    [SetWindowLong](#win32api.md#win32apiSetWindowLong)

    Places a long value at the specified offset into the extra window memory of the given window.&nbsp;

    [ShellExecute](#win32api.md#win32apiShellExecute)

    Executes an application.&nbsp;

    [ShowCursor](#win32api.md#win32apiShowCursor)

    The ShowCursor method displays or hides the cursor.&nbsp;

    [Sleep](#win32api.md#win32apiSleep)

    Suspends current application execution&nbsp;

    [TerminateProcess](#win32api.md#win32apiTerminateProcess)

    Terminates a process.&nbsp;

    [ToAsciiEx](#win32api.md#win32apiToAsciiEx)

    Translates the specified virtual-key code and keyboard state to the corresponding character or characters.&nbsp;

    [Unicode](#win32api.md#win32apiUnicode)

    Creates a new[PyUnicode](#README.md#PyUnicode)object&nbsp;

    [UpdateResource](#win32api.md#win32apiUpdateResource)

    Updates a resource in a PE file.&nbsp;

    [VkKeyScan](#win32api.md#win32apiVkKeyScan)

    Translates a character to the corresponding virtual-key code and shift state.&nbsp;

    [VkKeyScan](#win32api.md#win32apiVkKeyScan)

    Translates a character to the corresponding virtual-key code and shift state.&nbsp;

    [WinExec](#win32api.md#win32apiWinExec)

    Execute a program.&nbsp;

    [WinHelp](#win32api.md#win32apiWinHelp)

    Invokes the Windows Help engine.&nbsp;

    [WriteProfileSection](#win32api.md#win32apiWriteProfileSection)

    Writes a complete section to an INI file or registry.&nbsp;

    [WriteProfileVal](#win32api.md#win32apiWriteProfileVal)

    Write a value to a Windows INI file.&nbsp;

    [HIBYTE](#win32api.md#win32apiHIBYTE)

    An interface to the win32api HIBYTE macro.&nbsp;

    [LOBYTE](#win32api.md#win32apiLOBYTE)

    An interface to the win32api LOBYTE macro.&nbsp;

    [HIWORD](#win32api.md#win32apiHIWORD)

    An interface to the win32api HIWORD macro.&nbsp;

    [LOWORD](#win32api.md#win32apiLOWORD)

    An interface to the win32api LOWORD macro.&nbsp;

    [RGB](#win32api.md#win32apiRGB)

    An interface to the win32api RGB macro.&nbsp;

    [MAKELANGID](#win32api.md#win32apiMAKELANGID)

    Creates a language identifier from a primary language identifier and a sublanguage identifier.&nbsp;

    [MAKEWORD](#win32api.md#win32apiMAKEWORD)

    creates a WORD value by concatenating the specified values.&nbsp;

    [MAKELONG](#win32api.md#win32apiMAKELONG)

    creates a LONG value by concatenating the specified values.&nbsp;
------

