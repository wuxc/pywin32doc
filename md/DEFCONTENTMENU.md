# DEFCONTENTMENU

## DEFCONTENTMENU Object

A tuple representing a DEFCONTEXTMENU structure.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    

  -  *callback* : __PyIContextMenuCB__ 

    May be None 

bNoneOK */))

  -  *pidlFolder* : __PIDL__ 

    May be None

  -  *sf* :[PyIShellFolder](#pyishellfolder)

    The Shell data source object that is the parent of the child items specified in children. If parent is specified, this parameter can be NULL. 

bNoneOK */))

  -  *children* : [ __PIDL__ , ...]

    

  -  *unkAssocInfo* :[PyIUnknown](#pyiunknown)

    May be None 

bNoneOK */))