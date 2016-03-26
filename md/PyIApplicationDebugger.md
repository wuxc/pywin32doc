# PyIApplicationDebugger

## PyIApplicationDebugger Object

Description of the interface

#### Methods


  - [QueryAlive](PyIApplicationDebugger.md#pyiapplicationdebuggerqueryalive)

    Returns true if alive, else false.&nbsp;

  - [CreateInstanceAtDebugger](PyIApplicationDebugger.md#pyiapplicationdebuggercreateinstanceatdebugger)

    Create objects in the application process address space.&nbsp;

  - [onDebugOutput](PyIApplicationDebugger.md#pyiapplicationdebuggerondebugoutput)

    Called when[PyIDebugApplication::DebugOutput](PyIDebugApplication.md#pyidebugapplicationdebugoutput)is called.&nbsp;

  - [onHandleBreakPoint](PyIApplicationDebugger.md#pyiapplicationdebuggeronhandlebreakpoint)

    Called when a breakpoint is hit.&nbsp;

  - [onClose](PyIApplicationDebugger.md#pyiapplicationdebuggeronclose)

    Called when[PyIDebugApplication::Close](PyIDebugApplication.md#pyidebugapplicationclose)is called.&nbsp;

  - [onDebuggerEvent](PyIApplicationDebugger.md#pyiapplicationdebuggerondebuggerevent)

    Handle a custom event.&nbsp;

## [PyIApplicationDebugger](#pyiapplicationdebugger).CreateInstanceAtDebugger

 __CreateInstanceAtDebugger( *rclsid*  *, pUnkOuter*  *, dwClsContext*  *, riid* __ )
Create objects in the application process address space.

#### Parameters


  -  *rclsid* :[PyIID](#pyiid)

    Description for rclsid

  -  *pUnkOuter* :[PyIUnknown](#pyiunknown)

    Description for pUnkOuter

  -  *dwClsContext* : int

    Description for dwClsContext

  -  *riid* :[PyIID](#pyiid)

    Description for riid

#### Comments
Provides a mechanism for the debugger IDE, running out-of-process to the 

application, to create objects in the application process. 

This method simply delegates to CoCreateInstance.

## [PyIApplicationDebugger](#pyiapplicationdebugger).QueryAlive

 __QueryAlive(__ )
Returns true if alive, else false.

## [PyIApplicationDebugger](#pyiapplicationdebugger).onClose

 __onClose(__ )
Called when[PyIDebugApplication::Close](PyIDebugApplication.md#pyidebugapplicationclose)is called.

## [PyIApplicationDebugger](#pyiapplicationdebugger).onDebugOutput

 __onDebugOutput( *pstr* __ )
Called when[PyIDebugApplication::DebugOutput](PyIDebugApplication.md#pyidebugapplicationdebugoutput)is called.

#### Parameters


  -  *pstr* : __unicode__ 

    Description for pstr

#### Comments
The debugger can use this to display the string in an output window.

## [PyIApplicationDebugger](#pyiapplicationdebugger).onDebuggerEvent

 __onDebuggerEvent( *guid*  *, uUnknown* __ )
Description of onDebuggerEvent.

#### Parameters


  -  *guid* :[PyIID](#pyiid)

    

  -  *uUnknown* :[PyIUnknown](#pyiunknown)

    

#### Comments
The semantics of guid and unknown are entirely application/debugger defined
This method may return E_NOTIMPL.

## [PyIApplicationDebugger](#pyiapplicationdebugger).onHandleBreakPoint

 __onHandleBreakPoint( *prpt*  *, br*  *, pError* __ )
Called when a breakpoint is hit.

#### Parameters


  -  *prpt* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prpt

  -  *br* : int

    Description for br

  -  *pError* : __IActiveScriptErrorDebug__ 

    Description for pError

#### Comments
The application will remain 

suspended until the debugger IDE calls __PyIDebugApplication::ResumeFromBreakPoint__ .