# PyIAsyncOperation

## PyIAsyncOperation Object

Description of the interface

#### Methods


  - [SetAsyncMode](PyIAsyncOperation.md#pyiasyncoperationsetasyncmode)

    Description of SetAsyncMode&nbsp;

  - [GetAsyncMode](PyIAsyncOperation.md#pyiasyncoperationgetasyncmode)

    Description of GetAsyncMode&nbsp;

  - [StartOperation](PyIAsyncOperation.md#pyiasyncoperationstartoperation)

    Description of StartOperation&nbsp;

  - [InOperation](PyIAsyncOperation.md#pyiasyncoperationinoperation)

    Description of InOperation&nbsp;

  - [EndOperation](PyIAsyncOperation.md#pyiasyncoperationendoperation)

    Description of EndOperation&nbsp;

## [PyIAsyncOperation](#pyiasyncoperation).EndOperation

 __EndOperation( *hResult*  *, pbcReserved*  *, dwEffects* __ )
Description of EndOperation.

#### Parameters


  -  *hResult* : int

    Description for hResult

  -  *pbcReserved* :[PyIBindCtx](#pyibindctx)

    Description for pbcReserved

  -  *dwEffects* : int

    Description for dwEffects

## [PyIAsyncOperation](#pyiasyncoperation).GetAsyncMode

bool = __GetAsyncMode(__ )
Description of GetAsyncMode.

## [PyIAsyncOperation](#pyiasyncoperation).InOperation

 __InOperation(__ )
Description of InOperation.

## [PyIAsyncOperation](#pyiasyncoperation).SetAsyncMode

 __SetAsyncMode( *fDoOpAsync* __ )
Description of SetAsyncMode.

#### Parameters


  -  *fDoOpAsync* : int

    Description for fDoOpAsync

## [PyIAsyncOperation](#pyiasyncoperation).StartOperation

 __StartOperation( *pbcReserved* __ )
Description of StartOperation.

#### Parameters


  -  *pbcReserved* :[PyIBindCtx](#pyibindctx)

    Description for pbcReserved