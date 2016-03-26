# PyDEVMODEW

## PyDEVMODEW Object

Unicode version of[PyDEVMODE](#pydevmode)object 

PyDEVMODEW is only needed when win32api, win32gui, or win32print 

are built with UNICODE defined.  Currently, you must explicitely ask 

for the unicode version.

#### Methods


  - [Clear](PyDEVMODEW.md#pydevmodewclear)

    Resets all members of the structure&nbsp;

#### Properties

  -  __int SpecVersion__ 
    Should always be set to DM_SPECVERSION

  -  __int DriverVersion__ 
    Version nbr assigned to printer driver by vendor

  -  __int Size__ 
    Size of structure

  -  __int DriverExtra__ 
    Number of extra bytes allocated for driver data, can only be set when new object is created

  -  __int Fields__ 
    Bitmask of win32con.DM_* constants indicating which members are set

  -  __int Orientation__ 
    Only applies to printers, DMORIENT_PORTRAIT or DMORIENT_LANDSCAPE

  -  __int PaperSize__ 
    Use 0 if PaperWidth and PaperLength are set, otherwise win32con.DMPAPER_* constant

  -  __int PaperLength__ 
    Specified in 1/10 millimeters

  -  __int PaperWidth__ 
    Specified in 1/10 millimeters

  -  __int Position_x__ 
    Position of display relative to desktop

  -  __int Position_y__ 
    Position of display relative to desktop

  -  __int DisplayOrientation__ 
    Display rotation: DMDO_DEFAULT,DMDO_90, DMDO_180, DMDO_270

  -  __int DisplayFixedOutput__ 
    DMDFO_DEFAULT, DMDFO_CENTER, DMDFO_STRETCH

  -  __int Scale__ 
    Specified as percentage, eg 50 means half size of original

  -  __int Copies__ 
    Nbr of copies to print

  -  __int DefaultSource__ 
    DMBIN_* constant, or can be a printer-specific value

  -  __int PrintQuality__ 
    DMRES_* constant, interpreted as DPI if positive

  -  __int Color__ 
    DMCOLOR_COLOR or DMCOLOR_MONOCHROME

  -  __int Duplex__ 
    For printers that do two-sided printing: DMDUP_SIMPLEX, DMDUP_HORIZONTAL, DMDUP_VERTICAL

  -  __int YResolution__ 
    Vertical printer resolution in DPI - if this is set, PrintQuality indicates horizontal DPI

  -  __int TTOption__ 
    TrueType options: DMTT_BITMAP, DMTT_DOWNLOAD, DMTT_DOWNLOAD_OUTLINE, DMTT_SUBDEV

  -  __int Collate__ 
    DMCOLLATE_TRUE or DMCOLLATE_FALSE

  -  __int LogPixels__ 
    Pixels per inch (only for display devices

  -  __int BitsPerPel__ 
    Color resolution in bits per pixel

  -  __int PelsWidth__ 
    Pixel width of display

  -  __int PelsHeight__ 
    Pixel height of display

  -  __int DisplayFlags__ 
    Combination of DM_GRAYSCALE and DM_INTERLACED

  -  __int DisplayFrequency__ 
    Refresh rate

  -  __int DisplayOrientation__ 
    Display rotation: DMDO_DEFAULT,DMDO_90, DMDO_180, DMDO_270

  -  __int ICMMethod__ 
    Indicates where ICM is performed, one of win32con.DMICMMETHOD_* values

  -  __int ICMIntent__ 
    Intent of ICM, one of win32con.DMICM_* values

  -  __int MediaType__ 
    win32con.DMMEDIA_*, can also be a printer-specific value greater then DMMEDIA_USER

  -  __int DitherType__ 
    Dithering option, win32con.DMDITHER_*

  -  __int Reserved1__ 
    Reserved, use only 0

  -  __int Reserved2__ 
    Reserved, use only 0

  -  __int Nup__ 
    Controls printing of multiple logical pages per physical page, DMNUP_SYSTEM or DMNUP_ONEUP

  -  __int PanningWidth__ 
    Not used, leave as 0

  -  __int PanningHeight__ 
    Not used, leave as 0

  -  __[PyUnicode](#pyunicode)DeviceName__ 
    String of at most 32 chars

  -  __str FormName__ 
    Name of form as returned by[win32print::EnumForms](win32print.md#win32printenumforms), at most 32 chars

  -  __str DriverData__ 
    Driver data appended to end of structure