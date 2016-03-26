# PyDSCAPS

## PyDSCAPS Object

A Python object, representing a DSCAPS structure

#### Properties

  -  **integer dwFlags** 
    Specifies device capabilities\. Can be one or more of the following:

 **Flag**  **Description** DSCAPS\_PRIMARYMONOThe device supports monophonic primary buffers\.DSCAPS\_PRIMARYSTEREOThe device supports stereo primary buffers\.DSCAPS\_PRIMARY8BITThe device supports hardware-mixed secondary buffers with 8-bit samples\.DSCAPS\_PRIMARY16BITThe device supports primary sound buffers with 16-bit samples\.DSCAPS\_CONTINUOUSRATEThe device supports all sample rates between the dwMinSecondarySampleRate and dwMaxSecondarySampleRate member values\. Typically, this means that the actual output rate will be within \+/- 10 hertz \(Hz\) of the requested frequency\.DSCAPS\_EMULDRIVERThe device does not have a DirectSound driver installed, so it is being emulated through the waveform-audio functions\. Performance degradation should be expected\.DSCAPS\_CERTIFIEDThis driver has been tested and certified by Microsoft\.DSCAPS\_SECONDARYMONOThe device supports hardware-mixed monophonic secondary buffers\.DSCAPS\_SECONDARYSTEREOThe device supports hardware-mixed stereo secondary buffers\.DSCAPS\_SECONDARY8BITThe device supports hardware-mixed secondary buffers with 8-bit samples\.DSCAPS\_SECONDARY16BITThe device supports hardware-mixed secondary sound buffers with 16-bit samples\.
  -  **integer dwMinSecondarySampleRate** 
    Minimum sample rate supported by this device's hardware secondary sound buffers\.

  -  **integer dwMaxSecondarySampleRate** 
    Maximum sample rate supported by this device's hardware secondary sound buffers\.

  -  **integer dwPrimaryBuffers** 
    Number of primary buffers supported\. This value will always be 1\.

  -  **integer dwMaxHwMixingAllBuffers** 
    Specifies the total number of buffers that can be mixed in hardware\. This member can be less than the sum of dwMaxHwMixingStaticBuffers and dwMaxHwMixingStreamingBuffers\. Resource tradeoffs frequently occur\.

  -  **integer dwMaxHwMixingStaticBuffers** 
    Specifies the maximum number of static sound buffers\.

  -  **integer dwMaxHwMixingStreamingBuffers** 
    Specifies the maximum number of streaming sound buffers\.

  -  **integer dwFreeHwMixingAllBuffers** 
    Description of the free hardware mixing capabilities of the device\. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer\. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined\.

  -  **integer dwFreeHwMixingStaticBuffers** 
    Description of the free hardware mixing capabilities of the device\. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer\. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined\.

  -  **integer dwFreeHwMixingStreamingBuffers** 
    Description of the free hardware mixing capabilities of the device\. An application can use this value to determine whether hardware resources are available for allocation to a secondary sound buffer\. Also, by comparing these values to the members that specify maximum mixing capabilities, the resources that are already allocated can be determined\.

  -  **integer dwMaxHw3DAllBuffers** 
    Description of the hardware 3-D positional capabilities of the device\.

  -  **integer dwMaxHw3DStaticBuffers** 
    Description of the hardware 3-D positional capabilities of the device\.

  -  **integer dwMaxHw3DStreamingBuffers** 
    Description of the hardware 3-D positional capabilities of the device\.

  -  **integer dwFreeHw3DAllBuffers** 
    Description of the free, or unallocated, hardware 3-D positional capabilities of the device\.

  -  **integer dwFreeHw3DStaticBuffers** 
    Description of the free, or unallocated, hardware 3-D positional capabilities of the device\.

  -  **integer dwFreeHw3DStreamingBuffers** 
    Description of the free, or unallocated, hardware 3-D positional capabilities of the device\.

  -  **integer dwTotalHwMemBytes** 
    Size, in bytes, of the amount of memory on the sound card that stores static sound buffers\.

  -  **integer dwFreeHwMemBytes** 
    Size, in bytes, of the free memory on the sound card\.

  -  **integer dwMaxContigFreeHwMemBytes** 
    Size, in bytes, of the largest contiguous block of free memory on the sound card\.

  -  **integer dwUnlockTransferRateHwBuffers** 
    Description of the rate, in kilobytes per second, at which data can be transferred to hardware static sound buffers\. This and the number of bytes transferred determines the duration of a call to the IDirectSoundBuffer::Update method\.

  -  **integer dwPlayCpuOverheadSwBuffers** 
    Description of the processing overhead, as a percentage of the central processing unit, needed to mix software buffers \(those located in main system memory\)\. This varies according to the bus type, the processor type, and the clock speed\. The unlock transfer rate for software buffers is 0 because the data need not be transferred anywhere\. Similarly, the play processing overhead for hardware buffers is 0 because the mixing is done by the sound device\.