# PyDSCBCAPS

## PyDSCBCAPS Object

A Python object, representing a DSCBCAPS structure

#### Properties

  -  __integer dwFlags__ 
    Specifies device capabilities. Can be 0 or DSCBCAPS_EMULDRIVER (indicates that no DirectSound Device is available and standard wave audio functions are being used).

  -  __integer dwBufferBytes__ 
    The size, in bytes, of the capture buffer.