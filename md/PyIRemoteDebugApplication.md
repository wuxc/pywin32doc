# PyIRemoteDebugApplication

## PyIRemoteDebugApplication Object

Description of the interface

#### Methods


  - [ResumeFromBreakPoint](PyIRemoteDebugApplication.md#pyiremotedebugapplicationresumefrombreakpoint)

    Continue an application which is currently in a breakpoint\.&nbsp;

  - [CauseBreak](PyIRemoteDebugApplication.md#pyiremotedebugapplicationcausebreak)

    Causes the application to break into the debugger at the earliest opportunity\.&nbsp;

  - [ConnectDebugger](PyIRemoteDebugApplication.md#pyiremotedebugapplicationconnectdebugger)

    Connects a debugger to the application\.&nbsp;

  - [DisconnectDebugger](PyIRemoteDebugApplication.md#pyiremotedebugapplicationdisconnectdebugger)

    Disconnects the current debugger from the application\.&nbsp;

  - [GetDebugger](PyIRemoteDebugApplication.md#pyiremotedebugapplicationgetdebugger)

    Returns the current debugger connected to the application\.&nbsp;

  - [CreateInstanceAtApplication](PyIRemoteDebugApplication.md#pyiremotedebugapplicationcreateinstanceatapplication)

    Create objects in the application process address space\.&nbsp;

  - [QueryAlive](PyIRemoteDebugApplication.md#pyiremotedebugapplicationqueryalive)

    Indicates if the application is alive\.&nbsp;

  - [EnumThreads](PyIRemoteDebugApplication.md#pyiremotedebugapplicationenumthreads)

    Enumerates all threads known to be associated with the application\.&nbsp;

  - [GetName](PyIRemoteDebugApplication.md#pyiremotedebugapplicationgetname)

    Description of GetName&nbsp;

  - [GetRootNode](PyIRemoteDebugApplication.md#pyiremotedebugapplicationgetrootnode)

    Returns the application node under which all nodes associated with the application are added\.&nbsp;

  - [EnumGlobalExpressionContexts](PyIRemoteDebugApplication.md#pyiremotedebugapplicationenumglobalexpressioncontexts)

    Enumerates all global expression contexts\.&nbsp;

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.CauseBreak

 **CauseBreak\(** \)
Causes the application to break into the debugger at the earliest opportunity\.

#### Comments
Note that a long time may elapse before the application actually breaks, particularly if 

the application is not currently executing script code\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.ConnectDebugger

 **ConnectDebugger\( *pad* ** \)
Connects a debugger to the application\.

#### Parameters


  -  *pad* :[PyIApplicationDebugger](#pyiapplicationdebugger)

    Description for pad

#### Comments
Only one debugger may be connected at a 

time; this method fails if there is already a debugger connected\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.CreateInstanceAtApplication

[PyIUnknown](#pyiunknown)\= **CreateInstanceAtApplication\( *rclsid*  *, pUnkOuter*  *, dwClsContext*  *, riid* ** \)
Create objects in the application process address space\.

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

application, to create objects in the application process\. 

This method simply delegates to CoCreateInstance\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.DisconnectDebugger

 **DisconnectDebugger\(** \)
Disconnects the current debugger from the application\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.EnumGlobalExpressionContexts

 **IEnumDebugExpressionContexts** \= **EnumGlobalExpressionContexts\(** \)
Enumerates all global expression contexts

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.EnumThreads

[PyIEnumRemoteDebugApplicationThreads](#pyienumremotedebugapplicationthreads)\= **EnumThreads\(** \)
Enumerates all threads known to be associated with the application\.

#### Comments
New threads may be added at any time\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.GetDebugger

[PyIApplicationDebugger](#pyiapplicationdebugger)\= **GetDebugger\(** \)
Returns the current debugger connected to the application\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.GetName

 **GetName\(** \)
Description of GetName\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.GetRootNode

[PyIDebugApplicationNode](#pyidebugapplicationnode)\= **GetRootNode\(** \)
Returns the application node under which all nodes associated with the application are added\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.QueryAlive

 **QueryAlive\(** \)
Returns True if alive, else False\.

## [PyIRemoteDebugApplication](#pyiremotedebugapplication)\.ResumeFromBreakPoint

 **ResumeFromBreakPoint\( *prptFocus*  *, bra*  *, era* ** \)
Continue an application which is currently in a breakpoint\.

#### Parameters


  -  *prptFocus* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prptFocus

  -  *bra* : int

    Break resume action

  -  *era* : int

    Error resume action