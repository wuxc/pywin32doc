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


## [PyIDropTargetHelper](PyIDropTargetHelper.md#pyidroptargethelper)\.DragEnter

DragEnter\(hwnd, pDataObj, pt, dwEffect\)
Description of DragEnter\.

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Handle to target window

  - pDataObj : [PyIDataObject](PyIDataObject.md)

    Object that is dragged onto the window

  - pt : \(int, int\)

    Coordinates where drag operation entered the window

  - dwEffect : int

    One of shellcon\.DROPEFFECT\_\* values


## [PyIDropTargetHelper](PyIDropTargetHelper.md#pyidroptargethelper)\.DragLeave

DragLeave\(\)
Description of DragLeave\.


## [PyIDropTargetHelper](PyIDropTargetHelper.md#pyidroptargethelper)\.DragOver

DragOver\(hwnd, pt, pdwEffect\)
Description of DragOver\.

#### Parameters

  - hwnd : int

    

  - pt : \(int, int\)

    Description for pt

  - pdwEffect : int

    Description for pdwEffect


## [PyIDropTargetHelper](PyIDropTargetHelper.md#pyidroptargethelper)\.Drop

Drop\(pDataObj, pt, dwEffect\)
Description of Drop\.

#### Parameters

  - pDataObj : [PyIDataObject](PyIDataObject.md)

    Description for pDataObj

  - pt : \(int, int\)

    Description for pt

  - dwEffect : int

    Description for dwEffect