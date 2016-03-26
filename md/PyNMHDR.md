# PyNMHDR

## PyNMHDR Object

A Python object, representing an NMHDR 

structure

#### Comments
Typically you create a PyNMHDR 

(via[win32help::NMHDR](win32help.md#win32helpnmhdr)) object, and set its properties. 

The object can then be passed to any function which takes an NMHDR 

object.

Contains information about a notification message.

#### Properties

  -  __int hwndFrom__ 
    Window handle to the control sending a message. 

??? 64-bit problem here ???

  -  __unsigned int idFrom__ 
    Identifier of the control sending a message.

  -  __unsigned int code__ 
    Notification code. This member can be a 

control-specific notification code or it can be one of the common 

notification codes.