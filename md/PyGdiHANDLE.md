# PyGdiHANDLE


## PyGdiHANDLE Object

Gdi objects such as brush \(HBRUSH\), pen \(HPEN\), font \(HFONT\), region \(HRGN\), bitmap \(HBITMAP\) 

On destruction, the handle is closed using DeleteObject\.  The object's Close\(\) method also calls DeleteObject\. 

The gdi object should be deselected from any DC that it is selected into before it's closed\. 

Inherits the methods and properties of [PyHANDLE](PyHANDLE.md)\.