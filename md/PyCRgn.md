# PyCRgn

## PyCRgn Object



An object encapsulating an MFC PyCRgn class\.

## [PyCRgn](#pycrgn)\.CombineRgn



int =CombineRgn\(\)
Creates a new GDI region by combining two existing regions\. The regions are combined as specified by nCombineMode 

Return Values: success or failure flag \(BOOL\)

## [PyCRgn](#pycrgn)\.CopyRgn



int =CopyRgn\(\)
Copies the region defined by pRgnSrc into the CRgn object 

Return Values: success or failure flag \(BOOL\)

## [PyCRgn](#pycrgn)\.CreateEllipticRgn



int =CreateEllipticRgn\(\)
Initializes a region to an ellipse 

Return Values: success or failure flag \(BOOL\)

## [PyCRgn](#pycrgn)\.CreateRectRgn



int =CreateRectRgn\(\)
Initializes a region to a rectangle 

Return Values: success or failure flag \(BOOL\)

## [PyCRgn](#pycrgn)\.DeleteObject



int =DeleteObject\(\)
Deletes the attached Windows GDI Rgn object from memory by freeing all system storage associated with the Windows GDI object 

Return Values: None

## [PyCRgn](#pycrgn)\.GetRgnBox



int =GetRgnBox\(\)
Retrieves the coordinates of the bounding rectangle of the CRgn object 

Return Values: the bounding rectangle as a tuple \(l,t,r,b\)

## [PyCRgn](#pycrgn)\.GetSafeHandle



int =GetSafeHandle\(\)
A HANDLE to the attached Windows GDI object; otherwise NULL if no object is attached 

Return Values: the handle of the CRgn object