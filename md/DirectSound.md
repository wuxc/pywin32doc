# directsound


## Module directsound

A module encapsulating the DirectSound interfaces\. See [DirectSound examples](DirectSound.md#directsoundexamples)

 for a quick overview\.

#### Methods

  - [DirectSoundCreate](directsound.md#directsounddirectsoundcreate)

    Creates and initializes a new object that supports the IDirectSound interface\.&nbsp;

  - [DirectSoundEnumerate](directsound.md#directsounddirectsoundenumerate)

    The DirectSoundEnumerate function enumerates the DirectSound drivers installed in the system\.&nbsp;

  - [DirectSoundCaptureCreate](directsound.md#directsounddirectsoundcapturecreate)

    The DirectSoundCaptureCreate function creates and initializes an object that supports the IDirectSoundCapture interface\.&nbsp;

  - [DirectSoundCaptureEnumerate](directsound.md#directsounddirectsoundcaptureenumerate)

    The DirectSoundCaptureEnumerate function enumerates the DirectSoundCapture objects installed in the system\.&nbsp;

  - [DSCAPS](directsound.md#directsounddscaps)

    Creates a new [PyDSCAPS](PyDSCAPS.md) object\.&nbsp;

  - [DSBCAPS](directsound.md#directsounddsbcaps)

    Creates a new [PyDSBCAPS](PyDSBCAPS.md) object\.&nbsp;

  - [DSCCAPS](directsound.md#directsounddsccaps)

    Creates a new [PyDSCCAPS](PyDSCCAPS.md) object\.&nbsp;

  - [DSCBCAPS](directsound.md#directsounddscbcaps)

    Creates a new [PyDSCBCAPS](PyDSCBCAPS.md) object\.&nbsp;

  - [DSBUFFERDESC](directsound.md#directsounddsbufferdesc)

    Creates a new [PyDSBUFFERDESC](PyDSBUFFERDESC.md) object\.&nbsp;

  - [DSCBUFFERDESC](directsound.md#directsounddscbufferdesc)

    Creates a new [PyDSCBUFFERDESC](PyDSCBUFFERDESC.md) object\.&nbsp;


## DS3DMODE\_DISABLE

const directsound\.DS3DMODE\_DISABLE;

Processing of 3D sound is disabled\. The sound seems to originate from the center of the listener's head\.


## DS3DMODE\_HEADRELATIVE

const directsound\.DS3DMODE\_HEADRELATIVE;

Sound parameters \(position, velocity, and orientation\) are relative to the listener's parameters\. In this mode, the absolute parameters of the sound are updated automatically as the listener's parameters change, so that the relative parameters remain constant\.


## DS3DMODE\_NORMAL

const directsound\.DS3DMODE\_NORMAL;

Normal processing\. This is the default mode\.


## [directsound](directsound.md#directsound)\.DSBCAPS

[PyDSBCAPS](PyDSBCAPS.md) = DSBCAPS\(\)
Creates a new PyDSBCAPS object


## DSBCAPS\_CTRL3D

const directsound\.DSBCAPS\_CTRL3D;

The buffer is either a primary buffer or a secondary buffer that uses 3-D control\. To create a primary buffer, the dwFlags member of the DSBUFFERDESC structure should include the DSBCAPS\_PRIMARYBUFFER flag\.


## DSBCAPS\_CTRLFREQUENCY

const directsound\.DSBCAPS\_CTRLFREQUENCY;

The buffer must have frequency control capability\.


## DSBCAPS\_CTRLPAN

const directsound\.DSBCAPS\_CTRLPAN;

The buffer must have pan control capability\.


## DSBCAPS\_CTRLPOSITIONNOTIFY

const directsound\.DSBCAPS\_CTRLPOSITIONNOTIFY;

The buffer must have control position notify capability\.


## DSBCAPS\_CTRLVOLUME

const directsound\.DSBCAPS\_CTRLVOLUME;

The buffer must have volume control capability\.


## DSBCAPS\_GETCURRENTPOSITION2

const directsound\.DSBCAPS\_GETCURRENTPOSITION2;

Indicates that IDirectSoundBuffer::GetCurrentPosition should use the new behavior of the play cursor\. In DirectSound in DirectX 1, the play cursor was significantly ahead of the actual playing sound on emulated sound cards; it was directly behind the write cursor\. Now, if the DSBCAPS\_GETCURRENTPOSITION2 flag is specified, the application can get a more accurate play position\. If this flag is not specified, the old behavior is preserved for compatibility\. Note that this flag affects only emulated sound cards; if a DirectSound driver is present, the play cursor is accurate for DirectSound in all versions of DirectX\.


## DSBCAPS\_GLOBALFOCUS

const directsound\.DSBCAPS\_GLOBALFOCUS;

The buffer is a global sound buffer\. With this flag set, an application using DirectSound can continue to play its buffers if the user switches focus to another application, even if the new application uses DirectSound\. The one exception is if you switch focus to a DirectSound application that uses the DSSCL\_EXCLUSIVE or DSSCL\_WRITEPRIMARY flag for its cooperative level\. In this case, the global sounds from other applications will not be audible\.


## DSBCAPS\_LOCHARDWARE

const directsound\.DSBCAPS\_LOCHARDWARE;

The buffer is in hardware memory and uses hardware mixing\.


## DSBCAPS\_LOCSOFTWARE

const directsound\.DSBCAPS\_LOCSOFTWARE;

The buffer is in software memory and uses software mixing\.


## DSBCAPS\_MUTE3DATMAXDISTANCE

const directsound\.DSBCAPS\_MUTE3DATMAXDISTANCE;

The sound is reduced to silence at the maximum distance\. The buffer will stop playing when the maximum distance is exceeded, so that processor time is not wasted\.


## DSBCAPS\_PRIMARYBUFFER

const directsound\.DSBCAPS\_PRIMARYBUFFER;

Indicates that the buffer is a primary sound buffer\. If this value is not specified, a secondary sound buffer will be created\.


## DSBCAPS\_STATIC

const directsound\.DSBCAPS\_STATIC;

Indicates that the buffer will be used for static sound data\. Typically, these buffers are loaded once and played many times\. These buffers are candidates for hardware memory\.


## DSBCAPS\_STICKYFOCUS

const directsound\.DSBCAPS\_STICKYFOCUS;

Changes the focus behavior of the sound buffer\. This flag can be specified in an IDirectSound::CreateSoundBuffer call\. With this flag set, an application using DirectSound can continue to play its sticky focus buffers if the user switches to another application not using DirectSound\. In this situation, the application's normal buffers are muted, but the sticky focus buffers are still audible\. This is useful for nongame applications, such as movie playback \(DirectShow&\#153\), when the user wants to hear the soundtrack while typing in Microsoft Word or Microsoft&\#174 Excel, for example\. However, if the user switches to another DirectSound application, all sound buffers, both normal and sticky focus, in the previous application are muted\.


## DSBLOCK\_ENTIREBUFFER

const directsound\.DSBLOCK\_ENTIREBUFFER;

Unknown\.


## DSBLOCK\_FROMWRITECURSOR

const directsound\.DSBLOCK\_FROMWRITECURSOR;

Locks from the current write cursor, making a call to DirectSoundBuffer\.getCurrentPosition unnecessary\. If this flag is specified, the start parameter is ignored\. This flag is optional\.


## DSBPLAY\_LOOPING

const directsound\.DSBPLAY\_LOOPING;

Once the end of the audio buffer is reached, play restarts at the beginning of the buffer\. Play continues until explicitly stopped\. This flag must be set when playing primary sound buffers\.


## DSBSTATUS\_BUFFERLOST

const directsound\.DSBSTATUS\_BUFFERLOST;

The buffer is lost and must be restored before it can be played or locked\.


## DSBSTATUS\_LOOPING

const directsound\.DSBSTATUS\_LOOPING;

The buffer is being looped\. If this value is not set, the buffer will stop when it reaches the end of the sound data\. Note that if this value is set, the buffer must also be playing\.


## DSBSTATUS\_PLAYING

const directsound\.DSBSTATUS\_PLAYING;

The buffer is playing\. If this value is not set, the buffer is stopped\.


## [directsound](directsound.md#directsound)\.DSBUFFERDESC

[PyDSBUFFERDESC](PyDSBUFFERDESC.md) = DSBUFFERDESC\(\)
Creates a new PyDSBUFFERDESC object


## [directsound](directsound.md#directsound)\.DSCAPS

[PyDSCAPS](PyDSCAPS.md) = DSCAPS\(\)
Creates a new PyDSCAPS object\.


## DSCAPS\_CERTIFIED

const directsound\.DSCAPS\_CERTIFIED;

This driver has been tested and certified by Microsoft\.


## DSCAPS\_CONTINUOUSRATE

const directsound\.DSCAPS\_CONTINUOUSRATE;

The device supports all sample rates between the dwMinSecondarySampleRate and dwMaxSecondarySampleRate member values\. Typically, this means that the actual output rate will be within \+/- 10 hertz \(Hz\) of the requested frequency\.


## DSCAPS\_EMULDRIVER

const directsound\.DSCAPS\_EMULDRIVER;

The device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions\. Performance degradation should be expected\.


## DSCAPS\_PRIMARY16BIT

const directsound\.DSCAPS\_PRIMARY16BIT;

The device supports primary sound buffers with 16-bit samples\.


## DSCAPS\_PRIMARY8BIT

const directsound\.DSCAPS\_PRIMARY8BIT;

The device supports hardware-mixed secondary buffers with 8-bit samples\.


## DSCAPS\_PRIMARYMONO

const directsound\.DSCAPS\_PRIMARYMONO;

The device supports monophonic primary buffers\.


## DSCAPS\_PRIMARYSTEREO

const directsound\.DSCAPS\_PRIMARYSTEREO;

The device supports stereo primary buffers\.


## DSCAPS\_SECONDARY16BIT

const directsound\.DSCAPS\_SECONDARY16BIT;

The device supports hardware-mixed secondary sound buffers with 16-bit samples\.


## DSCAPS\_SECONDARY8BIT

const directsound\.DSCAPS\_SECONDARY8BIT;

The device supports hardware-mixed secondary buffers with 8-bit samples\.


## DSCAPS\_SECONDARYMONO

const directsound\.DSCAPS\_SECONDARYMONO;

The device supports hardware-mixed monophonic secondary buffers\.


## DSCAPS\_SECONDARYSTEREO

const directsound\.DSCAPS\_SECONDARYSTEREO;

The device supports hardware-mixed stereo secondary buffers\.


## [directsound](directsound.md#directsound)\.DSCBCAPS

[PyDSCBCAPS](PyDSCBCAPS.md) = DSCBCAPS\(\)
Creates a new PyDSCBCAPS object


## DSCBCAPS\_WAVEMAPPED

const directsound\.DSCBCAPS\_WAVEMAPPED;

The Win32 wave mapper will be used for formats not supported by the device\.


## [directsound](directsound.md#directsound)\.DSCBUFFERDESC

[PyDSCBUFFERDESC](PyDSCBUFFERDESC.md) = DSCBUFFERDESC\(\)
Creates a new PyDSCBUFFERDESC object


## [directsound](directsound.md#directsound)\.DSCCAPS

[PyDSCCAPS](PyDSCCAPS.md) = DSCCAPS\(\)
Creates a new PyDSCCAPS object


## DSCCAPS\_EMULDRIVER

const directsound\.DSCCAPS\_EMULDRIVER;

The device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions\. Performance degradation should be expected\.


## DSSCL\_EXCLUSIVE

const directsound\.DSSCL\_EXCLUSIVE;

Sets the application to the exclusive level\. When it has the input focus, the application will be the only one audible \(sounds from applications with the DSBCAPS\_GLOBALFOCUS flag set will be muted\)\. With this level, it also has all the privileges of the DSSCL\_PRIORITY level\. DirectSound will restore the hardware format, as specified by the most recent call to the DirectSoundBuffer\.setFormat method, once the application gains the input focus\. \(Note that DirectSound will always restore the wave format, no matter what priority level is set\.\)


## DSSCL\_NORMAL

const directsound\.DSSCL\_NORMAL;

Sets the application to a fully cooperative status\. Most applications should use this level, because it has the smoothest multitasking and resource-sharing behavior\.


## DSSCL\_PRIORITY

const directsound\.DSSCL\_PRIORITY;

Sets the application to the priority level\. Applications with this cooperative level can call the DirectSoundBuffer\.setFormat and DirectSound\.compact methods\.


## DSSCL\_WRITEPRIMARY

const directsound\.DSSCL\_WRITEPRIMARY;

This is the highest priority level\. The application has write access to the primary sound buffers\. No secondary sound buffers in any application can be played\.


## DSSPEAKER\_GEOMETRY\_MAX

const directsound\.DSSPEAKER\_GEOMETRY\_MAX;

The speakers are directed over an arc of 180 degrees\.


## DSSPEAKER\_GEOMETRY\_MIN

const directsound\.DSSPEAKER\_GEOMETRY\_MIN;

The speakers are directed over an arc of 5 degrees\.


## DSSPEAKER\_GEOMETRY\_NARROW

const directsound\.DSSPEAKER\_GEOMETRY\_NARROW;

The speakers are directed over an arc of 10 degrees\.


## DSSPEAKER\_GEOMETRY\_WIDE

const directsound\.DSSPEAKER\_GEOMETRY\_WIDE;

The speakers are directed over an arc of 20 degrees\.


## DSSPEAKER\_HEADPHONE

const directsound\.DSSPEAKER\_HEADPHONE;

The speakers are headphones\.


## DSSPEAKER\_MONO

const directsound\.DSSPEAKER\_MONO;

The speakers are monaural\.


## DSSPEAKER\_QUAD

const directsound\.DSSPEAKER\_QUAD;

The speakers are quadraphonic\.


## DSSPEAKER\_STEREO

const directsound\.DSSPEAKER\_STEREO;

The speakers are stereo \(default value\)\.


## DSSPEAKER\_SURROUND

const directsound\.DSSPEAKER\_SURROUND;

The speakers are surround sound\.


## [directsound](directsound.md#directsound)\.DirectSoundCaptureCreate

[PyIUnknown](PyIUnknown.md) = DirectSoundCaptureCreate\(guid, unk

\)
Creates and initializes a new object that supports the IDirectSoundCapture interface\.

#### Parameters

  - guid=None : [PyIID](PyIID.md)

    Address of the GUID that identifies the sound device\. The value of this parameter must be one of the GUIDs returned by DirectSoundCaptureEnumerate, or None for the default device\.

  - unk=None : PyIUknown

    The IUnknown for COM aggregation\.


## [directsound](directsound.md#directsound)\.DirectSoundCaptureEnumerate

list

 = DirectSoundCaptureEnumerate\(\)
Enumerates DirectSoundCapture drivers installed in the system\.


## [directsound](directsound.md#directsound)\.DirectSoundCreate

[PyIUnknown](PyIUnknown.md) = DirectSoundCreate\(guid, unk

\)
Creates and initializes a new object that supports the IDirectSound interface\.

#### Parameters

  - guid=None : [PyIID](PyIID.md)

    Address of the GUID that identifies the sound device\. The value of this parameter must be one of the GUIDs returned by DirectSoundEnumerate, or None for the default device\.

  - unk=None : PyIUknown

    The IUnknown for COM aggregation\.


## [directsound](directsound.md#directsound)\.DirectSoundEnumerate

list

 = DirectSoundEnumerate\(\)
Enumerates DirectSound drivers installed in the system\.