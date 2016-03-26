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

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager).GetFileOverlayInfo

int = __GetFileOverlayInfo( *path*  *, attrib*  *, flags* __ )
Returns an index into the system image list for the icon image or overlay image

#### Parameters


  -  *path* : str

    Full path to the file

  -  *attrib* : int

    File attributes (win32com.FILE_ATTRIBUTE_*)

  -  *flags* : int

    SIOM_OVERLAYINDEX (1) or SIOM_ICONINDEX (2)

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager).GetReservedOverlayInfo

 __GetReservedOverlayInfo( *path*  *, attrib*  *, flags*  *, ireservedID* __ )
Description of GetReservedOverlayInfo.

#### Parameters


  -  *path* : str

    Description for path

  -  *attrib* : int

    Description for attrib

  -  *flags* : int

    Description for flags

  -  *ireservedID* : int

    Description for ireservedID

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager).LoadNonloadedOverlayIdentifiers

 __LoadNonloadedOverlayIdentifiers(__ )
Description of LoadNonloadedOverlayIdentifiers.

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager).OverlayIndexFromImageIndex

 __OverlayIndexFromImageIndex( *iImage*  *, fAdd* __ )
Description of OverlayIndexFromImageIndex.

#### Parameters


  -  *iImage* : int

    Description for iImage

  -  *fAdd* : int

    Description for fAdd

## [PyIShellIconOverlayManager](#pyishelliconoverlaymanager).RefreshOverlayImages

 __RefreshOverlayImages( *flags* __ )
Description of RefreshOverlayImages.

#### Parameters


  -  *flags* : int

    Description for flags