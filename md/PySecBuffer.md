# PySecBuffer


## PySecBuffer Object

Python object wrapping a SecBuffer structure 

Created using win32security\.PySecBufferType\(type,size\) where type is a SECBUFFER\_\* constant

#### Methods

  - [Clear](PySecBuffer.md#pysecbufferclear)

    Resets all members of the structure&nbsp;

#### Properties

  - int BufferType

    

  - string Buffer

    

  - int BufferSize

    

  - int MaxBufferSize

    


## [PySecBuffer](PySecBuffer.md#pysecbuffer)\.Clear

Clear\(\)
Resets the buffer to all NULL's, and set the current size to maximum