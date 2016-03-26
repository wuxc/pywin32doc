# PyIDirectSoundCapture


## PyIDirectSoundCapture Object

The methods of the IDirectSoundCapture interface are used to create sound capture buffers\.

#### Methods

  - [Initialize](PyIDirectSoundCapture.md#pyidirectsoundcaptureinitialize)

    Description of Initialize\.&nbsp;

  - [CreateSoundBuffer](PyIDirectSoundCapture.md#pyidirectsoundcapturecreatesoundbuffer)

    Description of CreateSoundBuffer\.&nbsp;

  - [GetCaps](PyIDirectSoundCapture.md#pyidirectsoundcapturegetcaps)

    Description of GetCaps\.&nbsp;


## [PyIDirectSoundCapture](PyIDirectSoundCapture.md#pyidirectsoundcapture)\.CreateCaptureBuffer

CreateCaptureBuffer\(lpDSCBufferDesc, unk\)
The IDirectSoundCapture::CreateSoundBuffer method creates a DirectSoundBuffer object to hold a sequence of audio samples\.

#### Parameters

  - lpDSCBufferDesc : [PyDSCBUFFERDESC](PyDSCBUFFERDESC.md)

    a DSCBUFFERDESC structure containing values for the capture buffer being created\.

  - unk=None : PyIUknown

    The IUnknown for COM aggregation\.


## [PyIDirectSoundCapture](PyIDirectSoundCapture.md#pyidirectsoundcapture)\.GetCaps

GetCaps\(\)
The GetCaps method retrieves the capabilities of the hardware device that is represented by the DirectSound object\. See [DSCAPS contants](DSCAPS.md#dscapscontants)

\.


## [PyIDirectSoundCapture](PyIDirectSoundCapture.md#pyidirectsoundcapture)\.Initialize

Initialize\(\)
Not normally called directly\. Use DirectSoundCaptureCreate instead\.