# PyIUniformResourceLocator

## PyIUniformResourceLocator Object

Interface to an internet shortcut

#### Methods


  - [GetURL](PyIUniformResourceLocator.md#pyiuniformresourcelocatorgeturl)

    Returns the URL for the shortcut&nbsp;

  - [SetURL](PyIUniformResourceLocator.md#pyiuniformresourcelocatorseturl)

    Sets the URL for the shortcut&nbsp;

  - [InvokeCommand](PyIUniformResourceLocator.md#pyiuniformresourcelocatorinvokecommand)

    Performs one of the object's predefined actions&nbsp;

## [PyIUniformResourceLocator](#pyiuniformresourcelocator).GetURL

str = __GetURL(__ )
Returns the URL for the shortcut

## [PyIUniformResourceLocator](#pyiuniformresourcelocator).InvokeCommand

int = __InvokeCommand( *Verb*  *, Flags*  *, hwndParent* __ )
Performs one of the object's predefined actions

#### Parameters


  -  *Verb* : str

    The verb to be invoked

  -  *Flags=0* : int

    Combination of shellcon.IURL_INVOKECOMMAND_* flags

  -  *hwndParent=0* :[PyHANDLE](#pyhandle)

    Handle to parent window

## [PyIUniformResourceLocator](#pyiuniformresourcelocator).SetURL

 __SetURL( *URL*  *, InFlags* __ )
Sets the URL for the shortcut

#### Parameters


  -  *URL* : str

    The url to be set

  -  *InFlags=0* : int

    One of the shellcon.IURL_SETURL* flags