# PyIActiveDesktop


## PyIActiveDesktop Object

An interface to the ActiveDesktop

#### Methods

  - [ApplyChanges](PyIActiveDesktop.md#pyiactivedesktopapplychanges)

    Applies changes to ActiveDesktop settings and persists them to the registry\.&nbsp;

  - [GetWallpaper](PyIActiveDesktop.md#pyiactivedesktopgetwallpaper)

    Returns the current wallpaper&nbsp;

  - [SetWallpaper](PyIActiveDesktop.md#pyiactivedesktopsetwallpaper)

    Sets the desktop wallpaper&nbsp;

  - [GetWallpaperOptions](PyIActiveDesktop.md#pyiactivedesktopgetwallpaperoptions)

    Returns wallpaper style&nbsp;

  - [SetWallpaperOptions](PyIActiveDesktop.md#pyiactivedesktopsetwallpaperoptions)

    Sets wallpaper style&nbsp;

  - [GetPattern](PyIActiveDesktop.md#pyiactivedesktopgetpattern)

    Returns the wallpaper pattern&nbsp;

  - [SetPattern](PyIActiveDesktop.md#pyiactivedesktopsetpattern)

    Sets the wallpaper pattern&nbsp;

  - [GetDesktopItemOptions](PyIActiveDesktop.md#pyiactivedesktopgetdesktopitemoptions)

    Returns options for Active Desktop\.&nbsp;

  - [SetDesktopItemOptions](PyIActiveDesktop.md#pyiactivedesktopsetdesktopitemoptions)

    Sets Active Desktop options&nbsp;

  - [AddDesktopItem](PyIActiveDesktop.md#pyiactivedesktopadddesktopitem)

    Creates a new item to display on the desktop&nbsp;

  - [AddDesktopItemWithUI](PyIActiveDesktop.md#pyiactivedesktopadddesktopitemwithui)

    Adds a desktop item, allowing user interaction&nbsp;

  - [ModifyDesktopItem](PyIActiveDesktop.md#pyiactivedesktopmodifydesktopitem)

    Changes parameters for a desktop item&nbsp;

  - [RemoveDesktopItem](PyIActiveDesktop.md#pyiactivedesktopremovedesktopitem)

    Removes an item from the Active Desktop&nbsp;

  - [GetDesktopItemCount](PyIActiveDesktop.md#pyiactivedesktopgetdesktopitemcount)

    Returns number of defined desktop items\.&nbsp;

  - [GetDesktopItem](PyIActiveDesktop.md#pyiactivedesktopgetdesktopitem)

    Returns desktop item parameters by index&nbsp;

  - [GetDesktopItemByID](PyIActiveDesktop.md#pyiactivedesktopgetdesktopitembyid)

    Returns desktop item parameters by Id&nbsp;

  - [GenerateDesktopItemHtml](PyIActiveDesktop.md#pyiactivedesktopgeneratedesktopitemhtml)

    Creates an HTML page for the desktop item&nbsp;

  - [AddUrl](PyIActiveDesktop.md#pyiactivedesktopaddurl)

    Adds a web page to desktop, allowing user interaction&nbsp;

  - [GetDesktopItemBySource](PyIActiveDesktop.md#pyiactivedesktopgetdesktopitembysource)

    Returns desktop item parameters by URL&nbsp;


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.AddDesktopItem

AddDesktopItem\(comp, Reserved\)
Creates a new item to display on the desktop

#### Parameters

  - comp : dict

    [COMPONENT](COMPONENT.md) dictionary

  - Reserved=0 : int

    Use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.AddDesktopItemWithUI

AddDesktopItemWithUI\(hwnd, comp, Flags\)
Adds a desktop item, allowing user interaction

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Handle to parent window

  - comp : dict

    [COMPONENT](COMPONENT.md) dictionary

  - Flags : int

    One of shellcon\.DTI\_ADDUI\_\* flags


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.AddUrl

AddUrl\(hwnd, Source, comp, Flags\)
Adds a web page to desktop, allowing user interaction

#### Parameters

  - hwnd : [PyHANDLE](PyHANDLE.md)

    Parent windows for any user interactive

  - Source : [PyUNICODE](PyUNICODE.md)

    Source URL

  - comp : dict

    [COMPONENT](COMPONENT.md) dictionary

  - Flags : int

    ADDURL\_SILENT, or 0


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.ApplyChanges

ApplyChanges\(Flags\)
Applies changes to ActiveDesktop settings and persists them to the registry\.

#### Parameters

  - Flags : int

    Combination of shellcon\.AD\_APPLY\_\* flags


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GenerateDesktopItemHtml

GenerateDesktopItemHtml\(FileName, comp, Reserved\)
Creates an HTML page for the desktop item

#### Parameters

  - FileName : [PyUNICODE](PyUNICODE.md)

    Name of file to be created

  - comp : dict

    [COMPONENT](COMPONENT.md) dictionary specifying the desktop item

  - Reserved=0 : int

    Use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetDesktopItem

dict = GetDesktopItem\(Component, Reserved

\)
Returns desktop item parameters by index

#### Parameters

  - Component : int

    The zero-based index of the component to get

  - Reserved=0 : int

    Use 0 if passed in

#### Return Value
Returns a [COMPONENT](COMPONENT.md) dictionary describing the item


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetDesktopItemByID

dict = GetDesktopItemByID\(ID, reserved

\)
Returns desktop item parameters by Id

#### Parameters

  - ID : int

    The Id of the desktop item

  - reserved=0 : int

    Use 0 if passed in

#### Return Value
Returns a [COMPONENT](COMPONENT.md) dictionary


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetDesktopItemBySource

dict = GetDesktopItemBySource\(Source, Reserved

\)
Returns desktop item parameters by URL

#### Parameters

  - Source : [PyUNICODE](PyUNICODE.md)

    The URL address of the item to retrieve

  - Reserved=0 : int

    Use 0 if passed in

#### Return Value
Returns a [COMPONENT](COMPONENT.md) dictionary


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetDesktopItemCount

GetDesktopItemCount\(\)
Returns number of defined desktop items\.


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetDesktopItemOptions

dict = GetDesktopItemOptions\(\)
Returns options for Active Desktop\.

#### Return Value
Returns a [COMPONENTSOPT](COMPONENTSOPT.md) dictionary


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetPattern

GetPattern\(cchPattern, Reserved\)
Returns the wallpaper pattern

#### Parameters

  - cchPattern=1024 : int

    Number of characters to allocate for buffer

  - Reserved=0 : int

    Use 0 if passed in

#### Return Value
Returns a unicode string containing decimal values representing the pattern


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetWallpaper

[PyUNICODE](PyUNICODE.md) = GetWallpaper\(cchWallpaper, Reserved

\)
Returns the current wallpaper

#### Parameters

  - cchWallpaper=MAX\_PATH : int

    Number of characters to allocate for buffer

  - Reserved=0 : int

    Use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.GetWallpaperOptions

int = GetWallpaperOptions\(Reserved\)
Returns wallpaper style

#### Parameters

  - Reserved=0 : int

    Use 0 if passed in

#### Return Value
Returns one of the WPSTYLE\_\* values


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.ModifyDesktopItem

ModifyDesktopItem\(comp, Flags\)
Changes parameters for a desktop item

#### Parameters

  - comp : dict

    [COMPONENT](COMPONENT.md) dictionary

  - Flags : int

    Combination of shellcon\.COMP\_ELEM\_\* flags


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.RemoveDesktopItem

RemoveDesktopItem\(comp, Reserved\)
Removes an item from the Active Desktop

#### Parameters

  - comp : dict

    [COMPONENT](COMPONENT.md) dictionary specifying which component to remove

  - Reserved=0 : int

    Use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.SetDesktopItemOptions

SetDesktopItemOptions\(comp, Reserved\)
Sets Active Desktop options

#### Parameters

  - comp : dict

    [COMPONENTSOPT](COMPONENTSOPT.md) dictionary

  - Reserved=0 : int

    Use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.SetPattern

SetPattern\(Pattern, Reserved\)
Sets the wallpaper pattern

#### Parameters

  - Pattern : [PyUNICODE](PyUNICODE.md)

    String of decimal numbers representing a picture

  - Reserved=0 : int

    Use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.SetWallpaper

SetWallpaper\(Wallpaper, Reserved\)
Sets the desktop wallpaper

#### Parameters

  - Wallpaper : [PyUNICODE](PyUNICODE.md)

    File to be used as new wallpaper

  - Reserved=0 : int

    Reserved, use 0 if passed in


## [PyIActiveDesktop](PyIActiveDesktop.md#pyiactivedesktop)\.SetWallpaperOptions

SetWallpaperOptions\(Style, Reserved\)
Sets wallpaper style

#### Parameters

  - Style : int

    The wallpaper style, one of the WPSTYLE\_\* constants

  - Reserved=0 : int

    Reserved, use 0 if passed in