# PyIActiveScriptSiteDebug

## PyIActiveScriptSiteDebug Object



Description of the interface

#### Methods


  - [GetDocumentContextFromPosition](PyIActiveScriptSiteDebug.md#pyiactivescriptsitedebuggetdocumentcontextfromposition)

    Description of GetDocumentContextFromPosition&nbsp;

  - [GetApplication](PyIActiveScriptSiteDebug.md#pyiactivescriptsitedebuggetapplication)

    Description of GetApplication&nbsp;

  - [GetRootApplicationNode](PyIActiveScriptSiteDebug.md#pyiactivescriptsitedebuggetrootapplicationnode)

    Description of GetRootApplicationNode&nbsp;

  - [OnScriptErrorDebug](PyIActiveScriptSiteDebug.md#pyiactivescriptsitedebugonscripterrordebug)

    Allows a smart host to control the handling of runtime errors&nbsp;

## [PyIActiveScriptSiteDebug](#pyiactivescriptsitedebug)\.GetApplication

GetApplication\(\)
Description of GetApplication\.

## [PyIActiveScriptSiteDebug](#pyiactivescriptsitedebug)\.GetDocumentContextFromPosition

GetDocumentContextFromPosition\(dwSourceContext, uCharacterOffset, uNumChars\)
Description of GetDocumentContextFromPosition\.

#### Parameters


  - dwSourceContext : int

    Description for dwSourceContext

  - uCharacterOffset : int

    Description for uCharacterOffset

  - uNumChars : int

    Description for uNumChars

## [PyIActiveScriptSiteDebug](#pyiactivescriptsitedebug)\.GetRootApplicationNode

GetRootApplicationNode\(\)
Description of GetRootApplicationNode\.

## [PyIActiveScriptSiteDebug](#pyiactivescriptsitedebug)\.OnScriptErrorDebug



int, int =OnScriptErrorDebug\(\)
Allows a smart host to control the handling of runtime errors

#### Return Value
The result is a tuple of \(bCallDebugger, bCallOnScriptErrorWhenContinuing\)