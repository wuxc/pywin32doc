# PyHH

## PyHH_AKLINK Object

A Python object, representing an HH_AKLINK structure

#### Comments
Typically you create a PyHH_AKLINK (via[win32help::HH_AKLINK](win32help.md#win32helphh_aklink)) 

object, and set its properties. 

The object can then be passed to any function which takes an HH_AKLINK 

object.

Use this structure to specify one or more ALink names or KLink keywords 

that you want to search for.

If the lookup yields no matching topics, HtmlHelp() checks the values of 

the following HH_AKLINK members to determine what alternative action to 

take:

indexOnFail. If indexOnFail is TRUE, the Index tab is selected in the 

help window specified in window, and the keyword specified in 

keyword is selected in the entry field.

url. If indexOnFail is FALSE, the topic file specified in url 

appears in the help window specified in window.
msgText and msgTitle. If indexOnFail is FALSE and url is NULL, 

a message box appears using the text and caption specified in 

msgText and msgTitle.

Used by
 __HH_ALINK_LOOKUP__ 
 __HH_KEYWORD_LOOKUP__ 


#### Properties

  -  __int indexOnFail__ 
    Specifies whether to display the keyword in the 

Index tab of the HTML Help Viewer if the lookup fails. The value of 

window specifies the Help Viewer.

  -  __string keywords__ 
    Specifies one or more ALink names or KLink 

keywords to look up. Multiple entries are delimited by a semicolon.

  -  __string url__ 
    Specifies the topic file to navigate to if the lookup 

fails. url refers to a valid topic within the specified compiled help 

(.chm) file and does not support Internet protocols that point to an 

HTML file.

  -  __string msgText__ 
    Specifies the text to display in a message box if 

the lookup fails and indexOnFail is FALSE and url is NULL.

  -  __string msgTitle__ 
    Specifies the caption of the message box in which 

the msgText parameter appears.

  -  __string window__ 
    Specifies the name of the window type in which to 

display one of the following:

The selected topic, if the lookup yields one or more matching topics. 

The topic specified in url, if the lookup fails and a topic is specified 

in url.

The Index tab, if the lookup fails and indexOnFail is specified as TRUE.

## PyHH_FTS_QUERY Object

A Python object, representing an HH_FTS_QUERY 

structure

#### Comments
Typically you create a PyHH_FTS_QUERY 

(via[win32help::HH_FTS_QUERY](win32help.md#win32helphh_fts_query)) object, and set its properties. 

The object can then be passed to any function which takes an HH_FTS_QUERY 

object.

Use this structure for full-text search.

#### Properties

  -  __int uniCodeStrings__ 
    TRUE if all strings are Unicode.

  -  __long proximity__ 
    Word proximity.

  -  __int stemmedSearch__ 
    TRUE for StemmedSearch only.

  -  __int titleOnly__ 
    TRUE for Title search only.

  -  __int execute__ 
    TRUE to initiate the search.

  -  __string searchQuery__ 
    String containing the search query.

## PyHH_POPUP Object

A Python object, representing an HH_POPUP structure

#### Comments
Typically you create a PyHH_POPUP (via[win32help::HH_POPUP](win32help.md#win32helphh_popup)) 

object, and set its properties. 

The object can then be passed to any function which takes an HH_POPUP 

object.

Use this structure to specify or modify the attributes of a pop-up 

window.

Used by
 __HH_DISPLAY_TEXT_POPUP__ 


#### Properties

  -  __long hinst__ 
    Instance handle of the program or DLL to retrieve the 

string resource from. Ignored if idString is zero.

  -  __unsigned int idString__ 
    Specifies zero, or a resource ID in the 

program or DLL specified in hinst.

  -  __int clrForeground__ 
    Specifies the RGB value to use for the 

foreground color of the pop-up window. To use the system color for the 

window text, specify -1.

  -  __int clrBackground__ 
    Specifies the RGB value to use for the 

background color of the pop-up window. To use the system color for the 

window background, specify -1.

  -  __string text__ 
    Specifies the text to display if idString is zero.

  -  __string font__ 
    Specifies the font attributes to use for the text in 

the pop-up window.
Use the following format to specify font family, point size, character 

set, and font format:
facename[, point size[, charset[ BOLD ITALIC UNDERLINE]]]
To omit an attribute, enter a comma. For example, to specify bold, 10-pt, 

MS Sans Serif font, font would be:
MS Sans Serif, 10, , BOLD

  -  __tuple pt__ 
    (x,y). Specifies (in pixels) where the top center of the 

pop-up window should be located.

  -  __tuple margins__ 
    (left,top,right,bottom). Specifies (in pixels) the 

margins to use on the left, top, right, and bottom sides of the pop-up 

window. The default for all rectangle members is -1.

## PyHH_WINTYPE Object

A Python object, representing an HH_WINTYPE structure

#### Comments
Typically you create a PyHH_WINTYPE (via[win32help::HH_WINTYPE](win32help.md#win32helphh_wintype)) 

object, and set its properties. 

The object can then be passed to any function which takes an HH_WINTYPE 

object.

Use this structure to specify or modify the attributes of a window type. 

Window types can be defined by an author in a project (.hhp) file, or they 

can be defined programmatically using the HTML Help API.
When a HH_WINTYPE structure is passed to HtmlHelp() using the __HH_SET_WIN_TYPE__ command, the HTML Help API makes a private copy of the 

contents of the structure. The help developer is therefore responsible for 

freeing memory used by the HH_WINTYPE structure or character arrays 

within it. The help developer can free memory after calling __HH_SET_WIN_TYPE__ .

Used by
 __HH_SET_WIN_TYPE__ 
 __HH_GET_WIN_TYPE__ 


#### Properties

  -  __int uniCodeStrings__ 
    Specifies whether the strings used in this 

structure are UNICODE.

  -  __int validMembers__ 
    Specifies which members in the structure are valid.

  -  __int winProperties__ 
    Specifies the properties of the window, such as 

whether it is the standard HTML Help Viewer or whether it includes a 

Search tab.

  -  __int styles__ 
    Specifies the styles used to create the window. These 

styles can be ignored, combined with extended styles, or used exclusively 

depending on the value of the validMembers and winProperties parameters.

  -  __int exStyles__ 
    Specifies the extended styles used to create the 

window. These styles can be ignored, combined with default styles, or used 

exclusively depending on the value of the validMembers and winProperties 

parameters.

  -  __int showState__ 
    Specifies the initial display state of the window. 

Valid values are the same as those for the Win32 API ShowWindow function.

  -  __int hwndHelp__ 
    Specifies the handle of the window if the window has 

been created.

  -  __int hwndCaller__ 
    Specifies the window that will receive HTML Help 

notification messages. Notification messages are sent via Windows 

WM_NOTIFY messages.

  -  __int hwndToolBar__ 
    Specifies the handle of the toolbar.

  -  __int hwndNavigation__ 
    Specifies the handle of the Navigation pane.

  -  __int hwndHTML__ 
    Specifies the handle of the Topic pane, which hosts 

Shdocvw.dll.

  -  __int navWidth__ 
    Specifies the width of the Navigation pane when the 

Help Viewer is expanded.

  -  __int toolBarFlags__ 
    Specifies which buttons to include on the toolbar.

  -  __int notExpanded__ 
    Specifies that the Help Viewer open with the 

Navigation pane closed.

  -  __int curNavType__ 
    Specifies the default tab to display on the 

Navigation pane.

  -  __int idNotify__ 
    Specifies a non-zero ID for enabling HTML Help 

notification messages. This ID is passed as the wParam value of Windows 

WM_NOTIFY messages.

  -  __string typeName__ 
    A null-terminated string that specifies the name 

of the window type.

  -  __string caption__ 
    A null-terminated string that specifies the caption 

to display in the title bar of the window.

  -  __tuple windowPos__ 
    (left,top,right,bottom). Specifies the coordinates 

of the window in pixels.

  -  __tuple HTMLPos__ 
    (left,top,right,bottom). Specifies the coordinates 

of the Topic pane.

  -  __string toc__ 
    Specifies the contents (.hhc) file to display in the 

Navigation pane.

  -  __string index__ 
    Specifies the index (.hhk) file to display in the 

Navigation pane.

  -  __string file__ 
    Specifies the default HTML file to display in the 

Topic pane.

  -  __string home__ 
    Specifies the file or URL to display in the Topic pane 

when the Home button is clicked.

  -  __string jump1__ 
    Specifies the text to display underneath the Jump1 

button.

  -  __string jump2__ 
    Specifies the text to display underneath the Jump2 

button.

  -  __string urlJump1__ 
    Specifies the URL to jump to when the Jump1 button 

is clicked.

  -  __string urlJump2__ 
    Specifies the URL to jump to when the Jump2 button 

is clicked.