# PyNETRESOURCE

## PyNETRESOURCE Object

A Python object that encapsulates a Win32 NETRESOURCE structure.

#### Properties

  -  __integer dwScope__ 
    

  -  __integer dwType__ 
    

  -  __integer dwDisplayType__ 
    

  -  __integer dwUsage__ 
    

  -  __string localName__ 
    

  -  __string remoteName__ 
    

  -  __string comment__ 
    

  -  __string provider__ 
    

#### Comments
Note that in pywin32-212 and earlier, the string attributes 

were always strings, but empty strings when the underlying Windows 

structure had NULL.  On later pywin32 builds, these string attributes will 

return None in such cases.