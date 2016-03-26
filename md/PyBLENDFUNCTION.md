# PyBLENDFUNCTION


## PyBLENDFUNCTION Object

Tuple of four small ints used to fill a BLENDFUNCTION struct 

Each int must fit in a byte \(0-255\)\.

#### Win32 API References

  - Search for BLENDFUNCTION at [msdn](http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=BLENDFUNCTION.md), [google](http://www.google.com/search?q=BLENDFUNCTION.md) or [google groups](http://groups.google.com/groups?q=BLENDFUNCTION.md)\.

#### Items

  - \[0\] int : BlendOp

    Only defined value is AC\_SRC\_OVER \(0\)

  - \[1\] int : BlendFlags

    None currently defined, must be 0

  - \[2\] int : SourceConstantAlpha

    Transparency to be applied to entire source\. \(255 is opaque\)

  - \[3\] int : AlphaFormat

    Only defined flag is AC\_SRC\_ALPHA, used when src bitmap contains per-pixel alpha