# mmapfile


## Module mmapfile

Compiled extension module that provides access to the memory mapped file API

#### Methods

  - [mmapfile](mmapfile.md#mmapfilemmapfile)

    Creates or opens a file mapping, and maps a view into memory&nbsp;


## [mmapfile](mmapfile.md#mmapfile)\.mmapfile

[Pymmapfile](Pymmapfile.md) = mmapfile\(File, Name

, MaximumSize

, FileOffset

, NumberOfBytesToMap

\)
Creates or opens a memory mapped file\. 

This method uses the following API functions: CreateFileMapping, MapViewOfFile, VirtualQuery

#### Parameters

  - File : str

    Name of file\.  Use None or '' when opening an existing named mapping, or to use system pagefile\.

  - Name : str

    Name of mapping object to create or open, can be None

  - MaximumSize=0 : int

    Size of file mapping to create, should be specified as a multiple 

of system page size \(see [win32api::GetSystemInfo](win32api.md#win32apigetsysteminfo)\)\.  Defaults to size of existing file if 0\. 

If an existing named mapping is opened, the returned object will have the same size as the original mapping\.

  - FileOffset=0 : int

    Offset into the file at which to create view\.  This should be specified as a 

multiple of system allocation granularity\. \(see [win32api::GetSystemInfo](win32api.md#win32apigetsysteminfo)\)

  - NumberOfBytesToMap=0 : int

    Size of view to create, also a multiple of system page size\. 

If 0, view will span from offset to end of file mapping\.

#### Comments

Accepts keyword args\.

#### Win32 API References

  - Search for CreateFileMapping at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=CreateFileMapping.md), [google](http://www.google.com/search?q=CreateFileMapping.md) or [google groups](http://groups.google.com/groups?q=CreateFileMapping.md)\.

  - Search for MapViewOfFile at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=MapViewOfFile.md), [google](http://www.google.com/search?q=MapViewOfFile.md) or [google groups](http://groups.google.com/groups?q=MapViewOfFile.md)\.

  - Search for VirtualQuery at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=VirtualQuery.md), [google](http://www.google.com/search?q=VirtualQuery.md) or [google groups](http://groups.google.com/groups?q=VirtualQuery.md)\.