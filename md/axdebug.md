# axdebug

## Module axdebug

A module, encapsulating the ActiveX Debugging interfaces

## APPBREAKFLAG_DEBUGGER_BLOCK
 __const axdebug.APPBREAKFLAG_DEBUGGER_BLOCK;__ 
Languages should break immediately with BREAKREASON_DEBUGGER_BLOCK

## APPBREAKFLAG_DEBUGGER_HALT
 __const axdebug.APPBREAKFLAG_DEBUGGER_HALT;__ 
Languages should break immediately with BREAKREASON_DEBUGGER_HALT

## APPBREAKFLAG_STEP
 __const axdebug.APPBREAKFLAG_STEP;__ 
ADD_CONSTANT(APPBREAKFLAG_APPBREAKFLAG_NESTED);

## BREAKPOINT_DELETED
 __const axdebug.BREAKPOINT_DELETED;__ 


## BREAKPOINT_DISABLED
 __const axdebug.BREAKPOINT_DISABLED;__ 


## BREAKPOINT_ENABLED
 __const axdebug.BREAKPOINT_ENABLED;__ 


## BREAKREASON_BREAKPOINT
 __const axdebug.BREAKREASON_BREAKPOINT;__ 
Caused by an explicit breakpoint

## BREAKREASON_DEBUGGER_BLOCK
 __const axdebug.BREAKREASON_DEBUGGER_BLOCK;__ 
Caused by another thread breaking

## BREAKREASON_DEBUGGER_HALT
 __const axdebug.BREAKREASON_DEBUGGER_HALT;__ 
Caused by debugger IDE requested break

## BREAKREASON_ERROR
 __const axdebug.BREAKREASON_ERROR;__ 
Caused by an execution error

## BREAKREASON_HOST_INITIATED
 __const axdebug.BREAKREASON_HOST_INITIATED;__ 
Caused by host requested break

## BREAKREASON_LANGUAGE_INITIATED
 __const axdebug.BREAKREASON_LANGUAGE_INITIATED;__ 
Caused by a scripted break

## BREAKREASON_STEP
 __const axdebug.BREAKREASON_STEP;__ 
Caused by the stepping mode

## BREAKRESUMEACTION_ABORT
 __const axdebug.BREAKRESUMEACTION_ABORT;__ 
Abort the application

## BREAKRESUMEACTION_CONTINUE
 __const axdebug.BREAKRESUMEACTION_CONTINUE;__ 
Continue running

## BREAKRESUMEACTION_STEP_INTO
 __const axdebug.BREAKRESUMEACTION_STEP_INTO;__ 
Step into a procedure

## BREAKRESUMEACTION_STEP_OUT
 __const axdebug.BREAKRESUMEACTION_STEP_OUT;__ 
Step out of the current procedure

## BREAKRESUMEACTION_STEP_OVER
 __const axdebug.BREAKRESUMEACTION_STEP_OVER;__ 
Step over a procedure

## CLSID_DefaultDebugSessionProvider
 __const axdebug.CLSID_DefaultDebugSessionProvider;__ 
An IID object

## CLSID_MachineDebugManager
 __const axdebug.CLSID_MachineDebugManager;__ 
An IID object

## CLSID_ProcessDebugManager
 __const axdebug.CLSID_ProcessDebugManager;__ 
An IID object

## DBGPROP_ATTRIB_ACCESS_FINAL
 __const axdebug.DBGPROP_ATTRIB_ACCESS_FINAL;__ 


## DBGPROP_ATTRIB_ACCESS_PRIVATE
 __const axdebug.DBGPROP_ATTRIB_ACCESS_PRIVATE;__ 


## DBGPROP_ATTRIB_ACCESS_PROTECTED
 __const axdebug.DBGPROP_ATTRIB_ACCESS_PROTECTED;__ 


## DBGPROP_ATTRIB_ACCESS_PUBLIC
 __const axdebug.DBGPROP_ATTRIB_ACCESS_PUBLIC;__ 


## DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS
 __const axdebug.DBGPROP_ATTRIB_HAS_EXTENDED_ATTRIBS;__ 


## DBGPROP_ATTRIB_NO_ATTRIB
 __const axdebug.DBGPROP_ATTRIB_NO_ATTRIB;__ 


## DBGPROP_ATTRIB_STORAGE_FIELD
 __const axdebug.DBGPROP_ATTRIB_STORAGE_FIELD;__ 


## DBGPROP_ATTRIB_STORAGE_GLOBAL
 __const axdebug.DBGPROP_ATTRIB_STORAGE_GLOBAL;__ 


## DBGPROP_ATTRIB_STORAGE_STATIC
 __const axdebug.DBGPROP_ATTRIB_STORAGE_STATIC;__ 


## DBGPROP_ATTRIB_STORAGE_VIRTUAL
 __const axdebug.DBGPROP_ATTRIB_STORAGE_VIRTUAL;__ 


## DBGPROP_ATTRIB_TYPE_IS_CONSTANT
 __const axdebug.DBGPROP_ATTRIB_TYPE_IS_CONSTANT;__ 


## DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED
 __const axdebug.DBGPROP_ATTRIB_TYPE_IS_SYNCHRONIZED;__ 


## DBGPROP_ATTRIB_TYPE_IS_VOLATILE
 __const axdebug.DBGPROP_ATTRIB_TYPE_IS_VOLATILE;__ 


## DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE
 __const axdebug.DBGPROP_ATTRIB_VALUE_IS_EXPANDABLE;__ 


## DBGPROP_ATTRIB_VALUE_IS_INVALID
 __const axdebug.DBGPROP_ATTRIB_VALUE_IS_INVALID;__ 


## DBGPROP_ATTRIB_VALUE_READONLY
 __const axdebug.DBGPROP_ATTRIB_VALUE_READONLY;__ 


## DBGPROP_INFO_ATTRIBUTES
 __const axdebug.DBGPROP_INFO_ATTRIBUTES;__ 


## DBGPROP_INFO_AUTOEXPAND
 __const axdebug.DBGPROP_INFO_AUTOEXPAND;__ 


## DBGPROP_INFO_DEBUGPROP
 __const axdebug.DBGPROP_INFO_DEBUGPROP;__ 


## DBGPROP_INFO_FULLNAME
 __const axdebug.DBGPROP_INFO_FULLNAME;__ 


## DBGPROP_INFO_NAME
 __const axdebug.DBGPROP_INFO_NAME;__ 


## DBGPROP_INFO_TYPE
 __const axdebug.DBGPROP_INFO_TYPE;__ 


## DBGPROP_INFO_VALUE
 __const axdebug.DBGPROP_INFO_VALUE;__ 


## DEBUG_TEXT_ALLOWBREAKPOINTS
 __const axdebug.DEBUG_TEXT_ALLOWBREAKPOINTS;__ 
Allow breakpoints during the evaluation of the text. If this flag is not set then breakpoints will be ignored during the evaluation of the text.

## DEBUG_TEXT_ISEXPRESSION
 __const axdebug.DEBUG_TEXT_ISEXPRESSION;__ 
Indicates that the text is an expression as opposed to a statement. This flag may affect the way in which the text is parsed by some languages.

## DOCUMENTNAMETYPE_APPNODE
 __const axdebug.DOCUMENTNAMETYPE_APPNODE;__ 
Gets the name as it appears in the app tree

## DOCUMENTNAMETYPE_FILE_TAIL
 __const axdebug.DOCUMENTNAMETYPE_FILE_TAIL;__ 
Gets the filename without a path (for save as...)

## DOCUMENTNAMETYPE_TITLE
 __const axdebug.DOCUMENTNAMETYPE_TITLE;__ 
Gets the name as it appears on the doc viewer title bar

## DOCUMENTNAMETYPE_URL
 __const axdebug.DOCUMENTNAMETYPE_URL;__ 
Gets the URL of the document, if any

## ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller
 __const axdebug.ERRORRESUMEACTION_AbortCallAndReturnErrorToCaller;__ 


## ERRORRESUMEACTION_ReexecuteErrorStatement
 __const axdebug.ERRORRESUMEACTION_ReexecuteErrorStatement;__ 


## ERRORRESUMEACTION_SkipErrorStatement
 __const axdebug.ERRORRESUMEACTION_SkipErrorStatement;__ 


## EX_DBGPROP_INFO_DEBUGEXTPROP
 __const axdebug.EX_DBGPROP_INFO_DEBUGEXTPROP;__ 


## EX_DBGPROP_INFO_ID
 __const axdebug.EX_DBGPROP_INFO_ID;__ 


## EX_DBGPROP_INFO_LOCKBYTES
 __const axdebug.EX_DBGPROP_INFO_LOCKBYTES;__ 


## EX_DBGPROP_INFO_NTYPE
 __const axdebug.EX_DBGPROP_INFO_NTYPE;__ 


## EX_DBGPROP_INFO_NVALUE
 __const axdebug.EX_DBGPROP_INFO_NVALUE;__ 


## SOURCETEXT_ATTR_COMMENT
 __const axdebug.SOURCETEXT_ATTR_COMMENT;__ 


## SOURCETEXT_ATTR_FUNCTION_START
 __const axdebug.SOURCETEXT_ATTR_FUNCTION_START;__ 


## SOURCETEXT_ATTR_KEYWORD
 __const axdebug.SOURCETEXT_ATTR_KEYWORD;__ 


## SOURCETEXT_ATTR_NONSOURCE
 __const axdebug.SOURCETEXT_ATTR_NONSOURCE;__ 


## SOURCETEXT_ATTR_NUMBER
 __const axdebug.SOURCETEXT_ATTR_NUMBER;__ 


## SOURCETEXT_ATTR_OPERATOR
 __const axdebug.SOURCETEXT_ATTR_OPERATOR;__ 


## SOURCETEXT_ATTR_STRING
 __const axdebug.SOURCETEXT_ATTR_STRING;__ 


## TEXT_DOC_ATTR_READONLY
 __const axdebug.TEXT_DOC_ATTR_READONLY;__ 
Indicates that the document is read-only.