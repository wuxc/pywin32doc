# PyIDsObjectPicker


## PyIDsObjectPicker Object

A COM interface to ADSI's IDsObjectPicker interface\. 

Derived from [PyIUnknown](PyIUnknown.md)

#### Methods

  - [Initialize](PyIDsObjectPicker.md#pyidsobjectpickerinitialize)

    Initializes the IDsObjectPicker interface with information about the scopes, filters, and options used by the object picker dialog box\.&nbsp;

  - [InvokeDialog](PyIDsObjectPicker.md#pyidsobjectpickerinvokedialog)

    Displays a modal object picker dialog box and returns the user's selections\.&nbsp;


## [PyIDsObjectPicker](PyIDsObjectPicker.md#pyidsobjectpicker)\.Initialize

Initialize\(targetComputer, scopeInfos, options, attrNames\)
Initializes the IDsObjectPicker interface with information about the scopes, filters, and options used by the object picker dialog box\.

#### Parameters

  - targetComputer : [PyUnicode](PyUnicode.md)

    

  - scopeInfos : [PyDSOP\_SCOPE\_INIT\_INFOs](PyDSOP.md#pydsopscope_init_infos)

    

  - options=0 : int

    

  - attrNames=None : \[[PyUnicode](PyUnicode.md), \.\.\.\]

    


## [PyIDsObjectPicker](PyIDsObjectPicker.md#pyidsobjectpicker)\.InvokeDialog

[PyIDataObject](PyIDataObject.md) = InvokeDialog\(hwnd\)
Displays a modal object picker dialog box and returns the user's selections\.

#### Parameters

  - hwnd : int

    