# PyCDockContext


## PyCDockContext Object

A class which encapsulates an MFC CDockContext object

#### Methods

  - [EndDrag](PyCDockContext.md#pycdockcontextenddrag)

    &nbsp;

  - [StartDrag](PyCDockContext.md#pycdockcontextstartdrag)

    &nbsp;

  - [EndResize](PyCDockContext.md#pycdockcontextendresize)

    &nbsp;

  - [StartResize](PyCDockContext.md#pycdockcontextstartresize)

    &nbsp;

  - [ToggleDocking](PyCDockContext.md#pycdockcontexttoggledocking)

    &nbsp;

#### Properties

  - x,y ptLast

    

  - left, top, right, bottom rectLast

    

  - cx, cy sizeLast

    

  - int bDitherLast

    

  - left, top, right, bottom rectDragHorz

    

  - left, top, right, bottom rectDragVert

    

  - left, top, right, bottom rectFrameDragHorz

    

  - left, top, right, bottom rectFrameDragVert

    

  - int dwDockStyle

    allowable dock styles for bar

  - int dwOverDockStyle

    style of dock that rect is over

  - int dwStyle

    style of control bar

  - int bFlip

    if shift key is down

  - int bForceFrame

    if ctrl key is down 

CDC\* m\_pDC;                 // where to draw during drag

  - int bDragging

    

  - int nHitTest

    

  - int uMRUDockID

    

  - left, top, right, bottom rectMRUDockPos

    

  - int dwMRUFloatStyle

    

  - x,y ptMRUFloatPos

    Sentinel


## [PyCDockContext](PyCDockContext.md#pycdockcontext)\.EndDrag

int = EndDrag\(\)



## [PyCDockContext](PyCDockContext.md#pycdockcontext)\.EndResize

int = EndResize\(\)



## [PyCDockContext](PyCDockContext.md#pycdockcontext)\.StartDrag

int = StartDrag\(pt\)

#### Parameters

  - pt : int, int

    


## [PyCDockContext](PyCDockContext.md#pycdockcontext)\.StartResize

int = StartResize\(hittest, pt

\)

#### Parameters

  - hittest : int

    

  - pt : int, int

    


## [PyCDockContext](PyCDockContext.md#pycdockcontext)\.ToggleDocking

int = ToggleDocking\(\)
