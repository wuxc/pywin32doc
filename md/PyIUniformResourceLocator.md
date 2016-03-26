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


## [PyIUniformResourceLocator](PyIUniformResourceLocator.md#pyiuniformresourcelocator)\.GetURL

str = GetURL\(\)
Returns the URL for the shortcut


## [PyIUniformResourceLocator](PyIUniformResourceLocator.md#pyiuniformresourcelocator)\.InvokeCommand

int = InvokeCommand\(Verb, Flags

, hwndParent

\)
Performs one of the object's predefined actions

#### Parameters

  - Verb : str

    The verb to be invoked

  - Flags=0 : int

    Combination of shellcon\.IURL\_INVOKECOMMAND\_\* flags

  - hwndParent=0 : [PyHANDLE](PyHANDLE.md)

    Handle to parent window


## [PyIUniformResourceLocator](PyIUniformResourceLocator.md#pyiuniformresourcelocator)\.SetURL

SetURL\(URL, InFlags\)
Sets the URL for the shortcut

#### Parameters

  - URL : str

    The url to be set

  - InFlags=0 : int

    One of the shellcon\.IURL\_SETURL\* flags