# PyWAVEFORMATEX

## PyWAVEFORMATEX Object



A Python object, representing a WAVEFORMATEX structure

#### Properties

  - integer wFormatTag
    Waveform-audio format type\. pywintypes only defines WAVE\_FORMAT\_PCM as a constant\. Other values must be looked up in the mmsystem\.h header file\.

  - integer nChannels
    Number of channels\. 1 for Mono, 2 for Stereo, anything, but never 5\.1\.

  - integer nSamplesPerSec
    Sample rate, in samples per second \(hertz\), that each channel should be played or recorded\. If wFormatTag is WAVE\_FORMAT\_PCM, then common values for nSamplesPerSec are 8000, 11025, 22050, and 44100 Hz

  - integer nAvgBytesPerSec
    Required average data-transfer rate, in bytes per second, for the format tag\. If wFormatTag is WAVE\_FORMAT\_PCM, nAvgBytesPerSec should be equal to the product of nSamplesPerSec and nBlockAlign\.

  - integer nBlockAlign
    Block alignment, in bytes\. The block alignment is the minimum atomic unit of data for the wFormatTag format type\. If wFormatTag is WAVE\_FORMAT\_PCM, nBlockAlign should be equal to the product of nChannels and wBitsPerSample divided by 8 \(bits per byte\)\. For non-PCM formats, this member must be computed according to the manufacturer&\#146s specification of the format tag\.

  - integer wBitsPerSample
    Bits per sample for the wFormatTag format type\. If wFormatTag is WAVE\_FORMAT\_PCM, then wBitsPerSample should be equal to 8 or 16\. 

Sentinel