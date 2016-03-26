# PyBLENDFUNCTION

## PyBLENDFUNCTION Object

Tuple of four small ints used to fill a BLENDFUNCTION struct 

Each int must fit in a byte (0-255).

#### Win32 API References


  - Search for *BLENDFUNCTION* at[msdn](#http://search.msdn.microsoft.com/search/results.aspx?view=msdn&query=blendfunction),[google](#http://www.google.com/search?q=blendfunction)or[google groups](#http://groups.google.com/groups?q=blendfunction).

#### Items


  - [0] *int* : BlendOp

    Only defined value is AC_SRC_OVER (0)

  - [1] *int* : BlendFlags

    None currently defined, must be 0

  - [2] *int* : SourceConstantAlpha

    Transparency to be applied to entire source. (255 is opaque)

  - [3] *int* : AlphaFormat

    Only defined flag is AC_SRC_ALPHA, used when src bitmap contains per-pixel alpha