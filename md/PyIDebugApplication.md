# PyIDebugApplication

## PyIDebugApplication Object



This interface is an extension of[PyIRemoteDebugApplication](#pyiremotedebugapplication), exposing 

non-remotable methods for use by language engines and hosts\.

#### Methods


  - [SetName](PyIDebugApplication.md#pyidebugapplicationsetname)

    Sets the name of the application\.&nbsp;

  - [StepOutComplete](PyIDebugApplication.md#pyidebugapplicationstepoutcomplete)

    Called by language engines, in single step mode, just before they return to their caller\.&nbsp;

  - [DebugOutput](PyIDebugApplication.md#pyidebugapplicationdebugoutput)

    Causes the given string to be displayed by the debugger IDE\.&nbsp;

  - [StartDebugSession](PyIDebugApplication.md#pyidebugapplicationstartdebugsession)

    Causes a default debugger IDE to be started\.&nbsp;

  - [HandleBreakPoint](PyIDebugApplication.md#pyidebugapplicationhandlebreakpoint)

    Called by the language engine in the context of a thread that has hit a breakpoint\.&nbsp;

  - [Close](PyIDebugApplication.md#pyidebugapplicationclose)

    Causes this application to release all references and enter a zombie state\.&nbsp;

  - [GetBreakFlags](PyIDebugApplication.md#pyidebugapplicationgetbreakflags)

    Returns the current break flags for the application\.&nbsp;

  - [GetCurrentThread](PyIDebugApplication.md#pyidebugapplicationgetcurrentthread)

    Returns the application thread object associated with the currently running thread\.&nbsp;

  - [CreateAsyncDebugOperation](PyIDebugApplication.md#pyidebugapplicationcreateasyncdebugoperation)

    Creates an IDebugAsyncOperation object to wrap a provided[PyIDebugSyncOperation](#pyidebugsyncoperation) object\.&nbsp;

  - [AddStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationaddstackframesniffer)

    Adds a stack frame sniffer to this application\.&nbsp;

  - [RemoveStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationremovestackframesniffer)

    Removes a stack frame sniffer from this application\.&nbsp;

  - [QueryCurrentThreadIsDebuggerThread](PyIDebugApplication.md#pyidebugapplicationquerycurrentthreadisdebuggerthread)

    Determines if the current running thread is the debugger thread\.&nbsp;

  - [SynchronousCallInDebuggerThread](PyIDebugApplication.md#pyidebugapplicationsynchronouscallindebuggerthread)

    Provides a mechanism for the caller to run code in the debugger thread\.&nbsp;

  - [CreateApplicationNode](PyIDebugApplication.md#pyidebugapplicationcreateapplicationnode)

    Creates a new application node which is associated with a specific document provider\.&nbsp;

  - [FireDebuggerEvent](PyIDebugApplication.md#pyidebugapplicationfiredebuggerevent)

    Fire a generic event to the IApplicationDebugger \(if any\)&nbsp;

  - [HandleRuntimeError](PyIDebugApplication.md#pyidebugapplicationhandleruntimeerror)

    Description of HandleRuntimeError&nbsp;

  - [FCanJitDebug](PyIDebugApplication.md#pyidebugapplicationfcanjitdebug)

    Description of FCanJitDebug&nbsp;

  - [FIsAutoJitDebugEnabled](PyIDebugApplication.md#pyidebugapplicationfisautojitdebugenabled)

    Description of FIsAutoJitDebugEnabled&nbsp;

  - [AddGlobalExpressionContextProvider](PyIDebugApplication.md#pyidebugapplicationaddglobalexpressioncontextprovider)

    Description of AddGlobalExpressionContextProvider&nbsp;

  - [RemoveGlobalExpressionContextProvider](PyIDebugApplication.md#pyidebugapplicationremoveglobalexpressioncontextprovider)

    Description of RemoveGlobalExpressionContextProvider&nbsp;

## [PyIDebugApplication](#pyidebugapplication)\.AddGlobalExpressionContextProvider

AddGlobalExpressionContextProvider\(pdsfs\)
Description of AddGlobalExpressionContextProvider\.

#### Parameters


  - pdsfs :[PyIProvideExpressionContexts](#pyiprovideexpressioncontexts)

    Description for pdsfs

## [PyIDebugApplication](#pyidebugapplication)\.AddStackFrameSniffer



int =AddStackFrameSniffer\(pdsfs\)
Adds a stack frame sniffer to this application\.

#### Parameters


  - pdsfs :[PyIDebugStackFrameSniffer](#pyidebugstackframesniffer)

    Description for pdsfs

#### Comments


Generally called by a language engine 

to expose its stack frames to the debugger\. It is possible for other entities to 

expose stack frames\.

#### Return Value
The result is an integer cookie, to be passed to[PyIDebugApplication::RemoveStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationremovestackframesniffer)

## [PyIDebugApplication](#pyidebugapplication)\.Close

Close\(\)
Causes this application to release all references and enter a zombie state\.

#### Comments


Called by the owner of the application generally on shut down\.

## [PyIDebugApplication](#pyidebugapplication)\.CreateApplicationNode

[PyIDebugApplicationNode](#pyidebugapplicationnode) =CreateApplicationNode\(\)
Creates a new application node which is associated with a specific document provider\.

#### Comments


Before it is visible, the new node must be 

attached to a parent node\.

## [PyIDebugApplication](#pyidebugapplication)\.CreateAsyncDebugOperation

CreateAsyncDebugOperation\(psdo\)
Creates an IDebugAsyncOperation object to wrap a provided[PyIDebugSyncOperation](#pyidebugsyncoperation) object\.

#### Parameters


  - psdo :[PyIDebugSyncOperation](#pyidebugsyncoperation)

    Description for psdo

#### Comments


This provides a mechanism for language engines to implement asynchronous expression and 

evaluation, etc\. without having to know the details of synchronization with the 

debugger thread\. See the descriptions for[PyIDebugSyncOperation](#pyidebugsyncoperation) andPyIDebugAsyncOperation

 

for more details\.

## [PyIDebugApplication](#pyidebugapplication)\.DebugOutput

DebugOutput\(pstr\)
Causes the given string to be displayed by the debugger IDE, normally in an output window\.

#### Parameters


  - pstr :unicode

    Description for pstr

#### Comments


This mechanism provides the means for a language engine to implement language 

specific debugging output support\. Example: Debug\.writeln\("Help"\) in JavaScript\.

## [PyIDebugApplication](#pyidebugapplication)\.FCanJitDebug

FCanJitDebug\(\)
Description of FCanJitDebug\.

## [PyIDebugApplication](#pyidebugapplication)\.FIsAutoJitDebugEnabled

FIsAutoJitDebugEnabled\(\)
Description of FIsAutoJitDebugEnabled\.

## [PyIDebugApplication](#pyidebugapplication)\.FireDebuggerEvent

FireDebuggerEvent\(guid, unknown\)
Fire a generic event to the IApplicationDebugger \(if any\)

#### Parameters


  - guid :PyIIID

    A GUID\.

  - unknown :[PyIUnknown](#pyiunknown)

    An unknown object\.

## [PyIDebugApplication](#pyidebugapplication)\.GetBreakFlags



int =GetBreakFlags\(\)
Returns the current break flags for the application\.

## [PyIDebugApplication](#pyidebugapplication)\.GetCurrentThread

[PyIDebugApplicationThread](#pyidebugapplicationthread) =GetCurrentThread\(\)
Returns the application thread object associated with the currently running thread\.

## [PyIDebugApplication](#pyidebugapplication)\.HandleBreakPoint



int =HandleBreakPoint\(br\)
Called by the language engine in the context of a thread that has hit a breakpoint\.

#### Parameters


  - br : int

    Break reason - one of the BREAKREASON\_\* constants\.

#### Comments


This method causes the current thread to block and a notification of the breakpoint 

to be sent to the debugger IDE\. When the debugger IDE resumes the application this 

method returns with the action to be taken\.


Note: While in the breakpoint the language engine may be called in this thread to do 

various things such as enumerating stack frames or evaluating expressions\.

#### Return Value
The result is the break resume action - one of the BREAKRESUMEACTION contsants\.

## [PyIDebugApplication](#pyidebugapplication)\.HandleRuntimeError

HandleRuntimeError\(pErrorDebug, pScriptSite\)
Description of HandleRuntimeError\.

#### Parameters


  - pErrorDebug :[PyIActiveScriptErrorDebug](#pyiactivescripterrordebug)

    Description for pErrorDebug

  - pScriptSite :[PyIActiveScriptSite](#pyiactivescriptsite)

    Description for pScriptSite

## [PyIDebugApplication](#pyidebugapplication)\.QueryCurrentThreadIsDebuggerThread

QueryCurrentThreadIsDebuggerThread\(\)
Determines if the current running thread is the debugger thread\.

#### Return Value
Returns S\_OK if the current running thread is the debugger thread\. 

Otherwise, returns S\_FALSE\.

## [PyIDebugApplication](#pyidebugapplication)\.RemoveGlobalExpressionContextProvider

RemoveGlobalExpressionContextProvider\(dwCookie\)
Description of RemoveGlobalExpressionContextProvider\.

#### Parameters


  - dwCookie : int

    Description for dwCookie

## [PyIDebugApplication](#pyidebugapplication)\.RemoveStackFrameSniffer

RemoveStackFrameSniffer\(dwCookie\)
Removes a stack frame sniffer from this application\.

#### Parameters


  - dwCookie : int

    A cookie obtained from[PyIDebugApplication::AddStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationaddstackframesniffer)

## [PyIDebugApplication](#pyidebugapplication)\.SetName

SetName\(pstrName\)
Sets the name of the application\.

#### Parameters


  - pstrName :unicode

    The name of the application\.

#### Comments


The provided name will be returned in subsequent calls 

to &gtom PyIRemoteDebugApplication\.GetName&gt\.

## [PyIDebugApplication](#pyidebugapplication)\.StartDebugSession

StartDebugSession\(\)
Causes a default debugger IDE to be started and a debug session to be attached to 

this application if one does not already exist\.

#### Comments


This is used to implement just-in-time debugging\.

## [PyIDebugApplication](#pyidebugapplication)\.StepOutComplete

StepOutComplete\(\)
Called by language engines, in single step mode, just before they return to their caller\.

#### Comments


The process debug manager uses this opportunity to notify all 

other script engines that they should break at the first opportunity\. This is how 

cross language step modes are implemented\.

## [PyIDebugApplication](#pyidebugapplication)\.SynchronousCallInDebuggerThread

SynchronousCallInDebuggerThread\(pptc, dwParam1, dwParam2, dwParam3\)
Provides a mechanism for the caller to run code in the debugger thread\.

#### Parameters


  - pptc :PyIDebugThreadCall

    Description for pptc

  - dwParam1 : int

    Description for dwParam1

  - dwParam2 : int

    Description for dwParam2

  - dwParam3 : int

    Description for dwParam3

#### Comments


This is generally 

used so that language engines and hosts can implement free threaded objects on top 

of their single threaded implementations\.