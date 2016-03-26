# PyIExplorerCommand

## PyIExplorerCommand Object

Description of the interface

#### Methods


  - [GetTitle](PyIExplorerCommand.md#pyiexplorercommandgettitle)

    Description of GetTitle&nbsp;

  - [GetIcon](PyIExplorerCommand.md#pyiexplorercommandgeticon)

    Description of GetIcon&nbsp;

  - [GetToolTip](PyIExplorerCommand.md#pyiexplorercommandgettooltip)

    Description of GetToolTip&nbsp;

  - [GetCanonicalName](PyIExplorerCommand.md#pyiexplorercommandgetcanonicalname)

    Description of GetCanonicalName&nbsp;

  - [GetState](PyIExplorerCommand.md#pyiexplorercommandgetstate)

    Description of GetState&nbsp;

  - [Invoke](PyIExplorerCommand.md#pyiexplorercommandinvoke)

    Description of Invoke&nbsp;

  - [GetFlags](PyIExplorerCommand.md#pyiexplorercommandgetflags)

    Description of GetFlags&nbsp;

  - [EnumSubCommands](PyIExplorerCommand.md#pyiexplorercommandenumsubcommands)

    Description of EnumSubCommands&nbsp;

## [PyIExplorerCommand](#pyiexplorercommand).EnumSubCommands

[PyIEnumExplorerCommand](#pyienumexplorercommand)= __EnumSubCommands(__ )
Description of EnumSubCommands.

## [PyIExplorerCommand](#pyiexplorercommand).GetCanonicalName

[PyIID](#pyiid)= __GetCanonicalName(__ )
Description of GetCanonicalName.

## [PyIExplorerCommand](#pyiexplorercommand).GetFlags

int = __GetFlags(__ )
Description of GetFlags.

## [PyIExplorerCommand](#pyiexplorercommand).GetIcon

unicode = __GetIcon( *psiItemArray* __ )
Description of GetIcon.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

## [PyIExplorerCommand](#pyiexplorercommand).GetState

int = __GetState( *psiItemArray*  *, fOkToBeSlow* __ )
Description of GetState.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

  -  *fOkToBeSlow* : int

    Description for fOkToBeSlow

## [PyIExplorerCommand](#pyiexplorercommand).GetTitle

unicode = __GetTitle( *psiItemArray* __ )
Description of GetTitle.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

## [PyIExplorerCommand](#pyiexplorercommand).GetToolTip

unicode = __GetToolTip( *psiItemArray* __ )
Description of GetToolTip.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

## [PyIExplorerCommand](#pyiexplorercommand).Invoke

 __Invoke( *psiItemArray*  *, pbc* __ )
Description of Invoke.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Description for pbc