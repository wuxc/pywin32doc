# PySecBuffer

## PySecBuffer Object

Python object wrapping a SecBuffer structure 

Created using win32security.PySecBufferType(type,size) where type is a SECBUFFER_* constant

#### Methods


  - [Clear](PySecBuffer.md#pysecbufferclear)

    Resets all members of the structure&nbsp;

#### Properties

  -  __int BufferType__ 
    

  -  __string Buffer__ 
    

  -  __int BufferSize__ 
    

  -  __int MaxBufferSize__ 
    

## [PySecBuffer](#pysecbuffer).Clear

 __Clear(__ )
Resets the buffer to all NULL's, and set the current size to maximum