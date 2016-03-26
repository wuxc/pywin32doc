# axdebug

## Module axdebug

A module, encapsulating the ActiveX Debugging interfaces

## APPBREAKFLAG\_DEBUGGER\_BLOCK
 **const axdebug\.APPBREAKFLAG\_DEBUGGER\_BLOCK;** 
Languages should break immediately with BREAKREASON\_DEBUGGER\_BLOCK

## APPBREAKFLAG\_DEBUGGER\_HALT
 **const axdebug\.APPBREAKFLAG\_DEBUGGER\_HALT;** 
Languages should break immediately with BREAKREASON\_DEBUGGER\_HALT

## APPBREAKFLAG\_STEP
 **const axdebug\.APPBREAKFLAG\_STEP;** 
ADD\_CONSTANT\(APPBREAKFLAG\_APPBREAKFLAG\_NESTED\);

## BREAKPOINT\_DELETED
 **const axdebug\.BREAKPOINT\_DELETED;** 


## BREAKPOINT\_DISABLED
 **const axdebug\.BREAKPOINT\_DISABLED;** 


## BREAKPOINT\_ENABLED
 **const axdebug\.BREAKPOINT\_ENABLED;** 


## BREAKREASON\_BREAKPOINT
 **const axdebug\.BREAKREASON\_BREAKPOINT;** 
Caused by an explicit breakpoint

## BREAKREASON\_DEBUGGER\_BLOCK
 **const axdebug\.BREAKREASON\_DEBUGGER\_BLOCK;** 
Caused by another thread breaking

## BREAKREASON\_DEBUGGER\_HALT
 **const axdebug\.BREAKREASON\_DEBUGGER\_HALT;** 
Caused by debugger IDE requested break

## BREAKREASON\_ERROR
 **const axdebug\.BREAKREASON\_ERROR;** 
Caused by an execution error

## BREAKREASON\_HOST\_INITIATED
 **const axdebug\.BREAKREASON\_HOST\_INITIATED;** 
Caused by host requested break

## BREAKREASON\_LANGUAGE\_INITIATED
 **const axdebug\.BREAKREASON\_LANGUAGE\_INITIATED;** 
Caused by a scripted break

## BREAKREASON\_STEP
 **const axdebug\.BREAKREASON\_STEP;** 
Caused by the stepping mode

## BREAKRESUMEACTION\_ABORT
 **const axdebug\.BREAKRESUMEACTION\_ABORT;** 
Abort the application

## BREAKRESUMEACTION\_CONTINUE
 **const axdebug\.BREAKRESUMEACTION\_CONTINUE;** 
Continue running

## BREAKRESUMEACTION\_STEP\_INTO
 **const axdebug\.BREAKRESUMEACTION\_STEP\_INTO;** 
Step into a procedure

## BREAKRESUMEACTION\_STEP\_OUT
 **const axdebug\.BREAKRESUMEACTION\_STEP\_OUT;** 
Step out of the current procedure

## BREAKRESUMEACTION\_STEP\_OVER
 **const axdebug\.BREAKRESUMEACTION\_STEP\_OVER;** 
Step over a procedure

## CLSID\_DefaultDebugSessionProvider
 **const axdebug\.CLSID\_DefaultDebugSessionProvider;** 
An IID object

## CLSID\_MachineDebugManager
 **const axdebug\.CLSID\_MachineDebugManager;** 
An IID object

## CLSID\_ProcessDebugManager
 **const axdebug\.CLSID\_ProcessDebugManager;** 
An IID object

## DBGPROP\_ATTRIB\_ACCESS\_FINAL
 **const axdebug\.DBGPROP\_ATTRIB\_ACCESS\_FINAL;** 


## DBGPROP\_ATTRIB\_ACCESS\_PRIVATE
 **const axdebug\.DBGPROP\_ATTRIB\_ACCESS\_PRIVATE;** 


## DBGPROP\_ATTRIB\_ACCESS\_PROTECTED
 **const axdebug\.DBGPROP\_ATTRIB\_ACCESS\_PROTECTED;** 


## DBGPROP\_ATTRIB\_ACCESS\_PUBLIC
 **const axdebug\.DBGPROP\_ATTRIB\_ACCESS\_PUBLIC;** 


## DBGPROP\_ATTRIB\_HAS\_EXTENDED\_ATTRIBS
 **const axdebug\.DBGPROP\_ATTRIB\_HAS\_EXTENDED\_ATTRIBS;** 


## DBGPROP\_ATTRIB\_NO\_ATTRIB
 **const axdebug\.DBGPROP\_ATTRIB\_NO\_ATTRIB;** 


## DBGPROP\_ATTRIB\_STORAGE\_FIELD
 **const axdebug\.DBGPROP\_ATTRIB\_STORAGE\_FIELD;** 


## DBGPROP\_ATTRIB\_STORAGE\_GLOBAL
 **const axdebug\.DBGPROP\_ATTRIB\_STORAGE\_GLOBAL;** 


## DBGPROP\_ATTRIB\_STORAGE\_STATIC
 **const axdebug\.DBGPROP\_ATTRIB\_STORAGE\_STATIC;** 


## DBGPROP\_ATTRIB\_STORAGE\_VIRTUAL
 **const axdebug\.DBGPROP\_ATTRIB\_STORAGE\_VIRTUAL;** 


## DBGPROP\_ATTRIB\_TYPE\_IS\_CONSTANT
 **const axdebug\.DBGPROP\_ATTRIB\_TYPE\_IS\_CONSTANT;** 


