
## [win32profile](#README.md#win32profile).CreateEnvironmentBlock

dict = **CreateEnvironmentBlock( *Token*  *, Inherit* ** )
Retrieves environment variables for a user

#### Parameters


     *Token* :[PyHANDLE](#README.md#PyHANDLE)

    User token as returned by[win32security::LogonUser](#win32security.md#win32securityLogonUser), use None to retrieve system variables only

     *Inherit* : boolean

    Indicates if environment of current process should be inherited

## [win32profile](#README.md#win32profile).DeleteProfile

 **DeleteProfile( *SidString*  *, ProfilePath*  *, ComputerName* ** )
Remove profile for a user identified by string SID from specified machine.

#### Parameters


     *SidString* :[PyUnicode](#README.md#PyUnicode)

    String representation of user's Sid.  See[win32security::ConvertSidToStringSid](#win32security.md#win32securityConvertSidToStringSid).

     *ProfilePath=None* :[PyUnicode](#README.md#PyUnicode)

    Profile directory, value queried from registry if not specified

     *ComputerName=None* :[PyUnicode](#README.md#PyUnicode)

    Name of computer from which to delete profile, local machine assumed if not specified

## [win32profile](#README.md#win32profile).ExpandEnvironmentStringsForUser

[PyUnicode](#README.md#PyUnicode)= **ExpandEnvironmentStringsForUser( *Token*  *, Src* ** )
Replaces environment variables in a string with per-user values

#### Parameters


     *Token* :[PyHANDLE](#README.md#PyHANDLE)

    The logon token for a user.  Use None for system variables.

     *Src* :[PyUnicode](#README.md#PyUnicode)

    String containing environment variables enclosed in % signs

## [win32profile](#README.md#win32profile).GetAllUsersProfileDirectory

[PyUnicode](#README.md#PyUnicode)= **GetAllUsersProfileDirectory(** )
Retrieve All Users profile path

## [win32profile](#README.md#win32profile).GetDefaultUserProfileDirectory

[PyUnicode](#README.md#PyUnicode)= **GetDefaultUserProfileDirectory(** )
Retrieve Default user profile

## [win32profile](#README.md#win32profile).GetEnvironmentStrings

dict = **GetEnvironmentStrings(** )
Retrieves environment variables for current process

## [win32profile](#README.md#win32profile).GetProfileType

int = **GetProfileType(** )
Returns type of current user's profile

#### Return Value
Returns a combination of PT_* flags

## [win32profile](#README.md#win32profile).GetProfilesDirectory

[PyUnicode](#README.md#PyUnicode)= **GetProfilesDirectory(** )
Retrieves directory where user profiles are stored

## [win32profile](#README.md#win32profile).GetUserProfileDirectory

[PyUnicode](#README.md#PyUnicode)= **GetUserProfileDirectory( *Token* ** )
Returns profile directory for a logon token

#### Parameters


     *Token* :[PyHANDLE](#README.md#PyHANDLE)

    User token as returned by[win32security::LogonUser](#win32security.md#win32securityLogonUser)

## [win32profile](#README.md#win32profile).LoadUserProfile

[PyHKEY](#README.md#PyHKEY)= **LoadUserProfile( *hToken*  *, ProfileInfo* ** )
Loads user settings into registry

#### Parameters


     *hToken* :[PyHANDLE](#README.md#PyHANDLE)

    Logon token as returned by[win32security::LogonUser](#win32security.md#win32securityLogonUser),[win32security::OpenThreadToken](#win32security.md#win32securityOpenThreadToken), etc

     *ProfileInfo* :[PyPROFILEINFO](#README.md#PyPROFILEINFO)

    Dictionary representing a PROFILEINFO structure

#### Comments
SE_BACKUP_NAME and SE_RESTORE_NAME privs are required, but do not have to be enabled

#### Return Value
Returns a handle to user's registry key.

## [win32profile](#README.md#win32profile).UnloadUserProfile

 **UnloadUserProfile( *Token*  *, Profile* ** )
Unloads user profile loaded by[win32profile::LoadUserProfile](#win32profile.md#win32profileLoadUserProfile)

#### Parameters


     *Token* :[PyHANDLE](#README.md#PyHANDLE)

    Logon token as returned by[win32security::LogonUser](#win32security.md#win32securityLogonUser),[win32security::OpenProcessToken](#win32security.md#win32securityOpenProcessToken), etc

     *Profile* :[PyHKEY](#README.md#PyHKEY)

    Registry handle as returned by[win32profile::LoadUserProfile](#win32profile.md#win32profileLoadUserProfile)