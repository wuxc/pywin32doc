# PyITypeComp

## PyITypeComp Object

An object that implements the ITypeComp interface.

#### Methods


  - [Bind](PyITypeComp.md#pyitypecompbind)

    Retrieves specified binding description.&nbsp;

  - [BindType](PyITypeComp.md#pyitypecompbindtype)

    Retrieves specified binding description for a type 

sentinel&nbsp;


## [PyITypeComp](#pyitypecomp).Bind

 __DESCKIND__ = __Bind( *szName*  *, wflags* __ )
binds to a variable/type

#### Parameters


  -  *szName* : string

    The name to bind to

  -  *wflags=0* : int

    the bind flags

## [PyITypeComp](#pyitypecomp).BindType

 __DESCKIND__ = __BindType( *szName* __ )
binds to a type

#### Parameters


  -  *szName* : string

    The name to bind to