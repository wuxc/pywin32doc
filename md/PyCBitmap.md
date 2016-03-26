# PyCBitmap

## PyCBitmap Object



A bitmap class, derived from a[PyCGdiObject](#pycgdiobject)\.

#### Methods


  - [CreateCompatibleBitmap](PyCBitmap.md#pycbitmapcreatecompatiblebitmap)

    Creates a bitmap compatible with the specified device context\.&nbsp;

  - [GetSize](PyCBitmap.md#pycbitmapgetsize)

    Gets the size of the bitmap object, in pixels\.&nbsp;

  - [GetHandle](PyCBitmap.md#pycbitmapgethandle)

    Returns the HBITMAP for a bitmap\.&nbsp;

  - [LoadBitmap](PyCBitmap.md#pycbitmaploadbitmap)

    Loads a bitmap from a DLL object\.&nbsp;

  - [LoadBitmapFile](PyCBitmap.md#pycbitmaploadbitmapfile)

    Loads a bitmap from a file object\.&nbsp;

  - [LoadPPMFile](PyCBitmap.md#pycbitmaploadppmfile)

    Loads a bitmap from a file object containing a PPM format bitmap\.&nbsp;

  - [Paint](PyCBitmap.md#pycbitmappaint)

    Paints a bitmap to a windows DC\.&nbsp;

  - [GetInfo](PyCBitmap.md#pycbitmapgetinfo)

    Returns the BITMAP structure info\.&nbsp;

  - [GetBitmapBits](PyCBitmap.md#pycbitmapgetbitmapbits)

    Returns the bitmap bits\.&nbsp;

  - [SaveBitmapFile](PyCBitmap.md#pycbitmapsavebitmapfile)

    Saves a bitmap to a file\. 

sentinel&nbsp;

## [PyCBitmap](#pycbitmap)\.CreateCompatibleBitmap

CreateCompatibleBitmap\(dc, width, height\)
Creates a bitmap compatible with the specified device context\.

#### Parameters


  - dc :[PyCDC](#pycdc)

    Specifies the device context\.

  - width : int

    The width \(in bits\) of the bitmap

  - height : int

    The height \(in bits\) of the bitmap\.

## [PyCBitmap](#pycbitmap)\.GetBitmapBits



tuple/string =GetBitmapBits\(asString\)
Returns the bitmap bits\.

#### Parameters


  - asString=0 : int

    If False, the result is a tuple of 

integers, if True, the result is a Python string

## [PyCBitmap](#pycbitmap)\.GetHandle



int =GetHandle\(\)
Returns the HBITMAP for a bitmap object

## [PyCBitmap](#pycbitmap)\.GetInfo



dict =GetInfo\(\)
Returns the BITMAP structure info

#### Return Value
A dictionary of integers, keyed by the following strings:
 

bmType
 

bmWidth
 

bmHeight
 

bmWidthBytes
 

bmPlanes
 

bmBitsPixel


## [PyCBitmap](#pycbitmap)\.GetSize



\(cx,cy\) =GetSize\(\)
Returns the size of the bitmap object\.

## [PyCBitmap](#pycbitmap)\.LoadBitmap

LoadBitmap\(idRes, obDLL\)
Loads a bitmap from a DLL object\.

#### Parameters


  - idRes : int

    The resource ID of the bitmap

  - obDLL=None :[PyDLL](#pydll)

    The DLL object to load from\.

## [PyCBitmap](#pycbitmap)\.LoadBitmapFile

LoadBitmapFile\(fileObject\)
Loads a bitmap \(\.BMP\) format 

from a file object\.

#### Parameters


  - fileObject : file\[\.read\]

    The file object to load the \.BMP format file from\.

## [PyCBitmap](#pycbitmap)\.LoadPPMFile

LoadPPMFile\(fileObject, cols, rows\)
Loads a bitmap in Portable Pix Map \(PPM\) format 

from a file object\.

#### Parameters


  - fileObject : file\[\.read\]

    The file object to load the PPM format file from\.

  - cols : int

    The number of columns in the bitmap\.

  - rows : int

    The number of rows in the bitmap\.

## [PyCBitmap](#pycbitmap)\.Paint

Paint\(dcObject, rectDest, rectSrc\)
Paint a bitmap\.

#### Parameters


  - dcObject :[PyCDC](#pycdc)

    The DC object to paint the bitmap to\.

  - rectDest=\(0,0,0,0\) : \(left,top,right,bottom\)

    The destination rectangle to paint to\.

  - rectSrc=\(0,0,0,0\) : \(left,top,right,bottom\)

    The source rectangle to paint from\.

## [PyCBitmap](#pycbitmap)\.SaveBitmapFile



None =SaveBitmapFile\(dcObject, Filename\)
Saves a bitmap to a file\.

#### Parameters


  - dcObject :[PyCDC](#pycdc)

    The DC object that has rendered the bitmap\.

  - Filename : string

    The file to save the bitmap to