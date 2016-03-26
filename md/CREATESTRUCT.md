# CREATESTRUCT

## CREATESTRUCT Object

A representation of a Windows CREATESTRUCT structure.

#### Parameters


  -  *createParams* : int

    

  -  *hInstance* : int

    

  -  *hMenu* : int

    

  -  *hwndParent* : int

    

  -  *cy, cx, y, x* : (int, int, int, int)

    

  -  *style* : int

    

  -  *lpszName* : int

    A string cast to a long.

  -  *lpszClass* : int

    A string cast to a long!?

  -  *dwExStyle* : int

    

#### Comments
Note that the strings are passed as longs, which are there address 

in memory.  This is due to the internal mechanics of passing this structure around.