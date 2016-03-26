# PyIApplicationDebugger


## PyIApplicationDebugger Object

Description of the interface

#### Methods

  - [QueryAlive](PyIApplicationDebugger.md#pyiapplicationdebuggerqueryalive)

    Returns true if alive, else false\.&nbsp;

  - [CreateInstanceAtDebugger](PyIApplicationDebugger.md#pyiapplicationdebuggercreateinstanceatdebugger)

    Create objects in the application process address space\.&nbsp;

  - [onDebugOutput](PyIApplicationDebugger.md#pyiapplicationdebuggerondebugoutput)

    Called when [PyIDebugApplication::DebugOutput](PyIDebugApplication.md#pyidebugapplicationdebugoutput) is called\.&nbsp;

  - [onHandleBreakPoint](PyIApplicationDebugger.md#pyiapplicationdebuggeronhandlebreakpoint)

    Called when a breakpoint is hit\.&nbsp;

  - [onClose](PyIApplicationDebugger.md#pyiapplicationdebuggeronclose)

    Called when [PyIDebugApplication::Close](PyIDebugApplication.md#pyidebugapplicationclose) is called\.&nbsp;

  - [onDebuggerEvent](PyIApplicationDebugger.md#pyiapplicationdebuggerondebuggerevent)

    Handle a custom event\.&nbsp;


## [PyIApplicationDebugger](PyIApplicationDebugger.md#pyiapplicationdebugger)\.CreateInstanceAtDebugger

CreateInstanceAtDebugger\(rclsid, pUnkOuter, dwClsContext, riid\)
Create objects in the application process address space\.

#### Parameters

  - rclsid : [PyIID](PyIID.md)

    Description for rclsid

  - pUnkOuter : [PyIUnknown](PyIUnknown.md)

    Description for pUnkOuter

  - dwClsContext : int

    Description for dwClsContext

  - riid : [PyIID](PyIID.md)

    Description for riid

#### Comments

Provides a mechanism for the debugger IDE, running out-of-process to the 

application, to create objects in the application process\. 

This method simply delegates to CoCreateInstance\.


## [PyIApplicationDebugger](PyIApplicationDebugger.md#pyiapplicationdebugger)\.QueryAlive

QueryAlive\(\)
Returns true if alive, else false\.


## [PyIApplicationDebugger](PyIApplicationDebugger.md#pyiapplicationdebugger)\.onClose

onClose\(\)
Called when [PyIDebugApplication::Close](PyIDebugApplication.md#pyidebugapplicationclose) is called\.


## [PyIApplicationDebugger](PyIApplicationDebugger.md#pyiapplicationdebugger)\.onDebugOutput

onDebugOutput\(pstr\)
Called when [PyIDebugApplication::DebugOutput](PyIDebugApplication.md#pyidebugapplicationdebugoutput) is called\.

#### Parameters

  - pstr : unicode

    Description for pstr

#### Comments

The debugger can use this to display the string in an output window\.


## [PyIApplicationDebugger](PyIApplicationDebugger.md#pyiapplicationdebugger)\.onDebuggerEvent

onDebuggerEvent\(guid, uUnknown\)
Description of onDebuggerEvent\.

#### Parameters

  - guid : [PyIID](PyIID.md)

    

  - uUnknown : [PyIUnknown](PyIUnknown.md)

    

#### Comments

The semantics of guid and unknown are entirely application/debugger defined 

This method may return E\_NOTIMPL\.


## [PyIApplicationDebugger](PyIApplicationDebugger.md#pyiapplicationdebugger)\.onHandleBreakPoint

onHandleBreakPoint\(prpt, br, pError\)
Called when a breakpoint is hit\.

#### Parameters

  - prpt : [PyIRemoteDebugApplicationThread](PyIRemoteDebugApplicationThread.md)

    Description for prpt

  - br : int

    Description for br

  - pError : IActiveScriptErrorDebug

    Description for pError

#### Comments

The application will remain 

suspended until the debugger IDE calls PyIDebugApplication::ResumeFromBreakPoint

\.