# PyHHN


## PyHHN\_NOTIFY Object

A Python object, representing an HHN\_NOTIFY 

structure

#### Comments

Typically you create a PyHHN\_NOTIFY 

\(via [win32help::HHN\_NOTIFY](win32help.md#win32helphhn_notify)\) object, and set its properties\. 

The object can then be passed to any function which takes an HHN\_NOTIFY 

object\.
 

 

Use this structure to return the file name of the topic that has been 

navigated to, or to return the window type name of the help window that 

has been created\.
 

 

Used by
 

HHN\_NAVCOMPLETE

 

HHN\_WINDOW\_CREATE

#### Properties

  - NMHDR hdr

    Standard WM\_NOTIFY header\.\([win32help::NMHDR](win32help.md#win32helpnmhdr)\)

  - string url

    A multi-byte, zero-terminated string that specifies 

the topic navigated to, or the name of the help window being created\.