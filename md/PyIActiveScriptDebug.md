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


## [PyIActiveScriptDebug](PyIActiveScriptDebug.md#pyiactivescriptdebug)\.EnumCodeContextsOfPosition

EnumCodeContextsOfPosition\(dwSourceContext, uCharacterOffset, uNumChars\)
Description of EnumCodeContextsOfPosition\.

#### Parameters

  - dwSourceContext : int

    Description for dwSourceContext

  - uCharacterOffset : int

    Description for uCharacterOffset

  - uNumChars : int

    Description for uNumChars


## [PyIActiveScriptDebug](PyIActiveScriptDebug.md#pyiactivescriptdebug)\.GetScriptTextAttributes

\(int,\.\.\.\) = GetScriptTextAttributes\(pstrCode, pstrDelimiter

, dwFlags

\)
Returns the text attributes for an arbitrary block of script text\.

#### Parameters

  - pstrCode : string

    The script block text\.

  - pstrDelimiter : string

    See PyIActiveScriptParse::ParseScriptText

 for a description of this argument\.

  - dwFlags : int

    See PyIActiveScriptParse::ParseScriptText

 for a description of this argument\.

#### Comments

Smart hosts use this call to delegate GetText calls made on their axscript::PyIDebugDocumentText




## [PyIActiveScriptDebug](PyIActiveScriptDebug.md#pyiactivescriptdebug)\.GetScriptletTextAttributes

GetScriptletTextAttributes\(pstrCode, pstrDelimiter, dwFlags\)
Description of GetScriptletTextAttributes\.

#### Parameters

  - pstrCode : string

    The script block text\.

  - pstrDelimiter : string

    See PyIActiveScriptParse::ParseScriptText

 for a description of this argument\.

  - dwFlags : int

    See PyIActiveScriptParse::ParseScriptText

 for a description of this argument\.