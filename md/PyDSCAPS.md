# PyDSCAPS

## PyDSCAPS Object

A Python object, representing a DSCAPS structure

#### Properties

  -  __integer dwFlags__ 
    Specifies device capabilities. Can be one or more of the following:

 __Flag__  __Description__ DSCAPS_PRIMARYMONOThe device supports monophonic primary buffers.DSCAPS_PRIMARYSTEREOThe device supports stereo primary buffers.DSCAPS_PRIMARY8BITThe device supports hardware-mixed secondary buffers with 8-bit samples.DSCAPS_PRIMARY16BITThe device supports primary sound buffers with 16-bit samples.DSCAPS_CONTINUOUSRATEThe device supports all sample rates between the dwMinSecondarySampleRate and dwMaxSecondarySampleRate member values. Typically, this means that the actual output rate will be within +/- 10 hertz (Hz) of the requested frequency.DSCAPS_EMULDRIVERThe device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions. Performance degradation should be expected.DSCAPS_CERTIFIEDThis driver has been tested and certified by Microsoft.DSCAPS_SECONDARYMONOThe device supports hardware-mixed monophonic secondary buffers.DSCAPS_SECONDARYSTEREOThe device supports hardware-mixed stereo secondary buffers.DSCAPS_SECONDARY8BITThe device supports hardware-mixed secondary buffers with 8-bit samples.DSCAPS_SECONDARY16BITThe device supports hardware-mixed secondary sound buffers with 16-bit samples.
  -  __integer dwMinSecondarySampleRate__ 
    Minimum sample rate supported by this device's hardware secondary sound buffers.

  -  __integer dwMaxSecondarySampleRate__ 
    Maximum sample rate supported by this device's hardware secondary sound buffers.

  -  __integer dwPrimaryBuffers__ 
    Number of primary buffers supported. This value will always be 1.

  -  __integer dwMaxHwMixingAllBuffers__ 
    Specifies the total number of buffers that can be mixed in hardware. This member can be less than the sum of dwMaxHwMixingStaticBuffers and dwMaxHwMixingStreamingBuffers. Resource tradeoffs frequently occur.

  -  __integer dwMaxHwMixingStaticBuffers__ 
    Specifies the maximum number of static sound buffers.

  -  __integer dwMaxHwMixingStreamingBuffers__ 
    Specifies the maximum number of streaming sound buffers.

  -  __integer dwFreeHwMixingAllBuffers__ 
    Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined.

  -  __integer dwFreeHwMixingStaticBuffers__ 
    Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined.

  -  __integer dwFreeHwMixingStreamingBuffers__ 
    Description of the free hardware mixing capabilities of the device. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined.

  -  __integer dwMaxHw3DAllBuffers__ 
    Description of the hardware 3-D positional capabilities of the device.

  -  __integer dwMaxHw3DStaticBuffers__ 
    Description of the hardware 3-D positional capabilities of the device.

  -  __integer dwMaxHw3DStreamingBuffers__ 
    Description of the hardware 3-D positional capabilities of the device.

  -  __integer dwFreeHw3DAllBuffers__ 
    Description of the free, or unallocated, hardware 3-D positional capabilities of the device.

  -  __integer dwFreeHw3DStaticBuffers__ 
    Description of the free, or unallocated, hardware 3-D positional capabilities of the device.

  -  __integer dwFreeHw3DStreamingBuffers__ 
    Description of the free, or unallocated, hardware 3-D positional capabilities of the device.

  -  __integer dwTotalHwMemBytes__ 
    Size, in bytes, of the amount of memory on the sound card that stores static sound buffers.

  -  __integer dwFreeHwMemBytes__ 
    Size, in bytes, of the free memory on the sound card.

  -  __integer dwMaxContigFreeHwMemBytes__ 
    Size, in bytes, of the largest contiguous block of free memory on the sound card.

  -  __integer dwUnlockTransferRateHwBuffers__ 
    Description of the rate, in kilobytes per second, at which data can be transferred to hardware static sound buffers. This and the number of bytes transferred determines the duration of a call to the IDirectSoundBuffer::Update method.

  -  __integer dwPlayCpuOverheadSwBuffers__ 
    Description of the processing overhead, as a percentage of the central processing unit, needed to mix software buffers (those located in main system memory). This varies according to the bus type, the processor type, and the clock speed. The unlock transfer rate for software buffers is 0 because the data need not be transferred anywhere. Similarly, the play processing overhead for hardware buffers is 0 because the mixing is done by the sound device.