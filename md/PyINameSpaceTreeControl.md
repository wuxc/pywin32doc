# PyINameSpaceTreeControl

## PyINameSpaceTreeControl Object

Description of the interface

#### Methods


  - [Initialize](PyINameSpaceTreeControl.md#pyinamespacetreecontrolinitialize)

    Description of Initialize&nbsp;

  - [TreeAdvise](PyINameSpaceTreeControl.md#pyinamespacetreecontroltreeadvise)

    Description of TreeAdvise&nbsp;

  - [TreeUnadvise](PyINameSpaceTreeControl.md#pyinamespacetreecontroltreeunadvise)

    Description of TreeUnadvise&nbsp;

  - [AppendRoot](PyINameSpaceTreeControl.md#pyinamespacetreecontrolappendroot)

    Description of AppendRoot&nbsp;

  - [InsertRoot](PyINameSpaceTreeControl.md#pyinamespacetreecontrolinsertroot)

    Description of InsertRoot&nbsp;

  - [RemoveRoot](PyINameSpaceTreeControl.md#pyinamespacetreecontrolremoveroot)

    Description of RemoveRoot&nbsp;

  - [RemoveAllRoots](PyINameSpaceTreeControl.md#pyinamespacetreecontrolremoveallroots)

    Description of RemoveAllRoots&nbsp;

  - [GetRootItems](PyINameSpaceTreeControl.md#pyinamespacetreecontrolgetrootitems)

    Description of GetRootItems&nbsp;

  - [SetItemState](PyINameSpaceTreeControl.md#pyinamespacetreecontrolsetitemstate)

    Description of SetItemState&nbsp;

  - [GetItemState](PyINameSpaceTreeControl.md#pyinamespacetreecontrolgetitemstate)

    Description of GetItemState&nbsp;

  - [GetSelectedItems](PyINameSpaceTreeControl.md#pyinamespacetreecontrolgetselecteditems)

    Description of GetSelectedItems&nbsp;

  - [GetItemCustomState](PyINameSpaceTreeControl.md#pyinamespacetreecontrolgetitemcustomstate)

    Description of GetItemCustomState&nbsp;

  - [SetItemCustomState](PyINameSpaceTreeControl.md#pyinamespacetreecontrolsetitemcustomstate)

    Description of SetItemCustomState&nbsp;

  - [EnsureItemVisible](PyINameSpaceTreeControl.md#pyinamespacetreecontrolensureitemvisible)

    Description of EnsureItemVisible&nbsp;

  - [SetTheme](PyINameSpaceTreeControl.md#pyinamespacetreecontrolsettheme)

    Description of SetTheme&nbsp;

  - [GetNextItem](PyINameSpaceTreeControl.md#pyinamespacetreecontrolgetnextitem)

    Description of GetNextItem&nbsp;

  - [HitTest](PyINameSpaceTreeControl.md#pyinamespacetreecontrolhittest)

    Description of HitTest&nbsp;

  - [GetItemRect](PyINameSpaceTreeControl.md#pyinamespacetreecontrolgetitemrect)

    Description of GetItemRect&nbsp;

  - [CollapseAll](PyINameSpaceTreeControl.md#pyinamespacetreecontrolcollapseall)

    Description of CollapseAll&nbsp;

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.AppendRoot

 **AppendRoot\( *psiRoot*  *, grfEnumFlags*  *, grfRootStyle*  *, pif* ** \)
Description of AppendRoot\.

#### Parameters


  -  *psiRoot* :[PyIShellItem](#pyishellitem)

    Description for psiRoot

  -  *grfEnumFlags* : int

    Description for grfEnumFlags

  -  *grfRootStyle* : int

    Description for grfRootStyle

  -  *pif* : **PyIShellItemFilter** 

    Description for pif

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.CollapseAll

 **CollapseAll\(** \)
Description of CollapseAll\.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.EnsureItemVisible

 **EnsureItemVisible\( *psi* ** \)
Description of EnsureItemVisible\.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.GetItemCustomState

 **GetItemCustomState\( *psi* ** \)
Description of GetItemCustomState\.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.GetItemRect

 **GetItemRect\(** \)
Description of GetItemRect\.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.GetItemState

 **GetItemState\( *psi*  *, nstcisMask* ** \)
Description of GetItemState\.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *nstcisMask* : int

    Description for nstcisMask

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.GetNextItem

 **GetNextItem\( *psi*  *, nstcgi* ** \)
Description of GetNextItem\.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *nstcgi* : int

    Description for nstcgi

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.GetRootItems

 **GetRootItems\(** \)
Description of GetRootItems\.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.GetSelectedItems

 **GetSelectedItems\(** \)
Description of GetSelectedItems\.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.HitTest

 **HitTest\( *pt* ** \)
Description of HitTest\.

#### Parameters


  -  *pt* : \(int, int\)

    Description for ppt

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.Initialize

 **Initialize\( *hwndParent*  *, prc*  *, nsctsFlags* ** \)
Description of Initialize\.

#### Parameters


  -  *hwndParent* : int/long

    Description for hwndParent

  -  *prc* : \(int, int, int, int\)

    Description for prc

  -  *nsctsFlags* : int

    Description for nsctsFlags

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.InsertRoot

 **InsertRoot\( *iIndex*  *, psiRoot*  *, grfEnumFlags*  *, grfRootStyle*  *, pif* ** \)
Description of InsertRoot\.

#### Parameters


  -  *iIndex* : int

    Description for iIndex

  -  *psiRoot* :[PyIShellItem](#pyishellitem)

    Description for psiRoot

  -  *grfEnumFlags* : int

    Description for grfEnumFlags

  -  *grfRootStyle* : int

    Description for grfRootStyle

  -  *pif* : **PyIShellItemFilter** 

    Description for pif

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.RemoveAllRoots

 **RemoveAllRoots\(** \)
Description of RemoveAllRoots\.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.RemoveRoot

 **RemoveRoot\( *psiRoot* ** \)
Description of RemoveRoot\.

#### Parameters


  -  *psiRoot* :[PyIShellItem](#pyishellitem)

    Description for psiRoot

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.SetItemCustomState

 **SetItemCustomState\( *psi*  *, iStateNumber* ** \)
Description of SetItemCustomState\.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *iStateNumber* : int

    Description for iStateNumber

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.SetItemState

 **SetItemState\( *psi*  *, nstcisMask*  *, nstcisFlags* ** \)
Description of SetItemState\.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *nstcisMask* : int

    Description for nstcisMask

  -  *nstcisFlags* : int

    Description for nstcisFlags

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.SetTheme

 **SetTheme\( *pszTheme* ** \)
Description of SetTheme\.

#### Parameters


  -  *pszTheme* : **unicode** 

    Description for pszTheme

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.TreeAdvise

 **TreeAdvise\( *punk* ** \)
Description of TreeAdvise\.

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Description for punk

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol)\.TreeUnadvise

 **TreeUnadvise\( *dwCookie* ** \)
Description of TreeUnadvise\.

#### Parameters


  -  *dwCookie* : int

    Description for dwCookie