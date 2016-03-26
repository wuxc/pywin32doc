# PyICancelMethodCalls

## PyICancelMethodCalls Object

Interface to request cancellation of a call\. See[pythoncom::CoGetCancelObject](pythoncom.md#pythoncomcogetcancelobject)\.

#### Methods


  - [Cancel](PyICancelMethodCalls.md#pyicancelmethodcallscancel)

    Cancels a pending call&nbsp;

  - [TestCancel](PyICancelMethodCalls.md#pyicancelmethodcallstestcancel)

    Checks if a request has been made to cancel a call&nbsp;

## [PyICancelMethodCalls](#pyicancelmethodcalls)\.Cancel

 **Cancel\( *Seconds* ** \)
Cancels a pending call

#### Parameters


  -  *Seconds* : int

    Wait timeout in seconds

## [PyICancelMethodCalls](#pyicancelmethodcalls)\.TestCancel

int \= **TestCancel\(** \)
Checks if a request has been made to cancel a call

#### Return Value
Can return RPC\_S\_CALLPENDING or RPC\_E\_CALL\_CANCELED