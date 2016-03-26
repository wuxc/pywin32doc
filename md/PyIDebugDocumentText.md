# PyIDebugDocumentText

## PyIDebugDocumentText Object

The interface to a text only debug document. Derived from[PyIDebugDocument](#pyidebugdocument)

#### Methods


  - [GetDocumentAttributes](PyIDebugDocumentText.md#pyidebugdocumenttextgetdocumentattributes)

    Description of GetDocumentAttributes&nbsp;

  - [GetSize](PyIDebugDocumentText.md#pyidebugdocumenttextgetsize)

    Description of GetSize&nbsp;

  - [GetPositionOfLine](PyIDebugDocumentText.md#pyidebugdocumenttextgetpositionofline)

    Description of GetPositionOfLine&nbsp;

  - [GetLineOfPosition](PyIDebugDocumentText.md#pyidebugdocumenttextgetlineofposition)

    Description of GetLineOfPosition&nbsp;

  - [GetText](PyIDebugDocumentText.md#pyidebugdocumenttextgettext)

    Description of GetText&nbsp;

  - [GetPositionOfContext](PyIDebugDocumentText.md#pyidebugdocumenttextgetpositionofcontext)

    Description of GetPositionOfContext&nbsp;

  - [GetContextOfPosition](PyIDebugDocumentText.md#pyidebugdocumenttextgetcontextofposition)

    Description of GetContextOfPosition&nbsp;

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetContextOfPosition

 __GetContextOfPosition( *cCharacterPosition*  *, cNumChars* __ )
Description of GetContextOfPosition.

#### Parameters


  -  *cCharacterPosition* : int

    Description for cCharacterPosition

  -  *cNumChars* : int

    Description for cNumChars

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetDocumentAttributes

 __GetDocumentAttributes(__ )
Description of GetDocumentAttributes.

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetLineOfPosition

 __GetLineOfPosition( *cCharacterPosition* __ )
Description of GetLineOfPosition.

#### Parameters


  -  *cCharacterPosition* : int

    Description for cCharacterPosition

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetPositionOfContext

 __GetPositionOfContext( *psc* __ )
Description of GetPositionOfContext.

#### Parameters


  -  *psc* :[PyIDebugDocumentContext](#pyidebugdocumentcontext)

    Description for psc

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetPositionOfLine

 __GetPositionOfLine( *cLineNumber* __ )
Description of GetPositionOfLine.

#### Parameters


  -  *cLineNumber* : int

    Description for cLineNumber

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetSize

 __GetSize(__ )
Description of GetSize.

## [PyIDebugDocumentText](#pyidebugdocumenttext).GetText

 __GetText( *cCharacterPosition*  *, cMaxChars*  *, bWantAttr* __ )
Description of GetText.

#### Parameters


  -  *cCharacterPosition* : int

    

  -  *cMaxChars* : int

    Max chars to return

  -  *bWantAttr=1* : int

    Should the attributes be returned?