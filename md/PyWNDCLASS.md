# PyWNDCLASS

## PyWNDCLASS Object

A Python object, representing an WNDCLASS structure

#### Comments
Typically you create a PyWNDCLASS object, and set its properties. 

The object can then be passed to any function which takes an WNDCLASS object

#### Properties

  -  __integer style__ 
    

  -  __integer cbWndExtra__ 
    

  -  __integer hInstance__ 
    

  -  __integer hIcon__ 
    

  -  __integer hCursor__ 
    

  -  __integer hbrBackground__ 
    These 3 handled manually in PyWNDCLASS::getattro/setattro.  The pymeth below is used as an 

end tag, so these props will be lost if below it

  -  __string/[PyUnicode](#pyunicode)lpszMenuName__ 
    

  -  __string/[PyUnicode](#pyunicode)lpszClassName__ 
    

  -  __function lpfnWndProc__ 
    

#### Methods


  - [SetDialogProc](PyWNDCLASS.md#pywndclasssetdialogproc)

    Sets the WNDCLASS to be for a dialog box.&nbsp;

## [PyWNDCLASS](#pywndclass).SetDialogProc

 __SetDialogProc(__ )
Sets the WNDCLASS to be for a dialog box