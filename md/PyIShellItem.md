# PyIShellItem

## PyIShellItem Object

Interface that represents an item in the Explorer shell

#### Methods


  - [BindToHandler](PyIShellItem.md#pyishellitembindtohandler)

    Creates an instance of one of the item's handlers&nbsp;

  - [GetParent](PyIShellItem.md#pyishellitemgetparent)

    Retrieves the parent of this item&nbsp;

  - [GetDisplayName](PyIShellItem.md#pyishellitemgetdisplayname)

    Returns the display name of the item in the specified format&nbsp;

  - [GetAttributes](PyIShellItem.md#pyishellitemgetattributes)

    Returns shell attributes of the item&nbsp;

  - [Compare](PyIShellItem.md#pyishellitemcompare)

    Compares another shell item with this item&nbsp;

## [PyIShellItem](#pyishellitem).BindToHandler

interface = __BindToHandler( *pbc*  *, bhid*  *, riid* __ )
Creates an instance of one of the item's handlers

#### Parameters


  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Used to pass parameters that influence the binding operation, can be None

  -  *bhid* :[PyIID](#pyiid)

    GUID that identifies a handler (shell.BHID_*)

  -  *riid* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItem](#pyishellitem).Compare

int = __Compare( *psi*  *, hint* __ )
Compares another shell item with this item

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    A shell item to be compared with this item

  -  *hint* : int

    shellcon.SICHINT_* value indicating how the comparison is to be performed

#### Return Value
Returns 0 if items compare as equal, nonzero otherwise

## [PyIShellItem](#pyishellitem).GetAttributes

int = __GetAttributes( *Mask* __ )
Returns shell attributes of the item

#### Parameters


  -  *Mask* : int

    Combination of shellcon.SFGAO_* values indicating the flags to return

#### Return Value
Returns a combination of shellcon.SFGAO_* values

## [PyIShellItem](#pyishellitem).GetDisplayName

str = __GetDisplayName( *sigdnName* __ )
Returns the display name of the item in the specified format

#### Parameters


  -  *sigdnName* : int

    Format of name to return, shellcon.SIGDN_*

## [PyIShellItem](#pyishellitem).GetParent

[PyIShellItem](#pyishellitem)= __GetParent(__ )
Retrieves the parent of this item