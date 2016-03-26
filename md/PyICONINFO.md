# PyICONINFO

## PyICONINFO Object

Tuple describing an icon or cursor

#### Win32 API References


  - Search for *ICONINFO* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=iconinfo),[google](#http://www.google.com/search?q=iconinfo)or[google groups](#http://groups.google.com/groups?q=iconinfo).

#### Items


  - [0] *boolean* : Icon

    True indicates an icon, False for a cursor

  - [1] *int* : xHotSpot

    For a cursor, X coord of hotspot.  Ignored for icons

  - [2] *int* : yHotSpot

    For a cursor, Y coord of hotspot.  Ignored for icons

  - [3] *[PyGdiHANDLE](#pygdihandle)* : hbmMask

    Monochrome mask bitmap

  - [4] *[PyGdiHANDLE](#pygdihandle)* : hbmColor

    Color bitmap, may be None for black and white icon