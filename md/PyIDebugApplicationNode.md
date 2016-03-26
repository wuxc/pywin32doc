# PyIDebugApplicationNode

## PyIDebugApplicationNode Object

Provides the functionality of IDebugDocumentProvider, plus a context within a project tree\.  Derived from[PyIDebugDocumentProvider](#pyidebugdocumentprovider)

#### Methods


  - [EnumChildren](PyIDebugApplicationNode.md#pyidebugapplicationnodeenumchildren)

    Description of EnumChildren&nbsp;

  - [GetParent](PyIDebugApplicationNode.md#pyidebugapplicationnodegetparent)

    Description of GetParent&nbsp;

  - [SetDocumentProvider](PyIDebugApplicationNode.md#pyidebugapplicationnodesetdocumentprovider)

    Description of SetDocumentProvider&nbsp;

  - [Close](PyIDebugApplicationNode.md#pyidebugapplicationnodeclose)

    Description of Close&nbsp;

  - [Attach](PyIDebugApplicationNode.md#pyidebugapplicationnodeattach)

    Attach a node to its parent\.&nbsp;

  - [Detach](PyIDebugApplicationNode.md#pyidebugapplicationnodedetach)

    Detach a node from its parent\.&nbsp;

## [PyIDebugApplicationNode](#pyidebugapplicationnode)\.Attach

 **Attach\( *pdanParent* ** \)
Attach a node to its parent\.

#### Parameters


  -  *pdanParent* :[PyIDebugApplicationNode](#pyidebugapplicationnode)

    The parent node\.  None is not acceptable\.

## [PyIDebugApplicationNode](#pyidebugapplicationnode)\.Close

 **Close\(** \)
Description of Close\.

## [PyIDebugApplicationNode](#pyidebugapplicationnode)\.Detach

 **Detach\(** \)
Detach a node from its parent\.

## [PyIDebugApplicationNode](#pyidebugapplicationnode)\.EnumChildren

 **EnumChildren\(** \)
Description of EnumChildren\.

## [PyIDebugApplicationNode](#pyidebugapplicationnode)\.GetParent

[PyIDebugApplicationNode](#pyidebugapplicationnode)\= **GetParent\(** \)
Returns the parent node\.

## [PyIDebugApplicationNode](#pyidebugapplicationnode)\.SetDocumentProvider

 **SetDocumentProvider\( *pddp* ** \)
Description of SetDocumentProvider\.

#### Parameters


  -  *pddp* :[PyIDebugDocumentProvider](#pyidebugdocumentprovider)

    Description for pddp