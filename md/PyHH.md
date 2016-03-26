# PyHH

## PyHH\_AKLINK Object



A Python object, representing an HH\_AKLINK structure

#### Comments


Typically you create a PyHH\_AKLINK \(via[win32help::HH\_AKLINK](win32help.md#win32helphh_aklink)\) 

object, and set its properties\. 

The object can then be passed to any function which takes an HH\_AKLINK 

object\.

 

Use this structure to specify one or more ALink names or KLink keywords 

that you want to search for\.

 

If the lookup yields no matching topics, HtmlHelp\(\) checks the values of 

the following HH\_AKLINK members to determine what alternative action to 

take:

 

indexOnFail\. If indexOnFail is TRUE, the Index tab is selected in the 

help window specified in window, and the keyword specified in 

keyword is selected in the entry field\.

 

url\. If indexOnFail is FALSE, the topic file specified in url 

appears in the help window specified in window\.
 

msgText and msgTitle\. If indexOnFail is FALSE and url is NULL, 

a message box appears using the text and caption specified in 

msgText and msgTitle\.

 

Used by
HH\_ALINK\_LOOKUP
HH\_KEYWORD\_LOOKUP


#### Properties

  - int indexOnFail
    Specifies whether to display the keyword in the 

Index tab of the HTML Help Viewer if the lookup fails\. The value of 

window specifies the Help Viewer\.

  - string keywords
    Specifies one or more ALink names or KLink 

keywords to look up\. Multiple entries are delimited by a semicolon\.

  - string url
    Specifies the topic file to navigate to if the lookup 

fails\. url refers to a valid topic within the specified compiled help 

\(\.chm\) file and does not support Internet protocols that point to an 

HTML file\.

  - string msgText
    Specifies the text to display in a message box if 

the lookup fails and indexOnFail is FALSE and url is NULL\.

  - string msgTitle
    Specifies the caption of the message box in which 

the msgText parameter appears\.

  - string window
    Specifies the name of the window type in which to 

display one of the following:

 

The selected topic, if the lookup yields one or more matching topics\. 

The topic specified in url, if the lookup fails and a topic is specified 

in url\.

 

The Index tab, if the lookup fails and indexOnFail is specified as TRUE\.

## PyHH\_FTS\_QUERY Object



A Python object, representing an HH\_FTS\_QUERY 

structure

#### Comments


Typically you create a PyHH\_FTS\_QUERY 

\(via[win32help::HH\_FTS\_QUERY](win32help.md#win32helphh_fts_query)\) object, and set its properties\. 

The object can then be passed to any function which takes an HH\_FTS\_QUERY 

object\.

 

Use this structure for full-text search\.

#### Properties

  - int uniCodeStrings
    TRUE if all strings are Unicode\.

  - long proximity
    Word proximity\.

  - int stemmedSearch
    TRUE for StemmedSearch only\.

  - int titleOnly
    TRUE for Title search only\.

  - int execute
    TRUE to initiate the search\.

  - string searchQuery
    String containing the search query\.

## PyHH\_POPUP Object



A Python object, representing an HH\_POPUP structure

#### Comments


Typically you create a PyHH\_POPUP \(via[win32help::HH\_POPUP](win32help.md#win32helphh_popup)\) 

object, and set its properties\. 

The object can then be passed to any function which takes an HH\_POPUP 

object\.

 

Use this structure to specify or modify the attributes of a pop-up 

window\.

 

Used by
HH\_DISPLAY\_TEXT\_POPUP


#### Properties

  - long hinst
    Instance handle of the program or DLL to retrieve the 

string resource from\. Ignored if idString is zero\.

  - unsigned int idString
    Specifies zero, or a resource ID in the 

program or DLL specified in hinst\.

  - int clrForeground
    Specifies the RGB value to use for the 

foreground color of the pop-up window\. To use the system color for the 

window text, specify -1\.

  - int clrBackground
    Specifies the RGB value to use for the 

background color of the pop-up window\. To use the system color for the 

window background, specify -1\.

  - string text
    Specifies the text to display if idString is zero\.

  - string font
    Specifies the font attributes to use for the text in 

the pop-up window\.
 

Use the following format to specify font family, point size, character 

set, and font format:
 

facename\[, point size\[, charset\[ BOLD ITALIC UNDERLINE\]\]\]
 

To omit an attribute, enter a comma\. For example, to specify bold, 10-pt, 

MS Sans Serif font, font would be:
 

MS Sans Serif, 10, , BOLD

  - tuple pt
    \(x,y\)\. Specifies \(in pixels\) where the top center of the 

pop-up window should be located\.

  - tuple margins
    \(left,top,right,bottom\)\. Specifies \(in pixels\) the 

margins to use on the left, top, right, and bottom sides of the pop-up 

window\. The default for all rectangle members is -1\.

## PyHH\_WINTYPE Object



A Python object, representing an HH\_WINTYPE structure

#### Comments


Typically you create a PyHH\_WINTYPE \(via[win32help::HH\_WINTYPE](win32help.md#win32helphh_wintype)\) 

object, and set its properties\. 

The object can then be passed to any function which takes an HH\_WINTYPE 

object\.

 

Use this structure to specify or modify the attributes of a window type\. 

Window types can be defined by an author in a project \(\.hhp\) file, or they 

can be defined programmatically using the HTML Help API\.
 

When a HH\_WINTYPE structure is passed to HtmlHelp\(\) using theHH\_SET\_WIN\_TYPE



 command, the HTML Help API makes a private copy of the 

contents of the structure\. The help developer is therefore responsible for 

freeing memory used by the HH\_WINTYPE structure or character arrays 

within it\. The help developer can free memory after callingHH\_SET\_WIN\_TYPE



\.

 

Used by
HH\_SET\_WIN\_TYPE
HH\_GET\_WIN\_TYPE


#### Properties

  - int uniCodeStrings
    Specifies whether the strings used in this 

structure are UNICODE\.

  - int validMembers
    Specifies which members in the structure are valid\.

  - int winProperties
    Specifies the properties of the window, such as 

whether it is the standard HTML Help Viewer or whether it includes a 

Search tab\.

  - int styles
    Specifies the styles used to create the window\. These 

styles can be ignored, combined with extended styles, or used exclusively 

depending on the value of the validMembers and winProperties parameters\.

  - int exStyles
    Specifies the extended styles used to create the 

window\. These styles can be ignored, combined with default styles, or used 

exclusively depending on the value of the validMembers and winProperties 

parameters\.

  - int showState
    Specifies the initial display state of the window\. 

Valid values are the same as those for the Win32 API ShowWindow function\.

  - int hwndHelp
    Specifies the handle of the window if the window has 

been created\.

  - int hwndCaller
    Specifies the window that will receive HTML Help 

notification messages\. Notification messages are sent via Windows 

WM\_NOTIFY messages\.

  - int hwndToolBar
    Specifies the handle of the toolbar\.

  - int hwndNavigation
    Specifies the handle of the Navigation pane\.

  - int hwndHTML
    Specifies the handle of the Topic pane, which hosts 

Shdocvw\.dll\.

  - int navWidth
    Specifies the width of the Navigation pane when the 

Help Viewer is expanded\.

  - int toolBarFlags
    Specifies which buttons to include on the toolbar\.

  - int notExpanded
    Specifies that the Help Viewer open with the 

Navigation pane closed\.

  - int curNavType
    Specifies the default tab to display on the 

Navigation pane\.

  - int idNotify
    Specifies a non-zero ID for enabling HTML Help 

notification messages\. This ID is passed as the wParam value of Windows 

WM\_NOTIFY messages\.

  - string typeName
    A null-terminated string that specifies the name 

of the window type\.

  - string caption
    A null-terminated string that specifies the caption 

to display in the title bar of the window\.

  - tuple windowPos
    \(left,top,right,bottom\)\. Specifies the coordinates 

of the window in pixels\.

  - tuple HTMLPos
    \(left,top,right,bottom\)\. Specifies the coordinates 

of the Topic pane\.

  - string toc
    Specifies the contents \(\.hhc\) file to display in the 

Navigation pane\.

  - string index
    Specifies the index \(\.hhk\) file to display in the 

Navigation pane\.

  - string file
    Specifies the default HTML file to display in the 

Topic pane\.

  - string home
    Specifies the file or URL to display in the Topic pane 

when the Home button is clicked\.

  - string jump1
    Specifies the text to display underneath the Jump1 

button\.

  - string jump2
    Specifies the text to display underneath the Jump2 

button\.

  - string urlJump1
    Specifies the URL to jump to when the Jump1 button 

is clicked\.

  - string urlJump2
    Specifies the URL to jump to when the Jump2 button 

is clicked\.