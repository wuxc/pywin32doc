# directsound

## Module directsound

A module encapsulating the DirectSound interfaces. See[DirectSound examples](DirectSound.md#directsoundexamples)for a quick overview.

#### Methods


  - [DirectSoundCreate](directsound.md#directsounddirectsoundcreate)

    Creates and initializes a new object that supports the IDirectSound interface.&nbsp;

  - [DirectSoundEnumerate](directsound.md#directsounddirectsoundenumerate)

    The DirectSoundEnumerate function enumerates the DirectSound drivers installed in the system.&nbsp;

  - [DirectSoundCaptureCreate](directsound.md#directsounddirectsoundcapturecreate)

    The DirectSoundCaptureCreate function creates and initializes an object that supports the IDirectSoundCapture interface.&nbsp;

  - [DirectSoundCaptureEnumerate](directsound.md#directsounddirectsoundcaptureenumerate)

    The DirectSoundCaptureEnumerate function enumerates the DirectSoundCapture objects installed in the system.&nbsp;

  - [DSCAPS](directsound.md#directsounddscaps)

    Creates a new[PyDSCAPS](#pydscaps)object.&nbsp;

  - [DSBCAPS](directsound.md#directsounddsbcaps)

    Creates a new[PyDSBCAPS](#pydsbcaps)object.&nbsp;

  - [DSCCAPS](directsound.md#directsounddsccaps)

    Creates a new[PyDSCCAPS](#pydsccaps)object.&nbsp;

  - [DSCBCAPS](directsound.md#directsounddscbcaps)

    Creates a new[PyDSCBCAPS](#pydscbcaps)object.&nbsp;

  - [DSBUFFERDESC](directsound.md#directsounddsbufferdesc)

    Creates a new[PyDSBUFFERDESC](#pydsbufferdesc)object.&nbsp;

  - [DSCBUFFERDESC](directsound.md#directsounddscbufferdesc)

    Creates a new[PyDSCBUFFERDESC](#pydscbufferdesc)object.&nbsp;

## DS3DMODE_DISABLE
 __const directsound.DS3DMODE_DISABLE;__ 
Processing of 3D sound is disabled. The sound seems to originate from the center of the listener's head.

## DS3DMODE_HEADRELATIVE
 __const directsound.DS3DMODE_HEADRELATIVE;__ 
Sound parameters (position, velocity, and orientation) are relative to the listener's parameters. In this mode, the absolute parameters of the sound are updated automatically as the listener's parameters change, so that the relative parameters remain constant.

## DS3DMODE_NORMAL
 __const directsound.DS3DMODE_NORMAL;__ 
Normal processing. This is the default mode.

## [directsound](#directsound).DSBCAPS

[PyDSBCAPS](#pydsbcaps)= __DSBCAPS(__ )
Creates a new PyDSBCAPS object

## DSBCAPS_CTRL3D
 __const directsound.DSBCAPS_CTRL3D;__ 
The buffer is either a primary buffer or a secondary buffer that uses 3-D control. To create a primary buffer, the dwFlags member of the DSBUFFERDESC structure should include the DSBCAPS_PRIMARYBUFFER flag.

## DSBCAPS_CTRLFREQUENCY
 __const directsound.DSBCAPS_CTRLFREQUENCY;__ 
The buffer must have frequency control capability.

## DSBCAPS_CTRLPAN
 __const directsound.DSBCAPS_CTRLPAN;__ 
The buffer must have pan control capability.

## DSBCAPS_CTRLPOSITIONNOTIFY
 __const directsound.DSBCAPS_CTRLPOSITIONNOTIFY;__ 
The buffer must have control position notify capability.

## DSBCAPS_CTRLVOLUME
 __const directsound.DSBCAPS_CTRLVOLUME;__ 
The buffer must have volume control capability.

## DSBCAPS_GETCURRENTPOSITION2
 __const directsound.DSBCAPS_GETCURRENTPOSITION2;__ 
Indicates that IDirectSoundBuffer::GetCurrentPosition should use the new behavior of the play cursor. In DirectSound in DirectX 1, the play cursor was significantly ahead of the actual playing sound on emulated sound cards; it was directly behind the write cursor. Now, if the DSBCAPS_GETCURRENTPOSITION2 flag is specified, the application can get a more accurate play position. If this flag is not specified, the old behavior is preserved for compatibility. Note that this flag affects only emulated sound cards; if a DirectSound driver is present, the play cursor is accurate for DirectSound in all versions of DirectX.

## DSBCAPS_GLOBALFOCUS
 __const directsound.DSBCAPS_GLOBALFOCUS;__ 
The buffer is a global sound buffer. With this flag set, an application using DirectSound can continue to play its buffers if the user switches focus to another application, even if the new application uses DirectSound. The one exception is if you switch focus to a DirectSound application that uses the DSSCL_EXCLUSIVE or DSSCL_WRITEPRIMARY flag for its cooperative level. In this case, the global sounds from other applications will not be audible.

## DSBCAPS_LOCHARDWARE
 __const directsound.DSBCAPS_LOCHARDWARE;__ 
The buffer is in hardware memory and uses hardware mixing.

## DSBCAPS_LOCSOFTWARE
 __const directsound.DSBCAPS_LOCSOFTWARE;__ 
The buffer is in software memory and uses software mixing.

## DSBCAPS_MUTE3DATMAXDISTANCE
 __const directsound.DSBCAPS_MUTE3DATMAXDISTANCE;__ 
The sound is reduced to silence at the maximum distance. The buffer will stop playing when the maximum distance is exceeded, so that processor time is not wasted.

## DSBCAPS_PRIMARYBUFFER
 __const directsound.DSBCAPS_PRIMARYBUFFER;__ 
Indicates that the buffer is a primary sound buffer. If this value is not specified, a secondary sound buffer will be created.

## DSBCAPS_STATIC
 __const directsound.DSBCAPS_STATIC;__ 
Indicates that the buffer will be used for static sound data. Typically, these buffers are loaded once and played many times. These buffers are candidates for hardware memory.

## DSBCAPS_STICKYFOCUS
 __const directsound.DSBCAPS_STICKYFOCUS;__ 
Changes the focus behavior of the sound buffer. This flag can be specified in an IDirectSound::CreateSoundBuffer call. With this flag set, an application using DirectSound can continue to play its sticky focus buffers if the user switches to another application not using DirectSound. In this situation, the application's normal buffers are muted, but the sticky focus buffers are still audible. This is useful for nongame applications, such as movie playback (DirectShow&#153), when the user wants to hear the soundtrack while typing in Microsoft Word or Microsoft&#174 Excel, for example. However, if the user switches to another DirectSound application, all sound buffers, both normal and sticky focus, in the previous application are muted.

## DSBLOCK_ENTIREBUFFER
 __const directsound.DSBLOCK_ENTIREBUFFER;__ 
Unknown.

## DSBLOCK_FROMWRITECURSOR
 __const directsound.DSBLOCK_FROMWRITECURSOR;__ 
Locks from the current write cursor, making a call to DirectSoundBuffer.getCurrentPosition unnecessary. If this flag is specified, the start parameter is ignored. This flag is optional.

## DSBPLAY_LOOPING
 __const directsound.DSBPLAY_LOOPING;__ 
Once the end of the audio buffer is reached, play restarts at the beginning of the buffer. Play continues until explicitly stopped. This flag must be set when playing primary sound buffers.

## DSBSTATUS_BUFFERLOST
 __const directsound.DSBSTATUS_BUFFERLOST;__ 
The buffer is lost and must be restored before it can be played or locked.

## DSBSTATUS_LOOPING
 __const directsound.DSBSTATUS_LOOPING;__ 
The buffer is being looped. If this value is not set, the buffer will stop when it reaches the end of the sound data. Note that if this value is set, the buffer must also be playing.

## DSBSTATUS_PLAYING
 __const directsound.DSBSTATUS_PLAYING;__ 
The buffer is playing. If this value is not set, the buffer is stopped.

## [directsound](#directsound).DSBUFFERDESC

[PyDSBUFFERDESC](#pydsbufferdesc)= __DSBUFFERDESC(__ )
Creates a new PyDSBUFFERDESC object

## [directsound](#directsound).DSCAPS

[PyDSCAPS](#pydscaps)= __DSCAPS(__ )
Creates a new PyDSCAPS object.

## DSCAPS_CERTIFIED
 __const directsound.DSCAPS_CERTIFIED;__ 
This driver has been tested and certified by Microsoft.

## DSCAPS_CONTINUOUSRATE
 __const directsound.DSCAPS_CONTINUOUSRATE;__ 
The device supports all sample rates between the dwMinSecondarySampleRate and dwMaxSecondarySampleRate member values. Typically, this means that the actual output rate will be within +/- 10 hertz (Hz) of the requested frequency.

## DSCAPS_EMULDRIVER
 __const directsound.DSCAPS_EMULDRIVER;__ 
The device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions. Performance degradation should be expected.

## DSCAPS_PRIMARY16BIT
 __const directsound.DSCAPS_PRIMARY16BIT;__ 
The device supports primary sound buffers with 16-bit samples.

## DSCAPS_PRIMARY8BIT
 __const directsound.DSCAPS_PRIMARY8BIT;__ 
The device supports hardware-mixed secondary buffers with 8-bit samples.

## DSCAPS_PRIMARYMONO
 __const directsound.DSCAPS_PRIMARYMONO;__ 
The device supports monophonic primary buffers.

## DSCAPS_PRIMARYSTEREO
 __const directsound.DSCAPS_PRIMARYSTEREO;__ 
The device supports stereo primary buffers.

## DSCAPS_SECONDARY16BIT
 __const directsound.DSCAPS_SECONDARY16BIT;__ 
The device supports hardware-mixed secondary sound buffers with 16-bit samples.

## DSCAPS_SECONDARY8BIT
 __const directsound.DSCAPS_SECONDARY8BIT;__ 
The device supports hardware-mixed secondary buffers with 8-bit samples.

## DSCAPS_SECONDARYMONO
 __const directsound.DSCAPS_SECONDARYMONO;__ 
The device supports hardware-mixed monophonic secondary buffers.

## DSCAPS_SECONDARYSTEREO
 __const directsound.DSCAPS_SECONDARYSTEREO;__ 
The device supports hardware-mixed stereo secondary buffers.

## [directsound](#directsound).DSCBCAPS

[PyDSCBCAPS](#pydscbcaps)= __DSCBCAPS(__ )
Creates a new PyDSCBCAPS object

## DSCBCAPS_WAVEMAPPED
 __const directsound.DSCBCAPS_WAVEMAPPED;__ 
The Win32 wave mapper will be used for formats not supported by the device.

## [directsound](#directsound).DSCBUFFERDESC

[PyDSCBUFFERDESC](#pydscbufferdesc)= __DSCBUFFERDESC(__ )
Creates a new PyDSCBUFFERDESC object

## [directsound](#directsound).DSCCAPS

[PyDSCCAPS](#pydsccaps)= __DSCCAPS(__ )
Creates a new PyDSCCAPS object

## DSCCAPS_EMULDRIVER
 __const directsound.DSCCAPS_EMULDRIVER;__ 
The device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions. Performance degradation should be expected.

## DSSCL_EXCLUSIVE
 __const directsound.DSSCL_EXCLUSIVE;__ 
Sets the application to the exclusive level. When it has the input focus, the application will be the only one audible (sounds from applications with the DSBCAPS_GLOBALFOCUS flag set will be muted). With this level, it also has all the privileges of the DSSCL_PRIORITY level. DirectSound will restore the hardware format, as specified by the most recent call to the DirectSoundBuffer.setFormat method, once the application gains the input focus. (Note that DirectSound will always restore the wave format, no matter what priority level is set.)

## DSSCL_NORMAL
 __const directsound.DSSCL_NORMAL;__ 
Sets the application to a fully cooperative status. Most applications should use this level, because it has the smoothest multitasking and resource-sharing behavior.

## DSSCL_PRIORITY
 __const directsound.DSSCL_PRIORITY;__ 
Sets the application to the priority level. Applications with this cooperative level can call the DirectSoundBuffer.setFormat and DirectSound.compact methods.

## DSSCL_WRITEPRIMARY
 __const directsound.DSSCL_WRITEPRIMARY;__ 
This is the highest priority level. The application has write access to the primary sound buffers. No secondary sound buffers in any application can be played.

## DSSPEAKER_GEOMETRY_MAX
 __const directsound.DSSPEAKER_GEOMETRY_MAX;__ 
The speakers are directed over an arc of 180 degrees.

## DSSPEAKER_GEOMETRY_MIN
 __const directsound.DSSPEAKER_GEOMETRY_MIN;__ 
The speakers are directed over an arc of 5 degrees.

## DSSPEAKER_GEOMETRY_NARROW
 __const directsound.DSSPEAKER_GEOMETRY_NARROW;__ 
The speakers are directed over an arc of 10 degrees.

## DSSPEAKER_GEOMETRY_WIDE
 __const directsound.DSSPEAKER_GEOMETRY_WIDE;__ 
The speakers are directed over an arc of 20 degrees.

## DSSPEAKER_HEADPHONE
 __const directsound.DSSPEAKER_HEADPHONE;__ 
The speakers are headphones.

## DSSPEAKER_MONO
 __const directsound.DSSPEAKER_MONO;__ 
The speakers are monaural.

## DSSPEAKER_QUAD
 __const directsound.DSSPEAKER_QUAD;__ 
The speakers are quadraphonic.

## DSSPEAKER_STEREO
 __const directsound.DSSPEAKER_STEREO;__ 
The speakers are stereo (default value).

## DSSPEAKER_SURROUND
 __const directsound.DSSPEAKER_SURROUND;__ 
The speakers are surround sound.

## [directsound](#directsound).DirectSoundCaptureCreate

[PyIUnknown](#pyiunknown)= __DirectSoundCaptureCreate( *guid*  *, unk* __ )
Creates and initializes a new object that supports the IDirectSoundCapture interface.

#### Parameters


  -  *guid=None* :[PyIID](#pyiid)

    Address of the GUID that identifies the sound device. The value of this parameter must be one of the GUIDs returned by DirectSoundCaptureEnumerate, or None for the default device.

  -  *unk=None* : __PyIUknown__ 

    The IUnknown for COM aggregation.

## [directsound](#directsound).DirectSoundCaptureEnumerate

 __list__ = __DirectSoundCaptureEnumerate(__ )
Enumerates DirectSoundCapture drivers installed in the system.

## [directsound](#directsound).DirectSoundCreate

[PyIUnknown](#pyiunknown)= __DirectSoundCreate( *guid*  *, unk* __ )
Creates and initializes a new object that supports the IDirectSound interface.

#### Parameters


  -  *guid=None* :[PyIID](#pyiid)

    Address of the GUID that identifies the sound device. The value of this parameter must be one of the GUIDs returned by DirectSoundEnumerate, or None for the default device.

  -  *unk=None* : __PyIUknown__ 

    The IUnknown for COM aggregation.

## [directsound](#directsound).DirectSoundEnumerate

 __list__ = __DirectSoundEnumerate(__ )
Enumerates DirectSound drivers installed in the system.