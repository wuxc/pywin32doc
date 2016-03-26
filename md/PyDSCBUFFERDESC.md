# PyDSCBUFFERDESC

## PyDSCBUFFERDESC Object

A Python object, representing a DSCBUFFERDESC structure

#### Properties

  -  **integer dwFlags** 
    Identifies the capabilities to include when creating a new DirectSoundBuffer object\. Can be zero or the following flag:

 **Flag**  **Description** DSCBCAPS\_WAVEMAPPEDThe Win32 wave mapper will be used for formats not supported by the device\.
  -  **integer dwBufferBytes** 
    Size of the new buffer, in bytes\. This value must be 0 when creating primary buffers\. For secondary buffers, the minimum and maximum sizes allowed are specified by DSBSIZE\_MIN and DSBSIZE\_MAX\.

  -  **WAVEFORMATEX lpwfxFormat** 
    Structure specifying the waveform format for the buffer\. This value must be None for primary buffers\. The application can use IDirectSoundBuffer::SetFormat to set the format of the primary buffer\. 

Sentinel