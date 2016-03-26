# PyLOGBRUSH

## PyLOGBRUSH Object

Dict representing a LOGBRUSH struct as used with[win32gui::CreateBrushIndirect](win32gui.md#win32guicreatebrushindirect)and[win32gui::ExtCreatePen](win32gui.md#win32guiextcreatepen)

#### Win32 API References


  - Search for *LOGBRUSH* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=logbrush),[google](#http://www.google.com/search?q=logbrush)or[google groups](#http://groups.google.com/groups?q=logbrush).

#### Properties

  -  __int Style__ 
    Brush style, one of win32con.BS_* values

  -  __int Color__ 
    RGB color value.  Can also be DIB_PAL_COLORS or DIB_RGB_COLORS if Style is BS_DIBPATTERN or BS_DIBPATTERNPT=

  -  __int/[PyHANDLE](#pyhandle)Hatch__ 
    For BS_HATCH style, one of win32con.HS_*. Not used For BS_SOLID or BS_HOLLOW. 

For a pattern brush, this should be a handle to a bitmap