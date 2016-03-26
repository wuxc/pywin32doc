# PyBIND

## PyBIND\_OPTS Object



Dictionary representation of a BIND\_OPTS struct 

May eventually be extended to include BIND\_OPTS2 members

#### Properties

  - int Flags
    Value from BIND\_FLAGS enum: BIND\_MAYBOTHERUSER, BIND\_JUSTTESTEXISTENCE or 0

  - int Mode
    Combination of storagecon\.STGM\_\* values

  - int TickCountDeadline
    Operation timeout in milliseconds

  - int cbStruct
    Size of struct, ignored on input