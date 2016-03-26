# PyNOTIFYICONDATA

## PyNOTIFYICONDATA Object

Tuple used to fill a NOTIFYICONDATA struct as used with[win32gui::Shell\_NotifyIcon](win32gui.md#win32guishell_notifyicon)

#### Win32 API References


  - Search for *NOTIFYICONDATA* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=notifyicondata),[google](#http://www.google.com/search?q=notifyicondata)or[google groups](#http://groups.google.com/groups?q=notifyicondata)\.

#### Items


  - \[0\] *[PyHANDLE](#pyhandle)* : hWnd

    Handle to window that will process icon's messages

  - \[1\] *int* : ID

    Unique id used when hWnd processes messages from more than one icon

  - \[2\] *int* : Flags

    Combination of win32gui\.NIF\_\* flags

  - \[3\] *int* : CallbackMessage

    Message id to be pass to hWnd when processing messages

  - \[4\] *[PyHANDLE](#pyhandle)* : hIcon

    Handle to the icon to be displayed

  - \[5\] *str* : Tip

    Tooltip text \(optional\)

  - \[6\] *str* : Info

    Balloon tooltip text \(optional\)

  - \[7\] *int* : Timeout

    Timeout for balloon tooltip, in milliseconds \(optional\)

  - \[8\] *str* : InfoTitle

    Title for balloon tooltip \(optional\)

  - \[9\] *int* : InfoFlags

    Combination of win32gui\.NIIF\_\* flags \(optional\)