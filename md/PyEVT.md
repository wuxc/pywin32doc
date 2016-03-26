# PyEVT

## PyEVT_HANDLE Object

Handle to an event log, session, query, or any other object used with 

the Evt* event log functions on Vista and later. 

When the object is destroyed, EvtClose is called.

## PyEVT_RPC_LOGIN Object

Tuple containing login credentials for a remote Event Log connection

#### Comments
To use current login credentials, pass None for User, Domain, and Password

#### Items


  - [0] *string* : Server

    Machine to connect to (only required item)

  - [1] *string* : User

    User account to login with, defaults to None

  - [2] *string* : Domain

    Domain of account, defaults to None

  - [3] *string* : Password

    Password, defaults to None

  - [4] *int* : Flags

    Type of authentication, EvtRpcLogin*.  Default is EvtRpcLoginAuthDefault