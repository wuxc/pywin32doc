# PyHHNTRACK

## PyHHNTRACK Object

A Python object, representing an HHNTRACK 

structure

#### Comments
Typically you create a PyHHNTRACK 

(via[win32help::HHNTRACK](win32help.md#win32helphhntrack)) object, and set its properties. 

The object can then be passed to any function which takes an HHNTRACK 

object.

This structure returns the file name of the current topic and a constant 

that specfies the user action that is about to occur, such as hiding the 

Navigation pane by clicking the Hide button on the toolbar.

Used by
 __HHN_TRACK__ 


#### Properties

  -  __int action__ 
    Specifies the action the user is about to take. This 

is an HHACT_ constant.

  -  __NMHDR hdr__ 
    Standard WM_NOTIFY header([win32help::NMHDR](win32help.md#win32helpnmhdr)).

  -  __string curUrl__ 
    A multi-byte, zero-terminated string that specifies 

the topic navigated to, or the name of the help window being created.

  -  __HH_WINTYPE winType__ 
    A pointer to the current HH_WINTYPE structure 

([win32help::HH_WINTYPE](win32help.md#win32helphh_wintype)).