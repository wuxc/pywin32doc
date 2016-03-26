# PyPROFILEINFO

## PyPROFILEINFO Object

Dictionary containing data to fill a PROFILEINFO struct, to be passed to[win32profile::LoadUserProfile](win32profile.md#win32profileloaduserprofile)\. 

UserName is only required member\.

#### Win32 API References


  - Search for *PROFILEINFO* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=profileinfo),[google](#http://www.google.com/search?q=profileinfo)or[google groups](#http://groups.google.com/groups?q=profileinfo)\.

#### Properties

  -  **[PyUnicode](#pyunicode)UserName** 
    Name of user for which to load profile

  -  **int Flags** 
    Combination of PI\_\* flags

  -  **[PyUnicode](#pyunicode)ProfilePath** 
    Path to roaming profile, can be None\.  Use[win32net::NetUserGetInfo](win32net.md#win32netnetusergetinfo)to retrieve user's profile path

  -  **[PyUnicode](#pyunicode)DefaultPath** 
    Path to Default user profile, can be None

  -  **[PyUnicode](#pyunicode)ServerName** 
    Domain controller, can be None

  -  **[PyUnicode](#pyunicode)PolicyPath** 
    Location of policy file, can be None

  -  **[PyHKEY](#pyhkey)Profile** 
    Handle to root of user's registry key\. This member is output\.