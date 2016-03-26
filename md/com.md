# com



## com\_error Object

An exception raised when a COM exception occurs\.

#### Comments
This error is defined in the pywintypes module, but is 

also available via pythoncom\.com\_error\.
This exception is derived from the standard Python Exception object\.
Instances of these exception can be accessed via indexing 

or via attribute access\.  Attribute access is more forwards 

compatible with Python 3, so is recommended\.
See also[error](#error)

#### Items


  - \[0\] *int* : hresult

    The COM hresult

  - \[1\] *string* : strerror

    The error message

  - \[2\] *None/tuple* : excepinfo

    An optional EXCEPINFO tuple\.

  - \[3\] *None/int* : argerror

    The index of the argument in error, or \(usually\) None or -1


