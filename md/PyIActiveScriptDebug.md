# PyIActiveScriptDebug

## PyIActiveScriptDebug Object



Description of the interface

#### Methods


  - [GetScriptTextAttributes](PyIActiveScriptDebug.md#pyiactivescriptdebuggetscripttextattributes)

    Description of GetScriptTextAttributes&nbsp;

  - [GetScriptletTextAttributes](PyIActiveScriptDebug.md#pyiactivescriptdebuggetscriptlettextattributes)

    Description of GetScriptletTextAttributes&nbsp;

  - [EnumCodeContextsOfPosition](PyIActiveScriptDebug.md#pyiactivescriptdebugenumcodecontextsofposition)

    Description of EnumCodeContextsOfPosition&nbsp;

## [PyIActiveScriptDebug](#pyiactivescriptdebug)\.EnumCodeContextsOfPosition

EnumCodeContextsOfPosition\(dwSourceContext, uCharacterOffset, uNumChars\)
Description of EnumCodeContextsOfPosition\.

#### Parameters


  - dwSourceContext : int

    Description for dwSourceContext

  - uCharacterOffset : int

    Description for uCharacterOffset

  - uNumChars : int

    Description for uNumChars

## [PyIActiveScriptDebug](#pyiactivescriptdebug)\.GetScriptTextAttributes



\(int,\.\.\.\) =GetScriptTextAttributes\(pstrCode, pstrDelimiter, dwFlags\)
Returns the text attributes for an arbitrary block of script text\.

#### Parameters


  - pstrCode : string

    The script block text\.

  - pstrDelimiter : string

    SeePyIActiveScriptParse::ParseScriptText



 for a description of this argument\.

  - dwFlags : int

    SeePyIActiveScriptParse::ParseScriptText



 for a description of this argument\.

#### Comments


Smart hosts use this call to delegate GetText calls made on theiraxscript::PyIDebugDocumentText

## [PyIActiveScriptDebug](#pyiactivescriptdebug)\.GetScriptletTextAttributes

GetScriptletTextAttributes\(pstrCode, pstrDelimiter, dwFlags\)
Description of GetScriptletTextAttributes\.

#### Parameters


  - pstrCode : string

    The script block text\.

  - pstrDelimiter : string

    SeePyIActiveScriptParse::ParseScriptText



 for a description of this argument\.

  - dwFlags : int

    SeePyIActiveScriptParse::ParseScriptText



 for a description of this argument\.