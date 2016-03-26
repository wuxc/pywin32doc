# PyDSCBUFFERDESC

## PyDSCBUFFERDESC Object

A Python object, representing a DSCBUFFERDESC structure

#### Properties

  -  __integer dwFlags__ 
    Identifies the capabilities to include when creating a new DirectSoundBuffer object. Can be zero or the following flag:

 __Flag__  __Description__ DSCBCAPS_WAVEMAPPEDThe Win32 wave mapper will be used for formats not supported by the device.
  -  __integer dwBufferBytes__ 
    Size of the new buffer, in bytes. This value must be 0 when creating primary buffers. For secondary buffers, the minimum and maximum sizes allowed are specified by DSBSIZE_MIN and DSBSIZE_MAX.

  -  __WAVEFORMATEX lpwfxFormat__ 
    Structure specifying the waveform format for the buffer. This value must be None for primary buffers. The application can use IDirectSoundBuffer::SetFormat to set the format of the primary buffer. 

Sentinel