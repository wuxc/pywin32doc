# error

## error Object



An exception raised when a win32 error occurs

#### Comments


This error is defined in the pywintypes module, but most 

of the win32 modules expose this error object via their own 

error attribute - eg, win32api\.error is pywintypes\.error is 

win32gui\.error\.


This exception is derived from the standard Python Exception object\.


Instances of these exception can be accessed via indexing 

or via attribute access\.  Attribute access is more forwards 

compatible with Python 3, so is recommended\.


See also[com\_error](com.md#comerror)

#### Items


  - \[0\]int : winerror

    The windows error code\.

  - \[1\]string : funcname

    The name of the windows function that failed\.

  - \[2\]string : strerror

    The error message\.