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

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).AppendRoot

 __AppendRoot( *psiRoot*  *, grfEnumFlags*  *, grfRootStyle*  *, pif* __ )
Description of AppendRoot.

#### Parameters


  -  *psiRoot* :[PyIShellItem](#pyishellitem)

    Description for psiRoot

  -  *grfEnumFlags* : int

    Description for grfEnumFlags

  -  *grfRootStyle* : int

    Description for grfRootStyle

  -  *pif* : __PyIShellItemFilter__ 

    Description for pif

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).CollapseAll

 __CollapseAll(__ )
Description of CollapseAll.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).EnsureItemVisible

 __EnsureItemVisible( *psi* __ )
Description of EnsureItemVisible.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).GetItemCustomState

 __GetItemCustomState( *psi* __ )
Description of GetItemCustomState.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).GetItemRect

 __GetItemRect(__ )
Description of GetItemRect.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).GetItemState

 __GetItemState( *psi*  *, nstcisMask* __ )
Description of GetItemState.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *nstcisMask* : int

    Description for nstcisMask

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).GetNextItem

 __GetNextItem( *psi*  *, nstcgi* __ )
Description of GetNextItem.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *nstcgi* : int

    Description for nstcgi

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).GetRootItems

 __GetRootItems(__ )
Description of GetRootItems.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).GetSelectedItems

 __GetSelectedItems(__ )
Description of GetSelectedItems.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).HitTest

 __HitTest( *pt* __ )
Description of HitTest.

#### Parameters


  -  *pt* : (int, int)

    Description for ppt

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).Initialize

 __Initialize( *hwndParent*  *, prc*  *, nsctsFlags* __ )
Description of Initialize.

#### Parameters


  -  *hwndParent* : int/long

    Description for hwndParent

  -  *prc* : (int, int, int, int)

    Description for prc

  -  *nsctsFlags* : int

    Description for nsctsFlags

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).InsertRoot

 __InsertRoot( *iIndex*  *, psiRoot*  *, grfEnumFlags*  *, grfRootStyle*  *, pif* __ )
Description of InsertRoot.

#### Parameters


  -  *iIndex* : int

    Description for iIndex

  -  *psiRoot* :[PyIShellItem](#pyishellitem)

    Description for psiRoot

  -  *grfEnumFlags* : int

    Description for grfEnumFlags

  -  *grfRootStyle* : int

    Description for grfRootStyle

  -  *pif* : __PyIShellItemFilter__ 

    Description for pif

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).RemoveAllRoots

 __RemoveAllRoots(__ )
Description of RemoveAllRoots.

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).RemoveRoot

 __RemoveRoot( *psiRoot* __ )
Description of RemoveRoot.

#### Parameters


  -  *psiRoot* :[PyIShellItem](#pyishellitem)

    Description for psiRoot

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).SetItemCustomState

 __SetItemCustomState( *psi*  *, iStateNumber* __ )
Description of SetItemCustomState.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *iStateNumber* : int

    Description for iStateNumber

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).SetItemState

 __SetItemState( *psi*  *, nstcisMask*  *, nstcisFlags* __ )
Description of SetItemState.

#### Parameters


  -  *psi* :[PyIShellItem](#pyishellitem)

    Description for psi

  -  *nstcisMask* : int

    Description for nstcisMask

  -  *nstcisFlags* : int

    Description for nstcisFlags

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).SetTheme

 __SetTheme( *pszTheme* __ )
Description of SetTheme.

#### Parameters


  -  *pszTheme* : __unicode__ 

    Description for pszTheme

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).TreeAdvise

 __TreeAdvise( *punk* __ )
Description of TreeAdvise.

#### Parameters


  -  *punk* :[PyIUnknown](#pyiunknown)

    Description for punk

## [PyINameSpaceTreeControl](#pyinamespacetreecontrol).TreeUnadvise

 __TreeUnadvise( *dwCookie* __ )
Description of TreeUnadvise.

#### Parameters


  -  *dwCookie* : int

    Description for dwCookie