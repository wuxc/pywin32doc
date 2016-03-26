# FORM


## FORM\_INFO\_1 Object

A dictionary containing FORM\_INFO\_1W data

#### Properties

  - int Flags

    FORM\_USER, FORM\_BUILTIN, or FORM\_PRINTER

  - [PyUnicode](PyUnicode.md) Name

    Name of form

  - dict Size

    A dictionary representing a SIZEL structure \{'cx':int,'cy':int\}

  - dict ImageableArea

    A dictionary representing a RECTL structure \{'left':int, 'top':int, 'right':int, 'bottom':int\}