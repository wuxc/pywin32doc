# VARDESC

## VARDESC Object

A VARDESC object represents a COM VARDESC structure.

#### Properties

  -  __int memid__ 
    The dispid of the member

  -  __int/object value__ 
    A value for the variant.  If PERINSTANCE then an offset into the instance, otherwise a variant converted to a Python object.

  -  __[ELEMDESC](#elemdesc)elemdescVar__ 
    Object describing the member.

  -  __int varFlags__ 
    Variable flags

  -  __int varkind__ 
    Kind flags.

#### Items


  - [0] *int* : memid

    The id of the member

  - [1] *int/object* : value

    A value for the variant.  If PERINSTANCE then an offset into the instance, otherwise a variant converted to a Python object.

  - [2] *[ELEMDESC](#elemdesc)* : elemdescVar

    Object describing the member.

  - [3] *int* : varFlags

    Variable flags

  - [4] *int* : varKind

    Kind flags.