# PyBITMAP

## PyBITMAP Object

A Python object, representing an PyBITMAP structure

#### Comments
Typically you get one of these from GetObject.  Note that currently 

the bitmap bits are not exposed via this type - but the value of the 

pointer is.  You can use the struct and win32gui functions to unpack 

these bits manually if you really need them. 

Note that you are still responsible for the life of the win32 bitmap object. 

The object can then be passed to any function which takes an BITMAP object

#### Properties

  -  __integer bmType__ 
    

  -  __integer bmWidth__ 
    

  -  __integer bmHeight__ 
    

  -  __integer bmWidthBytes__ 
    

  -  __integer bmPlanes__ 
    

  -  __integer__ 
    