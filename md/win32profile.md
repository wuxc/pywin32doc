# win32profile

## Module win32profile



Wraps functions for dealing with user profiles

#### Methods


  - [CreateEnvironmentBlock](win32profile.md#win32profilecreateenvironmentblock)

    Retrieves environment variables for a user&nbsp;

  - [DeleteProfile](win32profile.md#win32profiledeleteprofile)

    Removes a user's profile&nbsp;

  - [ExpandEnvironmentStringsForUser](win32profile.md#win32profileexpandenvironmentstringsforuser)

    Replaces environment variables in a string with per-user values&nbsp;

  - [GetAllUsersProfileDirectory](win32profile.md#win32profilegetallusersprofiledirectory)

    Retrieve All Users profile directory&nbsp;

  - [GetDefaultUserProfileDirectory](win32profile.md#win32profilegetdefaultuserprofiledirectory)

    Retrieve profile path for Default user&nbsp;

  - [GetEnvironmentStrings](win32profile.md#win32profilegetenvironmentstrings)

    Retrieves environment variables for current process&nbsp;

  - [GetProfilesDirectory](win32profile.md#win32profilegetprofilesdirectory)

    Retrieves directory where user profiles are stored&nbsp;

  - [GetProfileType](win32profile.md#win32profilegetprofiletype)

    Returns type of current user's profile&nbsp;

  - [GetUserProfileDirectory](win32profile.md#win32profilegetuserprofiledirectory)

    Returns profile directory for a logon token&nbsp;

  - [LoadUserProfile](win32profile.md#win32profileloaduserprofile)

    Load user settings for a login token&nbsp;

  - [UnloadUserProfile](win32profile.md#win32profileunloaduserprofile)

    Unload profile loaded by LoadUserProfile&nbsp;

## [win32profile](#win32profile)\.CreateEnvironmentBlock



dict =CreateEnvironmentBlock\(Token, Inherit\)
Retrieves environment variables for a user

#### Parameters


  - Token :[PyHANDLE](#pyhandle)

    User token as returned by[win32security::LogonUser](win32security.md#win32securitylogonuser), use None to retrieve system variables only

  - Inherit : boolean

    Indicates if environment of current process should be inherited

## [win32profile](#win32profile)\.DeleteProfile

DeleteProfile\(SidString, ProfilePath, ComputerName\)
Remove profile for a user identified by string SID from specified machine\.

#### Parameters


  - SidString :[PyUnicode](#pyunicode)

    String representation of user's Sid\.  See[win32security::ConvertSidToStringSid](win32security.md#win32securityconvertsidtostringsid)\.

  - ProfilePath=None :[PyUnicode](#pyunicode)

    Profile directory, value queried from registry if not specified

  - ComputerName=None :[PyUnicode](#pyunicode)

    Name of computer from which to delete profile, local machine assumed if not specified

## [win32profile](#win32profile)\.ExpandEnvironmentStringsForUser

[PyUnicode](#pyunicode) =ExpandEnvironmentStringsForUser\(Token, Src\)
Replaces environment variables in a string with per-user values

#### Parameters


  - Token :[PyHANDLE](#pyhandle)

    The logon token for a user\.  Use None for system variables\.

  - Src :[PyUnicode](#pyunicode)

    String containing environment variables enclosed in % signs

## [win32profile](#win32profile)\.GetAllUsersProfileDirectory

[PyUnicode](#pyunicode) =GetAllUsersProfileDirectory\(\)
Retrieve All Users profile path

## [win32profile](#win32profile)\.GetDefaultUserProfileDirectory

[PyUnicode](#pyunicode) =GetDefaultUserProfileDirectory\(\)
Retrieve Default user profile

## [win32profile](#win32profile)\.GetEnvironmentStrings



dict =GetEnvironmentStrings\(\)
Retrieves environment variables for current process

## [win32profile](#win32profile)\.GetProfileType



int =GetProfileType\(\)
Returns type of current user's profile

#### Return Value
Returns a combination of PT\_\* flags

## [win32profile](#win32profile)\.GetProfilesDirectory

[PyUnicode](#pyunicode) =GetProfilesDirectory\(\)
Retrieves directory where user profiles are stored

## [win32profile](#win32profile)\.GetUserProfileDirectory

[PyUnicode](#pyunicode) =GetUserProfileDirectory\(Token\)
Returns profile directory for a logon token

#### Parameters


  - Token :[PyHANDLE](#pyhandle)

    User token as returned by[win32security::LogonUser](win32security.md#win32securitylogonuser)

## [win32profile](#win32profile)\.LoadUserProfile

[PyHKEY](#pyhkey) =LoadUserProfile\(hToken, ProfileInfo\)
Loads user settings into registry

#### Parameters


  - hToken :[PyHANDLE](#pyhandle)

    Logon token as returned by[win32security::LogonUser](win32security.md#win32securitylogonuser),[win32security::OpenThreadToken](win32security.md#win32securityopenthreadtoken), etc

  - ProfileInfo :[PyPROFILEINFO](#pyprofileinfo)

    Dictionary representing a PROFILEINFO structure

#### Comments


SE\_BACKUP\_NAME and SE\_RESTORE\_NAME privs are required, but do not have to be enabled

#### Return Value
Returns a handle to user's registry key\.

## [win32profile](#win32profile)\.UnloadUserProfile

UnloadUserProfile\(Token, Profile\)
Unloads user profile loaded by[win32profile::LoadUserProfile](win32profile.md#win32profileloaduserprofile)

#### Parameters


  - Token :[PyHANDLE](#pyhandle)

    Logon token as returned by[win32security::LogonUser](win32security.md#win32securitylogonuser),[win32security::OpenProcessToken](win32security.md#win32securityopenprocesstoken), etc

  - Profile :[PyHKEY](#pyhkey)

    Registry handle as returned by[win32profile::LoadUserProfile](win32profile.md#win32profileloaduserprofile)