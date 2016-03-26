# PyWAVEFORMATEX

## PyWAVEFORMATEX Object

A Python object, representing a WAVEFORMATEX structure

#### Properties

  -  __integer wFormatTag__ 
    Waveform-audio format type. pywintypes only defines WAVE_FORMAT_PCM as a constant. Other values must be looked up in the mmsystem.h header file.

  -  __integer nChannels__ 
    Number of channels. 1 for Mono, 2 for Stereo, anything, but never 5.1.

  -  __integer nSamplesPerSec__ 
    Sample rate, in samples per second (hertz), that each channel should be played or recorded. If wFormatTag is WAVE_FORMAT_PCM, then common values for nSamplesPerSec are 8000, 11025, 22050, and 44100 Hz

  -  __integer nAvgBytesPerSec__ 
    Required average data-transfer rate, in bytes per second, for the format tag. If wFormatTag is WAVE_FORMAT_PCM, nAvgBytesPerSec should be equal to the product of nSamplesPerSec and nBlockAlign.

  -  __integer nBlockAlign__ 
    Block alignment, in bytes. The block alignment is the minimum atomic unit of data for the wFormatTag format type. If wFormatTag is WAVE_FORMAT_PCM, nBlockAlign should be equal to the product of nChannels and wBitsPerSample divided by 8 (bits per byte). For non-PCM formats, this member must be computed according to the manufacturer&#146s specification of the format tag.

  -  __integer wBitsPerSample__ 
    Bits per sample for the wFormatTag format type. If wFormatTag is WAVE_FORMAT_PCM, then wBitsPerSample should be equal to 8 or 16. 

Sentinel