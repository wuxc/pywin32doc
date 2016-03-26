# PyDSCCAPS

## PyDSCCAPS Object

A Python object, representing a DSCCAPS structure

#### Properties

  -  __integer dwFlags__ 
    Specifies device capabilities. Can be zero or the following flag:

 __Flag__  __Description__ DSCCAPS_EMULDRIVERIndicates that no DirectSound Device is available and standard wave audio functions are being used.
  -  __integer dwFormats__ 
    Bitset of supported WAVE_FORMAT formats.

  -  __integer dwChannels__ 
    Number of channels supported by the device.