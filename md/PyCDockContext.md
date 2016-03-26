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

  -  __x,y ptLast__ 
    

  -  __left, top, right, bottom rectLast__ 
    

  -  __cx, cy sizeLast__ 
    

  -  __int bDitherLast__ 
    

  -  __left, top, right, bottom rectDragHorz__ 
    

  -  __left, top, right, bottom rectDragVert__ 
    

  -  __left, top, right, bottom rectFrameDragHorz__ 
    

  -  __left, top, right, bottom rectFrameDragVert__ 
    

  -  __int dwDockStyle__ 
    allowable dock styles for bar

  -  __int dwOverDockStyle__ 
    style of dock that rect is over

  -  __int dwStyle__ 
    style of control bar

  -  __int bFlip__ 
    if shift key is down

  -  __int bForceFrame__ 
    if ctrl key is down 

CDC* m_pDC;                 // where to draw during drag

  -  __int bDragging__ 
    

  -  __int nHitTest__ 
    

  -  __int uMRUDockID__ 
    

  -  __left, top, right, bottom rectMRUDockPos__ 
    

  -  __int dwMRUFloatStyle__ 
    

  -  __x,y ptMRUFloatPos__ 
    Sentinel

## [PyCDockContext](#pycdockcontext).EndDrag

int = __EndDrag(__ )


## [PyCDockContext](#pycdockcontext).EndResize

int = __EndResize(__ )


## [PyCDockContext](#pycdockcontext).StartDrag

int = __StartDrag( *pt* __ )


#### Parameters


  -  *pt* : int, int

    

## [PyCDockContext](#pycdockcontext).StartResize

int = __StartResize( *hittest*  *, pt* __ )


#### Parameters


  -  *hittest* : int

    

  -  *pt* : int, int

    

## [PyCDockContext](#pycdockcontext).ToggleDocking

int = __ToggleDocking(__ )
