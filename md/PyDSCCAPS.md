# PyDSCCAPS


## PyDSCCAPS Object

A Python object, representing a DSCCAPS structure

#### Properties

  - integer dwFlags

    Specifies device capabilities\. Can be zero or the following flag:

   

       Flag

   

   

       Description

   

DSCCAPS\_EMULDRIVERIndicates that no DirectSound Device is available and standard wave audio functions are being used\.

  - integer dwFormats

    Bitset of supported WAVE\_FORMAT formats\.

  - integer dwChannels

    Number of channels supported by the device\.