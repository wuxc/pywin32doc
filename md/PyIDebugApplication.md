# PyIDebugApplication

## PyIDebugApplication Object

This interface is an extension of[PyIRemoteDebugApplication](#pyiremotedebugapplication), exposing 

non-remotable methods for use by language engines and hosts.

#### Methods


  - [SetName](PyIDebugApplication.md#pyidebugapplicationsetname)

    Sets the name of the application.&nbsp;

  - [StepOutComplete](PyIDebugApplication.md#pyidebugapplicationstepoutcomplete)

    Called by language engines, in single step mode, just before they return to their caller.&nbsp;

  - [DebugOutput](PyIDebugApplication.md#pyidebugapplicationdebugoutput)

    Causes the given string to be displayed by the debugger IDE.&nbsp;

  - [StartDebugSession](PyIDebugApplication.md#pyidebugapplicationstartdebugsession)

    Causes a default debugger IDE to be started.&nbsp;

  - [HandleBreakPoint](PyIDebugApplication.md#pyidebugapplicationhandlebreakpoint)

    Called by the language engine in the context of a thread that has hit a breakpoint.&nbsp;

  - [Close](PyIDebugApplication.md#pyidebugapplicationclose)

    Causes this application to release all references and enter a zombie state.&nbsp;

  - [GetBreakFlags](PyIDebugApplication.md#pyidebugapplicationgetbreakflags)

    Returns the current break flags for the application.&nbsp;

  - [GetCurrentThread](PyIDebugApplication.md#pyidebugapplicationgetcurrentthread)

    Returns the application thread object associated with the currently running thread.&nbsp;

  - [CreateAsyncDebugOperation](PyIDebugApplication.md#pyidebugapplicationcreateasyncdebugoperation)

    Creates an IDebugAsyncOperation object to wrap a provided[PyIDebugSyncOperation](#pyidebugsyncoperation)object.&nbsp;

  - [AddStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationaddstackframesniffer)

    Adds a stack frame sniffer to this application.&nbsp;

  - [RemoveStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationremovestackframesniffer)

    Removes a stack frame sniffer from this application.&nbsp;

  - [QueryCurrentThreadIsDebuggerThread](PyIDebugApplication.md#pyidebugapplicationquerycurrentthreadisdebuggerthread)

    Determines if the current running thread is the debugger thread.&nbsp;

  - [SynchronousCallInDebuggerThread](PyIDebugApplication.md#pyidebugapplicationsynchronouscallindebuggerthread)

    Provides a mechanism for the caller to run code in the debugger thread.&nbsp;

  - [CreateApplicationNode](PyIDebugApplication.md#pyidebugapplicationcreateapplicationnode)

    Creates a new application node which is associated with a specific document provider.&nbsp;

  - [FireDebuggerEvent](PyIDebugApplication.md#pyidebugapplicationfiredebuggerevent)

    Fire a generic event to the IApplicationDebugger (if any)&nbsp;

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

## [PyIDebugApplication](#pyidebugapplication).AddGlobalExpressionContextProvider

 __AddGlobalExpressionContextProvider( *pdsfs* __ )
Description of AddGlobalExpressionContextProvider.

#### Parameters


  -  *pdsfs* :[PyIProvideExpressionContexts](#pyiprovideexpressioncontexts)

    Description for pdsfs

## [PyIDebugApplication](#pyidebugapplication).AddStackFrameSniffer

int = __AddStackFrameSniffer( *pdsfs* __ )
Adds a stack frame sniffer to this application.

#### Parameters


  -  *pdsfs* :[PyIDebugStackFrameSniffer](#pyidebugstackframesniffer)

    Description for pdsfs

#### Comments
Generally called by a language engine 

to expose its stack frames to the debugger. It is possible for other entities to 

expose stack frames.

#### Return Value
The result is an integer cookie, to be passed to[PyIDebugApplication::RemoveStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationremovestackframesniffer)

## [PyIDebugApplication](#pyidebugapplication).Close

 __Close(__ )
Causes this application to release all references and enter a zombie state.

#### Comments
Called by the owner of the application generally on shut down.

## [PyIDebugApplication](#pyidebugapplication).CreateApplicationNode

[PyIDebugApplicationNode](#pyidebugapplicationnode)= __CreateApplicationNode(__ )
Creates a new application node which is associated with a specific document provider.

#### Comments
Before it is visible, the new node must be 

attached to a parent node.

## [PyIDebugApplication](#pyidebugapplication).CreateAsyncDebugOperation

 __CreateAsyncDebugOperation( *psdo* __ )
Creates an IDebugAsyncOperation object to wrap a provided[PyIDebugSyncOperation](#pyidebugsyncoperation)object.

#### Parameters


  -  *psdo* :[PyIDebugSyncOperation](#pyidebugsyncoperation)

    Description for psdo

#### Comments
This provides a mechanism for language engines to implement asynchronous expression and 

evaluation, etc. without having to know the details of synchronization with the 

debugger thread. See the descriptions for[PyIDebugSyncOperation](#pyidebugsyncoperation)and __PyIDebugAsyncOperation__ for more details.

## [PyIDebugApplication](#pyidebugapplication).DebugOutput

 __DebugOutput( *pstr* __ )
Causes the given string to be displayed by the debugger IDE, normally in an output window.

#### Parameters


  -  *pstr* : __unicode__ 

    Description for pstr

#### Comments
This mechanism provides the means for a language engine to implement language 

specific debugging output support. Example: Debug.writeln("Help") in JavaScript.

## [PyIDebugApplication](#pyidebugapplication).FCanJitDebug

 __FCanJitDebug(__ )
Description of FCanJitDebug.

## [PyIDebugApplication](#pyidebugapplication).FIsAutoJitDebugEnabled

 __FIsAutoJitDebugEnabled(__ )
Description of FIsAutoJitDebugEnabled.

## [PyIDebugApplication](#pyidebugapplication).FireDebuggerEvent

 __FireDebuggerEvent( *guid*  *, unknown* __ )
Fire a generic event to the IApplicationDebugger (if any)

#### Parameters


  -  *guid* : __PyIIID__ 

    A GUID.

  -  *unknown* :[PyIUnknown](#pyiunknown)

    An unknown object.

## [PyIDebugApplication](#pyidebugapplication).GetBreakFlags

int = __GetBreakFlags(__ )
Returns the current break flags for the application.

## [PyIDebugApplication](#pyidebugapplication).GetCurrentThread

[PyIDebugApplicationThread](#pyidebugapplicationthread)= __GetCurrentThread(__ )
Returns the application thread object associated with the currently running thread.

## [PyIDebugApplication](#pyidebugapplication).HandleBreakPoint

int = __HandleBreakPoint( *br* __ )
Called by the language engine in the context of a thread that has hit a breakpoint.

#### Parameters


  -  *br* : int

    Break reason - one of the BREAKREASON_* constants.

#### Comments
This method causes the current thread to block and a notification of the breakpoint 

to be sent to the debugger IDE. When the debugger IDE resumes the application this 

method returns with the action to be taken.
Note: While in the breakpoint the language engine may be called in this thread to do 

various things such as enumerating stack frames or evaluating expressions.

#### Return Value
The result is the break resume action - one of the BREAKRESUMEACTION contsants.

## [PyIDebugApplication](#pyidebugapplication).HandleRuntimeError

 __HandleRuntimeError( *pErrorDebug*  *, pScriptSite* __ )
Description of HandleRuntimeError.

#### Parameters


  -  *pErrorDebug* :[PyIActiveScriptErrorDebug](#pyiactivescripterrordebug)

    Description for pErrorDebug

  -  *pScriptSite* :[PyIActiveScriptSite](#pyiactivescriptsite)

    Description for pScriptSite

## [PyIDebugApplication](#pyidebugapplication).QueryCurrentThreadIsDebuggerThread

 __QueryCurrentThreadIsDebuggerThread(__ )
Determines if the current running thread is the debugger thread.

#### Return Value
Returns S_OK if the current running thread is the debugger thread. 

Otherwise, returns S_FALSE.

## [PyIDebugApplication](#pyidebugapplication).RemoveGlobalExpressionContextProvider

 __RemoveGlobalExpressionContextProvider( *dwCookie* __ )
Description of RemoveGlobalExpressionContextProvider.

#### Parameters


  -  *dwCookie* : int

    Description for dwCookie

## [PyIDebugApplication](#pyidebugapplication).RemoveStackFrameSniffer

 __RemoveStackFrameSniffer( *dwCookie* __ )
Removes a stack frame sniffer from this application.

#### Parameters


  -  *dwCookie* : int

    A cookie obtained from[PyIDebugApplication::AddStackFrameSniffer](PyIDebugApplication.md#pyidebugapplicationaddstackframesniffer)

## [PyIDebugApplication](#pyidebugapplication).SetName

 __SetName( *pstrName* __ )
Sets the name of the application.

#### Parameters


  -  *pstrName* : __unicode__ 

    The name of the application.

#### Comments
The provided name will be returned in subsequent calls 

to &gtom PyIRemoteDebugApplication.GetName&gt.

## [PyIDebugApplication](#pyidebugapplication).StartDebugSession

 __StartDebugSession(__ )
Causes a default debugger IDE to be started and a debug session to be attached to 

this application if one does not already exist.

#### Comments
This is used to implement just-in-time debugging.

## [PyIDebugApplication](#pyidebugapplication).StepOutComplete

 __StepOutComplete(__ )
Called by language engines, in single step mode, just before they return to their caller.

#### Comments
The process debug manager uses this opportunity to notify all 

other script engines that they should break at the first opportunity. This is how 

cross language step modes are implemented.

## [PyIDebugApplication](#pyidebugapplication).SynchronousCallInDebuggerThread

 __SynchronousCallInDebuggerThread( *pptc*  *, dwParam1*  *, dwParam2*  *, dwParam3* __ )
Provides a mechanism for the caller to run code in the debugger thread.

#### Parameters


  -  *pptc* : __PyIDebugThreadCall__ 

    Description for pptc

  -  *dwParam1* : int

    Description for dwParam1

  -  *dwParam2* : int

    Description for dwParam2

  -  *dwParam3* : int

    Description for dwParam3

#### Comments
This is generally 

used so that language engines and hosts can implement free threaded objects on top 

of their single threaded implementations.