# PyPROFILEINFO

## PyPROFILEINFO Object

Dictionary containing data to fill a PROFILEINFO struct, to be passed to[win32profile::LoadUserProfile](win32profile.md#win32profileloaduserprofile). 

UserName is only required member.

#### Win32 API References


  - Search for *PROFILEINFO* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=profileinfo),[google](#http://www.google.com/search?q=profileinfo)or[google groups](#http://groups.google.com/groups?q=profileinfo).

#### Properties

  -  __[PyUnicode](#pyunicode)UserName__ 
    Name of user for which to load profile

  -  __int Flags__ 
    Combination of PI_* flags

  -  __[PyUnicode](#pyunicode)ProfilePath__ 
    Path to roaming profile, can be None.  Use[win32net::NetUserGetInfo](win32net.md#win32netnetusergetinfo)to retrieve user's profile path

  -  __[PyUnicode](#pyunicode)DefaultPath__ 
    Path to Default user profile, can be None

  -  __[PyUnicode](#pyunicode)ServerName__ 
    Domain controller, can be None

  -  __[PyUnicode](#pyunicode)PolicyPath__ 
    Location of policy file, can be None

  -  __[PyHKEY](#pyhkey)Profile__ 
    Handle to root of user's registry key. This member is output.