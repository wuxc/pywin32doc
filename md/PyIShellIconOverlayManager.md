# PyIShellIconOverlayManager

## PyIShellIconOverlayManager Object

Description of the interface

#### Methods


  - [GetFileOverlayInfo](PyIShellIconOverlayManager.md#pyishelliconoverlaymanagergetfileoverlayinfo)

    Description of GetFileOverlayInfo&nbsp;

  - [GetReservedOverlayInfo](PyIShellIconOverlayManager.md#pyishelliconoverlaymanagergetreservedoverlayinfo)

    Description of GetReservedOverlayInfo&nbsp;

  - [RefreshOverlayImages](PyIShellIconOverlayManager.md#pyishelliconoverlaymanagerrefreshoverlayimages)

    Description of RefreshOverlayImages&nbsp;

  - [LoadNonloadedOverlayIdentifiers](PyIShellIconOverlayManager.md#pyishelliconoverlaymanagerloadnonloadedoverlayidentifiers)

    Description of LoadNonloadedOverlayIdentifiers&nbsp;

  - [OverlayIndexFromImageIndex](PyIShellIconOverlayManager.md#pyishelliconoverlaymanageroverlayindexfromimageindex)

    Description of OverlayIndexFromImageIndex&nbsp;

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager)\.GetFileOverlayInfo

int \= **GetFileOverlayInfo\( *path*  *, attrib*  *, flags* ** \)
Returns an index into the system image list for the icon image or overlay image

#### Parameters


  -  *path* : str

    Full path to the file

  -  *attrib* : int

    File attributes \(win32com\.FILE\_ATTRIBUTE\_\*\)

  -  *flags* : int

    SIOM\_OVERLAYINDEX \(1\) or SIOM\_ICONINDEX \(2\)

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager)\.GetReservedOverlayInfo

 **GetReservedOverlayInfo\( *path*  *, attrib*  *, flags*  *, ireservedID* ** \)
Description of GetReservedOverlayInfo\.

#### Parameters


  -  *path* : str

    Description for path

  -  *attrib* : int

    Description for attrib

  -  *flags* : int

    Description for flags

  -  *ireservedID* : int

    Description for ireservedID

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager)\.LoadNonloadedOverlayIdentifiers

 **LoadNonloadedOverlayIdentifiers\(** \)
Description of LoadNonloadedOverlayIdentifiers\.

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager)\.OverlayIndexFromImageIndex

 **OverlayIndexFromImageIndex\( *iImage*  *, fAdd* ** \)
Description of OverlayIndexFromImageIndex\.

#### Parameters


  -  *iImage* : int

    Description for iImage

  -  *fAdd* : int

    Description for fAdd

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager)\.RefreshOverlayImages

 **RefreshOverlayImages\( *flags* ** \)
Description of RefreshOverlayImages\.

#### Parameters


  -  *flags* : int

    Description for flags