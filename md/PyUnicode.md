# PyUnicode

## PyUnicode Object



A Python object, representing a Unicode string\.

#### Comments


pywin32 uses the builtin Python Unicode object
In general, any pywin32/COM function documented as taking a 

PyUnicode parameter will also accept a Python string object, which will 

be automatically encoded using the MBCS encoding before being passed to the function\. 

Note that the reverse is generally \*not\* true - a function documented as accepting 

a string must be passed a string\.