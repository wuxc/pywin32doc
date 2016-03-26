# PyIDropTarget

## PyIDropTarget Object



Interface that acts as a target of OLE drag and drop operations

#### Methods


  - [DragEnter](PyIDropTarget.md#pyidroptargetdragenter)

    Called when an object is initially dragged into a window&nbsp;

  - [DragOver](PyIDropTarget.md#pyidroptargetdragover)

    Called as the dragged object moves over the window&nbsp;

  - [DragLeave](PyIDropTarget.md#pyidroptargetdragleave)

    Called as the object is dragged back out of the window&nbsp;

  - [Drop](PyIDropTarget.md#pyidroptargetdrop)

    Called when the object is dropped onto the window&nbsp;

## [PyIDropTarget](#pyidroptarget)\.DragEnter



int =DragEnter\(pDataObj, grfKeyState, pt, pdwEffect\)
Called when an object is initially dragged into a window

#### Parameters


  - pDataObj :[PyIDataObject](#pyidataobject)

    IDataObject interface that contains the object being dragged

  - grfKeyState : int

    Combination of win32con\.MK\_\* flags containing keyboard modifier state

  - pt : \(int, int\)

    \(x,y\) Screen coordinates of cursor

  - pdwEffect : int

    shellcon\.DROPEFFECT\_\* value

#### Return Value
Your implementation of this function should return a shellcon\.DROPEFFECT\_\* value indicating if the object can be accepted

## [PyIDropTarget](#pyidroptarget)\.DragLeave

DragLeave\(\)
Called as the object is dragged back out of the window

## [PyIDropTarget](#pyidroptarget)\.DragOver



int =DragOver\(grfKeyState, pt, pdwEffect\)
Called as the dragged object moves over the window

#### Parameters


  - grfKeyState : int

    Combination of win32con\.MK\_\* flags containing keyboard modifier state

  - pt : \(int, int\)

    \(x,y\) Screen coordinates of cursor

  - pdwEffect : int

    shellcon\.DROPEFFECT\_\* value

#### Return Value
Your implementation of this function should return a shellcon\.DROPEFFECT\_\* value indicating if the 

object can be accepted at the current position

## [PyIDropTarget](#pyidroptarget)\.Drop



int =Drop\(pDataObj, grfKeyState, pt, dwEffect\)
Called when the object is dropped onto the window

#### Parameters


  - pDataObj :[PyIDataObject](#pyidataobject)

    IDataObject interface containing the dropped object

  - grfKeyState : int

    Combination of win32con\.MK\_\* flags containing keyboard modifier state

  - pt : \(int, int\)

    \(x,y\) Screen coordinates of cursor

  - dwEffect : int

    shellcon\.DROPEFFECT\_\* value

#### Return Value
Your implementation of this function should return one of the shellcon\.DROPEFFECT\_\* values