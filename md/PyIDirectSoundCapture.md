# PyIDirectSoundCapture

## PyIDirectSoundCapture Object

The methods of the IDirectSoundCapture interface are used to create sound capture buffers.

#### Methods


  - [Initialize](PyIDirectSoundCapture.md#pyidirectsoundcaptureinitialize)

    Description of Initialize.&nbsp;

  - [CreateSoundBuffer](PyIDirectSoundCapture.md#pyidirectsoundcapturecreatesoundbuffer)

    Description of CreateSoundBuffer.&nbsp;

  - [GetCaps](PyIDirectSoundCapture.md#pyidirectsoundcapturegetcaps)

    Description of GetCaps.&nbsp;

## [PyIDirectSoundCapture](#pyidirectsoundcapture).CreateCaptureBuffer

 __CreateCaptureBuffer( *lpDSCBufferDesc*  *, unk* __ )
The IDirectSoundCapture::CreateSoundBuffer method creates a DirectSoundBuffer object to hold a sequence of audio samples.

#### Parameters


  -  *lpDSCBufferDesc* :[PyDSCBUFFERDESC](#pydscbufferdesc)

    a DSCBUFFERDESC structure containing values for the capture buffer being created.

  -  *unk=None* : __PyIUknown__ 

    The IUnknown for COM aggregation.

## [PyIDirectSoundCapture](#pyidirectsoundcapture).GetCaps

 __GetCaps(__ )
The GetCaps method retrieves the capabilities of the hardware device that is represented by the DirectSound object. See[DSCAPS contants](DSCAPS.md#dscapscontants).

## [PyIDirectSoundCapture](#pyidirectsoundcapture).Initialize

 __Initialize(__ )
Not normally called directly. Use DirectSoundCaptureCreate instead.