# PyHHNTRACK

## PyHHNTRACK Object



A Python object, representing an HHNTRACK 

structure

#### Comments


Typically you create a PyHHNTRACK 

\(via[win32help::HHNTRACK](win32help.md#win32helphhntrack)\) object, and set its properties\. 

The object can then be passed to any function which takes an HHNTRACK 

object\.

 

This structure returns the file name of the current topic and a constant 

that specfies the user action that is about to occur, such as hiding the 

Navigation pane by clicking the Hide button on the toolbar\.

 

Used by
HHN\_TRACK


#### Properties

  - int action
    Specifies the action the user is about to take\. This 

is an HHACT\_ constant\.

  - NMHDR hdr
    Standard WM\_NOTIFY header\([win32help::NMHDR](win32help.md#win32helpnmhdr)\)\.

  - string curUrl
    A multi-byte, zero-terminated string that specifies 

the topic navigated to, or the name of the help window being created\.

  - HH\_WINTYPE winType
    A pointer to the current HH\_WINTYPE structure 

\([win32help::HH\_WINTYPE](win32help.md#win32helphh_wintype)\)\.