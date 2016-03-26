# PyIDsObjectPicker

## PyIDsObjectPicker Object

A COM interface to ADSI's IDsObjectPicker interface.
Derived from[PyIUnknown](#pyiunknown)

#### Methods


  - [Initialize](PyIDsObjectPicker.md#pyidsobjectpickerinitialize)

    Initializes the IDsObjectPicker interface with information about the scopes, filters, and options used by the object picker dialog box.&nbsp;

  - [InvokeDialog](PyIDsObjectPicker.md#pyidsobjectpickerinvokedialog)

    Displays a modal object picker dialog box and returns the user's selections.&nbsp;

## [PyIDsObjectPicker](#pyidsobjectpicker).Initialize

 __Initialize( *targetComputer*  *, scopeInfos*  *, options*  *, attrNames* __ )
Initializes the IDsObjectPicker interface with information about the scopes, filters, and options used by the object picker dialog box.

#### Parameters


  -  *targetComputer* :[PyUnicode](#pyunicode)

    

  -  *scopeInfos* :[PyDSOP_SCOPE_INIT_INFOs](PyDSOP.md#pydsopscope_init_infos)

    

  -  *options=0* : int

    

  -  *attrNames=None* : [[PyUnicode](#pyunicode), ...]

    

## [PyIDsObjectPicker](#pyidsobjectpicker).InvokeDialog

[PyIDataObject](#pyidataobject)= __InvokeDialog( *hwnd* __ )
Displays a modal object picker dialog box and returns the user's selections.

#### Parameters


  -  *hwnd* : int

    