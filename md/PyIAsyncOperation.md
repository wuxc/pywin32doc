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


## [PyIAsyncOperation](PyIAsyncOperation.md#pyiasyncoperation)\.EndOperation

EndOperation\(hResult, pbcReserved, dwEffects\)
Description of EndOperation\.

#### Parameters

  - hResult : int

    Description for hResult

  - pbcReserved : [PyIBindCtx](PyIBindCtx.md)

    Description for pbcReserved

  - dwEffects : int

    Description for dwEffects


## [PyIAsyncOperation](PyIAsyncOperation.md#pyiasyncoperation)\.GetAsyncMode

bool = GetAsyncMode\(\)
Description of GetAsyncMode\.


## [PyIAsyncOperation](PyIAsyncOperation.md#pyiasyncoperation)\.InOperation

InOperation\(\)
Description of InOperation\.


## [PyIAsyncOperation](PyIAsyncOperation.md#pyiasyncoperation)\.SetAsyncMode

SetAsyncMode\(fDoOpAsync\)
Description of SetAsyncMode\.

#### Parameters

  - fDoOpAsync : int

    Description for fDoOpAsync


## [PyIAsyncOperation](PyIAsyncOperation.md#pyiasyncoperation)\.StartOperation

StartOperation\(pbcReserved\)
Description of StartOperation\.

#### Parameters

  - pbcReserved : [PyIBindCtx](PyIBindCtx.md)

    Description for pbcReserved