## DBGPROP\_ATTRIB\_TYPE\_IS\_SYNCHRONIZED
 **const axdebug\.DBGPROP\_ATTRIB\_TYPE\_IS\_SYNCHRONIZED;** 


## DBGPROP\_ATTRIB\_TYPE\_IS\_VOLATILE
 **const axdebug\.DBGPROP\_ATTRIB\_TYPE\_IS\_VOLATILE;** 


## DBGPROP\_ATTRIB\_VALUE\_IS\_EXPANDABLE
 **const axdebug\.DBGPROP\_ATTRIB\_VALUE\_IS\_EXPANDABLE;** 


## DBGPROP\_ATTRIB\_VALUE\_IS\_INVALID
 **const axdebug\.DBGPROP\_ATTRIB\_VALUE\_IS\_INVALID;** 


## DBGPROP\_ATTRIB\_VALUE\_READONLY
 **const axdebug\.DBGPROP\_ATTRIB\_VALUE\_READONLY;** 


## DBGPROP\_INFO\_ATTRIBUTES
 **const axdebug\.DBGPROP\_INFO\_ATTRIBUTES;** 


## DBGPROP\_INFO\_AUTOEXPAND
 **const axdebug\.DBGPROP\_INFO\_AUTOEXPAND;** 


## DBGPROP\_INFO\_DEBUGPROP
 **const axdebug\.DBGPROP\_INFO\_DEBUGPROP;** 


## DBGPROP\_INFO\_FULLNAME
 **const axdebug\.DBGPROP\_INFO\_FULLNAME;** 


## DBGPROP\_INFO\_NAME
 **const axdebug\.DBGPROP\_INFO\_NAME;** 


## DBGPROP\_INFO\_TYPE
 **const axdebug\.DBGPROP\_INFO\_TYPE;** 


## DBGPROP\_INFO\_VALUE
 **const axdebug\.DBGPROP\_INFO\_VALUE;** 


## DEBUG\_TEXT\_ALLOWBREAKPOINTS
 **const axdebug\.DEBUG\_TEXT\_ALLOWBREAKPOINTS;** 
Allow breakpoints during the evaluation of the text\. If this flag is not set then breakpoints will be ignored during the evaluation of the text\.

## DEBUG\_TEXT\_ISEXPRESSION
 **const axdebug\.DEBUG\_TEXT\_ISEXPRESSION;** 
Indicates that the text is an expression as opposed to a statement\. This flag may affect the way in which the text is parsed by some languages\.

## DOCUMENTNAMETYPE\_APPNODE
 **const axdebug\.DOCUMENTNAMETYPE\_APPNODE;** 
Gets the name as it appears in the app tree

## DOCUMENTNAMETYPE\_FILE\_TAIL
 **const axdebug\.DOCUMENTNAMETYPE\_FILE\_TAIL;** 
Gets the filename without a path \(for save as\.\.\.\)

## DOCUMENTNAMETYPE\_TITLE
 **const axdebug\.DOCUMENTNAMETYPE\_TITLE;** 
Gets the name as it appears on the doc viewer title bar

## DOCUMENTNAMETYPE\_URL
 **const axdebug\.DOCUMENTNAMETYPE\_URL;** 
Gets the URL of the document, if any

## ERRORRESUMEACTION\_AbortCallAndReturnErrorToCaller
 **const axdebug\.ERRORRESUMEACTION\_AbortCallAndReturnErrorToCaller;** 


## ERRORRESUMEACTION\_ReexecuteErrorStatement
 **const axdebug\.ERRORRESUMEACTION\_ReexecuteErrorStatement;** 


## ERRORRESUMEACTION\_SkipErrorStatement
 **const axdebug\.ERRORRESUMEACTION\_SkipErrorStatement;** 


## EX\_DBGPROP\_INFO\_DEBUGEXTPROP
 **const axdebug\.EX\_DBGPROP\_INFO\_DEBUGEXTPROP;** 


## EX\_DBGPROP\_INFO\_ID
 **const axdebug\.EX\_DBGPROP\_INFO\_ID;** 


## EX\_DBGPROP\_INFO\_LOCKBYTES
 **const axdebug\.EX\_DBGPROP\_INFO\_LOCKBYTES;** 


## EX\_DBGPROP\_INFO\_NTYPE
 **const axdebug\.EX\_DBGPROP\_INFO\_NTYPE;** 


## EX\_DBGPROP\_INFO\_NVALUE
 **const axdebug\.EX\_DBGPROP\_INFO\_NVALUE;** 


## SOURCETEXT\_ATTR\_COMMENT
 **const axdebug\.SOURCETEXT\_ATTR\_COMMENT;** 


## SOURCETEXT\_ATTR\_FUNCTION\_START
 **const axdebug\.SOURCETEXT\_ATTR\_FUNCTION\_START;** 


## SOURCETEXT\_ATTR\_KEYWORD
 **const axdebug\.SOURCETEXT\_ATTR\_KEYWORD;** 


## SOURCETEXT\_ATTR\_NONSOURCE
 **const axdebug\.SOURCETEXT\_ATTR\_NONSOURCE;** 


## SOURCETEXT\_ATTR\_NUMBER
 **const axdebug\.SOURCETEXT\_ATTR\_NUMBER;** 


## SOURCETEXT\_ATTR\_OPERATOR
 **const axdebug\.SOURCETEXT\_ATTR\_OPERATOR;** 


## SOURCETEXT\_ATTR\_STRING
 **const axdebug\.SOURCETEXT\_ATTR\_STRING;** 


## TEXT\_DOC\_ATTR\_READONLY
 **const axdebug\.TEXT\_DOC\_ATTR\_READONLY;** 
Indicates that the document is read-only\.