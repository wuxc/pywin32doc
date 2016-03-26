# _winxptheme

## Module \_winxptheme



A module which provides an interface to the Windows XP 

'theme' API\.
Note that this module will fail to load on 

non-Windows XP versions\.  Generally you should use the 

'winxptheme' module which will load on all Windows 

versions, and provide implementations of 

IsThemeActive\(\) or IsAppThemed\(\) which return False when 

XP is not used, and provides all objects from this module 

when XP is used\.  See winxptheme\.py for more details\.

#### Methods


  - [OpenThemeData](_winxptheme.md#_winxpthemeopenthemedata)

    Open the theme data for the specified HWND and 

semi-colon separated list of class names\.
OpenThemeData\(\) will try each class name, one at 

a time, and use the first matching theme info 

found\.  If a match is found, a theme handle 

to the data is returned\.  If no match is found, 

a "NULL" handle is returned\.
When the window is destroyed or a WM\_THEMECHANGED 

msg is received,[\_winxptheme::CloseThemeData](_winxptheme.md#_winxpthemeclosethemedata) should be 

called to close the theme handle\.&nbsp;

  - [CloseThemeData](_winxptheme.md#_winxpthemeclosethemedata)

    Closes the theme data handle\.  This should be done 

when the window being themed is destroyed or 

whenever a WM\_THEMECHANGED msg is received 

\(followed by an attempt to create a new Theme data 

handle\)\.&nbsp;

  - [DrawThemeBackground](_winxptheme.md#_winxpthemedrawthemebackground)

    Draws the theme-specified border and fill for 

the "iPartId" and "iStateId"\.  This could be 

based on a bitmap file, a border and fill, or 

other image description\.&nbsp;

  - [DrawThemeText](_winxptheme.md#_winxpthemedrawthemetext)

    Draws the text using the theme-specified 

color and font for the "iPartId" and "iStateId"\.&nbsp;

  - [GetThemeBackgroundContentRect](_winxptheme.md#_winxpthemegetthemebackgroundcontentrect)

    Gets the size of the content for the theme-defined 

background\.  This is usually the area inside the borders or Margins\.&nbsp;

  - [GetThemeBackgroundExtent](_winxptheme.md#_winxpthemegetthemebackgroundextent)

    Calculates the size/location of the theme- 

specified background based on the "pContentRect"\.&nbsp;

  - [IsThemeActive](_winxptheme.md#_winxpthemeisthemeactive)

    Can be used to test if a system theme is active 

for the current user session\.
use the API[\_winxptheme::IsAppThemed](_winxptheme.md#_winxpthemeisappthemed) to test if a theme is 

active for the calling process\.&nbsp;

  - [IsAppThemed](_winxptheme.md#_winxpthemeisappthemed)

    Returns True if a theme is active and available to 

the current process&nbsp;

  - [GetWindowTheme](_winxptheme.md#_winxpthemegetwindowtheme)

    If window is themed, returns its most recent 

HTHEME from OpenThemeData\(\) - otherwise, returns NULL\.&nbsp;

  - [EnableThemeDialogTexture](_winxptheme.md#_winxpthemeenablethemedialogtexture)

    Enables/disables dialog background theme\. 

This method can be used to 

tailor dialog compatibility with child windows and controls that 

may or may not coordinate the rendering of their client area backgrounds 

with that of their parent dialog in a manner that supports seamless 

background texturing\.&nbsp;

  - [IsThemeDialogTextureEnabled](_winxptheme.md#_winxpthemeisthemedialogtextureenabled)

    Reports whether the dialog supports background texturing\.&nbsp;

  - [GetThemeAppProperties](_winxptheme.md#_winxpthemegetthemeappproperties)

    Returns the app property flags that control theming&nbsp;

  - [EnableTheming](_winxptheme.md#_winxpthemeenabletheming)

    Enables or disables themeing for the current user 

in the current and future sessions\.&nbsp;

  - [SetWindowTheme](_winxptheme.md#_winxpthemesetwindowtheme)

    Rredirects an existing Window to use a different 

section of the current theme information than its class normally asks for\.&nbsp;

  - [GetCurrentThemeName](_winxptheme.md#_winxpthemegetcurrentthemename)

    Get the name of the current theme in-use, the 

canonical color scheme name \(not the display name\) and the 

canonical size name \(not the display name\)\.&nbsp;

## [\_winxptheme](#_winxptheme)\.CloseThemeData

CloseThemeData\(hTheme\)
Closes the theme data handle\.  This should be done 

when the window being themed is destroyed or 

whenever a WM\_THEMECHANGED msg is received 

\(followed by an attempt to create a new Theme data 

handle\)\.

#### Parameters


  - hTheme :[PyHTHEME](#pyhtheme)

    Open theme data handle \(returned from prior call 

to OpenThemeData\(\) API\)\.

## [\_winxptheme](#_winxptheme)\.DrawThemeBackground

DrawThemeBackground\(hTheme, hdc, iPartId, iStateId, pRect, pClipRect\)
Draws the theme-specified border and fill for 

the "iPartId" and "iStateId"\.  This could be 

based on a bitmap file, a border and fill, or 

other image description\.

#### Parameters


  - hTheme :[PyHTHEME](#pyhtheme)

    theme data handle

  - hdc : int

    HDC to draw into

  - iPartId : int

    part number to draw

  - iStateId : int

    state number \(of the part\) to draw

  - pRect : rect

    defines the size/location of the part

  - pClipRect : rect

    optional clipping rect \(don't draw outside it\)

## [\_winxptheme](#_winxptheme)\.DrawThemeText

DrawThemeText\(hTheme, hdc, iPartId, iStateId, pszText, dwCharCount, dwTextFlags, dwTextFlags2, pRect\)
Draws the text using the theme-specified 

color and font for the "iPartId" and "iStateId"\.

#### Parameters


  - hTheme :[PyHTHEME](#pyhtheme)

    theme data handle

  - hdc : int

    HDC to draw into

  - iPartId : int

    part number to draw

  - iStateId : int

    state number \(of the part\) to draw

  - pszText : string

    actual text to draw

  - dwCharCount : int

    number of chars to draw \(-1 for all\)

  - dwTextFlags : int

    same as DrawText\(\) "uFormat" param

  - dwTextFlags2 : int

    additional drawing options

  - pRect : rect

    defines the size/location of the part

## ETDT\_DISABLE
const \_winxptheme\.ETDT\_DISABLE;


## ETDT\_ENABLE
const \_winxptheme\.ETDT\_ENABLE;


## ETDT\_ENABLETAB
const \_winxptheme\.ETDT\_ENABLETAB;


## ETDT\_USETABTEXTURE
const \_winxptheme\.ETDT\_USETABTEXTURE;


## [\_winxptheme](#_winxptheme)\.EnableThemeDialogTexture

EnableThemeDialogTexture\(hdlg, dwFlags\)
Enables/disables dialog background theme\. 

This method can be used to 

tailor dialog compatibility with child windows and controls that 

may or may not coordinate the rendering of their client area backgrounds 

with that of their parent dialog in a manner that supports seamless 

background texturing\.

#### Parameters


  - hdlg : int

    The window handle of the target dialog

  - dwFlags : int

    ETDT\_ENABLE to enable the theme-defined dialog background texturing,
ETDT\_DISABLE to disable background texturing,
ETDT\_ENABLETAB to enable the theme-defined background 

texturing using the Tab texture

## [\_winxptheme](#_winxptheme)\.EnableTheming

EnableTheming\(fEnable\)
Enables or disables themeing for the current user 

in the current and future sessions\.

#### Parameters


  - fEnable : bool

    if False, disable theming & turn themes off\.
if True, enable themeing and, if user previously 

had a theme active, make it active now\.

## [\_winxptheme](#_winxptheme)\.GetCurrentThemeName



\(string, string, string\) =GetCurrentThemeName\(\)
Get the name of the current theme in-use, the 

canonical color scheme name \(not the display name\) and the 

canonical size name \(not the display name\)\.

## [\_winxptheme](#_winxptheme)\.GetThemeAppProperties



int =GetThemeAppProperties\(\)
Returns the app property flags that control theming

## [\_winxptheme](#_winxptheme)\.GetThemeBackgroundContentRect



rect =GetThemeBackgroundContentRect\(hTheme, hdc, iPartId, iStateId, pBoundingRect\)
Gets the size of the content for the theme-defined 

background\.  This is usually the area inside the borders or Margins\.

#### Parameters


  - hTheme :[PyHTHEME](#pyhtheme)

    theme data handle

  - hdc : int

    \(optional\) device content to be used for drawing

  - iPartId : int

    part number to draw

  - iStateId : int

    state number \(of the part\) to draw

  - pBoundingRect : rect

    the outer RECT of the part being drawn

#### Return Value
The result is a rect with the content area

## [\_winxptheme](#_winxptheme)\.GetThemeBackgroundExtent



rect =GetThemeBackgroundExtent\(hTheme, hdc, iPartId, iStateId, pContentRect\)
Calculates the size/location of the theme- 

specified background based on the "pContentRect"\.

#### Parameters


  - hTheme :[PyHTHEME](#pyhtheme)

    theme data handle

  - hdc : int

    \(optional\) device content to be used for drawing

  - iPartId : int

    part number to draw

  - iStateId : int

    state number \(of the part\) to draw

  - pContentRect : rect

    RECT that defines the content area

#### Return Value
Result is a rect with the overall size/location of part

## [\_winxptheme](#_winxptheme)\.GetWindowTheme

[PyHTHEME](#pyhtheme) =GetWindowTheme\(hwnd\)
If window is themed, returns its most recent 

HTHEME from OpenThemeData\(\) - otherwise, returns NULL\.

#### Parameters


  - hwnd : int

    The window to get the HTHEME of

## [\_winxptheme](#_winxptheme)\.IsAppThemed



bool =IsAppThemed\(\)
Returns True if a theme is active and available to 

the current process

## [\_winxptheme](#_winxptheme)\.IsThemeActive



bool =IsThemeActive\(\)
Can be used to test if a system theme is active 

for the current user session\.
use the API[\_winxptheme::IsAppThemed](_winxptheme.md#_winxpthemeisappthemed) to test if a theme is 

active for the calling process\.

## [\_winxptheme](#_winxptheme)\.IsThemeDialogTextureEnabled



bool =IsThemeDialogTextureEnabled\(hdlg\)
Reports whether the dialog supports background texturing\.

#### Parameters


  - hdlg : int

    The window handle of the target dialog

## [\_winxptheme](#_winxptheme)\.OpenThemeData

[PyHTHEME](#pyhtheme) =OpenThemeData\(hwnd, pszClassList\)
Open the theme data for the specified HWND and 

semi-colon separated list of class names\.
OpenThemeData\(\) will try each class name, one at 

a time, and use the first matching theme info 

found\.  If a match is found, a theme handle 

to the data is returned\.  If no match is found, 

a "NULL" handle is returned\.
When the window is destroyed or a WM\_THEMECHANGED 

msg is received,[\_winxptheme::CloseThemeData](_winxptheme.md#_winxpthemeclosethemedata) should be 

called to close the theme handle\.

#### Parameters


  - hwnd : int

    Window handle of the control/window to be themed

  - pszClassList : string

    Class name \(or list of names\) to match to theme data 

section\.  if the list contains more than one name, 

the names are tested one at a time for a match\. 

If a match is found, OpenThemeData\(\) returns a 

theme handle associated with the matching class\. 

This param is a list \(instead of just a single 

class name\) to provide the class an opportunity 

to get the "best" match between the class and 

the current theme\.  For example, a button might 

pass L"OkButton, Button" if its ID=ID\_OK\.  If 

the current theme has an entry for OkButton, 

that will be used\.  Otherwise, we fall back on 

the normal Button entry\.

## [\_winxptheme](#_winxptheme)\.SetWindowTheme

SetWindowTheme\(hwnd, pszSubAppName, pszSubIdList\)
Rredirects an existing Window to use a different 

section of the current theme information than its class normally asks for\.

#### Parameters


  - hwnd : int

    The handle of the window \(cannot be 0\)

  - pszSubAppName : string/None

    App \(group\) name to use in place of the calling 

app's name\.  If NULL, the actual calling app name will be used\.

  - pszSubIdList : string/None

    A semicolon separated list of class Id names to 

use in place of actual list passed by the window's class\.  if NULL, the id 

list from the calling class is used\.