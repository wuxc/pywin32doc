# PyPROFILEINFO


## PyPROFILEINFO Object

Dictionary containing data to fill a PROFILEINFO struct, to be passed to [win32profile::LoadUserProfile](win32profile.md#win32profileloaduserprofile)\. 

UserName is only required member\.

#### Win32 API References

  - Search for PROFILEINFO at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=PROFILEINFO.md), [google](http://www.google.com/search?q=PROFILEINFO.md) or [google groups](http://groups.google.com/groups?q=PROFILEINFO.md)\.

#### Properties

  - [PyUnicode](PyUnicode.md) UserName

    Name of user for which to load profile

  - int Flags

    Combination of PI\_\* flags

  - [PyUnicode](PyUnicode.md) ProfilePath

    Path to roaming profile, can be None\.  Use [win32net::NetUserGetInfo](win32net.md#win32netnetusergetinfo) to retrieve user's profile path

  - [PyUnicode](PyUnicode.md) DefaultPath

    Path to Default user profile, can be None

  - [PyUnicode](PyUnicode.md) ServerName

    Domain controller, can be None

  - [PyUnicode](PyUnicode.md) PolicyPath

    Location of policy file, can be None

  - [PyHKEY](PyHKEY.md) Profile

    Handle to root of user's registry key\. This member is output\.