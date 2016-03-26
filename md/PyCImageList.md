# PyCImageList

## PyCImageList Object

A Python type encapsulating an MFC CImageList class.

#### Methods


  - [Add](PyCImageList.md#pycimagelistadd)

    Adds an icon to the image list.&nbsp;

  - [Destroy](PyCImageList.md#pycimagelistdestroy)

    Destroys the underlying MFC imagelist object.&nbsp;

  - [DeleteImageList](PyCImageList.md#pycimagelistdeleteimagelist)

    Deletes an image list.&nbsp;

  - [GetBkColor](PyCImageList.md#pycimagelistgetbkcolor)

    Retrieves the background color of an Image List.&nbsp;

  - [GetSafeHandle](PyCImageList.md#pycimagelistgetsafehandle)

    Retrieves the HIMAGELIST for the object&nbsp;

  - [GetImageCount](PyCImageList.md#pycimagelistgetimagecount)

    Retrieves the number of images in an image list.&nbsp;

  - [GetImageInfo](PyCImageList.md#pycimagelistgetimageinfo)

    Retrieves information about an image.&nbsp;

  - [SetBkColor](PyCImageList.md#pycimagelistsetbkcolor)

    Sets the background color for an Image List.&nbsp;

## [PyCImageList](#pycimagelist).Add

int = __Add( *bitmap, bitmapMask* __ )
Adds an image to the list.

#### Parameters


  -  *bitmap, bitmapMask* : (int,int)

    2 Bitmaps to use (primary and mask)

#### Alternative Parameters


  -  *bitmap* 

    Bitmap to use

  -  *color* 

    Color to use for the mask.

#### Alternative Parameters


  -  *hIcon* 

    Handle of an icon to add.

#### Return Value
Zero-based index of the first new image.

## [PyCImageList](#pycimagelist).DeleteImageList

 __DeleteImageList(__ )
Deletes an image list.

#### Comments
This frees all resources associated with an image list. 

No further operations on the object will be allowed.

## [PyCImageList](#pycimagelist).Destroy

 __Destroy(__ )
Destroys the underlying CImageList

#### Comments
This method actually calls delete() on the CImageList - you 

should ensure that no controls still require access to this list.

## [PyCImageList](#pycimagelist).GetBkColor

int = __GetBkColor(__ )
Retrieves the background color of an Image List.

## [PyCImageList](#pycimagelist).GetImageCount

int = __GetImageCount(__ )
Retrieves the number of images in an image list.

## [PyCImageList](#pycimagelist).GetImageInfo

iiii(iiii) = __GetImageInfo( *index* __ )
Retrieves information about an image.

#### Parameters


  -  *index* : int

    Index of image.

#### Return Value
The return info is a tuple describing an IMAGELIST structure.

## [PyCImageList](#pycimagelist).GetSafeHandle

int = __GetSafeHandle(__ )
Retrieves the HIMAGELIST for the object

## [PyCImageList](#pycimagelist).SetBkColor

 __SetBkColor( *color* __ )
Sets the background color for an Image List.

#### Parameters


  -  *color* : int

    The new background color.