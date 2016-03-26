# PyIDebugDocumentText


## PyIDebugDocumentText Object

The interface to a text only debug document\. Derived from [PyIDebugDocument](PyIDebugDocument.md)

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


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetContextOfPosition

GetContextOfPosition\(cCharacterPosition, cNumChars\)
Description of GetContextOfPosition\.

#### Parameters

  - cCharacterPosition : int

    Description for cCharacterPosition

  - cNumChars : int

    Description for cNumChars


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetDocumentAttributes

GetDocumentAttributes\(\)
Description of GetDocumentAttributes\.


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetLineOfPosition

GetLineOfPosition\(cCharacterPosition\)
Description of GetLineOfPosition\.

#### Parameters

  - cCharacterPosition : int

    Description for cCharacterPosition


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetPositionOfContext

GetPositionOfContext\(psc\)
Description of GetPositionOfContext\.

#### Parameters

  - psc : [PyIDebugDocumentContext](PyIDebugDocumentContext.md)

    Description for psc


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetPositionOfLine

GetPositionOfLine\(cLineNumber\)
Description of GetPositionOfLine\.

#### Parameters

  - cLineNumber : int

    Description for cLineNumber


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetSize

GetSize\(\)
Description of GetSize\.


## [PyIDebugDocumentText](PyIDebugDocumentText.md#pyidebugdocumenttext)\.GetText

GetText\(cCharacterPosition, cMaxChars, bWantAttr\)
Description of GetText\.

#### Parameters

  - cCharacterPosition : int

    

  - cMaxChars : int

    Max chars to return

  - bWantAttr=1 : int

    Should the attributes be returned?