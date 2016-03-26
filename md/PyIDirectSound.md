# PyIDirectSound

## PyIDirectSound Object

Description of the interface

#### Methods


  - [Initialize](PyIDirectSound.md#pyidirectsoundinitialize)

    Description of Initialize.&nbsp;

  - [SetCooperativeLevel](PyIDirectSound.md#pyidirectsoundsetcooperativelevel)

    Description of SetCooperativeLevel.&nbsp;

  - [CreateSoundBuffer](PyIDirectSound.md#pyidirectsoundcreatesoundbuffer)

    Description of CreateSoundBuffer.&nbsp;

  - [GetCaps](PyIDirectSound.md#pyidirectsoundgetcaps)

    Description of GetCaps.&nbsp;

  - [Compact](PyIDirectSound.md#pyidirectsoundcompact)

    Description of Compact.&nbsp;

## [PyIDirectSound](#pyidirectsound).Compact

 __Compact(__ )
The Compact method moves the unused portions of on-board sound memory, if any, to a contiguous block so that the largest portion of free memory will be available.

## [PyIDirectSound](#pyidirectsound).CreateSoundBuffer

 __CreateSoundBuffer( *lpDSCBufferDesc*  *, unk* __ )
The IDirectSound::CreateSoundBuffer method creates a DirectSoundBuffer object to hold a sequence of audio samples.

#### Parameters


  -  *lpDSCBufferDesc* :[PyDSCBUFFERDESC](#pydscbufferdesc)

    a DSBUFFERDESC structure containing values for the sound buffer being created.

  -  *unk=None* : __PyIUknown__ 

    The IUnknown for COM aggregation.

## [PyIDirectSound](#pyidirectsound).GetCaps

 __GetCaps(__ )
The GetCaps method retrieves the capabilities of the hardware device that is represented by the DirectSound object. See[DSCAPS contants](DSCAPS.md#dscapscontants).

## [PyIDirectSound](#pyidirectsound).GetSpeakerConfig

 __GetSpeakerConfig(__ )
The GetSpeakerConfig method retrieves the speaker configuration.

## [PyIDirectSound](#pyidirectsound).Initialize

 __Initialize( *guid* __ )
Description of Initialize.

#### Parameters


  -  *guid* :[PyIID](#pyiid)

    Globally unique identifier (GUID) specifying the sound driver to which this DirectSound object binds. Pass None to select the primary sound driver.

## [PyIDirectSound](#pyidirectsound).SetCooperativeLevel

 __SetCooperativeLevel( *hwnd*  *, level* __ )
The IDirectSound::SetCooperativeLevel method sets the cooperative level of the application for this sound device.

#### Parameters


  -  *hwnd* : int

    Window handle to the application or None.

  -  *level* : int

    Requested priority level. Specify one of the following values:


## [PyIDirectSound](#pyidirectsound).SetSpeakerConfig

 __SetSpeakerConfig( *dwSpeakerConfig* __ )
The SetSpeakerConfig method specifies the speaker configuration of the DirectSound object.

#### Parameters


  -  *dwSpeakerConfig* : int

    Speaker configuration of the specified DirectSound object. See the DSSPEAKER constants.