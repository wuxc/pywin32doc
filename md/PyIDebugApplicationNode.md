# PyIDebugApplicationNode

## PyIDebugApplicationNode Object

Provides the functionality of IDebugDocumentProvider, plus a context within a project tree.  Derived from[PyIDebugDocumentProvider](#pyidebugdocumentprovider)

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

    Attach a node to its parent.&nbsp;

  - [Detach](PyIDebugApplicationNode.md#pyidebugapplicationnodedetach)

    Detach a node from its parent.&nbsp;

## [PyIDebugApplicationNode](#pyidebugapplicationnode).Attach

 __Attach( *pdanParent* __ )
Attach a node to its parent.

#### Parameters


  -  *pdanParent* :[PyIDebugApplicationNode](#pyidebugapplicationnode)

    The parent node.  None is not acceptable.

## [PyIDebugApplicationNode](#pyidebugapplicationnode).Close

 __Close(__ )
Description of Close.

## [PyIDebugApplicationNode](#pyidebugapplicationnode).Detach

 __Detach(__ )
Detach a node from its parent.

## [PyIDebugApplicationNode](#pyidebugapplicationnode).EnumChildren

 __EnumChildren(__ )
Description of EnumChildren.

## [PyIDebugApplicationNode](#pyidebugapplicationnode).GetParent

[PyIDebugApplicationNode](#pyidebugapplicationnode)= __GetParent(__ )
Returns the parent node.

## [PyIDebugApplicationNode](#pyidebugapplicationnode).SetDocumentProvider

 __SetDocumentProvider( *pddp* __ )
Description of SetDocumentProvider.

#### Parameters


  -  *pddp* :[PyIDebugDocumentProvider](#pyidebugdocumentprovider)

    Description for pddp