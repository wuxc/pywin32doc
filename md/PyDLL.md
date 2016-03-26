# PyDLL


## PyDLL Object

A DLL object\.  A general utility object, and not associated with an MFC object\.

#### Methods

  - [GetFileName](PyDLL.md#pydllgetfilename)

    Returns the file name of the DLL associated with the object\.&nbsp;

  - [AttachToMFC](PyDLL.md#pydllattachtomfc)

    Attaches the DLL to the internal list of MFC DLL's\.&nbsp;


## [PyDLL](PyDLL.md#pydll)\.AttachToMFC

AttachToMFC\(\)
Attaches the DLL object to the MFC list of DLL's\.

#### Comments

After calling this method, MFC will search this DLL when looking for resources\. 

A program can use this function once, instead of specifying the DLL 

in each call to load/find a resource\.
In addition, this is the only way that 

an application can provide status bar messages and tool tips for custom control 

ID's in an external DLL\.


## [PyDLL](PyDLL.md#pydll)\.GetFileName

string = GetFileName\(\)
Returns the name of the module associated with the DLL\.

#### Comments

Note that this is the name that Windows knows the DLL by, not necessarily 

the name that was specified\!


## [PyDLL](PyDLL.md#pydll)\.\_\_repr\_\_

string = \_\_repr\_\_\(\)
Returns the HINSTANCE and filename of the DLL\.

#### Win32 API References

  - Search for GetModuleFileName at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=GetModuleFileName.md), [google](http://www.google.com/search?q=GetModuleFileName.md) or [google groups](http://groups.google.com/groups?q=GetModuleFileName.md)\.