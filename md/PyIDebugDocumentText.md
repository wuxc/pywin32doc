# PyIDebugDocumentText

## PyIDebugDocumentText Object

The interface to a text only debug document\. Derived from[PyIDebugDocument](#pyidebugdocument)

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

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetContextOfPosition

 **GetContextOfPosition\( *cCharacterPosition*  *, cNumChars* ** \)
Description of GetContextOfPosition\.

#### Parameters


  -  *cCharacterPosition* : int

    Description for cCharacterPosition

  -  *cNumChars* : int

    Description for cNumChars

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetDocumentAttributes

 **GetDocumentAttributes\(** \)
Description of GetDocumentAttributes\.

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetLineOfPosition

 **GetLineOfPosition\( *cCharacterPosition* ** \)
Description of GetLineOfPosition\.

#### Parameters


  -  *cCharacterPosition* : int

    Description for cCharacterPosition

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetPositionOfContext

 **GetPositionOfContext\( *psc* ** \)
Description of GetPositionOfContext\.

#### Parameters


  -  *psc* :[PyIDebugDocumentContext](#pyidebugdocumentcontext)

    Description for psc

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetPositionOfLine

 **GetPositionOfLine\( *cLineNumber* ** \)
Description of GetPositionOfLine\.

#### Parameters


  -  *cLineNumber* : int

    Description for cLineNumber

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetSize

 **GetSize\(** \)
Description of GetSize\.

## [PyIDebugDocumentText](#pyidebugdocumenttext)\.GetText

 **GetText\( *cCharacterPosition*  *, cMaxChars*  *, bWantAttr* ** \)
Description of GetText\.

#### Parameters


  -  *cCharacterPosition* : int

    

  -  *cMaxChars* : int

    Max chars to return

  -  *bWantAttr\=1* : int

    Should the attributes be returned?