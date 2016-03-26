# VARDESC


## VARDESC Object

A VARDESC object represents a COM VARDESC structure\.

#### Properties

  - int memid

    The dispid of the member

  - int/object value

    A value for the variant\.  If PERINSTANCE then an offset into the instance, otherwise a variant converted to a Python object\.

  - [ELEMDESC](ELEMDESC.md) elemdescVar

    Object describing the member\.

  - int varFlags

    Variable flags

  - int varkind

    Kind flags\.

#### Items

  - \[0\] int : memid

    The id of the member

  - \[1\] int/object : value

    A value for the variant\.  If PERINSTANCE then an offset into the instance, otherwise a variant converted to a Python object\.

  - \[2\] [ELEMDESC](ELEMDESC.md) : elemdescVar

    Object describing the member\.

  - \[3\] int : varFlags

    Variable flags

  - \[4\] int : varKind

    Kind flags\.