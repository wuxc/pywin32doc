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

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnBreakFlagChange

 __OnBreakFlagChange( *abf*  *, prdatSteppingThread* __ )
Description of OnBreakFlagChange.

#### Parameters


  -  *abf* : int

    Description for abf

  -  *prdatSteppingThread* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prdatSteppingThread

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnClose

 __OnClose(__ )
Description of OnClose.

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnConnectDebugger

 __OnConnectDebugger( *pad* __ )
Description of OnConnectDebugger.

#### Parameters


  -  *pad* :[PyIApplicationDebugger](#pyiapplicationdebugger)

    Description for pad

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnCreateThread

 __OnCreateThread( *prdat* __ )
Description of OnCreateThread.

#### Parameters


  -  *prdat* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prdat

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnDebugOutput

 __OnDebugOutput( *pstr* __ )
Description of OnDebugOutput.

#### Parameters


  -  *pstr* : __unicode__ 

    Description for pstr

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnDestroyThread

 __OnDestroyThread( *prdat* __ )
Description of OnDestroyThread.

#### Parameters


  -  *prdat* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prdat

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnDisconnectDebugger

 __OnDisconnectDebugger(__ )
Description of OnDisconnectDebugger.

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnEnterBreakPoint

 __OnEnterBreakPoint( *prdat* __ )
Description of OnEnterBreakPoint.

#### Parameters


  -  *prdat* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prdat

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnLeaveBreakPoint

 __OnLeaveBreakPoint( *prdat* __ )
Description of OnLeaveBreakPoint.

#### Parameters


  -  *prdat* :[PyIRemoteDebugApplicationThread](#pyiremotedebugapplicationthread)

    Description for prdat

## [PyIRemoteDebugApplicationEvents](#pyiremotedebugapplicationevents).OnSetName

 __OnSetName( *pstrName* __ )
Description of OnSetName.

#### Parameters


  -  *pstrName* : __unicode__ 

    Description for pstrName