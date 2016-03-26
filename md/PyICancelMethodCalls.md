# PyICancelMethodCalls

## PyICancelMethodCalls Object

Interface to request cancellation of a call. See[pythoncom::CoGetCancelObject](pythoncom.md#pythoncomcogetcancelobject).

#### Methods


  - [Cancel](PyICancelMethodCalls.md#pyicancelmethodcallscancel)

    Cancels a pending call&nbsp;

  - [TestCancel](PyICancelMethodCalls.md#pyicancelmethodcallstestcancel)

    Checks if a request has been made to cancel a call&nbsp;

## [PyICancelMethodCalls](#pyicancelmethodcalls).Cancel

 __Cancel( *Seconds* __ )
Cancels a pending call

#### Parameters


  -  *Seconds* : int

    Wait timeout in seconds

## [PyICancelMethodCalls](#pyicancelmethodcalls).TestCancel

int = __TestCancel(__ )
Checks if a request has been made to cancel a call

#### Return Value
Can return RPC_S_CALLPENDING or RPC_E_CALL_CANCELED