# PyDLGTEMPLATE

## PyDLGTEMPLATE Object



A tuple of items describing a dialog box, that can be used to create the dialog\.

#### Win32 API References


  - Search forDLGTEMPLATE at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=dlgtemplate),[google](#http://www.google.com/search?q=dlgtemplate) or[google groups](#http://groups.google.com/groups?q=dlgtemplate)\.

#### Items


  - \[0\]string : caption

    The caption for the window

  - \[1\]\(int,int,int,int\) : \(x,y,cx,cy\)

    The bounding rectange for the dialog\.

  - \[2\]int : style

    The style bits for the dialog\.  Combination of WS\_\* and DS\_\* constants\. 

Note that the DS\_SETFONT style need never be specified - it is determined by the font item \(below\)
See MSDN documentation on Dialog Boxes for allowable values\.

  - \[3\]int : extStyle

    The extended style bits for the dialog\. Defaults to 0 if not passed and None is supported for backwards compatibility\.

  - \[4\]\(int, string\) : \(fontSize, fontName\)

    A tuple describing the font, or None if the system default font is to be used\.

  - \[5\][PyResourceId](#pyresourceid) : menuResource

    The resource ID of the menu to be used for the dialog, or None for no menu\.

  - \[6\][PyResourceId](#pyresourceid) : windowClass

    Window class name or atom as returned from RegisterWindowClass\.  Defaults to None\.