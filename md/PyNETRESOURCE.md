# PyNETRESOURCE


## PyNETRESOURCE Object

A Python object that encapsulates a Win32 NETRESOURCE structure\.

#### Properties

  - integer dwScope

    

  - integer dwType

    

  - integer dwDisplayType

    

  - integer dwUsage

    

  - string localName

    

  - string remoteName

    

  - string comment

    

  - string provider

    

#### Comments

Note that in pywin32-212 and earlier, the string attributes 

were always strings, but empty strings when the underlying Windows 

structure had NULL\.  On later pywin32 builds, these string attributes will 

return None in such cases\.