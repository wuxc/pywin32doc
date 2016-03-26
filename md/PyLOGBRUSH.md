# PyLOGBRUSH


## PyLOGBRUSH Object

Dict representing a LOGBRUSH struct as used with [win32gui::CreateBrushIndirect](win32gui.md#win32guicreatebrushindirect) and [win32gui::ExtCreatePen](win32gui.md#win32guiextcreatepen)

#### Win32 API References

  - Search for LOGBRUSH at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=LOGBRUSH.md), [google](http://www.google.com/search?q=LOGBRUSH.md) or [google groups](http://groups.google.com/groups?q=LOGBRUSH.md)\.

#### Properties

  - int Style

    Brush style, one of win32con\.BS\_\* values

  - int Color

    RGB color value\.  Can also be DIB\_PAL\_COLORS or DIB\_RGB\_COLORS if Style is BS\_DIBPATTERN or BS\_DIBPATTERNPT=

  - int/[PyHANDLE](PyHANDLE.md) Hatch

    For BS\_HATCH style, one of win32con\.HS\_\*\. Not used For BS\_SOLID or BS\_HOLLOW\. 

For a pattern brush, this should be a handle to a bitmap