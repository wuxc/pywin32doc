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


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.EnumSubCommands

[PyIEnumExplorerCommand](PyIEnumExplorerCommand.md) = EnumSubCommands\(\)
Description of EnumSubCommands\.


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.GetCanonicalName

[PyIID](PyIID.md) = GetCanonicalName\(\)
Description of GetCanonicalName\.


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.GetFlags

int = GetFlags\(\)
Description of GetFlags\.


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.GetIcon

unicode = GetIcon\(psiItemArray\)
Description of GetIcon\.

#### Parameters

  - psiItemArray : [PyIShellItemArray](PyIShellItemArray.md)

    Description for psiItemArray


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.GetState

int = GetState\(psiItemArray, fOkToBeSlow

\)
Description of GetState\.

#### Parameters

  - psiItemArray : [PyIShellItemArray](PyIShellItemArray.md)

    Description for psiItemArray

  - fOkToBeSlow : int

    Description for fOkToBeSlow


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.GetTitle

unicode = GetTitle\(psiItemArray\)
Description of GetTitle\.

#### Parameters

  - psiItemArray : [PyIShellItemArray](PyIShellItemArray.md)

    Description for psiItemArray


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.GetToolTip

unicode = GetToolTip\(psiItemArray\)
Description of GetToolTip\.

#### Parameters

  - psiItemArray : [PyIShellItemArray](PyIShellItemArray.md)

    Description for psiItemArray


## [PyIExplorerCommand](PyIExplorerCommand.md#pyiexplorercommand)\.Invoke

Invoke\(psiItemArray, pbc\)
Description of Invoke\.

#### Parameters

  - psiItemArray : [PyIShellItemArray](PyIShellItemArray.md)

    Description for psiItemArray

  - pbc : [PyIBindCtx](PyIBindCtx.md)

    Description for pbc