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

## [PyIShellItem](#pyishellitem)\.BindToHandler

interface \= **BindToHandler\( *pbc*  *, bhid*  *, riid* ** \)
Creates an instance of one of the item's handlers

#### Parameters


  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Used to pass parameters that influence the binding operation, can be None

  -  *bhid* :[PyIID](#pyiid)

    GUID that identifies a handler \(shell\.BHID\_\*\)

  -  *riid* :[PyIID](#pyiid)

    The interface to return

## [PyIShellItem](#pyishellitem)\.Compare

int \= **Compare\( *psi*  *, hint* ** \)
Compares another shell item with this item

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    A shell item to be compared with this item

  -  *hint* : int

    shellcon\.SICHINT\_\* value indicating how the comparison is to be performed

#### Return Value
Returns 0 if items compare as equal, nonzero otherwise

## [PyIShellItem](#pyishellitem)\.GetAttributes

int \= **GetAttributes\( *Mask* ** \)
Returns shell attributes of the item

#### Parameters


  -  *Mask* : int

    Combination of shellcon\.SFGAO\_\* values indicating the flags to return

#### Return Value
Returns a combination of shellcon\.SFGAO\_\* values

## [PyIShellItem](#pyishellitem)\.GetDisplayName

str \= **GetDisplayName\( *sigdnName* ** \)
Returns the display name of the item in the specified format

#### Parameters


  -  *sigdnName* : int

    Format of name to return, shellcon\.SIGDN\_\*

## [PyIShellItem](#pyishellitem)\.GetParent

[PyIShellItem](#pyishellitem)\= **GetParent\(** \)
Retrieves the parent of this item