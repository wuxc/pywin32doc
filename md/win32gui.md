# win32gui

## Module win32gui

A module which provides an interface to the native win32 

GUI API.
Note that a module[winxpgui](#winxpgui)also exists, 

which has the same methods as win32gui, but has an XP 

manifest and is setup for side-by-side sharing support for 

certain system DLLs, notably commctl32.

#### Methods


  - [EnumFontFamilies](win32gui.md#win32guienumfontfamilies)

    Enumerates the available font families.&nbsp;

  - [set_logger](win32gui.md#win32guiset_logger)

    Sets a logger object for exceptions and error information&nbsp;

  - [LOGFONT](win32gui.md#win32guilogfont)

    Creates a LOGFONT object.&nbsp;

  - [CreateFontIndirect](win32gui.md#win32guicreatefontindirect)

    function creates a logical font that has the specified characteristics. 

The font can subsequently be selected as the current font for any device context.&nbsp;

  - [GetObject](win32gui.md#win32guigetobject)

    Returns a struct containing the parameters used to create a GDI object&nbsp;

  - [GetObjectType](win32gui.md#win32guigetobjecttype)

    Returns the type (OBJ_* constant) of a GDI handle&nbsp;

  - [PyGetMemory](win32gui.md#win32guipygetmemory)

    Returns a buffer object from and address and length&nbsp;

  - [PyGetString](win32gui.md#win32guipygetstring)

    Returns a string from an address.&nbsp;

  - [PySetString](win32gui.md#win32guipysetstring)

    Copies a string to an address (null terminated). 

You almost certainly should use[win32gui::PySetMemory](win32gui.md#win32guipysetmemory)instead.&nbsp;

  - [PySetMemory](win32gui.md#win32guipysetmemory)

    Copies bytes to an address.&nbsp;

  - [PyGetArraySignedLong](win32gui.md#win32guipygetarraysignedlong)

    Returns a signed long from an array object at specified index&nbsp;

  - [PyGetBufferAddressAndLen](win32gui.md#win32guipygetbufferaddressandlen)

    Returns a buffer object address and len&nbsp;

  - [FlashWindow](win32gui.md#win32guiflashwindow)

    The FlashWindow function flashes the specified window one time. It does not change the active state of the window.&nbsp;

  - [FlashWindowEx](win32gui.md#win32guiflashwindowex)

    The FlashWindowEx function flashes the specified window a specified number of times.&nbsp;

  - [GetWindowLong](win32gui.md#win32guigetwindowlong)

    &nbsp;

  - [GetClassLong](win32gui.md#win32guigetclasslong)

    &nbsp;

  - [SetWindowLong](win32gui.md#win32guisetwindowlong)

    Places a long value at the specified offset into the extra window memory of the given window.&nbsp;

  - [CallWindowProc](win32gui.md#win32guicallwindowproc)

    &nbsp;

  - [SendMessage](win32gui.md#win32guisendmessage)

    Sends a message to the window.&nbsp;

  - [SendMessageTimeout](win32gui.md#win32guisendmessagetimeout)

    Sends a message to the window.&nbsp;

  - [PostMessage](win32gui.md#win32guipostmessage)

    &nbsp;

  - [PostThreadMessage](win32gui.md#win32guipostthreadmessage)

    &nbsp;

  - [ReplyMessage](win32gui.md#win32guireplymessage)

    Used to reply to a message sent through the SendMessage function without returning control to the function that called SendMessage.&nbsp;

  - [RegisterWindowMessage](win32gui.md#win32guiregisterwindowmessage)

    Defines a new window message that is guaranteed to be unique throughout the system. The message value can be used when sending or posting messages.&nbsp;

  - [DefWindowProc](win32gui.md#win32guidefwindowproc)

    &nbsp;

  - [EnumWindows](win32gui.md#win32guienumwindows)

    Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.&nbsp;

  - [EnumThreadWindows](win32gui.md#win32guienumthreadwindows)

    Enumerates all top-level windows associated with a thread on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE&nbsp;

  - [EnumChildWindows](win32gui.md#win32guienumchildwindows)

    Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE.&nbsp;

  - [DialogBox](win32gui.md#win32guidialogbox)

    Creates a modal dialog box.&nbsp;

  - [DialogBoxParam](win32gui.md#win32guidialogboxparam)

    See[win32gui::DialogBox](win32gui.md#win32guidialogbox)&nbsp;

  - [DialogBoxIndirect](win32gui.md#win32guidialogboxindirect)

    Creates a modal dialog box from a template, see[win32ui::CreateDialogIndirect](win32ui.md#win32uicreatedialogindirect)&nbsp;

  - [DialogBoxIndirectParam](win32gui.md#win32guidialogboxindirectparam)

    See[win32gui::DialogBoxIndirect](win32gui.md#win32guidialogboxindirect)&nbsp;

  - [CreateDialogIndirect](win32gui.md#win32guicreatedialogindirect)

    Creates a modeless dialog box from a template, see[win32ui::CreateDialogIndirect](win32ui.md#win32uicreatedialogindirect)&nbsp;

  - [DialogBoxIndirectParam](win32gui.md#win32guidialogboxindirectparam)

    See[win32gui::CreateDialogIndirect](win32gui.md#win32guicreatedialogindirect)&nbsp;

  - [EndDialog](win32gui.md#win32guienddialog)

    Ends a dialog box.&nbsp;

  - [GetDlgItem](win32gui.md#win32guigetdlgitem)

    Retrieves the handle to a control in the specified dialog box.&nbsp;

  - [GetDlgItemInt](win32gui.md#win32guigetdlgitemint)

    Returns the integer value of a dialog control&nbsp;

  - [SetDlgItemInt](win32gui.md#win32guisetdlgitemint)

    Places an integer value in a dialog control&nbsp;

  - [GetDlgCtrlID](win32gui.md#win32guigetdlgctrlid)

    Retrieves the identifier of the specified control.&nbsp;

  - [GetDlgItemText](win32gui.md#win32guigetdlgitemtext)

    Returns the text of a dialog control&nbsp;

  - [SetDlgItemText](win32gui.md#win32guisetdlgitemtext)

    Sets the text for a window or control&nbsp;

  - [GetNextDlgTabItem](win32gui.md#win32guigetnextdlgtabitem)

    Retrieves a handle to the first control that has the WS_TABSTOP style that precedes (or follows) the specified control.&nbsp;

  - [GetNextDlgGroupItem](win32gui.md#win32guigetnextdlggroupitem)

    Retrieves a handle to the first control in a group of controls that precedes (or follows) the specified control in a dialog box.&nbsp;

  - [SetWindowText](win32gui.md#win32guisetwindowtext)

    Sets the window text.&nbsp;

  - [GetWindowText](win32gui.md#win32guigetwindowtext)

    Get the window text.&nbsp;

  - [InitCommonControls](win32gui.md#win32guiinitcommoncontrols)

    Initializes the common controls.&nbsp;

  - [InitCommonControlsEx](win32gui.md#win32guiinitcommoncontrolsex)

    Initializes specific common controls.&nbsp;

  - [LoadCursor](win32gui.md#win32guiloadcursor)

    Loads a cursor.&nbsp;

  - [SetCursor](win32gui.md#win32guisetcursor)

    &nbsp;

  - [GetCursor](win32gui.md#win32guigetcursor)

    &nbsp;

  - [GetCursorInfo](win32gui.md#win32guigetcursorinfo)

    Retrieves information about the global cursor.&nbsp;

  - [CreateAcceleratorTable](win32gui.md#win32guicreateacceleratortable)

    Creates an accelerator table&nbsp;

  - [DestroyAccleratorTable](win32gui.md#win32guidestroyaccleratortable)

    Destroys an accelerator table&nbsp;

  - [LoadMenu](win32gui.md#win32guiloadmenu)

    Loads a menu&nbsp;

  - [DestroyMenu](win32gui.md#win32guidestroymenu)

    Destroys a previously loaded menu.&nbsp;

  - [SetMenu](win32gui.md#win32guisetmenu)

    Sets the menu for the specified window.&nbsp;

  - [GetMenu](win32gui.md#win32guigetmenu)

    Gets the menu for the specified window.&nbsp;

  - [LoadIcon](win32gui.md#win32guiloadicon)

    Loads an icon&nbsp;

  - [CopyIcon](win32gui.md#win32guicopyicon)

    Copies an icon&nbsp;

  - [DrawIcon](win32gui.md#win32guidrawicon)

    Draws an icon or cursor into the specified device context. 

To specify additional drawing options, use the[win32gui::DrawIconEx](win32gui.md#win32guidrawiconex)function.&nbsp;

  - [DrawIconEx](win32gui.md#win32guidrawiconex)

    Draws an icon or cursor into the specified device context, 

performing the specified raster operations, and stretching or compressing the 

icon or cursor as specified.&nbsp;

  - [CreateIconIndirect](win32gui.md#win32guicreateiconindirect)

    Creates an icon or cursor from an ICONINFO structure.&nbsp;

  - [CreateIconFromResource](win32gui.md#win32guicreateiconfromresource)

    Creates an icon or cursor from resource bits describing the icon.&nbsp;

  - [LoadImage](win32gui.md#win32guiloadimage)

    Loads a bitmap, cursor or icon&nbsp;

  - [DeleteObject](win32gui.md#win32guideleteobject)

    Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.&nbsp;

  - [BitBlt](win32gui.md#win32guibitblt)

    Performs a bit-block transfer of the color data corresponding 

to a rectangle of pixels from the specified source device context into a 

destination device context.&nbsp;

  - [StretchBlt](win32gui.md#win32guistretchblt)

    Copies a bitmap from a source rectangle into a destination 

rectangle, stretching or compressing the bitmap to fit the dimensions of the 

destination rectangle, if necessary&nbsp;

  - [PatBlt](win32gui.md#win32guipatblt)

    Paints a rectangle by combining the current brush with existing colors&nbsp;

  - [SetStretchBltMode](win32gui.md#win32guisetstretchbltmode)

    Sets the stretching mode used by[win32gui::StretchBlt](win32gui.md#win32guistretchblt)&nbsp;

  - [GetStretchBltMode](win32gui.md#win32guigetstretchbltmode)

    Returns the stretching mode used by[win32gui::StretchBlt](win32gui.md#win32guistretchblt)&nbsp;

  - [TransparentBlt](win32gui.md#win32guitransparentblt)

    Transfers color from one DC to another, with one color treated as transparent&nbsp;

  - [MaskBlt](win32gui.md#win32guimaskblt)

    Combines the color data for the source and destination 

bitmaps using the specified mask and raster operation.&nbsp;

  - [AlphaBlend](win32gui.md#win32guialphablend)

    Transfers color information using alpha blending&nbsp;

  - [ImageList_Add](win32gui.md#win32guiimagelist_add)

    Adds an image or images to an image list.&nbsp;

  - [ImageList_Create](win32gui.md#win32guiimagelist_create)

    Create an image list&nbsp;

  - [ImageList_Destroy](win32gui.md#win32guiimagelist_destroy)

    Destroy an imagelist&nbsp;

  - [ImageList_Draw](win32gui.md#win32guiimagelist_draw)

    Draw an image on an HDC&nbsp;

  - [ImageList_DrawEx](win32gui.md#win32guiimagelist_drawex)

    Draw an image on an HDC&nbsp;

  - [ImageList_GetIcon](win32gui.md#win32guiimagelist_geticon)

    Extract an icon from an imagelist&nbsp;

  - [ImageList_GetImageCount](win32gui.md#win32guiimagelist_getimagecount)

    Return count of images in imagelist&nbsp;

  - [ImageList_LoadImage](win32gui.md#win32guiimagelist_loadimage)

    Loads bitmaps, cursors or icons, creates imagelist&nbsp;

  - [ImageList_LoadBitmap](win32gui.md#win32guiimagelist_loadbitmap)

    Creates an image list from the specified bitmap resource.&nbsp;

  - [ImageList_Remove](win32gui.md#win32guiimagelist_remove)

    Remove an image from an imagelist&nbsp;

  - [ImageList_Replace](win32gui.md#win32guiimagelist_replace)

    Replace an image in an imagelist with a bitmap image&nbsp;

  - [ImageList_ReplaceIcon](win32gui.md#win32guiimagelist_replaceicon)

    Replace an image in an imagelist with an icon image&nbsp;

  - [ImageList_SetBkColor](win32gui.md#win32guiimagelist_setbkcolor)

    Set the background color for the imagelist&nbsp;

  - [ImageList_SetOverlayImage](win32gui.md#win32guiimagelist_setoverlayimage)

    Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image.&nbsp;

  - [MessageBox](win32gui.md#win32guimessagebox)

    Displays a message box&nbsp;

  - [MessageBeep](win32gui.md#win32guimessagebeep)

    Plays a waveform sound.&nbsp;

  - [CreateWindow](win32gui.md#win32guicreatewindow)

    Creates a new window.&nbsp;

  - [DestroyWindow](win32gui.md#win32guidestroywindow)

    &nbsp;

  - [EnableWindow](win32gui.md#win32guienablewindow)

    Enables and disables keyboard and mouse input to a window&nbsp;

  - [FindWindow](win32gui.md#win32guifindwindow)

    Retrieves a handle to the top-level window whose class name and window name match the specified strings.&nbsp;

  - [FindWindowEx](win32gui.md#win32guifindwindowex)

    Retrieves a handle to the top-level window whose class name and window name match the specified strings.&nbsp;

  - [DragAcceptFiles](win32gui.md#win32guidragacceptfiles)

    Registers whether a window accepts dropped files.&nbsp;

  - [DragDetect](win32gui.md#win32guidragdetect)

    captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point.&nbsp;

  - [SetDoubleClickTime](win32gui.md#win32guisetdoubleclicktime)

    &nbsp;

  - [GetDoubleClickTime](win32gui.md#win32guigetdoubleclicktime)

    &nbsp;

  - [HideCaret](win32gui.md#win32guihidecaret)

    Hides the caret&nbsp;

  - [SetCaretPos](win32gui.md#win32guisetcaretpos)

    Changes the position of the caret&nbsp;

  - [GetCaretPos](win32gui.md#win32guigetcaretpos)

    Returns the current caret position&nbsp;

  - [ShowCaret](win32gui.md#win32guishowcaret)

    Shows the caret at its current position&nbsp;

  - [ShowWindow](win32gui.md#win32guishowwindow)

    Shows or hides a window and changes its state&nbsp;

  - [IsWindowVisible](win32gui.md#win32guiiswindowvisible)

    Indicates if the window has the WS_VISIBLE style.&nbsp;

  - [IsWindowEnabled](win32gui.md#win32guiiswindowenabled)

    Indicates if the window is enabled.&nbsp;

  - [SetFocus](win32gui.md#win32guisetfocus)

    Sets focus to the specified window.&nbsp;

  - [GetFocus](win32gui.md#win32guigetfocus)

    Returns the HWND of the window with focus.&nbsp;

  - [UpdateWindow](win32gui.md#win32guiupdatewindow)

    &nbsp;

  - [BringWindowToTop](win32gui.md#win32guibringwindowtotop)

    &nbsp;

  - [SetActiveWindow](win32gui.md#win32guisetactivewindow)

    &nbsp;

  - [GetActiveWindow](win32gui.md#win32guigetactivewindow)

    &nbsp;

  - [SetForegroundWindow](win32gui.md#win32guisetforegroundwindow)

    &nbsp;

  - [GetForegroundWindow](win32gui.md#win32guigetforegroundwindow)

    &nbsp;

  - [GetClientRect](win32gui.md#win32guigetclientrect)

    Returns the rectangle of the client area of a window, in client coordinates&nbsp;

  - [GetDC](win32gui.md#win32guigetdc)

    Gets the device context for the window.&nbsp;

  - [SaveDC](win32gui.md#win32guisavedc)

    Save the state of a device context&nbsp;

  - [RestoreDC](win32gui.md#win32guirestoredc)

    Restores a device context state&nbsp;

  - [DeleteDC](win32gui.md#win32guideletedc)

    Deletes a DC&nbsp;

  - [CreateCompatibleDC](win32gui.md#win32guicreatecompatibledc)

    Creates a memory device context (DC) compatible with the specified device.&nbsp;

  - [CreateCompatibleBitmap](win32gui.md#win32guicreatecompatiblebitmap)

    Creates a bitmap compatible with the device that is associated with the specified device context.&nbsp;

  - [CreateBitmap](win32gui.md#win32guicreatebitmap)

    Creates a bitmap&nbsp;

  - [SelectObject](win32gui.md#win32guiselectobject)

    Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.&nbsp;

  - [GetCurrentObject](win32gui.md#win32guigetcurrentobject)

    Retrieves currently selected object from a DC&nbsp;

  - [GetWindowRect](win32gui.md#win32guigetwindowrect)

    Returns the rectangle for a window in screen coordinates&nbsp;

  - [GetStockObject](win32gui.md#win32guigetstockobject)

    Creates a handle to one of the standard system Gdi objects&nbsp;

  - [PostQuitMessage](win32gui.md#win32guipostquitmessage)

    &nbsp;

  - [WaitMessage](win32gui.md#win32guiwaitmessage)

    Waits for a message&nbsp;

  - [SetWindowPos](win32gui.md#win32guisetwindowpos)

    Sets the position and size of a window&nbsp;

  - [GetWindowPlacement](win32gui.md#win32guigetwindowplacement)

    Returns placement information about the current window.&nbsp;

  - [SetWindowPlacement](win32gui.md#win32guisetwindowplacement)

    Sets the windows placement&nbsp;

  - [RegisterClass](win32gui.md#win32guiregisterclass)

    Registers a window class.&nbsp;

  - [UnregisterClass](win32gui.md#win32guiunregisterclass)

    Unregisters a window class created by[win32gui::RegisterClass](win32gui.md#win32guiregisterclass)&nbsp;

  - [PumpMessages](win32gui.md#win32guipumpmessages)

    Runs a message loop until a WM_QUIT message is received.&nbsp;

  - [PumpWaitingMessages](win32gui.md#win32guipumpwaitingmessages)

    Pumps all waiting messages for the current thread.&nbsp;

  - [GetMessage](win32gui.md#win32guigetmessage)

    &nbsp;

  - [TranslateMessage](win32gui.md#win32guitranslatemessage)

    &nbsp;

  - [DispatchMessage](win32gui.md#win32guidispatchmessage)

    &nbsp;

  - [TranslateAccelerator](win32gui.md#win32guitranslateaccelerator)

    &nbsp;

  - [PeekMessage](win32gui.md#win32guipeekmessage)

    &nbsp;

  - [Shell_NotifyIcon](win32gui.md#win32guishell_notifyicon)

    Adds, removes or modifies a taskbar icon.&nbsp;

  - [GetSystemMenu](win32gui.md#win32guigetsystemmenu)

    &nbsp;

  - [DrawMenuBar](win32gui.md#win32guidrawmenubar)

    &nbsp;

  - [MoveWindow](win32gui.md#win32guimovewindow)

    &nbsp;

  - [CloseWindow](win32gui.md#win32guiclosewindow)

    &nbsp;

  - [DeleteMenu](win32gui.md#win32guideletemenu)

    &nbsp;

  - [RemoveMenu](win32gui.md#win32guiremovemenu)

    &nbsp;

  - [CreateMenu](win32gui.md#win32guicreatemenu)

    &nbsp;

  - [CreatePopupMenu](win32gui.md#win32guicreatepopupmenu)

    &nbsp;

  - [TrackPopupMenu](win32gui.md#win32guitrackpopupmenu)

    Display popup shortcut menu&nbsp;

  - [CommDlgExtendedError](win32gui.md#win32guicommdlgextendederror)

    &nbsp;

  - [ExtractIcon](win32gui.md#win32guiextracticon)

    &nbsp;

  - [ExtractIconEx](win32gui.md#win32guiextracticonex)

    &nbsp;

  - [DestroyIcon](win32gui.md#win32guidestroyicon)

    &nbsp;

  - [GetIconInfo](win32gui.md#win32guigeticoninfo)

    Returns parameters for an icon or cursor&nbsp;

  - [ScreenToClient](win32gui.md#win32guiscreentoclient)

    Convert screen coordinates to client coords&nbsp;

  - [ClientToScreen](win32gui.md#win32guiclienttoscreen)

    Convert client coordinates to screen coords&nbsp;

  - [PaintDesktop](win32gui.md#win32guipaintdesktop)

    Fills a DC with the destop background&nbsp;

  - [RedrawWindow](win32gui.md#win32guiredrawwindow)

    Causes a portion of a window to be redrawn&nbsp;

  - [GetTextExtentPoint32](win32gui.md#win32guigettextextentpoint32)

    Computes the width and height of the specified string of text.&nbsp;

  - [GetTextMetrics](win32gui.md#win32guigettextmetrics)

    Returns info for the font selected into a DC&nbsp;

  - [GetTextCharacterExtra](win32gui.md#win32guigettextcharacterextra)

    Returns the space between characters&nbsp;

  - [SetTextCharacterExtra](win32gui.md#win32guisettextcharacterextra)

    Sets the spacing between characters&nbsp;

  - [GetTextAlign](win32gui.md#win32guigettextalign)

    Returns horizontal and vertical alignment for text in a device context&nbsp;

  - [SetTextAlign](win32gui.md#win32guisettextalign)

    Sets horizontal and vertical alignment for text in a device context&nbsp;

  - [GetTextFace](win32gui.md#win32guigettextface)

    Retrieves the name of the font currently selected in a DC&nbsp;

  - [GetMapMode](win32gui.md#win32guigetmapmode)

    Returns the method a device context uses to translate logical units to physical units&nbsp;

  - [SetMapMode](win32gui.md#win32guisetmapmode)

    Sets the method used for translating logical units to device units&nbsp;

  - [GetGraphicsMode](win32gui.md#win32guigetgraphicsmode)

    Determines if advanced GDI features are enabled for a device context&nbsp;

  - [SetGraphicsMode](win32gui.md#win32guisetgraphicsmode)

    Enables or disables advanced graphics features for a DC&nbsp;

  - [GetLayout](win32gui.md#win32guigetlayout)

    Retrieves the layout mode of a device context&nbsp;

  - [SetLayout](win32gui.md#win32guisetlayout)

    Sets the layout for a device context&nbsp;

  - [GetPolyFillMode](win32gui.md#win32guigetpolyfillmode)

    Returns the polygon filling mode for a device context&nbsp;

  - [SetPolyFillMode](win32gui.md#win32guisetpolyfillmode)

    Sets the polygon filling mode for a device context&nbsp;

  - [GetWorldTransform](win32gui.md#win32guigetworldtransform)

    Retrieves a device context's coordinate space translation matrix&nbsp;

  - [SetWorldTransform](win32gui.md#win32guisetworldtransform)

    Transforms a device context's coordinate space&nbsp;

  - [ModifyWorldTransform](win32gui.md#win32guimodifyworldtransform)

    Combines a coordinate tranformation with device context's current transformation&nbsp;

  - [CombineTransform](win32gui.md#win32guicombinetransform)

    Combines two coordinate space transformations&nbsp;

  - [GetWindowOrgEx](win32gui.md#win32guigetwindoworgex)

    Retrievs the window origin for a DC&nbsp;

  - [SetWindowOrgEx](win32gui.md#win32guisetwindoworgex)

    Changes the window origin for a DC&nbsp;

  - [GetViewportOrgEx](win32gui.md#win32guigetviewportorgex)

    Retrievs the origin for a DC's viewport&nbsp;

  - [SetViewportOrgEx](win32gui.md#win32guisetviewportorgex)

    Changes the viewport origin for a DC&nbsp;

  - [GetWindowExtEx](win32gui.md#win32guigetwindowextex)

    Retrieves the window extents for a DC&nbsp;

  - [SetWindowExtEx](win32gui.md#win32guisetwindowextex)

    Changes the window extents for a DC&nbsp;

  - [GetViewportExtEx](win32gui.md#win32guigetviewportextex)

    Retrieves the viewport extents for a DC&nbsp;

  - [SetViewportExtEx](win32gui.md#win32guisetviewportextex)

    Changes the viewport extents for a DC&nbsp;

  - [GradientFill](win32gui.md#win32guigradientfill)

    Shades triangles or rectangles by interpolating between vertex colors&nbsp;

  - [GetOpenFileName](win32gui.md#win32guigetopenfilename)

    Creates an Open dialog box that lets the user specify the drive, directory, and the name of a file or set of files to open.&nbsp;

  - [InsertMenuItem](win32gui.md#win32guiinsertmenuitem)

    Inserts a menu item&nbsp;

  - [SetMenuItemInfo](win32gui.md#win32guisetmenuiteminfo)

    Sets menu information&nbsp;

  - [GetMenuItemInfo](win32gui.md#win32guigetmenuiteminfo)

    Gets menu information&nbsp;

  - [GetMenuItemCount](win32gui.md#win32guigetmenuitemcount)

    &nbsp;

  - [GetMenuItemRect](win32gui.md#win32guigetmenuitemrect)

    &nbsp;

  - [GetMenuState](win32gui.md#win32guigetmenustate)

    &nbsp;

  - [SetMenuDefaultItem](win32gui.md#win32guisetmenudefaultitem)

    &nbsp;

  - [GetMenuDefaultItem](win32gui.md#win32guigetmenudefaultitem)

    &nbsp;

  - [AppendMenu](win32gui.md#win32guiappendmenu)

    &nbsp;

  - [InsertMenu](win32gui.md#win32guiinsertmenu)

    &nbsp;

  - [EnableMenuItem](win32gui.md#win32guienablemenuitem)

    &nbsp;

  - [CheckMenuItem](win32gui.md#win32guicheckmenuitem)

    &nbsp;

  - [GetSubMenu](win32gui.md#win32guigetsubmenu)

    &nbsp;

  - [ModifyMenu](win32gui.md#win32guimodifymenu)

    Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item.&nbsp;

  - [GetMenuItemID](win32gui.md#win32guigetmenuitemid)

    Retrieves the menu item identifier of a menu item located at the specified position in a menu.&nbsp;

  - [SetMenuItemBitmaps](win32gui.md#win32guisetmenuitembitmaps)

    Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item.&nbsp;

  - [CheckMenuRadioItem](win32gui.md#win32guicheckmenuradioitem)

    Checks a specified menu item and makes it a 

radio item. At the same time, the function clears all other menu items in 

the associated group and clears the radio-item type flag for those items.&nbsp;

  - [SetMenuInfo](win32gui.md#win32guisetmenuinfo)

    Sets information for a specified menu.&nbsp;

  - [GetMenuInfo](win32gui.md#win32guigetmenuinfo)

    Gets information about a specified menu.&nbsp;

  - [DrawFocusRect](win32gui.md#win32guidrawfocusrect)

    Draws a standard focus outline around a rectangle&nbsp;

  - [DrawText](win32gui.md#win32guidrawtext)

    Draws formatted text on a device context&nbsp;

  - [LineTo](win32gui.md#win32guilineto)

    Draw a line from current position to specified point&nbsp;

  - [Ellipse](win32gui.md#win32guiellipse)

    Draws a filled ellipse on a device context&nbsp;

  - [Pie](win32gui.md#win32guipie)

    Draws a section of an ellipse cut by 2 radials&nbsp;

  - [Arc](win32gui.md#win32guiarc)

    Draws an arc defined by an ellipse and 2 radials&nbsp;

  - [ArcTo](win32gui.md#win32guiarcto)

    Draws an arc defined by an ellipse and 2 radials&nbsp;

  - [AngleArc](win32gui.md#win32guianglearc)

    Draws a line from current pos and a section of a circle's arc&nbsp;

  - [Chord](win32gui.md#win32guichord)

    Draws a chord defined by an ellipse and 2 radials&nbsp;

  - [ExtFloodFill](win32gui.md#win32guiextfloodfill)

    Fills an area with current brush&nbsp;

  - [SetPixel](win32gui.md#win32guisetpixel)

    Set the color of a single pixel&nbsp;

  - [GetPixel](win32gui.md#win32guigetpixel)

    Returns the RGB color of a single pixel&nbsp;

  - [GetROP2](win32gui.md#win32guigetrop2)

    Returns the foreground mixing mode of a DC&nbsp;

  - [SetROP2](win32gui.md#win32guisetrop2)

    Sets the foreground mixing mode of a DC&nbsp;

  - [SetPixelV](win32gui.md#win32guisetpixelv)

    Sets the color of a single pixel to an approximation of specified color&nbsp;

  - [MoveToEx](win32gui.md#win32guimovetoex)

    Changes the current drawing position&nbsp;

  - [GetCurrentPositionEx](win32gui.md#win32guigetcurrentpositionex)

    Returns a device context's current drawing position&nbsp;

  - [GetArcDirection](win32gui.md#win32guigetarcdirection)

    Returns the direction in which rectangles and arcs are drawn&nbsp;

  - [SetArcDirection](win32gui.md#win32guisetarcdirection)

    Sets the drawing direction for arcs and rectangles&nbsp;

  - [Polygon](win32gui.md#win32guipolygon)

    Draws a closed filled polygon defined by a sequence of points&nbsp;

  - [Polyline](win32gui.md#win32guipolyline)

    Connects a sequence of points using currently selected pen&nbsp;

  - [PolylineTo](win32gui.md#win32guipolylineto)

    Draws a series of lines starting from current position.  Updates current position with end point.&nbsp;

  - [PolyBezier](win32gui.md#win32guipolybezier)

    Draws a series of Bezier curves starting from first point specified.&nbsp;

  - [PolyBezierTo](win32gui.md#win32guipolybezierto)

    Draws a series of Bezier curves starting from current drawing position.&nbsp;

  - [PlgBlt](win32gui.md#win32guiplgblt)

    Copies color from a rectangle into a parallelogram&nbsp;

  - [CreatePolygonRgn](win32gui.md#win32guicreatepolygonrgn)

    Creates a region from a sequence of vertices&nbsp;

  - [ExtTextOut](win32gui.md#win32guiexttextout)

    Writes text to a DC.&nbsp;

  - [GetTextColor](win32gui.md#win32guigettextcolor)

    Returns the text color for a DC&nbsp;

  - [SetTextColor](win32gui.md#win32guisettextcolor)

    Changes the text color for a device context&nbsp;

  - [GetBkMode](win32gui.md#win32guigetbkmode)

    Returns the background mode for a device context&nbsp;

  - [SetBkMode](win32gui.md#win32guisetbkmode)

    Sets the background mode for a device context&nbsp;

  - [GetBkColor](win32gui.md#win32guigetbkcolor)

    Returns the background color for a device context&nbsp;

  - [SetBkColor](win32gui.md#win32guisetbkcolor)

    Sets the background color for a device context&nbsp;

  - [DrawEdge](win32gui.md#win32guidrawedge)

    Draws edge(s) of a rectangle&nbsp;

  - [FillRect](win32gui.md#win32guifillrect)

    Fills a rectangular area with specified brush&nbsp;

  - [FillRgn](win32gui.md#win32guifillrgn)

    Fills a region with specified brush&nbsp;

  - [PaintRgn](win32gui.md#win32guipaintrgn)

    Paints a region with current brush&nbsp;

  - [FrameRgn](win32gui.md#win32guiframergn)

    Draws a frame around a region&nbsp;

  - [InvertRgn](win32gui.md#win32guiinvertrgn)

    Inverts the colors in a region&nbsp;

  - [EqualRgn](win32gui.md#win32guiequalrgn)

    Determines if 2 regions are equal&nbsp;

  - [PtInRegion](win32gui.md#win32guiptinregion)

    Determines if a region contains a point&nbsp;

  - [PtInRect](win32gui.md#win32guiptinrect)

    Determines if a rectangle contains a point&nbsp;

  - [RectInRegion](win32gui.md#win32guirectinregion)

    Determines if a region and rectangle overlap at any point&nbsp;

  - [SetRectRgn](win32gui.md#win32guisetrectrgn)

    Makes an existing region rectangular&nbsp;

  - [CombineRgn](win32gui.md#win32guicombinergn)

    Combines two regions&nbsp;

  - [DrawAnimatedRects](win32gui.md#win32guidrawanimatedrects)

    Animates a rectangle in the manner of minimizing, mazimizing, or opening&nbsp;

  - [CreateSolidBrush](win32gui.md#win32guicreatesolidbrush)

    Creates a solid brush of specified color&nbsp;

  - [CreatePatternBrush](win32gui.md#win32guicreatepatternbrush)

    Creates a brush using a bitmap as a pattern&nbsp;

  - [CreateHatchBrush](win32gui.md#win32guicreatehatchbrush)

    Creates a hatch brush with specified style and color&nbsp;

  - [CreatePen](win32gui.md#win32guicreatepen)

    Create a GDI pen&nbsp;

  - [GetSysColor](win32gui.md#win32guigetsyscolor)

    Returns the color of a window element&nbsp;

  - [GetSysColorBrush](win32gui.md#win32guigetsyscolorbrush)

    Creates a handle to a system color brush&nbsp;

  - [InvalidateRect](win32gui.md#win32guiinvalidaterect)

    Invalidates a rectangular area of a window and adds it to the window's update region&nbsp;

  - [FrameRect](win32gui.md#win32guiframerect)

    Draws an outline around a rectangle&nbsp;

  - [InvertRect](win32gui.md#win32guiinvertrect)

    Inverts the colors in a regtangular region&nbsp;

  - [WindowFromDC](win32gui.md#win32guiwindowfromdc)

    Finds the window associated with a device context&nbsp;

  - [GetUpdateRgn](win32gui.md#win32guigetupdatergn)

    Copies the update region of a window into an existing region&nbsp;

  - [GetWindowRgn](win32gui.md#win32guigetwindowrgn)

    Copies the window region of a window into an existing region&nbsp;

  - [SetWindowRgn](win32gui.md#win32guisetwindowrgn)

    Sets the visible region of a window&nbsp;

  - [GetWindowRgnBox](win32gui.md#win32guigetwindowrgnbox)

    Returns the bounding box for a window's region&nbsp;

  - [ValidateRgn](win32gui.md#win32guivalidatergn)

    Removes a region from a window's update region&nbsp;

  - [InvalidateRgn](win32gui.md#win32guiinvalidatergn)

    Adds a region to a window's update region&nbsp;

  - [GetRgnBox](win32gui.md#win32guigetrgnbox)

    Calculates the bounding box of a region&nbsp;

  - [OffsetRgn](win32gui.md#win32guioffsetrgn)

    Relocates a region&nbsp;

  - [Rectangle](win32gui.md#win32guirectangle)

    Creates a solid rectangle using currently selected pen and brush&nbsp;

  - [RoundRect](win32gui.md#win32guiroundrect)

    Draws a rectangle with elliptically rounded corners, filled using using current brush&nbsp;

  - [BeginPaint](win32gui.md#win32guibeginpaint)

    &nbsp;

  - [EndPaint](win32gui.md#win32guiendpaint)

    &nbsp;

  - [BeginPath](win32gui.md#win32guibeginpath)

    Initializes a path in a DC&nbsp;

  - [EndPath](win32gui.md#win32guiendpath)

    Finalizes a path begun by[win32gui::BeginPath](win32gui.md#win32guibeginpath)&nbsp;

  - [AbortPath](win32gui.md#win32guiabortpath)

    Cancels a path begun by[win32gui::BeginPath](win32gui.md#win32guibeginpath)&nbsp;

  - [CloseFigure](win32gui.md#win32guiclosefigure)

    Closes a section of a path by connecting the beginning pos with the current pos&nbsp;

  - [FlattenPath](win32gui.md#win32guiflattenpath)

    Flattens any curves in current path into a series of lines&nbsp;

  - [FillPath](win32gui.md#win32guifillpath)

    Fills a path with currently selected brush&nbsp;

  - [WidenPath](win32gui.md#win32guiwidenpath)

    Widens current path by amount it would increase by if drawn with currently selected pen&nbsp;

  - [StrokePath](win32gui.md#win32guistrokepath)

    Draws current path with currently selected pen&nbsp;

  - [StrokeAndFillPath](win32gui.md#win32guistrokeandfillpath)

    Combines operations of StrokePath and FillPath with no overlap&nbsp;

  - [GetMiterLimit](win32gui.md#win32guigetmiterlimit)

    Retrieves the limit of miter joins for a DC&nbsp;

  - [SetMiterLimit](win32gui.md#win32guisetmiterlimit)

    Set the limit of miter joins for a DC&nbsp;

  - [PathToRegion](win32gui.md#win32guipathtoregion)

    Converts a closed path in a DC to a region&nbsp;

  - [GetPath](win32gui.md#win32guigetpath)

    Returns a sequence of points that describe the current path&nbsp;

  - [CreateRoundRectRgn](win32gui.md#win32guicreateroundrectrgn)

    Create a rectangular region with elliptically rounded corners,&nbsp;

  - [CreateRectRgnIndirect](win32gui.md#win32guicreaterectrgnindirect)

    Creates a rectangular region,&nbsp;

  - [CreateEllipticRgnIndirect](win32gui.md#win32guicreateellipticrgnindirect)

    Creates an ellipse region,&nbsp;

  - [CreateWindowEx](win32gui.md#win32guicreatewindowex)

    Creates a new window with Extended Style.&nbsp;

  - [GetParent](win32gui.md#win32guigetparent)

    Retrieves a handle to the specified child window's parent window.&nbsp;

  - [SetParent](win32gui.md#win32guisetparent)

    changes the parent window of the specified child window.&nbsp;

  - [GetCursorPos](win32gui.md#win32guigetcursorpos)

    retrieves the cursor's position, in screen coordinates.&nbsp;

  - [GetDesktopWindow](win32gui.md#win32guigetdesktopwindow)

    returns the desktop window&nbsp;

  - [GetWindow](win32gui.md#win32guigetwindow)

    returns a window that has the specified relationship (Z order or owner) to the specified window.&nbsp;

  - [GetWindowDC](win32gui.md#win32guigetwindowdc)

    returns the device context (DC) for the entire window, including title bar, menus, and scroll bars.&nbsp;

  - [IsIconic](win32gui.md#win32guiisiconic)

    determines whether the specified window is minimized (iconic).&nbsp;

  - [IsWindow](win32gui.md#win32guiiswindow)

    determines whether the specified window handle identifies an existing window.&nbsp;

  - [IsChild](win32gui.md#win32guiischild)

    Tests whether a window is a child window or descendant window of a specified parent window&nbsp;

  - [ReleaseCapture](win32gui.md#win32guireleasecapture)

    Releases the moust capture for a window.&nbsp;

  - [GetCapture](win32gui.md#win32guigetcapture)

    Returns the window with the mouse capture.&nbsp;

  - [SetCapture](win32gui.md#win32guisetcapture)

    Captures the mouse for the specified window.&nbsp;

  - [_TrackMouseEvent](win32gui.md#win32gui_trackmouseevent)

    Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.&nbsp;

  - [ReleaseDC](win32gui.md#win32guireleasedc)

    Releases a device context.&nbsp;

  - [CreateCaret](win32gui.md#win32guicreatecaret)

    Creates a new caret for a window&nbsp;

  - [DestroyCaret](win32gui.md#win32guidestroycaret)

    Destroys caret for current task&nbsp;

  - [ScrollWindowEx](win32gui.md#win32guiscrollwindowex)

    scrolls the content of the specified window's client area.&nbsp;

  - [SetScrollInfo](win32gui.md#win32guisetscrollinfo)

    Sets information about a scroll-bar&nbsp;

  - [GetScrollInfo](win32gui.md#win32guigetscrollinfo)

    Returns information about a scroll bar&nbsp;

  - [GetClassName](win32gui.md#win32guigetclassname)

    Retrieves the name of the class to which the specified window belongs.&nbsp;

  - [WindowFromPoint](win32gui.md#win32guiwindowfrompoint)

    Retrieves a handle to the window that contains the specified point.&nbsp;

  - [ChildWindowFromPoint](win32gui.md#win32guichildwindowfrompoint)

    Determines which, if any, of the child windows belonging to a parent window contains the specified point.&nbsp;

  - [ChildWindowFromPoint](win32gui.md#win32guichildwindowfrompoint)

    Determines which, if any, of the child windows belonging to a parent window contains the specified point.&nbsp;

  - [ListView_SortItems](win32gui.md#win32guilistview_sortitems)

    Uses an application-defined comparison function to sort the items of a list view control.&nbsp;

  - [ListView_SortItemsEx](win32gui.md#win32guilistview_sortitemsex)

    Uses an application-defined comparison function to sort the items of a list view control.&nbsp;

  - [CreateDC](win32gui.md#win32guicreatedc)

    Creates a device context for a printer or display device&nbsp;

  - [GetSaveFileNameW](win32gui.md#win32guigetsavefilenamew)

    Creates a dialog for user to specify location to save a file or files&nbsp;

  - [GetOpenFileNameW](win32gui.md#win32guigetopenfilenamew)

    Creates a dialog to allow user to select file(s) to open&nbsp;

  - [SystemParametersInfo](win32gui.md#win32guisystemparametersinfo)

    Queries or sets system-wide parameters. This function can also update the user profile while setting a parameter.&nbsp;

  - [SetLayeredWindowAttributes](win32gui.md#win32guisetlayeredwindowattributes)

    Sets the opacity and transparency color key of a layered window.&nbsp;

  - [GetLayeredWindowAttributes](win32gui.md#win32guigetlayeredwindowattributes)

    Retrieves the layering parameters of a window with the WS_EX_LAYERED extended style&nbsp;

  - [UpdateLayeredWindow](win32gui.md#win32guiupdatelayeredwindow)

    Updates the position, size, shape, content, and translucency of a layered window.&nbsp;

  - [AnimateWindow](win32gui.md#win32guianimatewindow)

    Enables you to produce special effects when showing or hiding windows. There are three types of animation: roll, slide, and alpha-blended fade.&nbsp;

  - [CreateBrushIndirect](win32gui.md#win32guicreatebrushindirect)

    Creates a GDI brush from a LOGBRUSH struct&nbsp;

  - [ExtCreatePen](win32gui.md#win32guiextcreatepen)

    Creates a GDI pen object&nbsp;

  - [DrawTextW](win32gui.md#win32guidrawtextw)

    Draws Unicode text on a device context.&nbsp;

  - [EnumPropsEx](win32gui.md#win32guienumpropsex)

    Enumerates properties attached to a window. 

Each property is passed to a callback function, which receives 4 arguments:
Handle to the window, name of the property, handle to the property data, and Param object passed to this function&nbsp;

  - [RegisterDeviceNotification](win32gui.md#win32guiregisterdevicenotification)

    Registers the device or type of device for which a window will receive notifications.&nbsp;

  - [UnregisterDeviceNotification](win32gui.md#win32guiunregisterdevicenotification)

    Unregisters a Device Notification handle. 

It is generally not necessary to call this function manually, but in some cases, 

handle values may be extracted via the struct module and need to be closed explicitly.&nbsp;

  - [RegisterHotKey](win32gui.md#win32guiregisterhotkey)

    Registers a hotkey for a window&nbsp;

## [win32gui](#win32gui).AbortPath

 __AbortPath( *hdc* __ )
Cancels a path begun by[win32gui::BeginPath](win32gui.md#win32guibeginpath)

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).AlphaBlend

 __AlphaBlend( *Dest*  *, XOriginDest*  *, YOriginDest*  *, WidthDest*  *, HeightDest*  *, Src*  *, XOriginSrc*  *, YOriginSrc*  *, WidthSrc*  *, HeightSrc*  *, blendFunction* __ )
Transfers color information using alpha blending

#### Parameters


  -  *Dest* :[PyHANDLE](#pyhandle)

    Destination device context handle

  -  *XOriginDest* : int

    X pos of dest rect

  -  *YOriginDest* : int

    Y pos of dest rect

  -  *WidthDest* : int

    Width of dest rect

  -  *HeightDest* : int

    Height of dest rect

  -  *Src* :[PyHANDLE](#pyhandle)

    Source DC handle

  -  *XOriginSrc* : int

    X pos of src rect

  -  *YOriginSrc* : int

    Y pos of src rect

  -  *WidthSrc* : int

    Width of src rect

  -  *HeightSrc* : int

    Height of src rect

  -  *blendFunction* :[PyBLENDFUNCTION](#pyblendfunction)

    Alpha blending parameters

## [win32gui](#win32gui).AngleArc

 __AngleArc( *hdc*  *, Y*  *, Y*  *, Radius*  *, StartAngle*  *, SweepAngle* __ )
Draws a line from current pos and a section of a circle's arc

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Y* : int

    x pos of circle

  -  *Y* : int

    y pos of circle

  -  *Radius* : int

    Radius of circle

  -  *StartAngle* : float

    Angle where arc starts, in degrees

  -  *SweepAngle* : float

    Angle that arc covers, in degrees

## [win32gui](#win32gui).AnimateWindow

 __AnimateWindow( *hwnd*  *, Time*  *, Flags* __ )
Enables you to produce special effects when showing or hiding windows. There are three types of animation: roll, slide, and alpha-blended fade.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    handle to window

  -  *Time* : int

    Duration of animation in ms

  -  *Flags* : int

    Animation type, combination of win32con.AW_* flags

#### Comments
This function is available on Win2k and later
Accepts keyword args

## [win32gui](#win32gui).AppendMenu

 __AppendMenu(__ )


## [win32gui](#win32gui).Arc

 __Arc( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect*  *, XRadial1*  *, YRadial1*  *, XRadial2*  *, YRadial2* __ )
Draws an arc defined by an ellipse and 2 radials

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context on which to draw

  -  *LeftRect* : int

    Left limit of ellipse

  -  *TopRect* : int

    Top limit of ellipse

  -  *RightRect* : int

    Right limit of ellipse

  -  *BottomRect* : int

    Bottom limit of ellipse

  -  *XRadial1* : int

    Horizontal pos of Radial1 endpoint

  -  *YRadial1* : int

    Vertical pos of Radial1 endpoint

  -  *XRadial2* : int

    Horizontal pos of Radial2 endpoint

  -  *YRadial2* : int

    Vertical pos of Radial2 endpoint

## [win32gui](#win32gui).ArcTo

 __ArcTo( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect*  *, XRadial1*  *, YRadial1*  *, XRadial2*  *, YRadial2* __ )
Draws an arc defined by an ellipse and 2 radials

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context on which to draw

  -  *LeftRect* : int

    Left limit of ellipse

  -  *TopRect* : int

    Top limit of ellipse

  -  *RightRect* : int

    Right limit of ellipse

  -  *BottomRect* : int

    Bottom limit of ellipse

  -  *XRadial1* : int

    Horizontal pos of Radial1 endpoint

  -  *YRadial1* : int

    Vertical pos of Radial1 endpoint

  -  *XRadial2* : int

    Horizontal pos of Radial2 endpoint

  -  *YRadial2* : int

    Vertical pos of Radial2 endpoint

#### Comments
Draws exactly as[win32gui::Arc](win32gui.md#win32guiarc), but changes current drawing position

## [win32gui](#win32gui).BeginPaint

hdc, paintstruct = __BeginPaint(__ )


## [win32gui](#win32gui).BeginPath

 __BeginPath( *hdc* __ )
Initializes a path in a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).BitBlt

 __BitBlt( *hdcDest*  *, x*  *, y*  *, width*  *, height*  *, hdcSrc*  *, nXSrc*  *, nYSrc*  *, dwRop* __ )
Performs a bit-block transfer of the color data corresponding 

to a rectangle of pixels from the specified source device context into a 

destination device context.

#### Parameters


  -  *hdcDest* : int

    handle to destination DC

  -  *x* : int

    x-coord of destination upper-left corner

  -  *y* : int

    y-coord of destination upper-left corner

  -  *width* : int

    width of destination rectangle

  -  *height* : int

    height of destination rectangle

  -  *hdcSrc* : int

    handle to source DC

  -  *nXSrc* : int

    x-coordinate of source upper-left corner

  -  *nYSrc* : int

    y-coordinate of source upper-left corner

  -  *dwRop* : int

    raster operation code

## [win32gui](#win32gui).BringWindowToTop

 __BringWindowToTop( *hwnd* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

## CLR_NONE
 __const win32gui.CLR_NONE;__ 


## [win32gui](#win32gui).CallWindowProc

int = __CallWindowProc( *wndproc*  *, hwnd*  *, msg*  *, wparam*  *, lparam* __ )


#### Parameters


  -  *wndproc* : int

    The wndproc to call - this is generally the return value of SetWindowLong(GWL_WNDPROC)

  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to the window

  -  *msg* : int

    A window message

  -  *wparam* : int/str

    Type is dependent on the message

  -  *lparam* : int/str

    Type is dependent on the message

## [win32gui](#win32gui).CheckMenuItem

int = __CheckMenuItem(__ )


## [win32gui](#win32gui).CheckMenuRadioItem

 __CheckMenuRadioItem( *hMenu*  *, idFirst*  *, idLast*  *, idCheck*  *, uFlags* __ )
Checks a specified menu item and makes it a 

radio item. At the same time, the function clears all other menu items in 

the associated group and clears the radio-item type flag for those items.

#### Parameters


  -  *hMenu* : int

    handle to menu

  -  *idFirst* : int

    identifier or position of first item

  -  *idLast* : int

    identifier or position of last item

  -  *idCheck* : int

    identifier or position of item to check

  -  *uFlags* : int

    options

## [win32gui](#win32gui).ChildWindowFromPoint

int = __ChildWindowFromPoint( *hwndParent*  *, point* __ )
Determines which, if any, of the child windows belonging to a parent window contains the specified point.

#### Parameters


  -  *hwndParent* : int

    The parent.

  -  *point* : (int, int)

    The point.

## [win32gui](#win32gui).ChildWindowFromPoint

int = __ChildWindowFromPoint( *hwndParent*  *, point*  *, flags* __ )
Determines which, if any, of the child windows belonging to a parent window contains the specified point.

#### Parameters


  -  *hwndParent* : int

    The parent.

  -  *point* : (int, int)

    The point.

  -  *flags* : int

    Specifies which child windows to skip. This parameter can be one or more of the CWP_* constants.

## [win32gui](#win32gui).Chord

 __Chord( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect*  *, XRadial1*  *, YRadial1*  *, XRadial2*  *, YRadial2* __ )
Draws a chord defined by an ellipse and 2 radials

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context on which to draw

  -  *LeftRect* : int

    Left limit of ellipse

  -  *TopRect* : int

    Top limit of ellipse

  -  *RightRect* : int

    Right limit of ellipse

  -  *BottomRect* : int

    Bottom limit of ellipse

  -  *XRadial1* : int

    Horizontal pos of Radial1 endpoint

  -  *YRadial1* : int

    Vertical pos of Radial1 endpoint

  -  *XRadial2* : int

    Horizontal pos of Radial2 endpoint

  -  *YRadial2* : int

    Vertical pos of Radial2 endpoint

## [win32gui](#win32gui).ClientToScreen

(int,int) = __ClientToScreen( *hWnd*  *, Point* __ )
Convert client coordinates to screen coords

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *Point* : (int,int)

    Client coordinates to be converted

## [win32gui](#win32gui).CloseFigure

 __CloseFigure( *hdc* __ )
Closes a section of a path by connecting the beginning pos with the current pos

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains an open path. See[win32gui::BeginPath](win32gui.md#win32guibeginpath).

## [win32gui](#win32gui).CloseWindow

 __CloseWindow(__ )


## [win32gui](#win32gui).CombineRgn

int = __CombineRgn( *Dest*  *, Src1*  *, Src2*  *, CombineMode* __ )
Combines two regions

#### Parameters


  -  *Dest* :[PyGdiHandle](#pygdihandle)

    Handle to existing region that will receive combined region

  -  *Src1* :[PyGdiHandle](#pygdihandle)

    Handle to first region

  -  *Src2* :[PyGdiHandle](#pygdihandle)

    Handle to second region

  -  *CombineMode* : int

    One of RGN_AND,RGN_COPY,RGN_DIFF,RGN_OR,RGN_XOR

#### Return Value
Returns the type of region created, one of NULLREGION, SIMPLEREGION, COMPLEXREGION

## [win32gui](#win32gui).CombineTransform

[PyXFORM](#pyxform)= __CombineTransform( *xform1*  *, xform2* __ )
Combines two coordinate space transformations

#### Parameters


  -  *xform1* :[PyXFORM](#pyxform)

    First transformation

  -  *xform2* :[PyXFORM](#pyxform)

    Second transformation

## [win32gui](#win32gui).CommDlgExtendedError

int = __CommDlgExtendedError(__ )


## [win32gui](#win32gui).CopyIcon

HICON = __CopyIcon( *hicon* __ )
Copies an icon

#### Parameters


  -  *hicon* : int

    Existing icon

## [win32gui](#win32gui).CreateAcceleratorTable

HACCEL = __CreateAcceleratorTable( *accels* __ )
Creates an accelerator table

#### Parameters


  -  *accels* : ( (int, int, int), ...)

    A sequence of (fVirt, key, cmd), 

as per the Win32 ACCEL structure.

## [win32gui](#win32gui).CreateBitmap

[PyGdiHANDLE](#pygdihandle)= __CreateBitmap( *width*  *, height*  *, cPlanes*  *, cBitsPerPixel*  *, bitmap bits* __ )
Creates a bitmap

#### Parameters


  -  *width* : int

    bitmap width, in pixels

  -  *height* : int

    bitmap height, in pixels

  -  *cPlanes* : int

    number of color planes

  -  *cBitsPerPixel* : int

    number of bits to identify color

  -  *bitmap bits* : None

    Must be None

## [win32gui](#win32gui).CreateBrushIndirect

[PyGdiHANDLE](#pygdihandle)= __CreateBrushIndirect( *lb* __ )
Creates a GDI brush from a LOGBRUSH struct

#### Parameters


  -  *lb* :[PyLOGBRUSH](#pylogbrush)

    Dict containing brush creation parameters

## [win32gui](#win32gui).CreateCaret

 __CreateCaret( *hWnd*  *, hBitmap*  *, nWidth*  *, nHeight* __ )
Creates a new caret for a window

#### Parameters


  -  *hWnd* : int

    handle to owner window

  -  *hBitmap* :[PyGdiHANDLE](#pygdihandle)

    handle to bitmap for caret shape

  -  *nWidth* : int

    caret width

  -  *nHeight* : int

    caret height

## [win32gui](#win32gui).CreateCompatibleBitmap

[PyGdiHANDLE](#pygdihandle)= __CreateCompatibleBitmap( *hdc*  *, width*  *, height* __ )
Creates a bitmap compatible with the device that is associated with the specified device context.

#### Parameters


  -  *hdc* : int

    handle to DC

  -  *width* : int

    width of bitmap, in pixels

  -  *height* : int

    height of bitmap, in pixels

## [win32gui](#win32gui).CreateCompatibleDC

HDC = __CreateCompatibleDC( *dc* __ )
Creates a memory device context (DC) compatible with the specified device.

#### Parameters


  -  *dc* : int

    handle to DC

## [win32gui](#win32gui).CreateDC

int = __CreateDC( *Driver*  *, Device*  *, InitData* __ )
Creates a device context for a printer or display device

#### Parameters


  -  *Driver* : string

    Name of display or print provider, usually DISPLAY or WINSPOOL

  -  *Device* : string

    Name of specific device, eg printer name returned from GetDefaultPrinter

  -  *InitData* :[PyDEVMODE](#pydevmode)

    A PyDEVMODE that specifies printing parameters, use None for printer defaults

## [win32gui](#win32gui).CreateDialogIndirect

int = __CreateDialogIndirect( *hInstance*  *, controlList*  *, hWndParent*  *, DialogFunc*  *, InitParam* __ )
Creates a modeless dialog box from a template, see[win32ui::CreateDialogIndirect](win32ui.md#win32uicreatedialogindirect)

#### Parameters


  -  *hInstance* :[PyHANDLE](#pyhandle)

    Handle to module creating the dialog box

  -  *controlList* :[PyDialogTemplate](#pydialogtemplate)

    Sequence containing a[PyDLGTEMPLATE](#pydlgtemplate), followed by variable number of[PyDLGITEMTEMPLATE](#pydlgitemtemplate)s

  -  *hWndParent* :[PyHANDLE](#pyhandle)

    Handle to dialog's parent window

  -  *DialogFunc* : function

    Dialog box procedure to process messages

  -  *InitParam=0* : int

    Initialization data to be passed to above procedure during WM_INITDIALOG processing

## [win32gui](#win32gui).CreateEllipticRgnIndirect

[PyGdiHandle](#pygdihandle)= __CreateEllipticRgnIndirect( *rc* __ )
Creates an ellipse region,

#### Parameters


  -  *rc* :[PyRECT](#pyrect)

    Coordinates of bounding rectangle in logical units

## [win32gui](#win32gui).CreateFontIndirect

[PyGdiHandle](#pygdihandle)= __CreateFontIndirect( *lplf* __ )
function creates a logical font that has the specified characteristics. 

The font can subsequently be selected as the current font for any device context.

#### Parameters


  -  *lplf* :[PyLOGFONT](#pylogfont)

    A LOGFONT object as returned by[win32gui::LOGFONT](win32gui.md#win32guilogfont)

## [win32gui](#win32gui).CreateHatchBrush

[PyGdiHANDLE](#pygdihandle)= __CreateHatchBrush( *Style*  *, clrref* __ )
Creates a hatch brush with specified style and color

#### Parameters


  -  *Style* : int

    Hatch style, one of win32con.HS_* constants

  -  *clrref* : int

    Rgb color value.  See[win32api::RGB](win32api.md#win32apirgb).

## [win32gui](#win32gui).CreateIconFromResource

[PyHANDLE](#pyhandle)= __CreateIconFromResource( *bits*  *, fIcon*  *, ver* __ )
Creates an icon or cursor from resource bits describing the icon.

#### Parameters


  -  *bits* : string

    The bits

  -  *fIcon* : bool

    True if an icon, False if a cursor.

  -  *ver=0x00030000* : int

    Specifies the version number of the icon or cursor 

format for the resource bits pointed to by the presbits parameter. 

This parameter can be 0x00030000.

## [win32gui](#win32gui).CreateIconIndirect

int = __CreateIconIndirect( *iconinfo* __ )
Creates an icon or cursor from an ICONINFO structure.

#### Parameters


  -  *iconinfo* :[PyICONINFO](#pyiconinfo)

    Tuple defining the icon parameters

## [win32gui](#win32gui).CreateMenu

int = __CreateMenu(__ )


#### Return Value
The result is a HMENU to the new menu.

## [win32gui](#win32gui).CreatePatternBrush

[PyGdiHANDLE](#pygdihandle)= __CreatePatternBrush( *hbmp* __ )
Creates a brush using a bitmap as a pattern

#### Parameters


  -  *hbmp* :[PyGdiHANDLE](#pygdihandle)

    Handle to a bitmap

## [win32gui](#win32gui).CreatePen

[PyGdiHANDLE](#pygdihandle)= __CreatePen( *PenStyle*  *, Width*  *, Color* __ )
Create a GDI pen

#### Parameters


  -  *PenStyle* : int

    One of win32con.PS_* pen styles

  -  *Width* : int

    Drawing width in logical units.  Use zero for single pixel.

  -  *Color* : int

    RGB color value.  See[win32api::RGB](win32api.md#win32apirgb).

## [win32gui](#win32gui).CreatePolygonRgn

[PyGdiHANDLE](#pygdihandle)= __CreatePolygonRgn( *Points*  *, PolyFillMode* __ )
Creates a region from a sequence of vertices

#### Parameters


  -  *Points* : [(int,int),...]

    Sequence of POINT tuples: ((x,y),...).

  -  *PolyFillMode* : int

    Filling mode, one of ALTERNATE, WINDING

## [win32gui](#win32gui).CreatePopupMenu

int = __CreatePopupMenu(__ )


#### Return Value
The result is a HMENU to the new menu.

## [win32gui](#win32gui).CreateRectRgnIndirect

[PyGdiHandle](#pygdihandle)= __CreateRectRgnIndirect( *rc* __ )
Creates a rectangular region,

#### Parameters


  -  *rc* :[PyRECT](#pyrect)

    Coordinates of rectangle

## [win32gui](#win32gui).CreateRoundRectRgn

[PyGdiHandle](#pygdihandle)= __CreateRoundRectRgn( *LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect*  *, WidthEllipse*  *, HeightEllipse* __ )
Create a rectangular region with elliptically rounded corners,

#### Parameters


  -  *LeftRect* : int

    Position of left edge of rectangle

  -  *TopRect* : int

    Position of top edge of rectangle

  -  *RightRect* : int

    Position of right edge of rectangle

  -  *BottomRect* : int

    Position of bottom edge of rectangle

  -  *WidthEllipse* : int

    Width of ellipse

  -  *HeightEllipse* : int

    Height of ellipse

## [win32gui](#win32gui).CreateSolidBrush

[PyGdiHANDLE](#pygdihandle)= __CreateSolidBrush( *Color* __ )
Creates a solid brush of specified color

#### Parameters


  -  *Color* : int

    RGB color value.  See[win32api::RGB](win32api.md#win32apirgb).

## [win32gui](#win32gui).CreateWindow

int = __CreateWindow( *className*  *, windowTitle*  *, style*  *, x*  *, y*  *, width*  *, height*  *, parent*  *, menu*  *, hinstance*  *, reserved* __ )
Creates a new window.

#### Parameters


  -  *className* : int/string

    

  -  *windowTitle* : string

    

  -  *style* : int

    The style for the window.

  -  *x* : int

    

  -  *y* : int

    

  -  *width* : int

    

  -  *height* : int

    

  -  *parent* : int

    Handle to the parent window.

  -  *menu* : int

    Handle to the menu to use for this window.

  -  *hinstance* : int

    

  -  *reserved* : None

    Must be None

## [win32gui](#win32gui).CreateWindowEx

int = __CreateWindowEx( *dwExStyle*  *, className*  *, windowTitle*  *, style*  *, x*  *, y*  *, width*  *, height*  *, parent*  *, menu*  *, hinstance*  *, reserved* __ )
Creates a new window with Extended Style.

#### Parameters


  -  *dwExStyle* : int

    extended window style

  -  *className* : int/string

    

  -  *windowTitle* : string

    

  -  *style* : int

    The style for the window.

  -  *x* : int

    

  -  *y* : int

    

  -  *width* : int

    

  -  *height* : int

    

  -  *parent* : int

    Handle to the parent window.

  -  *menu* : int

    Handle to the menu to use for this window.

  -  *hinstance* : int

    

  -  *reserved* : None

    Must be None

## [win32gui](#win32gui).DefWindowProc

int = __DefWindowProc( *hwnd*  *, message*  *, wparam*  *, lparam* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the Window

  -  *message* : int

    The ID of the message to send

  -  *wparam* : int

    An integer whose value depends on the message

  -  *lparam* : int

    An integer whose value depends on the message

## [win32gui](#win32gui).DeleteDC

 __DeleteDC( *hdc* __ )
Deletes a DC

#### Parameters


  -  *hdc* : int

    The source DC

## [win32gui](#win32gui).DeleteMenu

 __DeleteMenu( *hmenu*  *, position*  *, flags* __ )


#### Parameters


  -  *hmenu* : int

    The handle to the menu

  -  *position* : int

    The position to delete.

  -  *flags* : int

    

## [win32gui](#win32gui).DeleteObject

 __DeleteObject( *handle* __ )
Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.

#### Parameters


  -  *handle* :[PyGdiHANDLE](#pygdihandle)

    handle to the object to delete.

## [win32gui](#win32gui).DestroyAccleratorTable

 __DestroyAccleratorTable( *haccel* __ )
Destroys an accelerator table

#### Parameters


  -  *haccel* : int

    

## [win32gui](#win32gui).DestroyCaret

 __DestroyCaret(__ )
Destroys caret for current task

## [win32gui](#win32gui).DestroyIcon

 __DestroyIcon( *hicon* __ )


#### Parameters


  -  *hicon* : int

    The icon to destroy.

## [win32gui](#win32gui).DestroyMenu

 __DestroyMenu(__ )
Destroys a previously loaded menu.

## [win32gui](#win32gui).DestroyWindow

 __DestroyWindow( *hwnd* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).DialogBox

int = __DialogBox( *hInstance*  *, TemplateName*  *, hWndParent*  *, DialogFunc*  *, InitParam* __ )
Creates a modal dialog box.

#### Parameters


  -  *hInstance* :[PyHANDLE](#pyhandle)

    Handle to module that contains the dialog template

  -  *TemplateName* :[PyResourceId](#pyresourceid)

    Name or resource id of the dialog resource

  -  *hWndParent* :[PyHANDLE](#pyhandle)

    Handle to dialog's parent window

  -  *DialogFunc* : function

    Dialog box procedure to process messages

  -  *InitParam=0* : int

    Initialization data to be passed to above procedure during WM_INITDIALOG processing

## [win32gui](#win32gui).DialogBoxIndirect

int = __DialogBoxIndirect( *hInstance*  *, controlList*  *, hWndParent*  *, DialogFunc*  *, InitParam* __ )
Creates a modal dialog box from a template, see[win32ui::CreateDialogIndirect](win32ui.md#win32uicreatedialogindirect)

#### Parameters


  -  *hInstance* :[PyHANDLE](#pyhandle)

    Handle to module creating the dialog box

  -  *controlList* :[PyDialogTemplate](#pydialogtemplate)

    Sequence of items defining the dialog box and subcontrols

  -  *hWndParent* :[PyHANDLE](#pyhandle)

    Handle to dialog's parent window

  -  *DialogFunc* : function

    Dialog box procedure to process messages

  -  *InitParam=0* : long

    Initialization data to be passed to above procedure during WM_INITDIALOG processing

## [win32gui](#win32gui).DialogBoxIndirectParam

int = __DialogBoxIndirectParam(__ )
See[win32gui::DialogBoxIndirect](win32gui.md#win32guidialogboxindirect)

## [win32gui](#win32gui).DialogBoxIndirectParam

int = __DialogBoxIndirectParam(__ )
See[win32gui::CreateDialogIndirect](win32gui.md#win32guicreatedialogindirect)

## [win32gui](#win32gui).DialogBoxParam

int = __DialogBoxParam(__ )
See[win32gui::DialogBox](win32gui.md#win32guidialogbox)

## [win32gui](#win32gui).DispatchMessage

int = __DispatchMessage( *msg* __ )


#### Parameters


  -  *msg* : MSG

    

## [win32gui](#win32gui).DragAcceptFiles

 __DragAcceptFiles( *hwnd*  *, fAccept* __ )
Registers whether a window accepts dropped files.

#### Parameters


  -  *hwnd* : int

    Handle to the Window

  -  *fAccept* : int

    Value that indicates if the window identified by the hWnd parameter accepts dropped files. 

This value is True to accept dropped files or False to discontinue accepting dropped files.

## [win32gui](#win32gui).DragDetect

 __DragDetect( *hwnd*  *, point* __ )
captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point.

#### Parameters


  -  *hwnd* : int

    Handle to the Window

  -  *point* : (int, int)

    Initial position of the mouse, in screen coordinates. The function determines the coordinates of the drag rectangle by using this point.

#### Return Value
If the user moved the mouse outside of the drag rectangle while holding down the left button , the return value is nonzero.
If the user did not move the mouse outside of the drag rectangle while holding down the left button , the return value is zero.

## [win32gui](#win32gui).DrawAnimatedRects

 __DrawAnimatedRects( *hwnd*  *, idAni*  *, minCoords*  *, restCoords* __ )
Animates a rectangle in the manner of minimizing, mazimizing, or opening

#### Parameters


  -  *hwnd* : int

    handle to clipping window

  -  *idAni* : int

    type of animation, win32con.IDANI_*

  -  *minCoords* :[PyRECT](#pyrect)

    rectangle coordinates (minimized)

  -  *restCoords* :[PyRECT](#pyrect)

    rectangle coordinates (restored)

## [win32gui](#win32gui).DrawEdge

[PyRECT](#pyrect)= __DrawEdge( *hdc*  *, rc*  *, edge*  *, Flags* __ )
Draws edge(s) of a rectangle

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *rc* :[PyRECT](#pyrect)

    Rectangle whose edge(s) will be drawn

  -  *edge* : int

    Combination of win32con.BDR_* flags, or one of win32con.EDGE_* flags

  -  *Flags* : int

    Combination of win32con.BF_* flags

#### Return Value
BF_ADJUST flag causes input rectange to be shrunk by size of border.. Rectangle is always returned.

## [win32gui](#win32gui).DrawFocusRect

 __DrawFocusRect( *hDC*  *, rc* __ )
Draws a standard focus outline around a rectangle

#### Parameters


  -  *hDC* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *rc* : (int, int, int,int)

    Tuple of (left,top,right,bottom) defining the rectangle

## [win32gui](#win32gui).DrawIcon

 __DrawIcon( *hDC*  *, X*  *, Y*  *, hicon* __ )
Draws an icon or cursor into the specified device context. 

To specify additional drawing options, use the[win32gui::DrawIconEx](win32gui.md#win32guidrawiconex)function.

#### Parameters


  -  *hDC* : int

    handle to DC

  -  *X* : int

    x-coordinate of upper-left corner

  -  *Y* : int

    y-coordinate of upper-left corner

  -  *hicon* : int

    handle to icon

## [win32gui](#win32gui).DrawIconEx

 __DrawIconEx( *hDC*  *, xLeft*  *, yTop*  *, hIcon*  *, cxWidth*  *, cyWidth*  *, istepIfAniCur*  *, hbrFlickerFreeDraw*  *, diFlags* __ )
Draws an icon or cursor into the specified device context, 

performing the specified raster operations, and stretching or compressing the 

icon or cursor as specified.

#### Parameters


  -  *hDC* : int

    handle to device context

  -  *xLeft* : int

    x-coord of upper left corner

  -  *yTop* : int

    y-coord of upper left corner

  -  *hIcon* : int

    handle to icon

  -  *cxWidth* : int

    icon width

  -  *cyWidth* : int

    icon height

  -  *istepIfAniCur* : int

    frame index, animated cursor

  -  *hbrFlickerFreeDraw* :[PyGdiHANDLE](#pygdihandle)

    handle to background brush, can be None

  -  *diFlags* : int

    icon-drawing flags (win32con.DI_*)

## [win32gui](#win32gui).DrawMenuBar

 __DrawMenuBar( *hwnd* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).DrawText

(int,[PyRECT](#pyrect)) = __DrawText( *hDC*  *, String*  *, nCount*  *, Rect*  *, Format* __ )
Draws formatted text on a device context

#### Parameters


  -  *hDC* : int/[PyHANDLE](#pyhandle)

    The device context on which to draw

  -  *String* : str

    The text to be drawn

  -  *nCount* : int

    The number of characters, use -1 for simple null-terminated string

  -  *Rect* :[PyRECT](#pyrect)

    Tuple of 4 ints specifying the position (left, top, right, bottom)

  -  *Format* : int

    Formatting flags, combination of win32con.DT_* values

#### Return Value
Returns the height of the drawn text, and the rectangle coordinates

## [win32gui](#win32gui).DrawTextW

int,[PyRECT](#pyrect)= __DrawTextW( *hDC*  *, String*  *, Count*  *, Rect*  *, Format* __ )
Draws Unicode text on a device context.

#### Parameters


  -  *hDC* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *String* :[PyUnicode](#pyunicode)

    Text to be drawn

  -  *Count* : int

    Number of characters to draw, use -1 for entire null terminated string

  -  *Rect* :[PyRECT](#pyrect)

    Rectangle in which to draw text

  -  *Format* : int

    Formatting flags, combination of win32con.DT_* values

#### Comments
Accepts keyword args.

#### Return Value
Returns the height of the drawn text, and the rectangle coordinates

## [win32gui](#win32gui).Ellipse

 __Ellipse( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect* __ )
Draws a filled ellipse on a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context on which to draw

  -  *LeftRect* : int

    Left limit of ellipse

  -  *TopRect* : int

    Top limit of ellipse

  -  *RightRect* : int

    Right limit of ellipse

  -  *BottomRect* : int

    Bottom limit of ellipse

## [win32gui](#win32gui).EnableMenuItem

 __EnableMenuItem(__ )


## [win32gui](#win32gui).EnableWindow

int = __EnableWindow( *hWnd*  *, bEnable* __ )
Enables and disables keyboard and mouse input to a window

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to window

  -  *bEnable* : boolean

    True to enable input to the window, False to disable input

#### Return Value
Returns True if window was already disabled when call was made, False otherwise

## [win32gui](#win32gui).EndDialog

 __EndDialog( *hwnd*  *, result* __ )
Ends a dialog box.

#### Parameters


  -  *hwnd* : int

    Handle to the window.

  -  *result* : int

    result

## [win32gui](#win32gui).EndPaint

 __EndPaint( *hwnd*  *, ps* __ )


#### Parameters


  -  *hwnd* : int

    

  -  *ps* : paintstruct

    As returned from[win32gui::BeginPaint](win32gui.md#win32guibeginpaint)

## [win32gui](#win32gui).EndPath

 __EndPath( *hdc* __ )
Finalizes a path begun by[win32gui::BeginPath](win32gui.md#win32guibeginpath)

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).EnumChildWindows

 __EnumChildWindows( *hwnd*  *, callback*  *, extra* __ )
Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    The handle to the window to enumerate.

  -  *callback* : object

    A Python function to be used as the callback.

  -  *extra* : object

    Any python object - this is passed to the callback function as the second param (first is the hwnd).

## [win32gui](#win32gui).EnumFontFamilies

int = __EnumFontFamilies( *hdc*  *, Family*  *, EnumFontFamProc*  *, Param* __ )
Enumerates the available font families.

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context for which to enumerate available fonts

  -  *Family* : string/[PyUnicode](#pyunicode)

    Family of fonts to enumerate. If none, first member of each font family will be returned.

  -  *EnumFontFamProc* : function

    The Python function called with each font family. This function is called with 4 arguments.

  -  *Param* : object

    An arbitrary object to be passed to the callback function

#### Comments
The parameters that the callback function will receive are as follows:
[PyLOGFONT](#pylogfont)- contains the font parameters
None - Placeholder for a TEXTMETRIC structure, not supported yet
int - Font type, combination of DEVICE_FONTTYPE, RASTER_FONTTYPE, TRUETYPE_FONTTYPE
object - The Param originally passed in to EnumFontFamilies

## [win32gui](#win32gui).EnumPropsEx

 __EnumPropsEx( *hWnd*  *, EnumFunc*  *, Param* __ )
Enumerates properties attached to a window. 

Each property is passed to a callback function, which receives 4 arguments:
Handle to the window, name of the property, handle to the property data, and Param object passed to this function

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *EnumFunc* : function

    Callback function

  -  *Param* : object

    Arbitrary object to be passed to callback function

## [win32gui](#win32gui).EnumThreadWindows

 __EnumThreadWindows( *dwThreadId*  *, callback*  *, extra* __ )
Enumerates all top-level windows associated with a thread on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE

#### Parameters


  -  *dwThreadId* : int

    The id of the thread for which the windows need to be enumerated.

  -  *callback* : object

    A Python function to be used as the callback.

  -  *extra* : object

    Any python object - this is passed to the callback function as the second param (first is the hwnd).

## [win32gui](#win32gui).EnumWindows

 __EnumWindows( *callback*  *, extra* __ )
Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.

#### Parameters


  -  *callback* : function

    A Python function to be used as the callback.  Function can return False to stop enumeration, or raise an exception.

  -  *extra* : object

    Any python object - this is passed to the callback function as the second param (first is the hwnd).

## [win32gui](#win32gui).EqualRgn

boolean = __EqualRgn( *SrcRgn1*  *, SrcRgn2* __ )
Determines if 2 regions are equal

#### Parameters


  -  *SrcRgn1* :[PyGdiHandle](#pygdihandle)

    Handle to a region

  -  *SrcRgn2* :[PyGdiHandle](#pygdihandle)

    Handle to a region

## [win32gui](#win32gui).ExtCreatePen

[PyHANDLE](#pyhandle)= __ExtCreatePen( *PenStyle*  *, Width*  *, lb*  *, Style* __ )
Creates a GDI pen object

#### Parameters


  -  *PenStyle* : int

    Combination of win32con.PS_*.  Must contain either PS_GEOMETRIC or PS_COSMETIC.

  -  *Width* : int

    Width of pen in logical units.  Must be 1 for PS_COSMETIC.

  -  *lb* :[PyLOGBRUSH](#pylogbrush)

    Dict containing brush creation parameters

  -  *Style=None* : (int, ...)

    Sequence containing lengths of dashes and spaces  Used only with PS_USERSTYLE, otherwise must be None.

## [win32gui](#win32gui).ExtFloodFill

 __ExtFloodFill( **  *, XStart*  *, YStart*  *, Color*  *, FillType* __ )
Fills an area with current brush

#### Parameters


  -  *=hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *XStart* : int

    Horizontal starting pos

  -  *YStart* : int

    Vertical starting pos

  -  *Color* : int

    RGB color value.  See[win32api::RGB](win32api.md#win32apirgb).

  -  *FillType* : int

    One of win32con.FLOODFILL* values

## [win32gui](#win32gui).ExtTextOut

int = __ExtTextOut( *hdc*  *, int*  *, int*  *, int*  *, rect*  *, string*  *, tuple* __ )
Writes text to a DC.

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *int* : x

    The x coordinate to write the text to.

  -  *int* : y

    The y coordinate to write the text to.

  -  *int* : nOptions

    Specifies the rectangle type. This parameter can be one, both, or neither of ETO_CLIPPED and ETO_OPAQUE

  -  *rect* :[PyRECT](#pyrect)

    Specifies the text's bounding rectangle.  (Can be None.)

  -  *string* : text

    The text to write.

  -  *tuple* : (width1, width2, ...)

    Optional array of values that indicate distance between origins of character cells.

#### Win32 API References


  - Search for *ExtTextOut* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=exttextout),[google](#http://www.google.com/search?q=exttextout)or[google groups](#http://groups.google.com/groups?q=exttextout).

#### Return Value
Always none.  If the function fails, an exception is raised.

## [win32gui](#win32gui).ExtractIcon

int = __ExtractIcon( *hinstance*  *, moduleName*  *, index* __ )


#### Parameters


  -  *hinstance* : int

    

  -  *moduleName* : string/[PyUnicode](#pyunicode)

    

  -  *index* : int

    

#### Comments
You must destroy the icon handle returned by calling the[win32gui::DestroyIcon](win32gui.md#win32guidestroyicon)function.

#### Return Value
The result is a HICON.

## [win32gui](#win32gui).ExtractIconEx

int = __ExtractIconEx( *moduleName*  *, index*  *, numIcons* __ )


#### Parameters


  -  *moduleName* : string

    

  -  *index* : int

    

  -  *numIcons=1* : int

    

#### Comments
You must destroy each icon handle returned by calling the[win32gui::DestroyIcon](win32gui.md#win32guidestroyicon)function.

#### Return Value
If index==-1, the result is an integer with the number of icons in 

the file, otherwise it is 2 arrays of icon handles.

## [win32gui](#win32gui).FillPath

 __FillPath( *hdc* __ )
Fills a path with currently selected brush

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains a finalized path. See[win32gui::EndPath](win32gui.md#win32guiendpath).

#### Comments
Any open figures are closed and path is deselected from the DC.

## [win32gui](#win32gui).FillRect

 __FillRect( *hDC*  *, rc*  *, hbr* __ )
Fills a rectangular area with specified brush

#### Parameters


  -  *hDC* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *rc* :[PyRECT](#pyrect)

    Rectangle to be filled

  -  *hbr* :[PyGdiHANDLE](#pygdihandle)

    Handle to brush to be used to fill area

## [win32gui](#win32gui).FillRgn

 __FillRgn( *hdc*  *, hrgn*  *, hbr* __ )
Fills a region with specified brush

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to the device context

  -  *hrgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to the region

  -  *hbr* :[PyGdiHANDLE](#pygdihandle)

    Brush to be used

## [win32gui](#win32gui).FindWindow

[PyHANDLE](#pyhandle)= __FindWindow( *ClassName*  *, WindowName* __ )
Retrieves a handle to the top-level window whose class name and window name match the specified strings.

#### Parameters


  -  *ClassName* :[PyResourceId](#pyresourceid)

    Name or atom of window class to find, can be None

  -  *WindowName* : string

    Title of window to find, can be None

## [win32gui](#win32gui).FindWindowEx

[PyHANDLE](#pyhandle)= __FindWindowEx( *Parent*  *, ChildAfter*  *, ClassName*  *, WindowName* __ )
Retrieves a handle to the top-level window whose class name and window name match the specified strings.

#### Parameters


  -  *Parent* :[PyHANDLE](#pyhandle)

    Window whose child windows will be searched.  If 0, desktop window is assumed.

  -  *ChildAfter* :[PyHANDLE](#pyhandle)

    Child window after which to search in Z-order, can be 0 to search all

  -  *ClassName* :[PyResourceId](#pyresourceid)

    Name or atom of window class to find, can be None

  -  *WindowName* : string

    Title of window to find, can be None

## [win32gui](#win32gui).FlashWindow

int = __FlashWindow( *hwnd*  *, bInvert* __ )
The FlashWindow function flashes the specified window one time. It does not change the active state of the window.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *bInvert* : int

    Indicates if window should toggle between active and inactive

## [win32gui](#win32gui).FlashWindowEx

int = __FlashWindowEx( *hwnd*  *, dwFlags*  *, uCount*  *, dwTimeout* __ )
The FlashWindowEx function flashes the specified window a specified number of times.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *dwFlags* : int

    Combination of win32con.FLASHW_* flags

  -  *uCount* : int

    Nbr of times to flash

  -  *dwTimeout* : int

    Elapsed time between flashes, in milliseconds

## [win32gui](#win32gui).FlattenPath

 __FlattenPath( *hdc* __ )
Flattens any curves in current path into a series of lines

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains a closed path. See[win32gui::EndPath](win32gui.md#win32guiendpath).

## [win32gui](#win32gui).FrameRect

 __FrameRect( *hDC*  *, rc*  *, hbr* __ )
Draws an outline around a rectangle

#### Parameters


  -  *hDC* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *rc* :[PyRECT](#pyrect)

    Rectangle around which to draw

  -  *hbr* :[PyGdiHANDLE](#pygdihandle)

    Handle to brush created using CreateHatchBrush, CreatePatternBrush, CreateSolidBrush, or GetStockObject

## [win32gui](#win32gui).FrameRgn

 __FrameRgn( *hdc*  *, hrgn*  *, hbr*  *, Width*  *, Height* __ )
Draws a frame around a region

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to the device context

  -  *hrgn* :[PyGdiHandle](#pygdihandle)

    Handle to the region

  -  *hbr* :[PyGdiHandle](#pygdihandle)

    Handle to brush to be used

  -  *Width* : int

    Frame width

  -  *Height* : int

    Frame height

## [win32gui](#win32gui).GetActiveWindow

HWND = __GetActiveWindow(__ )


## [win32gui](#win32gui).GetArcDirection

int = __GetArcDirection( *hdc* __ )
Returns the direction in which rectangles and arcs are drawn

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Recturns one of win32con.AD_* values

## [win32gui](#win32gui).GetBkColor

int = __GetBkColor( *hdc* __ )
Returns the background color for a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns an RGB color value.  On error, returns CLR_INVALID.

## [win32gui](#win32gui).GetBkMode

int = __GetBkMode( *hdc* __ )
Returns the background mode for a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns OPAQUE, TRANSPARENT, or 0 on failure

## [win32gui](#win32gui).GetCapture

int = __GetCapture(__ )
Returns the window with the mouse capture.

## [win32gui](#win32gui).GetCaretPos

int,int = __GetCaretPos(__ )
Returns the current caret position

## [win32gui](#win32gui).GetClassLong

int = __GetClassLong( *hwnd*  *, index* __ )


#### Parameters


  -  *hwnd* : int

    

  -  *index* : int

    

## [win32gui](#win32gui).GetClassName

string = __GetClassName( *hwnd* __ )
Retrieves the name of the class to which the specified window belongs.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    The handle to the window

## [win32gui](#win32gui).GetClientRect

(left, top, right, bottom) = __GetClientRect( *hwnd* __ )
Returns the rectangle of the client area of a window, in client coordinates

#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).GetCurrentObject

[PyHANDLE](#pyhandle)= __GetCurrentObject( *hdc*  *, ObjectType* __ )
Retrieves currently selected object from a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *ObjectType* : int

    Type of object to retrieve, one of win32con.OBJ_*;

## [win32gui](#win32gui).GetCurrentPositionEx

(int,int) = __GetCurrentPositionEx( *hdc* __ )
Returns a device context's current drawing position

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context

## [win32gui](#win32gui).GetCursor

HCURSOR = __GetCursor(__ )


## [win32gui](#win32gui).GetCursorInfo

flags, hcursor, (x,y) = __GetCursorInfo(__ )
Retrieves information about the global cursor.

## [win32gui](#win32gui).GetCursorPos

(int, int) = __GetCursorPos(__ )
retrieves the cursor's position, in screen coordinates.

## [win32gui](#win32gui).GetDC

HDC = __GetDC( *hwnd* __ )
Gets the device context for the window.

#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).GetDesktopWindow

int = __GetDesktopWindow(__ )
returns the desktop window

## [win32gui](#win32gui).GetDlgCtrlID

int = __GetDlgCtrlID( *hwnd* __ )
Retrieves the identifier of the specified control.

#### Parameters


  -  *hwnd* : int

    The handle to the control

## [win32gui](#win32gui).GetDlgItem

HWND = __GetDlgItem( *hDlg*  *, IDDlgItem* __ )
Retrieves the handle to a control in the specified dialog box.

#### Parameters


  -  *hDlg* :[PyHANDLE](#pyhandle)

    Handle to a dialog window

  -  *IDDlgItem* : int

    Identifier of one of the dialog's controls

## [win32gui](#win32gui).GetDlgItemInt

 __GetDlgItemInt( *hDlg*  *, IDDlgItem*  *, Signed* __ )
Returns the integer value of a dialog control

#### Parameters


  -  *hDlg* :[PyHANDLE](#pyhandle)

    Handle to a dialog window

  -  *IDDlgItem* : int

    Identifier of one of the dialog's controls

  -  *Signed* : boolean

    Indicates whether control value should be interpreted as signed

## [win32gui](#win32gui).GetDlgItemText

string = __GetDlgItemText( *hDlg*  *, IDDlgItem* __ )
Returns the text of a dialog control

#### Parameters


  -  *hDlg* :[PyHANDLE](#pyhandle)

    Handle to a dialog window

  -  *IDDlgItem* : int

    The Id of a control within the dialog

## [win32gui](#win32gui).GetDoubleClickTime

int = __GetDoubleClickTime(__ )


## [win32gui](#win32gui).GetFocus

 __GetFocus(__ )
Returns the HWND of the window with focus.

## [win32gui](#win32gui).GetForegroundWindow

HWND = __GetForegroundWindow(__ )


## [win32gui](#win32gui).GetGraphicsMode

int = __GetGraphicsMode( *hdc* __ )
Determines if advanced GDI features are enabled for a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns GM_COMPATIBLE or GM_ADVANCED

## [win32gui](#win32gui).GetIconInfo

[PyICONINFO](#pyiconinfo)= __GetIconInfo( *hicon* __ )
Returns parameters for an icon or cursor

#### Parameters


  -  *hicon* :[PyHANDLE](#pyhandle)

    The icon to query

#### Return Value
The result is a tuple of (fIcon, xHotspot, yHotspot, hbmMask, hbmColor) 

The hbmMask and hbmColor items are bitmaps created for the caller, so must be freed.

## [win32gui](#win32gui).GetLayeredWindowAttributes

(int,int,int) = __GetLayeredWindowAttributes( *hwnd* __ )
Retrieves the layering parameters of a window with the WS_EX_LAYERED extended style

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    Handle to a layered window

#### Comments
This function only exists on WinXP and later.
Accepts keyword arguments.

#### Return Value
Returns a tuple of (color key, alpha, flags)

## [win32gui](#win32gui).GetLayout

int = __GetLayout( *hdc* __ )
Retrieves the layout mode of a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns one of win32con.LAYOUT_*

## [win32gui](#win32gui).GetMapMode

int = __GetMapMode( *hdc* __ )
Returns the method a device context uses to translate logical units to physical units

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns one of win32con.MM_* values

## [win32gui](#win32gui).GetMenu

 __GetMenu(__ )
Gets the menu for the specified window.

## [win32gui](#win32gui).GetMenuDefaultItem

int = __GetMenuDefaultItem( *hMenu*  *, fByPos*  *, flags* __ )


#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *fByPos* : int

    

  -  *flags* : int

    

## [win32gui](#win32gui).GetMenuInfo

 __GetMenuInfo( *hmenu*  *, info* __ )
Gets information about a specified menu.

#### Parameters


  -  *hmenu* : int

    handle to menu

  -  *info* : buffer

    A buffer to fill with the information.

#### Comments
See win32gui_struct for helper functions.
This function will raise NotImplementedError on early platforms (eg, Windows NT.)

## [win32gui](#win32gui).GetMenuItemCount

int = __GetMenuItemCount( *hMenu* __ )


#### Parameters


  -  *hMenu* : int

    Handle to the menu

## [win32gui](#win32gui).GetMenuItemID

int = __GetMenuItemID( *hMenu*  *, nPos* __ )
Retrieves the menu item identifier of a menu item located at the specified position in a menu.

#### Parameters


  -  *hMenu* : int

    handle to menu

  -  *nPos* : int

    position of menu item

## [win32gui](#win32gui).GetMenuItemInfo

 __GetMenuItemInfo( *hMenu*  *, uItem*  *, fByPosition*  *, menuItem* __ )
Gets menu information

#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *uItem* : int

    The menu item identifier or the menu item position.

  -  *fByPosition* : int

    Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.

  -  *menuItem* : buffer

    A string or buffer in the format of a __MENUITEMINFO__ structure.

## [win32gui](#win32gui).GetMenuItemRect

(int, int, int, int) = __GetMenuItemRect( *hWnd*  *, hMenu*  *, uItem* __ )


#### Parameters


  -  *hWnd* : int

    

  -  *hMenu* : int

    Handle to the menu

  -  *uItem* : int

    

## [win32gui](#win32gui).GetMenuState

int = __GetMenuState( *hMenu*  *, uID*  *, flags* __ )


#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *uID* : int

    

  -  *flags* : int

    

## [win32gui](#win32gui).GetMessage

MSG = __GetMessage( *hwnd*  *, min*  *, max* __ )


#### Parameters


  -  *hwnd* : int

    

  -  *min* : int

    

  -  *max* : int

    

## [win32gui](#win32gui).GetMiterLimit

float = __GetMiterLimit( *hdc* __ )
Retrieves the limit of miter joins for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).GetNextDlgGroupItem

HWND = __GetNextDlgGroupItem( *hDlg*  *, hCtl*  *, bPrevious* __ )
Retrieves a handle to the first control in a group of controls that precedes (or follows) the specified control in a dialog box.

#### Parameters


  -  *hDlg* : int

    handle to dialog box

  -  *hCtl* : int

    handle to known control

  -  *bPrevious* : int

    direction flag

## [win32gui](#win32gui).GetNextDlgTabItem

HWND = __GetNextDlgTabItem( *hDlg*  *, hCtl*  *, bPrevious* __ )
Retrieves a handle to the first control that has the WS_TABSTOP style that precedes (or follows) the specified control.

#### Parameters


  -  *hDlg* : int

    handle to dialog box

  -  *hCtl* : int

    handle to known control

  -  *bPrevious* : int

    direction flag

## [win32gui](#win32gui).GetObject

object = __GetObject( *handle* __ )
Returns a struct containing the parameters used to create a GDI object

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    Handle to the object.

#### Comments
The result depends on the type of the handle.


## [win32gui](#win32gui).GetObjectType

int = __GetObjectType( *h* __ )
Returns the type (OBJ_* constant) of a GDI handle

#### Parameters


  -  *h* :[PyHANDLE](#pyhandle)

    A handle to a GDI object

## [win32gui](#win32gui).GetOpenFileName

int = __GetOpenFileName( *OPENFILENAME* __ )
Creates an Open dialog box that lets the user specify the drive, directory, and the name of a file or set of files to open.

#### Parameters


  -  *OPENFILENAME* : string/bytes

    A string packed into an OPENFILENAME structure, probably via the struct module.

#### Comments
The[win32gui::GetOpenFileNameW](win32gui.md#win32guigetopenfilenamew)function is far more convenient to use.

#### Return Value
If the user presses OK, the function returns TRUE.  Otherwise, use CommDlgExtendedError for error details 

(ie, a win32gui.error is raised).  If the user cancels the dialog, the winerror attribute of the exception will be zero.

## [win32gui](#win32gui).GetOpenFileNameW

([PyUNICODE](#pyunicode),[PyUNICODE](#pyunicode), int) = __GetOpenFileNameW( *hwndOwner*  *, hInstance*  *, Filter*  *, CustomFilter*  *, FilterIndex*  *, File*  *, MaxFile*  *, InitialDir*  *, Title*  *, Flags*  *, DefExt*  *, TemplateName* __ )
Creates a dialog to allow user to select file(s) to open

#### Parameters


  -  *hwndOwner=None* :[PyHANDLE](#pyhandle)

    Handle to window that owns dialog

  -  *hInstance=None* :[PyHANDLE](#pyhandle)

    Handle to module that contains dialog template

  -  *Filter=None* :[PyUNICODE](#pyunicode)

    Contains pairs of descriptions and filespecs separated by NULLS, with a final trailing NULL. 

Example: 'Python Scripts\\0*.py;*.pyw;*.pys\\0Text files\\0*.txt\\0'

  -  *CustomFilter=None* :[PyUNICODE](#pyunicode)

    Description to be used for filter that user selected or typed, can also contain a filespec as above

  -  *FilterIndex=0* : int

    Specifies which of the filters is initially selected, use 0 for CustomFilter

  -  *File=None* :[PyUNICODE](#pyunicode)

    The file name initially displayed

  -  *MaxFile=1024* : int

    Number of characters to allocate for selected filename, override if large number of files expected

  -  *InitialDir=None* :[PyUNICODE](#pyunicode)

    The starting directory

  -  *Title=None* :[PyUNICODE](#pyunicode)

    The title of the dialog box

  -  *Flags=0* : int

    Combination of win32con.OFN_* constants

  -  *DefExt=None* :[PyUNICODE](#pyunicode)

    The default extension to use

  -  *TemplateName=None* :[PyResourceId](#pyresourceid)

    Name or resource id of dialog box template

#### Comments
Accepts keyword arguments, all arguments optional 

Input parameters and return values are identical to[win32gui::GetSaveFileNameW](win32gui.md#win32guigetsavefilenamew)

## [win32gui](#win32gui).GetParent

int = __GetParent( *child* __ )
Retrieves a handle to the specified child window's parent window.

#### Parameters


  -  *child* : int

    handle to child window

## [win32gui](#win32gui).GetPath

tuple,tuple = __GetPath( *hdc* __ )
Returns a sequence of points that describe the current path

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context containing a finalized path.  See[win32gui::EndPath](win32gui.md#win32guiendpath)

#### Return Value
Returns a sequence of POINT tuples, and a sequence of ints designating each point's function (combination of win32con.PT_* values)

## [win32gui](#win32gui).GetPixel

int = __GetPixel( *hdc*  *, XPos*  *, YPos* __ )
Returns the RGB color of a single pixel

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *XPos* : int

    Horizontal pos

  -  *YPos* : int

    Vertical pos

## [win32gui](#win32gui).GetPolyFillMode

int = __GetPolyFillMode( *hdc* __ )
Returns the polygon filling mode for a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns win32con.ALTERNATE or win32con.WINDING

## [win32gui](#win32gui).GetROP2

int = __GetROP2( *hdc* __ )
Returns the foreground mixing mode of a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns one of win32con.R2_* values

## [win32gui](#win32gui).GetRgnBox

int,[PyRECT](#pyrect)= __GetRgnBox( *hrgn* __ )
Calculates the bounding box of a region

#### Parameters


  -  *hrgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to a region

#### Return Value
Returns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION) and rectangle in logical units

## [win32gui](#win32gui).GetSaveFileNameW

([PyUNICODE](#pyunicode),[PyUNICODE](#pyunicode),int) = __GetSaveFileNameW( *hwndOwner*  *, hInstance*  *, Filter*  *, CustomFilter*  *, FilterIndex*  *, File*  *, MaxFile*  *, InitialDir*  *, Title*  *, Flags*  *, DefExt*  *, TemplateName* __ )
Creates a dialog for user to specify location to save a file or files

#### Parameters


  -  *hwndOwner=None* :[PyHANDLE](#pyhandle)

    Handle to window that owns dialog

  -  *hInstance=None* :[PyHANDLE](#pyhandle)

    Handle to module that contains dialog template

  -  *Filter=None* :[PyUNICODE](#pyunicode)

    Contains pairs of descriptions and filespecs separated by NULLS, with a final trailing NULL. 

Example: 'Python Scripts\\0*.py;*.pyw;*.pys\\0Text files\\0*.txt\\0'

  -  *CustomFilter=None* :[PyUNICODE](#pyunicode)

    Description to be used for filter that user selected or typed, can also contain a filespec as above

  -  *FilterIndex=0* : int

    Specifies which of the filters is initially selected, use 0 for CustomFilter

  -  *File=None* :[PyUNICODE](#pyunicode)

    The file name initially displayed

  -  *MaxFile=1024* : int

    Number of characters to allocate for selected filename(s), override if large number of files expected

  -  *InitialDir=None* :[PyUNICODE](#pyunicode)

    The starting directory

  -  *Title=None* :[PyUNICODE](#pyunicode)

    The title of the dialog box

  -  *Flags=0* : int

    Combination of win32con.OFN_* constants

  -  *DefExt=None* :[PyUNICODE](#pyunicode)

    The default extension to use

  -  *TemplateName=None* :[PyResourceId](#pyresourceid)

    Name or resource id of dialog box template

#### Comments
Accepts keyword arguments, all arguments optional

#### Return Value
Returns a tuple of 3 values ([PyUNICODE](#pyunicode),[PyUNICODE](#pyunicode), int):
First is the selected file(s). If multiple files are selected, returned string will be the directory followed by files names 

separated by nulls, otherwise it will be the full path.  In other words, if you use the OFN_ALLOWMULTISELECT flag 

you should split this value on \\0 characters and if the length of the result list is 1, it will be 

the full path, otherwise element 0 will be the directory and the rest of the elements will be filenames in 

this directory.
Second is a unicode string containing user-selected filter, will be None if CustomFilter was not specified
Third item contains flags pertaining to users input, such as OFN_READONLY and OFN_EXTENSIONDIFFERENT
If the user presses cancel or an error occurs, a 

win32gui.error is raised.  If the user pressed cancel, the error number (ie, the winerror attribute of the exception) will be zero.

## [win32gui](#win32gui).GetScrollInfo

[PySCROLLINFO](#pyscrollinfo)= __GetScrollInfo( *hwnd*  *, nBar*  *, mask* __ )
Returns information about a scroll bar

#### Parameters


  -  *hwnd* : int

    The handle to the window.

  -  *nBar* : int

    The scroll bar to examine.  Can be one of win32con.SB_CTL, win32con.SB_VERT or win32con.SB_HORZ

  -  *mask=SIF_ALL* : int

    The mask for attributes to retrieve.

## [win32gui](#win32gui).GetStockObject

[PyHANDLE](#pyhandle)= __GetStockObject( *Object* __ )
Creates a handle to one of the standard system Gdi objects

#### Parameters


  -  *Object* : int

    One of *_BRUSH, *_PEN, *_FONT, or *_PALLETTE constants

## [win32gui](#win32gui).GetStretchBltMode

int = __GetStretchBltMode( *hdc* __ )
Returns the stretching mode used by[win32gui::StretchBlt](win32gui.md#win32guistretchblt)

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns one of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS,WHITEONBLACK, or 0 on error.

## [win32gui](#win32gui).GetSubMenu

HMENU = __GetSubMenu( *hMenu*  *, nPos* __ )


#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *nPos* : int

    

## [win32gui](#win32gui).GetSysColor

int = __GetSysColor( *Index* __ )
Returns the color of a window element

#### Parameters


  -  *Index* : int

    One of win32con.COLOR_* values

## [win32gui](#win32gui).GetSysColorBrush

[PyGdiHANDLE](#pygdihandle)= __GetSysColorBrush( *Index* __ )
Creates a handle to a system color brush

#### Parameters


  -  *Index* : int

    Index of a window element color (win32con.COLOR_*)

## [win32gui](#win32gui).GetSystemMenu

int = __GetSystemMenu( *hwnd*  *, bRevert* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

  -  *bRevert* : int

    

#### Return Value
The result is a HMENU to the menu.

## [win32gui](#win32gui).GetTextAlign

int = __GetTextAlign( *hdc* __ )
Returns horizontal and vertical alignment for text in a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns combination of win32con.TA_* flags

## [win32gui](#win32gui).GetTextCharacterExtra

int = __GetTextCharacterExtra( *hdc* __ )
Returns the space between characters

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).GetTextColor

int = __GetTextColor( *hdc* __ )
Returns the text color for a DC

#### Parameters


  -  *hdc* : int

    Handle to a device context

#### Return Value
Returns an RGB color.  On error, returns CLR_INVALID

## [win32gui](#win32gui).GetTextExtentPoint32

cx, cy = __GetTextExtentPoint32( *hdc*  *, str* __ )
Computes the width and height of the specified string of text.

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    The device context

  -  *str* : string

    The string to measure.

## [win32gui](#win32gui).GetTextFace

[PyUnicode](#pyunicode)= __GetTextFace( *hdc* __ )
Retrieves the name of the font currently selected in a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Comments
Calls unicode api function (GetTextFaceW)

## [win32gui](#win32gui).GetTextMetrics

dict = __GetTextMetrics(__ )
Returns info for the font selected into a DC

## [win32gui](#win32gui).GetUpdateRgn

int = __GetUpdateRgn( *hWnd*  *, hRgn*  *, Erase* __ )
Copies the update region of a window into an existing region

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *hRgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to an existing region to receive update area

  -  *Erase* : boolean

    Indicates if window background is to be erased

#### Return Value
Returns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION

## [win32gui](#win32gui).GetViewportExtEx

(int,int) = __GetViewportExtEx( *hdc* __ )
Retrieves the viewport extents for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns the extents as (x,y) in logical units

## [win32gui](#win32gui).GetViewportOrgEx

(int,int) = __GetViewportOrgEx( *hdc* __ )
Retrievs the origin for a DC's viewport

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).GetWindow

int = __GetWindow( *hWnd*  *, uCmd* __ )
returns a window that has the specified relationship (Z order or owner) to the specified window.

#### Parameters


  -  *hWnd* : int

    handle to original window

  -  *uCmd* : int

    relationship flag

## [win32gui](#win32gui).GetWindowDC

int = __GetWindowDC( *hWnd* __ )
returns the device context (DC) for the entire window, including title bar, menus, and scroll bars.

#### Parameters


  -  *hWnd* : int

    handle of window

## [win32gui](#win32gui).GetWindowExtEx

(int,int) = __GetWindowExtEx( *hdc* __ )
Retrieves the window extents for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns the extents as (x,y) in logical units

## [win32gui](#win32gui).GetWindowLong

int = __GetWindowLong( *hwnd*  *, index* __ )


#### Parameters


  -  *hwnd* : int

    

  -  *index* : int

    

## [win32gui](#win32gui).GetWindowOrgEx

(int,int) = __GetWindowOrgEx( *hdc* __ )
Retrievs the window origin for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).GetWindowPlacement

tuple = __GetWindowPlacement(__ )
Returns placement information about the current window.

#### Return Value
The result is a tuple of 

(flags, showCmd, (minposX, minposY), (maxposX, maxposY), (normalposX, normalposY))


## [win32gui](#win32gui).GetWindowRect

(left, top, right, bottom) = __GetWindowRect( *hwnd* __ )
Returns the rectangle for a window in screen coordinates

#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).GetWindowRgn

int = __GetWindowRgn( *hWnd*  *, hRgn* __ )
Copies the window region of a window into an existing region

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *hRgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to an existing region that receives window region

#### Return Value
Returns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION

## [win32gui](#win32gui).GetWindowRgnBox

int,[PyRECT](#pyrect)= __GetWindowRgnBox( *hWnd* __ )
Returns the bounding box for a window's region

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window that has a window region. (see[win32gui::SetWindowRgn](win32gui.md#win32guisetwindowrgn))

#### Comments
Only available in winxpgui

#### Return Value
Returns type of region and rectangle coordinates in device units

## [win32gui](#win32gui).GetWindowText

string = __GetWindowText( *hwnd* __ )
Get the window text.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    The handle to the window

#### Comments
Note that previous versions of PyWin32 returned a (empty) Unicode 

object when the string was empty, or an MBCS encoded string value 

otherwise.  A String is now returned in all cases.

## [win32gui](#win32gui).GetWorldTransform

[PyXFORM](#pyxform)= __GetWorldTransform( *hdc* __ )
Retrieves a device context's coordinate space translation matrix

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Comments
DC's mode must be set to GM_ADVANCED.  See[win32gui::SetGraphicsMode](win32gui.md#win32guisetgraphicsmode).

## [win32gui](#win32gui).GradientFill

 __GradientFill( *hdc*  *, Vertex*  *, Mesh*  *, Mode* __ )
Shades triangles or rectangles by interpolating between vertex colors

#### Parameters


  -  *hdc* : int

    Handle to device context

  -  *Vertex* : ([PyTRIVERTEX](#pytrivertex),...)

    Sequence of TRIVERTEX dicts defining color info

  -  *Mesh* : tuple

    Sequence of tuples containing either 2 or 3 ints that index into the trivertex array to define either triangles or rectangles

  -  *Mode* : int

    win32con.GRADIENT_FILL_* value defining whether to fill by triangle or by rectangle

## [win32gui](#win32gui).HideCaret

 __HideCaret( *hWnd* __ )
Hides the caret

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Window that owns the caret, can be 0.

## ILC_COLOR
 __const win32gui.ILC_COLOR;__ 


## ILC_COLOR16
 __const win32gui.ILC_COLOR16;__ 


## ILC_COLOR24
 __const win32gui.ILC_COLOR24;__ 


## ILC_COLOR32
 __const win32gui.ILC_COLOR32;__ 


## ILC_COLOR4
 __const win32gui.ILC_COLOR4;__ 


## ILC_COLOR8
 __const win32gui.ILC_COLOR8;__ 


## ILC_COLORDDB
 __const win32gui.ILC_COLORDDB;__ 


## ILC_MASK
 __const win32gui.ILC_MASK;__ 


## ILD_BLEND
 __const win32gui.ILD_BLEND;__ 


## ILD_BLEND25
 __const win32gui.ILD_BLEND25;__ 


## ILD_BLEND50
 __const win32gui.ILD_BLEND50;__ 


## ILD_FOCUS
 __const win32gui.ILD_FOCUS;__ 


## ILD_MASK
 __const win32gui.ILD_MASK;__ 


## ILD_NORMAL
 __const win32gui.ILD_NORMAL;__ 


## ILD_SELECTED
 __const win32gui.ILD_SELECTED;__ 


## ILD_TRANSPARENT
 __const win32gui.ILD_TRANSPARENT;__ 


## IMAGE_BITMAP
 __const win32gui.IMAGE_BITMAP;__ 


## IMAGE_CURSOR
 __const win32gui.IMAGE_CURSOR;__ 


## IMAGE_ICON
 __const win32gui.IMAGE_ICON;__ 


## [win32gui](#win32gui).ImageList_Add

int = __ImageList_Add( *himl*  *, hbmImage*  *, hbmMask* __ )
Adds an image or images to an image list.

#### Parameters


  -  *himl* : int

    Handle to the image list.

  -  *hbmImage* :[PyGdiHANDLE](#pygdihandle)

    Handle to the bitmap that contains the image or images. The number of images is inferred from the width of the bitmap.

  -  *hbmMask* :[PyGdiHANDLE](#pygdihandle)

    Handle to the bitmap that contains the mask. If no mask is used with the image list, this parameter is ignored

#### Return Value
Returns the index of the first new image if successful, or -1 otherwise.

## [win32gui](#win32gui).ImageList_Create

HIMAGELIST = __ImageList_Create(__ )
Create an image list

## [win32gui](#win32gui).ImageList_Destroy

BOOL = __ImageList_Destroy(__ )
Destroy an imagelist

## [win32gui](#win32gui).ImageList_Draw

BOOL = __ImageList_Draw(__ )
Draw an image on an HDC

## [win32gui](#win32gui).ImageList_DrawEx

BOOL = __ImageList_DrawEx(__ )
Draw an image on an HDC

## [win32gui](#win32gui).ImageList_GetIcon

HICON = __ImageList_GetIcon(__ )
Extract an icon from an imagelist

## [win32gui](#win32gui).ImageList_GetImageCount

int = __ImageList_GetImageCount(__ )
Return count of images in imagelist

## [win32gui](#win32gui).ImageList_LoadBitmap

HANDLE = __ImageList_LoadBitmap(__ )
Creates an image list from the specified bitmap resource.

## [win32gui](#win32gui).ImageList_LoadImage

HANDLE = __ImageList_LoadImage(__ )
Loads bitmaps, cursors or icons, creates imagelist

## [win32gui](#win32gui).ImageList_Remove

BOOL = __ImageList_Remove(__ )
Remove an image from an imagelist

## [win32gui](#win32gui).ImageList_Replace

BOOL = __ImageList_Replace(__ )
Replace an image in an imagelist with a bitmap image

## [win32gui](#win32gui).ImageList_ReplaceIcon

BOOL = __ImageList_ReplaceIcon(__ )
Replace an image in an imagelist with an icon image

## [win32gui](#win32gui).ImageList_SetBkColor

COLORREF = __ImageList_SetBkColor(__ )
Set the background color for the imagelist

## [win32gui](#win32gui).ImageList_SetOverlayImage

 __ImageList_SetOverlayImage( *hImageList*  *, iImage*  *, iOverlay* __ )
Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image.

#### Parameters


  -  *hImageList* : int

    

  -  *iImage* : int

    

  -  *iOverlay* : int

    

## [win32gui](#win32gui).InitCommonControls

 __InitCommonControls(__ )
Initializes the common controls.

## [win32gui](#win32gui).InitCommonControlsEx

 __InitCommonControlsEx( *flag* __ )
Initializes specific common controls.

#### Parameters


  -  *flag* : int

    One of the ICC_ constants

## [win32gui](#win32gui).InsertMenu

 __InsertMenu(__ )


## [win32gui](#win32gui).InsertMenuItem

 __InsertMenuItem( *hMenu*  *, uItem*  *, fByPosition*  *, menuItem* __ )
Inserts a menu item

#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *uItem* : int

    The menu item identifier or the menu item position.

  -  *fByPosition* : int

    Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.

  -  *menuItem* : buffer

    A string or buffer in the format of a __MENUITEMINFO__ structure.

## [win32gui](#win32gui).InvalidateRect

 __InvalidateRect( *hWnd*  *, Rect*  *, Erase* __ )
Invalidates a rectangular area of a window and adds it to the window's update region

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to the window

  -  *Rect* :[PyRECT](#pyrect)

    Client coordinates defining area to be redrawn.  Use None for entire client area.

  -  *Erase* : boolean

    Indicates if background should be erased

## [win32gui](#win32gui).InvalidateRgn

 __InvalidateRgn( *hWnd*  *, hRgn*  *, Erase* __ )
Adds a region to a window's update region

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to the window

  -  *hRgn* :[PyGdiHANDLE](#pygdihandle)

    Region to be redrawn

  -  *Erase* : boolean

    Indidates if background should be erased

## [win32gui](#win32gui).InvertRect

 __InvertRect( *hDC*  *, rc* __ )
Inverts the colors in a regtangular region

#### Parameters


  -  *hDC* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *rc* :[PyRECT](#pyrect)

    Coordinates of rectangle to invert

## [win32gui](#win32gui).InvertRgn

 __InvertRgn( *hdc*  *, hrgn* __ )
Inverts the colors in a region

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to the device context

  -  *hrgn* :[PyGdiHandle](#pygdihandle)

    Handle to the region

## [win32gui](#win32gui).IsChild

 __IsChild( *hWndParent*  *, hWnd* __ )
Tests whether a window is a child window or descendant window of a specified parent window

#### Parameters


  -  *hWndParent* : int

    handle to parent window

  -  *hWnd* : int

    handle to window to test

## [win32gui](#win32gui).IsIconic

 __IsIconic( *hWnd* __ )
determines whether the specified window is minimized (iconic).

#### Parameters


  -  *hWnd* : int

    handle to window

## [win32gui](#win32gui).IsWindow

 __IsWindow( *hWnd* __ )
determines whether the specified window handle identifies an existing window.

#### Parameters


  -  *hWnd* : int

    handle to window

## [win32gui](#win32gui).IsWindowEnabled

int = __IsWindowEnabled( *hwnd* __ )
Indicates if the window is enabled.

#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).IsWindowVisible

int = __IsWindowVisible( *hwnd* __ )
Indicates if the window has the WS_VISIBLE style.

#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).LOGFONT

[PyLOGFONT](#pylogfont)= __LOGFONT(__ )
Creates a LOGFONT object.

## LR_CREATEDIBSECTION
 __const win32gui.LR_CREATEDIBSECTION;__ 


## LR_DEFAULTCOLOR
 __const win32gui.LR_DEFAULTCOLOR;__ 


## LR_DEFAULTSIZE
 __const win32gui.LR_DEFAULTSIZE;__ 


## LR_LOADFROMFILE
 __const win32gui.LR_LOADFROMFILE;__ 


## LR_LOADMAP3DCOLORS
 __const win32gui.LR_LOADMAP3DCOLORS;__ 


## LR_LOADTRANSPARENT
 __const win32gui.LR_LOADTRANSPARENT;__ 


## LR_MONOCHROME
 __const win32gui.LR_MONOCHROME;__ 


## LR_SHARED
 __const win32gui.LR_SHARED;__ 


## LR_VGACOLOR
 __const win32gui.LR_VGACOLOR;__ 


## [win32gui](#win32gui).LineTo

 __LineTo( *hdc*  *, XEnd*  *, YEnd* __ )
Draw a line from current position to specified point

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *XEnd* : int

    Horizontal position in logical units

  -  *YEnd* : int

    Vertical position in logical units

## [win32gui](#win32gui).ListView_SortItems

 __ListView_SortItems( *hwnd*  *, callback*  *, param* __ )
Uses an application-defined comparison function to sort the items of a list view control.

#### Parameters


  -  *hwnd* : int

    The handle to the window

  -  *callback* : object

    A callback object, taking 3 params.

  -  *param=None* : object

    The third param to the callback function.

## [win32gui](#win32gui).ListView_SortItemsEx

 __ListView_SortItemsEx( *hwnd*  *, callback*  *, param* __ )
Uses an application-defined comparison function to sort the items of a list view control.

#### Parameters


  -  *hwnd* : int

    The handle to the window

  -  *callback* : object

    A callback object, taking 3 params.

  -  *param=None* : object

    The third param to the callback function.

## [win32gui](#win32gui).LoadCursor

HCURSOR = __LoadCursor( *hinstance*  *, resid* __ )
Loads a cursor.

#### Parameters


  -  *hinstance* : int

    The module to load from

  -  *resid* : int

    The resource ID

## [win32gui](#win32gui).LoadIcon

HCURSOR = __LoadIcon( *hinstance*  *, resource_id* __ )
Loads an icon

#### Parameters


  -  *hinstance* : int

    

  -  *resource_id* : int/string

    

## [win32gui](#win32gui).LoadImage

HANDLE = __LoadImage( *hinst*  *, name*  *, type*  *, cxDesired*  *, cyDesired*  *, fuLoad* __ )
Loads a bitmap, cursor or icon

#### Parameters


  -  *hinst* : int

    Handle to an instance of the module that contains the image to be loaded. To load an OEM image, set this parameter to zero.

  -  *name* : int/string

    Specifies the image to load. If the hInst parameter is non-zero and the fuLoad parameter omits LR_LOADFROMFILE, name specifies the image resource in the hInst module. If the image resource is to be loaded by name, the name parameter is a string that contains the name of the image resource.

  -  *type* : int

    Specifies the type of image to be loaded.

  -  *cxDesired* : int

    Specifies the width, in pixels, of the icon or cursor. If this parameter is zero and the fuLoad parameter is LR_DEFAULTSIZE, the function uses the SM_CXICON or SM_CXCURSOR system metric value to set the width. If this parameter is zero and LR_DEFAULTSIZE is not used, the function uses the actual resource width.

  -  *cyDesired* : int

    Specifies the height, in pixels, of the icon or cursor. If this parameter is zero and the fuLoad parameter is LR_DEFAULTSIZE, the function uses the SM_CYICON or SM_CYCURSOR system metric value to set the height. If this parameter is zero and LR_DEFAULTSIZE is not used, the function uses the actual resource height.

  -  *fuLoad* : int

    

## [win32gui](#win32gui).LoadMenu

HMENU = __LoadMenu( *hinstance*  *, resource_id* __ )
Loads a menu

#### Parameters


  -  *hinstance* : int

    

  -  *resource_id* : int/string

    

## [win32gui](#win32gui).MaskBlt

 __MaskBlt( *Dest*  *, XDest*  *, YDest*  *, Width*  *, Height*  *, Src*  *, XSrc*  *, YSrc*  *, Mask*  *, xMask*  *, yMask*  *, Rop* __ )
Combines the color data for the source and destination 

bitmaps using the specified mask and raster operation.

#### Parameters


  -  *Dest* :[PyHANDLE](#pyhandle)

    Destination device context handle

  -  *XDest* : int

    X pos of dest rect

  -  *YDest* : int

    Y pos of dest rect

  -  *Width* : int

    Width of rect to be copied

  -  *Height* : int

    Height of rect to be copied

  -  *Src* :[PyHANDLE](#pyhandle)

    Source DC handle

  -  *XSrc* : int

    X pos of src rect

  -  *YSrc* : int

    Y pos of src rect

  -  *Mask* :[PyGdiHANDLE](#pygdihandle)

    Handle to monochrome bitmap used to mask color

  -  *xMask* : int

    X pos in mask

  -  *yMask* : int

    Y pos in mask

  -  *Rop* : int

    Foreground and background raster operations.  See MSDN docs for how to construct this value.

#### Comments
This function is not supported on Win9x.

#### Win32 API References


  - Search for *MaskBlt* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=maskblt),[google](#http://www.google.com/search?q=maskblt)or[google groups](#http://groups.google.com/groups?q=maskblt).

## [win32gui](#win32gui).MessageBeep

 __MessageBeep( *type* __ )
Plays a waveform sound.

#### Parameters


  -  *type* : int

    The type of the beep

## [win32gui](#win32gui).MessageBox

int = __MessageBox( *parent*  *, text*  *, caption*  *, flags* __ )
Displays a message box

#### Parameters


  -  *parent* : int

    The parent window

  -  *text* : string/[PyUnicode](#pyunicode)

    The text for the message box

  -  *caption* : string/[PyUnicode](#pyunicode)

    The caption for the message box

  -  *flags* : int

    

## [win32gui](#win32gui).ModifyMenu

 __ModifyMenu( *hMnu*  *, uPosition*  *, uFlags*  *, uIDNewItem*  *, newItem* __ )
Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item.

#### Parameters


  -  *hMnu* : int

    handle to menu

  -  *uPosition* : int

    menu item to modify

  -  *uFlags* : int

    options

  -  *uIDNewItem* : int

    identifier, menu, or submenu

  -  *newItem* : string

    menu item content

## [win32gui](#win32gui).ModifyWorldTransform

 __ModifyWorldTransform( *hdc*  *, Xform*  *, Mode* __ )
Combines a coordinate tranformation with device context's current transformation

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Xform* :[PyXFORM](#pyxform)

    Transformation to be applied.  Ignored if Mode is MWT_IDENTITY.

  -  *Mode* : int

    One of win32con.MWT_* values specifying how transformations will be combined

#### Comments
DC's mode must be set to GM_ADVANCED.  See[win32gui::SetGraphicsMode](win32gui.md#win32guisetgraphicsmode).

## [win32gui](#win32gui).MoveToEx

(int, int) = __MoveToEx( *hdc*  *, X*  *, Y* __ )
Changes the current drawing position

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context handle

  -  *X* : int

    Horizontal pos in logical units

  -  *Y* : int

    Vertical pos in logical units

#### Return Value
Returns the previous position as (X, Y)

## [win32gui](#win32gui).MoveWindow

 __MoveWindow( *hwnd*  *, x*  *, y*  *, width*  *, height*  *, bRepaint* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

  -  *x* : int

    

  -  *y* : int

    

  -  *width* : int

    

  -  *height* : int

    

  -  *bRepaint* : int

    

## NIF_ICON
 __const win32gui.NIF_ICON;__ 


## NIF_INFO
 __const win32gui.NIF_INFO;__ 


## NIF_MESSAGE
 __const win32gui.NIF_MESSAGE;__ 


## NIF_STATE
 __const win32gui.NIF_STATE;__ 
#define NIF_GUID NIF_GUID

## NIF_TIP
 __const win32gui.NIF_TIP;__ 


## NIIF_ERROR
 __const win32gui.NIIF_ERROR;__ 


## NIIF_ICON_MASK
 __const win32gui.NIIF_ICON_MASK;__ 


## NIIF_INFO
 __const win32gui.NIIF_INFO;__ 
#define NIIF_USER NIIF_USER

## NIIF_NONE
 __const win32gui.NIIF_NONE;__ 


## NIIF_NOSOUND
 __const win32gui.NIIF_NOSOUND;__ 


## NIIF_WARNING
 __const win32gui.NIIF_WARNING;__ 


## NIM_ADD
 __const win32gui.NIM_ADD;__ 
Adds an icon to the status area.

## NIM_DELETE
 __const win32gui.NIM_DELETE;__ 
Deletes an icon from the status area.

## NIM_MODIFY
 __const win32gui.NIM_MODIFY;__ 
Modifies an icon in the status area.

## NIM_SETFOCUS
 __const win32gui.NIM_SETFOCUS;__ 
Give the icon focus.

## NIM_SETVERSION
 __const win32gui.NIM_SETVERSION;__ 


## [win32gui](#win32gui).OffsetRgn

int = __OffsetRgn( *hrgn*  *, XOffset*  *, YOffset* __ )
Relocates a region

#### Parameters


  -  *hrgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to a region

  -  *XOffset* : int

    Horizontal offset

  -  *YOffset* : int

    Vertical offset

#### Return Value
Returns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION)

## [win32gui](#win32gui).PaintDesktop

 __PaintDesktop( *hdc* __ )
Fills a DC with the destop background

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

## [win32gui](#win32gui).PaintRgn

 __PaintRgn( *hdc*  *, hrgn* __ )
Paints a region with current brush

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to the device context

  -  *hrgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to the region

## [win32gui](#win32gui).PatBlt

 __PatBlt( *hdc*  *, XLeft*  *, YLeft*  *, Width*  *, Height*  *, Rop* __ )
Paints a rectangle by combining the current brush with existing colors

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *XLeft* : int

    Horizontal pos

  -  *YLeft* : int

    Vertical pos

  -  *Width* : int

    Width of rectangular area

  -  *Height* : int

    Height of rectangular area

  -  *Rop* : int

    Raster operation, one of PATCOPY,PATINVERT,DSTINVERT,BLACKNESS,WHITENESS

## [win32gui](#win32gui).PathToRegion

[PyGdiHANDLE](#pygdihandle)= __PathToRegion( *hdc* __ )
Converts a closed path in a DC to a region

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains a closed path. See[win32gui::EndPath](win32gui.md#win32guiendpath).

#### Comments
On success, the path is deselected from the DC

## [win32gui](#win32gui).PeekMessage

MSG = __PeekMessage( *hwnd*  *, filterMin*  *, filterMax*  *, removalOptions* __ )


#### Parameters


  -  *hwnd* : int

    

  -  *filterMin* : int

    

  -  *filterMax* : int

    

  -  *removalOptions* : int

    

## [win32gui](#win32gui).Pie

 __Pie( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect*  *, XRadial1*  *, YRadial1*  *, XRadial2*  *, YRadial2* __ )
Draws a section of an ellipse cut by 2 radials

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Device context on which to draw

  -  *LeftRect* : int

    Left limit of ellipse

  -  *TopRect* : int

    Top limit of ellipse

  -  *RightRect* : int

    Right limit of ellipse

  -  *BottomRect* : int

    Bottom limit of ellipse

  -  *XRadial1* : int

    Horizontal pos of Radial1 endpoint

  -  *YRadial1* : int

    Vertical pos of Radial1 endpoint

  -  *XRadial2* : int

    Horizontal pos of Radial2 endpoint

  -  *YRadial2* : int

    Vertical pos of Radial2 endpoint

## [win32gui](#win32gui).PlgBlt

 __PlgBlt( *Dest*  *, Point*  *, Src*  *, XSrc*  *, YSrc*  *, Width*  *, Height*  *, Mask*  *, xMask*  *, yMask* __ )
Copies color from a rectangle into a parallelogram

#### Parameters


  -  *Dest* :[PyHANDLE](#pyhandle)

    Destination DC

  -  *Point* : tuple

    Sequence of 3 POINT tuples (x,y) describing a paralellogram

  -  *Src* :[PyHANDLE](#pyhandle)

    Source device context

  -  *XSrc* : int

    Left edge of source rectangle

  -  *YSrc* : int

    Top of source rectangle

  -  *Width* : int

    Width of source rectangle

  -  *Height* : int

    Height of source rectangle

  -  *Mask=None* :[PyGdiHANDLE](#pygdihandle)

    Handle to monochrome bitmap to mask source, can be None

  -  *xMask=0* : int

    x pos in mask

  -  *yMask=0* : int

    y pos in mask

## [win32gui](#win32gui).PolyBezier

 __PolyBezier( *hdc*  *, Points* __ )
Draws a series of Bezier curves starting from first point specified.

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Points* : [(int,int),...]

    Sequence of POINT tuples: ((x,y),...).

#### Comments
Number of points must be a multiple of 3 plus 1.

## [win32gui](#win32gui).PolyBezierTo

 __PolyBezierTo( *hdc*  *, Points* __ )
Draws a series of Bezier curves starting from current drawing position.

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Points* : [(int,int),...]

    Sequence of POINT tuples: ((x,y),...).

#### Comments
Points must contain 3 points for each curve.  Current position is updated with last endpoint.

## [win32gui](#win32gui).Polygon

 __Polygon( *hdc*  *, Points* __ )
Draws a closed filled polygon defined by a sequence of points

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Points* : [(int,int),...]

    Sequence of POINT tuples: ((x,y),...)

## [win32gui](#win32gui).Polyline

 __Polyline( *hdc*  *, Points* __ )
Connects a sequence of points using currently selected pen

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Points* : [(int,int),...]

    Sequence of POINT tuples: ((x,y),...)

## [win32gui](#win32gui).PolylineTo

 __PolylineTo( *hdc*  *, Points* __ )
Draws a series of lines starting from current position.  Updates current position with end point.

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Points* : [(int,int),...]

    Sequence of POINT tuples: ((x,y),...)

## [win32gui](#win32gui).PostMessage

 __PostMessage( *hwnd*  *, message*  *, wparam*  *, lparam* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the Window

  -  *message* : int

    The ID of the message to post

  -  *wparam=0* : int

    An integer whose value depends on the message

  -  *lparam=0* : int

    An integer whose value depends on the message

## [win32gui](#win32gui).PostQuitMessage

 __PostQuitMessage( *rc* __ )


#### Parameters


  -  *rc* : int

    

## [win32gui](#win32gui).PostThreadMessage

 __PostThreadMessage( *threadId*  *, message*  *, wparam*  *, lparam* __ )


#### Parameters


  -  *threadId* : int

    The ID of the thread to post the message to.

  -  *message* : int

    The ID of the message to post

  -  *wparam* : int

    An integer whose value depends on the message

  -  *lparam* : int

    An integer whose value depends on the message

## [win32gui](#win32gui).PtInRect

boolean = __PtInRect( *rect*  *, point* __ )
Determines if a rectangle contains a point

#### Parameters


  -  *rect* : (int, int, int, int)

    The rect to check

  -  *point* : (int,int)

    The point

## [win32gui](#win32gui).PtInRegion

boolean = __PtInRegion( *hrgn*  *, X*  *, Y* __ )
Determines if a region contains a point

#### Parameters


  -  *hrgn* :[PyGdiHandle](#pygdihandle)

    Handle to a region

  -  *X* : int

    X coord

  -  *Y* : int

    Y coord

## [win32gui](#win32gui).PumpMessages

 __PumpMessages(__ )
Runs a message loop until a WM_QUIT message is received.

#### See Also


  - [win32gui::PumpWaitingMessages](win32gui.md#win32guipumpwaitingmessages)

#### Return Value
Returns exit code from PostQuitMessage when a WM_QUIT message is received

## [win32gui](#win32gui).PumpWaitingMessages

int = __PumpWaitingMessages(__ )
Pumps all waiting messages for the current thread.

#### See Also


  - [win32gui::PumpMessages](win32gui.md#win32guipumpmessages)

#### Win32 API References


  - Search for *PeekMessage and DispatchMessage* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=peekmessage and dispatchmessage),[google](#http://www.google.com/search?q=peekmessage and dispatchmessage)or[google groups](#http://groups.google.com/groups?q=peekmessage and dispatchmessage).

#### Return Value
Returns non-zero (exit code from PostQuitMessage) if a WM_QUIT message was received, else 0

## [win32gui](#win32gui).PyGetArraySignedLong

object = __PyGetArraySignedLong( *array*  *, index* __ )
Returns a signed long from an array object at specified index

#### Parameters


  -  *array* : array

    array object to use

  -  *index* : int

    index of offset

## [win32gui](#win32gui).PyGetBufferAddressAndLen

object = __PyGetBufferAddressAndLen( *obj* __ )
Returns a buffer object address and len

#### Parameters


  -  *obj* : buffer

    the buffer object

## [win32gui](#win32gui).PyGetMemory

object = __PyGetMemory( *addr*  *, len* __ )
Returns a buffer object from and address and length

#### Parameters


  -  *addr* : int

    Address of the memory to reference.

  -  *len* : int

    Number of bytes to return.

#### Comments
If zero is passed a ValueError will be raised.

## [win32gui](#win32gui).PyGetString

string = __PyGetString( *addr*  *, len* __ )
Returns a string from an address.

#### Parameters


  -  *addr* : int

    Address of the memory to reference

  -  *len* : int

    Number of characters to read.  If not specified, the 

string must be NULL terminated.

#### Return Value
If win32gui.UNICODE is True, this will return a unicode object.

## [win32gui](#win32gui).PySetMemory

object = __PySetMemory( *addr*  *, String* __ )
Copies bytes to an address.

#### Parameters


  -  *addr* : int

    Address of the memory to reference

  -  *String* : string or buffer

    The string to copy

## [win32gui](#win32gui).PySetString

object = __PySetString( *addr*  *, String*  *, maxLen* __ )
Copies a string to an address (null terminated). 

You almost certainly should use[win32gui::PySetMemory](win32gui.md#win32guipysetmemory)instead.

#### Parameters


  -  *addr* : int

    Address of the memory to reference

  -  *String* : str

    The string to copy

  -  *maxLen* : int

    Maximum number of chars to copy (optional)

## [win32gui](#win32gui).RectInRegion

boolean = __RectInRegion( *hrgn*  *, rc* __ )
Determines if a region and rectangle overlap at any point

#### Parameters


  -  *hrgn* :[PyGdiHandle](#pygdihandle)

    Handle to a region

  -  *rc* :[PyRECT](#pyrect)

    Rectangle coordinates in logical units

## [win32gui](#win32gui).Rectangle

 __Rectangle( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect* __ )
Creates a solid rectangle using currently selected pen and brush

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to device context

  -  *LeftRect* : int

    Position of left edge of rectangle

  -  *TopRect* : int

    Position of top edge of rectangle

  -  *RightRect* : int

    Position of right edge of rectangle

  -  *BottomRect* : int

    Position of bottom edge of rectangle

## [win32gui](#win32gui).RedrawWindow

 __RedrawWindow( *hWnd*  *, rcUpdate*  *, hrgnUpdate*  *, flags* __ )
Causes a portion of a window to be redrawn

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to window to be redrawn

  -  *rcUpdate* : (int,int,int,int)

    Rectangle (left, top, right, bottom) identifying part of window to be redrawn, can be None

  -  *hrgnUpdate* :[PyGdiHANDLE](#pygdihandle)

    Handle to region to be redrawn, can be None to indicate entire client area

  -  *flags* : int

    Combination of win32con.RDW_* flags

## [win32gui](#win32gui).RegisterClass

int = __RegisterClass( *wndClass* __ )
Registers a window class.

#### Parameters


  -  *wndClass* :[PyWNDCLASS](#pywndclass)

    An object describing the window class.

## [win32gui](#win32gui).RegisterDeviceNotification

[PyHDEVNOTIFY](#pyhdevnotify)= __RegisterDeviceNotification( *handle*  *, filter*  *, flags* __ )
Registers the device or type of device for which a window will receive notifications.

#### Parameters


  -  *handle* :[PyHANDLE](#pyhandle)

    The handle to a window or a service

  -  *filter* : buffer

    A buffer laid out like one of the DEV_BROADCAST_* structures, generally built by one of the win32gui_struct helpers.

  -  *flags* : int

    

#### Win32 API References


  - Search for *RegisterDeviceNotification* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=registerdevicenotification),[google](#http://www.google.com/search?q=registerdevicenotification)or[google groups](#http://groups.google.com/groups?q=registerdevicenotification).

## [win32gui](#win32gui).RegisterHotKey

 __RegisterHotKey( *hWnd*  *, id*  *, Modifiers*  *, vk* __ )
Registers a hotkey for a window

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to window that will receive WM_HOTKEY messages

  -  *id* : int

    Unique id to be used for the hot key

  -  *Modifiers* : int

    Control keys, combination of win32con.MOD_*

  -  *vk* : int

    Virtual key code

#### Win32 API References


  - Search for *RegisterHotKey* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=registerhotkey),[google](#http://www.google.com/search?q=registerhotkey)or[google groups](#http://groups.google.com/groups?q=registerhotkey).

## [win32gui](#win32gui).RegisterWindowMessage

int = __RegisterWindowMessage( *name* __ )
Defines a new window message that is guaranteed to be unique throughout the system. The message value can be used when sending or posting messages.

#### Parameters


  -  *name* : string/unicode

    The string

## [win32gui](#win32gui).ReleaseCapture

 __ReleaseCapture(__ )
Releases the moust capture for a window.

## [win32gui](#win32gui).ReleaseDC

int = __ReleaseDC( *hWnd*  *, hDC* __ )
Releases a device context.

#### Parameters


  -  *hWnd* : int

    handle to window

  -  *hDC* : int

    handle to device context

## [win32gui](#win32gui).RemoveMenu

 __RemoveMenu( *hmenu*  *, position*  *, flags* __ )


#### Parameters


  -  *hmenu* : int

    The handle to the menu

  -  *position* : int

    The position to delete.

  -  *flags* : int

    

## [win32gui](#win32gui).ReplyMessage

int = __ReplyMessage( *result* __ )
Used to reply to a message sent through the SendMessage function without returning control to the function that called SendMessage.

#### Parameters


  -  *result* : int

    Specifies the result of the message processing. The possible values are based on the message sent.

## [win32gui](#win32gui).RestoreDC

 __RestoreDC( *hdc*  *, SavedDC* __ )
Restores a device context state

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *SavedDC* : int

    Identifier of state to be restored, as returned by[win32gui::SaveDC](win32gui.md#win32guisavedc).

## [win32gui](#win32gui).RoundRect

 __RoundRect( *hdc*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect*  *, Width*  *, Height* __ )
Draws a rectangle with elliptically rounded corners, filled using using current brush

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to device context

  -  *LeftRect* : int

    Position of left edge of rectangle

  -  *TopRect* : int

    Position of top edge of rectangle

  -  *RightRect* : int

    Position of right edge of rectangle

  -  *BottomRect* : int

    Position of bottom edge of rectangle

  -  *Width* : int

    Width of ellipse

  -  *Height* : int

    Height of ellipse

## [win32gui](#win32gui).SaveDC

int = __SaveDC( *hdc* __ )
Save the state of a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to device context

#### Return Value
Returns a value identifying the state that can be passed to[win32gui::RestoreDC](win32gui.md#win32guirestoredc).  On error, returns 0.

## [win32gui](#win32gui).ScreenToClient

(int,int) = __ScreenToClient( *hWnd*  *, Point* __ )
Convert screen coordinates to client coords

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *Point* : (int,int)

    Screen coordinates to be converted

## [win32gui](#win32gui).ScrollWindowEx

int,[PyRECT](#pyrect)= __ScrollWindowEx( *hWnd*  *, dx*  *, dy*  *, rcScroll*  *, rcClip*  *, hrgnUpdate*  *, flags* __ )
scrolls the content of the specified window's client area.

#### Parameters


  -  *hWnd* : int

    handle to window to scroll

  -  *dx* : int

    Amount of horizontal scrolling, in device units

  -  *dy* : int

    Amount of vertical scrolling, in device units

  -  *rcScroll* :[PyRECT](#pyrect)

    Scroll rectangle, can be None for entire client area

  -  *rcClip* :[PyRECT](#pyrect)

    Clipping rectangle, can be None

  -  *hrgnUpdate* :[PyGdiHandle](#pygdihandle)

    Handle to region which will be updated with area invalidated by scroll operation, can be None

  -  *flags* : int

    Scrolling flags, combination of SW_ERASE,SW_INVALIDATE,SW_SCROLLCHILDREN,SW_SMOOTHSCROLL. 

If SW_SMOOTHSCROLL is specified, use upper 16 bits to specify time in milliseconds.

#### Return Value
Returns the type of region invalidated by scrolling, and a rectangle defining the affected area.

## [win32gui](#win32gui).SelectObject

HGDIOBJ = __SelectObject( *hdc*  *, object* __ )
Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.

#### Parameters


  -  *hdc* : int

    handle to DC

  -  *object* : int

    The GDI object

## [win32gui](#win32gui).SendMessage

int = __SendMessage( *hwnd*  *, message*  *, wparam*  *, lparam* __ )
Sends a message to the window.

#### Parameters


  -  *hwnd* : int

    The handle to the Window

  -  *message* : int

    The ID of the message to post

  -  *wparam=None* : int/str

    Type depends on the message

  -  *lparam=None* : int/str

    Type depends on the message

## [win32gui](#win32gui).SendMessageTimeout

int,int = __SendMessageTimeout( *hwnd*  *, message*  *, wparam*  *, lparam*  *, flags*  *, timeout* __ )
Sends a message to the window.

#### Parameters


  -  *hwnd* : int

    The handle to the Window

  -  *message* : int

    The ID of the message to post

  -  *wparam* : int

    An integer whose value depends on the message

  -  *lparam* : int

    An integer whose value depends on the message

  -  *flags* : int

    Send options

  -  *timeout* : int

    Timeout duration in milliseconds.

#### Return Value
The result is the result of the SendMessageTimeout call, plus the last 'result' param. 

If the timeout period expires, a pywintypes.error exception will be thrown, 

with zero as the error code.  See the Microsoft documentation for more information.

## [win32gui](#win32gui).SetActiveWindow

HWND = __SetActiveWindow( *hwnd* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).SetArcDirection

int = __SetArcDirection( *hdc*  *, ArcDirection* __ )
Sets the drawing direction for arcs and rectangles

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *ArcDirection* : int

    One of win32con.AD_* constants

#### Return Value
Returns the previous direction, or 0 on error.

## [win32gui](#win32gui).SetBkColor

int = __SetBkColor( *hdc*  *, color* __ )
Sets the background color for a device context

#### Parameters


  -  *hdc* : int/[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *color* : int

    

#### Return Value
Returns the previous color, or CLR_INVALID on failure

## [win32gui](#win32gui).SetBkMode

int = __SetBkMode( *hdc*  *, BkMode* __ )
Sets the background mode for a device context

#### Parameters


  -  *hdc* : int/[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *BkMode* : int

    OPAQUE or TRANSPARENT

#### Return Value
Returns the previous mode, or 0 on failure

## [win32gui](#win32gui).SetCapture

 __SetCapture(__ )
Captures the mouse for the specified window.

## [win32gui](#win32gui).SetCaretPos

 __SetCaretPos( *x*  *, y* __ )
Changes the position of the caret

#### Parameters


  -  *x* : int

    horizontal position

  -  *y* : int

    vertical position

## [win32gui](#win32gui).SetCursor

HCURSOR = __SetCursor( *hcursor* __ )


#### Parameters


  -  *hcursor* : int

    

## [win32gui](#win32gui).SetDlgItemInt

 __SetDlgItemInt( *hDlg*  *, IDDlgItem*  *, Value*  *, Signed* __ )
Places an integer value in a dialog control

#### Parameters


  -  *hDlg* :[PyHANDLE](#pyhandle)

    Handle to a dialog window

  -  *IDDlgItem* : int

    Identifier of one of the dialog's controls

  -  *Value* : int

    Value to placed in the control

  -  *Signed* : boolean

    Indicates if the input value is signed

## [win32gui](#win32gui).SetDlgItemText

 __SetDlgItemText( *hDlg*  *, IDDlgItem*  *, String* __ )
Sets the text for a window or control

#### Parameters


  -  *hDlg* :[PyHANDLE](#pyhandle)

    Handle to a dialog window

  -  *IDDlgItem* : int

    The Id of a control within the dialog

  -  *String* : str/unicode

    The text to put in the control

## [win32gui](#win32gui).SetDoubleClickTime

 __SetDoubleClickTime( *newVal* __ )


#### Parameters


  -  *newVal* : int

    

## [win32gui](#win32gui).SetFocus

 __SetFocus( *hwnd* __ )
Sets focus to the specified window.

#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).SetForegroundWindow

HWND = __SetForegroundWindow( *hwnd* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).SetGraphicsMode

int = __SetGraphicsMode( *hdc*  *, Mode* __ )
Enables or disables advanced graphics features for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Mode* : int

    GM_COMPATIBLE or GM_ADVANCED (from win32con)

#### Return Value
Returns the previous mode, one of win32con.GM_COMPATIBLE or win32con.GM_ADVANCED

## [win32gui](#win32gui).SetLayeredWindowAttributes

 __SetLayeredWindowAttributes( *hwnd*  *, Key*  *, Alpha*  *, Flags* __ )
Sets the opacity and transparency color key of a layered window.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    handle to the layered window

  -  *Key* : int

    Specifies the color key.  Use[win32api::RGB](win32api.md#win32apirgb)to generate value.

  -  *Alpha* : int

    Opacity, in the range 0-255

  -  *Flags* : int

    Combination of win32con.LWA_* values

#### Comments
This function only exists on Win2k and later
Accepts keyword arguments

## [win32gui](#win32gui).SetLayout

int = __SetLayout( *hdc*  *, Layout* __ )
Sets the layout for a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Layout* : int

    One of win32con.LAYOUT_* constants

#### Return Value
Returns the previous layout mode

## [win32gui](#win32gui).SetMapMode

int = __SetMapMode( *hdc*  *, MapMode* __ )
Sets the method used for translating logical units to device units

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *MapMode* : int

    The new mapping mode (win32con.MM_*)

#### Return Value
Returns the previous mapping mode, one of win32con.MM_* constants

## [win32gui](#win32gui).SetMenu

 __SetMenu( *hwnd*  *, hmenu* __ )
Sets the menu for the specified window.

#### Parameters


  -  *hwnd* : int

    

  -  *hmenu* : int

    

## [win32gui](#win32gui).SetMenuDefaultItem

 __SetMenuDefaultItem( *hMenu*  *, uItem*  *, fByPos* __ )


#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *uItem* : int

    

  -  *fByPos* : int

    

## [win32gui](#win32gui).SetMenuInfo

 __SetMenuInfo( *hmenu*  *, info* __ )
Sets information for a specified menu.

#### Parameters


  -  *hmenu* : int

    handle to menu

  -  *info* : __MENUINFO__ 

    menu information in the format of a buffer.

#### Comments
See win32gui_struct for helper functions.
This function will raise NotImplementedError on early platforms (eg, Windows NT.)

## [win32gui](#win32gui).SetMenuItemBitmaps

 __SetMenuItemBitmaps( *hMenu*  *, uPosition*  *, uFlags*  *, hBitmapUnchecked*  *, hBitmapChecked* __ )
Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item.

#### Parameters


  -  *hMenu* : int

    handle to menu

  -  *uPosition* : int

    menu item

  -  *uFlags* : int

    options

  -  *hBitmapUnchecked* :[PyGdiHANDLE](#pygdihandle)

    handle to unchecked bitmap, can be None

  -  *hBitmapChecked* :[PyGdiHANDLE](#pygdihandle)

    handle to checked bitmap, can be None

## [win32gui](#win32gui).SetMenuItemInfo

 __SetMenuItemInfo( *hMenu*  *, uItem*  *, fByPosition*  *, menuItem* __ )
Sets menu information

#### Parameters


  -  *hMenu* : int

    Handle to the menu

  -  *uItem* : int

    The menu item identifier or the menu item position.

  -  *fByPosition* : int

    Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.

  -  *menuItem* : buffer

    A string or buffer in the format of a __MENUITEMINFO__ structure.

## [win32gui](#win32gui).SetMiterLimit

float = __SetMiterLimit( *hdc*  *, NewLimit* __ )
Set the limit of miter joins for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *NewLimit* : float

    New limit to be set

#### Return Value
Returns the previous limit

## [win32gui](#win32gui).SetParent

int = __SetParent( *child*  *, child* __ )
changes the parent window of the specified child window.

#### Parameters


  -  *child* : int

    handle to window whose parent is changing

  -  *child* : int

    handle to new parent window

## [win32gui](#win32gui).SetPixel

int = __SetPixel( *hdc*  *, X*  *, Y*  *, Color* __ )
Set the color of a single pixel

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *X* : int

    Horizontal pos

  -  *Y* : int

    Vertical pos

  -  *Color* : int

    RGB color to be set.

#### Return Value
Returns the RGB color actually set, which may be different from the one passed in

## [win32gui](#win32gui).SetPixelV

 __SetPixelV( *hdc*  *, X*  *, Y*  *, Color* __ )
Sets the color of a single pixel to an approximation of specified color

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *X* : int

    Horizontal pos

  -  *Y* : int

    Vertical pos

  -  *Color* : int

    RGB color to be set.

## [win32gui](#win32gui).SetPolyFillMode

int = __SetPolyFillMode( *hdc*  *, PolyFillMode* __ )
Sets the polygon filling mode for a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *PolyFillMode* : int

    One of ALTERNATE or WINDING

#### Return Value
Returns the previous mode, one of win32con.ALTERNATE or win32con.WINDING

## [win32gui](#win32gui).SetROP2

int = __SetROP2( *hdc*  *, DrawMode* __ )
Sets the foreground mixing mode of a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *DrawMode* : int

    Mixing mode, one of win32con.R2_*.

#### Return Value
Returns previous mode

## [win32gui](#win32gui).SetRectRgn

 __SetRectRgn( *hrgn*  *, LeftRect*  *, TopRect*  *, RightRect*  *, BottomRect* __ )
Makes an existing region rectangular

#### Parameters


  -  *hrgn* :[PyGdiHandle](#pygdihandle)

    Handle to a region

  -  *LeftRect* : int

    Left edge in logical units

  -  *TopRect* : int

    Top edge in logical units

  -  *RightRect* : int

    Right edge in logical units

  -  *BottomRect* : int

    Bottom edge in logical units

## [win32gui](#win32gui).SetScrollInfo

 __SetScrollInfo( *hwnd*  *, nBar*  *, scollInfo*  *, bRedraw* __ )
Sets information about a scroll-bar

#### Parameters


  -  *hwnd* : int

    The handle to the window.

  -  *nBar* : int

    Identifies the bar.

  -  *scollInfo* :[PySCROLLINFO](#pyscrollinfo)

    Scollbar info.

  -  *bRedraw=1* : int

    Should the bar be redrawn?

#### Return Value
Returns an int with the current position of the scroll box.

## [win32gui](#win32gui).SetStretchBltMode

int = __SetStretchBltMode( *hdc*  *, StretchMode* __ )
Sets the stretching mode used by[win32gui::StretchBlt](win32gui.md#win32guistretchblt)

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *StretchMode* : int

    One of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS, or WHITEONBLACK (from win32con)

#### Return Value
If the function succeeds, the return value is the previous stretching mode.
If the function fails, the return value is zero.

## [win32gui](#win32gui).SetTextAlign

int = __SetTextAlign( *hdc*  *, Mode* __ )
Sets horizontal and vertical alignment for text in a device context

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Mode* : int

    Combination of win32con.TA_* constants

#### Return Value
Returns the previous alignment flags

## [win32gui](#win32gui).SetTextCharacterExtra

int = __SetTextCharacterExtra( *hdc*  *, CharExtra* __ )
Sets the spacing between characters

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *CharExtra* : int

    Space between adjacent chars, in logical units

#### Return Value
Returns the previous spacing

## [win32gui](#win32gui).SetTextColor

int = __SetTextColor( *hdc*  *, color* __ )
Changes the text color for a device context

#### Parameters


  -  *hdc* : int

    Handle to a device context

  -  *color* : int

    The RGB color value - see[win32api::RGB](win32api.md#win32apirgb)

#### Return Value
Returns the previous color, or CLR_INVALID on failure

## [win32gui](#win32gui).SetViewportExtEx

(int,int) = __SetViewportExtEx( *hdc*  *, XExtent*  *, YExtent* __ )
Changes the viewport extents for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *XExtent* : int

    New X extent in logical units

  -  *YExtent* : int

    New Y extent in logical units

#### Return Value
Returns the previous extents as (x,y) in logical units

## [win32gui](#win32gui).SetViewportOrgEx

(int,int) = __SetViewportOrgEx( *hdc*  *, X*  *, Y* __ )
Changes the viewport origin for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *X* : int

    New X coord in logical units

  -  *Y* : int

    New Y coord in logical units

#### Return Value
Returns the previous origin as (x,y)

## [win32gui](#win32gui).SetWindowExtEx

(int,int) = __SetWindowExtEx( *hdc*  *, XExtent*  *, YExtent* __ )
Changes the window extents for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *XExtent* : int

    New X extent in logical units

  -  *YExtent* : int

    New Y extent in logical units

#### Return Value
Returns the previous extents

## [win32gui](#win32gui).SetWindowLong

int = __SetWindowLong( *hwnd*  *, index*  *, value* __ )
Places a long value at the specified offset into the extra window memory of the given window.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    The handle to the window

  -  *index* : int

    The index of the item to set.

  -  *value* : object

    The value to set.

#### Comments
This function calls the SetWindowLongPtr Api function
If index is GWLP_WNDPROC, then the value parameter 

must be a callable object (or a dictionary) to use as the 

new window procedure.

## [win32gui](#win32gui).SetWindowOrgEx

(int,int) = __SetWindowOrgEx( *hdc*  *, X*  *, Y* __ )
Changes the window origin for a DC

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *X* : int

    New X coord in logical units

  -  *Y* : int

    New Y coord in logical units

#### Return Value
Returns the previous origin

## [win32gui](#win32gui).SetWindowPlacement

 __SetWindowPlacement( *hWnd*  *, placement* __ )
Sets the windows placement

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *placement* : (tuple)

    A tuple representing the WINDOWPLACEMENT structure.

## [win32gui](#win32gui).SetWindowPos

 __SetWindowPos( *hWnd*  *, InsertAfter*  *, X*  *, Y*  *, cx*  *, cy*  *, Flags* __ )
Sets the position and size of a window

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to the window

  -  *InsertAfter* :[PyHANDLE](#pyhandle)

    Window that hWnd will be placed below.  Can be a window handle or one of HWND_BOTTOM,HWND_NOTOPMOST,HWND_TOP, or HWND_TOPMOST

  -  *X* : int

    New X coord

  -  *Y* : int

    New Y coord

  -  *cx* : int

    New width of window

  -  *cy* : int

    New height of window

  -  *Flags* : int

    Combination of win32con.SWP_* flags

## [win32gui](#win32gui).SetWindowRgn

 __SetWindowRgn( *hWnd*  *, hRgn*  *, Redraw* __ )
Sets the visible region of a window

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to a window

  -  *hRgn* :[PyGdiHANDLE](#pygdihandle)

    Handle to region to be set, can be None

  -  *Redraw* : boolean

    Indicates if window should be completely redrawn

#### Comments
On success, the system assumes ownership of the region so you should call the handle's Detach() 

method to prevent it from being automatically closed.

## [win32gui](#win32gui).SetWindowText

 __SetWindowText(__ )
Sets the window text.

## [win32gui](#win32gui).SetWorldTransform

 __SetWorldTransform( *hdc*  *, Xform* __ )
Transforms a device context's coordinate space

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context

  -  *Xform* :[PyXFORM](#pyxform)

    Matrix defining the transformation

#### Comments
DC's mode must be set to GM_ADVANCED.  See[win32gui::SetGraphicsMode](win32gui.md#win32guisetgraphicsmode).

## [win32gui](#win32gui).Shell_NotifyIcon

 __Shell_NotifyIcon( *Message*  *, nid* __ )
Adds, removes or modifies a taskbar icon.

#### Parameters


  -  *Message* : int

    One of win32gui.NIM_* flags

  -  *nid* :[PyNOTIFYICONDATA](#pynotifyicondata)

    Tuple containing NOTIFYICONDATA info

## [win32gui](#win32gui).ShowCaret

 __ShowCaret( *hWnd* __ )
Shows the caret at its current position

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Window that owns the caret, can be 0.

## [win32gui](#win32gui).ShowWindow

boolean = __ShowWindow( *hWnd*  *, cmdShow* __ )
Shows or hides a window and changes its state

#### Parameters


  -  *hWnd* : int

    The handle to the window

  -  *cmdShow* : int

    Combination of win32con.SW_* flags

## [win32gui](#win32gui).StretchBlt

 __StretchBlt( *hdcDest*  *, x*  *, y*  *, width*  *, height*  *, hdcSrc*  *, nXSrc*  *, nYSrc*  *, nWidthSrc*  *, nHeightSrc*  *, dwRop* __ )
Copies a bitmap from a source rectangle into a destination 

rectangle, stretching or compressing the bitmap to fit the dimensions of the 

destination rectangle, if necessary

#### Parameters


  -  *hdcDest* : int

    handle to destination DC

  -  *x* : int

    x-coord of destination upper-left corner

  -  *y* : int

    y-coord of destination upper-left corner

  -  *width* : int

    width of destination rectangle

  -  *height* : int

    height of destination rectangle

  -  *hdcSrc* : int

    handle to source DC

  -  *nXSrc* : int

    x-coord of source upper-left corner

  -  *nYSrc* : int

    y-coord of source upper-left corner

  -  *nWidthSrc* : int

    width of source rectangle

  -  *nHeightSrc* : int

    height of source rectangle

  -  *dwRop* : int

    raster operation code

## [win32gui](#win32gui).StrokeAndFillPath

 __StrokeAndFillPath( *hdc* __ )
Combines operations of StrokePath and FillPath with no overlap

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains a closed path. See[win32gui::EndPath](win32gui.md#win32guiendpath).

## [win32gui](#win32gui).StrokePath

 __StrokePath( *hdc* __ )
Draws current path with currently selected pen

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains a closed path. See[win32gui::EndPath](win32gui.md#win32guiendpath).

## [win32gui](#win32gui).SystemParametersInfo

 __SystemParametersInfo( *Action*  *, Param*  *, WinIni* __ )
Queries or sets system-wide parameters. This function can also update the user profile while setting a parameter.

#### Parameters


  -  *Action* : int

    System parameter to query or set, one of the SPI_GET* or SPI_SET* constants

  -  *Param=None* : object

    depends on action to be taken

  -  *WinIni=0* : int

    Flags specifying whether change should be permanent, and if all windows should be notified of change. Combination of SPIF_UPDATEINIFILE, SPIF_SENDCHANGE, SPIF_SENDWININICHANGE

 __Action__  __Input/return type__ SPI_GETDESKWALLPAPERReturns the path to the bmp used as wallpaperSPI_SETDESKWALLPAPERParam should be a string specifying a .bmp fileSPI_GETDROPSHADOWReturns a booleanSPI_GETFLATMENUReturns a booleanSPI_GETFONTSMOOTHINGReturns a booleanSPI_GETICONTITLEWRAPReturns a booleanSPI_GETSNAPTODEFBUTTONReturns a booleanSPI_GETBEEPReturns a booleanSPI_GETBLOCKSENDINPUTRESETSReturns a booleanSPI_GETMENUUNDERLINESReturns a booleanSPI_GETKEYBOARDCUESReturns a booleanSPI_GETKEYBOARDPREFReturns a booleanSPI_GETSCREENSAVEACTIVEReturns a booleanSPI_GETSCREENSAVERRUNNINGReturns a booleanSPI_GETMENUDROPALIGNMENTReturns a boolean (True indicates left aligned, False right aligned)SPI_GETMENUFADEReturns a booleanSPI_GETLOWPOWERACTIVEReturns a booleanSPI_GETPOWEROFFACTIVEReturns a booleanSPI_GETCOMBOBOXANIMATIONReturns a booleanSPI_GETCURSORSHADOWReturns a booleanSPI_GETGRADIENTCAPTIONSReturns a booleanSPI_GETHOTTRACKINGReturns a booleanSPI_GETLISTBOXSMOOTHSCROLLINGReturns a booleanSPI_GETMENUANIMATIONReturns a booleanSPI_GETSELECTIONFADEReturns a booleanSPI_GETTOOLTIPANIMATIONReturns a booleanSPI_GETTOOLTIPFADEReturns a boolean (TRUE=fade, False=slide)SPI_GETUIEFFECTSReturns a booleanSPI_GETACTIVEWINDOWTRACKINGReturns a booleanSPI_GETACTIVEWNDTRKZORDERReturns a booleanSPI_GETDRAGFULLWINDOWSReturns a booleanSPI_GETSHOWIMEUIReturns a booleanSPI_GETMOUSECLICKLOCKReturns a booleanSPI_GETMOUSESONARReturns a booleanSPI_GETMOUSEVANISHReturns a booleanSPI_GETSCREENREADERReturns a booleanSPI_GETSHOWSOUNDSReturns a booleanSPI_SETDROPSHADOWParam must be a booleanSPI_SETDROPSHADOWParam must be a booleanSPI_SETMENUUNDERLINESParam must be a booleanSPI_SETKEYBOARDCUESParam must be a booleanSPI_SETMENUFADEParam must be a booleanSPI_SETCOMBOBOXANIMATIONParam must be a booleanSPI_SETCURSORSHADOWParam must be a booleanSPI_SETGRADIENTCAPTIONSParam must be a booleanSPI_SETHOTTRACKINGParam must be a booleanSPI_SETLISTBOXSMOOTHSCROLLINGParam must be a booleanSPI_SETMENUANIMATIONParam must be a booleanSPI_SETSELECTIONFADEParam must be a booleanSPI_SETTOOLTIPANIMATIONParam must be a booleanSPI_SETTOOLTIPFADEParam must be a booleanSPI_SETUIEFFECTSParam must be a booleanSPI_SETACTIVEWINDOWTRACKINGParam must be a booleanSPI_SETACTIVEWNDTRKZORDERParam must be a booleanSPI_SETMOUSESONARParam must be a booleanSPI_SETMOUSEVANISHParam must be a booleanSPI_SETMOUSECLICKLOCKParam must be a booleanSPI_SETFONTSMOOTHINGParam should specify a booleanSPI_SETICONTITLEWRAPParam should specify a booleanSPI_SETSNAPTODEFBUTTONParam is a booleanSPI_SETBEEPParam is a booleanSPI_SETBLOCKSENDINPUTRESETSParam is a booleanSPI_SETKEYBOARDPREFParam is a booleanSPI_SETMOUSEBUTTONSWAPParam is a booleanSPI_SETSCREENSAVEACTIVEParam is a booleanSPI_SETMENUDROPALIGNMENTParam is a boolean (True=left aligned, False=right aligned)SPI_SETLOWPOWERACTIVEParam is a booleanSPI_SETPOWEROFFACTIVEParam is a booleanSPI_SETDRAGFULLWINDOWSParam is a booleanSPI_SETSHOWIMEUIParam is a booleanSPI_SETSCREENREADERParam is a booleanSPI_SETSHOWSOUNDSParam is a booleanSPI_SETMOUSETRAILSParam should be an int specifying the nbr of cursors in the trail (0 or 1 means disabled)SPI_SETWHEELSCROLLLINESParam is an int specifying nbr of linesSPI_SETKEYBOARDDELAYParam is an int in the range 0 - 3SPI_SETKEYBOARDSPEEDParam is an int in the range 0 - 31SPI_SETDOUBLECLICKTIMEParam is an int (in milliseconds),  Use[win32gui::GetDoubleClickTime](win32gui.md#win32guigetdoubleclicktime)to retrieve the value.SPI_SETDOUBLECLKWIDTHParam is an int.  Use win32api.GetSystemMetrics(SM_CXDOUBLECLK) to retrieve the value.SPI_SETDOUBLECLKHEIGHTParam is an int,  Use win32api.GetSystemMetrics(SM_CYDOUBLECLK) to retrieve the value.SPI_SETMOUSEHOVERHEIGHTParam is an intSPI_SETMOUSEHOVERWIDTHParam is an intSPI_SETMOUSEHOVERTIMEParam is an intSPI_SETSCREENSAVETIMEOUTParam is an int specifying the timeout in secondsSPI_SETMENUSHOWDELAYParam is an int specifying the shortcut menu delay in millisecondsSPI_SETLOWPOWERTIMEOUTParam is an int (in seconds)SPI_SETPOWEROFFTIMEOUTParam is an int (in seconds)SPI_SETDRAGHEIGHTParam is an int. Use win32api.GetSystemMetrics(SM_CYDRAG) to retrieve the value.SPI_SETDRAGWIDTHParam is an int. Use win32api.GetSystemMetrics(SM_CXDRAG) to retrieve the value.SPI_SETBORDERParam is an intSPI_GETFONTSMOOTHINGCONTRASTReturns an intSPI_GETFONTSMOOTHINGTYPEReturns an intSPI_GETMOUSETRAILSReturns an int specifying the nbr of cursor images in the trail, 0 or 1 indicates disabledSPI_GETWHEELSCROLLLINESReturns the nbr of lines to scroll for the mouse wheelSPI_GETKEYBOARDDELAYReturns an intSPI_GETKEYBOARDSPEEDReturns an intSPI_GETMOUSESPEEDReturns an intSPI_GETMOUSEHOVERHEIGHTReturns an intSPI_GETMOUSEHOVERWIDTHReturns an intSPI_GETMOUSEHOVERTIMEReturns an intSPI_GETSCREENSAVETIMEOUTReturns an int (idle time in seconds)SPI_GETMENUSHOWDELAYReturns an int (shortcut delay in milliseconds)SPI_GETLOWPOWERTIMEOUTReturns an int (in seconds)SPI_GETPOWEROFFTIMEOUTReturns an int (in seconds)SPI_GETACTIVEWNDTRKTIMEOUTReturns an int (milliseconds)SPI_GETBORDERReturns an intSPI_GETCARETWIDTHReturns an intSPI_GETFOREGROUNDFLASHCOUNTReturns an intSPI_GETFOREGROUNDLOCKTIMEOUTReturns an intSPI_GETFOCUSBORDERHEIGHTReturns an intSPI_GETFOCUSBORDERWIDTHReturns an intSPI_GETMOUSECLICKLOCKTIMEReturns an int (in milliseconds)SPI_SETFONTSMOOTHINGCONTRASTParam should be an int in the range 1000 to 2200SPI_SETFONTSMOOTHINGTYPEParam should be one of the FE_FONTSMOOTHING* constantsSPI_SETMOUSESPEEDParam should be an int in the range 1 - 20SPI_SETACTIVEWNDTRKTIMEOUTParam is an int (in milliseconds)SPI_SETCARETWIDTHParam is an int (in pixels)SPI_SETFOREGROUNDFLASHCOUNTParam is an intSPI_SETFOREGROUNDLOCKTIMEOUTParam is an int (in milliseconds)SPI_SETFOCUSBORDERHEIGHTReturns an intSPI_SETFOCUSBORDERWIDTHReturns an intSPI_SETMOUSECLICKLOCKTIMEParam is an int (in milliseconds)SPI_GETICONTITLELOGFONTReturns a[PyLOGFONT](#pylogfont),SPI_SETICONTITLELOGFONTParam must be a[PyLOGFONT](#pylogfont),SPI_SETLANGTOGGLEParam is ignored. Sets the language toggle hotkey from registry key HKCU\\keyboard layout\\toggleSPI_SETICONSReloads the system icons.  Param is not usedSPI_GETMOUSEReturns a tuple of 3 ints containing the x and y mouse thresholds and the acceleration factor.SPI_SETMOUSEParam should be a sequence of 3 intsSPI_GETDEFAULTINPUTLANGReturns an int (locale id for default language)SPI_SETDEFAULTINPUTLANGParam is an int containing a locale idSPI_GETANIMATIONReturns an intSPI_SETANIMATIONParam is an intSPI_ICONHORIZONTALSPACINGFunctions as both a get and set operation.  If Param is None, functions as a get operation, otherwise Param is an int to be set as the new valueSPI_ICONVERTICALSPACINGFunctions as both a get and set operation.  If Param is None, functions as a get operation, otherwise Param is an int to be set as the new valueSPI_GETNONCLIENTMETRICSParam must be None.  The result is a dict.SPI_SETNONCLIENTMETRICSParam is a dict in the form of a NONCLIENTMETRICS struct, as returned by SPI_GETNONCLIENTMETRICS operationSPI_GETMINIMIZEDMETRICSReturns a dict representing a MINIMIZEDMETRICS struct.  Param is not used.SPI_SETMINIMIZEDMETRICSParam should be a MINIMIZEDMETRICS dict as returned by SPI_GETMINIMIZEDMETRICS actionSPI_SETDESKPATTERNUnsupported (obsolete)SPI_GETFASTTASKSWITCHUnsupported (obsolete)SPI_SETFASTTASKSWITCHUnsupported (obsolete)SPI_SETSCREENSAVERRUNNINGUnsupported (documented as internal use only)SPI_SCREENSAVERRUNNINGSame as SPI_SETSCREENSAVERRUNNINGSPI_SETPENWINDOWSUnsupported (only relevant for win95)SPI_GETWINDOWSEXTENSIONUnsupported (only relevant for win95)SPI_GETGRIDGRANULARITYUnsupported (obsolete)SPI_SETGRIDGRANULARITYUnsupported (obsolete)SPI_LANGDRIVERUnsupported (use is not documented)SPI_GETFONTSMOOTHINGORIENTATIONUnsupported (use is not documented)SPI_SETFONTSMOOTHINGORIENTATIONUnsupported (use is not documented)SPI_SETHANDHELDUnsupported (use is not documented)SPI_GETICONMETRICSNot implemented yetSPI_SETICONMETRICSNot implemented yetSPI_GETWORKAREANot implemented yetSPI_SETWORKAREANot implemented yetSPI_GETSERIALKEYSNot implemented yetSPI_SETSERIALKEYSNot implemented yetSPI_SETMOUSEKEYSNot implemented yetSPI_GETMOUSEKEYSNot implemented yetSPI_GETHIGHCONTRASTNot implemented yetSPI_SETHIGHCONTRASTNot implemented yetSPI_GETSOUNDSENTRYNot implemented yetSPI_SETSOUNDSENTRYNot implemented yetSPI_GETSTICKYKEYSNot implemented yetSPI_SETSTICKYKEYSNot implemented yetSPI_GETTOGGLEKEYSNot implemented yetSPI_SETTOGGLEKEYSNot implemented yetSPI_GETACCESSTIMEOUTNot implemented yetSPI_SETACCESSTIMEOUTNot implemented yetSPI_GETFILTERKEYSNot implemented yetSPI_SETFILTERKEYSNot implemented yet
#### Comments
Param and WinIni are not used with any of the SPI_GET operations
Boolean parameters can be any object that can be evaluated as True or False

#### Return Value
SPI_SET functions all return None on success.  Types returned by SPI_GET functions are dependent on the operation

## TPM_BOTTOMALIGN
 __const win32gui.TPM_BOTTOMALIGN;__ 


## TPM_CENTERALIGN
 __const win32gui.TPM_CENTERALIGN;__ 


## TPM_LEFTALIGN
 __const win32gui.TPM_LEFTALIGN;__ 


## TPM_LEFTBUTTON
 __const win32gui.TPM_LEFTBUTTON;__ 


## TPM_NONOTIFY
 __const win32gui.TPM_NONOTIFY;__ 


## TPM_RETURNCMD
 __const win32gui.TPM_RETURNCMD;__ 


## TPM_RIGHTALIGN
 __const win32gui.TPM_RIGHTALIGN;__ 


## TPM_RIGHTBUTTON
 __const win32gui.TPM_RIGHTBUTTON;__ 


## TPM_TOPALIGN
 __const win32gui.TPM_TOPALIGN;__ 


## TPM_VCENTERALIGN
 __const win32gui.TPM_VCENTERALIGN;__ 


## [win32gui](#win32gui).TrackPopupMenu

int = __TrackPopupMenu( *hmenu*  *, flags*  *, x*  *, y*  *, reserved*  *, hwnd*  *, prcRect* __ )
Display popup shortcut menu

#### Parameters


  -  *hmenu* : int

    The handle to the menu

  -  *flags* : uint

    flags

  -  *x* : int

    x pos

  -  *y* : int

    y pos

  -  *reserved* : int

    reserved

  -  *hwnd* : hwnd

    owner window

  -  *prcRect* :[PyRECT](#pyrect)

    Pointer to rec (can be None)

## [win32gui](#win32gui).TranslateAccelerator

int = __TranslateAccelerator( *hwnd*  *, haccel*  *, msg* __ )


#### Parameters


  -  *hwnd* : int

    

  -  *haccel* : int

    

  -  *msg* : MSG

    

## [win32gui](#win32gui).TranslateMessage

int = __TranslateMessage( *msg* __ )


#### Parameters


  -  *msg* : MSG

    

## [win32gui](#win32gui).TransparentBlt

 __TransparentBlt( *Dest*  *, XOriginDest*  *, YOriginDest*  *, WidthDest*  *, HeightDest*  *, Src*  *, XOriginSrc*  *, YOriginSrc*  *, WidthSrc*  *, HeightSrc*  *, Transparent* __ )
Transfers color from one DC to another, with one color treated as transparent

#### Parameters


  -  *Dest* :[PyHANDLE](#pyhandle)

    Destination device context handle

  -  *XOriginDest* : int

    X pos of dest rect

  -  *YOriginDest* : int

    Y pos of dest rect

  -  *WidthDest* : int

    Width of dest rect

  -  *HeightDest* : int

    Height of dest rect

  -  *Src* :[PyHANDLE](#pyhandle)

    Source DC handle

  -  *XOriginSrc* : int

    X pos of src rect

  -  *YOriginSrc* : int

    Y pos of src rect

  -  *WidthSrc* : int

    Width of src rect

  -  *HeightSrc* : int

    Height of src rect

  -  *Transparent* : int

    RGB color value that will be transparent

## [win32gui](#win32gui).UnregisterClass

 __UnregisterClass( *atom*  *, hinst* __ )
Unregisters a window class created by[win32gui::RegisterClass](win32gui.md#win32guiregisterclass)

#### Parameters


  -  *atom* :[PyResourceId](#pyresourceid)

    The atom or classname identifying the class previously registered.

  -  *hinst* :[PyHANDLE](#pyhandle)

    The handle to the instance unregistering the class, can be None

## [win32gui](#win32gui).UnregisterDeviceNotification

 __UnregisterDeviceNotification(__ )
Unregisters a Device Notification handle. 

It is generally not necessary to call this function manually, but in some cases, 

handle values may be extracted via the struct module and need to be closed explicitly.

## [win32gui](#win32gui).UpdateLayeredWindow

 __UpdateLayeredWindow( *hwnd*  *, hdcDst*  *, ptDst*  *, size*  *, hdcSrc*  *, ptSrc*  *, Key*  *, blend*  *, Flags* __ )
Updates the position, size, shape, content, and translucency of a layered window.

#### Parameters


  -  *hwnd* :[PyHANDLE](#pyhandle)

    handle to layered window

  -  *hdcDst=None* :[PyHANDLE](#pyhandle)

    handle to screen DC, can be None.  *Must* be None if hdcSrc is None

  -  *ptDst=None* : (x,y)

    New screen position, can be None.

  -  *size=None* : (cx, cy)

    New size of the layered window, can be None.  *Must* be None if hdcSrc is None.

  -  *hdcSrc=None* : int

    handle to surface DC for the window, can be None

  -  *ptSrc=None* : (x,y)

    layer position, can be None.  *Must* be None if hdcSrc is None.

  -  *Key=0* : int

    Color key, generate using[win32api::RGB](win32api.md#win32apirgb)

  -  *blend=(0,0,255,0)* : (int, int, int, int)

    [PyBLENDFUNCTION](#pyblendfunction)specifying alpha blending parameters

  -  *Flags=0* : int

    One of the win32con.ULW_* values.  Use 0 if hdcSrc is None.

#### Comments
This function is only available on Windows 2000 and later
Accepts keyword arguments.

## [win32gui](#win32gui).UpdateWindow

 __UpdateWindow( *hwnd* __ )


#### Parameters


  -  *hwnd* : int

    The handle to the window

## [win32gui](#win32gui).ValidateRgn

 __ValidateRgn( *hWnd*  *, hRgn* __ )
Removes a region from a window's update region

#### Parameters


  -  *hWnd* :[PyHANDLE](#pyhandle)

    Handle to the window

  -  *hRgn* :[PyGdiHANDLE](#pygdihandle)

    Region to be validated

## [win32gui](#win32gui).WaitMessage

 __WaitMessage(__ )
Waits for a message

## [win32gui](#win32gui).WidenPath

 __WidenPath( *hdc* __ )
Widens current path by amount it would increase by if drawn with currently selected pen

#### Parameters


  -  *hdc* :[PyHANDLE](#pyhandle)

    Handle to a device context that contains a closed path. See[win32gui::EndPath](win32gui.md#win32guiendpath).

## [win32gui](#win32gui).WindowFromDC

[PyHANDLE](#pyhandle)= __WindowFromDC( *hDC* __ )
Finds the window associated with a device context

#### Parameters


  -  *hDC* :[PyHANDLE](#pyhandle)

    Handle to a device context

#### Return Value
Returns a handle to the window, or 0 if the DC is not associated with a window

## [win32gui](#win32gui).WindowFromPoint

int = __WindowFromPoint( *point* __ )
Retrieves a handle to the window that contains the specified point.

#### Parameters


  -  *point* : (int, int)

    The point.

## [win32gui](#win32gui)._TrackMouseEvent

 ___TrackMouseEvent( *tme* __ )
Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.

#### Parameters


  -  *tme* :[TRACKMOUSEEVENT](#trackmouseevent)

    

## [win32gui](#win32gui).set_logger

 __set_logger( *logger* __ )
Sets a logger object for exceptions and error information

#### Parameters


  -  *logger* : object

    A logger object, generally from the standard logger package.

#### Comments
Once a logger has been set for the module, unhandled exceptions, such as 

from a window's WNDPROC, will be written (via logger.exception()) to the log 

instead of to stderr.
Note that using this with the Python 2.3 logging package will prevent the 

traceback from being written to the log.  However, it is possible to use 

the Python 2.4 logging package directly with Python 2.3