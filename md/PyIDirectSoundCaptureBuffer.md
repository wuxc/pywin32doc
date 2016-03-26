# PyIDirectSoundCaptureBuffer


## PyIDirectSoundCaptureBuffer Object

The methods of the IDirectSoundCaptureBuffer interface are used to manipulate sound capture buffers\.

#### Methods

  - [Initialize](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebufferinitialize)

    Description of GetCaps\.&nbsp;

  - [SetCooperativeLevel](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffersetcooperativelevel)

    Description of GetFormat\.&nbsp;

  - [GetStatus](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffergetstatus)

    Description of GetStatus\.&nbsp;

  - [Initialize](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebufferinitialize)

    Description of Initialize\.&nbsp;

  - [GetCurrentPosition](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffergetcurrentposition)

    Description of GetCaps\.&nbsp;

  - [Play](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebufferplay)

    Description of Start\.&nbsp;

  - [Stop](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebufferstop)

    Description of Stop\.&nbsp;

  - [Unlock](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebufferunlock)

    Description of Update\.&nbsp;


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.GetCaps

GetCaps\(\)
Returns the capabilities of the DirectSound Capture Buffer\.


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.GetCurrentPosition

GetCurrentPosition\(\)
Returns a tuple of the current capture and read position in the buffer\. The capture position is ahead of the read position\. These positions are not always identical due to possible buffering of captured data either on the physical device or in the host\. The data after the read position up to and including the capture position is not necessarily valid data\.


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.GetFormat

GetFormat\(\)
Retrieves the current format of the sound capture buffer as a WAVEFORMATEX object\.


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.GetStatus

GetStatus\(\)
Retrieves the current status of the sound capture buffer\.


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.Initialize

Initialize\(\)
Not normally used\. Used IDirectSoundCapture\.CreateCaptureBuffer instead\.


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.Start

Start\(dwFlags\)
The PyIDirectSoundCaptureBuffer::Start method puts the capture buffer into the capture state and begins capturing data into the buffer\. If the capture buffer is already in the capture state then the method has no effect\.

#### Parameters

  - dwFlags=0 : int

    Flags that specify the behavior for the capture buffer when capturing sound data\. Possible values for dwFlags can be one of the following: 

DSCBSTART\_LOOPING


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.Stop

Stop\(\)
The IDirectSoundCaptureBuffer::Stop method puts the capture buffer into the "stop" state and stops capturing data\. If the capture buffer is already in the stop state then the method has no effect\.


## [PyIDirectSoundCaptureBuffer](PyIDirectSoundCaptureBuffer.md#pyidirectsoundcapturebuffer)\.Update

Update\(dwReadCursor, dwReadBytes, dwFlags\)
Retrieve data from the capture buffer\.

#### Parameters

  - dwReadCursor : int

    Offset, in bytes, from the start of the buffer to where the update begins\.

  - dwReadBytes : int

    Size, in bytes, of the portion of the buffer to update\.

  - dwFlags=0 : int

    Flags modifying the update event\. This value can be 0 or the following flag: DSCBLOCK\_ENTIREBUFFER 

The dwReadBytes parameter is to be ignored and the entire capture buffer is to be locked\.