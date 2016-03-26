# PyHHN

## PyHHN_NOTIFY Object

A Python object, representing an HHN_NOTIFY 

structure

#### Comments
Typically you create a PyHHN_NOTIFY 

(via[win32help::HHN_NOTIFY](win32help.md#win32helphhn_notify)) object, and set its properties. 

The object can then be passed to any function which takes an HHN_NOTIFY 

object.

Use this structure to return the file name of the topic that has been 

navigated to, or to return the window type name of the help window that 

has been created.

Used by
 __HHN_NAVCOMPLETE__ 
 __HHN_WINDOW_CREATE__ 


#### Properties

  -  __NMHDR hdr__ 
    Standard WM_NOTIFY header.([win32help::NMHDR](win32help.md#win32helpnmhdr))

  -  __string url__ 
    A multi-byte, zero-terminated string that specifies 

the topic navigated to, or the name of the help window being created.