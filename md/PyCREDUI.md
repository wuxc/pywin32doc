# PyCREDUI

## PyCREDUI\_INFO Object



A dictionary representing a CREDUI\_INFO structure, used with[win32cred::CredUIPromptForCredentials](win32cred.md#win32credcreduipromptforcredentials)

#### Comments


All members are optional

#### Win32 API References


  - Search forCREDUI\_INFO at[msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CREDUI.md#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=creduiinfo),[google](http://www.google.com/search?q=CREDUI.md#http://www.google.com/search?q=creduiinfo) or[google groups](http://groups.google.com/groups?q=CREDUI.md#http://groups.google.com/groups?q=creduiinfo)\.

#### Properties

  - [PyHANDLE](#pyhandle) Parent
    Handle to parent window, can be None

  - [PyUnicode](#pyunicode) MessageText
    Message to appear in dialog

  - [PyUnicode](#pyunicode) CaptionText
    Title of the dialog window

  - [PyHANDLE](#pyhandle) Banner
    Handle to a bitmap to be displayed