# PyResourceId

## PyResourceId Object

Identifies a resource or function in a module\. 

This can be a WORD-sized integer value \(0-65536\), or string/unicode 

depending on whether the \*A or \*W API function is to be called\. 

Class atoms as used with[win32gui::CreateWindow](win32gui.md#win32guicreatewindow)are also treated 

as resource ids since they can also be represented by a name or WORD id\. 

When passing resource names and types as strings, they are usually formatted 

as a pound sign followed by decimal form of the id\.  \('\#42' for example\)