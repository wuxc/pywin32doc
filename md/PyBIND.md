# PyBIND

## PyBIND_OPTS Object

Dictionary representation of a BIND_OPTS struct 

May eventually be extended to include BIND_OPTS2 members

#### Properties

  -  __int Flags__ 
    Value from BIND_FLAGS enum: BIND_MAYBOTHERUSER, BIND_JUSTTESTEXISTENCE or 0

  -  __int Mode__ 
    Combination of storagecon.STGM_* values

  -  __int TickCountDeadline__ 
    Operation timeout in milliseconds

  -  __int cbStruct__ 
    Size of struct, ignored on input