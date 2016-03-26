# PyIServiceProvider


## PyIServiceProvider Object

A Python interface to IServiceProvider

#### Methods

  - [QueryService](PyIServiceProvider.md#pyiserviceproviderqueryservice)

    Creates or accesses the specified service and returns an interface object to the specified interface for the service\.&nbsp;




## [PyIServiceProvider](PyIServiceProvider.md#pyiserviceprovider)\.QueryService

[PyIUnknown](PyIUnknown.md) = QueryService\(clsid, iid

\)
Creates or accesses the specified service and returns an interface object to the specified interface for the service\.

#### Parameters

  - clsid : [PyIID](PyIID.md)

    Unique identifier for the requested service\.

  - iid : [PyIID](PyIID.md)

    Unique identifier for the requested interface on the service\.