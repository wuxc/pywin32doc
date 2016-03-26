# PyDEVMODE

## PyDEVMODE Object



Python object wrapping a DEVMODE structure

#### Methods


  - [Clear](PyDEVMODE.md#pydevmodeclear)

    Resets all members of the structure&nbsp;

#### Properties

  - int SpecVersion
    Should always be set to DM\_SPECVERSION

  - int DriverVersion
    Version nbr assigned to printer driver by vendor

  - int Size
    Size of structure

  - int DriverExtra
    Number of extra bytes allocated for driver data, can only be set when new object is created

  - int Fields
    Bitmask of win32con\.DM\_\* constants indicating which members are set

  - int Orientation
    Only applies to printers, DMORIENT\_PORTRAIT or DMORIENT\_LANDSCAPE

  - int PaperSize
    Use 0 if PaperWidth and PaperLength are set, otherwise win32con\.DMPAPER\_\* constant

  - int PaperLength
    Specified in 1/10 millimeters

  - int PaperWidth
    Specified in 1/10 millimeters

  - int Position\_x
    Position of display relative to desktop

  - int Position\_y
    Position of display relative to desktop

  - int DisplayOrientation
    Display rotation: DMDO\_DEFAULT,DMDO\_90, DMDO\_180, DMDO\_270

  - int DisplayFixedOutput
    DMDFO\_DEFAULT, DMDFO\_CENTER, DMDFO\_STRETCH

  - int Scale
    Specified as percentage, eg 50 means half size of original

  - int Copies
    Nbr of copies to print

  - int DefaultSource
    DMBIN\_\* constant, or can be a printer-specific value

  - int PrintQuality
    DMRES\_\* constant, interpreted as DPI if positive

  - int Color
    DMCOLOR\_COLOR or DMCOLOR\_MONOCHROME

  - int Duplex
    For printers that do two-sided printing: DMDUP\_SIMPLEX, DMDUP\_HORIZONTAL, DMDUP\_VERTICAL

  - int YResolution
    Vertical printer resolution in DPI - if this is set, PrintQuality indicates horizontal DPI

  - int TTOption
    TrueType options: DMTT\_BITMAP, DMTT\_DOWNLOAD, DMTT\_DOWNLOAD\_OUTLINE, DMTT\_SUBDEV

  - int Collate
    DMCOLLATE\_TRUE or DMCOLLATE\_FALSE

  - int LogPixels
    Pixels per inch \(only for display devices

  - int BitsPerPel
    Color resolution in bits per pixel

  - int PelsWidth
    Pixel width of display

  - int PelsHeight
    Pixel height of display

  - int DisplayFlags
    Combination of DM\_GRAYSCALE and DM\_INTERLACED

  - int DisplayFrequency
    Refresh rate

  - int DisplayOrientation
    Display rotation: DMDO\_DEFAULT,DMDO\_90, DMDO\_180, DMDO\_270

  - int ICMMethod
    Indicates where ICM is performed, one of win32con\.DMICMMETHOD\_\* values

  - int ICMIntent
    Intent of ICM, one of win32con\.DMICM\_\* values

  - int MediaType
    win32con\.DMMEDIA\_\*, can also be a printer-specific value greater then DMMEDIA\_USER

  - int DitherType
    Dithering option, win32con\.DMDITHER\_\*

  - int Reserved1
    Reserved, use only 0

  - int Reserved2
    Reserved, use only 0

  - int Nup
    Controls printing of multiple logical pages per physical page, DMNUP\_SYSTEM or DMNUP\_ONEUP

  - int PanningWidth
    Not used, leave as 0

  - int PanningHeight
    Not used, leave as 0

  - str DeviceName
    String of at most 32 chars

  - str FormName
    Name of form as returned by[win32print::EnumForms](win32print.md#win32printenumforms), at most 32 chars

  - str DriverData
    Driver data appended to end of structure

## [PyDEVMODE](#pydevmode)\.Clear

Clear\(\)
Resets all members of the structure

## [PyDEVMODE](#pydevmode)\.Clear

Clear\(\)
Resets all members of the structure