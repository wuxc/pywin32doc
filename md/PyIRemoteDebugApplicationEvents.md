# PyIRemoteDebugApplicationEvents


## PyIRemoteDebugApplicationEvents Object

Description of the interface

#### Methods

  - [OnConnectDebugger](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsonconnectdebugger)

    Description of OnConnectDebugger&nbsp;

  - [OnDisconnectDebugger](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsondisconnectdebugger)

    Description of OnDisconnectDebugger&nbsp;

  - [OnSetName](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsonsetname)

    Description of OnSetName&nbsp;

  - [OnDebugOutput](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsondebugoutput)

    Description of OnDebugOutput&nbsp;

  - [OnClose](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsonclose)

    Description of OnClose&nbsp;

  - [OnEnterBreakPoint](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsonenterbreakpoint)

    Description of OnEnterBreakPoint&nbsp;

  - [OnLeaveBreakPoint](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsonleavebreakpoint)

    Description of OnLeaveBreakPoint&nbsp;

  - [OnCreateThread](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsoncreatethread)

    Description of OnCreateThread&nbsp;

  - [OnDestroyThread](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsondestroythread)

    Description of OnDestroyThread&nbsp;

  - [OnBreakFlagChange](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationeventsonbreakflagchange)

    Description of OnBreakFlagChange&nbsp;


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnBreakFlagChange

OnBreakFlagChange\(abf, prdatSteppingThread\)
Description of OnBreakFlagChange\.

#### Parameters

  - abf : int

    Description for abf

  - prdatSteppingThread : [PyIRemoteDebugApplicationThread](PyIRemoteDebugApplicationThread.md)

    Description for prdatSteppingThread


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnClose

OnClose\(\)
Description of OnClose\.


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnConnectDebugger

OnConnectDebugger\(pad\)
Description of OnConnectDebugger\.

#### Parameters

  - pad : [PyIApplicationDebugger](PyIApplicationDebugger.md)

    Description for pad


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnCreateThread

OnCreateThread\(prdat\)
Description of OnCreateThread\.

#### Parameters

  - prdat : [PyIRemoteDebugApplicationThread](PyIRemoteDebugApplicationThread.md)

    Description for prdat


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnDebugOutput

OnDebugOutput\(pstr\)
Description of OnDebugOutput\.

#### Parameters

  - pstr : unicode

    Description for pstr


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnDestroyThread

OnDestroyThread\(prdat\)
Description of OnDestroyThread\.

#### Parameters

  - prdat : [PyIRemoteDebugApplicationThread](PyIRemoteDebugApplicationThread.md)

    Description for prdat


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnDisconnectDebugger

OnDisconnectDebugger\(\)
Description of OnDisconnectDebugger\.


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnEnterBreakPoint

OnEnterBreakPoint\(prdat\)
Description of OnEnterBreakPoint\.

#### Parameters

  - prdat : [PyIRemoteDebugApplicationThread](PyIRemoteDebugApplicationThread.md)

    Description for prdat


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnLeaveBreakPoint

OnLeaveBreakPoint\(prdat\)
Description of OnLeaveBreakPoint\.

#### Parameters

  - prdat : [PyIRemoteDebugApplicationThread](PyIRemoteDebugApplicationThread.md)

    Description for prdat


## [PyIRemoteDebugApplicationEvents](PyIRemoteDebugApplicationEvents.md#pyiremotedebugapplicationevents)\.OnSetName

OnSetName\(pstrName\)
Description of OnSetName\.

#### Parameters

  - pstrName : unicode

    Description for pstrName