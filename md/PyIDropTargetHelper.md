# PyIDropTargetHelper

## PyIDropTargetHelper Object

Description of the interface

#### Methods


  - [DragEnter](PyIDropTargetHelper.md#pyidroptargethelperdragenter)

    Description of DragEnter&nbsp;

  - [DragOver](PyIDropTargetHelper.md#pyidroptargethelperdragover)

    Description of DragOver&nbsp;

  - [DragLeave](PyIDropTargetHelper.md#pyidroptargethelperdragleave)

    Description of DragLeave&nbsp;

  - [Drop](PyIDropTargetHelper.md#pyidroptargethelperdrop)

    Description of Drop&nbsp;

## [PyIDropTargetHelper](#pyidroptargethelper)\.DragEnter

 **DragEnter\( *hwnd*  *, pDataObj*  *, pt*  *, dwEffect* ** \)
Description of DragEnter\.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to target window

  -  *pDataObj* :[PyIDataObject](#pyidataobject)

    Object that is dragged onto the window

  -  *pt* : \(int, int\)

    Coordinates where drag operation entered the window

  -  *dwEffect* : int

    One of shellcon\.DROPEFFECT\_\* values

## [PyIDropTargetHelper](#pyidroptargethelper)\.DragLeave

 **DragLeave\(** \)
Description of DragLeave\.

## [PyIDropTargetHelper](#pyidroptargethelper)\.DragOver

 **DragOver\( *hwnd*  *, pt*  *, pdwEffect* ** \)
Description of DragOver\.

#### Parameters


  -  *hwnd* : int

    

  -  *pt* : \(int, int\)

    Description for pt

  -  *pdwEffect* : int

    Description for pdwEffect

## [PyIDropTargetHelper](#pyidroptargethelper)\.Drop

 **Drop\( *pDataObj*  *, pt*  *, dwEffect* ** \)
Description of Drop\.

#### Parameters


  -  *pDataObj* :[PyIDataObject](#pyidataobject)

    Description for pDataObj

  -  *pt* : \(int, int\)

    Description for pt

  -  *dwEffect* : int

    Description for dwEffect