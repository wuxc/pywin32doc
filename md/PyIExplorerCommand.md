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

## [PyIExplorerCommand](#pyiexplorercommand)\.EnumSubCommands

[PyIEnumExplorerCommand](#pyienumexplorercommand)\= **EnumSubCommands\(** \)
Description of EnumSubCommands\.

## [PyIExplorerCommand](#pyiexplorercommand)\.GetCanonicalName

[PyIID](#pyiid)\= **GetCanonicalName\(** \)
Description of GetCanonicalName\.

## [PyIExplorerCommand](#pyiexplorercommand)\.GetFlags

int \= **GetFlags\(** \)
Description of GetFlags\.

## [PyIExplorerCommand](#pyiexplorercommand)\.GetIcon

unicode \= **GetIcon\( *psiItemArray* ** \)
Description of GetIcon\.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

## [PyIExplorerCommand](#pyiexplorercommand)\.GetState

int \= **GetState\( *psiItemArray*  *, fOkToBeSlow* ** \)
Description of GetState\.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

  -  *fOkToBeSlow* : int

    Description for fOkToBeSlow

## [PyIExplorerCommand](#pyiexplorercommand)\.GetTitle

unicode \= **GetTitle\( *psiItemArray* ** \)
Description of GetTitle\.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

## [PyIExplorerCommand](#pyiexplorercommand)\.GetToolTip

unicode \= **GetToolTip\( *psiItemArray* ** \)
Description of GetToolTip\.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

## [PyIExplorerCommand](#pyiexplorercommand)\.Invoke

 **Invoke\( *psiItemArray*  *, pbc* ** \)
Description of Invoke\.

#### Parameters


  -  *psiItemArray* :[PyIShellItemArray](#pyishellitemarray)

    Description for psiItemArray

  -  *pbc* :[PyIBindCtx](#pyibindctx)

    Description for pbc