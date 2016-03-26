# PyWNDCLASS

## PyWNDCLASS Object



A Python object, representing an WNDCLASS structure

#### Comments


Typically you create a PyWNDCLASS object, and set its properties\. 

The object can then be passed to any function which takes an WNDCLASS object

#### Properties

  - integer style
    

  - integer cbWndExtra
    

  - integer hInstance
    

  - integer hIcon
    

  - integer hCursor
    

  - integer hbrBackground
    These 3 handled manually in PyWNDCLASS::getattro/setattro\.  The pymeth below is used as an 

end tag, so these props will be lost if below it

  - string/[PyUnicode](#pyunicode) lpszMenuName
    

  - string/[PyUnicode](#pyunicode) lpszClassName
    

  - function lpfnWndProc
    

#### Methods


  - [SetDialogProc](PyWNDCLASS.md#pywndclasssetdialogproc)

    Sets the WNDCLASS to be for a dialog box\.&nbsp;

## [PyWNDCLASS](#pywndclass)\.SetDialogProc

SetDialogProc\(\)
Sets the WNDCLASS to be for a dialog box