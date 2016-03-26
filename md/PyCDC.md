# PyCDC

## PyCDC Object

A Device Context.  Encapsulates an MFC __CDC__ class.

#### Methods


  - [AbortDoc](PyCDC.md#pycdcabortdoc)

    Aborts a print job&nbsp;

  - [Arc](PyCDC.md#pycdcarc)

    Draws an arc.&nbsp;

  - [BeginPath](PyCDC.md#pycdcbeginpath)

    Opens a path bracket in the device context&nbsp;

  - [BitBlt](PyCDC.md#pycdcbitblt)

    Copies a bitmap&nbsp;

  - [Chord](PyCDC.md#pycdcchord)

    Draws a chord.&nbsp;

  - [CreateCompatibleDC](PyCDC.md#pycdccreatecompatibledc)

    Creates a memory DC compatible with this DC.&nbsp;

  - [CreatePrinterDC](PyCDC.md#pycdccreateprinterdc)

    Creates a device context for a specific printer&nbsp;

  - [DeleteDC](PyCDC.md#pycdcdeletedc)

    Deletes all resources associated with a device context.&nbsp;

  - [DPtoLP](PyCDC.md#pycdcdptolp)

    Convert from device points to logical points.&nbsp;

  - [Draw3dRect](PyCDC.md#pycdcdraw3drect)

    Draws a three-dimensional rectangle.&nbsp;

  - [DrawFocusRect](PyCDC.md#pycdcdrawfocusrect)

    Draws a rectangle in the style used to indicate the rectangle has focus&nbsp;

  - [DrawFrameControl](PyCDC.md#pycdcdrawframecontrol)

    Draws a frame control of the specified type and style.&nbsp;

  - [DrawIcon](PyCDC.md#pycdcdrawicon)

    Draws an icon on the DC.&nbsp;

  - [DrawText](PyCDC.md#pycdcdrawtext)

    Formats text in the given rectangle&nbsp;

  - [Ellipse](PyCDC.md#pycdcellipse)

    Draws an Ellipse.&nbsp;

  - [EndDoc](PyCDC.md#pycdcenddoc)

    Finishes spooling the document and starts printing it&nbsp;

  - [EndPage](PyCDC.md#pycdcendpage)

    Finishes a page on a printer DC&nbsp;

  - [EndPath](PyCDC.md#pycdcendpath)

    Closes a path bracket and selects the path defined by the bracket into the specified device context&nbsp;

  - [ExtTextOut](PyCDC.md#pycdcexttextout)

    Writes text to the DC.&nbsp;

  - [FillPath](PyCDC.md#pycdcfillpath)

    Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode.&nbsp;

  - [FillRect](PyCDC.md#pycdcfillrect)

    Fills a given rectangle with the specified brush&nbsp;

  - [FillSolidRect](PyCDC.md#pycdcfillsolidrect)

    Fills the given rectangle with the specified solid color.&nbsp;

  - [FrameRect](PyCDC.md#pycdcframerect)

    Draws a border around the rectangle specified by rect&nbsp;

  - [GetBrushOrg](PyCDC.md#pycdcgetbrushorg)

    Retrieves the origin (in device units) of the brush currently selected for the device context.&nbsp;

  - [GetClipBox](PyCDC.md#pycdcgetclipbox)

    Retrives the current clipping region.&nbsp;

  - [GetCurrentPosition](PyCDC.md#pycdcgetcurrentposition)

    Retrieves the current position (in logical coordinates).&nbsp;

  - [GetDeviceCaps](PyCDC.md#pycdcgetdevicecaps)

    Retrieves current device capabilities.&nbsp;

  - [GetHandleAttrib](PyCDC.md#pycdcgethandleattrib)

    Retrieves the handle of the attribute device context.&nbsp;

  - [GetHandleOutput](PyCDC.md#pycdcgethandleoutput)

    Retrieves the handle of the output device context.&nbsp;

  - [GetMapMode](PyCDC.md#pycdcgetmapmode)

    Gets the mapping mode for the device context.&nbsp;

  - [GetNearestColor](PyCDC.md#pycdcgetnearestcolor)

    Returns the closest color a device can map.&nbsp;

  - [GetPixel](PyCDC.md#pycdcgetpixel)

    Returns the value of a pixel at a location&nbsp;

  - [GetSafeHdc](PyCDC.md#pycdcgetsafehdc)

    Returns the underlying windows handle for the DC object.&nbsp;

  - [GetTextExtent](PyCDC.md#pycdcgettextextent)

    Calculates the size of the string.&nbsp;

  - [GetTextExtentPoint](PyCDC.md#pycdcgettextextentpoint)

    Alias for GetTextExtent - Calculates the size of the string.&nbsp;

  - [GetTextFace](PyCDC.md#pycdcgettextface)

    Retrieves the name of the current font.&nbsp;

  - [GetTextMetrics](PyCDC.md#pycdcgettextmetrics)

    Retrieves the metrics for the current font.&nbsp;

  - [GetViewportExt](PyCDC.md#pycdcgetviewportext)

    Gets the viewport extent of the device context&nbsp;

  - [GetViewportOrg](PyCDC.md#pycdcgetviewportorg)

    Gets the viewport origin of the device context&nbsp;

  - [GetWindowExt](PyCDC.md#pycdcgetwindowext)

    Gets the window extent of the device context&nbsp;

  - [GetWindowOrg](PyCDC.md#pycdcgetwindoworg)

    Retrieves the x- and y-coordinates of the origin of the window associated with the device context.&nbsp;

  - [IntersectClipRect](PyCDC.md#pycdcintersectcliprect)

    Creates a new clipping region by forming the intersection of the current region and the rectangle specified&nbsp;

  - [IsPrinting](PyCDC.md#pycdcisprinting)

    Returns 1 if the DC is currently printing, else 0&nbsp;

  - [LineTo](PyCDC.md#pycdclineto)

    Draws a line to a specified point.&nbsp;

  - [LPtoDP](PyCDC.md#pycdclptodp)

    Convert from logical points to device points&nbsp;

  - [MoveTo](PyCDC.md#pycdcmoveto)

    Moves the current position to a specifed point.&nbsp;

  - [OffsetWindowOrg](PyCDC.md#pycdcoffsetwindoworg)

    Modifies the coordinates of the window origin relative to the coordinates of the current window origin.&nbsp;

  - [OffsetViewportOrg](PyCDC.md#pycdcoffsetviewportorg)

    Modifies the coordinates of the viewport origin relative to the coordinates of the current viewport origin&nbsp;

  - [PatBlt](PyCDC.md#pycdcpatblt)

    Creates a bit pattern on the device.&nbsp;

  - [Pie](PyCDC.md#pycdcpie)

    Draws a pie shape with specific starting and ending points in a rectangle&nbsp;

  - [PolyBezier](PyCDC.md#pycdcpolybezier)

    Draws one or more Bezier splines.&nbsp;

  - [Polygon](PyCDC.md#pycdcpolygon)

    Draws an Polygon.&nbsp;

  - [Polyline](PyCDC.md#pycdcpolyline)

    Draws a Polyline.&nbsp;

  - [RealizePalette](PyCDC.md#pycdcrealizepalette)

    Maps palette entries in the current logical palette to the system palette.&nbsp;

  - [Rectangle](PyCDC.md#pycdcrectangle)

    Draws a rectangle using the current pen. The interior of the rectangle is filled using the current brush.&nbsp;

  - [RectVisible](PyCDC.md#pycdcrectvisible)

    Determines if a rectangle is currently visisble in the viewport.&nbsp;

  - [RestoreDC](PyCDC.md#pycdcrestoredc)

    Restores a saved DC.&nbsp;

  - [SaveDC](PyCDC.md#pycdcsavedc)

    Saves a DC.&nbsp;

  - [ScaleWindowExt](PyCDC.md#pycdcscalewindowext)

    Modifies the window extents relative to the current values.&nbsp;

  - [ScaleViewportExt](PyCDC.md#pycdcscaleviewportext)

    Modifies the viewport extents relative to the current values.&nbsp;

  - [SelectClipRgn](PyCDC.md#pycdcselectcliprgn)

    Selects the given region as the current clipping region for the device context&nbsp;

  - [SelectObject](PyCDC.md#pycdcselectobject)

    Selects an object into the DC.&nbsp;

  - [SelectObject](PyCDC.md#pycdcselectobject)

    Selects the logical palette.&nbsp;

  - [SetBkColor](PyCDC.md#pycdcsetbkcolor)

    Sets the background color.&nbsp;

  - [SetBkMode](PyCDC.md#pycdcsetbkmode)

    Sets the background mode.&nbsp;

  - [SetBrushOrg](PyCDC.md#pycdcsetbrushorg)

    Specifies the origin that GDI will assign to the next brush that the application selects into the device context.&nbsp;

  - [SetGraphicsMode](PyCDC.md#pycdcsetgraphicsmode)

    Sets the graphics mode for the specified device context&nbsp;

  - [SetMapMode](PyCDC.md#pycdcsetmapmode)

    Sets the device mapping mode.&nbsp;

  - [SetPixel](PyCDC.md#pycdcsetpixel)

    Set a pixel to a color&nbsp;

  - [SetPolyFillMode](PyCDC.md#pycdcsetpolyfillmode)

    Sets the polygon-filling mode.&nbsp;

  - [SetROP2](PyCDC.md#pycdcsetrop2)

    Sets the current drawing mode.&nbsp;

  - [SetTextAlign](PyCDC.md#pycdcsettextalign)

    Sets the text alignment.&nbsp;

  - [SetTextColor](PyCDC.md#pycdcsettextcolor)

    Sets the text foreground color.&nbsp;

  - [SetWindowExt](PyCDC.md#pycdcsetwindowext)

    Sets the extents of the window.&nbsp;

  - [SetWindowOrg](PyCDC.md#pycdcsetwindoworg)

    Sets the window origin of the device context&nbsp;

  - [SetViewportExt](PyCDC.md#pycdcsetviewportext)

    Sets the extents of the window's viewport.&nbsp;

  - [SetViewportOrg](PyCDC.md#pycdcsetviewportorg)

    Sets the viewport origin of the device context&nbsp;

  - [SetWorldTransform](PyCDC.md#pycdcsetworldtransform)

    sets a two-dimensional linear transformation between world space and page space for the specified device context.&nbsp;

  - [StartDoc](PyCDC.md#pycdcstartdoc)

    Starts spooling a document to a printer DC&nbsp;

  - [StartPage](PyCDC.md#pycdcstartpage)

    Starts a new page on a printer DC&nbsp;

  - [StretchBlt](PyCDC.md#pycdcstretchblt)

    Copies a bitmap from the source device context to this device context.&nbsp;

  - [StrokeAndFillPath](PyCDC.md#pycdcstrokeandfillpath)

    Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush. The device context must contain a closed path.&nbsp;

  - [StrokePath](PyCDC.md#pycdcstrokepath)

    Renders the specified path by using the current pen.&nbsp;

  - [TextOut](PyCDC.md#pycdctextout)

    Writes text to the DC.&nbsp;

## [PyCDC](#pycdc).AbortDoc

 __AbortDoc(__ )
Aborts a print job

## [PyCDC](#pycdc).Arc

 __Arc( *rect*  *, pointStart*  *, pointEnd* __ )
Draws an eliptical arc.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    Specifies the ellipse's bounding rectangle

  -  *pointStart* : (x,y)

    Specifies the x- and y-coordinates 

of the point that defines the arc's starting point (in logical units). 

This point does not have to lie exactly on the arc.

  -  *pointEnd* : (x,y)

    Specifies the x- and y-coordinates 

of the point that defines the arc's ending point (in logical units). 

This point does not have to lie exactly on the arc.

#### Comments
The arc drawn by using the function is a segment of the ellipse defined by the specified bounding rectangle. 

The actual starting point of the arc is the point at which a ray drawn 

from the center of the bounding rectangle through the specified starting 

point intersects the ellipse. The actual ending point of the arc is the 

point at which a ray drawn from the center of the bounding rectangle through 

the specified ending point intersects the ellipse. The arc is drawn in a 

counterclockwise direction. Since an arc is not a closed figure, it is 

not filled. Both the width and height of the rectangle must be greater 

than 2 units and less than 32,767 units.

#### MFC References


  - CDC::Arc

#### Return Value
Always none.  If the function fails, an exception is raised.

## [PyCDC](#pycdc).BeginPath

 __BeginPath(__ )
Opens a path bracket in the device context

## [PyCDC](#pycdc).BitBlt

 __BitBlt( *destPos*  *, size*  *, dc*  *, srcPos*  *, rop* __ )
Copies a bitmap from the source device context to this device context.

#### Parameters


  -  *destPos* : (x,y)-ints

    The logical x,y coordinates of the upper-left corner of the destination rectangle.

  -  *size* : (width, height)-ints

    Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

  -  *dc* :[PyCDC](#pycdc)

    Specifies the PyCDC object from which the bitmap will be copied. It must be None if rop specifies a raster operation that does not include a source.

  -  *srcPos* : (xSrc, ySrc)-ints

    Specifies the logical x,y coordinates of the upper-left corner of the source bitmap.

  -  *rop* : int

    Specifies the raster operation to be performed. See the win32 api documentation for details.

#### MFC References


  - CDC::BitBlt

## [PyCDC](#pycdc).Chord

 __Chord( *rect*  *, pointStart*  *, pointEnd* __ )
Draws a chord.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    Specifies the ellipse's bounding rectangle

  -  *pointStart* : (x,y)

    Specifies the x- and y-coordinates 

of the point that defines the arc's starting point (in logical units). 

This point does not have to lie exactly on the arc.

  -  *pointEnd* : (x,y)

    Specifies the x- and y-coordinates 

of the point that defines the arc's ending point (in logical units). 

This point does not have to lie exactly on the arc.

#### Comments
Draws a chord (a closed figure bounded by the intersection 

of an ellipse and a line segment). The rect parameter specify the 

upper-left and lower-right corners, respectively, of a rectangle 

bounding the ellipse that is part of the chord. 

The pointStart and pointEnd parameters specify 

the endpoints of a line that intersects the ellipse. 

The chord is drawn by using the selected pen and filled 

by using the selected brush.

#### MFC References


  - CDC::Chord

#### Return Value
Always none.  If the function fails, an exception is raised.

## [PyCDC](#pycdc).CreateCompatibleDC

 __CreateCompatibleDC( *dcFrom* __ )
Creates a memory device context that is compatible with this DC.

#### Parameters


  -  *dcFrom=None* :[PyCDC](#pycdc)

    The source DC, or None to make a screen compatible DC.

#### Comments
Note that unlike the MFC version, this function 

calls the global CreateCompatibleDC function and returns 

a new[PyCDC](#pycdc)object.

#### MFC References


  - CDC::CreateCompatibleDC

## [PyCDC](#pycdc).CreatePrinterDC

 __CreatePrinterDC( *printerName* __ )
Creates a device context for a specific printer

#### Parameters


  -  *printerName=None* : string

    The printer name, or None for the default printer

#### MFC References


  - CDC::CreateDC

## [PyCDC](#pycdc).DPtoLP

(x,y) = __DPtoLP( *point* __ )
Converts device units into logical units.

#### Parameters


  -  *point* : (x,y)

    The point to convert

#### Alternative Parameters


  -  *x* 

    The x coordinate to convert.

  -  *y* 

    The y coordinate to convert.

#### MFC References


  - CDC::DPtoLP

#### To Do
Should really handle list of (x,y) points

#### Return Value
The converted coordinates.

## [PyCDC](#pycdc).DeleteDC

 __DeleteDC(__ )
Deletes all resources associated with a device context.

#### Comments
In general, do not call this function; the destructor will do it for you.
An application should not call DeleteDC if objects have been selected into the device context. Objects must first be selected out of the device context before it it is deleted.
An application must not delete a device context whose handle was obtained by calling CWnd::GetDC. Instead, it must call CWnd::ReleaseDC to free the device context.
The DeleteDC function is generally used to delete device contexts created with CreateDC, CreateIC, or CreateCompatibleDC.

## [PyCDC](#pycdc).Draw3dRect

 __Draw3dRect( *rect*  *, colorTopLeft*  *, colorBotRight* __ )
Draws a three-dimensional rectangle.

#### Parameters


  -  *rect* : (left, top, right, bottom

    Specifies the bounding rectangle, in logical units.

  -  *colorTopLeft* : int

    Specifies the color of the top and left sides of the three-dimensional rectangle.

  -  *colorBotRight* : int

    Specifies the color of the bottom and right sides of the three-dimensional rectangle.

#### MFC References


  - CDC::Draw3dRect

## [PyCDC](#pycdc).DrawFocusRect

 __DrawFocusRect( *rect* __ )
Draws a rectangle in the style used to 

indicate the rectangle has focus

#### Parameters


  -  *rect* : (left, top, right, bottom)

    The coordinates of the 

rectangle

#### MFC References


  - CDC::DrawFocusRect

## [PyCDC](#pycdc).DrawFrameControl

 __DrawFrameControl( *rect*  *, typ*  *, state* __ )
Draws a frame control of the specified type and style.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    Specifies the bounding rectangle, in logical units.

  -  *typ* : int

    

  -  *state* : int

    

#### MFC References


  - CDC::DrawFrameControl

## [PyCDC](#pycdc).DrawIcon

 __DrawIcon( *point*  *, hIcon* __ )
Draws an icon on the DC.

#### Parameters


  -  *point* : (x,y)

    The point coordinate to draw to.

  -  *hIcon* :[PyHANDLE](#pyhandle)

    The handle of the icon to draw.

#### MFC References


  - CDC::DrawIcon

## [PyCDC](#pycdc).DrawText

s,rc,forat = __DrawText( *s*  *, tuple*  *, format* __ )
Formats text in the given rectangle

#### Parameters


  -  *s* : string

    The desired output string

  -  *tuple* : (int, int, int, int)

    The bounding rectangle in the form: 

(left, top, right, bottom) expressed in logical units (depending on 

selected coordinate system - see[PyCDC::SetMapMode](PyCDC.md#pycdcsetmapmode))

  -  *format* : int

    Specifies one or more bit-or'd format values, such as 

DT_BOTTOM, DT_CENTERDT_RIGHT, DT_VCENTER. For a complete list, see 

the Microsoft Win32 API documentation.

#### Example
Example
import win32ui&ltnl&gt

 import win32con&ltnl&gt

 INCH = 1440   # twips - 1440 per inch allows fine res&ltnl&gt

 def drawtext_test():&ltnl&gt

     dc = win32ui.CreateDC()&ltnl&gt

     dc.CreatePrinterDC()                # ties to default printer&ltnl&gt

     dc.StartDoc('My Python Document')&ltnl&gt

     dc.StartPage()&ltnl&gt

 &ltnl&gt

     # note: upper left is 0,0 with x increasing to the right,&ltnl&gt

     #       and y decreasing (negative) moving down&ltnl&gt

     dc.SetMapMode(win32con.MM_TWIPS)&ltnl&gt

 &ltnl&gt

     # Centers "TEST" about an inch down on page&ltnl&gt

     dc.DrawText('TEST', (0,INCH*-1,INCH*8,INCH*-2), win32con.DT_CENTER )&ltnl&gt

     dc.EndPage()&ltnl&gt

     dc.EndDoc()&ltnl&gt

     del dc&ltnl&gt
#### Return Value
Height of text in pixels
The return value is the height of the text, in logical units. 

If DT_VCENTER or DT_BOTTOM is specified, the return value is the 

offset from rect.top to the bottom of the drawn text. 

If the function fails, the return value is zero (no Python exception is thrown)

## [PyCDC](#pycdc).Ellipse

 __Ellipse( *rect* __ )
Draws an Ellipse.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    Specifies the ellipse's bounding rectangle

#### Comments
The center of the ellipse is the center of the bounding rectangle 

specified by rect. The ellipse is drawn with the current pen, and its 

interior is filled with the current brush.

#### MFC References


  - CDC::Ellipse

#### Return Value
Always none.  If the function fails, an exception is raised.

## [PyCDC](#pycdc).EndDoc

 __EndDoc(__ )
Finishes spooling the document and starts printing it

## [PyCDC](#pycdc).EndPage

 __EndPage(__ )
Finishes a page on a printer DC

## [PyCDC](#pycdc).EndPath

 __EndPath(__ )
Closes a path bracket and selects the path defined by the bracket into the specified device context

## [PyCDC](#pycdc).ExtTextOut

 __ExtTextOut( *int*  *, int*  *, int*  *, rect*  *, string*  *, tuple* __ )
Writes text to the DC.

#### Parameters


  -  *int* : x

    The x coordinate to write the text to.

  -  *int* : y

    The y coordinate to write the text to.

  -  *int* : nOptions

    Specifies the rectangle type. This parameter can be one, both, or neither of ETO_CLIPPED and ETO_OPAQUE

  -  *rect* : (left, top, right, bottom)

    Specifies the text's bounding rectangle.  (Can be None.)

  -  *string* : text

    The text to write.

  -  *tuple* : (width1, width2, ...)

    Optional array of values that indicate distance between origins of character cells.

#### MFC References


  - CDC::ExtTextOut

#### Return Value
Always none.  If the function fails, an exception is raised.

## [PyCDC](#pycdc).FillPath

 __FillPath(__ )
Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode. After its interior is filled, the path is discarded from the device context.

## [PyCDC](#pycdc).FillRect

 __FillRect( *rect*  *, brush* __ )
Fills a given rectangle with the specified brush

#### Parameters


  -  *rect* : (left, top, right, bottom

    Specifies the bounding rectangle, in logical units.

  -  *brush* :[PyCBrush](#pycbrush)

    Specifies the brush to use.

#### MFC References


  - CDC::FillRect

## [PyCDC](#pycdc).FillSolidRect

 __FillSolidRect( *rect*  *, color* __ )
Fills the given rectangle with the specified solid color.

#### Parameters


  -  *rect* : (left, top, right, bottom

    Specifies the bounding rectangle, in logical units.

  -  *color* : int

    Specifies the color to use.

#### MFC References


  - CDC::FillSolidRect

## [PyCDC](#pycdc).FrameRect

 __FrameRect( *rect*  *, brush* __ )
Draws a border around the rectangle specified by rect

#### Parameters


  -  *rect* : (left, top, right, bottom

    Specifies the bounding rectangle, in logical units.

  -  *brush* :[PyCBrush](#pycbrush)

    Specifies the brush to use.

#### MFC References


  - CDC::FrameRect

## [PyCDC](#pycdc).GetBrushOrg

(int,int) = __GetBrushOrg(__ )
Retrieves the origin (in device units) of the brush currently selected for the device context.

#### MFC References


  - CDC::GetBrushOrg

## [PyCDC](#pycdc).GetClipBox

(left, top, right, bottom) = __GetClipBox(__ )
Retrieves the dimensions of the smallest bounding rectangle around the current clipping boundary.

#### MFC References


  - CDC::GetClipBox

#### Return Value
A tuple of integers specifying the rectangle.

## [PyCDC](#pycdc).GetCurrentPosition

(x, y) = __GetCurrentPosition(__ )
Retrieves the current position (in logical coordinates).

## [PyCDC](#pycdc).GetDeviceCaps

int = __GetDeviceCaps( *index* __ )
Retrieves a capability of the device context.

#### Parameters


  -  *index* : int

    The information requested.  See the win32api documentation for details.

#### MFC References


  - CDC::GetDeviceCaps

#### Return Value
The value of the requested capability

## [PyCDC](#pycdc).GetHandleAttrib

int = __GetHandleAttrib(__ )
Retrieves the handle of the attribute device context.

## [PyCDC](#pycdc).GetHandleOutput

int = __GetHandleOutput(__ )
Retrieves the handle of the output device context.

## [PyCDC](#pycdc).GetMapMode

int = __GetMapMode(__ )
Gets the mapping mode for the device context.

#### MFC References


  - CDC::GetMapMode

## [PyCDC](#pycdc).GetNearestColor

int = __GetNearestColor( *color* __ )
Returns the closest color a device can map.

#### Parameters


  -  *color* : int

    Specifies the color to be matched.

## [PyCDC](#pycdc).GetPixel

 __GetPixel( *x*  *, y* __ )
Gets a pixel at a local in a device context

#### Parameters


  -  *x* : int

    Horizontal coordinate.

  -  *y* : int

    Vertical coordinate.

## [PyCDC](#pycdc).GetSafeHdc

int = __GetSafeHdc(__ )
Returns the HDC of this DC object.

#### MFC References


  - CDC::GetSafeHdc

## [PyCDC](#pycdc).GetTextExtent

(x,y) = __GetTextExtent( *text* __ )
Calculates the width and height of a line of text using the current font to determine the dimensions.

#### Parameters


  -  *text* : string

    The text to calculate for.

#### MFC References


  - CFC::GetTextExtent

#### Return Value
A tuple of integers with the size of the string, in logical units.

## [PyCDC](#pycdc).GetTextExtentPoint

(x,y) = __GetTextExtentPoint( *text* __ )
An alias for[PyCDC::GetTextExtent](PyCDC.md#pycdcgettextextent). 

GetTextExtentPoint is the preferred win32api name, but GetTextExtent is the MFC name.
Calculates the width and height of a line of text using the current font to determine the dimensions.

#### Parameters


  -  *text* : string

    The text to calculate for.

#### Return Value
A tuple of integers with the size of the string, in logical units.

## [PyCDC](#pycdc).GetTextFace

string = __GetTextFace(__ )
Returns typeface name of the current font.

#### MFC References


  - CDC::GetTextFace

## [PyCDC](#pycdc).GetTextMetrics

dict = __GetTextMetrics(__ )
Retrieves the metrics for the current font in this device context.

#### MFC References


  - CDC::GetTextMetrics

#### Return Value
A dictionary of integers, keyed by the following strings:
tmHeight
tmAscent
tmDescent
tmInternalLeading
tmExternalLeading
tmAveCharWidth
tmMaxCharWidth
tmWeight
tmItalic
tmUnderlined
tmStruckOut
tmFirstChar
tmLastChar
tmDefaultChar
tmBreakChar
tmPitchAndFamily
tmCharSet
tmOverhang
tmDigitizedAspectX
tmDigitizedAspectY


## [PyCDC](#pycdc).GetViewportExt

x, y = __GetViewportExt(__ )
Gets the viewport extent of the device context

## [PyCDC](#pycdc).GetViewportOrg

x, y = __GetViewportOrg(__ )
Gets the viewport origin of the device context

## [PyCDC](#pycdc).GetWindowExt

x, y = __GetWindowExt(__ )
Gets the window extent of the device context

## [PyCDC](#pycdc).GetWindowOrg

x, y = __GetWindowOrg(__ )
Retrieves the x- and y-coordinates of the origin of the window associated with the device context.

## [PyCDC](#pycdc).IntersectClipRect

 __IntersectClipRect( *rect* __ )
Creates a new clipping region by forming the intersection of the current region and the rectangle specified

#### Parameters


  -  *rect* : (left, top, right, bottom)

    Specifies the bounding rectangle, in logical units.

#### MFC References


  - CDC::IntersectClipRect

#### Return Value
region type as integer

## [PyCDC](#pycdc).IsPrinting

int = __IsPrinting(__ )
Returns 1 if the DC is currently printing, else 0

## [PyCDC](#pycdc).LPtoDP

(x,y) = __LPtoDP( *point* __ )
Converts logical units into device units.

#### Parameters


  -  *point* : (x,y)

    The point coordinate to convert.

#### Alternative Parameters


  -  *x* 

    The x coordinate to convert.

  -  *y* 

    The y coordinate to convert.

#### MFC References


  - CDC::LPtoDP

#### Return Value
The converted coordinates.

## [PyCDC](#pycdc).LineTo

 __LineTo( *point* __ )
Draws a line to a specified point, using the currently selected pen.

#### Parameters


  -  *point* : (x,y)

    The point coordinate to draw to.

#### Alternative Parameters


  -  *x* 

    The x coordinate to draw to.

  -  *y* 

    The y coordinate to draw to.

#### MFC References


  - CDC::LineTo

## [PyCDC](#pycdc).MoveTo

(x,y) = __MoveTo( *point* __ )
Moves the current position to a specified point.

#### Parameters


  -  *point* : (x,y)

    The point coordinate to move to.

#### Alternative Parameters


  -  *x* 

    The x coordinate to move to.

  -  *y* 

    The y coordinate to move to.

#### MFC References


  - CDC::MoveTo

#### Return Value
The previous position.

## [PyCDC](#pycdc).OffsetViewportOrg

x, y = __OffsetViewportOrg( *x,y* __ )
Modifies the coordinates of the viewport origin relative to the coordinates of the current viewport origin

#### Parameters


  -  *x,y* : int, int

    The new origin offset.

#### Return Value
The previous viewport origin as a tuple (x,y)

## [PyCDC](#pycdc).OffsetWindowOrg

x, y = __OffsetWindowOrg( *x,y* __ )
Modifies the coordinates of the window origin relative to the coordinates of the current window origin.

#### Parameters


  -  *x,y* : int, int

    The new origin offset.

#### Return Value
The previous origin as a tuple (x,y)

## [PyCDC](#pycdc).PatBlt

 __PatBlt( *destPos*  *, size*  *, rop* __ )
Creates a bit pattern on the device.

#### Parameters


  -  *destPos* : (x,y)-ints

    The logical x,y coordinates of the upper-left corner of the destination rectangle.

  -  *size* : (width, height)-ints

    Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

  -  *rop* : int

    Specifies the raster operation to be performed. See the win32 api documentation for details.

#### MFC References


  - CDC::BitBlt

## [PyCDC](#pycdc).Pie

 __Pie( *x1*  *, y1*  *, x2*  *, y2*  *, x3*  *, y3*  *, x4*  *, y4* __ )
Draws a pie slice in a device context

#### Parameters


  -  *x1* : int

    X coordinate of upper left corner

  -  *y1* : int

    Y coordinate of upper left corner

  -  *x2* : int

    X coordinate of lower right corner

  -  *y2* : int

    Y coordinate of lower right corner

  -  *x3* : int

    X coordinate of starting point of arc

  -  *y3* : int

    Y coordinate of starting point of arc

  -  *x4* : int

    X coordinate of ending point of arc

  -  *y4* : int

    Y coordinate of ending point of arc

## [PyCDC](#pycdc).PolyBezier

 __PolyBezier(__ )
Draws one or more Bezier splines.

## [PyCDC](#pycdc).Polygon

 __Polygon(__ )
Draws an Polygon.

## [PyCDC](#pycdc).Polyline

 __Polyline( *points* __ )
Draws a Polyline.

#### Parameters


  -  *points* : [(x, y), ...]

    A sequence of points

## [PyCDC](#pycdc).RealizePalette

int = __RealizePalette(__ )
Maps palette entries in the current logical palette to the system palette.

#### Return Value
Indicates how many entries in the logical palette were mapped to different entries 

in the system palette. This represents the number of entries that this function 

remapped to accommodate changes in the system palette since the logical palette 

was last realized.

## [PyCDC](#pycdc).RectVisible

int = __RectVisible( *rect* __ )
Determines whether any part of the given rectangle lies within the clipping region of the display context.

#### Parameters


  -  *rect* : (left, top, right, bottom)

    The coordinates of the reactangle to be checked.

#### MFC References


  - CDC::RectVisible

#### Return Value
Non zero if any part of the rectangle lies within the clipping region, else zero.

## [PyCDC](#pycdc).Rectangle

rc = __Rectangle(__ )
Draws a rectangle using the current pen. The interior of the rectangle is filled using the current brush.

## [PyCDC](#pycdc).RestoreDC

 __RestoreDC( *saved* __ )
Restores the state of the device context.

#### Parameters


  -  *saved* : int

    The id of a previously saved device context.  See[PyCDC::SaveDC](PyCDC.md#pycdcsavedc)

#### MFC References


  - CDC::RestoreDC

## [PyCDC](#pycdc).SaveDC

int = __SaveDC(__ )
Saves the current state of the device context.  Windows manages a stack of state information. 

The saved device context can later be restored by using __CDC::RestoreDC__ 

#### MFC References


  - CDC::SaveDC

#### Return Value
An integer identifying the context, which can be used by[PyCDC::RestoreDC](PyCDC.md#pycdcrestoredc). 

An exception is raised if this function fails.

## [PyCDC](#pycdc).ScaleViewportExt

x, y = __ScaleViewportExt(__ )
Modifies the viewport extents relative to the current values.

## [PyCDC](#pycdc).ScaleWindowExt

x, y = __ScaleWindowExt(__ )
Modifies the window extents relative to the current values.

## [PyCDC](#pycdc).SelectClipRgn

obRgn = __SelectClipRgn(__ )
Selects the given region as the current clipping region for the device context

#### Return Value
The return value specifies the region's complexity (integer)

## [PyCDC](#pycdc).SelectObject

object = __SelectObject( *ob* __ )
Selects an object into the device context.
Currently, only[PyCFont](#pycfont),[PyCBitMap](#pycbitmap),[PyCBrush](#pycbrush)and __PyCPen__ objects are supported.

#### Parameters


  -  *ob* : object

    The object to select.

#### MFC References


  - CDC::SelectObject

#### Return Value
The previously selected object.  This will be the same type as the object parameter.

## [PyCDC](#pycdc).SelectPalette

int = __SelectPalette( *hPalette*  *, forceBackground* __ )
Sets the logical palette.

#### Parameters


  -  *hPalette* : int

    The handle to the palette

  -  *forceBackground* : int

    Specifies whether the logical palette is forced to be a background palette.

#### MFC References


  - CDC::SelectePalette

#### Return Value
The previous palette handle.

## [PyCDC](#pycdc).SetBkColor

int = __SetBkColor( *color* __ )
Sets the current background color to the specified color.

#### Parameters


  -  *color* : int

    A windows color specification.  See the win32api documentation for details.

#### Comments
If the background mode is OPAQUE, the system uses the background color 

to fill the gaps in styled lines, the gaps between hatched lines in brushes, and 

the background in character cells. 

The system also uses the background color when converting bitmaps between color and 

monochrome device contexts.

#### MFC References


  - CDC::SetBkColor

#### Return Value
The return value is the previous background color.

## [PyCDC](#pycdc).SetBkMode

int = __SetBkMode( *mode* __ )
Sets the current background mode to the specified mode.

#### Parameters


  -  *mode* : int

    A background mode.  May be either TRANSPARENT or OPAQUE.

#### Comments
Specifies the mode to be set.  This parameter can be either OPAQUE or TRANSPARENT

#### MFC References


  - CDC::SetBkMode

#### Return Value
The return value is the previous background mode.

## [PyCDC](#pycdc).SetBrushOrg

(int, int) = __SetBrushOrg( *point* __ )
Specifies the origin that GDI will assign to the next brush that the application selects into the device context.

#### Parameters


  -  *point* : (x,y)

    The new origin in device units.

#### MFC References


  - CDC::SetBrushOrg

#### Return Value
The previous origin in device units.

## [PyCDC](#pycdc).SetGraphicsMode

int = __SetGraphicsMode( *mode* __ )
Sets the graphics mode for the specified device context

#### Parameters


  -  *mode* : int

    The new mode.

## [PyCDC](#pycdc).SetMapMode

int = __SetMapMode( *newMode* __ )
Sets the mapping mode for the device context.

#### Parameters


  -  *newMode* : int

    The new mode.  Can be one of 

MM_ANISOTROPIC, MM_HIENGLISH, MM_HIMETRIC, MM_ISOTROPIC, MM_LOENGLISH, MM_LOMETRIC, MM_TEXT, MM_TWIPS

#### MFC References


  - CDC::SetMapMode

#### Return Value
The previous mapping mode.

## [PyCDC](#pycdc).SetPixel

 __SetPixel( *x*  *, y*  *, color* __ )
Sets a pixel in a device context

#### Parameters


  -  *x* : int

    Horizontal coordinate.

  -  *y* : int

    Vertical coordinate.

  -  *color* : int

    The brush color.

## [PyCDC](#pycdc).SetPolyFillMode

(int) = __SetPolyFillMode( *point* __ )
Sets the polygon-filling mode.

#### Parameters


  -  *point* : (x,y)

    The new origin in device units.

#### MFC References


  - CDC::SetPolyFillMode

#### Return Value
The previous PolyFillMode as integer
The previous PolyFillMode.

## [PyCDC](#pycdc).SetROP2

dict = __SetROP2( *mode* __ )
Sets the current drawing mode.

#### Parameters


  -  *mode* : int

    The new drawing mode.

#### MFC References


  - CDC::SetROP2

## [PyCDC](#pycdc).SetTextAlign

int = __SetTextAlign( *newFlags* __ )
Sets the text-alignment flags.

#### Parameters


  -  *newFlags* : int

    The new alignment flags.  Can be a combination of (TA_CENTER, TA_LEFT, TA_RIGHT), (TA_BASELINE, TA_BOTTOM, TA_TOP) and (TA_NOUPDATECP, TA_UPDATECP)
The default is TA_LEFT|TA_TOP|TA_NOUPDATECP

#### MFC References


  - CDC::SetTextAlign

#### Return Value
The old alignment flags.

## [PyCDC](#pycdc).SetTextColor

int = __SetTextColor( *color* __ )
Sets the text color to the specified color.

#### Parameters


  -  *color* : int

    A windows color specification.  See the win32api documentation for details.

#### Comments
This text color is used when writing text to this device context and also when converting bitmaps between color and monochrome device contexts. 

If the device cannot represent the specified color, the system sets the text color to the nearest physical color. 

The background color for a character is specified by the SetBkColor and SetBkMode member functions.

#### MFC References


  - CDC::SetTextColor

#### Return Value
The return value is the previous text color.

## [PyCDC](#pycdc).SetViewportExt

(x,y) = __SetViewportExt( *size* __ )
Sets the x,y extents of the viewport of the device context.

#### Parameters


  -  *size* : (x,y)

    The new size.

#### MFC References


  - CDC::SetViewportExt

#### Return Value
The previous extents of the viewport (in logical units).

## [PyCDC](#pycdc).SetViewportOrg

x, y = __SetViewportOrg( *x,y* __ )
Sets the viewport origin of the device context

#### Parameters


  -  *x,y* : int, int

    The new origin.

## [PyCDC](#pycdc).SetWindowExt

(x,y) = __SetWindowExt( *size* __ )
Sets the x,y extents of the window associated with the device context.

#### Parameters


  -  *size* : (x,y)

    The new size.

#### MFC References


  - CDC::SetWindowExt

#### Return Value
The previous extents of the window (in logical units).

## [PyCDC](#pycdc).SetWindowOrg

x, y = __SetWindowOrg( *x,y* __ )
Sets the window origin of the device context

#### Parameters


  -  *x,y* : int, int

    The new origin.

## [PyCDC](#pycdc).SetWorldTransform

int = __SetWorldTransform(__ )
sets a two-dimensional linear transformation between world space and page space for the specified device context. This transformation can be used to scale, rotate, shear, or translate graphics output.

## [PyCDC](#pycdc).StartDoc

 __StartDoc( *docName*  *, outputFile* __ )
Starts spooling a document to a printer DC

#### Parameters


  -  *docName* : string

    The document name

  -  *outputFile* : string

    The output file name. Use this to spool to a file. Omit to send to the printer.

## [PyCDC](#pycdc).StartPage

 __StartPage(__ )
Starts a new page on a printer DC

## [PyCDC](#pycdc).StretchBlt

 __StretchBlt( *destPos*  *, size*  *, dc*  *, srcPos*  *, size*  *, rop* __ )
Copies a bitmap from the source device context to this device context.

#### Parameters


  -  *destPos* : (x,y)-ints

    The logical x,y coordinates of the upper-left corner of the destination rectangle.

  -  *size* : (width, height)-ints

    Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

  -  *dc* :[PyCDC](#pycdc)

    Specifies the PyCDC object from which the bitmap will be copied. It must be None if rop specifies a raster operation that does not include a source.

  -  *srcPos* : (xSrc, ySrc)-ints

    Specifies the logical x,y coordinates of the upper-left corner of the source bitmap.

  -  *size* : (widthsrc, heightsrc)-ints

    Specifies the width and height (in logical units) of the destination rectangle and source bitmap.

  -  *rop* : int

    Specifies the raster operation to be performed. See the win32 api documentation for details.

#### MFC References


  - CDC::StretchBlt

## [PyCDC](#pycdc).StrokeAndFillPath

 __StrokeAndFillPath(__ )
Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush. The device context must contain a closed path.

## [PyCDC](#pycdc).StrokePath

 __StrokePath(__ )
Renders the specified path by using the current pen.

## [PyCDC](#pycdc).TextOut

 __TextOut( *int*  *, int*  *, string* __ )
Outputs text to the display context, using the currently selected font.

#### Parameters


  -  *int* : x

    The x coordinate to write the text to.

  -  *int* : y

    The y coordinate to write the text to.

  -  *string* : text

    The text to write.

#### MFC References


  - CDC::TextOut

#### Return Value
Always none.  If the function fails, an exception is raised.